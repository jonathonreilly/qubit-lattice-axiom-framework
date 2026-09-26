#!/usr/bin/env python3
"""Independent exact controls; reads no primary source or previous checker."""
from __future__ import annotations

import itertools as it
import json
import math
import random
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

import numpy as np
import sympy as s

HERE = Path(__file__).resolve().parent
(HERE / "PROGRESS.log").write_text("")
CHECKS = []


def check(name, ok, **details):
    if not bool(ok):
        raise AssertionError(name)
    CHECKS.append(dict(name=name, status="PASS", **details))
    with (HERE / "PROGRESS.log").open("a") as stream:
        stream.write(name + " PASS\n")


def equal_matrix(a, b):
    return all(s.simplify(x) == 0 for x in a-b)


V = [(0, 0, 0), (1, 0, 0), (-1, 0, 0),
     (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
LABEL = {v: a for a, v in enumerate(V)}
WORDS3 = list(it.product(range(7), repeat=3))
INDEX3 = {word: k for k, word in enumerate(WORDS3)}
PAIRS = list(it.combinations_with_replacement(range(7), 2))
INDEX2 = {pair: k for k, pair in enumerate(PAIRS)}
TRIPLES = list(it.combinations(range(7), 3))
W = [1, 2, 3, 4, 5, 6, 7]
DEN = sum(W)
P = [F(w, DEN) for w in W]


def parity(sequence):
    return (-1)**sum(sequence[i] > sequence[j]
                    for i in range(len(sequence)) for j in range(i+1, len(sequence)))


def rotations(proper_only=True):
    answer = []
    for perm in it.permutations(range(3)):
        for signs in it.product((-1, 1), repeat=3):
            determinant = parity(perm)*math.prod(signs)
            if proper_only and determinant != 1:
                continue
            mapping = []
            for vector in V:
                moved = [0]*3
                for i in range(3):
                    moved[perm[i]] = signs[i]*vector[i]
                mapping.append(LABEL[tuple(moved)])
            answer.append((perm, signs, mapping, determinant))
    return answer


ROTATIONS = rotations()


@lru_cache(None)
def arbitrary_tensor(sorted_word):
    return (sum((i+1)*(a+1)**2 for i, a in enumerate(sorted_word)) % 19)-9


def tensor(word):
    return arbitrary_tensor(tuple(sorted(word)))


def drive_on_ring(word, x, k):
    L = len(word)
    a, b = word[x], word[(x+1) % L]
    value = 0
    for j in range(k):
        context = ([word[(x+d) % L] for d in range(-j, 0)] +
                   [word[(x+d) % L] for d in range(2, k-j+1)])
        value += tensor(context+[a])-tensor(context+[b])
    return value


rng = random.Random(20260921)
arbitrary_controls = []
for k in range(1, 6):
    for _ in range(100):
        word = [rng.randrange(7) for _ in range(2*k+3)]
        assert sum(drive_on_ring(word, x, k) for x in range(len(word))) == 0
        x = rng.randrange(len(word))
        before = drive_on_ring(word, x, k)
        swapped = word.copy()
        swapped[x], swapped[(x+1) % len(word)] = swapped[(x+1) % len(word)], swapped[x]
        assert drive_on_ring(swapped, x, k) == -before
    check(f"arbitrary_tensor_k_{k}/periodic_balance_and_antisymmetry", True,
          exact_seeded_strings=100)
    product_numerator = 0
    conditional_numerators = [0]*7
    for word in it.product(range(7), repeat=k):
        value = tensor(word)
        product_numerator += math.prod(W[a] for a in word)*value
    for a in range(7):
        for rest in it.product(range(7), repeat=k-1):
            conditional_numerators[a] += math.prod(W[b] for b in rest)*tensor((a,)+rest)
    potential = F(product_numerator, DEN**k)
    predicted = [k*P[a]*(F(conditional_numerators[a], DEN**(k-1))-potential)
                 for a in range(7)]
    raw = [0]*7
    for rest in it.product(range(7), repeat=k-1):
        weights_rest = math.prod(W[a] for a in rest)
        for a, b in it.product(range(7), repeat=2):
            value = k*(tensor((a,)+rest)-tensor((b,)+rest))*W[a]*W[b]*weights_rest
            raw[a] += value
            raw[b] -= value
    direct = [F(value, 2*DEN**(k+1)) for value in raw]
    check(f"arbitrary_tensor_k_{k}/exact_product_current",
          predicted == direct and sum(direct) == 0,
          potential=str(potential), currents=[str(x) for x in direct])
    arbitrary_controls.append(dict(k=k, potential=str(potential),
                                   currents=[str(x) for x in direct]))


def cubic_tensor_times_three(word, axis):
    a, b, c = word
    n = [int(z != 0) for z in word]
    f = [V[z][axis] for z in word]
    q = [x*x for x in f]
    sum_nnf = sum(n[i]*n[j]*f[k] for i, j, k in ((0, 1, 2), (0, 2, 1), (1, 2, 0)))
    sum_nqf = sum(n[i]*q[j]*f[k] for i, j, k in it.permutations(range(3)))
    assert sum_nqf % 2 == 0
    return 2*sum_nnf-3*(sum_nqf//2)+9*f[0]*f[1]*f[2]


T = [{word: cubic_tensor_times_three(word, axis) for word in WORDS3}
     for axis in range(3)]
check("cubic_tensor/full_symmetry_and_norm",
      all(T[i][word] == T[i][tuple(sorted(word))] for i in range(3) for word in WORDS3)
      and {value for table in T for value in table.values()} == {0, -1, 1, -2, 2, -6, 6, -10, 10}
      and all(T[i][word] == 0 for i in range(3) for word in WORDS3 if 0 in word),
      tensor_supremum="10/3 at alpha=1")
for perm, signs, mapping, det in rotations(False):
    for i in range(3):
        for word in WORDS3:
            assert T[perm[i]][tuple(mapping[a] for a in word)] == signs[i]*T[i][word]
check("cubic_tensor/all_48_joint_cubic_transformations", True, tensor_cases=48*3*7**3)


def cubic_drive_times_three(word, axis=0):
    l2, l1, a, b, r1, r2 = word
    table = T[axis]
    return (table[(a, r1, r2)]-table[(b, r1, r2)]
            +table[(l1, a, r1)]-table[(l1, b, r1)]
            +table[(l2, l1, a)]-table[(l2, l1, b)])


cubic_raw = {"linear_K_11": [0]*7, "positive_floor_1": [0]*7}
min_h, max_h = 0, 0
for word in it.product(range(7), repeat=6):
    h3 = cubic_drive_times_three(word)
    min_h, max_h = min(min_h, h3), max(max_h, h3)
    weights = math.prod(W[a] for a in word)
    a, b = word[2:4]
    for name, rate_numerator in (("linear_K_11", 66+h3),
                                 ("positive_floor_1", 3+max(h3, 0))):
        cubic_raw[name][a] += weights*rate_numerator
        cubic_raw[name][b] -= weights*rate_numerator
rho0 = sum(P[1:])
qi0, gi0 = P[1]+P[2], P[1]-P[2]
potential0 = rho0*(2*rho0-3*qi0)*gi0+3*gi0**3
R0, Q0, V0 = (4*rho0-3*qi0)*gi0, -3*rho0*gi0, 2*rho0**2-3*rho0*qi0+9*gi0**2
predicted0 = [P[a]*((0 if a == 0 else R0+Q0*V[a][0]**2+V0*V[a][0])-3*potential0)
              for a in range(7)]
for name, scale in (("linear_K_11", 6), ("positive_floor_1", 3)):
    direct = [F(value, scale*DEN**6) for value in cubic_raw[name]]
    check("cubic_tensor/exact_six_site_current/"+name, direct == predicted0,
          currents=[str(x) for x in direct], local_strings=7**6)
check("cubic_tensor/sharp_drive_bound", (min_h, max_h) == (-60, 60),
      drive_range=["-20", "20"], linear_rate_range=[1, 21], positive_rate_range=[1, 21])
contracted = F(sum(T[0][word]*math.prod(W[a] for a in word) for word in WORDS3), 3*DEN**3)
check("cubic_tensor/product_polynomial", contracted == potential0,
      potential=str(potential0))


alpha, rho, z = s.symbols("alpha rho z", real=True)
qs = s.symbols("q1:4", real=True)
gs = s.symbols("g1:4", real=True)
nus = s.symbols("nu1:4", real=True)
rs = sum(qs)
currents = []
for i in range(3):
    potential = alpha*(rs*(2*rs-3*qs[i])*gs[i]+3*gs[i]**3)
    R = alpha*(4*rs-3*qs[i])*gs[i]
    Q = -3*alpha*rs*gs[i]
    Z = alpha*(2*rs**2-3*rs*qs[i]+9*gs[i]**2)
    drift = R-3*potential
    jq = s.Matrix([qs[j]*drift+int(i == j)*(Q*qs[i]+Z*gs[i]) for j in range(3)])
    jg = s.Matrix([gs[j]*drift+int(i == j)*(Q*gs[i]+Z*qs[i]) for j in range(3)])
    check(f"cubic_flux/total_density_identity_axis_{i}",
          s.expand(sum(jq)-3*(1-rs)*potential) == 0)
    balance = dict(zip(qs, [rho/3]*3))
    density_balanced = s.simplify(sum(jq).subs(balance))
    vector_balanced = jg.subs(balance).applyfunc(s.simplify)
    quadrupole_balanced = (jq-s.ones(3, 1)*sum(jq)/3).subs(balance).applyfunc(s.simplify)
    expected_density = 3*alpha*(1-rho)*(rho**2*gs[i]+3*gs[i]**3)
    expected_vector = s.Matrix([alpha*rho**3*int(i == j)/3
        +3*alpha*(rho*(1-rho)*gs[i]-3*gs[i]**3)*gs[j] for j in range(3)])
    expected_quad = s.Matrix([3*alpha*(3*int(i == j)-1)*gs[i]**3 for j in range(3)])
    check(f"cubic_flux/exact_balanced_nonlinear_currents_axis_{i}",
          s.simplify(density_balanced-expected_density) == 0
          and equal_matrix(vector_balanced, expected_vector)
          and equal_matrix(quadrupole_balanced, expected_quad))
    currents.append(jq.col_join(jg))
balance_zero = dict(zip(qs, [rho/3]*3)) | dict(zip(gs, [0]*3))
Jac = sum((nus[i]*currents[i].jacobian(qs+gs).subs(balance_zero) for i in range(3)), s.zeros(6))
top = alpha*rho**2*(1-rho)*s.ones(3)*s.diag(*nus)
bottom = alpha*rho**2*s.diag(*nus)*s.ones(3)
expected_Jac = s.zeros(3).row_join(top).col_join(bottom.row_join(s.zeros(3)))
check("cubic_flux/full_six_field_linearization", equal_matrix(Jac, expected_Jac))
speed_squared = 3*alpha**2*rho**4*(1-rho)*sum(nu**2 for nu in nus)
characteristic = Jac.charpoly(z)
check("cubic_flux/full_characteristic_polynomial",
      s.factor(characteristic.as_expr().subs(characteristic.gen, z)
               -z**4*(z**2-speed_squared)) == 0,
      characteristic_polynomial="z^4 (z^2-3 alpha^2 rho^4 (1-rho) |nu|^2)")
check("cubic_flux/cubic_minimal_polynomial",
      equal_matrix(Jac**3, speed_squared*Jac))

rotation45 = s.Matrix([[1, -1, 0], [1, 1, 0], [0, 0, s.sqrt(2)]])/s.sqrt(2)
g_before = s.Matrix([s.Rational(1, 12), 0, 0])
g_after = rotation45*g_before
def balanced_density_current(g):
    return s.Matrix([s.Rational(3, 2)*(x/4+3*x**3) for x in g])
defect = (balanced_density_current(g_after)-rotation45*balanced_density_current(g_before)).applyfunc(s.simplify)
check("cubic_flux/continuous_rotation_counterexample", defect != s.zeros(3, 1),
      rho="1/2", alpha="1", initial_g=["1/12", "0", "0"],
      actual_minus_rotated_density_current=[str(v) for v in defect])


def rank_mod(matrix, prime=1009):
    """Exact rank over a prime field; supplies a rational-rank lower bound."""
    matrix = np.array(matrix, dtype=np.int64, copy=True) % prime
    rows, columns = matrix.shape
    row = 0
    for col in range(columns):
        candidates = np.flatnonzero(matrix[row:, col])
        if not len(candidates):
            continue
        pivot = row+int(candidates[0])
        matrix[[row, pivot]] = matrix[[pivot, row]]
        matrix[row, col:] = matrix[row, col:]*pow(int(matrix[row, col]), prime-2, prime) % prime
        chosen = np.flatnonzero(matrix[row+1:, col])+row+1
        if len(chosen):
            matrix[chosen, col:] = (matrix[chosen, col:]
                 -matrix[chosen, col, None]*matrix[row, col:][None, :]) % prime
        row += 1
        if row == rows:
            break
    return row


constraint_rows = []
for l, a, b, r in it.product(range(7), repeat=4):
    if a > b:
        continue
    row = np.zeros(7**3, dtype=np.int64)
    for triple, coefficient in (((l, a, b), 1), ((l, b, a), 1),
                                ((a, b, r), -1), ((b, a, r), -1)):
        row[INDEX3[triple]] += coefficient
    constraint_rows.append(row)
constraints = np.array(constraint_rows)
basis = np.zeros((7**3, len(PAIRS)+len(TRIPLES)), dtype=np.int64)
for row, (x, y, z0) in enumerate(WORDS3):
    for pair, coefficient in (((x, y), 1), ((y, z0), 1), ((x, z0), -1)):
        basis[row, INDEX2[tuple(sorted(pair))]] += coefficient
    if len({x, y, z0}) == 3:
        basis[row, len(PAIRS)+TRIPLES.index(tuple(sorted((x, y, z0))))] = parity((x, y, z0))
rank_constraints = rank_mod(constraints)
rank_basis = rank_mod(basis)
check("four_site_classification/complete_coboundary_antisymmetry_kernel",
      np.all(constraints@basis == 0) and rank_constraints == 280 and rank_basis == 63,
      triple_potential_dimension=343, constraint_rank_mod_1009=rank_constraints,
      explicit_rational_kernel_dimension=rank_basis,
      symmetric_tensor_parameters=28, alternating_tensor_parameters=35)
images = np.array([basis[INDEX3[(l, a, b)]]-basis[INDEX3[(a, b, r)]]
                   for l, a, b, r in it.product(range(7), repeat=4)])
constant_gauge = np.concatenate((np.ones(len(PAIRS), dtype=np.int64),
                                 np.zeros(len(TRIPLES), dtype=np.int64)))
check("four_site_classification/additive_constant_is_only_gauge",
      rank_mod(images) == 62 and np.all(basis@constant_gauge == 1)
      and np.all(images@constant_gauge == 0), drive_space_dimension=62,
      constant_tensor_gauge_verified=True)


cov_rows = []
for perm, signs, mapping, _ in ROTATIONS:
    for i in range(3):
        for pair in PAIRS:
            row = np.zeros(3*len(PAIRS), dtype=np.int64)
            moved = tuple(sorted(mapping[a] for a in pair))
            row[perm[i]*len(PAIRS)+INDEX2[moved]] += 1
            row[i*len(PAIRS)+INDEX2[pair]] -= signs[i]
            cov_rows.append(row)
cov_constraints = np.array(cov_rows)
cov_basis = np.zeros((3*len(PAIRS), 3), dtype=np.int64)
for i in range(3):
    for pair in PAIRS:
        a, b = pair
        fa, fb = V[a][i], V[b][i]
        na, nb = int(a != 0), int(b != 0)
        qa, qb = fa*fa, fb*fb
        cov_basis[i*len(PAIRS)+INDEX2[pair]] = [fa+fb, na*fb+fa*nb, qa*fb+fa*qb]
rank_cov = rank_mod(cov_constraints)
check("proper_cubic_mean_potential/complete_three_parameter_space",
      rank_cov == 81 and rank_mod(cov_basis) == 3
      and np.all(cov_constraints@cov_basis == 0),
      ambient_symmetric_tensor_parameters=84, constraint_rank_mod_1009=rank_cov,
      potential_basis=["g_i", "rho g_i", "q_i g_i"])


def det3(a, b, c):
    va, vb, vc = V[a], V[b], V[c]
    return (va[0]*(vb[1]*vc[2]-vb[2]*vc[1])
            -va[1]*(vb[0]*vc[2]-vb[2]*vc[0])
            +va[2]*(vb[0]*vc[1]-vb[1]*vc[0]))


ALT = {word: det3(*word) for word in WORDS3}
def alt_drive(word):
    l, a, b, r = word
    return ALT[(l, a, b)]-ALT[(a, b, r)]


alt_raw = [0]*7
for word in it.product(range(7), repeat=4):
    h = alt_drive(word)
    l, a, b, r = word
    assert alt_drive((l, b, a, r)) == -h
    rate = 1+max(h, 0)
    weights = math.prod(W[c] for c in word)
    alt_raw[a] += rate*weights
    alt_raw[b] -= rate*weights
    for perm, signs, mapping, _ in ROTATIONS:
        for i in range(3):
            moved = tuple(mapping[c] for c in (word if signs[i] == 1 else word[::-1]))
            assert alt_drive(moved) == h
check("alternating_drive/nonzero_proper_cubic_example",
      alt_drive((1, 3, 5, 0)) == 1 and alt_raw == [0]*7,
      witness_word=["+e1", "+e2", "+e3", "vacancy"],
      actual_positive_part_product_currents=[str(F(x, DEN**4)) for x in alt_raw])
inverted = tuple(LABEL[tuple(-x for x in V[a])] for a in (0, 5, 3, 1))
check("alternating_drive/improper_rotation_counterexample", alt_drive(inverted) == -1,
      original_drive=1, inversion_transformed_drive=-1,
      original_positive_part_rate=2, transformed_positive_part_rate=1)


u, v, w = s.symbols("u v w", real=True)
small_a = u+rho*(v+2*w/3)
beta = rho*(v-u-2*rho*(v+w/3))/3
gamma = v*rho/3
Z = u+2*rho*(v+w/3)
check("quadratic_mean_potential/balanced_spectrum_identities",
      s.expand(small_a+3*beta-(1-rho)*Z) == 0
      and s.expand(small_a+3*gamma-Z) == 0)
tuned = {u: 0, w: -3*v/2}
check("quadratic_mean_potential/all_density_isotropy_tuning",
      s.simplify(small_a.subs(tuned)) == 0
      and s.simplify((3*beta*gamma).subs(tuned)-v**2*rho**2*(1-rho)/3) == 0,
      tuning="u=0, w=-3v/2, v nonzero",
      squared_speed="v^2 rho^2 (1-rho)/3")


RESULT = {
    "checks_passed": len(CHECKS), "checks_failed": 0,
    "arbitrary_degree_controls": arbitrary_controls,
    "dependencies": {"numpy": np.__version__, "sympy": s.__version__},
    "checks": CHECKS,
    "scope": "Exact finite controls for separately proved arbitrary-degree and classification statements; no primary source imported.",
}
serialized = json.dumps(RESULT, indent=2, sort_keys=True)+"\n"
(HERE / "RESULTS.json").write_text(serialized)
print(serialized, end="")
