"""T3: minimum weight of a nontrivial logical operator of the Chamon rule
(X on +-x, Y on +-y, Z on +-z neighbours; identity at centre) on the L^3
torus, one sublattice (the code factorises by site parity for even L).
This weight is the lowest order at which a one-site perturbation can split
the code space.  Exact by meet-in-the-middle up to weight 2*WMAX.
usage: python3 t3_chamon_distance.py L WMAX
"""
import sys, itertools
import numpy as np

L = int(sys.argv[1]); WMAX = int(sys.argv[2])
sites = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
odd = [s for s in sites if sum(s) % 2 == 1]     # qubits of one copy
even = [s for s in sites if sum(s) % 2 == 0]    # stabilizer centres of that copy
qi = {s: i for i, s in enumerate(odd)}
n = len(odd); m = len(even)


def add(a, b):
    return tuple((a[i] + b[i]) % L for i in range(3))


# stabilizer symplectic rows over GF(2): length 2n (x-part, z-part)
rows = []
for r in even:
    v = np.zeros(2 * n, dtype=np.uint8)
    for d, lab in [((1, 0, 0), 'X'), ((-1, 0, 0), 'X'), ((0, 1, 0), 'Y'), ((0, -1, 0), 'Y'), ((0, 0, 1), 'Z'), ((0, 0, -1), 'Z')]:
        q = qi[add(r, d)]
        if lab in 'XY':
            v[q] ^= 1
        if lab in 'YZ':
            v[n + q] ^= 1
    rows.append(v)
Smat = np.array(rows)


def rref(M):
    M = M.copy() % 2
    piv = []
    r = 0
    for c in range(M.shape[1]):
        p = None
        for i in range(r, M.shape[0]):
            if M[i, c]:
                p = i; break
        if p is None:
            continue
        M[[r, p]] = M[[p, r]]
        for i in range(M.shape[0]):
            if i != r and M[i, c]:
                M[i] ^= M[r]
        piv.append(c); r += 1
        if r == M.shape[0]:
            break
    return M[:r], piv


SB, piv = rref(Smat)
rankS = len(piv)
k = n - rankS
print(f"L={L}: copy has n={n} qubits, {m} generators, rank {rankS}, logical qubits k={k} (both copies: {2*k})", flush=True)


def in_span(v):
    v = v.copy()
    for row, c in zip(SB, piv):
        if v[c]:
            v ^= row
    return not v.any()


# syndrome of single-site Paulis: bit j set if anticommutes with generator j
def symp(a, b):
    return (int(a[:n] @ b[n:]) + int(a[n:] @ b[:n])) % 2


single = {}
for q in range(n):
    for lab, (xb, zb) in {'X': (1, 0), 'Y': (1, 1), 'Z': (0, 1)}.items():
        v = np.zeros(2 * n, dtype=np.uint8); v[q] = xb; v[n + q] = zb
        syn = 0
        for j in range(m):
            if symp(v, Smat[j]):
                syn |= 1 << j
        single[(q, lab)] = (syn, v)

# enumerate all Paulis of weight <= WMAX with syndromes
from collections import defaultdict
table = defaultdict(list)
labs = ['X', 'Y', 'Z']
for w in range(1, WMAX + 1):
    for qs in itertools.combinations(range(n), w):
        for ls in itertools.product(labs, repeat=w):
            syn = 0
            for q, l in zip(qs, ls):
                syn ^= single[(q, l)][0]
            table[syn].append((qs, ls))
print(f"enumerated weight<= {WMAX}: {sum(len(v) for v in table.values())} Paulis", flush=True)


def vec(qs, ls):
    v = np.zeros(2 * n, dtype=np.uint8)
    for q, l in zip(qs, ls):
        v ^= single[(q, l)][1]
    return v


best = None
# weight <= WMAX with zero syndrome
for (qs, ls) in table.get(0, []):
    if not in_span(vec(qs, ls)):
        w = len(qs)
        if best is None or w < best[0]:
            best = (w, qs, ls)
# products of two with equal syndrome, total weight <= 2*WMAX
for syn, lst in table.items():
    if len(lst) < 2:
        continue
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            v = vec(*lst[i]) ^ vec(*lst[j])
            w = int(((v[:n] | v[n:]) > 0).sum())
            if w == 0 or (best is not None and w >= best[0]):
                continue
            if not in_span(v):
                best = (w, lst[i], lst[j])
if best is None:
    print(f"L={L}: no nontrivial logical of weight <= {2*WMAX}; d >= {2*WMAX+1}", flush=True)
else:
    print(f"L={L}: minimum-weight nontrivial logical found: weight {best[0]} (search complete up to {2*WMAX}) -> d = {best[0]}", flush=True)
    print("   witness:", best[1:], flush=True)
