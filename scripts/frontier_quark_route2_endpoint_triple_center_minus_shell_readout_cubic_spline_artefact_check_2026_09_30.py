#!/usr/bin/env python3
"""Route-2 endpoint triple: the centre-minus-shell readout is a global cubic-spline artefact.

Verifier for
`QUARK_ROUTE2_ENDPOINT_TRIPLE_CENTER_MINUS_SHELL_READOUT_IS_A_GLOBAL_CUBIC_SPLINE_ARTEFACT_ON_A_ONE_SITE_SPIKE_BOUNDED_THEOREM_NOTE_2026-09-30.md`.

Claim checked (narrow):

* the lattice potentials of the centre source `e0` and of the shell source
  `s_unit = (1/6) sum_arms e_arm` differ at exactly one site (the origin) and
  by exactly `1/6`, in every Dirichlet box and for every added perturbation
  direction (an exact identity, checked here with an independent solver);
* the repo's Route-2 tensor readout sees the lattice potential only through
  `tcomp.interpolated_phi`, a GLOBAL cubic spline (`map_coordinates(order=3)`),
  whose interpolant of a one-site spike rings with ratio `sqrt(3) - 2` per
  lattice step;
* with the spline, the unmodified runner reproduces the size-15 values
  `(beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E) ~ (-1, -2, 21/4)`;
* with a LOCAL interpolant whose stencil does not touch the origin, the same
  functional on the same fields gives `q_T = q_E = 1`, `rho_E = 0` at every
  size, including size 15 and sizes up to 81.

It does not derive any readout law and does not touch any audit row.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

sys.dont_write_bytecode = True

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    "docs/QUARK_ROUTE2_ENDPOINT_TRIPLE_CENTER_MINUS_SHELL_READOUT_IS_A_GLOBAL_CUBIC_SPLINE_ARTEFACT_ON_A_ONE_SITE_SPIKE_BOUNDED_THEOREM_NOTE_2026-09-30.md",
    "scripts/frontier_quark_route2_honest_gravity_metric_rhoe_characterization.py",
    "scripts/frontier_tensorial_einstein_regge_completion.py",
    "scripts/frontier_same_source_metric_ansatz_scan.py",
    "scripts/frontier_one_parameter_reduced_shell_law_self_contained_replay_2026_06_17.py",
    "scripts/frontier_quark_endpoint_readout_constraints.py",
)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import numpy as np  # noqa: E402
from scipy.fft import dstn, idstn  # noqa: E402
from scipy.ndimage import map_coordinates  # noqa: E402

import frontier_quark_route2_honest_gravity_metric_rhoe_characterization as rh  # noqa: E402
import frontier_same_source_metric_ansatz_scan as same  # noqa: E402

tcomp = rh.tcomp

NOTE = ROOT / AUDIT_INPUT_PATHS[0]

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    line = f"[{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def below(x: float) -> str:
    """Decade bound for a noise-level number, so the printed transcript does not depend on rounding noise."""
    return "<1e%d" % math.ceil(math.log10(max(abs(x), 1.0e-300)))


def rnd(x: float, digits: int = 4) -> float:
    """Round and remove negative zero for stable printing."""
    return round(float(x), digits) + 0.0


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


# ----------------------------------------------------------------------------
# Independent Dirichlet solver (DST-I), no repo linear algebra.
# ----------------------------------------------------------------------------
_LAM: dict[int, np.ndarray] = {}


def _lam(n: int) -> np.ndarray:
    if n not in _LAM:
        k = np.arange(1, n + 1)
        l1 = 2.0 * (1.0 - np.cos(np.pi * k / (n + 1)))
        _LAM[n] = l1[:, None, None] + l1[None, :, None] + l1[None, None, :]
    return _LAM[n]


def dst_solve(f: np.ndarray) -> np.ndarray:
    """Solve -Lap u = f on the interior cube with zero Dirichlet values outside."""
    return idstn(dstn(f, type=1) / _lam(f.shape[0]), type=1)


def neg_lap(u: np.ndarray) -> np.ndarray:
    up = np.pad(u, 1)
    return (
        6.0 * u
        - up[2:, 1:-1, 1:-1] - up[:-2, 1:-1, 1:-1]
        - up[1:-1, 2:, 1:-1] - up[1:-1, :-2, 1:-1]
        - up[1:-1, 1:-1, 2:] - up[1:-1, 1:-1, :-2]
    )


def own_sources(n_int: int) -> tuple[np.ndarray, np.ndarray]:
    c = n_int // 2
    e0 = np.zeros((n_int, n_int, n_int))
    e0[c, c, c] = 1.0
    s = np.zeros((n_int, n_int, n_int))
    for axis in range(3):
        for sign in (1, -1):
            idx = [c, c, c]
            idx[axis] += sign
            s[tuple(idx)] = 1.0 / 6.0
    return e0, s


def build_size_system_dst(size: int) -> "rh.SizeSystem":
    """Drop-in for rh.build_size_system using the DST solver (same object, fast at large size)."""
    interior = size - 2
    center = interior // 2
    support = [
        same.flat_idx(center + v[0], center + v[1], center + v[2], interior)
        for v in same.SUPPORT_COORDS
    ]
    cols = []
    for site in support:
        f = np.zeros(interior ** 3)
        f[site] = 1.0
        cols.append(dst_solve(f.reshape(interior, interior, interior)).reshape(-1))
    g0p = np.column_stack(cols)
    return rh.SizeSystem(size=size, interior=interior, support=support, g0p=g0p, gs=g0p[support, :])


def solve_from_source_dst(source_grid: np.ndarray) -> np.ndarray:
    """Drop-in for the shell-replay Dirichlet solve (same operator, DST instead of SuperLU)."""
    out = np.zeros_like(source_grid)
    out[1:-1, 1:-1, 1:-1] = dst_solve(source_grid[1:-1, 1:-1, 1:-1])
    return out


# ----------------------------------------------------------------------------
# Local (compact-stencil) Lagrange interpolant with an origin-touch counter.
# ----------------------------------------------------------------------------
class LocalLagrange:
    def __init__(self, npts: int) -> None:
        self.npts = npts
        self.lo = npts // 2 - 1   # 4 points: one below floor; 6 points: two below floor
        self.calls = 0
        self.touch_origin = 0
        self.pad = 4
        self._src = None      # the grid last padded (padding is redone only when the grid object changes)
        self._padded = None

    def weights(self, t: float) -> np.ndarray:
        nodes = np.arange(self.npts, dtype=float)
        w = np.ones(self.npts)
        for i in range(self.npts):
            for j in range(self.npts):
                if i != j:
                    w[i] *= (t - nodes[j]) / (nodes[i] - nodes[j])
        return w

    def __call__(self, phi_grid: np.ndarray, xyz: np.ndarray) -> float:
        # Outside the box the Dirichlet potential is 0 (equal to mode="nearest" at the wall).
        if self._src is not phi_grid:
            self._src = phi_grid
            self._padded = np.pad(phi_grid, self.pad)
        grid = self._padded
        c = (phi_grid.shape[0] - 1) // 2 + self.pad
        idx, ws = [], []
        for a in range(3):
            u = c + float(xyz[a])
            base = math.floor(u) - self.lo
            idx.append(np.arange(base, base + self.npts))
            ws.append(self.weights(u - base))
        self.calls += 1
        if all(c in idx[a] for a in range(3)):
            self.touch_origin += 1
        sub = grid[np.ix_(idx[0], idx[1], idx[2])]
        return float(np.einsum("i,j,k,ijk->", ws[0], ws[1], ws[2], sub))


def row_values(size: int) -> dict:
    rh.ETA_CACHE.clear()
    rh.ANCHOR_CACHE.clear()
    r = rh.compute_row(size)
    return {
        "N": size,
        "qT": r.q_t,
        "qE": r.q_e,
        "rhoE": r.rho_e,
        "sTE": r.gamma_t_shell / r.gamma_e_shell,
        "gTc": r.gamma_t_center,
        "gTs": r.gamma_t_shell,
        "gEc": r.gamma_e_center,
        "gEs": r.gamma_e_shell,
    }


def fmt(d: dict) -> str:
    return (
        f"N={d['N']:3d} q_T={rnd(d['qT'], 6):+.6f} q_E={rnd(d['qE'], 6):+.6f} rho_E={rnd(d['rhoE'], 4):+.4f} "
        f"alpha_T/alpha_E={rnd(d['sTE'], 4):+.4f}"
    )


def main() -> int:
    print("Route-2 endpoint triple: centre-minus-shell readout versus interpolation")

    # ------------------------------------------------------------------ PART 1
    section("PART 1: exact identity phi(e0) - phi(s_unit) = delta_origin / 6 (independent DST solver)")
    original_build = rh.build_size_system
    original_interp = tcomp.interpolated_phi
    for size in (15, 21, 41):
        n_int = size - 2
        c = n_int // 2
        e0, s = own_sources(n_int)
        pe, ps = dst_solve(e0), dst_solve(s)
        resid = float(np.max(np.abs(neg_lap(pe) - e0)))
        d = pe - ps
        origin = float(d[c, c, c])
        d[c, c, c] = 0.0
        off = float(np.max(np.abs(d)))
        print(f"  N={size:3d}: max|phi_e0 - phi_s| off origin {below(off)}; difference at origin = {origin:.12f}")
        check(f"N={size}: DST solve satisfies the lattice equation", resid < 1.0e-12, f"residual {below(resid)}")
        check(
            f"N={size}: potentials of e0 and s_unit are identical at every site except the origin",
            off < 1.0e-14,
            f"max off-origin difference {below(off)}",
        )
        check(f"N={size}: the origin difference is exactly 1/6", abs(origin - 1.0 / 6.0) < 1.0e-14, f"diff={origin:.12f}")

    # Tie the independent objects to the repo's own source vectors and Green columns (size 15).
    sysm = original_build(15)
    sysd = build_size_system_dst(15)
    g_gap = float(np.max(np.abs(sysm.g0p - sysd.g0p)))
    e0_own, s_own = own_sources(13)
    pe_repo = rh.phi_from_q(sysm, rh.E0)[1:-1, 1:-1, 1:-1]
    ps_repo = rh.phi_from_q(sysm, rh.S_UNIT)[1:-1, 1:-1, 1:-1]
    gap_e = float(np.max(np.abs(pe_repo - dst_solve(e0_own))))
    gap_s = float(np.max(np.abs(ps_repo - dst_solve(s_own))))
    check("repo Green columns (SuperLU) equal the independent DST columns at N=15", g_gap < 1.0e-10, f"max gap {below(g_gap)}")
    check(
        "repo sources E0 and S_UNIT are the centre delta and the mean of the six arms",
        gap_e < 1.0e-10 and gap_s < 1.0e-10,
        f"gaps {below(gap_e)}, {below(gap_s)}",
    )

    # The identity survives every perturbation direction, so it covers the finite-difference stencil in q.
    worst = 0.0
    for direction in (rh.EX, rh.TX, rh.TY, rh.TZ, rh.E1, rh.E2):
        for t in (rh.EPS, -rh.EPS):
            diff = rh.phi_from_q(sysm, rh.E0 + t * direction) - rh.phi_from_q(sysm, rh.S_UNIT + t * direction)
            cc = 7
            spike_only = diff.copy()
            spike_only[cc, cc, cc] -= 1.0 / 6.0
            worst = max(worst, float(np.max(np.abs(spike_only))))
    check(
        "phi(E0 + t d) - phi(S_UNIT + t d) is the same one-site spike for every readout direction d and t = +-EPS",
        worst < 1.0e-14,
        f"max deviation from delta_origin/6 {below(worst)}",
    )

    ae, as_ = rh.anchor(sysm, rh.E0), rh.anchor(sysm, rh.S_UNIT)
    check(
        "the reduced-shell anchor is identical for the centre and shell sources",
        abs(ae - as_) < 1.0e-12 * abs(ae),
        f"anchor(E0)={ae:.10e} anchor(S)={as_:.10e}",
    )

    # ------------------------------------------------------------------ PART 2
    section("PART 2: unmodified repo readout (global cubic spline, original max-abs floor)")
    spline_rows = {}
    for size in (13, 15, 17):
        spline_rows[size] = row_values(size)
        print("  SPLINE " + fmt(spline_rows[size]))
    r15 = spline_rows[15]
    beta_t = 6.0 * (r15["qT"] - 1.0)
    beta_e = 6.0 * (r15["qE"] - 1.0)
    print(f"  size-15 triple with the spline: ({beta_t:+.6f}, {r15['sTE']:+.6f}, {beta_e:+.6f})")
    check(
        "spline replay at N=15 gives the quoted triple (-1, -2, 21/4) to the quoted accuracy",
        abs(beta_t + 1.0) < 1.0e-3 and abs(r15["sTE"] + 2.0) < 1.0e-2 and abs(beta_e - 21.0 / 4.0) < 1.0e-2,
        f"beta_T/alpha_T={beta_t:+.6f}, alpha_T/alpha_E={r15['sTE']:+.6f}, beta_E/alpha_E={beta_e:+.6f}",
    )
    check(
        "the spline values are not a plateau: N=13 and N=17 are far from the triple",
        abs(spline_rows[13]["rhoE"] - 21.0 / 4.0) > 5.0 and abs(spline_rows[17]["rhoE"] - 21.0 / 4.0) > 5.0,
        f"rho_E(13)={spline_rows[13]['rhoE']:+.3f}, rho_E(17)={spline_rows[17]['rhoE']:+.3f}",
    )

    # ------------------------------------------------------------------ PART 3
    section("PART 3: what the global cubic spline does to a one-site spike")
    z = math.sqrt(3.0) - 2.0

    def b3(t: float) -> float:
        t = abs(t)
        if t < 1.0:
            return 2.0 / 3.0 - t * t + t ** 3 / 2.0
        if t < 2.0:
            return (2.0 - t) ** 3 / 6.0
        return 0.0

    def eta(x: float, kmax: int = 60) -> float:
        # cubic-spline interpolant of the lattice delta: B-spline coefficients sqrt(3) z^|k|
        return sum(math.sqrt(3.0) * z ** abs(k) * b3(x - k) for k in range(-kmax, kmax + 1))

    big = 41
    g = np.zeros((big, big, big))
    g[20, 20, 20] = 1.0
    worst_kernel = 0.0
    for x in (2.25, 3.25, 4.25, 5.25, 6.25):
        num = float(map_coordinates(g, np.array([[20 + x], [20.0], [20.0]]), order=3, mode="nearest")[0])
        worst_kernel = max(worst_kernel, abs(num - eta(x)))
    check(
        "scipy's 3-D spline of a lattice delta equals the analytic cardinal kernel sqrt(3) z^|k| B3 (z = sqrt(3) - 2)",
        worst_kernel < 1.0e-12,
        f"max gap on the axis {below(worst_kernel)}",
    )
    ratios = [eta(x + 1.0) / eta(x) for x in (2.25, 3.25, 4.25)]
    check(
        "successive lattice steps of the ringing alternate in sign with ratio z = -0.2679",
        all(abs(q - z) < 5.0e-3 for q in ratios),
        "ratios=" + ", ".join(f"{q:+.4f}" for q in ratios),
    )

    size = 15
    n_int = size - 2
    _, s_own = own_sources(n_int)
    phi_s = np.zeros((size, size, size))
    phi_s[1:-1, 1:-1, 1:-1] = dst_solve(s_own)
    spike = np.zeros((size, size, size))
    spike[7, 7, 7] = 1.0 / 6.0
    h = rh.RICCI_H

    def sp(grid: np.ndarray, x: float) -> float:
        return float(map_coordinates(grid, np.array([[7 + x], [7.0], [7.0]]), order=3, mode="nearest")[0])

    def d2(grid: np.ndarray, x: float) -> float:
        return (sp(grid, x + h) - 2.0 * sp(grid, x) + sp(grid, x - h)) / h ** 2

    x0 = rh.PROBE_RADIUS
    ring, field = d2(spike, x0), d2(phi_s, x0)
    print(f"  N=15, probe (4.25,0,0): d2 of spline(spike/6) = {ring:+.4e}; d2 of spline(phi_shell) = {field:+.4e}; ratio = {ring / field:+.3f}")
    check(
        "the spline's ringing curvature of the spike is opposite in sign and larger than the shell field's own curvature at the probe",
        ring < 0.0 < field and 1.0 < abs(ring / field) < 2.0,
        f"ring/field={ring / field:+.3f}",
    )

    # ------------------------------------------------------------------ PART 4
    section("PART 4: same functional, same fields, LOCAL interpolation (DST Green columns)")
    rh.build_size_system = build_size_system_dst
    original_solve = rh.shell_replay.solve_from_source
    rh.shell_replay.solve_from_source = solve_from_source_dst
    local4 = LocalLagrange(4)
    tcomp.interpolated_phi = local4
    rows4 = {}
    for size in (11, 13, 15, 17, 21, 41, 81):
        rows4[size] = row_values(size)
        print(f"  LOCAL4 {fmt(rows4[size])}")
    print(f"  4-point stencils containing the origin site: {local4.touch_origin} of {local4.calls}")
    check("no 4-point stencil of any probe evaluation contains the origin site", local4.touch_origin == 0, f"{local4.touch_origin}/{local4.calls}")
    dev_q = max(max(abs(d["qT"] - 1.0), abs(d["qE"] - 1.0)) for d in rows4.values())
    dev_rho = max(abs(d["rhoE"]) for d in rows4.values())
    check(
        "local interpolation: q_T = q_E = 1 at every size (11 to 81), including size 15",
        dev_q < 1.0e-5,
        f"max |q-1| {below(dev_q)}",
    )
    check(
        "local interpolation: beta_T/alpha_T = beta_E/alpha_E = 0 (rho_E = 0), not 21/4, at every size",
        dev_rho < 1.0e-3,
        f"max |rho_E| {below(dev_rho)}",
    )
    check(
        "same fields, same functional: spline rho_E(15) and local rho_E(15) differ by more than 5",
        abs(spline_rows[15]["rhoE"] - rows4[15]["rhoE"]) > 5.0,
        f"spline={rnd(spline_rows[15]['rhoE'], 4):+.4f}, local={rnd(rows4[15]['rhoE'], 4):+.4f}",
    )

    local6 = LocalLagrange(6)
    tcomp.interpolated_phi = local6
    rows6 = {}
    for size in (13, 15, 17, 19, 21):
        rows6[size] = row_values(size)
        print(f"  LOCAL6 {fmt(rows6[size])}")
    print(f"  6-point stencils containing the origin site: {local6.touch_origin} of {local6.calls} (diagonal probes only)")
    dev6_q = max(max(abs(d["qT"] - 1.0), abs(d["qE"] - 1.0)) for d in rows6.values())
    dev6_rho = max(abs(d["rhoE"]) for d in rows6.values())
    check(
        "a wider 6-point stencil that touches the origin only weakly still gives q close to 1 and |rho_E| far below 21/4",
        dev6_q < 0.02 and dev6_rho < 0.1,
        f"max |q-1| = {dev6_q:.3f}, max |rho_E| = {dev6_rho:.3f}",
    )

    rh.build_size_system = original_build
    rh.shell_replay.solve_from_source = original_solve
    tcomp.interpolated_phi = original_interp

    print("\n  alpha_T/alpha_E (shell only, not covered by the identity), information only:")
    print("    N   " + "  ".join(f"{n:>8d}" for n in (13, 15, 17)))
    print("    spline  " + "  ".join(f"{spline_rows[n]['sTE']:+8.3f}" for n in (13, 15, 17)))
    print("    local4  " + "  ".join(f"{rows4[n]['sTE']:+8.3f}" for n in (13, 15, 17)))
    print("    local6  " + "  ".join(f"{rows6[n]['sTE']:+8.3f}" for n in (13, 15, 17)))

    # ------------------------------------------------------------------ PART 5
    section("PART 5: note boundary")
    note_text = " ".join(NOTE.read_text(encoding="utf-8").split()) if NOTE.exists() else ""
    check(
        "the note exists and states the identity, the artefact reading and its scope limits",
        "delta_origin / 6" in note_text
        and "global cubic spline" in note_text
        and "does not derive" in note_text,
        "identity, mechanism and boundary phrases present",
    )

    total = PASS_COUNT + FAIL_COUNT
    print()
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT} TOTAL={total}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
