"""R15-6 step 2: the memory reader MR and its sign theorem on class H1; its failure modes outside H1.
Homogeneous, kappa = 1, u = ln a.  Observables the reader may use: h = -rho_tot'/3 and h' (vacuum-blind: they
annihilate any constant AND any w = -1 stress at every instant).
MR:  B(u) := 4h + h'  (= rho_m + (4/3) q_lat when content = radiation + dust and the latent heat q_lat >= 0 goes to radiation)
     m_hat(u) := min_{u' <= u} e^{3u'} B(u')            (running minimum: causal, one-sided)
     R := (3/4) h + (1/4) m_hat e^{-3u};   3H^2 = R;   g/H^2 = V'/R with V = rho_tot - R  (r156_identity).
Class H1: radiation (receives all latent heat) + conserved dust + a w = -1 vacuum rho_v(u) that is non-increasing,
          with a quiet start (q_lat ~ 0 at the first sample).  Claim (proved in report): on H1, R = rho_nc exactly,
          hence V = rho_v and g/H^2 = rho_v'/rho_nc <= 0 at every instant.
Outside H1 (tests): latent heat into dust; a species going non-relativistic (w: 1/3 -> 0); a vacuum rise (q_lat < 0).
Subtraction rule: eps = R/rho_nc - 1; Lt/rho_nc := (R - rho_nc)/rho_nc (= Lambda_tilde/(kappa rho_nc)); nothing else subtracted.
"""
import numpy as np
from scipy.integrate import solve_ivp
def tanh_step(u, uT, W):
    x = (u - uT)/W; t = np.tanh(x); s = (1 + t)/2; s1 = (1 - t**2)/(2*W); s2 = -2*t*s1/W
    return s, s1, s2
def run(label, D, W, uT=0.0, rv0=5.0, q0=1.0, m0=0.05, fdust=0.0, mass_thr=None, n=6001):
    """Content: radiation q, dust m, optional species X (w: 1/3 -> 0 at u = mass_thr[0] over width mass_thr[1],
    initial density mass_thr[2]), vacuum rho_v = rv0 - D s(u); latent heat D s' split (1-fdust) to q, fdust to m."""
    us = np.linspace(uT - 12*W - 2, uT + 12*W + 4, n)
    def wX(u):
        if mass_thr is None: return 0.0, 0.0
        um, Wm, _ = mass_thr; t = np.tanh((u - um)/Wm)
        return (1 - t)/6, -(1 - t**2)/(6*Wm)
    def rhs(u, y):
        q, m, X = y; s, s1, s2 = tanh_step(u, uT, W); w, _ = wX(u)
        return [-4*q + (1 - fdust)*D*s1, -3*m + fdust*D*s1, -3*(1 + w)*X]
    X0 = 0.0 if mass_thr is None else mass_thr[2]
    sol = solve_ivp(rhs, (us[0], us[-1]), [q0*np.exp(-4*us[0]), m0*np.exp(-3*us[0]), X0*np.exp(-4*us[0])],
                    t_eval=us, rtol=1e-12, atol=1e-18, method='DOP853')
    q, m, X = sol.y; s, s1, s2 = tanh_step(us, uT, W)
    w, w1 = np.array([wX(x)[0] for x in us]), np.array([wX(x)[1] for x in us])
    rv = rv0 - D*s; rnc = q + m + X; rtot = rnc + rv
    # exact analytic derivatives of the observables (no vacuum value enters):
    h = (4*q/3 + m + (1 + w)*X)                                         # (rho+p)_tot
    dq = -4*q + (1 - fdust)*D*s1; dm = -3*m + fdust*D*s1; dX = -3*(1 + w)*X
    hp = 4*dq/3 + dm + w1*X + (1 + w)*dX                                 # h'
    B = 4*h + hp
    mhat = np.minimum.accumulate(np.exp(3*us)*B)
    R = 0.75*h + 0.25*mhat*np.exp(-3*us)
    V = rtot - R
    gH2 = np.gradient(V, us)/R                                           # identity
    gor = -D*s1/rnc                                                      # oracle: rho_v'/rho_nc
    eps = R/rnc - 1
    alpha = D/np.interp(uT, us, rnc)
    print(f"[{label}] D={D} W={W} alpha=D/rho_nc(uT)={alpha:+.3g} fdust={fdust} mass_thr={mass_thr}")
    print(f"   max|eps| = {np.max(np.abs(eps)):.2e};  eps(end) = {eps[-1]:+.2e};  min R/rho_nc = {np.min(R/rnc):.4f}")
    print(f"   MR g/H^2 in [{gH2.min():+.3e}, {gH2.max():+.3e}];  oracle g/H^2 in [{gor.min():+.3e}, {gor.max():+.3e}];"
          f"  max|MR - oracle| = {np.max(np.abs(gH2 - gor)):.2e}")
    print(f"   Lt/rho_nc at end = {eps[-1]:+.3e};  Lt/rho_nc x e^{{3u}} trend (dust-like if const): "
          f"{eps[-1]*rnc[-1]*np.exp(3*us[-1]):+.3e} vs {eps[-200]*rnc[-200]*np.exp(3*us[-200]):+.3e}")
    # cumulative instantaneous-influence measure over the transition (oracle g, exact on H1):
    Qb = 4.5*h/rnc                                                      # Qbar/H^2 = (9/2)(rho+p)_nc/rho_nc
    I1 = np.trapezoid(np.abs(gor), us); I2 = np.trapezoid(1.5*np.abs(gor)/Qb, us)
    print(f"   int|g|/H^2 du = {I1:.3f} (alpha/(1+alpha) = {alpha/(1+alpha):.3f});  int (3/2)|g|/Qbar du (k->0 kick, cumulative) = {I2:.3f}")
    return us, gH2, eps
print("=== Class H1 (radiation + dust + non-increasing vacuum, latent heat to radiation) ===")
for D, W in [(0.01, 0.15), (0.05, 0.3), (0.3, 0.3), (0.7, 0.3), (0.01, 0.02), (0.3, 0.005), (5.0, 0.05), (50.0, 0.01)]:
    run("H1", D, W)
print("=== Outside H1 ===")
run("latent heat 30% to dust", 0.3, 0.05, fdust=0.3)
run("vacuum RISE (q_lat<0, NEC holds)", -0.3, 0.05)
run("species non-relativistic (no vacuum change)", 0.0, 0.3, mass_thr=(0.5, 0.3, 0.5))
run("species non-relativistic + drop", 0.3, 0.05, mass_thr=(0.5, 0.3, 0.5))
