/**
 * openextraflame - brochage par carte.
 *
 * Le BROCHAGE ne vit plus ici : chaque carte est declaree dans boards/<carte>.json
 * et lu depuis l'en-tete engendre board_pins.h (tools/gen_board.py, a la
 * configuration CMake). -DBOARD=isno-super | external | blacklabel choisit la
 * carte ; ce firmware ne code AUCUNE broche, il les LIT.
 *
 * Le PROFIL de fonctionnalites (TARGET_EXTERNAL / TARGET_BLACKLABEL) reste une
 * definition de compilation posee par le CMakeLists racine selon la carte : il
 * gouverne des fonctions entieres (pont cloud, partition secret1, LEDs par etat)
 * bien au-dela des broches, et vit donc a la portee globale, pas ici.
 */
#pragma once

#include "driver/gpio.h"
#include "driver/uart.h"

/* Engendre dans build/board/board_pins.h depuis boards/${BOARD}.json. */
#include "board_pins.h"

#if !defined(TARGET_EXTERNAL) && !defined(TARGET_BLACKLABEL)
    #error "Aucun profil defini : le CMakeLists racine le pose depuis -DBOARD."
#endif
