#!/usr/bin/env python3
"""Garde-fou CI : hd.max_uri_handlers DOIT etre >= au nombre de routes HTTP declarees.

ESP-IDF droppe SILENCIEUSEMENT les routes au-dela de max_uri_handlers (juste un log W,
facile a rater). Le 2026-11-15 : 50 routes pour max=40 -> les routes #41..#50, dont
/debug/uart-set (le switch d'inversion de ligne), n'etaient jamais enregistrees -> "Failed
to fetch" cote navigateur, et 9 autres routes mortes. Ce controle rend le defaut visible a
la construction au lieu de le laisser muet a l'execution.

Usage : python3 tools/check_uri_handlers.py   (rend 0 si OK, 1 sinon)
"""
import re
import sys
import pathlib

SRC = pathlib.Path(__file__).resolve().parent.parent / "firmware" / "main" / "web_ui.c"


def main() -> int:
    if not SRC.exists():
        print(f"ECHEC : {SRC} introuvable")
        return 1
    text = SRC.read_text(encoding="utf-8")

    m = re.search(r"max_uri_handlers\s*=\s*(\d+)", text)
    if not m:
        print("ECHEC : max_uri_handlers introuvable dans web_ui.c")
        return 1
    max_handlers = int(m.group(1))

    # Une route = une entree { .uri = "...", .method = ..., .handler = ... }.
    # On compte les '.uri = "' (avec chaine litterale) pour ne pas attraper autre chose.
    routes = len(re.findall(r"\.uri\s*=\s*\"", text))

    print(f"max_uri_handlers = {max_handlers} ; routes HTTP declarees = {routes}")
    if max_handlers < routes:
        print(
            f"ECHEC : max_uri_handlers ({max_handlers}) < routes ({routes}). "
            f"ESP-IDF enregistrera seulement les {max_handlers} premieres et droppera "
            f"les {routes - max_handlers} suivantes en silence. Augmente hd.max_uri_handlers."
        )
        return 1
    print("OK : assez de slots pour toutes les routes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
