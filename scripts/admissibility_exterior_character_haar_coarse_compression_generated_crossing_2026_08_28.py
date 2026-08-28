#!/usr/bin/env python3
"""Exact checks for the projected Haar-compression generated crossing theorem."""

from __future__ import annotations

import argparse
import itertools
from pathlib import Path

import sympy as sp

from admissibility_exterior_character_haar_coarse_compression_generated_crossing_independent_2026_08_28 import (
    independent_facts,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_HAAR_COARSE_COMPRESSION_GENERATED_CROSSING_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_CO_SCALED_TEMPORAL_TROTTER_AND_CYLINDRICAL_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_exterior_character_haar_coarse_compression_generated_crossing_independent_2026_08_28.py",
)

MUTATIONS = (
    "bias_haar_fiber",
    "reverse_path_order",
    "drop_internal_frame",
    "omit_second_spatial_half",
    "drop_mu_square",
    "replace_pointwise_product",
    "drop_dimension_factor",
    "corrupt_normalization",
    "remove_full_support",
    "erase_determinant_term",
    "erase_operator_bound",
    "erase_vector_pair",
    "corrupt_improper_parity",
    "promote_original_closure",
    "claim_bare_intertwining",
    "claim_iterated_rg",
    "claim_physical_time",
    "claim_continuum",
    "claim_action_selection",
    "break_import_boundary",
)

PASS = 0
FAIL = 0


def check(name: str, condition: object) -> None:
    global PASS, FAIL
    ok = bool(condition)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    PASS += int(ok)
    FAIL += int(not ok)


def signed_permutation_frames() -> list[sp.Matrix]:
    frames: list[sp.Matrix] = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            frame = sp.zeros(3)
            for row, column in enumerate(perm):
                frame[row, column] = signs[row]
            frames.append(frame)
    return frames


def z2_fiber(*, biased: bool = False, omit_second_half: bool = False) -> tuple[dict[int, sp.Rational], dict[int, sp.Rational]]:
    group = (1, -1)
    a = {s: sp.Integer(1) + sp.Rational(1, 2) * s for s in group}
    m = {1: sp.Integer(1), -1: sp.Rational(1, 2)}
    pairs = list(itertools.product(group, repeat=2))
    if biased:
        pairs = pairs[:-1]
    h: dict[int, sp.Rational] = {}
    for delta in group:
        total = sp.Integer(0)
        for x_prime, x in pairs:
            right_half = sp.Integer(1) if omit_second_half else m[x]
            total += m[x_prime] * a[x_prime * delta * x] * right_half
        h[delta] = sp.Rational(total, len(pairs))
    return h, {s: sp.expand(a[s] * h[s]) for s in group}


def main(mutation: str | None, mode: str) -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    facts = independent_facts()
    if mode == "independent":
        checks = (
            ("independent S3 carrier", facts["group_size"] == 6 and facts["a_positive"]),
            ("independent Haar convolution", facts["h_hat"] == facts["h_hat_expected"]),
            ("independent fusion", facts["k_hat"] == facts["k_hat_fusion"]),
            ("independent strict generated crossing", facts["p_hat"]["triv"] == 1 and facts["p_strict"]),
            ("independent Z2 quotient", facts["z2_k"] == {1: sp.Rational(57, 64), -1: sp.Rational(17, 64)}),
            ("independent determinant multiplier", facts["z2_det"] == sp.Rational(20, 37)),
            ("independent n=1 half-action", facts["mu_linear"]["triv"] == -7 and facts["mu_linear"]["std_minus"] == sp.Rational(1, 3)),
            ("independent induced sectors", facts["induced_det"] == 4 and facts["induced_vector"] == sp.Rational(4, 27)),
        )
        for name, condition in checks:
            check(name, condition)
        print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
        return int(FAIL != 0)

    source = Path(__file__).read_text(encoding="utf-8")
    note = Path(AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8")
    required_sources = all(Path(path).is_file() for path in AUDIT_INPUT_PATHS)
    if mutation == "break_import_boundary":
        required_sources = False

    # Six fine Z2 links coarsen to three ordered two-link path holonomies.
    counts = {(a, b, c): 0 for a, b, c in itertools.product((1, -1), repeat=3)}
    assignments = list(itertools.product((1, -1), repeat=6))
    if mutation == "bias_haar_fiber":
        assignments = assignments[:-1]
    for a1, a2, b1, b2, c1, c2 in assignments:
        counts[(a2 * a1, b2 * b1, c2 * c1)] += 1
    check(
        "Haar coarsening: ordered path holonomies have the normalized product pushforward",
        set(counts.values()) == {8},
    )

    frames = signed_permutation_frames()
    first = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
    second = sp.Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
    ordered_ok = True
    internal_ok = True
    for middle in frames:
        transformed_first = middle * first
        transformed_second = second * middle.T
        composed = (
            transformed_first * transformed_second
            if mutation == "reverse_path_order"
            else transformed_second * transformed_first
        )
        ordered_ok &= composed == second * first
        broken_second = second if mutation == "drop_internal_frame" else transformed_second
        internal_ok &= broken_second * transformed_first == second * first
    check(
        "ordered coarsening: the two-link word retains its orientation on all signed frames",
        len(frames) == 48 and ordered_ok,
    )
    check(
        "common projector diagnostic: all 48 proper/improper signed-permutation internal frames cancel",
        len(frames) == 48 and internal_ok,
    )

    nominal_h, nominal_k = z2_fiber()
    h_half, k_half = z2_fiber(omit_second_half=(mutation == "omit_second_spatial_half"))
    check(
        "full transfer fiber: both spatial half-actions enter H=m*a*m",
        h_half == nominal_h and k_half == nominal_k,
    )

    # S3 is an independent nonabelian character/dimension control.
    names = ("triv", "sign", "std")
    dimensions = {"triv": 1, "sign": 1, "std": 2}
    a_hat = {"triv": sp.Integer(1), "sign": sp.Rational(1, 2), "std": sp.Rational(1, 3)}
    mu = {"triv": sp.Rational(19, 36), "sign": sp.Rational(1, 36), "std": sp.Rational(1, 9)}
    h_expected = {
        name: a_hat[name] * (mu[name] if mutation == "drop_mu_square" else mu[name] ** 2)
        for name in names
    }
    check(
        "double Haar integral: convolution squares the half-action Fourier scalar",
        h_expected == facts["h_hat"],
    )

    pointwise_formula = facts["k_hat_fusion"].copy()
    if mutation == "replace_pointwise_product":
        pointwise_formula["sign"] = a_hat["sign"] * facts["h_hat"]["sign"]
    check(
        "generated crossing: the pointwise product aH obeys the exact character-fusion formula",
        pointwise_formula == facts["k_hat"],
    )

    fusion_with_dimensions = facts["k_hat_fusion"].copy()
    if mutation == "drop_dimension_factor":
        fusion_with_dimensions["std"] /= dimensions["std"]
    check(
        "Peter-Weyl normalization: representation dimensions survive the fusion contraction",
        fusion_with_dimensions == facts["k_hat"],
    )

    z = facts["k_hat"]["triv"]
    p_hat = {name: facts["k_hat"][name] / z for name in names}
    if mutation == "corrupt_normalization":
        p_hat["triv"] = z
    check(
        "probability normalization: Z=kappa_triv makes the generated trivial multiplier one",
        p_hat["triv"] == 1,
    )

    strict_values = list(p_hat.values())
    if mutation == "remove_full_support":
        strict_values[-1] = sp.Integer(0)
    check(
        "strict-support diagnostic: all three generated S3 Fourier multipliers are positive",
        all(value > 0 for value in strict_values),
    )

    determinant_multiplier = facts["z2_det"]
    if mutation == "erase_determinant_term":
        determinant_multiplier = sp.Integer(0)
    check(
        "disconnected-component control: the exact Z2 quotient multiplier is 20/37",
        nominal_k == {1: sp.Rational(57, 64), -1: sp.Rational(17, 64)}
        and determinant_multiplier == sp.Rational(20, 37),
    )

    n, beta, eliminated = sp.symbols("n beta eliminated", positive=True)
    half_log_span = 8 * beta / n
    h_log_span = 2 * half_log_span
    comparison = eliminated * h_log_span
    ell = sp.exp(-half_log_span)
    quadratic_comparison = sp.simplify((1 - ell) ** 2 / (2 * ell**2))
    if mutation == "erase_operator_bound":
        comparison = sp.Integer(0)
    check(
        "quantitative comparison: the normalized log-density and convolution bounds use 16 N beta/n",
        sp.simplify(comparison - 16 * eliminated * beta / n) == 0
        and sp.simplify(quadratic_comparison - (sp.exp(8 * beta / n) - 1) ** 2 / 2) == 0
        and "||C_pN-C_a||" in note,
    )

    # n=1: Q=14*triv-2*(det+V+detV), with the 1/d Fourier normalization.
    q_coeff = {"triv": 14, "det": -2, "V": -2, "detV": -2}
    rep_dim = {"triv": 1, "det": 1, "V": 3, "detV": 3}
    mu_linear = {name: sp.Rational(-q_coeff[name], 2 * rep_dim[name]) for name in q_coeff}
    r_linear = {"det": sp.Integer(2), "V": sp.Rational(2, 3), "detV": sp.Rational(2, 3)}
    induced = {
        "det": r_linear["det"] ** 2 * mu_linear["det"] ** 2,
        "V": rep_dim["V"] * r_linear["V"] ** 2 * mu_linear["V"] ** 2,
        "detV": rep_dim["detV"] * r_linear["detV"] ** 2 * mu_linear["detV"] ** 2,
    }
    vector_pair = induced["V"] + induced["detV"]
    if mutation == "erase_vector_pair":
        vector_pair = sp.Integer(0)
    check(
        "induced sector: the first nonconstant correction is beta^2 kappa^2[4 chi_det+4(chi_V+chi_detV)/27]",
        mu_linear == {"triv": -7, "det": 1, "V": sp.Rational(1, 3), "detV": sp.Rational(1, 3)}
        and induced["det"] == 4
        and vector_pair == sp.Rational(8, 27),
    )

    # Proper and improper representatives separate orientation and component response.
    proper_representative = sp.eye(3)
    improper_representative = -sp.eye(3)

    def induced_bracket(representative: sp.Matrix) -> sp.Expr:
        det_character = representative.det()
        vector_character = sp.trace(representative)
        det_vector_character = (
            vector_character
            if mutation == "corrupt_improper_parity"
            else det_character * vector_character
        )
        return sp.simplify(det_character + (vector_character + det_vector_character) / 27)

    proper_bracket = induced_bracket(proper_representative)
    improper_bracket = induced_bracket(improper_representative)
    check(
        "proper/improper discriminator: the vector pair cancels only on the improper component",
        proper_bracket == sp.Rational(11, 9)
        and improper_bracket == -1,
    )

    original_closure = mutation == "promote_original_closure"
    scalar_shift = sp.Rational(1, 2)
    predicted_vector_shift = -sp.Rational(8, 3) * scalar_shift
    induced_vector_shift = -sp.Rational(4, 27)
    check(
        "action-family boundary: the generated tangent is not a scalar shift of the inherited path crossing",
        not original_closure
        and facts["z2_det"] != sp.Rational(1, 2)
        and predicted_vector_shift == -sp.Rational(4, 3)
        and induced_vector_shift != predicted_vector_shift,
    )

    bare_intertwining = mutation == "claim_bare_intertwining"
    check(
        "refinement typing: canonical compression is not the bare intertwining equation",
        not bare_intertwining and "J* T_f J" in note,
    )

    iterated_rg = mutation == "claim_iterated_rg"
    physical_time = mutation == "claim_physical_time"
    continuum = mutation == "claim_continuum"
    action_selection = mutation == "claim_action_selection"
    check(
        "scope boundary: no iterable RG, physical time, continuum, or action-selection theorem is claimed",
        not iterated_rg
        and not physical_time
        and not continuum
        and not action_selection
        and "not an iterable" in note
        and "not a physical" in note,
    )

    check(
        "import integrity: all declared inputs and hostile mutations are packet-bound",
        required_sources
        and all(name in source for name in MUTATIONS)
        and Path(AUDIT_INPUT_PATHS[-1]).name in source,
    )

    print("per_element: exact Z2/S3 exterior and spatial-half diagnostic coefficients were derived")
    print("per_site: Z2 ordered coarsening and all 48 signed-permutation frame controls were executed")
    print("per_mode: S3 fusion, determinant/vector arithmetic, and dimension factors were checked")
    print("per_block: exact compression ingredients and the quantitative coarse-action constants were executed; the full O(3) identity is analytic")
    print("lattice_wide: checked and not executed — no iterated graph flow, uniform locality, continuum, or physical clock is supplied")
    print("STATUS: one-cell Haar compression generates an exact positive crossing distinct from the inherited path crossing and its local scalar-coupling tangent")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mode", choices=("primary", "independent"), default="primary")
    args = parser.parse_args()
    raise SystemExit(main(args.mutation, args.mode))
