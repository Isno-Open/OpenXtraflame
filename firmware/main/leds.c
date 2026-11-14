/**
 * openextraflame - LED status indicators
 *
 * TARGET_EXTERNAL: single LED, blinks per state pattern
 * TARGET_BLACKLABEL: 4 LEDs (POWER, BLE, WIFI, SERVER) - repurposed
 */

#include "leds.h"
#include "hardware_config.h"
#include "driver/gpio.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/event_groups.h"

/* La LED d'etat unique reflete la COMMUNICATION POELE : fixe = comm valide,
 * clignote = pas de comm valide (mauvais branchement / mauvais sens du connecteur,
 * poele muet). Elle lit directement STOVE_ONLINE pour etre independante du Wi-Fi/MQTT :
 * au banc on branche l'adaptateur et on retourne le connecteur jusqu'a la LED fixe. */
extern EventGroupHandle_t app_event_group;
extern const int STOVE_ONLINE_BIT;

static led_state_t current_state = LED_STATE_UNKNOWN;

static void gpio_output(int pin)
{
    if (pin < 0) return;
    gpio_config_t io = {
        .pin_bit_mask = (1ULL << pin),
        .mode = GPIO_MODE_OUTPUT,
    };
    gpio_config(&io);
}

#if STATUS_LED_ENABLED
static void status_led_task(void *arg)
{
    bool phase = false;
    for (;;) {
        EventBits_t bits = app_event_group ? xEventGroupGetBits(app_event_group) : 0;
        bool stove_ok = (bits & STOVE_ONLINE_BIT) != 0;
        int on;
        if (stove_ok) {
            on = 1;                 /* comm poele valide : LED fixe */
        } else {
            phase = !phase;         /* pas de comm valide : clignotement ~2 Hz */
            on = phase ? 1 : 0;
        }
    #if STATUS_LED_INVERTED
        gpio_set_level(STATUS_LED_PIN, on ? 0 : 1);
    #else
        gpio_set_level(STATUS_LED_PIN, on ? 1 : 0);
    #endif
        vTaskDelay(pdMS_TO_TICKS(250));
    }
}
#endif

void leds_init(void)
{
#if STATUS_LED_ENABLED
    gpio_output(STATUS_LED_PIN);
    xTaskCreate(status_led_task, "status_led", 2048, NULL, 2, NULL);
#endif
#ifdef TARGET_BLACKLABEL
    gpio_output(LED_POWER_PIN);
    gpio_output(LED_BLE_PIN);
    gpio_output(LED_WIFI_PIN);
    gpio_output(LED_SERVER_PIN);
#endif
    leds_set_state(LED_STATE_BOOT);
}

static void set_pin(int pin, int on)
{
    if (pin < 0) return;
#ifdef LED_ACTIVE_HIGH
    gpio_set_level(pin, on ? 1 : 0);
#else
    gpio_set_level(pin, on ? 0 : 1);
#endif
}

void leds_set_state(led_state_t state)
{
    current_state = state;

    /* La LED d'etat unique (STATUS_LED) est pilotee par status_led_task selon la
     * comm poele (fixe = OK, clignote = pas bon), pas ici. */

#ifdef TARGET_BLACKLABEL
    /* Reuse Extraflame's 4 LEDs as our own status */
    set_pin(LED_POWER_PIN,  1);                     /* always on when powered */
    set_pin(LED_BLE_PIN,    state == LED_STATE_AP_MODE);
    set_pin(LED_WIFI_PIN,   state != LED_STATE_WIFI_OFFLINE
                          && state != LED_STATE_AP_MODE
                          && state != LED_STATE_BOOT);
    set_pin(LED_SERVER_PIN, state == LED_STATE_ALL_OK
                          || state == LED_STATE_STOVE_OFFLINE);
#endif
}
