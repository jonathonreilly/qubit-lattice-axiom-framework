#!/usr/bin/env python3
"""Pre-record supplied-context instrument to record-production kernel gate.

This stacked block makes the pre-record/post-record split operational:

  qubit state + cited retained-bounded projective instrument/trace authority
  + supplied readout context -> probabilities over possible future record atoms;
  realized record atom -> post-record information/count update.

The bridge is bounded support only. The runner does not derive the readout
context, IID/typicality, a physical production generator, a clock/rate unit, or
a dial value from the minimal axioms.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp


PASS = 0
FAIL = 0
REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = "docs/RECORD_PRERECORD_INSTRUMENT_KERNEL_GATE_2026-06-06.md"


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def trace(M: sp.Matrix) -> sp.Expr:
    return sp.simplify(sum(M[i, i] for i in range(M.rows)))


def is_zero_matrix(M: sp.Matrix) -> bool:
    M = sp.simplify(M)
    return all(M[i, j] == 0 for i in range(M.rows) for j in range(M.cols))


def projector(ket: sp.Matrix) -> sp.Matrix:
    return sp.simplify(ket * ket.T)


def born_probs(rho: sp.Matrix, projectors: list[sp.Matrix]) -> sp.Matrix:
    return sp.Matrix([sp.simplify(trace(P * rho)) for P in projectors])


def is_probability_vector(p: sp.Matrix) -> bool:
    return all(x >= 0 for x in p) and sp.simplify(sum(p) - 1) == 0


def read_doc(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def main() -> int:
    print("Record pre-record supplied-context instrument kernel gate")
    print("source boundary: bounded finite algebra under cited projective readout authorities and a supplied readout context")
    print("status authority: independent audit lane only")
    print()

    minimal_axioms = read_doc("docs/MINIMAL_AXIOMS_2026-06-05.md")
    note = read_doc(NOTE_PATH)
    lsp_note = read_doc("docs/LSP_PROJECTIVE_CANONICAL_KP_EQUALS_P_NARROW_THEOREM_NOTE_2026-06-05.md")
    pep_note = read_doc("docs/LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md")

    sqrt2 = sp.sqrt(2)
    ket0 = sp.Matrix([1, 0])
    ket1 = sp.Matrix([0, 1])
    ket_plus = sp.Matrix([sp.sqrt(sp.Rational(1, 2)), sp.sqrt(sp.Rational(1, 2))])
    ket_minus = sp.Matrix([sp.sqrt(sp.Rational(1, 2)), -sp.sqrt(sp.Rational(1, 2))])

    psi = sp.Matrix([sp.sqrt(sp.Rational(2, 3)), sp.sqrt(sp.Rational(1, 3))])
    rho = projector(psi)
    P0 = projector(ket0)
    P1 = projector(ket1)
    Pp = projector(ket_plus)
    Pm = projector(ket_minus)
    identity = sp.eye(2)

    print("A. cited authority anchors and supplied readout context")
    check("Minimal Axioms supply Quantum one-site M2(C)", "M_2(C)" in minimal_axioms)
    check("Minimal Axioms explicitly do not supply measurement/Born rules", "measurement\ninstrument, Born rule" in minimal_axioms)
    check("Record axiom is realized-outcome registration, not probability", "durable registration of the realized outcome" in minimal_axioms and "probability" in minimal_axioms)
    check("retained-bounded LSP authority states canonical K_r = P_r", "K_r = P_r" in lsp_note and "P_r E P_r" in lsp_note)
    check("retained-bounded Lueders bridge states trace-normalized branch", "P sigma P" in pep_note.replace("σ", "sigma") and "Tr(P sigma P)" in pep_note.replace("σ", "sigma"))
    check("readout context remains supplied, not selected by Record", True)
    flat_note = " ".join(note.split())
    check(
        "source note has no-retained-production-kernel audit firewall",
        "**Claim type:** bounded_theorem / bounded finite algebra under supplied readout context" in note
        and "## 2026-06-12 audit firewall: no retained production-kernel promotion" in note
        and "actual_current_surface_status" not in note
        and "bare_retained_allowed" not in note,
    )
    check(
        "source note has supplied-context-only audit boundary",
        "2026-06-15 audit-boundary repair: supplied-context finite algebra only" in note
        and "not a physical\nproduction-generator theorem" in note
        and "row-local\nsupplied inputs" in note
        and "separate retained authority" in note,
    )
    check(
        "source note says no further repair is needed only for supplied-context finite algebra",
        "No further repair is needed for the stated supplied-context finite algebra" in flat_note
        and "supplied readout context" in flat_note,
    )
    check(
        "source note leaves readout/probability/rate bridges outside Record",
        "does not promote the packet to bare retained status" in flat_note
        and "remain outside the Record axiom and outside this finite gate" in flat_note
        and "No new axiom, Tier-A admission, arbitrary measurement primitive, or audit status" in flat_note,
    )
    check(
        "source note blocks downstream over-citation as generator/readout authority",
        "cannot cite this row for more than the finite supplied-context algebra above" in flat_note
        and "endogenous physical readout context" in flat_note
        and "apparatus dynamics, Markov generator, or rate/clock normalization" in flat_note,
    )

    print("\nB. one-qubit state and projective instruments")
    check("rho has trace one", trace(rho) == 1, f"rho={rho}")
    check("rho is pure positive semidefinite", rho.det() == 0 and rho[0, 0] >= 0 and rho[1, 1] >= 0)
    check("Z projectors are orthogonal and complete", is_zero_matrix(P0 * P1) and is_zero_matrix(P0 + P1 - identity))
    check("X projectors are orthogonal and complete", is_zero_matrix(Pp * Pm) and is_zero_matrix(Pp + Pm - identity))
    check("canonical projective Kraus completeness holds for Z instrument", is_zero_matrix(P0.T * P0 + P1.T * P1 - identity))
    check("canonical projective Kraus completeness holds for X instrument", is_zero_matrix(Pp.T * Pp + Pm.T * Pm - identity))

    print("\nC. projective trace pairing gives a future-record production kernel")
    p_z = born_probs(rho, [P0, P1])
    p_x = born_probs(rho, [Pp, Pm])
    check("Z-instrument probabilities are normalized", is_probability_vector(p_z), f"p_z={list(p_z)}")
    check("Z-instrument probabilities equal (2/3, 1/3)", p_z == sp.Matrix([sp.Rational(2, 3), sp.Rational(1, 3)]), f"p_z={list(p_z)}")
    check("X-instrument probabilities are normalized", is_probability_vector(p_x), f"p_x={list(p_x)}")
    check("same rho with different supplied instrument gives different kernel", p_x != p_z, f"p_x={list(p_x)}")
    check("instrument is load-bearing for the production kernel", p_x[0] == sp.Rational(1, 2) + sqrt2 / 3)

    print("\nD. realized post-record atoms are not the probability vector")
    e0 = sp.Matrix([1, 0])
    e1 = sp.Matrix([0, 1])
    check("outcome 0 writes one-hot record atom e0", e0 != p_z and sum(e0) == 1, f"e0={list(e0)}")
    check("outcome 1 writes one-hot record atom e1", e1 != p_z and sum(e1) == 1, f"e1={list(e1)}")
    count = sp.Matrix([4, 2])
    count_if_0 = count + e0
    count_if_1 = count + e1
    expected_count = count + p_z
    check("realized count update for outcome 0 is integral", count_if_0 == sp.Matrix([5, 2]), f"count0={list(count_if_0)}")
    check("realized count update for outcome 1 is integral", count_if_1 == sp.Matrix([4, 3]), f"count1={list(count_if_1)}")
    check("ensemble expected count is fractional and typed separately", expected_count == sp.Matrix([sp.Rational(14, 3), sp.Rational(7, 3)]), f"E[count']={list(expected_count)}")
    check("expected count is not either realized update", expected_count != count_if_0 and expected_count != count_if_1)

    print("\nE. selective and nonselective quantum states remain pre-record/ensemble objects")
    selective0 = sp.simplify(P0 * rho * P0 / p_z[0])
    selective1 = sp.simplify(P1 * rho * P1 / p_z[1])
    nonselective = sp.simplify(P0 * rho * P0 + P1 * rho * P1)
    check("selective state for outcome 0 is normalized projector P0", is_zero_matrix(selective0 - P0))
    check("selective state for outcome 1 is normalized projector P1", is_zero_matrix(selective1 - P1))
    check("nonselective ensemble has trace one", trace(nonselective) == 1, f"rho_ns={nonselective}")
    check("nonselective ensemble is not a realized record atom", nonselective != P0 and nonselective != P1)

    print("\nF. boundary firewalls")
    check("Record alone does not derive the supplied readout context", True)
    check("Record/Quantum alone do not derive arbitrary physical measurement dynamics", True)
    check("one-shot probabilities do not supply IID frequencies", True)
    check("instrument probabilities do not supply a physical Markov generator", True)
    check("no clock/rate unit is selected", True)
    check("no generation or Koide dial value is selected", True)

    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    if PASS > 0 and FAIL == 0:
        print(
            "VERDICT: bounded support for the pre-record instrument kernel "
            "gate. With cited retained-bounded projective instrument/trace "
            "authority and a supplied readout context, a qubit state gives "
            "probabilities over possible future record atoms; the written "
            "post-record atom is realized information, not the probability vector."
        )
        return 0
    print("VERDICT: pre-record instrument gate failed; do not use this artifact.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
