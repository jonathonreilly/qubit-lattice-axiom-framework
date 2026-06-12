#!/usr/bin/env python3
"""Self-check runner for the outcome-factorization weakening note."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "PRODUCT_FORM_PREMISE_WEAKENS_TO_OUTCOME_FACTORIZATION_BOUNDED_NOTE_2026-06-12.md"
GLEASON_PATH = ROOT / "docs" / "GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md"
BUSCH_PATH = ROOT / "docs" / "BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, ok: bool, detail: str = "") -> None:
        status = "PASS" if ok else "FAIL"
        if ok:
            self.passed += 1
        else:
            self.failed += 1
        suffix = f" :: {detail}" if detail else ""
        print(f"{status:4} {self.passed + self.failed:02d} {label}{suffix}")


def kron(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    return sp.kronecker_product(a, b)


def tr(m: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(m))


def partial_trace_second(rho: sp.Matrix, da: int, db: int) -> sp.Matrix:
    return sp.Matrix(
        da,
        da,
        lambda i, k: sp.simplify(sum(rho[i * db + j, k * db + j] for j in range(db))),
    )


def partial_trace_first(rho: sp.Matrix, da: int, db: int) -> sp.Matrix:
    return sp.Matrix(
        db,
        db,
        lambda j, l: sp.simplify(sum(rho[i * db + j, i * db + l] for i in range(da))),
    )


def normalized_note_text(text: str) -> str:
    return (
        text.replace("`", "")
        .replace("*", "")
        .replace("\n", " ")
        .replace("—", "-")
        .replace("  ", " ")
    )


def main() -> int:
    c = Checks()

    ps, pd, x = sp.symbols("p_s p_d x", nonzero=True)
    denom = ps**2 + pd**2
    q_s = sp.simplify(ps**2 / denom)
    q_d = sp.simplify(pd**2 / denom)
    odds_new = sp.simplify(q_s / q_d)
    c.check(
        "L1 agreement-conditioning uses only m(j,k)=p_j p_k",
        q_s == ps**2 / (ps**2 + pd**2) and q_d == pd**2 / (ps**2 + pd**2),
        f"q_s={q_s}, q_d={q_d}",
    )
    c.check(
        "L1 quotient odds flow is x -> x^2",
        sp.simplify(odds_new.subs(ps, x * pd) - x**2) == 0,
        f"q_s/q_d={odds_new}",
    )

    r, rout = sp.symbols("r r_out", nonnegative=True)
    r_next = sp.simplify((2 * r) ** 2 / 2)
    r_inverse = sp.sqrt(rout / 2)
    c.check(
        "L1b retained coordinate map and inverse",
        r_next == 2 * r**2 and sp.simplify(2 * r_inverse**2 - rout) == 0,
        f"r_next={r_next}, inverse={r_inverse}",
    )

    I3 = sp.eye(3)
    I9 = sp.eye(9)
    P_s = sp.diag(1, 0, 0)
    P_d = sp.diag(0, 1, 1)
    X = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    rho = I9 / 9 + kron(X, X) / 36
    eigs = list(rho.eigenvals().keys())
    c.check(
        "L2 witness is a density matrix",
        tr(rho) == 1 and all(sp.simplify(ev) >= 0 for ev in eigs),
        f"trace={tr(rho)}, eigenvalues={sorted(map(str, eigs))}",
    )

    weights = {
        ("s", "s"): tr(kron(P_s, P_s) * rho),
        ("s", "d"): tr(kron(P_s, P_d) * rho),
        ("d", "s"): tr(kron(P_d, P_s) * rho),
        ("d", "d"): tr(kron(P_d, P_d) * rho),
    }
    expected_weights = {
        ("s", "s"): sp.Rational(1, 9),
        ("s", "d"): sp.Rational(2, 9),
        ("d", "s"): sp.Rational(2, 9),
        ("d", "d"): sp.Rational(4, 9),
    }
    c.check(
        "L2 partition weights factor exactly with p_s=1/3, p_d=2/3",
        weights == expected_weights,
        str(weights),
    )

    exp_ab = tr(rho * kron(X, X))
    exp_a = tr(rho * kron(X, I3))
    exp_b = tr(rho * kron(I3, X))
    corr = sp.simplify(exp_ab - exp_a * exp_b)
    c.check(
        "L2 off-partition observable correlation certifies non-productness",
        corr == sp.Rational(1, 9) and exp_a == 0 and exp_b == 0,
        f"<X tensor X>={exp_ab}, <X>_1={exp_a}, <X>_2={exp_b}, covariance={corr}",
    )

    sigma1 = partial_trace_second(rho, 3, 3)
    sigma2 = partial_trace_first(rho, 3, 3)
    product_of_marginals = kron(sigma1, sigma2)
    c.check(
        "L2 witness differs from sigma1 tensor sigma2; covariance excludes any product representation",
        sigma1 == I3 / 3 and sigma2 == I3 / 3 and rho != product_of_marginals and corr != 0,
        f"sigma1={sigma1}, sigma2={sigma2}",
    )

    s00, s01, s02, s10, s11, s12, s20, s21, s22 = sp.symbols(
        "s00 s01 s02 s10 s11 s12 s20 s21 s22"
    )
    sigma = sp.Matrix([[s00, s01, s02], [s10, s11, s12], [s20, s21, s22]])
    u, a11, a12, a21, a22 = sp.symbols("u a11 a12 a21 a22", nonzero=True)
    det_a = a11 * a22 - a12 * a21
    U = sp.Matrix([[u, 0, 0], [0, a11, a12], [0, a21, a22]])
    U_inv = sp.Matrix(
        [
            [1 / u, 0, 0],
            [0, a22 / det_a, -a12 / det_a],
            [0, -a21 / det_a, a11 / det_a],
        ]
    )
    sigma_frame = sp.simplify(U * sigma * U_inv)
    inv_s = sp.simplify(tr(P_s * sigma_frame) - tr(P_s * sigma))
    inv_d = sp.simplify(tr(P_d * sigma_frame) - tr(P_d * sigma))
    c.check(
        "L3 generic block-frame motion preserves both registered weights",
        inv_s == 0 and inv_d == 0,
        f"delta_s={inv_s}, delta_d={inv_d}",
    )

    half = sp.sqrt(sp.Rational(1, 2))
    V = sp.Matrix([[half, -half, 0], [half, half, 0], [0, 0, 1]])
    sigma_pure_s = sp.diag(1, 0, 0)
    sigma_moved = sp.simplify(V * sigma_pure_s * V.T)
    ps_before = tr(P_s * sigma_pure_s)
    ps_after = sp.simplify(tr(P_s * sigma_moved))
    pd_after = sp.simplify(tr(P_d * sigma_moved))
    c.check(
        "L3 negative control: non-commuting unitary changes weights",
        ps_before == 1 and ps_after == sp.Rational(1, 2) and pd_after == sp.Rational(1, 2),
        f"p_s before={ps_before}, after={ps_after}; p_d after={pd_after}",
    )

    c.check(
        "L4 assembly: factorized outcomes imply flow; frame motion is invisible; witness is strictly weaker",
        sp.simplify(odds_new.subs(ps, x * pd) - x**2) == 0
        and inv_s == 0
        and inv_d == 0
        and weights == expected_weights
        and corr != 0,
    )

    note = NOTE_PATH.read_text(encoding="utf-8")
    gleason = GLEASON_PATH.read_text(encoding="utf-8")
    busch = BUSCH_PATH.read_text(encoding="utf-8")
    normalized = normalized_note_text(note)
    lowered = normalized.lower()

    c.check(
        "B-check Gleason dependency claim phrase is present",
        "m(P) = Tr" in gleason and "Born rule" in gleason,
    )
    c.check(
        "B-check Busch dependency claim phrase is present",
        "m(E) = Tr" in busch and "unique density matrix" in busch,
    )
    c.check(
        "B-check note declares bounded theorem and standard status authority",
        "**Claim type:** bounded_theorem" in note
        and "**Status authority:** independent audit lane only" in note
        and "**Date:** 2026-06-12" in note,
    )
    c.check(
        "B-check scope-only quotes from the unaudited unraveling lane are present",
        "Scope-only context" in note
        and "The stationarity failure is concentrated in the bi-frame" in normalized
        and "cross-edge independence and convolution structure are not tested here." in normalized,
    )
    c.check(
        "B-check firewall sentences are present",
        "named, not discharged" in lowered
        and "does not consume the unaudited" in lowered
        and "the occupancy binary stays open" in lowered
        and "r-d stays proposed" in lowered,
    )
    terminal_words = re.compile(r"\b(closes?|closed|closing|closure|settles?|settled)\b", re.IGNORECASE)
    c.check(
        "B-check terminal-status language absent from note",
        terminal_words.search(note) is None,
    )

    links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", note)
    expected_links = [
        (
            "`GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`",
            "GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md",
        ),
        (
            "`BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`",
            "BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md",
        ),
        ("`MINIMAL_AXIOMS_2026-06-05.md`", "MINIMAL_AXIOMS_2026-06-05.md"),
    ]
    c.check(
        "B-check markdown link inventory is exactly the three dependency links",
        links == expected_links,
        str(links),
    )

    context_names = [
        "UNRAVELED_STEP_LAW_BI_INVARIANT_QUASI_STATIONARITY_SPLIT_BOUNDED_THEOREM_NOTE_2026-06-10.md",
        "UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md",
        "wave-10 reduction note",
        "wave-8a anatomy note",
        "FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md",
        "POST_RECORD_FLOW_THERMAL_STABLE_SETTING_CERTIFICATE_2026-06-06.md",
    ]
    context_backticked = all(f"`{name}`" in note for name in context_names)
    context_linked = any(target in " ".join(link[1] for link in links) for target in context_names)
    c.check(
        "B-check unraveling and companion context names are backticked only",
        context_backticked and not context_linked,
    )
    c.check(
        "B-check No-promotion statement present",
        "**No-promotion statement:**" in note
        and "does not promote, demote, or set the audit status" in normalized
        and "independent audit lane is the single status authority" in normalized,
    )
    c.check(
        "B-check Does-NOT list preserves the open residue boundaries",
        "Does not discharge or assert outcome-level independence" in note
        and "Does not adopt R-D" in note
        and "Does not select a cell" in note
        and "Does not fix `r`" in note
        and "Does not decide the occupancy binary" in note,
    )

    print(f"\nSUMMARY: PASS={c.passed} FAIL={c.failed}")
    if c.passed < 14 or c.failed:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
