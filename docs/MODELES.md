# Codes de modèle Extraflame et type de poêle

Le firmware du module Black Label (v1.8) contient une table de **239 codes de modèle** à 12 chiffres. Pour chaque code, il donne le **type de poêle**, qui choisit le bloc de registres à utiliser (voir [REGISTRES.md](REGISTRES.md)), et trois valeurs par défaut : produit à eau, nombre de ventilateurs tangentiels, nombre de canalisations. Ces trois valeurs peuvent ensuite être remplacées par des valeurs enregistrées dans le module (ses journaux parlent de valeurs « récupérées de l'EEPROM »).

Tout est lu tel quel dans le firmware. Rien n'est vérifié sur un poêle, sauf la ligne de la Teodora Evo.

## Comment le module choisit le type

1. Il lit le code de modèle enregistré dans le module (champ `stove_model`) et le cherche dans la table. Si ce champ est vide ou inconnu, c'est le premier code de la table, le code générique, qui est pris.
2. Le type est celui de la ligne trouvée.
3. Exception : pour le premier code, `009278451000` (l'article `9278451` est le module Black Label lui-même dans le tarif), le type peut être remplacé par une ligne `model:STOVE_TYPE_…` de la table dynamique que le module reçoit (voir « Tables dynamiques » dans [REGISTRES.md](REGISTRES.md)). Sans elle, c'est `I_VENT`.

Le numéro du type est son rang dans cette liste, en partant de 0 (ordre de la table des noms `STOVE_TYPE_*` du firmware) : `I_IDRO`, `I_IDRO_2`, `I_VENT`, `I_VENT_2`, `I_VENT_3`, `I_VENT_4`, `I_VENT_5`, `I_CANAL`, `I_CANAL_2`, `I_CANAL_3`, `I_CANAL_4`, `I_CALD`.

## Répartition

| Type | Modèles |
|---|---|
| `I_IDRO` | 11 |
| `I_IDRO_2` | 10 |
| `I_VENT` | 130 |
| `I_VENT_2` | 8 |
| `I_VENT_3` | 6 |
| `I_VENT_4` | 0 |
| `I_VENT_5` | 1 |
| `I_CANAL` | 49 |
| `I_CANAL_2` | 9 |
| `I_CANAL_3` | 14 |
| `I_CANAL_4` | 1 |
| `I_CALD` | 0 |

Trois types (`I_VENT_4`, `I_VENT_5` hors un modèle, `I_CALD`) n'ont aucun ou presque aucun modèle dans la table : ils ne peuvent être atteints que par l'exception ci-dessus.

## Table

Les noms viennent du tarif export La Nordica-Extraflame 1.2023 (article = chiffres 3 à 9 du code) et de l'outil de compatibilité du fabricant (`compatibility.extraflame.it`), interrogé article par article le 2026-11-25. Un même article peut porter un autre nom selon le pays ou l'année. Vue par type, avec les registres propres à chacun : [POELES.md](POELES.md).

## Audit : ces modèles sont-ils tous « Black Label » ?

Oui. Les outils de compatibilité du groupe (`compatibility.extraflame.it` pour La Nordica-Extraflame, `compatibility.dalzotto.com` pour sa filiale Dal Zotto) connaissent 111 des 123 articles de la table, et répondent pour **les 111** : module blanc non compatible, module noir compatible, module gris compatible. Quatre articles sont des Dal Zotto (Leyla Elite, Inserto 700 Air, Inserto 850 Elite) : le même module noir sert donc les deux marques. Les 12 autres articles sont absents des deux bases (colonnes « ? »). La table du firmware est donc bien la liste des poêles du module noir.

Trois enseignements de plus, tirés d'un sondage de 40 modèles du tarif 2023 absents de la table :

- **Le module gris couvre plus large.** Tous les poêles du module noir l'acceptent, mais aussi des poêles du module blanc (Luisella, Virna Idro, Comfort Idro L80) et des modèles récents que le noir ne couvre pas (Noris, Mirka, Marina Idro, Debby Plus Evo, Lina Top).
- **Les poêles du module blanc ne sont pas dans la table** et ne sont pas donnés compatibles avec le noir : ce n'est pas le même firmware avec un autre boîtier.
- **Quelques poêles donnés compatibles avec le noir manquent dans la table** de ce firmware de décembre 2022 (Dahiana VFS, Dahiana Plus VFS, Iside Idro H15, Pamela Crystal dans une finition, Marilena Plus AD Crystal) : ils ont pu être ajoutés par une mise à jour du module, ou passer par le code générique.

Colonnes : eau (0 = poêle à air), ventilateurs tangentiels, canalisations. Les valeurs 10, 11 et 12 sont recopiées telles quelles, leur sens n'est pas établi.

| Code de modèle | Modèle | Type | Eau | Tangentiels | Canalisations | Module noir | Module gris |
|---|---|---|---|---|---|---|---|
| `009278451000` | module Wi-Fi Black Label (code générique) | `I_VENT` | 0 |  | 0 |  |  |
| `001283000000` | MARILENA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001283001000` | MARILENA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001283002000` | MARILENA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001283500000` | AMIKA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283501000` | AMIKA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283502000` | AMIKA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283503000` | AMIKA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283600000` | DEBBY CX | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283601000` | DEBBY CX | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283602000` | DEBBY CX | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283100000` | LEYLA ELITE (Dal Zotto) | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001283101000` | LEYLA ELITE (Dal Zotto) | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001282800000` | TERRY PLUS | `I_CANAL_2` | 0 | 2 | 2 | oui | oui |
| `001282801000` | TERRY PLUS | `I_CANAL_2` | 0 | 2 | 2 | oui | oui |
| `001282801001` | TERRY PLUS | `I_CANAL_2` | 0 | 2 | 2 | oui | oui |
| `001282800001` | TERRY PLUS | `I_CANAL_2` | 0 | 2 | 2 | oui | oui |
| `001282801002` | TERRY PLUS | `I_CANAL_2` | 0 | 2 | 2 | oui | oui |
| `001282800002` | TERRY PLUS | `I_CANAL_2` | 0 | 2 | 2 | oui | oui |
| `001282801003` | TERRY PLUS | `I_CANAL_2` | 0 | 2 | 2 | oui | oui |
| `001282800003` | TERRY PLUS | `I_CANAL_2` | 0 | 2 | 2 | oui | oui |
| `001282802003` | TERRY PLUS | `I_CANAL_2` | 0 | 2 | 2 | oui | oui |
| `001283350000` | COMFORT P85 PLUS | `I_CANAL_3` | 0 | 2 | 12 | oui | oui |
| `001283350001` | COMFORT P85 PLUS | `I_CANAL_3` | 0 | 2 | 12 | oui | oui |
| `001283300000` | COMFORT P85 | `I_VENT_2` | 0 | 2 | 0 | oui | oui |
| `001283400000` | COMFORT P70 AIR | `I_VENT_2` | 0 | 2 | 0 | oui | oui |
| `001283400001` | COMFORT P70 AIR | `I_VENT_2` | 0 | 2 | 0 | oui | oui |
| `001283603000` | DEBBY | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283604000` | DEBBY | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283605000` | DEBBY | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283003000` | MARILENA PLUS AD | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001283004000` | MARILENA PLUS AD | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001283005000` | MARILENA PLUS AD | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001283003001` | MARILENA PLUS AD | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001283004001` | MARILENA PLUS AD | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001283005001` | MARILENA PLUS AD | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001284200000` |  | `I_CANAL` | 0 | 2 | 1 | ? | ? |
| `001284000000` | DAHIANA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284001000` | DAHIANA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284002000` | DAHIANA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284050000` | DAHIANA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001284051000` | DAHIANA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001284052000` | DAHIANA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001284100000` | TEOREMA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284101000` | TEOREMA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284102000` | TEOREMA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284150000` | TEOREMA PLUS | `I_CANAL_3` | 0 | 2 | 2 | oui | oui |
| `001284151000` | TEOREMA PLUS | `I_CANAL_3` | 0 | 2 | 2 | oui | oui |
| `001284152000` | TEOREMA PLUS | `I_CANAL_3` | 0 | 2 | 2 | oui | oui |
| `001284150001` | TEOREMA PLUS | `I_CANAL_3` | 0 | 2 | 2 | oui | oui |
| `001284151001` | TEOREMA PLUS | `I_CANAL_3` | 0 | 2 | 2 | oui | oui |
| `001284152001` | TEOREMA PLUS | `I_CANAL_3` | 0 | 2 | 2 | oui | oui |
| `001284150002` | TEOREMA PLUS | `I_CANAL_3` | 0 | 2 | 2 | oui | oui |
| `001284151002` | TEOREMA PLUS | `I_CANAL_3` | 0 | 2 | 2 | oui | oui |
| `001284152002` | TEOREMA PLUS | `I_CANAL_3` | 0 | 2 | 2 | oui | oui |
| `004273107000` | pièce « corps » Marilena Plus AD Cry | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `004273108000` | pièce « corps » Marilena Plus AD Pt | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `004273107001` | pièce « corps » Marilena Plus AD Cry | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `004273108001` | pièce « corps » Marilena Plus AD Pt | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001282406000` | ANGELA EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001282407000` | ANGELA EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001282408000` | ANGELA EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001282506000` | ANGELA PLUS EVO | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001282507000` | ANGELA PLUS EVO | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001282508000` | ANGELA PLUS EVO | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001283450000` | COMFORT P70 AIR PLUS | `I_CANAL_4` | 0 | 2 | 11 | oui | oui |
| `001284400000` | INSERTO 700 AIR (Dal Zotto) | `I_VENT_2` | 0 | 2 | 0 | oui | oui |
| `001284400001` | INSERTO 700 AIR (Dal Zotto) | `I_VENT_2` | 0 | 2 | 0 | oui | oui |
| `001284550000` | INSERTO 850 ELITE (Dal Zotto) | `I_CANAL_3` | 0 | 2 | 12 | oui | oui |
| `001284550001` | INSERTO 850 ELITE (Dal Zotto) | `I_CANAL_3` | 0 | 2 | 12 | oui | oui |
| `001283300001` | COMFORT P85 | `I_VENT_2` | 0 | 2 | 0 | oui | oui |
| `001282309000` | MOIRA EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001282310000` | MOIRA EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001282311000` | MOIRA EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283500001` | AMIKA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283501001` | AMIKA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283502001` | AMIKA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283503001` | AMIKA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283600001` | DEBBY CX | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283601001` | DEBBY CX | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283602001` | DEBBY CX | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283603001` | DEBBY | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283604001` | DEBBY | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283605001` | DEBBY | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284000001` | DAHIANA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284001001` | DAHIANA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284002001` | DAHIANA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284050001` | DAHIANA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001284051001` | DAHIANA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001284052001` | DAHIANA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001284100001` | TEOREMA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284101001` | TEOREMA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284102001` | TEOREMA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284000002` | DAHIANA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284001002` | DAHIANA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284002002` | DAHIANA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284050002` | DAHIANA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001284051002` | DAHIANA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001284052002` | DAHIANA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001284100002` | TEOREMA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284101002` | TEOREMA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284102002` | TEOREMA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284003002` | DAHIANA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284053002` | DAHIANA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001284000003` | DAHIANA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284001003` | DAHIANA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284002003` | DAHIANA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284050003` | DAHIANA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001284051003` | DAHIANA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001284052003` | DAHIANA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001284100003` | TEOREMA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284101003` | TEOREMA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284102003` | TEOREMA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284003003` | DAHIANA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284053003` | DAHIANA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001282406001` | ANGELA EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001282407001` | ANGELA EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001282408001` | ANGELA EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001282506001` | ANGELA PLUS EVO | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001282507001` | ANGELA PLUS EVO | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001282508001` | ANGELA PLUS EVO | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001284003001` | DAHIANA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284053001` | DAHIANA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001284300000` | ROSANNA IDRO | `I_IDRO` | 1 | 1 | 0 | oui | oui |
| `001284301000` | ROSANNA IDRO | `I_IDRO` | 1 | 1 | 0 | oui | oui |
| `001284302000` | ROSANNA IDRO | `I_IDRO` | 1 | 1 | 0 | oui | oui |
| `001284300001` | ROSANNA IDRO | `I_IDRO` | 1 | 1 | 0 | oui | oui |
| `001284301001` | ROSANNA IDRO | `I_IDRO` | 1 | 1 | 0 | oui | oui |
| `001284302001` | ROSANNA IDRO | `I_IDRO` | 1 | 1 | 0 | oui | oui |
| `001275002000` | TEODORA EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001281704000` | MIETTA EVO | `I_VENT_3` | 0 | 3 | 0 | oui | oui |
| `001281705000` | MIETTA EVO | `I_VENT_3` | 0 | 3 | 0 | oui | oui |
| `001284600000` | SINFONY | `I_VENT_3` | 0 | 3 | 0 | oui | oui |
| `001284601000` | SINFONY | `I_VENT_3` | 0 | 3 | 0 | oui | oui |
| `001284700000` | LUCE | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284701000` | LUCE | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283500002` | AMIKA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283501002` | AMIKA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283502002` | AMIKA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283503002` | AMIKA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283500003` | AMIKA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283501003` | AMIKA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283502003` | AMIKA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283503003` | AMIKA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283600002` | DEBBY CX | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283601002` | DEBBY CX | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283602002` | DEBBY CX | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283603002` | DEBBY | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283604002` | DEBBY | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283605002` | DEBBY | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001283606000` |  | `I_VENT` | 0 | 2 | 0 | ? | ? |
| `001283606001` |  | `I_VENT` | 0 | 2 | 0 | ? | ? |
| `001283606002` |  | `I_VENT` | 0 | 2 | 0 | ? | ? |
| `001283607000` |  | `I_VENT` | 0 | 2 | 0 | ? | ? |
| `001283607001` |  | `I_VENT` | 0 | 2 | 0 | ? | ? |
| `001283607002` |  | `I_VENT` | 0 | 2 | 0 | ? | ? |
| `001283608000` |  | `I_VENT` | 0 | 2 | 0 | ? | ? |
| `001283608001` |  | `I_VENT` | 0 | 2 | 0 | ? | ? |
| `001283608002` |  | `I_VENT` | 0 | 2 | 0 | ? | ? |
| `001282103000` |  | `I_IDRO_2` | 11 | 1 | 0 | ? | ? |
| `001282104000` |  | `I_IDRO_2` | 11 | 1 | 0 | ? | ? |
| `001281703000` |  | `I_VENT_5` | 10 | 1 | 0 | ? | ? |
| `001283300002` | COMFORT P85 | `I_VENT_2` | 0 | 2 | 0 | oui | oui |
| `001283350002` | COMFORT P85 PLUS | `I_CANAL_3` | 0 | 2 | 12 | oui | oui |
| `001283400002` | COMFORT P70 AIR | `I_VENT_2` | 0 | 2 | 0 | oui | oui |
| `001284800000` | SABRY | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284801000` | SABRY | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284802000` | SABRY | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284800001` | SABRY | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284801001` | SABRY | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284802001` | SABRY | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284900000` | KLAUDIA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284901000` | KLAUDIA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284902000` | KLAUDIA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284950000` | KLAUDIA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001284951000` | KLAUDIA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001284952000` | KLAUDIA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001284900001` | KLAUDIA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284901001` | KLAUDIA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284902001` | KLAUDIA | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001284950001` | KLAUDIA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001284951001` | KLAUDIA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001284952001` | KLAUDIA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001285100000` | RAFFAELLA IDRO H15 | `I_IDRO` | 1 | 1 | 0 | oui | oui |
| `001285101000` | RAFFAELLA IDRO H15 | `I_IDRO` | 1 | 1 | 0 | oui | oui |
| `001285102000` | RAFFAELLA IDRO H15 | `I_IDRO` | 1 | 1 | 0 | oui | oui |
| `001285150000` | RAFFAELLA IDRO H18 | `I_IDRO` | 1 | 1 | 0 | oui | oui |
| `001285151000` | RAFFAELLA IDRO H18 | `I_IDRO` | 1 | 1 | 0 | oui | oui |
| `001285200000` | GABRIELLA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001285201000` | GABRIELLA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001285202000` | GABRIELLA PLUS | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `004273111000` | pièce « corps » Gabriella Plus Pt | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001285400000` | PAMELA STEEL | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001285401000` | PAMELA STEEL | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001285402000` | PAMELA CRYSTAL | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001275706000` | SOUVENIR LUX EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001275707000` | SOUVENIR LUX EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001275708000` | SOUVENIR LUX EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001275709000` | SOUVENIR PETRA EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001275706001` | SOUVENIR LUX EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001275707001` | SOUVENIR LUX EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001275708001` | SOUVENIR LUX EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001275709001` | SOUVENIR PETRA EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001275754000` | SOUVENIR STEEL EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001275755000` | SOUVENIR STEEL EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001275756000` | SOUVENIR STEEL EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001275754001` | SOUVENIR STEEL EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001275755001` | SOUVENIR STEEL EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001275756001` | SOUVENIR STEEL EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001280103000` | ANNABELLA AD EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001280104000` | ANNABELLA AD EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001280105000` | ANNABELLA AD EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001280106000` | ANNABELLA AD EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001280212000` | KETTY EVO 2.0 | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001280213000` | KETTY EVO 2.0 | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001280214000` | KETTY EVO 2.0 | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001280215000` | KETTY EVO 2.0 | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001280212001` | KETTY EVO 2.0 | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001280213001` | KETTY EVO 2.0 | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001280214001` | KETTY EVO 2.0 | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001280215001` | KETTY EVO 2.0 | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001281706000` |  | `I_VENT_3` | 0 | 3 | 0 | ? | ? |
| `001281707000` |  | `I_VENT_3` | 0 | 3 | 0 | ? | ? |
| `001282105000` | FIANDRA IDRO EVO | `I_IDRO_2` | 1 | 1 | 0 | oui | oui |
| `001282106000` | FIANDRA IDRO EVO | `I_IDRO_2` | 1 | 1 | 0 | oui | oui |
| `001282107000` |  | `I_IDRO_2` | 1 | 1 | 0 | ? | ? |
| `001282108000` |  | `I_IDRO_2` | 1 | 1 | 0 | ? | ? |
| `001282109000` |  | `I_IDRO_2` | 1 | 1 | 0 | ? | ? |
| `001280508000` | GIUSY EVO 2.0 | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001280509000` | GIUSY EVO 2.0 | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001280510000` | GIUSY EVO 2.0 | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001280556000` | GIUSY PLUS EVO 2.0 | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001280557000` | GIUSY PLUS EVO 2.0 | `I_CANAL` | 0 | 2 | 1 | oui | oui |
| `001280605000` | SERAFINA LUX EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001280606000` | SERAFINA LUX EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001280607000` | SERAFINA PETRA EVO | `I_VENT` | 0 | 2 | 0 | oui | oui |
| `001285300000` | GUENDA IDRO | `I_IDRO_2` | 1 | 1 | 0 | oui | oui |
| `001285301000` | GUENDA IDRO | `I_IDRO_2` | 1 | 1 | 0 | oui | oui |
| `001285302000` | GUENDA IDRO | `I_IDRO_2` | 1 | 1 | 0 | oui | oui |
