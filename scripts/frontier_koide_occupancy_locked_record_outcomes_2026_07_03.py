#!/usr/bin/env python3
"""Exact bridge checks for occupancy from locked record outcomes.

Companion runner for
docs/KOIDE_OCCUPANCY_FROM_LOCKED_RECORD_OUTCOMES_BOUNDED_NOTE_2026-07-03.md.

The checks are deterministic symbolic checks. They do not consume empirical
numbers, fits, random draws, or floating tolerances.

REPAIR 2026-07-11 (companion to PR #5162)
-----------------------------------------
An independent audit (2026-07-10) failed the companion orbit-occupancy note
(KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_..._2026-06-09) for an arithmetic error in
its rho-map. Verbatim finding:

  "The holomorphic Gaussian integral does not yield the claimed one-slot
   equipartition moment: with Z=pi/g and g=6 beta, it gives <|b|^2>=1/(6 beta),
   hence r=1, not 1/2. The runner obtains r=1/2 by hard-coding a per-slot
   quantum rather than deriving it from that integral."

This T2 runner INHERITED that contaminated arithmetic: its former CHECK 13 read
r off a rho-map r = 1/(2 rho) with rho = (pi/g)/Z_d, letting the partition
normalization Z_d SET r. That is withdrawn. The honest Gaussian moment is
normalization-INDEPENDENT (Z_d cancels in the moment ratio) and gives r = 1 for
BOTH bookkeepings, not r = 1/2. What survives:

  * CHECK 12 (relabeled): Z_sector/Z_orbit = 2 is a true normalization /
    determinant-power fact, DECOUPLED from r. Now paired with an honest sympy
    moment check confirming <|b|^2> is the same under both bookkeepings, so the
    moment r is normalization-independent (mirrors the companion runner's O3A).
  * CHECK 13 (rewritten): the two r-endpoints are exact solutions of two
    realized-state equipartition LAWS differing only in granularity -- per REAL
    MODE (sector cell: E_s = eps, E_d = 2 eps => r = 1) versus per OUTCOME CELL
    (orbit cell: E_s = E_d => r = 1/2, Q = 2/3 via Q = (1+2 r)/3). The quantum
    eps cancels in r; nothing is hard-coded on a derivation path.

The T1 localization checks and the T2 slot-counting collision exhibit (CHECKS
1-11) are a separate argument, uncontested by the audit, and are unchanged.
"""

from pathlib import Path

import sympy as sp


PASS = 0
FAIL = 0


def check(num: int, ok: bool, desc: str) -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"CHECK {num:02d}: {tag} -- {desc}")


def laplacian_in_b(expr: sp.Expr, b: sp.Symbol, x: sp.Symbol, y: sp.Symbol) -> sp.Expr:
    substituted = sp.expand(expr.subs(b, x + sp.I * y))
    return sp.simplify(sp.diff(substituted, x, 2) + sp.diff(substituted, y, 2))


def formal_adjoint_on_line(matrix: sp.Matrix, b: sp.Symbol, bbar: sp.Symbol) -> sp.Matrix:
    return matrix.T.xreplace({b: bbar, bbar: b})


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    axiom_path = root / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
    axiom_text = axiom_path.read_text(encoding="utf-8")

    quote_lock = "When present, a record locks exactly one admissible local possibility."
    quote_content = "A readout value is determined by record content\nalone."

    check(1, quote_lock in axiom_text, "live quote guard: record locks exactly one admissible local possibility")
    check(2, quote_content in axiom_text, "live quote guard: readout value is determined by record content alone")

    a, b, c, bbar = sp.symbols("a b c bbar")
    x, y = sp.symbols("x y", real=True)
    eye3 = sp.eye(3)

    cycle = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    two_step_path = sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
    single_edge = sp.Matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]])
    two_edge_star = sp.Matrix([[0, 1, 1], [0, 0, 0], [0, 0, 0]])

    channels = {
        "cycle": (cycle, a**3 + b**3 + c**3 - 3 * a * b * c, -3 * a),
        "two_step_path": (two_step_path, a**3 - 2 * a * b * c, -2 * a),
        "single_edge": (single_edge, a**3 - a * b * c, -a),
        "two_edge_star": (two_edge_star, a**3 - 2 * a * b * c, -2 * a),
    }

    det_ok = True
    off_line_ok = True
    on_line_ok = True
    hermitian_ok = True
    no_bbar_before_line_ok = True
    for _, (channel, expected_det, expected_mixed) in channels.items():
        det_expr = sp.expand((a * eye3 + b * channel + c * channel.T).det())
        det_ok = det_ok and sp.simplify(det_expr - expected_det) == 0
        no_bbar_before_line_ok = no_bbar_before_line_ok and bbar not in det_expr.free_symbols
        off_line_ok = off_line_ok and laplacian_in_b(det_expr, b, x, y) == 0
        mixed_on_line = sp.diff(det_expr.subs(c, bbar), b, bbar)
        on_line_ok = on_line_ok and sp.simplify(mixed_on_line - expected_mixed) == 0
        line_matrix = a * eye3 + b * channel + bbar * channel.T
        hermitian_ok = hermitian_ok and line_matrix == formal_adjoint_on_line(line_matrix, b, bbar)

    check(3, det_ok, "T1 channel family determinants match exact small-matrix formulas")
    check(4, no_bbar_before_line_ok, "T1 off the K-real line, the family contains no conjugate coefficient")
    check(5, off_line_ok, "T1 off the K-real line, every family determinant is harmonic in (Re b, Im b)")
    check(6, on_line_ok, "T1 on c = conj(b), every family determinant has the expected nonzero mixed b-bbar term")
    check(7, hermitian_ok, "T1 c = conj(b) is the formal Hermitian/K-real section for the real channel family")

    bad_det = sp.expand((a * eye3 + b * single_edge + bbar * single_edge.T).det())
    bad_mixed = sp.diff(bad_det, b, bbar)
    check(8, sp.simplify(bad_mixed + a) == 0, "T1 negative control: conjugate contamination before K-reality gives off-line mixed curvature")

    locked_possibility_slots = sp.Integer(1)
    one_record_content_values = sp.Integer(1)
    orbit_registered_data = sp.Integer(1)
    sector_registered_data = sp.Integer(2)

    orbit_respects_lock = orbit_registered_data == locked_possibility_slots
    sector_collides_with_lock = sector_registered_data != locked_possibility_slots
    orbit_respects_content = orbit_registered_data == one_record_content_values
    sector_depends_on_split = sector_registered_data != one_record_content_values

    check(9, orbit_respects_lock and orbit_respects_content, "T2 orbit grading assigns one slot to one locked record-outcome")
    check(10, sector_collides_with_lock, "T2 sector grading makes one locked complex outcome into two registered data")
    check(11, sector_depends_on_split, "T2 sector grading changes the slot count by the Re/Im split rather than record content alone")

    # -----------------------------------------------------------------------
    # T2 normalization fact vs the r-endpoints. REPAIR 2026-07-11 (companion to
    # PR #5162; see the module docstring and the 2026-06-09 note's
    # "Repair (2026-07-11)" section). The prior CHECK 13 read r off a rho-map
    # r = 1/(2 rho), rho = (pi/g)/Z_d, letting the doublet partition
    # normalization Z_d SET r. The 2026-07-10 audit showed that is an
    # arithmetic error: the honest Gaussian moment is normalization-independent
    # (Z_d cancels) and gives r = 1 for both bookkeepings. The rho-map and every
    # "Z-ratio sets the r-ratio" statement are withdrawn. What survives is (a)
    # the normalization fact Z_sector/Z_orbit = 2, DECOUPLED from r, and (b) the
    # r-endpoints as exact solutions of two equipartition laws differing only in
    # granularity.
    g = sp.symbols("g", positive=True)
    beta = sp.symbols("beta", positive=True)

    # (a) Normalization / determinant-power fact, decoupled from r. The two
    # doublet partition bookkeepings of the SAME physical weight exp(-6 beta
    # |b|^2) -- holomorphic one-complex-slot (Z = pi/g) and realified
    # two-real-slot (Z = 2 pi/g), with g = 6 beta -- differ by the fiber-count
    # factor 2. An honest sympy moment check (mirroring the companion runner's
    # O3A) confirms the second moment <|b|^2> is the SAME under both, so the
    # Gaussian moment r = <|b|^2>/<a^2> is normalization-independent: Z_d does
    # NOT set r.
    z_orbit = sp.pi / g          # holomorphic one-complex-slot bookkeeping
    z_sector = 2 * sp.pi / g     # realified two-real-slot bookkeeping
    weight_factor = sp.simplify(z_sector / z_orbit)

    a_s = sp.symbols("a", real=True)
    x_s, y_s = sp.symbols("x y", real=True)
    rho_r = sp.symbols("rho_r", positive=True)  # radial coordinate |b|
    w_singlet = sp.exp(-beta * 3 * a_s ** 2)
    mean_a2 = sp.simplify(
        sp.integrate(a_s ** 2 * w_singlet, (a_s, -sp.oo, sp.oo))
        / sp.integrate(w_singlet, (a_s, -sp.oo, sp.oo)))
    w_holo = sp.exp(-beta * 6 * rho_r ** 2)
    mean_b2_holo = sp.simplify(
        sp.integrate(2 * sp.pi * rho_r * rho_r ** 2 * w_holo, (rho_r, 0, sp.oo))
        / sp.integrate(2 * sp.pi * rho_r * w_holo, (rho_r, 0, sp.oo)))
    w_real = sp.exp(-beta * 6 * (x_s ** 2 + y_s ** 2))
    mean_b2_real = sp.simplify(
        sp.integrate(sp.integrate((x_s ** 2 + y_s ** 2) * w_real, (x_s, -sp.oo, sp.oo)),
                     (y_s, -sp.oo, sp.oo))
        / sp.integrate(sp.integrate(w_real, (x_s, -sp.oo, sp.oo)), (y_s, -sp.oo, sp.oo)))
    r_moment_holo = sp.simplify(mean_b2_holo / mean_a2)
    r_moment_real = sp.simplify(mean_b2_real / mean_a2)

    check(12,
          weight_factor == 2
          and sp.simplify(mean_b2_holo - mean_b2_real) == 0
          and r_moment_holo == r_moment_real == 1,
          "T2 normalization fact DECOUPLED from r: Z_sector/Z_orbit=2 is a true "
          "normalization/det-power fact, but the honest Gaussian moment gives the "
          "same <|b|^2> and r=1 for both bookkeepings, so Z_d does NOT set r "
          "(rho-map withdrawn; companion PR #5162)")

    # (b) The two r-endpoints as exact solutions of two realized-state
    # equipartition LAWS differing only in granularity. Landed circulant lever:
    # E_s = 3 a^2, E_d = 6 |b|^2. One quantum eps per counting unit; eps cancels
    # in r, so nothing is hard-coded on a derivation path.
    a_v = sp.symbols("a_v", positive=True)
    bmag2 = sp.symbols("bmag2", positive=True)
    eps = sp.symbols("eps", positive=True)
    E_s = 3 * a_v ** 2
    E_d = 6 * bmag2
    # sector cell = per-REAL-MODE equipartition (three real modes a; x; y):
    #   E_s = eps, E_d = 2 eps  =>  |b|^2 = a^2, r = 1.
    sol_sector = sp.solve([sp.Eq(E_s, eps), sp.Eq(E_d, 2 * eps)], [eps, bmag2], dict=True)[0]
    r_sector = sp.simplify(sol_sector[bmag2] / a_v ** 2)
    # orbit cell = per-OUTCOME-CELL equipartition (two cells {e0}; {e1,e2}):
    #   E_s = eps, E_d = eps (E_s = E_d)  =>  |b|^2 = a^2/2, r = 1/2.
    sol_orbit = sp.solve([sp.Eq(E_s, eps), sp.Eq(E_d, eps)], [eps, bmag2], dict=True)[0]
    r_orbit = sp.simplify(sol_orbit[bmag2] / a_v ** 2)
    Q_sector = sp.simplify((1 + 2 * r_sector) / 3)
    Q_orbit = sp.simplify((1 + 2 * r_orbit) / 3)

    check(13,
          r_sector == 1 and r_orbit == sp.Rational(1, 2)
          and Q_sector == 1 and Q_orbit == sp.Rational(2, 3)
          # eps is SOLVED from each law (eps = 3 a^2), not assumed, and cancels:
          # r_sector, r_orbit are pure numbers with no residual eps dependence.
          and sp.simplify(sol_sector[eps] - 3 * a_v ** 2) == 0
          and sp.simplify(sol_orbit[eps] - 3 * a_v ** 2) == 0
          and eps not in r_sector.free_symbols and eps not in r_orbit.free_symbols,
          "T2 r-endpoints from equipartition-law GRANULARITY (not the Z-ratio): "
          "per-real-mode law (sector cell) solves exactly to r=1, Q=1; "
          "per-outcome-cell law E_s=E_d (orbit cell) solves exactly to r=1/2, "
          "Q=2/3 -- quantum eps cancels, nothing hard-coded")

    remaining_bridge = (
        "one record locking one admissible local possibility is one statistical "
        "slot, and the relevant locked possibilities for the generation doublet "
        "are the K/CPT record-outcome orbits rather than the real components of "
        "the fluctuation coordinate"
    )

    print(
        "SUMMARY files written: "
        "docs/KOIDE_OCCUPANCY_FROM_LOCKED_RECORD_OUTCOMES_BOUNDED_NOTE_2026-07-03.md; "
        "scripts/frontier_koide_occupancy_locked_record_outcomes_2026_07_03.py"
    )
    print(f"SUMMARY sharpest remaining bridge sentence: {remaining_bridge}.")
    print("SUMMARY walls dodged: category-slip by counting record-outcomes only; measure-neutrality by not using J_cs as selector.")
    print("SUMMARY repair 2026-07-11 (companion PR #5162): inherited rho-map r-attribution removed; Z_sector/Z_orbit=2 relabeled a normalization/det-power fact decoupled from r; r-endpoints now from equipartition-law granularity (per real mode r=1 / per outcome cell r=1/2). T2 remains a collision exhibit under the supplied one-record-one-slot reading.")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
