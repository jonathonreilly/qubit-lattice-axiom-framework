#!/usr/bin/env python3
"""Velocity-RG gauge tensor block, exact lattice WTI, xi-affine drag -- exact-support runner.

Companion runner for
docs/VELOCITY_RG_GAUGE_TENSOR_WTI_XI_AFFINE_DRAG_EXACT_SUPPORT_NOTE_2026-07-17.md

What this runner certifies (two tiers, kept separate):

EXACT TIER (machine-precision identities on the stated finite objects):
  V1  The quadratic (abelian) part of the Wilson plaquette action equals
      K(q) delta_munu - qhat_mu qhat_nu (K = sum_mu qhat_mu^2) EXACTLY in the
      LINK-MIDPOINT mode convention A_mu(x) = Re[eps_mu e^{iq.(x+e_mu/2)}]
      (a site-centered control shows the residual per-direction phases);
      color normalization tr(T^a T^b) = delta^{ab}/2 (su(2) fundamental);
      the form has the exact gauge-orbit zero mode M qhat = 0; the
      xi-family fixed form has the EXACT closed inverse
      (M + xi^-1 qhat qhat^T)^-1 = P_T/K + xi qhat qhat^T/K^2.
  V2  Exact lattice Ward-Takahashi identity for the gauged cos vertex,
      khat_mu Gamma_mu(p, p-k) = S0^-1(p) - S0^-1(p-k), INCLUDING anisotropic
      fermion velocities v_mu (a no-half-shift vertex control violates it).
  V3  The one-loop RAINBOW velocity-drag response a_rb(xi) is EXACTLY affine
      in the gauge parameter xi, and its xi-slope equals a WTI-derived
      longitudinal closed form assembled WITHOUT vertex functions; the
      same-order TADPOLE (fermion-line seagull contracted with the gauge
      line) has the EXACT closed form (1 - xi)(C_s - C_t), whose xi-slope
      -(C_s - C_t) cancels the rainbow's small-probe slope.
      All xi-statements are exact properties of the DECLARED gauge-line
      family D_w(xi) (isotropic projector numerator over the anisotropic
      scalar K_w = sum_mu w_mu khat_mu^2): equal to the V1 covariant-gauge
      closed inverse at w = 1, NOT the inverse of an anisotropic Wilson
      tensor for w != 1 (khat^T D_w(0) != 0). No anisotropic-inverse
      derivation is claimed.

WITNESS TIER (labeled finite-grid one-loop witnesses; no continuum claim):
  V4  As the probe momentum delta -> 0 the rainbow xi-slope approaches the
      PURE GAUGE-LINE integral +(C_s - C_t), C_mu = mean_BZ cos(k_mu)/K_w^2;
      C_s and C_t individually grow with N (log-divergent pieces) while the
      difference's increments shrink through N=24 (finite-grid convergence
      witness for the split).
  V5  The xi-shift of the rainbow response is CONSTANT-DOMINATED over the
      log/const fit window (the log-coefficient shift is a small
      finite-delta transient, bounded by 20% of the constant shift), and
      the per-delta xi-slopes approach the pure gauge-line constant of V4
      MONOTONICALLY through the sampled probe ladder -- and the TOTAL
      xi-slope (rainbow + tadpole) decreases strictly through the four
      sampled probes. Finite samples certify a TREND, not a delta -> 0
      physical limit; the log/const fit split is a diagnostic only.
  V6  Drag-direction convention table, BOTH sectors in ONE Euclidean
      functional-integral convention (see note for the sign derivation):
        fermion two-point: S^-1 = S0^-1 - Sigma, Sigma the standard
          second-order connected insertion, rainbow (the coded -Sig/tot)
          PLUS tadpole (sigma_tad_split);
        gauge two-point: Gamma_2 = M/g^2 + Pi with Pi the second variation
          of -tr log Dslash[A] (bubble + seagull signs as coded; the
          transversality of the DEFORMED-kernel Pi is re-certified here).
      Witnesses: gauge sector faster => fermion velocity response POSITIVE
      (dragged toward the gauge speed); fermion sector faster => induced
      gauge transverse anisotropy POSITIVE (gauge dragged toward the fermion
      speed). These are finite-grid STATIC self-energy responses at fixed
      probes (no shell derivative, counterterm split, or log-coefficient
      extraction): direction PROXIES, not RG beta coefficients. In the 2x2
      exchange algebra built from the proxies the difference mode contracts
      (eigenstructure checked exactly).
  V7  Finite-grid robustness proxies: A_F sign stable N=10 -> N=12; fermion
      drag sign stable and monotone under halving the deformation.

Units: both responses are quoted per unit g^2 with the group factors shown
explicitly (C_F = 3/4 fermion line, su(2) fundamental; T_F = 1/2 already
inside Pi via the 0.5 color-trace factor, seagull-runner convention).
Axis 0 = temporal throughout; the offset (half-integer) BZ grid avoids the
massless propagator pole.

Prints are platform-stable: pass/fail details quote the bound, not raw
residual noise digits; O(1) physics numbers are printed to <= 5 significant
digits.

Output ends with 'TOTAL: PASS=N FAIL=0' on success.
"""

from __future__ import annotations

import math

import numpy as np

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


def hr(title: str) -> None:
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


def bd(name: str, bound: str, ok: bool, val: float) -> str:
    """Platform-stable detail: on pass quote the bound only."""
    if ok:
        return f"{name} within bound {bound} (residual suppressed)"
    return f"{name} = {val!r} VIOLATES bound {bound}"


# ---------------------------------------------------------------------------
# Gamma matrices (seagull-runner block set) and lattice helpers
# ---------------------------------------------------------------------------
I2 = np.eye(2, dtype=complex)
Z2 = np.zeros((2, 2), complex)
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)


def blk(A, B, C, D):
    return np.block([[A, B], [C, D]])


g = np.array(
    [
        blk(Z2, -1j * sx, 1j * sx, Z2),
        blk(Z2, -1j * sy, 1j * sy, Z2),
        blk(Z2, -1j * sz, 1j * sz, Z2),
        blk(I2, Z2, Z2, -I2),
    ],
    complex,
)


def qhat(q):
    return 2 * np.sin(np.array(q) / 2)


def make_bz_grid(n):
    return (np.arange(n) + 0.5) / n * 2 * np.pi - np.pi


def S0inv(p, v):
    return 1j * sum(v[m] * math.sin(p[m]) * g[m] for m in range(4))


# ---------------------------------------------------------------------------
# V1 -- exact gauge tensor block
# ---------------------------------------------------------------------------
def S2_lattice(A):
    s = 0.0
    for mu in range(4):
        for nu in range(mu + 1, 4):
            F = (np.roll(A[..., nu], -1, axis=mu) - A[..., nu]) - (
                np.roll(A[..., mu], -1, axis=nu) - A[..., mu]
            )
            s += 0.5 * np.sum(F**2)
    return s


def plaquette_mode(N, qidx, eps, midpoint: bool):
    X = np.stack(np.meshgrid(*[np.arange(N)] * 4, indexing="ij"), -1)
    q = 2 * np.pi * np.array(qidx) / N
    phase = X @ q
    shift = (q / 2) if midpoint else np.zeros(4)
    A = np.stack(
        [np.real(np.exp(1j * (phase + shift[m]))) * eps[m] for m in range(4)], -1
    )
    s_lat = S2_lattice(A)
    qh = qhat(q)
    K = float(np.sum(qh**2))
    M = K * np.eye(4) - np.outer(qh, qh)
    V = N**4
    s_pred = 0.5 * V * 0.5 * (eps @ M @ eps)
    return s_lat, s_pred


def part_1(rng) -> None:
    hr("V1: exact gauge tensor block (plaquette form, zero mode, xi-inverse)")
    N = 6
    worst = 0.0
    good = True
    for qidx in [(1, 0, 0, 0), (1, 2, 0, 1), (2, 1, 1, 0)]:
        eps = rng.standard_normal(4)
        a, b = plaquette_mode(N, qidx, eps, midpoint=True)
        rel = abs(a - b) / max(abs(b), 1e-30)
        worst = max(worst, rel)
        good &= abs(a - b) <= 1e-9 * max(abs(b), 1.0)
    check(
        "plaquette quadratic form == K*delta - qhat qhat^T EXACTLY "
        "(link-midpoint modes, direct lattice sum, 3 modes)",
        good,
        bd("worst rel err", "1e-9", good, worst),
    )

    eps = rng.standard_normal(4)
    a, b = plaquette_mode(N, (1, 2, 0, 1), eps, midpoint=False)
    rel = abs(a - b) / max(abs(b), 1e-30)
    ok = rel > 1e-3
    check(
        "CONTROL: site-centered modes (no half-shift) MISS the closed form "
        "(link-midpoint is the exact convention)",
        ok,
        f"site-centered rel mismatch = {rel:.4f} > 1e-3",
    )

    T = [sx / 2, sy / 2, sz / 2]
    col = all(
        abs(np.trace(T[a2] @ T[b2]) - 0.5 * (a2 == b2)) < 1e-14
        for a2 in range(3)
        for b2 in range(3)
    )
    check("color normalization tr(T^a T^b) = delta^{ab}/2 (su(2) fundamental)", col)

    good_zero = True
    good_inv = True
    worst_zero = 0.0
    worst_inv = 0.0
    for _ in range(6):
        q = rng.uniform(-3, 3, 4)
        qh = qhat(q)
        K = float(qh @ qh)
        M = K * np.eye(4) - np.outer(qh, qh)
        rz = float(np.max(np.abs(M @ qh)))
        worst_zero = max(worst_zero, rz)
        good_zero &= rz < 1e-11 * max(K, 1.0)
        xi = rng.uniform(0.1, 2.5)
        Mfix = M + np.outer(qh, qh) / xi
        PT = np.eye(4) - np.outer(qh, qh) / K
        D = PT / K + xi * np.outer(qh, qh) / K**2
        ri = float(np.max(np.abs(Mfix @ D - np.eye(4))))
        worst_inv = max(worst_inv, ri)
        good_inv &= ri < 1e-11
    check(
        "exact gauge-orbit zero mode: M qhat = 0 (6 seeded momenta)",
        good_zero,
        bd("max |M qhat| / max(K,1)", "1e-11", good_zero, worst_zero),
    )
    check(
        "exact closed inverse: (M + xi^-1 qhat qhat^T)^-1 == "
        "P_T/K + xi qhat qhat^T/K^2 (6 seeded (q, xi))",
        good_inv,
        bd("max |Mfix D - 1|", "1e-11", good_inv, worst_inv),
    )


# ---------------------------------------------------------------------------
# V2 -- exact lattice WTI
# ---------------------------------------------------------------------------
def part_2(rng) -> None:
    hr("V2: exact lattice Ward-Takahashi identity (anisotropic velocities)")
    worst = 0.0
    good = True
    worst_ctrl = None
    for _ in range(6):
        p = rng.uniform(-3, 3, 4)
        k = rng.uniform(-3, 3, 4)
        v = rng.uniform(0.5, 1.5, 4)
        kh = qhat(k)
        lhs = sum(kh[m] * 1j * v[m] * math.cos(p[m] - k[m] / 2) * g[m] for m in range(4))
        rhs = S0inv(p, v) - S0inv(p - k, v)
        r = float(np.max(np.abs(lhs - rhs)))
        worst = max(worst, r)
        good &= r < 1e-11
        lhs_ctrl = sum(kh[m] * 1j * v[m] * math.cos(p[m]) * g[m] for m in range(4))
        rc = float(np.max(np.abs(lhs_ctrl - rhs)))
        worst_ctrl = rc if worst_ctrl is None else min(worst_ctrl, rc)
    check(
        "khat.Gamma == S0^-1(p) - S0^-1(p-k) EXACTLY for the midpoint cos "
        "vertex, INCLUDING anisotropic v_mu (6 seeded draws)",
        good,
        bd("worst residual", "1e-11", good, worst),
    )
    ok = worst_ctrl > 1e-2
    check(
        "CONTROL: no-half-shift vertex cos(p_mu) VIOLATES the WTI "
        "(midpoint is the Ward-exact vertex)",
        ok,
        f"min residual over draws = {worst_ctrl:.4f} > 1e-2",
    )


# ---------------------------------------------------------------------------
# One-loop machinery (fermion side): drag response and WTI slope
# ---------------------------------------------------------------------------
def sigma_kin_aniso(Ng, xi, dlt, eps=0.10, chunk=40000):
    """Fermion kinetic-coefficient anisotropy (out_s - out_t) at probe dlt,
    one-gluon exchange (RAINBOW diagram) with anisotropic gauge weights w
    and gauge param xi.  Coded object: Sig = -(sum)/tot == the standard
    second-order connected insertion Sigma; the vertices are coded as
    gamma*cos WITHOUT the explicit i, and the (i)(i) = -1 of the i-full
    vertices is carried by the overall minus (see note, sign chain).  The
    same-order fermion-line seagull TADPOLE is sigma_tad_split below.
    Gauge line: the DECLARED family
    D_w(xi)_munu = (delta_munu - (1 - xi) khat_mu khat_nu / K_w) / K_w,
    K_w = sum_mu w_mu khat_mu^2 -- isotropic projector numerator over the
    anisotropic scalar denominator. At w = 1 this is the V1 covariant-gauge
    closed inverse; for w != 1 it is NOT the inverse of an anisotropic
    Wilson tensor (khat^T D_w(0) != 0), and no such derivation is claimed."""
    ax = make_bz_grid(Ng)
    w = np.array([1 - eps / 2, 1 + eps / 2, 1 + eps / 2, 1 + eps / 2])
    out = {}
    for axis in (0, 1):
        p = np.zeros(4)
        p[axis] = dlt
        Sig = np.zeros((4, 4), complex)
        tot = Ng**4
        i0 = 0
        while i0 < tot:
            idx = np.arange(i0, min(i0 + chunk, tot))
            i0 += chunk
            a, r = np.divmod(idx, Ng**3)
            b, r = np.divmod(r, Ng**2)
            c, d = np.divmod(r, Ng)
            k = np.stack([ax[a], ax[b], ax[c], ax[d]], 1)
            pk = p - k
            s = np.sin(pk)
            Df = np.sum(s**2, 1)
            Sf = (-1j * np.einsum("ca,aij->cij", s, g)) / Df[:, None, None]
            kh = 2 * np.sin(k / 2)
            K = np.sum(w * kh**2, 1)
            cmu = np.cos(p - k / 2)
            for mu in range(4):
                VS = (cmu[:, mu][:, None, None] * g[mu]) @ Sf
                for nu in range(4):
                    Dmn = ((mu == nu) * 1.0 - (1 - xi) * kh[:, mu] * kh[:, nu] / K) / K
                    Sig += np.einsum(
                        "c,cij->ij", Dmn, (VS @ (cmu[:, nu][:, None, None] * g[nu]))
                    )
        Sig = -Sig / tot
        out[axis] = np.real(np.trace(g[axis] @ Sig) / (4j * np.sin(dlt)))
    return out[1] - out[0]


def sigma_tad_split(Ng, xi, eps=0.10):
    """Same-order fermion-line seagull TADPOLE.  Expanding the covariant
    kinetic kernel sin(p_mu + A_mu) to O(A^2) gives the seagull vertex
    V2_mu = -i v_mu sin(p_mu) g_mu; contracting with the coincident gauge
    line gives Sigma_tad = -(1/2) sum_mu <D_mumu>_BZ V2_mu.  The kinetic
    extraction out = Re tr(g Sig)/(4i sin(dlt)) collapses to
    out_tad_axis = (1/2) <D_axis,axis>_BZ -- EXACTLY probe-independent.
    Split identity, exact on any grid (kh_s^2 - kh_t^2 = 2 cos k_t
    - 2 cos k_s pointwise):
        (out_s - out_t)_tad = (1 - xi)(C_s - C_t)."""
    ax = make_bz_grid(Ng)
    w = np.array([1 - eps / 2, 1 + eps / 2, 1 + eps / 2, 1 + eps / 2])
    k = np.stack(np.meshgrid(*[ax] * 4, indexing="ij"), -1).reshape(-1, 4)
    kh = 2 * np.sin(k / 2)
    K = (kh**2) @ w

    def D_diag(mu):
        return float(np.mean((1.0 - (1 - xi) * kh[:, mu] ** 2 / K) / K))

    return 0.5 * (D_diag(1) - D_diag(0))


def slope_pred(Ng, dlt, eps=0.10, chunk=40000):
    """WTI-derived xi-slope: d Sigma / d xi assembled WITHOUT vertex
    functions.  d/dxi of the gauge line is +khat khat^T/K^2; contracting
    khat.Gamma via the exact WTI (V2) gives the integrand
    S0^-1(p) S_f S0^-1(p) - 2 S0^-1(p) + S0^-1(p-k).  The runner vertex is
    (gamma cos) WITHOUT the i (i^2 = -1 absorbed), so khat.Gamma_runner =
    [S0^-1(p) - S0^-1(p-k)]/i and the sandwich picks up an extra -1
    (the -term below); overall -Sig/tot as in sigma_kin_aniso."""
    ax = make_bz_grid(Ng)
    w = np.array([1 - eps / 2, 1 + eps / 2, 1 + eps / 2, 1 + eps / 2])
    out = {}
    for axis in (0, 1):
        p = np.zeros(4)
        p[axis] = dlt
        S0inv_p = S0inv(p, np.ones(4))
        Sig = np.zeros((4, 4), complex)
        tot = Ng**4
        i0 = 0
        while i0 < tot:
            idx = np.arange(i0, min(i0 + chunk, tot))
            i0 += chunk
            a, r = np.divmod(idx, Ng**3)
            b, r = np.divmod(r, Ng**2)
            c, d = np.divmod(r, Ng)
            k = np.stack([ax[a], ax[b], ax[c], ax[d]], 1)
            pk = p - k
            s = np.sin(pk)
            Df = np.sum(s**2, 1)
            Sf = (-1j * np.einsum("ca,aij->cij", s, g)) / Df[:, None, None]
            S0inv_pk = 1j * np.einsum("ca,aij->cij", s, g)
            kh = 2 * np.sin(k / 2)
            K = np.sum(w * kh**2, 1)
            term = (
                S0inv_p[None, :, :] @ Sf @ S0inv_p[None, :, :]
                - 2 * S0inv_p[None, :, :]
                + S0inv_pk
            )
            Sig += np.einsum("c,cij->ij", 1.0 / K**2, -term)
        Sig = -Sig / tot
        out[axis] = np.real(np.trace(g[axis] @ Sig) / (4j * np.sin(dlt)))
    return out[1] - out[0]


def C_split_detail(Ng, eps=0.10):
    """Pure gauge-line integrals C_mu = mean_BZ cos(k_mu)/K_w(k)^2."""
    ax = make_bz_grid(Ng)
    w = np.array([1 - eps / 2, 1 + eps / 2, 1 + eps / 2, 1 + eps / 2])
    k = np.stack(np.meshgrid(*[ax] * 4, indexing="ij"), -1).reshape(-1, 4)
    kh = 2 * np.sin(k / 2)
    K = (kh**2) @ w
    Ct = float(np.mean(np.cos(k[:, 0]) / K**2))
    Cs = float(np.mean(np.cos(k[:, 1]) / K**2))
    return Cs, Ct


# ---------------------------------------------------------------------------
# V3 -- exact xi-affinity of the drag response
# ---------------------------------------------------------------------------
def part_3() -> dict:
    hr("V3: rainbow a(xi) exactly affine; tadpole closed form; WTI slope")
    Ng, dlt = 10, 0.30
    xis = [0.0, 0.5, 1.0, 1.7]
    vals = [sigma_kin_aniso(Ng, x, dlt) for x in xis]
    sl = (vals[-1] - vals[0]) / (xis[-1] - xis[0])
    lin_res = max(
        abs(vals[i] - (vals[0] + sl * (xis[i] - xis[0]))) for i in range(len(xis))
    )
    ok = lin_res < 1e-11
    check(
        "RAINBOW a_rb(xi) EXACTLY affine in xi over xi in {0, 0.5, 1.0, 1.7} "
        "(N=10, delta=0.30)",
        ok,
        bd("max dev from line", "1e-11", ok, lin_res)
        + f"; a_rb(1)={vals[2]:+.5f}, slope={sl:+.5f}",
    )

    sp = slope_pred(Ng, dlt)
    ok = abs(sp - sl) < 1e-10
    check(
        "rainbow xi-slope == WTI-derived longitudinal closed form "
        "(assembled WITHOUT vertex functions)",
        ok,
        bd("|pred - measured|", "1e-10", ok, abs(sp - sl))
        + f"; pred={sp:+.5f}",
    )

    Cs10, Ct10 = C_split_detail(Ng)
    cs10 = Cs10 - Ct10
    tads = [sigma_tad_split(Ng, x) for x in xis]
    dev_tad = max(abs(tads[i] - (1 - xis[i]) * cs10) for i in range(len(xis)))
    ok = dev_tad < 1e-11
    check(
        "TADPOLE split == (1 - xi)(C_s - C_t) EXACTLY (same-order fermion-"
        "line seagull; probe-independent; xi-slope = -(C_s - C_t))",
        ok,
        bd("max dev from closed form", "1e-11", ok, dev_tad)
        + f"; tad(0)={tads[0]:+.6f}, C_s-C_t={cs10:+.6f}",
    )

    tots = [vals[i] + tads[i] for i in range(len(xis))]
    ok = all((t < 0) == (tots[0] < 0) for t in tots)
    check(
        "sign of the TOTAL drag a_rb(xi) + a_tad(xi) is xi-ROBUST across "
        "the covariant family xi in [0, 1.7]",
        ok,
        "totals " + ", ".join(f"{t:+.5f}" for t in tots),
    )
    return {"slope": sl, "vals": vals, "xis": xis}


# ---------------------------------------------------------------------------
# V4 -- delta->0 pure gauge-line limit and IR-finite split
# ---------------------------------------------------------------------------
def part_4() -> dict:
    hr("V4: small-probe gauge-line constant; IR-finite (C_s - C_t) split")
    Ng = 10
    Cs10, Ct10 = C_split_detail(Ng)
    cs = Cs10 - Ct10
    sp_small = slope_pred(Ng, 0.05)
    ok = abs(sp_small - cs) < 5e-3 * max(abs(cs), 1e-6)
    check(
        "small probe delta=0.05: RAINBOW xi-slope within rel 5e-3 of "
        "+(C_s - C_t), a PURE GAUGE-LINE integral (no fermion line; N=10; "
        "finite-probe witness, no delta -> 0 limit claim)",
        ok,
        f"slope(0.05)={sp_small:+.6f} vs +(C_s-C_t)={cs:+.6f} "
        f"(rel bound 5e-3 {'holds' if ok else 'VIOLATED'})",
    )

    rows = []
    prev = None
    for N in (8, 12, 16, 20, 24):
        Cs, Ct = C_split_detail(N)
        d = Cs - Ct
        if prev is not None:
            rows.append((N, Cs - prev[0], Ct - prev[1], d - prev[2]))
        prev = (Cs, Ct, d)
    dCs_last = rows[-1][1]
    dDiff_last = rows[-1][3]
    grow = all(r[1] > 0 and r[2] > 0 for r in rows)
    ok = grow and dCs_last > 10 * abs(dDiff_last)
    check(
        "C_s, C_t individually still GROWING at N=24 (log-divergent pieces; "
        "last increment > 10x the difference increment)",
        ok,
        f"dC_s(20->24)={dCs_last:+.5f}, dDiff(20->24)={dDiff_last:+.6f}",
    )
    diffs_shrink = all(
        abs(rows[i + 1][3]) < abs(rows[i][3]) for i in range(len(rows) - 1)
    )
    ok = diffs_shrink and abs(dDiff_last) < 0.05 * abs(prev[2])
    check(
        "(C_s - C_t) increments SHRINK through N=24 (strictly; last < 5% of "
        "value): finite-grid convergence witness for the split (no "
        "continuum claim)",
        ok,
        f"(C_s-C_t)(N=24)={prev[2]:+.6f}, |dDiff_last|/|value|="
        f"{abs(dDiff_last) / max(abs(prev[2]), 1e-30):.4f}",
    )
    return {"cs": cs, "cs24": prev[2]}


# ---------------------------------------------------------------------------
# V5 -- gauge invariance of the log coefficient
# ---------------------------------------------------------------------------
def part_5(p4: dict) -> dict:
    hr("V5: xi-shift constant-dominated (fit diagnostic); TOTAL xi-slope "
       "decreasing through the probe ladder")
    Ng = 10
    dls = [0.5, 0.35, 0.25, 0.18]
    X = np.array([math.log(1 / d) for d in dls])
    fits = {}
    ys_by_xi = {}
    for xi in (0.0, 1.0):
        ys = [sigma_kin_aniso(Ng, xi, d) for d in dls]
        ys_by_xi[xi] = ys
        A, B = np.polyfit(X, np.array(ys), 1)
        fits[xi] = (float(A), float(B))
        print(
            f"  xi={xi}: A_F(log)={A:+.5f}  B_F(const)={B:+.5f}  "
            "raw=" + ", ".join(f"{y:+.5f}" for y in ys)
        )
    A0, B0 = fits[0.0]
    A1, B1 = fits[1.0]
    ok = abs(A1 - A0) < 0.20 * abs(B1 - B0)
    check(
        "xi-shift of the RAINBOW response CONSTANT-DOMINATED over the fit "
        "window: log-coefficient shift |A(1)-A(0)| < 20% of the constant "
        "shift |B(1)-B(0)| (delta in [0.18, 0.5]; A_F itself is "
        "subdominant to B_F at both xi; the (A, B) split is a "
        "FIT-PIVOT-DEPENDENT diagnostic, not an extracted RG coefficient)",
        ok,
        f"A(0)={A0:+.5f} A(1)={A1:+.5f} B(1)-B(0)={B1 - B0:+.5f} "
        f"ratio={abs(A1 - A0) / max(abs(B1 - B0), 1e-30):.2f}",
    )

    slopes = [ys_by_xi[1.0][i] - ys_by_xi[0.0][i] for i in range(len(dls))]
    cs = p4["cs"]
    devs = [abs(s - cs) for s in slopes]
    mono = all(devs[i + 1] < devs[i] for i in range(len(devs) - 1))
    ok = mono and devs[0] < 0.30 * abs(cs)
    check(
        "per-delta RAINBOW xi-slope a_rb(1)-a_rb(0) approaches +(C_s - C_t) "
        "MONOTONICALLY through the sampled probe ladder (deviations "
        "strictly shrinking; worst < 30%; V4 witnesses delta=0.05 at rel "
        "5e-3; finite samples, no delta -> 0 limit claim)",
        ok,
        "slopes " + ", ".join(f"{s:+.6f}" for s in slopes) + f" vs {cs:+.6f}",
    )

    tad_sl = sigma_tad_split(Ng, 1.0) - sigma_tad_split(Ng, 0.0)
    tot_slopes = [s + tad_sl for s in slopes]
    mono_t = all(
        abs(tot_slopes[i + 1]) < abs(tot_slopes[i])
        for i in range(len(tot_slopes) - 1)
    )
    ok = mono_t and abs(tot_slopes[-1]) < 0.10 * abs(cs)
    check(
        "TOTAL xi-slope (rainbow + tadpole) decreases STRICTLY through the "
        "four sampled probes (final < 10% of C_s - C_t): a xi-robustness "
        "TREND witness for the declared family (no delta -> 0 limit claim)",
        ok,
        "total slopes " + ", ".join(f"{s:+.6f}" for s in tot_slopes)
        + f"; scale C_s-C_t = {cs:+.6f}",
    )
    return {"ys1": ys_by_xi[1.0], "dls": dls}


# ---------------------------------------------------------------------------
# Gauge-side machinery: Pi from the second variation of -tr log Dslash[A]
# ---------------------------------------------------------------------------
def pi_munu(qv, N, v, include_seagull=True, chunk=50000):
    """Fermion-loop Pi for the kernel sum_mu v_mu sin(k_mu).  Gauging
    k_mu -> k_mu + A_mu puts v_mu into the propagators, the one-gluon vertex
    v_mu cos(k_mu + q_mu/2), AND the seagull -v_mu sin(k_mu) delta_munu.
    Signs are those of the second variation of -tr log Dslash[A]
    (+ bubble, - seagull trace); the 0.5 is the color trace T_F = 1/2."""
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
        Sk = (-1j * np.einsum("ca,aij->cij", sk, g)) / Dk[:, None, None]
        Skq = (-1j * np.einsum("ca,aij->cij", skq, g)) / Dkq[:, None, None]
        cmid = np.cos(k + q / 2) * v
        sk_mu = np.sin(k) * v
        for mu in range(4):
            Vmu = 1j * cmid[:, mu][:, None, None] * g[mu]
            SV = Sk @ Vmu @ Skq
            for nu in range(4):
                Vnu = 1j * cmid[:, nu][:, None, None] * g[nu]
                Pi[mu, nu] += np.einsum("cii->", SV @ Vnu)
            if include_seagull:
                Dmm = (-1j) * sk_mu[:, mu][:, None, None] * g[mu]
                Pi[mu, mu] += -np.einsum("cij,cji->", Sk, Dmm)
    return 0.5 * Pi / tot


def ward(Pi, qv):
    kh = qhat(qv)
    return float(
        np.max(np.abs(kh @ Pi)) / (np.linalg.norm(kh) * np.max(np.abs(Pi)) + 1e-30)
    )


# ---------------------------------------------------------------------------
# V6 -- drag-direction convention table (both sectors, one convention)
# ---------------------------------------------------------------------------
def part_6() -> dict:
    hr("V6: drag directions, BOTH sectors in ONE functional-integral convention")
    # Discharge C_F from the SU(2) fundamental generator algebra (no import):
    # T^a = sigma^a/2, sum_a T^a T^a = C_F * I.
    paulis = [
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    ]
    casimir = sum((p / 2) @ (p / 2) for p in paulis)
    C_F = float(np.real(casimir[0, 0]))
    ok = (
        np.max(np.abs(casimir - C_F * np.eye(2))) < 1e-15
        and abs(C_F - 3.0 / 4.0) < 1e-15
    )
    check(
        "C_F discharged from the SU(2) fundamental generator algebra: "
        "sum_a T^a T^a = (3/4) I exactly (no hard-coded Casimir)",
        ok,
        "casimir sum is C_F*I with C_F = 3/4 (exact rational check)",
    )

    print("  Convention (single Euclidean bookkeeping; sign chain in the "
          "note):")
    print("    fermion: S^-1 = S0^-1 - Sigma (rainbow + tadpole); kinetic "
          "coeffs v_mu -> v_mu - g^2 C_F out_mu (linear in v)")
    print("    gauge:   Gamma_2 = M/g^2 + Pi (Pi = second variation of "
          "-tr log Dslash); c_mu -> w_mu + g^2 Pi_T/qhat^2")

    # Fermion response to a FASTER gauge sector: weights w = (1-e/2, 1+e/2,..)
    # give gauge speed sqrt(w_s/w_t) => EXACT offset dv_B = sqrt(w_s/w_t) - 1
    # (the eps/2 linearization is NOT used; for eps=0.10 the exact offset is
    # sqrt(1.05/0.95) - 1, about 2.6% larger than eps/2).
    eps = 0.10
    sig_rb = sigma_kin_aniso(10, 0.0, 0.30, eps=eps)
    sig_tad = sigma_tad_split(10, 0.0, eps=eps)
    sig = sig_rb + sig_tad
    dvB_off = float(np.sqrt((1 + eps / 2) / (1 - eps / 2)) - 1.0)
    dvF_resp = -C_F * sig
    ok = dvF_resp > 0
    check(
        f"gauge sector FASTER (exact dv_B={dvB_off:+.5f}) => fermion "
        "velocity STATIC response POSITIVE (rainbow + tadpole TOTAL): "
        "fermion dragged TOWARD the gauge speed",
        ok,
        f"dv_F response = -C_F*(out_s-out_t)_total = {dvF_resp:+.5f} per "
        f"g^2 (rainbow {sig_rb:+.5f} + tadpole {sig_tad:+.5f}; C_F "
        f"discharged above; N=10, delta=0.30)",
    )

    # Gauge response to a FASTER fermion sector: v = (1-e/2, 1+e/2, ...)
    # (linear coefficients) => offset dv_F = v_s/v_t - 1.
    N = 12
    v_def = np.array([1 - 0.05, 1 + 0.05, 1 + 0.05, 1 + 0.05])
    dvF_off = float(v_def[1] / v_def[0] - 1.0)
    Pi_t = np.real(pi_munu([0.3, 0.0, 0.0, 0.0], N, v_def))
    Pi_s = np.real(pi_munu([0.0, 0.3, 0.0, 0.0], N, v_def))
    w_t = ward(Pi_t, [0.3, 0.0, 0.0, 0.0])
    w_s = ward(Pi_s, [0.0, 0.3, 0.0, 0.0])
    ok = max(w_t, w_s) < 0.05
    check(
        "deformed-kernel Pi stays TRANSVERSE at both probes (the sign chain "
        "consumes the -tr log assembly this certifies)",
        ok,
        f"normalized Ward residuals ({w_t:.4f}, {w_s:.4f}) < 0.05 (N=12)",
    )
    kh2 = float(qhat([0.3, 0.0, 0.0, 0.0])[0] ** 2)
    piT_t = float(Pi_t[1, 1]) / kh2
    piT_s = float(Pi_s[2, 2]) / kh2
    ind = piT_s - piT_t
    dvB_resp = ind / 2
    ok = dvB_resp > 0
    check(
        "fermion sector FASTER (dv_F=+0.10526) => induced gauge transverse "
        "anisotropy STATIC response POSITIVE: gauge dragged TOWARD the "
        "fermion speed",
        ok,
        f"dv_B response = (piT_s - piT_t)/2 = {dvB_resp:+.5f} per g^2 "
        f"(T_F=1/2 inside Pi; N=12, probe q=0.3, spatial polarization both)",
    )

    a_proxy = dvF_resp / dvB_off
    b_proxy = dvB_resp / dvF_off
    ok = a_proxy > 0 and b_proxy > 0
    check(
        "exchange-matrix coefficients: a-proxy > 0 AND b-proxy > 0 "
        "(finite-grid STATIC-RESPONSE sign witnesses for the named open "
        "input of the exchange-matrix support note; NOT RG beta-function "
        "coefficients -- no shell derivative or log-coefficient extraction)",
        ok,
        f"a-proxy={a_proxy:+.4f} b-proxy={b_proxy:+.4f} per g^2 "
        "(magnitudes are labeled finite-grid scheme proxies; the signs are "
        "the witnessed content)",
    )

    F = np.array([[-a_proxy, a_proxy], [b_proxy, -b_proxy]])
    ev = np.sort(np.linalg.eigvals(F).real)
    ok_eig = abs(ev[1]) < 1e-10 and abs(ev[0] + (a_proxy + b_proxy)) < 1e-10
    null = F @ np.array([1.0, 1.0])
    ok = ok_eig and float(np.max(np.abs(null))) < 1e-10
    check(
        "2x2 exchange algebra: eigenvalues {0, -(a+b)}; null direction "
        "(1,1) (common speed); the DIFFERENCE mode contracts",
        ok,
        f"contraction rate a+b = {a_proxy + b_proxy:+.4f} per g^2"
        if ok
        else f"eig={ev!r} null={null!r}",
    )
    return {"sig": sig, "eps": eps}


# ---------------------------------------------------------------------------
# V7 -- finite-grid robustness proxies
# ---------------------------------------------------------------------------
def part_7(p5: dict, p6: dict) -> None:
    hr("V7: finite-grid robustness proxies (labeled; no continuum claim)")
    dls = p5["dls"]
    ys10 = p5["ys1"]
    ys12 = [sigma_kin_aniso(12, 1.0, d) for d in dls]
    signs = all((a < 0) == (b < 0) for a, b in zip(ys10, ys12))
    reldiff = max(
        abs(a - b) / max(abs(a), abs(b)) for a, b in zip(ys10, ys12)
    )
    ok = signs and reldiff < 0.5
    check(
        "drag response a(xi=1, delta) sign stable and magnitude within 50% "
        "under N=10 -> N=12, all four probe deltas (labeled finite-grid "
        "proxy; the tadpole split vanishes at xi=1, so this IS the total)",
        ok,
        "a(N=12) " + ", ".join(f"{y:+.5f}" for y in ys12)
        + f"; worst reldiff vs N=10 = {reldiff:.2f}",
    )

    sig10 = p6["sig"]
    sig05 = sigma_kin_aniso(10, 0.0, 0.30, eps=0.05) + sigma_tad_split(
        10, 0.0, eps=0.05
    )
    ok = ((sig05 < 0) == (sig10 < 0)) and abs(sig05) < abs(sig10)
    check(
        "TOTAL fermion drag (rainbow + tadpole) sign stable and monotone "
        "under halving the gauge deformation (eps 0.10 -> 0.05)",
        ok,
        f"total-split(0.10)={sig10:+.5f}  total-split(0.05)={sig05:+.5f}",
    )


def main() -> int:
    print("Velocity-RG gauge tensor block, exact WTI, xi-affine drag -- "
          "exact-support runner")
    print("(exact tier V1-V3; labeled finite-grid witness tier V4-V7; "
          "see companion note)")
    rng = np.random.default_rng(7)
    part_1(rng)
    part_2(rng)
    part_3()
    p4 = part_4()
    p5 = part_5(p4)
    p6 = part_6()
    part_7(p5, p6)
    hr("SCORECARD")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
