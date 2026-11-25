# Registres par modèle de poêle Extraflame

Pour chaque type de poêle : les modèles qui en relèvent, puis seulement les registres **propres à ce type**. Les registres identiques pour tous les types sont donnés une fois, au début.

Sources, toutes lues telles quelles :
- les adresses, les bornes et les codes d'alarme viennent du firmware du module Wi-Fi Black Label v1.8 (voir [REGISTRES.md](REGISTRES.md) pour la carte brute des 12 types) ;
- le type de chaque code de modèle vient de la table du même firmware ([MODELES.md](MODELES.md)) ;
- les **noms commerciaux** viennent du tarif export La Nordica-Extraflame 1.2023, dont les codes d'article à 7 chiffres sont le milieu des codes de modèle à 12 chiffres (`0012750020xx` = article `1275002`, Teodora Evo). Ce tarif nomme 81 des 124 articles. Six autres (Dahiana, Dahiana Plus) viennent de la liste « valable aussi pour » de leur notice, et un (Debby CX) du catalogue 2025. Vingt-sept sont **probables** : leur code est dans la même série qu'un modèle nommé, d'une autre couleur ou d'une autre version, et leur type concorde. Cette déduction est à confirmer, elle s'est déjà trompée une fois. Neuf restent sans nom : ils ne sont ni dans le tarif 2023 ni dans le catalogue 2025, ce sont donc sans doute des modèles sortis du catalogue avant 2023.

Seules les lignes de la Teodora Evo (type `I_VENT`) marquées dans REGISTRES.md ont été vérifiées sur un poêle. Tout le reste est relevé, non vérifié.

Lecture : `loc 0x00` pour la RAM, `0x20` pour l'EEPROM ; écriture : `0x80` pour la RAM, `0xA0` pour l'EEPROM.

## Registres communs à tous les types

| Banque | Adresse | Nom Extraflame | Bornes |
|---|---|---|---|
| EEPROM | `0x4D` | `SET_CHRONO1_START` | 0 à 144 |
| EEPROM | `0x4E` | `SET_CHRONO1_STOP` | 0 à 144 |
| EEPROM | `0x4F` | `SET_CHRONO1_DAY1` | 0 à 1 |
| EEPROM | `0x50` | `SET_CHRONO1_DAY2` | 0 à 1 |
| EEPROM | `0x51` | `SET_CHRONO1_DAY3` | 0 à 1 |
| EEPROM | `0x52` | `SET_CHRONO1_DAY4` | 0 à 1 |
| EEPROM | `0x53` | `SET_CHRONO1_DAY5` | 0 à 1 |
| EEPROM | `0x54` | `SET_CHRONO1_DAY6` | 0 à 1 |
| EEPROM | `0x55` | `SET_CHRONO1_DAY7` | 0 à 1 |
| EEPROM | `0x56` | `SET_CHRONO1_TEMP` | selon le type |
| EEPROM | `0x57` | `SET_CHRONO2_START` | 0 à 144 |
| EEPROM | `0x58` | `SET_CHRONO2_STOP` | 0 à 144 |
| EEPROM | `0x59` | `SET_CHRONO2_DAY1` | 0 à 1 |
| EEPROM | `0x5A` | `SET_CHRONO2_DAY2` | 0 à 1 |
| EEPROM | `0x5B` | `SET_CHRONO2_DAY3` | 0 à 1 |
| EEPROM | `0x5C` | `SET_CHRONO2_DAY4` | 0 à 1 |
| EEPROM | `0x5D` | `SET_CHRONO2_DAY5` | 0 à 1 |
| EEPROM | `0x5E` | `SET_CHRONO2_DAY6` | 0 à 1 |
| EEPROM | `0x5F` | `SET_CHRONO2_DAY7` | 0 à 1 |
| EEPROM | `0x60` | `SET_CHRONO2_TEMP` | selon le type |
| EEPROM | `0x61` | `SET_CHRONO3_START` | 0 à 144 |
| EEPROM | `0x62` | `SET_CHRONO3_STOP` | 0 à 144 |
| EEPROM | `0x63` | `SET_CHRONO3_DAY1` | 0 à 1 |
| EEPROM | `0x64` | `SET_CHRONO3_DAY2` | 0 à 1 |
| EEPROM | `0x65` | `SET_CHRONO3_DAY3` | 0 à 1 |
| EEPROM | `0x66` | `SET_CHRONO3_DAY4` | 0 à 1 |
| EEPROM | `0x67` | `SET_CHRONO3_DAY5` | 0 à 1 |
| EEPROM | `0x68` | `SET_CHRONO3_DAY6` | 0 à 1 |
| EEPROM | `0x69` | `SET_CHRONO3_DAY7` | 0 à 1 |
| EEPROM | `0x6A` | `SET_CHRONO3_TEMP` | selon le type |
| EEPROM | `0x6B` | `SET_CHRONO4_START` | 0 à 144 |
| EEPROM | `0x6C` | `SET_CHRONO4_STOP` | 0 à 144 |
| EEPROM | `0x6D` | `SET_CHRONO4_DAY1` | 0 à 1 |
| EEPROM | `0x6E` | `SET_CHRONO4_DAY2` | 0 à 1 |
| EEPROM | `0x6F` | `SET_CHRONO4_DAY3` | 0 à 1 |
| EEPROM | `0x70` | `SET_CHRONO4_DAY4` | 0 à 1 |
| EEPROM | `0x71` | `SET_CHRONO4_DAY5` | 0 à 1 |
| EEPROM | `0x72` | `SET_CHRONO4_DAY6` | 0 à 1 |
| EEPROM | `0x73` | `SET_CHRONO4_DAY7` | 0 à 1 |
| EEPROM | `0x74` | `SET_CHRONO4_TEMP` | selon le type |
| EEPROM | `0xF8` | `SET_TIME_DAY` | 1 à 7 |
| EEPROM | `0xF9` | `SET_TIME_HOURS` | 0 à 255 |
| EEPROM | `0xFA` | `SET_TIME_MINUTES` | 0 à 255 |
| EEPROM | `0xFB` | `SET_TIME_DATE` | 0 à 255 |
| EEPROM | `0xFC` | `SET_TIME_MONTH` | 0 à 255 |
| EEPROM | `0xFD` | `SET_TIME_YEAR` | 0 à 255 |
| RAM | `0x21` | `RAM_STOVE_STATUS` |  |
| RAM | `0x33` | `RAM_ALLARM` |  |
| RAM | `0xE8` | `RAM_STATO_GESTITO` |  |
| RAM | `0x66` | `RAM_RESET_UTENTE` |  |
| RAM | `0x55` | `RAM_ACCENDI` |  |
| RAM | `0xAA` | `RAM_SPEGNI` |  |
| RAM | `0x02` | `RAM_T_FUMI` |  |
| RAM | `0x34` | `RAM_POT_REALE` |  |
| RAM | `0x06` | `RAM_SBLOCCO` |  |

Codes d'alarme communs (registre `RAM_ALLARM`) : `01` SONDA_FUMI_BIT, `02` HOT_FUMI_BIT, `03` SONDA_FUMI_CORTO_BIT, `04` ASPIRATORE_GUASTO_BIT, `08` MANCATA_ACCENSIONE_BIT, `10` MANCATA_FIAMMA_BIT, `20` ALL_DEPR_BIT, `FF` ALLARME_ACCENSIONE_BLACKOUT_BIT.

## `I_IDRO` : hydro (poêle à eau)

**Modèles** : RAFFAELLA IDRO H15, RAFFAELLA IDRO H18, ROSANNA IDRO.

| Banque | Adresse | Nom Extraflame | Bornes |
|---|---|---|---|
| EEPROM | `0x45` | `SET_POWER` | 1 à 5 |
| EEPROM | `0x30` | `SET_AMB` | 6 à 38 |
| EEPROM | `0x31` | `SET_TEMP` | 65 à 80 |
| EEPROM | `0x3F` | `SET_TANG_ENABLE` | 0 à 1 |
| EEPROM | `0x40` | `SET_TANG_VEL` | 7 à 11 |
| EEPROM | `0xB9` | `SET_CHRONO_ENABLE1` | 0 à 1 |
| EEPROM | `0xBA` | `SET_CHRONO_ENABLE2` | 0 à 1 |
| EEPROM | `0xBB` | `SET_CHRONO_ENABLE3` | 0 à 1 |
| EEPROM | `0xBC` | `SET_CHRONO_ENABLE4` | 0 à 1 |
| EEPROM | `0x48` | `SET_CHRONO1_POWER` | 1 à 5 |
| EEPROM | `0x49` | `SET_CHRONO2_POWER` | 1 à 5 |
| EEPROM | `0x75` | `SET_CHRONO3_POWER` | 1 à 5 |
| EEPROM | `0xB7` | `SET_CHRONO4_POWER` | 1 à 5 |
| EEPROM | `0x1D1` | `COUNTERS_H_1_MSB` |  |
| EEPROM | `0x1D0` | `COUNTERS_H_1_LSB` |  |
| EEPROM | `0x1D3` | `COUNTERS_H_2_MSB` |  |
| EEPROM | `0x1D2` | `COUNTERS_H_2_LSB` |  |
| EEPROM | `0x1D5` | `COUNTERS_H_3_MSB` |  |
| EEPROM | `0x1D4` | `COUNTERS_H_3_LSB` |  |
| EEPROM | `0x1D7` | `COUNTERS_H_4_MSB` |  |
| EEPROM | `0x1D6` | `COUNTERS_H_4_LSB` |  |
| EEPROM | `0x1D9` | `COUNTERS_H_5_MSB` |  |
| EEPROM | `0x1D8` | `COUNTERS_H_5_LSB` |  |
| EEPROM | `0x1EB` | `COUNTERS_H_TOT_MSB` |  |
| EEPROM | `0x1EA` | `COUNTERS_H_TOT_LSB` |  |
| EEPROM | `0x1EF` | `COUNTERS_STARTS_MSB` |  |
| EEPROM | `0x1EE` | `COUNTERS_STARTS_LSB` |  |
| RAM | `0x01` | `RAM_TH20` |  |
| RAM | `0xA6` | `RAM_TAMB` |  |
| RAM | `0xE0` | `RAM_T_PUFFER_SUP` |  |
| RAM | `0xE2` | `RAM_T_PUFFER_INF` |  |
| RAM | `0xDF` | `RAM_T_BOILER` |  |
| RAM | `0x6C` | `RAM_T_H20_RIT` |  |
| RAM | `0x75` | `RAM_CAUSA_STATO7` |  |
| RAM | `0xFC` | `RAM_MOD` |  |

Bornes des registres communs pour ce type : `65 à 80` pour `SET_CHRONO1_TEMP`, `65 à 80` pour `SET_CHRONO2_TEMP`, `65 à 80` pour `SET_CHRONO3_TEMP`, `65 à 80` pour `SET_CHRONO4_TEMP`.

Alarmes propres : `81` SONDA_H20_BIT, `C9` ALLARME_COMANDO_COCLEA_BIT, `88` ALLARME_PRESSIONE_H20_MIN_BIT, `90` SONDA_BOILER_BIT, `A0` SONDA_PUFFER_BIT, `C2` PWM_INTERFACCIA_BIT, `C3` PWM_CALDO_BIT, `C4` PWM_STOP_BIT, `C5` PWM_STOP2_BIT, `C6` PWM_BLOCCO_BIT, `C7` PWM_FLUSSO_BIT, `98` ALLARME_PRESSIONE_H20_MAX_BIT, `82` ALLARME_SOVRATEMPERATURA_H2O_BIT.

## `I_IDRO_2` : hydro, variante 2

**Modèles** : FIANDRA IDRO EVO, GUENDA IDRO.

| Banque | Adresse | Nom Extraflame | Bornes |
|---|---|---|---|
| EEPROM | `0x45` | `SET_POWER` | 1 à 5 |
| EEPROM | `0x30` | `SET_AMB` | 6 à 40 |
| EEPROM | `0x31` | `SET_TEMP` | 65 à 80 |
| EEPROM | `0x3F` | `SET_TANG_ENABLE` | 0 à 1 |
| EEPROM | `0x40` | `SET_TANG_VEL` | 7 à 11 |
| EEPROM | `0xB8` | `SET_CHRONO_ENABLE` | 0 à 1 |
| EEPROM | `0xB9` | `SET_CHRONO_ENABLE1` | 0 à 1 |
| EEPROM | `0xBA` | `SET_CHRONO_ENABLE2` | 0 à 1 |
| EEPROM | `0xBB` | `SET_CHRONO_ENABLE3` | 0 à 1 |
| EEPROM | `0xBC` | `SET_CHRONO_ENABLE4` | 0 à 1 |
| EEPROM | `0xD4` | `SET_CHRONO1_POWER` | 1 à 5 |
| EEPROM | `0xD5` | `SET_CHRONO2_POWER` | 1 à 5 |
| EEPROM | `0xD6` | `SET_CHRONO3_POWER` | 1 à 5 |
| EEPROM | `0xD7` | `SET_CHRONO4_POWER` | 1 à 5 |
| EEPROM | `0xD1` | `COUNTERS_H_1_MSB` |  |
| EEPROM | `0xD0` | `COUNTERS_H_1_LSB` |  |
| EEPROM | `0xD3` | `COUNTERS_H_2_MSB` |  |
| EEPROM | `0xD2` | `COUNTERS_H_2_LSB` |  |
| EEPROM | `0xD5` | `COUNTERS_H_3_MSB` |  |
| EEPROM | `0xD4` | `COUNTERS_H_3_LSB` |  |
| EEPROM | `0xD7` | `COUNTERS_H_4_MSB` |  |
| EEPROM | `0xD6` | `COUNTERS_H_4_LSB` |  |
| EEPROM | `0xD9` | `COUNTERS_H_5_MSB` |  |
| EEPROM | `0xD8` | `COUNTERS_H_5_LSB` |  |
| EEPROM | `0x1EB` | `COUNTERS_H_TOT_MSB` |  |
| EEPROM | `0x1EA` | `COUNTERS_H_TOT_LSB` |  |
| EEPROM | `0x1EF` | `COUNTERS_STARTS_MSB` |  |
| EEPROM | `0x1EE` | `COUNTERS_STARTS_LSB` |  |
| RAM | `0x01` | `RAM_TH20` |  |
| RAM | `0xA6` | `RAM_TAMB` |  |
| RAM | `0xE0` | `RAM_T_PUFFER_SUP` |  |
| RAM | `0xE2` | `RAM_T_PUFFER_INF` |  |
| RAM | `0xDF` | `RAM_T_BOILER` |  |
| RAM | `0x6C` | `RAM_T_H20_RIT` |  |

Bornes des registres communs pour ce type : `65 à 80` pour `SET_CHRONO1_TEMP`, `65 à 80` pour `SET_CHRONO2_TEMP`, `65 à 80` pour `SET_CHRONO3_TEMP`, `65 à 80` pour `SET_CHRONO4_TEMP`.

Alarmes propres : `81` SONDA_H20_BIT, `C9` ALLARME_COMANDO_COCLEA_BIT, `88` ALLARME_PRESSIONE_H20_MIN_BIT, `90` SONDA_BOILER_BIT, `A0` SONDA_PUFFER_BIT, `C2` PWM_INTERFACCIA_BIT, `C3` PWM_CALDO_BIT, `C4` PWM_STOP_BIT, `C5` PWM_STOP2_BIT, `C6` PWM_BLOCCO_BIT, `C7` PWM_FLUSSO_BIT, `98` ALLARME_PRESSIONE_H20_MAX_BIT, `82` ALLARME_SOVRATEMPERATURA_H2O_BIT, `84` GUASTO_BOTOLA_BIT, `C1` CORRENTE_MAX_BIT.

## `I_VENT` : ventilé

**Modèles** : AMIKA, ANGELA EVO, ANNABELLA AD EVO, DAHIANA, DEBBY, DEBBY CX, GIUSY EVO 2.0, KETTY EVO 2.0, KLAUDIA, MOIRA EVO, PAMELA STEEL, SABRY, SERAFINA LUX EVO, SERAFINA PETRA EVO, SOUVENIR LUX EVO, SOUVENIR PETRA EVO, SOUVENIR STEEL EVO, TEODORA EVO, TEOREMA.

Probables, par leur série de codes : DEBBY ou DEBBY CX (articles `1283601`, `1283602`, `1283606` à `1283608`), PAMELA STEEL ou PAMELA CRYSTAL.

Articles sans nom trouvé : `1284700`, `1284701`.

| Banque | Adresse | Nom Extraflame | Bornes |
|---|---|---|---|
| EEPROM | `0x7F` | `SET_POWER` | 1 à 5 |
| EEPROM | `0x7D` | `SET_AMB` | 6 à 38 |
| EEPROM | `0x44` | `SET_TANG_VEL` | 0 à 2 |
| EEPROM | `0xAF` | `SET_CHRONO_ENABLE1` | 0 à 1 |
| EEPROM | `0xB0` | `SET_CHRONO_ENABLE2` | 0 à 1 |
| EEPROM | `0xB1` | `SET_CHRONO_ENABLE3` | 0 à 1 |
| EEPROM | `0xB2` | `SET_CHRONO_ENABLE4` | 0 à 1 |
| EEPROM | `0x8E` | `SET_CHRONO1_POWER` | 1 à 5 |
| EEPROM | `0x8F` | `SET_CHRONO2_POWER` | 1 à 5 |
| EEPROM | `0x90` | `SET_CHRONO3_POWER` | 1 à 5 |
| EEPROM | `0x91` | `SET_CHRONO4_POWER` | 1 à 5 |
| EEPROM | `0xD1` | `COUNTERS_H_1_MSB` |  |
| EEPROM | `0xD0` | `COUNTERS_H_1_LSB` |  |
| EEPROM | `0xD3` | `COUNTERS_H_2_MSB` |  |
| EEPROM | `0xD2` | `COUNTERS_H_2_LSB` |  |
| EEPROM | `0xD5` | `COUNTERS_H_3_MSB` |  |
| EEPROM | `0xD4` | `COUNTERS_H_3_LSB` |  |
| EEPROM | `0xD7` | `COUNTERS_H_4_MSB` |  |
| EEPROM | `0xD6` | `COUNTERS_H_4_LSB` |  |
| EEPROM | `0xD9` | `COUNTERS_H_5_MSB` |  |
| EEPROM | `0xD8` | `COUNTERS_H_5_LSB` |  |
| EEPROM | `0xEB` | `COUNTERS_H_TOT_MSB` |  |
| EEPROM | `0xEA` | `COUNTERS_H_TOT_LSB` |  |
| EEPROM | `0xEF` | `COUNTERS_STARTS_MSB` |  |
| EEPROM | `0xEE` | `COUNTERS_STARTS_LSB` |  |
| RAM | `0x01` | `RAM_TAMB` |  |
| RAM | `0xA5` | `RAM_MOD` |  |

Bornes des registres communs pour ce type : `6 à 38` pour `SET_CHRONO1_TEMP`, `6 à 38` pour `SET_CHRONO2_TEMP`, `6 à 38` pour `SET_CHRONO3_TEMP`, `6 à 38` pour `SET_CHRONO4_TEMP`.

Alarmes propres : `82` ALLARME_COMANDO_COCLEA_BIT, `81` BLOCCO_COCLEA_BIT.

## `I_VENT_2` : ventilé, variante 2

**Modèles** : COMFORT P70 AIR, COMFORT P85.

Articles sans nom trouvé : `1284400`.

| Banque | Adresse | Nom Extraflame | Bornes |
|---|---|---|---|
| EEPROM | `0x7F` | `SET_POWER` | 1 à 5 |
| EEPROM | `0x7D` | `SET_AMB` | 6 à 38 |
| EEPROM | `0x44` | `SET_TANG_VEL` | 0 à 2 |
| EEPROM | `0xAF` | `SET_CHRONO_ENABLE1` | 0 à 1 |
| EEPROM | `0xB0` | `SET_CHRONO_ENABLE2` | 0 à 1 |
| EEPROM | `0xB1` | `SET_CHRONO_ENABLE3` | 0 à 1 |
| EEPROM | `0xB2` | `SET_CHRONO_ENABLE4` | 0 à 1 |
| EEPROM | `0x9E` | `SET_CHRONO1_POWER` | 1 à 5 |
| EEPROM | `0x9F` | `SET_CHRONO2_POWER` | 1 à 5 |
| EEPROM | `0xA0` | `SET_CHRONO3_POWER` | 1 à 5 |
| EEPROM | `0xA1` | `SET_CHRONO4_POWER` | 1 à 5 |
| EEPROM | `0xC6` | `SET_CHECKPELLET_ENABLED` | 0 à 1 |
| EEPROM | `0xD1` | `COUNTERS_H_1_MSB` |  |
| EEPROM | `0xD0` | `COUNTERS_H_1_LSB` |  |
| EEPROM | `0xD3` | `COUNTERS_H_2_MSB` |  |
| EEPROM | `0xD2` | `COUNTERS_H_2_LSB` |  |
| EEPROM | `0xD5` | `COUNTERS_H_3_MSB` |  |
| EEPROM | `0xD4` | `COUNTERS_H_3_LSB` |  |
| EEPROM | `0xD7` | `COUNTERS_H_4_MSB` |  |
| EEPROM | `0xD6` | `COUNTERS_H_4_LSB` |  |
| EEPROM | `0xD9` | `COUNTERS_H_5_MSB` |  |
| EEPROM | `0xD8` | `COUNTERS_H_5_LSB` |  |
| EEPROM | `0x1EB` | `COUNTERS_H_TOT_MSB` |  |
| EEPROM | `0x1EA` | `COUNTERS_H_TOT_LSB` |  |
| EEPROM | `0x1EF` | `COUNTERS_STARTS_MSB` |  |
| EEPROM | `0x1EE` | `COUNTERS_STARTS_LSB` |  |
| RAM | `0x01` | `RAM_TAMB` |  |
| RAM | `0x75` | `RAM_CAUSA_STATO7` |  |
| RAM | `0x73` | `RAM_MOD` |  |
| RAM | `0xB2` | `RAM_SERBATORIO_VUOTO` |  |

Bornes des registres communs pour ce type : `6 à 38` pour `SET_CHRONO1_TEMP`, `6 à 38` pour `SET_CHRONO2_TEMP`, `6 à 38` pour `SET_CHRONO3_TEMP`, `6 à 38` pour `SET_CHRONO4_TEMP`.

Alarmes propres : `82` ALLARME_COMANDO_COCLEA_BIT.

## `I_VENT_3` : ventilé, variante 3

**Modèles** : MIETTA EVO, SINFONY.

| Banque | Adresse | Nom Extraflame | Bornes |
|---|---|---|---|
| EEPROM | `0x7F` | `SET_POWER` | 1 à 5 |
| EEPROM | `0x7D` | `SET_AMB` | 6 à 38 |
| EEPROM | `0x44` | `SET_TANG_VEL` | 0 à 2 |
| EEPROM | `0xAB` | `SET_CAN1_VEL` |  |
| EEPROM | `0x7E` | `SET_CAN1_TEMP` |  |
| EEPROM | `0xAF` | `SET_CHRONO_ENABLE1` | 0 à 1 |
| EEPROM | `0xB0` | `SET_CHRONO_ENABLE2` | 0 à 1 |
| EEPROM | `0xB1` | `SET_CHRONO_ENABLE3` | 0 à 1 |
| EEPROM | `0xB2` | `SET_CHRONO_ENABLE4` | 0 à 1 |
| EEPROM | `0x9E` | `SET_CHRONO1_POWER` | 1 à 5 |
| EEPROM | `0x9F` | `SET_CHRONO2_POWER` | 1 à 5 |
| EEPROM | `0xA0` | `SET_CHRONO3_POWER` | 1 à 5 |
| EEPROM | `0xA1` | `SET_CHRONO4_POWER` | 1 à 5 |
| EEPROM | `0xD1` | `COUNTERS_H_1_MSB` |  |
| EEPROM | `0xD0` | `COUNTERS_H_1_LSB` |  |
| EEPROM | `0xD3` | `COUNTERS_H_2_MSB` |  |
| EEPROM | `0xD2` | `COUNTERS_H_2_LSB` |  |
| EEPROM | `0xD5` | `COUNTERS_H_3_MSB` |  |
| EEPROM | `0xD4` | `COUNTERS_H_3_LSB` |  |
| EEPROM | `0xD7` | `COUNTERS_H_4_MSB` |  |
| EEPROM | `0xD6` | `COUNTERS_H_4_LSB` |  |
| EEPROM | `0xD9` | `COUNTERS_H_5_MSB` |  |
| EEPROM | `0xD8` | `COUNTERS_H_5_LSB` |  |
| EEPROM | `0x1EB` | `COUNTERS_H_TOT_MSB` |  |
| EEPROM | `0x1EA` | `COUNTERS_H_TOT_LSB` |  |
| EEPROM | `0x1EF` | `COUNTERS_STARTS_MSB` |  |
| EEPROM | `0x1EE` | `COUNTERS_STARTS_LSB` |  |
| RAM | `0x01` | `RAM_TAMB` |  |
| RAM | `0xC0` | `RAM_T_CAMERA` |  |
| RAM | `0x73` | `RAM_MOD` |  |

Bornes des registres communs pour ce type : `6 à 38` pour `SET_CHRONO1_TEMP`, `6 à 38` pour `SET_CHRONO2_TEMP`, `6 à 38` pour `SET_CHRONO3_TEMP`, `6 à 38` pour `SET_CHRONO4_TEMP`.

Alarmes propres : `C0` ALLARME_COMANDO_COCLEA_BIT, `84` GUASTO_BOTOLA_BIT, `A0` BLOCCO_COCLEA_BIT, `CD` SONDA_CAMERA_BIT, `88` CORRENTE_MAX_BIT.

## `I_VENT_4` : ventilé, variante 4

**Modèles** : aucun modèle nommé.

Aucun code de modèle de la table ne donne ce type.

| Banque | Adresse | Nom Extraflame | Bornes |
|---|---|---|---|
| EEPROM | `0x7F` | `SET_POWER` | 1 à 5 |
| EEPROM | `0x7D` | `SET_AMB` | 6 à 38 |
| EEPROM | `0x44` | `SET_TANG_VEL` | 0 à 2 |
| EEPROM | `0xAF` | `SET_CHRONO_ENABLE1` | 0 à 1 |
| EEPROM | `0xB0` | `SET_CHRONO_ENABLE2` | 0 à 1 |
| EEPROM | `0xB1` | `SET_CHRONO_ENABLE3` | 0 à 1 |
| EEPROM | `0xB2` | `SET_CHRONO_ENABLE4` | 0 à 1 |
| EEPROM | `0x8E` | `SET_CHRONO1_POWER` | 1 à 5 |
| EEPROM | `0x8F` | `SET_CHRONO2_POWER` | 1 à 5 |
| EEPROM | `0x90` | `SET_CHRONO3_POWER` | 1 à 5 |
| EEPROM | `0x91` | `SET_CHRONO4_POWER` | 1 à 5 |
| EEPROM | `0xD1` | `COUNTERS_H_1_MSB` |  |
| EEPROM | `0xD0` | `COUNTERS_H_1_LSB` |  |
| EEPROM | `0xD3` | `COUNTERS_H_2_MSB` |  |
| EEPROM | `0xD2` | `COUNTERS_H_2_LSB` |  |
| EEPROM | `0xD5` | `COUNTERS_H_3_MSB` |  |
| EEPROM | `0xD4` | `COUNTERS_H_3_LSB` |  |
| EEPROM | `0xD7` | `COUNTERS_H_4_MSB` |  |
| EEPROM | `0xD6` | `COUNTERS_H_4_LSB` |  |
| EEPROM | `0xD9` | `COUNTERS_H_5_MSB` |  |
| EEPROM | `0xD8` | `COUNTERS_H_5_LSB` |  |
| EEPROM | `0xEB` | `COUNTERS_H_TOT_MSB` |  |
| EEPROM | `0xEA` | `COUNTERS_H_TOT_LSB` |  |
| EEPROM | `0xEF` | `COUNTERS_STARTS_MSB` |  |
| EEPROM | `0xEE` | `COUNTERS_STARTS_LSB` |  |
| RAM | `0x01` | `RAM_TAMB` |  |
| RAM | `0xA5` | `RAM_MOD` |  |

Bornes des registres communs pour ce type : `6 à 38` pour `SET_CHRONO1_TEMP`, `6 à 38` pour `SET_CHRONO2_TEMP`, `6 à 38` pour `SET_CHRONO3_TEMP`, `6 à 38` pour `SET_CHRONO4_TEMP`.

Alarmes propres : `82` ALLARME_COMANDO_COCLEA_BIT, `81` BLOCCO_COCLEA_BIT.

## `I_VENT_5` : ventilé, variante 5

Probables, par leur série de codes : MIETTA EVO.

| Banque | Adresse | Nom Extraflame | Bornes |
|---|---|---|---|
| EEPROM | `0x7F` | `SET_POWER` | 1 à 5 |
| EEPROM | `0x7D` | `SET_AMB` | 6 à 41 |
| EEPROM | `0x3F` | `SET_TANG_ENABLE` | 0 à 1 |
| EEPROM | `0x40` | `SET_TANG_VEL` | 7 à 11 |
| EEPROM | `0xAE` | `SET_CHRONO_ENABLE` | 0 à 1 |
| EEPROM | `0xAF` | `SET_CHRONO_ENABLE1` | 0 à 1 |
| EEPROM | `0xB0` | `SET_CHRONO_ENABLE2` | 0 à 1 |
| EEPROM | `0xB1` | `SET_CHRONO_ENABLE3` | 0 à 1 |
| EEPROM | `0xB2` | `SET_CHRONO_ENABLE4` | 0 à 1 |
| EEPROM | `0xD1` | `COUNTERS_H_1_MSB` |  |
| EEPROM | `0xD0` | `COUNTERS_H_1_LSB` |  |
| EEPROM | `0xD3` | `COUNTERS_H_2_MSB` |  |
| EEPROM | `0xD2` | `COUNTERS_H_2_LSB` |  |
| EEPROM | `0xD5` | `COUNTERS_H_3_MSB` |  |
| EEPROM | `0xD4` | `COUNTERS_H_3_LSB` |  |
| EEPROM | `0xD7` | `COUNTERS_H_4_MSB` |  |
| EEPROM | `0xD6` | `COUNTERS_H_4_LSB` |  |
| EEPROM | `0xD9` | `COUNTERS_H_5_MSB` |  |
| EEPROM | `0xD8` | `COUNTERS_H_5_LSB` |  |
| EEPROM | `0x1EB` | `COUNTERS_H_TOT_MSB` |  |
| EEPROM | `0x1EA` | `COUNTERS_H_TOT_LSB` |  |
| EEPROM | `0x1EF` | `COUNTERS_STARTS_MSB` |  |
| EEPROM | `0x1EE` | `COUNTERS_STARTS_LSB` |  |
| RAM | `0x01` | `RAM_TAMB` |  |

Bornes des registres communs pour ce type : `6 à 41` pour `SET_CHRONO1_TEMP`, `6 à 41` pour `SET_CHRONO2_TEMP`, `6 à 41` pour `SET_CHRONO3_TEMP`, `6 à 41` pour `SET_CHRONO4_TEMP`.

Alarmes propres : `82` ALLARME_COMANDO_COCLEA_BIT, `84` GUASTO_BOTOLA_BIT, `88` CORRENTE_MAX_BIT.

## `I_CANAL` : canalisé, une canalisation

**Modèles** : ANGELA PLUS EVO, DAHIANA PLUS, GABRIELLA PLUS, GIUSY PLUS EVO 2.0, KLAUDIA PLUS, MARILENA PLUS AD.

Articles sans nom trouvé : `1283100`, `1283101`, `1284200`, `4273107`, `4273108`, `4273111`.

| Banque | Adresse | Nom Extraflame | Bornes |
|---|---|---|---|
| EEPROM | `0x7F` | `SET_POWER` | 1 à 5 |
| EEPROM | `0x7D` | `SET_AMB` | 6 à 38 |
| EEPROM | `0x44` | `SET_TANG_VEL` | 0 à 2 |
| EEPROM | `0xAB` | `SET_CAN1_VEL` | 0 à 3 |
| EEPROM | `0x80` | `SET_CAN1_TEMP` | 6 à 38 |
| EEPROM | `0xAF` | `SET_CHRONO_ENABLE1` | 0 à 1 |
| EEPROM | `0xB0` | `SET_CHRONO_ENABLE2` | 0 à 1 |
| EEPROM | `0xB1` | `SET_CHRONO_ENABLE3` | 0 à 1 |
| EEPROM | `0xB2` | `SET_CHRONO_ENABLE4` | 0 à 1 |
| EEPROM | `0x8E` | `SET_CHRONO1_POWER` | 1 à 5 |
| EEPROM | `0x8F` | `SET_CHRONO2_POWER` | 1 à 5 |
| EEPROM | `0x90` | `SET_CHRONO3_POWER` | 1 à 5 |
| EEPROM | `0x91` | `SET_CHRONO4_POWER` | 1 à 5 |
| EEPROM | `0xD1` | `COUNTERS_H_1_MSB` |  |
| EEPROM | `0xD0` | `COUNTERS_H_1_LSB` |  |
| EEPROM | `0xD3` | `COUNTERS_H_2_MSB` |  |
| EEPROM | `0xD2` | `COUNTERS_H_2_LSB` |  |
| EEPROM | `0xD5` | `COUNTERS_H_3_MSB` |  |
| EEPROM | `0xD4` | `COUNTERS_H_3_LSB` |  |
| EEPROM | `0xD7` | `COUNTERS_H_4_MSB` |  |
| EEPROM | `0xD6` | `COUNTERS_H_4_LSB` |  |
| EEPROM | `0xD9` | `COUNTERS_H_5_MSB` |  |
| EEPROM | `0xD8` | `COUNTERS_H_5_LSB` |  |
| EEPROM | `0xEB` | `COUNTERS_H_TOT_MSB` |  |
| EEPROM | `0xEA` | `COUNTERS_H_TOT_LSB` |  |
| EEPROM | `0xEF` | `COUNTERS_STARTS_MSB` |  |
| EEPROM | `0xEE` | `COUNTERS_STARTS_LSB` |  |
| RAM | `0x01` | `RAM_TAMB` |  |
| RAM | `0xA5` | `RAM_MOD` |  |

Bornes des registres communs pour ce type : `6 à 38` pour `SET_CHRONO1_TEMP`, `6 à 38` pour `SET_CHRONO2_TEMP`, `6 à 38` pour `SET_CHRONO3_TEMP`, `6 à 38` pour `SET_CHRONO4_TEMP`.

Alarmes propres : `82` ALLARME_COMANDO_COCLEA_BIT.

## `I_CANAL_2` : canalisé, variante 2

**Modèles** : TERRY PLUS.

| Banque | Adresse | Nom Extraflame | Bornes |
|---|---|---|---|
| EEPROM | `0x7F` | `SET_POWER` | 1 à 5 |
| EEPROM | `0x7D` | `SET_AMB` | 6 à 38 |
| EEPROM | `0x44` | `SET_TANG_VEL` | 0 à 2 |
| EEPROM | `0xAB` | `SET_CAN1_VEL` | 0 à 3 |
| EEPROM | `0xAC` | `SET_CAN2_VEL` | 0 à 3 |
| EEPROM | `0x80` | `SET_CAN1_TEMP` | 6 à 38 |
| EEPROM | `0x81` | `SET_CAN2_TEMP` | 6 à 38 |
| EEPROM | `0xAF` | `SET_CHRONO_ENABLE1` | 0 à 1 |
| EEPROM | `0xB0` | `SET_CHRONO_ENABLE2` | 0 à 1 |
| EEPROM | `0xB1` | `SET_CHRONO_ENABLE3` | 0 à 1 |
| EEPROM | `0xB2` | `SET_CHRONO_ENABLE4` | 0 à 1 |
| EEPROM | `0x9E` | `SET_CHRONO1_POWER` | 1 à 5 |
| EEPROM | `0x9F` | `SET_CHRONO2_POWER` | 1 à 5 |
| EEPROM | `0xA0` | `SET_CHRONO3_POWER` | 1 à 5 |
| EEPROM | `0xA1` | `SET_CHRONO4_POWER` | 1 à 5 |
| EEPROM | `0xD1` | `COUNTERS_H_1_MSB` |  |
| EEPROM | `0xD0` | `COUNTERS_H_1_LSB` |  |
| EEPROM | `0xD3` | `COUNTERS_H_2_MSB` |  |
| EEPROM | `0xD2` | `COUNTERS_H_2_LSB` |  |
| EEPROM | `0xD5` | `COUNTERS_H_3_MSB` |  |
| EEPROM | `0xD4` | `COUNTERS_H_3_LSB` |  |
| EEPROM | `0xD7` | `COUNTERS_H_4_MSB` |  |
| EEPROM | `0xD6` | `COUNTERS_H_4_LSB` |  |
| EEPROM | `0xD9` | `COUNTERS_H_5_MSB` |  |
| EEPROM | `0xD8` | `COUNTERS_H_5_LSB` |  |
| EEPROM | `0x1EB` | `COUNTERS_H_TOT_MSB` |  |
| EEPROM | `0x1EA` | `COUNTERS_H_TOT_LSB` |  |
| EEPROM | `0x1EF` | `COUNTERS_STARTS_MSB` |  |
| EEPROM | `0x1EE` | `COUNTERS_STARTS_LSB` |  |
| RAM | `0x01` | `RAM_TAMB` |  |

Bornes des registres communs pour ce type : `6 à 38` pour `SET_CHRONO1_TEMP`, `6 à 38` pour `SET_CHRONO2_TEMP`, `6 à 38` pour `SET_CHRONO3_TEMP`, `6 à 38` pour `SET_CHRONO4_TEMP`.

Alarmes propres : `C0` ALLARME_COMANDO_COCLEA_BIT, `84` GUASTO_BOTOLA_BIT, `A0` BLOCCO_COCLEA_BIT, `CD` SONDA_CAMERA_BIT, `88` CORRENTE_MAX_BIT.

## `I_CANAL_3` : canalisé, variante 3

**Modèles** : COMFORT P85 PLUS, TEOREMA PLUS.

Articles sans nom trouvé : `1284550`.

| Banque | Adresse | Nom Extraflame | Bornes |
|---|---|---|---|
| EEPROM | `0x7F` | `SET_POWER` | 1 à 5 |
| EEPROM | `0x7D` | `SET_AMB` | 6 à 38 |
| EEPROM | `0x44` | `SET_TANG_VEL` | 0 à 2 |
| EEPROM | `0xAB` | `SET_CAN1_VEL` | 0 à 3 |
| EEPROM | `0xAC` | `SET_CAN2_VEL` | 0 à 3 |
| EEPROM | `0x80` | `SET_CAN1_TEMP` | 6 à 38 |
| EEPROM | `0x81` | `SET_CAN2_TEMP` | 6 à 38 |
| EEPROM | `0xAF` | `SET_CHRONO_ENABLE1` | 0 à 1 |
| EEPROM | `0xB0` | `SET_CHRONO_ENABLE2` | 0 à 1 |
| EEPROM | `0xB1` | `SET_CHRONO_ENABLE3` | 0 à 1 |
| EEPROM | `0xB2` | `SET_CHRONO_ENABLE4` | 0 à 1 |
| EEPROM | `0x9E` | `SET_CHRONO1_POWER` | 1 à 5 |
| EEPROM | `0x9F` | `SET_CHRONO2_POWER` | 1 à 5 |
| EEPROM | `0xA0` | `SET_CHRONO3_POWER` | 1 à 5 |
| EEPROM | `0xA1` | `SET_CHRONO4_POWER` | 1 à 5 |
| EEPROM | `0xC6` | `SET_CHECKPELLET_ENABLED` | 0 à 1 |
| EEPROM | `0xD1` | `COUNTERS_H_1_MSB` |  |
| EEPROM | `0xD0` | `COUNTERS_H_1_LSB` |  |
| EEPROM | `0xD3` | `COUNTERS_H_2_MSB` |  |
| EEPROM | `0xD2` | `COUNTERS_H_2_LSB` |  |
| EEPROM | `0xD5` | `COUNTERS_H_3_MSB` |  |
| EEPROM | `0xD4` | `COUNTERS_H_3_LSB` |  |
| EEPROM | `0xD7` | `COUNTERS_H_4_MSB` |  |
| EEPROM | `0xD6` | `COUNTERS_H_4_LSB` |  |
| EEPROM | `0xD9` | `COUNTERS_H_5_MSB` |  |
| EEPROM | `0xD8` | `COUNTERS_H_5_LSB` |  |
| EEPROM | `0x1EB` | `COUNTERS_H_TOT_MSB` |  |
| EEPROM | `0x1EA` | `COUNTERS_H_TOT_LSB` |  |
| EEPROM | `0x1EF` | `COUNTERS_STARTS_MSB` |  |
| EEPROM | `0x1EE` | `COUNTERS_STARTS_LSB` |  |
| RAM | `0x01` | `RAM_TAMB` |  |
| RAM | `0x75` | `RAM_CAUSA_STATO7` |  |
| RAM | `0x73` | `RAM_MOD` |  |
| RAM | `0xB2` | `RAM_SERBATORIO_VUOTO` |  |

Bornes des registres communs pour ce type : `6 à 38` pour `SET_CHRONO1_TEMP`, `6 à 38` pour `SET_CHRONO2_TEMP`, `6 à 38` pour `SET_CHRONO3_TEMP`, `6 à 38` pour `SET_CHRONO4_TEMP`.

Alarmes propres : `82` ALLARME_COMANDO_COCLEA_BIT.

## `I_CANAL_4` : canalisé, variante 4

**Modèles** : COMFORT P70 AIR PLUS.

| Banque | Adresse | Nom Extraflame | Bornes |
|---|---|---|---|
| EEPROM | `0x7F` | `SET_POWER` | 1 à 5 |
| EEPROM | `0x7D` | `SET_AMB` | 6 à 38 |
| EEPROM | `0x44` | `SET_TANG_VEL` | 0 à 2 |
| EEPROM | `0xAB` | `SET_CAN1_VEL` | 0 à 3 |
| EEPROM | `0x80` | `SET_CAN1_TEMP` | 6 à 38 |
| EEPROM | `0xAF` | `SET_CHRONO_ENABLE1` | 0 à 1 |
| EEPROM | `0xB0` | `SET_CHRONO_ENABLE2` | 0 à 1 |
| EEPROM | `0xB1` | `SET_CHRONO_ENABLE3` | 0 à 1 |
| EEPROM | `0xB2` | `SET_CHRONO_ENABLE4` | 0 à 1 |
| EEPROM | `0x9E` | `SET_CHRONO1_POWER` | 1 à 5 |
| EEPROM | `0x9F` | `SET_CHRONO2_POWER` | 1 à 5 |
| EEPROM | `0xA0` | `SET_CHRONO3_POWER` | 1 à 5 |
| EEPROM | `0xA1` | `SET_CHRONO4_POWER` | 1 à 5 |
| EEPROM | `0xC6` | `SET_CHECKPELLET_ENABLED` | 0 à 1 |
| EEPROM | `0xD1` | `COUNTERS_H_1_MSB` |  |
| EEPROM | `0xD0` | `COUNTERS_H_1_LSB` |  |
| EEPROM | `0xD3` | `COUNTERS_H_2_MSB` |  |
| EEPROM | `0xD2` | `COUNTERS_H_2_LSB` |  |
| EEPROM | `0xD5` | `COUNTERS_H_3_MSB` |  |
| EEPROM | `0xD4` | `COUNTERS_H_3_LSB` |  |
| EEPROM | `0xD7` | `COUNTERS_H_4_MSB` |  |
| EEPROM | `0xD6` | `COUNTERS_H_4_LSB` |  |
| EEPROM | `0xD9` | `COUNTERS_H_5_MSB` |  |
| EEPROM | `0xD8` | `COUNTERS_H_5_LSB` |  |
| EEPROM | `0x1EB` | `COUNTERS_H_TOT_MSB` |  |
| EEPROM | `0x1EA` | `COUNTERS_H_TOT_LSB` |  |
| EEPROM | `0x1EF` | `COUNTERS_STARTS_MSB` |  |
| EEPROM | `0x1EE` | `COUNTERS_STARTS_LSB` |  |
| RAM | `0x01` | `RAM_TAMB` |  |
| RAM | `0x75` | `RAM_CAUSA_STATO7` |  |
| RAM | `0x73` | `RAM_MOD` |  |
| RAM | `0xB2` | `RAM_SERBATORIO_VUOTO` |  |

Bornes des registres communs pour ce type : `6 à 38` pour `SET_CHRONO1_TEMP`, `6 à 38` pour `SET_CHRONO2_TEMP`, `6 à 38` pour `SET_CHRONO3_TEMP`, `6 à 38` pour `SET_CHRONO4_TEMP`.

Alarmes propres : `82` ALLARME_COMANDO_COCLEA_BIT.

## `I_CALD` : chaudière

**Modèles** : aucun modèle nommé.

Aucun code de modèle de la table ne donne ce type.

| Banque | Adresse | Nom Extraflame | Bornes |
|---|---|---|---|
| EEPROM | `0x7F` | `SET_POWER` | 1 à 5 |
| EEPROM | `0x7D` | `SET_AMB` |  |
| EEPROM | `0x44` | `SET_TANG_VEL` |  |
| EEPROM | `0xAB` | `SET_CAN1_VEL` |  |
| EEPROM | `0x80` | `SET_CAN1_TEMP` |  |
| EEPROM | `0xAF` | `SET_CHRONO_ENABLE1` | 0 à 1 |
| EEPROM | `0xB0` | `SET_CHRONO_ENABLE2` | 0 à 1 |
| EEPROM | `0xB1` | `SET_CHRONO_ENABLE3` | 0 à 1 |
| EEPROM | `0xB2` | `SET_CHRONO_ENABLE4` | 0 à 1 |
| EEPROM | `0x8E` | `SET_CHRONO1_POWER` | 1 à 5 |
| EEPROM | `0x8F` | `SET_CHRONO2_POWER` | 1 à 5 |
| EEPROM | `0x90` | `SET_CHRONO3_POWER` | 1 à 5 |
| EEPROM | `0x91` | `SET_CHRONO4_POWER` | 1 à 5 |
| EEPROM | `0xD1` | `COUNTERS_H_1_MSB` |  |
| EEPROM | `0xD0` | `COUNTERS_H_1_LSB` |  |
| EEPROM | `0xD3` | `COUNTERS_H_2_MSB` |  |
| EEPROM | `0xD2` | `COUNTERS_H_2_LSB` |  |
| EEPROM | `0xD5` | `COUNTERS_H_3_MSB` |  |
| EEPROM | `0xD4` | `COUNTERS_H_3_LSB` |  |
| EEPROM | `0xD7` | `COUNTERS_H_4_MSB` |  |
| EEPROM | `0xD6` | `COUNTERS_H_4_LSB` |  |
| EEPROM | `0xD9` | `COUNTERS_H_5_MSB` |  |
| EEPROM | `0xD8` | `COUNTERS_H_5_LSB` |  |
| EEPROM | `0xEB` | `COUNTERS_H_TOT_MSB` |  |
| EEPROM | `0xEA` | `COUNTERS_H_TOT_LSB` |  |
| EEPROM | `0xEF` | `COUNTERS_STARTS_MSB` |  |
| EEPROM | `0xEE` | `COUNTERS_STARTS_LSB` |  |
| RAM | `0x01` | `RAM_TH20` |  |
| RAM | `0x19` | `RAM_BULBO` |  |
| RAM | `0x340` | `RAM_T_CAMERA` |  |
| RAM | `0xE0` | `RAM_T_PUFFER_SUP` |  |
| RAM | `0xE2` | `RAM_T_PUFFER_INF` |  |
| RAM | `0xDF` | `RAM_T_BOILER` |  |
| RAM | `0x6C` | `RAM_T_H20_RIT` |  |
| RAM | `0xC1` | `RAM_CAUSA_STATO7` |  |
| RAM | `0xFC` | `RAM_MOD` |  |

Bornes des registres communs pour ce type : `65 à 80` pour `SET_CHRONO1_TEMP`, `65 à 80` pour `SET_CHRONO2_TEMP`, `65 à 80` pour `SET_CHRONO3_TEMP`, `65 à 80` pour `SET_CHRONO4_TEMP`.

Alarmes propres : `82` SONDA_H20_BIT, `C9` ALLARME_COMANDO_COCLEA_BIT, `88` ALLARME_PRESSIONE_H20_MIN_BIT, `90` SONDA_BOILER_BIT, `A0` SONDA_PUFFER_BIT, `C2` PWM_INTERFACCIA_BIT, `C3` PWM_CALDO_BIT, `C4` PWM_STOP_BIT, `C5` PWM_STOP2_BIT, `C6` PWM_BLOCCO_BIT, `C7` PWM_FLUSSO_BIT, `98` ALLARME_PRESSIONE_H20_MAX_BIT, `84` GUASTO_BOTOLA_BIT, `CA` BLOCCO_COCLEA_BIT, `CD` SONDA_CAMERA_BIT, `C1` CORRENTE_MAX_BIT, `F0` BULBO_ON_VALUE.

