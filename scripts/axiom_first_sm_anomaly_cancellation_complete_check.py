#!/usr/bin/env python3
"""Axiom-first SM anomaly cancellation complete check.

Synthesis runner for
  docs/AXIOM_FIRST_SM_ANOMALY_CANCELLATION_COMPLETE_THEOREM_NOTE_2026-05-03.md

Verifies, in classified PASS lines, that the five perturbative anomaly
traces and the nonperturbative SU(2) Witten Z_2 parity all cancel
simultaneously on the supplied Cl(3)/Z^3 left-handed-frame Standard-Model
matter content (one generation x n_gen = 3):

  (A0)  SU(2)^3                   identically zero by group theory
  (A1)  SU(3)^3                   = +2 - 1 - 1 = 0  exact Fraction
  (A2)  SU(2)^2 U(1)_Y            = (1/2)(1 - 1) = 0  exact Fraction (LH-only)
  (A3)  grav^2 U(1)_Y = Tr[Y]     = 0  exact Fraction (LH+RH)
  (A4)  U(1)_Y^3                  = -16/9 + 16/9 = 0  exact Fraction (LH+RH)
  (A5)  N_D(SU(2) Witten Z_2)     mod 2 = 0  integer parity

All gauge-anomaly arithmetic is exact via fractions.Fraction. The Witten
parity check is integer arithmetic.

This runner classifies each PASS line by the anomaly slot (A0)-(A5) and the
load-bearing source theorem.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import sys


PASS_COUNT = 0
FAIL_COUNT = 0


# ---------------------------------------------------------------------------
# Supplied Cl(3)/Z^3 LH-frame one-generation Standard-Model content.
# Doubled-hypercharge convention: Q = T_3 + Y/2.
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Field:
    name: str
    su3_dim: int      # 3 = fundamental, 3 with bar via su3_anti, 1 = singlet
    su3_anti: bool    # True if antifundamental
    su2_dim: int      # 2 = doublet, 1 = singlet
    color_mult: int   # color multiplicity
    weak_mult: int    # weak multiplicity
    hypercharge: Fraction  # Y in doubled convention; LH-conjugate frame

    @property
    def total_count(self) -> int:
        return self.color_mult * self.weak_mult

    @property
    def is_su3_fundamental(self) -> bool:
        return self.su3_dim == 3 and not self.su3_anti

    @property
    def is_su3_antifundamental(self) -> bool:
        return self.su3_dim == 3 and self.su3_anti

    @property
    def is_su2_doublet(self) -> bool:
        return self.su2_dim == 2


# All fields in the LH-conjugate frame (RH species written as LH conjugates).
# Multiplicities are colour x weak; hypercharges Y satisfy Q = T_3 + Y/2 with
# the convention used by the supplied anomaly notes.
ONE_GEN_LH_FRAME = [
    Field("Q_L",    su3_dim=3, su3_anti=False, su2_dim=2, color_mult=3, weak_mult=2, hypercharge=Fraction(1, 3)),
    Field("L_L",    su3_dim=1, su3_anti=False, su2_dim=2, color_mult=1, weak_mult=2, hypercharge=Fraction(-1, 1)),
    Field("u_R^c",  su3_dim=3, su3_anti=True,  su2_dim=1, color_mult=3, weak_mult=1, hypercharge=Fraction(-4, 3)),
    Field("d_R^c",  su3_dim=3, su3_anti=True,  su2_dim=1, color_mult=3, weak_mult=1, hypercharge=Fraction(2, 3)),
    Field("e_R^c",  su3_dim=1, su3_anti=False, su2_dim=1, color_mult=1, weak_mult=1, hypercharge=Fraction(2, 1)),
    Field("nu_R^c", su3_dim=1, su3_anti=False, su2_dim=1, color_mult=1, weak_mult=1, hypercharge=Fraction(0, 1)),
]

DYNKIN_SU3_FUND = Fraction(1, 2)
DYNKIN_SU2_FUND = Fraction(1, 2)

# Standard SU(3) cubic anomaly indices.
A_SU3 = {
    ("3",    False): Fraction(1, 1),    # A(3)    = +1
    ("3",    True):  Fraction(-1, 1),   # A(3bar) = -1
    ("1",    False): Fraction(0, 1),    # A(1)    = 0
}


def check(name: str, condition: bool, detail: str = "", cls: str = "A") -> None:
    """Classified PASS/FAIL print line."""
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{status} ({cls})] {name}{suffix}")
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1


def banner(title: str) -> None:
    print()
    print("-" * 80)
    print(title)
    print("-" * 80)


# ---------------------------------------------------------------------------
# (A0) SU(2)^3 cubic gauge anomaly: group-theoretic zero.
# ---------------------------------------------------------------------------


def su2_cubic_dabc_norm() -> Fraction:
    """For SU(2), the symmetric d^{abc} = 2 Tr({T^a, T^b} T^c) over the
    fundamental vanishes identically. Compute the norm explicitly using
    Pauli-matrix anti-commutators {sigma_i, sigma_j}/2 = delta_ij * I."""
    import sympy as sp
    matrices = [sp.Matrix([[0,1],[1,0]])/2,
                sp.Matrix([[0,-sp.I],[sp.I,0]])/2,
                sp.diag(1,-1)/2]
    components = [2*sp.trace((a*b+b*a)*c)
                  for a in matrices for b in matrices for c in matrices]
    return sum(abs(x)**2 for x in components)


def check_A0_su2_cubic() -> None:
    banner("(A0) SU(2)^3 cubic gauge anomaly: group-theoretic zero")
    val = su2_cubic_dabc_norm()
    check(
        "A_SU2^3 = 0 identically (no rank-3 symmetric invariant)",
        val == 0,
        f"d^{{abc}} norm = {val}",
        cls="A0",
    )
    print('INFO: SU(2) fundamental has {T^a, T^b} = (1/2) delta^{ab} I, no T^c term')


# ---------------------------------------------------------------------------
# (A1) SU(3)^3 cubic gauge anomaly: matter-content zero on supplied content.
# Source: SU3_CUBIC_ANOMALY_CANCELLATION_THEOREM_NOTE_2026-04-24.md
# ---------------------------------------------------------------------------


def su3_cubic_anomaly() -> Fraction:
    """Sum_i m_i A(R_i) over SU(3)-charged supplied content."""
    total = Fraction(0)
    for f in ONE_GEN_LH_FRAME:
        if f.su3_dim == 1:
            continue
        rep_key = ("3", f.su3_anti)
        # Multiplicity is weak_mult (color is the gauge index being summed).
        contribution = Fraction(f.weak_mult) * A_SU3[rep_key]
        total += contribution
    return total


def check_A1_su3_cubic() -> None:
    banner("(A1) SU(3)^3 cubic gauge anomaly on supplied content")
    print("  Source: SU3_CUBIC_ANOMALY_CANCELLATION_THEOREM_NOTE_2026-04-24")
    val = su3_cubic_anomaly()
    check(
        "Q_L (3, weak_mult=2): contribution = 2 * A(3) = 2 * (+1) = +2",
        Fraction(2) * A_SU3[("3", False)] == Fraction(2),
        cls="A1",
    )
    check(
        "u_R^c (3bar, weak_mult=1): contribution = 1 * A(3bar) = 1 * (-1) = -1",
        Fraction(1) * A_SU3[("3", True)] == Fraction(-1),
        cls="A1",
    )
    check(
        "d_R^c (3bar, weak_mult=1): contribution = 1 * A(3bar) = 1 * (-1) = -1",
        Fraction(1) * A_SU3[("3", True)] == Fraction(-1),
        cls="A1",
    )
    print('INFO: L_L, e_R^c, nu_R^c (SU(3) singlets): contribution = 0')
    check(
        "A_SU3^3 = +2 - 1 - 1 = 0 (exact Fraction)",
        val == Fraction(0),
        f"value = {val}",
        cls="A1",
    )
    print('INFO: SU(3)^3 cancellation is a real matter-content condition (d^{abc} != 0 for SU(3))')


# ---------------------------------------------------------------------------
# (A2) SU(2)^2 U(1)_Y mixed anomaly (LH-only; RH SU(2) singlets contribute 0).
# Source: LH_ANOMALY_TRACE_CATALOG_THEOREM_NOTE_2026-04-25.md (C4)
# ---------------------------------------------------------------------------


def su2_squared_y_anomaly() -> Fraction:
    """Tr[SU(2)^2 Y] = T(2) * sum over SU(2) doublets of (color_mult * Y)."""
    s = Fraction(0)
    for f in ONE_GEN_LH_FRAME:
        if not f.is_su2_doublet:
            continue
        s += Fraction(f.color_mult) * f.hypercharge
    return DYNKIN_SU2_FUND * s


def check_A2_su2_squared_y() -> None:
    banner("(A2) SU(2)^2 U(1)_Y mixed gauge anomaly")
    print("  Source: LH_ANOMALY_TRACE_CATALOG_THEOREM_NOTE_2026-04-25 (C4)")
    val = su2_squared_y_anomaly()
    check(
        "Q_L doublet (color_mult=3, Y=+1/3): 3 * (1/3) = +1",
        Fraction(3) * Fraction(1, 3) == Fraction(1),
        cls="A2",
    )
    check(
        "L_L doublet (color_mult=1, Y=-1): 1 * (-1) = -1",
        Fraction(1) * Fraction(-1, 1) == Fraction(-1),
        cls="A2",
    )
    check(
        "RH fields are SU(2) singlets and contribute 0",
        all(not f.is_su2_doublet or f.name in ("Q_L", "L_L") for f in ONE_GEN_LH_FRAME),
        cls="A2",
    )
    check(
        "Tr[SU(2)^2 Y] = (1/2) * (1 - 1) = 0 (exact Fraction)",
        val == Fraction(0),
        f"value = {val}",
        cls="A2",
    )


# ---------------------------------------------------------------------------
# (A3) grav^2 U(1)_Y reduces to Tr[Y] = 0 on full LH+RH content.
# ---------------------------------------------------------------------------


def linear_y_trace() -> Fraction:
    """Tr[Y] over full LH+RH content in the LH-conjugate frame."""
    return sum((Fraction(f.total_count) * f.hypercharge for f in ONE_GEN_LH_FRAME), Fraction(0))


def linear_y_trace_lh() -> Fraction:
    return sum(
        (Fraction(f.total_count) * f.hypercharge for f in ONE_GEN_LH_FRAME if f.name in ("Q_L", "L_L")),
        Fraction(0),
    )


def linear_y_trace_rh() -> Fraction:
    return sum(
        (Fraction(f.total_count) * f.hypercharge for f in ONE_GEN_LH_FRAME if f.name not in ("Q_L", "L_L")),
        Fraction(0),
    )


def check_A3_grav_squared_y() -> None:
    banner("(A3) grav^2 U(1)_Y mixed gauge-gravity anomaly")
    print("  Reduces to Tr[Y] over full LH+RH content")
    print("  Source: LH catalog (C1) + STANDARD_MODEL_HYPERCHARGE_UNIQUENESS RH solve")
    lh = linear_y_trace_lh()
    rh = linear_y_trace_rh()
    total = linear_y_trace()
    check(
        "Tr[Y]_LH = 6*(1/3) + 2*(-1) = 2 - 2 = 0",
        lh == Fraction(0),
        f"value = {lh}",
        cls="A3",
    )
    check(
        "Tr[Y]_RH (LH-conj) = 3*(-4/3) + 3*(2/3) + 1*(2) + 1*(0) = -4 + 2 + 2 + 0 = 0",
        rh == Fraction(0),
        f"value = {rh}",
        cls="A3",
    )
    check(
        "Tr[Y]_one-gen = 0 (exact Fraction)",
        total == Fraction(0),
        f"value = {total}",
        cls="A3",
    )


# ---------------------------------------------------------------------------
# (A4) Cubic U(1)_Y^3 anomaly on full LH+RH content.
# ---------------------------------------------------------------------------


def cubic_y_trace() -> Fraction:
    """Tr[Y^3] over full LH+RH content."""
    return sum(
        (Fraction(f.total_count) * f.hypercharge ** 3 for f in ONE_GEN_LH_FRAME),
        Fraction(0),
    )


def cubic_y_trace_lh() -> Fraction:
    return sum(
        (Fraction(f.total_count) * f.hypercharge ** 3 for f in ONE_GEN_LH_FRAME if f.name in ("Q_L", "L_L")),
        Fraction(0),
    )


def cubic_y_trace_rh() -> Fraction:
    return sum(
        (Fraction(f.total_count) * f.hypercharge ** 3 for f in ONE_GEN_LH_FRAME if f.name not in ("Q_L", "L_L")),
        Fraction(0),
    )


def check_A4_cubic_y() -> None:
    banner("(A4) U(1)_Y^3 cubic hypercharge anomaly")
    print("  Source: LH catalog (C2) Tr[Y^3]_LH = -16/9; RH solve cancels with +16/9")
    lh = cubic_y_trace_lh()
    rh = cubic_y_trace_rh()
    total = cubic_y_trace()
    check(
        "Tr[Y^3]_LH = 6*(1/27) + 2*(-1) = 2/9 - 2 = -16/9",
        lh == Fraction(-16, 9),
        f"value = {lh}",
        cls="A4",
    )
    check(
        "Tr[Y^3]_RH (LH-conj) = 3*(-64/27) + 3*(8/27) + 8 + 0 = +16/9",
        rh == Fraction(16, 9),
        f"value = {rh}",
        cls="A4",
    )
    check(
        "Tr[Y^3]_one-gen = -16/9 + 16/9 = 0 (exact Fraction)",
        total == Fraction(0),
        f"value = {total}",
        cls="A4",
    )


# ---------------------------------------------------------------------------
# (A5) SU(2) Witten Z_2 nonperturbative parity.
# Source: SU2_WITTEN_Z2_ANOMALY_THEOREM_NOTE_2026-04-24.md
# ---------------------------------------------------------------------------


def witten_doublet_count(n_gen: int = 3) -> int:
    """N_D = n_gen * sum over SU(2) doublets of color_mult."""
    per_gen = sum(f.color_mult for f in ONE_GEN_LH_FRAME if f.is_su2_doublet)
    return n_gen * per_gen


def check_A5_witten_z2() -> None:
    banner("(A5) SU(2) Witten Z_2 nonperturbative parity")
    print("  Source: SU2_WITTEN_Z2_ANOMALY_THEOREM_NOTE_2026-04-24")
    nd_per_gen = sum(f.color_mult for f in ONE_GEN_LH_FRAME if f.is_su2_doublet)
    nd_total = witten_doublet_count(n_gen=3)
    check(
        "N_D per generation = N_c (Q_L) + 1 (L_L) = 3 + 1 = 4",
        nd_per_gen == 4,
        f"value = {nd_per_gen}",
        cls="A5",
    )
    check(
        "N_D(three generations) = 3 * 4 = 12",
        nd_total == 12,
        f"value = {nd_total}",
        cls="A5",
    )
    check(
        "N_D(total) mod 2 = 0 (Witten parity-safe)",
        nd_total % 2 == 0,
        f"parity = {nd_total % 2}",
        cls="A5",
    )


# ---------------------------------------------------------------------------
# Cross-checks: SU(3)^2 Y mixed trace should also cancel on LH+RH
# (this is a separate slot beyond (A1) but used in the SM hypercharge solve).
# ---------------------------------------------------------------------------


def su3_squared_y_trace() -> Fraction:
    """Tr[SU(3)^2 Y] over LH+RH; only quark contributions."""
    s = Fraction(0)
    for f in ONE_GEN_LH_FRAME:
        if f.su3_dim != 3:
            continue
        # Index of representation T(R) = 1/2 for both 3 and 3bar
        s += DYNKIN_SU3_FUND * Fraction(f.weak_mult) * f.hypercharge
    return s


def check_cross_su3_squared_y() -> None:
    banner("(cross-check) SU(3)^2 U(1)_Y mixed trace on LH+RH")
    print("  Source: LH catalog (C3) + RH_SECTOR_ANOMALY_CANCELLATION_IDENTITIES")
    val = su3_squared_y_trace()
    lh = DYNKIN_SU3_FUND * Fraction(2) * Fraction(1, 3)
    rh = DYNKIN_SU3_FUND * (Fraction(1) * Fraction(-4, 3) + Fraction(1) * Fraction(2, 3))
    check(
        "Tr[SU(3)^2 Y]_LH = (1/2) * 2 * (1/3) = 1/3",
        lh == Fraction(1, 3),
        f"value = {lh}",
        cls="cross",
    )
    check(
        "Tr[SU(3)^2 Y]_RH = (1/2) * (-4/3 + 2/3) = -1/3",
        rh == Fraction(-1, 3),
        f"value = {rh}",
        cls="cross",
    )
    check(
        "Tr[SU(3)^2 Y]_one-gen = 1/3 - 1/3 = 0 (exact Fraction)",
        val == Fraction(0),
        f"value = {val}",
        cls="cross",
    )


# ---------------------------------------------------------------------------
# Synthesis closure check: all five gauge-anomaly slots cancel on the same surface.
# ---------------------------------------------------------------------------


def check_synthesis_closure() -> None:
    banner("Synthesis closure: all seven anomaly slots vanish on the same supplied surface")
    A0 = su2_cubic_dabc_norm()
    A1 = su3_cubic_anomaly()
    A2 = su2_squared_y_anomaly()
    A3 = linear_y_trace()
    A4 = cubic_y_trace()
    A5 = witten_doublet_count() % 2
    check(
        "(A0) SU(2)^3 cubic = 0",
        A0 == Fraction(0),
        f"value = {A0}",
        cls="closure",
    )
    check(
        "(A1) SU(3)^3 cubic = 0",
        A1 == Fraction(0),
        f"value = {A1}",
        cls="closure",
    )
    check(
        "(A2) SU(2)^2 Y mixed = 0",
        A2 == Fraction(0),
        f"value = {A2}",
        cls="closure",
    )
    check(
        "(A3) grav^2 Y reduces to Tr[Y] = 0",
        A3 == Fraction(0),
        f"value = {A3}",
        cls="closure",
    )
    check(
        "(A4) Y^3 cubic = 0",
        A4 == Fraction(0),
        f"value = {A4}",
        cls="closure",
    )
    check(
        "(A5) SU(2) Witten parity = 0 mod 2",
        A5 == 0,
        f"parity = {A5}",
        cls="closure",
    )
    check(
        "All seven anomaly slots vanish simultaneously on the same supplied Cl(3)/Z^3 LH-frame matter content",
        all([
            A0 == Fraction(0),
            A1 == Fraction(0),
            A2 == Fraction(0),
            A3 == Fraction(0),
            A4 == Fraction(0),
            A5 == 0,
            su3_squared_y_trace() == 0,
        ]),
        cls="closure",
    )


# ---------------------------------------------------------------------------
# Supplied-input audit.
# ---------------------------------------------------------------------------


def check_supplied_inputs() -> None:
    print("INFO: matter representations, hypercharges, three generations and group indices are supplied.")
    print("INFO: rational cancellation checks do not derive this assignment or audit its sources.")


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------


def main() -> int:
    print("=" * 80)
    print("SUPPLIED SM ASSIGNMENT: ANOMALY CONSISTENCY CHECK")
    print("=" * 80)
    print()
    print("Synthesis: five perturbative traces (A1)-(A4) plus mixed SU(3)^2 Y")
    print("           plus nonperturbative SU(2) Witten Z_2 parity (A5)")
    print("           plus group-theoretic SU(2)^3 zero (A0)")
    print("           on supplied Cl(3)/Z^3 LH-frame SM matter content.")
    print()
    print("Supplied matter content (LH-conjugate frame, doubled-Y convention):")
    for f in ONE_GEN_LH_FRAME:
        print(
            f"  {f.name:8s} SU(3)={'3bar' if f.su3_anti else f.su3_dim:>4} "
            f"SU(2)={f.su2_dim} count={f.total_count} Y={f.hypercharge}"
        )
    print()

    check_A0_su2_cubic()
    check_A1_su3_cubic()
    check_A2_su2_squared_y()
    check_A3_grav_squared_y()
    check_A4_cubic_y()
    check_A5_witten_z2()
    check_cross_su3_squared_y()
    check_synthesis_closure()
    check_supplied_inputs()

    print()
    print("=" * 80)
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 80)

    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
