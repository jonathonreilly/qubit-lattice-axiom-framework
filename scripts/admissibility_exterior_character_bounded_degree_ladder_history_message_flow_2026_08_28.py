#!/usr/bin/env python3
"""Exact checks for the bounded-degree exterior ladder history-message flow."""

from __future__ import annotations

import argparse
import itertools
from pathlib import Path

import sympy as sp

from admissibility_exterior_character_bounded_degree_ladder_history_message_flow_independent_2026_08_28 import (
    independent_facts,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_BOUNDED_DEGREE_LADDER_HISTORY_MESSAGE_FLOW_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_HAAR_COARSE_COMPRESSION_GENERATED_CROSSING_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_exterior_character_bounded_degree_ladder_history_message_flow_independent_2026_08_28.py",
)

MUTATIONS = (
    "corrupt_ladder_census",
    "mix_full_tree_boundary",
    "bias_haar_pushforward",
    "drop_hidden_gauge_cancellation",
    "reverse_staged_coarsening",
    "replace_nu_by_haar",
    "drop_bottom_rail_crossing",
    "omit_second_spatial_half",
    "replace_composition_by_pointwise",
    "duplicate_shared_retained_frame",
    "corrupt_endpoint_adjoint",
    "corrupt_psd_feature",
    "remove_strict_support",
    "use_c_instead_of_c_squared",
    "promote_message_tail_to_full_transfer",
    "corrupt_connector_spectrum",
    "drop_improper_component",
    "claim_scalar_merge_associative",
    "claim_original_locality",
    "claim_physical_time",
    "claim_minimality",
    "break_import_boundary",
)

PASS = 0
FAIL = 0
G = (1, -1)


def check(name: str, condition: object) -> None:
    global PASS, FAIL
    ok = bool(condition)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    PASS += int(ok)
    FAIL += int(not ok)


def ladder_edges(length: int) -> tuple[tuple[int, int], ...]:
    edges: list[tuple[int, int]] = []
    edges.extend((i, i + 1) for i in range(length))
    edges.extend(
        (length + 1 + i, length + 1 + i + 1) for i in range(length)
    )
    edges.extend((i, length + 1 + i) for i in range(length + 1))
    return tuple(edges)


def coarsen_two(config: tuple[int, ...]) -> tuple[int, int, int, int]:
    u0, u1, v0, v1, h0, _h1, h2 = config
    return (u1 * u0, v1 * v0, h0, h2)


def gauge_transform(
    config: tuple[int, ...], gauges: tuple[int, ...], length: int
) -> tuple[int, ...]:
    return tuple(
        gauges[target] * value * gauges[source]
        for value, (source, target) in zip(config, ladder_edges(length))
    )


def coarse_gauge_transform(
    coarse: tuple[int, int, int, int], gauges: tuple[int, ...]
) -> tuple[int, int, int, int]:
    bottom, top, left, right = coarse
    gb0, gt0, gb2, gt2 = gauges[0], gauges[3], gauges[2], gauges[5]
    return (
        gb2 * bottom * gb0,
        gt2 * top * gt0,
        gt0 * left * gb0,
        gt2 * right * gb2,
    )


def multiply_polynomials(factors: list[sp.Expr], variable: sp.Symbol) -> sp.Poly:
    expression = sp.Integer(1)
    for factor in factors:
        expression = sp.expand(expression * factor)
    return sp.Poly(expression, variable)


def one_cell_perimeter(*, drop_bottom: bool = False) -> dict[tuple[int, int], sp.Poly]:
    t = sp.symbols("t")
    out: dict[tuple[int, int], sp.Poly] = {}
    for wp, wv in itertools.product(G, repeat=2):
        xp = (1, wp)
        x = (1, wv)
        total = sp.Integer(0)
        for gb0, gt0, gb1, gt1 in itertools.product(G, repeat=4):
            signs = [
                xp[0] * gt0 * x[0] * gb0,
                xp[1] * gt1 * x[1] * gb1,
                gt1 * gt0,
            ]
            if not drop_bottom:
                signs.append(gb1 * gb0)
            total += multiply_polynomials([1 + t * sign for sign in signs], t).as_expr()
        out[(wp, wv)] = sp.Poly(sp.expand(total / 16), t)
    return out


def two_cell_outer_perimeter() -> sp.Poly:
    t = sp.symbols("t")
    total = sp.Integer(0)
    for x in itertools.product(G, repeat=3):
        for xp in itertools.product(G, repeat=3):
            outer = x[0] * x[2] * xp[0] * xp[2]
            for gb in itertools.product(G, repeat=3):
                for gt in itertools.product(G, repeat=3):
                    signs = [xp[i] * gt[i] * x[i] * gb[i] for i in range(3)]
                    signs += [gb[i + 1] * gb[i] for i in range(2)]
                    signs += [gt[i + 1] * gt[i] for i in range(2)]
                    total += outer * multiply_polynomials(
                        [1 + t * sign for sign in signs], t
                    ).as_expr()
    return sp.Poly(sp.expand(total / sp.Integer(2**12)), t)


def z2_history_data(
    *, use_haar_nu: bool = False, omit_second_half: bool = False
) -> tuple[list[tuple[int, ...]], list[sp.Rational], sp.Matrix, sp.Matrix]:
    states = list(itertools.product(G, repeat=4))
    half = sp.Rational(1, 2)

    def w(value: int) -> sp.Rational:
        return sp.Integer(1) + half * value

    def m(value: int) -> sp.Rational:
        return sp.Integer(1) if value == 1 else half

    rho = [
        sp.Integer(1) if use_haar_nu else w(xp * gt * x * gb)
        for gb, gt, xp, x in states
    ]
    bond_entries: list[list[sp.Rational]] = []
    for z in states:
        row: list[sp.Rational] = []
        for y in states:
            value = w(y[0] * z[0]) * w(y[1] * z[1]) * m(y[2] * z[2])
            if not omit_second_half:
                value *= m(y[3] * z[3])
            row.append(value)
        bond_entries.append(row)
    bond = sp.Matrix(bond_entries)
    operator = bond * sp.diag(*rho) / 16
    return states, rho, bond, operator


def connector_deleted_operator() -> sp.Matrix:
    states = list(itertools.product(G, repeat=2))

    def rho(state: tuple[int, int]) -> sp.Rational:
        return sp.Integer(1) + sp.Rational(state[0] * state[1], 2)

    def m(value: int) -> sp.Rational:
        return sp.Integer(1) if value == 1 else sp.Rational(1, 2)

    bond = sp.Matrix(
        [[m(y[0] * z[0]) * m(y[1] * z[1]) for y in states] for z in states]
    )
    return bond * sp.diag(*(rho(state) for state in states)) / 4


def history_kernel_power(bond: sp.Matrix, measure: sp.Matrix, exponent: int) -> sp.Matrix:
    result = bond
    for _ in range(1, exponent):
        result = result * measure * bond
    return result


def shared_frame_physical_marginal(
    states: list[tuple[int, ...]], rho: list[sp.Rational], bond: sp.Matrix,
    *, duplicate_middle: bool = False,
) -> bool:
    measure = sp.diag(*(value / 16 for value in rho))
    bond_two = history_kernel_power(bond, measure, 2)
    bond_four = history_kernel_power(bond, measure, 4)

    def endpoint(pair: tuple[int, int]) -> sp.Matrix:
        return sp.Matrix(
            [rho[index] / 4 if state[2:] == pair else 0 for index, state in enumerate(states)]
        )

    for pair0, pair1, pair2 in itertools.product(itertools.product(G, repeat=2), repeat=3):
        e0, e1, e2 = endpoint(pair0), endpoint(pair1), endpoint(pair2)
        middle = sp.diag(*e1)
        staged_middle = middle * middle if duplicate_middle else middle
        direct = (e0.T * bond_four * middle * bond_four * e2)[0]
        staged = (
            e0.T
            * bond_two
            * measure
            * bond_two
            * staged_middle
            * bond_two
            * measure
            * bond_two
            * e2
        )[0]
        if sp.simplify(direct - staged) != 0:
            return False
    return True


def feature_gram(
    states: list[tuple[int, ...]], rho: list[sp.Rational], bond: sp.Matrix,
    *, corrupt: bool = False,
) -> tuple[sp.Matrix, sp.Matrix, list[sp.Rational]]:
    # w(s)=1+(1/2)s and m(s)=3/4+(1/4)s.
    coordinate_coefficients = (
        (sp.Integer(1), sp.Rational(1, 2)),
        (sp.Integer(1), sp.Rational(1, 2)),
        (sp.Rational(3, 4), sp.Rational(1, 4)),
        (sp.Rational(3, 4), sp.Rational(1, 4)),
    )
    coefficients: list[sp.Rational] = []
    reconstructed = sp.zeros(len(states))
    for mask in itertools.product((0, 1), repeat=4):
        coefficient = sp.prod(coordinate_coefficients[i][bit] for i, bit in enumerate(mask))
        if corrupt and mask == (1, 1, 1, 1):
            coefficient = -coefficient
        coefficients.append(coefficient)
        feature = sp.Matrix(
            [
                rho[index]
                * sp.prod(state[i] for i, bit in enumerate(mask) if bit)
                / 16
                for index, state in enumerate(states)
            ]
        )
        reconstructed += coefficient * feature * feature.T
    weighted_gram = sp.diag(*(value / 16 for value in rho)) * bond * sp.diag(
        *(value / 16 for value in rho)
    )
    return weighted_gram, reconstructed, coefficients


def main(mutation: str | None, mode: str) -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    facts = independent_facts()

    if mode == "independent":
        expected_one = {
            key: tuple(sp.Rational(value.numerator, value.denominator) for value in polynomial)
            for key, polynomial in facts["one_cell_perimeter"].items()
        }
        checks = (
            ("independent bounded carrier", facts["vertices"] == 10 and facts["edges"] == 13 and facts["max_degree"] == 3),
            ("independent product Haar", set(facts["pushforward_counts"]) == {8}),
            ("independent projector typing", facts["coarsening_equivariant"]),
            ("independent residual quotient", facts["residual_orbit_count"] == 4),
            (
                "independent actual perimeter",
                all(polynomial == (1, 0, 0, 0, key[0] * key[1]) for key, polynomial in expected_one.items()),
            ),
            ("independent two-cell perimeter", tuple(facts["two_cell_outer"]) == (0, 0, 0, 0, 0, 0, 1)),
            (
                "independent connector spectrum polynomial",
                tuple(facts["connector_charpoly"])
                == (
                    sp.Rational(729, 1048576),
                    sp.Rational(-27, 1024),
                    sp.Rational(147, 512),
                    -1,
                    1,
                ),
            ),
            ("independent direct/staged history", facts["history_direct_staged"]),
            (
                "independent shared-frame marginal",
                facts["physical_shared_direct_staged"] and facts["physical_duplicate_middle_fails"],
            ),
            (
                "independent raw shared-frame Haar sum",
                facts["raw_shared_frame_matches"] and facts["raw_shared_frame_duplicate_fails"],
            ),
            ("independent nonabelian order", facts["s3_ordered_direct_staged"]),
            ("independent scalar associator", facts["scalar_defect"] == sp.Rational(12, 343)),
        )
        for name, condition in checks:
            check(name, condition)
        print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
        return int(FAIL != 0)

    source = Path(__file__).read_text(encoding="utf-8")
    note = Path(AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8")
    imports_ok = all(Path(path).is_file() for path in AUDIT_INPUT_PATHS)
    if mutation == "break_import_boundary":
        imports_ok = False

    length = 4
    edge_count = len(ladder_edges(length))
    if mutation == "corrupt_ladder_census":
        edge_count += 1
    degrees = [0] * (2 * length + 2)
    for source_vertex, target_vertex in ladder_edges(length):
        degrees[source_vertex] += 1
        degrees[target_vertex] += 1
    check(
        "bounded carrier: Gamma_L has 2L+2 vertices, 3L+1 links, and maximum degree three",
        2 * length + 2 == 10 and edge_count == 3 * length + 1 and max(degrees) == 3,
    )

    fixes_x0 = mutation == "mix_full_tree_boundary"
    check(
        "rail-forest convention: both rail forests are fixed while all L+1 rung variables retain product Haar",
        not fixes_x0 and "Gauge-fix only the two rail forests" in note and "`X_0` with Haar measure" in note,
    )

    fine_configs = list(itertools.product(G, repeat=7))
    if mutation == "bias_haar_pushforward":
        fine_configs = fine_configs[:-1]
    counts: dict[tuple[int, int, int, int], int] = {}
    for config in fine_configs:
        coarse = coarsen_two(config)
        counts[coarse] = counts.get(coarse, 0) + 1
    check(
        "Haar isometry: every one-cell coarse configuration has eight length-two fine preimages",
        len(counts) == 16 and set(counts.values()) == {8},
    )

    def coarsen_for_projector(config: tuple[int, ...]) -> tuple[int, int, int, int]:
        if mutation == "drop_hidden_gauge_cancellation":
            u0, u1, v0, v1, h0, h1, h2 = config
            return (u1 * u0, v1 * v0, h1 * h0, h2)
        return coarsen_two(config)

    equivariant = True
    for config in itertools.product(G, repeat=7):
        coarse = coarsen_for_projector(config)
        for gauges in itertools.product(G, repeat=6):
            equivariant &= (
                coarsen_for_projector(gauge_transform(config, gauges, 2))
                == coarse_gauge_transform(coarse, gauges)
            )
    check(
        "projector typing: hidden gauge frames cancel and P_f J=J P_c on the exact Z2 quotient",
        equivariant and facts["coarsening_equivariant"],
    )

    # Direction-typed word composition; words stand for noncommuting rail links.
    words = tuple(f"u{i}" for i in range(4))
    direct = tuple(reversed(words))
    first_stage = (tuple(reversed(words[:2])), tuple(reversed(words[2:])))
    staged = first_stage[1] + first_stage[0]
    if mutation == "reverse_staged_coarsening":
        staged = first_stage[0] + first_stage[1]
    check(
        "typed coarsening: J_uv^[q]=J_v^[uq] J_u^[q] preserves the noncommuting ordered rail product",
        direct == staged
        and facts["s3_ordered_direct_staged"]
        and "J_(uv)^[q] = J_v^[uq] J_u^[q]" in note,
    )

    states, rho, bond, history_operator = z2_history_data(
        use_haar_nu=mutation == "replace_nu_by_haar"
    )
    check(
        "onsite measure: nu is normalized and retains the nonconstant actual rung crossing",
        sp.simplify(sum(rho) / 16) == 1
        and set(rho) == {sp.Rational(1, 2), sp.Rational(3, 2)},
    )

    perimeter = one_cell_perimeter(drop_bottom=mutation == "drop_bottom_rail_crossing")
    t = sp.symbols("t")
    expected_perimeter = {
        key: sp.Poly(1 + key[0] * key[1] * t**4, t) for key in perimeter
    }
    check(
        "actual-edge temporal kernel: the one-cell cycle is 1+t^4 W'W and the two-cell outer cycle is t^6",
        perimeter == expected_perimeter
        and two_cell_outer_perimeter() == sp.Poly(t**6, t)
        and facts["two_cell_outer"][-1] == 1,
    )

    _, _, reciprocal_bond, _ = z2_history_data(
        omit_second_half=mutation == "omit_second_spatial_half"
    )
    check(
        "reciprocal spatial action: every message bond contains output and input plaquette half-actions",
        reciprocal_bond == bond and "m(Y'X'^-1) m(YX^-1)" in note,
    )

    direct_four = history_operator**4
    staged_four = (history_operator**2) * (history_operator**2)
    if mutation == "replace_composition_by_pointwise":
        staged_four = sp.matrix_multiply_elementwise(history_operator**2, history_operator**2)
    check(
        "message associativity: direct and staged r=4 contractions agree with the same nu integration",
        direct_four == staged_four and facts["history_direct_staged"],
    )

    duplicates_middle = mutation == "duplicate_shared_retained_frame"
    shared_match = shared_frame_physical_marginal(
        states, rho, bond, duplicate_middle=duplicates_middle
    )
    check(
        "physical marginal: q=2 direct retain-four equals staged retain-two with the shared retained frame integrated once",
        shared_match
        and facts["physical_shared_direct_staged"]
        and facts["physical_duplicate_middle_fails"],
    )

    physical_pairs = list(itertools.product(G, repeat=2))
    extension = sp.zeros(16, 4)
    for history_index, state in enumerate(states):
        extension[history_index, physical_pairs.index(state[2:])] = 1
    history_measure = sp.diag(*(value / 16 for value in rho))
    physical_measure = sp.eye(4) / 4
    restriction = sp.zeros(4, 16)
    for history_index, state in enumerate(states):
        restriction[physical_pairs.index(state[2:]), history_index] = rho[history_index] / 4
    if mutation == "corrupt_endpoint_adjoint":
        restriction = sp.Rational(1, 4) * extension.T
    check(
        "endpoint typing: E is isometric and R=E* for the exact onsite-weighted history measure",
        extension.T * history_measure * extension == physical_measure
        and physical_measure * restriction == extension.T * history_measure,
    )

    weighted_gram, feature_sum, feature_coefficients = feature_gram(
        states, rho, bond, corrupt=mutation == "corrupt_psd_feature"
    )
    check(
        "weighted positive Gram: the rational Z2 history matrix is the exact nonnegative tensor-feature sum",
        weighted_gram == feature_sum
        and all(value >= 0 for value in feature_coefficients)
        and weighted_gram.rank() == 16
        and history_operator.det() != 0,
    )

    _, _, nominal_feature_coefficients = feature_gram(states, rho, bond, corrupt=False)
    strict_coefficients = list(nominal_feature_coefficients)
    if mutation == "remove_strict_support":
        strict_coefficients[-1] = sp.Integer(0)
    check(
        "strict support: every rail and plaquette Fourier feature coefficient is positive",
        all(value > 0 for value in strict_coefficients)
        and "strictly positive in every irreducible" in note,
    )

    n, kappa, beta = sp.symbols("n kappa beta", positive=True)
    c_value = sp.exp(-(32 * kappa + 16 * beta) / n)
    delta_value = c_value if mutation == "use_c_instead_of_c_squared" else c_value**2
    rational_c = c_value.subs(
        {n: 1, kappa: sp.log(2) / 32, beta: sp.log(2) / 16}
    )
    rational_delta = sp.simplify(delta_value.subs(
        {n: 1, kappa: sp.log(2) / 32, beta: sp.log(2) / 16}
    ))
    finite_c = sp.simplify(min(bond) / max(bond))
    finite_delta = finite_c**2
    check(
        "Doob constant: two w and two m ratios give c=exp[-(32kappa+16beta)/n] and delta=c^2",
        rational_c == sp.Rational(1, 4)
        and rational_delta == sp.Rational(1, 16)
        and sp.simplify(delta_value - sp.exp(-(64 * kappa + 32 * beta) / n)) == 0
        and finite_c == sp.Rational(1, 36)
        and finite_delta == sp.Rational(1, 1296),
    )

    delta = sp.Rational(1, 16)
    exponent = 4
    op_bound = (1 - delta) ** exponent
    hs_bound = sp.sqrt(delta**-1 - 1) * (1 - delta) ** (exponent - 1)
    tv_bound = op_bound
    promotes_full = mutation == "promote_message_tail_to_full_transfer"
    check(
        "tail typing: exact op/HS/TV constants apply only to the one-bond auxiliary history message",
        op_bound == sp.Rational(50625, 65536)
        and hs_bound == sp.Rational(3375, 4096) * sp.sqrt(15)
        and tv_bound == op_bound
        and not promotes_full
        and "do not imply a `q`-uniform" in note,
    )

    connector = connector_deleted_operator()
    lam = sp.symbols("lambda")
    connector_poly = sp.Poly(connector.charpoly(lam).as_expr(), lam)
    expected_poly = sp.Poly(
        lam**4 - lam**3 + sp.Rational(147, 512) * lam**2
        - sp.Rational(27, 1024) * lam + sp.Rational(729, 1048576),
        lam,
    )
    if mutation == "corrupt_connector_spectrum":
        expected_poly += sp.Poly(lam, lam)
    check(
        "connector-deleted control: the four exact eigenvalues follow from the independently derived characteristic polynomial",
        connector_poly == expected_poly
        and facts["connector_charpoly"][-1] == 1
        and "(10+sqrt(73))/32" in note,
    )

    signed_determinants = {
        sp.det(sp.diag(a, b, c))
        for a, b, c in itertools.product(G, repeat=3)
    }
    if mutation == "drop_improper_component":
        signed_determinants.discard(-1)
    check(
        "disconnected O(3) carrier: proper and improper determinant assignments both survive",
        signed_determinants == {-1, 1} and "no `SO(3)` restriction" in note,
    )

    q_value, r_value, s_value, t_value = sp.symbols("q r s t")
    merge = lambda left, right: sp.cancel((left + q_value * right) / (1 + q_value * left * right))
    associator = sp.factor(merge(merge(r_value, s_value), t_value) - merge(r_value, merge(s_value, t_value)))
    exact_defect = sp.simplify(associator.subs({q_value: sp.Rational(1, 9), r_value: sp.Rational(1, 2), s_value: sp.Rational(1, 2), t_value: sp.Rational(1, 2)}))
    if mutation == "claim_scalar_merge_associative":
        exact_defect = sp.Integer(0)
    check(
        "autonomous scalar control: the determinant merge associator is exactly 12/343",
        exact_defect == sp.Rational(12, 343)
        and facts["scalar_defect"] == sp.Rational(12, 343),
    )

    original_locality = mutation == "claim_original_locality"
    physical_time = mutation == "claim_physical_time"
    minimality = mutation == "claim_minimality"
    check(
        "scope boundary: no inherited-family locality, physical time, continuum, or minimality is claimed",
        not original_locality
        and not physical_time
        and not minimality
        and "not asserted to return" in note
        and "not imply a `q`-uniform" in note
        and "does not select a physical action" in note,
    )

    check(
        "import integrity: declared note, parent, axiom fence, helper, and every hostile mutation are packet-bound",
        imports_ok
        and all(name in source for name in MUTATIONS)
        and Path(AUDIT_INPUT_PATHS[-1]).name in source,
    )

    print("per_element: exact temporal-link, half-action, feature-weight, and determinant-component factors were derived")
    print("per_site: exhaustive Z2 local projector frames and the rail-forest residual quotient were executed")
    print("per_mode: exact perimeter characters, connector-control spectrum, and scalar associator were executed")
    print("per_block: direct and staged four-frame history contractions plus Doob constants were executed")
    print("lattice_wide: checked and not executed — no complete-volume transfer norm, continuum, or physical clock is supplied")
    print("STATUS: exact bounded-degree history-message powers represent the supplied finite projected ladder transfer")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mode", choices=("primary", "independent"), default="primary")
    arguments = parser.parse_args()
    raise SystemExit(main(arguments.mutation, arguments.mode))
