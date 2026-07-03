"""Record-dominated regime: the pointer-sector transport generator and the vacuous link generator.

Gauge-link dynamics frontier (campaign block 03, route R-A continuation: the
compression/averaging level). Two sibling results bound the matter-induced
composite link U_eff = polar(M(x,y)) (the cross-site matter-bilinear
unitarization, COLOR_LINK_INDEX_ROUTING... note):

  - block 01 (INDUCED_COMPOSITE_LINK_TRAJECTORY... note, on main): the induced
    link trajectory exists and is locally covariant but is NOT autonomous in
    U_eff (the increment consumes discarded matter data).
  - block 02 (RECORD_INSTRUMENT_COMPOSITE_LINK... note, PR #3425): under named
    record instruments, the link carrier M(x,y) is erased content; in the
    record-dominated regime the link is slaved/frozen and the pointer-sector
    flow is the autonomous object at leading order.

This block asks the compression-level question exactly: in the record-dominated
regime, IS there an autonomous continuous/discrete generator, and on WHAT
carrier? The answer, exact at full record strength on a single edge:

  - the LOCAL COLOR DENSITIES (pointer sector) carry an exact autonomous CPTP
    transport map (a random-unitary channel), gauge-covariant, with a strict
    Lyapunov monotone (arrow) and an admitted rate -- a genuine generator;
  - the composite LINK's induced generator is exactly the identity (frozen) for
    cos(2 tau) > 0 and a Z_2 flip for cos(2 tau) < 0: it carries NO arrow and NO
    rate -- the vacuous (F = 0) generator. The only link "flow" is isotropic
    contraction of the source magnitude toward degeneracy.

So the record-dominated matter compression realizes the continuous-generator residual
as a COLOR-DENSITY (pointer-sector) transport generator with the link as its
frozen, covariantly-transported coefficient -- NOT as a dynamics of the link.
Honest negatives: the generator's covariance is INHERITED from the color-blind
total-occupation instrument; the frame-naming occupation-basis instrument breaks
it, so no einselection-selection is discharged. The rate and the background V
are admitted/frozen; the link-generator residual is shaped, not delivered.

Exact finite-dimensional model. One-body space = (sites) x C^3 (the supplied
per-site C^3 color carrier; MR_color residual). H_edge = kappa [[0,V],[V^dag,0]]
with V unitary (free V = I, or a frozen generic SU(3) background); H^2 = kappa^2,
so e^{-iH tau} = cos(kappa tau) - i sin(kappa tau) H/kappa exactly (kappa = 1).
The record step is the block-02 partial-strength Lueders instrument
rho -> (1-lam) rho + lam sum_P P rho P.

Memory-safe: <= 12x12 dense matrices, no eigendecomposition of large objects,
no Monte-Carlo fits. Prints "TOTAL: PASS=N FAIL=0" on success.
"""
from __future__ import annotations

import numpy as np

rng = np.random.default_rng(20260609)
TOL = 1e-12
PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] {name}" + (f"  ({detail})" if detail else ""))


def info(name: str, detail: str) -> None:
    print(f"  [INFO] {name}  ({detail})")


# ----------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------

def rand_unitary(n: int) -> np.ndarray:
    z = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    return q * (d / np.abs(d))


def rand_su(n: int) -> np.ndarray:
    u = rand_unitary(n)
    return u / np.linalg.det(u) ** (1.0 / n)


def rand_psd(n: int, scale: float = 1.0) -> np.ndarray:
    a = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    h = a @ a.conj().T
    h = h / np.linalg.norm(h, 2) * scale
    return h


def rand_density_block(n: int, scale: float = 0.4) -> np.ndarray:
    """A Hermitian one-body density block with eigenvalues in (0, 1)."""
    h = rand_psd(n, scale=scale)
    ev = np.linalg.eigvalsh(h)
    # rescale spectrum into (0.05, 0.95)
    lo, hi = ev.min(), ev.max()
    if hi - lo < 1e-9:
        return 0.5 * np.eye(n, dtype=complex)
    u, s, _ = np.linalg.svd(h)
    s2 = 0.05 + 0.9 * (s - s.min()) / (s.max() - s.min())
    return (u * s2) @ u.conj().T


def polar_u(m: np.ndarray) -> np.ndarray:
    """Unitary polar factor U of m = U |m| (|m| = (m^dag m)^{1/2})."""
    u, _, vh = np.linalg.svd(m)
    return u @ vh


def edge_hamiltonian(V: np.ndarray, kappa: float = 1.0) -> np.ndarray:
    n = V.shape[0]
    H = np.zeros((2 * n, 2 * n), dtype=complex)
    H[:n, n:] = kappa * V
    H[n:, :n] = kappa * V.conj().T
    return H


def expm_edge(V: np.ndarray, tau: float, kappa: float = 1.0) -> np.ndarray:
    """exp(-i H tau) for the edge Hamiltonian, via the exact H^2 = kappa^2 identity."""
    n = V.shape[0]
    H = edge_hamiltonian(V, kappa)
    return np.cos(kappa * tau) * np.eye(2 * n, dtype=complex) - 1j * np.sin(kappa * tau) / kappa * H


def assemble_rho(Pxx: np.ndarray, Pyy: np.ndarray, Mxy: np.ndarray) -> np.ndarray:
    n = Pxx.shape[0]
    rho = np.zeros((2 * n, 2 * n), dtype=complex)
    rho[:n, :n] = Pxx
    rho[n:, n:] = Pyy
    rho[:n, n:] = Mxy
    rho[n:, :n] = Mxy.conj().T
    return rho


def blocks(rho: np.ndarray, n: int):
    return rho[:n, :n], rho[n:, n:], rho[:n, n:]


# Lueders instruments at the per-site occupancy level (block-02 frame-naming occupation-basis instrument / color-blind total-occupation instrument), here
# acting on the one-body density blocks (the Fock-level closure is the block-02
# result; reused as method).

def instrument_IA(Pxx: np.ndarray, Pyy: np.ndarray, Mxy: np.ndarray, lam: float):
    """Per-site occupation-basis dephasing: damps off-diagonal of each local block
    and damps the cross block. Frame-naming (local color-frame redundancy-shaped)."""
    dPxx = (1 - lam) * Pxx + lam * np.diag(np.diag(Pxx))
    dPyy = (1 - lam) * Pyy + lam * np.diag(np.diag(Pyy))
    dMxy = (1 - lam) * Mxy  # both endpoints instrumented -> (1-lam)^2 below
    dMxy = (1 - lam) * dMxy
    return dPxx, dPyy, dMxy


def instrument_IB(Pxx: np.ndarray, Pyy: np.ndarray, Mxy: np.ndarray, lam: float):
    """Per-site total-occupation Lueders: preserves the full local color density,
    damps the cross block. Color-blind (names no frame)."""
    dMxy = (1 - lam) * (1 - lam) * Mxy
    return Pxx.copy(), Pyy.copy(), dMxy


def hamiltonian_step(Pxx, Pyy, Mxy, V, tau, kappa=1.0):
    n = V.shape[0]
    U = expm_edge(V, tau, kappa)
    rho = assemble_rho(Pxx, Pyy, Mxy)
    rho2 = U @ rho @ U.conj().T
    return blocks(rho2, n)


def composite_step(Pxx, Pyy, Mxy, V, tau, lam, instrument, kappa=1.0):
    Pxx, Pyy, Mxy = instrument(Pxx, Pyy, Mxy, lam)
    return hamiltonian_step(Pxx, Pyy, Mxy, V, tau, kappa)


# Closed leading/exact pointer map (the candidate autonomous generator)

def pointer_map(Pxx, Pyy, V, tau):
    c2 = np.cos(tau) ** 2
    s2 = np.sin(tau) ** 2
    Pxx2 = c2 * Pxx + s2 * (V @ Pyy @ V.conj().T)
    Pyy2 = c2 * Pyy + s2 * (V.conj().T @ Pxx @ V)
    return Pxx2, Pyy2


def source_s(Pxx, Pyy, V):
    # s = i ( Pxx V - V Pyy ) = -i ( V Pyy - Pxx V )
    return 1j * (Pxx @ V - V @ Pyy)


def imbalance_D(Pxx, Pyy, V):
    return Pxx - V @ Pyy @ V.conj().T


def fn(a):
    return float(np.linalg.norm(a))


# ----------------------------------------------------------------------------
print("=" * 78)
print("PART A -- exact lam=1 closed autonomous pointer map (single edge)")
print("=" * 78)

n = 3
V = rand_su(n)
Vfree = np.eye(n, dtype=complex)

# A1: H^2 = kappa^2 identity, exact polynomial exponential vs scipy-free eigh
H = edge_hamiltonian(V)
check("A1 H_edge^2 = I (kappa=1)", fn(H @ H - np.eye(2 * n)) < TOL, f"{fn(H @ H - np.eye(2*n)):.2e}")
# exact exponential vs eigendecomposition (independent method)
w, Q = np.linalg.eigh(H)
tau0 = 0.37
Uexp_eig = Q @ np.diag(np.exp(-1j * w * tau0)) @ Q.conj().T
check("A1b exact polynomial exp(-iH tau) vs eigh", fn(expm_edge(V, tau0) - Uexp_eig) < TOL,
      f"{fn(expm_edge(V, tau0) - Uexp_eig):.2e}")

# A2/A3: at lam=1, the full composite step's local blocks equal the closed pointer map
maxdev_xx = 0.0
maxdev_yy = 0.0
for _ in range(12):
    Pxx = rand_density_block(n)
    Pyy = rand_density_block(n)
    Mxy = rand_density_block(n) * 0.3  # arbitrary cross block; erased at lam=1
    tau = float(rng.uniform(0.1, 1.4))
    P2, Pyy_next, _ = composite_step(Pxx, Pyy, Mxy, V, tau, lam=1.0, instrument=instrument_IB)
    Pm, Rm = pointer_map(Pxx, Pyy, V, tau)
    maxdev_xx = max(maxdev_xx, fn(P2 - Pm))
    maxdev_yy = max(maxdev_yy, fn(Pyy_next - Rm))
check("A2 lam=1 step M(x,x)' = cos^2 M(x,x) + sin^2 V M(y,y) V^dag", maxdev_xx < 1e-11, f"{maxdev_xx:.2e}")
check("A3 lam=1 step M(y,y)' = cos^2 M(y,y) + sin^2 V^dag M(x,x) V", maxdev_yy < 1e-11, f"{maxdev_yy:.2e}")

# A4: the pointer map is a random-unitary channel (convex combo of identity and
# conjugation by the unitary W = [[0,V],[V^dag,0]]) -> CPTP, hence CP and TP.
W = np.zeros((2 * n, 2 * n), dtype=complex)
W[:n, n:] = V
W[n:, :n] = V.conj().T
check("A4a W unitary", fn(W @ W.conj().T - np.eye(2 * n)) < TOL, f"{fn(W @ W.conj().T - np.eye(2*n)):.2e}")
# conjugation-by-W component reproduces the swap-conjugation (V Pyy V^dag, V^dag Pxx V)
Pxx = rand_density_block(n)
Pyy = rand_density_block(n)
rho_diag = assemble_rho(Pxx, Pyy, np.zeros((n, n), dtype=complex))
wconj = W @ rho_diag @ W.conj().T
swap_xx, swap_yy, _ = blocks(wconj, n)
check("A4b conj-by-W = (V M(y,y) V^dag, V^dag M(x,x) V)",
      fn(swap_xx - V @ Pyy @ V.conj().T) < TOL and fn(swap_yy - V.conj().T @ Pxx @ V) < TOL,
      f"{max(fn(swap_xx - V @ Pyy @ V.conj().T), fn(swap_yy - V.conj().T @ Pxx @ V)):.2e}")
# trace preserving + PSD preserving on random PSD joint inputs
tp_ok = True
psd_ok = True
for _ in range(20):
    Pxx = rand_density_block(n)
    Pyy = rand_density_block(n)
    tau = float(rng.uniform(0.05, 1.5))
    Pm, Rm = pointer_map(Pxx, Pyy, V, tau)
    tp_ok &= abs((np.trace(Pm) + np.trace(Rm)) - (np.trace(Pxx) + np.trace(Pyy))) < 1e-11
    psd_ok &= (np.linalg.eigvalsh(Pm).min() > -1e-11) and (np.linalg.eigvalsh(Rm).min() > -1e-11)
check("A4c pointer map trace-preserving (total occupation conserved)", tp_ok)
check("A4d pointer map PSD-preserving (CP: random-unitary channel)", psd_ok)

# A5: gauge covariance under joint local rotation (g_x, g_y) with V -> g_x V g_y^dag
gx = rand_su(n)
gy = rand_su(n)
Vp = gx @ V @ gy.conj().T
maxdev_cov = 0.0
for _ in range(8):
    Pxx = rand_density_block(n)
    Pyy = rand_density_block(n)
    tau = float(rng.uniform(0.1, 1.3))
    Pm, Rm = pointer_map(Pxx, Pyy, V, tau)
    Pm_g, Rm_g = pointer_map(gx @ Pxx @ gx.conj().T, gy @ Pyy @ gy.conj().T, Vp, tau)
    maxdev_cov = max(maxdev_cov, fn(Pm_g - gx @ Pm @ gx.conj().T), fn(Rm_g - gy @ Rm @ gy.conj().T))
check("A5 pointer generator joint-locally gauge covariant", maxdev_cov < 1e-11, f"{maxdev_cov:.2e}")

# ----------------------------------------------------------------------------
print("=" * 78)
print("PART B -- Lyapunov arrow, fixed-point manifold, rate")
print("=" * 78)

# B1: imbalance D = M(x,x) - V M(y,y) V^dag contracts exactly: D' = cos(2 tau) D
maxdev_D = 0.0
for _ in range(12):
    Pxx = rand_density_block(n)
    Pyy = rand_density_block(n)
    tau = float(rng.uniform(0.05, 1.5))
    Pm, Rm = pointer_map(Pxx, Pyy, V, tau)
    D = imbalance_D(Pxx, Pyy, V)
    Dp = imbalance_D(Pm, Rm, V)
    maxdev_D = max(maxdev_D, fn(Dp - np.cos(2 * tau) * D))
check("B1 imbalance D' = cos(2 tau) D (exact)", maxdev_D < 1e-11, f"{maxdev_D:.2e}")

# B2: Lyapunov L = ||D||^2 strictly decreasing off-balance for tau in (0, pi/2)
strict = True
for tau in np.linspace(0.05, np.pi / 2 - 0.05, 25):
    Pxx = rand_density_block(n)
    Pyy = rand_density_block(n)
    D = imbalance_D(Pxx, Pyy, V)
    L = fn(D) ** 2
    Pm, Rm = pointer_map(Pxx, Pyy, V, tau)
    Lp = fn(imbalance_D(Pm, Rm, V)) ** 2
    ratio = Lp / L
    strict &= ratio < 1.0 - 1e-9 or abs(ratio - np.cos(2 * tau) ** 2) < 1e-9
check("B2 Lyapunov L=||D||^2 strictly decreasing off-balance (tau in (0,pi/2))", strict)
# endpoints: tau=0 (no evolution) and tau=pi/2 (||D|| preserved) are the non-contracting cases
Pxx = rand_density_block(n)
Pyy = rand_density_block(n)
L0 = fn(imbalance_D(Pxx, Pyy, V)) ** 2
Pm, Rm = pointer_map(Pxx, Pyy, V, np.pi / 2)
Lpi2 = fn(imbalance_D(Pm, Rm, V)) ** 2
check("B2b tau=pi/2 preserves ||D|| (full-swap oscillation, not contraction)", abs(Lpi2 - L0) < 1e-10, f"{abs(Lpi2-L0):.2e}")

# B3: fixed-point manifold M(x,x) = V M(y,y) V^dag is exactly fixed
Pyy = rand_density_block(n)
Pxx_fixed = V @ Pyy @ V.conj().T
tau = 0.6
Pm, Rm = pointer_map(Pxx_fixed, Pyy, V, tau)
check("B3 balance manifold M(x,x)=V M(y,y) V^dag is a fixed point", fn(Pm - Pxx_fixed) < TOL and fn(Rm - Pyy) < TOL,
      f"{max(fn(Pm - Pxx_fixed), fn(Rm - Pyy)):.2e}")

# B4: iterate relaxes monotonically to the balance manifold (arrow), rate cos(2 tau)
Pxx = rand_density_block(n)
Pyy = rand_density_block(n)
tau = 0.45
Ls = []
Pc, Rc = Pxx.copy(), Pyy.copy()
for _ in range(40):
    Ls.append(fn(imbalance_D(Pc, Rc, V)) ** 2)
    Pc, Rc = pointer_map(Pc, Rc, V, tau)
monotone = all(Ls[i + 1] <= Ls[i] + 1e-12 for i in range(len(Ls) - 1))
check("B4 iterate monotonically relaxes to balance (record arrow)", monotone and Ls[-1] < 1e-3 * Ls[0],
      f"L0={Ls[0]:.3e} L40={Ls[-1]:.3e}")
info("B4 rate", f"||D|| per-step factor = cos(2*0.45) = {np.cos(2*0.45):.4f}")

# ----------------------------------------------------------------------------
print("=" * 78)
print("PART C -- the link's induced generator is vacuous (frozen / Z_2 flip)")
print("=" * 78)

# C1: source s' = cos(2 tau) s (exact)
maxdev_s = 0.0
for _ in range(12):
    Pxx = rand_density_block(n)
    Pyy = rand_density_block(n)
    tau = float(rng.uniform(0.05, 1.5))
    Pm, Rm = pointer_map(Pxx, Pyy, V, tau)
    s = source_s(Pxx, Pyy, V)
    sp = source_s(Pm, Rm, V)
    maxdev_s = max(maxdev_s, fn(sp - np.cos(2 * tau) * s))
check("C1 link source s' = cos(2 tau) s (exact)", maxdev_s < 1e-11, f"{maxdev_s:.2e}")

# C2: U_eff = polar(s) frozen for cos(2 tau)>0; Z_2 flip for cos(2 tau)<0
froz = True
flip = True
for _ in range(8):
    Pxx = rand_density_block(n)
    Pyy = rand_density_block(n)
    s = source_s(Pxx, Pyy, V)
    if np.linalg.matrix_rank(np.round(s, 9)) < n:
        continue
    U0 = polar_u(s)
    # tau in (0, pi/4): cos(2tau)>0
    tau_p = 0.3
    Pm, Rm = pointer_map(Pxx, Pyy, V, tau_p)
    Up = polar_u(source_s(Pm, Rm, V))
    froz &= fn(Up - U0) < 1e-9
    # tau in (pi/4, pi/2): cos(2tau)<0 -> negative scalar -> -U0
    tau_m = 1.1
    Pm2, Rm2 = pointer_map(Pxx, Pyy, V, tau_m)
    Um = polar_u(source_s(Pm2, Rm2, V))
    flip &= fn(Um + U0) < 1e-9
check("C2a link frozen polar(s')=polar(s) for cos(2 tau)>0", froz)
check("C2b link Z_2 flip polar(s')=-polar(s) for cos(2 tau)<0", flip)

# C3: the only link 'flow' is isotropic contraction of |s| toward degeneracy
# (the link carries no arrow and no rate; |s| -> 0 at the balance fixed point)
Pxx = rand_density_block(n)
Pyy = rand_density_block(n)
tau = 0.45
Pc, Rc = Pxx.copy(), Pyy.copy()
smags = []
dirdev = []
s0dir = polar_u(source_s(Pc, Rc, V))
for _ in range(30):
    s = source_s(Pc, Rc, V)
    smags.append(fn(s))
    if fn(s) > 1e-7:
        dirdev.append(fn(polar_u(s) - s0dir))
    Pc, Rc = pointer_map(Pc, Rc, V, tau)
check("C3a source magnitude |s| contracts to 0 (link degenerates at balance)", smags[-1] < 1e-3 * smags[0],
      f"|s|_0={smags[0]:.3e} |s|_30={smags[-1]:.3e}")
check("C3b link direction frozen while magnitude contracts (vacuous generator)", max(dirdev) < 1e-8,
      f"max dir dev = {max(dirdev):.2e}")

# ----------------------------------------------------------------------------
print("=" * 78)
print("PART D -- link non-autonomy at the compressed level; boundaries")
print("=" * 78)

# D1: NEW exhibit -- two slow-manifold states with the SAME U_eff = polar(s) but
# DIFFERENT imbalance D give DIFFERENT autonomous pointer flow. The genuine
# generator is autonomous in the pointer densities, NOT in the link variable.
Pxx = rand_density_block(n)
Pyy = rand_density_block(n)
s = source_s(Pxx, Pyy, V)
# state 2 = uniform downscale by kappa: s -> kappa s (polar unchanged), D -> kappa D
kap = 0.5
Pxx2, Pyy2 = kap * Pxx, kap * Pyy
U_eff_1 = polar_u(s)
U_eff_2 = polar_u(source_s(Pxx2, Pyy2, V))
same_link = fn(U_eff_1 - U_eff_2) < 1e-9
tau = 0.4
flow1 = pointer_map(Pxx, Pyy, V, tau)[0] - Pxx       # = -sin^2(tau) D_1
flow2 = pointer_map(Pxx2, Pyy2, V, tau)[0] - Pxx2     # = -sin^2(tau) D_2 = kappa * flow1
diff_flow = fn(flow1 - flow2)
check("D1a two states share U_eff = polar(s) exactly", same_link, f"{fn(U_eff_1 - U_eff_2):.2e}")
check("D1b but their autonomous pointer flows differ at order 1 (link is a lossy coordinate)",
      diff_flow > 0.1 * fn(flow1), f"||flow1-flow2||={diff_flow:.3e}, ||flow1||={fn(flow1):.3e}")
# autonomy DOES hold in the pointer densities (by construction of the map)
check("D1c flow IS autonomous in (M(x,x),M(y,y)) (the generator's true carrier)",
      fn(flow2 - kap * flow1) < 1e-11, f"{fn(flow2 - kap*flow1):.2e}")

# D2: weak-record boundary -- as lam -> 0 the composite step departs from the
# closed pointer map at order 1 (recovers the block-01 non-slaved regime).
Pxx = rand_density_block(n)
Pyy = rand_density_block(n)
Mxy = rand_density_block(n) * 0.3
tau = 0.6
dev_by_lam = {}
for lam in (1.0, 0.7, 0.3, 0.0):
    P2, Pyy_next, _ = composite_step(Pxx, Pyy, Mxy, V, tau, lam=lam, instrument=instrument_IB)
    Pm, Rm = pointer_map(Pxx, Pyy, V, tau)
    dev_by_lam[lam] = fn(P2 - Pm) + fn(Pyy_next - Rm)
check("D2 slaving is record-dominated: dev(lam=1) ~ 0 << dev(lam=0) order 1",
      dev_by_lam[1.0] < 1e-11 and dev_by_lam[0.0] > 0.05,
      f"dev(1)={dev_by_lam[1.0]:.2e} dev(0.3)={dev_by_lam[0.3]:.3e} dev(0)={dev_by_lam[0.0]:.3e}")
# monotone: weaker records -> larger departure (single Hamiltonian-step proxy, leading order)
mono = dev_by_lam[1.0] <= dev_by_lam[0.7] <= dev_by_lam[0.3] <= dev_by_lam[0.0] + 1e-12
check("D2b departure grows monotonically as records weaken", mono)

# D3: trace-blocking compression -- the COARSEST gauge-invariant pointer
# observable (tr M(x,x), tr M(y,y)) carries a closed autonomous 2x2
# doubly-stochastic flow toward equal occupation, with ZERO link content.
maxdev_tr = 0.0
for _ in range(10):
    Pxx = rand_density_block(n)
    Pyy = rand_density_block(n)
    tau = float(rng.uniform(0.1, 1.4))
    Pm, Rm = pointer_map(Pxx, Pyy, V, tau)
    c2, s2 = np.cos(tau) ** 2, np.sin(tau) ** 2
    tr_pred_x = c2 * np.trace(Pxx) + s2 * np.trace(Pyy)
    tr_pred_y = c2 * np.trace(Pyy) + s2 * np.trace(Pxx)
    maxdev_tr = max(maxdev_tr, abs(np.trace(Pm) - tr_pred_x), abs(np.trace(Rm) - tr_pred_y))
check("D3 trace-blocking: (tr M(x,x),tr M(y,y)) closed 2x2 doubly-stochastic flow",
      maxdev_tr < 1e-11, f"{maxdev_tr:.2e}")
# doubly-stochastic matrix [[c2,s2],[s2,c2]] relaxes to equal occupation; carries no link data
DS = np.array([[np.cos(0.5) ** 2, np.sin(0.5) ** 2], [np.sin(0.5) ** 2, np.cos(0.5) ** 2]])
fixed = DS @ np.array([1.0, 1.0])
check("D3b trace-block fixed point = equal occupation (gauge-invariant, no link content)",
      fn(fixed - np.array([1.0, 1.0])) < TOL)

# ----------------------------------------------------------------------------
print("=" * 78)
print("PART E -- the generator's covariance is instrument-inherited (no discharge)")
print("=" * 78)

# E1: under the FULL composite step at lam=1, color-blind total-occupation instrument keeps the local-density spectrum
# (Ad-covariant pointer content); frame-naming occupation-basis instrument changes it (frame-naming). So the covariant
# pointer transport generator is the color-blind instrument's footprint, not derived.
Pxx = rand_density_block(n)
Pyy = rand_density_block(n)
Mxy = rand_density_block(n) * 0.3
# instrument action only (the record step), compare local-density spectra
PxxA, PyyA, _ = instrument_IA(Pxx, Pyy, Mxy, lam=1.0)
PxxB, PyyB, _ = instrument_IB(Pxx, Pyy, Mxy, lam=1.0)
spec0 = np.sort(np.linalg.eigvalsh(Pxx))
specA = np.sort(np.linalg.eigvalsh(PxxA))
specB = np.sort(np.linalg.eigvalsh(PxxB))
check("E1a color-blind total-occupation instrument preserves local color-density spectrum (Ad-covariant content)", fn(specB - spec0) < TOL,
      f"{fn(specB - spec0):.2e}")
check("E1b frame-naming occupation-basis instrument changes the local-density spectrum (frame-naming, order 1)", fn(specA - spec0) > 0.05,
      f"{fn(specA - spec0):.3e}")

# E2: covariance of the realized pointer map breaks under frame-naming occupation-basis instrument at order 1
# (compare g-conjugated frame-naming occupation-basis instrument step vs frame-naming occupation-basis instrument step of g-conjugated state)
gx = rand_su(n)
gy = rand_su(n)
Vp = gx @ V @ gy.conj().T
tau = 0.5
# color-blind total-occupation instrument realized step (should be covariant)
def realized_step(Pxx, Pyy, Mxy, Vmat, instrument):
    return composite_step(Pxx, Pyy, Mxy, Vmat, tau, lam=1.0, instrument=instrument)
P2b, R2b, M2b = realized_step(Pxx, Pyy, Mxy, V, instrument_IB)
P2b_g, R2b_g, _ = realized_step(gx @ Pxx @ gx.conj().T, gy @ Pyy @ gy.conj().T,
                                gx @ Mxy @ gy.conj().T, Vp, instrument_IB)
covB = fn(P2b_g - gx @ P2b @ gx.conj().T)
P2a, R2a, M2a = realized_step(Pxx, Pyy, Mxy, V, instrument_IA)
P2a_g, R2a_g, _ = realized_step(gx @ Pxx @ gx.conj().T, gy @ Pyy @ gy.conj().T,
                                gx @ Mxy @ gy.conj().T, Vp, instrument_IA)
covA = fn(P2a_g - gx @ P2a @ gx.conj().T)
check("E2a color-blind total-occupation instrument realized pointer step joint-locally covariant (exact)", covB < 1e-10, f"{covB:.2e}")
check("E2b frame-naming occupation-basis instrument realized pointer step covariance broken at order 1 (frame-naming)", covA > 0.05, f"{covA:.3e}")
info("E2 footprint", "the covariant pointer transport generator is the color-blind total-occupation instrument's footprint; "
                      "frame-naming occupation-basis instrument gives a frame-dependent generator -- no einselection-selection is discharged")

# ----------------------------------------------------------------------------
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
