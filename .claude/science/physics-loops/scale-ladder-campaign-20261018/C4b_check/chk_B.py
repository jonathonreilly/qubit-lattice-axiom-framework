#!/usr/bin/env python3
"""C4b_check part B: independent position-space reproduction of C4b B1/B2 (K2 = a_s K1) and hidden-choice probes.
Engine: vc_core (Euler-operator Poisson brackets of sympy-Function densities; own sqrt(g)R)."""
from vc_core import *

lam1, nu, K1, K2, mu, lf = sp.symbols("lam1 nu K1 K2 mu lam_f", positive=True)
s1, s2, kap, w, q, a = sp.symbols("s1 s2 kappa w q a", real=True)
divxi = sum(D(xi[k], k) for k in R3)
Np = lambda S1, S2: S1 * sum(xi[k] * D(N, k) for k in R3) + S2 * N * divxi

# ---------------------------------------------------------------- controls
R1, R2 = sqrtgR_series(2)
trh = sum(hf(k, k) for k in R3)
R1hand = sum(D(D(hf(i, j), i), j) for i in R3 for j in R3) - sum(D(D(trh, k), k) for k in R3)
check("T1", sp.expand(R1 - R1hand) == 0, "own [sqrt g R]^(1) of delta + h = d_i d_j h_ij - lap tr h")
# linearised diffeo identity of sqrt(g) R as a density (a test of the code's R2, not an input)
dR = hdeg_filter(pb(N * R1 + N * R2, Pdot(LieDelta(xi) + LieH(xi)), ferm=False), 1)
idt = div_eqs(sp.expand(dR + sum(xi[k] * D(N, k) for k in R3) * R1), N)
check("T2", idt == [], "{int N sqrt(g)R, int P L_xi(delta+h)} at O(h) = -int (xi.dN) R1 (density of weight 1): "
      "own R2 consistent with own R1")
F1, F2 = spinrot([1, 0, 0]), spinrot([0, 1, 0])
check("T3", div_eqs(sp.expand(N * (pb(F1, F2, grav=False) - 2 * bil(SIG[2]))), N) == [],
      "spinor bracket {int s1, int s2} = 2 int s3")
# flat walker algebra: {C[N], C[M]} = v^2 Kosmann[w] with w = N dM - M dN, solve for weight and spin coefficient
w0 = [sp.expand(N * D(M, k) - M * D(N, k)) for k in R3]
E0 = sp.eye(3)
br = pb(walker(N, E0), walker(M, E0), grav=False)
ww, kk, cv = sp.symbols("ww kk cv", real=True)
sol = vsolve(div_eqs(sp.expand(br - kosmann(w0, cv, ww, kk)), N), [cv, ww, kk])
check("T4", sol == [{cv: 1, ww: sp.Rational(1, 2), kk: sp.Rational(1, 4)}],
      f"flat walker {{C[N],C[M]}} = G_K[N dM - M dN] with G_K = int chibar i(xi.d + w div xi + i kap curl xi.sigma) chi: "
      f"forces w = 1/2 (half-density) and kap = 1/4: {sol}")

# ---------------------------------------------------------------- gravity h-linear {C, G}
Cg = N * (-K1 * R1 - K2 * R2)
Gg = Pdot(lam1 * LieDelta(xi) + mu * LieH(xi))
rg = sp.expand(hdeg_filter(pb(Cg, Gg, ferm=False), 1) - Np(s1, s2) * (-K1 * R1))
eg = div_eqs(rg, N)
solg = vsolve(eg, [K2, s1, s2])
check("G1", solg == [{K2: mu * K1 / lam1, s1: -mu, s2: 0}],
      f"gravity's h-linear {{C,G}} (G = lam1 G1 + mu int P L_xi h): lam1 K2 = mu K1, s1 = -mu, s2 = 0: {solg}")
# {G,G} at order P (h^0) fixes mu to the structure constant nu
lb = [sp.expand(sum(xi[k] * D(eta[i], k) - eta[k] * D(xi[i], k) for k in R3)) for i in R3]
Ge = Pdot(lam1 * LieDelta(eta) + mu * LieH(eta))
gg = hdeg_filter(pb(Gg, Ge, ferm=False), 0)
nus = sp.Symbol("nus", real=True)
Pr = Pdot(lam1 * LieDelta(lb))
# compare modulo divergence: test field = xi0 (gg is linear in xi)
sgg = vsolve(div_eqs(sp.expand(gg - nus * Pr), xi[0]), [nus])
check("G2", sgg == [{nus: mu}] or sgg == [{nus: -mu}],
      f"{{G[xi],G[eta]}} at order P = (+-)mu lam1 G1[[xi,eta]] (sign = bracket orientation): {sgg}; so the structure "
      f"constant nu of {{G,G}} = nu G[[xi,eta]] equals mu: G2 = nu int P L_xi h is forced, not a choice")
ORI = sgg[0][nus] / mu    # +-1: orientation of {G,G}

# ---------------------------------------------------------------- matter {C, G} at order chi chi
def matter_res(Ef, lam_f, wt, kp, S1, S2, Gmu=None):
    Cf = walker(N, Ef)
    G = Pdot(lam1 * LieDelta(xi)) + kosmann(xi, lam_f, wt, kp)
    r = hdeg_filter(pb(Cf, G), 0) - walker(Np(S1, S2), E0)
    return div_eqs(sp.expand(r), N)

Ea = (sp.eye(3) - a * Hm / 2).applyfunc(sp.expand)
ef = matter_res(Ea, lf, sp.Rational(1, 2), kap, s1, s2)
solf = vsolve(ef, [a, s1, s2, kap])
check("M1", solf == [{a: lf / lam1, s1: -lf, s2: 0, kap: sp.Rational(1, 4)}],
      f"walker {{C,G}} at order chi chi, frame delta - a h/2: a lam1 = lam_f, s1 = -lam_f, s2 = 0, Kosmann kap = 1/4: {solf}  "
      f"(C4b A2)")

# ---------------------------------------------------------------- B1, B2: joint
def joint(aval, extra_unk=()):
    efa = matter_res((sp.eye(3) - aval * Hm / 2).applyfunc(sp.expand), nu, sp.Rational(1, 2), sp.Rational(1, 4), s1, s2)
    egn = [sp.expand(e.subs(mu, nu)) for e in eg]
    return vsolve(egn + efa, [lam1, K2, s1, s2] + list(extra_unk))
sB1 = joint(1)
check("B1", sB1 == [{lam1: nu, K2: K1, s1: -nu, s2: 0}], f"a = 1, lam_f = nu, mu = nu: unique lam1 = nu, K2 = K1: {sB1}")
sB2 = joint(a)
check("B2", len(sB2) == 1 and sp.simplify(sB2[0][K2] - a * K1) == 0 and sp.simplify(sB2[0][lam1] - nu / a) == 0,
      f"a free: lam1 = nu/a, K2 = a K1: {sB2}.  Invariant content: gamma = a K1/K2 = 1 for every a")

# ---------------------------------------------------------------- hidden-choice probes
# H1: density weight of chi free (w), plus an isotropic trace coupling q trh delta in the frame (the only other
#     isotropic no-derivative h-linear frame term); unknowns a-relation, s1, s2, kap, q
Eq = (sp.eye(3) - a * Hm / 2 + q * trh * sp.eye(3)).applyfunc(sp.expand)
eH1 = matter_res(Eq, lf, w, kap, s1, s2)
sH1 = vsolve(eH1, [a, s1, s2, kap, q, w])
print("   H1 solutions:", sH1)
okH1 = len(sH1) == 1 and sp.simplify(sH1[0][a] - lf / lam1) == 0 and sH1[0][kap] == sp.Rational(1, 4) and sH1[0][w] == sp.Rational(1, 2) and sp.simplify(sH1[0][s2] - 2 * lam1 * q) == 0
check("H1", okH1, f"density weight w of chi left free and a trace coupling q tr h delta added: a lam1 = lam_f survives; "
      f"w = 1/2 is FORCED (with w free sympy.solve silently drops the w-equations; vsolve back-substitutes), q only moves s2 = 2 lam1 q (density convention): {sH1}")
# H2: G2 normalisation mu kept free in gravity (the matter side has no mu at this order): K2 = (mu/nu) a K1 ...
egm = eg
efa = matter_res(Ea, lf, sp.Rational(1, 2), sp.Rational(1, 4), s1, s2)
sH2 = vsolve(egm + efa, [K2, s1, s2, a, mu])
print("   H2 solutions:", sH2)
okH2 = len(sH2) == 1 and sp.simplify(sH2[0][mu] - lf) == 0 and sp.simplify(sH2[0][K2] - lf * K1 / lam1) == 0 \
    and sp.simplify(sH2[0][a] - lf / lam1) == 0
check("H2", okH2,
      f"mu, lam_f free: common lapse rule s1 = -mu = -lam_f forces mu = lam_f; K2/K1 = mu/lam1 = a.  So K2 = a K1 needs only "
      f"one common lapse rule (mu = lam_f), and {{G,G}} (G2) plus the fermion {{G,G}} (C1) both give it as nu: {sH2}")
total()
