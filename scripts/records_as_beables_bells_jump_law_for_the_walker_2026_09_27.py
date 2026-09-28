#!/usr/bin/env python3
"""Records as beables under the moving-records reading: Bell's jump law for the campaign's walker.

Reading tested (supplied, not adopted): the actual world is a configuration of
records (one record per walker, at a site); a unitary wave psi evolves by the
walker's Hamiltonian and is never acted on by the records; a record moves only
to a nearest-neighbour site, with Bell's minimal jump rate

    rate(x -> y) = max(0, J_yx) / P(x),   J_yx = 2 Im[psi_y^dag H_yx psi_x],   P(x) = |psi_x|^2

(for several walkers, x is the joint configuration and the rate of one record's
move is computed from the joint wave). Reference only: J. S. Bell, "Beables for
quantum field theory" (1984); Duerr, Goldstein, Tumulka, Zanghi, "Bell-type
quantum field theories" (2005).

Checks:
A. Equivariance: for the walker H = sum_j sin k_j sigma_j (1D, 2D, 3D), the
   master equation of the jump law reproduces dP/dt of the Schroedinger
   evolution exactly, and every jump is between nearest neighbours.
B. Covariance: under each proper cubic rotation (with the spin-1/2 action on
   the coin) the rate table of the rotated wave is the rotated rate table.
C. No back-action: the records never change psi, so the lattice energy <H> is
   exactly conserved through any number of record moves. This is bookkeeping:
   no energy is assigned to records, and the sharp lock never happens.
D. Bell: two walkers on separate rings with singlet coins; each wing's setting
   is a local coin rotation; the walker's own motion (sigma_z = +1 right,
   -1 left) steers the coin into position; the outcome is read from the record
   alone (right or left of the start). Monte Carlo record trajectories
   reproduce the |psi|^2 correlations and CHSH = 2.79 (2 sqrt 2 times 0.9867:
   each wing's sin k dispersion leaves a small part of its packet on the wrong
   side), far above 2.
E. No signalling: wing B's record statistics do not depend on A's setting.
G. The sea's own records: with antiperiodic (time-reversal-invariant)
   boundaries, in the unique half-filled ground state of the walker sea (1D
   ring of 6, 2D 2x2, 3D 2x2x2), the currents between site-occupation
   configurations vanish: the vacuum's records are at rest. A generic twist
   (0.4 on a ring of 4) breaks time reversal and gives currents although the
   ground state is unique.
F. The price: the odds are not local in the records. After A's coin has
   steered A's record right or left (B frozen), B's instantaneous rates from
   its start site depend on which side A's record is on (an illustration; the
   nonlocality follows from the law's form and Bell's theorem via D).

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys

AUDIT_INPUT_PATHS = (
    'docs/RECORDS_AS_BEABLES_UNDER_THE_MOVING_RECORDS_READING_BELLS_JUMP_LAW_GIVES_NEAREST_NEIGHBOUR_MOVES_EQUIVARIANT_ODDS_AND_BELL_CORRELATIONS_WITH_NONLOCAL_ODDS_BOUNDED_THEOREM_NOTE_2026-09-27.md',
    'docs/DYNAMICS_CLAUSE_BELL_VALUES_OF_RECORD_LAWS_RECORDS_ONLY_FORMATION_STAYS_AT_TWO_THE_DYNAMICS_CLAUSE_REACHES_TWO_ROOT_TWO_BOUNDED_THEOREM_NOTE_2026-09-24.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
)
AUDIT_TIMEOUT_SEC = 900

import numpy as np
from scipy.linalg import expm
from scipy.spatial.transform import Rotation as Rot

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]])
SZ = np.array([[1, 0], [0, -1]], complex)
PAULI = [SX, SY, SZ]
rng = np.random.default_rng(20260927)


def walker(L, dim):
    sites = list(itertools.product(range(L), repeat=dim))
    idx = {s: i for i, s in enumerate(sites)}
    N = len(sites)
    h = np.zeros((2 * N, 2 * N), complex)
    nbr = set()
    for s in sites:
        i = idx[s]
        for j in range(dim):
            t = list(s); t[j] = (t[j] + 1) % L
            k = idx[tuple(t)]
            A = PAULI[j] / (2j)
            h[2 * i:2 * i + 2, 2 * k:2 * k + 2] += A
            h[2 * k:2 * k + 2, 2 * i:2 * i + 2] += A.conj().T
            nbr.add((i, k)); nbr.add((k, i))
    return h, sites, idx, N, nbr


def rates(psi, h, N):
    Q = psi.reshape(N, 2)
    Pr = np.sum(np.abs(Q) ** 2, axis=1)
    hb = h.reshape(N, 2, N, 2)
    J = 2 * np.imag(np.einsum('ya,yaxb,xb->yx', Q.conj(), hb, Q))
    R = np.where(J > 0, J, 0) / np.where(Pr > 1e-300, Pr, np.inf)[None, :]
    np.fill_diagonal(R, 0.0)
    return R, Pr


# ---------------------------------------------------------------- A equivariance, nearest-neighbour jumps
arows = []
for (L, dim) in [(8, 1), (4, 2), (3, 3)]:
    h, sites, idx, N, nbr = walker(L, dim)
    worst = 0.0
    nn = True
    for _ in range(5):
        psi = rng.normal(size=2 * N) + 1j * rng.normal(size=2 * N); psi /= np.linalg.norm(psi)
        R, Pr = rates(psi, h, N)
        dP_schr = 2 * np.real(np.sum((psi.conj() * (-1j * h @ psi)).reshape(N, 2), axis=1))
        dP_jump = R @ Pr - R.sum(axis=0) * Pr
        worst = max(worst, np.abs(dP_schr - dP_jump).max())
        nn = nn and all((x, y) in nbr for y, x in zip(*np.nonzero(R)))
    arows.append((L, dim, worst, nn))
check("A: Bell's jump law reproduces the Schroedinger dP/dt exactly (equivariance), with nearest-neighbour jumps only",
      all(w < 1e-12 and nn for L, d, w, nn in arows), "; ".join(f"{d}D L={L}: max error {w:.1e}" for L, d, w, nn in arows))

# ---------------------------------------------------------------- B covariance under proper cubic rotations
L = 3
h3, sites3, idx3, N3, _ = walker(L, 3)
psi = rng.normal(size=2 * N3) + 1j * rng.normal(size=2 * N3); psi /= np.linalg.norm(psi)
R0, _ = rates(psi, h3, N3)
worst_cov = 0.0
count = 0
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        Rm = np.zeros((3, 3))
        for i in range(3):
            Rm[i, perm[i]] = signs[i]
        if np.linalg.det(Rm) < 0:
            continue
        count += 1
        rv = Rot.from_matrix(Rm).as_rotvec(); th = np.linalg.norm(rv)
        nax = rv / th if th > 0 else np.array([0, 0, 1.0])
        D = np.cos(th / 2) * np.eye(2) - 1j * np.sin(th / 2) * sum(nax[j] * PAULI[j] for j in range(3))
        # rotated wave: psi'(R x) = D psi(x)
        site_map = [idx3[tuple(int(v) % L for v in Rm @ np.array(s))] for s in sites3]
        psi_r = np.zeros_like(psi)
        for i, j in enumerate(site_map):
            psi_r[2 * j:2 * j + 2] = D @ psi[2 * i:2 * i + 2]
        Rr, _ = rates(psi_r, h3, N3)
        worst_cov = max(worst_cov, max(abs(Rr[site_map[y], site_map[x]] - R0[y, x]) for x in range(N3) for y in range(N3)))
check("B: the jump law is covariant under the 24 proper cubic rotations (spin-1/2 coin action)",
      count == 24 and worst_cov < 1e-10, f"{count} rotations; max rate mismatch {worst_cov:.1e}")

# ---------------------------------------------------------------- C no back-action
h1, _, _, N1, _ = walker(12, 1)
psi = rng.normal(size=2 * N1) + 1j * rng.normal(size=2 * N1); psi /= np.linalg.norm(psi)
U = expm(-1j * h1 * 0.05)
E0 = np.real(psi.conj() @ h1 @ psi)
x = int(rng.choice(N1, p=np.sum(np.abs(psi.reshape(N1, 2)) ** 2, axis=1)))
moves = 0
for step in range(400):
    R, Pr = rates(psi, h1, N1)
    tot = R[:, x].sum() * 0.05
    if rng.random() < tot:
        x = int(rng.choice(N1, p=R[:, x] / R[:, x].sum())); moves += 1
    psi = U @ psi
E1 = np.real(psi.conj() @ h1 @ psi)
check("C: by construction the records never act on the wave, so the wave's energy is unaffected by their moves "
      "(bookkeeping: no lock happens in this reading; no energy is assigned to records)", abs(E1 - E0) < 1e-10 and moves > 0,
      f"{moves} record moves; |Delta <H>| = {abs(E1 - E0):.1e}")

# ---------------------------------------------------------------- D, E, F Bell with records alone
Lr = 24; c0 = Lr // 2
hr = np.zeros((2 * Lr, 2 * Lr), complex)
for xx in range(Lr):
    yy = (xx + 1) % Lr; A = SZ / (2j)
    hr[2 * xx:2 * xx + 2, 2 * yy:2 * yy + 2] += A; hr[2 * yy:2 * yy + 2, 2 * xx:2 * xx + 2] += A.conj().T
hloc = hr.reshape(Lr, 2, Lr, 2)


def packet(coin):
    xs = np.arange(Lr); env = np.exp(-(xs - c0) ** 2 / (2 * 1.5 ** 2)); env /= np.linalg.norm(env)
    return np.kron(env, coin)


def Ry(t):
    return np.cos(t / 2) * np.eye(2) - 1j * np.sin(t / 2) * SY


up = np.array([1, 0], complex); dn = np.array([0, 1], complex)
Tend, dt = 8.0, 0.02
nst = int(Tend / dt)
U1 = expm(-1j * hr * dt)
sgnx = np.sign(np.arange(Lr) - c0 + 0.5)


def bell_run(thA, thB, nruns, seed, probe_nonlocal=False):
    r = np.random.default_rng(seed)
    RA = np.kron(np.eye(Lr), Ry(thA)); RB = np.kron(np.eye(Lr), Ry(thB))
    Psi = ((np.kron(RA @ packet(up), RB @ packet(dn)) - np.kron(RA @ packet(dn), RB @ packet(up))) / np.sqrt(2)).reshape(2 * Lr, 2 * Lr)
    Pc = np.einsum('iajb->ij', np.abs(Psi.reshape(Lr, 2, Lr, 2)) ** 2)
    ids = r.choice(Lr * Lr, size=nruns, p=(Pc / Pc.sum()).ravel())
    xa, xb = ids // Lr, ids % Lr
    nonlocal_spread = 0.0
    for step in range(nst):
        Q = Psi.reshape(Lr, 2, Lr, 2)
        P = np.einsum('iajb->ij', np.abs(Q) ** 2)
        JA = 2 * np.imag(np.einsum('yaXb,yaxc,xcXb->yxX', Q.conj(), hloc, Q))
        JB = 2 * np.imag(np.einsum('Xayb,ybxc,Xaxc->yxX', Q.conj(), hloc, Q))
        RAt = np.where(JA > 0, JA, 0) / np.where(P > 1e-300, P, np.inf)[None, :, :]
        RBt = np.where(JB > 0, JB, 0) / np.where(P.T > 1e-300, P.T, np.inf)[None, :, :]
        if probe_nonlocal and step == nst // 2:
            # B's rightward jump rate at a well-populated site xB, with A's record on the right versus the left
            PB = P.sum(axis=0)
            xB0 = int(np.argmax(PB))
            right = np.arange(c0 + 1, Lr); left = np.arange(0, c0)
            wR, wL = P[right, xB0], P[left, xB0]
            yB = (xB0 + 1) % Lr
            rR = np.sum(wR * RBt[yB, xB0, right]) / max(wR.sum(), 1e-300)
            rL = np.sum(wL * RBt[yB, xB0, left]) / max(wL.sum(), 1e-300)
            nonlocal_spread = (rR, rL, xB0)
        for side in (0, 1):
            rt = RAt[:, xa, xb] if side == 0 else RBt[:, xb, xa]
            jump = r.random(nruns) < rt.sum(axis=0) * dt
            if jump.any():
                cum = np.cumsum(rt[:, jump] / rt[:, jump].sum(axis=0), axis=0)
                dest = (cum < r.random(jump.sum())).sum(axis=0)
                if side == 0:
                    xa[jump] = dest
                else:
                    xb[jump] = dest
        Psi = (np.kron(U1, np.eye(2 * Lr)) @ Psi.reshape(-1)).reshape(2 * Lr, 2 * Lr)
        Psi = (np.kron(np.eye(2 * Lr), U1) @ Psi.reshape(-1)).reshape(2 * Lr, 2 * Lr)
    P = np.einsum('iajb->ij', np.abs(Psi.reshape(Lr, 2, Lr, 2)) ** 2)
    sa, sb = np.sign(xa - c0 + 0.5), np.sign(xb - c0 + 0.5)
    return np.mean(sa * sb), np.einsum('i,j,ij->', sgnx, sgnx, P), np.mean(sb), nonlocal_spread


def chsh(E):
    vals = [E[0] + E[1] + E[2] - E[3], E[0] + E[1] - E[2] + E[3], E[0] - E[1] + E[2] + E[3], -E[0] + E[1] + E[2] + E[3]]
    return max(abs(v) for v in vals)


settings = [(0.0, np.pi / 4), (0.0, -np.pi / 4), (np.pi / 2, np.pi / 4), (np.pi / 2, -np.pi / 4)]
nruns = 3000
res = [bell_run(a, b, nruns, 100 + i, probe_nonlocal=(i == 0)) for i, (a, b) in enumerate(settings)]
E_rec = [r_[0] for r_ in res]; E_ex = [r_[1] for r_ in res]
sig = 1 / np.sqrt(nruns)
check("D: outcomes read from records sampled in quantum equilibrium reproduce the |psi|^2 correlations (within 4 sigma) "
      "and CHSH far above 2",
      all(abs(a - b) < 4 * sig for a, b in zip(E_rec, E_ex)) and chsh(E_rec) > 2.6 and abs(chsh(E_ex) - 2.79) < 0.02,
      f"E(records) = {[round(e, 3) for e in E_rec]}; E(|psi|^2) = {[round(e, 4) for e in E_ex]}; "
      f"CHSH records {chsh(E_rec):.3f}, exact {chsh(E_ex):.4f} (2 sqrt 2 = {2*np.sqrt(2):.4f}; the gap is packet overlap)")
mB = [r_[2] for r_ in res]
check("E: no signalling in quantum equilibrium: wing B's record statistics do not depend on A's setting (within 4 sigma)",
      abs(mB[0] - mB[2]) < 4 * np.sqrt(2) * sig and abs(mB[1] - mB[3]) < 4 * np.sqrt(2) * sig,
      f"<s_B> with thA = 0: {mB[0]:+.3f}, {mB[1]:+.3f}; with thA = pi/2: {mB[2]:+.3f}, {mB[3]:+.3f}")
# sequential version: A's record is steered first (B frozen), then B's first-jump odds from its start site
thA, thB = 0.0, np.pi / 4
RA0 = np.kron(np.eye(Lr), Ry(thA)); RB0 = np.kron(np.eye(Lr), Ry(thB))
Psi = ((np.kron(RA0 @ packet(up), RB0 @ packet(dn)) - np.kron(RA0 @ packet(dn), RB0 @ packet(up))) / np.sqrt(2)).reshape(2 * Lr, 2 * Lr)
UA = expm(-1j * hr * Tend)
Psi = (np.kron(UA, np.eye(2 * Lr)) @ Psi.reshape(-1)).reshape(2 * Lr, 2 * Lr)
Q = Psi.reshape(Lr, 2, Lr, 2)
P = np.einsum('iajb->ij', np.abs(Q) ** 2)
JB = 2 * np.imag(np.einsum('Xayb,ybxc,Xaxc->yxX', Q.conj(), hloc, Q))
RBt = np.where(JB > 0, JB, 0) / np.where(P.T > 1e-300, P.T, np.inf)[None, :, :]
right = np.arange(c0 + 1, Lr); left = np.arange(0, c0)
def avg_rate(xs, to):
    w = P[xs, c0]
    return np.sum(w * RBt[to, c0, xs]) / w.sum()
rRR, rLR = avg_rate(right, c0 + 1), avg_rate(left, c0 + 1)
rRL, rLL = avg_rate(right, c0 - 1), avg_rate(left, c0 - 1)
check("F: the price: once A's record has gone right or left, B's instantaneous jump rates from its start site depend "
      "on which (nonlocal odds; the jumps themselves stay nearest-neighbour)",
      abs(rRR - rLR) > 0.2 * max(rRR, rLR) and abs(rRL - rLL) > 0.2 * max(rRL, rLL),
      f"B's rate to the right: {rRR:.3f} if A's record is right, {rLR:.3f} if left; to the left: {rRL:.3f} / {rLL:.3f}")

# ---------------------------------------------------------------- G the sea's own records at rest
import scipy.sparse as sps
import scipy.sparse.linalg as spla


def onebody_twisted(L, dim, phase=np.pi):
    sites = list(itertools.product(range(L), repeat=dim)); idx = {s: i for i, s in enumerate(sites)}; N = len(sites)
    h = np.zeros((2 * N, 2 * N), complex)
    for s_ in sites:
        i = idx[s_]
        for j in range(dim):
            t = list(s_); t[j] += 1; ph = 1.0
            if t[j] == L:
                t[j] = 0; ph = np.exp(1j * phase)
            k = idx[tuple(t)]; A = PAULI[j] / (2j) * ph
            h[2 * i:2 * i + 2, 2 * k:2 * k + 2] += A; h[2 * k:2 * k + 2, 2 * i:2 * i + 2] += A.conj().T
    return h, N


def sea_currents(L, dim, phase=np.pi):
    h, N = onebody_twisted(L, dim, phase); M = 2 * N
    basis = list(itertools.combinations(range(M), N)); index = {c: i for i, c in enumerate(basis)}
    rows, cols, vals = [], [], []
    for j, c in enumerate(basis):
        occ = set(c)
        for p in range(M):
            for q in range(M):
                if h[p, q] == 0 or q not in occ or (p != q and p in occ):
                    continue
                sign = (-1) ** sum(1 for x in occ if x < q)
                new = sorted((occ - {q}) | {p}); sign *= (-1) ** sum(1 for x in new if x < p)
                rows.append(index[tuple(new)]); cols.append(j); vals.append(h[p, q] * sign)
    H = sps.csr_matrix((vals, (rows, cols)), shape=(len(basis), len(basis)))
    w, v = spla.eigsh(H, k=2, which='SA'); o = np.argsort(w); g = v[:, o[0]]
    siteconf = lambda c: tuple(sum(1 for m in c if m // 2 == x) for x in range(N))
    Hc = H.tocoo(); J = {}
    for r_, c_, val in zip(Hc.row, Hc.col, Hc.data):
        A_, B_ = siteconf(basis[r_]), siteconf(basis[c_])
        if A_ != B_:
            J[(A_, B_)] = J.get((A_, B_), 0) + 2 * np.imag(np.conj(g[r_]) * val * g[c_])
    return w[o[1]] - w[o[0]], max(abs(x) for x in J.values())


grows = [(L, d) + sea_currents(L, d) for (L, d) in [(6, 1), (2, 2), (2, 3)]]
gen_gap, gen_J = sea_currents(4, 1, phase=0.4)
check("G: the sea's own records are at rest: with antiperiodic (time-reversal-invariant) boundaries, in the unique ground state of the "
      "half-filled walker sea the currents between site-occupation configurations vanish; a generic twist, which breaks time reversal, "
      "gives currents even with a unique ground state",
      all(gap > 0.1 and mJ < 1e-12 for L, d, gap, mJ in grows) and gen_gap > 0.1 and gen_J > 0.01,
      "; ".join(f"{d}D L={L}: gap {gap:.3f}, max |J| {mJ:.1e}" for L, d, gap, mJ in grows)
      + f"; 1D L=4 with twist 0.4: gap {gen_gap:.3f}, max |J| {gen_J:.3f}")

print('per_element: the jump law and its equivariance are checked on explicit Bloch/real-space operators.')
print('per_site: rates are nearest-neighbour by construction and checked.')
print('per_mode: checked and not executed - the beables are site occupations, not modes; momentum modes enter only through the wave.')
print('per_block: two-walker Monte Carlo on 24-site rings (3000 runs per setting).')
print('lattice_wide: checked and not executed - many-walker seas, creation of records and interacting dynamics are not treated.')
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
