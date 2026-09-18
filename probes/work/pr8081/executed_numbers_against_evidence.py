#!/usr/bin/env python3
"""J:attack:PR8081 - correlated Ward note, attack pattern (c) EXECUTED NUMBERS.

Every executed duration, RSS, peak, event count, Wick count, channel count,
scale count, interval endpoint and status named in
NATIVE_CORRELATED_WARD_CERTIFICATES_NOTE_2026-09-10.md is checked against the
PR-head dual ROOT_ACCEPTANCE/RESULT (and EVENTS.ndjson.gz). T-spectrum of the
K6 disjoint-pair adjacency and L(E,F) branch agreement are recomputed exactly.

HIT if a stated executed number disagrees with the retained evidence.
"""
from __future__ import annotations

import gzip
import json
import subprocess
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
HEAD = "ac5e0c248f9af28f86ee148e95c148a74e260524"
NOTE = "docs/NATIVE_CORRELATED_WARD_CERTIFICATES_NOTE_2026-09-10.md"
PK = ".claude/science/physics-loops/native-correlated-ward-20260910/source_draft/"
DUAL = PK + "evidence/dual/"

STATED = {
    "residual": {
        "prior": (-734.76773, 826.14955),
        "signed": (-489.19594, 665.70731),
    },
    "variational": {
        "prior": (-737.70476, 890.22488),
        "signed": (-441.59020, 696.19304),
    },
}


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True)


def show_bytes(path: str) -> bytes:
    if git("cat-file", "-e", HEAD).returncode != 0:
        git("fetch", "origin", "codex/native-correlated-ward-20260910", "--quiet")
    r = git("show", f"{HEAD}:{path}")
    if r.returncode != 0:
        raise SystemExit((r.stderr or b"").decode()[:400])
    return r.stdout


def show(path: str) -> str:
    return show_bytes(path).decode()


def showj(path: str):
    return json.loads(show(path))


def fl(x):
    if isinstance(x, str) and "/" in x:
        return float(F(x))
    if isinstance(x, list):
        return [fl(i) for i in x]
    return float(x) if isinstance(x, (int, float)) else x


def rnd5(x: float) -> float:
    return round(x, 5)


def main() -> None:
    hits, rows = [], []

    def check(name, ok, detail):
        rows.append(f"[{'ok' if ok else 'MISMATCH'}] {name}: {detail}")
        if not ok:
            hits.append(f"{name}: {detail}")

    note = show(NOTE)
    acc = showj(DUAL + "ROOT_ACCEPTANCE.json")
    res = showj(DUAL + "RESULT.json")
    ev = gzip.decompress(show_bytes(DUAL + "EVENTS.ndjson.gz")).decode().strip().splitlines()

    check(
        "events",
        res["events"] == 763 and len(ev) == 763 and acc["schema"]["events"] == 763,
        f"RESULT {res['events']}, EVENTS.ndjson.gz {len(ev)}, acceptance {acc['schema']['events']} (note: 763)",
    )
    check("choices", res["choices"] == 2 == acc["schema"]["count"], f"RESULT {res['choices']} (note: both modes)")
    check("oracle", res["native_oracle_calls"] == 0, f"native_oracle_calls {res['native_oracle_calls']}")
    check(
        "external_seconds",
        abs(float(acc["external_seconds"]) - 4.65) < 0.005,
        f"ROOT_ACCEPTANCE {acc['external_seconds']} (note: 4.65)",
    )
    check(
        "rss",
        acc["external_rss_bytes"] == 82706432,
        f"external_rss_bytes {acc['external_rss_bytes']} (note: 82,706,432)",
    )
    check(
        "peak",
        acc["sampled_whole_tree_peak"] == 119488512,
        f"sampled_whole_tree_peak {acc['sampled_whole_tree_peak']} (note: 119,488,512)",
    )
    check(
        "nine_files",
        len(acc["output_hashes"]) == 9,
        f"{len(acc['output_hashes'])} output_hashes (note: nine files)",
    )
    check(
        "wick",
        res["logical_Wick_words"] == 5130 and res["max_actual_Wick_words"] == 684,
        f"logical {res['logical_Wick_words']} actual {res['max_actual_Wick_words']} (note: 684 vs 5130)",
    )
    check(
        "status",
        acc["status"].startswith("ACCEPTED")
        and all(r["status"] == "INDETERMINATE_SIGN" for r in res["rows"]),
        f"{acc['status']}; {[r['status'] for r in res['rows']]}",
    )
    check("claim_scope_inconclusive" in note or True, "inconclusive" in note.lower() or "INDETERMINATE" in note, "note states inconclusive")

    for r in res["rows"]:
        mode = r["mode"]
        nch = len(r["channels"])
        check(f"{mode} channels", nch == 15, f"{nch} (note: 15 two-neighbor channels)")
        prior = [rnd5(fl(x)) for x in r["spectral_alpha_interval"]]
        signed = [rnd5(fl(x)) for x in r["alpha_interval"]]
        sp, ss = STATED[mode]["prior"], STATED[mode]["signed"]
        check(f"{mode} prior", tuple(prior) == sp, f"{prior} vs note {list(sp)}")
        check(f"{mode} signed", tuple(signed) == ss, f"{signed} vs note {list(ss)}")
        lo, hi = fl(r["alpha_interval"])
        check(f"{mode} contains0", lo <= 0 <= hi, f"[{lo:.5f},{hi:.5f}]")
        lams = []
        for c in r["candidates"]:
            lam = str(c.get("lambda"))
            ai = fl(c["alpha_interval"])
            lams.append((lam, ai[0], ai[1]))
        check(f"{mode} five_scales", len(lams) == 5, f"{[t[0] for t in lams]}")
        by = {t[0]: t[1:] for t in lams}
        best = by["1"]
        for name, pair in by.items():
            if name == "1":
                continue
            worse = pair[0] <= best[0] + 1e-9 and pair[1] >= best[1] - 1e-9
            check(
                f"{mode} lambda{name}_vs_1",
                worse,
                f"lambda {name} {pair} vs lambda1 {best} (note: lambda=1 supplies both endpoints)",
            )

    # T spectrum: disjoint 2-subsets of 6 labels
    edges = list(combinations(range(6), 2))
    T = np.zeros((15, 15), dtype=int)
    for i, a in enumerate(edges):
        for j, b in enumerate(edges):
            if i != j and set(a).isdisjoint(b):
                T[i, j] = 1
    w = sorted(np.linalg.eigvalsh(T.astype(float)).round(8).tolist())
    counts = Counter(int(round(x)) for x in w)
    check(
        "T_spectrum",
        counts == {6: 1, -3: 5, 1: 9},
        f"{dict(counts)} (note: 6,-3,1 with multiplicities 1,5,9)",
    )

    # L(E,F) branch agreement at F=2E and F=4E
    def L(E, F):
        if F <= 2 * E:
            return -3 * E * E - 3 * E * F
        if F <= 4 * E:
            return -6 * E * E - 3 * F * F / 4
        return 6 * E * E - 6 * E * F

    E = F(3, 7)
    check("L_at_2E", L(E, 2 * E) == L(E, 2 * E), "tautology")
    a = -3 * E * E - 3 * E * (2 * E)
    b = -6 * E * E - 3 * (2 * E) * (2 * E) / 4
    c = -6 * E * E - 3 * (4 * E) * (4 * E) / 4
    d = 6 * E * E - 6 * E * (4 * E)
    check("L_join_2E", a == b, f"{a} vs {b}")
    check("L_join_4E", c == d, f"{c} vs {d}")

    for line in rows:
        print(line)
    if hits:
        for h in hits:
            print("HIT: " + h)
        print("SUMMARY: pattern (c) EXECUTED NUMBERS; " + "; ".join(hits))
    else:
        print(
            "SUMMARY: pattern (c) EXECUTED NUMBERS; dual 4.65s / 82706432 RSS / 119488512 peak / "
            "763 events / 684 vs 5130 Wick words / 15 channels / five scales, rounded intervals, "
            "T-spectrum 6,-3,1 (1,5,9) and L(E,F) joins all match the PR-head evidence"
        )


if __name__ == "__main__":
    main()
