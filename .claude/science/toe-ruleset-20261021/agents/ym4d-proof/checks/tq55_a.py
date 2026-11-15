"""tq55_a: rotlet in R^4 -- symmetric, degree -4, divergence-free, nonzero angular-momentum flux.
Exact rational polynomial arithmetic (fractions only). Criteria: tq55_a_criteria.md (written first)."""
from fractions import Fraction as Fr
from itertools import product

# polynomial = dict{exponent tuple: Fraction}
def padd(p, q, c=Fr(1)):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, Fr(0)) + c * v
        if r[k] == 0: del r[k]
    return r
def pmul(p, q):
    r = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = tuple(a + b for a, b in zip(k1, k2))
            r[k] = r.get(k, Fr(0)) + v1 * v2
            if r[k] == 0: del r[k]
    return r
def pscale(p, c): return {k: c * v for k, v in p.items() if c * v != 0}
def pdiff(p, i):
    r = {}
    for k, v in p.items():
        if k[i] > 0:
            kk = list(k); kk[i] -= 1; kk = tuple(kk)
            r[kk] = r.get(kk, Fr(0)) + v * k[i]
            if r[kk] == 0: del r[kk]
    return r
def var(i, d):
    k = [0]*d; k[i] = 1; return {tuple(k): Fr(1)}
def const(c, d): return {tuple([0]*d): Fr(c)} if c != 0 else {}
def r2(d):
    p = {}
    for i in range(d): p = padd(p, pmul(var(i, d), var(i, d)))
    return p
# rational function (P, k) = P / |x|^k ; derivative d_i(P|x|^-k) = [(d_i P)|x|^2 - k x_i P]/|x|^(k+2)
def rdiff(f, i, d):
    P, k = f
    return (padd(pmul(pdiff(P, i), r2(d)), pmul(var(i, d), P), Fr(-k)), k + 2)
def is_zero(P): return len(P) == 0
def homog_degree(P):
    degs = {sum(k) for k in P}
    return degs.pop() if len(degs) == 1 else None

# exact normalized sphere moments on S^{d-1}
def dfact_odd(k):  # (2k-1)!!
    r = 1
    for j in range(1, 2*k, 2): r *= j
    return r
def gamma_half_ratio(k):  # Gamma(k+1/2)/Gamma(1/2) = (2k-1)!!/2^k
    return Fr(dfact_odd(k), 2**k)
def gamma_int_ratio(K, d):  # Gamma(d/2)/Gamma(K+d/2), d even
    h = d // 2
    num = 1
    for j in range(1, h): num *= j            # (h-1)!
    den = 1
    for j in range(1, K + h): den *= j        # (K+h-1)!
    return Fr(num, den)
def sphere_mean_monomial(k, d):
    if any(e % 2 for e in k): return Fr(0)
    half = [e // 2 for e in k]
    r = Fr(1)
    for h in half: r *= gamma_half_ratio(h)
    return r * gamma_int_ratio(sum(half), d)
def sphere_mean(P, d):  # P evaluated on |n|=1 (homogeneous or not: substitute |n|=1 is implicit, P is a polynomial in n)
    return sum((v * sphere_mean_monomial(k, d) for k, v in P.items()), Fr(0))

out = []
def rep(s): out.append(s); print(s)

d = 4
# P0 moment self-test
m1 = sphere_mean_monomial((2,0,0,0), 4); m2 = sphere_mean_monomial((4,0,0,0), 4); m3 = sphere_mean_monomial((2,2,0,0), 4)
tot = 4*m2 + 12*m3
P0 = (m1 == Fr(1,4) and m2 == Fr(1,8) and m3 == Fr(1,24) and tot == 1)
rep(f"P0 moments <n1^2>={m1} <n1^4>={m2} <n1^2n2^2>={m3} sum={tot} -> {'PASS' if P0 else 'FAIL'}")

def antisym(a, b, d):
    M = [[Fr(0)]*d for _ in range(d)]; M[a][b] = Fr(1); M[b][a] = Fr(-1); return M
def Mx(M, mu, d):  # (Mx)_mu = M_{mu a} x_a
    p = {}
    for a in range(d):
        if M[mu][a] != 0: p = padd(p, pscale(var(a, d), M[mu][a]))
    return p
def rotlet(M, d, sign=+1):
    # numerator N_{mu nu} = (Mx)_mu x_nu + sign*(Mx)_nu x_mu
    return [[padd(pmul(Mx(M, mu, d), var(nu, d)), pmul(Mx(M, nu, d), var(mu, d)), Fr(sign)) for nu in range(d)] for mu in range(d)]
def divergence(N, k, d):
    res = []
    for nu in range(d):
        tot = {}
        for mu in range(d):
            Pd, kd = rdiff((N[mu][nu], k), mu, d)
            tot = padd(tot, Pd)   # all have same kd = k+2
        res.append(tot)
    return res
def flux_over_area(N, k, J, d):
    # flux density on unit sphere: n_mu N_{mu nu}(n) (Jn)_nu (|n|=1 so |x|^-k = 1); return sphere mean
    dens = {}
    for mu in range(d):
        for nu in range(d):
            Jn = {}
            for b in range(d):
                if J[nu][b] != 0: Jn = padd(Jn, pscale(var(b, d), J[nu][b]))
            dens = padd(dens, pmul(pmul(var(mu, d), N[mu][nu]), Jn))
    return sphere_mean(dens, d)

# P1, P2
P1 = True; P2 = True
for a in range(d):
    for b in range(a+1, d):
        M = antisym(a, b, d); N = rotlet(M, d)
        sym = all(N[m][n] == N[n][m] for m in range(d) for n in range(d))
        div = divergence(N, 6, d)
        dz = all(is_zero(x) for x in div)
        hd = {homog_degree(N[m][n]) for m in range(d) for n in range(d) if not is_zero(N[m][n])}
        P1 = P1 and sym and dz
        P2 = P2 and (hd == {2})
        rep(f"  M=E{a+1}{b+1}-E{b+1}{a+1}: symmetric={sym} divergence-free={dz} numerator degrees={sorted(hd)}")
rep(f"P1 symmetric & divergence-free for all 6 basis M -> {'PASS' if P1 else 'FAIL'}")
rep(f"P2 numerator degree 2 with k=6 (homogeneous degree -4) -> {'PASS' if P2 else 'FAIL'}")
J12 = antisym(0, 1, d); J34 = antisym(2, 3, d); J13 = antisym(0, 2, d)
f3 = flux_over_area(rotlet(J12, d), 6, J12, d)
P3 = (f3 == Fr(1, 2))
rep(f"P3 flux/|S^3| (M=J=E12-E21) = {f3} (expected 1/2) -> {'PASS' if P3 else 'FAIL'}")
f4 = flux_over_area(rotlet(J12, d), 6, J34, d)
P4 = (f4 == 0)
rep(f"P4 flux/|S^3| (M=E12-E21, J=E34-E43) = {f4} (expected 0) -> {'PASS' if P4 else 'FAIL'}")

# P5 improvement tensors Delta = d_mu d_nu Phi - delta Lap Phi
def improvement(Phi, d):
    # returns numerator matrix with common k
    first = [rdiff(Phi, mu, d) for mu in range(d)]
    second = [[rdiff(first[mu], nu, d) for nu in range(d)] for mu in range(d)]
    k2 = second[0][0][1]
    lap = {}
    for mu in range(d): lap = padd(lap, second[mu][mu][0])
    N = [[padd(second[mu][nu][0], lap if mu == nu else {}, Fr(-1)) for nu in range(d)] for mu in range(d)]
    return N, k2
P5 = True
for name, Phi in [("|x|^-2", (const(1, d), 2)), ("x1 x2 |x|^-4", (pmul(var(0, d), var(1, d)), 4))]:
    N, k2 = improvement(Phi, d)
    sym = all(N[m][n] == N[n][m] for m in range(d) for n in range(d))
    dz = all(is_zero(x) for x in divergence(N, k2, d))
    # on the unit sphere |x|^-k2 = 1 but the numerator is homogeneous of degree (k2 - 4); evaluate directly
    fa = flux_over_area(N, k2, J12, d); fb = flux_over_area(N, k2, J13, d)
    ok = sym and dz and fa == 0 and fb == 0
    P5 = P5 and ok
    rep(f"  improvement Phi={name}: k={k2} symmetric={sym} divergence-free={dz} flux(J12)={fa} flux(J13)={fb}")
rep(f"P5 improvement tensors divergence-free with zero flux -> {'PASS' if P5 else 'FAIL'}")

# Controls (must FIRE = nonzero)
NJ = rotlet(J12, d)
c1a = any(not is_zero(x) for x in divergence(NJ, 5, d))
c1b = any(not is_zero(x) for x in divergence(NJ, 7, d))
rep(f"C1 |x|^-5 divergence nonzero={c1a}; |x|^-7 divergence nonzero={c1b} -> {'FIRED' if (c1a and c1b) else 'DID NOT FIRE'}")
d3 = 3
M3 = antisym(0, 1, d3); N3 = rotlet(M3, d3)
c2 = any(not is_zero(x) for x in divergence(N3, 6, d3))
rep(f"C2 R^3 analogue with |x|^-6 divergence nonzero={c2} -> {'FIRED' if c2 else 'DID NOT FIRE'}")
NA = rotlet(J12, d, sign=-1)
c3 = any(not is_zero(x) for x in divergence(NA, 6, d))
rep(f"C3 antisymmetric combination divergence nonzero={c3} -> {'FIRED' if c3 else 'DID NOT FIRE'}")
Nhalf = [[pmul(Mx(J12, mu, d), var(nu, d)) for nu in range(d)] for mu in range(d)]
fhalf = flux_over_area(Nhalf, 6, J12, d)
c4 = (fhalf != Fr(1, 2))
rep(f"C4 flux with only the first term of sigma = {fhalf} (must differ from 1/2) -> {'FIRED' if c4 else 'DID NOT FIRE'}")

allpass = P0 and P1 and P2 and P3 and P4 and P5 and c1a and c1b and c2 and c3 and c4
rep(f"OVERALL: {'PASS' if allpass else 'FAIL'}")
