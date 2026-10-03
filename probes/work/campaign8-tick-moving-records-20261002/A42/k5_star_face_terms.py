"""A42 check k5: are A20's gate terms S_x (compass star) and F_x (face term)
exactly invariant (with sign) under the 24 rotations about x, for each onsite action?
A Pauli string is a dict site -> axis index; a rotation R maps sigma^a at p to
(rho(R) e_a).sigma at R p, which for these actions is a signed Pauli.
"""
import itertools, numpy as np
ROTS = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        R = np.zeros((3, 3), int)
        for i, p in enumerate(perm): R[p, i] = signs[i]
        if round(np.linalg.det(R)) == 1: ROTS.append(R)
sgn = lambda R: int(round(np.linalg.det(np.abs(R))))
ACT = {'trivial': lambda R: np.eye(3, dtype=int), 'sign_twist': lambda R: np.diag([1, sgn(R), sgn(R)]),
       'axis': lambda R: sgn(R) * np.abs(R), 'full': lambda R: R}
E = np.eye(3, dtype=int)
S = {}
for a in range(3):
    S[tuple(E[a])] = a; S[tuple(-E[a])] = a
F = {}
for a, b in itertools.combinations(range(3), 2):
    c = 3 - a - b
    for sa, sb in itertools.product([1, -1], repeat=2):
        F[tuple(sa * E[a] + sb * E[b])] = c
def image(string, R, rho):
    out, sign = {}, 1
    M = rho(R)
    for p, a in string.items():
        v = M[:, a]                      # rho(R) e_a, a signed basis vector
        k = int(np.argmax(np.abs(v))); sign *= int(v[k])
        out[tuple(int(t) for t in R @ np.array(p))] = k
    return out, sign
for name, rho in ACT.items():
    res = []
    for lab, st in [('S_x', S), ('F_x', F)]:
        bad = sum(1 for R in ROTS if image(st, R, rho) != (st, 1))
        res.append(f'{lab}: {bad}/24 rotations fail')
    print(f'{name:11s}', '; '.join(res))
