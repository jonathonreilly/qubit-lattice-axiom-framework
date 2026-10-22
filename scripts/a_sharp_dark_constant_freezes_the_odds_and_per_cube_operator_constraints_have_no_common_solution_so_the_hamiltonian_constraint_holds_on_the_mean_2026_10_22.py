AUDIT_INPUT_PATHS = ('docs/A_SHARP_DARK_CONSTANT_FREEZES_THE_ODDS_AND_PER_CUBE_OPERATOR_CONSTRAINTS_HAVE_NO_COMMON_SOLUTION_SO_THE_HAMILTONIAN_CONSTRAINT_HOLDS_ON_THE_MEAN_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""problem-of-time probe: can the odds obey the Hamiltonian constraint under a fixed tick?

Toy: one cube = one edge register (n = 0..2S, length l = 1 + n/2S, ghost-sign edge hop
w (V + V^dag), V normalised on its domain) + one matter two-level mode (dust energy M and an
atom splitting Omega read with the conformal lapse N = sig*l, volume-mode A3 in hop form).
Two cubes: two such registers, one fermion shared between the cubes, a hinge two-register
hop, each shared term counted half in each cube (CL-3's "shared equally").
Half-ticks: A = edge hop, B = matter phase on the edges (diagonal in n).
Self-contained (numpy/scipy only)."""
import time
import numpy as np
from scipy.linalg import expm, eigh, schur
from scipy.special import logsumexp
from scipy.signal import hilbert
from scipy.optimize import brentq, minimize_scalar

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
NP = NF = 0


def rep(ok, tag, msg):
    global NP, NF
    NP += bool(ok)
    NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} | {msg}")


def hop(d):
    return np.diag(np.ones(d - 1), 1) + np.diag(np.ones(d - 1), -1)


SX = np.array([[0., 1.], [1., 0.]])
SZ = np.diag([1., -1.])
I2 = np.eye(2)


def cube(twoS, w=1.0, sig=1.0, M=1.0, Om=0.4, E0=1.5):
    d = twoS + 1
    l = 1.0 + np.arange(d) / twoS
    Kkin = np.kron(w * hop(d), I2)
    Kpot = np.kron(np.diag(sig * l), M * I2 + 0.5 * Om * SX) - E0 * np.eye(2 * d)
    return Kkin, Kpot, l


def floquet(Kkin, Kpot, eps):
    UA = expm(-1j * eps * Kkin)
    UB = expm(-1j * eps * Kpot)
    return UA, UB, UB @ UA


# ============ A. constraint versus tick (exact statements on the toy)
print("== A. the Hamiltonian constraint as an operator on the odds")
Kkin, Kpot, l = cube(60)
eps = 0.5
UA, UB, UF = floquet(Kkin, Kpot, eps)
Tq, V = schur(UF, output="complex")
ph = np.diag(Tq)
rng = np.random.default_rng(1)
# A1 any sharp quasi-energy (dark constant) state: every probability frozen; the
# distribution over quasi-energies of ANY state is a constant of the tick
j = 7
psi = V[:, j] / np.linalg.norm(V[:, j])
P0 = abs(psi) ** 2
x = psi.copy()
dmax = 0.0
for _ in range(300):
    x = UF @ x
    dmax = max(dmax, abs(abs(x) ** 2 - P0).max())
phi = rng.normal(size=UF.shape[0]) + 1j * rng.normal(size=UF.shape[0])
phi /= np.linalg.norm(phi)
Vi = V.conj().T
w0 = abs(Vi @ phi) ** 2
y = np.linalg.matrix_power(UF, 137) @ phi
w1 = abs(Vi @ y) ** 2
rep(dmax < 1e-12 and abs(w1 - w0).max() < 1e-10, "A1 [T]",
    f"sharp dark constant (eigen-phase of the tick): max|dP| over 300 ticks {dmax:.1e} -> odds frozen for "
    f"EVERY value of c, not only c = 0; spectral weights of a random state conserved {abs(w1-w0).max():.1e}: "
    f"restricting to the c = 0 eigenspace IS the fixed-point space of the tick")

# A2 the constraint read from the total phase, K = Kkin + Kpot, is not the tick's
# conserved quasi-energy: ker K is not invariant under alternating half-ticks (BCH, O(eps))
Ktot = Kkin + Kpot
lam, W = eigh(Ktot)
jj = np.argmin(abs(lam))
res = []
for e in (0.2, 0.1, 0.05):
    Kp = Kpot - lam[jj] * np.eye(len(lam))   # tune the supplied constant: K psi = 0 exactly
    K0 = Kkin + Kp
    _, _, U = floquet(Kkin, Kp, e)
    z = W[:, jj].astype(complex)
    r = 0.0
    for _ in range(int(40 / e)):
        z = U @ z
        r = max(r, np.linalg.norm(K0 @ z))
    res.append(r)
rat = [res[0] / res[1], res[1] / res[2]]
rep(res[2] > 1e-4 and all(1.7 < q < 2.3 for q in rat), "A2 [T+D]",
    f"K psi = 0 at t=0; max|K U^t psi| over 40 tick-units = {res[0]:.2e}, {res[1]:.2e}, {res[2]:.2e} at eps = "
    f".2/.1/.05 (ratios {rat[0]:.2f}, {rat[1]:.2f} -> O(eps)): the half-ticks keep the shadow i log U_F, not K")

# A3 finite register: the operator constraint has no solution unless a supplied constant is tuned
dist = []
for E0 in rng.uniform(1.0, 2.0, 5):
    kk, pp, _ = cube(60, E0=E0)
    dist.append(np.min(abs(eigh(kk + pp, eigvals_only=True))))
gap = np.min(np.diff(np.sort(lam)))
rep(min(dist) > 1e-6, "A3 [T]",
    f"spectrum of K on a 61-value register is discrete (min level spacing {gap:.2e}); random supplied constant "
    f"E0: dist(0, spec K) = {min(dist):.1e}..{max(dist):.1e} > 0, ker K = {{0}}; a kernel needs E0 in a finite set (codim 1)")

# A4 two cubes: per-cube constraints, each shared term counted half in each cube
twoS2 = 12
d2 = twoS2 + 1
l2 = 1.0 + np.arange(d2) / twoS2
Vr = np.diag(np.ones(d2 - 1), -1)          # raiser, normalised on its domain
Id = np.eye(d2)
L1 = np.kron(np.kron(np.diag(l2), Id), I2)
L2 = np.kron(np.kron(Id, np.diag(l2)), I2)
P1 = np.kron(np.kron(Id, Id), np.diag([1., 0.]))
P2 = np.kron(np.kron(Id, Id), np.diag([0., 1.]))
h1 = np.kron(np.kron(hop(d2), Id), I2) + L1 @ P1
h2 = np.kron(np.kron(Id, hop(d2)), I2) + L2 @ P2
h12 = 0.5 * (np.kron(np.kron(Vr, Vr.T), I2) + np.kron(np.kron(Vr.T, Vr), I2)) \
    + 0.3 * 0.5 * (L1 + L2) @ np.kron(np.kron(Id, Id), SX)
Dm = h1.shape[0]
H1b = h1 + 0.5 * h12
H2b = h2 + 0.5 * h12


def smin_joint(E0):
    A = H1b - E0 * np.eye(Dm)
    B = H2b - E0 * np.eye(Dm)
    return np.sqrt(max(eigh(A @ A + B @ B, eigvals_only=True, subset_by_index=[0, 0])[0], 0))


grid = np.linspace(-4, 5, 181)
vals = [smin_joint(e) for e in grid]
i0 = int(np.argmin(vals))
opt = minimize_scalar(smin_joint, bounds=(grid[max(i0 - 1, 0)], grid[min(i0 + 1, 180)]), method="bounded")
comm = np.linalg.norm(H1b @ H2b - H2b @ H1b) / np.linalg.norm(H1b) / np.linalg.norm(H2b) * np.sqrt(Dm)
lg = eigh(H1b + H2b, eigvals_only=True)
rep(opt.fun > 1e-3 and comm > 1e-2, "A4 [T+D]",
    f"two cubes ({Dm} states): ||[H1,H2]|| rel {comm:.2f}; min over the supplied constant of "
    f"sigma_min([H1-E0; H2-E0]) = {opt.fun:.3f} at E0 = {opt.x:.2f} > 0: NO odds obey both cube constraints for ANY E0; "
    f"the sum H1 + H2 - 2E0 has a kernel at E0 = {lg[len(lg)//2]/2:.3f} (one global condition)")

# A5 contrast: Gauss's law (link register between two sites, spin S = 1)
dS = 3
Ve = np.diag(np.ones(dS - 1), -1)
c = np.array([[0., 1.], [0., 0.]])
Zf = np.diag([1., -1.])
c1 = np.kron(np.kron(c, I2), np.eye(dS))
c2 = np.kron(np.kron(Zf, c), np.eye(dS))
U_ = np.kron(np.eye(4), Ve)
Ev = np.kron(np.eye(4), np.diag([-1., 0., 1.]))
n1 = c1.conj().T @ c1
n2 = c2.conj().T @ c2
Hg = c2.conj().T @ U_ @ c1
Hg = Hg + Hg.conj().T + 0.7 * Ev @ Ev
G1 = n1 + Ev
G2 = n2 - Ev
Ug = expm(-1j * 0.9 * Hg)
cg = max(np.linalg.norm(Ug @ G - G @ Ug) for G in (G1, G2))
mask = (abs(np.diag(G1) - 1) < 1e-9) & (abs(np.diag(G2) - 0) < 1e-9)
sub = Ug[np.ix_(mask, mask)]
nontriv = np.linalg.norm(sub - np.eye(mask.sum()) * sub[0, 0])
rep(cg < 1e-12 and mask.sum() >= 2 and nontriv > 0.1, "A5 [T]",
    f"Gauss: [U, G_x] = {cg:.0e}, integer spectra, sector (G1,G2) = (1,0) has dim {mask.sum()}, and the tick acts "
    f"on it non-trivially (|U - phase| = {nontriv:.2f}): Gauss's law is a symmetry, the Hamiltonian constraint is the tick's own generator")

# ============ B. relational time and CL-2's history
print("== B. relational time (Page-Wootters) and the actual configuration")
# B1 sharp sector on a finite register: generic eigenvector has a definite atom level
twoS = 200
d = twoS + 1
lB = 1.0 + np.arange(d) / twoS
w, sig, M = 1.0, 1.0, 1.0


def chain(Om, s):
    return w * hop(d) + np.diag(sig * lB * (M + s * 0.5 * Om))


Kfull = np.kron(w * hop(d), I2) + np.kron(np.diag(sig * lB), M * I2 + 0.2 * SX)
le, ve = eigh(Kfull)
jj = np.argmin(abs(le - 1.5))
vv = ve[:, jj].reshape(d, 2)
xb = np.array([1, 1]) / np.sqrt(2)
wplus = np.sum(abs(vv @ xb) ** 2)
rep(min(wplus, 1 - wplus) < 1e-10, "B1 [T]",
    f"Omega = 0.2: the sharp state nearest c = 0 has atom energy weight {wplus:.3f} on one level (other {1-wplus:.1e}): "
    f"a non-degenerate sharp sector is ONE state, the atom is in a stationary level, nothing changes relative to anything")

# B2 tune the two supplied constants (E0, Omega) so both atom levels meet c = 0:
la0 = eigh(chain(0.2, +1), eigvals_only=True)
jp = int(np.argmin(abs(la0 - 1.5)))
lm0 = eigh(chain(0.2, -1), eigvals_only=True)
jm = int(np.searchsorted(lm0, la0[jp]))


def dif(Om):
    return eigh(chain(Om, +1), eigvals_only=True)[jp] - eigh(chain(Om, -1), eigvals_only=True)[jm]


Omt = brentq(dif, 0.2, 0.26, xtol=1e-14)
ap, vp = eigh(chain(Omt, +1))
am, vm = eigh(chain(Omt, -1))
E0t = ap[jp]
fp, fm = vp[:, jp], vm[:, jm]
# conditional atom state at edge value n: (fp(n)|+> + fm(n)|->)/norm (x basis), real
sy = 2 * np.imag(np.conj(fp) * fm)
cut = slice(20, d - 20)
hp, hm = hilbert(fp), hilbert(fm)
rel = np.unwrap(np.angle(hp[cut]) - np.angle(hm[cut]))
vel = np.sqrt(4 * w ** 2 - (E0t - sig * lB * M) ** 2)
tau_rel = np.cumsum(Omt * sig * lB / vel)[cut]
fitslope = np.polyfit(tau_rel - tau_rel[0], rel - rel[0], 1)[0]
dev = np.max(abs((rel - rel[0]) - (tau_rel - tau_rel[0])))
# forward branch's conditional sigma_y amplitude, for contrast
syf = 2 * np.imag(np.conj(hp[cut]) * hm[cut]) / (abs(hp[cut]) ** 2 + abs(hm[cut]) ** 2)
rep(np.max(abs(sy)) < 1e-14 and abs(abs(fitslope) - 1) < 0.02 and np.max(abs(syf)) > 0.9, "B2 [T+D]",
    f"tuned (E0, Omega) = ({E0t:.4f}, {Omt:.5f}): sharp c = 0 state with both levels; conditional <sigma_y>(n) = "
    f"{np.max(abs(sy)):.0e} for every n (real K: forward and backward histories superposed, no time direction); "
    f"forward branch (analytic signal in n): relative phase / (Omega x proper time on the orbit) slope {abs(fitslope):.4f}, "
    f"max dev {dev:.2f} rad over {rel[-1]-rel[0]:.0f} rad, and its <sigma_y> swings to {np.max(abs(syf)):.2f}")


# B3 CL-2 transport (fewest changes incl. edge units, then greatest entropy; entropic OT, small reg)
def transport(P, Q, Uh, cost, reg=0.05, it=600):
    mask = abs(Uh) > 1e-12
    logK = np.where(mask, -cost / reg, -np.inf)
    lp, lq = np.log(P + 1e-300), np.log(Q + 1e-300)
    f = np.zeros(len(P))
    g = np.zeros(len(Q))
    for _ in range(it):
        f = lp - logsumexp(logK + g[None, :], axis=1)
        g = lq - logsumexp(logK + f[:, None], axis=0)
    T = np.exp(f[:, None] + logK + g[None, :])
    return T, abs(T.sum(1) - P).max() + abs(T.sum(0) - Q).max()


twoS = 60
Kkin, Kpot, lC = cube(twoS, Om=0.4)
dC = twoS + 1
UA, UB, UF = floquet(Kkin, Kpot, 0.5)
nn = np.repeat(np.arange(dC), 2)
aa = np.tile([0, 1], dC)
cost = abs(nn[:, None] - nn[None, :]) + abs(aa[:, None] - aa[None, :])   # cost[x, x']
n0, s0 = 12, 3.0
k0 = -np.arccos((1.5 - (1 + n0 / twoS)) / 2.0)        # sin k0 < 0: edge moves up
amp = np.exp(-(np.arange(dC) - n0) ** 2 / (4 * s0 ** 2) + 1j * k0 * np.arange(dC))
Phi = np.kron(amp, np.array([1., 0.]))
Phi /= np.linalg.norm(Phi)
Tq, V = schur(UF, output="complex")
ph = np.diag(Tq)
Vn = V
js = int(np.argmax(abs(Vn.conj().T @ Phi)))
psi_s = Vn[:, js]


def simulate(psi, nt, nrun, rng, sharp=False):
    paths = np.zeros((nrun, nt + 1), dtype=int)
    means = np.zeros(nt + 1)
    x = psi.copy()
    P = abs(x) ** 2
    st = rng.choice(len(P), size=nrun, p=P / P.sum())
    paths[:, 0] = nn[st]
    means[0] = P @ nn
    errs = 0.0
    cache = {}
    for t in range(nt):
        for h, Uh in enumerate((UA, UB)):
            y = Uh @ x
            Q = abs(y) ** 2
            if sharp and h in cache:
                T = cache[h]
            else:
                T, e = transport(P, Q, Uh.T, cost)
                errs = max(errs, e)
                cache[h] = T
            cond = T / np.maximum(T.sum(1, keepdims=True), 1e-300)
            cum = np.cumsum(cond[st], axis=1)
            st = np.minimum((cum < rng.random((nrun, 1)) * cum[:, -1:]).sum(1), len(Q) - 1)
            x, P = y, Q
        paths[:, t + 1] = nn[st]
        means[t + 1] = P @ nn
    return paths, means, errs


# quasi-energy (dark constant) operator per tick, U_F = exp(-i KF)
KF = V @ np.diag(-np.angle(ph)) @ V.conj().T
mu1 = np.vdot(Phi, KF @ Phi).real
dK = np.sqrt(max(np.vdot(Phi, KF @ KF @ Phi).real - mu1 ** 2, 0))


rngs = np.random.default_rng(7)
# packet (spread dark constant): sharp edge motion
pk, mk, ek = simulate(Phi, 30, 200, rngs)
ck = np.corrcoef(np.arange(31), pk.mean(0))[0, 1]
lagk = np.max(abs(pk.mean(0) - mk))
rep(ek < 1e-3 and pk[:, -1].mean() - pk[:, 0].mean() > 15 and ck > 0.99 and lagk < 1.0, "B3 [D]",
    f"packet (dark constant <c> {mu1:+.3f}, spread {dK:.3f}/tick): actual edge value "
    f"advances {pk[:, -1].mean() - pk[:, 0].mean():.1f} units in 30 ticks, mean path follows <n>_t "
    f"(max dev {lagk:.2f}, Sinkhorn marginal residual {ek:.0e}), corr(record count, actual n) {ck:.3f}: the half-tick record count is a clock with something to time")
# sharp: same physics label, c sharp
ps, ms, es = simulate(psi_s, 300, 200, rngs, sharp=True)
disp = ps[:, -1] - ps[:, 0]
moves = np.mean(np.abs(np.diff(ps, axis=1)) > 0)
cs = np.mean([abs(np.corrcoef(np.arange(301), p)[0, 1]) for p in ps if p.std() > 0] or [0.0])
rep(es < 1e-6 and abs(disp.mean()) < 2.0 and moves < 0.2, "B4 [D]",
    f"sharp sector (overlap {abs(np.vdot(psi_s, Phi))**2:.2f} with the packet): odds frozen; actual edge moves in "
    f"{moves:.3f} of ticks, net drift {disp.mean():+.2f} +- {disp.std()/np.sqrt(len(disp)):.2f} units over 300 ticks, "
    f"mean |corr(t, n)| {cs:.2f}: CL-2's history exists but records no expansion; the record count advances, nothing it times does")

# B4b both half-ticks hop the edges and carry matter phase (closer to CL-1's two tilings)
UA0, UB0 = UA, UB
UA = expm(-1j * 0.5 * (Kkin + Kpot))
UB = expm(-1j * 0.5 * (0.6 * Kkin + 1.3 * Kpot))
Tq2, V2 = schur(UB @ UA, output="complex")
psi2 = V2[:, int(np.argmax(abs(V2.conj().T @ Phi)))]
p2, _, e2 = simulate(psi2, 300, 200, rngs, sharp=True)
mv2 = np.mean(np.abs(np.diff(p2, axis=1)) > 0)
UA, UB = UA0, UB0
rep(e2 < 1e-6 and mv2 < 0.05, "B4b [D]",
    f"both half-ticks move edges: actual edge changes between whole ticks in {mv2:.3f} of ticks: the fewest-change "
    f"transports P -> P' -> P act on the edge as monotone (quantile) maps, so their composition returns each value to itself")

# B5 the conserved dark-constant distribution of the packet; Mandelstam-Tamm need for a spread
y = Phi.copy()
mt_ok = True
tq = None
for t in range(1, 60):
    y = UF @ y
    ov = abs(np.vdot(Phi, y))
    if dK * t <= np.pi / 2:
        mt_ok &= ov >= np.cos(dK * t) - 1e-9
    if tq is None and ov < 0.1:
        tq = t
rep(mt_ok and tq is not None, "B5 [T]",
    f"packet: <c> = {mu1:+.3f}, spread dK = {dK:.3f} per tick (conserved exactly with the whole distribution); "
    f"|<Phi|U^t Phi>| >= cos(dK t) holds; overlap < 0.1 after {tq} ticks: a history of T distinguishable ticks needs dK >~ pi/(2T)")

# ============ C. estimates against measurement
print("== C. estimates")
# needed global spread: one Planck-energy quantum per tick (state changes every tick) vs N_eff room
E_P = 1.22e19                      # GeV
rho_g = 0.26 * 1e-9                # photon energy density today ~0.26 eV/cm^3 -> GeV/cm^3
V_H = 4 / 3 * np.pi * (1.37e28) ** 3   # cm^3
room = 0.04 * rho_g * 1.68 * V_H        # dark radiation allowed by N_eff (~4% of radiation) in GeV
rep(E_P / room < 1e-40, "C1 [E]",
    f"a global dark-constant spread of one Planck energy (enough to change the state every tick) vs the N_eff room "
    f"for dark radiation in a Hubble volume {room:.1e} GeV: ratio {E_P/room:.0e}; the mean is bounded by N_eff, the spread is invisible")
print("supplied: one-cube hop-form ghost kinetic + conformal-lapse dust/atom terms (volume-mode A3 form), A/B split as")
print("  edges/matter (not the even/odd tilings), two-cube shared terms halved, CL-2 transport via entropic OT (reg 0.05),")
print("  edge units counted in the cost (law text); not built: lattice cube tick, momentum constraint as operator, splits.")
print(f"elapsed {time.time()-T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
