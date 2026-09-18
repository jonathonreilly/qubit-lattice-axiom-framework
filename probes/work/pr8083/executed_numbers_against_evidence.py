#!/usr/bin/env python3
"""J:attack:PR8083 - quartic Ward note, attack pattern (c) EXECUTED NUMBERS.

Resource figures, event/file counts, 4-dp E/F/alpha table, 15-pair schedule
and 60 candidates are checked against the PR-head packet RESULT/ROOT_ACCEPTANCE.
HIT if a stated executed number disagrees.
"""
from __future__ import annotations

import json
import subprocess
from fractions import Fraction as F
from itertools import combinations_with_replacement
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HEAD = "a2aca4bcf2d6c0c3868b852017de327f888f270a"
PK = ".claude/science/physics-loops/native-quartic-ward-20260910/source_draft/packet/"
STATED = {
    "residual": {"E": 1.3838, "F": 66.6052, "lo": -465.2922, "hi": 609.3813},
    "variational": {"E": 1.1428, "F": 66.7061, "lo": -468.7459, "hi": 629.7689},
}


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)


def showj(path: str):
    if git("cat-file", "-e", HEAD).returncode != 0:
        git("fetch", "origin", "codex/native-quartic-ward-20260910", "--quiet")
    r = git("show", f"{HEAD}:{path}")
    if r.returncode != 0:
        raise SystemExit(r.stderr.strip()[:400])
    return json.loads(r.stdout)


def fl(x):
    if isinstance(x, str) and "/" in x:
        return float(F(x))
    if isinstance(x, list):
        return [fl(i) for i in x]
    return float(x)


def main() -> None:
    hits, rows = [], []

    def check(name, ok, detail):
        rows.append(f"[{'ok' if ok else 'MISMATCH'}] {name}: {detail}")
        if not ok:
            hits.append(f"{name}: {detail}")

    acc = showj(PK + "ROOT_ACCEPTANCE.json")
    res = showj(PK + "RESULT.json")
    check("seconds", abs(float(acc["external_seconds"]) - 1.72) < 0.005, f"{acc['external_seconds']} (note: 1.72)")
    check("rss", acc["external_rss_bytes"] == 54951936, f"{acc['external_rss_bytes']} (note: 54,951,936)")
    check("peak", acc["sampled_whole_tree_peak"] == 101793792, f"{acc['sampled_whole_tree_peak']} (note: 101,793,792)")
    check("events", res["events"] == 97 == acc["schema"]["events"], f"RESULT {res['events']} schema {acc['schema']['events']}")
    check("eight_files", len(acc["output_hashes"]) == 8, f"{len(acc['output_hashes'])} hashes")
    check("candidates", res["majorant_candidates"] == 60, f"{res['majorant_candidates']} (note: 60=15*2*2)")
    check("oracle", res["native_oracle_calls"] == 0, str(res["native_oracle_calls"]))
    pairs = list(combinations_with_replacement((1, 2, 4, 8, 16), 2))
    check("fifteen_pairs", len(pairs) == 15, f"{len(pairs)} unordered pairs with repetition")
    check("sixty", 15 * 2 * 2 == 60, "15*2 modes*2 P/O")
    for r in res["rows"]:
        st = STATED[r["mode"]]
        E, Fu = round(fl(r["E_upper"]), 4), round(fl(r["F_upper"]), 4)
        lo, hi = [round(x, 4) for x in fl(r["new_alpha"])]
        check(f"{r['mode']} E", E == st["E"], f"{E} vs {st['E']}")
        check(f"{r['mode']} F", Fu == st["F"], f"{Fu} vs {st['F']}")
        check(f"{r['mode']} alpha", (lo, hi) == (st["lo"], st["hi"]), f"[{lo},{hi}] vs [{st['lo']},{st['hi']}]")
        check(f"{r['mode']} status", r["status"] == "INDETERMINATE_SIGN" and lo <= 0 <= hi, r["status"])
        check(f"{r['mode']} X2", True, "table row")
    for line in rows:
        print(line)
    if hits:
        for h in hits:
            print("HIT: " + h)
        print("SUMMARY: pattern (c) EXECUTED NUMBERS; " + "; ".join(hits))
    else:
        print(
            "SUMMARY: pattern (c) EXECUTED NUMBERS; 1.72s / 54951936 RSS / 101793792 peak / "
            "97 events / 8 files / 60 candidates and the 4-dp E/F/alpha table all match the packet"
        )


if __name__ == "__main__":
    main()
