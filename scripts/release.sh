#!/bin/bash
# Compile les deux cibles d'OpenXtraflame et produit les fichiers d'une release, dans le
# conteneur ESP-IDF officiel. Reproductible : rien ne depend du poste.
#
#   bash scripts/release.sh
#   -> dist/openextraflame-<cible>.bin                 image seule, pour l'onglet OTA (Pull)
#   -> dist/openxtraflame-<cible>-<version>.tar.gz     bootloader + partitions + ota_data + image + flash.sh
#
# Cibles : blacklabel (module Extraflame d'origine, reflash) et external (ESP32 spare, M5Stack).
# La version vient de PROJECT_VER dans firmware/CMakeLists.txt, seule declaration.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
IMAGE="${IDF_IMAGE:-espressif/idf:v5.2.7}"
cd "$ROOT/firmware"
VER=$(sed -n 's/^set(PROJECT_VER "\(.*\)")/\1/p' CMakeLists.txt)
[ -n "$VER" ] || { echo "PROJECT_VER introuvable"; exit 1; }
mkdir -p "$ROOT/dist"
run() { docker run --rm -u "$(id -u):$(id -g)" -e HOME=/tmp -v "$ROOT/firmware":/w -w /w "$IMAGE" bash -c "$*"; }
for target in blacklabel external; do
  B="build-$target"
  echo "== $target ($VER, $IMAGE)"
  run "idf.py -B $B -DSDKCONFIG=$B/sdkconfig -DIDF_TARGET=esp32 -DOPENXFLAME_TARGET=$target build" | tail -n 3
  [ "$(python3 -c "import json,sys; print(json.load(open(sys.argv[1]))['project_version'])" "$B/project_description.json")" = "$VER" ] || { echo "version compilee != $VER"; exit 1; }
  cp "$B/openextraflame.bin" "$ROOT/dist/openextraflame-$target.bin"
  P="$ROOT/dist/pkg-$target"; rm -rf "$P"; mkdir -p "$P"
  cp "$B/bootloader/bootloader.bin" "$B/partition_table/partition-table.bin" "$B/ota_data_initial.bin" "$B/openextraflame.bin" "$P/"
  # Offsets : ceux de partitions.csv et du bootloader ESP32 (0x1000), repris de flash_args.
  {
    echo '#!/bin/bash'
    echo "# OpenXtraflame $VER, cible $target : flash complet d'une carte (esptool, pip install esptool)."
    echo '# Usage : bash flash.sh /dev/ttyUSB0'
    echo 'PORT="${1:-/dev/ttyUSB0}"'
    echo "esptool.py --chip esp32 -p \"\$PORT\" --baud 460800 write_flash $(sed -n '1p' "$B/flash_args") \\"
    sed -n '2,$p' "$B/flash_args" | awk '{printf "  %s %s", $1, $2; sub(/^.*\//, "", $2)} END {print ""}' | sed 's#bootloader/bootloader.bin#bootloader.bin#; s#partition_table/partition-table.bin#partition-table.bin#'
  } > "$P/flash.sh"
  chmod +x "$P/flash.sh"
  tar -C "$P" -czf "$ROOT/dist/openxtraflame-$target-$VER.tar.gz" .
  rm -rf "$P"
done
ls -la "$ROOT/dist"
