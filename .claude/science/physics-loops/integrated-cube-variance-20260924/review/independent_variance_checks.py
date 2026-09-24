"""Independent finite controls for the averaged-variance PRE.

No campaign builder or author argument is imported. The cube loss bound is
proved by the local blocks and the combinatorial cover, not by sampled phases.
The two-level diagnostic is only a check of the Hermitian/no-event distinction.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import hashlib
import json

import numpy as np
import sympy as sp

A = (0, 3, 5, 6)
B = (1, 2, 4, 7)
edges = tuple((a, b) for a in A for b in B if (a ^ b).bit_count() == 1)
neighbors = {a: tuple(b for aa, b in edges if aa == a) for a in A}

# Two positive local charges: input is the occupied leaf, output the vacant leaf.
same_sign = sp.ones(3) - sp.eye(3)
same_gram = same_sign.T * same_sign
assert same_gram == sp.eye(3) + sp.ones(3)
same_spectrum = same_gram.eigenvals()
assert same_spectrum == {sp.Integer(1): 2, sp.Integer(4): 1}

# Opposite local charges: input (occupied leaf, A charge), output (+ leaf,- leaf).
opposite_inputs = [(k, sign) for k in range(3) for sign in (1, -1)]
opposite_outputs = [(p, m) for p in range(3) for m in range(3) if p != m]
opposite = sp.zeros(6)
for col, (old, sign) in enumerate(opposite_inputs):
    for destination in range(3):
        if destination == old:
            continue
        output = (destination, old) if sign == 1 else (old, destination)
        opposite[opposite_outputs.index(output), col] += 1
opposite_spectrum = (opposite.T * opposite).eigenvals()
assert opposite_spectrum == {sp.Integer(0): 1, sp.Integer(1): 2, sp.Integer(3): 2, sp.Integer(4): 1}

words = []
for occupied in combinations(range(8), 6):
    for minus in occupied:
        words.append(tuple(0 if v not in occupied else -1 if v == minus else 1 for v in range(8)))
pwords = [q for q in words if all(q[a] for a in A)]
onewords = [q for q in words if sum(not q[a] for a in A) == 1]
assert (len(pwords), len(onewords)) == (36, 96)
index1 = {q: i for i, q in enumerate(onewords)}

cover_count = Counter()
cover_rows = []
for q in pwords:
    vacancies = {b for b in B if not q[b]}
    active = [a for a in A if vacancies.issubset(neighbors[a])]
    assert len(active) == 2
    local_occupied_pairs = [set([a]) | (set(neighbors[a]) - vacancies) for a in active]
    assert len(local_occupied_pairs[0]) == len(local_occupied_pairs[1]) == 2
    assert not (local_occupied_pairs[0] & local_occupied_pairs[1])
    negative = q.index(-1)
    outside_count = sum(negative not in pair for pair in local_occupied_pairs)
    assert outside_count in (1, 2)
    cover_count[outside_count] += 1
    cover_rows.append({'q': q, 'vacant_B': sorted(vacancies), 'active_A': active, 'negative_outside_local_pair_count': outside_count})
assert cover_count == {1: 24, 2: 12}

# An independent full charge-hop Gram calculation at the flat phase.
F = sp.zeros(96, 36)
for col, q in enumerate(pwords):
    for a, b in edges:
        if q[a] and not q[b]:
            nq = list(q)
            nq[a], nq[b] = 0, q[a]
            F[index1[tuple(nq)], col] += 1
Gamma = sp.diag(*[2 * int(any(not q[a] and not q[b] for a, b in edges)) for q in onewords])
Gamma_B = F.T * Gamma * F
assert all(Gamma_B[i, i] == 8 for i in range(36))
assert Gamma_B == Gamma_B.T
flat_spectrum = Gamma_B.eigenvals()
assert min(flat_spectrum) >= 2 and max(flat_spectrum) <= 16

# Defect discriminator: replacing the unsigned same-charge hop by an oriented
# incidence would introduce a spurious dark direction and invalidate the bound.
wrong_same_sign = sp.Matrix([[1, -1, 0], [0, 1, -1], [-1, 0, 1]])
assert wrong_same_sign.det() == 0
assert same_sign.det() != 0

# Exact energy-identity coefficient check on a noncommuting finite example.
alpha = sp.Rational(3, 7)
H = sp.Matrix([[2, 1], [1, -1]])
G = sp.diag(0, 2)
u = sp.Matrix([1, sp.I])
du = -sp.I * H * u - alpha * G * u
inner = lambda x, y: (sp.conjugate(x).T * y)[0]
g_derivative = inner(du, G * u) + inner(u, G * du)
identity_residual = sp.simplify(inner(H*u, H*u) - inner(du, du) - alpha**2 * inner(G*u, G*u) - alpha * g_derivative)
wrong_endpoint_residual = sp.simplify(inner(H*u, H*u) - inner(du, du) - alpha**2 * inner(G*u, G*u) - 2*alpha * g_derivative)
assert identity_residual == 0 and wrong_endpoint_residual != 0

# Separate two-level diagnostic: low eigenstate of the dissipative generator
# carries a Hermitian energy norm of order 1/epsilon, despite its slow evolution.
# This is not the cube and does not establish the cube limit.
kappa = .7
lower, upper = .2, .4
toy_rows = []
for epsilon in (.2, .1, .05, .025):
    h = np.array([[epsilon**2, -epsilon], [-epsilon, 1.]], dtype=complex)
    gamma = np.diag([0., 2.])
    heff = h - .5j*kappa*epsilon**2*gamma
    vals, vecs = np.linalg.eig(heff)
    idx = int(np.argmin(abs(vals)))
    vec = vecs[:, idx] / np.linalg.norm(vecs[:, idx])
    rate = float(2 * (-1j*vals[idx]/epsilon**4).real)
    integral = (np.exp(rate*upper)-np.exp(rate*lower))/rate
    coefficient = float(epsilon**2 * np.vdot(h@vec, h@vec).real / epsilon**8 * integral)
    predicted = float(kappa/2*(np.exp(-2*kappa*lower)-np.exp(-2*kappa*upper)))
    toy_rows.append({'epsilon':epsilon,'scaled_integrated_low_H_squared':coefficient,'limiting_survival_coefficient':predicted,'absolute_error':abs(coefficient-predicted)})
assert toy_rows[-1]['absolute_error'] < toy_rows[0]['absolute_error']/20

def spectrum_dict(d):
    return {str(value): int(multiplicity) for value, multiplicity in sorted(d.items(), key=lambda x:float(x[0]))}

result = {
    'same_sign_F': [list(same_sign.row(i)) for i in range(3)],
    'same_sign_Gram_spectrum': spectrum_dict(same_spectrum),
    'opposite_sign_Gram_spectrum': spectrum_dict(opposite_spectrum),
    'cover_counts': dict(cover_count),
    'complete_cover_rows': cover_rows,
    'flat_complete_Gamma_B_spectrum': spectrum_dict(flat_spectrum),
    'wrong_signed_hop_determinant': str(wrong_same_sign.det()),
    'correct_unsigned_hop_determinant': str(same_sign.det()),
    'energy_identity_residual': str(identity_residual),
    'wrong_endpoint_coefficient_residual': str(wrong_endpoint_residual),
    'two_level_diagnostic_only': toy_rows,
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
result['same_sign_F'] = [[int(x) for x in row] for row in result['same_sign_F']]
Path(__file__).with_name('FINITE_CHECKS.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k != 'complete_cover_rows'}, indent=2))
print('All exact assertions completed; the toy diagnostic is not a cube asymptotic proof.')
