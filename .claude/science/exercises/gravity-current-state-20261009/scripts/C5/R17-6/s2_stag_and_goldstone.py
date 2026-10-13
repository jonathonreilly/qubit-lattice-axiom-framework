# R17-6 s2: (i) shift action == natural action conjugated by the on-site flip
# U_stag (flip every slot whose staggered sign exp(i pi sum pos) is -1), for all
# 24 rotations about a site and all N0914 slots in a 4^3 window; translations
# pick up a global flip. (ii) Goldstone-route partner count: minimum number of
# Goldstone branches whose generator rep W (any O-rep up to dim 12) supports two
# branches with helicity-2 characters on a C4 axis and a C2' face diagonal,
# with type-A/type-B (Watanabe-Murayama) assignments.
import itertools, numpy as np
G = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[perm[i], i] = signs[i]
        if round(np.linalg.det(M)) == 1: G.append(M)
# slots: doubled coordinates; diag (i,i) at 2x, face (i,j) at 2x+e_i+e_j
def stag(P2):  # P2 = doubled position (ints); stag = (-1)^{sum(P2)/2} for integer sum/2... use exp(i pi sum pos)
    s = sum(P2)  # sum of doubled coords; pos sum = s/2 ; diag: s even ; face: s even too (two half-integers)
    assert s % 2 == 0
    return 1 if (s // 2) % 2 == 0 else -1
bad = 0; tot = 0
for x in itertools.product(range(-2, 2), repeat=3):
    for (i, j) in [(0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (0, 2)]:
        P2 = 2 * np.array(x) + (np.eye(3, dtype=int)[i] + np.eye(3, dtype=int)[j] if i != j else 0)
        for M in G:
            gi = int(np.nonzero(M[:, i])[0][0]); gj = int(np.nonzero(M[:, j])[0][0])
            tens_sign = int(M[gi, i] * M[gj, j]) if i != j else 1
            stag_change = stag(M @ P2) * stag(P2)
            tot += 1; bad += (tens_sign != stag_change)
        # translation by e_x: stag always flips
        assert stag(P2 + np.array([2, 0, 0])) == -stag(P2)
print(f'(i) shift-sign == staggered-sign change: {tot - bad}/{tot} slot-rotation pairs agree; unit translations flip stag on every slot')
# Gauss row weight parity (global flip preserves zero syndrome iff every row has even weight)
print('    vector Gauss row weight (N0914:95-97): 2 diagonal + 4 face = 6 (even) -> global flip F_all preserves the mod-2 sector')
# (ii) Goldstone enumeration
IRR = {'A1': (1, 0, 1), 'A2': (1, 1, 0), 'E': (2, 1, 1), 'T1': (3, 0, 1), 'T2': (3, 1, 2)}  # (dim, mult C4=-1, mult C2'=+1)
names = list(IRR)
best = None; examples = []
for nA in itertools.product(range(0, 5), repeat=5):
    for nB in itertools.product(range(0, 5, 2), repeat=5):   # type-B part needs even multiplicity (real irreps)
        dA = sum(n * IRR[r][0] for n, r in zip(nA, names)); dB = sum(n * IRR[r][0] for n, r in zip(nB, names))
        if dA + dB == 0 or dA + dB > 12: continue
        aA = sum(n * IRR[r][1] for n, r in zip(nA, names)); bA = sum(n * IRR[r][2] for n, r in zip(nA, names))
        aB = sum(n * IRR[r][1] for n, r in zip(nB, names)); bB = sum(n * IRR[r][2] for n, r in zip(nB, names))
        # modes along C4 axis with eigenvalue -1: aA + aB/2 ; along C2' with +1: bA + bB/2
        if aA + aB // 2 >= 2 and bA + bB // 2 >= 2:
            Nmodes = dA + dB // 2
            if best is None or Nmodes < best:
                best = Nmodes; examples = []
            if Nmodes == best and len(examples) < 8:
                examples.append(({r: n for r, n in zip(names, nA) if n}, {r: n for r, n in zip(names, nB) if n}))
print(f'(ii) minimum Goldstone branch count with two helicity-2 branches (C4 axis and C2\' diagonal): {best}')
for e in examples: print('     type-A part', e[0], ' type-B part', e[1])
