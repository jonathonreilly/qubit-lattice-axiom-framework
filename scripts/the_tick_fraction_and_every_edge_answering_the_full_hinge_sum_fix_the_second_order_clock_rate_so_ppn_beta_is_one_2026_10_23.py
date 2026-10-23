AUDIT_INPUT_PATHS = ('docs/THE_TICK_FRACTION_AND_EVERY_EDGE_ANSWERING_THE_FULL_HINGE_SUM_FIX_THE_SECOND_ORDER_CLOCK_RATE_SO_PPN_BETA_IS_ONE_BOUNDED_THEOREM_NOTE_2026-10-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Tick-fraction beta: second-order static field of the tick-fraction rule.
Static hinge sum S/dt = (1/8 pi G) sum_e N_e l_e delta_e -> (1/16 pi G) int N sqrt(h) R3
(Regge: sum l delta -> (1/2) int sqrt(h) R3), kept EXACT (no quadratic truncation).
Spherical static fields: site tick fraction N(r); spatial edges h = a^2 dr^2 + b^2 r^2 dOmega^2.
Self-contained; seeded; numpy + scipy + sympy only."""
AUDIT_TIMEOUT_SEC = 120
import time
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

np.random.seed(20261023)
T0 = time.time()
P = F = 0
def check(name, ok, info=""):
    global P, F
    if ok: P += 1
    else: F += 1
    print(("PASS" if ok else "FAIL") + f": {name}" + (f"  [{info}]" if info else ""))

# ---------- A. exact reduced hinge sum, spherical ----------
r, th, ph = sp.symbols('r theta phi', positive=True)
X = (r, th, ph)
N = sp.Function('N')(r); a = sp.Function('a')(r); b = sp.Function('b')(r)
def ricci_scalar_3(g):
    gi = sp.simplify(g.inv()); n = 3
    G = [[[sp.simplify(sum(gi[i, d]*(sp.diff(g[d, j], X[k]) + sp.diff(g[d, k], X[j]) - sp.diff(g[j, k], X[d]))
               for d in range(n))/2) for k in range(n)] for j in range(n)] for i in range(n)]
    R = 0
    for j in range(n):
        for k in range(n):
            Rjk = sum(sp.diff(G[i][j][k], X[i]) - sp.diff(G[i][j][i], X[k]) +
                      sum(G[i][i][d]*G[d][j][k] - G[i][k][d]*G[d][j][i] for d in range(n))
                      for i in range(n))
            R += gi[j, k]*Rjk
    return sp.simplify(R)
h = sp.diag(a**2, b**2*r**2, b**2*r**2*sp.sin(th)**2)
R3 = ricci_scalar_3(h)
L = sp.simplify(N*a*b**2*r**2*R3)          # sqrt(h)/sin(theta) * N * R3
from sympy.calculus.euler import euler_equations
EL = euler_equations(L, [N, a, b], r)
EN, Ea, Eb = [e.lhs for e in EL]
# A1 Schwarzschild (isotropic) satisfies every response equation (tick fraction + all edges)
M, A, C, m = sp.symbols('M A C m', positive=True)
sch = {N: (1 - M/(2*r))/(1 + M/(2*r)), a: (1 + M/(2*r))**2, b: (1 + M/(2*r))**2}
res = [sp.simplify(E.subs(sch).doit()) for E in (EN, Ea, Eb)]
check("A1 exterior: N=(1-M/2r)/(1+M/2r), a=b=(1+M/2r)^2 solves tick + radial-edge + tangential-edge equations",
      all(x == 0 for x in res))
# A2 conformal family phi = 1 + A/r, N = 1 - C/(r+A): tick eq + trace hold for all A,C; anisotropic edge eq needs C=2A
fam = {N: 1 - C/(r + A), a: (1 + A/r)**2, b: (1 + A/r)**2}
eN = sp.simplify(EN.subs(fam).doit()); ea = sp.simplify(Ea.subs(fam).doit()); eb = sp.simplify(Eb.subs(fam).doit())
# trace direction: delta a = delta b = delta(phi^2) -> E_a + E_b
etr = sp.simplify(ea + eb)
check("A2 conformal family: tick eq and density (trace) eq hold for ANY A, C", eN == 0 and etr == 0,
      f"E_N={eN}, E_a+E_b={etr}")
ean = sp.factor(sp.simplify(ea))
check("A3 radial-edge (anisotropic) equation forces C = 2A", sp.simplify(ean.subs(C, 2*A)) == 0 and ean != 0,
      f"E_a = {ean}")
# A4 uniqueness: areal gauge b r = R(r) = r, a free. Tick eq -> a = (1-2m/r)^(-1/2); edge eq -> N = c sqrt(1-2m/r)
Ra = sp.Function('A_')(r)
ar = {a: 1/sp.sqrt(1 - 2*m/r), b: sp.Integer(1)}
eNa = sp.simplify(EN.subs(ar).doit())
check("A4 areal gauge: tick eq (Hamiltonian constraint) solved by a = (1-2m/r)^(-1/2)", eNa == 0)
# general solution of the tick eq: E_N is 1st order in a: (r(1 - 1/a^2))' = 0
eNg = sp.simplify(EN.subs(b, 1).doit())
q = sp.simplify(sp.diff(r*(1 - 1/a**2), r))
check("A5 tick eq in areal gauge = 2a (r(1-1/a^2))': one integration constant m, no source outside",
      sp.simplify(eNg - 2*a*q) == 0, "E_N = 2a d/dr[r(1-1/a^2)]")
eAa = sp.simplify(Ea.subs(ar).doit())
sol = sp.dsolve(sp.Eq(sp.numer(sp.together(eAa)), 0), N)
Nsol = sol.rhs
ok5 = sp.simplify(Nsol/sp.sqrt(1 - 2*m/r)).free_symbols <= {sp.Symbol('C1')}
check("A6 radial-edge eq then gives N = C1 sqrt(1-2m/r): one-parameter exterior (Birkhoff) for ANY source",
      ok5, f"N = {Nsol}")
eBa = sp.simplify(Eb.subs(ar).subs(N, sp.sqrt(1 - 2*m/r)).doit())
check("A7 tangential-edge eq holds identically on that solution (no extra condition)", eBa == 0)
# A8 PPN readout: isotropic radius rho, r = rho (1 + m/2rho)^2 ; U = m/rho (m = Kepler mass from g00)
rho, u = sp.symbols('rho u', positive=True)
g00 = sp.simplify(((1 - m/(2*rho))/(1 + m/(2*rho)))**2)
gss = sp.simplify((1 + m/(2*rho))**4)
r_of = rho*(1 + m/(2*rho))**2
check("A8 areal and isotropic forms agree: 1-2m/r(rho) = N_iso^2", sp.simplify(1 - 2*m/r_of - g00) == 0)
s00 = sp.series(g00.subs(m, u*rho), u, 0, 3).removeO()
sss = sp.series(gss.subs(m, u*rho), u, 0, 2).removeO()
beta = sp.simplify(s00.coeff(u, 2)/2); gamma = sp.simplify(sss.coeff(u, 1)/2)
check("A9 g00 = -(1 - 2U + 2 beta U^2), g_ij = (1 + 2 gamma U) delta_ij  ->  beta = 1, gamma = 1 (forced)",
      beta == 1 and gamma == 1 and s00.coeff(u, 1) == -2, f"beta={beta}, gamma={gamma}")

# ---------- B. option table (rule-internal choices) ----------
# B1 conformal family readout: beta = 1/2 + A/C, gamma = 2A/C  -> beta - 1 = (gamma - 1)/2
Nf = 1 - C/(rho + A); phif = 1 + A/rho
s = sp.series((Nf**2).subs({A: sp.Symbol('k')*C}).subs(C, u*rho), u, 0, 3).removeO()
k = sp.Symbol('k')
bf = sp.simplify(s.coeff(u, 2)/2); gf = sp.simplify(sp.series((phif**4).subs(A, k*u*rho), u, 0, 2).removeO().coeff(u, 1)/2)
check("B1 density-only response (edges locked conformal): beta = 1/2 + A/C, gamma = 2A/C, beta-1 = (gamma-1)/2",
      sp.simplify(bf - (sp.Rational(1, 2) + k)) == 0 and sp.simplify(gf - 2*k) == 0)
# B2 quadratic truncation (linear field eqs) is parameterisation-dependent
U = sp.Symbol('U')
opts = {'N = 1+Phi': 1 - U, 'N = exp(Phi)': sp.exp(-U), 'N = 1/(1-Phi)': 1/(1 + U),
        'N^2 = 1+2Phi': sp.sqrt(1 - 2*U)}
bt = {kk: sp.series(v**2, U, 0, 3).removeO().coeff(U, 2)/2 for kk, v in opts.items()}
check("B2 quadratic truncation of the hinge sum leaves beta undetermined (field-variable choice)",
      len(set(bt.values())) > 1, ", ".join(f"{kk}: beta={vv}" for kk, vv in bt.items()))
# B3 source coupling: exterior is the A6 one-parameter family for any coupling -m N f(Omega), f arbitrary
print("INFO B3 source coupling (-mN, -mN Omega^k, -mN^2, ...) enters only the constant m (Kepler mass); A4-A7 use exterior eqs only, so beta is coupling-independent")
# B4 density-only response, uniform ball (G=1, R=1): gamma_ext = int rho/phi / int rho N  (body-dependent)
def ball(GM):
    rho0 = 3*GM/(4*np.pi)
    src = lambda x: rho0 if x < 1 else 0.0
    def fphi(x, y):           # phi'' + 2phi'/x = -2 pi rho/phi
        return [y[1], -2*np.pi*src(x)/y[0] - 2*y[1]/x]
    def miss(p0):
        x0 = 1e-6; s0 = solve_ivp(fphi, [x0, 1.0], [p0, 0.0], rtol=1e-12, atol=1e-14)
        return s0.y[0, -1] + s0.y[1, -1] - 1.0     # exterior phi = 1 + A/x
    p0 = brentq(miss, 1.0, 1.0 + 10*GM, xtol=1e-15)
    def fall(x, y):           # y = phi, phi', N, J=x^2 phi^2 N'
        ph_, dph, Nn, J = y
        return [dph, -2*np.pi*src(x)/ph_ - 2*dph/x, J/(x*x*ph_*ph_), 4*np.pi*src(x)*Nn*x*x]
    x0 = 1e-6; S = solve_ivp(fall, [x0, 1.0], [p0, 0.0, 1.0, 0.0], rtol=1e-12, atol=1e-15)
    phR, dphR, NR, J = S.y[:, -1]
    Aext = -dphR                         # phi = 1 + A/x at x = 1
    # exterior N = Ninf - J/(x + A)   (x^2 phi^2 N' = J)
    Ninf = NR + J/(1 + Aext)
    Cext = J/Ninf
    return 2*Aext/Cext
for GM in (1e-3, 1e-2):
    gx = ball(GM); bx = 0.5 + gx/2
    check(f"B4 density-only, ball GM/R={GM:g}: gamma-1 ~ +0.6 GM/R, beta-1 ~ +0.3 GM/R (body-dependent)",
          abs((gx - 1)/(0.6*GM) - 1) < 0.05, f"gamma-1={gx-1:.4e}, beta-1={bx-1:.4e}")
print("INFO Sun GM/R = 2.12e-6: density-only option would give beta-1 ~ 6.4e-7, gamma-1 ~ 1.3e-6 (but violates the edge eqs)")

# ---------- C. measured comparator (test only) ----------
check("C1 full rule: |beta - 1| = 0 < 1e-4 (perihelion / lunar ranging)", abs(float(beta) - 1) < 1e-4)
check("C2 Nordtvedt eta = 4beta - gamma - 3 = 0 for the full rule (no body dependence)",
      4*beta - gamma - 3 == 0)
print(f"elapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={P} FAIL={F}")
