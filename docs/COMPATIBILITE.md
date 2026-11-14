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

⚠️ **Le +12V est dangereux et le montage DIY n'est PAS protégé.** Relier le +12 V (ou le
+5 V fixe) à l'ESP32 ou au côté basse tension du level-shifter le détruit. Un branchement
direct (shifter + fils) n'a **aucune protection** contre une inversion de fils, une
surtension ou une décharge : une erreur de câblage est fatale pour l'ESP. L'adaptateur isolé
du projet (carte `micronova-iso-adapter`, isolateur + protections d'entrée) est fait pour
retirer ce risque ; en DIY, vérifier deux fois avant de mettre sous tension. // The +12 V is
dangerous and a DIY build has NO protection. Wiring the +12 V (or the steady +5 V) to the
ESP32 or the low-voltage side destroys it. A direct build (shifter + wires) has no protection
against reversed wires, over-voltage or ESD. The project's isolated adapter removes that risk;
in DIY, double-check before powering up.

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
