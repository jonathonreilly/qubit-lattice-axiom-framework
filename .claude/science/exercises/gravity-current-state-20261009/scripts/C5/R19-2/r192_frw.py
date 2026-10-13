#!/usr/bin/env python3
"""R19-2 [C]: the homogeneous (k = 0) mode of an FRW version of Pi.
 [C1] symbolic: covariant lift B of R18-7's Pi (K^{mu nu} = nabla^mu V^nu + nabla^nu V^mu, the curved-space form of
      K = i(p^a D^b + p^b D^a)/p^2 - i p^a p^b (p.D)/p^4 = d^a V^b + d^b V^a) on spatially flat FRW, V = (V(t), 0, 0, 0).
 [C2] lift A (K pressureless in the cosmic frame, the k = 0 content of R18-7's Pi on Minkowski): exact solution
      rho_n(t) = -a^-3 int_{t0}^t p_tot d(a^3), checked against direct ODE integration on a LambdaCDM background.
 [C3] lift B on the same background, zero start: late-time rho_n = alpha rho_s + beta p_s; w today; de Sitter growing mode.
Background (comparator, RECALLED): H0 = 67.7 km/s/Mpc, Omega_m = 0.31, Omega_r = 9.1e-5, Omega_L = 0.69.
At O(G noise^2) the noise sector is computed on this fixed background (first iteration).
"""
import sympy as sp, numpy as np
from scipy import integrate
t = sp.Symbol('t'); A = sp.Function('A')(t); V = sp.Function('V')(t)
X = sp.symbols('x0:4')
g = sp.diag(-1, A**2, A**2, A**2); ginv = g.inv()
coords = [t, X[1], X[2], X[3]]
Gam = [[[sp.simplify(sum(ginv[l, s] * (sp.diff(g[s, m], coords[n]) + sp.diff(g[s, n], coords[m]) - sp.diff(g[m, n], coords[s]))
                         for s in range(4)) / 2) for n in range(4)] for m in range(4)] for l in range(4)]
Vu = [V, 0, 0, 0]
nabV = [[sp.simplify(sp.diff(Vu[n], coords[m]) + sum(Gam[n][m][l] * Vu[l] for l in range(4))) for n in range(4)] for m in range(4)]  # nabla_m V^n
up = [[sp.simplify(sum(ginv[m, s] * nabV[s][n] for s in range(4))) for n in range(4)] for m in range(4)]                          # nabla^m V^n
K = sp.Matrix(4, 4, lambda m, n: sp.simplify(up[m][n] + up[n][m]))
H = sp.diff(A, t) / A
print("[C1] lift B on FRW, V^mu = (V(t),0,0,0):")
print("     K^00 =", sp.simplify(K[0, 0]), " ;  K^i_j = K^{ij} g_{jj} =", sp.simplify(K[1, 1] * g[1, 1]), " ; off-diagonal zero:", all(K[m, n] == 0 for m in range(4) for n in range(4) if m != n))
rhoK = K[0, 0]; pK = sp.simplify(K[1, 1] * g[1, 1])
print("     => rho_K = -2 V',  p_K = 2 H V  (p_K = 0 only if H = 0: on Minkowski it reduces to R18-7's k = 0 content)")
divK0 = sp.simplify(sp.diff(K[0, 0], t) + sum(sp.diff(K[m, 0], coords[m]) for m in range(1, 4))
                    + sum(Gam[m][m][l] * K[l, 0] for m in range(4) for l in range(4)) + sum(Gam[0][m][l] * K[m, l] for m in range(4) for l in range(4)))
print("     nabla_mu K^{mu 0} =", sp.simplify(divK0), "  [should equal rho_K' + 3H(rho_K + p_K) = -2V'' - 6 H V' + 6 H^2 V]")
print("     check:", sp.simplify(divK0 - (sp.diff(rhoK, t) + 3 * H * (rhoK + pK))) == 0)

# ---------------- background ----------------
H0 = 67.7e3 / 3.0857e22; Om, Orad, OL = 0.31, 9.1e-5, 0.69
def Hz(a): return H0 * np.sqrt(Orad / a**4 + Om / a**3 + OL)
# integrate in N = ln a; d/dt = H d/dN
def run_liftA(a_on, ps=1.0, ramp=0.05):
    # switch-on profile s(N) over Delta N = ramp (ramp << 1 Hubble time, stands in for the gain time tau << 1/H)
    s = lambda N: 0.0 if N < np.log(a_on) else (1.0 if N > np.log(a_on) + ramp else 0.5 * (1 - np.cos(np.pi * (N - np.log(a_on)) / ramp)))
    f = lambda N, y: [-3 * (y[0] + ps * s(N))]          # d rho/dN = -3 (rho + p_tot), p_tot = p_s s(N) (p_K = 0)
    sol = integrate.solve_ivp(f, [np.log(a_on) - 0.01, 0.0], [0.0], rtol=1e-11, atol=1e-14, max_step=0.01)
    rho0 = sol.y[0, -1]
    return rho0, -ps * (1 - a_on**3)
print("\n[C2] lift A (p_K = 0): late-time rho_n in units of -p_s (exact solution 1 - (a_on/a)^3; ramp correction O(ramp))")
for a_on in [1e-9, 1e-3, 1 / 1101, 0.1, 0.5]:
    num, ex = run_liftA(a_on)
    print("     switch-on a = %.3g: numeric rho_n(today)/(-p_s) = %.9f ; exact %.9f ; w_n today = %.9f"
          % (a_on, num / (-1.0), ex / (-1.0), -1.0 / (1 - a_on**3)))
print("     remainder: rho_n + p_s = p_s (a_on/a)^3 (negative dust for p_s < 0); relative to matter it is constant = |p_s|/rho_m(a_on)")

print("\n[C3] lift B (covariant): -2V'' - 6HV' + 6H^2 V = -D_s, D_s = rho_s' + 3H(rho_s + p_s); rho_n = rho_s - 2V'; p_n = p_s + 2HV")
def run_liftB(a_on, rs, ps, Nend=0.0):
    # variables in N: V, dV/dt. With u = dV/dt: dV/dN = u/H ; du/dN = (1/H)(-3H u + 3H^2 V + D/2)  where D = 3H(rs+ps) after switch-on
    def f(N, y):
        a = np.exp(N); h = Hz(a); on = 1.0 if N >= np.log(a_on) else 0.0
        D = 3 * h * (rs + ps) * on
        V_, u = y
        return [u / h, (-3 * h * u + 3 * h * h * V_ + D / 2) / h]
    # switch-on: rho_s jumps at a_on; Lemma-P-type zero start of the total requires rho_K(a_on) = -rho_s, i.e. V'(t_on) = rho_s/2
    y0 = [0.0, rs / 2]
    sol = integrate.solve_ivp(f, [np.log(a_on), Nend], y0, rtol=1e-10, atol=1e-30, max_step=0.005, dense_output=True)
    V_, u = sol.y[:, -1]; h = Hz(np.exp(Nend))
    return rs - 2 * u, ps + 2 * h * V_
for a_on in [1e-3, 0.1]:
    r1, p1 = run_liftB(a_on, 1.0, 0.0); r2, p2 = run_liftB(a_on, 0.0, 1.0)
    print("     switch-on a = %.3g: rho_n(today) = %+.4f rho_s %+.4f p_s ; p_n(today) = %+.4f rho_s %+.4f p_s" % (a_on, r1, r2, p1, p2))
    for rs, ps, lab in ((4.0, -4.0 / 3, "complete-split IR content (rho_s, p_s) = (4, -4/3) U_IR"),):
        rr, pp = run_liftB(a_on, rs, ps)
        print("       %s: rho_n = %+.4f U_IR, w_n = %+.4f   [lift A gives rho_n = +1.3333 U_IR, w = -1]" % (lab, rr, pp / rr))
# de Sitter growing mode
lam = np.roots([1, 3, -3])
print("     pure de Sitter: homogeneous solutions V ~ exp(lambda H t), lambda = %s -> a growing mode exp(%.4f H t) is excited by a zero start" % (np.round(lam, 4), max(lam)))
# era-wise quasi-attractor for constant eps = -Hdot/H^2: rho_n = rho_s + (rho_s + p_s) eps/(1 - eps)
for eps_, lab in ((2.0, "radiation"), (1.5, "matter"), (0.0, "de Sitter")):
    print("     constant-eps tracker (%s, eps = %.1f): rho_n = rho_s + (rho_s + p_s) * %.3f" % (lab, eps_, eps_ / (1 - eps_)))
