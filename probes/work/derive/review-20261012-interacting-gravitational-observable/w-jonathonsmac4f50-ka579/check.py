#!/usr/bin/env python3
"""check.py -- review-20261012-interacting-gravitational-observable (J:derive ... :a1)

Self-contained exact-arithmetic checks (sympy / Fractions only; no floating point
decides any PASS).  Setting: the lane-supplied d=1 box law (R8-1/R9-2 style): a
translation-invariant fibre over total lattice momentum P with internal matrix
Hamiltonian H(P), first moment K' = (1/2){H, X} + B(P), X = i d/dP, B = a
translation-invariant (fibre-diagonal) Hermitian completion, uniform lapse
H_g = H + g K'.  Definitions used throughout:

    J = i[H,K']   (gravitating momentum, the integral of T^{01})
    N = i[H,J]    (source of the momentum Ward identity; N=0 <=> J conserved)
    A = -i[K',J] - H   (boost-closure defect; A=0 <=> [K',J] = iH)

Nothing here derives the four axioms' content; the axioms (docs/MINIMAL_AXIOMS_2026-06-29.md)
supply no dynamics and no stress, so H, K', B are lane-supplied objects.
"""
import random
import sys
import time

import sympy as sp

T0 = time.time()
RESULTS = []


def rec(name, ok, detail=""):
    RESULTS.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + name + ((" -- " + detail) if detail else ""))
    sys.stdout.flush()


def zero_matrix(M):
    return all(sp.simplify(e) == 0 for e in M)


def comm(a, b):
    return a * b - b * a


def acomm(a, b):
    return a * b + b * a


def rnd_rat(rng, lim=5):
    return sp.Rational(rng.randint(-lim, lim), rng.randint(1, 4))


def rnd_herm(rng, n):
    M = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            M[i, j] = rnd_rat(rng) + sp.I * rnd_rat(rng)
    return M + M.H


# ---------------------------------------------------------------------------
# S1.  Exact reduction: the uniform-field response depends on the stress only
#      through (H, K).  Matrix identities, random exact Hermitian H, K.
# ---------------------------------------------------------------------------
g = sp.symbols("g", real=True)
rng = random.Random(20261012)
ok = True
for n in (3, 4, 5):
    H = rnd_herm(rng, n)
    K = rnd_herm(rng, n)
    Hg = H + g * K
    J = sp.I * comm(H, K)
    N = sp.I * comm(H, J)
    A = -sp.I * comm(K, J) - H
    c1 = zero_matrix(sp.I * comm(Hg, K) - J)                       # dK/dt = J
    c2 = zero_matrix(sp.I * comm(Hg, H) + g * J)                   # dH/dt = -g J
    c3 = zero_matrix(sp.I * comm(Hg, J) - (N - g * (H + A)))       # dJ/dt = N - g(H+A)
    ok = ok and c1 and c2 and c3
rec("S1 exact identities dK/dt=J, dH/dt=-gJ, dJ/dt=N-g(H+A) (3 random Hermitian pairs, n=3,4,5)", ok)

# ---------------------------------------------------------------------------
# S2.  Finite-dimensional trace obstruction (operator form of the zone-mean
#      statement): tr A = -tr H, tr N = 0 for ANY finite H, K.
# ---------------------------------------------------------------------------
ok = True
for n in (2, 3, 4, 6):
    H = rnd_herm(rng, n)
    K = rnd_herm(rng, n)
    J = sp.I * comm(H, K)
    N = sp.I * comm(H, J)
    A = -sp.I * comm(K, J) - H
    ok = ok and sp.simplify(A.trace() + H.trace()) == 0 and sp.simplify(N.trace()) == 0
rec("S2 finite-dim: tr A = -tr H and tr N = 0 for random (H,K); so A=0 on a finite invariant sector forces tr H = 0",
    ok, "no positive-energy finite-dimensional sector closes the boost algebra")

# ---------------------------------------------------------------------------
# S3.  Fibre calculus: operator identities on a generic 2-component test spinor
#      with generic symmetric H(P), B(P).  J = (1/2){H,H'} + i[H,B];
#      A = (1/2){H,J_P} - (1/2){X,N} - i[B,J] - H.
# ---------------------------------------------------------------------------
P = sp.symbols("P", real=True)
fa, fb, fd, f1, f2, b11, b12, b22 = [sp.Function(n)(P) for n in "a b d f1 f2 b11 b12 b22".split()]
Hs = sp.Matrix([[fa, fb], [fb, fd]])
Bs = sp.Matrix([[b11, b12], [b12, b22]])
psi = sp.Matrix([f1, f2])


def Xop(v):
    return sp.I * v.diff(P)


def Kop(v):
    return (Hs * Xop(v) + Xop(Hs * v)) / 2 + Bs * v


Hp = Hs.diff(P)
Jf = (Hs * Hp + Hp * Hs) / 2 + sp.I * comm(Hs, Bs)
d1 = sp.simplify(sp.I * (Hs * Kop(psi) - Kop(Hs * psi)) - Jf * psi)
rec("S3a operator identity i[H,K'] psi = ((1/2){H,H'} + i[H,B]) psi (generic symmetric H(P), B(P))",
    all(e == 0 for e in d1))
Nf = sp.I * comm(Hs, Jf)
Jfp = Jf.diff(P)
lhs = -sp.I * (Kop(Jf * psi) - Jf * Kop(psi)) - Hs * psi
rhs = (Hs * Jfp + Jfp * Hs) / 2 * psi - (Xop(Nf * psi) + Nf * Xop(psi)) / 2 - sp.I * comm(Bs, Jf) * psi - Hs * psi
d2 = sp.simplify(lhs - rhs)
rec("S3b operator identity A = (1/2){H,J_P} - (1/2){X,N} - i[B,J] - H (generic H(P), B(P))",
    all(e == 0 for e in d2))

# ---------------------------------------------------------------------------
# S4.  Plateau: H(P)=sqrt(M^2+P^2) with constant noncommuting-with-anything mass matrix M
#      => J = P*1, N = 0, A = 0 exactly (the box-sector Poincare closure).
# ---------------------------------------------------------------------------
tt = sp.symbols("t", real=True)          # rational parametrisation of the rotation: C=(1-t^2)/(1+t^2), S=2t/(1+t^2)
Cc = (1 - tt ** 2) / (1 + tt ** 2)
Ss = 2 * tt / (1 + tt ** 2)
mu1, mu2 = sp.symbols("mu1 mu2", positive=True)
Pp = sp.symbols("P", positive=True)
Rm = sp.Matrix([[Cc, -Ss], [Ss, Cc]])
e1 = sp.sqrt(mu1 ** 2 + Pp ** 2)
e2 = sp.sqrt(mu2 ** 2 + Pp ** 2)
Hpl = Rm * sp.diag(e1, e2) * Rm.T
Hplp = Hpl.diff(Pp)
Jpl = (Hpl * Hplp + Hplp * Hpl) / 2
Jpl = Jpl.applyfunc(sp.simplify)
Npl = (sp.I * comm(Hpl, Jpl)).applyfunc(sp.simplify)
Apl = ((Hpl * Jpl.diff(Pp) + Jpl.diff(Pp) * Hpl) / 2 - Hpl).applyfunc(sp.simplify)
rec("S4 plateau fibre H=sqrt(M^2+P^2): J = P*1, N = 0, A = 0 exactly (B=0)",
    Jpl == sp.Matrix([[Pp, 0], [0, Pp]]) and Npl == sp.zeros(2, 2) and Apl == sp.zeros(2, 2))

# ---------------------------------------------------------------------------
# S5.  Shell source, B = 0, two-channel switch family
#      H = H0 + c(P)(H_M - H0), H0 = diag(h1,h2), H_M = R diag(g1,g2) R^T,
#      h_i' = P/h_i, g_i' = P/g_i.   Closed form of N.
# ---------------------------------------------------------------------------
c, cp = sp.symbols("c cp", real=True)
h1, h2, g1, g2 = sp.symbols("h1 h2 g1 g2", positive=True)
H0 = sp.diag(h1, h2)
HM = Rm * sp.diag(g1, g2) * Rm.T
H0p = sp.diag(Pp / h1, Pp / h2)
HMp = Rm * sp.diag(Pp / g1, Pp / g2) * Rm.T
Hsh = H0 + c * (HM - H0)
Hshp = H0p + c * (HMp - H0p) + cp * (HM - H0)
Jsh = (Hsh * Hshp + Hshp * Hsh) / 2
Nsh = sp.I * comm(Hsh, Jsh)
claimed = (-sp.I * Cc * Ss * (g1 - g2) * (h1 - h2)
           * (Pp * c * (c - 1) * (g1 * g2 - h1 * h2) - cp * g1 * g2 * h1 * h2)
           * (c * (g1 + g2 - h1 - h2) + h1 + h2) / (2 * g1 * g2 * h1 * h2))
diff = sp.simplify(Nsh[0, 1] - claimed)
rec("S5a closed form N_01 = -i C S (g1-g2)(h1-h2) [P c(c-1)(g1 g2 - h1 h2) - c' g1 g2 h1 h2] tr(H)/(2 g1 g2 h1 h2)",
    diff == 0 and sp.simplify(Nsh[0, 0]) == 0 and sp.simplify(Nsh[1, 1]) == 0 and sp.simplify(Nsh[1, 0] + Nsh[0, 1]) == 0)
sol = sp.solve(sp.Eq(claimed, 0), cp)
rec("S5b with mixing (C S (g1-g2)(h1-h2) != 0): N = 0 iff c' = -P c(1-c) (1/(h1 h2) - 1/(g1 g2))  (logistic law)",
    len(sol) == 1 and sp.simplify(sol[0] - (-Pp * c * (1 - c) * (1 / (h1 * h2) - 1 / (g1 * g2)))) == 0)
# exact rational instance: M0 = diag(5,16), M = R diag(9,35) R^T, R = [[3/5,-4/5],[4/5,3/5]]; at P=12 all roots rational
sub_inst = {h1: 13, h2: 20, g1: 15, g2: 37, tt: sp.Rational(1, 2), Pp: 12}
kappa12 = sp.Rational(12) * (sp.Rational(1, 260) - sp.Rational(1, 555))
rec("S5c instance P=12: sqrt(25+144)=13, sqrt(256+144)=20, sqrt(81+144)=15, sqrt(1225+144)=37; kappa(12)=12(1/260-1/555)=59/2405",
    (25 + 144 == 13 ** 2) and (256 + 144 == 20 ** 2) and (81 + 144 == 15 ** 2) and (1225 + 144 == 37 ** 2)
    and kappa12 == sp.Rational(59, 2405)
    and sp.simplify(sol[0].subs(sub_inst) + sp.Rational(59, 2405) * c * (1 - c)) == 0)
# the logistic coefficient stays bounded on the whole window, so an N=0 profile cannot reach 0 or 1
P_ = sp.symbols("P_", nonnegative=True)
b0 = sp.expand((25 + P_ ** 2) * (256 + P_ ** 2) - 80 ** 2)
bM = sp.expand((81 + P_ ** 2) * (1225 + P_ ** 2) - 315 ** 2)
ok_pos = all(co >= 0 for co in sp.Poly(b0, P_).all_coeffs()) and all(co >= 0 for co in sp.Poly(bM, P_).all_coeffs())
# kappa(P) in [-P/315, P/80]  =>  |int_0^12 kappa| <= max(144/160, 144/630) = 9/10 ; e^{9/10} < 3 since e^9 < 3^10
bound = max(sp.Rational(144, 160), sp.Rational(144, 630))
rec("S5d bounded-odds corollary: det H0 >= 80, det H_M >= 315 on P>=0, so |change of logit c| <= 9/10 on [0,12], e^{9/10}<3: "
    "an exactly source-free profile (B=0) keeps c(12)/(1-c(12)) within a factor 3 of c(0)/(1-c(0)) and never reaches 0 or 1",
    ok_pos and bound == sp.Rational(9, 10) and sp.N(sp.exp(9), 30) < 3 ** 10)

# ---------------------------------------------------------------------------
# S6.  Universal completion: B_ik = i J_ik/(E_i - E_k) (H-eigenbasis) makes J exactly
#      conserved; J_B is the dephased (H-diagonal) part of J_0.  Exact rational data.
# ---------------------------------------------------------------------------
rng2 = random.Random(7)
ok = True
for n in (3, 4):
    Sx = sp.zeros(n, n)
    for i in range(n):
        for j in range(i + 1, n):
            v = rnd_rat(rng2, 3)
            Sx[i, j], Sx[j, i] = v, -v
    Qm = (sp.eye(n) - Sx) * (sp.eye(n) + Sx).inv()          # rational orthogonal (Cayley)
    E = [sp.Rational(k + 1) + sp.Rational(k, 7) ** 2 for k in range(n)]
    Hm = Qm * sp.diag(*E) * Qm.T
    J0 = rnd_herm(rng2, n)
    Jt = Qm.T * J0 * Qm
    Bt = sp.zeros(n, n)
    for i in range(n):
        for k in range(n):
            if i != k:
                Bt[i, k] = sp.I * Jt[i, k] / (E[i] - E[k])
    Bm = Qm * Bt * Qm.T
    JB = J0 + sp.I * comm(Hm, Bm)
    ok = (ok and zero_matrix(Bm - Bm.H)
          and zero_matrix(JB - Qm * sp.diag(*[Jt[i, i] for i in range(n)]) * Qm.T)
          and zero_matrix(comm(Hm, JB))
          and sp.simplify(JB.trace() - J0.trace()) == 0)
rec("S6 B_ik = i J_ik/(E_i-E_k): B Hermitian, J_B = H-dephased J_0, [H,J_B]=0 exactly, tr J_B = tr J_0 (n=3,4 exact rational)", ok,
    "pole at E_i=E_k: B is quasi-local only if J_0 has no on-shell off-diagonal part")

# ---------------------------------------------------------------------------
# S7.  Trace lemma (completion independent) and the obstruction numbers.
# ---------------------------------------------------------------------------
cf = sp.Function("cf")(Pp)
h_a = sp.sqrt(25 + Pp ** 2)
h_b = sp.sqrt(256 + Pp ** 2)
g_a = sp.sqrt(81 + Pp ** 2)
g_b = sp.sqrt(1225 + Pp ** 2)
Rr = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)], [sp.Rational(4, 5), sp.Rational(3, 5)]])
H0i = sp.diag(h_a, h_b)
HMi = Rr * sp.diag(g_a, g_b) * Rr.T
Hi = H0i + cf * (HMi - H0i)
Hip = Hi.diff(Pp)
trl = sp.simplify((Hi * Hip).trace() - sp.diff((Hi * Hi).trace(), Pp) / 2)
rec("S7a tr J_0 = tr((1/2){H,H'}) = (1/2) d/dP tr(H^2) for the symbolic switch profile c(P)", trl == 0)
Bgen = sp.Matrix([[sp.Function("q1")(Pp), sp.Function("q2")(Pp)], [sp.Function("q2")(Pp), sp.Function("q3")(Pp)]])
rec("S7b tr(i[H,B]) = 0 for generic B(P): the fibre trace of J is the same for every first-moment completion",
    sp.simplify((sp.I * comm(Hi, Bgen)).trace()) == 0)
tau_plateau = sp.simplify((HMi * HMi).trace() - 2 * Pp ** 2)
tau_free = sp.simplify((H0i * H0i).trace() - 2 * Pp ** 2)
Delta = tau_plateau - tau_free
rec("S7c tau(P)=tr H^2 - 2P^2 equals tr M^2 = 1306 on the plateau (c=1) and tr M_0^2 = 281 in the free region (c=0); Delta = 1025 != 0",
    tau_plateau == 1306 and tau_free == 281 and Delta == 1025)
# nondegeneracy of H(c) at P=12 for all c in [0,1] (discriminant polynomial has no real root in [0,1])
Hnum = (H0 + c * (HM - H0)).subs(sub_inst)
disc = sp.expand((Hnum[0, 0] - Hnum[1, 1]) ** 2 + 4 * Hnum[0, 1] ** 2)
pd = sp.Poly(disc, c)
rec("S7d H(c) at P=12 has distinct eigenvalues for every c in [0,1] (discriminant > 0; Sturm count of roots in [0,1] is 0)",
    pd.count_roots(0, 1) == 0 and disc.subs(c, 0) > 0)

# ---------------------------------------------------------------------------
# S8.  Diagonal lemma: for N=0 (J = sum_i j_i |e_i><e_i|) the H-eigenbasis matrix of
#      (1/2){H,J_P} has diagonal E_i j_i' and off-diagonal (1/2)(E1+E2)(j2-j1) alpha'(up to sign);
#      the B-term -i[B,J] has zero diagonal.  Hence A=0 forces j_i' = 1.
# ---------------------------------------------------------------------------
al = sp.Function("al")(P)
E1f, E2f, j1f, j2f = [sp.Function(n)(P) for n in ["E1", "E2", "j1", "j2"]]
Ra = sp.Matrix([[sp.cos(al), -sp.sin(al)], [sp.sin(al), sp.cos(al)]])
Hd = Ra * sp.diag(E1f, E2f) * Ra.T
Jd = Ra * sp.diag(j1f, j2f) * Ra.T
Mt = (Ra.T * ((Hd * Jd.diff(P) + Jd.diff(P) * Hd) / 2) * Ra).applyfunc(sp.simplify)
cond_diag = sp.simplify(Mt[0, 0] - E1f * j1f.diff(P)) == 0 and sp.simplify(Mt[1, 1] - E2f * j2f.diff(P)) == 0
off = Mt[0, 1]
cand_p = sp.simplify(off - sp.Rational(1, 2) * (E1f + E2f) * (j2f - j1f) * al.diff(P))
cand_m = sp.simplify(off + sp.Rational(1, 2) * (E1f + E2f) * (j2f - j1f) * al.diff(P))
Bd = sp.Matrix([[sp.Function("p1")(P), sp.Function("p2")(P)], [sp.Function("p2")(P), sp.Function("p3")(P)]])
Bt2 = (Ra.T * (-sp.I * comm(Bd, Jd)) * Ra).applyfunc(sp.simplify)
rec("S8 eigenbasis form: diag[(1/2){H,J_P}] = E_i j_i', offdiag = +/-(1/2)(E1+E2)(j2-j1)alpha'; diag[-i[B,J]] = 0",
    cond_diag and (cand_p == 0 or cand_m == 0) and sp.simplify(Bt2[0, 0]) == 0 and sp.simplify(Bt2[1, 1]) == 0)

# ---------------------------------------------------------------------------
# S9.  Weyl-midpoint density family: moments (exact Gaussian integrals).
#      f(Q) = chi(Q) int phi(P+Q) w(P+Q/2) psi(P) dP,  chi even, chi(0)=1, chi'(0)=0.
# ---------------------------------------------------------------------------
Pq, Q, c2 = sp.symbols("Pq Q c2", real=True)


def gauss_int(poly, a_, b_):
    poly = sp.Poly(sp.expand(poly), Pq)
    mu = b_ / (2 * a_)
    var = 1 / (2 * a_)

    def mom(n):
        tot = 0
        for k in range(0, n + 1, 2):
            tot += (sp.binomial(n, k) * mu ** (n - k) * var ** (k // 2) * (sp.factorial2(k - 1) if k > 0 else 1))
        return tot

    res = 0
    for (n,), co in poly.terms():
        res += co * mom(n)
    return sp.sqrt(sp.pi / a_) * sp.exp(b_ ** 2 / (4 * a_)) * res


E0 = -(Pq - sp.Rational(1, 3)) ** 2 - Pq ** 2 / 2
A_, B_, C_ = sp.Rational(3, 2), sp.Rational(2, 3), -sp.Rational(1, 9)


def Iint(poly):
    return sp.exp(C_) * gauss_int(poly, A_, B_)


polyphi = lambda x: 1 + x
polypsi = 2 - Pq + Pq ** 2
wfun = lambda x: 1 + x ** 2 / 3 + x ** 3 / 5
Eq = -(Pq + Q - sp.Rational(1, 3)) ** 2 - Pq ** 2 / 2
ipoly = polyphi(Pq + Q) * wfun(Pq + Q / 2) * polypsi * (1 + c2 * Q ** 2 / 2)


def fn(n):
    d = sp.diff(ipoly * sp.exp(Eq), Q, n).subs(Q, 0)
    return sp.simplify(Iint(sp.expand(sp.simplify(d / sp.exp(E0)))))


f0, f1_, f2_ = fn(0), fn(1), fn(2)
psiF = polypsi * sp.exp(-Pq ** 2 / 2)
Xf = lambda u: sp.I * sp.diff(u, Pq)


def expect(Opsi):
    pol = sp.simplify(polyphi(Pq) * Opsi / sp.exp(-Pq ** 2 / 2))
    return sp.simplify(Iint(sp.expand(pol)))


wP = wfun(Pq)
e_w = expect(wP * psiF)
e_a1 = expect(Xf(wP * psiF) + wP * Xf(psiF))
dd = Xf(Xf(wP * psiF)) + 2 * Xf(wP * Xf(psiF)) + wP * Xf(Xf(psiF))
e_dd = expect(dd)
rec("S9a zeroth and first moments: f(0)=<w>, f'(0)=(i/2)<{X,w}> for every even chi (chi'(0)=0)",
    sp.simplify(f0 - e_w) == 0 and sp.simplify(f1_ - sp.I / 2 * e_a1) == 0)
rec("S9b second moment: f''(0) = chi''(0)<w> - (1/4)<{X,{X,w}}>; chi''(0) = c2 is NOT fixed by (H,K): composition-dependent tidal ambiguity",
    sp.simplify(f2_ - c2 * f0 + e_dd / 4) == 0 and sp.simplify(sp.diff(f2_, c2) - f0) == 0)

# ---------------------------------------------------------------------------
# S10.  Size of that ambiguity in a non-uniform field: a W-density smeared with variance s^2
#       feels Phi + (1/2)s^2 Phi'' + ...; test Phi = x^3 with a Gaussian kernel.
# ---------------------------------------------------------------------------
xx, XX, s = sp.symbols("xx XX s", real=True)
# <x^3> for a normal kernel of mean X, variance s^2, from its moment generating function exp(X u + s^2 u^2/2)
uu = sp.symbols("uu", real=True)
sm = sp.simplify(sp.diff(sp.exp(XX * uu + s ** 2 * uu ** 2 / 2), uu, 3).subs(uu, 0))
force_ratio = sp.simplify(sp.diff(sm, XX) / sp.diff(XX ** 3, XX) - 1)
rec("S10 smeared coupling of Phi=x^3: int Phi rho = X^3 + 3 s^2 X; relative force correction = (1/2)s^2 Phi'''/Phi' = s^2/X^2",
    sp.simplify(sm - (XX ** 3 + 3 * s ** 2 * XX)) == 0 and sp.simplify(force_ratio - s ** 2 / XX ** 2) == 0)

# ---------------------------------------------------------------------------
# S11.  Centroid claim re-derived exactly: two bodies, general dispersions, lapse exchange
#       H = e1(k1)+e2(k2)+lam e1 e2 u(x1-x2).  J_E = sum e_i e_i' depends on k only.
# ---------------------------------------------------------------------------
x1, x2, k1, k2, lam = sp.symbols("x1 x2 k1 k2 lam", real=True)
ef1 = sp.Function("e1")
ef2 = sp.Function("e2")
uf = sp.Function("u")
Htot = ef1(k1) + ef2(k2) + lam * ef1(k1) * ef2(k2) * uf(x1 - x2)
JE = ef1(k1) * sp.diff(ef1(k1), k1) + ef2(k2) * sp.diff(ef2(k2), k2)


def pb(F, G):  # {F,G} = sum dF/dx dG/dk - dF/dk dG/dx
    return (sp.diff(F, x1) * sp.diff(G, k1) - sp.diff(F, k1) * sp.diff(G, x1)
            + sp.diff(F, x2) * sp.diff(G, k2) - sp.diff(F, k2) * sp.diff(G, x2))


dJdt = pb(JE, Htot)                                   # dF/dt = {F,H}
Hess1 = sp.diff(JE, k1, 1)                            # = (e1 e1')' = Hess(e1^2/2)
Hess2 = sp.diff(JE, k2, 1)
r_ = x1 - x2
expected = -lam * ef1(k1) * ef2(k2) * sp.diff(uf(r_), x1) * (Hess1 - Hess2)
rec("S11a exact all orders in lam: dJ_E/dt = -lam e1 e2 u'(x1-x2) [Hess(e1^2/2)(k1) - Hess(e2^2/2)(k2)]",
    sp.simplify(dJdt - expected) == 0)
ktot = k1 + k2
rec("S11b crystal momentum k1+k2 is conserved exactly ({k1+k2, H} = 0)", sp.simplify(pb(ktot, Htot)) == 0)
# Poincare dispersions (Hess = 1) give dJ_E/dt = 0:
em1 = sp.sqrt(sp.Symbol("m1", positive=True) ** 2 + k1 ** 2)
em2 = sp.sqrt(sp.Symbol("m2", positive=True) ** 2 + k2 ** 2)
rec("S11c Hess(e^2/2) = 1 for e = sqrt(m^2+k^2) (so A_i = 0 and dJ_E/dt = 0 for box-type legs)",
    sp.simplify(sp.diff(em1 * sp.diff(em1, k1), k1) - 1) == 0 and sp.simplify(sp.diff(em2 * sp.diff(em2, k2), k2) - 1) == 0)

# ---------------------------------------------------------------------------
# S12.  Lemma Q arithmetic under a stress with an interacting part supported on box legs:
#       free dust kernel F00(k',k) = (e(k')+e(k))/2 > 0 straddles the face, so
#       [T00_free, Q_box] has the nonzero element F00 (c(k)-c(k')) = F00.
# ---------------------------------------------------------------------------
delta, m_, b_ = sp.symbols("delta m b", positive=True)
eps = lambda k: sp.sqrt(m_ ** 2 + k ** 2)
F00 = (eps(b_ + delta) + eps(b_ - delta)) / 2
rec("S12 straddling-face element F00 = (e(b+d)+e(b-d))/2 > 0 for all d>0 (so the free part leaks charge across the face)",
    sp.limit(F00, delta, 0) == eps(b_) and F00.subs({m_: 3, b_: 4, delta: sp.Rational(1, 10)}) > 0)

# ---------------------------------------------------------------------------
total = len(RESULTS)
npass = sum(RESULTS)
nfail = total - npass
print("runtime %.1f s" % (time.time() - T0))
print("TOTAL: PASS=%d FAIL=%d" % (npass, nfail))
if nfail == 0:
    print("HIT: (scoped, finite-channel) with N the momentum-Ward source and A the boost defect, no choice of "
          "translation-invariant first-moment completion B and no switch profile makes N=A=0 across a plateau-to-free "
          "switch whenever tr(M^2) differs between the interacting and free mass operators (instance: 1306 vs 281); "
          "for B=0 the source has a closed form whose vanishing is a logistic law that never reaches 0 or 1.")
print("SUMMARY: exact checks of (i) the reduction of the bound-body fall to (H,K), (ii) a closed-form shell source and "
      "a completion-independent trace obstruction to extending universal fall through the interaction switch in a "
      "finite-channel fibre, (iii) the free second-moment parameter of the Weyl-midpoint stress; the continuum "
      "(infinite-channel) version of the obstruction, d>=2, N>=3 and gauge fields remain open.")
sys.exit(0 if nfail == 0 else 1)
