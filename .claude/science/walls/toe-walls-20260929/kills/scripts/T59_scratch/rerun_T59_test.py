#!/usr/bin/env python3
"""T59 test: what does cosmic history actually have to supply?  (see PREREG.md)

Parts A,B: freeze-out yield, initial-state independence and expansion-history kernel
           (SUPPLIED Boltzmann model; not a lattice derivation).
Part C   : exact symbolic check of block 146's homogeneous model (H_rad gate).
Parts D,E,F: flat LCDM bookkeeping (counting numerology, fixed-lattice causal fill, age vs (H0,L)).
"""
import sys, json, math
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.special import kve
from scipy.optimize import brentq

OUT = {}
def log(*a):
    print(*a); sys.stdout.flush()

# ---------------------------------------------------------------- A, B
MPL = 1.220890e19          # GeV
M   = 3940.0               # GeV (16 v, repo's dark mass; used only as a scale)
G_DOF, GST = 2.0, 427.0/4.0
S0, RHOC_H2 = 2891.2, 1.05368e-5     # cm^-3, GeV cm^-3
COEF = math.log(45.0/(4*math.pi**4) * G_DOF/GST)

def lnYeq(x):
    return COEF + 2*np.log(x) + np.log(kve(2, x)) - x

def rhs_factory(lam, q, fun=None):
    def rhs(x, D):
        c = lam * x**(q-4.0)
        if fun is not None:
            c = c * fun(x)
        r = kve(1, x)/kve(2, x)
        Ye = math.exp(lnYeq(x))
        return [r - 2.0*c*Ye*math.sinh(D[0])]
    return rhs

def a_rate(lam, q, x):
    """local relaxation rate a = c(x) Yeq(x) of the deviation D = ln(Y/Yeq) (linear regime: dD/dx = -2 a D)."""
    return lam * x**(q-4.0) * math.exp(lnYeq(x))

def run(lam, q, xi, ratio, xmax=400.0, fun=None, dense=False):
    """ratio = Y_i/Yeq(x_i).  If the local relaxation rate a is so large that memory is erased within
    dx << x (a >= 1e6: exact Riccati solution u = tanh(a dx + atanh u0) is within e^-80 of 1 after
    dx = 40/a), start D-form integration at x1 = xi + 40/a with D = 0; otherwise integrate D directly."""
    ai = a_rate(lam, q, xi)
    if (ratio < 0.5 or ratio > 2.0) and ai >= 1e6:
        x1, D0 = xi + 40.0/ai, 0.0
    else:
        x1, D0 = xi, math.log(ratio)
    sol = solve_ivp(rhs_factory(lam, q, fun), (x1, xmax), [D0], method="Radau",
                    rtol=1e-9, atol=1e-11, dense_output=dense)
    if not sol.success:
        raise RuntimeError(sol.message)
    lnY = lnYeq(xmax) + sol.y[0, -1]
    return (lnY, sol) if dense else lnY

def omega_h2(lnY):
    return M*math.exp(lnY)*S0/RHOC_H2

# choose lam so Omega h^2 = 0.12 in the radiation baseline
def f(lnlam):
    return omega_h2(run(math.exp(lnlam), 2.0, 1.0, 1.0)) - 0.12
lnlam = brentq(f, math.log(1e11), math.log(1e17), xtol=1e-10)
LAM = math.exp(lnlam)
lnY0, sol0 = run(LAM, 2.0, 1.0, 1.0, dense=True)
# freeze-out point: first x with Y/Yeq = 2.5
xs = np.linspace(1.0, 400.0, 400000)
Dv = sol0.sol(xs)[0]
XF = float(xs[np.argmax(Dv >= math.log(2.5))])
log(f"lam = {LAM:.4e}  Omega h^2 = {omega_h2(lnY0):.5f}  x_F(Y=2.5Yeq) = {XF:.2f}  Y_inf = {math.exp(lnY0):.4e}")
OUT["lam"] = LAM; OUT["xF"] = XF; OUT["Yinf"] = math.exp(lnY0); OUT["Oh2"] = omega_h2(lnY0)

# ---- A: initial state independence
log("\n== A. initial-state independence (q=2)")
xis = [0.3, 0.5, 1.0, 2.0, 4.0, 8.0]
ratios = [1e-12, 1e-6, 1.0, 1e3]
grid = {}
for xi in xis:
    for r in ratios:
        grid[(xi, r)] = run(LAM, 2.0, xi, r)
vals = np.array(list(grid.values()))
spreadA = float(np.exp(vals.max()-lnY0) - 1.0), float(1.0 - np.exp(vals.min()-lnY0))
maxdev = float(np.max(np.abs(np.exp(vals-lnY0)-1.0)))
log(f"max |Y_inf/Y_base - 1| over {len(vals)} starts (x_i<=8): {maxdev:.3e}")
for xi in xis:
    row = "  x_i=%4.1f " % xi + " ".join((f"{np.exp(grid[(xi,r)]-lnY0):.6f}" if (xi,r) in grid else "   skipped") for r in ratios)
    log(row)
# control: late starts
ctrl = {}
for xi in [30.0, 60.0]:
    for r in [1e-12, 1.0, 1e3]:
        ctrl[(xi, r)] = float(np.exp(run(LAM, 2.0, xi, r)-lnY0))
log("control (late starts, Y_inf/Y_base):", {f"{k[0]:.0f},{k[1]:.0e}": round(v, 4) for k, v in ctrl.items()})
# how late can we start? scan x_i with worst-case ratios
thr = None
scan = []
for xi in [8, 10, 12, 14, 16, 18, 20, 22, 25, 27, 30]:
    devs = []
    for r in [1e-12, 1e-6, 1.0, 1e3]:
        try:
            devs.append(abs(np.exp(run(LAM, 2.0, float(xi), r)-lnY0)-1.0))
        except RuntimeError:
            pass      # extreme stiffness (ratio 1e-12 at x_i>=16): skipped, 1e-6 is reported
    scan.append((xi, max(devs)))
log("start-time scan: x_i -> worst-case |dY/Y|:", [(a, f"{b:.2e}") for a, b in scan])
OUT["A_maxdev_xi_le_8"] = maxdev
OUT["A_control"] = {f"{k[0]:.0f}_{k[1]:.0e}": v for k, v in ctrl.items()}
OUT["A_scan"] = scan
A_pass = maxdev <= 0.01
A_ctrl_ok = max(abs(v-1.0) for k, v in ctrl.items() if k[1] != 1.0) > 0.5
log(f"A verdict: spread<=1% -> {A_pass}; control shows real inequality -> {A_ctrl_ok}")

# ---- B1: kernel
log("\n== B1. response kernel K(ln x) = d ln Y_inf / d ln H(x)")
sig = 0.2
eps = 0.02
centres = np.exp(np.linspace(math.log(0.2), math.log(500.0), 48))
du = float(np.diff(np.log(centres)).mean())
def bump(xc):
    def w(x):
        u = math.log(x) - math.log(xc)
        return math.exp(-u*u/(2*sig*sig))/(sig*math.sqrt(2*math.pi))
    return w
K = []
for xc in centres:
    w = bump(xc)
    up = run(LAM, 2.0, 0.2, 1.0, fun=lambda x, w=w: 1.0/(1.0+eps*w(x)))
    dn = run(LAM, 2.0, 0.2, 1.0, fun=lambda x, w=w: 1.0/(1.0-eps*w(x)))
    K.append((up-dn)/(2*eps))
K = np.array(K)
base_lnY_02 = run(LAM, 2.0, 0.2, 1.0)
gup = run(LAM, 2.0, 0.2, 1.0, fun=lambda x: 1.0/(1.0+eps))
gdn = run(LAM, 2.0, 0.2, 1.0, fun=lambda x: 1.0/(1.0-eps))
Gresp = (gup-gdn)/(2*eps)
Kint = float(K.sum()*du)
absK = np.abs(K)
cum = np.cumsum(absK)/absK.sum()
u = np.log(centres)
def pct(p):
    return float(np.exp(np.interp(p, cum, u)))
x05, x50, x95 = pct(0.05), pct(0.50), pct(0.95)
outside = float(absK[(centres < 1.0) | (centres > 300.0)].sum()/absK.sum())
log(f"global response d lnY/d lnH = {Gresp:.4f}; integral of kernel = {Kint:.4f} (rel diff {abs(Kint/Gresp-1):.3e})")
log(f"5/50/95 % of |K| at x = {x05:.2f} / {x50:.2f} / {x95:.2f}; decades in x = {math.log10(x95/x05):.2f}; "
    f"time span (t~x^2) decades = {2*math.log10(x95/x05):.2f}; fraction of |K| outside [1,300] = {outside:.3f}")
neg = float(K[K < 0].sum()*du)
log(f"negative lobe integral = {neg:.4f}")
for xc, k in list(zip(centres, K))[::4]:
    log(f"   x={xc:8.2f}  K={k:9.5f}")
OUT["B1"] = dict(global_response=Gresp, kernel_integral=Kint, x05=x05, x50=x50, x95=x95,
                 decades_x=math.log10(x95/x05), frac_outside_1_300=outside, negative_lobe=neg)
B1_pass = (math.log10(x95/x05) <= 1.5) and (abs(Kint/Gresp-1) <= 0.05)
B1_fail = outside > 0.10
log(f"B1 verdict: window<=1.5 decades & integral ok -> {B1_pass}; >10% outside -> {B1_fail}")

# ---- B2: exponent scan
log("\n== B2. dependence on the expansion law H = H_m x^-q (same lam = same H at x=1)")
B2 = {}
for q in [0.0, 1.0, 1.5, 2.0, 2.5]:
    lnY = run(LAM, q, 1.0, 1.0)
    # xF for this q
    lnYq, solq = run(LAM, q, 1.0, 1.0, dense=True)
    Dq = solq.sol(xs)[0]
    xfq = float(xs[np.argmax(Dq >= math.log(2.5))])
    ana = (3-q)*xfq**(3-q)/LAM
    B2[q] = dict(Yinf=math.exp(lnY), ratio_to_q2=math.exp(lnY-lnY0), xF=xfq, analytic=ana,
                 num_over_ana=math.exp(lnY)/ana)
    log(f"  q={q:3.1f}  Y_inf={math.exp(lnY):.3e}  Y/Y(q=2)={math.exp(lnY-lnY0):10.3f}  xF={xfq:6.2f}  "
        f"analytic {(3-q)}*xF^{3-q}/lam = {ana:.3e}  num/ana={math.exp(lnY)/ana:.2f}")
OUT["B2"] = B2
B2_pass = B2[1.0]["ratio_to_q2"] >= 10.0
log(f"B2 verdict: Y(q=1)/Y(q=2) >= 10 -> {B2_pass}")

# ---------------------------------------------------------------- C symbolic
log("\n== C. block 146 homogeneous model, exact symbolic check")
import sympy as sp
t, t1, t0, eps_, al, Kc, s = sp.symbols("t t1 t0 epsilon alpha K s", positive=True)
Gn = 1/(16*sp.pi*Kc)
resC = {}

# (i) generic: acceleration eq + continuity => first integral
tt = sp.symbols("tt")
l = sp.Function("l")(tt); rho = sp.Function("rho")(tt); w = sp.symbols("w")
G = sp.symbols("G", positive=True)
H = sp.diff(l, tt)/l
p = w*rho
acc = sp.Eq(sp.diff(l, tt, 2)/l, -sp.Rational(4, 3)*sp.pi*G*(rho+3*p))
cont = sp.Eq(sp.diff(rho, tt), -3*H*(rho+p))
q1 = sp.diff(l, tt)**2 - sp.Rational(8, 3)*sp.pi*G*rho*l**2
dq1 = sp.diff(q1, tt)
dq1 = dq1.subs(sp.diff(rho, tt), sp.solve(cont, sp.diff(rho, tt))[0])
dq1 = dq1.subs(sp.diff(l, tt, 2), sp.solve(acc, sp.diff(l, tt, 2))[0])
resC["i_first_integral_residual"] = sp.simplify(dq1)
log("  (i) d/dt[ldot^2 - (8piG/3) rho l^2] on-shell =", resC["i_first_integral_residual"])

# (ii) block 146 branches
def check_branch(ell, mfun, name):
    lam_ = sp.log(ell)
    ld = sp.diff(lam_, t); ldd = sp.diff(lam_, t, 2)
    ck = -24*al
    m = mfun(lam_)
    cons = sp.simplify(m + ck*ell**3*ld**2)                       # m = -c_k l^3 ldot^2
    dm = sp.diff(mfun(sp.Symbol("L_")), sp.Symbol("L_")).subs(sp.Symbol("L_"), lam_)
    leq = sp.simplify(ck*ell**3*(2*ldd+3*ld**2) + dm)             # length equation
    rho_ = m/ell**3
    pr = -dm/(3*ell**3)                                           # m' = -3 p l^3
    acc_ = sp.simplify(sp.diff(ell, t, 2)/ell + (rho_+3*pr)/(48*al))
    # coefficient matching: residual of H^2 = (8 pi G/3) rho with G = 1/(16 pi K) (alpha kept symbolic;
    # t1 / t0 are substituted by the caller BEFORE alpha -> K/4, so the residual factors as (K-4 alpha))
    fried = ld**2 - sp.Rational(8, 3)*sp.pi*Gn*rho_
    return dict(constraint=cons, length_eq=leq, accel=acc_, friedmann_at_alpha_K4=fried,
                p_over_rho=sp.simplify(pr/rho_))
ell_r = (1+t/t1)**sp.Rational(1, 2)
r = check_branch(ell_r, lambda L: eps_*sp.exp(-L), "radiation")
r = {k: sp.simplify(v.subs(t1, sp.sqrt(6*al/eps_))) if k != "p_over_rho" else v for k, v in r.items()}
r["friedmann_general_alpha"] = r.pop("friedmann_at_alpha_K4")
r["friedmann_at_alpha_K4"] = sp.simplify(r["friedmann_general_alpha"].subs(al, Kc/4))
r["friedmann_zero_iff"] = sp.solve(sp.Eq(sp.numer(sp.together(r["friedmann_general_alpha"])), 0), Kc)
log("  (ii) massless/radiation branch residuals:", r)
resC["ii_rad"] = {k: str(v) for k, v in r.items()}
m0 = sp.symbols("m0", positive=True)
ell_m = (1+t/t0)**sp.Rational(2, 3)
mm = check_branch(ell_m, lambda L: m0 + 0*L, "matter")
mm = {k: sp.simplify(v.subs(t0, sp.Rational(4, 3)*sp.sqrt(6*al/m0))) if k != "p_over_rho" else v for k, v in mm.items()}
mm["friedmann_general_alpha"] = mm.pop("friedmann_at_alpha_K4")
mm["friedmann_at_alpha_K4"] = sp.simplify(mm["friedmann_general_alpha"].subs(al, Kc/4))
log("  (ii) rest-content/matter branch residuals:", mm)
resC["ii_matter"] = {k: str(v) for k, v in mm.items()}

# (iii) kinetic-prefactor exponent s: L = -24 alpha l^s ldot^2 - m ; density rho = m/l^s
# constraint: lamdot^2 = m l^-s /(24 alpha). power-law solutions l ~ t^p.
Lm = sp.symbols("L_", positive=True)
# radiation content m = eps/l: ldot^2/l^2 = eps l^(-1-s)/(24 al)  ->  ldot^2 ~ l^(1-s)  -> l ~ t^(2/(1+s))
# matter content m = m0: ldot^2/l^2 ~ l^-s -> ldot ~ l^(1-s/2) -> l ~ t^(2/s)
pr_rad = sp.simplify(2/(1+s)); pr_mat = sp.simplify(2/s)
def exponent_check(expo, coeff_pow):     # ldot^2 ~ l^(coeff_pow): l = t^p -> p^2 t^(2p-2) = t^(p*coeff_pow)
    p_ = sp.symbols("p_")
    sol = sp.solve(sp.Eq(2*p_-2, p_*coeff_pow), p_)
    return sol[0]
p_rad = sp.simplify(exponent_check(None, 1-s))
p_mat = sp.simplify(exponent_check(None, 2-s))
log("  (iii) exponent from constraint scaling: radiation p =", p_rad, " matter p =", p_mat,
    "; at s=3:", p_rad.subs(s, 3), p_mat.subs(s, 3),
    "; s=2:", p_rad.subs(s, 2), p_mat.subs(s, 2))
resC["iii"] = dict(rad=str(p_rad), mat=str(p_mat))
SKIP = ("p_over_rho", "friedmann_general_alpha", "friedmann_zero_iff")
C_pass = (resC["i_first_integral_residual"] == 0 and all(v == 0 for k, v in r.items() if k not in SKIP)
          and r["friedmann_zero_iff"] == [4*al]
          and r["p_over_rho"] == sp.Rational(1, 3)
          and all(v == 0 for k, v in mm.items() if k not in SKIP) and mm["p_over_rho"] == 0
          and p_rad.subs(s, 3) == sp.Rational(1, 2) and p_mat.subs(s, 3) == sp.Rational(2, 3)
          and p_rad.subs(s, 2) != sp.Rational(1, 2))
log("C verdict: all residuals zero and exponents as stated ->", C_pass)
OUT["C"] = resC; OUT["C_pass"] = bool(C_pass)

# ---------------------------------------------------------------- D, E, F
log("\n== E/D/F flat LCDM bookkeeping")
def Efun(a, Om, Or, OL): return math.sqrt(Or*a**-4 + Om*a**-3 + OL)
def Ht0(Om, Or, OL):
    return quad(lambda a: 1.0/(a*Efun(a, Om, Or, OL)), 0, 1, limit=400)[0]
def horizon(Om, Or, OL):
    return quad(lambda a: 1.0/(a*a*Efun(a, Om, Or, OL)), 0, 1, limit=400)[0]
Ee = {}
for H0 in [60.0, 67.4, 75.0]:
    for Om in [0.25, 0.315, 0.40]:
        Or = 4.18e-5/(H0/100.0)**2
        OL = 1-Om-Or
        Ee[(H0, Om)] = horizon(Om, Or, OL)/Ht0(Om, Or, OL)
log("E. particle horizon / (c t0):", {f"{k[0]},{k[1]}": round(v, 3) for k, v in Ee.items()})
E_min = min(Ee.values())
OUT["E"] = dict(min=E_min, max=max(Ee.values()))
E_pass = E_min >= 2.0
log(f"E verdict: min ratio {E_min:.3f} >= 2 -> {E_pass}; volume shortfall factor {E_min**3:.1f}+")

# D
Om, Or = 0.315, 9.2e-5; OL = 1-Om-Or
def V4u():
    def integrand(a):
        E = Efun(a, Om, Or, OL)
        chi = quad(lambda ap: 1.0/(ap*ap*Efun(ap, Om, Or, OL)), a, 1.0, limit=200)[0]
        return (4*math.pi/3)*(a*chi)**3 / (a*E)
    return quad(integrand, 1e-8, 1.0, limit=400)[0]
V4 = V4u()
Vsimple = (4*math.pi/3)*Ht0(Om, Or, OL)
prodD1 = 3*OL*math.sqrt(V4)
prodD2 = 3*OL*math.sqrt(Vsimple)
log(f"D. Lambda l_P^2 * sqrt(V4/l_P^4) = 3 OmegaL sqrt(V4u): past-cone {prodD1:.3f}; Hubble-volume x age {prodD2:.3f} "
    f"(independent of H0 by construction: circular with L ~ O(1))")
OUT["D"] = dict(past_cone=prodD1, hubble_vol_age=prodD2)
D_pass = all(abs(math.log10(v)) <= 1.5 for v in (prodD1, prodD2))
log(f"D verdict (order-of-magnitude, uninformative): {D_pass}")

# F
t0G = 13.8
F = {}
for L in [0.5, 0.6, 0.685, 0.75, 0.85]:
    Om_ = 1-L-9.2e-5
    F[L] = 977.8*Ht0(Om_, 9.2e-5, L)/t0G
log("F. H0 [km/s/Mpc] at fixed t0=13.8 Gyr vs L:", {k: round(v, 2) for k, v in F.items()})
Fspread = (max(F.values())-min(F.values()))/np.mean(list(F.values()))
OUT["F"] = dict(H0_by_L={str(k): v for k, v in F.items()}, spread=float(Fspread))
F_pass = Fspread > 0.10
log(f"F verdict: relative H0 spread {Fspread:.3f} > 0.10 -> {F_pass}")

# ---- G: K of the Kolb-Turner note is a function of T0, g*S(T0), H100, MPl only (repo P*)
hb = 1.973269804e-14   # GeV cm
T0 = 2.7255*8.617333e-14      # GeV
s0_GeV3 = (2*math.pi**2/45)*3.909*T0**3
H100 = 100.0/3.0856775814913673e19*6.582119569e-25   # 100 km/s/Mpc in GeV
rhoc_h2 = 3*H100**2*MPL**2/(8*math.pi)
Kkt = s0_GeV3*math.sqrt(45/math.pi)/rhoc_h2
log(f"\nG. K = s0 sqrt(45/pi)/(rho_c/h^2) from (T0, g*S, H100, MPl) = {Kkt:.4e} GeV^-1 (note quotes ~1.04e9; textbook 1.07e9)")
OUT["G_K"] = Kkt
# Omega h^2 scales as T0^3 at fixed everything else; Omega_DM/Omega_b does not depend on T0
OUT["G_scaling"] = "Omega h^2 ~ s0 ~ T0^3; Omega_DM/Omega_b = m_DM Y_DM/(m_p Y_B) has no T0, H0 or age"
G_pass = abs(Kkt/1.04e9-1) < 0.05
OUT["verdicts"] = dict(G_pass=bool(G_pass), A_pass=bool(A_pass), A_control_real=bool(A_ctrl_ok), B1_pass=bool(B1_pass), B1_fail=bool(B1_fail),
                       B2_pass=bool(B2_pass), C_pass=bool(C_pass), D_pass=bool(D_pass), E_pass=bool(E_pass), F_pass=bool(F_pass))
log("\nSUMMARY", json.dumps(OUT["verdicts"]))
with open(__file__.replace("T59_test.py", "T59_results.json"), "w") as fh:
    json.dump(OUT, fh, indent=1, default=str)
