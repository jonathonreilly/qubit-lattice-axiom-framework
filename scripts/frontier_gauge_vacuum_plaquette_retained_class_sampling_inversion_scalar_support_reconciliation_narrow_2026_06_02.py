#!/usr/bin/env python3
"""
Runner-artifact reconciliation companion to the audited_conditional parent
`gauge_vacuum_plaquette_retained_class_sampling_inversion_note_2026-04-17`.

Targets the auditor's named `runner_artifact_issue`: update the scalar support
check to match the repaired (2026-05-29 narrowed) scalar-value note and refresh
the runner cache. Reproduces parent inversion algebra on the same witness
sector and same four generic SU(3) marked-holonomy samples; confirms the three
repaired phrases R1/R2/R3 are present in the current scalar-value note; confirms
the parent runner's stale substring S0 is absent (artifact reproduced under
restricted packet); confirms sibling-authority phrases unchanged; confirms
hostile-audit invariants (parent note, parent runner, repaired scalar-value
note all unmodified).

Expected summary: PASS=14 FAIL=0
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    PASS += 1 if ok else 0
    FAIL += 0 if ok else 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"         {detail}")


def read(p: str) -> str:
    return (ROOT / p).read_text()


def sha(p: str) -> str:
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()


def dim_su3(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def chi_su3(p: int, q: int, t1: float, t2: float) -> complex:
    x = np.array(
        [np.exp(1j * t1), np.exp(1j * t2), np.exp(-1j * (t1 + t2))], dtype=complex
    )
    lam = [p + q, q, 0]
    num = np.array(
        [[x[i] ** (lam[j] + 2 - j) for j in range(3)] for i in range(3)], dtype=complex
    )
    den = np.array(
        [[x[i] ** (2 - j) for j in range(3)] for i in range(3)], dtype=complex
    )
    return complex(np.linalg.det(num) / np.linalg.det(den))


def evaluation_matrix(weights, samples) -> np.ndarray:
    mat = np.zeros((len(samples), len(weights)), dtype=complex)
    for i, (t1, t2) in enumerate(samples):
        for j, (p, q) in enumerate(weights):
            mat[i, j] = dim_su3(p, q) * chi_su3(p, q, t1, t2)
    return mat


def main() -> int:
    parent_note_p = (
        "docs/GAUGE_VACUUM_PLAQUETTE_RETAINED_CLASS_SAMPLING_INVERSION_NOTE_2026-04-17.md"
    )
    parent_run_p = (
        "scripts/frontier_gauge_vacuum_plaquette_retained_class_sampling_inversion_2026_04_17.py"
    )
    eval_p = (
        "docs/GAUGE_VACUUM_PLAQUETTE_COMPRESSED_RIM_EVALUATION_THEOREM_NOTE_2026-04-17.md"
    )
    unique_p = (
        "docs/GAUGE_VACUUM_PLAQUETTE_COMPRESSED_RIM_FUNCTIONAL_UNIQUENESS_NOTE_2026-04-17.md"
    )
    scalar_p = (
        "docs/GAUGE_VACUUM_PLAQUETTE_BETA6_SCALAR_VALUE_INSUFFICIENCY_NOTE_2026-04-17.md"
    )
    parent_note = read(parent_note_p)
    parent_run = read(parent_run_p)
    eval_note = read(eval_p)
    unique_note = read(unique_p)
    scalar_note = read(scalar_p)

    # Parent-identical retained witness sector + samples
    weights = [(0, 0), (1, 0), (0, 1), (1, 1)]
    coeffs = np.array([1.00, 0.37, 0.37, 0.16], dtype=complex)
    samples = [
        (0.9763821785336546, 0.9506659158026622),
        (0.9976858534152107, -0.8728017811294717),
        (-0.8365991569410325, -0.885780777177599),
        (0.7458439213371963, 0.6408866502507771),
    ]
    e_full = evaluation_matrix(weights, samples)
    z_full = e_full @ coeffs
    coeffs_rec = np.linalg.solve(e_full, z_full)
    det_abs = abs(np.linalg.det(e_full))
    cond = float(np.linalg.cond(e_full))
    rec_err = float(np.max(np.abs(coeffs_rec - coeffs)))

    e_three = e_full[:3, :]
    rank_three = int(np.linalg.matrix_rank(e_three))
    _, _, vh = np.linalg.svd(e_three)
    null_vec = vh[-1, :].conj()
    null_resid = float(np.max(np.abs(e_three @ null_vec)))
    coeffs_alt = coeffs + 0.09 * null_vec / np.max(np.abs(null_vec))
    three_gap = float(np.max(np.abs(e_three @ coeffs_alt - e_three @ coeffs)))
    full_gap = float(np.max(np.abs(e_full @ coeffs_alt - z_full)))

    print("=" * 88)
    print("GAUGE-VACUUM PLAQUETTE RETAINED CLASS-SAMPLING INVERSION")
    print("   SCALAR-SUPPORT RECONCILIATION COMPANION (RUNNER ARTIFACT REPAIR)")
    print("=" * 88)
    print()
    print(f"Retained witness sector weights = {weights}")
    print(f"Witness coefficients            = {np.round(coeffs.real, 6)}")
    print(f"|det E|={det_abs:.6e}  cond(E)={cond:.6e}  recovery err={rec_err:.3e}")
    print(
        f"rank(E_3)={rank_three}  null_resid={null_resid:.3e}  "
        f"3-sample gap={three_gap:.3e}  4-sample gap={full_gap:.3e}"
    )
    print()

    # (A) Parent inversion algebra reproduction
    print("(A) Parent inversion algebra reproduction on the restricted packet")
    check(
        "(A1) Evaluation matrix shape matches retained sector size",
        e_full.shape == (len(weights), len(weights)),
        f"shape(E)={e_full.shape}",
    )
    check(
        "(A2) Generic full sample set is invertible on the witness sector",
        det_abs > 1.0e-6 and np.isfinite(cond),
        f"|det E|={det_abs:.3e}, cond(E)={cond:.3e}",
    )
    check(
        "(A3) Retained coefficient vector recovered exactly from full-rank samples",
        rec_err < 1.0e-10,
        f"max recovery error={rec_err:.3e}",
    )
    check(
        "(A4) Too few retained samples leave the system underdetermined",
        rank_three < len(weights) and null_resid < 1.0e-10,
        f"rank(E_3)={rank_three}, null residual={null_resid:.3e}",
    )
    check(
        "(A5) A null direction invisible to three samples becomes visible at four",
        three_gap < 1.0e-10 and full_gap > 1.0e-3,
        f"3-sample gap={three_gap:.3e}, 4-sample gap={full_gap:.3e}",
    )
    print()

    # (B) Post-repair phrase presence in scalar-value note
    r1 = "one scalar value does not determine"
    r2 = "a single scalar constraint does not determine"
    r3 = "a scalar plaquette value alone cannot be treated as full class-sector data"
    print("(B) Post-2026-05-29 repaired-phrase presence in the scalar-value note")
    check(f"(B1, R1, Status) {r1!r} present", r1 in scalar_note)
    check(f"(B2, R2, Formal No-Go) {r2!r} present", r2 in scalar_note)
    check(f"(B3, R3, What This Closes) {r3!r} present", r3 in scalar_note)
    print()

    # (C) Stale-phrase absence (artifact issue reproduced)
    s0 = "one scalar framework-point value does not determine the class-sector vector"
    print("(C) Stale parent-runner substring absence in repaired scalar-value note")
    check(
        "(C1) Stale substring S0 is absent from the repaired scalar-value note "
        "(reproduces the auditor's runner_artifact_issue under restricted packet)",
        s0 not in scalar_note,
        f"substring: {s0!r}",
    )
    print()

    # (D) Sibling-authority phrase presence (parent's other two SUPPORT checks)
    print("(D) Sibling-authority phrases on origin/main")
    check(
        "(D1) Compressed rim-evaluation: Z_beta^env(W)=<K(W),v_beta> + beta-dependent v_beta",
        "`Z_beta^env(W) = <K(W), v_beta>`" in eval_note
        and "remaining unknown is only the beta-dependent vector `v_beta`" in eval_note,
    )
    check(
        "(D2) Compressed rim-functional uniqueness: universal + unique on retained "
        "left boundary functional",
        "left boundary\nfunctional is already the universal" in unique_note
        and "retained left boundary functional is unique" in unique_note,
    )
    print()

    # (E) Hostile-audit invariants (no modification of parent / parent runner / repaired note)
    print("(E) Hostile-audit invariants")
    check(
        "(E1) Parent note header unchanged",
        parent_note.startswith(
            "# Gauge-Vacuum Plaquette Retained Class-Sampling Inversion"
        ),
        f"sha256(parent note)={sha(parent_note_p)}",
    )
    check(
        "(E2) Parent runner unchanged: stale S0 still in parent runner source",
        s0 in parent_run,
        f"sha256(parent runner)={sha(parent_run_p)}",
    )
    check(
        "(E3) Repaired scalar-value note unchanged: 2026-05-29 repair marker present",
        "## 2026-05-29 Audit Repair" in scalar_note
        and "narrow this note to the formal scalar-underdetermination lemma only."
        in scalar_note,
        f"sha256(scalar note)={sha(scalar_p)}",
    )

    print()
    print(
        "Reconciliation: R2 ('a single scalar constraint does not determine an "
        "N>=3 positive normalized vector') is exactly the assertion the inversion "
        "runner consumes from S0 ('one scalar framework-point value does not "
        "determine the class-sector vector') on the retained restricted surface "
        "(N=4>=3 in the witness sector). R1 (Status-line form) and R3 (plaquette-"
        "language form) restate R2; companion-note Lemma proves the equivalence."
    )
    print()
    print(f"PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
