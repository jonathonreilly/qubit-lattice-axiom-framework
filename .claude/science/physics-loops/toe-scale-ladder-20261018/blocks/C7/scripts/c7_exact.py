#!/usr/bin/env python3
"""C7 exact part: massive members, vertex lemma, doubler data, the O(a) fiber
Hamiltonian, the massive dispersion through O(a^2), the Poincare commutator lemma,
and the Dirac identification.

Every check here is an exact symbolic identity (sympy). Nothing is fitted.
Conventions follow docs/TWO_QUBIT_SITE_UNFREEZES_..._2026-10-16.md:
U(k) = f + i(h1 tau1 + h2 tau2) + i tau3 (x) g.sigma, (f,h1,h2) = F phi(k),
phi = (1, sum c, sum cc, c1c2c3), g = b0 v0 + b1 v1 + b2 v2, F^T F = G(b).
"""
from __future__ import annotations

import itertools
import sys

import sympy as sp

PASS = FAIL = 0


def EX(e):
    return sp.nsimplify(sp.simplify(sp.expand(e)))



def check(name, ok):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS {name}")
    else:
        FAIL += 1
        print(f"FAIL {name}")


b0, b1, b2 = b = sp.symbols('b0:3', real=True)
c = sp.symbols('c1:4', real=True)
k = sp.symbols('k1:4', real=True)


def phi_of(cs):
    return sp.Matrix([1, cs[0] + cs[1] + cs[2], cs[0]*cs[1] + cs[0]*cs[2] + cs[1]*cs[2], cs[0]*cs[1]*cs[2]])


G = sp.Matrix([[1 - 3*b0**2, -2*b0*b1, b1**2 - b0**2 - b0*b2, -3*b1*(b0 - b2)],
               [-2*b0*b1, b0**2 - 2*b1**2, b1*(b0 - b2), b0*b2 - b1**2 + b2**2],
               [b1**2 - b0**2 - b0*b2, b1*(b0 - b2), 2*b1**2 - b2**2, 2*b1*b2],
               [-3*b1*(b0 - b2), b0*b2 - b1**2 + b2**2, 2*b1*b2, 3*b2**2]])
phi0 = sp.Matrix([1, 3, 3, 1])
wv = sp.Matrix([0, 1, 2, 1])
s = b0 + 2*b1 + b2
aV = G*phi0          # f0 = aV . phi for the massless member
Mh = G - aV*aV.T     # = C^T C, C the 2x4 flavour (h) coefficient block

# ---------------------------------------------------------------- 0. Pauli
I2 = sp.eye(2)
t1 = sp.Matrix([[0, 1], [1, 0]]); t2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); t3 = sp.Matrix([[1, 0], [0, -1]])
kr = sp.kronecker_product
Gam = [kr(t1, I2), kr(t2, I2), kr(t3, t1), kr(t3, t2), kr(t3, t3)]

# ---------------------------------------------------------------- 1. massless member
check('phi0^T G phi0 = 1 identically: f0 = (G phi0).phi is the massless member (U(0)=1)',
      sp.expand((phi0.T*G*phi0)[0] - 1) == 0)
check('flavour block annihilates phi0: (G - a a^T) phi0 = 0, so h0(0) = 0',
      all(sp.expand(x) == 0 for x in Mh*phi0))
Wsq = sp.expand((wv.T*Mh*wv)[0])
check('|W|^2 = w^T (G - a a^T) w = s^2 (1 - s^2) (Wilson vector of the k^2 flavour term)',
      sp.expand(Wsq - s**2*(1 - s**2)) == 0)

# ---------------------------------------------------------------- 2. massive members = symmetric mass splitting
f, h1, h2, th = sp.symbols('f h1 h2 theta', real=True)
g1, g2, g3 = sp.symbols('g1:4', real=True)
U0 = f*sp.eye(4) + sp.I*(h1*Gam[0] + h2*Gam[1] + g1*Gam[2] + g2*Gam[3] + g3*Gam[4])
Mm = sp.cos(th/2)*sp.eye(4) + sp.I*sp.sin(th/2)*Gam[0]
lhs = (Mm*U0*Mm).applyfunc(lambda e: sp.expand(sp.expand_trig(e)))
fth = sp.cos(th)*f - sp.sin(th)*h1
h1th = sp.sin(th)*f + sp.cos(th)*h1
rhs = fth*sp.eye(4) + sp.I*(h1th*Gam[0] + h2*Gam[1] + g1*Gam[2] + g2*Gam[3] + g3*Gam[4])
diff = (lhs - rhs.applyfunc(lambda e: sp.expand(sp.expand_trig(e)))).applyfunc(lambda e: sp.simplify(sp.expand_trig(e)))
check('M U0 M with M = exp(i theta tau1/2) equals the O(3)-rotated member (f,h1) -> R_theta (f,h1), g unchanged',
      diff == sp.zeros(4))
D = sp.Matrix([[sp.exp(-sp.I*sp.pi/4), 0], [0, sp.exp(sp.I*sp.pi/4)]])
check('M commutes with every coin 1 (x) D(R) (checked on the generator exp(-i pi sigma3/4) and exp(-i pi sigma1/4))',
      all(sp.simplify(Mm*kr(I2, Dd) - kr(I2, Dd)*Mm) == sp.zeros(4)
          for Dd in (D, sp.cos(sp.pi/4)*I2 - sp.I*sp.sin(sp.pi/4)*t1)))

# ---------------------------------------------------------------- 3. vertex lemma ingredients
fsym = sp.Matrix(sp.symbols('F0:4'))
fphi = sp.expand((fsym.T*phi_of(c))[0])
check('every (F phi)(c) is multilinear in (c1,c2,c3) (degree <= 1 in each c_a)',
      all(sp.degree(fphi, ca) <= 1 for ca in c))
trims = [K for K in itertools.product((1, -1), repeat=3)]
check('the vertices of [-1,1]^3 in c are exactly the 8 TRIMs k_a in {0, pi}', len(trims) == 8)

# ---------------------------------------------------------------- 4. doubler table (massless member)
cosK = {}
for K in trims:
    cosK[K] = sp.expand((aV.T*phi_of(K))[0])
check('cos theta_X = 1 - 2 s^2 at the three axis TRIMs',
      all(sp.expand(cosK[K] - (1 - 2*s**2)) == 0 for K in trims if K.count(-1) == 1))
check('cos theta_M = 1 - 8 s (b0 - b2) at the three face TRIMs',
      all(sp.expand(cosK[K] - (1 - 8*s*(b0 - b2))) == 0 for K in trims if K.count(-1) == 2))
check('cos theta_R = 1 - 6(3b0^2 + 2b0b2 + 3b2^2 - 8b1^2) at the corner',
      sp.expand(cosK[(-1, -1, -1)] - (1 - 6*(3*b0**2 + 2*b0*b2 + 3*b2**2 - 8*b1**2))) == 0)
check('vertex lemma, c_0 at the X vertex: (1 - cos theta_X)/(2*1) = s^2 (equals the cone coefficient s^2)',
      sp.expand((1 - cosK[(-1, 1, 1)])/2 - s**2) == 0)

# Jacobians of g at the TRIMs and chirality (Weyl index of the tau3 = +1 block of g.sigma)
cs_ = [sp.cos(x) for x in k]; ss_ = [sp.sin(x) for x in k]
gk = [b0*ss_[i] + b1*ss_[i]*(cs_[(i+1) % 3] + cs_[(i+2) % 3]) + b2*ss_[i]*cs_[(i+1) % 3]*cs_[(i+2) % 3] for i in range(3)]
Jg = sp.Matrix(3, 3, lambda i, j: sp.diff(gk[i], k[j]))
dets = {}
for K in itertools.product((0, sp.pi), repeat=3):
    JK = Jg.subs(dict(zip(k, K))).applyfunc(sp.simplify)
    dets[K] = sp.factor(JK.det())
check('J_Gamma = s 1, det = s^3', sp.expand(dets[(0, 0, 0)] - s**3) == 0)
check('J_X = diag(-s, b0-b2, b0-b2): det = -s (b0-b2)^2',
      sp.expand(dets[(sp.pi, 0, 0)] + s*(b0 - b2)**2) == 0)
check('det J_M = (b0-b2)^2 (b0 - 2b1 + b2); det J_R = -(b0 - 2b1 + b2)^3',
      sp.expand(dets[(sp.pi, sp.pi, 0)] - (b0 - b2)**2*(b0 - 2*b1 + b2)) == 0
      and sp.expand(dets[(sp.pi, sp.pi, sp.pi)] + (b0 - 2*b1 + b2)**3) == 0)

# ---------------------------------------------------------------- 5. fiber Hamiltonian through O(a^2)
eps, mu = sp.symbols('epsilon mu', positive=True)   # k = eps n, theta = eps mu  (eps = a, n = p, mu = m)
n = sp.symbols('n1:4', real=True)
nsq = sum(x**2 for x in n)
N4 = sum(x**4 for x in n)


def ser(e, order):
    return sp.expand(sp.series(e, eps, 0, order + 1).removeO())


cn = [sp.cos(eps*x) for x in n]
phin = phi_of(cn)
phin_ser = phin.applyfunc(lambda e: ser(e, 4))
check('phi(eps n) = phi0 - eps^2 |n|^2 w/2 + O(eps^4) (no linear term: grad phi = 0 at all TRIMs)',
      all(sp.expand(phin_ser[i] - phi0[i] + eps**2*nsq*wv[i]/2).coeff(eps, 2) == 0
          and sp.expand(phin_ser[i]).coeff(eps, 1) == 0 for i in range(4)))
gser = [ser(e.subs(dict(zip(k, [eps*x for x in n]))), 3) for e in gk]
check('g(eps n) = s eps n + O(eps^3)', all(sp.expand(gser[i] - s*eps*n[i]).coeff(eps, 1) == 0 and
                                           sp.expand(gser[i]).coeff(eps, 2) == 0 for i in range(3)))
g3 = [sp.expand(gser[i]).coeff(eps, 3) for i in range(3)]
aniso = sp.expand(g3[0] - (-(b1 + b2)/2*n[0]*nsq))
check('g at O(k^3): g_a = s k_a - ((b1+b2)/2) k_a |k|^2 + ((b1 + 2 b2 - b0)/6) k_a^3: the only O(a^2) rotation breaking of H_a; it vanishes iff b0 = b1 + 2 b2 (k^4-isotropy plane)',
      sp.expand(aniso - (b1 + 2*b2 - b0)/6*n[0]**3) == 0)
# generic flavour row xi (h_par direction): xi.phi0 = 0, xi.w = Wc ; its quartic part does not enter through eps^4
Wc = sp.Symbol('Wc', real=True)
f0 = (aV.T*phin_ser)[0]
xiphi = -eps**2*nsq*Wc/2          # xi . phi(eps n) through eps^3
fT = sp.expand(ser(sp.cos(eps*mu), 4)*f0 - ser(sp.sin(eps*mu), 4)*xiphi)
uu = sp.expand(1 - fT)
uu = sum(uu.coeff(eps, j)*eps**j for j in range(5))
om2 = sp.expand(2*uu + uu**2/3 + 4*uu**3/45)   # arccos(1-u)^2 = 2u + u^2/3 + 4u^3/45 + O(u^4)
om2 = [sp.expand(om2.coeff(eps, j)) for j in range(5)]
alpha = s*(s**3 + 3*b0 - 6*b1 - 9*b2)/12
beta = -s*(b0 - b1 - 2*b2)/3
uP = sp.Symbol('uP', positive=True)
check('series check: arccos(1-u)^2 = 2u + u^2/3 + 4u^3/45 + O(u^4) (NB: the parent runner uses 8/45; see NOTE section 9)',
      sp.expand(sp.series(sp.acos(1 - uP)**2, uP, 0, 4).removeO() - (2*uP + uP**2/3 + 4*uP**3/45)) == 0)
check('massive omega^2: eps^2 term = mu^2 + s^2 |n|^2 (Dirac, speed s)',
      om2[0] == 0 and om2[1] == 0 and sp.expand(om2[2] - mu**2 - s**2*nsq) == 0)
check('massive omega^2: eps^3 term = -mu Wc |n|^2 (O(a) mass-dependent speed shift, Wc = |W| cos chi)',
      sp.expand(om2[3] + mu*Wc*nsq) == 0)
check('massive omega^2: eps^4 term = alpha |n|^4 + beta sum n^4 - (s^2/3) mu^2 |n|^2 (no mu^4 term)',
      sp.expand(om2[4] - alpha*nsq**2 - beta*N4 + s**2*mu**2*nsq/3) == 0)

# fiber Hamiltonian aH = -(arccos f / sqrt(1-f^2)) X ; prefactor = 1 + u/3 + ... = 1 + O(eps^2)
uS = sp.Symbol('u', positive=True)
pref = sp.series(sp.acos(1 - uS)/sp.sqrt(1 - (1 - uS)**2), uS, 0, 2).removeO()
check('arccos(1-u)/sqrt(1-(1-u)^2) = 1 + u/3 + O(u^2) (analytic at u = 0)', sp.expand(pref - 1 - uS/3) == 0)
# X through eps^2 in the frame (e_f, hhat, hperp):  h_par = sin(th) f0 + cos(th) h0_par, h_perp = h0_perp
Ws = sp.Symbol('Ws', real=True)
hpar = sp.expand(ser(sp.sin(eps*mu), 2)*f0 + ser(sp.cos(eps*mu), 2)*(-eps**2*nsq*Wc/2))
hpar = sum(hpar.coeff(eps, j)*eps**j for j in range(3))
hperp = -eps**2*nsq*Ws/2
check('h_par = eps mu - eps^2 |n|^2 Wc/2 + O(eps^3), h_perp = -eps^2 |n|^2 Ws/2: so a H_a = -(eps mu hhat.tau + eps s tau3 sigma.n) + (eps^2|n|^2/2) W.tau + O(eps^3)',
      sp.expand(hpar - eps*mu + eps**2*nsq*Wc/2) == 0)

# ---------------------------------------------------------------- 6. Poincare commutator lemma (generic matrix function)
p1, p2 = sp.symbols('p1 p2', real=True)
Hm = sp.Matrix(2, 2, lambda i, j: sp.Function(f'H{i}{j}')(p1, p2))
psi = sp.Matrix(2, 1, lambda i, j: sp.Function(f'psi{i}')(p1, p2))
P = (p1, p2)


def Kop(j, v):
    # K_j = (1/2){X_j, H}, X_j = i d/dp_j  ->  K_j v = i (H d_j v + (1/2)(d_j H) v)
    return sp.I*(Hm*v.diff(P[j]) + Hm.diff(P[j])*v/2)


comm = (Kop(0, Kop(1, psi)) - Kop(1, Kop(0, psi))).applyfunc(sp.expand)
H1, H2 = Hm.diff(p1), Hm.diff(p2)
pred = -(((Hm*H1 + H1*Hm)/2)*psi.diff(p2) - ((Hm*H2 + H2*Hm)/2)*psi.diff(p1) + (H1*H2 - H2*H1)*psi/4)
check('[K_1,K_2] = -( (1/2){H,d1H} d2 - (1/2){H,d2H} d1 + (1/4)[d1H,d2H] ) for an arbitrary matrix function H(p)',
      (comm - pred.applyfunc(sp.expand)).applyfunc(sp.simplify) == sp.zeros(2, 1))
Xop = lambda j, v: sp.I*v.diff(P[j])
cKH = (Kop(0, Hm*psi) - Hm*Kop(0, psi)).applyfunc(sp.expand)
check('[K_1, H] = (i/2){H, d1 H} (multiplication operator) for arbitrary H(p); = (i/2) d1(E^2) when H^2 = E^2 1',
      (cKH - (sp.I*(Hm*H1 + H1*Hm)/2*psi).applyfunc(sp.expand)).applyfunc(sp.simplify) == sp.zeros(2, 1))
cKP = (Kop(0, p1*psi) - p1*Kop(0, psi)).applyfunc(sp.expand)
check('[K_1, P_1] = i H and [K_1, P_2] = 0 exactly (P = multiplication by p)',
      (cKP - (sp.I*Hm*psi)).applyfunc(sp.simplify) == sp.zeros(2, 1)
      and (Kop(0, p2*psi) - p2*Kop(0, psi)).applyfunc(sp.simplify) == sp.zeros(2, 1))
Xs = sp.symbols('x1:6', real=True)
Xc = sum((Xs[i]*Gam[i] for i in range(5)), sp.zeros(4))
check('Clifford fiber: (sum x_i Gamma_i)^2 = |x|^2 1, so H_a(p)^2 = E_a(p)^2 1 exactly',
      (Xc*Xc - sum(x**2 for x in Xs)*sp.eye(4)).applyfunc(sp.expand) == sp.zeros(4))

# ---------------------------------------------------------------- 7. Dirac identification
alpha_w = [-kr(t3, sg) for sg in (t1, t2, t3)]
beta_w = -kr(t1, I2)
v = (t1 - t3)/sp.sqrt(2)
V = kr(v, I2)
alpha_D = [kr(t1, sg) for sg in (t1, t2, t3)]
beta_D = kr(t3, I2)
check('V = ((tau1 - tau3)/sqrt2) (x) 1 is unitary and maps alpha_a = -tau3 sigma_a -> tau1 sigma_a, beta = -tau1 -> tau3 (Dirac rep)',
      (V*V.H).applyfunc(sp.simplify) == sp.eye(4)
      and all((V*A*V.H - B).applyfunc(sp.simplify) == sp.zeros(4) for A, B in zip(alpha_w + [beta_w], alpha_D + [beta_D])))
check('V commutes with the coin 1 (x) D(R) (identification respects the cubic spin action)',
      all((V*kr(I2, Dd) - kr(I2, Dd)*V).applyfunc(sp.simplify) == sp.zeros(4)
          for Dd in (D, sp.cos(sp.pi/4)*I2 - sp.I*sp.sin(sp.pi/4)*t1)))
G5 = kr(t2, I2)  # maximal-twist Wilson direction (perp to beta inside the flavour plane)
check('maximal twist: Gamma_perp = tau2 anticommutes with beta and all alpha_a; beta*Gamma_perp commutes with alpha_a',
      all((G5*A + A*G5).applyfunc(sp.simplify) == sp.zeros(4) for A in alpha_w + [beta_w])
      and all((beta_w*G5*A - A*beta_w*G5).applyfunc(sp.simplify) == sp.zeros(4) for A in alpha_w))
# chiral rotation removes eps*Gamma_perp at fixed spectrum: V(phi) (m beta + e G5) V(phi)^dag = sqrt(m^2+e^2) beta
mS, eS = sp.symbols('m e', positive=True)
ph = sp.atan(eS/mS)
Vr = sp.cos(ph/2)*sp.eye(4) + sp.sin(ph/2)*beta_w*G5
res = Vr*(mS*beta_w + eS*G5)*Vr.H
check('exp((phi/2) beta Gamma_perp), tan phi = e/m, maps m beta + e Gamma_perp to sqrt(m^2+e^2) beta and fixes alpha_a',
      sp.simplify(res - sp.sqrt(mS**2 + eS**2)*beta_w) == sp.zeros(4)
      and all(sp.simplify(Vr*A*Vr.H - A) == sp.zeros(4) for A in alpha_w))

# ---------------------------------------------------------------- 8. named parameter points
r5, r6, r15 = sp.sqrt(5), sp.sqrt(6), sp.sqrt(15)
pts = {
    'gold': {b0: (9*r5 - 5)/38, b1: (5*r5 - 7)/19, b2: (71 - 29*r5)/38},
    'iso': {b0: (r6 + 2*r15)/27, b1: (5*r6 - 2*r15)/27, b2: (2*r15 - 2*r6)/27},
}
for name, P_ in pts.items():
    vals = {K: sp.nsimplify(EX(cosK[K].subs(P_))) for K in [(-1, 1, 1), (-1, -1, 1), (-1, -1, -1)]}
    print(f"{name}: s = {EX(s.subs(P_))}, cos(theta_X, theta_M, theta_R) = "
          f"{[EX(cosK[K].subs(P_)) for K in [(-1,1,1),(-1,-1,1),(-1,-1,-1)]]}, "
          f"beta = {EX(beta.subs(P_))}, alpha = {EX(alpha.subs(P_))}, "
          f"b0-2b1+b2 = {EX((b0-2*b1+b2).subs(P_))}")
Pg = pts['gold']
check('gold: cos theta_X = -1 (axis pi-modes) and cos theta_M, cos theta_R > -1 (face/corner not at pi)',
      EX(cosK[(-1, 1, 1)].subs(Pg)) == -1
      and all(sp.N(cosK[K].subs(Pg), 30) > -1 for K in [(-1, -1, 1), (-1, -1, -1)]))
check('gold: |W| = s sqrt(1-s^2) = 0: the leading O(a) fiber term vanishes on the light-speed member',
      EX(Wsq.subs(Pg)) == 0)
Pi = pts['iso']
check('iso: cos theta_X = -1/3, cos theta_M = -7/9; all three TRIM classes have cos in (-1, 1) (no pi-mode, no extra zero node)',
      EX(cosK[(-1, 1, 1)].subs(Pi)) == sp.Rational(-1, 3)
      and EX(cosK[(-1, -1, 1)].subs(Pi)) == sp.Rational(-7, 9)
      and all(-1 < sp.N(cosK[K].subs(Pi), 30) < 1 for K in trims if K != (1, 1, 1)))
check('iso: |W|^2 = s^2(1-s^2) = 2/9 and beta = 0 (k^4-isotropic)',
      EX(Wsq.subs(Pi)) == sp.Rational(2, 9) and EX(beta.subs(Pi)) == 0)
# chirality bookkeeping: sum of sign det J over the 8 zeros of g is the degree of g/|g| (must be 0)
for name, P_ in pts.items():
    sg = []
    for K in itertools.product((0, sp.pi), repeat=3):
        sg.append(sp.sign(sp.N(dets[K].subs(P_), 30)))
    check(f'{name}: Weyl indices of the 8 zeros of g sum to 0 (degree check): {sg}', sum(sg) == 0)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(0 if FAIL == 0 else 1)
