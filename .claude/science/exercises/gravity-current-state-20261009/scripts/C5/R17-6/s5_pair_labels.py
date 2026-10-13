# R17-6 s5: Gamma-point O-content of two-slot composite labels n_s*n_t (natural,
# pure-permutation action) for N0914's slot placement, by orbit of slot pairs
# modulo translations. Shows whether composite few-site labels carry T2 at k = 0.
import itertools, numpy as np
G = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[perm[i], i] = signs[i]
        if round(np.linalg.det(M)) == 1: G.append(M)
def cls(M):
    tr = np.trace(M)
    return {3: 'E', 0: 'C3', 1: 'C4'}.get(tr, 'C2' if np.count_nonzero(M - np.diag(np.diag(M))) == 0 else "C2'")
CL = ['E', 'C3', 'C2', 'C4', "C2'"]
IRR = {'A1': [1, 1, 1, 1, 1], 'A2': [1, 1, 1, -1, -1], 'E': [2, -1, 2, 0, 0], 'T1': [3, 0, -1, 1, -1], 'T2': [3, 0, -1, -1, 1]}
# slots in doubled coords: diag type at 2x, face (i,j) at 2x+e_i+e_j ; label type = position class
def slot_list(R):
    out = []
    for x in itertools.product(range(-R, R + 1), repeat=3):
        X = 2 * np.array(x)
        for i in range(3): out.append(('d', i, tuple(X)))
        for i, j in [(0, 1), (1, 2), (0, 2)]:
            e = np.zeros(3, int); e[i] = 1; e[j] = 1; out.append(('f', (i, j), tuple(X + e)))
    return out
def act(M, s):
    kind, t, P = s; P2 = tuple(M @ np.array(P))
    if kind == 'd':
        return ('d', int(np.nonzero(M[:, t])[0][0]), P2)
    i, j = t; gi = int(np.nonzero(M[:, i])[0][0]); gj = int(np.nonzero(M[:, j])[0][0])
    return ('f', tuple(sorted((gi, gj))), P2)
def canon_pair(a, b):
    # translate so that the pair is canonical: subtract 2*floor(min position / 2)
    pa, pb = np.array(a[2]), np.array(b[2])
    shift = 2 * (np.minimum(pa, pb) // 2)  # even shift keeps slot types
    # canonical: sort the two translated slots, then choose min over translations that keep both in a fixed window
    cands = []
    for s in [pa, pb]:
        sh = 2 * (s // 2)
        A = (a[0], a[1], tuple(pa - sh)); B = (b[0], b[1], tuple(pb - sh))
        cands.append(tuple(sorted([A, B], key=str)))
    return min(cands, key=str)
slots = slot_list(1)
# nearest pairs: distance (in doubled coords) squared <= 2*... take |dP|^2 <= 4 (i.e. distance <= 1)
pairs = set()
base = [s for s in slots if all(0 <= c <= 1 for c in s[2])]  # slots in the home cell
for a in base:
    for b in slots:
        if a == b: continue
        d2 = sum((np.array(a[2]) - np.array(b[2])) ** 2)
        if d2 <= 4: pairs.add(canon_pair(a, b))
pairs = sorted(pairs, key=str)
# orbits under O (mod translation)
remaining = set(pairs); orbits = []
while remaining:
    p = next(iter(remaining)); orb = set()
    for M in G:
        q = canon_pair(act(M, p[0]), act(M, p[1])); orb.add(q)
    orbits.append(sorted(orb, key=str)); remaining -= orb
print(f'{len(pairs)} nearest slot pairs (|d| <= 1) mod translations in {len(orbits)} O-orbits')
for orb in orbits:
    chis = []
    for M in G:
        chis.append(sum(1 for p in orb if canon_pair(act(M, p[0]), act(M, p[1])) == p))
    dec = {}
    for nm, ch in IRR.items():
        s = sum(ch[CL.index(cls(M))] * chis[i] for i, M in enumerate(G)) / 24
        if round(s): dec[nm] = int(round(s))
    a, b = orb[0]
    d = np.array(b[2]) - np.array(a[2])
    print(f'  orbit size {len(orb):2d}  example {a[0]}{a[1]}@{a[2]} -- {b[0]}{b[1]}@{b[2]} (2d={tuple(d)})  Gamma content {dec}')
