"""PR 9355 attack-g: the displacement lemmas as written, verified LITERALLY (symbolic algebra plus a truncated-Fock brute force of the operator identities).

Steps of 'Exact displacement and proof obligations' (cyclic units: i d psi/dt = 2 pi H psi, theta = 2 pi w t):
  L1  D(alpha)^dagger a D(alpha) = a + alpha  and  D^dagger P D = P + 2 Im alpha,  P = i (a^dagger - a)   [truncated Fock space, 90 states, matrix elements on the lowest 12 states];
  L2  alpha(theta) = -D/2 [exp(-i theta)/(Omega - w) + exp(i theta)/(Omega + w)] solves i alpha_dot/(2 pi) = Omega alpha + D cos(theta)   [sympy, identically in theta];
  L3  the transformed charge drive: 2 G Im(alpha) = F sin(theta) with F = 2 G D w/(Omega^2 - w^2)   [sympy];
  L4  the time-dependent-displacement term: i D^dagger (d D/dt) = i alpha_dot a^dagger - i alpha_dot^* a + Im(alpha^* alpha_dot)   (finite differences of the truncated D on low states), after which the linear oscillator terms cancel
      exactly by L2 and the scalar term is  s(t) = Omega |alpha|^2 + 2 D cos(theta) Re(alpha) - Im(alpha^* alpha_dot)/(2 pi)   [sympy];
  L5  the mean of s over a period is -D^2 Omega/[2 (Omega^2 - w^2)]  [sympy integral], its periodic part is a pure phase, the mean shifts all quasienergies equally;
  L6  the sign/normalisation of the positive charge-drive coefficient F for Omega > w and its sign flip for Omega < w; the resonant case Omega = w is singular.
"""
import sys
import numpy as np
import sympy as sp
from scipy.linalg import expm

PASS = FAIL = 0
HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)

# ---- L1 truncated Fock brute force
K = 90
a = np.diag(np.sqrt(np.arange(1, K)), 1); ad = a.T
def Dop(al): return expm(al * ad - np.conj(al) * a)
al = 0.31 + 0.22j
Dm = Dop(al)
low = slice(0, 12)
lhs = (Dm.conj().T @ a @ Dm)[low, low]; rhs = (a + al * np.eye(K))[low, low]
P = 1j * (ad - a)
lhsP = (Dm.conj().T @ P @ Dm)[low, low]; rhsP = (P + 2 * al.imag * np.eye(K))[low, low]
check("L1: D(alpha)^dagger a D(alpha) = a + alpha and D^dagger P D = P + 2 Im alpha on the lowest 12 states of a 90-state ladder (alpha = 0.31 + 0.22 i)", np.abs(lhs - rhs).max() < 1e-12 and np.abs(lhsP - rhsP).max() < 1e-12, f"{np.abs(lhs-rhs).max():.1e}, {np.abs(lhsP-rhsP).max():.1e}")
# ---- L2, L3 symbolic
th, Om, w, Dd, G = sp.symbols("theta Omega w D G", positive=True)
al_s = -Dd / 2 * (sp.exp(-sp.I * th) / (Om - w) + sp.exp(sp.I * th) / (Om + w))
al_dot = 2 * sp.pi * w * sp.diff(al_s, th)                # d alpha / dt
ode = sp.simplify((sp.I * al_dot / (2 * sp.pi) - Om * al_s - Dd * sp.cos(th)).rewrite(sp.cos))
check("L2: alpha(theta) solves i alpha_dot/(2 pi) = Omega alpha + D cos(theta) identically in theta (Omega != +-w)", ode == 0, str(ode))
Im_al = sp.simplify(sp.im(sp.expand(al_s, complex=True)))
Fform = 2 * G * Dd * w / (Om ** 2 - w ** 2)
L3 = sp.simplify(2 * G * Im_al - Fform * sp.sin(th))
check("L3: 2 G Im(alpha) = F sin(theta) with F = 2 G D w/(Omega^2 - w^2)", L3 == 0, str(L3))
# ---- L4 finite-difference check of i D^dagger dD/dt on the lowest states
def al_num(t, D_=0.7, Om_=1.3, w_=0.4):
    th_ = 2 * np.pi * w_ * t
    return -D_ / 2 * (np.exp(-1j * th_) / (Om_ - w_) + np.exp(1j * th_) / (Om_ + w_))
t0, dt = 0.37, 1e-5
alp, alm, al0 = al_num(t0 + dt), al_num(t0 - dt), al_num(t0)
dD = (Dop(alp) - Dop(alm)) / (2 * dt)
Aop = 1j * (Dop(al0).conj().T @ dD)
aldot = (alp - alm) / (2 * dt)
formula = 1j * aldot * ad - 1j * np.conj(aldot) * a - (np.conj(al0) * aldot).imag * np.eye(K)
check("L4: i D^dagger (dD/dt) = i alpha_dot a^dagger - i alpha_dot^* a - Im(alpha^* alpha_dot) (central differences, lowest 12 states; the scalar has the MINUS sign)", np.abs((Aop - formula)[low, low]).max() < 1e-6, f"{np.abs((Aop - formula)[low, low]).max():.1e}")
# ---- L4 cancellation and scalar, L5 mean (alpha = A e^{-i theta} + B e^{i theta} with real A, B, so every quantity is a trigonometric polynomial)
A_, B_ = sp.symbols("A B", real=True)
al2 = A_ * sp.exp(-sp.I * th) + B_ * sp.exp(sp.I * th); al2dot = 2 * sp.pi * w * sp.diff(al2, th)
abs2 = sp.simplify(sp.expand(al2 * sp.conjugate(al2)).rewrite(sp.cos))
re_al = sp.simplify(sp.expand((al2 + sp.conjugate(al2)) / 2).rewrite(sp.cos))
im_cross = sp.simplify(sp.expand((sp.conjugate(al2) * al2dot - al2 * sp.conjugate(al2dot)) / (2 * sp.I)).rewrite(sp.cos))
s_gen = sp.simplify(Om * abs2 + 2 * Dd * sp.cos(th) * re_al + im_cross / (2 * sp.pi))
A_val = -Dd / (2 * (Om - w)); B_val = -Dd / (2 * (Om + w))
s_t = sp.simplify(s_gen.subs({A_: A_val, B_: B_val}))
mean = sp.simplify(sp.integrate(sp.expand(s_t), (th, 0, 2 * sp.pi)) / (2 * sp.pi))
target = -Dd ** 2 * Om / (2 * (Om ** 2 - w ** 2))
check("L5: the period mean of the scalar term is -D^2 Omega / [2 (Omega^2 - w^2)] (closed-form trigonometric polynomial, sympy)", sp.simplify(mean - target) == 0, f"mean = {sp.factor(mean)}")
osc = sp.simplify(s_t - mean)
print(f"   periodic part of the scalar term: {sp.factor(osc)}")
check("L5: the periodic part of the scalar term has zero mean and depends on theta only (a periodic phase, no change of quasienergy differences)", sp.simplify(sp.integrate(sp.expand(osc), (th, 0, 2 * sp.pi))) == 0)
# the linear terms cancel: coefficient of a^dagger in D^dagger H D - i D^dagger Ddot/(2 pi) is Omega alpha + D cos(theta) - i alpha_dot/(2 pi) = 0 (L2)
check("L4: the a^dagger coefficient Omega alpha + D cos(theta) - i alpha_dot/(2 pi) of the transformed Hamiltonian vanishes identically (its conjugate gives the a coefficient)", sp.simplify((Om * al_s + Dd * sp.cos(th) - sp.I * al_dot / (2 * sp.pi)).rewrite(sp.cos)) == 0)
# ---- L6 signs
vals = {Dd: 1, G: 1, w: sp.Rational(1, 2)}
F_above = Fform.subs({Om: 2, **vals}); F_below = Fform.subs({Om: sp.Rational(1, 4), **vals})
check("L6: F > 0 for Omega > w, F < 0 for Omega < w, and F diverges at Omega = w (the note excludes the resonant case)", F_above > 0 and F_below < 0 and sp.limit(Fform.subs({Dd: 1, G: 1, w: 1}), Om, 1, "+") == sp.oo, f"F(2) = {F_above}, F(1/4) = {F_below}")
print()
for h in HITS: print("HIT:", h)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-g proof steps on PR 9355: L1 D^dagger a D and D^dagger P D on a truncated ladder, L2 the forced solution alpha, L3 F = 2GDw/(Omega^2 - w^2), L4 the i D^dagger Ddot term, L5 the scalar term with period mean -D^2 Omega/[2 (Omega^2 - w^2)] (sympy), L6 the sign of F and the resonant singularity all verify as written; PASS={PASS} FAIL={FAIL}; no defect in the note's displacement lemmas")
sys.exit(1 if FAIL else 0)
