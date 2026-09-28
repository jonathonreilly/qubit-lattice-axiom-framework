#!/usr/bin/env python3
"""A photon from a neighbourhood constraint on Z^3: qubits that obey an ice rule carry a massless light-like pattern.

Question (the owner, 2026-09-28): can the qubits and a neighbourhood rule for
records themselves be the force carriers? Test: an in-framework qubit model
on Z^3 whose only rule is a nearest-neighbour constraint plus nearest-neighbour
moves that keep it; does a massless light-like pattern appear? Reference only
(re-derived here, not imported): quantum spin ice and U(1) quantum link
models (Hermele, Fisher and Balents 2004; Banerjee et al. 2008; Shannon et al.
2012); the single-mode (Feynman-Bijl) bound.

Embedding in Z^3 (a torus of size 2L): a site is typed by how many of its
coordinates are odd.
  vertex (V): none odd;  link (E): one odd (the odd axis is the link's
  direction);  plaquette centre (P): two odd;  cube centre (C): three odd.
The E sites carry the qubits: up/down = the field E = +1/-1 along the link's
positive axis. The V, P and C sites are spectators (no record content here).
  Constraint (ice rule, a Gauss law): at every V site, its six nearest
  neighbours (all E sites) satisfy div E = sum_a (E(v+e_a) - E(v-e_a)) = 0.
  Moves (ring exchange): at every P site, its four in-plane nearest
  neighbours (E sites), when they circulate, flip together (all four
  reversed), which keeps every constraint. Hamiltonian in the constrained
  space: H = -K sum_p F_p + V sum_p F_p^2 (F_p flips plaquette p if
  flippable; V = K is the Rokhsar-Kivelson (RK) point, whose ground state is
  the equal superposition of all constrained configurations of a sector).

PRE-REGISTERED (written before running):
  P1 embedding: every constraint and every move involves only nearest
     neighbours of one V or P site of Z^3.
  P2 the moves preserve the constraint exactly.
  P3 the constrained ensemble (the RK ground state's weights) has transverse
     field fluctuations S_T(q) that stay finite as q -> 0 (S_T at the smallest
     q >= 0.1 of its value at q = pi), with the longitudinal part zero.
  P4 the single-mode bound at the RK point, E_min(q) <= omega_SMA(q) =
     f(q)/S_T(q), goes to zero as q -> 0 with a fitted exponent in [1.7, 2.3]
     (gapless; quadratic at the RK point).
  P5 on the smallest cluster (2x2x2 coarse cells, 24 qubits) exact
     diagonalisation reproduces the single-mode expression and the lowest
     level reached from A|psi0> lies at or below it.
  P6 harmonic (weak-coupling) regime of the same lattice gauge theory: exactly
     two massless polarisations with linear dispersion; random local
     gauge-invariant perturbations keep them massless; a gauge-breaking A^2
     term gaps them.
  FAIL if S_T(q -> 0) -> 0 (no free transverse field) or omega_SMA(q -> 0)
  stays finite.

Checks A-F test P1-P6. Prints one line per check, the N5 resolution lines and
TOTAL: PASS=N FAIL=M.
"""
import itertools
import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg import eigsh

AUDIT_TIMEOUT_SEC = 900

PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


# ---------------------------------------------------------------- A embedding in Z^3
def z3_embedding(L):
    n = 2 * L; ok = True
    kinds = {}
    for s in itertools.product(range(n), repeat=3):
        kinds[s] = sum(c % 2 for c in s)
    E = lambda s: kinds[tuple(c % n for c in s)] == 1
    nv = npl = 0
    for s, k in kinds.items():
        if k == 0:   # vertex: all six nearest neighbours are link sites
            nv += 1
            ok &= all(E(tuple(np.add(s, d))) for d in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)])
        if k == 2:   # plaquette centre: the four in-plane nearest neighbours are link sites
            npl += 1
            even_axis = [a for a in range(3) if s[a] % 2 == 0][0]
            inplane = [a for a in range(3) if a != even_axis]
            ok &= all(E(tuple(np.add(s, sg * np.eye(3, dtype=int)[a]))) for a in inplane for sg in (1, -1))
            # the out-of-plane neighbours are cube centres or vertices? they are not link sites
            ok &= not any(E(tuple(np.add(s, sg * np.eye(3, dtype=int)[even_axis]))) for sg in (1, -1))
    nE = sum(1 for k in kinds.values() if k == 1)
    return ok, nv, npl, nE


ok, nv, npl, nE = z3_embedding(3)
check("A: embedding: the ice rule involves exactly the six nearest neighbours of each all-even site, and each move exactly the four in-plane nearest neighbours of a two-odd site",
      ok and nE == 3 * nv and npl == 3 * nv,
      f"Z^3 torus 6^3: {nv} vertex sites, {nE} link sites (qubits), {npl} plaquette sites; all neighbourhoods as required")


# ---------------------------------------------------------------- coarse-lattice tools
def initial_ice(L):
    r = np.indices((L, L, L))
    return [((-1) ** (r[(a + 1) % 3] + r[(a + 2) % 3])).astype(int) for a in range(3)]


def divergence(E):
    return sum(E[a] - np.roll(E[a], 1, axis=a) for a in range(3))


def plaquette_state(E, a, b, r):   # plaquette in the (a, b) plane with lower corner r
    L = E[0].shape[0]; ea = np.eye(3, dtype=int)[a]; eb = np.eye(3, dtype=int)[b]
    t = lambda v: tuple(np.mod(v, L))
    return (E[a][t(r)], E[b][t(np.add(r, ea))], E[a][t(np.add(r, eb))], E[b][t(r)])


def flip(E, a, b, r):
    L = E[0].shape[0]; ea = np.eye(3, dtype=int)[a]; eb = np.eye(3, dtype=int)[b]
    t = lambda v: tuple(np.mod(v, L))
    for arr, pos in ((E[a], t(r)), (E[b], t(np.add(r, ea))), (E[a], t(np.add(r, eb))), (E[b], t(r))):
        arr[pos] *= -1


def flippable(st):
    return st in ((1, 1, -1, -1), (-1, -1, 1, 1))


def loop_update(E, rng):
    """Long-loop update (uniform over divergence-free configurations): walk along outgoing arrows until a vertex repeats; reverse the loop."""
    L = E[0].shape[0]
    v = tuple(rng.integers(L, size=3)); path = [v]; seen = {v: 0}; links = []
    while True:
        outs = []
        for a in range(3):
            if E[a][v] == 1:                       # link v -> v + e_a points out of v
                outs.append((a, v, tuple(np.mod(np.add(v, np.eye(3, dtype=int)[a]), L))))
            w = tuple(np.mod(np.subtract(v, np.eye(3, dtype=int)[a]), L))
            if E[a][w] == -1:                      # link w -> v stored at w, pointing from v to w
                outs.append((a, w, w))
        a, pos, nxt = outs[rng.integers(len(outs))]
        links.append((a, pos)); v = nxt
        if v in seen:
            for (aa, pp) in links[seen[v]:]:
                E[aa][pp] *= -1
            return
        seen[v] = len(links); path.append(v)


# ---------------------------------------------------------------- B moves preserve the constraint
rng = np.random.default_rng(7)
Lb = 4; Eb = initial_ice(Lb)
for _ in range(2000):
    loop_update(Eb, rng)
viol = 0; nflip = 0
for _ in range(5000):
    a, b = rng.choice(3, 2, replace=False); r = rng.integers(Lb, size=3)
    if flippable(plaquette_state(Eb, a, b, r)):
        flip(Eb, a, b, r); nflip += 1
    viol = max(viol, int(np.abs(divergence(Eb)).max()))
check("B: the ring-exchange moves keep the ice rule exactly (and the loop updates sample only rule-respecting configurations)",
      viol == 0 and nflip > 100, f"{nflip} flips on a 4^3 coarse torus; largest divergence afterwards {viol}")


# ---------------------------------------------------------------- C/D constrained ensemble, S_T(q), single-mode bound
def ensemble(L, nsamp, loops_between, seed):
    rng = np.random.default_rng(seed); E = initial_ice(L)
    for _ in range(L ** 3):
        loop_update(E, rng)
    qs = [2 * np.pi * m / L for m in range(1, L // 2 + 1)]
    ST = np.zeros(len(qs)); SL = np.zeros(len(qs)); rho = 0.0
    pos = np.arange(L)
    for s in range(nsamp):
        for _ in range(loops_between):
            loop_update(E, rng)
        for d in range(3):                       # q along axis d
            other = [a for a in range(3) if a != d]
            for pol in other:                    # transverse polarisations
                Ed = E[pol].sum(axis=tuple(a for a in range(3) if a != d))
                for i, q in enumerate(qs):
                    ST[i] += abs(np.sum(Ed * np.exp(1j * q * pos))) ** 2 / L ** 3 / 6
            El = E[d].sum(axis=tuple(a for a in range(3) if a != d))
            for i, q in enumerate(qs):
                SL[i] += abs(np.sum(El * np.exp(1j * q * (pos + 0.5)))) ** 2 / L ** 3 / 3
        fl_all = []
        for (a, b) in ((0, 1), (1, 2), (2, 0)):
            st0 = E[a]; st1 = np.roll(E[b], -1, axis=a); st2 = np.roll(E[a], -1, axis=b); st3 = E[b]
            fl = ((st0 == 1) & (st1 == 1) & (st2 == -1) & (st3 == -1)) | ((st0 == -1) & (st1 == -1) & (st2 == 1) & (st3 == 1))
            fl_all.append(fl.mean())
        rho += np.mean(fl_all)
    return np.array(qs), ST / nsamp, SL / nsamp, rho / nsamp

ens = {L: ensemble(L, 400, L ** 3 // 8, seed=L) for L in (8, 12)}
qs8, ST8, SL8, rho8 = ens[8]; qs12, ST12, SL12, rho12 = ens[12]
check("C: the constrained ensemble has a free transverse field: S_T(q) stays finite as q -> 0 while the longitudinal part is exactly zero (P3)",
      SL8.max() < 1e-20 and SL12.max() < 1e-20 and ST8[0] >= 0.1 * ST8[-1] and ST12[0] >= 0.1 * ST12[-1],
      f"L=8: S_T at q = {np.round(qs8, 3).tolist()}: {np.round(ST8, 3).tolist()}, max S_L {SL8.max():.1e}; "
      f"L=12: S_T at q = {np.round(qs12, 3).tolist()}: {np.round(ST12, 3).tolist()}; flippable fraction {rho8:.3f}, {rho12:.3f}")

K = 1.0
qall = np.concatenate([qs8, qs12]); Sall = np.concatenate([ST8, ST12]); rall = np.concatenate([[rho8] * len(qs8), [rho12] * len(qs12)])
omega = 8 * K * rall * np.sin(qall / 2) ** 2 / Sall       # f(q)/S_T(q), f per cell = (K/2) rho * 16 sin^2(q/2)
small = qall < 1.6
slope = np.polyfit(np.log(qall[small]), np.log(omega[small]), 1)[0]
check("D: the single-mode bound at the RK point goes to zero at long wavelength, quadratically: the constrained qubits have gapless light-like excitations (P4)",
      1.7 <= slope <= 2.3 and omega[np.argmin(qall)] < 0.2 * omega[np.argmax(qall)],
      f"omega_SMA(q)/K: " + ", ".join(f"q={q:.3f}: {w:.4f}" for q, w in sorted(zip(qall, omega))) + f"; fitted exponent {slope:.2f}")


# ---------------------------------------------------------------- E exact diagonalisation on 2x2x2
def enumerate_ice_fast(L, chunk=1 << 20):
    nl = 3 * L ** 3; goods = []
    for start in range(0, 2 ** nl, chunk):
        b = np.arange(start, min(start + chunk, 2 ** nl), dtype=np.int64)
        bitsarr = (((b[:, None] >> np.arange(nl)) & 1) * 2 - 1).astype(np.int8)
        Es = [bitsarr[:, a * L ** 3:(a + 1) * L ** 3].reshape(-1, L, L, L) for a in range(3)]
        div = sum(Es[a].astype(np.int16) - np.roll(Es[a], 1, axis=a + 1) for a in range(3))
        goods.append(b[~np.any(div.reshape(len(b), -1), axis=1)])
    b = np.concatenate(goods)
    bitsarr = (((b[:, None] >> np.arange(nl)) & 1) * 2 - 1).astype(int)
    return b, [bitsarr[:, a * L ** 3:(a + 1) * L ** 3].reshape(-1, L, L, L) for a in range(3)]

Ld = 2
codes, Es = enumerate_ice_fast(Ld)
index = {int(c): i for i, c in enumerate(codes)}; nconf = len(codes)
plaqs = [(a, b_, r) for (a, b_) in ((0, 1), (1, 2), (2, 0)) for r in itertools.product(range(Ld), repeat=3)]
rows, cols = [], []; flipcount = np.zeros(nconf)
for i in range(nconf):
    E = [Es[a][i].copy() for a in range(3)]
    for (a, b_, r) in plaqs:
        if flippable(plaquette_state(E, a, b_, r)):
            flip(E, a, b_, r)
            code = sum(((1 if E[aa].reshape(-1)[j] == 1 else 0) << (aa * Ld ** 3 + j)) for aa in range(3) for j in range(Ld ** 3))
            rows.append(index[code]); cols.append(i); flipcount[i] += 1
            flip(E, a, b_, r)
F = sps.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(nconf, nconf))
H = -K * F + K * sps.diags(flipcount)      # RK point V = K: sum_p F_p^2 counts flippable plaquettes
# ground state in the sector of the zero-flux reference configuration: connected component of the initial ice state
ref = initial_ice(Ld); refcode = sum(((1 if ref[aa].reshape(-1)[j] == 1 else 0) << (aa * Ld ** 3 + j)) for aa in range(3) for j in range(Ld ** 3))
comp = {index[refcode]}; frontier = [index[refcode]]; Fc = F.tocsc()
while frontier:
    new = []
    for i in frontier:
        for j in Fc[:, i].indices:
            if j not in comp:
                comp.add(j); new.append(j)
    frontier = new
comp = sorted(comp); Hs = H[comp][:, comp]
psi0 = np.ones(len(comp)) / np.sqrt(len(comp))
e0 = float(psi0 @ (Hs @ psi0))
# SMA operator: A = sum_r E_y(r) e^{i q x}, q = pi along x (coarse)
q = np.pi
Ey = Es[1][comp]; A = (Ey * np.exp(1j * q * np.arange(Ld))[None, :, None, None]).sum(axis=(1, 2, 3))
phi = A * psi0; overlap = np.vdot(psi0, phi); phi = phi - overlap * psi0; nrm = np.vdot(phi, phi).real
e_sma_direct = float(np.vdot(phi, Hs @ phi).real / nrm - e0)
lowest_exc = float(np.sort(np.linalg.eigvalsh(Hs.toarray()))[1] - e0)
flip_frac = float(np.mean(flipcount[comp] > 0))
rho_xy = []
for i in comp:
    E = [Es[a][i] for a in range(3)]
    rho_xy.append(np.mean([flippable(plaquette_state(E, 0, 1, r)) for r in itertools.product(range(Ld), repeat=3)]))
f_formula = 8 * K * np.mean(rho_xy) * np.sin(q / 2) ** 2
S_formula = nrm / Ld ** 3
e_sma_formula = f_formula / S_formula
# Lanczos from phi within its symmetry sector: lowest Ritz value from the Krylov space of phi
kry = [phi / np.sqrt(nrm)]; Hm = Hs.astype(complex)
T = np.zeros((40, 40)); beta = 0.0; vprev = np.zeros_like(kry[0]); v = kry[0]
m = 0
for m in range(40):
    w = Hm @ v - beta * vprev; alpha = np.vdot(v, w).real; w = w - alpha * v
    w = w - np.vdot(psi0, w) * psi0          # keep the ground state out (it is exactly degenerate-free here; rounding would reintroduce it)
    for u in kry:
        w = w - np.vdot(u, w) * u
    T[m, m] = alpha; beta = np.linalg.norm(w)
    if beta < 1e-10 or m == 39:
        break
    T[m, m + 1] = T[m + 1, m] = beta; vprev, v = v, w / beta; kry.append(v)
ritz = np.linalg.eigvalsh(T[:m + 1, :m + 1])[0] - e0
check("E: exact diagonalisation on 2x2x2 coarse cells (24 qubits): the RK ground state has energy zero, the single-mode expression matches the direct expectation, and the lowest level reached from A|psi0> lies at or below it (P5)",
      abs(e0) < 1e-10 and abs(e_sma_direct - e_sma_formula) < 1e-9 and lowest_exc - 1e-9 <= ritz <= e_sma_direct + 1e-9,
      f"{nconf} ice configurations, {len(comp)} in the reference sector; E0 = {e0:.1e}; <psi0|A|psi0> = {abs(overlap):.1e}; SMA at q = pi: direct {e_sma_direct:.6f}, formula {e_sma_formula:.6f}; "
      f"lowest level reached from A|psi0> {ritz:.6f}; lowest excitation of the sector {lowest_exc:.6f}")


# ---------------------------------------------------------------- F harmonic regime: protected massless photons
def curl_matrix(k):
    ph = 2 * np.sin(k / 2)
    return np.array([[0, -ph[2], ph[1]], [ph[2], 0, -ph[0]], [-ph[1], ph[0], 0]], complex)


def spectrum(k, W, Z, m2=0.0):
    C = curl_matrix(k); Kmat = C.conj().T @ W(k) @ C + m2 * np.eye(3)
    ph = 2 * np.sin(k / 2); nrm_ = np.linalg.norm(ph)
    if nrm_ < 1e-12:
        P = np.eye(3)
    else:
        u = ph / nrm_; P = np.eye(3) - np.outer(u, u)       # transverse projector (the Gauss law removes the longitudinal E)
    Zk = Z(k); Zt = P @ Zk @ P
    ev, U = np.linalg.eigh(Zt); keep = ev > 1e-9
    Zh = U[:, keep] @ np.diag(np.sqrt(ev[keep])) @ U[:, keep].conj().T
    w2 = np.linalg.eigvalsh(Zh @ P @ Kmat @ P @ Zh)
    return np.sqrt(np.clip(np.sort(w2)[-2:], 0, None))     # two transverse modes


rngF = np.random.default_rng(11)
Bw = rngF.normal(size=(4, 3, 3)); Bz = rngF.normal(size=(4, 3, 3))
Wloc = lambda k: np.eye(3) + 0.3 * sum((B @ B.T) * np.cos(k[i % 3]) ** 2 for i, B in enumerate(Bw))
Zloc = lambda k: (np.eye(3) + 0.3 * sum((B @ B.T) * np.cos(k[(i + 1) % 3]) ** 2 for i, B in enumerate(Bz)))
I3 = lambda k: np.eye(3)
kdir = np.array([1.0, 0.37, 0.21]); kdir /= np.linalg.norm(kdir)
ks = [0.4, 0.2, 0.1, 0.05]
pure = [spectrum(t * kdir, I3, I3) for t in ks]
pert = [spectrum(t * kdir, Wloc, Zloc) for t in ks]
mass = [spectrum(t * kdir, Wloc, Zloc, m2=0.05) for t in ks]
lin = [p[0] / t for p, t in zip(pure, ks)]
check("F: harmonic regime: exactly two massless polarisations with linear dispersion; random local gauge-invariant perturbations keep them massless; a gauge-breaking A^2 term gaps them (P6)",
      all(abs(x - 1) < 0.01 for x in lin) and all(abs((p.max() / t) / (pert[-1].max() / ks[-1]) - 1) < 0.1 for p, t in zip(pert, ks)) and mass[-1].min() > 0.1,
      f"pure: omega/|k| at |k| = {ks}: {[round(x, 4) for x in lin]}; perturbed (gauge-invariant): omega/|k| = {[round(p.max() / t, 4) for p, t in zip(pert, ks)]}; "
      f"with A^2 mass: min omega {[round(p.min(), 4) for p in mass]}")

print("per_element: the constraint and each ring-exchange move are checked on explicit Z^3 neighbourhoods and on explicit configurations.")
print("per_site: every vertex site's six neighbours and every plaquette site's four in-plane neighbours are verified to be link (qubit) sites.")
print("per_mode: transverse and longitudinal structure factors at each lattice momentum; harmonic modes from explicit 3x3 symbols.")
print("per_block: exact diagonalisation of the 24-qubit cluster; loop Monte Carlo on 8^3 and 12^3 coarse tori (1536 and 5184 qubits).")
print("lattice_wide: checked and not executed - the linear photon away from the RK point in the full quantum model needs quantum Monte Carlo (not run).")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
