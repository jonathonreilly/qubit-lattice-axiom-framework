"""R15-6 step 1: the reader identity  g/H^2 = (dV/du)/R,  V := rho_tot - R  (the reader's inferred vacuum),
homogeneous, kappa = 1, u = ln a.  Derivation: lam = 3H^2 - rho_tot = -(V) [since 3H^2 = R],  Lemma C: lam_dot = -3 H g
=> -V_dot = -3 H g => g = V_dot/(3H) => g/H^2 = (dV/du)/(3H^2) = V'/R.
Equivalent:  g/H^2 = -(R' + 3h)/R,  h := (rho+p)_tot = -rho_tot'/3 (vacuum-blind).
Check 1 (sympy): g = -2Hdot - (rho+p)_tot with 3H^2 = R and total conservation equals V_dot/(3H).
Check 2 (numerics): on R14-5's own step histories with R14-5's Prony-2 reader, compare R15-1's g (finite-difference
formula g = -2 H dH/du - (4q/3+m)) with V'/R; oracle reader g/H^2 = rho_v'/rho_nc.
"""
import numpy as np, sympy as sp
# ---- Check 1 (sympy)
u = sp.symbols('u'); R = sp.Function('R')(u); rt = sp.Function('rho_tot')(u)
H = sp.sqrt(R/3)
h = -sp.diff(rt, u)/3                       # (rho+p)_tot from total conservation: d rho/du = -3 h
Hdot = H*sp.diff(H, u)                      # dH/dt = H dH/du
g_formula = -2*Hdot - h                     # R14-5 / R15-1 homogeneous bookkeeping (kappa = 1)
V = rt - R
g_identity = H*sp.diff(V, u)/3/H**2*H**2    # g = V_dot/(3H) = H V'/(3H) = V'/3 ... in units: g = H^2 * V'/R
g_identity = sp.diff(V, u)/3                # since H^2 = R/3:  H^2 * V'/R = V'/3
print("Check 1: g_formula - V'/3 =", sp.simplify(g_formula - g_identity))
print("         i.e. g/H^2 = V'/R exactly (3H^2 = R).")
# ---- Check 2 (numerics), R14-5 history generator (copied logic of r145_homog.py)
from scipy.integrate import solve_ivp
def history(D, W, uT=0.0, rv0=5.0, q0=1.0, m0=0.05, n=4001):
    us_ = sp.symbols('us')
    s = (1 + sp.tanh((us_ - uT)/W))/2
    sd = [sp.lambdify(us_, sp.diff(s, us_, j), 'numpy') for j in range(0, 6)]
    us = np.linspace(uT - 12*W - 2, uT + 12*W + 3, n)
    sol = solve_ivp(lambda x, y: [-4*y[0] + D*sd[1](x)], (us[0], us[-1]), [q0*np.exp(-4*us[0])],
                    t_eval=us, rtol=1e-12, atol=1e-16, method='DOP853')
    q = sol.y[0]; m = m0*np.exp(-3*us); rv = rv0 - D*sd[0](us)
    def Dj(j):
        out = (-4.0)**j*q + (-3.0)**j*m
        acc = 0
        for i in range(j):
            acc = acc + (-4.0)**(j-1-i)*sd[i+1](us)
        return out + D*acc - D*(sd[j](us) if j > 0 else 0)
    return us, q, m, rv, Dj, sd
def prony2(Dj, us):
    mk = [None] + [(-1)**k*Dj(k) for k in range(1, 5)]
    rho_hat = np.empty_like(us)
    for i in range(len(us)):
        M = [mk[1][i], mk[2][i], mk[3][i], mk[4][i]]
        Hk = np.array([[M[0], M[1]], [M[1], M[2]]]); rhs = -np.array([M[2], M[3]])
        c0, c1 = np.linalg.solve(Hk, rhs); x = np.roots([1, c1, c0])
        V = np.vander(x, 2, increasing=True).T
        nu = np.linalg.solve(V.astype(complex), np.array(M[:2], dtype=complex))
        rho_hat[i] = np.real(np.sum(nu/x))
    return rho_hat
for D, W in [(0.01, 0.15), (0.05, 0.3), (0.3, 0.3), (0.7, 0.3), (0.01, 0.02)]:
    us, q, m, rv, Dj, sd = history(D, W)
    rnc = q + m; rtot = rnc + rv
    R = prony2(Dj, us)
    H2 = R/3; Hh = np.sqrt(np.clip(H2, 1e-300, None)); dHdu = np.gradient(Hh, us)
    g151 = -2*Hh*dHdu - (4*q/3 + m)                  # R15-1 formula
    Vr = rtot - R; gid = np.gradient(Vr, us)/3        # identity: g = V'/3  (kappa=1)
    ok = R > 0
    j0 = np.searchsorted(us, -6*W); j1 = np.searchsorted(us, 6*W)
    sel = ok.copy(); sel[:j0] = False; sel[j1:] = False
    # smooth samples: R>0 at the sample and both neighbours, |d ln R/du| < 50
    smooth = sel & np.r_[False, ok[:-2] & ok[2:], False] & (np.abs(np.gradient(R, us)/R) < 50)
    rr = np.abs(g151[smooth] - gid[smooth])/(np.abs(gid[smooth]) + 1e-3*np.abs(H2[smooth]))
    rel = np.median(rr); rel90 = np.percentile(rr, 90)
    gor = -D*sd[1](us)/rnc                            # oracle reader: g/H^2 = rho_v'/rho_nc
    print(f"D={D} W={W}: |g_R15-1 - V'/3|/|V'/3| on smooth step samples: median {rel:.1e}, 90th pct {rel90:.1e};"
          f"  Prony max g/H^2 = {np.max((gid/H2)[sel]):+.3e};  oracle g/H^2 in [{gor.min():+.3e}, {gor.max():+.1e}]")
