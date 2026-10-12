"""R16-6 control: bag-model first-order transition with deep supercooling (homogeneous, kappa=1, u=ln a).
Content: radiation rho_r (all dof) + false-vacuum stress B*f(u) (w=-1) + true vacuum V_t (any constant).
f=1 until nucleation at T_n, then f -> 0 over width W in u; latent heat into radiation: rho_r' = -4 rho_r - B f'.
Readers (each sets the background H^2 = R/3; content evolution in u is reader independent):
  IE    : R(u0) = rho_eq(h0) (equilibrium start above T_c), then R' = -3h.          [this item]
  PEoS  : R = rho_eq(h), the equilibrium (single-valued) map incl. mixed-phase branch. [R15-6 P-EoS, literal]
  MR    : R15-6 running-minimum reader; with no dust here it returns (3/4)h = rho_r.   [R15-6]
Outputs: Lambda_late := R - (rho_tot - V_t) (relative to the LATE vacuum), g/H^2 = V'/R (Lemma I),
         integral of (g/H^2) R du = Delta V, e-folds of acceleration (R' > -2R).
"""
import numpy as np
from scipy.integrate import solve_ivp
af, at, B = 1.0, 0.3, 1.0
Tc4 = 3*B/(af-at)
hf_c, ht_c = 4/3*af*Tc4, 4/3*at*Tc4
def rho_eq(h):
    h = np.asarray(h, float)
    f = np.clip((h-ht_c)/(hf_c-ht_c), 0, 1)
    return 0.75*h + f*B
def run(Tn_over_Tc, W):
    T0_4 = 30*Tc4
    u0 = 0.0
    un = 0.25*np.log(T0_4/(Tn_over_Tc**4*Tc4))      # false-phase radiation a_f T^4 ∝ e^{-4u}
    x  = lambda u: np.clip((u-un)/W, -300, 300)
    f  = lambda u: 0.5*(1-np.tanh(x(u)))
    fp = lambda u: -0.5/W/np.cosh(x(u))**2
    u1 = un + 6.0
    # log variables keep relative precision: y0 = ln rho_r, y1 = ln R_IE
    def rhs(u, y):
        rr, RIE = np.exp(y[0]), np.exp(y[1])
        h = 4/3*rr
        return [-4 - B*fp(u)/rr, -3*h/RIE]
    rr0 = af*T0_4
    h0 = 4/3*rr0
    y0 = [np.log(rr0), np.log(rho_eq(h0))]
    us = np.linspace(u0, u1, 200001)
    sol = solve_ivp(rhs, (u0, u1), y0, t_eval=us, rtol=1e-12, atol=1e-14, method='DOP853', max_step=W/4)
    rr, RIE = np.exp(sol.y)
    h = 4/3*rr
    rho_nc_late = B*f(us) + rr          # content measured from the LATE (true) vacuum; V_t never enters a reader
    out = {}
    readers = {'IE': RIE, 'PEoS': rho_eq(h), 'MR': 0.75*h}
    ib = np.searchsorted(us, un-4*W)
    for name, R in readers.items():
        dlnR = np.gradient(np.log(R), us)
        if name == 'IE':
            dlnR = -3*h/R                  # exact ODE right-hand side
        gH2 = -3*h/R - dlnR                # = V'/R with V' = -3h - R'  (Lemma I); V_t-independent
        Lam = (R - rho_nc_late)/rho_nc_late
        acc = (dlnR > -2)
        nacc = acc.sum()*(us[1]-us[0])
        integ = np.trapezoid(gH2*R, us)
        out[name] = dict(min_gH2=gH2.min(), max_gH2=gH2.max(), Lam_late_end=Lam[-1],
                         Lam_before=Lam[ib], intg=integ, nacc=nacc, Dabs=(R[-1]-rho_nc_late[-1])/rho_nc_late[0])
    return out, un
print("bag model: a_f=1, a_t=0.3, B=1, T_c^4=%.4f; start T0^4 = 30 T_c^4 (equilibrium, false phase)" % Tc4)
print("every reader uses h only, so a constant true vacuum V_t of any size never enters R (shift invariance, Lemma B);")
print("NOTE: for IE the end value of Lam_late/rho_nc is ODE round-off: an absolute offset D is a constant, so D/rho_nc grows like e^{4u}.")
print("      The bracket gives D relative to the initial density (the integration-constant error). Analytically D = 0 (r166_identity.out:2).")
print("g/H^2 is computed from V' = -3h - R' and is V_t-independent.")
print("columns: reader | min g/H^2 | max g/H^2 | Lam_late/rho_nc at u_n-4W | Lam_late/rho_nc at end | int(g/H^2)R du (= Delta V; -B means the false vacuum was absorbed) | e-folds accelerating")
for Tn, W in [(0.9, 0.05), (0.5, 0.02), (0.3, 0.02), (0.1, 0.01), (0.1, 0.2)]:
    out, un = run(Tn, W)
    print("T_n/T_c=%.2f W=%.3f  (B/rho_r at nucleation = %.3g)" % (Tn, W, B/(af*Tn**4*Tc4)))
    for k, o in out.items():
        print("  %-5s %+.3e %+.3e  %+.3e  %+.3e  %+.5f  %.2f   [(R-rho_nc)/rho_nc(u0) at end = %+.2e]" % (k, o['min_gH2'], o['max_gH2'], o['Lam_before'], o['Lam_late_end'], o['intg'], o['nacc'], o['Dabs']))
