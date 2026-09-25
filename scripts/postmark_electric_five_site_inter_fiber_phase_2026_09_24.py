#!/usr/bin/env python3
"""Exact five-site cell and principal readout-phase diagnostics.

The algebra is conditional on the supplied one-vacancy hop labels. This
runner checks the signed Casimir regrouping, the primitive five-cell Bloch
symbol, first-order compressions at the same-fiber Bragg crossings, the
period-three character's fiber shift, and the stationary geometry of the
frozen principal inter-fiber phase. It does not approximate the global
finite-spin propagator or prove a fixed-time readout limit.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
from pathlib import Path

import numpy as np
import scipy
import sympy as sp

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ['docs/FAST_VACANCY_MOTION_AFTER_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/POSTMARK_ELECTRIC_CORE_AND_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/POSTMARK_ELECTRIC_EXACT_SIDE_FIXED_INDEX_KERNEL_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/POSTMARK_ELECTRIC_FIVE_SITE_INTER_FIBER_PHASE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/POSTMARK_ELECTRIC_MOVING_INDEX_CELL_SYMBOL_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/ZERO_MODE_AND_GOEGENBAUER_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'scripts/core_derivation.py']

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUTPUT = ROOT / "outputs" / "postmark_moving_index_2026_09_24" / "FIVE_SITE_INTER_FIBER_PHASE_RESULTS.json"
SOURCE_REVISION = "0e6ad8285096ed668816f18caaa6fbbfbd9c50e8"

POS_LEFT = (0, 1, 0, 1, 1, 1, 2, 1, 2, 2, 2, 3, 2, 3, 3)
POS_RIGHT = (0, 0, 0, 1, 0, 1, 1, 1, 2, 1, 2, 2, 2, 3, 2)
NEG_LEFT = (-1, -2, -1, -2, -2, -2, -3, -2, -3, -3, -3, -4, -3, -4, -4)
NEG_RIGHT = (-1, -1, -1, -2, -1, -2, -2, -2, -3, -2, -3, -3, -3, -4, -3)
ELL = (0, 1, 0, 1, 1)
RHO = (0, 0, 0, 1, 0)
PREVIOUS_RHO = (-1, 0, 0, 0, 1)


def f(m: int) -> int:
    return m * (m + 1)


def edge_labels(n: int) -> tuple[int, int]:
    """Supplied signed effective Casimir labels on edge n -> n+1."""
    if n >= 0:
        k, r = divmod(n, 15)
        return 3 * k + POS_LEFT[r], 3 * k + POS_RIGHT[r]
    cells = -(n // 15)
    r = n + 15 * cells
    return 3 * cells + NEG_LEFT[r], 3 * cells + NEG_RIGHT[r]


def load_physical_hops():
    path = HERE / "core_derivation.py"
    spec = importlib.util.spec_from_file_location("five_site_physical_hops", path)
    if spec is None or spec.loader is None:
        raise ImportError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


physical_model = load_physical_hops()


def verify_signed_cell_family() -> dict:
    checked = 0
    for n in range(-1000, 1001):
        h, s = divmod(n, 5)
        ml, mr = edge_labels(n)
        _prev_l, prev_r = edge_labels(n - 1)
        got = (f(ml), f(mr), f(prev_r))
        want = (f(h + ELL[s]), f(h + RHO[s]), f(h + PREVIOUS_RHO[s]))
        if got != want:
            raise ArithmeticError(("signed five-site Casimir identity", n, got, want))
        checked += 1
    if any(POS_LEFT[s + 5] != POS_LEFT[s] + 1 or
           POS_RIGHT[s + 5] != POS_RIGHT[s] + 1 for s in range(10)):
        raise ArithmeticError("positive labels do not shift by five sites")
    if any(NEG_LEFT[s + 5] != NEG_LEFT[s] - 1 or
           NEG_RIGHT[s + 5] != NEG_RIGHT[s] - 1 for s in range(10)):
        raise ArithmeticError("negative labels do not reflect-shift by five sites")
    if any(NEG_LEFT[s] != -POS_LEFT[s] - 1 or
           NEG_RIGHT[s] != -POS_RIGHT[s] - 1 for s in range(15)):
        raise ArithmeticError("negative labels do not obey Casimir reflection")
    return {
        "edges_checked": checked,
        "positive_raw_label_shift": "+1 per five residues",
        "negative_raw_label_shift": "-1 per five residues; converted by f(m)=f(-m-1)",
        "cell_left_offsets": list(ELL),
        "cell_right_offsets": list(RHO),
        "previous_right_offsets": list(PREVIOUS_RHO),
    }


def verify_physical_coefficients() -> dict:
    rows = []
    for spin in (1, 2, 3, 5, 8):
        casimir = spin * (spin + 1)
        lo, hi = -5 * spin, 5 * spin - 4
        path = physical_model.walk_nodes(5 * spin)
        inverse = {state: n for n, state in path.items()}
        worst = 0.0
        for n in range(lo, hi + 1):
            ml, mr = edge_labels(n)
            _prev_l, prev_r = edge_labels(n - 1)
            diagonal = 2.0 - (f(ml) + f(prev_r)) / casimir
            h2 = physical_model.finite_spin_h2(path[n], spin)
            direct_diagonal = -float(h2.get(path[n], 0.0))
            worst = max(worst, abs(diagonal - direct_diagonal))
            if n < hi:
                link = math.sqrt((1.0 - f(ml) / casimir) *
                                 (1.0 - f(mr) / casimir))
                direct_link = -float(h2.get(path[n + 1], 0.0))
                if inverse.get(path[n + 1]) != n + 1:
                    raise ArithmeticError(("physical path coordinate", spin, n))
                worst = max(worst, abs(link - direct_link))
        if worst > 2e-12:
            raise ArithmeticError(("five-site/physical coefficient mismatch", spin, worst))
        rows.append({"spin": spin, "dimension": hi - lo + 1,
                     "max_abs_entry_error": worst})
    return {"sentinel_spins": rows,
            "largest_abs_entry_error": max(r["max_abs_entry_error"] for r in rows)}


def subprincipal_cell_coefficients() -> dict:
    u = sp.symbols("u", real=True)
    alpha = lambda a: sp.expand(u**2 - u * (2 * a + 1))
    diagonal = [sp.factor(alpha(ELL[s]) + alpha(PREVIOUS_RHO[s])
                          ) for s in range(5)]
    links = [sp.factor((alpha(ELL[s]) + alpha(RHO[s])) / 2)
             for s in range(5)]
    expected_d = [2*u**2, 2*u*(u-2), 2*u*(u-1),
                  2*u*(u-2), 2*u*(u-3)]
    expected_b = [u*(u-1), u*(u-2), u*(u-1),
                  u*(u-3), u*(u-2)]
    if any(sp.expand(a-b) != 0 for a,b in zip(diagonal, expected_d)):
        raise ArithmeticError(("subprincipal diagonal", diagonal))
    if any(sp.expand(a-b) != 0 for a,b in zip(links, expected_b)):
        raise ArithmeticError(("subprincipal links", links))
    return {"diagonal_1_over_S": [str(z) for z in diagonal],
            "positive_link_1_over_S": [str(z) for z in links],
            "staggered_offdiagonal_sign": "minus the positive link"}


def verify_bloch_symbol() -> dict:
    maximum_error = 0.0
    samples = 0
    for w in (0.17, 0.53, 0.91):
        for theta in (0.0, 0.37, 1.9, np.pi, 5.4):
            matrix = np.zeros((5, 5), dtype=np.complex128)
            matrix[np.diag_indices(5)] = 2.0 * w
            for s in range(4):
                matrix[s, s + 1] = matrix[s + 1, s] = -w
            matrix[0, 4] = -w * np.exp(-1j * theta)
            matrix[4, 0] = -w * np.exp(1j * theta)
            q = (theta + 2.0 * np.pi * np.arange(5)) / 5.0
            expected = np.sort(2.0 * w - 2.0 * w * np.cos(q))
            error = float(np.max(np.abs(np.linalg.eigvalsh(matrix) - expected)))
            maximum_error = max(maximum_error, error)
            samples += 1
    if maximum_error > 2e-12:
        raise ArithmeticError(("five-cell Bloch eigenvalues", maximum_error))
    return {"matrix_samples": samples,
            "maximum_eigenvalue_error": maximum_error,
            "eigenvalues": "2*w - 2*w*cos((theta+2*pi*l)/5), l=0,...,4"}


def verify_frozen_cell_eigenvalue_expansion() -> dict:
    theta = 0.371
    rows = []
    for spin in (100, 200, 400, 800):
        h = spin // 5
        u = h / spin
        casimir = spin * (spin + 1)
        exact = np.zeros((5, 5), dtype=np.complex128)
        asymptotic = np.zeros((5, 5), dtype=np.complex128)
        w = 1.0 - u * u
        for s in range(5):
            exact[s, s] = (2.0 -
                           (f(h + ELL[s]) + f(h + PREVIOUS_RHO[s])) /
                           casimir)
            alpha_left = u*u - u*(2*ELL[s] + 1)
            alpha_previous = u*u - u*(2*PREVIOUS_RHO[s] + 1)
            d1 = alpha_left + alpha_previous
            asymptotic[s, s] = 2.0*w + d1/spin
            positive_link = math.sqrt(
                (1.0 - f(h + ELL[s]) / casimir) *
                (1.0 - f(h + RHO[s]) / casimir))
            alpha_right = u*u - u*(2*RHO[s] + 1)
            b1 = (alpha_left + alpha_right) / 2.0
            if s < 4:
                exact[s, s + 1] = exact[s + 1, s] = -positive_link
                asymptotic[s, s + 1] = asymptotic[s + 1, s] = -w - b1/spin
            else:
                exact[0, 4] = -positive_link * np.exp(-1j * theta)
                exact[4, 0] = -positive_link * np.exp(1j * theta)
                asymptotic[0, 4] = (-w - b1/spin) * np.exp(-1j * theta)
                asymptotic[4, 0] = (-w - b1/spin) * np.exp(1j * theta)
        exact_eigs = np.linalg.eigvalsh(exact)
        asymptotic_eigs = np.linalg.eigvalsh(asymptotic)
        error = float(np.max(np.abs(exact_eigs - asymptotic_eigs)))
        rows.append({"S": spin, "u": u, "theta": theta,
                     "max_eigenvalue_error": error,
                     "S2_scaled_error": spin*spin*error})
    return {"samples": rows,
            "scope": "finite frozen-cell corroboration of the O(S^-2) remainder; not a uniform proof"}


def verify_non_crossing_subprincipal_band() -> dict:
    u, k = sp.symbols("u k", real=True)
    alpha = lambda a: sp.expand(u**2 - u * (2 * a + 1))
    diagonal = [sp.expand(alpha(ELL[s]) + alpha(PREVIOUS_RHO[s]))
                for s in range(5)]
    links = [sp.expand((alpha(ELL[s]) + alpha(RHO[s])) / 2)
             for s in range(5)]
    got = sp.simplify(sum(diagonal) / 5 -
                      2 * sp.cos(k) * sum(links) / 5)
    expected = sp.expand(
        2 * u**2 * (1 - sp.cos(k)) +
        u * (18 * sp.cos(k) - 16) / 5)
    if sp.simplify(got - expected) != 0:
        raise ArithmeticError(("non-crossing five-cell band correction",
                               got, expected))
    cell_phase_correction = sp.simplify(
        -5 * expected / (2 * (1 - u**2) * sp.sin(k)))
    return {
        "correction": str(expected),
        "coordinate": "u=h/S, with the physical momentum k and the five-cell wrap theta=5*k modulo 2*pi",
        "fixed_energy_cell_phase_increment": f"theta_S=theta+({cell_phase_correction})/S+O(S^-2)",
        "validity": "diagonal first-order eigenvalue correction only where the selected principal band is nondegenerate",
        "crossing_rule": "replace this scalar correction by the four compressed matrices at same-fiber degeneracies; exclude turning points sin(k)=0",
    }


def verify_bragg_crossing_compressions() -> dict:
    u = sp.symbols("u", real=True)
    rt5 = sp.sqrt(5)
    root_plus = sp.sqrt(10 + 2 * rt5)
    root_minus = sp.sqrt(10 - 2 * rt5)
    alpha = lambda a: sp.expand(u**2 - u * (2 * a + 1))
    diagonal = [sp.expand(alpha(ELL[s]) + alpha(PREVIOUS_RHO[s]))
                for s in range(5)]
    links = [sp.expand((alpha(ELL[s]) + alpha(RHO[s])) / 2)
             for s in range(5)]

    cases = (
        (sp.Integer(0), (1, 4),
         u * ((25 - 5 * rt5) * u - 41 + 9 * rt5) / 10,
         u * (2 + sp.I * (root_plus - root_minus)) / 5,
         4 * (rt5 - 1) * sp.Abs(u) / 5,
         (1-u**2) * root_plus / 5),
        (sp.Integer(0), (2, 3),
         u * ((25 + 5 * rt5) * u - 41 - 9 * rt5) / 10,
         u * (2 + sp.I * (root_plus + root_minus)) / 5,
         4 * (rt5 + 1) * sp.Abs(u) / 5,
         (1-u**2) * root_minus / 5),
        (sp.pi, (0, 4),
         u * ((15 - 5 * rt5) * u - 23 + 9 * rt5) / 10,
         2 * u * (3 - rt5) / 5,
         4 * (3 - rt5) * sp.Abs(u) / 5,
         (1-u**2) * root_minus / 5),
        (sp.pi, (1, 3),
         u * ((15 + 5 * rt5) * u - 23 - 9 * rt5) / 10,
         2 * u * (3 + rt5) / 5,
         4 * (3 + rt5) * sp.Abs(u) / 5,
         (1-u**2) * root_plus / 5),
    )
    records = []
    for theta, pair, mu, z, expected_gap, expected_slope in cases:
        matrix = sp.zeros(5)
        for s in range(5):
            matrix[s, s] = diagonal[s]
        for s in range(4):
            matrix[s, s + 1] = matrix[s + 1, s] = -links[s]
        matrix[0, 4] = -links[4] * sp.exp(-sp.I * theta)
        matrix[4, 0] = -links[4] * sp.exp(sp.I * theta)

        i, j = pair
        qi = (theta + 2 * sp.pi * i) / 5
        qj = (theta + 2 * sp.pi * j) / 5
        vi = sp.Matrix([sp.exp(sp.I * qi * s) / sp.sqrt(5)
                        for s in range(5)])
        vj = sp.Matrix([sp.exp(sp.I * qj * s) / sp.sqrt(5)
                        for s in range(5)])
        computed = sp.Matrix([
            [(vi.conjugate().T * matrix * vi)[0],
             (vi.conjugate().T * matrix * vj)[0]],
            [(vj.conjugate().T * matrix * vi)[0],
             (vj.conjugate().T * matrix * vj)[0]],
        ])
        expected = sp.Matrix([[mu, z], [sp.conjugate(z), mu]])
        # Every entry is a polynomial of degree at most two in u. Three
        # exact algebraic specializations therefore check the identity while
        # avoiding branch-sensitive radical rewrites in SymPy's simplifier.
        algebraic_zero = sp.Symbol("_algebraic_zero")
        for value in (computed - expected):
            for sample in (0, 1, 2):
                minimal = sp.minpoly(sp.expand(value.subs(u, sample)),
                                     algebraic_zero)
                if sp.simplify(minimal - algebraic_zero) != 0:
                    raise ArithmeticError(("five-cell crossing compression",
                                           str(theta), pair, sample, minimal))
        gap_square = sp.expand(4 * z * sp.conjugate(z) - expected_gap**2)
        for sample in (0, 1, 2):
            minimal = sp.minpoly(gap_square.subs(u, sample), algebraic_zero)
            if sp.simplify(minimal - algebraic_zero) != 0:
                raise ArithmeticError(("five-cell first-order gap", str(theta),
                                       pair, sample, z, expected_gap, minimal))
        slope_square = sp.expand(
            (2 * (1-u**2) * (sp.sin(qi) - sp.sin(qj)) / 5)**2 -
            expected_slope**2)
        # Both squared slopes share the factor (1-u^2)^2; sample away from
        # its zeros so this exact algebraic check tests the coefficient.
        if sp.minpoly(slope_square.subs(u, sp.Rational(1, 2)),
                      algebraic_zero) != algebraic_zero:
            raise ArithmeticError(("five-cell crossing slope", str(theta),
                                   pair, slope_square))
        records.append({
            "theta": "0" if theta == 0 else "pi",
            "band_pair": list(pair),
            "compressed_matrix": [[str(mu), str(z)],
                                  [str(sp.conjugate(z)), str(mu)]],
            "first_order_eigenvalue_gap": str(expected_gap),
            "principal_difference_slope_magnitude": str(expected_slope),
            "scope": "frozen five-site cell; coefficient multiplies 1/S; no global scattering estimate",
        })
    return {"crossings_checked": len(records), "records": records}


def verify_character_fiber_shift() -> dict:
    # A three-cell discrete Fourier transform resolves the exact 4*pi/3 shift.
    cells = 3
    dft = np.exp(-2j * np.pi * np.outer(np.arange(cells), np.arange(cells)) / cells)
    omega = np.exp(2j * np.pi / 3)
    internal = omega ** np.arange(5)
    maximum_error = 0.0
    for h in range(cells):
        for s in range(5):
            basis = np.zeros((cells, 5), dtype=np.complex128)
            basis[h, s] = 1.0
            actual = dft @ ((omega ** ((5 * np.arange(cells)[:, None] +
                                       np.arange(5)[None, :]) % 3)) * basis)
            transformed = dft @ basis
            shifted = np.array([internal * transformed[(k - 2) % cells]
                                for k in range(cells)])
            maximum_error = max(maximum_error,
                                float(np.max(np.abs(actual - shifted))))
    if maximum_error > 2e-12:
        raise ArithmeticError(("period-three Bloch-fiber shift", maximum_error))
    return {"basis_vectors_checked": cells * 5,
            "shift_angle_mod_2pi": "4*pi/3",
            "internal_multiplier": [str(sp.simplify(sp.exp(2*sp.pi*sp.I*s/3)))
                                    for s in range(5)],
            "maximum_dft_error": maximum_error,
            "fourier_convention": "F_s(theta)=sum_h exp(-i*h*theta) psi_(h,s)"}


def verify_principal_phase_stationary_set() -> dict:
    x, k = sp.symbols("x k", real=True)
    delta = sp.simplify(2 * sp.sqrt(3) * (1 - x**2) * sp.sin(k + sp.pi/3))
    dx = sp.factor(sp.diff(delta, x))
    dk = sp.factor(sp.diff(delta, k))
    hessian = sp.hessian(delta, (x, k))
    points = ((sp.Integer(0), sp.pi/6),
              (sp.Integer(0), 7*sp.pi/6))
    records = []
    for point in points:
        substitution = {x: point[0], k: point[1]}
        gradient = [sp.simplify(dx.subs(substitution)),
                    sp.simplify(dk.subs(substitution))]
        hess = hessian.subs(substitution).applyfunc(sp.simplify)
        determinant = sp.simplify(hess.det())
        if gradient != [0, 0] or determinant != 24:
            raise ArithmeticError(("stationary point/Hessian", point,
                                   gradient, hess, determinant))
        records.append({"point": [str(point[0]), str(point[1])],
                        "hessian": [[str(hess[i,j]) for j in range(2)]
                                    for i in range(2)],
                        "determinant": str(determinant)})
    # In |x|<1, dk=0 iff cos(k+pi/3)=0. Then sin is nonzero, so dx=0 iff x=0.
    return {"phase_difference": "2*sqrt(3)*(1-x^2)*sin(k+pi/3)",
            "gradient": [str(dx), str(dk)],
            "all_joint_critical_points_for_x_in_(-1,1)": records,
            "determinant_at_each": 24}


def verify_principal_lobe_action() -> dict:
    lam = sp.symbols("lambda", positive=True)
    x = sp.symbols("x", real=True)
    a = sp.symbols("a", positive=True)
    arcsine_area = sp.integrate(
        1 / sp.sqrt(a**2 - x**2), (x, 0, a))
    if sp.simplify(arcsine_area - sp.pi / 2) != 0:
        raise ArithmeticError(("principal lobe arcsine integral",
                               arcsine_area))
    w = 1 - x**2
    radicand_identity = sp.simplify(
        w * (1 - lam / (4 * w)) - (w - lam / 4))
    if radicand_identity != 0:
        raise ArithmeticError(("principal action derivative radicand",
                               radicand_identity))
    return {
        "principal_symbol": "nu(x,k)=4*(1-x^2)*sin(k/2)^2",
        "turning_point": "a=sqrt(1-lambda/4)",
        "positive_lobe_area_in_x_k": "2*integral_0^a (pi-2*asin(sqrt(lambda)/(2*sqrt(1-x^2)))) dx",
        "area_derivative": "-pi/(2*sqrt(lambda))",
        "area_at_lambda_zero": "2*pi",
        "area": "pi*(2-sqrt(lambda))",
        "physical_site_coordinate": "y=n/S=5*x when x=h/S",
        "principal_action_in_physical_coordinate": "5*pi*(2-sqrt(lambda))",
        "integral_check": str(arcsine_area),
        "radicand_identity_exact": str(radicand_identity),
        "scope": "classical principal-symbol lobe area only; no Bohr-Sommerfeld error or finite-spin phase accuracy is established",
    }


def source_hashes() -> dict:
    out = {}
    for rel in AUDIT_INPUT_PATHS:
        path = ROOT / rel
        out[rel] = hashlib.sha256(path.read_bytes()).hexdigest()
    return out


def main() -> None:
    bragg_crossings = verify_bragg_crossing_compressions()
    result = {
        "actual_current_surface_status": "conditional-support",
        "scope_statement": "Bounded exact coefficient and frozen-symbol identities under supplied model inputs; no global finite-spin propagator or readout limit is established.",
        "historical_author_source_revision": SOURCE_REVISION,
        "source_sha256": source_hashes(),
        "read_inventory": {
            "scientific_computation_input": [
                "scripts/core_derivation.py, imported for the supplied physical path and finite-spin two-hop coefficients"
            ],
            "provenance_hash_inputs": list(AUDIT_INPUT_PATHS),
            "runner_source_identity": "Bound by scripts/runner_cache.py; this runner does not hash its own source bytes."
        },
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "sympy": sp.__version__,
        "operator": "N_S=J M_S J on I_S=[-5S,5S-4]; C=S(S+1)",
        "exact_signed_five_site_family": verify_signed_cell_family(),
        "physical_hop_crosscheck": verify_physical_coefficients(),
        "subprincipal_cell_coefficients": subprincipal_cell_coefficients(),
        "principal_five_cell_bloch_symbol": verify_bloch_symbol(),
        "frozen_cell_eigenvalue_expansion_check": verify_frozen_cell_eigenvalue_expansion(),
        "non_crossing_scalar_subprincipal_band": verify_non_crossing_subprincipal_band(),
        "same_fiber_bragg_crossing_compressions": bragg_crossings,
        "period_three_character_action": verify_character_fiber_shift(),
        "principal_lobe_action": verify_principal_lobe_action(),
        "principal_inter_fiber_phase_stationary_set": verify_principal_phase_stationary_set(),
        "same_fiber_bragg_crossing_rule": "theta=0 pairs (1,4),(2,3); theta=pi pairs (0,4),(1,3); exact first-order compressions and frozen-cell gaps are recorded above",
        "readout_equal_energy_points": ["k=-pi/3 mod 2*pi", "k=2*pi/3 mod 2*pi"],
        "scope_limit": "The finite N_S has a slowly varying five-site cell structure. These local-symbol identities do not control transport for time theta=C/4, central matching, alias sums, or p_S.",
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    print("TOTAL: PASS=9 FAIL=0 (executed identity/finite-control families; no asymptotic certification)")


if __name__ == "__main__":
    main()
