"""Actual infinite-background local operators, finite word matrices, tensor bounds.

The infinite threshold theorem is analytic, not an extrapolation of these checks.
"""

# Canonical packaging; supplied scientific fixtures below are unchanged.
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['docs/POLARIZED_WORD_CARRIER_AND_ESSENTIAL_THRESHOLD_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'docs/NATIVE_RK_CHARGE_STABILITY_NOTE_2026-09-08.md', 'docs/NATIVE_LOW_CHARGE_U1_DICTIONARY_NOTE_2026-09-08.md', 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md']
from pathlib import Path as _InputPath
_REPO_ROOT = _InputPath(__file__).resolve().parents[1]
_INPUT_TEXT = {q: (_REPO_ROOT / q).read_text() for q in AUDIT_INPUT_PATHS}
assert 'polarized_word_carrier_and_essential_threshold_bounded_theorem_note_2026-09-15' in _INPUT_TEXT['docs/POLARIZED_WORD_CARRIER_AND_ESSENTIAL_THRESHOLD_BOUNDED_THEOREM_NOTE_2026-09-15.md']
_OUTPUT_JSON = _REPO_ROOT / 'logs/runner-cache/polarized_word_check_2026_09_15.json'
_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
from collections import Counter
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib
import json
import math
import time
import numpy as np
from scipy.sparse import coo_matrix

START = time.monotonic()
CHECKS = Counter()


def require(condition, label):
    if not condition:
        raise AssertionError(label)
    CHECKS[label] += 1


def shift(v, a, delta=1):
    return tuple(x + (delta if i == a else 0) for i, x in enumerate(v))


def physical_edge(i, j):
    low, high = sorted((i, j))
    axis = next(a for a in range(3) if low[a] != high[a])
    require(shift(low, axis) == high, 'physical nearest-neighbor edge')
    return low, axis


@lru_cache(None)
def path_edges(state):
    anchor, word = state
    edges = []
    current = anchor
    for axis in word:
        edges.append((current, axis))
        current = shift(current, axis)
    return frozenset(edges), current


def n_value(edge, flipped):
    origin, _ = edge
    baseline = int(sum(origin) % 2 == 0)
    return baseline ^ int(edge in flipped)


def neighbors(v):
    return sorted(shift(v, a, delta) for a in range(3) for delta in (-1, 1))


def degree(v, flipped):
    return sum(n_value(physical_edge(v, w), flipped) for w in neighbors(v))


def native_a(i, j, flipped):
    amplitude = -1 if i > j else 1
    low, high = sorted((i, j))
    for vertex, other in ((low, high), (high, low)):
        for neighbor in neighbors(vertex):
            if neighbor < other:
                amplitude *= 1 - 2 * n_value(physical_edge(vertex, neighbor), flipped)
    out = set(flipped)
    e = physical_edge(i, j)
    if e in out:
        out.remove(e)
    else:
        out.add(e)
    return frozenset(out), complex(amplitude)


def transition(state, operation, letter=None):
    m, word = state
    if operation == 'append':
        return m, word + (letter,)
    if operation == 'prepend':
        return shift(m, letter, -1), (letter,) + word
    require(len(word) >= 2, 'no empty word enters physical sector')
    if operation == 'popright':
        return m, word[:-1]
    if operation == 'popleft':
        return shift(m, word[0]), word[1:]
    raise ValueError(operation)


@lru_cache(None)
def native_hop(state, target):
    original, p = path_edges(state)
    final, p2 = path_edges(target)
    difference = original ^ final
    require(len(difference) == 1, 'word transition flips exactly one actual edge')
    origin, axis = next(iter(difference))
    i, j = origin, shift(origin, axis)
    bi, bj = (-1) ** degree(i, original), (-1) ** degree(j, original)
    require(bi != bj, 'native hopping factor nonzero')
    toggled, a = native_a(i, j, original)
    require(toggled == final, 'native hop exact edge image')
    amplitude = 0.5j * (bi - bj) * a
    require(abs(amplitude) == 1, 'native hop unit modulus')
    for v in {i, j, state[0], p, target[0], p2}:
        q = (-1) ** sum(v) * (degree(v, final) - 3)
        expected = int(v == p2) - int(v == target[0])
        require(q == expected, 'literal full-background endpoint charge')
    return amplitude


@lru_cache(None)
def frame(target):
    state = ((0, 0, 0), (0,))
    phase = 1 + 0j

    def perform(operation, letter=None):
        nonlocal state, phase
        out = transition(state, operation, letter)
        phase = -phase / native_hop(state, out)
        state = out

    def set_letter(letter):
        if state[1] == (letter,):
            return
        perform('prepend', 0)
        perform('popright')
        perform('append', letter)
        perform('popleft')

    anchor, word = target
    for axis in range(3):
        set_letter(axis)
        for _ in range(abs(anchor[axis])):
            if anchor[axis] > 0:
                perform('append', axis)
                perform('popleft')
            else:
                perform('prepend', axis)
                perform('popright')
    set_letter(word[0])
    for letter in word[1:]:
        perform('append', letter)
    require(state == target, 'canonical native path reaches requested word and anchor')
    return phase


native_states = 0
native_ring_checks = 0
for anchor in ((0, 0, 0), (-1, 1, 0)):
    for n in range(1, 5):
        for word in product(range(3), repeat=n):
            state = (anchor, word)
            original, endpoint = path_edges(state)
            native_states += 1
            targets = [transition(state, op, i) for op in ('append', 'prepend') for i in range(3)]
            if n >= 2:
                targets += [transition(state, 'popright'), transition(state, 'popleft')]
            require(len(set(targets)) == (6 if n == 1 else 8), 'native word hopping degree')
            for target in targets:
                require(frame(target) * native_hop(state, target) * frame(state).conjugate() == -1,
                        'canonical infinite-background frame negative native hop')
            predicted = {}
            for j in range(n - 1):
                if word[j] != word[j + 1]:
                    swapped = word[:j] + (word[j + 1], word[j]) + word[j + 2:]
                    target = (anchor, swapped)
                    predicted[path_edges(target)[0]] = target
            faces = set()
            for origin, a in original:
                for b in range(3):
                    if b != a:
                        for base in (origin, shift(origin, b, -1)):
                            faces.add((base, min(a, b), max(a, b)))
            actual = set()
            for base, a, b in faces:
                cycle = [base, shift(base, a), shift(shift(base, a), b), shift(base, b)]
                pairs = list(zip(cycle, cycle[1:] + cycle[:1]))
                bits = [n_value(physical_edge(i, j), original) for i, j in pairs]
                if any(bits[j] == bits[(j + 1) % 4] for j in range(4)):
                    continue
                out = original
                amplitude = 1j ** 4
                for i, j in reversed(pairs):
                    out, factor = native_a(i, j, out)
                    amplitude *= factor
                require(out in predicted, 'every actual gated native face is an adjacent letter swap')
                target = predicted[out]
                require(frame(target) * amplitude * frame(state).conjugate() == 1,
                        'actual native ring phase in canonical word frame')
                actual.add(out)
                native_ring_checks += 1
            require(actual == set(predicted), 'all and only adjacent unequal letters are flippable faces')

# A bent nonmonotone path is not a one-positive/one-negative finite perturbation
# of this polarized background. Do not replace the directed word carrier.
nonmonotone = frozenset([((0, 0, 0), 0), ((1, 0, 0), 1), ((0, 1, 0), 0)])
vertices = {v for origin, a in nonmonotone for v in (origin, shift(origin, a))}
bad_charges = sorted((-1) ** sum(v) * (degree(v, nonmonotone) - 3) for v in vertices)
require(bad_charges != [-1, 0, 0, 1], 'undirected-path replacement rejected on actual charges')


MAX_N = 7
WORDS = [w for n in range(1, MAX_N + 1) for w in product(range(3), repeat=n)]
INDEX = {w: i for i, w in enumerate(WORDS)}
OFFSETS = {n: sum(3 ** j for j in range(1, n)) for n in range(1, MAX_N + 1)}
DIM = len(WORDS)


def matrices(k):
    ar, ac, av, kr, kc, kv = [], [], [], [], [], []
    for w, col in INDEX.items():
        if len(w) < MAX_N:
            for i in range(3):
                for new, factor in ((w + (i,), 1), ((i,) + w, np.exp(1j * k[i]))):
                    row = INDEX[new]
                    ar.extend([row, col]); ac.extend([col, row]); av.extend([factor, np.conj(factor)])
        for j in range(len(w) - 1):
            if w[j] != w[j + 1]:
                new = w[:j] + (w[j + 1], w[j]) + w[j + 2:]
                kr.extend([col, INDEX[new]]); kc.extend([col, col]); kv.extend([1, -1])
    return (coo_matrix((av, (ar, ac)), shape=(DIM, DIM)).tocsr(),
            coo_matrix((kv, (kr, kc)), shape=(DIM, DIM)).tocsr())


def tensor(factors):
    result = np.array([1.0 + 0j])
    for factor in factors:
        result = np.kron(result, factor)
    return result


def embedded(factors):
    n = len(factors)
    result = np.zeros(DIM, complex)
    result[OFFSETS[n]:OFFSETS[n] + 3 ** n] = tensor(factors)
    return result


u = np.ones(3, complex) / math.sqrt(3)
fiber_results = []
texture_results = []
for k in ((0.0, 0.0, 0.0), (0.3, -0.7, 1.2), (math.pi / 2,) * 3):
    v = np.exp(1j * np.array(k)) / math.sqrt(3)
    _, _, vh = np.linalg.svd(np.vstack([u.conj(), v.conj()]))
    w = vh.conj().T[:, -1]
    require(abs(np.vdot(u, w)) < 1e-14 and abs(np.vdot(v, w)) < 1e-14,
            'marker orthogonal to both endpoint vectors')
    A, K = matrices(k)
    marker = {(r, s): embedded([v] * r + [w] + [u] * s)
              for r in range(4) for s in range(4)}
    gram = np.array([[np.vdot(x, y) for y in marker.values()] for x in marker.values()])
    require(np.max(abs(gram - np.eye(16))) < 2e-14, 'finite two-ended marker vectors orthonormal')
    maximum_error = 0.0
    for r in range(3):
        for s in range(3):
            target = marker[r + 1, s] + marker[r, s + 1]
            if r:
                target += marker[r - 1, s]
            if s:
                target += marker[r, s - 1]
            error = np.linalg.norm(A @ marker[r, s] - math.sqrt(3) * target)
            maximum_error = max(maximum_error, error)
    require(maximum_error < 2e-14, 'actual word-matrix action equals two half-lines')

    def curve(s):
        if s <= 0.5:
            return np.cos(math.pi * s) * v + np.sin(math.pi * s) * w
        return np.cos(math.pi * (s - 0.5)) * w + np.sin(math.pi * (s - 0.5)) * u

    def factors(n):
        return [curve(j / (n + 1)) for j in range(1, n + 1)]

    def overlaps(n):
        old, new = factors(n), factors(n + 1)
        left = np.vdot(new[0], v) * np.prod([np.vdot(new[j + 1], old[j]) for j in range(n)])
        right = np.prod([np.vdot(new[j], old[j]) for j in range(n)]) * np.vdot(new[-1], u)
        ring = sum(1 - abs(np.vdot(old[j], old[j + 1])) ** 2 for j in range(n - 1))
        return left, right, ring

    for n in range(1, 6):
        x, y = embedded(factors(n)), embedded(factors(n + 1))
        left, right, ring = overlaps(n)
        require(abs(np.vdot(y, A @ x) - math.sqrt(3) * (left + right)) < 2e-14,
                'full finite word matrix versus tensor creation contractions')
        require(abs(np.vdot(x, K @ x) - ring) < 2e-14,
                'full finite word matrix versus tensor swap contractions')
    for N in (8, 16, 32, 64, 128):
        b = np.sqrt(2 / (N + 2)) * np.sin(math.pi * np.arange(1, N + 2) / (N + 2))
        data = [overlaps(n) for n in range(N, 2 * N + 1)]
        for n, (left, right, ring) in zip(range(N, 2 * N + 1), data):
            require(abs(left - 1) <= math.pi ** 2 / (2 * (n + 1)) + 1e-13
                    and abs(right - 1) <= math.pi ** 2 / (2 * (n + 1)) + 1e-13,
                    'complex horizontal creation-overlap bound')
            require(-1e-13 <= ring <= math.pi ** 2 / n + 1e-13,
                    'ferromagnetic texture energy bound')
        hopping = 2 * math.sqrt(3) * sum(b[j] * b[j + 1] * (data[j][0] + data[j][1]).real
                                       for j in range(N))
        ring = sum(b[j] ** 2 * data[j][2] for j in range(N + 1))
        for J in (0, 1, 100):
            excess = 4 * math.sqrt(3) - hopping + J * ring
            bound = J * math.pi ** 2 / N + 4 * math.sqrt(3) * (
                1 - (1 - math.pi ** 2 / (2 * (N + 1))) * math.cos(math.pi / (N + 2)))
            require(-1e-12 <= excess <= bound + 1e-12, 'actual tensor trial obeys analytic threshold bound')
            texture_results.append({'k': k, 'N': N, 'J': J, 'lambda': 1,
                                    'energy_above_threshold': excess, 'analytic_upper': bound})
    fiber_results.append({'k': k, 'finite_word_dimension': DIM,
                          'marker_action_error': maximum_error})

A0, K0 = matrices((0, 0, 0))
for N in (3, 5, 7):
    radial = sum(math.sqrt(2 / (N + 1)) * math.sin(math.pi * n / (N + 1))
                 * embedded([u] * n) for n in range(1, N + 1))
    require(np.linalg.norm(K0 @ radial) < 1e-13, 'uniform word radial trial has exactly zero ring action numerically')
    expectation = math.fsum(z.real for z in radial.conj() * (A0 @ radial))
    require(abs(expectation - 4 * math.sqrt(3) * math.cos(math.pi / (N + 1))) < 1e-13,
            'radial finite word hopping expectation')

# A curve with the same projective direction but uncontrolled complex phase
# has a persistent boundary-creation phase; large n does not remove it.
mutant_n = 64
old = [np.exp(0.5j * math.pi * (1 - j / (mutant_n + 1))) * u
       for j in range(1, mutant_n + 1)]
new = [np.exp(0.5j * math.pi * (1 - j / (mutant_n + 2))) * u
       for j in range(1, mutant_n + 2)]
mutant_left = np.vdot(new[0], 1j * u) * np.prod([np.vdot(new[j + 1], old[j]) for j in range(mutant_n)])
require(abs(mutant_left - 1) > 0.7
        and abs(mutant_left - 1) > math.pi ** 2 / (2 * (mutant_n + 1)),
        'omitting horizontal complex phase control fails creation bound')

root = Path(__file__).resolve().parents[1]
result = {'status': 'PASS_personal_bounded_native_and_tensor_challenges',
          'native_states': native_states, 'native_ring_checks': native_ring_checks,
          'nonmonotone_mutant_charges': bad_charges,
          'finite_fiber_checks': fiber_results, 'texture_trials': texture_results,
          'periodic_to_polarized_energy_separation_per_lambda': 36 / 5 - 4 * math.sqrt(3),
          'nonhorizontal_curve_creation_gap': float(abs(mutant_left - 1)),
          'checks': dict(CHECKS), 'seconds': time.monotonic() - START,
          'limits': ['finite native words/anchors, not all configurations',
                     'infinite classification and spectral threshold proved analytically',
                     'no infinite matrix diagonalization or spectral extrapolation',
                     'tensor product contractions avoid exponential enumeration',
                     'specified polarized finite-excitation boundary sector',
                     'not the periodic ground state or a selected physical vacuum',
                     'same author; no independent scientific review'],
          'sha256': {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in [Path(__file__).resolve(), root / 'docs/POLARIZED_WORD_CARRIER_AND_ESSENTIAL_THRESHOLD_BOUNDED_THEOREM_NOTE_2026-09-15.md']}}
output = json.dumps(result, indent=2)
_OUTPUT_JSON.write_text(output + '\n')
print(output)

if __name__ == '__main__':
    print('TOTAL: PASS=1 FAIL=0')
    print('Completed family: complete finite companion program; individual checks and diagnostics remain in structured JSON')
    print('per_element: word/native-hop and radial identities')
    print('per_site: finite polarized words and edge configurations')
    print('per_mode: finite truncated word spectra and radial moments')
    print('per_block: one complete companion family; imported helpers are shared implementation, not independent evidence')
    print('lattice_wide: analytical claims and infinite/iterated limits checked in written proof, not executed here')
