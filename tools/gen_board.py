#!/usr/bin/env python3
"""Engendre board_pins.h depuis une declaration de carte.

    python3 tools/gen_board.py boards/isno-super.json build/board/board_pins.h

Meme format de declaration que isno-launcher : le brochage vit par carte dans
boards/<carte>.json, le firmware LE LIT, il n'en connait aucun. Appele par CMake
a la configuration ; rien d'engendre n'est commis.

openextraflame ne pilote pas de radio : il parle au poele en UART (bus Micronova)
et allume des LEDs. Les noms de macros sont ceux QUE LE CODE lit deja
(STOVE_UART_*, STATUS_LED_*, LED_*_PIN, CONFIG_BUTTON_*), pas ceux d'un firmware
radio : chaque firmware garde son vocabulaire, seul le format est partage.

Les jetons GPIO_NUM_x / UART_* viennent de driver/gpio.h et driver/uart.h, que
hardware_config.h inclut avant cet en-tete.
"""
import json
import sys

_DATA = {5: "UART_DATA_5_BITS", 6: "UART_DATA_6_BITS", 7: "UART_DATA_7_BITS", 8: "UART_DATA_8_BITS"}
_PARITY = {"none": "UART_PARITY_DISABLE", "even": "UART_PARITY_EVEN", "odd": "UART_PARITY_ODD"}
_STOP = {1: "UART_STOP_BITS_1", 15: "UART_STOP_BITS_1_5", 2: "UART_STOP_BITS_2"}


def _gpio(pin):
    """GPIO_NUM_x pour une vraie broche, (-1) pour absente."""
    return "GPIO_NUM_%d" % pin if isinstance(pin, int) and pin >= 0 else "(-1)"


def header(d):
    u = d.get("uart", {})
    ui = d.get("ui", {})
    leds = d.get("leds", {})
    if "tx" not in u or "rx" not in u:
        raise SystemExit("la carte %s ne declare pas d'UART (tx/rx) pour le poele" % d["id"])
    stop = _STOP.get(int(u.get("stop_bits", 2)))
    data = _DATA.get(int(u.get("data_bits", 8)))
    parity = _PARITY.get(str(u.get("parity", "none")).lower())
    if not (stop and data and parity):
        raise SystemExit("UART invalide dans %s (data/parity/stop)" % d["id"])
    led = ui.get("led", -1)
    L = [
        "/* ENGENDRE par tools/gen_board.py depuis boards/%s.json. Ne pas modifier. */" % d["id"],
        "#ifndef OPENXFLAME_BOARD_PINS_H",
        "#define OPENXFLAME_BOARD_PINS_H",
        "",
        '#define BOARD_NAME                  "%s"' % d.get("name", d["id"]),
        '#define AP_SSID_PREFIX              "OpenXtraflame_"',
        "",
        "/* UART vers le poele (bus Micronova). */",
        "#define STOVE_UART_NUM              UART_NUM_%d" % int(u.get("num", 1)),
        "#define STOVE_UART_TX_PIN           %s" % _gpio(u["tx"]),
        "#define STOVE_UART_RX_PIN           %s" % _gpio(u["rx"]),
        "#define STOVE_UART_BAUD             %d" % int(u.get("baud", 1200)),
        "#define STOVE_UART_DATA_BITS        %s" % data,
        "#define STOVE_UART_PARITY           %s" % parity,
        "#define STOVE_UART_STOP_BITS        %s" % stop,
        "",
        "/* LED d'etat unique (carte d'appoint / Super). */",
        "#define STATUS_LED_ENABLED          %d" % (1 if isinstance(led, int) and led >= 0 else 0),
        "#define STATUS_LED_PIN              %s" % _gpio(led),
        "#define STATUS_LED_INVERTED         %d" % (0 if ui.get("led_active_high", True) else 1),
        "",
        "/* Bouton de configuration. */",
        "#define CONFIG_BUTTON_ENABLED       %d" % (1 if isinstance(ui.get("button", -1), int) and ui.get("button", -1) >= 0 else 0),
        "#define CONFIG_BUTTON_PIN           %s" % _gpio(ui.get("button", -1)),
        "#define CONFIG_BUTTON_ACTIVE_LOW    %d" % (1 if ui.get("button_active_low", True) else 0),
        "",
        "/* LEDs par etat (carte Black Label d'origine), -1 quand absentes. */",
        "#define LED_POWER_PIN               %s" % _gpio(leds.get("power", -1)),
        "#define LED_BLE_PIN                 %s" % _gpio(leds.get("ble", -1)),
        "#define LED_WIFI_PIN                %s" % _gpio(leds.get("wifi", -1)),
        "#define LED_SERVER_PIN              %s" % _gpio(leds.get("server", -1)),
        "#define LED_ACTIVE_HIGH             %d" % (1 if leds.get("active_high", True) else 0),
        "",
        "#endif",
    ]
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    d = json.load(open(sys.argv[1], encoding="utf-8"))
    text = header(d)
    try:
        if open(sys.argv[2], encoding="utf-8").read() == text:
            sys.exit(0)  # inchange : ne pas toucher au fichier, sinon tout recompile
    except FileNotFoundError:
        pass
    open(sys.argv[2], "w", encoding="utf-8").write(text)
