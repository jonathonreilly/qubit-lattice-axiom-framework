#!/usr/bin/env python3
"""Cross-sector front-speed B4 two-surface alignment -- bounded-theorem runner.

Companion runner for
docs/CROSS_SECTOR_FRONT_SPEED_B4_TWO_SURFACE_ALIGNMENT_BOUNDED_THEOREM_NOTE_2026-07-16.md

Conditional bounded theorem; THREE supplied legs are declared in the note:
  (leg 1) ALLORDERS_B4 premise (A): exact B4 invariance of the regulated
       action and measure on the Z^4 surface is SUPPLIED, not derived from
       the four axioms.
  (leg 2) `taste_orbit_summed_front_speed_readout_context`: the taste-orbit-
       SUMMED marginal curvature is identified as the fermion-side observable.
       Declared supplied context, not derived; on the single-taste reading
       the alignment theorem does NOT follow from this runner.
  (leg 3) `euclidean_marginal_front_speed_bridge_context`: the finite-grid
       EUCLIDEAN marginal coefficient ratio is identified with a physical
       (Lorentzian) front speed. No pole readout or Euclidean-to-Lorentzian
       continuation is constructed here; what the runner certifies is the
       Euclidean marginal coefficient statement, and every "front speed"
       phrase is conditional on this declared bridge.

Statement verified (Euclidean marginal coefficients, conditional): on the Z^4
B4-covariant Wilson+staggered surface, B4 pins EACH sector's diagonal marginal
kinetic form isotropic -- for the fermion observable this requires the JOINT
(taste, axis) representation lemma of V5, not the 4-component counting alone --
so each sector's Euclidean marginal coefficient ratio c_s/c_t equals 1 in
lattice units, the overall kinetic normalizations Z_F and Z_G cancel in the
ratio, and the cross-sector ratio equals 1 order-by-order on that surface. On
the broken-B4 surface (Z^3 + continuous tick; time-fixing S3), the same exact
counting leaves each sector's c_t/c_s an independent singlet of the
time-fixing subgroup: the time-fixing symmetry alone does NOT force
cross-sector equality. That is a symmetry-counting statement only -- it does
NOT establish that dynamics realizes arbitrary (a_F, a_G); the landed
velocity-RG mutual-drag flow is a live dynamical route toward equality on
that surface and is not contradicted here.

The two computed one-loop channels are representative B4-covariant instances
sharing the Wilson gluon block and the gauged staggered cos-vertex/seagull
rules; they are NOT assembled at a single common parameter point (Pi: landed
seagull kernel, massless fermion loop; Sigma_g: one-gluon exchange at the
IR-safe mass M=0.21, with the fermion-line tadpole evaluated separately in
V4 -- direction-blind on-surface, hence an isotropic marginal renormalization
there). Each channel's own B4 covariance is what the theorem consumes; the
instances are witnesses, not the proof.

Verification map (explicit-name-first; the V-codes key the note's table):
  V1  Clifford algebra for BOTH landed gamma conventions (taste kron set,
      seagull block set); W_B taste-rotation unitarity + conjugation for all
      16 taste shifts B; gauged cos-vertex taste covariance
      cos((p+piB-q/2)_mu) = (-1)^{B_mu} cos((p-q/2)_mu).
  V2  Gauge sector (seagull-runner kernel, T_F=1/2, 0.5*Pi/tot): seagull-
      completed Pi transverse (normalized Ward residual |khat.Pi|/(|khat||Pi|);
      thresholds stated at the checks) with the bubble (no seagull) assembly
      much worse; B4 isotropy piT(temporal)==piT(spatial) at v=1; eta=1 fixed
      point (induced anisotropy vanishes at isotropic input); the anisotropic
      control gauges the DEFORMED kernel consistently -- v_mu enters the
      propagators, the vertices, AND the seagull (gauging
      sum_mu v_mu sin(k_mu + A_mu)) -- and the deformed-kernel Pi stays
      transverse at the same normalized-Ward threshold.
  V3  Fermion sector, three kernels on the honest observable
      G_hon = Dinv(p) - Sigma(p,B) (the observable READS the taste shift B --
      non-degeneracy gates, never a W_B-conjugation define-away):
      (a) rainbow scalar-gluon calibration; (b) gauged cos-vertex on the
      Wilson block, Feynman gauge xi_gauge=1; (c) same in Landau gauge
      xi_gauge=0. Per-taste anisotropy NONZERO and kernel-
      dependent (three kernels, distinct values, signs differ); hw2 6-orbit
      taste-sum anisotropy ZERO within tolerance for all three; orbit zero
      structural across N=12 and N=10 for (a) and (b).
  V4  Off-surface controls: temporal-edge deformed Wilson block
      (2/xi)sin(xi q0/2) at xi=0.7 / xi=1.3 gives NONZERO orbit anisotropy
      with a sign straddle across xi=1 (rainbow; two samples -- no
      isolated-zero claim) and NONZERO at xi=1.3 (gauged vertex);
      cross-sector control (Pi carries no internal gluon line yet feels the
      fermion-velocity deformation) -- a symmetry-tracking witness, NOT a
      dynamical-unconstraint claim; tadpole T_mu (declared normalization:
      mean over the BZ grid, Landau form on the Wilson block) direction-blind
      on-surface and direction-sensitive off-surface.
  V5  Exact invariant counting (sympy Reynolds), TWO representations:
      (i) the 4-dim diagonal marginal coefficient vector: B4 acts through its
      S4 quotient with invariant rank 1 (isotropic image); the time-fixing S3
      (O_h horn) has rank 2. (ii) the JOINT 24-dim (hw2 taste B, axis mu)
      representation the fermion observable actually lives in: S4 invariant
      rank 2 (orbit indicators {mu in B}, {mu not in B}); each axis lies in
      exactly 3 of the 6 hw2 tastes, so UNIFORM taste averaging (the leg-2
      orbit sum) composed with the Reynolds projector has rank 1 with
      isotropic image; joint time-fixing S3 rank 6, averaging to rank 2.
  V6  Speed arithmetic (sympy exact + numeric): constant kinetic
      normalizations Z_F, Z_G cancel in v = sqrt(c_s/c_t); pinned-surface
      ratio = 1 identically; broken-surface ratio = sqrt(a_F/a_G) depends
      only on the quotient of the two independent per-sector anisotropies
      (scale-invariance gated) -- symmetry counting only, no
      dynamical-freedom claim; numeric delta(v_F/v_G) = sqrt(vF2/vG2) - 1
      = 0 on-surface, primary gate on the gauged cos-vertex curvatures with
      the rainbow curvatures as a labeled robustness gate.

Platform-stable output policy: gated prints are bound checks at the pass
tolerances; raw machine-noise residuals are never printed on the pass path.
O(1) landmark values are rounded to at most 4 decimals where stable.

Momentum axis 0 = temporal throughout. Offset BZ grid k = 2 pi (j+1/2)/N - pi
(B4-symmetric; required for exact taste-orbit sums). M = 0.21 internal
infrared-safe mass. Grids: N=12 primary, N=10 secondary. Single process,
chunked BZ loops; no dense objects beyond 4x4 gamma algebra and N^4 x 4
momentum arrays.
"""

from __future__ import annotations

import itertools as it
import sys

import numpy as np
import sympy as sp

np.seterr(all="ignore")
PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    line = f"[{tag}] {label}"
    if detail:
        line += f"  ::  {detail}"
    print(line)
    return ok


def bound_detail(name: str, value: float, bound: str, ok: bool) -> str:
    """Platform-stable detail: on pass, state the bound; on fail, show the value."""
    if ok:
        return f"|{name}| < {bound} (bound holds; residual suppressed)"
    return f"|{name}| = {value!r} EXCEEDS {bound}"


def hr(title: str) -> None:
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


# ---------------------------------------------------------------------------
# Gamma conventions (BOTH landed sets)
# ---------------------------------------------------------------------------
M = 0.21
I4 = np.eye(4, dtype=complex)
I2 = np.eye(2, dtype=complex)
Z2 = np.zeros((2, 2), complex)
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)

# taste-runner kron set
Gt = [np.kron(sx, sx), np.kron(sx, sy), np.kron(sx, sz), np.kron(sy, I2)]
G5 = Gt[0] @ Gt[1] @ Gt[2] @ Gt[3]

# seagull-runner block set
blk = lambda A, B, C, D: np.block([[A, B], [C, D]])
gb = np.array(
    [
        blk(Z2, -1j * sx, 1j * sx, Z2),
        blk(Z2, -1j * sy, 1j * sy, Z2),
        blk(Z2, -1j * sz, 1j * sz, Z2),
        blk(I2, Z2, Z2, -I2),
    ],
    complex,
)


def taste_rotation(B):
    W = I4.copy()
    for mu in range(4):
        if B[mu]:
            W = W @ (G5 @ Gt[mu])
    return W


# ---------------------------------------------------------------------------
# Shared BZ machinery (offset grid; axis 0 = temporal)
# ---------------------------------------------------------------------------
def make_bz_grid(n):
    return (np.arange(n) + 0.5) / n * 2 * np.pi - np.pi


def bz_points(n):
    return np.array(list(it.product(make_bz_grid(n), repeat=4)))


def gluon_block_lat(qpts, xi=1.0):
    """Wilson gluon block; xi deforms the TEMPORAL (axis 0) edge as
    (2/xi)sin(xi q0/2) so small-q0 is xi-independent (isolates B4-covariance
    breaking; xi=1 is the B4-covariant surface)."""
    val = ((2.0 / xi) * np.sin(xi * qpts[:, 0] / 2.0)) ** 2
    for d in range(1, 4):
        val = val + (2.0 * np.sin(qpts[:, d] / 2.0)) ** 2
    return val + 1e-9


# ---------------------------------------------------------------------------
# Fermion kernel (a): rainbow honest observable (taste-runner calibration kernel)
# ---------------------------------------------------------------------------
def self_energy(p, B, qpts, gluon):
    Bv = np.asarray(B, float) * np.pi
    sk = np.sin((p + Bv)[None, :] - qpts)
    den = M * M + np.sum(sk**2, axis=1)
    D = 1.0 / gluon(qpts)
    w = D / den / len(qpts)
    A = 4.0 * M * np.sum(w)
    Bc = np.array([2.0 * np.sum(w * sk[:, mu]) for mu in range(4)])
    return A * I4 + 1j * sum(Gt[mu] * Bc[mu] for mu in range(4))


def dirac_inverse(p):
    return M * I4 + 1j * sum(Gt[mu] * np.sin(p[mu]) for mu in range(4))


def hon_dispersion(p, B, qpts, gluon):
    Gop = dirac_inverse(p) - self_energy(p, B, qpts, gluon)
    return float(np.min(np.linalg.eigvalsh(Gop.conj().T @ Gop)))


def hon_curv(direction, B, qpts, gluon, eps=0.02):
    p0 = np.zeros(4)
    pp = np.zeros(4)
    pm = np.zeros(4)
    pp[direction] = eps
    pm[direction] = -eps
    return (
        hon_dispersion(pp, B, qpts, gluon)
        - 2.0 * hon_dispersion(p0, B, qpts, gluon)
        + hon_dispersion(pm, B, qpts, gluon)
    ) / eps**2


# ---------------------------------------------------------------------------
# Fermion kernels (b),(c): gauged cos-vertex Sigma on the Wilson block
# ---------------------------------------------------------------------------
def self_energy_gauged(p, B, qpts, Kvals, xi_gauge=1.0):
    """Sigma_g(p,B) = -(1/Nq) sum_q sum_{mu,nu} cos((p+piB-q/2)_mu) g_mu
    S(p-q+piB) cos((p+piB-q/2)_nu) g_nu D_munu(q), with D built from the Wilson
    block Kvals and gauge parameter xi_gauge (1 = Feynman diagonal, 0 = Landau
    transverse)."""
    Bv = np.asarray(B, float) * np.pi
    pk = (p + Bv)[None, :] - qpts
    s = np.sin(pk)
    den = M * M + np.sum(s**2, axis=1)
    Sf = (M * I4[None, :, :] - 1j * np.einsum("ca,aij->cij", s, np.array(Gt))) / den[
        :, None, None
    ]
    c = np.cos((p + Bv)[None, :] - qpts / 2.0)
    Sig = np.zeros((4, 4), complex)
    if xi_gauge == 1.0:
        w = 1.0 / Kvals
        for mu in range(4):
            V = c[:, mu][:, None, None] * Gt[mu]
            Sig += np.einsum("c,cij->ij", w, V @ Sf @ V)
    else:
        kh = 2.0 * np.sin(qpts / 2.0)
        for mu in range(4):
            VS = (c[:, mu][:, None, None] * Gt[mu]) @ Sf
            for nu in range(4):
                Dmn = ((mu == nu) * 1.0 - (1 - xi_gauge) * kh[:, mu] * kh[:, nu] / Kvals) / Kvals
                Sig += np.einsum("c,cij->ij", Dmn, VS @ (c[:, nu][:, None, None] * Gt[nu]))
    return -Sig / len(qpts)


def hon_dispersion_g(p, B, qpts, Kvals, xi_gauge=1.0):
    Gop = dirac_inverse(p) - self_energy_gauged(p, B, qpts, Kvals, xi_gauge=xi_gauge)
    return float(np.min(np.linalg.eigvalsh(Gop.conj().T @ Gop)))


def hon_curv_g(direction, B, qpts, Kvals, eps=0.02, xi_gauge=1.0):
    p0 = np.zeros(4)
    pp = np.zeros(4)
    pm = np.zeros(4)
    pp[direction] = eps
    pm[direction] = -eps
    return (
        hon_dispersion_g(pp, B, qpts, Kvals, xi_gauge=xi_gauge)
        - 2.0 * hon_dispersion_g(p0, B, qpts, Kvals, xi_gauge=xi_gauge)
        + hon_dispersion_g(pm, B, qpts, Kvals, xi_gauge=xi_gauge)
    ) / eps**2


# ---------------------------------------------------------------------------
# Gauge side: seagull-completed transverse Pi (seagull-runner kernel, block gammas)
# ---------------------------------------------------------------------------
def khat(qv):
    return 2 * np.sin(np.array(qv) / 2)


def pi_munu(qv, N, v, include_seagull=True, chunk=50000):
    """Fermion-loop Pi for the kernel sum_mu v_mu sin(k_mu). Gauging
    k_mu -> k_mu + A_mu puts v_mu into the propagators, the one-gluon vertex
    v_mu cos(k_mu + q_mu/2), AND the seagull -v_mu sin(k_mu) delta_munu: the
    anisotropic control deforms one consistent gauged kernel."""
    q = np.array(qv, float)
    ax = make_bz_grid(N)
    Pi = np.zeros((4, 4), complex)
    tot = N**4
    i0 = 0
    while i0 < tot:
        idx = np.arange(i0, min(i0 + chunk, tot))
        i0 += chunk
        a, r = np.divmod(idx, N**3)
        b, r = np.divmod(r, N**2)
        c, d = np.divmod(r, N)
        k = np.stack([ax[a], ax[b], ax[c], ax[d]], 1)
        kq = k + q
        sk = np.sin(k) * v
        skq = np.sin(kq) * v
        Dk = np.sum(sk**2, 1)
        Dkq = np.sum(skq**2, 1)
        Sk = (-1j * np.einsum("ca,aij->cij", sk, gb)) / Dk[:, None, None]
        Skq = (-1j * np.einsum("ca,aij->cij", skq, gb)) / Dkq[:, None, None]
        cmid = np.cos(k + q / 2) * v
        sk_mu = np.sin(k) * v
        for mu in range(4):
            Vmu = 1j * cmid[:, mu][:, None, None] * gb[mu]
            SV = Sk @ Vmu @ Skq
            for nu in range(4):
                Vnu = 1j * cmid[:, nu][:, None, None] * gb[nu]
                Pi[mu, nu] += np.einsum("cii->", SV @ Vnu)
            if include_seagull:
                Dmm = (-1j) * sk_mu[:, mu][:, None, None] * gb[mu]
                Pi[mu, mu] += -np.einsum("cij,cji->", Sk, Dmm)
    return 0.5 * Pi / tot  # T_F = 1/2 (seagull-runner convention)


def ward(Pi, qv):
    """Normalized Ward residual |khat . Pi| / (|khat| |Pi|) (max norms on Pi,
    Euclidean norm on khat) -- dimensionless in the external momentum."""
    kh = khat(qv)
    return np.max(np.abs(kh @ Pi)) / (np.linalg.norm(kh) * np.max(np.abs(Pi)) + 1e-30)


def piT(qaxis, q, N, v):
    qv = [0.0, 0.0, 0.0, 0.0]
    qv[qaxis] = q
    Pi = np.real(pi_munu(qv, N, v))
    b = (qaxis + 1) % 4
    return Pi[b, b] / (khat(qv)[qaxis] ** 2)


# ===========================================================================
def part_1() -> None:
    hr("Clifford (both sets), W_B conjugation, cos-vertex taste covariance (V1)")
    for name, GG in (("taste kron set", Gt), ("seagull block set", list(gb))):
        worst = 0.0
        for mu in range(4):
            for nu in range(4):
                anti = GG[mu] @ GG[nu] + GG[nu] @ GG[mu]
                worst = max(worst, float(np.max(np.abs(anti - 2 * (mu == nu) * I4))))
        ok = worst < 1e-12
        check(f"Clifford {{g,g}}=2delta ({name})", ok,
              bound_detail("max dev", worst, "1e-12", ok))

    worst = 0.0
    ok = True
    for B in it.product([0, 1], repeat=4):
        W = taste_rotation(B)
        if float(np.max(np.abs(W.conj().T @ W - I4))) > 1e-12:
            ok = False
        for mu in range(4):
            dev = float(
                np.max(np.abs(W.conj().T @ Gt[mu] @ W - ((-1) ** B[mu]) * Gt[mu]))
            )
            worst = max(worst, dev)
            if dev > 1e-10:
                ok = False
    check("W_B unitary AND W_B^-1 g_mu W_B = (-1)^{B_mu} g_mu (all 16 B)", ok,
          bound_detail("worst dev", worst, "1e-10", ok))

    rng = np.random.default_rng(7)
    worst = 0.0
    for _ in range(5):
        p = rng.uniform(-np.pi, np.pi, 4)
        q = rng.uniform(-np.pi, np.pi, 4)
        for B in it.product([0, 1], repeat=4):
            Bv = np.asarray(B, float) * np.pi
            lhs = np.cos(p + Bv - q / 2.0)
            rhs = np.array([(-1) ** B[mu] for mu in range(4)]) * np.cos(p - q / 2.0)
            worst = max(worst, float(np.max(np.abs(lhs - rhs))))
    ok = worst < 1e-12
    check("gauged cos vertex taste-covariant: cos(p+piB-q/2)=(-1)^B cos(p-q/2)",
          ok, bound_detail("worst dev (all 16 B, 5 random p,q)", worst, "1e-12", ok))


def part_2() -> dict:
    hr("Gauge sector: seagull-completed transverse Pi, B4 isotropy, eta=1 (V2)")
    N = 12
    iso = np.array([1.0, 1.0, 1.0, 1.0])
    qvs = ([0.0, 0.4, 0.0, 0.0], [0.3, 0.3, 0.0, 0.0], [0.0, 0.0, 0.0, 0.5])
    w_sea = [ward(np.real(pi_munu(qv, N, iso)), qv) for qv in qvs]
    check("normalized Ward residual |khat.Pi|/(|khat||Pi|) < 5% WITH seagull (N=12)",
          max(w_sea) < 0.05, f"worst residual={max(w_sea):.4f} < 0.05")
    w_bub = [ward(np.real(pi_munu(qv, N, iso, include_seagull=False)), qv) for qv in qvs]
    check("bubble (no seagull) Ward residual is LARGE (seagull is load-bearing)",
          min(w_bub) > 0.25 and min(w_bub) > 3 * max(w_sea),
          f"bubble min={min(w_bub):.4f} > 0.25 and > 3x seagull worst")
    v_def = np.array([1 - 0.05, 1 + 0.05, 1 + 0.05, 1 + 0.05])
    w_def = [ward(np.real(pi_munu(qv, N, v_def)), qv) for qv in qvs]
    check("DEFORMED-kernel Pi stays transverse (v_mu in propagators, vertices, "
          "seagull; eps=0.10)",
          max(w_def) < 0.05, f"worst residual={max(w_def):.4f} < 0.05")

    qq = [0.5, 0.3, 0.18]
    diffs = [abs(piT(0, q, N, iso) - piT(1, q, N, iso)) for q in qq]
    ok = max(diffs) < 1e-8
    check("B4 isotropy at v=1: piT(temporal)==piT(spatial) (< 1e-8)",
          ok, bound_detail("max piT diff (q in {0.5,0.3,0.18})", max(diffs), "1e-8", ok))

    def induced(eps, q):
        v = np.array([1 - eps / 2, 1 + eps / 2, 1 + eps / 2, 1 + eps / 2])
        return piT(1, q, N, v) - piT(0, q, N, v)

    ind0 = induced(0.0, 0.3)
    ok = abs(ind0) < 1e-8
    check("eta=1 fixed point: induced Pi anisotropy vanishes at eps=0",
          ok, bound_detail("induced(0)", ind0, "1e-8", ok))
    ind1 = induced(0.10, 0.3)
    return {"N": N, "ind1": ind1, "pit0": piT(0, 0.3, N, iso), "pit1": piT(1, 0.3, N, iso)}


def part_3() -> dict:
    hr("Fermion sector: three kernels -- rainbow, gauged Feynman, gauged Landau (V3)")
    n = 12
    qpts = bz_points(n)
    gluon1 = lambda q: gluon_block_lat(q, xi=1.0)
    hw2 = [tuple(s) for s in it.product([0, 1], repeat=4) if sum(s) == 2]
    B_rep = (0, 1, 1, 0)

    p_test = np.array([0.11, 0.15, 0.19, 0.13])
    nondeg = float(np.max(np.abs(
        self_energy(p_test, (0, 0, 0, 0), qpts, gluon1)
        - self_energy(p_test, B_rep, qpts, gluon1))))
    check("NON-DEGENERACY: Sigma(B=0) != Sigma(B_rep) (taste shift visible)",
          nondeg > 1e-4, f"||dSigma||={nondeg:.4f} > 1e-4")

    c_rep = [hon_curv(d, B_rep, qpts, gluon1) for d in range(4)]
    a_rep = c_rep[0] - np.mean(c_rep[1:])
    check("rainbow PER-TASTE anisotropy A(B_rep) ~ -0.2 (NONZERO, negative)",
          -0.35 < a_rep < -0.10,
          f"A={a_rep:+.4f} curv={[round(v, 4) for v in c_rep]}")

    co = [np.mean([hon_curv(d, B, qpts, gluon1) for B in hw2]) for d in range(4)]
    a_orb = co[0] - np.mean(co[1:])
    ok = abs(a_orb) < 1e-6
    check("rainbow hw2 ORBIT-SUM anisotropy ~ 0 on-surface (N=12)",
          ok, bound_detail("A_orbit", a_orb, "1e-6", ok))

    q10 = bz_points(10)
    co10 = [np.mean([hon_curv(d, B, q10, gluon1) for B in hw2]) for d in range(4)]
    a10 = co10[0] - np.mean(co10[1:])
    ok = abs(a10) < 1e-6
    check("rainbow orbit-sum zero STRUCTURAL (also N=10)",
          ok, bound_detail("A_orbit(N=10)", a10, "1e-6", ok))

    # kernel (b): gauged cos-vertex Sigma on the Wilson block (same Wilson block Pi gauges; Feynman)
    K1 = gluon_block_lat(qpts, xi=1.0)
    nondeg_g = float(np.max(np.abs(
        self_energy_gauged(p_test, (0, 0, 0, 0), qpts, K1)
        - self_energy_gauged(p_test, B_rep, qpts, K1))))
    check("GAUGED-VERTEX Sigma_g: taste shift visible (non-degeneracy)",
          nondeg_g > 1e-4, f"||dSigma_g||={nondeg_g:.4f} > 1e-4")

    cg_rep = [hon_curv_g(d, B_rep, qpts, K1) for d in range(4)]
    ag_rep = cg_rep[0] - np.mean(cg_rep[1:])
    check("GAUGED-VERTEX (Feynman) per-taste anisotropy NONZERO on-surface",
          abs(ag_rep) > 0.01,
          f"A_g={ag_rep:+.4f} curv={[round(v, 4) for v in cg_rep]}")

    cog = [np.mean([hon_curv_g(d, B, qpts, K1) for B in hw2]) for d in range(4)]
    ag_orb = cog[0] - np.mean(cog[1:])
    ok = abs(ag_orb) < 1e-6
    check("GAUGED-VERTEX hw2 ORBIT-SUM anisotropy ~ 0 on-surface (gauged cos-vertex on the Wilson block)",
          ok, bound_detail("A_g_orbit", ag_orb, "1e-6", ok))

    K10 = gluon_block_lat(q10, xi=1.0)
    cog10 = [np.mean([hon_curv_g(d, B, q10, K10) for B in hw2]) for d in range(4)]
    ag10 = cog10[0] - np.mean(cog10[1:])
    ok = abs(ag10) < 1e-6
    check("GAUGED-VERTEX orbit-sum zero STRUCTURAL (also N=10)",
          ok, bound_detail("A_g_orbit(N=10)", ag10, "1e-6", ok))

    # kernel (c): same gauged vertex, Landau gauge xi_gauge=0 (N=10 for cost)
    cL_rep = [hon_curv_g(d, B_rep, q10, K10, xi_gauge=0.0) for d in range(4)]
    aL_rep = cL_rep[0] - np.mean(cL_rep[1:])
    check("GAUGED-VERTEX (Landau) per-taste anisotropy NONZERO (N=10)",
          abs(aL_rep) > 0.01,
          f"A_L={aL_rep:+.4f} curv={[round(v, 4) for v in cL_rep]}")

    coL = [np.mean([hon_curv_g(d, B, q10, K10, xi_gauge=0.0) for B in hw2])
           for d in range(4)]
    aL_orb = coL[0] - np.mean(coL[1:])
    ok = abs(aL_orb) < 1e-6
    check("GAUGED-VERTEX (Landau) hw2 ORBIT-SUM anisotropy ~ 0 (gauge-robust)",
          ok, bound_detail("A_L_orbit", aL_orb, "1e-6", ok))

    # three-kernel witness at matched N=10: the UNPROTECTED per-taste value is
    # kernel-dependent (distinct values, signs differ) while the orbit sum is
    # zero for all three -- the orbit zero is symmetry-driven, not kernel tuning.
    cr10 = [hon_curv(d, B_rep, q10, gluon1) for d in range(4)]
    ar10 = cr10[0] - np.mean(cr10[1:])
    cf10 = [hon_curv_g(d, B_rep, q10, K10) for d in range(4)]
    af10 = cf10[0] - np.mean(cf10[1:])
    trio = [ar10, af10, aL_rep]
    pair_min = min(abs(x - y) for x, y in it.combinations(trio, 2))
    signs = sorted(np.sign(t) for t in trio)
    check("PER-TASTE value KERNEL-DEPENDENT at matched N=10 (3 kernels, signs differ)",
          pair_min > 0.03 and signs[0] < 0 < signs[-1],
          f"A(rainbow)={ar10:+.4f} A(Feynman)={af10:+.4f} A(Landau)={aL_rep:+.4f} "
          f"min pairwise sep={pair_min:.4f} > 0.03")
    return {"co": co, "cog": cog, "hw2": hw2, "qpts": qpts}


def part_4(p3: dict) -> None:
    hr("Off-surface controls, deformation-response witness, tadpole direction test (V4)")
    qpts = p3["qpts"]
    hw2 = p3["hw2"]

    def orbit_aniso(gluon):
        co = [np.mean([hon_curv(d, B, qpts, gluon) for B in hw2]) for d in range(4)]
        return co[0] - np.mean(co[1:])

    a07 = orbit_aniso(lambda q: gluon_block_lat(q, xi=0.7))
    a13 = orbit_aniso(lambda q: gluon_block_lat(q, xi=1.3))
    check("rainbow xi=0.7 orbit anisotropy NONZERO off-surface",
          abs(a07) > 1e-4, f"A(xi=0.7)={a07:+.4f}, |A| > 1e-4")
    check("rainbow xi=1.3 orbit anisotropy NONZERO off-surface",
          abs(a13) > 1e-4, f"A(xi=1.3)={a13:+.4f}, |A| > 1e-4")
    check("xi<1 / xi>1 STRADDLE in sign across xi=1 (two samples; no isolated-zero claim)",
          np.sign(a07) != np.sign(a13) and abs(a07) > 1e-4 and abs(a13) > 1e-4,
          f"sign(0.7)={np.sign(a07):+.0f} sign(1.3)={np.sign(a13):+.0f}, both |A| > 1e-4")

    K13 = gluon_block_lat(qpts, xi=1.3)
    cog13 = [np.mean([hon_curv_g(d, B, qpts, K13) for B in hw2]) for d in range(4)]
    ag13 = cog13[0] - np.mean(cog13[1:])
    check("GAUGED-VERTEX orbit anisotropy NONZERO off-surface (xi=1.3)",
          abs(ag13) > 1e-4, f"A_g(xi=1.3)={ag13:+.4f}, |A_g| > 1e-4")

    # deformation-response witness (symmetry-tracking, NOT a dynamical-unconstraint
    # claim): the fermion-loop Pi carries NO internal gluon line in this diagram
    # class, so the gauge-block deformation cannot move it; the fermion-velocity
    # deformation DOES move it.
    check("Pi FEELS the fermion deformation (induced anisotropy at eps=0.10 nonzero)",
          abs(_P2["ind1"]) > 1e-4,
          f"induced(0.10)={_P2['ind1']:+.4f}; Pi has no internal gluon line by construction")

    # tadpole T_mu; declared normalization: mean over the BZ grid, Landau form on
    # the Wilson block
    kh = 2.0 * np.sin(qpts / 2.0)

    def tadpole(xi):
        K = gluon_block_lat(qpts, xi=xi)
        return np.array([np.mean((1.0 - kh[:, mu] ** 2 / K) / K) for mu in range(4)])

    T1 = tadpole(1.0)
    T13 = tadpole(1.3)
    sp1 = (T1.max() - T1.min()) / abs(T1.mean())
    d13 = abs(T13[0] - T13[1]) / abs(T13.mean())
    ok = sp1 < 1e-10
    check("tadpole T_mu DIRECTION-BLIND on-surface (relative spread < 1e-10)",
          ok, bound_detail("rel spread", sp1, "1e-10", ok))
    check("tadpole T_mu DIRECTION-SENSITIVE off-surface (xi=1.3)",
          d13 > 1e-3, f"rel |T_t - T_s|={d13:.4f} > 1e-3")


def part_5() -> None:
    hr("Exact invariant counting + joint (hw2 taste, axis) representation lemma (V5)")

    def reynolds(perms):
        P = sp.zeros(4, 4)
        for prm in perms:
            Mx = sp.zeros(4, 4)
            for i, j in enumerate(prm):
                Mx[i, j] = 1
            P += Mx
        return P / len(perms)

    # B4 acts on diagonal marginal coefficients c_mu p_mu^2 through its S4
    # quotient (signs act trivially on p_mu^2)
    R4 = reynolds(list(it.permutations(range(4))))
    e0 = sp.Matrix([1, 0, 0, 0])
    img4 = R4 * e0
    check("B4 (S4 quotient) Reynolds rank on {c_mu} = 1 (single marginal invariant)",
          R4.rank() == 1, f"rank={R4.rank()}")
    check("B4 projection of c=(1,0,0,0) is ISOTROPIC (all entries equal 1/4)",
          all(sp.simplify(img4[i] - sp.Rational(1, 4)) == 0 for i in range(4)),
          f"image={list(img4)}")

    # O_h horn: time axis fixed, S3 on spatial axes
    perms3 = [(0,) + tuple(x + 1 for x in prm) for prm in it.permutations(range(3))]
    R3 = reynolds(perms3)
    img3 = R3 * e0
    check("O_h (time-fixing S3) Reynolds rank on {c_mu} = 2 (c_t independent of c_s)",
          R3.rank() == 2, f"rank={R3.rank()}")
    check("O_h projection keeps c_t != c_s (image (1,0,0,0) survives)",
          sp.simplify(img3[0] - 1) == 0 and all(sp.simplify(img3[i]) == 0 for i in (1, 2, 3)),
          f"image={list(img3)}")

    # JOINT (hw2 taste B, axis mu) representation lemma. The fermion object is
    # the 24-dim coefficient array c_{B,mu} (6 hw2 tastes x 4 axes), NOT a
    # single 4-vector. S4 acts jointly: B -> B o p, mu -> p^{-1}(mu) (membership
    # mu in B is preserved). Averaged over the full group / subgroup, the
    # anti-homomorphism convention gives the same Reynolds projector.
    hw2 = [tuple(s) for s in it.product([0, 1], repeat=4) if sum(s) == 2]
    pairs = [(bi, mu) for bi in range(6) for mu in range(4)]
    pidx = {p: i for i, p in enumerate(pairs)}

    def joint_matrix(prm):
        Mx = sp.zeros(24, 24)
        for bi, mu in pairs:
            B = hw2[bi]
            newB = tuple(B[prm[j]] for j in range(4))
            Mx[pidx[(hw2.index(newB), prm.index(mu))], pidx[(bi, mu)]] = 1
        return Mx

    def joint_reynolds(perms):
        R = sp.zeros(24, 24)
        for prm in perms:
            R += joint_matrix(prm)
        return R / len(perms)

    in_b = sp.Matrix([1 if hw2[bi][mu] == 1 else 0 for bi, mu in pairs])
    out_b = sp.Matrix([1 if hw2[bi][mu] == 0 else 0 for bi, mu in pairs])

    R24 = joint_reynolds(list(it.permutations(range(4))))
    check("JOINT S4 invariant rank on c_{B,mu} = 2 (orbit indicators {mu in B}, "
          "{mu not in B})",
          R24.rank() == 2 and R24 * in_b == in_b and R24 * out_b == out_b,
          f"rank={R24.rank()}; both orbit indicators are fixed vectors")

    counts = [sum(hw2[bi][mu] for bi in range(6)) for mu in range(4)]
    check("each axis lies in EXACTLY 3 of the 6 hw2 tastes",
          counts == [3, 3, 3, 3], f"counts={counts}")

    Avg = sp.zeros(4, 24)
    for bi, mu in pairs:
        Avg[mu, pidx[(bi, mu)]] += sp.Rational(1, 6)
    AR = Avg * R24
    iso_img = all(sp.simplify(AR[i, j] - AR[0, j]) == 0
                  for j in range(24) for i in range(1, 4))
    check("UNIFORM hw2 averaging o S4 Reynolds: rank 1, image ISOTROPIC "
          "(the V3 orbit-sum zero is this representation-forced projection)",
          AR.rank() == 1 and iso_img, f"rank={AR.rank()}; all rows equal")

    R24_3 = joint_reynolds(perms3)
    check("JOINT time-fixing S3 invariant rank = 6 (six (taste-type, axis-role) "
          "orbits)",
          R24_3.rank() == 6, f"rank={R24_3.rank()}")
    AR3 = Avg * R24_3
    check("uniform hw2 averaging o time-fixing S3 Reynolds: rank 2 -- time-fixing "
          "symmetry alone does NOT force c_t = c_s (symmetry counting only)",
          AR3.rank() == 2, f"rank={AR3.rank()}")


def part_6(p3: dict) -> None:
    hr("Speed arithmetic: Z cancellation, pinned ratio = 1, broken freedom (V6)")
    ZF, ZG = sp.symbols("Z_F Z_G", positive=True)
    ctF, csF, ctG, csG = sp.symbols("c_tF c_sF c_tG c_sG", positive=True)
    vF = sp.sqrt((ZF * csF) / (ZF * ctF))
    vG = sp.sqrt((ZG * csG) / (ZG * ctG))
    ratio = vF / vG
    check("overall kinetic normalizations Z_F, Z_G CANCEL in v_F/v_G (exact)",
          sp.simplify(ratio - sp.sqrt(csF * ctG / (ctF * csG))) == 0,
          "v_F/v_G = sqrt(c_sF c_tG / (c_tF c_sG)) -- no Z dependence")
    pinned = sp.simplify(ratio.subs({csF: ctF, csG: ctG}) - 1)
    check("on the B4-pinned surface (c_t=c_s per sector) v_F/v_G = 1 IDENTICALLY",
          pinned == 0, f"residual={pinned}")
    aF, aG = sp.symbols("a_F a_G", positive=True)
    lam = sp.symbols("lambda_s", positive=True)
    broken = ratio.subs({csF: aF * ctF, csG: aG * ctG})
    dF = sp.simplify(sp.diff(broken, aF))
    dG = sp.simplify(sp.diff(broken, aG))
    scale_inv = sp.simplify(broken.subs({aF: lam * aF, aG: lam * aG}, simultaneous=True)
                            - broken) == 0
    check("broken-B4 surface: v_F/v_G = sqrt(a_F/a_G) -- two independent per-sector "
          "anisotropies, ratio depends only on their quotient (scale-invariant)",
          sp.simplify(broken - sp.sqrt(aF / aG)) == 0 and dF != 0 and dG != 0
          and scale_inv,
          f"ratio={sp.simplify(broken)}; ratio(lam aF, lam aG) == ratio")

    # numeric two-surface witness from the computed data. delta is taken on the
    # SPEED ratio v_F/v_G = sqrt(vF2/vG2), not on the squared ratio. Primary
    # gate: the gauged cos-vertex curvatures; the rainbow
    # curvatures are kept as a labeled robustness gate.
    vG2 = _P2["pit1"] / _P2["pit0"]
    for label, curv in (("gauged cos-vertex (primary)", p3["cog"]),
                        ("rainbow (robustness)", p3["co"])):
        vF2 = np.mean(curv[1:]) / curv[0]
        delta = float(np.sqrt(vF2 / vG2)) - 1.0
        ok = abs(vF2 - 1) < 1e-6 and abs(vG2 - 1) < 1e-8 and abs(delta) < 1e-6
        check(f"NUMERIC delta(v_F/v_G)=sqrt(vF2/vG2)-1 = 0 on-surface -- {label}",
              ok,
              "|vF^2 ratio - 1| < 1e-6 AND |vG^2 ratio - 1| < 1e-8 AND "
              "|delta| < 1e-6 (bounds hold; residuals suppressed)" if ok else
              f"vF2-1={vF2 - 1!r} vG2-1={vG2 - 1!r} delta={delta!r}")


_P2 = {}


def main() -> int:
    global _P2
    print("Cross-sector front-speed B4 two-surface alignment -- bounded-theorem runner")
    print("(conditional on ALLORDERS_B4 premise (A) and the declared supplied context")
    print(" `taste_orbit_summed_front_speed_readout_context`; see companion note)")
    part_1()
    _P2 = part_2()
    p3 = part_3()
    part_4(p3)
    part_5()
    part_6(p3)
    hr("SCORECARD")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
