# board_pins.h est ENGENDRE a la configuration depuis boards/${BOARD}.json, dans
# le dossier de construction : rien d'engendre n'est commis. boards/ et tools/
# vivent a la racine du depot. ESP-IDF lit ce fichier une premiere fois en
# « expansion precoce » dans un autre processus CMake : on n'engendre qu'a la
# vraie configuration.
set(BOARD_JSON "${CMAKE_CURRENT_LIST_DIR}/../../boards/${BOARD}.json")
set(BOARD_HDR_DIR "${CMAKE_BINARY_DIR}/board")
if(NOT CMAKE_BUILD_EARLY_EXPANSION)
    if(NOT EXISTS "${BOARD_JSON}")
        message(FATAL_ERROR "carte inconnue : ${BOARD_JSON} n'existe pas (-DBOARD=isno-super | external | blacklabel)")
    endif()
    file(MAKE_DIRECTORY "${BOARD_HDR_DIR}")
    execute_process(COMMAND python3 "${CMAKE_CURRENT_LIST_DIR}/../../tools/gen_board.py" "${BOARD_JSON}" "${BOARD_HDR_DIR}/board_pins.h"
                    RESULT_VARIABLE r)
    if(NOT r EQUAL 0)
        message(FATAL_ERROR "gen_board.py a refuse ${BOARD_JSON}")
    endif()
    set_property(DIRECTORY APPEND PROPERTY CMAKE_CONFIGURE_DEPENDS "${BOARD_JSON}" "${CMAKE_CURRENT_LIST_DIR}/../../tools/gen_board.py")
endif()

idf_component_register(
    SRCS
        "main.c"
        "config_nvs.c"
        "wifi_bridge.c"
        "mqtt_bridge.c"
        "cloud_bridge.c"
        "cloud_rest.c"
        "micronova.c"
        "web_ui.c"
        "leds.c"
        "ota.c"
        "log_ring.c"
        "alarm_history.c"
        "pellet_forecast.c"
        "params_diff.c"
    INCLUDE_DIRS
        "."
        "${BOARD_HDR_DIR}"
    EMBED_TXTFILES
        "web/index.html"
        "web/style.css"
        "web/script.js"
        "certs/extraflame_ca.pem"
    REQUIRES
        nvs_flash
        esp_wifi
        esp_netif
        esp_event
        mqtt
        esp_http_server
        esp_http_client
        esp_https_ota
        app_update
        mbedtls
        esp-tls
        espressif__mdns
        driver
        esp_driver_uart
        esp_driver_gpio
        espressif__cjson
)
