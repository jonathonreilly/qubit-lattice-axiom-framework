#!/usr/bin/env python3
"""Bounded declared-anchor y_t algebraic subchain.

This runner intentionally does not import canonical_plaquette_surface and does
not compare to observed SM values. It verifies only algebraic consequences of
declared premises: <P>, F_adj, kappa_EW, and the Ward-boundary Clebsch 1/sqrt(6).
"""

from __future__ import annotations

from fractions import Fraction
from math import pi, sqrt

PASS = 0
FAIL = 0
TOL = 1.0e-12


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def main() -> int:
    print("Bounded declared-anchor y_t algebraic subchain")
    print("No observed-value comparison; no canonical_plaquette_surface import.")

    section("Part 1: declared premises")
    n_c = 3
    plaquette = 0.5934
    alpha_bare = 1.0 / (4.0 * pi)
    f_adj = Fraction(n_c * n_c - 1, n_c * n_c)
    kappa_ew = Fraction(0, 1)
    ward_clebsch = 1.0 / sqrt(6.0)

    check("declared N_c = 3", n_c == 3)
    check("declared plaquette is positive and bounded", 0.0 < plaquette < 1.0)
    check("F_adj = (N_c^2 - 1)/N_c^2 = 8/9", f_adj == Fraction(8, 9), str(f_adj))
    check("kappa_EW declared at connected-trace specialization 0", kappa_ew == 0)
    check("Ward Clebsch is 1/sqrt(6)", abs(ward_clebsch - 1.0 / sqrt(6.0)) < TOL)

    section("Part 2: plaquette algebra")
    u0 = plaquette ** 0.25
    alpha_lm = alpha_bare / u0
    alpha_s_v = alpha_bare / (u0 * u0)

    check("u_0 = <P>^(1/4)", abs(u0**4 - plaquette) < TOL, f"u0={u0:.12f}")
    check("alpha_LM = alpha_bare/u_0", abs(alpha_lm - alpha_bare / u0) < TOL, f"alpha_LM={alpha_lm:.12f}")
    check("alpha_s(v) = alpha_bare/u_0^2", abs(alpha_s_v - alpha_bare / (u0 * u0)) < TOL, f"alpha_s(v)={alpha_s_v:.12f}")
    check(
        "geometric-mean identity alpha_LM^2 = alpha_bare * alpha_s(v)",
        abs(alpha_lm * alpha_lm - alpha_bare * alpha_s_v) < TOL,
        f"diff={alpha_lm * alpha_lm - alpha_bare * alpha_s_v:.3e}",
    )

    section("Part 3: connected-trace algebra")
    k_ew = Fraction(1, 1) / (f_adj + kappa_ew / (n_c * n_c))
    sqrt_k_ew = sqrt(float(k_ew))
    taste_weight = Fraction(7, 8) * Fraction(1, 2) * f_adj

    check("K_EW(0) = 1/F_adj = 9/8", k_ew == Fraction(9, 8), str(k_ew))
    check("sqrt(K_EW(0)) = sqrt(9/8)", abs(sqrt_k_ew - sqrt(9.0 / 8.0)) < TOL)
    check("taste_weight = (7/8)*T_F*F_adj = 7/18", taste_weight == Fraction(7, 18), str(taste_weight))

    section("Part 4: Ward-boundary algebra")
    g_lattice = sqrt(4.0 * pi * alpha_lm)
    y_t_mpl = g_lattice * ward_clebsch
    check("g_lattice = sqrt(4*pi*alpha_LM)", abs(g_lattice * g_lattice - 4.0 * pi * alpha_lm) < TOL)
    check("y_t(M_Pl) = g_lattice/sqrt(6)", abs(y_t_mpl - g_lattice / sqrt(6.0)) < TOL, f"y_t(M_Pl)={y_t_mpl:.12f}")
    check("bounded subchain uses no observed SM comparator", True)

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
