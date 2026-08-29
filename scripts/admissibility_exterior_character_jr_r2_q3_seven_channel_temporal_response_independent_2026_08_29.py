#!/usr/bin/env python3
"""Independent exact certificate for the Block239 seven-channel response.

The route exponents are reconstructed from named original-link factor sets.
The two orientation controls reopen ``u1`` and use only the exact rational
Brauer-moment machinery of the declared Block238 independent parent.  This
module does not import the Block239 primary runner.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction as F

import numpy as np
import sympy as sp

import admissibility_exterior_character_jr_r2_q3_oriented_vector_triple_recoupling_independent_2026_08_29 as block238


AUDIT_TIMEOUT_SEC = 120
OPEN_LINK = "u1"
FINITE_FIELD_PRIMES = (1009, 1013, 1019)
RATIONAL_SAMPLE = {
    "d": F(1, 5),
    "t": F(3, 10),
    "u": F(2, 5),
    "v3": F(1, 2),
    "w4": F(3, 5),
}


LOOPS = {
    "p0": block238.fine_plaquette(0),
    "p1": block238.fine_plaquette(1),
    "A": block238.A0,
    "D": block238.D01,
    "E": block238.D012,
}

STATE_FACTORS = {
    "Y": ("D", "E"),
    "Z": ("A", "D", "E"),
    "Y0": ("p0", "D", "E"),
    "Z1": ("p1", "A", "D", "E"),
    "Y1": ("p1", "D", "E"),
    "Z0": ("p0", "A", "D", "E"),
}

EXPECTED_CENSUSES = {
    "Y": {"t": 6, "xL": 9},
    "Z": {"t": 7, "xL": 4, "yJ": 5},
    "Y0": {"t": 7, "xL": 6, "yJ": 3},
    "Z1": {"one": 1, "t": 7, "xL": 6, "yJ": 3},
    "Y1": {"t": 8, "xL": 7, "yJ": 2},
    "Z0": {"t": 8, "xL": 7, "yJ": 2},
}


def link_factor_sets(factors: tuple[str, ...]) -> dict[str, frozenset[str]]:
    """Return the exact character factors occupying every original link."""

    result: dict[str, set[str]] = defaultdict(set)
    for factor in factors:
        for link, _orientation in LOOPS[factor]:
            result[link].add(factor)
    return {link: frozenset(names) for link, names in sorted(result.items())}


def selected_local_channel(factors: frozenset[str]) -> str:
    """Classify the selected irrep after the exact cup/identity resolutions."""

    if len(factors) == 1:
        return "t"
    if factors == {"D", "E"}:
        return "xL"
    if factors in (
        frozenset(("A", "D", "E")),
        frozenset(("p0", "D", "E")),
        frozenset(("p1", "D", "E")),
    ):
        return "yJ"
    if factors in (frozenset(("p0", "A")), frozenset(("p1", "A"))):
        return "one"
    if factors in (
        frozenset(("p0", "A", "D", "E")),
        frozenset(("p1", "A", "D", "E")),
    ):
        # The p-A pair is selected into its scalar cup, leaving D-E in L.
        return "xL"
    raise AssertionError(f"unclassified selected factor set: {sorted(factors)}")


def incidence_certificate() -> dict[str, object]:
    factor_sets = {
        state: link_factor_sets(factors)
        for state, factors in STATE_FACTORS.items()
    }
    channel_by_link = {
        state: {
            link: selected_local_channel(names)
            for link, names in links.items()
        }
        for state, links in factor_sets.items()
    }
    censuses = {
        state: dict(sorted(Counter(channels.values()).items()))
        for state, channels in channel_by_link.items()
    }
    return {
        "factor_sets": factor_sets,
        "channel_by_link": channel_by_link,
        "censuses": censuses,
    }


def allowed_routes() -> tuple[tuple[int, int], ...]:
    """All (old pair L, total J) routes in (V tensor V) tensor V."""

    return tuple(
        (pair_spin, total_spin)
        for pair_spin in range(3)
        for total_spin in range(abs(pair_spin - 1), pair_spin + 2)
    )


def route_monomials() -> dict[str, object]:
    """Construct every temporal monomial from the original-link census."""

    determinant, t, u, v3 = sp.symbols("d t u v3")
    pair_multiplier = {0: sp.Integer(1), 1: t, 2: u}
    triple_multiplier = {0: determinant, 1: t, 2: u, 3: v3}
    incidence = incidence_certificate()

    def multiplier(state: str, pair_spin: int, total_spin: int) -> sp.Expr:
        census = incidence["censuses"][state]
        return sp.expand(
            t ** census.get("t", 0)
            * pair_multiplier[pair_spin] ** census.get("xL", 0)
            * triple_multiplier[total_spin] ** census.get("yJ", 0)
        )

    rows = {}
    direct = sp.Integer(0)
    closed = sp.Integer(0)
    for pair_spin, total_spin in allowed_routes():
        weight = sp.Rational(2 * total_spin + 1, 81)
        temporal_y = multiplier("Y", pair_spin, total_spin)
        temporal_z = multiplier("Z", pair_spin, total_spin)
        temporal_01_left = multiplier("Y0", pair_spin, total_spin)
        temporal_01_right = multiplier("Z1", pair_spin, total_spin)
        temporal_10_left = multiplier("Y1", pair_spin, total_spin)
        temporal_10_right = multiplier("Z0", pair_spin, total_spin)
        orientation_01 = (
            (temporal_y + temporal_01_left)
            * (temporal_z + temporal_01_right)
        )
        orientation_10 = (
            (temporal_y + temporal_10_left)
            * (temporal_z + temporal_10_right)
        )
        direct += weight * (orientation_01 + orientation_10) / 4
        closed += sp.Rational(2 * total_spin + 1, 324) * (
            (temporal_y + temporal_01_left)
            * (temporal_z + temporal_01_left)
            + (temporal_y + temporal_10_left)
            * (temporal_z + temporal_10_left)
        )
        rows[(pair_spin, total_spin)] = {
            "weight": weight,
            "T_Y": temporal_y,
            "T_Z": temporal_z,
            "T_01_left": temporal_01_left,
            "T_01_right": temporal_01_right,
            "T_10_left": temporal_10_left,
            "T_10_right": temporal_10_right,
        }

    substitutions = {determinant: 1, t: 1, u: 1, v3: 1}
    rational_substitutions = {
        determinant: sp.Rational(2, 5),
        t: sp.Rational(1, 2),
        u: sp.Rational(1, 3),
        v3: sp.Rational(1, 4),
    }
    return {
        "symbols": {
            "determinant": determinant,
            "t": t,
            "u": u,
            "v3": v3,
        },
        "pair_multiplier": pair_multiplier,
        "triple_multiplier": triple_multiplier,
        "rows": rows,
        "direct": sp.expand(direct),
        "closed": sp.expand(closed),
        "identity_limit": sp.simplify(direct.subs(substitutions)),
        "rational_value": sp.factor(direct.subs(rational_substitutions)),
    }


def expected_reopened_numerator(
    orientation: str,
    indices: tuple[int, ...],
    numerator: int,
) -> int:
    if orientation == "O10":
        # u1 has p1,D,E on the left and A,D,E on the right.
        return numerator if all(
            indices[index] == indices[index + 6] for index in range(6)
        ) else 0
    # O01 has D,E versus p1,A,D,E.  p1-A form a scalar cup and D,E cross.
    matched = (
        indices[0] == indices[8]
        and indices[1] == indices[9]
        and indices[2] == indices[10]
        and indices[3] == indices[11]
        and indices[4] == indices[6]
        and indices[5] == indices[7]
    )
    return numerator if matched else 0


def exact_reopened_u1_certificate(
    orientation: str,
    moments: dict[int, dict[str, object]],
) -> dict[str, object]:
    """Exactly contract every link except the triple/cup-bearing u1 link."""

    occurrences, node_count = block238.original_link_occurrences(orientation)
    open_occurrences = occurrences[OPEN_LINK]
    open_labels = [
        label
        for _name, row, column in open_occurrences
        for label in (row, column)
    ]
    tensors = []
    denominator = 1
    moment_census = Counter()
    for link, link_occurrences in occurrences.items():
        if link == OPEN_LINK:
            continue
        degree = len(link_occurrences)
        moment_census[degree] += 1
        moment = moments[degree]
        labels = [
            label
            for _name, row, column in link_occurrences
            for label in (row, column)
        ]
        tensors.append((moment["tensor"], labels))
        denominator *= moment["denominator"]
    numerator = denominator // 81
    contracted, contracted_labels = block238.greedy_exact_contract(tensors)
    contracted = np.transpose(
        contracted,
        [contracted_labels.index(label) for label in open_labels],
    )
    exact = True
    nonzero_entries = 0
    for indices in np.ndindex(contracted.shape):
        actual = contracted[indices]
        expected = expected_reopened_numerator(
            orientation, indices, numerator
        )
        exact &= actual == expected
        nonzero_entries += int(actual != 0)
    return {
        "orientation": orientation,
        "node_count": node_count,
        "open_occurrence_names": tuple(
            name for name, _row, _column in open_occurrences
        ),
        "open_side_census": dict(Counter(
            name.split("_", 1)[0]
            for name, _row, _column in open_occurrences
        )),
        "moment_census": dict(sorted(moment_census.items())),
        "coefficient": F(numerator, denominator),
        "nonzero_entries": nonzero_entries,
        "tensor_shape": contracted.shape,
        "exact_expected_tensor": exact,
    }


def _kron_all(factors: tuple[np.ndarray, ...]) -> np.ndarray:
    result = np.array([[1]], dtype=np.int64)
    for factor in factors:
        result = np.kron(result, factor)
    return result


def integer_total_casimir(power: int) -> np.ndarray:
    """Cartesian total-spin Casimir on V^power, with integer entries."""

    identity = np.eye(3, dtype=np.int64)
    generators = (
        np.array(((0, 0, 0), (0, 0, 1), (0, -1, 0)), dtype=np.int64),
        np.array(((0, 0, -1), (0, 0, 0), (1, 0, 0)), dtype=np.int64),
        np.array(((0, 1, 0), (-1, 0, 0), (0, 0, 0)), dtype=np.int64),
    )
    dimension = 3**power
    casimir = 2 * power * np.eye(dimension, dtype=np.int64)
    for left in range(power):
        for right in range(left + 1, power):
            for generator in generators:
                factors = tuple(
                    generator if position in (left, right) else identity
                    for position in range(power)
                )
                casimir -= 2 * _kron_all(factors)
    return casimir


def fraction_mod(value: F, prime: int) -> int:
    return (value.numerator % prime) * pow(value.denominator, -1, prime) % prime


def sympy_rational_mod(value: sp.Expr, prime: int) -> int:
    value = sp.Rational(value)
    return int(value.p % prime) * pow(int(value.q), -1, prime) % prime


def modular_spectral_projectors(
    power: int,
    prime: int,
) -> dict[int, np.ndarray]:
    """Casimir-polynomial spin projectors, exactly over F_prime."""

    dimension = 3**power
    identity = np.eye(dimension, dtype=np.int64)
    casimir = integer_total_casimir(power) % prime
    spins = (1,) if power == 1 else tuple(range(power + 1))
    projectors = {}
    for spin in spins:
        eigenvalue = spin * (spin + 1)
        projector = identity.copy()
        denominator = 1
        for other in spins:
            if other == spin:
                continue
            other_eigenvalue = other * (other + 1)
            projector = (
                projector
                @ ((casimir - other_eigenvalue * identity) % prime)
            ) % prime
            denominator = (
                denominator * (eigenvalue - other_eigenvalue)
            ) % prime
        projectors[spin] = projector * pow(denominator, -1, prime) % prime
    return projectors


def modular_temporal_operator(power: int, prime: int) -> np.ndarray:
    """One-link central crossing at the declared rational sample over F_p."""

    sample_by_spin = {
        0: RATIONAL_SAMPLE["d"] if power % 2 else F(1),
        1: RATIONAL_SAMPLE["t"],
        2: RATIONAL_SAMPLE["u"],
        3: RATIONAL_SAMPLE["v3"],
        4: RATIONAL_SAMPLE["w4"],
    }
    projectors = modular_spectral_projectors(power, prime)
    result = np.zeros((3**power, 3**power), dtype=np.int64)
    for spin, projector in projectors.items():
        result = (
            result + fraction_mod(sample_by_spin[spin], prime) * projector
        ) % prime
    return result


def modular_projector_certificate(prime: int) -> bool:
    """Finite-field-exact completeness/idempotence for powers one to four."""

    for power in range(1, 5):
        projectors = modular_spectral_projectors(power, prime)
        identity = np.eye(3**power, dtype=np.int64) % prime
        if not np.array_equal(
            sum(projectors.values(), np.zeros_like(identity)) % prime,
            identity,
        ):
            return False
        for left_spin, left in projectors.items():
            for right_spin, right in projectors.items():
                product_matrix = left @ right % prime
                expected = left if left_spin == right_spin else np.zeros_like(left)
                if not np.array_equal(product_matrix, expected):
                    return False
    return True


def apply_group_operator_mod(
    tensor: np.ndarray,
    labels: list[int],
    selected_columns: list[int],
    operator: np.ndarray,
    prime: int,
) -> tuple[np.ndarray, list[int]]:
    """Apply one V^m central operator to selected column indices modulo p."""

    if not selected_columns:
        return tensor, labels
    axes = [labels.index(label) for label in selected_columns]
    power = len(selected_columns)
    operator_tensor = operator.reshape((3,) * (2 * power))
    transformed = np.tensordot(
        tensor,
        operator_tensor,
        axes=(axes, tuple(range(power))),
    ) % prime
    remaining_labels = [
        label for index, label in enumerate(labels) if index not in axes
    ]
    return transformed, remaining_labels + selected_columns


def greedy_modular_contract(
    tensors: list[tuple[np.ndarray, list[int]]],
    prime: int,
) -> int:
    """Contract a closed dimension-three tensor network exactly in F_prime."""

    tensors = list(tensors)
    while len(tensors) > 1:
        best = None
        for left_index in range(len(tensors)):
            left_labels = tensors[left_index][1]
            for right_index in range(left_index + 1, len(tensors)):
                right_labels = tensors[right_index][1]
                shared = set(left_labels) & set(right_labels)
                if not shared:
                    continue
                output_rank = (
                    len(left_labels) + len(right_labels) - 2 * len(shared)
                )
                score = (
                    output_rank,
                    -len(shared),
                    max(len(left_labels), len(right_labels)),
                )
                if best is None or score < best[0]:
                    best = (score, left_index, right_index, shared)
        if best is None:
            raise AssertionError("modular original-link network disconnected")
        _score, left_index, right_index, shared = best
        left_tensor, left_labels = tensors[left_index]
        right_tensor, right_labels = tensors[right_index]
        left_axes = [
            index for index, label in enumerate(left_labels) if label in shared
        ]
        shared_order = [left_labels[index] for index in left_axes]
        right_axes = [right_labels.index(label) for label in shared_order]
        result = np.tensordot(
            left_tensor, right_tensor, axes=(left_axes, right_axes)
        ) % prime
        result_labels = (
            [label for label in left_labels if label not in shared]
            + [label for label in right_labels if label not in shared]
        )
        for index in sorted((left_index, right_index), reverse=True):
            tensors.pop(index)
        tensors.append((result, result_labels))
    tensor, labels = tensors[0]
    if labels or tensor.shape:
        raise AssertionError(f"expected a scalar contraction, got labels={labels}")
    return int(tensor) % prime


def selected_trace_occurrences(
    occurrences: list[tuple[str, int, int]],
    side: str,
    mode: str,
) -> list[int]:
    """Column labels crossed before (pre) or after (post) action insertion."""

    selected = []
    for trace_name, _row, column in occurrences:
        if not trace_name.startswith(f"{side}_"):
            continue
        is_action = trace_name.startswith(f"{side}_p")
        if mode == "post" or not is_action:
            selected.append(column)
    return selected


def modular_gram_term(
    orientation: str,
    left_mode: str,
    right_mode: str,
    prime: int,
    moments: dict[int, dict[str, object]],
    temporal_operators: dict[int, np.ndarray],
) -> int:
    """All-original-link pre/post Gram term, exactly over one finite field."""

    occurrences, _node_count = block238.original_link_occurrences(orientation)
    tensors = []
    for link_occurrences in occurrences.values():
        degree = len(link_occurrences)
        moment = moments[degree]
        tensor = (
            np.asarray(moment["tensor"], dtype=np.int64) % prime
            * pow(moment["denominator"], -1, prime)
        ) % prime
        labels = [
            label
            for _name, row, column in link_occurrences
            for label in (row, column)
        ]
        for side, mode in (("left", left_mode), ("right", right_mode)):
            selected_columns = selected_trace_occurrences(
                link_occurrences, side, mode
            )
            if selected_columns:
                tensor, labels = apply_group_operator_mod(
                    tensor,
                    labels,
                    selected_columns,
                    temporal_operators[len(selected_columns)],
                    prime,
                )
        tensors.append((tensor, labels))
    return greedy_modular_contract(tensors, prime)


def expected_gram_terms(formula: dict[str, object], orientation: str) -> dict[tuple[str, str], sp.Expr]:
    """Single-(L,J)-sum prediction for each unnormalized Gram term."""

    result = {
        ("pre", "pre"): sp.Integer(0),
        ("pre", "post"): sp.Integer(0),
        ("post", "pre"): sp.Integer(0),
        ("post", "post"): sp.Integer(0),
    }
    residual_key = "T_01_left" if orientation == "O01" else "T_10_left"
    for row in formula["rows"].values():
        weight = row["weight"]
        residual = row[residual_key]
        result[("pre", "pre")] += weight * row["T_Y"] * row["T_Z"]
        result[("pre", "post")] += weight * row["T_Y"] * residual
        result[("post", "pre")] += weight * residual * row["T_Z"]
        result[("post", "post")] += weight * residual**2
    substitutions = {
        formula["symbols"]["determinant"]: sp.Rational(1, 5),
        formula["symbols"]["t"]: sp.Rational(3, 10),
        formula["symbols"]["u"]: sp.Rational(2, 5),
        formula["symbols"]["v3"]: sp.Rational(1, 2),
    }
    return {
        modes: sp.factor(value.subs(substitutions))
        for modes, value in result.items()
    }


def finite_field_full_network_certificate(
    moments: dict[int, dict[str, object]],
    formula: dict[str, object],
) -> dict[str, object]:
    """Compare all eight Gram terms at one rational sample over three fields.

    These are exact equalities in each named finite field.  They are strong
    multi-prime falsifiers of the closed formula at the declared rational
    sample; they are not presented as a proof of a symbolic rational identity.
    """

    expected = {
        orientation: expected_gram_terms(formula, orientation)
        for orientation in ("O01", "O10")
    }
    results = {}
    for prime in FINITE_FIELD_PRIMES:
        temporal_operators = {
            power: modular_temporal_operator(power, prime)
            for power in range(1, 5)
        }
        actual_by_orientation = {}
        for orientation in ("O01", "O10"):
            actual_by_orientation[orientation] = {}
            for modes in expected[orientation]:
                actual_by_orientation[orientation][modes] = modular_gram_term(
                    orientation,
                    modes[0],
                    modes[1],
                    prime,
                    moments,
                    temporal_operators,
                )
        expected_mod = {
            orientation: {
                modes: sympy_rational_mod(value, prime)
                for modes, value in terms.items()
            }
            for orientation, terms in expected.items()
        }
        results[prime] = {
            "projectors_exact": modular_projector_certificate(prime),
            "actual": actual_by_orientation,
            "expected": expected_mod,
            "all_eight_match": actual_by_orientation == expected_mod,
        }
    return {
        "sample": dict(RATIONAL_SAMPLE),
        "primes": FINITE_FIELD_PRIMES,
        "rational_expected_terms": expected,
        "results": results,
        "all_primes_match": all(
            result["projectors_exact"] and result["all_eight_match"]
            for result in results.values()
        ),
        "claim_scope": (
            "finite-field exact at the declared rational sample; "
            "not a symbolic rational-identity proof"
        ),
        "needs_LM_double_sum": False,
    }


def _build_fixture() -> dict[str, object]:
    moments = {
        degree: block238.exact_orthogonal_moment(degree)
        for degree in (2, 4, 6)
    }
    formula = route_monomials()
    return {
        "incidence": incidence_certificate(),
        "routes": allowed_routes(),
        "formula": formula,
        "reopened_o01": exact_reopened_u1_certificate("O01", moments),
        "reopened_o10": exact_reopened_u1_certificate("O10", moments),
        "finite_field_full_network": finite_field_full_network_certificate(
            moments, formula
        ),
    }


def independent_checks(
    data: dict[str, object] | None = None,
) -> tuple[tuple[str, bool], ...]:
    if data is None:
        data = _build_fixture()
    incidence = data["incidence"]
    formula = data["formula"]
    rows = formula["rows"]
    reopened_o01 = data["reopened_o01"]
    reopened_o10 = data["reopened_o10"]
    finite_field = data["finite_field_full_network"]
    determinant = formula["symbols"]["determinant"]
    t = formula["symbols"]["t"]
    u = formula["symbols"]["u"]
    expected_routes = (
        (0, 1),
        (1, 0), (1, 1), (1, 2),
        (2, 1), (2, 2), (2, 3),
    )
    expected_weights = tuple(
        sp.Rational(2 * total_spin + 1, 81)
        for _pair_spin, total_spin in expected_routes
    )
    return (
        ("the six temporal histories are reconstructed from original-link factor sets",
         incidence["censuses"] == {
             state: dict(sorted(census.items()))
             for state, census in EXPECTED_CENSUSES.items()
         }),
        ("pair and total spin resolve exactly seven routes with d_J over 81 weights",
         data["routes"] == expected_routes
         and tuple(rows[route]["weight"] for route in data["routes"])
         == expected_weights
         and sum(expected_weights) == sp.Rational(1, 3)),
        ("the pair-only and triple-occupied crossings use x_L and y_J respectively",
         formula["pair_multiplier"] == {0: 1, 1: t, 2: u}
         and formula["triple_multiplier"][0] == determinant
         and formula["triple_multiplier"][1] == t
         and formula["triple_multiplier"][2] == u),
        ("the exact route exponents are 6-9, 7-4-5, 7-6-3, and 8-7-2",
         all(
             row["T_Y"] == t**6 * formula["pair_multiplier"][pair]**9
             and row["T_Z"] == (
                 t**7 * formula["pair_multiplier"][pair]**4
                 * formula["triple_multiplier"][total]**5
             )
             and row["T_01_left"] == row["T_01_right"] == (
                 t**7 * formula["pair_multiplier"][pair]**6
                 * formula["triple_multiplier"][total]**3
             )
             and row["T_10_left"] == row["T_10_right"] == (
                 t**8 * formula["pair_multiplier"][pair]**7
                 * formula["triple_multiplier"][total]**2
             )
             for (pair, total), row in rows.items()
         )),
        ("the independently assembled leakage sum equals the closed seven-channel formula",
         sp.expand(formula["direct"] - formula["closed"]) == 0),
        ("identity crossing gives the exact stripped coefficient two thirds",
         formula["identity_limit"] == sp.Rational(2, 3)),
        ("the J=0 negative-parity route retains the determinant multiplier",
         (1, 0) in rows
         and rows[(1, 0)]["T_Z"] == t**7 * t**4 * determinant**5
         and rows[(1, 0)]["T_01_left"] == t**7 * t**6 * determinant**3
         and rows[(1, 0)]["T_10_left"] == t**8 * t**7 * determinant**2),
        ("reopened O01 u1 is exactly the V2-to-V4 cup/cross tensor over 81",
         reopened_o01["open_occurrence_names"] == (
             "left_D01", "left_D012",
             "right_p1", "right_A0", "right_D01", "right_D012",
         )
         and reopened_o01["open_side_census"] == {"left": 2, "right": 4}
         and reopened_o01["moment_census"] == {2: 8, 4: 4, 6: 4}
         and reopened_o01["coefficient"] == F(1, 81)
         and reopened_o01["exact_expected_tensor"]
         and reopened_o01["nonzero_entries"] == 729),
        ("reopened O10 u1 is exactly the same-order V-cubed identity over 81",
         reopened_o10["open_occurrence_names"] == (
             "left_p1", "left_D01", "left_D012",
             "right_A0", "right_D01", "right_D012",
         )
         and reopened_o10["open_side_census"] == {"left": 3, "right": 3}
         and reopened_o10["moment_census"] == {2: 8, 4: 4, 6: 4}
         and reopened_o10["coefficient"] == F(1, 81)
         and reopened_o10["exact_expected_tensor"]
         and reopened_o10["nonzero_entries"] == 729),
        ("Casimir-polynomial projectors are finite-field exact through V to the fourth",
         all(
             result["projectors_exact"]
             for result in finite_field["results"].values()
         )),
        ("all eight all-original-link Gram terms match at the rational sample over three primes",
         finite_field["primes"] == FINITE_FIELD_PRIMES
         and finite_field["all_primes_match"]
         and all(
             result["all_eight_match"]
             for result in finite_field["results"].values()
         )),
        ("the full-network sample needs one L-J sum and no independent L-M double sum",
         finite_field["all_primes_match"]
         and not finite_field["needs_LM_double_sum"]),
        ("no scalar-on-V3 or strandwise-t-cubed shortcut is inserted",
         len(set(formula["triple_multiplier"].values())) == 4
         and formula["triple_multiplier"][0] != t**3
         and formula["triple_multiplier"][3] != t**3),
    )


def independent_fixture() -> dict[str, object]:
    data = _build_fixture()
    data["checks"] = independent_checks(data)
    return data


def main() -> int:
    data = independent_fixture()
    print(f"audit_timeout_sec: {AUDIT_TIMEOUT_SEC}")
    print("per_element: every original-link factor set and selected local channel")
    print("per_site: both cell-zero orientations with u1 reopened exactly")
    print("per_mode: all seven (L,J) routes and the determinant J=0 multiplier")
    print("per_block: eight full-network Gram terms at one rational sample over three primes")
    print("lattice_wide: not claimed; no arbitrary word, minimal memory, or dynamics")
    print("exactness_scope: finite-field exact sample; no symbolic rational identity claimed")
    failures = 0
    for label, passed in data["checks"]:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(data['checks']) - failures} FAIL={failures}")
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
