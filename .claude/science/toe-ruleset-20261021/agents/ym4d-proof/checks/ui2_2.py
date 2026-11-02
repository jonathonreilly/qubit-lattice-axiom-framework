# ui2_2 — Lemma VS (iv) algebra + exact gauge-row EOM identity (criteria: ui2_2_criteria.md, written before this script).
from fractions import Fraction as Fr
import random, sympy as sp
random.seed(20261029)
res = {}
# ---------- Part A ----------
def rmat(r, c, lo=-3, hi=3): return sp.Matrix(r, c, lambda i, j: sp.Rational(random.randint(lo, hi), random.randint(1, 3)))
n, k = 7, 3
A0 = rmat(n, n); Cc = A0*A0.T + sp.eye(n)                      # SPD
D = rmat(n, k)
while D.rank() < k: D = rmat(n, k)
Ci = Cc.inv()
def Pi_of(Cinv): return Cinv - Cinv*D*(D.T*Cinv*D).inv()*D.T*Cinv
Pi = Pi_of(Ci)
X = Pi + D*D.T
B = sp.Matrix.hstack(*D.T.nullspace())                          # basis of E = ker D^T (7x4)
M = rmat(n, 5); H0 = rmat(5, 5); H = H0 + H0.T; G0 = rmat(5, 5); G = G0*G0.T
res['A1'] = (Pi*D).is_zero_matrix
res['A2'] = X.det() != 0 and (Pi*X.inv()*Pi - Pi).is_zero_matrix
res['A3'] = sp.simplify(X.det()*(B.T*Cc*B).det() - (D.T*D).det()*(B.T*B).det()) == 0
def schur_ok(PiU):
    Xu = PiU + D*D.T
    Z = H + M.T*PiU*M + G; Y = -M.T*PiU
    return (Z - Y*Xu.inv()*Y.T - (H + G)).is_zero_matrix
res['A4'] = schur_ok(Pi)
res['Ac1_fires'] = (not (Ci*D).is_zero_matrix) and (not schur_ok(Ci))
# ---------- Part B ----------
def qm(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return (a1*a2 - b1*b2 - c1*c2 - d1*d2, a1*b2 + b1*a2 + c1*d2 - d1*c2,
            a1*c2 - b1*d2 + c1*a2 + d1*b2, a1*d2 + b1*c2 - c1*b2 + d1*a2)
def qa(p, q): return tuple(x + y for x, y in zip(p, q))
def qs(c, p): return tuple(c*x for x in p)
def qconj(p): return (p[0], -p[1], -p[2], -p[3])
ONE = (Fr(1), Fr(0), Fr(0), Fr(0)); ZERO = (Fr(0),)*4
def rq_unit():
    w = [Fr(random.randint(-4, 4), random.randint(1, 4)) for _ in range(3)]; nn = sum(x*x for x in w)
    return ((1 - nn)/(1 + nn), 2*w[0]/(1 + nn), 2*w[1]/(1 + nn), 2*w[2]/(1 + nn))
def rq_im(): return (Fr(0),) + tuple(Fr(random.randint(-3, 3), random.randint(1, 3)) for _ in range(3))
# truncated polynomials in (t, s), total degree <= 2: dict {(i, j): quaternion}
KEYS = [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)]
def pm(P, Q):
    R = {}
    for (i, j), p in P.items():
        for (a, b), q in Q.items():
            if i + a + j + b <= 2: R[(i + a, j + b)] = qa(R.get((i + a, j + b), ZERO), qm(p, q))
    return R
def expo(Xq, Yq, sign=1):   # exp(sign*(tX + sY)) truncated
    L = {(1, 0): qs(sign, Xq), (0, 1): qs(sign, Yq)}
    Q2 = pm(L, L)
    R = {(0, 0): ONE}; R.update(L)
    for kk, v in Q2.items(): R[kk] = qa(R.get(kk, ZERO), qs(Fr(1, 2), v))
    return R
S = 2
sites = [(a, b) for a in range(S) for b in range(S)]
def sh(x, mu): return ((x[0] + (1 if mu == 0 else 0)) % S, (x[1] + (1 if mu == 1 else 0)) % S)
links = [(x, mu) for x in sites for mu in (0, 1)]
def f_poly(U, Xf, Yf):
    tot = {}
    def lk(b): return pm({(0, 0): U[b]}, expo(Xf[b], Yf[b]))
    def lki(b): return pm(expo(Xf[b], Yf[b], -1), {(0, 0): qconj(U[b])})
    for x in sites:
        Up = pm(pm(pm(lk((x, 0)), lk((sh(x, 0), 1))), lki((sh(x, 1), 0))), lki((x, 1)))
        for kk, v in Up.items(): tot[kk] = tot.get(kk, Fr(0)) - v[0]
    return tot
def Hess(U, Xf, Yf): return f_poly(U, Xf, Yf).get((1, 1), Fr(0))
def Grad(U, Yf): return f_poly(U, {b: ZERO for b in links}, Yf).get((0, 1), Fr(0))
def Dlam(U, lam): return {b: qa(qm(qm(qconj(U[b]), lam[b[0]]), U[b]), qs(-1, lam[sh(b[0], b[1])])) for b in links}
def lbar(U, lam): return {b: qa(qm(qm(qconj(U[b]), lam[b[0]]), U[b]), lam[sh(b[0], b[1])]) for b in links}
def comm_field(Af, Bf): return {b: qa(qm(Af[b], Bf[b]), qs(-1, qm(Bf[b], Af[b]))) for b in links}
U = {b: rq_unit() for b in links}
okB1 = True; c1 = c2 = c3 = True
for _ in range(3):
    Xf = {b: rq_im() for b in links}; lam = {x: rq_im() for x in sites}
    lhs = Hess(U, Xf, Dlam(U, lam))
    cf = comm_field(lbar(U, lam), Xf)
    okB1 = okB1 and lhs == -Fr(1, 2)*Grad(U, cf)
    c1 = c1 and lhs == -Grad(U, cf)                                      # Bc1: coefficient 1
    c2 = c2 and lhs == -Fr(1, 2)*Grad(U, comm_field(Dlam(U, lam), Xf))   # Bc2: derivative vertex
    c3 = c3 and lhs == 0                                                 # Bc3: on-shell form
res['B1'] = okB1
res['B2'] = any(Grad(U, {b: (rq_im() if b == bb else ZERO) for b in links}) != 0 for bb in links)
U1 = {b: ONE for b in links}; Xf = {b: rq_im() for b in links}; lam = {x: rq_im() for x in sites}
res['B3'] = Hess(U1, Xf, Dlam(U1, lam)) == 0 and Grad(U1, comm_field(lbar(U1, lam), Xf)) == 0
res['Bc1_fires'] = not c1; res['Bc2_fires'] = not c2; res['Bc3_fires'] = not c3
for kk, v in res.items(): print(kk, 'PASS' if v else 'FAIL')
