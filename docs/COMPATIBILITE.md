# Matériel compatible // Compatible hardware

Liste des poêles testés avec OpenXtraflame, tenue à partir des retours (forum, issues).
Une ligne = un retour vérifié. // List of stoves tested with OpenXtraflame, kept from reports
(forum, issues). One row = one verified report.

Les poêles à pellets La Nordica-Extraflame utilisent une carte **Micronova** et un bus
**série à UNE ligne DATA** (1200 bauds, 8N2). Le module Wi-Fi d'origine se décline en
générations (**Black Label** = app Total Control 2.0, **White Label** = Total Control,
**Grey Label** = Total Control 3.0) ; OpenXtraflame se branche directement sur le port
**SERIAL** du poêle, sans ce module. // The stoves use a **Micronova** board and a
**single DATA line** serial bus (1200 baud, 8N2). The original Wi-Fi module comes in
generations (Black / White / Grey Label); OpenXtraflame connects directly to the stove's
**SERIAL** port, without that module.

Tableau bilingue : une cellule qui diffère entre les langues s'écrit « français // anglais ».

| Marque // Brand | Modèle // Model | Génération // Generation | Connecteur SERIAL, brochage // SERIAL connector, pinout | Interface testée // Tested interface | Réglages // Settings | État // Status | Retour // Report |
|---|---|---|---|---|---|---|---|
| La Nordica-Extraflame | Comfort P85 | Black Label (compat. constructeur) // Black Label (vendor compat.) | 4 broches : 1=GND, 2=+5V, 3=+12V ⚠️, 4=DATA // 4-pin: 1=GND, 2=+5V, 3=+12V ⚠️, 4=DATA | ESP32 + level-shifter bidirectionnel BSS138 (DIY) // ESP32 + BSS138 bidirectional level shifter (DIY) | carte `external-swire` ; UART1 1200 8N2 ; TX=GPIO23 (drain ouvert), RX=GPIO5 ; **inversion RX ON, TX non inversé** // board `external-swire`; UART1 1200 8N2; TX=GPIO23 (open-drain), RX=GPIO5; **RX inversion ON, TX not inverted** | en ligne, décodage en cours de confirmation // online, decoding being confirmed | [#2](https://github.com/Isno-Open/OpenXtraflame/issues/2) (depretmathieu-code) |

Colonne État // Status: « en ligne » = l'ESP dialogue avec le poêle ; « décode » = les
valeurs correspondent à la réalité. // "online" = the ESP talks to the stove; "decoding" =
values match reality.

Un retour à ajouter ? Ouvrez une issue avec la marque, le modèle, la génération (Label), le
**brochage du connecteur SERIAL**, l'interface utilisée et les réglages qui ont marché
(broches, inversion). // A report to add? Open an issue with the brand, model, generation
(Label), the **SERIAL connector pinout**, the interface used and the settings that worked.

## Particularités connues // Known specifics

**Brochage du connecteur SERIAL : à relever, il n'est PAS universel.** Sur le Comfort P85 :
1=GND, 2=+5V, 3=+12V, 4=DATA, avec la **DATA sur la broche qui « bouge »** (les deux autres
5 V / 12 V sont des alimentations fixes). Toujours repérer la DATA à l'oscillo ou via le
diagnostic série du web avant de câbler. // The SERIAL pinout is NOT universal. On the P85:
1=GND, 2=+5V, 3=+12V, 4=DATA; DATA is the pin that toggles (the 5 V / 12 V pins are steady
supplies). Always identify DATA before wiring.

⚠️ **Tout le bus est en 5 V et l'ESP32 est en 3,3 V : même le 5 V le grille.** Les GPIO de
l'ESP32 ne tolèrent PAS le 5 V, donc relier **n'importe quelle broche 5 V (la DATA comme
l'alim) directement à l'ESP32 le détruit** ; le +12 V est pire encore (il détruit aussi le
côté bas du shifter). **Rien du poêle ne doit toucher l'ESP32 en direct : tout transite par
le level-shifter.** Mais attention : **le level-shifter n'est qu'un TRADUCTEUR de niveau,
pas une protection ni une isolation.** Même avec lui, l'ESP grille si on met du 5 V sur sa
référence `LV` (au lieu du 3,3 V), si le +12 V atteint le côté HV, ou sur un transitoire du
bus : les MOSFET du BSS138 ne bloquent pas une surtension, et il n'y a ni TVS ni clamp. Un
montage DIY n'a donc **AUCUNE protection** contre une inversion de fils, une surtension ou
une décharge : une erreur de câblage est fatale. L'adaptateur isolé du
projet (carte `micronova-iso-adapter`, isolateur + protections d'entrée) retire ce risque ;
en DIY, vérifier deux fois avant de mettre sous tension. // The whole bus is 5 V and the ESP32
is 3.3 V only: even the 5 V destroys it. ESP32 GPIOs are NOT 5 V tolerant, so wiring any 5 V
pin (DATA or supply) directly to the ESP32 destroys it; the +12 V is worse (it also kills the
low side of the shifter). Nothing from the stove should touch the ESP32 directly: everything
goes through the level shifter. But beware: the level shifter is only a level TRANSLATOR,
not protection nor isolation. Even with it, the ESP is destroyed if 5 V reaches its `LV`
reference (instead of 3.3 V), if the +12 V reaches the HV side, or on a bus transient: the
BSS138 MOSFETs do not block over-voltage, and there is no TVS or clamp. A DIY build has NO
protection against reversed wires, over-voltage or ESD. The project's isolated adapter removes
that risk.

**Inversion de ligne selon l'interface.** Un poêle Black Label attend une **inversion RX**
(le firmware d'origine utilise `RXD_INV`). Avec un level-shifter **passif non inverseur**, on
met donc l'**inversion RX sur ON** côté firmware, mais **jamais l'inversion TX** : le TX est
en drain ouvert, et l'inverser tiendrait la ligne basse en permanence. Le signe d'une
inversion RX à l'envers : des octets reçus tout en haut (0xF_) qui, inversés, redonnent des
valeurs basses cohérentes (températures ~18-25). // Line inversion depends on the interface.
A Black Label stove expects RX inversion (the original firmware uses `RXD_INV`). With a
passive non-inverting level shifter, set RX inversion ON but never TX inversion (TX is
open-drain; inverting it would hold the line low). Symptom of wrong RX inversion: received
bytes all high (0xF_) that, inverted, give sensible low values (temperatures ~18-25).
