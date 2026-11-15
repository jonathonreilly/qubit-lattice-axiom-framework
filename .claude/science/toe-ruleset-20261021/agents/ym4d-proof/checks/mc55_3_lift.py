# mc55_3 -- exact SU(2) test of MINCB55 Lemma LIFT_j's counting (d = 3, L = 3).
# Criteria: checks/mc55_3_criteria.md (written before this script). Exact rationals; one sqrt via rigorous integer enclosure.
from fractions import Fraction as F
from itertools import permutations, product
from math import isqrt
import random

d, L, S = 3, 3, 6                      # dimension, block side, fine torus side (2 blocks per direction)
nL = (2*d*(L-1) + L + 1) * ((2*L - 1) + (d - 1)*(L - 1))   # = 144
assert nL == 144

def qmul(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return (a1*a2 - b1*b2 - c1*c2 - d1*d2, a1*b2 + b1*a2 + c1*d2 - d1*c2,
            a1*c2 - b1*d2 + c1*a2 + d1*b2, a1*d2 + b1*c2 - c1*b2 + d1*a2)
def qinv(q):  # unit quaternion
    return (q[0], -q[1], -q[2], -q[3])
ONE = (F(1), F(0), F(0), F(0))
def stereo(v):
    n2 = sum(F(x)**2 for x in v)
    return ((1 - n2) / (1 + n2),) + tuple(2*F(x) / (1 + n2) for x in v)
def dist2(p, q):  # |p - q|^2
    return sum((x - y)**2 for x, y in zip(p, q))
def is_unit(q): return sum(x*x for x in q) == 1

def add(x, mu, s=1):
    y = list(x); y[mu] = (y[mu] + s) % S; return tuple(y)
sites = list(product(range(S), repeat=d))

def build(kind, seed):
    rnd = random.Random(seed)
    U = {}
    if kind == 'random':
        for x in sites:
            for mu in range(d):
                v = [F(rnd.choice((-1, 0, 1)), 10**5) for _ in range(3)]
                U[(x, mu)] = stereo(v)
    else:  # aligned: U_1(x) = q^{f(x_2)}, other links 1; f = 0,1,2,3,2,1 -> (1,2)-plaquettes q^{+-1}
        q = stereo([F(1, 10**5), F(0), F(0)])
        f = [0, 1, 2, 3, 2, 1]
        def qp(n):
            r = ONE
            for _ in range(abs(n)): r = qmul(r, q if n > 0 else qinv(q))
            return r
        for x in sites:
            for mu in range(d):
                U[(x, mu)] = qp(-f[x[1]]) if mu == 0 else ONE
    g = {x: stereo([F(rnd.randint(-3, 3), 2) for _ in range(3)]) for x in sites}
    Ug = {}
    for (x, mu), u in U.items():
        Ug[(x, mu)] = qmul(qmul(g[x], u), qinv(g[add(x, mu)]))
    for u in Ug.values(): assert is_unit(u)
    return Ug

def step(U, x, mu, s):
    # transport along one step from x in direction s*e_mu; returns (quaternion, new site)
    if s == 1: return U[(x, mu)], add(x, mu)
    y = add(x, mu, -1); return qinv(U[(y, mu)]), y
def transport(U, x, moves):
    T = ONE
    for (mu, s) in moves:
        u, x = step(U, x, mu, s); T = qmul(T, u)
    return T, x
def axial_moves(c, z, order):
    mv = []
    for mu in order:
        dz = (z[mu] - c[mu]) % S
        if dz > S // 2: dz -= S
        mv += [(mu, 1 if dz > 0 else -1)] * abs(dz)
    return mv
def root(x): return tuple(3*(xi // 3) + 1 for xi in x)
def plaquettes(U):
    out = []
    for x in sites:
        for mu in range(d):
            for nu in range(mu + 1, d):
                T, _ = transport(U, x, [(mu, 1), (nu, 1), (mu, -1), (nu, -1)])
                out.append(T)
    return out

def sqrt_enclose(x):  # rigorous rational enclosure of sqrt(x), x = p/q >= 0
    p, q = x.numerator, x.denominator; Sc = 10**30
    r = isqrt(p * q * Sc * Sc)
    return F(r, Sc * q), F(r + 1, Sc * q)

def run(kind, seed):
    U = build(kind, seed)
    eps2 = max(dist2(T, ONE) for T in plaquettes(U))
    order0 = tuple(range(d))
    h = {}
    for z in sites:
        c = root(z); T, end = transport(U, c, axial_moves(c, z, order0)); assert end == z; h[z] = T
    L1 = all(h[c] == ONE for c in set(root(z) for z in sites))
    L2 = True; maxr = 0; C1_fail = False
    for x in sites:
        for mu in range(d):
            y = add(x, mu); c = root(x)
            if root(y) != c: continue
            r = sum(abs(x[nu] - c[nu]) for nu in range(mu + 1, d)); maxr = max(maxr, r)
            uh = qmul(qmul(h[x], U[(x, mu)]), qinv(h[y]))
            if r == 0:
                L1 = L1 and (uh == ONE)
            else:
                lhs = dist2(uh, ONE)
                if not (lhs <= r * r * eps2): L2 = False
                if lhs > max(r - 1, 0)**2 * eps2: C1_fail = True
    L2 = L2 and maxr <= (d - 1) * (L - 1) // 2
    L3 = True; L4 = True; C2_fail = False
    rhs4 = (F(17, 10) * F(14142, 10000) * nL)**2 * eps2
    regime = (F(104, 100) * F(14143, 10000) * nL)**2 * eps2 <= F(1, 400)
    for X in product(range(2), repeat=d):
        cX = tuple(3*Xi + 1 for Xi in X)
        for mu in range(d):
            cY = add(cX, mu, 3)
            conts = []
            for sigma in permutations(range(d)):
                for yp in product(*[range(cX[i] - 1, cX[i] + 2) for i in range(d)]):
                    T1, e1 = transport(U, cX, axial_moves(cX, yp, sigma)); assert e1 == yp
                    T2, e2 = transport(U, yp, [(mu, 1)] * L)
                    T3, e3 = transport(U, cY, axial_moves(cY, e2, sigma)); assert e3 == e2
                    conts.append(qmul(qmul(T1, T2), qinv(T3)))
            M = tuple(sum(t[i] for t in conts) / len(conts) for i in range(4))
            nM2 = sum(m * m for m in M); mlo, mhi = sqrt_enclose(nM2)
            # face links: x in B(X) with x_mu = cX_mu + 1, y = x + e_mu in B(X + e_mu)
            for x in product(*[[cX[i] + 1] if i == mu else range(cX[i] - 1, cX[i] + 2) for i in range(d)]):
                x = tuple(xi % S for xi in x); y = add(x, mu)
                assert root(x) == cX and root(y) == cY
                Tb = qmul(qmul(h[x], U[(x, mu)]), qinv(h[y]))
                for Tc in conts:
                    dd = dist2(Tb, Tc)
                    if not (dd <= nL * nL * eps2): L3 = False
                    if dd > eps2: C2_fail = True
                inner = sum(a * b for a, b in zip(M, Tb))
                assert inner > 0
                lhs4_upper = 2 - 2 * inner / mhi
                if not (lhs4_upper <= rhs4): L4 = False
    L4 = L4 and regime
    return dict(eps=float(F(sqrt_enclose(eps2)[1])), L1=L1, L2=L2, L3=L3, L4=L4, C1_fail=C1_fail, C2_fail=C2_fail)

results = []
for kind, seed in [('random', 1), ('random', 2), ('random', 3), ('random', 4), ('aligned', 5)]:
    r = run(kind, seed); results.append((kind, seed, r))
    print(f"{kind} seed={seed}: eps'~{r['eps']:.3e}  L1={r['L1']} L2={r['L2']} L3={r['L3']} L4={r['L4']}  "
          f"C1(undersized ladder) {'FAILS' if r['C1_fail'] else 'holds'}  C2(n_L->1) {'FAILS' if r['C2_fail'] else 'holds'}")
gates = all(r['L1'] and r['L2'] and r['L3'] and r['L4'] for _, _, r in results)
al = results[-1][2]
controls = al['C1_fail'] and al['C2_fail']
print(f"gates L1-L4 on all instances: {'hold' if gates else 'DO NOT all hold'}; controls on the aligned instance: {'both fired' if controls else 'NOT both fired'}")
print(f"VERDICT mc55_3: {'PASS' if (gates and controls) else 'FAIL'}")
