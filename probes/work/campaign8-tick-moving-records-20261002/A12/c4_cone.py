"""C4: causal structure of a T-tick windowed formation instrument (single-particle sector, 1D Dirac step).
Two implementations of the same detector (window w(t), carrier Omega, site x, R component):
 (reg) time-ordered: a one-slot register at x, phase e^{-i Omega} per tick, swaps amplitude with (x,R)
       by angle theta_t = g w(t) after each tick's step; the record is decided from the register at the end.
 (end) memoryless: one reach-T weight F = |m><m| applied at the end of the window, m = U^T chi, where
       chi is the pulled-back window mode (identical statistics to (reg) at weak coupling, no interventions).
'Bob' non-selectively dephases site y (both components) at the start of tick s ("is the particle at y?").
Strict cone (one site per tick): Bob can affect the record only if d = |y-x| <= T - s.
Report |Delta P| (with Bob minus without) versus d for both implementations."""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[v] = "1"
import numpy as np

N, m, Om, T, s, x = 96, 0.3, np.pi / 2, 24, 16, 48
cm, sm = np.cos(m), np.sin(m)
w = np.sin(np.pi * (np.arange(T) + 1) / (T + 1)) ** 2            # Hann switching


def step(psi):                                                       # psi[:,0]=R, psi[:,1]=L
    R, Lc = np.roll(psi[:, 0], 1), np.roll(psi[:, 1], -1)
    return np.stack([cm * R - 1j * sm * Lc, -1j * sm * R + cm * Lc], axis=1)


def step_back(psi):
    R, Lc = psi[:, 0], psi[:, 1]
    R0, L0 = cm * R + 1j * sm * Lc, 1j * sm * R + cm * Lc             # C(m)^-1 = C(-m)
    return np.stack([np.roll(R0, -1), np.roll(L0, 1)], axis=1)


def run_register(psi0, g, bob_y=None):
    """Exact (non-perturbative) register model; Bob splits the state into Kraus branches."""
    branches = [(psi0.copy(), 0j)]
    for t in range(T):
        if bob_y is not None and t == s:
            new = []
            for psi, r in branches:
                P = np.zeros_like(psi); P[bob_y] = psi[bob_y]
                new += [(P, 0j), (psi - P, r)]                   # register amplitude is 'not at y'
            branches = new
        out = []
        for psi, r in branches:
            psi = step(psi); r = r * np.exp(-1j * Om)
            th = g * w[t]
            a = psi[x, 0]
            psi[x, 0], r = np.cos(th) * a - np.sin(th) * r, np.sin(th) * a + np.cos(th) * r
            out.append((psi, r))
        branches = out
    return sum(abs(r) ** 2 for _, r in branches)


def end_mode(g):
    """m = sum_t g w(t) e^{i Om (T-1-t)} U^{T-1-t} e_{x,R}  (pushed-forward window mode at time T)."""
    mvec = np.zeros((N, 2), complex)
    for t in range(T):
        v = np.zeros((N, 2), complex); v[x, 0] = 1
        for _ in range(T - 1 - t):
            v = step(v)
        mvec += g * w[t] * np.exp(1j * Om * (T - 1 - t)) * v
    return mvec


def run_end(psi0, mvec, bob_y=None):
    if bob_y is None:
        psi = psi0.copy()
        for _ in range(T):
            psi = step(psi)
        return abs(np.vdot(mvec, psi)) ** 2
    psi = psi0.copy()
    for _ in range(s):
        psi = step(psi)
    P = np.zeros_like(psi); P[bob_y] = psi[bob_y]
    tot = 0.0
    for br in (P, psi - P):
        for _ in range(T - s):
            br = step(br)
        tot += abs(np.vdot(mvec, br)) ** 2
    return tot


rng = np.random.default_rng(7)
psi0 = rng.normal(size=(N, 2)) + 1j * rng.normal(size=(N, 2)); psi0 /= np.linalg.norm(psi0)
# consistency: both implementations agree without interventions at weak coupling
for g in (0.01, 0.05):
    pr, pe = run_register(psi0, g), run_end(psi0, end_mode(g))
    print(f"g={g}: P_reg={pr:.6e}  P_end={pe:.6e}  rel diff={abs(pr-pe)/pe:.2e} (O(g^2) expected)")
# step_back sanity
v = rng.normal(size=(N, 2)) + 0j
print(f"step_back(step(v)) error {np.abs(step_back(step(v)) - v).max():.1e}")
# strict cone of the step itself: support growth of e_x after t steps
v = np.zeros((N, 2), complex); v[x, 0] = 1
for _ in range(10):
    v = step(v)
supp = np.nonzero(np.abs(v).sum(1) > 0)[0]
print(f"support of U^10 e_x: sites {supp.min()-x:+d}..{supp.max()-x:+d} (strict cone: |d| <= 10)")
g = 0.3
mv = end_mode(g)
base_r, base_e = run_register(psi0, g), run_end(psi0, mv)
print(f"\nT={T}, Bob at tick s={s}; past cone of the record at (x,T) reaches d <= T-s = {T-s}")
print(f"{'d':>3} {'|dP| register (time-ordered)':>29} {'|dP| end-time weight':>21}")
for d in (0, 4, 7, 8, 9, 10, 12, 16, 20, 24, 28, 31, 32, 33, 36, 40):
    y = (x + d) % N
    dr = abs(run_register(psi0, g, y) - base_r)
    de = abs(run_end(psi0, mv, y) - base_e)
    print(f"{d:3d} {dr:29.3e} {de:21.3e}" + ("   <- outside past cone" if d > T - s else ""))
