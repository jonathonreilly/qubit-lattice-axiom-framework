"""Bounded native L4 phase/locality challenges; not a D=2 sector census.

This constructs native operators directly and imports no author helper.
The same campaign author runs/reviews it; this is not an independent audit.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from functools import lru_cache
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import math
import time
import numpy as np

START = time.monotonic()
COUNTS = Counter()


def require(condition, name):
    if not condition:
        raise AssertionError(name)
    COUNTS[name] += 1


L = 4
VERTICES = list(product(range(L), repeat=3))
VID = {r: i for i, r in enumerate(VERTICES)}


def shift(v, axis, amount=1):
    r = list(VERTICES[v])
    r[axis] = (r[axis] + amount) % L
    return VID[tuple(r)]


EDGES = sorted({tuple(sorted((v, shift(v, a))))
                for v in range(len(VERTICES)) for a in range(3)})
EID = {e: k for k, e in enumerate(EDGES)}
INC = [sum(1 << k for k, e in enumerate(EDGES) if v in e)
       for v in range(len(VERTICES))]
EPS = [(-1) ** sum(r) for r in VERTICES]
NEIGHBORS = [sorted(j if i == v else i for i, j in EDGES if v in (i, j))
             for v in range(len(VERTICES))]
STAR = []
QUAD = []
for i, j in EDGES:
    mask = 0
    for v, other in ((i, j), (j, i)):
        for neighbor in NEIGHBORS[v]:
            if neighbor < other:
                mask ^= 1 << EID[tuple(sorted((v, neighbor)))]
    STAR.append(mask)
    parity_interval = 0
    for v in range(i, j):
        parity_interval ^= INC[v]
    QUAD.append(mask ^ parity_interval)
UPPER = [m & ~((1 << (i + 1)) - 1) for i, m in enumerate(QUAD)]
require(all(((QUAD[i] >> j) & 1) == ((QUAD[j] >> i) & 1)
            for i in range(len(EDGES)) for j in range(len(EDGES))),
        'native quadratic phase symmetry')
PLAQUETTES = []
for v in range(len(VERTICES)):
    for a, b in combinations(range(3), 2):
        cycle = [v, shift(v, a), shift(shift(v, a), b), shift(v, b)]
        oriented = list(zip(cycle, cycle[1:] + cycle[:1]))
        edges = tuple(EID[tuple(sorted(e))] for e in oriented)
        PLAQUETTES.append((tuple(oriented), edges, sum(1 << e for e in edges)))
require(len(VERTICES) == 64 and len(EDGES) == len(PLAQUETTES) == 192,
        'actual cubic L4 geometry')
require(all(sum(e in p[1] for p in PLAQUETTES) == 4
            for e in range(len(EDGES))), 'four plaquettes per physical edge')


@lru_cache(None)
def charges(bits):
    return tuple(EPS[v] * ((bits & INC[v]).bit_count() - 3)
                 for v in range(len(VERTICES)))


@lru_cache(None)
def positions(bits):
    q = charges(bits)
    require(q.count(1) == q.count(-1) == 1 and all(abs(x) <= 1 for x in q),
            'D2 low domain')
    return q.index(1), q.index(-1)


@lru_cache(None)
def phase(bits):
    parity = 0
    rest = bits
    while rest:
        low = rest & -rest
        e = low.bit_length() - 1
        parity ^= (UPPER[e] & bits).bit_count() % 2
        rest ^= low
    p, m = positions(bits)
    hole_sign = (-1) ** (p + m - int(m < p))
    return (-1j) ** (bits.bit_count() % 4) * (-1) ** parity * hole_sign


def native_a(bits, i, j):
    e = EID[tuple(sorted((i, j)))]
    amplitude = (-1) ** ((STAR[e] & bits).bit_count() + int(i > j))
    return bits ^ (1 << e), complex(amplitude)


def native_t_edge(bits, e):
    i, j = EDGES[e]
    bi = (-1) ** (bits & INC[i]).bit_count()
    bj = (-1) ** (bits & INC[j]).bit_count()
    if bi == bj:
        return {}
    new = bits ^ (1 << e)
    if any(abs(q) > 1 for q in charges(new)):
        return {}
    amplitude = 0.5j * (bi - bj) * (-1) ** (STAR[e] & bits).bit_count()
    return {new: amplitude}


@lru_cache(None)
def native_hops(bits):
    result = {}
    for e in range(len(EDGES)):
        result.update(native_t_edge(bits, e))
    return result


def native_ring(bits, p):
    oriented, edges, mask = PLAQUETTES[p]
    values = [(bits >> e) & 1 for e in edges]
    if any(values[i] == values[(i + 1) % 4] for i in range(4)):
        return {}
    out = bits
    amplitude = 1j ** 4
    for i, j in reversed(oriented):
        out, factor = native_a(out, i, j)
        amplitude *= factor
    require(out == bits ^ mask, 'ordered native ring support')
    return {bits: 1.0, out: -amplitude}


@lru_cache(None)
def ring_sum(bits):
    result = defaultdict(complex)
    for p in range(len(PLAQUETTES)):
        for out, amplitude in native_ring(bits, p).items():
            result[out] += amplitude
    return {out: amp for out, amp in result.items() if amp}


def commutator_column(bits, left, right):
    result = defaultdict(complex)
    for intermediate, a in right(bits).items():
        for out, b in left(intermediate).items():
            result[out] += a * b
    for intermediate, a in left(bits).items():
        for out, b in right(intermediate).items():
            result[out] -= a * b
    return {out: amp for out, amp in result.items() if amp}


seed = 0
for e, (i, j) in enumerate(EDGES):
    axis = next(a for a in range(3) if VERTICES[i][a] != VERTICES[j][a])
    root = i if shift(i, axis) == j else j
    if VERTICES[root][axis] % 2:
        seed |= 1 << e
require(all(q == 0 for q in charges(seed)), 'explicit ice seed')
adjacent = seed ^ (1 << EID[tuple(sorted((VID[(0, 0, 0)], VID[(1, 0, 0)])))])
require(positions(adjacent) == (VID[(0, 0, 0)], VID[(1, 0, 0)]),
        'adjacent signed pair')
separated = next(out for out in native_hops(adjacent)
                 if positions(out)[0] == positions(adjacent)[0])
require(len(native_hops(adjacent)) == 6 and len(native_hops(separated)) == 8,
        'degree six and degree eight fixtures')

# Keep positive position fixed while varying ring background and negative position.
FIXED = {adjacent, separated}
for start in (adjacent, separated):
    flips = [out for out in ring_sum(start) if out != start]
    FIXED.update(sorted(flips)[:8])
FIXED = sorted(FIXED)
require(len({positions(bits)[0] for bits in FIXED}) == 1,
        'common positive position for coherent Gram challenge')
positive_columns = []
degree_counts = Counter()
wrong_frame_cases = 0
phase_checked_hops = 0
phase_checked_rings = 0
for bits in FIXED:
    p, m = positions(bits)
    column = {out: a for out, a in native_hops(bits).items()
              if positions(out)[0] != p}
    positive_columns.append(column)
    require(len(column) in (3, 4), 'positive degree three or four')
    degree_counts[len(column)] += 1
    for out, amplitude in native_hops(bits).items():
        transformed = phase(out) * amplitude * phase(bits).conjugate()
        require(transformed == -1, 'native signed-hole hop is negative one')
        wrong_frame_cases += int(amplitude != -1)
        phase_checked_hops += 1
        require(native_hops(out)[bits] == amplitude.conjugate(),
                'native hopping Hermiticity')
    for pidx in range(len(PLAQUETTES)):
        for out, amplitude in native_ring(bits, pidx).items():
            require(positions(out) == positions(bits), 'ring preserves signed positions')
            transformed = phase(out) * amplitude * phase(bits).conjugate()
            require(transformed == (1 if out == bits else -1),
                    'native signed-hole RK ring matrix')
            phase_checked_rings += 1
require(wrong_frame_cases > 0, 'omitting native phase has adverse cases')
gram = np.array([[sum(a.conjugate() * col2.get(out, 0)
                      for out, a in col1.items())
                  for col2 in positive_columns] for col1 in positive_columns])
require(np.array_equal(gram, np.diag([len(c) for c in positive_columns])),
        'coherent positive-hop Gram is exact diagonal')
rng = np.random.default_rng(710915)
vec = rng.normal(size=len(FIXED)) + 1j * rng.normal(size=len(FIXED))
vec /= np.linalg.norm(vec)
escape_coefficient = float(np.vdot(vec, gram @ vec).real)
require(3 <= escape_coefficient <= 4, 'arbitrary coherent fixture escape interval')

# Both products are evaluated on the original global configurations, not on a
# projected finite exploration graph. Far ring terms therefore have to cancel.
commutator_l1 = []
commutator_nonzeros = []
for bits in FIXED[:6]:
    col = commutator_column(bits, ring_sum, native_hops)
    value = sum(abs(a) for a in col.values())
    require(value <= 192, 'full native ring-hopping commutator column bound')
    commutator_l1.append(value)
    commutator_nonzeros.append(len(col))
require(max(commutator_l1) > 0, 'ring-hopping commutator not set to zero')
local_pairs = 0
for bits in FIXED[:2]:
    p, m = positions(bits)
    eligible_candidates = [e for e, ends in enumerate(EDGES) if p in ends or m in ends]
    for e in eligible_candidates:
        for pidx, (_, edges, _) in enumerate(PLAQUETTES):
            col = commutator_column(bits, lambda z: native_ring(z, pidx),
                                    lambda z: native_t_edge(z, e))
            if e not in edges:
                require(not col, 'off-plaquette native commutator cancels exactly')
            else:
                require(sum(abs(a) for a in col.values()) <= 4,
                        'on-plaquette commutator column bound')
            local_pairs += 1

# Actual unitary J=0 propagation: enumerate powers on the complete global
# configurations reached at each order. The omitted operator tail has an
# analytic rational bound from ||T||<=8, rather than a truncated graph law.
p_initial = positions(adjacent)[0]
powers = [{adjacent: 1}]
for order in range(1, 5):
    column = defaultdict(int)
    for bits, coefficient in powers[-1].items():
        for out, amplitude in native_hops(bits).items():
            factor = -1j * amplitude
            require(factor in (-1, 1), 'native real-time generator integer entry')
            column[out] += coefficient * int(factor.real)
    powers.append({out: value for out, value in column.items() if value})
time_certificates = []
for instant in (Fraction(1, 128), Fraction(1, 64), Fraction(1, 40)):
    partial = defaultdict(Fraction)
    for order, column in enumerate(powers):
        coefficient = instant ** order / math.factorial(order)
        for bits, value in column.items():
            partial[bits] += coefficient * value
    squared = sum(value ** 2 for bits, value in partial.items()
                  if positions(bits)[0] != p_initial)
    dyadic_scale = 1 << 64
    sqrt_floor = Fraction(math.isqrt(squared.numerator * dyadic_scale ** 2
                                    // squared.denominator), dyadic_scale)
    tail = (8 * instant) ** 5 / (120 * (1 - 8 * instant))
    lower_probability = (sqrt_floor - tail) ** 2
    upper_probability = (sqrt_floor + Fraction(1, dyadic_scale) + tail) ** 2
    require(sqrt_floor > tail and lower_probability >= Fraction(3, 4) * instant ** 2,
            'certified actual J0 unitary escape lower bound')
    # sqrt(3)/64 is the J=0 interval endpoint; square the exact comparison.
    require((64 * instant) ** 2 <= 3, 'certificate time in uniform theorem interval')
    time_certificates.append({'time': str(instant),
                              'operator_tail_bound': str(tail),
                              'escape_probability_lower': float(lower_probability),
                              'escape_probability_upper': float(upper_probability),
                              'claimed_lower': float(Fraction(3, 4) * instant ** 2),
                              'rational_certificate_lower': str(lower_probability)})


def distance(v, w):
    return sum(min((a - b) % L, (b - a) % L)
               for a, b in zip(VERTICES[v], VERTICES[w]))


for bits in FIXED:
    r = distance(p_initial, positions(bits)[0])
    commutator_norm = sum(abs(amplitude) * abs(distance(p_initial, positions(out)[0]) - r)
                          for out, amplitude in native_hops(bits).items())
    require(commutator_norm <= 4, 'actual charge-distance commutator column bound')


def translate(bits, displacement, staggered=True):
    out = 0
    odd = (sum(displacement) % 2) if staggered else 0
    mapping = [VID[tuple((r[a] + displacement[a]) % L for a in range(3))]
               for r in VERTICES]
    for e, (i, j) in enumerate(EDGES):
        target = EID[tuple(sorted((mapping[i], mapping[j])))]
        if ((bits >> e) & 1) ^ odd:
            out |= 1 << target
    return out


translation_cases = 0
ordinary_mutant_cases = 0
for bits in FIXED[:4]:
    for displacement in ((1, 0, 0), (0, 1, 1), (1, 1, 1), (2, 0, 0)):
        out = translate(bits, displacement)
        mapping = [VID[tuple((r[a] + displacement[a]) % L for a in range(3))]
                   for r in VERTICES]
        require(positions(out) == tuple(mapping[v] for v in positions(bits)),
                'staggered translation preserves signed identity')
        require(set(native_hops(out)) == {translate(z, displacement)
                                         for z in native_hops(bits)},
                'staggered translation preserves hopping support')
        require({translate(z, displacement) for z in ring_sum(bits)} == set(ring_sum(out)),
                'staggered translation preserves ring support')
        if sum(displacement) % 2:
            ordinary = translate(bits, displacement, staggered=False)
            require(positions(ordinary) == tuple(mapping[v] for v in reversed(positions(bits))),
                    'ordinary odd translation exchanges signed identities')
            ordinary_mutant_cases += 1
        translation_cases += 1
    require(translate(translate(bits, (1, 0, 0)), (0, 1, 0))
            == translate(bits, (1, 1, 0)), 'staggered translation group law')

# General spectral identity challenged through a separately constructed weighted
# graph with a specified positive ground vector. This is deliberately a toy
# algebra check, not the full native D2 spectrum.
toy_size = 9
psi = np.sqrt(np.arange(1, toy_size + 1, dtype=float))
psi /= np.linalg.norm(psi)
weights = rng.uniform(0.1, 1.0, size=(toy_size, toy_size))
weights = (weights + weights.T) / 2
np.fill_diagonal(weights, 0)
hamiltonian = -weights.copy()
np.fill_diagonal(hamiltonian, (weights @ psi) / psi)
f = np.exp(1j * rng.uniform(0, 2 * math.pi, size=toy_size))
lhs = np.vdot(f * psi, hamiltonian @ (f * psi)).real
rhs = 0.5 * sum(weights[i, j] * psi[i] * psi[j] * abs(f[i] - f[j]) ** 2
                for i in range(toy_size) for j in range(toy_size))
require(np.linalg.norm(hamiltonian @ psi) < 1e-14,
        'separate weighted-graph ground vector')
require(abs(lhs - rhs) < 1e-13, 'complex ground-state Dirichlet identity')
require(abs(lhs - 2 * rhs) > 1e-2, 'missing one-half Dirichlet mutant rejected')
eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
mass = abs(eigenvectors.conj().T @ (f * psi)) ** 2
require(abs(np.dot(eigenvalues, mass) - lhs) < 1e-13,
        'separate spectral measure first moment')
require(mass[eigenvalues <= 2 * lhs].sum() >= 0.5,
        'separate spectral Markov weight')

root = Path(__file__).resolve().parents[1]
result = {
    'status': 'PASS_bounded_checks_personal_not_independent',
    'geometry': {'vertices': 64, 'edges': 192, 'plaquettes': 192},
    'fixed_positive_configurations': len(FIXED),
    'positive_degree_counts': degree_counts,
    'phase_checked_hops': phase_checked_hops,
    'phase_checked_ring_entries': phase_checked_rings,
    'native_phase_omission_adverse_cases': wrong_frame_cases,
    'coherent_escape_coefficient': escape_coefficient,
    'full_commutator_column_l1': commutator_l1,
    'full_commutator_column_nonzeros': commutator_nonzeros,
    'local_commutator_pairs': local_pairs,
    'unitary_taylor_power_support_sizes': [len(column) for column in powers],
    'certified_actual_J0_unitary_escape': time_certificates,
    'translation_cases': translation_cases,
    'ordinary_translation_adverse_cases': ordinary_mutant_cases,
    'toy_dirichlet_absolute_error': abs(lhs - rhs),
    'checks': dict(COUNTS),
    'seconds': time.monotonic() - START,
    'limits': ['finite selected global native configurations; no sector census',
               'commutator products untruncated, but only selected columns checked',
               'no finite-volume native ground-state diagonalization',
               'toy spectral identity is not a native spectral calculation',
               'J0 unitary intervals include exact rational operator-tail bounds',
               'uniform time and momentum theorems rely on the written proofs',
               'no independent scientific review'],
    'sha256': {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
               for p in [Path(__file__).resolve(),
                         root / 'notes/BLOCK7_NATIVE_CHARGE_MOTION_AND_SPECTRAL_WEIGHT.md']},
}
text = json.dumps(result, indent=2)
Path(__file__).with_suffix('.json').write_text(text + '\n')
print(text)
