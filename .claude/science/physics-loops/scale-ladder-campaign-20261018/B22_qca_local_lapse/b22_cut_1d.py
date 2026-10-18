"""B22 runner 1: causal-cut local lapse for the 1D Dirac walk W = S.C (brickwork form).

Claims tested (labels in the output):
  C1 [exact, trivial]   path independence of cut evolution for a generic (non-free, random-gate)
                        brickwork circuit: any order of legal local advances between two cuts gives
                        the same unitary; legal advances from one cut commute.
  C2 [exact]            Heisenberg row lemma: the single-particle matrix of a cut evolution W_F has
                        row j equal to row j of the uniform evolution by lambda_j layers, lambda_j
                        = number of gates on wire j (causality).
  C3 [exact]            the fixed-operator group commutator C = W_N W_M W_N^-1 W_M^-1 is far from 1
                        (path independence does not make the canonical-picture commutator trivial).
  C4 [exact, massless]  defect lemma: on any cut, adjacent wire counts differ by <= 1, so a cut whose
                        period count changes by T in total has >= T odd-count wires; for theta = 0 the
                        cut map is a permutation that flips chirality exactly on the odd-count wires.
  C5 [numerical]        consequence: with integer-period ("staircase") lapses, the massless
                        group commutator transfers weight to the other chirality and displaces
                        R and L packets in opposite directions, unlike the continuum Dirac-algebra
                        prediction (same displacement -v^2 w for both).  With smooth real lapses
                        (half-period regions) it fails grossly.
"""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qca1d import Brick1D, omega_walk, g1, oo1

PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"\n        {detail}" if detail else ""))


rng = np.random.default_rng(22)
t0 = time.time()

# ---------------------------------------------------------------- C1: generic many-body circuit
Lq = 8                       # qubits on a ring; bonds b = (b, b+1 mod Lq); bond parity = b % 2
def rand_u4():
    z = (rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))) / np.sqrt(2)
    q, r = np.linalg.qr(z); return q * (np.diag(r) / abs(np.diag(r)))
GATES = {}                   # (bond, layer) -> random 4x4, generic and position/time dependent
def gate(b, t):
    if (b, t) not in GATES: GATES[(b, t)] = rand_u4()
    return GATES[(b, t)]
def apply2(psi, U, q1, q2):
    T = psi.reshape([2] * Lq)
    T = np.moveaxis(T, (q1, q2), (0, 1))
    sh = T.shape
    T = (U @ T.reshape(4, -1)).reshape(sh)
    T = np.moveaxis(T, (0, 1), (q1, q2))
    return T.reshape(-1)
# cut = zigzag tau_b (next layer index of bond b); flat: tau_b = b % 2.  Legal move at b:
# tau_{b-1} = tau_{b+1} = tau_b + 1  -> apply gate (b, tau_b), tau_b += 2
def legal(tau):
    return [b for b in range(Lq) if tau[(b - 1) % Lq] == tau[b] + 1 and tau[(b + 1) % Lq] == tau[b] + 1]
def run(order, psi):
    for b, t in order:
        psi = apply2(psi, gate(b, t), b, (b + 1) % Lq)
    return psi
def random_extension(start, target):
    tau = list(start); order = []
    while tau != list(target):
        cand = [b for b in legal(tau) if tau[b] < target[b]]
        b = cand[rng.integers(len(cand))]
        order.append((b, tau[b])); tau[b] += 2
    return order
tau0 = [b % 2 for b in range(Lq)]
worst = 0.0; comm_worst = 0.0; nprobe = 0
for trial in range(6):
    tau = list(tau0)
    for _ in range(int(rng.integers(6, 20))):          # random target cut
        b = rng.choice(legal(tau)); tau[b] += 2
    target = tau
    psi = rng.normal(size=2 ** Lq) + 1j * rng.normal(size=2 ** Lq); psi /= np.linalg.norm(psi)
    ref = run(random_extension(tau0, target), psi)
    for _ in range(5):
        worst = max(worst, np.linalg.norm(run(random_extension(tau0, target), psi) - ref))
    # two legal moves from the same cut commute (disjoint supports)
    lg = legal(target)
    for i in range(len(lg)):
        for j in range(i + 1, len(lg)):
            a, b = lg[i], lg[j]
            p1 = run([(a, target[a]), (b, target[b])], psi); p2 = run([(b, target[b]), (a, target[a])], psi)
            comm_worst = max(comm_worst, np.linalg.norm(p1 - p2)); nprobe += 1
check("C1 [exact, trivial] path independence: 6 random cuts x 6 random move orders, generic random 2-qubit gates on an "
      "8-qubit ring; and legal moves from one cut commute",
      worst < 1e-12 and comm_worst < 1e-12 and nprobe > 0,
      f"max |U_order1 psi - U_order2 psi| = {worst:.2e}; max commutator of co-legal moves = {comm_worst:.2e} ({nprobe} pairs)")

# ---------------------------------------------------------------- C2: Heisenberg row lemma
Lc = 64; th = 0.3
B = Brick1D(Lc, th)
kk = 2 * np.pi / Lc
F = lambda X: 2 * (3.5 + 2.0 * np.sin(kk * X) + 1.2 * np.cos(2 * kk * X))  # layers, > 0 (cut above the flat one)
Fe, Fo = F(B.Xe), F(B.Xo)
assert max(np.abs(np.diff(np.r_[Fe, Fo][np.argsort(np.r_[B.Xe, B.Xo])]))) < 1.0   # slope bound per half cell
Wmat = np.stack([B.apply(np.eye(2 * Lc)[:, j].astype(complex), F) for j in range(2 * Lc)], axis=1)
# wire counts lambda_j
lam = np.zeros(2 * Lc, int)
for t, m, inv in B.ops(F):
    idx = np.where(m)[0]
    if t % 2 == 0: lam[2 * idx] += 1; lam[2 * idx + 1] += 1
    else: lam[2 * idx + 1] += 1; lam[(2 * idx + 2) % (2 * Lc)] += 1
def uniform(nl):
    U = np.eye(2 * Lc, dtype=complex)
    for t in range(nl):
        U = np.stack([B.layer(U[:, j].copy(), t, np.ones(Lc, bool)) for j in range(2 * Lc)], axis=1)
    return U
cache = {}
err = 0.0
for j in range(2 * Lc):
    if lam[j] not in cache: cache[lam[j]] = uniform(lam[j])
    err = max(err, np.abs(Wmat[j] - cache[lam[j]][j]).max())
check("C2 [exact] row j of the cut evolution W_F equals row j of the uniform evolution by lambda_j layers (theta = 0.3, "
      f"Lc = {Lc}, wire counts {lam.min()}..{lam.max()})",
      err < 1e-12 and np.allclose(Wmat.conj().T @ Wmat, np.eye(2 * Lc)), f"max entry deviation {err:.2e}; W_F unitary")

# ---------------------------------------------------------------- C3: canonical-picture commutator is non-trivial
FN = lambda X: 2 * 3 * np.cos(kk * X); FM = lambda X: 2 * 3 * np.sin(kk * X)
Cmat = np.stack([B.group_commutator(np.eye(2 * Lc)[:, j].astype(complex), FN, FM) for j in range(2 * Lc)], axis=1)
nC = np.linalg.norm(Cmat - np.eye(2 * Lc), 2)
check("C3 [exact] the fixed-operator group commutator W_N W_M W_N^-1 W_M^-1 is not the identity (operator norm of C - 1)",
      nC > 0.5, f"||C - 1|| = {nC:.3f} (N = 3 cos, M = 3 sin periods, Lc = {Lc})")

# ---------------------------------------------------------------- C4: defect lemma (massless)
def stair(y, d):
    f = np.floor(y); r = y - f
    return f + np.clip((r - 0.5) / d + 0.5, 0, 1)
B0 = Brick1D(256, 0.0); kk0 = 2 * np.pi / 256
ok4 = True; info = []
for A in (3, 5, 9):
    Fs = lambda X: 2 * stair(A * np.cos(kk0 * X) + 0.37, min(0.9, 1.5 * A * kk0))
    Wp = np.stack([B0.apply(np.eye(512)[:, j].astype(complex), Fs) for j in range(512)], axis=1)
    perm = np.argmax(np.abs(Wp), axis=0)
    is_perm = np.allclose(np.abs(Wp).sum(axis=0), 1) and len(set(perm)) == 512
    lamw = np.zeros(512, int)
    for t, m, inv in B0.ops(Fs):
        idx = np.where(m)[0]
        if t % 2 == 0: lamw[2 * idx] += 1; lamw[2 * idx + 1] += 1
        else: lamw[2 * idx + 1] += 1; lamw[(2 * idx + 2) % 512] += 1
    adj = np.max(np.abs(np.diff(np.r_[lamw, lamw[0]])))
    odd = int(np.sum(lamw % 2))
    nper = np.round(Fs(np.arange(256) + 0.25) / 2).astype(int)
    TV = int(np.sum(np.abs(np.diff(np.r_[nper, nper[0]]))))
    # chirality of flat data: a-sites (even) hold right movers; content of source j sits at perm[j]
    flips = int(np.sum((perm % 2) != (np.arange(512) % 2)))
    # which wires hold flipped content = odd-count wires?
    flipped_targets = set(perm[(perm % 2) != (np.arange(512) % 2)])
    odd_wires = set(np.where(lamw % 2 == 1)[0])
    ok4 &= is_perm and adj <= 1 and odd >= TV and flips == odd and flipped_targets == odd_wires
    info.append(f"A={A}: TV={TV}, odd wires={odd}, chirality flips={flips}, max adjacent count difference={adj}")
check("C4 [exact, massless] cut map is a permutation; adjacent wire counts differ by <= 1; #odd-count wires >= total "
      "variation of the period count; chirality flips occur exactly on the odd-count wires", ok4, "; ".join(info))

# ---------------------------------------------------------------- C5: consequence for the group commutator
Lc = 4096; kk = 2 * np.pi / Lc
rows = []
for th in (0.0, 0.2):
    B = Brick1D(Lc, th); ks = B.kgrid()
    for A in (16, 32, 64):
        d = min(0.9, 1.5 * A * kk)
        FNs = lambda X: 2 * stair(A * np.cos(kk * X), d); FMs = lambda X: 2 * stair(A * np.sin(kk * X), d)
        w = A * A * kk
        for k0 in (0.1, -0.1):
            psi = B.packet(k0, 1000.0, 20.0, +1)
            out = B.group_commutator(psi, FNs, FMs)
            dx = B.xmean(out) - B.xmean(psi)
            Ok = B.to_k(out)
            same = sum(abs(np.vdot(B.band(k, +1)[1], Ok[n])) ** 2 for n, k in enumerate(ks))
            rows.append((th, A, k0, w, dx, -w * g1(k0, th), same))
    if th == 0.0:
        A = 32
        FNr = lambda X: 2 * A * np.cos(kk * X); FMr = lambda X: 2 * A * np.sin(kk * X)
        psi = B.packet(0.1, 1000.0, 20.0, +1)
        out = B.group_commutator(psi, FNr, FMr)
        dx_smooth = B.xmean(out) - B.xmean(psi); w_s = A * A * kk
print("\n  theta    A    k0      w      dx(measured)  -w*g(k0)  same-band weight")
for r in rows:
    print(f"  {r[0]:.1f}  {r[1]:4d}  {r[2]:+.1f}  {r[3]:7.3f}  {r[4]:10.4f}  {r[5]:9.4f}   {r[6]:.4f}")
m = [r for r in rows if r[0] == 0.0]
opp = all(np.sign(m[i][4]) != np.sign(m[i + 1][4]) for i in range(0, len(m), 2))
leak = all(r[6] < 0.99 for r in m)
grow = m[0][6] > m[2][6] > m[4][6]
check("C5 [numerical] massless walk, staircase integer-period lapses N = A cos, M = A sin (uniform w): R (k0=+0.1) and L "
      "(k0=-0.1) packets are displaced in opposite directions and lose weight to the other band, the loss growing with A; "
      "the continuum Dirac-algebra value is -v^2 w for both",
      opp and leak and grow, "")
check("C5b [numerical] massless walk, smooth real lapse (half-period regions): gross failure of the leading-order form",
      abs(dx_smooth) > 5 * w_s, f"A = 32: displacement {dx_smooth:.2f} cells vs -v^2 w = {-w_s:.3f}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}  ({time.time() - t0:.1f} s)")
