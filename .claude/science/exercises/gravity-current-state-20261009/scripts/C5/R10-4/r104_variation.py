"""R10-4 symbolic checks.

S1. 4-form record density: metric variation at fixed record count gives
    T_vac = -(eps - q eps') g  (Gibbs-Duhem form), in FRW minisuperspace
    and for a generic 4x4 metric (Jacobi formula, numeric finite difference).
S2. Varying the accumulated count A (the 3-form potential) gives eps'(q) = mu = const.
S3. Phase transition at fixed mu: rho_V shifts by Delta exactly for a q-independent shift;
    for a q-dependent kick, rho_V(mu) = -P(mu) changes by P_old(mu)-P_new(mu); d rho_V/d mu = -q.
S4. 3-form (conserved current) records: fluid with rho = eps(n), p = n eps' - eps;
    Lorentz-invariant vacuum needs n eps'(n) = 0, so rho_vac = eps at a stationary point
    or eps(0); FRW dilution n ~ a^-3 drives rho -> eps(0).
"""
import sympy as sp
import numpy as np

print("=== S1: FRW minisuperspace, records fixed under metric variation ===")
t = sp.symbols('t', real=True)
N = sp.Function('N', positive=True)(t)
a = sp.Function('a', positive=True)(t)
A = sp.Function('A')(t)          # accumulated record count per comoving coordinate 3-cell
eps = sp.Function('eps')
q = sp.diff(A, t) / (N * a**3)   # formation events per proper 4-volume
L = -N * a**3 * eps(q)           # vacuum Lagrangian sqrt(-g) * (-eps)
# energy density rho = -(1/a^3) dL/dN  (Hamiltonian constraint convention for a matter Lagrangian)
dLdN = sp.diff(L, N)
rho = sp.simplify(-dLdN / a**3)
Q = sp.symbols('q', positive=True)
rho_q = sp.simplify(rho.subs(sp.diff(A, t), Q * N * a**3))
print("rho =", rho_q)
# pressure p = (1/(3 N a^2)) dL/da
dLda = sp.diff(L, a)
p = sp.simplify(dLda / (3 * N * a**2))
p_q = sp.simplify(p.subs(sp.diff(A, t), Q * N * a**3))
print("p   =", p_q)
print("rho + p =", sp.simplify(rho_q + p_q), "(vacuum equation of state p = -rho)")
epsq = eps(Q)
target = epsq - Q * sp.diff(epsq, Q)
print("rho - (eps - q eps') =", sp.simplify(rho_q - target))

print("\n=== S2: vary the accumulated count A ===")
pA = sp.diff(L, sp.diff(A, t))
pA_q = sp.simplify(pA.subs(sp.diff(A, t), Q * N * a**3))
print("dL/dA_dot =", pA_q, " ; Euler-Lagrange: d/dt(dL/dA_dot) = 0  =>  eps'(q) = mu, a constant")

print("\n=== S1b: generic metric, numeric Jacobi-formula check ===")
rng = np.random.default_rng(1)
M = rng.normal(size=(4, 4)); M = M + M.T
g0 = np.diag([-1.0, 1.0, 1.0, 1.0]) + 0.1 * M
def sqrtg(g): return np.sqrt(-np.linalg.det(g))
c = 2.7  # metric-independent count per coordinate 4-cell
def epsf(x): return 0.3 + np.sin(x) + 0.2 * x**3   # arbitrary smooth eps(q)
def depsf(x): return np.cos(x) + 0.6 * x**2
def S(g): return -sqrtg(g) * epsf(c / sqrtg(g))
h = 1e-6
dS = np.zeros((4, 4))
for i in range(4):
    for j in range(4):
        E = np.zeros((4, 4)); E[i, j] += 0.5; E[j, i] += 0.5
        dS[i, j] = (S(g0 + h * E) - S(g0 - h * E)) / (2 * h)
qv = c / sqrtg(g0)
ginv = np.linalg.inv(g0)
# Expected: dS/dg_{mu nu} = -(1/2) sqrt(-g) (eps - q eps') g^{mu nu}
pred = -0.5 * sqrtg(g0) * (epsf(qv) - qv * depsf(qv)) * ginv
print("max |dS/dg - pred| =", np.max(np.abs(dS - pred)), " (scale", np.max(np.abs(pred)), ")")
# Compare: if q were an independent scalar (records varied freely / not fixed counts):
pred_free = -0.5 * sqrtg(g0) * epsf(qv) * ginv
print("max |dS/dg - pred_if_q_metric_independent| =", np.max(np.abs(dS - pred_free)))

print("\n=== S3: phase transitions at fixed mu ===")
mu, Lb, D, k = sp.symbols('mu Lambda_b Delta k', real=True)
qq = sp.symbols('q', positive=True)
# Example eps(q): Maxwell-type four-form plus quartic, KV-like: eps = Lb - q^2/2 + k q^4/4
eps_ex = Lb - qq**2 / 2 + k * qq**4 / 4
rhoV = sp.simplify(eps_ex - qq * sp.diff(eps_ex, qq))
print("eps(q) =", eps_ex, " ; rho_V(q) = eps - q eps' =", rhoV)
print("compressibility^-1 = q^2 eps'' =", sp.simplify(qq**2 * sp.diff(eps_ex, qq, 2)))
# Legendre: d rho_V/d mu = -q along eps'(q)=mu
qs = sp.symbols('q_s', positive=True)
drho_dq = sp.diff(rhoV, qq)
dmu_dq = sp.diff(sp.diff(eps_ex, qq), qq)
print("d rho_V / d mu = (d rho_V/dq)/(d mu/dq) =", sp.simplify(drho_dq / dmu_dq))
# q-independent shift Lb -> Lb + D at fixed mu: q unchanged (eps' unchanged), rho_V -> rho_V + D
print("q-independent shift: eps' unchanged =>", sp.simplify(sp.diff(eps_ex + D, qq) - sp.diff(eps_ex, qq)) == 0,
      "; rho_V shift =", sp.simplify((eps_ex + D - qq * sp.diff(eps_ex + D, qq)) - rhoV))
# Equilibrium zero: rho_V(q0)=0 fixes q0 and mu0 = eps'(q0); mu0 depends on Lb
sol = sp.solve(sp.Eq(rhoV, 0), qq)
print("rho_V(q0)=0 roots:", sol)
# take the root with Lb<0 handled generally: use implicit differentiation instead of a closed form
q0s = sp.symbols('q0', positive=True)
# along the family rho_V(q0; Lb) = 0, mu0 = eps'(q0): d mu0/d Lb = eps''(q0) * dq0/dLb, dq0/dLb = -(d rhoV/dLb)/(d rhoV/dq)
drho_dLb = sp.diff(rhoV, Lb)
dq0_dLb = -drho_dLb / sp.diff(rhoV, qq)
dmu0_dLb = sp.simplify(sp.diff(eps_ex, qq, 2) * dq0_dLb)
print("d mu0 / d Lambda_b along rho_V(q0)=0 :", dmu0_dLb, " (= 1/q0: a shift Delta in Lambda_b needs delta mu = Delta/q0)")
# numeric example: k=1, Lb=-0.1
num = {k: 1, Lb: sp.Rational(1, 20)}
roots = [r for r in sp.solve(sp.Eq(rhoV.subs(num), 0), qq) if r.is_real and r > 0]
print("example k=1, Lb=+0.05: equilibrium q0 =", [sp.N(r, 8) for r in roots],
      "; mu0 =", [sp.N(sp.diff(eps_ex, qq).subs(num).subs(qq, r), 8) for r in roots],
      "; chi^-1 =", [sp.N((qq**2*sp.diff(eps_ex, qq, 2)).subs(num).subs(qq, r), 8) for r in roots])
print("Interpretation: the zero needs mu = mu0(final Lb); a later shift Lb->Lb+Delta needs delta mu = +Delta/q0 at first order,")
print("which a conserved mu cannot supply. Tuning precision on mu: rho_Lambda/(q0*|delta mu| scale) = rho_Lambda/Delta.")

# q-dependent kick: eps -> eps + Delta * (q/qs)^2 ; at fixed mu q moves; rho_V change = P_old(mu)-P_new(mu)
eps_new = eps_ex + D * (qq / qs)**2
rho_new = sp.simplify(eps_new - qq * sp.diff(eps_new, qq))
print("q-dependent kick Delta*(q/qs)^2: rho_V_new(q) - rho_V_old(q) =", sp.simplify(rho_new - rhoV),
      " (a term quadratic in q is not removed by the Legendre map; only terms LINEAR in q drop out)")
eps_lin = eps_ex + D * qq / qs
print("linear kick Delta*q/qs: rho_V change =", sp.simplify((eps_lin - qq*sp.diff(eps_lin, qq)) - rhoV),
      "; but eps' shifts by Delta/qs, so at fixed mu q must move:  eps'_new(q') = mu")

print("\n=== S4: conserved 3-form current (records as conserved number current) ===")
n = sp.symbols('n', positive=True)
f = sp.Function('f')
eps_n = Lb + f(n)
rho_f = eps_n
p_f = n * sp.diff(eps_n, n) - eps_n
print("fluid: rho =", rho_f, "; p =", sp.simplify(p_f), "; rho + p =", sp.simplify(rho_f + p_f))
print("Lorentz-invariant vacuum (T ~ g) needs rho + p = n f'(n) = 0 => n = 0 or f'(n)=0;")
print("then rho_vac = Lb + f(n_*) at a stationary point or Lb + f(0): no zero condition.")
# FRW: conserved comoving count => n = n_i (a_i/a)^3 -> 0
ai, ni, x = sp.symbols('a_i n_i x', positive=True)
nf = ni * (ai / x)**3
print("n(a) =", nf, " -> limit a->oo:", sp.limit(nf, x, sp.oo), " => rho -> Lb + f(0)")
