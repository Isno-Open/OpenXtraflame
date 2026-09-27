# Top-level CMakeLists for openextraflame firmware
cmake_minimum_required(VERSION 3.16)

# La carte visee : -DBOARD=isno-super (ESP32-S3), external ou blacklabel (ESP32).
# Le brochage en est engendre dans board_pins.h (voir main/CMakeLists.txt).
set(BOARD "isno-super" CACHE STRING "carte visee : boards/<BOARD>.json")

# Le PROFIL de fonctionnalites suit la carte. Seule la carte d'origine Extraflame
# (blacklabel) porte le pont cloud, la matricola et la partition secret1 ; toute
# autre carte (ESP32 d'appoint, Super) est du profil « external ». C'est une
# regle locale au firmware, pas une propriete de la carte : elle ne vit donc pas
# dans boards/<carte>.json (isno-super.json est une copie verbatim du launcher).
if(BOARD STREQUAL "blacklabel")
    add_compile_definitions(TARGET_BLACKLABEL=1)
else()
    add_compile_definitions(TARGET_EXTERNAL=1)
endif()
message(STATUS "openextraflame : carte ${BOARD}")

# Firmware version stamped into esp_app_get_description()->version, shown in
# the Web UI header and the OTA tab. Bump on each release.
set(PROJECT_VER "v0.1.0-rc5")

include($ENV{IDF_PATH}/tools/cmake/project.cmake)
project(openextraflame)
