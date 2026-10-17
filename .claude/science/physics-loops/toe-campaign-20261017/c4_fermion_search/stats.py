"""Levin-Wen T-junction exchange sign for a point charge of a translation-invariant Pauli stabilizer rule.

gens: list of dicts {star position: tuple of q labels}. charge: index j of the generator type whose
single violation is the charge. Legs: operators T_a with syndrome exactly {gen j at 0, gen j at t_a},
found by GF(2) least-support solving inside a box. Statistic = product of pairwise commutation signs.
"""
import itertools, numpy as np
STAR = [(0,0,0),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
SYM = {0:(0,0),1:(1,0),2:(1,1),3:(0,1)}
def build(gens, q, R):
    sites = [p for p in itertools.product(range(-R, R+1), repeat=3)]
    sidx = {p:i for i,p in enumerate(sites)}
    nq = q*len(sites)
    # generator instances fully inside the box
    inst = []
    for v in sites:
        for j,g in enumerate(gens):
            ok = all(tuple(np.add(v,p)) in sidx for p in g)
            if ok: inst.append((v,j))
    # syndrome matrix: rows = generator instances, cols = Pauli basis (x then z per qubit)
    M = np.zeros((len(inst), 2*nq), np.uint8)
    for r,(v,j) in enumerate(inst):
        for p,labs in gens[j].items():
            s = sidx[tuple(np.add(v,p))]
            for a,l in enumerate(labs):
                xb,zb = SYM[l]
                # symplectic: Pauli basis element X_{s,a} anticommutes with generator iff generator has z there
                if zb: M[r, q*s+a] ^= 1
                if xb: M[r, nq+q*s+a] ^= 1
    return sites, sidx, inst, M, nq
def solve(M, target):
    """Find w with M w = target over GF(2) (Gaussian elimination); None if unsolvable."""
    A = np.concatenate([M, target[:,None]], axis=1).astype(np.uint8)
    m, n = M.shape; piv = []; r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i,c]), None)
        if p is None: continue
        A[[r,p]] = A[[p,r]]
        rows = np.nonzero(A[:,c])[0]; rows = rows[rows != r]
        A[rows] ^= A[r]
        piv.append(c); r += 1
        if r == m: break
    if any(A[i,-1] and not A[i,:-1].any() for i in range(m)): return None
    w = np.zeros(n, np.uint8)
    for i,c in enumerate(piv): w[c] = A[i,-1]
    return w
def symp(w1, w2, nq):
    return int((w1[:nq] @ w2[nq:] + w1[nq:] @ w2[:nq]) % 2)
def t_junction(gens, q, j, legs, R=4):
    """j: generator index, or a list of (offset, generator index) forming a composite charge."""
    pattern = [((0,0,0), j)] if isinstance(j, int) else j
    sites, sidx, inst, M, nq = build(gens, q, R)
    iidx = {x:i for i,x in enumerate(inst)}
    T = []
    for t in legs:
        tgt = np.zeros(len(inst), np.uint8)
        for off, jj in pattern:
            tgt[iidx[(tuple(off), jj)]] ^= 1; tgt[iidx[(tuple(np.add(off, t)), jj)]] ^= 1
        w = solve(M, tgt)
        if w is None: return None, f'no leg operator to {t} in box R={R}'
        T.append(w)
    signs = [symp(T[a], T[b], nq) for a,b in ((0,1),(1,2),(0,2))]
    return (-1) ** sum(signs), signs
