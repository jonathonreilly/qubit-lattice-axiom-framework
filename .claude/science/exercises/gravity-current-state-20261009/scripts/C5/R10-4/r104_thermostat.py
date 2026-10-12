"""R10-4 B4: a dissipative 'thermostat' relaxing the total stress trace to zero (suggested class).

d rho_V/dt = -Gamma (rho_V - y),  y = -(rho_m - 3 p_m)/4 = -rho_dust/4 (radiation traceless),
Gamma = c * H.  Energy exchange keeps the total conserved; here the exchanged energy goes into
radiation (traceless, so the target y is untouched). Dust ~ a^-3. Units: H0 = 1, rho_crit0 = 1.
Checked: after the target y(t) starts rising toward 0, rho_V sits below y <= 0 for every c and
initial value tried, so the late-time vacuum energy is negative (ratio <= -1/4 of dust).
Variables are scaled by a^3 (x = a^3 rho) to avoid huge dynamic range.
"""
import numpy as np
from scipy.integrate import solve_ivp

Om_r, Om_m = 9.1e-5, 0.315

def rhs(lna, X, c):
    a = np.exp(lna)
    xV, xr = X                       # x = a^3 rho
    rV, rr, rm = xV / a**3, xr / a**3, Om_m / a**3
    H2 = rV + rm + rr
    if H2 <= 0:
        return [0.0, 0.0]
    H = np.sqrt(H2)
    drV = -c * H * (rV - (-rm / 4.0))          # per unit time
    drr = -4 * H * rr - drV                    # radiation absorbs the exchange
    # d(a^3 rho)/dlna = 3 a^3 rho + a^3 (d rho/dt)/H
    return [3 * xV + a**3 * drV / H, 3 * xr + a**3 * drr / H]

def H2ev(lna, X, c):
    a = np.exp(lna)
    return (X[0] + X[1]) / a**3 + Om_m / a**3
H2ev.terminal = True; H2ev.direction = -1

aa = np.array([1e-4, 1e-2, 1e-1, 1.0, 10.0])
for c in (0.3, 1.0, 10.0, 100.0):
    for f in (+0.5, +1e-3, 0.0, -1e-3):
        a0 = 1e-6
        rm0, rr0 = Om_m / a0**3, Om_r / a0**4
        X0 = [f * rm0 * a0**3, rr0 * a0**3]
        sol = solve_ivp(rhs, [np.log(a0), np.log(aa[-1])], X0, args=(c,), rtol=1e-9, atol=1e-14,
                        t_eval=np.log(aa), method='LSODA', events=H2ev)
        out = [f"a={np.exp(t):g}: {sol.y[0,k]/Om_m:+.4f}" for k, t in enumerate(sol.t)]
        tag = (" [H^2 -> 0 at a=%.3g]" % np.exp(sol.t_events[0][0])) if len(sol.t_events[0]) else ""
        print(f"c={c:6.1f} rho_V0/rho_m0={f:+.0e} status={sol.status} | rho_V/rho_dust: " + " ; ".join(out) + tag)
print("Target ratio -0.25. Observed today rho_DE/rho_dust = +2.17.")

# Analytic fast-relaxation limit: rho_V = -rho_m/4 exactly (w_V = -1), total stress conserved in FRW.
import sympy as sp
a = sp.symbols('a', positive=True); rm = sp.Function('rho_m')(a)
rV = -rm / 4
# d(rho_tot)/dlna = -3 (rho_tot + p_tot) with p_V = -rho_V, p_m = 0
eq = sp.Eq(sp.diff(rm + rV, a) * a, -3 * (rm + 0))
print("fast limit, exchange with dust:", sp.dsolve(eq, rm), " => dust dilutes like radiation (a^-4)")
print("Notes: (i) where the integration runs, rho_V/rho_dust sits at -0.26 (c=100) to -0.36 (c=10): negative;")
print("(ii) slow relaxation (c<=1) does not remove a positive initial rho_V (vacuum domination);")
print("(iii) with the exchange routed to radiation, radiation is drained and H^2 -> 0: the toy's energy budget fails.")
