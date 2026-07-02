#!/usr/bin/env python3
"""Restricted-packet verifier for the Koide Q reduced-carrier audit row.

This runner checks the source-side packet now available for
`KOIDE_Q_REDUCED_OBSERVABLE_RESTRICTION_THEOREM_2026-04-22.md`:

1. the parent reduced determinant theorem and cached algebra runner;
2. the physical-carrier/readout obstruction note and cached runner; and
3. the `D_red = I_2` normalization-freedom no-go note and cached runner.

It does not audit the row, promote status, or edit audit-owned files.
"""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def sha256_file(rel: str) -> str:
    return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status} {name}{suffix}")


def cache_meta(cache_text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in cache_text.splitlines():
        if ": " not in line or line.startswith("-----"):
            continue
        key, value = line.split(": ", 1)
        if key in {"runner", "runner_sha256", "exit_code", "status"}:
            out[key] = value.strip()
    return out


PARENT_NOTE = "docs/KOIDE_Q_REDUCED_OBSERVABLE_RESTRICTION_THEOREM_2026-04-22.md"
CARRIER_NOTE = "docs/KOIDE_Q_REDUCED_CARRIER_PHYSICAL_IDENTIFICATION_OBSTRUCTION_NOTE_2026-06-12.md"
DRED_NOTE = "docs/KOIDE_Q_DRED_NORMALIZATION_FREEDOM_NO_GO_NOTE_2026-06-15.md"

PARENT_RUNNER = "scripts/frontier_koide_q_reduced_observable_restriction_theorem.py"
CARRIER_RUNNER = "scripts/frontier_koide_q_reduced_carrier_physical_identification_obstruction_2026_06_12.py"
DRED_RUNNER = "scripts/koide_q_dred_normalization_freedom_no_go_2026_06_15.py"

CACHES = {
    PARENT_RUNNER: "logs/runner-cache/frontier_koide_q_reduced_observable_restriction_theorem.txt",
    CARRIER_RUNNER: "logs/runner-cache/frontier_koide_q_reduced_carrier_physical_identification_obstruction_2026_06_12.txt",
    DRED_RUNNER: "logs/runner-cache/koide_q_dred_normalization_freedom_no_go_2026_06_15.txt",
}


def main() -> int:
    print("Koide Q reduced-carrier restricted packet verifier")
    print("=" * 72)

    parent = read(PARENT_NOTE)
    carrier = read(CARRIER_NOTE)
    dred = read(DRED_NOTE)

    check("parent note exists", (ROOT / PARENT_NOTE).is_file())
    check("carrier obstruction note exists", (ROOT / CARRIER_NOTE).is_file())
    check("D_red normalization no-go note exists", (ROOT / DRED_NOTE).is_file())

    parent_needles = [
        "bounded algebraic support theorem",
        "not a closure theorem",
        "physical charged-lepton observable carrier/readout",
        "D_red = I_2",
        "KOIDE_Q_REDUCED_CARRIER_PHYSICAL_IDENTIFICATION_OBSTRUCTION_NOTE_2026-06-12.md",
        "KOIDE_Q_DRED_NORMALIZATION_FREEDOM_NO_GO_NOTE_2026-06-15.md",
        "koide_q_reduced_reaudit_packet_verifier_2026_06_17.py",
        "does not promote this row",
    ]
    for needle in parent_needles:
        check(f"parent records {needle!r}", needle in parent)

    check(
        "parent preserves exact reduced determinant support",
        "W_red(K)" in parent
        and "log det(I_2 + K)" in parent
        and "exact determinant" in parent,
    )
    check(
        "parent leaves audit authority external",
        "independent audit lane only" in parent
        and "modify the parent row's audit-ledger entry" in parent,
    )

    carrier_needles = [
        "reduced two-slot carrier",
        "coarse-graining/readout",
        "Record/Quantum axioms do not supply the missing readout context",
        "not been derived as the physical",
        "add a new axiom",
    ]
    for needle in carrier_needles:
        check(f"carrier obstruction records {needle!r}", needle in carrier)

    dred_needles = [
        "For every `c > 0`",
        "`D_red = c I_2`",
        "source-coordinate rescaling",
        "normalization bridge or convention",
        "It does not add an axiom",
    ]
    for needle in dred_needles:
        check(f"D_red no-go records {needle!r}", needle in dred)

    cache_needles = {
        PARENT_RUNNER: [
            "PASSED: 15/15",
            "It does not by itself prove that this reduced carrier is the physical",
        ],
        CARRIER_RUNNER: [
            "TOTAL: PASS=13 FAIL=0",
            "missing bridge is a real readout/coarse-graining theorem",
        ],
        DRED_RUNNER: [
            "TOTAL: PASS=14 FAIL=0",
            "positive repair must supply a physical response-unit theorem or approved premise",
        ],
    }

    for runner, cache in CACHES.items():
        check(f"{runner} exists", (ROOT / runner).is_file())
        check(f"{cache} exists", (ROOT / cache).is_file())
        cache_text = read(cache)
        meta = cache_meta(cache_text)
        check(f"{cache} records runner path", meta.get("runner") == runner, f"runner={meta.get('runner')}")
        check(f"{cache} exits zero", meta.get("exit_code") == "0", f"exit_code={meta.get('exit_code')}")
        check(f"{cache} status ok", meta.get("status") == "ok", f"status={meta.get('status')}")
        check(
            f"{cache} sha matches source",
            meta.get("runner_sha256") == sha256_file(runner),
            f"cache={meta.get('runner_sha256')}, live={sha256_file(runner)}",
        )
        for needle in cache_needles[runner]:
            check(f"{cache} contains {needle!r}", needle in cache_text)

    check(
        "packet class is boundary/exact-support only, not status promotion",
        "does not promote this row" in parent
        and "does not refute the reduced-observable theorem" in dred
        and "close the physical charged-lepton Koide `Q` bridge" in carrier,
    )

    print("=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        return 1
    print(
        "Koide Q reduced packet is source-side re-audit ready: exact "
        "determinant support is cached, and both live blockers are explicit "
        "non-promotional boundary notes."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
