#!/usr/bin/env python3
"""Massive continuum limit of the supplied two-qubit cubic Dirac walk.

Source note:
  docs/TWO_QUBIT_CUBIC_DIRAC_WALK_MASSIVE_CONTINUUM_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-26.md

Two implementation paths:
  exact_part()   sympy identities: massless member and Wilson vector, massive members
                 as M U0 M, vertex-lemma ingredients and the TRIM table, Jacobians of g,
                 the generator expansion through O(a^2), the massive dispersion, the
                 Poincare commutator lemma, the Dirac identification, named points;
  numeric_part() explicit 4x4 matrices with matrix exponentials, Schur logarithms and
                 matrix powers: unitarity and covariance, TRIM and vertex-lemma bounds,
                 convergence of U^n to exp(-i t H_D) with its O(a) / O(a^2) dichotomy,
                 dispersion fits and the Gaussian doubler tail.
The expected constants (s, |W| = s sqrt(1 - s^2), TRIM cosines, alpha, beta) come from the
analytic formulas; only the remainder constant C3 is measured, and it is reported as a
sample maximum, not a certified bound.

Supplied premises (not derived): a two-qubit site with the cubic coin 1 (x) D(R) (outside
the one-qubit axiom), the Clifford walk family of the two-qubit cubic-tick note, and the
declared scaling tau = a, b fixed, mass angle theta = m a.
"""
from __future__ import annotations

import itertools
import os
import sys

for _var in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_var, "1")

import numpy as np
import sympy as sp
from scipy.linalg import expm, schur

AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/TWO_QUBIT_CUBIC_DIRAC_WALK_MASSIVE_CONTINUUM_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-26.md",
)

PASS = FAIL = 0


def check(name, ok):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS {name}", flush=True)
    else:
        FAIL += 1
        print(f"FAIL {name}", flush=True)


def EX(e):
    return sp.nsimplify(sp.simplify(sp.expand(e)))


def exact_part():
    print("== exact (sympy) identities", flush=True)
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
    check('series check: arccos(1-u)^2 = 2u + u^2/3 + 4u^3/45 + O(u^4)',
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



def numeric_part():
    print("== numerical checks (independent matrix implementation)", flush=True)
    I2 = np.eye(2); t1 = np.array([[0, 1], [1, 0]], complex); t2 = np.array([[0, -1j], [1j, 0]]); t3 = np.diag([1.0, -1.0]).astype(complex)
    TAU = [np.kron(t1, I2), np.kron(t2, I2)]
    TS = [np.kron(t3, x) for x in (t1, t2, t3)]
    ALPHA = [-x for x in TS]


    def Gmat(b0, b1, b2):
        return np.array([[1 - 3*b0**2, -2*b0*b1, b1**2 - b0**2 - b0*b2, -3*b1*(b0 - b2)],
                         [-2*b0*b1, b0**2 - 2*b1**2, b1*(b0 - b2), b0*b2 - b1**2 + b2**2],
                         [b1**2 - b0**2 - b0*b2, b1*(b0 - b2), 2*b1**2 - b2**2, 2*b1*b2],
                         [-3*b1*(b0 - b2), b0*b2 - b1**2 + b2**2, 2*b1*b2, 3*b2**2]])


    def phi(k):
        c = np.cos(k)
        return np.array([1.0, c.sum(), c[0]*c[1] + c[0]*c[2] + c[1]*c[2], c.prod()])


    def gvec(b, k):
        c, s = np.cos(k), np.sin(k)
        return np.array([s[i]*(b[0] + b[1]*(c[(i+1) % 3] + c[(i+2) % 3]) + b[2]*c[(i+1) % 3]*c[(i+2) % 3]) for i in range(3)])


    phi0 = np.array([1.0, 3, 3, 1]); wv = np.array([0.0, 1, 2, 1])


    class Walk:
        def __init__(self, b, name):
            self.b = np.array(b, float); self.name = name
            G = Gmat(*self.b)
            ev, V = np.linalg.eigh(G)
            keep = ev > 1e-13
            F = (V[:, keep]*np.sqrt(ev[keep])).T
            if F.shape[0] < 3:
                F = np.vstack([F, np.zeros((3 - F.shape[0], 4))])
            e = F @ phi0
            Q = np.linalg.qr(np.column_stack([e, np.eye(3)]))[0][:, :3]
            if Q[:, 0] @ e < 0:
                Q[:, 0] *= -1
            F = Q.T @ F
            W = F[1:] @ wv
            if np.linalg.norm(W) > 1e-12:          # rotate the h-plane so that W lies on h1
                ang = np.arctan2(W[1], W[0])
                R = np.array([[np.cos(ang), np.sin(ang)], [-np.sin(ang), np.cos(ang)]])
                F[1:] = R @ F[1:]
            self.F = F
            self.Wvec = F[1:] @ wv
            self.s = self.b[0] + 2*self.b[1] + self.b[2]

        def U0(self, k):
            f, h1, h2 = self.F @ phi(k)
            g = gvec(self.b, k)
            return f*np.eye(4) + 1j*(h1*TAU[0] + h2*TAU[1] + sum(g[i]*TS[i] for i in range(3)))

        def U(self, k, th, chi):
            Mm = expm(0.5j*th*(np.cos(chi)*TAU[0] + np.sin(chi)*TAU[1]))
            return Mm @ self.U0(k) @ Mm


    def logH(Um, a):
        """(i/a) Log U, principal branch, via complex Schur form (diagonal for normal U)."""
        T, Z = schur(Um, output='complex')
        lam = np.diag(T)
        return (1j/a) * (Z @ np.diag(np.log(lam/np.abs(lam))) @ Z.conj().T)


    def HD(p, m, s, chi):
        beta = -(np.cos(chi)*TAU[0] + np.sin(chi)*TAU[1])
        return s*sum(p[i]*ALPHA[i] for i in range(3)) + m*beta


    def opn(A):
        return np.linalg.norm(A, 2)


    # ---------------------------------------------------------------- parameter points
    co = [259200000000, -453744000000, 12644840000, 1185396800, -39225499]
    ustar = min(r.real for r in np.roots(co) if abs(r.imag) < 1e-12 and r.real > 0)
    r5, r6, r15 = np.sqrt(5), np.sqrt(6), np.sqrt(15)
    walks = [Walk((11/30, np.sqrt(ustar), 3/20), 'bstar'),
             Walk(((r6 + 2*r15)/27, (5*r6 - 2*r15)/27, (2*r15 - 2*r6)/27), 'iso'),
             Walk(((9*r5 - 5)/38, (5*r5 - 7)/19, (71 - 29*r5)/38), 'gold')]
    TRIM = [np.array(K)*np.pi for K in itertools.product((0, 1), repeat=3)]
    rng = np.random.default_rng(7)

    for Wk in walks:
        print(f"--- {Wk.name}: b = {Wk.b}, s = {Wk.s:.10f}, |W| = {np.linalg.norm(Wk.Wvec):.10f}")
        check(f'{Wk.name}: |W| = s sqrt(1-s^2)', abs(np.linalg.norm(Wk.Wvec) - abs(Wk.s)*np.sqrt(max(0, 1 - Wk.s**2))) < 1e-7)
        Ks = rng.uniform(-np.pi, np.pi, (300, 3))
        err = max(opn(Wk.U(k, 0.2, 0.7) @ Wk.U(k, 0.2, 0.7).conj().T - np.eye(4)) for k in Ks)
        check(f'{Wk.name}: massive member M U0 M unitary (theta=0.2, chi=0.7), max err {err:.1e}', err < 1e-12)
        # covariance under the cubic C4 about z: k -> R k, W = 1 (x) exp(-i pi sigma3/4)
        Rz = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]); Dz = np.kron(I2, expm(-0.25j*np.pi*t3))
        cov = max(opn(Wk.U(Rz @ k, 0.2, 0.7) - Dz @ Wk.U(k, 0.2, 0.7) @ Dz.conj().T) for k in Ks[:50])
        check(f'{Wk.name}: massive member is cubic covariant (C4z), err {cov:.1e}', cov < 1e-12)

        # quasienergy table at TRIMs, massless and massive
        for th, chi in ((0.0, 0.0), (0.1, 0.0), (0.1, np.pi/2)):
            qe = [np.max(np.abs(np.angle(np.linalg.eigvals(Wk.U(K, th, chi))))) for K in TRIM]
            print(f"   theta={th}, chi={chi:.3f}: TRIM quasienergies |omega| = {np.round(qe, 6)}")
        th = 0.1
        q0 = [np.max(np.abs(np.angle(np.linalg.eigvals(Wk.U(K, 0, 0))))) for K in TRIM]
        ok = True
        for chi in np.linspace(0, np.pi, 7):
            qt = [np.max(np.abs(np.angle(np.linalg.eigvals(Wk.U(K, th, chi))))) for K in TRIM]
            ok &= all(abs(x - y) <= th + 1e-12 for x, y in zip(qt, q0))
        check(f'{Wk.name}: |omega_K(theta) - theta_K| <= theta at all TRIMs (theta=0.1, 7 twist angles)', ok)
        if Wk.name == 'gold':
            dX = max(abs(np.max(np.abs(np.angle(np.linalg.eigvals(Wk.U(np.array([np.pi, 0, 0]), th, chi))))) - (np.pi - th))
                     for th in (0.05, 0.1, 0.3) for chi in (0, 1.0, np.pi/2))
            check(f'gold: massive axis doubler sits at quasienergy pi - theta exactly (U(X) = -U(0)), err {dX:.1e}', dX < 1e-10)

        # vertex-lemma bound and the global minimum at the TRIMs (sampled sanity check; the lemma itself is exact)
        for th, chi in ((0.0, 0.0), (0.1, 0.0), (0.1, np.pi/2)):
            fK = [np.real(np.trace(Wk.U(K, th, chi)))/4 for K in TRIM]
            cth = min((np.cos(th) - fK[i])/(2*np.count_nonzero(TRIM[i])) for i in range(1, 8))
            Kr = rng.uniform(-np.pi, np.pi, (1500, 3))
            lhs = np.array([1 - np.real(np.trace(Wk.U(k, th, chi)))/4 for k in Kr])
            rhs = (1 - np.cos(th)) + cth*np.array([np.sum(1 - np.cos(k)) for k in Kr])
            check(f'{Wk.name}: theta={th}, chi={chi:.2f}: 1 - cos omega >= (1 - cos theta) + c_theta sum(1 - cos k_a), c_theta = {cth:.4f} (1500 random k)',
                  np.all(lhs >= rhs - 1e-12) and cth > 0)
            fpi = 1 + np.array([np.real(np.trace(Wk.U(k, th, chi)))/4 for k in Kr])
            print(f"   min over samples of 1 + cos omega = {fpi.min():.4e}; min over TRIMs = {min(1 + x for x in fK):.4e}")
            check(f'{Wk.name}: theta={th}, chi={chi:.2f}: sampled min of 1 + cos omega >= its TRIM minimum',
                  fpi.min() >= min(1 + x for x in fK) - 1e-12)

    # ---------------------------------------------------------------- fiber Hamiltonian and convergence
    m, t, Pmax = 1.0, 1.0, 2.0
    dirs = rng.normal(size=(40, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
    psamp = [r*d for d in dirs for r in (0.5, 1.0, 2.0)]
    alist = [0.04, 0.02, 0.01, 0.005]
    for Wk in walks:
        for chi in (0.0, np.pi/2):
            Wt = Wk.Wvec[0]*TAU[0] + Wk.Wvec[1]*TAU[1]
            C3 = []
            errs, errsV = [], []
            for a in alist:
                r3, e1, e2 = 0.0, 0.0, 0.0
                n = int(round(t/a))
                for p in psamp:
                    Um = Wk.U(a*p, m*a, chi)
                    Ha = logH(Um, a)
                    Hd = HD(p, m, Wk.s, chi)
                    lead = Hd + 0.5*a*(p @ p)*Wt
                    r3 = max(r3, opn(Ha - lead)/(a**2*(np.linalg.norm(p) + m)**3))
                    Un = np.linalg.matrix_power(Um, n)
                    E = expm(-1j*t*Hd)
                    e1 = max(e1, opn(Un - E))
                    # momentum-dependent chiral rotation (maximal twist only removes the O(a) term)
                    eps_ = 0.5*a*(p @ p)*np.linalg.norm(Wk.Wvec)
                    beta = -(np.cos(chi)*TAU[0] + np.sin(chi)*TAU[1])
                    Gp = -(np.cos(chi + np.pi/2)*TAU[0] + np.sin(chi + np.pi/2)*TAU[1])  # perp flavour direction
                    sgn = np.sign(np.real(np.trace(Wt @ Gp))) or 1.0
                    ph = np.arctan(eps_/m)
                    Vr = np.cos(ph/2)*np.eye(4) + sgn*np.sin(ph/2)*beta @ Gp
                    e2 = max(e2, opn(Vr @ Un @ Vr.conj().T - E))
                C3.append(r3); errs.append(e1); errsV.append(e2)
            sl = np.polyfit(np.log(alist), np.log(errs), 1)[0]
            slV = np.polyfit(np.log(alist), np.log(errsV), 1)[0]
            print(f"   {Wk.name} chi={chi:.3f}: max_p ||U^n - e^(-itH_D)|| = {np.array(errs)} slope {sl:.3f}; "
                  f"with p-dependent chiral rotation: {np.array(errsV)} slope {slV:.3f}; C3 estimates {np.round(C3, 4)}")
            check(f'{Wk.name} chi={chi:.2f}: remainder ||H_a - H_D - (a/2)p^2 W.tau|| / (a^2(|p|+m)^3) stays bounded as a -> 0 (max {max(C3):.3f})',
                  max(C3) < 5 and C3[-1] <= 1.2*C3[0] + 1e-3)
            bound = [alist[i]*0 + t*(0.5*alist[i]*np.linalg.norm(Wk.Wvec)*Pmax**2 + max(C3)*alist[i]**2*(Pmax + m)**3) for i in range(len(alist))]
            check(f'{Wk.name} chi={chi:.2f}: error <= t(|W| a P^2/2 + C3 a^2 (P+m)^3) (t multiple of a, floor term zero)',
                  all(e <= bb*1.0001 + 1e-12 for e, bb in zip(errs, bound)))
            if Wk.name == 'gold':
                check(f'gold chi={chi:.2f}: |W| = 0, convergence is O(a^2) (slope {sl:.2f})', sl > 1.8)
            elif chi == 0.0:
                check(f'{Wk.name} chi=0 (Wilson-aligned mass): convergence is O(a) (slope {sl:.2f}) and the chiral rotation does not help (slope {slV:.2f})',
                      0.85 < sl < 1.2 and slV < 1.3)
            else:
                check(f'{Wk.name} chi=pi/2 (maximal twist): constant identification O(a) (slope {sl:.2f}); p-dependent chiral rotation V_a(p) gives O(a^2) (slope {slV:.2f})',
                      0.85 < sl < 1.2 and slV > 1.8)

    # floor term: t not a multiple of a
    Wk = walks[0]
    a = 0.01; tt = 1.0 + 0.6*a; n = int(np.floor(tt/a))
    p = np.array([0.3, 0.2, 0.1])
    fe = opn(np.linalg.matrix_power(Wk.U(a*p, m*a, 0.0), n) - expm(-1j*tt*HD(p, m, Wk.s, 0.0)))
    print(f"   floor-term example: a={a}, t={tt}: error {fe:.4e} vs a*E = {a*np.sqrt(m**2 + Wk.s**2*p@p):.4e}")
    check('floor term: with t/a non-integer the error includes (t - na) E <= a E (example within bound)',
          fe <= a*np.sqrt(m**2 + Wk.s**2*p @ p)*0.61 + t*(0.5*a*np.linalg.norm(Wk.Wvec)*(p @ p) + 3*a**2) + 1e-12)

    # ---------------------------------------------------------------- dispersion coefficients (numerical fits)
    print('--- massive dispersion: E_a^2 a^2 = omega^2 fitted in eps for (k, theta) = eps (n, mu)')
    for Wk in walks:
        b0, b1, b2 = Wk.b; s = Wk.s
        alpha = s*(s**3 + 3*b0 - 6*b1 - 9*b2)/12; beta = -s*(b0 - b1 - 2*b2)/3
        Wn = np.linalg.norm(Wk.Wvec)
        for chi in (0.0, np.pi/2, 1.0):
            ok = True
            for nd in (np.array([1.0, 0, 0]), np.array([1.0, 1, 0])/np.sqrt(2), np.array([1.0, 1, 1])/np.sqrt(3), np.array([0.3, -0.5, 0.81])):
                mu = 0.7
                nd = nd/np.linalg.norm(nd)
                pred = lambda e: (mu**2 + s**2)*e**2 - mu*Wn*np.cos(chi)*e**3 + (alpha + beta*np.sum(nd**4) - s**2*mu**2/3)*e**4
                # exact omega from the matrix, mpmath-free: residual should scale as e^5
                res = []
                for e in (0.02, 0.01):
                    om = np.max(np.abs(np.angle(np.linalg.eigvals(Wk.U(e*nd, e*mu, chi)))))
                    res.append(abs(om**2 - pred(e)))
                slope = np.log(res[0]/res[1])/np.log(2)
                ok &= slope > 4.5
            check(f'{Wk.name} chi={chi:.2f}: omega^2 = theta^2 + s^2 k^2 - theta |W| cos(chi) k^2 + alpha|k|^4 + beta sum k^4 - (s^2/3) theta^2 k^2 + O(eps^5) along 4 directions', ok)

    # ---------------------------------------------------------------- Gaussian doubler overlap (1D factor)
    from scipy.special import erfc
    print('--- Gaussian packet: lattice-momentum weight at |k_a| >= pi/2 (1D factor), FFT vs erfc')
    for Sa in (1.0, 1.5, 2.0):
        N = 4096
        x = np.arange(N) - N//2
        psi = np.exp(-x**2/(4*Sa**2)); psi /= np.linalg.norm(psi)
        pk = np.abs(np.fft.fft(psi))**2; pk /= pk.sum()
        kk = 2*np.pi*np.fft.fftfreq(N)
        w = pk[np.abs(kk) >= np.pi/2].sum()
        pred = erfc(np.pi/2*np.sqrt(2)*Sa)
        print(f"   Sigma/a = {Sa}: weight {w:.3e}, erfc(kappa sqrt2 Sigma/a) = {pred:.3e}")
        check(f'Sigma/a={Sa}: doubler-region weight equals the Gaussian tail erfc(pi Sigma/(sqrt2 a)) to 5%',
              abs(w - pred) <= 0.05*pred + 1e-300)



def main():
    exact_part()
    numeric_part()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
