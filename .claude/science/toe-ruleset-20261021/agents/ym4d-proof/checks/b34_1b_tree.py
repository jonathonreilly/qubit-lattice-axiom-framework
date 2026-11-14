# b34_1b — corrected re-run of b34_1 (multilin multiplicity fix); exact check of the implicit-function / envelope derivative tree formulas (BFT34_55 §1.4).
# Criteria: checks/b34_1_criteria.md (written before this script). Plain python, fractions only.
import itertools, random, sys
from fractions import Fraction as Fr
from math import factorial

p, q = 2, 2           # dim Z, dim V
NV = p + q            # variables x = (Z_0..Z_{p-1}, V_0..V_{q-1})

# ---------- truncated polynomial arithmetic (dict: exponent tuple -> Fraction) ----------
def padd(a, b):
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, 0) + v
        if r[k] == 0: del r[k]
    return r
def pscale(a, c):
    return {k: v * c for k, v in a.items() if v * c != 0}
def pmul(a, b, D):
    r = {}
    for ka, va in a.items():
        da = sum(ka)
        for kb, vb in b.items():
            if da + sum(kb) > D: continue
            k = tuple(x + y for x, y in zip(ka, kb))
            r[k] = r.get(k, 0) + va * vb
    return {k: v for k, v in r.items() if v != 0}
def ppow(a, e, D):
    r = {tuple([0] * NV): Fr(1)}
    for _ in range(e): r = pmul(r, a, D)
    return r
def var(i):
    k = [0] * NV; k[i] = 1
    return {tuple(k): Fr(1)}
def compose(poly, Zs, D):
    """substitute Z_i -> Zs[i] (polys in V only) into poly(Z, V); result truncated at degree D"""
    out = {}
    cache = {}
    for k, c in poly.items():
        term = {tuple([0] * NV): Fr(c)}
        for i in range(p):
            if k[i]:
                key = (i, k[i])
                if key not in cache: cache[key] = ppow(Zs[i], k[i], D)
                term = pmul(term, cache[key], D)
        vk = tuple([0] * p + list(k[p:]))
        term = pmul(term, {vk: Fr(1)}, D)
        out = padd(out, term)
    return out

def mat_inv(M):
    n = len(M); A = [[Fr(x) for x in row] + [Fr(int(i == j)) for j in range(n)] for i, row in enumerate(M)]
    for c in range(n):
        piv = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[piv] = A[piv], A[c]
        pv = A[c][c]; A[c] = [x / pv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]; A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [row[n:] for row in A]

# ---------- multilinear derivative D^r f(0)[u_1..u_r] = coeff of t_1..t_r in f(sum t_i u_i) ----------
def multilin(f, us):
    r = len(us); tot = Fr(0)
    for k, c in f.items():
        if sum(k) != r: continue
        # sum over maps sigma: [r] -> variables with counts == k
        slots = []
        for v in range(NV): slots += [v] * k[v]
        # every bijection (factor copy -> direction) counts; no de-duplication (fix of b34_1's defect:
        # de-duplicating dropped the multiplicity prod_k gamma_k!)
        for perm in itertools.permutations(range(r)):
            assign = tuple(slots[perm[i]] for i in range(r))
            prod = Fr(1)
            for i in range(r):
                prod *= us[i][assign[i]]
                if prod == 0: break
            tot += c * prod
    return tot

def set_partitions(lst):
    if not lst:
        yield []
        return
    first, rest = lst[0], lst[1:]
    for part in set_partitions(rest):
        yield [[first]] + part
        for i in range(len(part)):
            yield part[:i] + [[first] + part[i]] + part[i + 1:]

def pairs(S, exclude_trivial):
    S = list(S)
    for w in range(len(S) + 1):
        for W in itertools.combinations(S, w):
            rest = [s for s in S if s not in W]
            for P in set_partitions(rest):
                if exclude_trivial and len(W) == 0 and len(P) == 1: continue
                yield P, list(W)

def zdir(z):  return [Fr(x) for x in z] + [Fr(0)] * q
def vdir(a):  return [Fr(0)] * p + [Fr(int(j == a)) for j in range(q)]

def make_tree(G, Ginv, idx, mode=None):
    memo = {}
    def Zd(S, root):
        key = (tuple(S), root)
        if key in memo: return memo[key]
        acc = [Fr(0)] * p
        for P, W in pairs(S, True):
            if root and mode == 'K1' and len(P) >= 2: continue
            if root and mode == 'K3' and len(P) >= 1 and len(W) >= 1: continue
            mult = factorial(len(P)) if (root and mode == 'K2') else 1
            us = [zdir(Zd(B, False)) for B in P] + [vdir(idx[i]) for i in W]
            for j in range(p):
                acc[j] += mult * multilin(G[j], us)
        res = [sum(Ginv[j][l] * acc[l] for l in range(p)) for j in range(p)]
        memo[key] = res
        return res
    return Zd

def deriv_coeff(poly, idx):
    beta = [0] * q
    for a in idx: beta[a] += 1
    k = tuple([0] * p + beta)
    c = poly.get(k, Fr(0))
    m = 1
    for b in beta: m *= factorial(b)
    return c * m

def solve_Z(G, A, D):
    Ainv = mat_inv(A)
    H = []
    for j in range(p):
        hj = {k: v for k, v in G[j].items() if sum(k) >= 2}
        H.append(hj)
    BV = []
    for j in range(p):
        BV.append({k: v for k, v in G[j].items() if sum(k) == 1 and any(k[p:])})
    Z = [dict() for _ in range(p)]
    for it in range(D + 3):
        rhs = [padd(BV[j], compose(H[j], Z, D)) for j in range(p)]
        newZ = []
        for i in range(p):
            acc = {}
            for j in range(p):
                acc = padd(acc, pscale(rhs[j], -Ainv[i][j]))
            newZ.append(acc)
        if newZ == Z: break
        Z = newZ
    return Z

def rnd_poly(rng, degs, lo, hi):
    f = {}
    for k in itertools.product(range(6), repeat=NV):
        if sum(k) in degs:
            c = rng.randint(lo, hi)
            if c: f[k] = Fr(c)
    return f

def grad_Z(F):
    G = []
    for j in range(p):
        g = {}
        for k, c in F.items():
            if k[j] > 0:
                kk = list(k); kk[j] -= 1
                g[tuple(kk)] = g.get(tuple(kk), 0) + c * k[j]
        G.append({k: v for k, v in g.items() if v != 0})
    return G
def dF_dV(F, a):
    g = {}
    for k, c in F.items():
        if k[p + a] > 0:
            kk = list(k); kk[p + a] -= 1
            g[tuple(kk)] = g.get(tuple(kk), 0) + c * k[p + a]
    return {k: v for k, v in g.items() if v != 0}

def bell(n):
    return sum(1 for _ in set_partitions(list(range(n))))

out = []
def log(s): out.append(s); print(s)

ok_P1 = ok_P2 = True
fire = {'K1': False, 'K2': False, 'K3': False, 'K4': False}
for seed in (11, 23, 37):
    rng = random.Random(seed)
    # ---- U-part ----
    while True:
        A = [[rng.randint(-3, 3) for _ in range(p)] for _ in range(p)]
        if A[0][0] * A[1][1] - A[0][1] * A[1][0] != 0: break
    B = [[rng.randint(-3, 3) for _ in range(q)] for _ in range(p)]
    G = []
    for j in range(p):
        g = rnd_poly(rng, {2, 3, 4}, -3, 3)
        for i in range(p):
            k = [0] * NV; k[i] = 1
            if A[j][i]: g[tuple(k)] = Fr(A[j][i])
        for a in range(q):
            k = [0] * NV; k[p + a] = 1
            if B[j][a]: g[tuple(k)] = Fr(B[j][a])
        G.append(g)
    Ainv = mat_inv(A)
    Gm = [[-x for x in row] for row in Ainv]
    Z = solve_Z(G, A, 4)
    nU = 0; badU = 0
    for n in range(1, 5):
        for idx in itertools.product(range(q), repeat=n):
            truth = [deriv_coeff(Z[j], idx) for j in range(p)]
            tree = make_tree(G, Gm, idx)(list(range(n)), True)
            nU += 1
            if tree != truth: badU += 1
            for K in ('K1', 'K2', 'K3'):
                if not fire[K]:
                    alt = make_tree(G, Gm, idx, K)(list(range(n)), True)
                    if alt != truth: fire[K] = True
    log(f"seed {seed}: U-part {nU} derivative vectors compared, mismatches {badU}")
    ok_P1 &= (badU == 0)
    # ---- E-part ----
    while True:
        a11, a12, a22 = rng.randint(-3, 3), rng.randint(-3, 3), rng.randint(-3, 3)
        if a11 * a22 - a12 * a12 != 0: break
    As = [[a11, a12], [a12, a22]]
    F = rnd_poly(rng, {3, 4, 5}, -2, 2)
    # quadratic part 1/2 Z^T As Z + Z^T B V
    def addm(k, c):
        if c: F[k] = F.get(k, 0) + Fr(c)
    addm((2, 0, 0, 0), Fr(a11, 2)); addm((0, 2, 0, 0), Fr(a22, 2)); addm((1, 1, 0, 0), a12)
    for i in range(p):
        for a in range(q):
            k = [0] * NV; k[i] = 1; k[p + a] = 1; addm(tuple(k), B[i][a])
    F = {k: v for k, v in F.items() if v != 0}
    GF = grad_Z(F)
    AsF = [[Fr(As[i][j]) for j in range(p)] for i in range(p)]
    ZF = solve_Z(GF, As, 5)
    E = compose(F, ZF, 5)
    GmF = [[-x for x in row] for row in mat_inv(As)]
    nE = 0; badE = 0
    for n in range(1, 6):
        for idx in itertools.product(range(q), repeat=n):
            truth = deriv_coeff(E, idx)
            Zd = make_tree(GF, GmF, idx)
            f1 = dF_dV(F, idx[0])
            def Etree(drop_rootW):
                tot = Fr(0)
                for P, W in pairs(list(range(1, n)), False):
                    if drop_rootW and len(W) > 0: continue
                    us = [zdir(Zd(Bk, False)) for Bk in P] + [vdir(idx[i]) for i in W]
                    if len(us) == 0:
                        tot += f1.get(tuple([0] * NV), Fr(0))
                    else:
                        tot += multilin(f1, us)
                return tot
            val = Etree(False)
            nE += 1
            if val != truth: badE += 1
            if not fire['K4'] and Etree(True) != truth: fire['K4'] = True
    log(f"seed {seed}: E-part {nE} derivatives compared, mismatches {badE}")
    ok_P2 &= (badE == 0)

cntU = [sum(1 for _ in pairs(list(range(n)), True)) for n in range(1, 5)]
cntE = [sum(1 for _ in pairs(list(range(n - 1)), False)) for n in range(1, 6)]
def Tfull(m, memo={}):
    if m in memo: return memo[m]
    tot = 0
    for P, W in pairs(list(range(m)), True):
        prod = 1
        for Bk in P: prod *= Tfull(len(Bk))
        tot += prod
    memo[m] = tot
    return tot
TU = [Tfull(n) for n in range(1, 5)]
log(f"(P,W) counts U: {cntU} (expected [1, 4, 14, 51]); Bell B(n+1)-1: {[bell(n+1)-1 for n in range(1,5)]}")
log(f"(P,W) counts E: {cntE} (expected [1, 2, 5, 15, 52]); Bell B(n): {[bell(n) for n in range(1,6)]}")
log(f"fully expanded tree counts T(n), n=1..4 (informational): {TU}")
ok_P3 = (cntU == [1, 4, 14, 51]) and (cntE == [1, 2, 5, 15, 52])
log(f"controls fired: {fire}")
log(f"P1 {'PASS' if ok_P1 else 'FAIL'}; P2 {'PASS' if ok_P2 else 'FAIL'}; P3 {'PASS' if ok_P3 else 'FAIL'}; "
    f"controls {'ALL FIRED' if all(fire.values()) else 'NOT ALL FIRED (non-decisive)'}")
log("OVERALL: " + ("PASS" if (ok_P1 and ok_P2 and ok_P3 and all(fire.values())) else "FAIL"))
