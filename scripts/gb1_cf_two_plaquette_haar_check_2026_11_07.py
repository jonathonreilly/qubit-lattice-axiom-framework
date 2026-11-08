#!/usr/bin/env python3
"""Exact restricted-input Haar checker for the specified seven-link patch.

Main operator entries are integrated Wilson polynomials, not products of
five-state local operators. All scientific arithmetic is rational. The only
floating-point quantities are elapsed-time and operating-system RSS receipts.
Run only after lab_ops preflight --numeric and a unique numeric lease.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import resource
import signal
import sys
import time
from fractions import Fraction as Q


AUDIT_TIMEOUT_SEC = 85
LINKS = ("AB", "BC", "DE", "EF", "AD", "BE", "CF")
ENDS = (("A", "B"), ("B", "C"), ("D", "E"), ("E", "F"),
        ("A", "D"), ("B", "E"), ("C", "F"))
VERTICES = tuple("ABCDEF")
NAMES = ("empty", "L", "R", "O")
WORDS = {
    "empty": (),
    "L": ((0, 1), (5, 1), (2, -1), (4, -1)),
    "R": ((1, 1), (6, 1), (3, -1), (5, -1)),
    "O": ((0, 1), (1, 1), (6, 1), (3, -1), (2, -1), (4, -1)),
}
ABSENT = (-1,) * len(LINKS)
START = time.monotonic()
CHECKS: list[dict] = []


class RejectedCandidate(ValueError):
    """An exact proposed coefficient object disagrees with its Haar derivation."""


def validate_candidate(derived, proposed) -> bool:
    if type(derived) is not type(proposed) or derived != proposed:
        raise RejectedCandidate("proposed object differs from exact Haar result")
    return True


def candidate_rejected(derived, proposed) -> bool:
    try:
        validate_candidate(derived, proposed)
    except RejectedCandidate:
        return True
    return False


def emit(label: str, value) -> None:
    print(json.dumps({"label": label, "value": value}, sort_keys=True), flush=True)


def check(label: str, condition: bool, **evidence) -> None:
    row = {"check": label, "ok": bool(condition), **evidence}
    CHECKS.append(row)
    print(json.dumps(row, sort_keys=True), flush=True)
    if not condition:
        raise AssertionError(label)


def memory_bytes() -> int:
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(peak if sys.platform == "darwin" else 1024 * peak)


def resource_checkpoint() -> None:
    if time.monotonic() - START >= AUDIT_TIMEOUT_SEC:
        raise RuntimeError("85-second wall budget reached")
    if memory_bytes() >= 250_000_000:
        raise MemoryError("250 MB RSS budget reached")


def alarm_handler(_signum, _frame) -> None:
    raise TimeoutError("85-second exact-check wall alarm")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sphere_moment(exponents: tuple[int, ...]) -> Q:
    """Uniform S^3 moment, from rotational symmetry / sphere beta integral."""
    if any(k % 2 for k in exponents):
        return Q(0)
    pairs = sum(exponents) // 2
    numerator = math.prod(math.prod(range(1, k, 2)) for k in exponents)
    denominator = math.prod(4 + 2 * j for j in range(pairs))
    return Q(numerator, denominator)


def projected_coordinate(mu: int) -> list[list[Q]]:
    """Local audit only; main loop matrices never use these 5x5 matrices."""
    basis = [(Q(1), (0,) * 4)]
    basis += [(Q(2), tuple(int(i == j) for i in range(4))) for j in range(4)]
    return [[ci * cj * sphere_moment(tuple(ei[k] + ej[k] + int(k == mu)
                                         for k in range(4)))
             for cj, ej in basis] for ci, ei in basis]


def proposed_coordinate(mu: int, coefficient: Q) -> list[list[Q]]:
    result = zero(5)
    result[0][mu + 1] = result[mu + 1][0] = coefficient
    return result


def quaternion_product(left: int, right: int) -> tuple[int, int]:
    """e_0=I, e_j=i sigma_j: e_j e_k=-delta_jk I-epsilon_jkl e_l."""
    if left == 0:
        return 1, right
    if right == 0:
        return 1, left
    if left == right:
        return -1, 0
    sign = -1 if (left, right) in ((1, 2), (2, 3), (3, 1)) else 1
    return sign, 6 - left - right


def wilson_polynomial(word: tuple[tuple[int, int], ...]) -> dict[tuple[int, ...], Q]:
    """Expand the ordinary color trace; coordinate 0 denotes x_4."""
    if not word:
        return {ABSENT: Q(1)}
    result: dict[tuple[int, ...], Q] = {}
    for coordinates in itertools.product(range(4), repeat=len(word)):
        component, coefficient = 0, 1
        key = list(ABSENT)
        for (edge, direction), mu in zip(word, coordinates):
            if key[edge] != -1:
                raise ValueError("the simple-loop contract was violated")
            key[edge] = mu
            sign, component = quaternion_product(mu, component)
            coefficient *= sign * (direction if mu else 1)
        if component == 0:
            result[tuple(key)] = Q(2 * coefficient)
    return result


def support(poly: dict[tuple[int, ...], Q]) -> tuple[int, ...]:
    if not poly:
        return ()
    masks = {tuple(i for i, mu in enumerate(key) if mu != -1) for key in poly}
    if len(masks) != 1:
        raise ValueError("inhomogeneous link support")
    return next(iter(masks))


def haar_contract_shared(p: dict, q: dict) -> dict:
    """Integrate every common edge using int x_mu x_nu=delta_mu,nu/4."""
    common = tuple(sorted(set(support(p)) & set(support(q))))
    right_only = tuple(sorted(set(support(q)) - set(common)))
    index: dict[tuple, list] = {}
    for key, coefficient in q.items():
        index.setdefault(tuple(key[i] for i in common), []).append((key, coefficient))
    result: dict[tuple[int, ...], Q] = {}
    moment = Q(1, 4) ** len(common)
    for left_key, left_coefficient in p.items():
        for right_key, right_coefficient in index.get(
                tuple(left_key[i] for i in common), ()):
            key = list(left_key)
            for edge in common:
                key[edge] = -1
            for edge in right_only:
                key[edge] = right_key[edge]
            term = tuple(key)
            result[term] = result.get(term, Q(0)) + moment * left_coefficient * right_coefficient
    return {key: coefficient for key, coefficient in result.items() if coefficient}


def haar_inner(p: dict, q: dict) -> Q:
    if support(p) != support(q):
        return Q(0)
    return sum((coefficient * q.get(key, Q(0)) for key, coefficient in p.items()), Q(0)) / (
        4 ** len(support(p)))


def haar_triple(p: dict, q: dict, r: dict) -> Q:
    supports = [set(support(poly)) for poly in (p, q, r)]
    if any(sum(edge in used for used in supports) % 2 for edge in range(len(LINKS))):
        return Q(0)
    return haar_inner(haar_contract_shared(p, q), r)


def scaled_poly(poly: dict, coefficient: Q) -> dict:
    return {key: coefficient * value for key, value in poly.items() if coefficient * value}


def reflect(poly: dict) -> dict:
    edge_map = (1, 0, 3, 2, 6, 5, 4)
    reverse = {0, 1, 2, 3}
    result = {}
    for key, coefficient in poly.items():
        mapped = list(ABSENT)
        for edge, mu in enumerate(key):
            mapped[edge_map[edge]] = mu
            if edge in reverse and mu > 0:
                coefficient = -coefficient
        result[tuple(mapped)] = coefficient
    return result


def singlet_multiplicity(half_spins: int) -> int:
    """Fuse half-spins, with integer keys equal to twice the total spin."""
    multiplicities = {0: 1}
    for _ in range(half_spins):
        following: dict[int, int] = {}
        for twice_j, multiplicity in multiplicities.items():
            for next_j in (twice_j - 1, twice_j + 1):
                if next_j >= 0:
                    following[next_j] = following.get(next_j, 0) + multiplicity
        multiplicities = following
    return multiplicities.get(0, 0)


def zero(n: int = 4) -> list[list[Q]]:
    return [[Q(0) for _ in range(n)] for _ in range(n)]


def identity(n: int = 4) -> list[list[Q]]:
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def add(a: list, b: list) -> list:
    return [[x + y for x, y in zip(arow, brow)] for arow, brow in zip(a, b)]


def scale(a: list, q: Q) -> list:
    return [[q * x for x in row] for row in a]


def subtract(a: list, b: list) -> list:
    return add(a, scale(b, Q(-1)))


def multiply(a: list, b: list) -> list:
    n = len(a)
    return [[sum((a[i][k] * b[k][j] for k in range(n)), Q(0))
             for j in range(n)] for i in range(n)]


def commutator(a: list, b: list) -> list:
    return subtract(multiply(a, b), multiply(b, a))


def transpose(a: list) -> list:
    return [list(row) for row in zip(*a)]


def strings(a: list) -> list:
    return [[str(x) for x in row] for row in a]


def series(a: list, divisor: int, degree: int) -> list:
    result = [identity()]
    for n in range(1, degree + 1):
        result.append(scale(multiply(result[-1], a), Q(1, divisor * n)))
    return result


def series_multiply(a: list, b: list) -> list:
    degree = min(len(a), len(b)) - 1
    result = []
    for n in range(degree + 1):
        coefficient = zero()
        for k in range(n + 1):
            coefficient = add(coefficient, multiply(a[k], b[n - k]))
        result.append(coefficient)
    return result


def complex_multiply(a: tuple, b: tuple) -> tuple:
    ar, ai = a
    br, bi = b
    return (subtract(multiply(ar, br), multiply(ai, bi)),
            add(multiply(ar, bi), multiply(ai, br)))


def exp_pi_halves(a: list, half_pi_units: int) -> tuple:
    """Exact exp(-i*k*pi*B/2), from its checked squared spectral projectors."""
    a2 = multiply(a, a)
    p1 = scale(subtract(scale(identity(), Q(4)), a2), Q(1, 3))
    p2 = scale(subtract(a2, identity()), Q(1, 3))
    if half_pi_units == 1:
        return scale(p2, Q(-1)), scale(multiply(a, p1), Q(-1))
    if half_pi_units == 2:
        return subtract(p2, p1), zero()
    if half_pi_units == 4:
        return identity(), zero()
    raise ValueError("unsupported exact angle")


def complex_strings(a: tuple) -> dict:
    return {"real": strings(a[0]), "imag": strings(a[1])}


def first_difference(actual: dict, proposed: dict) -> dict | None:
    for key in sorted(set(actual) | set(proposed)):
        if actual.get(key, Q(0)) != proposed.get(key, Q(0)):
            return {"coordinate_key": key, "actual": str(actual.get(key, Q(0))),
                    "proposed": str(proposed.get(key, Q(0)))}
    return None


def main() -> None:
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC)
    required_threads = ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                        "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS")
    check("single_math_thread_environment", all(os.environ.get(key) == "1"
                                               for key in required_threads))
    emit("provenance", {
        "checker": "independently authored in a fresh same-family context; no primary imports; not an audit",
        "arithmetic": "exact Fraction rational; complex matrices are rational real/imag pairs",
        "source_sha256": sha256(Path(__file__).resolve()),
        "model_source": "self-contained definitions in this runner",
        "coordinate_order": ["x4", "x1", "x2", "x3"],
        "basis_order": NAMES, "link_order": LINKS,
    })

    local = [projected_coordinate(mu) for mu in range(4)]
    check("supplied_local_normalization_matches_Haar",
          all(validate_candidate(local[mu], proposed_coordinate(mu, Q(1, 2))) for mu in range(4)),
          derived_transition=str(local[0][0][1]))
    normalization_mutation = proposed_coordinate(0, Q(1))
    check("mutation_altered_local_coefficient_rejected",
          candidate_rejected(local[0], normalization_mutation),
          actual=str(local[0][0][1]), mutated=str(normalization_mutation[0][1]))

    polynomials = {name: wilson_polynomial(WORDS[name]) for name in NAMES}
    emit("Wilson_polynomials", {name: {"terms": len(poly),
                                       "support": [LINKS[i] for i in support(poly)]}
                               for name, poly in polynomials.items()})
    resource_checkpoint()
    admissible = []
    for mask in itertools.product((0, 1), repeat=len(LINKS)):
        occupied = tuple(i for i, bit in enumerate(mask) if bit)
        multiplicity = math.prod(singlet_multiplicity(sum(vertex in ENDS[i] for i in occupied))
                                 for vertex in VERTICES)
        if multiplicity:
            admissible.append((occupied, multiplicity))
    dimension = sum(multiplicity for _, multiplicity in admissible)
    emit("six_vertex_fusion", {"dimension": dimension,
                              "admissible": [{"links": [LINKS[i] for i in occupied],
                                              "multiplicity": multiplicity}
                                             for occupied, multiplicity in admissible]})
    check("basis_spans_every_singlet_assignment",
          {occupied for occupied, _ in admissible} == {support(p) for p in polynomials.values()}
          and all(mult == 1 for _, mult in admissible))
    gram = [[haar_inner(polynomials[a], polynomials[b]) for b in NAMES] for a in NAMES]
    check("Haar_orthonormal_basis", gram == identity(), gram=strings(gram))

    shared = haar_contract_shared(polynomials["L"], polynomials["R"])
    common_ratio = {shared.get(key, Q(0)) / coefficient
                    for key, coefficient in polynomials["O"].items()}
    emit("shared_link_contraction", {"terms": len(shared),
                                    "outer_trace_ratios": sorted(map(str, common_ratio)),
                                    "triple_integral": str(haar_triple(polynomials["L"],
                                                                       polynomials["R"],
                                                                       polynomials["O"]))})
    check("index_identity_agrees_with_coordinate_Haar_contraction",
          validate_candidate(shared, scaled_poly(polynomials["O"], Q(1, 2))))
    mutation_witness = first_difference(shared, polynomials["O"])
    check("mutation_omitted_shared_dimension_factor_rejected",
          candidate_rejected(shared, polynomials["O"]),
          witness=mutation_witness)
    incomplete_shared = dict(shared)
    del incomplete_shared[min(incomplete_shared)]
    check("tamper_missing_contraction_term_fails_closed",
          candidate_rejected(shared, incomplete_shared),
          witness=first_difference(shared, incomplete_shared))

    magnetic = {
        square: [[2 * haar_triple(polynomials[bra], polynomials[square], polynomials[ket])
                  for ket in NAMES] for bra in NAMES]
        for square in ("L", "R")
    }
    electric = [[Q(3, 4) * len(support(polynomials[name])) if i == j else Q(0)
                 for j in range(len(NAMES))] for i, name in enumerate(NAMES)]
    left, right = magnetic["L"], magnetic["R"]
    exchange = [[haar_inner(polynomials[bra], reflect(polynomials[ket]))
                 for ket in NAMES] for bra in NAMES]
    for name, matrix in (("B_L", left), ("B_R", right), ("E", electric), ("X", exchange)):
        emit(name, strings(matrix))
    check("Hermitian_magnetics", left == transpose(left) and right == transpose(right))
    check("reflection_is_unitary_involution", multiply(exchange, exchange) == identity()
          and exchange == transpose(exchange))
    check("reflection_maps_square_operators", multiply(multiply(exchange, left), exchange) == right)
    check("reflection_preserves_electric_sum", commutator(exchange, electric) == zero())
    c = commutator(left, right)
    emit("magnetic_commutator", strings(c))
    emit("magnetic_commutator_is_zero", c == zero())
    check("commutator_antisymmetric_under_exchange",
          multiply(multiply(exchange, c), exchange) == scale(c, Q(-1)))
    h = add(left, right)
    check("joint_generator_exchange_commutator_zero", commutator(exchange, h) == zero())

    degree = 4
    lr = series_multiply(series(left, 1, degree), series(right, 1, degree))
    rl = series_multiply(series(right, 1, degree), series(left, 1, degree))
    sl = series_multiply(series_multiply(series(left, 2, degree), series(right, 1, degree)),
                         series(left, 2, degree))
    sr = series_multiply(series_multiply(series(right, 2, degree), series(left, 1, degree)),
                         series(right, 2, degree))
    ordered_difference = [subtract(a, b) for a, b in zip(lr, rl)]
    strang_difference = [subtract(a, b) for a, b in zip(sl, sr)]
    emit("ordered_exchange_difference_series_in_z_equals_minus_it",
         {str(n): strings(m) for n, m in enumerate(ordered_difference) if m != zero()})
    emit("Strang_exchange_difference_series_in_z_equals_minus_it",
         {str(n): strings(m) for n, m in enumerate(strang_difference) if m != zero()})
    check("ordered_second_order_matches_commutator", ordered_difference[2] == c)
    check("Strang_third_order_matches_nested_commutator",
          strang_difference[3] == scale(commutator(h, c), Q(-1, 8)))
    check("Strang_through_second_order_equals_joint_series", sl[:3] == series(h, 1, degree)[:3]
          and sr[:3] == series(h, 1, degree)[:3])

    for name, matrix in (("B_L", left), ("B_R", right)):
        square = multiply(matrix, matrix)
        check(name + "_squared_spectrum_polynomial",
              multiply(subtract(square, identity()), subtract(square, scale(identity(), Q(4))))
              == zero())
    lp, rp = exp_pi_halves(left, 1), exp_pi_halves(right, 1)
    lpi, rpi = exp_pi_halves(left, 2), exp_pi_halves(right, 2)
    ordered_at_half_pi = complex_multiply(lp, rp)
    reversed_at_half_pi = complex_multiply(rp, lp)
    strang_l_at_pi = complex_multiply(complex_multiply(lp, rpi), lp)
    strang_r_at_pi = complex_multiply(complex_multiply(rp, lpi), rp)
    emit("ordered_at_pi_over_2", complex_strings(ordered_at_half_pi))
    emit("reversed_at_pi_over_2", complex_strings(reversed_at_half_pi))
    emit("Strang_L_at_pi", complex_strings(strang_l_at_pi))
    emit("Strang_R_at_pi", complex_strings(strang_r_at_pi))
    # These are computed findings, deliberately not prescribed PASS outcomes.
    emit("update_exchange_findings", {
        "ordered_equal_at_pi_over_2": ordered_at_half_pi == reversed_at_half_pi,
        "Strang_equal_at_pi": strang_l_at_pi == strang_r_at_pi,
        "ordered_equal_at_pi": complex_multiply(lpi, rpi) == complex_multiply(rpi, lpi),
        "joint_generator_commutes_with_exchange": commutator(exchange, h) == zero(),
        "scope": "the x=1 patch reflection only; equal square coefficients",
    })
    resource_checkpoint()
    signal.setitimer(signal.ITIMER_REAL, 0)
    emit("resources", {"elapsed_seconds": round(time.monotonic() - START, 6),
                       "peak_RSS_bytes": memory_bytes(), "wall_limit_seconds": 90,
                       "RSS_limit_bytes": 250_000_000})
    emit("software_check_totals", {"passed": sum(row["ok"] for row in CHECKS),
                                   "failed": sum(not row["ok"] for row in CHECKS),
                                   "scientific_status": "bounded exact computation, not audit"})


if __name__ == "__main__":
    main()
