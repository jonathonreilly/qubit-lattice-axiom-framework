#!/usr/bin/env python3
"""Certifier for the discrete-Poisson = exact c=infinity field bridge theorem.

Operator under test (exactly as in scripts/wave_retarded_gravity.py line 125):

    f_next = 2 f_curr - f_prev + h2 (lap[f_curr] + src)

with lap the interior-only 5-point Dirichlet stencil
    lap[i,j] = f[i-1,j] + f[i+1,j] + f[i,j-1] + f[i,j+1] - 4 f[i,j]
on an nw x nw grid, f=0 on the boundary, only interior points updated,
h2 = H^2 (H = 0.5), dt = 1, src a fixed point source.

Bridge theorem (proved analytically in the source note; this runner is the
numerical certificate):

  The discrete Poisson solve f*, defined by  L f* = -src  with the same
  Dirichlet boundary, is the EXACT c=infinity instantaneous field of this
  operator, in two precise senses:

  (A) FIXED POINT. f* is the unique time-independent fixed point of the
      update. Uniqueness <=> the interior Dirichlet 5-point Laplacian L is
      invertible. L is symmetric negative-definite (all eigenvalues in
      [-8,0), strictly), hence invertible; f* = -L^{-1} src is unique.

  (B) c -> infinity / STATIC IDENTIFICATION. f* is independent of h2 (=c^2
      dt^2). It is exactly the static (time-independent) solution of the
      wave operator for the current source, i.e. the elliptic limit. With
      any positive damping it is the unique attractor; undamped, it is the
      exact time-average of the frozen-source-from-rest evolution.

  NEGATIVE CONTROL. The finite-time undamped frozen-source snapshot formerly
      used by wave_retarded_gravity.py does NOT equal f*. It carries a fixed
      transient about f*; only its infinite-time average is f*. Using that
      snapshot as the c=infinity comparator is therefore incorrect. We
      quantify the gap for the exact parameters used by
      wave_retarded_gravity.py (NL=30, source switched on at NL//3,
      read at NL-1), and include a generic center-source stress case.

All checks are deterministic and use only numpy. PASS prints CERT lines;
any FAIL raises SystemExit(1).
"""

from __future__ import annotations

import numpy as np

# Heavy compute / sweep runner — `AUDIT_TIMEOUT_SEC = 1800` ceiling.
AUDIT_TIMEOUT_SEC = 1800

H = 0.5
H2 = H * H
TOL = 1e-10


def interior_dirichlet_laplacian(nint: int) -> np.ndarray:
    """Dense interior-only 5-point Dirichlet Laplacian on an nint x nint grid.

    Acts on the (nint^2) interior unknowns; boundary f is identically 0 and
    contributes nothing (Dirichlet). This is exactly the linear operator the
    leapfrog update applies to interior points.
    """
    n = nint * nint
    mat = np.zeros((n, n))

    def idx(i: int, j: int) -> int:
        return i * nint + j

    for i in range(nint):
        for j in range(nint):
            r = idx(i, j)
            mat[r, r] = -4.0
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ii, jj = i + di, j + dj
                if 0 <= ii < nint and 0 <= jj < nint:
                    mat[r, idx(ii, jj)] += 1.0
    return mat


def report(label: str, ok: bool, detail: str) -> bool:
    tag = "CERT" if ok else "FAIL"
    print(f"  [{tag}] {label}: {detail}")
    return ok


def part_a_fixed_point_uniqueness() -> bool:
    """L symmetric negative-definite => f* = -L^{-1} src unique fixed point."""
    print("\n(A) FIXED-POINT UNIQUENESS (L symmetric negative-definite)")
    all_ok = True
    # Cover small grids and the exact wave_retarded_gravity.py interior size.
    # nw = 2*int(8/0.5)+1 = 33 -> interior 31x31.
    for nint in (3, 5, 8, 15, 31):
        mat = interior_dirichlet_laplacian(nint)
        sym = float(np.max(np.abs(mat - mat.T)))
        ev = np.linalg.eigvalsh(mat)
        neg_def = bool(ev.max() < -TOL)
        # Gershgorin/known bound: eigenvalues of 2D 5-point lie in (-8, 0).
        in_band = bool(ev.min() > -8.0 - TOL and ev.max() < 0.0)
        ok = (sym < TOL) and neg_def and in_band
        all_ok &= report(
            f"nint={nint:2d}",
            ok,
            f"sym_err={sym:.1e} eig in [{ev.min():.5f},{ev.max():.5f}] "
            f"neg_def={neg_def} in(-8,0)={in_band}",
        )

    # Uniqueness in action: solve L f* = -src and confirm exact fixed point.
    nint = 31
    mat = interior_dirichlet_laplacian(nint)
    n = nint * nint
    src = np.zeros(n)
    src[n // 2] = 0.004  # match S in the harness
    fstar = np.linalg.solve(mat, -src)
    res = float(np.max(np.abs(mat @ fstar + src)))
    # second time-difference vanishes => update residual is exactly H2*(L f*+src)
    update_res = H2 * res
    ok = res < 1e-12 and update_res < 1e-12
    all_ok &= report(
        "f* solves L f*=-src and is exact update fixed point",
        ok,
        f"|L f*+src|={res:.2e}, leapfrog residual H2*|L f*+src|={update_res:.2e}",
    )
    return all_ok


def part_b_cinf_identification() -> bool:
    """f* is h2(=c^2)-independent and is the elliptic/static solution."""
    print("\n(B) c->infinity / STATIC IDENTIFICATION (f* independent of c)")
    all_ok = True
    nint = 15
    mat = interior_dirichlet_laplacian(nint)
    n = nint * nint
    src = np.zeros(n)
    src[n // 2] = 1.0
    fstar = np.linalg.solve(mat, -src)
    # f* solves L f*=-src with NO reference to h2; the time-independent fixed
    # point of the update is the SAME f* for every h2>0 (c-independent).
    for h2 in (0.01, 0.25, 1.0, 3.0):
        res = h2 * float(np.max(np.abs(mat @ fstar + src)))
        ok = res < 1e-12
        all_ok &= report(
            f"h2={h2:5.2f}",
            ok,
            f"fixed-point residual h2*|L f*+src|={res:.2e} (same f* for all c)",
        )

    # Adiabatic / damped attractor: with positive damping gamma>0 the
    # frozen-source-from-rest evolution converges to f* (the c=inf field that
    # the slow source tracks). Update with a standard velocity damping term.
    gamma = 0.02
    fprev = np.zeros(n)
    fcurr = np.zeros(n)
    for _ in range(2, 8000):
        fnext = 2 * fcurr - fprev + H2 * (mat @ fcurr + src) - 2 * gamma * (fcurr - fprev)
        fprev, fcurr = fcurr, fnext
    gap_damped = float(np.max(np.abs(fcurr - fstar)))
    ok = gap_damped < 1e-8
    all_ok &= report(
        "damped late snapshot -> f*",
        ok,
        f"gamma={gamma}, max|f-f*|={gap_damped:.2e} (unique attractor)",
    )

    # Undamped time-AVERAGE equals f* exactly (per-mode <1-cos-tan*sin> -> 1).
    fprev = np.zeros(n)
    fcurr = np.zeros(n)
    acc = np.zeros(n)
    steps = 200000
    for _ in range(steps):
        fnext = 2 * fcurr - fprev + H2 * (mat @ fcurr + src)
        fprev, fcurr = fcurr, fnext
        acc += fcurr
    avg_gap = float(np.max(np.abs(acc / steps - fstar)))
    ok = avg_gap < 5e-4  # 1/steps Cesaro residual; shrinks like 1/N
    all_ok &= report(
        "undamped time-average -> f*",
        ok,
        f"steps={steps}, max|<f>-f*|={avg_gap:.2e} (Cesaro O(1/N))",
    )
    return all_ok


def part_b_modal_closed_form() -> bool:
    """Exact per-mode solution from rest matches the simulation to machine eps."""
    print("\n(B') EXACT MODAL CLOSED FORM (undamped frozen source from rest)")
    nint = 15
    mat = interior_dirichlet_laplacian(nint)
    n = nint * nint
    src = np.zeros(n)
    src[n // 2] = 1.0
    fstar = np.linalg.solve(mat, -src)

    mu, vecs = np.linalg.eigh(mat)  # L = V diag(mu) V^T, mu<0
    s = vecs.T @ src
    xstar = -s / mu  # modal fixed point; V @ xstar == f*

    costh = 1.0 + H2 * mu / 2.0  # 2 cos theta = 2 + h2 mu
    stable = bool(np.all(costh > -1.0) and np.all(costh < 1.0))
    costh_c = np.clip(costh, -1.0 + 1e-15, 1.0 - 1e-15)
    theta = np.arccos(costh_c)

    def x_closed(steps: int) -> np.ndarray:
        # From rest (two zero levels x_0=x_1=0):
        # x_n = x*[1 - cos(theta n) - tan(theta/2) sin(theta n)]
        return xstar * (1.0 - np.cos(theta * steps) - np.tan(theta / 2.0) * np.sin(theta * steps))

    # Simulate exactly as the harness seeds it: f_prev=f_curr=0 (levels 0,1).
    fprev = np.zeros(n)
    fcurr = np.zeros(n)
    snaps = [fprev.copy(), fcurr.copy()]
    for _ in range(2, 1500):
        fnext = 2 * fcurr - fprev + H2 * (mat @ fcurr + src)
        fprev, fcurr = fcurr, fnext
        snaps.append(fcurr.copy())

    worst = 0.0
    for nstep in (2, 3, 8, 51, 138, 1000):
        cl = vecs @ x_closed(nstep)
        worst = max(worst, float(np.max(np.abs(cl - snaps[nstep]))))
    ok = stable and worst < 1e-10
    return report(
        "closed form vs simulation",
        ok,
        f"CFL-stable(|2cos|<2)={stable}, max|closed-sim|={worst:.2e} over sampled t; "
        f"per mode x_n=x*[1-cos(th n)-tan(th/2)sin(th n)], 2cos th=2+h2 mu",
    )


def part_c_undamped_snapshot_not_fstar() -> bool:
    """Negative control: the tested undamped finite-time snapshots are not f*."""
    print("\n(C) NEGATIVE CONTROL: tested undamped finite-time snapshots are NOT f*")
    all_ok = True

    # (C1) Generic frozen source stress case: minimum over the tested late
    #      snapshots is bounded away from zero.
    nint = 15
    mat = interior_dirichlet_laplacian(nint)
    n = nint * nint
    src = np.zeros(n)
    src[n // 2] = 1.0
    fstar = np.linalg.solve(mat, -src)
    fprev = np.zeros(n)
    fcurr = np.zeros(n)
    gaps = []
    for _ in range(2, 6000):
        fnext = 2 * fcurr - fprev + H2 * (mat @ fcurr + src)
        fprev, fcurr = fcurr, fnext
        gaps.append(float(np.max(np.abs(fcurr - fstar))))
    min_gap = min(gaps)
    fstar_scale = float(np.max(np.abs(fstar)))
    ok = min_gap > 0.01 * fstar_scale  # never gets within 1% of f*
    all_ok &= report(
        "min over t of max|snap-f*| (generic frozen source)",
        ok,
        f"min_gap={min_gap:.4f} = {min_gap / fstar_scale:.1%} of |f*|; "
        f"transient-contaminated over tested window",
    )

    # (C2) EXACT harness parameters: the comparator built by
    #      wave_retarded_gravity._make_instantaneous uses the LAST undamped
    #      snapshot full[NL-1] of a frozen solve switched on at NL//3.
    #      Quantify how far that is from the true Poisson field f*.
    nl = 30
    src_on = nl // 3
    hw = int(8 / H)
    nw = 2 * hw + 1

    def lap_yz(f: np.ndarray) -> np.ndarray:
        out = np.zeros_like(f)
        out[1:-1, 1:-1] = (
            f[:-2, 1:-1] + f[2:, 1:-1] + f[1:-1, :-2] + f[1:-1, 2:] - 4.0 * f[1:-1, 1:-1]
        )
        return out

    sy = nw // 2
    sz = 6 + nw // 2  # iz_start = 6 in the harness
    strength = 0.004
    fprev = np.zeros((nw, nw))
    fcurr = np.zeros((nw, nw))
    last = fcurr.copy()
    for t in range(2, nl):
        lp = lap_yz(fcurr)
        s2 = np.zeros((nw, nw))
        if t >= src_on:
            s2[sy, sz] = strength
        fnext = 2 * fcurr - fprev + H2 * (lp + s2)
        fprev, fcurr = fcurr, fnext
        last = fcurr.copy()
    snapshot = last  # == history[NL-1], the harness "instantaneous" comparator

    # True c=inf field for this source: interior Poisson solve.
    nint2 = nw - 2
    big = interior_dirichlet_laplacian(nint2)
    rhs = np.zeros(nint2 * nint2)
    rhs[(sy - 1) * nint2 + (sz - 1)] = -strength  # L f = -src
    sol = np.linalg.solve(big, rhs)
    fstar_grid = np.zeros((nw, nw))
    fstar_grid[1:-1, 1:-1] = sol.reshape(nint2, nint2)

    peak = float(np.max(np.abs(fstar_grid)))
    gap = float(np.max(np.abs(snapshot - fstar_grid)))
    rel = gap / max(peak, 1e-30)
    # Slowest-mode ring period vs available active steps.
    mu_all = np.linalg.eigvalsh(big)
    mu_slow = mu_all[np.argmin(-mu_all)]
    costh = 1.0 + H2 * mu_slow / 2.0
    period = 2.0 * np.pi / np.arccos(np.clip(costh, -1.0, 1.0))
    active_steps = (nl - 1) - src_on
    # Assert the comparator is meaningfully WRONG (proves the point):
    ok = rel > 0.05 and period > active_steps
    all_ok &= report(
        "harness full[NL-1] comparator vs true Poisson f*",
        ok,
        f"rel gap={rel:.1%} (peak |f*|={peak:.2e}); slowest ring period "
        f"={period:.0f} steps >> {active_steps} active steps => UNSETTLED. "
        f"Harness 'instantaneous' field is transient-contaminated, NOT f*.",
    )
    return all_ok


def main() -> None:
    print("=" * 72)
    print("WAVE-POISSON c=infinity BRIDGE THEOREM CERTIFIER")
    print(f"operator: f_next = 2 f_curr - f_prev + h2 (lap[f_curr] + src), "
          f"H={H}, h2={H2}")
    print("=" * 72)

    ok_a = part_a_fixed_point_uniqueness()
    ok_b = part_b_cinf_identification()
    ok_bp = part_b_modal_closed_form()
    ok_c = part_c_undamped_snapshot_not_fstar()

    print("\n" + "=" * 72)
    print("SUMMARY")
    print(f"  (A) fixed-point uniqueness (L neg-def, f* unique) : {'PASS' if ok_a else 'FAIL'}")
    print(f"  (B) c->inf static identification (f* c-independent): {'PASS' if ok_b else 'FAIL'}")
    print(f"  (B') exact modal closed form                      : {'PASS' if ok_bp else 'FAIL'}")
    print(f"  (C) tested undamped snapshots != f* (neg control): {'PASS' if ok_c else 'FAIL'}")
    verdict = ok_a and ok_b and ok_bp and ok_c
    print(f"\n  THEOREM CERTIFIED: {'YES' if verdict else 'NO'}")
    print("  -> discrete Poisson solve f* IS the exact c=infinity instantaneous")
    print("     field (fixed-point + static senses); the harness finite-time")
    print("     undamped frozen-source snapshot is NOT f* and is an incorrect")
    print("     comparator.")
    print("=" * 72)

    if not verdict:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
