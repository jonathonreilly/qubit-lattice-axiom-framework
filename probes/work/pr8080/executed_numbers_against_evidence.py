#!/usr/bin/env python3
"""J:attack:PR8080 - stronger native Ward note, attack pattern (c) EXECUTED NUMBERS.

Every executed duration, byte count, event count, error bound and status named
in NATIVE_STRONGER_WARD_ESTIMATORS_NOTE_2026-09-10.md is checked against the
PR-head evidence (spectral-residual RESULT/ROOT_ACCEPTANCE, EVENTS.ndjson,
degree20-ward RESULT) and formula (1) is recomputed from the certified
E, F, a, chi, psi fractions.

HIT if a stated executed number disagrees with the retained evidence or (1).
"""
from __future__ import annotations

import json
import subprocess
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HEAD = "ac7bc8d614a67cec5a86d59253be17bf04b98f34"
NOTE = "docs/NATIVE_STRONGER_WARD_ESTIMATORS_NOTE_2026-09-10.md"
PK = ".claude/science/physics-loops/native-stronger-ward-20260910/source_draft/"
SPEC = PK + "evidence/spectral-residual/"
D20 = PK + "evidence/degree20-ward/"


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)


def show(path: str) -> str:
    if git("cat-file", "-e", HEAD).returncode != 0:
        git("fetch", "origin", "codex/native-stronger-ward-20260910", "--quiet")
    r = git("show", f"{HEAD}:{path}")
    if r.returncode != 0:
        raise SystemExit(f"cannot read {path}: {r.stderr.strip()[:400]}")
    return r.stdout


def showj(path: str):
    return json.loads(show(path))


def main() -> None:
    hits, rows = [], []

    def check(name, ok, detail):
        rows.append(f"[{'ok' if ok else 'MISMATCH'}] {name}: {detail}")
        if not ok:
            hits.append(f"{name}: {detail}")

    note = show(NOTE)
    acc = showj(SPEC + "ROOT_ACCEPTANCE.json")
    res = showj(SPEC + "RESULT.json")
    d20 = showj(D20 + "RESULT.json")

    # --- spectral execution ---
    check(
        "events",
        res["events"] == 588 and acc["schema"]["events"] == 588,
        f"RESULT {res['events']}, acceptance {acc['schema']['events']} (note: 588; EVENTS.ndjson hashed, not stored)",
    )
    check("choices", res["choices"] == 2 == acc["schema"]["count"], f"RESULT {res['choices']} (note: both / two choices)")
    check("oracle", res["native_oracle_calls"] == 0, f"native_oracle_calls {res['native_oracle_calls']} (note: no sign)")
    check(
        "external_seconds",
        abs(float(acc["external_seconds"]) - 1.87) < 0.005,
        f"ROOT_ACCEPTANCE external_seconds {acc['external_seconds']} (note: 1.87)",
    )
    check(
        "peak_bytes",
        acc["sampled_whole_tree_peak"] == 122683392,
        f"sampled_whole_tree_peak {acc['sampled_whole_tree_peak']} (note: 122,683,392)",
    )
    ceiling = 384 * 1024 * 1024
    check(
        "resource_ceiling",
        acc["sampled_whole_tree_peak"] <= ceiling and float(acc["external_seconds"]) <= 30,
        f"peak {acc['sampled_whole_tree_peak']} <= 384MiB={ceiling}, {acc['external_seconds']}s <= 30 (note: 30s/384MiB)",
    )
    check(
        "status",
        acc["status"].startswith("ACCEPTED")
        and all(r["status"] == "INDETERMINATE_SIGN" for r in res["rows"]),
        f"acceptance {acc['status']}; row status {[r['status'] for r in res['rows']]} (note: ACCEPTED, BOTH INDETERMINATE_SIGN)",
    )

    h = F(1)
    delta = h / 4
    X2 = F(15) / (delta * delta)  # (sqrt(15)/delta)^2
    V2 = (F(8) * h * h) * F(15) / (delta ** 4)  # (2 sqrt(2) h * sqrt(15) / delta^2)^2

    stated = {"residual": F("624367") / F(100), "variational": F("651172") / F(100)}
    for r in res["rows"]:
        mode = r["mode"]
        E, Ff, a, b = map(F, (r["E_upper"], r["F_upper"], r["a_upper"], r["b_upper"]))
        chi, psi = F(r["chi_upper"]), F(r["psi_upper"])
        X, V = F(r["X_upper"]), F(r["V_upper"])
        err = F(r["error_upper"])
        rhs = 6 * (E * (a + chi) + min(E * b + chi * Ff, E * psi + a * Ff))
        check(f"{mode} formula(1)", err == rhs, f"error_upper {float(err):.8f} vs 6[E(a+chi)+min(...)] {float(rhs):.8f}")
        check(f"{mode} chi", chi == min(X, a + E), f"chi={float(chi)} min(X,a+E)={float(min(X, a + E))}")
        check(f"{mode} psi", psi == min(V, b + Ff), f"psi={float(psi)} min(V,b+F)={float(min(V, b + Ff))}")
        rounded = round(float(err), 2)
        target = float(stated[mode])
        check(f"{mode} stated", abs(rounded - target) < 0.005, f"{rounded} vs note ~{target}")
        lo, hi = map(F, r["alpha_interval"])
        check(f"{mode} contains0", lo <= 0 <= hi, f"alpha [{float(lo):.4f},{float(hi):.4f}]")
        check(f"{mode} X_upper", X * X >= X2, f"X_upper^2={float(X*X)} vs 15/delta^2={float(X2)} (enclosure)")
        check(f"{mode} V_upper", V * V >= V2, f"V_upper^2={float(V*V)} vs j^2 15/delta^4={float(V2)} (enclosure)")

    # ninety ordered terms of the degree-(2,0) protocol
    ow = [r.get("ordered_words") for r in d20["rows"]]
    st = [r.get("status") for r in d20["rows"]]
    check(
        "ninety_terms",
        ow == [90, 90] and st == ["INDETERMINATE_SIGN", "INDETERMINATE_SIGN"],
        f"degree20-ward ordered_words {ow} status {st} (note: ninety ordered terms, both inconclusive)",
    )

    compact = showj(PK + "COMPACT_OUTPUT.json")
    check(
        "compact_28",
        compact.get("checks") == 28 and "INDETERMINATE_SIGN" in compact.get("spectral_outcome", ""),
        f"COMPACT_OUTPUT checks={compact.get('checks')} outcome={compact.get('spectral_outcome')}",
    )

    for line in rows:
        print(line)
    if hits:
        for hmsg in hits:
            print("HIT: " + hmsg)
        print("SUMMARY: pattern (c) EXECUTED NUMBERS; " + "; ".join(hits))
    else:
        print(
            "SUMMARY: pattern (c) EXECUTED NUMBERS; spectral 1.87s / 122683392 B / 588 events, "
            "error bounds 6243.67 and 6511.72, formula (1), X=sqrt(15)/delta, V=j sqrt(15)/delta^2, "
            "ninety ordered_words and both INDETERMINATE_SIGN all match the PR-head evidence"
        )


if __name__ == "__main__":
    main()
