"""R17-7 probes (b), (c), (d) for (S): C = E0[H].
(b) Grid zero-point (R11-3: w >= 0, rho + p_U = -<eps trA>/6 > 0).  Homogeneous, kappa = 1, N = 1.
    B1 (sympy): R15-1 Lemma V re-derived with (S): E-sector energy lambda, pressure p_E; site-frame grid vacuum
        (rho_v, p_v) constant; matter conserved separately; total conserved (bridge d-i: exchange allowed).
        Show: geometry depends on Lt := lambda + rho_v and g' only; p_v drops out; (S) sets lambda = -e0 with
        e0 = rho_v + rho_rest  => Lt = -rho_rest = 0 when the rest of the ground-state energy is counted in e0.
    B2 (sympy): no exchange (d-ii) + metric GR: the constant site-frame vacuum is conserved only if (rho+p)_v = 0;
        the (S) residual (vacuum + Lambda counterterm) is (rho, p) = (0, rho_v + p_v).
    B3 numbers: the residual enthalpy from R11-3's table (counted once; per real scalar, lattice units, m = 1).
(c) Metastability.  C1: SM order of magnitude (RECALLED inputs).  C2 (sympy): three rules on a decay history:
    (S) C = E0; (S'-start) C = V of the basin at the first reading; (S'-current) C = V of the current basin.
(d) Covariant form.  D1 (sympy): G = kappa(T - C(x) g) with conserved T forces dC = 0 (Bianchi).
    D2: R15-1 Lemma S remote coefficient (3g/2)/(k^2/a^2 + Qbar) at g = 0 (counted once; GR control).
Subtraction rule (named before the run): residuals are measured from the (S) zero C = E0 only.
"""
import sympy as sp
import numpy as np

print("B1. Lemma V with (S), homogeneous (bridge d-i):")
t = sp.symbols('t')
H = sp.Function('H')(t); lam = sp.Function('lam')(t); rm = sp.Function('rho_m')(t)
rv, pv, pm, gp, rrest = sp.symbols('rho_v p_v p_m gprime rho_rest', real=True)
pE = gp - lam - (rv + pv)                      # Lemma V definition of g' (N = 1)
# total conservation: d/dt(lam + rho_v + rho_m) + 3H(lam + p_E + rho_v + p_v + rho_m + p_m) = 0 with matter conserved
cons = sp.diff(lam, t) + 3*H*(lam + pE + rv + pv)
print("   lambda' from total conservation:", sp.simplify(sp.solve(sp.Eq(cons, 0), sp.diff(lam, t))[0]), " (= -3 H g')")
fried = sp.Eq(3*H**2, rm + lam + rv)
accel = sp.Eq(-2*sp.diff(H, t) - 3*H**2, pm + pE + pv)
Hdot = sp.solve(accel.subs(3*H**2, rm + lam + rv), sp.diff(H, t))[0]
print("   -2 H' =", sp.simplify(-2*Hdot), " ; p_v appears:", sp.simplify(-2*Hdot).has(pv))
print("   Friedmann: 3H^2 = rho_m + (lambda + rho_v): geometry sees only Lt = lambda + rho_v and g'.")
e0 = rv + rrest
print("   (S): lambda_bare = -e0 = -(rho_v + rho_rest), rho_rest = the other ground-state energy (EW etc.) already in rho_tot;")
print("        Lt_late = lambda + rho_v + rho_rest(our vacuum) =", sp.simplify(-e0 + rv + rrest), " => exactly zero, any p_v.")

print("B2. No exchange (d-ii), metric GR, constant site-frame vacuum:")
Hs = sp.symbols('H', positive=True)
Q = 3*Hs*(rv + pv)                              # rho_v' + 3H(rho_v + p_v) with rho_v' = 0
print("   vacuum non-conservation rho_v' + 3H(rho+p)_v =", Q, " -> consistent only if (rho+p)_v = 0 (P70)")
print("   (S) residual (vacuum + counterterm Lambda_bare = -kappa rho_v): rho_res = 0, p_res =", sp.simplify(pv + rv))
print("   inhomogeneous Euler (R15-1, counted once): (rho+p)_v d ln N = 0 -> fails in every potential well unless (rho+p)_v = 0")

print("B3. Residual enthalpy from R11-3's table (C5_R11-3_report.md:135-141, counted once), per real scalar, m = 1:")
rhoL_over_Pl = None
for name, rho, rpp in [('L', 1.1938, 2.0683), ('G', 1.5567, 1.8492), ('NN', 1.3000, 1.3991)]:
    print("   %-2s: rho_v = %.4f, (rho+p)_v = %.4f, ratio = %.3f -> (S) leaves p_res = %.4f /a^4 ~ %.1e rho_Lambda at a = l_P"
          % (name, rho, rpp, rpp/rho, rpp, rpp*1.22089e19**4/2.520e-47))

print("C1. SM metastability under (S) (RECALLED inputs; order of magnitude; cutoff on the field range is a reading):")
rhoL = 2.520e-47; MP = 1.22089e19
for lam_min, hmax in [(-0.0037*4/1.0, 1e17), (-0.013, 1.22089e19)]:
    pass
for lam_eff, hmax, lab in [(-0.015, 1e17, 'lambda_min ~ -0.015 near 1e17 GeV'), (-0.013, MP, 'lambda(M_P) ~ -0.013 at h = M_P')]:
    V = lam_eff*hmax**4/4
    print("   %s: V ~ %.2e GeV^4 -> Lambda_late = kappa(V_EW - E0) >~ %.1e rho_Lambda" % (lab, V, -V/rhoL))
print("   instability scale (RECALLED): lambda < 0 above ~1e10-1e11 GeV at m_t ~ 172.6-173 GeV; stability needs m_t <~ 171 GeV")

print("C2. Three rules on a decay history (+ basin our vacuum V_p, true vacuum V_m < V_p, decay at t_d), homogeneous:")
Vp, Vm, td, kap = sp.symbols('V_p V_m t_d kappa', real=True)
th = sp.Heaviside(t - td)
Vlate = Vp + (Vm - Vp)*th                       # the vacuum the history is in
rules = {"(S) C = E0 = V_m": Vm + 0*t, "(S'-start) C = V_p": Vp + 0*t, "(S'-current) C = V(current basin)": Vlate}
for name, C in rules.items():
    Lt_before = sp.simplify(kap*(Vp - C.subs(t, td - 1)))
    Lt_after = sp.simplify(kap*(Vm - C.subs(t, td + 1)))
    g = sp.simplify(kap/3*sp.diff(C, t))      # Theorem Z: g = (kappa/3)(rho_tot - R)' = (kappa/3) C'
    print("   %-36s Lambda_before = %-16s Lambda_after = %-16s g = %s" % (name, Lt_before, Lt_after, g))

print("D1. Local covariant form G_mn = kappa (T_mn - C(x) g_mn), conserved T: Bianchi requires")
x0, x1, x2, x3 = sp.symbols('x0:4', real=True)
Cx = sp.Function('C')(x0, x1, x2, x3)
eta = sp.diag(-1, 1, 1, 1)
div = [sum(sp.diff(Cx*eta[m, n], [x0, x1, x2, x3][m])*eta[m, m] for m in range(4)) for n in range(4)]
print("   nabla^m (C g_mn) =", div, " (flat, Cartesian) -> must vanish -> C = constant.")
print("   So every local form of 'C tracks something' is either a constant (the law constant e0[H]) or needs a")
print("   non-conserved exchange sector (g != 0: R15-1 signalling).")
g_, k, Qb = sp.symbols('g k Qbar', real=True)
coef = (sp.Rational(3, 2)*g_)/(k**2 + Qb)
print("D2. R15-1 Lemma S remote response coefficient (3g/2)/(k^2/a^2 + Qbar) at g = 0:", coef.subs(g_, 0), "(ultralocal: GR)")
