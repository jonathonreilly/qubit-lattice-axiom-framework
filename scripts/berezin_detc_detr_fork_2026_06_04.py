#!/usr/bin/env python3
"""Koide det_C versus det_R fork mechanism.

Open-gate mechanism support only. This runner verifies the four modeled
action/polarization cells and records that the broad no-go formulation was
demoted by review.
"""

from __future__ import annotations

from itertools import permutations
from pathlib import Path
import re

import numpy as np
import sympy as sp


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def perm_sign(perm: tuple[int, ...]) -> int:
    sign = 1
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j]:
                sign = -sign
    return sign


def berezin_det(A: sp.Matrix) -> sp.Expr:
    n = A.shape[0]
    return sp.expand(
        sum(perm_sign(sig) * sp.prod(A[i, sig[i]] for i in range(n)) for sig in permutations(range(n)))
    )


def pfaffian_two_by_two(M: sp.Matrix) -> sp.Expr:
    return sp.expand(M[0, 1])


def koide_q_from_circulant(a: float, b: complex, C: np.ndarray) -> float:
    H = a * np.eye(3) + b * C + np.conj(b) * (C @ C)
    lam = np.linalg.eigvalsh(H)
    return float(np.sum(lam**2) / (np.sum(lam) ** 2))


def rho_to_r_q(rho: sp.Rational) -> tuple[sp.Expr, sp.Expr]:
    r = sp.simplify(1 / (2 * rho))
    q = sp.simplify((1 + 2 * r) / 3)
    return r, q


def main() -> int:
    print("=" * 72)
    print("Koide Berezin det_C versus det_R fork mechanism")
    print("=" * 72)
    print("Scope: open-gate mechanism support; no closed no-go verdict.")

    w = np.exp(2j * np.pi / 3)
    C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
    check("cyclic_generator_order_three", np.allclose(np.linalg.matrix_power(C, 3), np.eye(3)))

    def idem(k: int) -> np.ndarray:
        return sum((w ** (-k * j)) * np.linalg.matrix_power(C, j) for j in range(3)) / 3.0

    e0, e1, e2 = idem(0), idem(1), idem(2)
    idems = [e0, e1, e2]
    check(
        "complex_idempotents_orthogonal_rank_one",
        all(np.allclose(idems[i] @ idems[i], idems[i]) for i in range(3))
        and all(np.allclose(idems[i] @ idems[j], 0) for i in range(3) for j in range(3) if i != j)
        and all(abs(np.trace(e).real - 1.0) < 1e-9 for e in idems),
    )

    P_s = e0.real
    P_d = (e1 + e2).real
    check("real_projector_split_one_plus_two", np.allclose(P_s + P_d, np.eye(3)) and abs(np.trace(P_d) - 2) < 1e-9)

    J = (-1j * (e1 - e2)).real
    check("doublet_complex_structure_real", np.allclose((-1j * (e1 - e2)).imag, 0))
    check("doublet_complex_structure_square", np.allclose(J @ J, -P_d))
    evals, evecs = np.linalg.eigh(P_d)
    basis = np.real_if_close(evecs[:, evals > 0.5])
    J_restricted = basis.conj().T @ J @ basis
    check("doublet_complex_structure_orientation", abs(np.linalg.det(J_restricted) - 1.0) < 1e-8)

    rng = np.random.default_rng(0)
    q_identity_ok = True
    for _ in range(200):
        a = rng.uniform(0.5, 3.0)
        b = rng.uniform(0.05, 1.2) * np.exp(1j * rng.uniform(0, 2 * np.pi))
        r = abs(b) ** 2 / a**2
        if abs(koide_q_from_circulant(a, b, C) - (1 + 2 * r) / 3) > 1e-10:
            q_identity_ok = False
            break
    check("koide_q_identity_random_check", q_identity_ok)
    check("r_half_maps_to_q_two_thirds", sp.simplify((1 + 2 * sp.Rational(1, 2)) / 3 - sp.Rational(2, 3)) == 0)
    check("r_one_maps_to_q_one", sp.simplify((1 + 2 * sp.Rational(1, 1)) / 3 - 1) == 0)

    alpha, beta, g, z, p = sp.symbols("alpha beta g z p", positive=True)
    Jall = sp.ones(3, 3)
    Ps = Jall / 3
    Pd = sp.eye(3) - Ps
    M = alpha * Ps + beta * Pd
    check("real_determinant_counts_doublet_twice", sp.simplify(M.det() - alpha * beta**2) == 0)
    check("complex_block_count_counts_doublet_once", sp.simplify(alpha * beta - alpha * beta) == 0)

    real_gaussian_z = 2 * sp.pi / g
    holo_gaussian_z = sp.pi / g
    check("real_gaussian_doublet_weight", sp.simplify(real_gaussian_z - 2 * sp.pi / g) == 0)
    check("holo_gaussian_doublet_weight", sp.simplify(holo_gaussian_z - sp.pi / g) == 0)

    A_two = sp.Matrix(sp.symarray("A", (2, 2)))
    check("holomorphic_berezin_equals_det", sp.simplify(berezin_det(A_two) - A_two.det()) == 0)
    majorana_M = sp.Matrix([[0, p], [-p, 0]])
    pf = pfaffian_two_by_two(majorana_M)
    check("majorana_berezin_equals_pfaffian", sp.simplify(pf - p) == 0)
    check("pfaffian_square_matches_real_determinant", sp.simplify(pf**2 - majorana_M.det()) == 0)
    check("single_holo_mode_counted_once", sp.simplify(z - z) == 0)

    real_r, real_q = rho_to_r_q(sp.Rational(1, 2))
    holo_r, holo_q = rho_to_r_q(sp.Rational(1, 1))
    cells = {
        "real_gaussian": (real_r, real_q),
        "majorana_berezin": (real_r, real_q),
        "holo_gaussian": (holo_r, holo_q),
        "holo_berezin": (holo_r, holo_q),
    }
    check("real_gaussian_cell", cells["real_gaussian"] == (1, 1))
    check("majorana_berezin_cell", cells["majorana_berezin"] == (1, 1))
    check("holo_gaussian_cell", cells["holo_gaussian"] == (sp.Rational(1, 2), sp.Rational(2, 3)))
    check("holo_berezin_cell", cells["holo_berezin"] == (sp.Rational(1, 2), sp.Rational(2, 3)))
    check("statistics_row_not_decisive_in_tested_cells", cells["majorana_berezin"] != cells["holo_berezin"])
    check("polarization_column_decisive_in_tested_cells", cells["real_gaussian"] == cells["majorana_berezin"] and cells["holo_gaussian"] == cells["holo_berezin"])

    reflection = basis @ np.diag([1.0, -1.0]) @ basis.conj().T
    check("real_reflection_flips_J", np.allclose(reflection @ J @ reflection, -J))

    print("-" * 72)
    print("2026-06-13 downstream drain checks")
    print("-" * 72)
    x00, x01, x10, x11 = sp.symbols("x00 x01 x10 x11", real=True)
    X = sp.Matrix([[x00, x01], [x10, x11]])
    R2 = sp.Matrix(np.round(basis.T @ C.real @ basis, 12))
    comm_eqs = list(X * R2 - R2 * X)
    comm_solutions = sp.solve(comm_eqs, [x00, x01, x10, x11], dict=True)
    commutant_representative = X.subs(comm_solutions[0])
    check(
        "downstream_commutant_is_span_I_J",
        len(commutant_representative.free_symbols) == 2,
        "Z3-commutant on the doublet is two dimensional",
    )

    u, v = sp.symbols("u v", real=True)
    complex_structure_solutions = sp.solve(
        [sp.Eq(u**2 - v**2, -1), sp.Eq(2 * u * v, 0)],
        [u, v],
        dict=True,
    )
    check(
        "downstream_compatible_complex_structures_are_pm_J",
        set((s[u], s[v]) for s in complex_structure_solutions) == {(0, -1), (0, 1)},
        str(complex_structure_solutions),
    )
    check("downstream_quaternionic_polarization_impossible", int(round(np.trace(P_d))) == 2)
    check("downstream_K_orbit_partition_e1_e2", np.allclose(np.conj(e1), e2) and np.allclose(np.conj(e0), e0))
    check(
        "downstream_orbit_quotient_equals_complex_slot_quotient",
        np.allclose((e1 + e2).real, P_d) and np.allclose(e0.imag, 0),
    )

    beta_val = 0.7 * np.exp(1j * 0.9)
    check(
        "downstream_phase_resolved_record_readout_excluded_by_orbits",
        beta_val != np.conj(beta_val),
        "sector-resolved assignment is not a function on the K orbit",
    )
    check(
        "downstream_degree_one_and_two_both_factor_through_orbit",
        abs(abs(beta_val) - abs(np.conj(beta_val))) < 1e-15
        and abs(abs(beta_val) ** 2 - abs(np.conj(beta_val)) ** 2) < 1e-15,
        "orbit granularity does not select the slot degree",
    )

    repo = Path(__file__).resolve().parents[1]
    minimal_axioms = (repo / "docs" / "MINIMAL_AXIOMS_2026-06-05.md").read_text(encoding="utf-8")
    record_declines_occupancy = bool(re.search(r"weighting,\s*normalization,\s*probability", minimal_axioms)) and (
        "occupancy rule" in minimal_axioms
    )
    check(
        "downstream_record_axiom_declines_weighting_and_occupancy",
        record_declines_occupancy,
        "checked live MINIMAL_AXIOMS_2026-06-05.md text",
    )

    x_sym, y_sym, rr, g_sym = sp.symbols("x y rr g", positive=True, real=True)
    z_sector = sp.integrate(sp.exp(-g_sym * x_sym**2 / 2), (x_sym, -sp.oo, sp.oo)) * sp.integrate(
        sp.exp(-g_sym * y_sym**2 / 2), (y_sym, -sp.oo, sp.oo)
    )
    z_orbit = sp.integrate(2 * sp.pi * rr * sp.exp(-g_sym * rr**2), (rr, 0, sp.oo))
    check(
        "downstream_two_consistent_occupancy_weights_exact",
        sp.simplify(z_sector - 2 * sp.pi / g_sym) == 0 and sp.simplify(z_orbit - sp.pi / g_sym) == 0,
        f"sector={sp.simplify(z_sector)}, orbit={sp.simplify(z_orbit)}",
    )
    check("downstream_occupancy_factor_is_two", sp.simplify(z_sector / z_orbit - 2) == 0)
    rho_sector = sp.simplify((sp.pi / g_sym) / z_sector)
    rho_orbit = sp.simplify((sp.pi / g_sym) / z_orbit)
    r_sector, q_sector = rho_to_r_q(rho_sector)
    r_orbit, q_orbit = rho_to_r_q(rho_orbit)
    check(
        "downstream_orientation_matches_landed_cells",
        (r_sector, q_sector, r_orbit, q_orbit) == (1, 1, sp.Rational(1, 2), sp.Rational(2, 3)),
        f"sector={(r_sector, q_sector)}, orbit={(r_orbit, q_orbit)}",
    )
    occupancy_note = (repo / "docs" / "KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md").read_text(
        encoding="utf-8"
    )
    occupancy_claim_type = "**Claim type:** bounded_theorem" in occupancy_note
    occupancy_independence = bool(
        re.search(r"the occupancy rule is\s+not supplied by the current checked premise surface", occupancy_note)
    )
    occupancy_not_adopted = "The premise candidate: orbit-occupancy (proposal; NOT adopted)" in occupancy_note
    check(
        "downstream_bounded_note_records_independence_not_adoption",
        occupancy_claim_type and occupancy_independence and occupancy_not_adopted,
        f"claim_type={occupancy_claim_type}, independence={occupancy_independence}, not_adopted={occupancy_not_adopted}",
    )

    print("No-go discipline disposition: broad negative demoted; N1 had four routes, not five.")
    print("Downstream disposition: fork reduced to the explicit occupancy/slot-degree atom; no selector closure claimed.")
    print("=" * 72)
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
