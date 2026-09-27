#!/usr/bin/env python3
"""A strictly local walker is left-right balanced whether time flows or ticks;
only tails (or interactions) give a chiral spectrum.

Objects (supplied comparators, none adopted):
- flowing walker: H(k) = sum_j sin k_j sigma_j (the campaign's walker);
- ticking walker: the ordered conditional-shift product
  U_-(k) = S_x(k_x) S_y(k_y) S_z(k_z), S_j(q) = cos q - i sin q sigma_j
  (the cycle-7 cubic factorisation of the published BCC Weyl walk);
- a rotation-covariant tick with tails:
  U_g(k) = c_x c_y c_z - i g(k) s(k).sigma,  g = sqrt((1 - (c_x c_y c_z)^2)/|s|^2).

Checks:
A. Flowing walker: exact nodes at {0, pi}^3 with chirality (-1)^(number of pi's);
   total 0.  Random range-one two-band Hamiltonians: all numerically located
   zeros of d(k) have total chirality 0.
B. Ticking walker, exact (sympy): 16 nodes. The 8 corners are right-handed
   (4 at quasi-energy 0, 4 at pi); the 8 points (pi/2)(+-1, +-1, +-1) are
   left-handed (4 at 0, 4 at pi). Numerical root search finds no others.
C. Winding numbers W3 = -(1/24 pi^2) int tr(U^-1 dU)^3 (a right-handed node at
   quasi-energy 0 counts +1): U_- gives 0,
   exp(-iH) gives 0, U_g gives 4, and W3(U_g U_-) = 4 (additivity).
D. Random strictly local ticks (products of conditional shifts along random
   lattice vectors with random constant coins; random brickwork one-body
   circuits on a 2x2x2 cell with random U(4) gates) all give W3 = 0.
E. Magnetic slab (flux 2 pi/12 per plaquette, 12 x 12, B along z): the ticking
   walker's states within 0.35 of quasi-energy 0 all move along +B at k_z = 0 and
   pi and all against it at k_z = pi/2 (the left-handed partners); the flowing
   walker's zero-energy states at k_z = 0 move both ways.
F. U_g: unitary; covariant under all 24 proper cubic rotations (spin-1/2 coin);
   its only nodes are the 8 corners, all right-handed; its real-space amplitude
   along an axis falls as r^-6 (not strictly local).

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys

AUDIT_INPUT_PATHS = (
    'docs/LATTICE_HANDEDNESS_A_STRICTLY_LOCAL_WALKER_IS_LEFT_RIGHT_BALANCED_WHETHER_TIME_FLOWS_OR_TICKS_ONLY_TAILS_OR_INTERACTIONS_GIVE_A_CHIRAL_SPECTRUM_BOUNDED_THEOREM_NOTE_2026-09-27.md',
    'docs/work_history/repo/review_feedback/CUBIC_QUBIT_RELATIVISTIC_REDUCTION_CYCLE7_NOTE_2026-07-14.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
)
AUDIT_TIMEOUT_SEC = 900

import numpy as np
import sympy as sp
from scipy.optimize import least_squares
from scipy.spatial.transform import Rotation as Rot
from scipy.stats import unitary_group

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


rng = np.random.default_rng(20260927)
SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]])
SZ = np.array([[1, 0], [0, -1]], complex)
PAULI = [SX, SY, SZ]
I2 = np.eye(2)

# ---------------------------------------------------------------- A flowing walker
k1, k2, k3 = sp.symbols('k1 k2 k3', real=True)
K = (k1, k2, k3)
d_flow = sp.Matrix([sp.sin(k1), sp.sin(k2), sp.sin(k3)])
chis = []
for c in itertools.product((0, 1), repeat=3):
    pt = {k1: c[0] * sp.pi, k2: c[1] * sp.pi, k3: c[2] * sp.pi}
    Jm = d_flow.jacobian(K).subs(pt)
    chis.append((c, sp.sign(Jm.det()), all(v == 0 for v in d_flow.subs(pt))))
check("A: flowing walker: 8 exact nodes at {0,pi}^3, chirality (-1)^(#pi), total 0",
      all(z for _, _, z in chis) and all(ch == (-1) ** sum(c) for c, ch, _ in chis) and sum(ch for _, ch, _ in chis) == 0,
      "; ".join(f"{c}:{int(ch):+d}" for c, ch, _ in chis))


def random_two_band():
    A = [rng.normal(size=(3,)) + 1j * rng.normal(size=(3,)) for _ in range(3)]
    B = rng.normal(size=3)

    def d(k):
        out = B.copy()
        for j in range(3):
            out = out + 2 * np.real(A[j] * np.exp(1j * k[j]))
        return out
    return d


fam_rows = []
g8 = np.linspace(0, 2 * np.pi, 10, endpoint=False)
for fam in range(5):
    d = random_two_band()
    zeros = []
    for k0 in itertools.product(g8, repeat=3):
        r = least_squares(d, np.array(k0), xtol=1e-14, ftol=1e-14, gtol=1e-14)
        if np.linalg.norm(d(r.x)) < 1e-10:
            kz = np.mod(r.x, 2 * np.pi)
            if not any(np.linalg.norm(np.angle(np.exp(1j * (kz - z)))) < 1e-6 for z in zeros):
                zeros.append(kz)
    tot = 0
    for z in zeros:
        Jn = np.zeros((3, 3))
        for c in range(3):
            e = np.zeros(3); e[c] = 1e-6
            Jn[:, c] = (d(z + e) - d(z - e)) / 2e-6
        tot += int(np.sign(np.linalg.det(Jn)))
    fam_rows.append((len(zeros), tot))
check("A: random range-one two-band Hamiltonians: located zeros have total chirality 0 (Nielsen-Ninomiya)",
      all(t == 0 for n, t in fam_rows), "; ".join(f"{n} zeros, total {t}" for n, t in fam_rows))

# ---------------------------------------------------------------- B ticking walker, exact
def S_sym(q, j):
    sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])][j]
    return sp.cos(q) * sp.eye(2) - sp.I * sp.sin(q) * sig


U_sym = S_sym(k1, 0) * S_sym(k2, 1) * S_sym(k3, 2)
a_sym = sp.simplify((U_sym[0, 0] + U_sym[1, 1]) / 2)
sigs = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
b_sym = sp.Matrix([sp.simplify(sp.I * (s * U_sym).trace() / 2) for s in sigs])
node_rows = []
corner_pts = [tuple(c * sp.pi for c in cc) for cc in itertools.product((0, 1), repeat=3)]
half_pts = [tuple(s * sp.pi / 2 for s in ss) for ss in itertools.product((1, -1), repeat=3)]
for pt in corner_pts + half_pts:
    sub = dict(zip(K, pt))
    a0 = sp.simplify(a_sym.subs(sub))
    b0 = [sp.simplify(v) for v in b_sym.subs(sub)]
    if not (a0 in (1, -1) and all(v == 0 for v in b0)):
        continue
    Jm = b_sym.jacobian(K).subs(sub).applyfunc(sp.simplify)
    chi = sp.sign((a0 * Jm).det())   # U ~ a0 (1 - i (a0 J) dk.sigma): local Weyl form about quasi-energy 0 or pi
    node_rows.append((pt, int(a0), int(chi)))
corner_nodes = [r for r in node_rows if r[0] in corner_pts]
half_nodes = [r for r in node_rows if r[0] in half_pts]
ok = (len(corner_nodes) == 8 and all(ch == 1 for _, _, ch in corner_nodes)
      and len(half_nodes) == 8 and all(ch == -1 for _, _, ch in half_nodes)
      and sum(1 for _, a0, _ in corner_nodes if a0 == 1) == 4 and sum(1 for _, a0, _ in half_nodes if a0 == 1) == 4)
check("B: ordered tick U_-: exact nodes: 8 corners right-handed (4 at quasi-energy 0, 4 at pi), "
      "8 points (pi/2)(+-1,+-1,+-1) left-handed (4 at 0, 4 at pi)", ok,
      f"corners {[(tuple(sp.nsimplify(x/sp.pi) for x in p), a0, ch) for p, a0, ch in corner_nodes][:2]}...; "
      f"half points {[(tuple(sp.nsimplify(x/sp.pi) for x in p), a0, ch) for p, a0, ch in half_nodes][:2]}...")


def U_minus(k):
    out = I2.copy()
    for j in range(3):
        out = out @ (np.cos(k[j]) * I2 - 1j * np.sin(k[j]) * PAULI[j])
    return out


def b_of(M):
    return np.array([np.real(1j * np.trace(P @ M) / 2) for P in PAULI])


found = []
for k0 in itertools.product(np.linspace(0, 2 * np.pi, 12, endpoint=False), repeat=3):
    r = least_squares(lambda k: b_of(U_minus(k)), np.array(k0), xtol=1e-14, ftol=1e-14, gtol=1e-14)
    if np.linalg.norm(b_of(U_minus(r.x))) < 1e-10:
        kz = np.mod(r.x, 2 * np.pi)
        if not any(np.linalg.norm(np.angle(np.exp(1j * (kz - z)))) < 1e-6 for z in found):
            found.append(kz)
check("B: numerical root search (12^3 starts) finds exactly these 16 nodes of U_- and no others", len(found) == 16,
      f"{len(found)} distinct nodes")


# ---------------------------------------------------------------- C winding numbers
def W3(Ufun, n):
    ks = (np.arange(n) + 0.5) * 2 * np.pi / n
    h = 1e-5
    tot = 0.0
    eps3 = [((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1), ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)]
    for kk in itertools.product(ks, repeat=3):
        k = np.array(kk)
        Ui = np.linalg.inv(Ufun(k))
        A = []
        for j in range(3):
            e = np.zeros(3); e[j] = h
            A.append(Ui @ (Ufun(k + e) - Ufun(k - e)) / (2 * h))
        tot += sum(sg * np.trace(A[i] @ A[j] @ A[l]) for (i, j, l), sg in eps3)
    # normalised so that the right-handed node U ~ 1 - i k.sigma counts +1 (the trace form gives -1 for it)
    return -np.real(tot) * (2 * np.pi / n) ** 3 / (24 * np.pi ** 2)


def U_flow(k):
    s = np.sin(k)
    r = np.linalg.norm(s)
    return np.cos(r) * I2 - 1j * (np.sinc(r / np.pi)) * sum(s[j] * PAULI[j] for j in range(3))


def U_g(k):
    c, s = np.cos(k), np.sin(k)
    a = c.prod()
    s2 = (s ** 2).sum()
    g = np.sqrt(max(1 - a * a, 0.0) / s2) if s2 > 1e-300 else 1.0
    return a * I2 - 1j * g * sum(s[j] * PAULI[j] for j in range(3))


w_m, w_f, w_g, w_gm = W3(U_minus, 24), W3(U_flow, 24), W3(U_g, 32), W3(lambda k: U_g(k) @ U_minus(k), 32)
check("C: W3(U_-) = 0, W3(exp(-iH)) = 0, W3(U_g) = 4, W3(U_g U_-) = 4",
      abs(w_m) < 1e-6 and abs(w_f) < 1e-6 and abs(w_g - 4) < 1e-3 and abs(w_gm - 4) < 1e-3,
      f"{w_m:.2e}, {w_f:.2e}, {w_g:.5f}, {w_gm:.5f}")


# ---------------------------------------------------------------- D random strictly local ticks
def cond_shift(v, n):
    n = np.asarray(n, float); n = n / np.linalg.norm(n)
    ns = sum(c * P for c, P in zip(n, PAULI))
    return lambda k: np.cos(v @ k) * I2 - 1j * np.sin(v @ k) * ns


def random_product(depth=6):
    fs = []
    for _ in range(depth):
        v = rng.integers(-2, 3, size=3)
        while not v.any():
            v = rng.integers(-2, 3, size=3)
        fs.append(cond_shift(v, rng.normal(size=3)))
        C = unitary_group.rvs(2, random_state=rng)
        fs.append(lambda k, C=C: C)

    def U(k):
        M = I2.copy()
        for f in fs:
            M = M @ f(k)
        return M
    return U


cells = list(itertools.product((0, 1), repeat=3))
ci = {c: i for i, c in enumerate(cells)}


def brick_layer(G, j, parity):
    def M(Kv):
        out = np.zeros((16, 16), complex)
        for c in cells:
            if c[j] != parity:
                continue
            d = list(c); d[j] = (c[j] + 1) % 2; d = tuple(d)
            ph = np.exp(1j * Kv[j]) if parity == 1 else 1.0
            Ph = np.diag([1, 1, ph, ph])
            Gk = Ph.conj() @ G @ Ph
            idx = [2 * ci[c], 2 * ci[c] + 1, 2 * ci[d], 2 * ci[d] + 1]
            for r_ in range(4):
                for s_ in range(4):
                    out[idx[r_], idx[s_]] += Gk[r_, s_]
        return out
    return M


def random_brick(depth=6):
    Ls = [brick_layer(unitary_group.rvs(4, random_state=rng), t % 3, (t // 3) % 2) for t in range(depth)]

    def U(Kv):
        M = np.eye(16, dtype=complex)
        for L in Ls:
            M = L(Kv) @ M
        return M
    return U


d_prod = [W3(random_product(), 16) for _ in range(5)]
d_brick = [W3(random_brick(), 10) for _ in range(3)]
check("D: random strictly local ticks (shift products; brickwork one-body circuits) all have W3 = 0",
      max(abs(x) for x in d_prod + d_brick) < 1e-6,
      f"products {[f'{x:.1e}' for x in d_prod]}; brickwork {[f'{x:.1e}' for x in d_brick]}")


# ---------------------------------------------------------------- E magnetic slab
def slab_ops(L, flux):
    N = L * L
    idx = lambda x, y: (x % L) * L + (y % L)
    Tx = np.zeros((N, N), complex); Ty = np.zeros((N, N), complex)
    for x in range(L):
        for y in range(L):
            Tx[idx(x + 1, y), idx(x, y)] = 1
            Ty[idx(x, y + 1), idx(x, y)] = np.exp(1j * flux * x)
    return Tx, Ty, N


Lm = 12
Tx, Ty, Nm = slab_ops(Lm, 2 * np.pi / Lm)
Pp = [0.5 * (I2 + P) for P in PAULI]; Pm_ = [0.5 * (I2 - P) for P in PAULI]
Sx = np.kron(Tx, Pp[0]) + np.kron(Tx.conj().T, Pm_[0])
Sy = np.kron(Ty, Pp[1]) + np.kron(Ty.conj().T, Pm_[1])
Szop = np.kron(np.eye(Nm), SZ)


def tick_slopes(kz, win=0.35):
    U = Sx @ Sy @ np.kron(np.eye(Nm), np.cos(kz) * I2 - 1j * np.sin(kz) * SZ)
    w, V = np.linalg.eig(U)
    e = -np.angle(w)
    sel = np.where(np.abs(e) < win)[0]
    sl = [np.real(V[:, i].conj() @ Szop @ V[:, i]) / np.real(V[:, i].conj() @ V[:, i]) for i in sel]
    return sum(s > 0.5 for s in sl), sum(s < -0.5 for s in sl), len(sel)


Hx = np.kron(Tx.conj().T, SX / (2j)); Hx = Hx + Hx.conj().T
Hy = np.kron(Ty.conj().T, SY / (2j)); Hy = Hy + Hy.conj().T


def flow_slopes(kz, win=0.35):
    H = Hx + Hy + np.sin(kz) * Szop
    w, V = np.linalg.eigh(H)
    sel = np.where(np.abs(w) < win)[0]
    sl = [np.real(V[:, i].conj() @ (np.cos(kz) * Szop) @ V[:, i]) for i in sel]
    return sum(s > 0.5 for s in sl), sum(s < -0.5 for s in sl), len(sel)


t0, tpi, thalf = tick_slopes(0.0), tick_slopes(np.pi), tick_slopes(np.pi / 2)
f0 = flow_slopes(0.0)
check("E: magnetic slab: tick's quasi-energy-0 states move along +B at k_z = 0, pi and against it at k_z = pi/2; "
      "the flowing walker's move both ways at k_z = 0",
      t0[0] > 0 and t0[1] == 0 and tpi[0] > 0 and tpi[1] == 0 and thalf[0] == 0 and thalf[1] > 0 and f0[0] > 0 and f0[1] > 0,
      f"tick (up, down, total): k_z=0 {t0}, pi {tpi}, pi/2 {thalf}; flowing k_z=0 {f0}")

# ---------------------------------------------------------------- F covariant tick with tails
worst_u = max(np.abs(U_g(k) @ U_g(k).conj().T - I2).max() for k in rng.uniform(0, 2 * np.pi, (200, 3)))
mats = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3))
        for i in range(3):
            R[i, perm[i]] = signs[i]
        if np.linalg.det(R) > 0:
            mats.append(R)
worst_c = 0.0
for R in mats:
    rv = Rot.from_matrix(R).as_rotvec(); th = np.linalg.norm(rv)
    nax = rv / th if th > 0 else np.array([0, 0, 1.0])
    D = np.cos(th / 2) * I2 - 1j * np.sin(th / 2) * sum(nax[j] * PAULI[j] for j in range(3))
    for k in rng.uniform(0, 2 * np.pi, (10, 3)):
        worst_c = max(worst_c, np.abs(U_g(R @ k) - D @ U_g(k) @ D.conj().T).max())
check("F: U_g is unitary and covariant under all 24 proper cubic rotations (spin-1/2 coin)",
      worst_u < 1e-12 and worst_c < 1e-12 and len(mats) == 24, f"unitarity {worst_u:.1e}, covariance {worst_c:.1e}")
# nodes of U_g: b = g s with g > 0 vanishes only where s = 0 (the corners); local form there
g_chis = []
for cc in itertools.product((0, 1), repeat=3):
    k0 = np.array(cc) * np.pi
    a0 = np.real(np.trace(U_g(k0))) / 2
    Jn = np.zeros((3, 3))
    for c in range(3):
        e = np.zeros(3); e[c] = 1e-6
        Jn[:, c] = (b_of(U_g(k0 + e)) - b_of(U_g(k0 - e))) / 2e-6
    g_chis.append(int(np.sign(np.linalg.det(np.sign(a0) * Jn))))
gmin = min(np.sqrt(max(1 - np.cos(k).prod() ** 2, 0) / (np.sin(k) ** 2).sum())
           for k in rng.uniform(0, 2 * np.pi, (20000, 3)))
check("F: U_g's nodes are the 8 corners (g > 0 elsewhere), all right-handed", all(c == 1 for c in g_chis) and gmin > 0,
      f"chiralities {g_chis}; min g over 20000 samples {gmin:.3f}")
n = 256
ks = np.arange(n) * 2 * np.pi / n
KX, KY, KZ = np.meshgrid(ks, ks, ks, indexing='ij')
a_ = np.cos(KX) * np.cos(KY) * np.cos(KZ)
s2_ = np.sin(KX) ** 2 + np.sin(KY) ** 2 + np.sin(KZ) ** 2
g_ = np.sqrt(np.clip(1 - a_ ** 2, 0, None) / np.where(s2_ > 0, s2_, 1)); g_[s2_ == 0] = 1.0
Bx = np.fft.ifftn(g_ * np.sin(KX))
rs = [9, 17, 33, 65]
amps = [abs(Bx[r, 0, 0]) for r in rs]
expo = [np.log(amps[i + 1] / amps[i]) / np.log(rs[i + 1] / rs[i]) for i in range(len(rs) - 1)]
check("F: U_g's amplitude along an axis falls as r^-6 (quasi-local, not strictly local)",
      all(a > 1e-12 for a in amps) and abs(expo[-1] + 6) < 0.3,
      f"|U(r,0,0)| at r = {rs}: {['%.2e' % a for a in amps]}; local exponents {['%.2f' % x for x in expo]}")

print('per_element: exact node locations and Jacobians are checked symbolically.')
print('per_site: not applicable - one-body Bloch operators.')
print('per_mode: Brillouin-zone winding integrals and node censuses are evaluated.')
print('per_block: 12x12 magnetic slab spectra are computed.')
print('lattice_wide: the degree-zero theorem for all strictly local ticks is proved in the note (K-theory), not by the runner.')

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
