#!/usr/bin/env python3
"""Verify the source-side Dirac dynamics unlock path from the axiom reset.

This runner checks wiring, not audit status. It verifies that the stacked PR
contains a coherent route:

    #4747 axioms -> strict NN composition -> flux(-1) / K1 selector
      -> P-KIN/P-SD retirement path -> staggered-Dirac kinetic clause

It deliberately preserves the boundary that probability, temporal dynamics,
AC_phi_lambda, theta, source/action, and observable bridges remain separate.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PATH_NOTE = ROOT / "docs" / "DIRAC_DYNAMICS_UNLOCK_PATH_FROM_AXIOM_RESET_2026-06-30.md"
BRIDGE_NOTE = ROOT / "docs" / "STRICT_NN_COMPOSITION_FLUX_SELECTOR_BRIDGE_THEOREM_NOTE_2026-06-30.md"
BRIDGE_RUNNER = ROOT / "scripts" / "strict_nn_composition_flux_selector_2026_06_30.py"
KINETIC_NOTE = ROOT / "docs" / "STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md"
KS_NOTE = ROOT / "docs" / "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md"
GATE_NOTE = ROOT / "docs" / "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
INDEX_NO_GO = ROOT / "docs" / "INDEX_PAIRING_NOT_FORCED_KINETIC_ORDER_SELECTOR_NO_GO_NOTE_2026-06-08.md"

PASS = 0
FAIL = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def run_bridge_runner() -> str:
    proc = subprocess.run(
        [sys.executable, str(BRIDGE_RUNNER)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return proc.stdout + proc.stderr


def main() -> int:
    print("=== Dirac dynamics unlock path from #4747 axioms ===")

    for path in [AXIOMS, PATH_NOTE, BRIDGE_NOTE, BRIDGE_RUNNER, KINETIC_NOTE, KS_NOTE, GATE_NOTE, INDEX_NO_GO]:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    axioms = read(AXIOMS)
    axioms_flat = flat(axioms)
    path_note = read(PATH_NOTE)
    path_flat = flat(path_note)
    bridge = read(BRIDGE_NOTE)
    bridge_flat = flat(bridge)
    kinetic = read(KINETIC_NOTE)
    kinetic_flat = flat(kinetic)
    ks = read(KS_NOTE)
    ks_flat = flat(ks)
    gate = read(GATE_NOTE)
    gate_flat = flat(gate)
    index_no_go = read(INDEX_NO_GO)
    index_flat = flat(index_no_go)

    print("\nPART A -- #4747 axiom inputs")
    check("axioms supply Z^3 nearest-neighbor locality", "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency" in axioms_flat)
    check("axioms supply proper cubic rotations", "proper cubic rotations" in axioms)
    check("axioms supply one-site M_2(C) possibility domain", "full one-site possibility domain has algebraic presentation `M_2(C)`" in axioms)
    check("axioms supply nearest-neighbor admissibility rule", "one fixed nearest-neighbor admissibility rule" in axioms)
    check("axioms supply available subset of possibilities", "determine the available subset of possibilities" in axioms)
    check("axioms keep dynamics downstream", "Admissibility is not a dynamics axiom" in axioms)

    print("\nPART B -- bridge theorem surface")
    check("bridge note declares unbounded bridge theorem", "positive_theorem candidate / unbounded bridge theorem" in bridge)
    check("bridge note states strict NN composition", "Strict NN composition" in bridge and "must not create a direct face-diagonal availability influence" in bridge_flat)
    check("bridge note uses free Z^3 translation algebra", "free\ntranslation algebra of `Z^3`" in bridge or "free `Z^3` translation algebra" in bridge)
    check("bridge note names independent face-diagonal monomials", "the monomials for the twelve face diagonals\nare independent" in bridge)
    check("bridge note states anticommutator condition", "Gamma_mu Gamma_nu + Gamma_nu Gamma_mu = 0" in bridge)
    check("bridge note selects flux -1 and rejects flux +1", "flux `-1`" in bridge and "flux(+1)" in bridge)
    check("bridge note preserves non-kinetic boundaries", "probability" in bridge and "Hamiltonian" in bridge and "theta" in bridge)

    bridge_output = run_bridge_runner()
    check("bridge runner PASS=16 FAIL=0", "TOTAL: PASS=16 FAIL=0" in bridge_output)
    check("bridge runner verdict is unbounded free-Z3 coefficient identity", "unbounded free-Z^3 coefficient identity" in bridge_output)

    print("\nPART C -- existing blockers match the new bridge")
    check("index no-go identifies kinetic-order selector", "kinetic-order selector" in index_flat)
    check("index no-go says first-order kinetic order is unsupplied antecedent", "first-order-in-space is the unsupplied antecedent" in index_no_go)
    check("kinetic note names K0 flux(+1)", "K0" in kinetic and "flux `+1`" in kinetic)
    check("kinetic note names K1 flux(-1)", "K1" in kinetic and "flux `−1`" in kinetic)
    check("kinetic note names B-BIT residual", "B-BIT" in kinetic)
    check("kinetic note says P-SD theorem on surviving branch", "P-SD: yes" in kinetic)
    check("kinetic note says P-KIN reduced to one bit", "P-KIN: reduced to one bit" in kinetic)

    print("\nPART D -- downstream activation path")
    check("KS note declares P-KIN premise boundary", "| B2 | P-KIN" in ks)
    check("KS note declares P-SD premise boundary", "| B3 | P-SD" in ks)
    check("KS note already records P-SD discharged on K1", "P-SD discharged on K1" in ks or "P-SD is discharged" in ks)
    check("KS note already records P-KIN reduced to P-FLUX", "P-KIN reduced to P-FLUX" in ks or "P-KIN is reduced to P-FLUX" in ks)
    check("gate note names kinetic-class / P-FLUX supply line", "kinetic-class / P-FLUX supply line" in gate)
    check("gate note marks current old closure bounded/conditional", "current closure remains bounded/conditional" in gate)
    check("gate note names staggered-Dirac realization definition", "Realization Definition" in gate)

    print("\nPART E -- new path note hygiene")
    check("path note defines Dirac dynamics narrowly", "static spatial first-order\nDirac/staggered kinetic spine" in path_note)
    check("path note maps P-KIN/P-SD retirement", "P-KIN/P-SD/P-FLUX" in path_note and "strict NN composition" in path_note)
    check("path note gives re-audit target list", "Audit Work After This PR" in path_note and "Re-audit" in path_note)
    check("path note gives minimal axiom fallback", "Minimal Axiom Fallback" in path_note and "not a broad Dynamics axiom" in path_note)
    check("path note explicitly leaves AC_phi_lambda open", "`AC_phi_lambda`" in path_note and "What Still Does Not Unlock" in path_note)
    check("path note explicitly leaves temporal dynamics open", "temporal dynamics" in path_flat and "time metric" in path_note)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS -- unlock path is wired; audit status remains review-owned.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
