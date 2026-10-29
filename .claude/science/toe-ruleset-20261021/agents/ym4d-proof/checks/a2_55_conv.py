# a2_55_conv.py -- exact checks for ALIGN2_55 Lemma CONV-P, Steps 1 and 3. Criteria: a2_55_conv_criteria.md (written first).
# Fractions/ints only. Prints to stdout only.
from fractions import Fraction as F
import random, itertools, sys

# ---------------- Part I: nilpotent Lie algebra (strictly upper-triangular 6x6) ----------------
NM = 6
def zero(): return [[F(0)]*NM for _ in range(NM)]
def eye():
    M = zero()
    for i in range(NM): M[i][i] = F(1)
    return M
def add(A, B): return [[A[i][j]+B[i][j] for j in range(NM)] for i in range(NM)]
def sub(A, B): return [[A[i][j]-B[i][j] for j in range(NM)] for i in range(NM)]
def scal(s, A): return [[s*A[i][j] for j in range(NM)] for i in range(NM)]
def mul(A, B):
    C = zero()
    for i in range(NM):
        for k in range(NM):
            if A[i][k] != 0:
                aik = A[i][k]
                for j in range(NM):
                    if B[k][j] != 0: C[i][j] += aik*B[k][j]
    return C
def eq(A, B): return all(A[i][j] == B[i][j] for i in range(NM) for j in range(NM))
def rand_su(rng):
    M = zero()
    for i in range(NM):
        for j in range(i+1, NM):
            M[i][j] = F(rng.randint(-9, 9), rng.randint(1, 7))
    return M
def expm(X):  # finite series (X nilpotent)
    R, P = eye(), eye()
    for n in range(1, 2*NM):
        P = scal(F(1, n), mul(P, X)); R = add(R, P)
    return R
# t-matrices: (M0, M1) = M0 + t*M1, truncated at degree 1
def tmul(A, B): return (mul(A[0], B[0]), add(mul(A[0], B[1]), mul(A[1], B[0])))
def tadd(A, B): return (add(A[0], B[0]), add(A[1], B[1]))
def tscal(s, A): return (scal(s, A[0]), scal(s, A[1]))
def K_direct(X, a, c):
    E = expm(X)
    M = tmul(tmul((eye(), a), (E, zero())), (eye(), scal(F(-1), c)))
    N = (sub(M[0], eye()), M[1])            # M = I + N, N nilpotent
    L, Pw = (zero(), zero()), (eye(), zero())
    for m in range(1, 2*NM):
        Pw = tmul(Pw, N)
        L = tadd(L, tscal(F((-1)**(m+1), m), Pw))
    return L[1]                              # coefficient of t in log M
def bernoulli(nmax):
    B = [F(0)]*(nmax+1); B[0] = F(1)
    from math import comb
    for m in range(1, nmax+1):
        B[m] = -sum(comb(m+1, k)*B[k] for k in range(m)) / (m+1)
    return B
BN = bernoulli(24)
from math import factorial
def ad(X, Y): return sub(mul(X, Y), mul(Y, X))
def series_ad(coefs, X, Y):  # sum_n coefs[n] ad_X^n Y
    R, T = zero(), Y
    for n, cf in enumerate(coefs):
        if n > 0: T = ad(X, T)
        if cf != 0: R = add(R, scal(cf, T))
    return R
NS = 14
psi_m = [BN[n]/factorial(n) for n in range(NS)]                 # z/(e^z-1)
psi_p = [((-1)**n)*BN[n]/factorial(n) for n in range(NS)]       # z/(1-e^{-z})
Phi   = [ (2*BN[n]/factorial(n) if (n % 2 == 0 and n >= 2) else F(0)) for n in range(NS)]  # z coth(z/2) - 2
res = {}
fires = {'CI1': False, 'CI2': False, 'CI3': False}
okI1 = okI2 = True
for seed in (11, 22, 33):
    rng = random.Random(seed)
    X, a, c = rand_su(rng), rand_su(rng), rand_su(rng)
    K = K_direct(X, a, c)
    rhs1 = sub(series_ad(psi_m, X, a), series_ad(psi_p, X, c))
    okI1 &= eq(K, rhs1)
    lbar = scal(F(1, 2), add(a, c)); dl = sub(c, a)
    lhs2 = sub(K, sub(a, c))
    rhs2 = sub(scal(F(-1), ad(X, lbar)), scal(F(1, 2), series_ad(Phi, X, dl)))
    okI2 &= eq(lhs2, rhs2)
    if not eq(K, sub(series_ad(psi_p, X, a), series_ad(psi_m, X, c))): fires['CI1'] = True
    if not eq(lhs2, scal(F(-1), ad(X, lbar))): fires['CI2'] = True
    if not eq(lhs2, sub(ad(X, lbar), scal(F(1, 2), series_ad(Phi, X, dl)))): fires['CI3'] = True
print("Part I: I1 (K == psi_-(ad X)a - psi_+(ad X)c) :", "PASS" if okI1 else "FAIL")
print("Part I: I2 (K' == -[X,lbar] - 1/2 Phi(ad X) dlam):", "PASS" if okI2 else "FAIL")
for k_, v in fires.items(): print("Part I control", k_, "FIRES" if v else "does NOT fire")

# ---------------- Part II: su(2) = (R^3, x), d = 4 torus of side 3 ----------------
d, S = 4, 3
def cross(u, v): return (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])
def dot(u, v): return u[0]*v[0]+u[1]*v[1]+u[2]*v[2]
def vadd(u, v): return (u[0]+v[0], u[1]+v[1], u[2]+v[2])
def vsc(s, u): return (s*u[0], s*u[1], s*u[2])
Z0 = (F(0), F(0), F(0))
sites = list(itertools.product(range(S), repeat=d))
def shift(z, mu, s=1):
    z = list(z); z[mu] = (z[mu]+s) % S; return tuple(z)
links = [(z, mu) for z in sites for mu in range(d)]
plaqs = [(z, mu, nu) for z in sites for mu in range(d) for nu in range(mu+1, d)]
def bnd(P):
    z, mu, nu = P
    return [((z, mu), 1), ((shift(z, mu), nu), 1), ((shift(z, nu), mu), -1), ((z, nu), -1)]
def rv(rng): return (F(rng.randint(-9, 9), rng.randint(1, 5)), F(rng.randint(-9, 9), rng.randint(1, 5)), F(rng.randint(-9, 9), rng.randint(1, 5)))
def buildW(G, y, coef_b1_own=F(1, 2), eps3_W=-1):
    W = {b: Z0 for b in links}; mass = {b: F(0) for b in links}
    for P in plaqs:
        (b1, e1), (b2, e2), (b3, e3), (b4, e4) = bnd(P)
        e3w = eps3_W
        gy = lambda b: cross(G[P], y[b])
        terms = [(b1, coef_b1_own, e1, b1), (b1, F(1), e2, b2), (b2, F(1, 2), e2, b2),
                 (b3, F(1, 2), e3w, b3), (b4, F(1), e3w, b3), (b4, F(1, 2), e4, b4)]
        for (target, cf, eps, src) in terms:
            W[target] = vadd(W[target], vsc(cf*eps, gy(src)))
            mass[target] += abs(cf)
    return W, mass
okII1 = True; okII2 = True
firesII = {'CII1': False, 'CII2': False, 'CII3': False}
for seed in (101, 202, 303):
    rng = random.Random(seed)
    G = {P: rv(rng) for P in plaqs}; y = {b: rv(rng) for b in links}; lam = {z: rv(rng) for z in sites}
    def lbar(b): z, mu = b; return vsc(F(1, 2), vadd(lam[z], lam[shift(z, mu)]))
    def dlam(b): z, mu = b; return vadd(lam[shift(z, mu)], vsc(F(-1), lam[z]))
    LHS = F(0)
    for P in plaqs:
        for (b, e) in bnd(P):
            LHS += e*dot(G[P], cross(y[b], lbar(b)))
    def RHS_of(W, with_W=True):
        R = F(0)
        for P in plaqs:
            dy = Z0
            for (b, e) in bnd(P): dy = vadd(dy, vsc(e, y[b]))
            R += dot(G[P], cross(dy, lam[P[0]]))
        if with_W:
            for b in links: R += dot(W[b], dlam(b))
        return R
    W, mass = buildW(G, y)
    okII1 &= (LHS == RHS_of(W))
    if seed == 101:
        okII2 &= all(mass[b] == 2*(d-1) for b in links)
        base_count = {z: 0 for z in sites}
        for P in plaqs: base_count[P[0]] += 1
        okII2 &= all(v == d*(d-1)//2 for v in base_count.values())
        print("Part II: max/min coefficient mass per link =", max(mass.values()), min(mass.values()))
    if LHS != RHS_of(W, with_W=False): firesII['CII1'] = True
    W2, _ = buildW(G, y, coef_b1_own=F(1))
    if LHS != RHS_of(W2): firesII['CII2'] = True
    W3, _ = buildW(G, y, eps3_W=+1)
    if LHS != RHS_of(W3): firesII['CII3'] = True
print("Part II: II1 (G-slot decomposition exact):", "PASS" if okII1 else "FAIL")
print("Part II: II2 (mass 2(d-1)=6 per link; d(d-1)/2=6 plaquettes per base):", "PASS" if okII2 else "FAIL")
for k_, v in firesII.items(): print("Part II control", k_, "FIRES" if v else "does NOT fire")
overall = okI1 and okI2 and okII1 and okII2 and all(fires.values()) and all(firesII.values())
print("OVERALL:", "PASS" if overall else "FAIL")
