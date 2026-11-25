# Carte des registres Micronova du module Extraflame Black Label

Les adresses que le module Wi-Fi officiel d'Extraflame (Black Label T009_3, firmware v1.8 de décembre 2022) lit et écrit sur le bus Micronova, pour **chacun des 12 types de poêle** qu'il connaît. Elles sont lues telles quelles dans sa table `Addrs_dyn` ; seules les lignes marquées « vérifié » ont été contrôlées sur un poêle réel (Teodora Evo, famille ventilée).

Ce document ne contient que des faits d'interopérabilité : adresses et noms de registres. Ni binaire, ni code décompilé, ni donnée propre à un poêle ou à un compte.

## Comment la table est rangée dans le firmware

- Un tableau de **102 pointeurs vers les noms** des registres : 82 registres EEPROM (`EEPROM_*`), puis 20 registres RAM (`RAM_*`). Les compteurs `EEPROM_ADDRS_COUNT` et `RAM_ADDRS_COUNT` du firmware donnent ces deux nombres. Il est suivi de **37 noms de constantes** : codes d'alarme et valeurs d'état.
- **12 blocs de 406 octets, un par type de poêle**, chacun fait de quatre tableaux dans le même ordre que les noms :
  1. 82 octets : la **valeur maximale** admise pour chaque registre EEPROM ;
  2. 82 octets : la **valeur minimale** ;
  3. 102 adresses sur 16 bits (`0xFFFF` = ce type n'a pas ce registre, case vide ci-dessous) ;
  4. 37 octets : la valeur de chaque constante pour ce type.
- Le bloc d'un type se trouve par **cinq tables de 12 pointeurs** (maximums, minimums, adresses EEPROM, adresses RAM, constantes), indexées par le numéro du type, de 0 à 11 : `I_IDRO`, `I_IDRO_2`, `I_VENT` à `I_VENT_5`, `I_CANAL` à `I_CANAL_4`, `I_CALD`. C'est aussi l'ordre des noms `STOVE_TYPE_*` dans le firmware. Le type d'un poêle vient de son code de modèle : voir [MODELES.md](MODELES.md).

Trois recoupements indépendants confirment le décodage. Sur le bloc ventilé, `0x21` (état), `0x01` (ambiance), `0x7F` (puissance) et `0x7D` (consigne) sont exactement les adresses vérifiées sur la Teodora Evo. La température de l'eau (`RAM_TH20_ADDR`) et ses alarmes n'existent que pour la chaudière et les deux hydros. Et dans les 12 blocs, une borne n'est renseignée que là où une adresse existe : puissance de 1 à 5, programmes horaires de 0 à 144 (dizaines de minutes sur 24 h), jours à 0 ou 1.

Lecture : `loc 0x00` pour la RAM, `0x20` pour l'EEPROM ; écriture : `0x80` pour la RAM, `0xA0` pour l'EEPROM. Voir [PROTOCOLE-MICRONOVA.md](PROTOCOLE-MICRONOVA.md).

## Ce qui est vérifié (Teodora Evo, famille ventilée)

| Registre | Adresse | Mesure |
|---|---|---|
| `RAM_STOVE_STATUS_ADDR` | `0x21` | état cohérent avec le poêle |
| `RAM_TAMB_ADDR` | `0x01` | 61 = 30,5 °C |
| `EEPROM_SET_POWER_ADDR` | `0x7F` | 4 quand l'écran affiche 4 |
| `EEPROM_SET_AMB_ADDR` | `0x7D` | 27 quand l'écran affiche 27 |

Tout le reste est **lu dans la table, non vérifié**. Une mesure par ligne est bienvenue (issue GitHub avec le modèle, le type détecté et la valeur lue face à l'écran).

## Points ouverts

- **`RAM_T_FUMI_ADDR`** vaut `0x02` dans les 12 tables, alors que la mesure sur la Teodora a trouvé la température des fumées affichée en RAM `0x5A`. À trancher.
- **`RAM_ACCENDI` (`0x55`) et `RAM_SPEGNI` (`0xAA`)** ressemblent à des valeurs de commande plus qu'à des adresses : sur la Teodora, l'allumage passe par `0x21` = 1 et l'extinction par `0x21` = 6.
- **`EEPROM_SET_CHRONO_ENABLE_ADDR`** (interrupteur général de programmation) n'existe que pour `I_IDRO_2` (`0xB8`) et `I_VENT_5` (`0xAE`). OpenXtraflame écrit `0xAE` sur la Teodora : à vérifier, ou à réserver aux poêles `I_VENT_5`.
- Les adresses `0xDF`, `0xE0` et `0xE2` que `micronova.h` attribue à la trémie vide, à la cause de la veille et à la modulation pour la famille ventilée sont celles des températures de ballon et de chaudière (`I_CALD`, `I_IDRO`). Pour `I_VENT`, la modulation est en `0xA5`, et la trémie et la cause de la veille n'existent pas.
- Les alarmes et le déblocage ne sont pas en `0x40` et `0x41`, comme on le lit parfois : la table donne `0x33` et `0x06` pour tous les types.
- La table des 239 codes de modèle est décodée ([MODELES.md](MODELES.md)). Le module de la Teodora Evo mesurée porte le code générique `009278451000`, qui donne `I_VENT` par défaut : pour ce type, l'interrupteur général de programmation (`0xAE`) n'existe pas. Reste à savoir si le module remplace ce type par un autre (voir l'exception décrite dans MODELES.md).

## Bornes des réglages (EEPROM)

Les valeurs que le module officiel accepte d'écrire, par type. Les programmes horaires 2 à 4 ont les mêmes bornes que le programme 1. Les consignes sont en °C, les heures de début et de fin en dizaines de minutes. Un firmware qui écrit dans ces registres devrait s'y tenir.

| Registre | CALD | CANAL | CANAL_2 | CANAL_3 | CANAL_4 | IDRO | IDRO_2 | VENT | VENT_2 | VENT_3 | VENT_4 | VENT_5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `SET_POWER` | 1 à 5 | 1 à 5 | 1 à 5 | 1 à 5 | 1 à 5 | 1 à 5 | 1 à 5 | 1 à 5 | 1 à 5 | 1 à 5 | 1 à 5 | 1 à 5 |
| `SET_AMB` | 0 à 0 | 6 à 38 | 6 à 38 | 6 à 38 | 6 à 38 | 6 à 38 | 6 à 40 | 6 à 38 | 6 à 38 | 6 à 38 | 6 à 38 | 6 à 41 |
| `SET_TEMP` |  |  |  |  |  | 65 à 80 | 65 à 80 |  |  |  |  |  |
| `SET_TANG_ENABLE` |  |  |  |  |  | 0 à 1 | 0 à 1 |  |  |  |  | 0 à 1 |
| `SET_TANG_VEL` | 0 à 0 | 0 à 2 | 0 à 2 | 0 à 2 | 0 à 2 | 7 à 11 | 7 à 11 | 0 à 2 | 0 à 2 | 0 à 2 | 0 à 2 | 7 à 11 |
| `SET_CAN1_VEL` | 0 à 0 | 0 à 3 | 0 à 3 | 0 à 3 | 0 à 3 |  |  |  |  | 0 à 0 |  |  |
| `SET_CAN2_VEL` |  |  | 0 à 3 | 0 à 3 |  |  |  |  |  |  |  |  |
| `SET_CAN1_TEMP` | 0 à 0 | 6 à 38 | 6 à 38 | 6 à 38 | 6 à 38 |  |  |  |  | 0 à 0 |  |  |
| `SET_CAN2_TEMP` |  |  | 6 à 38 | 6 à 38 |  |  |  |  |  |  |  |  |
| `SET_CHRONO_ENABLE` |  |  |  |  |  |  | 0 à 1 |  |  |  |  | 0 à 1 |
| `SET_CHRONO_ENABLE1` | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 |
| `SET_CHRONO_ENABLE2` | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 |
| `SET_CHRONO_ENABLE3` | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 |
| `SET_CHRONO_ENABLE4` | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 |
| `SET_CHRONO1_START` | 0 à 144 | 0 à 144 | 0 à 144 | 0 à 144 | 0 à 144 | 0 à 144 | 0 à 144 | 0 à 144 | 0 à 144 | 0 à 144 | 0 à 144 | 0 à 144 |
| `SET_CHRONO1_STOP` | 0 à 144 | 0 à 144 | 0 à 144 | 0 à 144 | 0 à 144 | 0 à 144 | 0 à 144 | 0 à 144 | 0 à 144 | 0 à 144 | 0 à 144 | 0 à 144 |
| `SET_CHRONO1_DAY1` | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 |
| `SET_CHRONO1_DAY2` | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 |
| `SET_CHRONO1_DAY3` | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 |
| `SET_CHRONO1_DAY4` | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 |
| `SET_CHRONO1_DAY5` | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 |
| `SET_CHRONO1_DAY6` | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 |
| `SET_CHRONO1_DAY7` | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 | 0 à 1 |
| `SET_CHRONO1_TEMP` | 65 à 80 | 6 à 38 | 6 à 38 | 6 à 38 | 6 à 38 | 65 à 80 | 65 à 80 | 6 à 38 | 6 à 38 | 6 à 38 | 6 à 38 | 6 à 41 |
| `SET_CHRONO1_POWER` | 1 à 5 | 1 à 5 | 1 à 5 | 1 à 5 | 1 à 5 | 1 à 5 | 1 à 5 | 1 à 5 | 1 à 5 | 1 à 5 | 1 à 5 |  |
| `SET_TIME_DAY` | 1 à 7 | 1 à 7 | 1 à 7 | 1 à 7 | 1 à 7 | 1 à 7 | 1 à 7 | 1 à 7 | 1 à 7 | 1 à 7 | 1 à 7 | 1 à 7 |
| `SET_TIME_HOURS` | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 |
| `SET_TIME_MINUTES` | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 |
| `SET_TIME_DATE` | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 |
| `SET_TIME_MONTH` | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 |
| `SET_TIME_YEAR` | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 | 0 à 255 |
| `SET_CHECKPELLET_ENABLED` |  |  |  | 0 à 1 | 0 à 1 |  |  |  | 0 à 1 |  |  |  |

Pour la famille ventilée de base, la consigne d'ambiance va donc de 6 à 38 °C et la puissance de 1 à 5. Les registres de l'horloge (heures, minutes, date, mois, année) n'ont pas de borne dans la table (0 à 255).

## Codes d'alarme et valeurs d'état

Les 37 constantes du firmware, avec leur valeur par type (hexadécimal, `00` = sans objet pour ce type). Les noms sont ceux d'Extraflame, en italien. Les codes d'alarme sont ceux qu'on lit dans `RAM_ALLARM_ADDR` (`0x33`), que le module publie tel quel (`{"alarmCode": n}`).

| Constante | Sens | CALD | CANAL | CANAL_2 | CANAL_3 | CANAL_4 | IDRO | IDRO_2 | VENT | VENT_2 | VENT_3 | VENT_4 | VENT_5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `NESSUN_ALLARME` | aucune alarme | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 |
| `SONDA_FUMI_BIT` | sonde de fumées | 01 | 01 | 01 | 01 | 01 | 01 | 01 | 01 | 01 | 01 | 01 | 01 |
| `HOT_FUMI_BIT` | fumées trop chaudes | 02 | 02 | 02 | 02 | 02 | 02 | 02 | 02 | 02 | 02 | 02 | 02 |
| `SONDA_FUMI_CORTO_BIT` | sonde de fumées en court-circuit | 03 | 03 | 03 | 03 | 03 | 03 | 03 | 03 | 03 | 03 | 03 | 03 |
| `ASPIRATORE_GUASTO_BIT` | extracteur de fumées en panne | 04 | 04 | 04 | 04 | 04 | 04 | 04 | 04 | 04 | 04 | 04 | 04 |
| `MANCATA_ACCENSIONE_BIT` | allumage manqué | 08 | 08 | 08 | 08 | 08 | 08 | 08 | 08 | 08 | 08 | 08 | 08 |
| `MANCATA_FIAMMA_BIT` | flamme perdue | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 |
| `ALL_DEPR_BIT` | dépression | 20 | 20 | 20 | 20 | 20 | 20 | 20 | 20 | 20 | 20 | 20 | 20 |
| `SONDA_H20_BIT` | sonde d'eau | 82 | 00 | 00 | 00 | 00 | 81 | 81 | 00 | 00 | 00 | 00 | 00 |
| `ALLARME_COMANDO_COCLEA_BIT` | commande de la vis sans fin | C9 | 82 | C0 | 82 | 82 | C9 | C9 | 82 | 82 | C0 | 82 | 82 |
| `ALLARME_PRESSIONE_H20_MIN_BIT` | pression d'eau trop basse | 88 | 00 | 00 | 00 | 00 | 88 | 88 | 00 | 00 | 00 | 00 | 00 |
| `SONDA_BOILER_BIT` | sonde du ballon sanitaire | 90 | 00 | 00 | 00 | 00 | 90 | 90 | 00 | 00 | 00 | 00 | 00 |
| `SONDA_PUFFER_BIT` | sonde du ballon tampon | A0 | 00 | 00 | 00 | 00 | A0 | A0 | 00 | 00 | 00 | 00 | 00 |
| `PWM_INTERFACCIA_BIT` | circulateur : interface | C2 | 00 | 00 | 00 | 00 | C2 | C2 | 00 | 00 | 00 | 00 | 00 |
| `PWM_CALDO_BIT` | circulateur : surchauffe | C3 | 00 | 00 | 00 | 00 | C3 | C3 | 00 | 00 | 00 | 00 | 00 |
| `PWM_STOP_BIT` | circulateur : arrêt | C4 | 00 | 00 | 00 | 00 | C4 | C4 | 00 | 00 | 00 | 00 | 00 |
| `PWM_STOP2_BIT` | circulateur : arrêt 2 | C5 | 00 | 00 | 00 | 00 | C5 | C5 | 00 | 00 | 00 | 00 | 00 |
| `PWM_BLOCCO_BIT` | circulateur : blocage | C6 | 00 | 00 | 00 | 00 | C6 | C6 | 00 | 00 | 00 | 00 | 00 |
| `PWM_FLUSSO_BIT` | circulateur : débit | C7 | 00 | 00 | 00 | 00 | C7 | C7 | 00 | 00 | 00 | 00 | 00 |
| `ALLARME_PRESSIONE_H20_MAX_BIT` | pression d'eau trop haute | 98 | 00 | 00 | 00 | 00 | 98 | 98 | 00 | 00 | 00 | 00 | 00 |
| `ALLARME_ACCENSIONE_BLACKOUT_BIT` | allumage après coupure de courant | FF | FF | FF | FF | FF | FF | FF | FF | FF | FF | FF | FF |
| `ALLARME_SOVRATEMPERATURA_H2O_BIT` | surchauffe de l'eau | 00 | 00 | 00 | 00 | 00 | 82 | 82 | 00 | 00 | 00 | 00 | 00 |
| `CAN1_STATUS_REQUEST_BY_SHORT_BIT` | canalisation 1 : demande par contact | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 |
| `CAN1_STATUS_REQUEST_BY_SENSOR_BIT` | canalisation 1 : demande par sonde | 00 | 01 | 01 | 01 | 01 | 00 | 00 | 00 | 00 | 00 | 00 | 00 |
| `CAN2_STATUS_REQUEST_BY_SHORT_BIT` | canalisation 2 : demande par contact | 00 | 00 | 02 | 02 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 |
| `CAN2_STATUS_REQUEST_BY_SENSOR_BIT` | canalisation 2 : demande par sonde | 00 | 00 | 03 | 03 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 |
| `GESTIONE_PUL_ORD_APRI_BIT` | nettoyage : ouvrir | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 |
| `GESTIONE_PUL_ORD_CHIUDI_BIT` | nettoyage : fermer | 01 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 |
| `STATO_PUL_ORD_OFF_VALUE` | nettoyage : arrêté | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 |
| `STATO_PUL_ORD_APERTURA_VALUE` | nettoyage : ouverture | 01 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 |
| `STATO_PUL_ORD_APERTO_VALUE` | nettoyage : ouvert | 02 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 |
| `STATO_PUL_ORD_CHIUSURA_VALUE` | nettoyage : fermeture | 03 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 |
| `GUASTO_BOTOLA_BIT` | trappe en panne | 84 | 00 | 84 | 00 | 00 | 00 | 84 | 00 | 00 | 84 | 00 | 84 |
| `BLOCCO_COCLEA_BIT` | vis sans fin bloquée | CA | 00 | A0 | 00 | 00 | 00 | 00 | 81 | 00 | A0 | 81 | 00 |
| `SONDA_CAMERA_BIT` | sonde de chambre | CD | 00 | CD | 00 | 00 | 00 | 00 | 00 | 00 | CD | 00 | 00 |
| `CORRENTE_MAX_BIT` | courant maximal | C1 | 00 | 88 | 00 | 00 | 00 | C1 | 00 | 00 | 88 | 00 | 88 |
| `BULBO_ON_VALUE` | thermostat à bulbe actif | F0 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 | 00 |

La traduction des noms est la mienne, le sens exact de plusieurs constantes (notamment les `PWM_*` et `PUL_ORD_*`) reste à confirmer. Pour un poêle ventilé de base, les alarmes utiles sont donc : `01` sonde de fumées, `02` fumées trop chaudes, `03` sonde en court-circuit, `04` extracteur, `08` allumage manqué, `10` flamme perdue, `20` dépression, `81` vis sans fin bloquée, `82` commande de la vis.

## Registres EEPROM (82)

| # | Nom Extraflame | CALD | CANAL | CANAL_2 | CANAL_3 | CANAL_4 | IDRO | IDRO_2 | VENT | VENT_2 | VENT_3 | VENT_4 | VENT_5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | `EEPROM_SET_POWER_ADDR` | 0x7F | 0x7F | 0x7F | 0x7F | 0x7F | 0x45 | 0x45 | 0x7F | 0x7F | 0x7F | 0x7F | 0x7F |
| 1 | `EEPROM_SET_AMB_ADDR` | 0x7D | 0x7D | 0x7D | 0x7D | 0x7D | 0x30 | 0x30 | 0x7D | 0x7D | 0x7D | 0x7D | 0x7D |
| 2 | `EEPROM_SET_TEMP_ADDR` |  |  |  |  |  | 0x31 | 0x31 |  |  |  |  |  |
| 3 | `EEPROM_SET_TANG_ENABLE_ADDR` |  |  |  |  |  | 0x3F | 0x3F |  |  |  |  | 0x3F |
| 4 | `EEPROM_SET_TANG_VEL_ADDR` | 0x44 | 0x44 | 0x44 | 0x44 | 0x44 | 0x40 | 0x40 | 0x44 | 0x44 | 0x44 | 0x44 | 0x40 |
| 5 | `EEPROM_SET_CAN1_VEL_ADDR` | 0xAB | 0xAB | 0xAB | 0xAB | 0xAB |  |  |  |  | 0xAB |  |  |
| 6 | `EEPROM_SET_CAN2_VEL_ADDR` |  |  | 0xAC | 0xAC |  |  |  |  |  |  |  |  |
| 7 | `EEPROM_SET_CAN1_TEMP_ADDR` | 0x80 | 0x80 | 0x80 | 0x80 | 0x80 |  |  |  |  | 0x7E |  |  |
| 8 | `EEPROM_SET_CAN2_TEMP_ADDR` |  |  | 0x81 | 0x81 |  |  |  |  |  |  |  |  |
| 9 | `EEPROM_SET_CHRONO_ENABLE_ADDR` |  |  |  |  |  |  | 0xB8 |  |  |  |  | 0xAE |
| 10 | `EEPROM_SET_CHRONO_ENABLE1_ADDR` | 0xAF | 0xAF | 0xAF | 0xAF | 0xAF | 0xB9 | 0xB9 | 0xAF | 0xAF | 0xAF | 0xAF | 0xAF |
| 11 | `EEPROM_SET_CHRONO_ENABLE2_ADDR` | 0xB0 | 0xB0 | 0xB0 | 0xB0 | 0xB0 | 0xBA | 0xBA | 0xB0 | 0xB0 | 0xB0 | 0xB0 | 0xB0 |
| 12 | `EEPROM_SET_CHRONO_ENABLE3_ADDR` | 0xB1 | 0xB1 | 0xB1 | 0xB1 | 0xB1 | 0xBB | 0xBB | 0xB1 | 0xB1 | 0xB1 | 0xB1 | 0xB1 |
| 13 | `EEPROM_SET_CHRONO_ENABLE4_ADDR` | 0xB2 | 0xB2 | 0xB2 | 0xB2 | 0xB2 | 0xBC | 0xBC | 0xB2 | 0xB2 | 0xB2 | 0xB2 | 0xB2 |
| 14 | `EEPROM_SET_CHRONO1_START_ADDR` | 0x4D | 0x4D | 0x4D | 0x4D | 0x4D | 0x4D | 0x4D | 0x4D | 0x4D | 0x4D | 0x4D | 0x4D |
| 15 | `EEPROM_SET_CHRONO1_STOP_ADDR` | 0x4E | 0x4E | 0x4E | 0x4E | 0x4E | 0x4E | 0x4E | 0x4E | 0x4E | 0x4E | 0x4E | 0x4E |
| 16 | `EEPROM_SET_CHRONO1_DAY1_ADDR` | 0x4F | 0x4F | 0x4F | 0x4F | 0x4F | 0x4F | 0x4F | 0x4F | 0x4F | 0x4F | 0x4F | 0x4F |
| 17 | `EEPROM_SET_CHRONO1_DAY2_ADDR` | 0x50 | 0x50 | 0x50 | 0x50 | 0x50 | 0x50 | 0x50 | 0x50 | 0x50 | 0x50 | 0x50 | 0x50 |
| 18 | `EEPROM_SET_CHRONO1_DAY3_ADDR` | 0x51 | 0x51 | 0x51 | 0x51 | 0x51 | 0x51 | 0x51 | 0x51 | 0x51 | 0x51 | 0x51 | 0x51 |
| 19 | `EEPROM_SET_CHRONO1_DAY4_ADDR` | 0x52 | 0x52 | 0x52 | 0x52 | 0x52 | 0x52 | 0x52 | 0x52 | 0x52 | 0x52 | 0x52 | 0x52 |
| 20 | `EEPROM_SET_CHRONO1_DAY5_ADDR` | 0x53 | 0x53 | 0x53 | 0x53 | 0x53 | 0x53 | 0x53 | 0x53 | 0x53 | 0x53 | 0x53 | 0x53 |
| 21 | `EEPROM_SET_CHRONO1_DAY6_ADDR` | 0x54 | 0x54 | 0x54 | 0x54 | 0x54 | 0x54 | 0x54 | 0x54 | 0x54 | 0x54 | 0x54 | 0x54 |
| 22 | `EEPROM_SET_CHRONO1_DAY7_ADDR` | 0x55 | 0x55 | 0x55 | 0x55 | 0x55 | 0x55 | 0x55 | 0x55 | 0x55 | 0x55 | 0x55 | 0x55 |
| 23 | `EEPROM_SET_CHRONO1_TEMP_ADDR` | 0x56 | 0x56 | 0x56 | 0x56 | 0x56 | 0x56 | 0x56 | 0x56 | 0x56 | 0x56 | 0x56 | 0x56 |
| 24 | `EEPROM_SET_CHRONO1_POWER_ADDR` | 0x8E | 0x8E | 0x9E | 0x9E | 0x9E | 0x48 | 0xD4 | 0x8E | 0x9E | 0x9E | 0x8E |  |
| 25 | `EEPROM_SET_CHRONO2_START_ADDR` | 0x57 | 0x57 | 0x57 | 0x57 | 0x57 | 0x57 | 0x57 | 0x57 | 0x57 | 0x57 | 0x57 | 0x57 |
| 26 | `EEPROM_SET_CHRONO2_STOP_ADDR` | 0x58 | 0x58 | 0x58 | 0x58 | 0x58 | 0x58 | 0x58 | 0x58 | 0x58 | 0x58 | 0x58 | 0x58 |
| 27 | `EEPROM_SET_CHRONO2_DAY1_ADDR` | 0x59 | 0x59 | 0x59 | 0x59 | 0x59 | 0x59 | 0x59 | 0x59 | 0x59 | 0x59 | 0x59 | 0x59 |
| 28 | `EEPROM_SET_CHRONO2_DAY2_ADDR` | 0x5A | 0x5A | 0x5A | 0x5A | 0x5A | 0x5A | 0x5A | 0x5A | 0x5A | 0x5A | 0x5A | 0x5A |
| 29 | `EEPROM_SET_CHRONO2_DAY3_ADDR` | 0x5B | 0x5B | 0x5B | 0x5B | 0x5B | 0x5B | 0x5B | 0x5B | 0x5B | 0x5B | 0x5B | 0x5B |
| 30 | `EEPROM_SET_CHRONO2_DAY4_ADDR` | 0x5C | 0x5C | 0x5C | 0x5C | 0x5C | 0x5C | 0x5C | 0x5C | 0x5C | 0x5C | 0x5C | 0x5C |
| 31 | `EEPROM_SET_CHRONO2_DAY5_ADDR` | 0x5D | 0x5D | 0x5D | 0x5D | 0x5D | 0x5D | 0x5D | 0x5D | 0x5D | 0x5D | 0x5D | 0x5D |
| 32 | `EEPROM_SET_CHRONO2_DAY6_ADDR` | 0x5E | 0x5E | 0x5E | 0x5E | 0x5E | 0x5E | 0x5E | 0x5E | 0x5E | 0x5E | 0x5E | 0x5E |
| 33 | `EEPROM_SET_CHRONO2_DAY7_ADDR` | 0x5F | 0x5F | 0x5F | 0x5F | 0x5F | 0x5F | 0x5F | 0x5F | 0x5F | 0x5F | 0x5F | 0x5F |
| 34 | `EEPROM_SET_CHRONO2_TEMP_ADDR` | 0x60 | 0x60 | 0x60 | 0x60 | 0x60 | 0x60 | 0x60 | 0x60 | 0x60 | 0x60 | 0x60 | 0x60 |
| 35 | `EEPROM_SET_CHRONO2_POWER_ADDR` | 0x8F | 0x8F | 0x9F | 0x9F | 0x9F | 0x49 | 0xD5 | 0x8F | 0x9F | 0x9F | 0x8F |  |
| 36 | `EEPROM_SET_CHRONO3_START_ADDR` | 0x61 | 0x61 | 0x61 | 0x61 | 0x61 | 0x61 | 0x61 | 0x61 | 0x61 | 0x61 | 0x61 | 0x61 |
| 37 | `EEPROM_SET_CHRONO3_STOP_ADDR` | 0x62 | 0x62 | 0x62 | 0x62 | 0x62 | 0x62 | 0x62 | 0x62 | 0x62 | 0x62 | 0x62 | 0x62 |
| 38 | `EEPROM_SET_CHRONO3_DAY1_ADDR` | 0x63 | 0x63 | 0x63 | 0x63 | 0x63 | 0x63 | 0x63 | 0x63 | 0x63 | 0x63 | 0x63 | 0x63 |
| 39 | `EEPROM_SET_CHRONO3_DAY2_ADDR` | 0x64 | 0x64 | 0x64 | 0x64 | 0x64 | 0x64 | 0x64 | 0x64 | 0x64 | 0x64 | 0x64 | 0x64 |
| 40 | `EEPROM_SET_CHRONO3_DAY3_ADDR` | 0x65 | 0x65 | 0x65 | 0x65 | 0x65 | 0x65 | 0x65 | 0x65 | 0x65 | 0x65 | 0x65 | 0x65 |
| 41 | `EEPROM_SET_CHRONO3_DAY4_ADDR` | 0x66 | 0x66 | 0x66 | 0x66 | 0x66 | 0x66 | 0x66 | 0x66 | 0x66 | 0x66 | 0x66 | 0x66 |
| 42 | `EEPROM_SET_CHRONO3_DAY5_ADDR` | 0x67 | 0x67 | 0x67 | 0x67 | 0x67 | 0x67 | 0x67 | 0x67 | 0x67 | 0x67 | 0x67 | 0x67 |
| 43 | `EEPROM_SET_CHRONO3_DAY6_ADDR` | 0x68 | 0x68 | 0x68 | 0x68 | 0x68 | 0x68 | 0x68 | 0x68 | 0x68 | 0x68 | 0x68 | 0x68 |
| 44 | `EEPROM_SET_CHRONO3_DAY7_ADDR` | 0x69 | 0x69 | 0x69 | 0x69 | 0x69 | 0x69 | 0x69 | 0x69 | 0x69 | 0x69 | 0x69 | 0x69 |
| 45 | `EEPROM_SET_CHRONO3_TEMP_ADDR` | 0x6A | 0x6A | 0x6A | 0x6A | 0x6A | 0x6A | 0x6A | 0x6A | 0x6A | 0x6A | 0x6A | 0x6A |
| 46 | `EEPROM_SET_CHRONO3_POWER_ADDR` | 0x90 | 0x90 | 0xA0 | 0xA0 | 0xA0 | 0x75 | 0xD6 | 0x90 | 0xA0 | 0xA0 | 0x90 |  |
| 47 | `EEPROM_SET_CHRONO4_START_ADDR` | 0x6B | 0x6B | 0x6B | 0x6B | 0x6B | 0x6B | 0x6B | 0x6B | 0x6B | 0x6B | 0x6B | 0x6B |
| 48 | `EEPROM_SET_CHRONO4_STOP_ADDR` | 0x6C | 0x6C | 0x6C | 0x6C | 0x6C | 0x6C | 0x6C | 0x6C | 0x6C | 0x6C | 0x6C | 0x6C |
| 49 | `EEPROM_SET_CHRONO4_DAY1_ADDR` | 0x6D | 0x6D | 0x6D | 0x6D | 0x6D | 0x6D | 0x6D | 0x6D | 0x6D | 0x6D | 0x6D | 0x6D |
| 50 | `EEPROM_SET_CHRONO4_DAY2_ADDR` | 0x6E | 0x6E | 0x6E | 0x6E | 0x6E | 0x6E | 0x6E | 0x6E | 0x6E | 0x6E | 0x6E | 0x6E |
| 51 | `EEPROM_SET_CHRONO4_DAY3_ADDR` | 0x6F | 0x6F | 0x6F | 0x6F | 0x6F | 0x6F | 0x6F | 0x6F | 0x6F | 0x6F | 0x6F | 0x6F |
| 52 | `EEPROM_SET_CHRONO4_DAY4_ADDR` | 0x70 | 0x70 | 0x70 | 0x70 | 0x70 | 0x70 | 0x70 | 0x70 | 0x70 | 0x70 | 0x70 | 0x70 |
| 53 | `EEPROM_SET_CHRONO4_DAY5_ADDR` | 0x71 | 0x71 | 0x71 | 0x71 | 0x71 | 0x71 | 0x71 | 0x71 | 0x71 | 0x71 | 0x71 | 0x71 |
| 54 | `EEPROM_SET_CHRONO4_DAY6_ADDR` | 0x72 | 0x72 | 0x72 | 0x72 | 0x72 | 0x72 | 0x72 | 0x72 | 0x72 | 0x72 | 0x72 | 0x72 |
| 55 | `EEPROM_SET_CHRONO4_DAY7_ADDR` | 0x73 | 0x73 | 0x73 | 0x73 | 0x73 | 0x73 | 0x73 | 0x73 | 0x73 | 0x73 | 0x73 | 0x73 |
| 56 | `EEPROM_SET_CHRONO4_TEMP_ADDR` | 0x74 | 0x74 | 0x74 | 0x74 | 0x74 | 0x74 | 0x74 | 0x74 | 0x74 | 0x74 | 0x74 | 0x74 |
| 57 | `EEPROM_SET_CHRONO4_POWER_ADDR` | 0x91 | 0x91 | 0xA1 | 0xA1 | 0xA1 | 0xB7 | 0xD7 | 0x91 | 0xA1 | 0xA1 | 0x91 |  |
| 58 | `EEPROM_SET_TIME_DAY_ADDR` | 0xF8 | 0xF8 | 0xF8 | 0xF8 | 0xF8 | 0xF8 | 0xF8 | 0xF8 | 0xF8 | 0xF8 | 0xF8 | 0xF8 |
| 59 | `EEPROM_SET_TIME_HOURS_ADDR` | 0xF9 | 0xF9 | 0xF9 | 0xF9 | 0xF9 | 0xF9 | 0xF9 | 0xF9 | 0xF9 | 0xF9 | 0xF9 | 0xF9 |
| 60 | `EEPROM_SET_TIME_MINUTES_ADDR` | 0xFA | 0xFA | 0xFA | 0xFA | 0xFA | 0xFA | 0xFA | 0xFA | 0xFA | 0xFA | 0xFA | 0xFA |
| 61 | `EEPROM_SET_TIME_DATE_ADDR` | 0xFB | 0xFB | 0xFB | 0xFB | 0xFB | 0xFB | 0xFB | 0xFB | 0xFB | 0xFB | 0xFB | 0xFB |
| 62 | `EEPROM_SET_TIME_MONTH_ADDR` | 0xFC | 0xFC | 0xFC | 0xFC | 0xFC | 0xFC | 0xFC | 0xFC | 0xFC | 0xFC | 0xFC | 0xFC |
| 63 | `EEPROM_SET_TIME_YEAR_ADDR` | 0xFD | 0xFD | 0xFD | 0xFD | 0xFD | 0xFD | 0xFD | 0xFD | 0xFD | 0xFD | 0xFD | 0xFD |
| 64 | `EEPROM_SET_CHECKPELLET_ENABLED` |  |  |  | 0xC6 | 0xC6 |  |  |  | 0xC6 |  |  |  |
| 65 | `EEPROM_COUNTERS_H_1_MSB` | 0xD1 | 0xD1 | 0xD1 | 0xD1 | 0xD1 | 0x1D1 | 0xD1 | 0xD1 | 0xD1 | 0xD1 | 0xD1 | 0xD1 |
| 66 | `EEPROM_COUNTERS_H_1_LSB` | 0xD0 | 0xD0 | 0xD0 | 0xD0 | 0xD0 | 0x1D0 | 0xD0 | 0xD0 | 0xD0 | 0xD0 | 0xD0 | 0xD0 |
| 67 | `EEPROM_COUNTERS_H_2_MSB` | 0xD3 | 0xD3 | 0xD3 | 0xD3 | 0xD3 | 0x1D3 | 0xD3 | 0xD3 | 0xD3 | 0xD3 | 0xD3 | 0xD3 |
| 68 | `EEPROM_COUNTERS_H_2_LSB` | 0xD2 | 0xD2 | 0xD2 | 0xD2 | 0xD2 | 0x1D2 | 0xD2 | 0xD2 | 0xD2 | 0xD2 | 0xD2 | 0xD2 |
| 69 | `EEPROM_COUNTERS_H_3_MSB` | 0xD5 | 0xD5 | 0xD5 | 0xD5 | 0xD5 | 0x1D5 | 0xD5 | 0xD5 | 0xD5 | 0xD5 | 0xD5 | 0xD5 |
| 70 | `EEPROM_COUNTERS_H_3_LSB` | 0xD4 | 0xD4 | 0xD4 | 0xD4 | 0xD4 | 0x1D4 | 0xD4 | 0xD4 | 0xD4 | 0xD4 | 0xD4 | 0xD4 |
| 71 | `EEPROM_COUNTERS_H_4_MSB` | 0xD7 | 0xD7 | 0xD7 | 0xD7 | 0xD7 | 0x1D7 | 0xD7 | 0xD7 | 0xD7 | 0xD7 | 0xD7 | 0xD7 |
| 72 | `EEPROM_COUNTERS_H_4_LSB` | 0xD6 | 0xD6 | 0xD6 | 0xD6 | 0xD6 | 0x1D6 | 0xD6 | 0xD6 | 0xD6 | 0xD6 | 0xD6 | 0xD6 |
| 73 | `EEPROM_COUNTERS_H_5_MSB` | 0xD9 | 0xD9 | 0xD9 | 0xD9 | 0xD9 | 0x1D9 | 0xD9 | 0xD9 | 0xD9 | 0xD9 | 0xD9 | 0xD9 |
| 74 | `EEPROM_COUNTERS_H_5_LSB` | 0xD8 | 0xD8 | 0xD8 | 0xD8 | 0xD8 | 0x1D8 | 0xD8 | 0xD8 | 0xD8 | 0xD8 | 0xD8 | 0xD8 |
| 75 | `EEPROM_COUNTERS_H_TOT_MSB` | 0xEB | 0xEB | 0x1EB | 0x1EB | 0x1EB | 0x1EB | 0x1EB | 0xEB | 0x1EB | 0x1EB | 0xEB | 0x1EB |
| 76 | `EEPROM_COUNTERS_H_TOT_LSB` | 0xEA | 0xEA | 0x1EA | 0x1EA | 0x1EA | 0x1EA | 0x1EA | 0xEA | 0x1EA | 0x1EA | 0xEA | 0x1EA |
| 77 | `EEPROM_COUNTERS_STARTS_MSB` | 0xEF | 0xEF | 0x1EF | 0x1EF | 0x1EF | 0x1EF | 0x1EF | 0xEF | 0x1EF | 0x1EF | 0xEF | 0x1EF |
| 78 | `EEPROM_COUNTERS_STARTS_LSB` | 0xEE | 0xEE | 0x1EE | 0x1EE | 0x1EE | 0x1EE | 0x1EE | 0xEE | 0x1EE | 0x1EE | 0xEE | 0x1EE |
| 79 | `EEPROM_SET_AUTOMATIC_MODE` |  |  |  |  |  |  |  |  |  |  |  |  |
| 80 | `EEPROM_SET_AIR_ZONE_CONTROL` |  |  |  |  |  |  |  |  |  |  |  |  |
| 81 | `EEPROM_SET_AIR_ZONE_CONTROL_AVAIL` |  |  |  |  |  |  |  |  |  |  |  |  |

## Registres RAM (20)

| # | Nom Extraflame | CALD | CANAL | CANAL_2 | CANAL_3 | CANAL_4 | IDRO | IDRO_2 | VENT | VENT_2 | VENT_3 | VENT_4 | VENT_5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 82 | `RAM_STOVE_STATUS_ADDR` | 0x21 | 0x21 | 0x21 | 0x21 | 0x21 | 0x21 | 0x21 | 0x21 | 0x21 | 0x21 | 0x21 | 0x21 |
| 83 | `RAM_TH20_ADDR` | 0x01 |  |  |  |  | 0x01 | 0x01 |  |  |  |  |  |
| 84 | `RAM_TAMB_ADDR` |  | 0x01 | 0x01 | 0x01 | 0x01 | 0xA6 | 0xA6 | 0x01 | 0x01 | 0x01 | 0x01 | 0x01 |
| 85 | `RAM_ALLARM_ADDR` | 0x33 | 0x33 | 0x33 | 0x33 | 0x33 | 0x33 | 0x33 | 0x33 | 0x33 | 0x33 | 0x33 | 0x33 |
| 86 | `RAM_STATO_GESTITO` | 0xE8 | 0xE8 | 0xE8 | 0xE8 | 0xE8 | 0xE8 | 0xE8 | 0xE8 | 0xE8 | 0xE8 | 0xE8 | 0xE8 |
| 87 | `RAM_RESET_UTENTE` | 0x66 | 0x66 | 0x66 | 0x66 | 0x66 | 0x66 | 0x66 | 0x66 | 0x66 | 0x66 | 0x66 | 0x66 |
| 88 | `RAM_ACCENDI` | 0x55 | 0x55 | 0x55 | 0x55 | 0x55 | 0x55 | 0x55 | 0x55 | 0x55 | 0x55 | 0x55 | 0x55 |
| 89 | `RAM_SPEGNI` | 0xAA | 0xAA | 0xAA | 0xAA | 0xAA | 0xAA | 0xAA | 0xAA | 0xAA | 0xAA | 0xAA | 0xAA |
| 90 | `RAM_T_FUMI_ADDR` | 0x02 | 0x02 | 0x02 | 0x02 | 0x02 | 0x02 | 0x02 | 0x02 | 0x02 | 0x02 | 0x02 | 0x02 |
| 91 | `RAM_POT_REALE_ADDR` | 0x34 | 0x34 | 0x34 | 0x34 | 0x34 | 0x34 | 0x34 | 0x34 | 0x34 | 0x34 | 0x34 | 0x34 |
| 92 | `RAM_BULBO_ADDR` | 0x19 |  |  |  |  |  |  |  |  |  |  |  |
| 93 | `RAM_SBLOCCO_ADDR` | 0x06 | 0x06 | 0x06 | 0x06 | 0x06 | 0x06 | 0x06 | 0x06 | 0x06 | 0x06 | 0x06 | 0x06 |
| 94 | `RAM_T_CAMERA_ADDR` | 0x340 |  |  |  |  |  |  |  |  | 0xC0 |  |  |
| 95 | `RAM_T_PUFFER_SUP_ADDR` | 0xE0 |  |  |  |  | 0xE0 | 0xE0 |  |  |  |  |  |
| 96 | `RAM_T_PUFFER_INF_ADDR` | 0xE2 |  |  |  |  | 0xE2 | 0xE2 |  |  |  |  |  |
| 97 | `RAM_T_BOILER_ADDR` | 0xDF |  |  |  |  | 0xDF | 0xDF |  |  |  |  |  |
| 98 | `RAM_T_H20_RIT_ADDR` | 0x6C |  |  |  |  | 0x6C | 0x6C |  |  |  |  |  |
| 99 | `RAM_CAUSA_STATO7_ADDR` | 0xC1 |  |  | 0x75 | 0x75 | 0x75 |  |  | 0x75 |  |  |  |
| 100 | `RAM_MOD_ADDR` | 0xFC | 0xA5 |  | 0x73 | 0x73 | 0xFC |  | 0xA5 | 0x73 | 0x73 | 0xA5 |  |
| 101 | `RAM_SERBATORIO_VUOTO_ADDR` |  |  |  | 0xB2 | 0xB2 |  |  |  | 0xB2 |  |  |  |
