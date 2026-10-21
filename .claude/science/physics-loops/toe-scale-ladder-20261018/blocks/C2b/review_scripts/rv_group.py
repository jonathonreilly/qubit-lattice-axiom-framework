#!/usr/bin/env python3
"""Reviewer check of C2b claim (1), independent of scripts/kip_group_theory.py.
Method differs: (a) subgroups H with O <= H <= B4 are enumerated as unions of right cosets O g
(B4 has 16 of them): all 2^15 subsets containing the identity coset are tested for closure;
(b) invariant counts by explicit null spaces (SVD) of (rho(g) - 1) over generators/all elements,
not characters; (c) F^2 / F Ftilde identification by explicit tensors in F-index space."""
import itertools, sys
import numpy as np
P = F = 0
def chk(n, ok):
    global P, F
    P += bool(ok); F += (not ok); print(('PASS ' if ok else 'FAIL ') + n, flush=True)
# B4 as 4x4 signed permutation matrices, axis 0 = tick
els = []
for p in itertools.permutations(range(4)):
    for s in itertools.product((1, -1), repeat=4):
        M = np.zeros((4, 4), int)
        for i in range(4): M[i, p[i]] = s[i]
        els.append(M)
K = {M.tobytes(): i for i, M in enumerate(els)}
n = len(els); chk('|B4| = 384', n == 384)
Oset = [i for i, M in enumerate(els) if M[0, 0] == 1 and round(np.linalg.det(M)) == 1]
chk('|O| = 24', len(Oset) == 24)
mul = lambda i, j: K[(els[i] @ els[j]).tobytes()]
# right cosets O g
cos = []; seen = set()
for g in range(n):
    if g in seen: continue
    c = frozenset(mul(o, g) for o in Oset); cos.append(c); seen |= c
chk('16 cosets', len(cos) == 16)
e = K[np.eye(4, dtype=int).tobytes()]
i0 = [i for i, c in enumerate(cos) if e in c][0]
others = [i for i in range(16) if i != i0]
subs = []
for mask in range(1 << 15):
    H = set(cos[i0])
    for b, i in enumerate(others):
        if mask >> b & 1: H |= cos[i]
    # closure test (finite => subgroup)
    Hl = list(H); ok = True
    for a in Hl:
        for b in Hl:
            if mul(a, b) not in H: ok = False; break
        if not ok: break
    if ok: subs.append(frozenset(H))
print('orders:', sorted(len(H) for H in subs))
chk('exactly 7 subgroups contain O', len(subs) == 7)
pairs = list(itertools.combinations(range(4), 2))
def inv_dim(mats, dim):
    A = np.vstack([Mt - np.eye(dim) for Mt in mats])
    s = np.linalg.svd(A, compute_uv=False)
    return int(np.sum(s < 1e-9)), A
def sym_rep(M):   # action on symmetric T: T -> M T M^T, as matrix on 10-dim basis
    B = [(i, j) for i in range(4) for j in range(i, 4)]
    R = np.zeros((10, 10))
    for c, (i, j) in enumerate(B):
        E = np.zeros((4, 4)); E[i, j] = E[j, i] = 1
        T = M @ E @ M.T
        R[:, c] = [T[a, b] for (a, b) in B]
    return R
def anti_rep(M):
    R = np.zeros((6, 6))
    for c, (i, j) in enumerate(pairs):
        E = np.zeros((4, 4)); E[i, j] = 1; E[j, i] = -1
        T = M @ E @ M.T
        R[:, c] = [T[a, b] for (a, b) in pairs]
    return R
def quadF_rep(M):  # quadratic forms on F (6-dim): Q -> L^T Q L, L = anti_rep(M)^{-1}... invariance only matters
    L = anti_rep(M); B = [(a, b) for a in range(6) for b in range(a, 6)]
    R = np.zeros((21, 21))
    for c, (a, b) in enumerate(B):
        E = np.zeros((6, 6)); E[a, b] = E[b, a] = 1
        T = L.T @ E @ L
        R[:, c] = [T[x, y] for (x, y) in B]
    return R
# explicit F^2 and F Ftilde as quadratic forms on F_{ij}, i<j
F2 = np.eye(6)
FFt = np.zeros((6, 6))
for a, (i, j) in enumerate(pairs):
    for b, (k, l) in enumerate(pairs):
        if len({i, j, k, l}) == 4:
            FFt[a, b] = round(np.linalg.det(np.eye(4)[[i, j, k, l]]))
vec = lambda Q: np.array([Q[a, b] for a in range(6) for b in range(a, 6)])
rows = []
for H in sorted(subs, key=len):
    Ms = [els[g] for g in H]
    nS, _ = inv_dim([sym_rep(M) for M in Ms], 10)
    nA, _ = inv_dim([anti_rep(M) for M in Ms], 6)
    nF, A = inv_dim([quadF_rep(M) for M in Ms], 21)
    proper = all(round(np.linalg.det(M)) == 1 for M in Ms)
    mix = any(M[0, 0] == 0 for M in Ms)
    pureT = any((M == np.diag([-1, 1, 1, 1])).all() for M in Ms)
    tflip = any(M[0, 0] == -1 for M in Ms)
    f2inv = np.allclose(A @ vec(F2), 0); fftinv = np.allclose(A @ vec(FFt), 0)
    # isotropic delta in invariant symmetric space?
    suff = nS == 1 and nA == 0 and (nF == 1 or (nF == 2 and fftinv and f2inv))
    rows.append((len(H), proper, mix, nS, nA, nF, suff, H, pureT, tflip))
    print(f'|H|={len(H):3d} proper={proper} mixes_t={mix} has_T=diag(-1,1,1,1):{pureT} some t->-t:{tflip} '
          f'nS={nS} nA={nA} nF={nF} F2inv={f2inv} FFt_inv={fftinv} sufficient={suff}')
suff = [r for r in rows if r[6]]
chk('sufficient groups are exactly orders 192 and 384', sorted(r[0] for r in suff) == [192, 384])
g192 = [r for r in suff if r[0] == 192][0]
chk('order-192 group = det(+1) subgroup of B4 (proper hypercubic B4+)',
    g192[7] == frozenset(i for i, M in enumerate(els) if round(np.linalg.det(M)) == 1))
R = np.eye(4, dtype=int); R[0, 0] = R[1, 1] = 0; R[1, 0] = 1; R[0, 1] = -1   # t -> x -> -t
# generated group <O, R>
G = set(Oset); fr = list(G)
while fr:
    new = []
    for a in fr:
        for b in Oset + [K[R.tobytes()]]:
            c = mul(a, b)
            if c not in G: G.add(c); new.append(c)
    fr = new
chk('<O, R_tx> = B4+ (order 192)', frozenset(G) == g192[7])
chk('B4+ contains no pure time reflection diag(-1,1,1,1)', not g192[8])
chk('B4+ does contain t -> -t combined with a spatial flip (R_tx^2 = diag(-1,-1,1,1))', g192[9]
    and (R @ R == np.diag([-1, -1, 1, 1])).all())
chk('under B4+: F^2 and F Ftilde are the 2 invariants; nS=1, nA=0', g192[3:6] == (1, 0, 2))
chk('no proper group of order < 192 has nS = 1', all(r[3] == 2 for r in rows if r[0] < 192))
print(f'TOTAL: PASS={P} FAIL={F}')
sys.exit(1 if F else 0)
