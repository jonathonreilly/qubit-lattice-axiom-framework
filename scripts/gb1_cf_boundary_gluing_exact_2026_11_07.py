#!/usr/bin/env python3
"""Exact sparse certificate for a supplied finite SU(2) link model.

Run after lab_ops numeric preflight and under a unique numeric lease.
No mutable workflow, goal, or specification is read. The independently
authored fusion checker is imported only after both derivations were frozen.
Scientific coefficients use rational/Gaussian-rational arithmetic only.
Floating point is confined to elapsed-time/resource diagnostics.
"""

from __future__ import annotations

from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import os
import platform
import resource
import signal
import sys
import threading
import time

import gb1_cf_boundary_fusion_check_2026_11_07 as fusion_check


AUDIT_TIMEOUT_SEC = 80
AUDIT_INPUT_PATHS = ("scripts/gb1_cf_boundary_fusion_check_2026_11_07.py",)
MEMORY_STOP_BYTES = 290_000_000
START = time.monotonic()


def peak_rss():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return value if sys.platform == "darwin" else value * 1024


def resource_watch():
    while True:
        if peak_rss() > MEMORY_STOP_BYTES:
            print("RESOURCE STOP: peak RSS exceeded 290 MB", flush=True)
            os._exit(90)
        time.sleep(0.1)


class G:
    """An exact element of Q[i]."""

    __slots__ = ("r", "i")

    def __init__(self, r=0, i=0):
        self.r, self.i = F(r), F(i)

    @staticmethod
    def as_g(value):
        return value if isinstance(value, G) else G(value)

    def __add__(self, other):
        other = self.as_g(other)
        return G(self.r + other.r, self.i + other.i)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-self.as_g(other))

    def __mul__(self, other):
        other = self.as_g(other)
        return G(self.r * other.r - self.i * other.i,
                 self.r * other.i + self.i * other.r)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.as_g(other)
        denominator = other.r ** 2 + other.i ** 2
        return G((self.r * other.r + self.i * other.i) / denominator,
                 (self.i * other.r - self.r * other.i) / denominator)

    def conj(self):
        return G(self.r, -self.i)

    def __bool__(self):
        return bool(self.r or self.i)

    def __eq__(self, other):
        other = self.as_g(other)
        return self.r == other.r and self.i == other.i

    def __str__(self):
        if not self.i:
            return str(self.r)
        if not self.r:
            return f"{self.i}i"
        return f"{self.r}{'+' if self.i > 0 else ''}{self.i}i"


I = G(0, 1)


def clean(vector):
    return {key: value for key, value in vector.items() if value}


def add(*vectors):
    out = {}
    for vector in vectors:
        for key, value in vector.items():
            out[key] = out.get(key, G()) + value
    return clean(out)


def scale(value, vector):
    return clean({key: value * amplitude for key, amplitude in vector.items()})


def difference(left, right):
    return add(left, scale(-1, right))


def inner(left, right):
    return sum((G.as_g(value).conj() * right.get(key, G())
                for key, value in left.items()), G())


def norm_squared(vector):
    result = inner(vector, vector)
    assert result.i == 0
    return result.r


def basis(*key):
    return {tuple(key): G(1)}


def emit(label, value):
    print(label + ": " + json.dumps(value, default=str, sort_keys=True), flush=True)


def entries(vector):
    return [[list(key), str(value)] for key, value in sorted(vector.items())]


def epsilon(a, b, c):
    if len({a, b, c}) < 3:
        return 0
    return 1 if (a, b, c) in ((1, 2, 3), (2, 3, 1), (3, 1, 2)) else -1


def quaternion_product(a, b):
    """Return sign,index for e_a e_b, where e_j=i sigma_j and e_4=I."""
    if a == 4:
        return 1, b
    if b == 4:
        return 1, a
    if a == b:
        return -1, 4
    c = 6 - a - b
    return -epsilon(a, b, c), c


E_COLOR = {
    1: ((G(), I), (I, G())),
    2: ((G(), G(1)), (G(-1), G())),
    3: ((I, G()), (G(), -I)),
    4: ((G(1), G()), (G(), G(1))),
}


def make_cut():
    columns = [basis(0, 0)] + [{} for _ in range(4)]
    for first, second in product(range(1, 5), repeat=2):
        sign, coarse = quaternion_product(second, first)
        columns[coarse][(first, second)] = G(F(sign, 2))
    return columns


def split_link(vector, position, columns):
    out = {}
    for key, amplitude in vector.items():
        for pair, coefficient in columns[key[position]].items():
            dest = key[:position] + pair + key[position + 1:]
            out[dest] = out.get(dest, G()) + amplitude * coefficient
    return clean(out)


def with_color(vector, color):
    return {(color,) + key: value for key, value in vector.items()}


def pull_cut(vector, columns):
    out = {}
    for color, coarse in product(range(2), range(5)):
        value = inner(with_color(columns[coarse], color), vector)
        if value:
            out[(color, coarse)] = value
    return out


def project_cut(vector, columns):
    return split_link(pull_cut(vector, columns), 1, columns)


def local_u(vector, edge, dagger=False):
    """Act on color and one link using the raw P_mu definition."""
    out = {}
    for key, amplitude in vector.items():
        color, occupied = key[0], key[edge + 1]
        for mu in (range(1, 5) if occupied == 0 else (occupied,)):
            new_occupied = mu if occupied == 0 else 0
            for new_color in range(2):
                coefficient = (E_COLOR[mu][color][new_color].conj()
                               if dagger else E_COLOR[mu][new_color][color]) / 2
                if coefficient:
                    dest = list(key)
                    dest[0], dest[edge + 1] = new_color, new_occupied
                    dest = tuple(dest)
                    out[dest] = out.get(dest, G()) + coefficient * amplitude
    return clean(out)


def chain_u(vector, count, dagger=False, reverse_order=False):
    # Forward actions U_1 then U_2 give the operator U_2 U_1.
    order = list(range(count))
    if dagger:
        order.reverse()
    if reverse_order:
        order.reverse()
    for edge in order:
        vector = local_u(vector, edge, dagger)
    return vector


def ell(mu, nu):
    return {(mu, nu): -I, (nu, mu): I}


def matrix_add(*matrices):
    return add(*matrices)


def endpoint_fields():
    j = {1: ell(2, 3), 2: ell(3, 1), 3: ell(1, 2)}
    k = {a: ell(a, 4) for a in j}
    plus = {a: scale(F(1, 2), matrix_add(j[a], k[a])) for a in j}
    minus = {a: scale(F(1, 2), matrix_add(j[a], scale(-1, k[a]))) for a in j}
    return plus, minus


def local_matrix(matrix, edge, vector):
    out = {}
    for key, amplitude in vector.items():
        for (row, column), value in matrix.items():
            if column == key[edge]:
                dest = key[:edge] + (row,) + key[edge + 1:]
                out[dest] = out.get(dest, G()) + value * amplitude
    return clean(out)


def gauss(vector, vertex, axis, plus, minus):
    return add(local_matrix(plus[axis], vertex - 1, vector),
               local_matrix(minus[axis], vertex, vector))


def sparse_rank(rows):
    """Exact row rank over Q for sparse rational rows."""
    pivots = {}
    for input_row in rows:
        row = {key: F(value) for key, value in input_row.items() if value}
        while row:
            column = min(row)
            if column not in pivots:
                value = row[column]
                pivots[column] = {key: val / value for key, val in row.items()}
                break
            multiplier = row[column]
            for key, value in pivots[column].items():
                row[key] = row.get(key, F(0)) - multiplier * value
                if not row[key]:
                    del row[key]
    return len(pivots)


def action_rows(states, actions, imaginary=False):
    lookup = {state: number for number, state in enumerate(states)}
    rows = [{} for _ in range(len(states) * len(actions))]
    for column, state in enumerate(states):
        for number, action in enumerate(actions):
            for dest, coefficient in action(basis(*state)).items():
                value = coefficient / I if imaginary else G.as_g(coefficient)
                assert value.i == 0
                rows[number * len(states) + lookup[dest]][column] = value.r
    return rows


def electric(vector, edge):
    return {key: F(3, 4) * value for key, value in vector.items() if key[edge] != 0}


def verify_isometry(columns):
    for mu, nu in product(range(5), repeat=2):
        value = inner(columns[mu], columns[nu])
        if value != int(mu == nu):
            raise ValueError(f"cut metric ({mu},{nu})={value}, required {int(mu == nu)}")


def verify_chain(columns, reverse_order=False):
    for color, mu, dagger in product(range(2), range(5), (False, True)):
        coarse = basis(color, mu)
        image = split_link(coarse, 1, columns)
        fine = chain_u(image, 2, dagger, reverse_order)
        lifted = split_link(local_u(coarse, 0, dagger), 1, columns)
        residual = difference(fine, lifted)
        if residual:
            raise ValueError(f"full operator residual: color={color},mu={mu},dagger={dagger},norm2={norm_squared(residual)}")


def verify_electric_accounting(columns, weight):
    for mu in range(5):
        image = columns[mu]
        fine = scale(weight, add(electric(image, 0), electric(image, 1)))
        coarse = scale(F(3, 4) if mu else 0, image)
        residual = difference(fine, coarse)
        if residual:
            raise ValueError(f"electric accounting residual: mu={mu},norm2={norm_squared(residual)}")


def rejected(label, check):
    try:
        check()
    except ValueError as error:
        emit(label, {"rejected": True, "reason": str(error)})
        return
    raise AssertionError(f"Mutation escaped rejection: {label}")


def half_spin(vector, axis, positions):
    out = {}
    for key, value in vector.items():
        for position in positions:
            if axis == "z":
                out[key] = out.get(key, G()) + (F(1, 2) if key[position] == 0 else F(-1, 2)) * value
            elif (axis == "+" and key[position] == 1) or (axis == "-" and key[position] == 0):
                dest = key[:position] + (1-key[position],) + key[position + 1:]
                out[dest] = out.get(dest, G()) + value
    return clean(out)


def pair_singlet_project(vector, first, second):
    # s=|01>-|10>, <s|s>=2, projector=ss^dagger/2.
    out = {}
    for key, value in vector.items():
        pair = key[first], key[second]
        if pair not in ((0, 1), (1, 0)):
            continue
        incoming = 1 if pair == (0, 1) else -1
        for a, b, outgoing in ((0, 1, 1), (1, 0, -1)):
            dest = list(key)
            dest[first], dest[second] = a, b
            dest = tuple(dest)
            out[dest] = out.get(dest, G()) + F(incoming * outgoing, 2) * value
    return clean(out)


def boundary_grouping_example():
    # Regions A and B each carry one half-spin. Region C retains two ends.
    singlet_pair = {(0, 1): G(1), (1, 0): G(-1)}
    assert norm_squared(singlet_pair) == 2
    pair_states = list(product(range(2), repeat=2))
    for state in pair_states:
        projected = pair_singlet_project(basis(*state), 0, 1)
        assert pair_singlet_project(projected, 0, 1) == projected
    pair_norm_mutant = scale(2, pair_singlet_project(basis(0, 1), 0, 1))
    idempotence_defect = difference(scale(2, pair_singlet_project(pair_norm_mutant, 0, 1)), pair_norm_mutant)
    assert idempotence_defect

    double_singlet = {(a, b, c, d): x * y
                      for (a, b), x in singlet_pair.items()
                      for (c, d), y in singlet_pair.items()}
    triplet_channel = {
        (0, 0, 1, 1): G(1), (1, 1, 0, 0): G(1),
        (0, 1, 0, 1): G(F(-1, 2)), (0, 1, 1, 0): G(F(-1, 2)),
        (1, 0, 0, 1): G(F(-1, 2)), (1, 0, 1, 0): G(F(-1, 2)),
    }
    for vector in (double_singlet, triplet_channel):
        for axis in ("z", "+", "-"):
            assert not half_spin(vector, axis, range(4))
    assert not inner(double_singlet, triplet_channel)
    assert pair_singlet_project(double_singlet, 0, 1) == double_singlet
    assert not pair_singlet_project(triplet_channel, 0, 1)
    assert not pair_singlet_project(triplet_channel, 2, 3)
    states = list(product(range(2), repeat=4))
    actions = [lambda vector, axis=axis: half_spin(vector, axis, range(4))
               for axis in ("z", "+", "-")]
    full_rank = sparse_rank(action_rows(states, actions))
    early_actions = actions + [lambda vector: difference(vector, pair_singlet_project(vector, 0, 1))]
    early_rank = sparse_rank(action_rows(states, early_actions))
    emit("boundary_grouping", {
        "singlet_metric": str(norm_squared(singlet_pair)),
        "unnormalized_singlet_projector_idempotence_defect_norm2": str(norm_squared(idempotence_defect)),
        "all_four_ends_global_singlet_dimension": len(states) - full_rank,
        "after_premature_AB_singlet_dimension": len(states) - early_rank,
        "retained_channel_norm2": str(norm_squared(double_singlet)),
        "discarded_triplet_channel": entries(triplet_channel),
        "discarded_channel_norm2": str(norm_squared(triplet_channel)),
        "discarded_channel_total_Gauss_action": "zero for J_z,J_+,J_-",
        "premature_AB_singlet_action_on_discarded_channel": "zero",
    })
    assert len(states) - full_rank == 2
    assert len(states) - early_rank == 1


def main():
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError("numeric time budget")))
    signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC)
    threading.Thread(target=resource_watch, daemon=True).start()
    thread_names = ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS")
    assert all(os.environ.get(name) == "1" for name in thread_names)
    emit("execution", {
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "parent_source_revision": "ba7790560e50afe712a68d42f550493e980cb19c",
        "arithmetic": "exact rational and Gaussian rational; no floating-point scientific coefficients",
        "python": platform.python_version(), "AUDIT_TIMEOUT_SEC": AUDIT_TIMEOUT_SEC,
        "memory_stop_bytes": MEMORY_STOP_BYTES,
        "thread_settings": {name: os.environ[name] for name in thread_names},
        "mutable_workflow_or_spec_inputs": [],
    })
    # Check quaternion multiplication against explicit 2x2 Gaussian matrices.
    for a, b in product(range(1, 5), repeat=2):
        sign, c = quaternion_product(a, b)
        for row, column in product(range(2), repeat=2):
            value = sum((E_COLOR[a][row][k] * E_COLOR[b][k][column] for k in range(2)), G())
            assert value == sign * E_COLOR[c][row][column]
    cut = make_cut()
    verify_isometry(cut)
    emit("cut_columns_link_order_g1_g2", {str(mu): entries(column) for mu, column in enumerate(cut)})
    emit("cut_metric", [[str(inner(a, b)) for b in cut] for a in cut])
    plus, minus = endpoint_fields()
    for mu, axis in product(range(5), range(1, 4)):
        assert not gauss(cut[mu], 1, axis, plus, minus)
        for fields, fine_edge in ((plus, 1), (minus, 0)):
            coarse = local_matrix(fields[axis], 0, basis(mu))
            assert split_link(coarse, 0, cut) == local_matrix(fields[axis], fine_edge, cut[mu])
    states2 = list(product(range(5), repeat=2))
    actions2 = [lambda vector, axis=axis: gauss(vector, 1, axis, plus, minus)
                for axis in range(1, 4)]
    rank2 = sparse_rank(action_rows(states2, actions2, imaginary=True))
    assert len(states2) - rank2 == len(cut)
    emit("internal_Gauss_two_links", {"stacked_generator_rank": rank2,
                                       "kernel_dimension": len(states2) - rank2,
                                       "cut_image_dimension": len(cut),
                                       "endpoint_intertwiners": "N-_coarse -> N-_first; N+_coarse -> N+_second"})
    verify_chain(cut)
    for color, mu, dagger in product(range(2), range(5), (False, True)):
        image = with_color(cut[mu], color)
        actual = chain_u(image, 2, dagger)
        assert not difference(actual, project_cut(actual, cut))
    emit("chain_operator", {"full_unprojected_intertwining": "(U2 U1) D = D U and (U2 U1)^dagger D = D U^dagger",
                             "image_leakage_for_all_color_link_basis_inputs": "exactly zero"})

    three = []
    for mu in range(5):
        left = split_link(cut[mu], 0, cut)
        right = split_link(cut[mu], 1, cut)
        assert left == right
        three.append(left)
        for vertex, axis in product((1, 2), range(1, 4)):
            assert not gauss(left, vertex, axis, plus, minus)
    verify_isometry(three)
    states3 = list(product(range(5), repeat=3))
    actions3 = [lambda vector, vertex=vertex, axis=axis: gauss(vector, vertex, axis, plus, minus)
                for vertex, axis in product((1, 2), range(1, 4))]
    rank3 = sparse_rank(action_rows(states3, actions3, imaginary=True))
    assert len(states3) - rank3 == len(three)
    for color, mu, dagger in product(range(2), range(5), (False, True)):
        actual = chain_u(with_color(three[mu], color), 3, dagger)
        coarse_output = local_u(basis(color, mu), 0, dagger)
        lifted = split_link(split_link(coarse_output, 1, cut), 1, cut)
        assert actual == lifted
    emit("second_subdivision", {"coassociativity": "exact equality on all five coarse basis vectors",
                                 "image_support_sizes": [len(vector) for vector in three],
                                 "stacked_internal_Gauss_rank": rank3,
                                 "joint_internal_kernel_dimension": len(states3) - rank3,
                                 "three_link_chain_and_adjoint_full_intertwining": True})

    electric_data = {}
    for count, columns in ((2, cut), (3, three)):
        diagonal = []
        for mu, image in enumerate(columns):
            total = add(*(electric(image, edge) for edge in range(count)))
            expected = scale(F(3, 4) if mu else 0, image)
            for edge in range(count):
                assert electric(image, edge) == expected
            assert total == scale(count, expected)
            diagonal.append(str(inner(image, total)))
        electric_data[str(count) + "_fine_links"] = diagonal
    verify_electric_accounting(cut, F(1, 2))
    emit("electric_accounting", electric_data)
    mutated_cut = [cut[0]] + [scale(2, vector) for vector in cut[1:]]
    rejected("mutation_missing_cut_half", lambda: verify_isometry(mutated_cut))
    rejected("mutation_unweighted_electric_sum", lambda: verify_electric_accounting(cut, F(1)))
    rejected("mutation_reversed_chain_order", lambda: verify_chain(cut, reverse_order=True))
    wrong_chain = chain_u(with_color(cut[0], 0), 2, reverse_order=True)
    wrong_leak = difference(wrong_chain, project_cut(wrong_chain, cut))
    assert wrong_leak
    emit("wrong_chain_full_image_witness", {"input": "color 0, coarse empty state",
                                            "leakage_norm2": str(norm_squared(wrong_leak))})
    boundary_grouping_example()
    # A duplicate physical link is not an independent pair carrying both copies
    # of its full operator algebra. Display the raw noncommuting coordinates.
    p1 = {(1, 0): G(F(1, 2)), (0, 1): G(F(1, 2))}
    p2 = {(2, 0): G(F(1, 2)), (0, 2): G(F(1, 2))}
    witness = difference(local_matrix(p1, 0, local_matrix(p2, 0, basis(2))),
                         local_matrix(p2, 0, local_matrix(p1, 0, basis(2))))
    assert witness
    emit("overlap_coordinate_witness", {"commutator_input": "|2>",
                                         "P1_P2_minus_P2_P1_output": entries(witness)})
    # Integrated after freezing the separate coordinate and coefficient/fusion derivations.
    fusion_check.cut_checks()
    fusion_check.graph_checks(None)
    emit("separately_authored_fusion_certificate", {"exact_equalities": fusion_check.CHECKS,
         "helper": AUDIT_INPUT_PATHS[0], "formal_audit": False})
    emit("resources", {"elapsed_seconds_diagnostic": round(time.monotonic() - START, 5),
                       "peak_RSS_bytes": peak_rss(),
                       "largest_Gauss_domain_dimension": len(states3),
                       "largest_cut_vector_support": max(len(vector) for vector in three)})
    print("AUTHOR CERTIFICATE COMPLETE: exact finite identities and explicit rejected mutations; no independent status.", flush=True)
    signal.setitimer(signal.ITIMER_REAL, 0)


if __name__ == "__main__":
    main()
