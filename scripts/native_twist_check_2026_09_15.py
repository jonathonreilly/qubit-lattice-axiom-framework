"""Native winding tapes plus a separate exact weighted-graph response check.

No diagonalization of the full native D2 sector, and no independent review.
"""

# Canonical packaging; supplied scientific fixtures below are unchanged.
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['docs/FINITE_NATIVE_WINDING_CURVATURE_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'docs/NATIVE_CHARGE_MOTION_AND_SPECTRAL_WEIGHT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'docs/NATIVE_GLOBAL_CHARGE_CONNECTIVITY_AND_EXCHANGE_NOTE_2026-09-08.md']
from pathlib import Path as _InputPath
_REPO_ROOT = _InputPath(__file__).resolve().parents[1]
_INPUT_TEXT = {q: (_REPO_ROOT / q).read_text() for q in AUDIT_INPUT_PATHS}
assert 'finite_native_winding_curvature_bounded_theorem_note_2026-09-15' in _INPUT_TEXT['docs/FINITE_NATIVE_WINDING_CURVATURE_BOUNDED_THEOREM_NOTE_2026-09-15.md']
_OUTPUT_JSON = _REPO_ROOT / 'logs/runner-cache/native_twist_check_2026_09_15.json'
_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import math
import time
import numpy as np
import sympy as sp

START = time.monotonic()
CHECKS = Counter()


def require(condition, name):
    if not condition:
        raise AssertionError(name)
    CHECKS[name] += 1


def native_geometry(length):
    vertices = list(product(range(length), repeat=3))
    index = {v: i for i, v in enumerate(vertices)}
    epsilon = [(-1) ** sum(v) for v in vertices]

    def shifted(v, axis, amount=1):
        r = list(vertices[v])
        r[axis] = (r[axis] + amount) % length
        return index[tuple(r)]

    positive = [(v, shifted(v, a), a) for v in range(len(vertices)) for a in range(3)]
    edges = sorted(tuple(sorted((v, w))) for v, w, _ in positive)
    require(len(edges) == len(set(edges)), 'simple physical edge geometry')
    edge_index = {e: i for i, e in enumerate(edges)}
    orientation = {edge_index[tuple(sorted((v, w)))]: (v, w, a) for v, w, a in positive}
    incident = [sum(1 << e for e, ends in enumerate(edges) if v in ends)
                for v in range(len(vertices))]
    neighbors = [sorted(w if v == x else v for v, w in edges if x in (v, w))
                 for x in range(len(vertices))]
    masks = []
    for i, j in edges:
        mask = 0
        for x, y in ((i, j), (j, i)):
            for v in neighbors[x]:
                if v < y:
                    mask ^= 1 << edge_index[tuple(sorted((x, v)))]
        masks.append(mask)

    def charge(bits):
        return tuple(epsilon[v] * ((bits & incident[v]).bit_count() - 3)
                     for v in range(len(vertices)))

    def pos(bits):
        q = charge(bits)
        require(q.count(1) == q.count(-1) == 1 and all(abs(z) <= 1 for z in q),
                'every winding prefix in actual D2 low domain')
        return q.index(1), q.index(-1)

    def polarization(bits):
        out = [0, 0, 0]
        for e, (v, _, a) in orientation.items():
            out[a] -= epsilon[v] * (2 * ((bits >> e) & 1) - 1)
        require(all(z % 2 == 0 for z in out), 'integer electric polarization')
        return tuple(z // 2 for z in out)

    def hop(bits, source, target):
        e = edge_index[tuple(sorted((source, target)))]
        i, j = edges[e]
        bi = (-1) ** (bits & incident[i]).bit_count()
        bj = (-1) ** (bits & incident[j]).bit_count()
        require(bi != bj, 'nonzero ambient native hopping factor')
        result = bits ^ (1 << e)
        amplitude = 0.5j * (bi - bj) * (-1) ** (masks[e] & bits).bit_count()
        pos(result)
        q = charge(bits)[source]
        require(q in (-1, 1) and charge(bits)[target] == 0,
                'charged source and neutral target')
        v, w, axis = orientation[e]
        sigma = 1 if (source, target) == (v, w) else -1
        before, after = polarization(bits), polarization(result)
        require(all(after[a] - before[a] == (q * sigma if a == axis else 0)
                    for a in range(3)), 'exact physical signed-hop polarization increment')
        return result, amplitude, q, axis, sigma

    polarized = sum(1 << e for e, (v, _, _) in orientation.items() if epsilon[v] == 1)
    require(not any(charge(polarized)), 'full polarized ice seed')
    tapes = []
    for axis in range(3):
        bits = polarized ^ (1 << edge_index[tuple(sorted((0, shifted(0, axis))))])
        initial = bits
        amplitude = 1 + 0j
        phases = [0, 0]
        tape = []
        seen = set()
        for step in range(2 * length):
            require(bits not in seen, 'winding cycle has distinct intermediate configurations')
            seen.add(bits)
            p, m = pos(bits)
            source = p if step % 2 == 0 else m
            target = shifted(source, axis)
            before = bits
            bits, factor, q, used_axis, sigma = hop(bits, source, target)
            require(used_axis == axis and sigma == 1, 'forward native winding step')
            amplitude *= factor
            phases[0 if q == 1 else 1] += sigma
            tape.append({'step': step, 'charge': q, 'source': vertices[source],
                         'target': vertices[target], 'native_phase': [factor.real, factor.imag],
                         'configuration_before_hex': hex(before)})
        require(bits == initial, 'winding restores every physical edge bit')
        require(amplitude == 1, 'native complete winding phase positive')
        require(phases == [length, length], 'both charges wind once')
        require(phases[0] - phases[1] == 0 and Fraction(sum(phases), length) == 2,
                'difference twist trivial but common twist nontrivial')
        tapes.append({'axis': axis, 'length': length, 'steps': 2 * length,
                      'signed_holonomy': 0, 'positive_only_holonomy': 1,
                      'common_holonomy': 2, 'native_product': [amplitude.real, amplitude.imag],
                      'tape': tape})

    # A second ice background has many flippable faces, unlike the polarized one.
    if length == 4:
        ice = sum(1 << e for e, (v, _, a) in orientation.items() if vertices[v][a] % 2)
        require(not any(charge(ice)), 'second ice background')
        bits = ice ^ (1 << edge_index[tuple(sorted((0, shifted(0, 0))))])
        flippable = 0
        before = polarization(bits)
        for v in range(len(vertices)):
            for a, b in combinations(range(3), 2):
                cycle = [v, shifted(v, a), shifted(shifted(v, a), b), shifted(v, b)]
                face = [edge_index[tuple(sorted(e))]
                        for e in zip(cycle, cycle[1:] + cycle[:1])]
                values = [(bits >> e) & 1 for e in face]
                if all(values[i] != values[(i + 1) % 4] for i in range(4)):
                    out = bits ^ sum(1 << e for e in face)
                    require(charge(out) == charge(bits), 'actual gated face preserves charges')
                    require(polarization(out) == before, 'actual gated face preserves polarization')
                    flippable += 1
        require(flippable > 0, 'nonempty gated-ring control')
    else:
        flippable = None
    return {'L': length, 'vertices': len(vertices), 'edges': len(edges),
            'flippable_ring_checks': flippable, 'cycles': tapes}


native_results = [native_geometry(length) for length in (4, 6, 8)]

# Separate exact graph: ground vector known from construction, but not a native
# spectrum. Compare eigenvalue perturbation with weighted least squares.
n = 8
graph_edges = [(i, (i + 1) % n) for i in range(n)] + [(0, 3), (2, 5), (1, 6)]
v = sp.Matrix([1, 2, 1, 3, 2, 1, 2, 3])
normalizer = (v.T * v)[0]
a = [sp.Rational((i % 3) + 1, 3) for i in range(len(graph_edges))]
B = sp.zeros(len(graph_edges), n)
H = sp.zeros(n)
for e, (x, y) in enumerate(graph_edges):
    B[e, x], B[e, y] = -1, 1
    H[x, y] = H[y, x] = -a[e]
for x in range(n):
    H[x, x] = -sum(H[x, y] * v[y] for y in range(n) if x != y) / v[x]
require(H * v == sp.zeros(n, 1), 'separate graph exact positive ground vector')
c = sp.diag(*[a[e] * v[x] * v[y] / normalizer for e, (x, y) in enumerate(graph_edges)])
alpha = sp.Matrix([sp.Rational(1, 4) if e < n and e % 2 == 0 else 0
                   for e in range(len(graph_edges))])
potential = sp.Matrix([sp.Rational(i % 2, 4) for i in range(n)])
alpha_minus = alpha - B * potential


def curvature_network(form):
    laplacian = B.T * c * B
    rhs = B.T * c * form
    # Pin h_0=0, independent of the eigenvector normalization below.
    reduced = laplacian[1:, 1:].inv() * rhs[1:, :]
    h = sp.Matrix([0] + list(reduced))
    residual = form - B * h
    return sp.factor(2 * (residual.T * c * residual)[0])


def curvature_perturbation(form):
    first, second = sp.zeros(n), sp.zeros(n)
    for e, (x, y) in enumerate(graph_edges):
        first[y, x] = -sp.I * a[e] * form[e]
        first[x, y] = sp.I * a[e] * form[e]
        second[x, y] = second[y, x] = a[e] * form[e] ** 2
    bordered = H.row_join(v).col_join(v.T.row_join(sp.zeros(1)))
    correction = bordered.inv() * (-first * v).col_join(sp.zeros(1, 1))
    tangent = correction[:n, :]
    return sp.factor(((v.T * second * v)[0] + 2 * (v.T * first * tangent)[0]) / normalizer)


D = curvature_network(alpha)
for label, form in [('positive', alpha), ('negative', alpha_minus),
                    ('difference', alpha - alpha_minus), ('sum', alpha + alpha_minus)]:
    require(curvature_network(form) == curvature_perturbation(form),
            'exact network versus eigenvalue perturbation ' + label)
require(D > 0 and curvature_network(alpha_minus) == D
        and curvature_network(alpha - alpha_minus) == 0
        and curvature_network(alpha + alpha_minus) == 4 * D,
        'separate graph rank-one species response')
cycle_lower = sp.factor(2 / sum(1 / c[e, e] for e in range(n)))
bare_upper = sp.factor(2 * (alpha.T * c * alpha)[0])
require(0 < cycle_lower <= D <= bare_upper, 'exact winding conductance sandwich')
require(D < bare_upper, 'discarding background corrector changes response')


def twisted_matrix(phi_plus, phi_minus):
    out = np.array(H, dtype=complex)
    form = phi_plus * np.array(alpha, dtype=float).ravel() + phi_minus * np.array(alpha_minus, dtype=float).ravel()
    for e, (x, y) in enumerate(graph_edges):
        out[y, x] = -float(a[e]) * np.exp(1j * form[e])
        out[x, y] = out[y, x].conjugate()
    return out


eigenvalue_checks = []
for h in (0.08, 0.04, 0.02):
    ground = float(np.linalg.eigvalsh(twisted_matrix(h, 0))[0])
    curvature = 2 * ground / h ** 2
    require(ground > 0 and abs(curvature - float(D)) < 2e-5,
            'separate graph finite-angle eigenvalue challenge')
    eigenvalue_checks.append({'angle': h, 'energy': ground, 'curvature_estimate': curvature})
phi_plus, phi_minus = 0.37, -0.11
unitary = np.diag(np.exp(1j * phi_minus * np.array(potential, dtype=float).ravel()))
twist_error = float(np.max(abs(unitary @ twisted_matrix(phi_plus, phi_minus)
                                 @ unitary.conj().T - twisted_matrix(phi_plus + phi_minus, 0))))
require(twist_error < 1e-14, 'separate graph full twist unitary identity')

root = Path(__file__).resolve().parents[1]
result = {'status': 'PASS_personal_finite_challenges_not_independent_review',
          'N5_scope': {
              'per_element': '108 actual native signed-hop increments and phases',
              'per_site': 'full low-charge vectors on every winding prefix;94 gated faces',
              'per_mode': 'one uniform twist per axis; no full native spectrum computed',
              'per_block': 'native D2 tapes; separate eight-vertex response algebra control',
              'lattice_wide': 'finiteL4,L6,L8 tapes; general finite identity is analytic; no thermodynamic stiffness'},
          'native_tapes': native_results,
          'exact_separate_graph': {'curvature': str(D), 'cycle_lower': str(cycle_lower),
                                   'bare_upper': str(bare_upper), 'unitary_error': twist_error,
                                   'finite_angle_challenges': eigenvalue_checks},
          'checks': dict(CHECKS), 'seconds': time.monotonic() - START,
          'limits': ['native checks use actual full configurations and phases',
                     'explicit winding tapes are not a full configuration census',
                     'weighted graph spectrum is a distinct algebra control, not native D2',
                     'native ground amplitudes and thermodynamic stiffness not computed',
                     'no independent scientific review'],
          'sha256': {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in [Path(__file__).resolve(),
                               root / 'docs/FINITE_NATIVE_WINDING_CURVATURE_BOUNDED_THEOREM_NOTE_2026-09-15.md']}}
output = json.dumps(result, indent=2)
_OUTPUT_JSON.write_text(output + '\n')
print(output)

if __name__ == '__main__':
    print('TOTAL: PASS=1 FAIL=0')
    print('Completed family: complete finite companion program; individual checks and diagnostics remain in structured JSON')
    print('per_element: signed polarization increments and winding identities')
    print('per_site: finite native winding configurations')
    print('per_mode: finite twist/curvature controls, not thermodynamic stiffness')
    print('per_block: one complete companion family; imported helpers are shared implementation, not independent evidence')
    print('lattice_wide: analytical claims and infinite/iterated limits checked in written proof, not executed here')
