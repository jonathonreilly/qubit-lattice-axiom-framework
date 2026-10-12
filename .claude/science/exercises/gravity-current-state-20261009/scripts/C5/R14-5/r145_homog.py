"""R14-5 (b): homogeneous zero-mode-lapse model through a vacuum step (kappa = 1, u = ln a).
Content: radiation q(u), dust m(u) = m0 e^{-3u}, vacuum rho_v(u) = rv0 - D s(u), s = (1+tanh((u-uT)/W))/2,
latent heat into radiation: q' = -4 q + D s'(u)  (exact total conservation at the background level).
Zero-mode law (global P-T reader, Prony order 2 on the GLOBAL mean density, no memory X):
   moments m_k = (-d/du)^k rho_tot, k=1..4 (exact, analytic in s);  rho_hat = sum nu_i / x_i ;  3H^2 = rho_hat.
Bookkeeping (Lemma C, C3):  Lt := 3H^2 - rho_nc (= lam + rho_v, the only vacuum-dependent number entering
local physics);  lam = 3H^2 - rho_tot;  g = -2 dH/dt - (rho+p)_nc = -2 H dH/du - (4q/3 + m).
Control (unimodular, g == 0):  dH/dt = -(rho+p)_tot/2, i.e. H^2 - rho_tot/3 conserved -> Lemma PT.
Subtraction rule: 'leak' eps = rho_hat/rho_nc - 1 (nothing else subtracted); 'Lt/rho_nc' as defined.
Node reality is tested (R13-3 referee finding 5).
"""
import numpy as np, sympy as sp
uu = sp.symbols('u')
def run(D, W, uT=0.0, rv0=5.0, q0=1.0, m0=0.05, label=""):
    s = (1 + sp.tanh((uu - uT)/W))/2
    sd = [sp.lambdify(uu, sp.diff(s, uu, j), 'numpy') for j in range(0, 6)]
    us = np.linspace(uT - 12*W - 2, uT + 12*W + 3, 4001)
    # radiation by integrating q' = -4q + D s'
    from scipy.integrate import solve_ivp
    sol = solve_ivp(lambda u, y: [-4*y[0] + D*sd[1](u)], (us[0], us[-1]), [q0*np.exp(-4*us[0])],
                    t_eval=us, rtol=1e-12, atol=1e-16, method='DOP853')
    q = sol.y[0]; m = m0*np.exp(-3*us); rv = rv0 - D*sd[0](us)
    # derivatives D^j rho_tot
    def Dj(j):
        out = (-4.0)**j*q + (-3.0)**j*m
        acc = 0
        for i in range(j):
            acc = acc + (-4.0)**(j-1-i)*sd[i+1](us)
        out = out + D*acc - D*(sd[j](us) if j > 0 else 0)
        return out
    mk = [None] + [(-1)**k*Dj(k) for k in range(1, 5)]  # m_k = (-d/du)^k rho_tot
    rho_hat = np.empty_like(us); real_nodes = np.ones_like(us, dtype=bool); detn = np.empty_like(us)
    for i in range(len(us)):
        M = [mk[1][i], mk[2][i], mk[3][i], mk[4][i]]           # M_j = sum nu x^j, j=0..3
        Hk = np.array([[M[0], M[1]], [M[1], M[2]]]); rhs = -np.array([M[2], M[3]])
        detn[i] = np.linalg.det(Hk)/(M[0]*M[2])
        c0, c1 = np.linalg.solve(Hk, rhs)
        x = np.roots([1, c1, c0])
        if np.any(np.abs(np.imag(x)) > 1e-12*np.max(np.abs(x))): real_nodes[i] = False
        V = np.vander(x, 2, increasing=True).T                   # rows j=0,1
        nu = np.linalg.solve(V.astype(complex), np.array(M[:2], dtype=complex))
        rho_hat[i] = np.real(np.sum(nu/x))
    rnc = q + m
    eps = rho_hat/rnc - 1
    H2 = rho_hat/3; Lt = 3*H2 - rnc; lam = 3*H2 - (rnc + rv)
    H = np.sqrt(np.clip(H2, 1e-300, None)); dHdu = np.gradient(H, us)
    gfun = -2*H*dHdu - (4*q/3 + m)
    # unimodular control: H^2 - rho_tot/3 = C fixed by GR before the step (C=0 means Lambda_eff = rv0 before)
    # choose C so that Lambda_eff = 0 BEFORE the step (tuned to the initial vacuum): C = -rv0/3
    H2_U = (rnc + rv)/3 - rv0/3
    Leff_U = 3*H2_U - rnc
    i_late = np.searchsorted(us, uT + 10*W)
    i_end = -1
    print(f"[{label}] D={D} (alpha=D/q(uT)={D/np.interp(uT, us, q):.3g}) W={W}")
    print(f"   max|eps| = {np.max(np.abs(eps)):.3e} at u-uT = {us[np.argmax(np.abs(eps))]-uT:+.3f};  eps(uT+10W) = {eps[i_late]:+.3e};  eps(end) = {eps[i_end]:+.3e}")
    iT = np.searchsorted(us, uT)
    print(f"   eps(uT) = {eps[iT]:+.4e};  min normalised Hankel det = {np.min(np.abs(detn)):.2e} at u-uT = {us[np.argmin(np.abs(detn))]-uT:+.3f} (vs {np.abs(detn[0]):.2e} before)")
    print(f"   complex Prony nodes at {np.sum(~real_nodes)} of {len(us)} samples; min rho_hat/rho_nc = {np.min(rho_hat/rnc):+.4f}")
    print(f"   Lt/rho_nc: before = {Lt[0]/rnc[0]:+.3e}, at uT+10W = {Lt[i_late]/rnc[i_late]:+.3e}, end = {Lt[i_end]/rnc[i_end]:+.3e}")
    print(f"   lam + rho_v (=Lt): end = {lam[i_end] + rv[i_end]:+.3e};  lam end = {lam[i_end]:+.4f} vs -rho_v_final = {-(rv0-D):+.4f}")
    j0 = np.searchsorted(us, uT - 6*W); j1 = np.searchsorted(us, uT + 6*W)
    print(f"   g/H^2: before = {gfun[50]/H2[50]:+.3e}, peak in step = {np.max(np.abs(gfun[j0:j1]/H2[j0:j1])):.3e}, end = {gfun[-50]/H2[-50]:+.3e}")
    print(f"   CONTROL unimodular (g=0, tuned to initial vacuum): Leff/rho_nc end = {Leff_U[i_end]/rnc[i_end]:+.3e} (= D/rho_nc: {D/rnc[i_end]:+.3e})")
    return eps
for D, W in [(0.01, 0.15), (0.05, 0.3), (0.3, 0.3), (0.7, 0.3), (0.01, 0.02)]:
    run(D, W, label="step")
