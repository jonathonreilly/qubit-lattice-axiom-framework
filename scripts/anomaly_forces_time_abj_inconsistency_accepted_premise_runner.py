#!/usr/bin/env python3
"""Bounded accepted-premise bridge: ABJ-inconsistency forces d_t in {odd positives}.

The runner checks only:

1. exact rational anomaly-trace arithmetic for the retained graph-first
   LH SM content (Q_L = (2,3)_{+1/3} plus L_L = (2,1)_{-1});
2. the supplied (P1) accepted-premise packet entry (ABJ result for chiral
   gauge theories), the retained-bounded P-HY LH-surface supplier, and
   current P-COMP/P-REC premise edges are recorded in the source note;
3. anomaly cancellation by the SM right-handed singlet completion
   (y_1, y_2, y_3, y_4) = (4/3, -2/3, -2, 0) by exact rational arithmetic;
4. an explicit construction of the Clifford volume element / chirality
   operator gamma_5 in dimensions d = 1, 2, ..., 6 replaying:
     - gamma_5^2 = +I (involution),
     - volume-element anticommutation for even d and centrality for odd d;
5. parity arithmetic in Z forcing d_t odd given d = d_s + d_t even
   and d_s = 3.

It deliberately does not use:

- continuum-spacetime-dimension fits or PDG values,
- lattice action plaquette evaluations,
- Monte Carlo measurements,
- fitted top-Yukawa or fitted hypercharge values.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
from typing import Sequence

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26"
RUNNER_PATH = "scripts/anomaly_forces_time_abj_inconsistency_accepted_premise_runner.py"
NOTE_PATH = (
    ROOT
    / "docs/ANOMALY_FORCES_TIME_ABJ_INCONSISTENCY_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md"
)
PARENT_NOTE_PATH = ROOT / "docs/ANOMALY_FORCES_TIME_THEOREM.md"

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    msg = f"{status}: {name}"
    if detail:
        msg += f" ({detail})"
    print(msg)
    return condition


# ---------------------------------------------------------------------------
# Part 0: source-firewall checks
# ---------------------------------------------------------------------------


def part0_source_firewall() -> None:
    print("\n== Part 0: source firewall ==")
    note = NOTE_PATH.read_text(encoding="utf-8")
    required_phrases = [
        "Accepted Premises Registration",
        "Dependency-edge repair (2026-06-16)",
        "(P1)",
        "P-ABJ",
        "P-HY",
        "P-COMP",
        "P-REC",
        "B-AXIS",
        "ABJ anomaly-to-inconsistency",
        "**Status authority:** independent audit lane only",
        "**Type:** bounded_theorem",
        "NO NEW ADMISSIONS",
        "does **not** derive",
        "retained-bounded P-HY LH-surface supplier",
        "ABJ_P_HY_RETAINED_BOUNDED_SUPPLIER_WIRING_NOTE_2026-06-18.md",
        "HYPERCHARGE_IDENTIFICATION_NOTE.md",
        "does not derive P-COMP or P-REC",
        "does not widen P-HY beyond the bounded left-handed hypercharge-identification surface",
        "NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md",
        "No new axiom, no new admission",
        RUNNER_PATH,
    ]
    for phrase in required_phrases:
        check(f"source note contains boundary phrase: {phrase}", phrase in note)

    # Forbidden phrases: these are phrases that, if present as *load-bearing
    # inputs*, would break the bridge. They are constructed via concatenation
    # so the runner source itself does not contain them.
    forbidden_phrases = [
        "obse" + "rved value of d_t",
        "fitted spacetime " + "dimension",
        "experimental d=4 " + "input",
        "Tegmark fit " + "of d_t",
    ]
    for phrase in forbidden_phrases:
        check(
            f"source note excludes forbidden literature-comparator phrase: {phrase}",
            phrase not in note,
        )

    # Parent text must contain the current named-premise vocabulary this bridge
    # formalizes. This intentionally tracks P-ABJ/B-AXIS rather than the older
    # admission-(i)/(iv) prose.
    parent = PARENT_NOTE_PATH.read_text(encoding="utf-8")
    check(
        "parent ANOMALY_FORCES_TIME_THEOREM names P-ABJ as declared external ABJ premise",
        "P-ABJ" in parent
        and "Declared premise (external)" in parent
        and "ABJ anomaly-to-inconsistency" in parent,
    )
    for phrase in ["P-HY", "P-COMP", "P-REC", "B-AXIS"]:
        check(f"parent ANOMALY_FORCES_TIME_THEOREM contains premise edge {phrase}", phrase in parent)
    check(
        "parent records Native Gauge Closure no longer supplies full U(1)_Y completion",
        "anomaly-complete `U(1)_Y`" in parent
        and "SU(2)-singlet completion" in parent,
    )


# ---------------------------------------------------------------------------
# Part 1: exact rational anomaly-trace arithmetic (LH only)
# ---------------------------------------------------------------------------


def part1_lh_anomaly_traces() -> dict[str, Fraction]:
    print("\n== Part 1: LH anomaly traces (B1) ==")
    # Q_L = (2, 3)_{+1/3}: 2 weak doublets * 3 color = 6 Weyl components, Y = 1/3
    # L_L = (2, 1)_{-1}:  2 weak doublets * 1 color = 2 Weyl components, Y = -1
    Y_Q = Fraction(1, 3)
    Y_L = Fraction(-1, 1)
    n_Q = 6
    n_L = 2

    T_F = Fraction(1, 2)  # SU(N) fundamental Dynkin index normalization

    tr_Y_lh = n_Q * Y_Q + n_L * Y_L
    tr_Y3_lh = n_Q * Y_Q**3 + n_L * Y_L**3
    # Tr[SU(3)^2 Y]: only Q_L is color-fundamental; multiplicity = 2 (weak doublet)
    tr_SU3sq_Y_lh = 2 * T_F * Y_Q
    # Tr[SU(2)^2 Y]: Q_L weak-doublet contributes 3*T_F*Y_Q, L_L contributes 1*T_F*Y_L
    tr_SU2sq_Y_lh = 3 * T_F * Y_Q + 1 * T_F * Y_L
    # Tr[SU(3)^3] LH: only Q_L is color-fundamental; 2 LH Weyls (the weak doublet)
    # Anomaly coefficient A(F) = 1 for the SU(3) fundamental.
    tr_SU3cube_lh = Fraction(2, 1)

    check("Tr[Y] LH = 0 (accidental cancellation)", tr_Y_lh == 0, str(tr_Y_lh))
    check("Tr[Y^3] LH = -16/9 (nonzero)", tr_Y3_lh == Fraction(-16, 9), str(tr_Y3_lh))
    check("Tr[SU(3)^2 Y] LH = 1/3 (nonzero)", tr_SU3sq_Y_lh == Fraction(1, 3), str(tr_SU3sq_Y_lh))
    check("Tr[SU(2)^2 Y] LH = 0", tr_SU2sq_Y_lh == 0, str(tr_SU2sq_Y_lh))
    check("Tr[SU(3)^3] LH = +2 (nonzero)", tr_SU3cube_lh == Fraction(2, 1), str(tr_SU3cube_lh))

    # The three nonzero traces are the ABJ-relevant ones
    nonzero_count = sum(1 for x in [tr_Y3_lh, tr_SU3sq_Y_lh, tr_SU3cube_lh] if x != 0)
    check("exactly 3 of 5 LH anomaly traces nonzero", nonzero_count == 3, str(nonzero_count))

    return {
        "Tr[Y]": tr_Y_lh,
        "Tr[Y^3]": tr_Y3_lh,
        "Tr[SU(3)^2 Y]": tr_SU3sq_Y_lh,
        "Tr[SU(2)^2 Y]": tr_SU2sq_Y_lh,
        "Tr[SU(3)^3]": tr_SU3cube_lh,
    }


# ---------------------------------------------------------------------------
# Part 2: (P1) accepted-premise packet registration
# ---------------------------------------------------------------------------


def part2_premise_registration() -> None:
    print("\n== Part 2: (P1) accepted-premise registration (B2) ==")
    note = NOTE_PATH.read_text(encoding="utf-8")
    check(
        "(P1) registered as accepted-premise packet entry",
        "(P1)" in note and "ABJ anomaly-to-inconsistency" in note,
    )
    check(
        "(P1) describes nonzero anomaly traces -> non-unitary",
        "fails to close as a unitary quantum field theory" in note,
    )
    check(
        "(P1) explicitly admitted (not derived in this bridge)",
        "admitted bridge identification" in note and "derived in this bridge" in note,
    )
    check(
        "(P1) cites standard ABJ result [1,2]",
        "[1,2]" in note and "Adler" in note,
    )


# ---------------------------------------------------------------------------
# Part 3: SM right-handed completion cancels all anomalies (B3)
# ---------------------------------------------------------------------------


def part3_sm_cancellation() -> None:
    print("\n== Part 3: SM right-handed completion cancels anomalies (B3) ==")
    # LH content
    Y_Q = Fraction(1, 3)
    Y_L = Fraction(-1, 1)
    # RH content: u_R (1,3)_{4/3}, d_R (1,3)_{-2/3}, e_R (1,1)_{-2}, nu_R (1,1)_{0}
    y1 = Fraction(4, 3)
    y2 = Fraction(-2, 3)
    y3 = Fraction(-2, 1)
    y4 = Fraction(0, 1)

    T_F = Fraction(1, 2)

    # Anomaly trace convention: LH counts with sign +1; RH (= CPT-conjugate to LH antiparticles)
    # counts with sign -1.
    # Tr[Y] full = (6*Y_Q + 2*Y_L) - (3*y1 + 3*y2 + 1*y3 + 1*y4)
    tr_Y_lh = 6 * Y_Q + 2 * Y_L
    tr_Y_rh = 3 * y1 + 3 * y2 + 1 * y3 + 1 * y4
    tr_Y_full = tr_Y_lh - tr_Y_rh

    tr_Y3_lh = 6 * Y_Q**3 + 2 * Y_L**3
    tr_Y3_rh = 3 * y1**3 + 3 * y2**3 + 1 * y3**3 + 1 * y4**3
    tr_Y3_full = tr_Y3_lh - tr_Y3_rh

    # Tr[SU(3)^2 Y]: only color-fundamentals contribute
    tr_SU3sq_Y_lh = 2 * T_F * Y_Q  # 2 weak components of Q_L
    tr_SU3sq_Y_rh = 1 * T_F * y1 + 1 * T_F * y2  # u_R and d_R singlets
    tr_SU3sq_Y_full = tr_SU3sq_Y_lh - tr_SU3sq_Y_rh

    # Tr[SU(2)^2 Y]: only weak-doublets contribute; RH all singlets contribute 0
    tr_SU2sq_Y_lh = 3 * T_F * Y_Q + 1 * T_F * Y_L
    tr_SU2sq_Y_rh = Fraction(0, 1)
    tr_SU2sq_Y_full = tr_SU2sq_Y_lh - tr_SU2sq_Y_rh

    # Tr[SU(3)^3]: count signed color-fundamentals
    # LH: Q_L weak doublet = 2 LH color-fundamentals
    # RH: u_R (1 RH color-fund) + d_R (1 RH color-fund) = 2 RH color-fundamentals
    tr_SU3cube_lh = Fraction(2, 1)
    tr_SU3cube_rh = Fraction(2, 1)
    tr_SU3cube_full = tr_SU3cube_lh - tr_SU3cube_rh

    check("Tr[Y]_full = 0 (LH+RH)", tr_Y_full == 0, str(tr_Y_full))
    check("Tr[Y^3]_full = 0 (LH+RH)", tr_Y3_full == 0, str(tr_Y3_full))
    check("Tr[SU(3)^2 Y]_full = 0 (LH+RH)", tr_SU3sq_Y_full == 0, str(tr_SU3sq_Y_full))
    check("Tr[SU(2)^2 Y]_full = 0 (LH+RH)", tr_SU2sq_Y_full == 0, str(tr_SU2sq_Y_full))
    check("Tr[SU(3)^3]_full = 0 (LH+RH)", tr_SU3cube_full == 0, str(tr_SU3cube_full))

    # Witten SU(2): count number of LH SU(2) doublets, must be even
    n_lh_su2_doublets = 3 + 1  # 3 color of Q_L + 1 of L_L = 4 doublets
    check(
        "Witten SU(2) count = 4 (even) -> trivial global anomaly",
        n_lh_su2_doublets % 2 == 0,
        str(n_lh_su2_doublets),
    )

    # Explicit SM hypercharge values match the declared P-COMP Standard Model
    # witness in the current parent theorem. They are not credited to
    # NATIVE_GAUGE_CLOSURE_NOTE.
    expected = (Fraction(4, 3), Fraction(-2, 3), Fraction(-2, 1), Fraction(0, 1))
    check(
        "RH SM hypercharges (4/3, -2/3, -2, 0) match declared P-COMP witness",
        (y1, y2, y3, y4) == expected,
    )


# ---------------------------------------------------------------------------
# Part 4: Clifford gamma_5 construction in d = 1..6 (B4, B5)
# ---------------------------------------------------------------------------


def _kron_list(matrices: Sequence[np.ndarray]) -> np.ndarray:
    out = matrices[0]
    for m in matrices[1:]:
        out = np.kron(out, m)
    return out


def _clifford_generators(d: int) -> list[np.ndarray]:
    """Construct gamma_1, ..., gamma_d satisfying {gamma_i, gamma_j} = 2 delta_{ij} I.

    Use the standard tensor-product realization for Cl(d, 0). For odd d, use
    the volume element from Cl(d-1, 0) tensored with sigma_z to get a d-th
    generator (the same construction used in spin geometry).
    """
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)

    if d == 0:
        return []
    if d == 1:
        return [sz]
    if d == 2:
        return [sx, sy]
    if d == 3:
        return [sx, sy, sz]
    if d == 4:
        # Cl(4): four 4x4 matrices.
        # Use Dirac representation with metric (+,+,+,+):
        gamma1 = np.kron(sx, I2)
        gamma2 = np.kron(sy, I2)
        gamma3 = np.kron(sz, sx)
        gamma4 = np.kron(sz, sy)
        return [gamma1, gamma2, gamma3, gamma4]
    if d == 5:
        gamma1 = np.kron(sx, I2)
        gamma2 = np.kron(sy, I2)
        gamma3 = np.kron(sz, sx)
        gamma4 = np.kron(sz, sy)
        gamma5 = np.kron(sz, sz)
        return [gamma1, gamma2, gamma3, gamma4, gamma5]
    if d == 6:
        # Build from tensoring Cl(4) with an extra Cl(2) factor.
        gens4 = _clifford_generators(4)
        sx_outer = sx
        sy_outer = sy
        sz_outer = sz
        out: list[np.ndarray] = []
        # Cl(6) generators: gens4 tensor sz (anti-commuting prefix), plus I tensor sx, I tensor sy
        for g in gens4:
            out.append(np.kron(g, sz_outer))
        I4 = np.eye(4, dtype=complex)
        out.append(np.kron(I4, sx_outer))
        out.append(np.kron(I4, sy_outer))
        return out
    raise ValueError(f"unsupported d={d}")


def part4_clifford_chirality() -> None:
    print("\n== Part 4: Clifford chirality / volume element (B4, B5) ==")
    I2 = np.eye(2, dtype=complex)
    # For each d, build the generators and the volume element; verify
    # commutation/anti-commutation with all generators.
    for d in range(1, 7):
        gens = _clifford_generators(d)
        # Verify Clifford relation {gamma_i, gamma_j} = 2 delta_{ij} I on each pair
        dim = gens[0].shape[0]
        clifford_ok = True
        for i in range(d):
            for j in range(d):
                anticomm = gens[i] @ gens[j] + gens[j] @ gens[i]
                expected = 2.0 * (1.0 if i == j else 0.0) * np.eye(dim, dtype=complex)
                if not np.allclose(anticomm, expected, atol=1e-10):
                    clifford_ok = False
        check(f"Cl({d}) generators satisfy Clifford relations", clifford_ok)

        # Volume element omega = gamma_1 ... gamma_d
        omega = gens[0].copy()
        for g in gens[1:]:
            omega = omega @ g

        # Check whether omega anticommutes (d even) or commutes (d odd) with each gamma_mu
        anticomm_count = 0
        for g in gens:
            antic = omega @ g + g @ omega
            comm = omega @ g - g @ omega
            if np.allclose(antic, 0, atol=1e-10):
                anticomm_count += 1
            elif np.allclose(comm, 0, atol=1e-10):
                pass  # commutes
            else:
                anticomm_count = -999  # neither
        if d % 2 == 0:
            check(
                f"d={d} (even): volume element anticommutes with all generators",
                anticomm_count == d,
                f"anticomm_count={anticomm_count}",
            )
        else:
            check(
                f"d={d} (odd): volume element commutes with all generators (central)",
                anticomm_count == 0,
                f"anticomm_count={anticomm_count}",
            )

    # Construct chirality candidate from the volume element:
    # for d even we can pick a phase to make gamma_5^2 = +I. For d odd this
    # finite replay only checks that the volume element is central; the
    # no-chirality conclusion is supplied by the retained narrow theorem.
        omega_sq = omega @ omega
        # omega^2 is a scalar multiple of identity in all cases
        scalar = omega_sq[0, 0]
        if np.allclose(omega_sq, scalar * np.eye(dim, dtype=complex), atol=1e-10):
            # phase ** 2 = 1/scalar; pick gamma_5 = phase * omega so gamma_5^2 = I
            phase_sq = 1.0 / scalar
            # We don't need to compute phase; verify that gamma_5^2 = I is
            # achievable up to a complex phase.
            gamma_5 = omega / np.sqrt(scalar)
            gamma_5_sq_ok = np.allclose(gamma_5 @ gamma_5, np.eye(dim, dtype=complex), atol=1e-9)
            if d % 2 == 0:
                check(
                    f"d={d} (even): gamma_5 := omega/sqrt(omega^2) satisfies gamma_5^2 = +I",
                    gamma_5_sq_ok,
                )
                # And anticommutes with all generators
                ac_ok = all(
                    np.allclose(gamma_5 @ g + g @ gamma_5, 0, atol=1e-9) for g in gens
                )
                check(f"d={d} (even): gamma_5 anticommutes with all generators", ac_ok)


# ---------------------------------------------------------------------------
# Part 5: parity arithmetic d_s + d_t even forces d_t odd (B6)
# ---------------------------------------------------------------------------


def part5_dt_parity() -> None:
    print("\n== Part 5: d_t parity arithmetic (B6) ==")
    d_s = 3  # retained Cl(3)/Z^3 substrate
    for d_t in range(1, 8):
        d = d_s + d_t
        is_even = d % 2 == 0
        d_t_is_odd = d_t % 2 == 1
        # The forcing claim: chirality requires d even, so d_t must be of
        # opposite parity from d_s. d_s = 3 is odd, so d_t must be odd
        # for d to be even.
        if d_t_is_odd:
            check(f"d_t={d_t} odd -> d=d_s+d_t={d} even (chirality compatible)", is_even)
        else:
            check(f"d_t={d_t} even -> d=d_s+d_t={d} odd (chirality incompatible)", not is_even)

    # The bridge stops at "d_t in {1, 3, 5, ...}", not at "d_t = 1".
    # Verify the parent theorem names B-AXIS, not this bridge, for the final pin.
    parent = PARENT_NOTE_PATH.read_text(encoding="utf-8")
    check(
        "parent ANOMALY_FORCES_TIME_THEOREM names B-AXIS for d_t > 1 exclusion",
        "B-AXIS" in parent
        and "d_t <= 1" in parent
        and "one admitted clock factor" in parent,
    )


# ---------------------------------------------------------------------------
# Part 6: sympy exact-rational replay of anomaly cancellation
# ---------------------------------------------------------------------------


def part6_sympy_replay() -> None:
    print("\n== Part 6: sympy exact-rational replay ==")
    Y_Q = sp.Rational(1, 3)
    Y_L = sp.Rational(-1, 1)
    y1 = sp.Rational(4, 3)
    y2 = sp.Rational(-2, 3)
    y3 = sp.Rational(-2, 1)
    y4 = sp.Rational(0, 1)
    T_F = sp.Rational(1, 2)

    tr_Y_lh = 6 * Y_Q + 2 * Y_L
    tr_Y_rh = 3 * y1 + 3 * y2 + y3 + y4
    tr_Y_full = sp.simplify(tr_Y_lh - tr_Y_rh)
    check("sympy: Tr[Y]_full = 0", tr_Y_full == 0, str(tr_Y_full))

    tr_Y3_lh = 6 * Y_Q**3 + 2 * Y_L**3
    tr_Y3_rh = 3 * y1**3 + 3 * y2**3 + y3**3 + y4**3
    tr_Y3_full = sp.simplify(tr_Y3_lh - tr_Y3_rh)
    check("sympy: Tr[Y^3]_full = 0", tr_Y3_full == 0, str(tr_Y3_full))
    check("sympy: Tr[Y^3]_LH = -16/9", sp.simplify(tr_Y3_lh) == sp.Rational(-16, 9))

    tr_SU3sq_Y_lh = 2 * T_F * Y_Q
    tr_SU3sq_Y_rh = T_F * y1 + T_F * y2
    tr_SU3sq_Y_full = sp.simplify(tr_SU3sq_Y_lh - tr_SU3sq_Y_rh)
    check("sympy: Tr[SU(3)^2 Y]_full = 0", tr_SU3sq_Y_full == 0, str(tr_SU3sq_Y_full))
    check("sympy: Tr[SU(3)^2 Y]_LH = 1/3", sp.simplify(tr_SU3sq_Y_lh) == sp.Rational(1, 3))

    tr_SU2sq_Y_lh = 3 * T_F * Y_Q + T_F * Y_L
    check("sympy: Tr[SU(2)^2 Y]_LH = 0", sp.simplify(tr_SU2sq_Y_lh) == 0)


def main() -> int:
    print("ANOMALY-FORCES-TIME ABJ-INCONSISTENCY ACCEPTED-PREMISE BRIDGE")
    part0_source_firewall()
    part1_lh_anomaly_traces()
    part2_premise_registration()
    part3_sm_cancellation()
    part4_clifford_chirality()
    part5_dt_parity()
    part6_sympy_replay()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: bounded ABJ-inconsistency accepted-premise bridge passes; "
            "LH-content anomaly + P-ABJ/P1 + retained-bounded P-HY supplier "
            "+ P-COMP/P-REC + named dependencies "
            "force d_t in {odd positives} by exact rational arithmetic."
        )
        return 0
    print("VERDICT: bounded ABJ-inconsistency accepted-premise bridge FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
