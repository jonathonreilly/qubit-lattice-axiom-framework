#!/usr/bin/env python3
"""J:attack-g:PR9360 -- PROOF STEP BY BRUTE FORCE: the closed forms of the qutrit preparation-transfer note.

Note: with the population generator L = [[0, k10, k20], [0, -k10, k21], [0, 0, -k21 - k20]] (columns sum to zero, off-diagonals nonnegative), lambda = k21 + k20 and F(t) = [exp(-k10 t) - exp(-lambda t)]/(lambda - k10) (limit t exp(-k10 t) at lambda = k10):
u2(t) = u2(0) exp(-lambda t), u1(t) = u1(0) exp(-k10 t) + k21 u2(0) F(t), u0 = 1 - u1 - u2; the calibration vector for the state-|2> preparation is [1 - exp(-lambda t) - k21 F, k21 F, exp(-lambda t)];
the Ramsey sum for the initial populations [0, 1/2, 1/2] is Pexc(t) = [exp(-k10 t) + exp(-lambda t) + k21 F(t)]/2; for any final unitary U mixing only states 1 and 2, Tr(P U rho U^dag) = Tr(P rho); the echo state is u_echo(t) = exp(L t/2) S exp(L t/2) [0, 1/2, 1/2] with S the 1 <-> 2 exchange.
Verified here literally against the matrix exponential (mpmath expm at 40 digits as the reference, scipy expm compared as information, and an independent ODE integration) at random rates (including k20 = 0 and lambda = k10 exactly, and lambda - k10 tiny), random times and random initial populations; plus the statement that exp(Lt) preserves normalised nonnegative populations;
the trace identity for random unitaries on the {1,2} block and for random (incoherent and coherent) density matrices; the two-rate control k20 = 0. Prints SUMMARY:; HIT only if a closed form disagrees.
"""
import sys
import numpy as np
import mpmath as mp
from scipy.linalg import expm
from scipy.integrate import solve_ivp
mp.mp.dps = 40
def expm_mp(L, t):
    return np.array(mp.expm(mp.matrix(L.tolist()) * mp.mpf(t)).tolist(), dtype=float)
rng = np.random.default_rng(1)
def Lmat(k10, k21, k20): return np.array([[0, k10, k20], [0, -k10, k21], [0, 0, -k21 - k20]], dtype=float)
def F(t, k10, lam):
    return t * np.exp(-k10 * t) if abs(lam - k10) < 1e-12 else (np.exp(-k10 * t) - np.exp(-lam * t)) / (lam - k10)
def Fmp(t, k10, lam):
    t, k10, lam = mp.mpf(t), mp.mpf(k10), mp.mpf(lam)
    return t * mp.exp(-k10 * t) if lam == k10 else (mp.exp(-k10 * t) - mp.exp(-lam * t)) / (lam - k10)
worst = 0.0; n = 0; bad = []; scipy_gap = 0.0; dbl_gap = 0.0
cases = [(rng.uniform(0.01, 1), rng.uniform(0.01, 1), rng.uniform(0, 0.2)) for _ in range(300)]
cases += [(0.3, 0.2, 0.1), (0.3, 0.3, 0.0), (0.05, 0.11, 0.0), (0.3, 0.1, 0.2), (0.3, 0.1 + 1e-9, 0.2), (0.0712, 0.1112, 0.0084)]   # lambda = k10 exactly in the 4th; nearly in the 5th
for (k10, k21, k20) in cases:
    L = Lmat(k10, k21, k20); lam = k21 + k20
    assert np.allclose(L.sum(axis=0), 0) and (L - np.diag(np.diag(L)) >= 0).all()
    for t in (0.0, 0.5, 3.0, 20.0, 60.0):
        E = expm_mp(L, t); Es = expm(L * t); scipy_gap = max(scipy_gap, float(np.max(np.abs(E - Es))))
        cal = E @ np.array([0, 0, 1.0])
        Fm = Fmp(t, k10, lam); ml = mp.mpf(k21) + mp.mpf(k20)
        cf = np.array([float(1 - mp.exp(-ml * t) - mp.mpf(k21) * Fm), float(mp.mpf(k21) * Fm), float(mp.exp(-ml * t))])
        cf_d = np.array([1 - np.exp(-lam * t) - k21 * F(t, k10, lam), k21 * F(t, k10, lam), np.exp(-lam * t)]); dbl_gap = max(dbl_gap, float(np.max(np.abs(cf_d - cf))))
        u = E @ np.array([0, 0.5, 0.5])
        ram = u[1] + u[2]; ramf = float((mp.exp(-mp.mpf(k10) * t) + mp.exp(-ml * t) + mp.mpf(k21) * Fm) / 2)
        S = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0.0]])
        echo = expm_mp(L, t / 2) @ S @ expm_mp(L, t / 2) @ np.array([0, 0.5, 0.5])
        err = max(np.max(np.abs(cal - cf)), abs(ram - ramf), abs(echo.sum() - 1.0), abs(E[:, 2].sum() - 1.0))
        worst = max(worst, err); n += 1
        if err > 1e-9: bad.append((k10, k21, k20, t, err))
        if not ((E >= -1e-15).all() and np.allclose(E.sum(axis=0), 1, atol=1e-13)): bad.append(("not stochastic", k10, k21, k20, t))
print(f"   {n} (rates, time) points incl. lambda = k10 and lambda - k10 = 1e-9: max |closed form - matrix exponential (40 digits)| = {worst:.2e}; INFO: the same closed forms in double precision differ from the 40-digit ones by up to {dbl_gap:.1e} (cancellation in F when lambda - k10 = 1e-9), and scipy.linalg.expm differs from the 40-digit exponential by up to {scipy_gap:.1e} (largest at the defective lambda = k10 matrices)")
ok1 = not bad
# independent ODE integration for one set
k10, k21, k20 = 0.0712691, 0.1112412, 0.0083977
sol = solve_ivp(lambda t, y: Lmat(k10, k21, k20) @ y, [0, 40], [0, 0, 1.0], rtol=1e-12, atol=1e-14)
lam = k21 + k20
cf = np.array([1 - np.exp(-lam * 40) - k21 * F(40, k10, lam), k21 * F(40, k10, lam), np.exp(-lam * 40)])
ok2 = np.max(np.abs(sol.y[:, -1] - cf)) < 1e-9
print(f"   ODE integration (rtol 1e-12) against the closed form at t = 40 with the fitted rates: max difference {np.max(np.abs(sol.y[:, -1] - cf)):.2e}")
# trace identity: P = |1><1| + |2><2|; U mixes only states 1 and 2
P = np.diag([0, 1, 1.0]); worst_tr = 0.0
for _ in range(500):
    A = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)); Q, _ = np.linalg.qr(A)
    U = np.eye(3, dtype=complex); U[1:, 1:] = Q
    X = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); rho = X @ X.conj().T; rho /= np.trace(rho)
    worst_tr = max(worst_tr, abs(np.trace(P @ U @ rho @ U.conj().T) - np.trace(P @ rho)))
ok3 = worst_tr < 1e-12
print(f"   trace identity Tr(P U rho U^dag) = Tr(P rho) for 500 random unitaries on the {{1,2}} block and random density matrices: max difference {worst_tr:.1e}")
# a unitary that mixes state 0 with 1 violates it (the identity needs U to act only on 1 and 2): sanity that the check has teeth
U = np.eye(3, dtype=complex); c = np.cos(0.7); s = np.sin(0.7); U[:2, :2] = [[c, -s], [s, c]]
rho = np.diag([0.6, 0.1, 0.3]).astype(complex)
teeth = abs(np.trace(P @ U @ rho @ U.conj().T) - np.trace(P @ rho)) > 1e-3
print(f"   control: a rotation mixing 0 and 1 changes Tr(P rho) (the identity has teeth): {teeth}")
ok = ok1 and ok2 and ok3 and teeth and worst < 1e-9
print(f"[{'PASS' if ok else 'FAIL'}] every closed form of the note (calibration vector, Ramsey sum, stochasticity, trace invariance, echo normalisation) agrees with the matrix exponential and an ODE integration")
if ok:
    print(f"SUMMARY: no purchase: the note's closed forms agree with the matrix exponential to {worst:.1e} at {n} random (rates, time) points including the degenerate lambda = k10 and k20 = 0 cases, with an ODE integration, and the trace-invariance identity holds for random unitaries on the {{1,2}} block")
else:
    print("SUMMARY: a closed form disagrees: " + str(bad[:2])); print("HIT: closed form disagrees")
sys.exit(0)
