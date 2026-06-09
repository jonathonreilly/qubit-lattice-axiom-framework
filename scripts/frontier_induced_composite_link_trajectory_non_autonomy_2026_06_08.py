"""Induced composite-link trajectory: covariance, exact increment law, non-autonomy.

Gauge-link dynamics frontier question: does the matter dynamics induce
the gauge-link dynamics through the composite link U_eff(t) = polar(M(x,y;t))
(the cross-site matter-bilinear unitarization of
COLOR_LINK_INDEX_ROUTING_VIA_CROSS_SITE_MATTER_BILINEAR_UNITARIZATION_BOUNDED_THEOREM_NOTE_2026-06-08)?

Exact finite-dimensional model. One-body space = (sites) x C^3 (the supplied
per-site C^3 color carrier; MR_color residual). The one-body density rho
(0 <= rho <= 1, fermionic-Gaussian reading; cross-site block M(x,y) = the
one-body density block) evolves exactly: rho(t) = e^{-iHt} rho(0) e^{iHt},
computed by eigh. Hamiltonians: (i) H_free = kappa A (x) I_3 (color-diagonal
uniform nearest-neighbor hopping); (ii) H_cov with a frozen generic SU(3) link
background V_xy on each edge; (iii) a staggered-sign variant of (ii).

Four exact test families (Parts 1-4):
  1. rank-3 well-definedness of U_eff along trajectories + exact degeneracy
     characterization (endpoint amplitude-rank bound).
  2. equivariance: global-SU(3) exact for H_free; FAILS for frozen background
     (teeth, measured); restored exactly as JOINT local covariance
     (state + background co-rotated).
  3. exact increment law: dM/dt = local-density term + chord term (linear in
     other bilinears); dU_eff/dt = U Omega with Omega the unique solution of
     the Sylvester equation Omega Q + Q Omega = U^dag Mdot - Mdot^dag U;
     su(3)-projected increment is Z_3-branch-free. Wilson-staple-direction
     overlap reported as INFO (diagnostic only, no claim).
  4. NON-AUTONOMY exhibit: two physical one-body densities with the SAME
     U_eff(0), SAME local color densities, SAME Mdot(0), but order-1 different
     dU_eff/dt (both H_free and H_cov) -- the hidden positive part Q enters
     the polar projection. COMPLEMENTARY RIGIDITY: at minimal occupancy
     (exactly 3 occupied modes, invertible endpoint blocks) the Schur identity
     M M(y,y)^{-1} M^dag = M(x,x) forces Q = the matrix geometric mean
     P_left # P_right -- the hidden-Q channel closes at K=3 and opens at K>=4.

Memory-safe: <= 12x12 dense matrices, eigh only, no large inverses, no MC.
Prints "TOTAL: PASS=N FAIL=0" on success.
"""
from __future__ import annotations

import numpy as np

RNG = np.random.default_rng(20260608)

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    msg = f"[{tag}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)


def info(name: str, detail: str) -> None:
    print(f"[INFO] {name}: {detail}")


# ----------------------------------------------------------------------
# linear-algebra helpers (3x3 color blocks; one-body space site x color)
# ----------------------------------------------------------------------

def crand(*shape):
    return RNG.standard_normal(shape) + 1j * RNG.standard_normal(shape)


def haar_su3():
    """Generic SU(3) element via QR of a complex Gaussian + det reduction."""
    z = crand(3, 3)
    q, r = np.linalg.qr(z)
    q = q @ np.diag(np.exp(-1j * np.angle(np.diag(r))))
    return q / np.linalg.det(q) ** (1.0 / 3.0)


def polar_uq(m):
    """m = u q with q = (m^dag m)^{1/2} PD Hermitian, u unitary (m invertible)."""
    w, v = np.linalg.eigh(m.conj().T @ m)
    q = v @ np.diag(np.sqrt(w)) @ v.conj().T
    u = m @ v @ np.diag(1.0 / np.sqrt(w)) @ v.conj().T
    return u, q


def sylvester_omega(q, s):
    """Unique solution of Omega q + q Omega = s for PD Hermitian q (eigenbasis)."""
    w, v = np.linalg.eigh(q)
    sb = v.conj().T @ s @ v
    return v @ (sb / (w[:, None] + w[None, :])) @ v.conj().T


def sqrtm_pd(x):
    w, v = np.linalg.eigh(x)
    return v @ np.diag(np.sqrt(w)) @ v.conj().T


def geom_mean(a, b):
    """Matrix geometric mean a # b (unique PD solution of x a^{-1} x = b)."""
    rs = sqrtm_pd(a)
    rsi = np.linalg.inv(rs)
    return rs @ sqrtm_pd(rsi @ b @ rsi) @ rs


def block(mat, x, y):
    """3x3 color block (x,y) of a one-body operator on sites x color."""
    return mat[3 * x: 3 * x + 3, 3 * y: 3 * y + 3]


def site_amplitudes(modes, x):
    """3xK amplitude block G(x): rows color, columns occupied modes."""
    return modes[3 * x: 3 * x + 3, :]


def evolve(rho, h_eigs, h_vecs, t):
    e = h_vecs @ np.diag(np.exp(-1j * h_eigs * t)) @ h_vecs.conj().T
    return e @ rho @ e.conj().T


def mdot_exact(rho, ham, x, y):
    """d/dt M(x,y) = -i (H rho - rho H) block (x,y) -- exact at this rho."""
    comm = -1j * (ham @ rho - rho @ ham)
    return block(comm, x, y)


def su3_part(omega):
    return omega - (np.trace(omega) / 3.0) * np.eye(3)


# ----------------------------------------------------------------------
# model: 4-cycle graph (sites 0-1-2-3-0), C^3 color carrier per site
# ----------------------------------------------------------------------

N_SITES = 4
DIM = 3 * N_SITES
EDGES = [(0, 1), (1, 2), (2, 3), (3, 0)]
KAPPA = 1.0


def build_h(links, signs=None):
    """Nearest-neighbor hopping with 3x3 link matrices on each edge."""
    ham = np.zeros((DIM, DIM), complex)
    for k, (x, y) in enumerate(EDGES):
        s = 1.0 if signs is None else signs[k]
        ham[3 * x: 3 * x + 3, 3 * y: 3 * y + 3] = KAPPA * s * links[k]
        ham[3 * y: 3 * y + 3, 3 * x: 3 * x + 3] = KAPPA * s * links[k].conj().T
    return ham


def random_orthonormal_modes(k, zero_color_row_at_site=None):
    """K orthonormal occupied modes in C^DIM (columns); optional engineered
    color-rank deficiency at one site (color component 2 zeroed there)."""
    w = crand(DIM, k)
    if zero_color_row_at_site is not None:
        w[3 * zero_color_row_at_site + 2, :] = 0.0
    q, _ = np.linalg.qr(w)  # column ops preserve zero rows
    return q[:, :k]


ID3 = np.eye(3)
LINKS_FREE = [ID3.copy() for _ in EDGES]
LINKS_COV = [haar_su3() for _ in EDGES]
STAG_SIGNS = [1.0, -1.0, 1.0, -1.0]

H_FREE = build_h(LINKS_FREE)
H_COV = build_h(LINKS_COV)
H_COV_STAG = build_h(LINKS_COV, signs=STAG_SIGNS)

check("setup: H_free, H_cov, H_cov_stag Hermitian",
      max(np.abs(h - h.conj().T).max() for h in (H_FREE, H_COV, H_COV_STAG)) < 1e-14)

K_MODES = 4
MODES0 = random_orthonormal_modes(K_MODES)
RHO0 = MODES0 @ MODES0.conj().T  # rank-4 projector: 4 occupied modes (>= 3)

check("setup: rho(0) physical, >=3 occupied modes",
      np.linalg.eigvalsh(RHO0).min() > -1e-12
      and np.linalg.eigvalsh(RHO0).max() < 1 + 1e-12
      and np.linalg.matrix_rank(RHO0) >= 3,
      f"rank={np.linalg.matrix_rank(RHO0)}")

T_SAMPLES = np.linspace(0.0, 8.0, 33)

EIG_FREE = np.linalg.eigh(H_FREE)
EIG_COV = np.linalg.eigh(H_COV)
EIG_COV_STAG = np.linalg.eigh(H_COV_STAG)

print()
print("== Part 1: rank-3 well-definedness along trajectories ==")

for label, (evals, evecs) in [("free", EIG_FREE), ("cov", EIG_COV)]:
    sig3_min = np.inf
    udev_max = 0.0
    for t in T_SAMPLES:
        rho_t = evolve(RHO0, evals, evecs, t)
        for (x, y) in EDGES:
            m = block(rho_t, x, y)
            sig = np.linalg.svd(m, compute_uv=False)
            sig3_min = min(sig3_min, sig[2])
            if sig[2] > 1e-8:
                u, _ = polar_uq(m)
                udev_max = max(udev_max, np.abs(u.conj().T @ u - ID3).max())
    check(f"existence [{label}]: rank-3 maintained on all 4 edges, t in [0,8]",
          sig3_min > 1e-6, f"min sigma_3 = {sig3_min:.3e}")
    check(f"existence [{label}]: U_eff exactly unitary wherever defined",
          udev_max < 1e-10, f"max |U^dag U - I| = {udev_max:.3e}")

# exact degeneracy characterization: rank(M(x,y)) <= min rank of endpoint blocks
bound_ok = True
for _ in range(20):
    kk = int(RNG.integers(1, 5))
    modes = random_orthonormal_modes(kk)
    rho = modes @ modes.conj().T
    for (x, y) in EDGES:
        rm = np.linalg.matrix_rank(block(rho, x, y), tol=1e-10)
        rx = np.linalg.matrix_rank(site_amplitudes(modes, x), tol=1e-10)
        ry = np.linalg.matrix_rank(site_amplitudes(modes, y), tol=1e-10)
        if rm > min(rx, ry):
            bound_ok = False
check("existence: rank bound rank(M(x,y)) <= min(rank G(x), rank G(y)) (20 random draws)",
      bound_ok)

# engineered degeneracy: color support at site 1 confined to 2D at t=0
modes_def = random_orthonormal_modes(K_MODES, zero_color_row_at_site=1)
rho_def = modes_def @ modes_def.conj().T
sig0 = np.linalg.svd(block(rho_def, 0, 1), compute_uv=False)
check("existence: engineered 2D-color-support state => M(0,1;0) rank-deficient",
      sig0[2] < 1e-12, f"sigma_3 = {sig0[2]:.3e}")
restored = []
for evals, evecs in (EIG_FREE, EIG_COV):
    rho_t = evolve(rho_def, evals, evecs, 0.7)
    restored.append(np.linalg.svd(block(rho_t, 0, 1), compute_uv=False)[2])
check("existence [cov]: hopping evolution restores rank-3 by t=0.7 (degeneracy not invariant)",
      restored[1] > 1e-6, f"sigma_3(t=0.7) = {restored[1]:.3e}")
info("existence [free] restored sigma_3(t=0.7)", f"{restored[0]:.3e}")

print()
print("== Part 2: equivariance / covariance of the induced trajectory ==")

T_EQ = [0.0, 0.5, 1.7, 4.0]


def ueff_traj(rho_init, ham, times, edges=EDGES):
    evals, evecs = np.linalg.eigh(ham)
    out = {}
    for t in times:
        rho_t = evolve(rho_init, evals, evecs, t)
        for (x, y) in edges:
            u, _ = polar_uq(block(rho_t, x, y))
            out[(t, x, y)] = u
    return out


# (a) free H, global g: exact equivariance of the whole trajectory
dev_free = 0.0
base_free = ueff_traj(RHO0, H_FREE, T_EQ)
for _ in range(3):
    g = haar_su3()
    gbig = np.kron(np.eye(N_SITES), g)
    rot = ueff_traj(gbig @ RHO0 @ gbig.conj().T, H_FREE, T_EQ)
    for key, u in base_free.items():
        dev_free = max(dev_free, np.abs(rot[key] - g @ u @ g.conj().T).max())
check("covariance [free]: global-SU(3) equivariance U_eff^g(t) = g U_eff(t) g^dag exact",
      dev_free < 1e-10, f"max dev = {dev_free:.3e} (3 random g)")

# (b) cov H frozen background, global g: equivariance FAILS (teeth)
g = haar_su3()
gbig = np.kron(np.eye(N_SITES), g)
base_cov = ueff_traj(RHO0, H_COV, T_EQ)
rot_cov = ueff_traj(gbig @ RHO0 @ gbig.conj().T, H_COV, T_EQ)
viol = max(np.abs(rot_cov[key] - g @ base_cov[key] @ g.conj().T).max()
           for key in base_cov)
check("covariance [cov, frozen background]: global equivariance FAILS (teeth)",
      viol > 1e-2, f"max violation = {viol:.3f}")

# (c) cov H, JOINT local transformation: exact local covariance
dev_joint = 0.0
for trial in range(3):
    gs = [haar_su3() for _ in range(N_SITES)]
    gloc = np.zeros((DIM, DIM), complex)
    for xx in range(N_SITES):
        gloc[3 * xx: 3 * xx + 3, 3 * xx: 3 * xx + 3] = gs[xx]
    links_rot = [gs[x] @ LINKS_COV[k] @ gs[y].conj().T
                 for k, (x, y) in enumerate(EDGES)]
    h_rot = build_h(links_rot)
    rot = ueff_traj(gloc @ RHO0 @ gloc.conj().T, h_rot, T_EQ)
    for (t, x, y), u in base_cov.items():
        dev_joint = max(dev_joint,
                        np.abs(rot[(t, x, y)] - gs[x] @ u @ gs[y].conj().T).max())
check("covariance [cov]: joint local covariance U_eff -> g_x U_eff g_y^dag exact along trajectory",
      dev_joint < 1e-10, f"max dev = {dev_joint:.3e} (3 random local tuples)")

# (d) staggered-sign variant: same local covariance
base_stag = ueff_traj(RHO0, H_COV_STAG, T_EQ)
gs = [haar_su3() for _ in range(N_SITES)]
gloc = np.zeros((DIM, DIM), complex)
for xx in range(N_SITES):
    gloc[3 * xx: 3 * xx + 3, 3 * xx: 3 * xx + 3] = gs[xx]
links_rot = [gs[x] @ LINKS_COV[k] @ gs[y].conj().T for k, (x, y) in enumerate(EDGES)]
h_rot = build_h(links_rot, signs=STAG_SIGNS)
rot = ueff_traj(gloc @ RHO0 @ gloc.conj().T, h_rot, T_EQ)
dev_stag = max(np.abs(rot[key] - gs[key[1]] @ base_stag[key] @ gs[key[2]].conj().T).max()
               for key in base_stag)
check("covariance [cov, staggered signs]: joint local covariance exact",
      dev_stag < 1e-10, f"max dev = {dev_stag:.3e}")

print()
print("== Part 3: exact increment law ==")

# (a) block decomposition: Mdot = local-density term + chord term, exactly
TEST_EDGE = (0, 1)
NBR = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}
LINK_OF = {}
for k, (x, y) in enumerate(EDGES):
    LINK_OF[(x, y)] = KAPPA * LINKS_COV[k]
    LINK_OF[(y, x)] = KAPPA * LINKS_COV[k].conj().T

dec_dev = 0.0
for t in (0.0, 0.9, 3.1):
    rho_t = evolve(RHO0, EIG_COV[0], EIG_COV[1], t)
    for (x, y) in EDGES:
        v_xy = LINK_OF[(x, y)]
        local = -1j * (v_xy @ block(rho_t, y, y) - block(rho_t, x, x) @ v_xy)
        chord = np.zeros((3, 3), complex)
        for z in NBR[x]:
            if z != y:
                chord += -1j * (LINK_OF[(x, z)] @ block(rho_t, z, y))
        for z in NBR[y]:
            if z != x:
                chord -= -1j * (block(rho_t, x, z) @ LINK_OF[(z, y)])
        direct = mdot_exact(rho_t, H_COV, x, y)
        dec_dev = max(dec_dev, np.abs(local + chord - direct).max())
check("increment [cov]: Mdot = local-density term + chord term (exact decomposition, all edges)",
      dec_dev < 1e-12, f"max dev = {dec_dev:.3e}")

# magnitudes (structure characterization only)
rho_t = evolve(RHO0, EIG_COV[0], EIG_COV[1], 0.9)
x, y = TEST_EDGE
v_xy = LINK_OF[TEST_EDGE]
local = -1j * (v_xy @ block(rho_t, y, y) - block(rho_t, x, x) @ v_xy)
chord = mdot_exact(rho_t, H_COV, x, y) - local
info("increment [cov] t=0.9 edge(0,1) magnitudes",
     f"|local|_F = {np.linalg.norm(local):.3f}, |chord|_F = {np.linalg.norm(chord):.3f}")

# (b) Mdot formula vs finite differences of the exact trajectory
hh = 1e-4
fd_dev = 0.0
for t in (0.4, 2.2):
    rs = [evolve(RHO0, EIG_COV[0], EIG_COV[1], t + s * hh) for s in (-2, -1, 1, 2)]
    md_fd = (8 * (block(rs[2], *TEST_EDGE) - block(rs[1], *TEST_EDGE))
             - (block(rs[3], *TEST_EDGE) - block(rs[0], *TEST_EDGE))) / (12 * hh)
    rho_t = evolve(RHO0, EIG_COV[0], EIG_COV[1], t)
    fd_dev = max(fd_dev, np.abs(md_fd - mdot_exact(rho_t, H_COV, *TEST_EDGE)).max())
check("increment [cov]: Mdot block formula vs 4th-order finite difference",
      fd_dev < 1e-8, f"max dev = {fd_dev:.3e}")

# (c) polar increment: Udot = U Omega, Omega Q + Q Omega = U^dag Mdot - h.c.
for label, ham, (evals, evecs) in [("free", H_FREE, EIG_FREE), ("cov", H_COV, EIG_COV)]:
    pol_dev = 0.0
    ah_dev = 0.0
    for t in (0.4, 2.2):
        rho_t = evolve(RHO0, evals, evecs, t)
        m = block(rho_t, *TEST_EDGE)
        u, q = polar_uq(m)
        md = mdot_exact(rho_t, ham, *TEST_EDGE)
        b = u.conj().T @ md
        om = sylvester_omega(q, b - b.conj().T)
        ah_dev = max(ah_dev, np.abs(om + om.conj().T).max())
        us = []
        for s in (-2, -1, 1, 2):
            rr = evolve(RHO0, evals, evecs, t + s * hh)
            uu, _ = polar_uq(block(rr, *TEST_EDGE))
            us.append(uu)
        ud_fd = (8 * (us[2] - us[1]) - (us[3] - us[0])) / (12 * hh)
        pol_dev = max(pol_dev, np.abs(ud_fd - u @ om).max())
    check(f"increment [{label}]: polar increment Udot = U*Sylvester(Q, U^dag Mdot - h.c.) vs FD",
          pol_dev < 1e-7, f"max dev = {pol_dev:.3e}")
    check(f"increment [{label}]: Omega anti-Hermitian", ah_dev < 1e-12,
          f"max dev = {ah_dev:.3e}")

# (c2) known-answer test of the Sylvester machinery, independent of finite
# differences: M(t) = e^{tX} U0 (Q0 + t^2 P) with X anti-Hermitian has
# polar factor e^{tX} U0 exactly, so Udot(0) = X U0 a priori.
ka_dev = 0.0
for _ in range(5):
    xa = crand(3, 3)
    xa = (xa - xa.conj().T) / 2.0  # anti-Hermitian
    u_known, _ = polar_uq(crand(3, 3))
    gq = crand(3, 3)
    q_known = gq @ gq.conj().T + 0.3 * ID3  # PD
    m0 = u_known @ q_known
    mdot0 = xa @ m0  # d/dt[e^{tX} u_known (q_known + t^2 P)] at t=0
    bb = u_known.conj().T @ mdot0
    om_test = sylvester_omega(q_known, bb - bb.conj().T)
    ka_dev = max(ka_dev, np.abs(u_known @ om_test - xa @ u_known).max())
check("increment: Sylvester machinery known-answer test (Udot(0) = X U0 a priori, 5 draws)",
      ka_dev < 1e-11, f"max dev = {ka_dev:.3e}")

# (d) su(3)-projected increment is Z_3-branch-free
rho_t = evolve(RHO0, EIG_COV[0], EIG_COV[1], 0.4)
m = block(rho_t, *TEST_EDGE)
u, q = polar_uq(m)
md = mdot_exact(rho_t, H_COV, *TEST_EDGE)
b = u.conj().T @ md
om = sylvester_omega(q, b - b.conj().T)
om_su3 = su3_part(om)
branch_dev = 0.0
# statement: S = omega^k * u * det(u)^{-1/3} for any branch k gives
# S^dag Sdot whose su(3) projection equals su3_part(Omega) for every k
# (the center phase omega^k cancels in S^dag Sdot; the U(1) residue sits
# in the trace part only).
for kk in range(3):
    w3 = np.exp(2j * np.pi * kk / 3.0)
    s_branch = w3 * u / np.linalg.det(u) ** (1.0 / 3.0)
    # d/dt [w3 * u * det(u)^{-1/3}] = w3 [udot det^{-1/3} - (1/3) u det^{-1/3} tr(u^{-1} udot)]
    det13 = np.linalg.det(u) ** (1.0 / 3.0)
    udot = u @ om
    sdot = w3 * (udot / det13 - (1.0 / 3.0) * (u / det13) * np.trace(om))
    om_s = s_branch.conj().T @ sdot
    branch_dev = max(branch_dev, np.abs(su3_part(om_s) - om_su3).max())
check("increment: su(3)-projected increment identical on all three Z_3 det-branches",
      branch_dev < 1e-12, f"max dev = {branch_dev:.3e}")

# (e) INFO: Wilson-staple-force direction overlap (diagnostic only, no claim)
# staple for edge (0,1) on the 4-cycle: path 0-3-2-1 in the frozen background
stap = LINKS_COV[3].conj().T @ LINKS_COV[2].conj().T @ LINKS_COV[1].conj().T
f_w = LINKS_COV[0] @ stap.conj().T
f_w = (f_w - f_w.conj().T) / 2.0
f_w = su3_part(f_w)
overlaps = []
for t in np.linspace(0.1, 6.0, 13):
    rho_t = evolve(RHO0, EIG_COV[0], EIG_COV[1], t)
    m = block(rho_t, *TEST_EDGE)
    sig = np.linalg.svd(m, compute_uv=False)
    if sig[2] < 1e-8:
        continue
    u, q = polar_uq(m)
    md = mdot_exact(rho_t, H_COV, *TEST_EDGE)
    b = u.conj().T @ md
    om_s3 = su3_part(sylvester_omega(q, b - b.conj().T))
    num = np.real(np.trace(om_s3.conj().T @ f_w))
    den = np.linalg.norm(om_s3) * np.linalg.norm(f_w)
    overlaps.append(num / den)
overlaps = np.array(overlaps)
info("increment [cov] Wilson-staple-direction overlap cos-angle along trajectory",
     f"mean = {overlaps.mean():+.3f}, min = {overlaps.min():+.3f}, "
     f"max = {overlaps.max():+.3f} (diagnostic; no stable alignment claimed)")

print()
print("== Part 4: non-autonomy exhibit + minimal-occupancy rigidity ==")

# two-site model: one edge, one-body space C^6
g1, g2 = crand(3, 3), crand(3, 3)
rho_a = np.block([[g1 @ g1.conj().T, g1 @ g2.conj().T],
                  [g2 @ g1.conj().T, g2 @ g2.conj().T]])
rho_a = rho_a + 0.10 * (np.trace(rho_a).real / 6.0) * np.eye(6)
rho_a = rho_a / (1.3 * np.linalg.eigvalsh(rho_a).max())
p1p = rho_a[:3, :3].copy()
p2 = rho_a[3:, 3:].copy()
m_a = rho_a[:3, 3:].copy()
u0, q_a = polar_uq(m_a)

# perturb the positive part: Delta >= 0 keeps Q_B = Q_A + Delta PD at any
# size; a deterministic backoff respects the rho_B physicality constraint
# (Schur complement of the fixed diagonal blocks).
d_raw = crand(3, 3)
delta0 = d_raw @ d_raw.conj().T
delta0 *= 0.5 * np.linalg.norm(q_a) / np.linalg.norm(delta0)
q_b = None
rho_b = None
for back in range(12):
    cand_q = q_a + delta0 / (2.0 ** back)
    cand_rho = np.block([[p1p, u0 @ cand_q], [(u0 @ cand_q).conj().T, p2]])
    ev = np.linalg.eigvalsh(cand_rho)
    if ev.min() > 1e-6 and ev.max() <= 1.0:
        q_b = cand_q
        rho_b = cand_rho
        break
assert q_b is not None, "backoff failed to find a physical rho_B"

eigs_a = np.linalg.eigvalsh(rho_a)
eigs_b = np.linalg.eigvalsh(rho_b)
check("non-autonomy: rho_A, rho_B physical one-body densities (0 < eigs <= 1)",
      eigs_a.min() > 0 and eigs_a.max() <= 1 + 1e-12
      and eigs_b.min() > 0 and eigs_b.max() <= 1 + 1e-12,
      f"eigs_A in [{eigs_a.min():.3f},{eigs_a.max():.3f}], "
      f"eigs_B in [{eigs_b.min():.3f},{eigs_b.max():.3f}]")
check("non-autonomy: both states carry rank-3 cross-site bilinears (>=3 occupied modes)",
      np.linalg.svd(m_a, compute_uv=False)[2] > 1e-6
      and np.linalg.svd(u0 @ q_b, compute_uv=False)[2] > 1e-6
      and np.linalg.matrix_rank(rho_a) >= 3 and np.linalg.matrix_rank(rho_b) >= 3)

u_b, _ = polar_uq(u0 @ q_b)
check("non-autonomy: SAME U_eff(0) (exact)", np.abs(u_b - u0).max() < 1e-12,
      f"dev = {np.abs(u_b - u0).max():.3e}")
check("non-autonomy: SAME local color densities M(x,x), M(y,y) (exact by construction)",
      np.abs(rho_b[:3, :3] - p1p).max() < 1e-15
      and np.abs(rho_b[3:, 3:] - p2).max() < 1e-15)
check("non-autonomy: positive parts differ", np.linalg.norm(q_a - q_b) > 0.01,
      f"|Q_A - Q_B|_F = {np.linalg.norm(q_a - q_b):.4f}")

v_2s = haar_su3()
for label, vlink in [("cov", v_2s), ("free", ID3)]:
    h2 = np.zeros((6, 6), complex)
    h2[:3, 3:] = KAPPA * vlink
    h2[3:, :3] = KAPPA * vlink.conj().T
    md_a = (-1j * (h2 @ rho_a - rho_a @ h2))[:3, 3:]
    md_b = (-1j * (h2 @ rho_b - rho_b @ h2))[:3, 3:]
    check(f"non-autonomy [{label}]: SAME Mdot(0) (depends only on matched local densities)",
          np.abs(md_a - md_b).max() < 1e-15,
          f"dev = {np.abs(md_a - md_b).max():.3e}")
    bb = u0.conj().T @ md_a
    ss = bb - bb.conj().T
    om_a = sylvester_omega(q_a, ss)
    om_b = sylvester_omega(q_b, ss)
    sep = np.linalg.norm(om_a - om_b)
    check(f"non-autonomy [{label}]: dU_eff/dt DIFFERS", sep > 0.05,
          f"|Omega_A - Omega_B|_F = {sep:.4f}")
    # finite-difference confirmation from the two exact evolutions
    w2, v2 = np.linalg.eigh(h2)
    fd_max = 0.0
    for rho_x, om_x in ((rho_a, om_a), (rho_b, om_b)):
        us = []
        for s in (-2, -1, 1, 2):
            ee = v2 @ np.diag(np.exp(-1j * w2 * s * hh)) @ v2.conj().T
            rr = ee @ rho_x @ ee.conj().T
            uu, _ = polar_uq(rr[:3, 3:])
            us.append(uu)
        ud_fd = (8 * (us[2] - us[1]) - (us[3] - us[0])) / (12 * hh)
        fd_max = max(fd_max, np.abs(ud_fd - u0 @ om_x).max())
    check(f"non-autonomy [{label}]: both increments confirmed by finite differences",
          fd_max < 1e-8, f"max dev = {fd_max:.3e}")

# trajectory separation (the two induced trajectories genuinely part ways)
h2 = np.zeros((6, 6), complex)
h2[:3, 3:] = KAPPA * v_2s
h2[3:, :3] = KAPPA * v_2s.conj().T
w2, v2 = np.linalg.eigh(h2)
seps = []
for t in (0.25, 0.5):
    ee = v2 @ np.diag(np.exp(-1j * w2 * t)) @ v2.conj().T
    ua, _ = polar_uq((ee @ rho_a @ ee.conj().T)[:3, 3:])
    ub2, _ = polar_uq((ee @ rho_b @ ee.conj().T)[:3, 3:])
    seps.append(np.linalg.norm(ua - ub2))
check("non-autonomy [cov]: induced trajectories with identical U_eff(0) separate",
      seps[1] > 1e-3, f"|U_A - U_B|_F at t=0.25, 0.5 = {seps[0]:.4f}, {seps[1]:.4f}")

# minimal-occupancy rigidity: K=3 forces Q to be a matrix geometric mean
rig_schur = 0.0
rig_gm = 0.0
for _ in range(10):
    ga, gb = crand(3, 3), crand(3, 3)
    mm = ga @ gb.conj().T
    pp1 = ga @ ga.conj().T
    pp2 = gb @ gb.conj().T
    rig_schur = max(rig_schur,
                    np.abs(mm @ np.linalg.inv(pp2) @ mm.conj().T - pp1).max())
    uu, qq = polar_uq(mm)
    rig_gm = max(rig_gm,
                 np.abs(qq - geom_mean(uu.conj().T @ pp1 @ uu, pp2)).max())
check("minimal-occupancy rigidity: K=3 Schur identity M M(y,y)^{-1} M^dag = M(x,x) (10 draws)",
      rig_schur < 1e-10, f"max dev = {rig_schur:.3e}")
check("minimal-occupancy rigidity: K=3 rigidity Q = (U^dag M(x,x) U) # M(y,y) -- geometric mean forced",
      rig_gm < 1e-10, f"max dev = {rig_gm:.3e}")

schur4_min = np.inf
for _ in range(10):
    ga, gb = crand(3, 4), crand(3, 4)
    mm = ga @ gb.conj().T
    schur4_min = min(schur4_min,
                     np.abs(mm @ np.linalg.inv(gb @ gb.conj().T) @ mm.conj().T
                            - ga @ ga.conj().T).max())
check("minimal-occupancy rigidity: K=4 breaks the Schur identity (hidden-Q freedom opens; 10 draws)",
      schur4_min > 1e-2, f"min dev = {schur4_min:.3f}")

print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
