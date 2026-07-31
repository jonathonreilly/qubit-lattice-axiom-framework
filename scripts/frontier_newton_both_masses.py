#!/usr/bin/env python3
"""Finite centroid-proxy test for a supplied directed-hopping model.

The historical filename is not a physical identification.  This is a
dimensionless formal diagnostic with two declared coefficients:
  - open 3D cubic graph with one complex scalar amplitude per site
  - supplied operator shift (code value 0.001)
  - two separate orbitals at fixed separation
  - each orbital has its own declared coefficient M_A, M_B
  - the field source uses those coefficients as weights
  - the hopping matrices use them as spatially constant diagonal offsets
  - the declared observable is an early-time centroid-velocity proxy
      P_A^mut = M_A * (v_A^shared - v_A^self)
      P_B^mut = M_B * (v_B^self - v_B^shared)

What this can test:
  - whether the A proxy is linear in the partner coefficient M_B
  - whether the B proxy is linear in the partner coefficient M_A
  - whether the two formal signed proxies satisfy the declared comparator

Scope boundary:
  - no Wilson-Dirac, mass, gravity, momentum, force, or Newton interpretation
  - no continuum conservation theorem
  - no exclusion of alternate readouts or parameter surfaces
"""

from __future__ import annotations

# Heavy finite sweep: allow the cache/audit lane up to 30 minutes under
# concurrency contention.  The result remains a finite criterion report.
AUDIT_TIMEOUT_SEC = 1800

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve


# ── parameters ──────────────────────────────────────────────────────────
SIDE = 15
N = SIDE ** 3
HOPPING_R = 1.0
DT = 0.08
REG = 1e-6
N_STEPS = 18
SIGMA = 1.0
SOURCE_COUPLING = 5.0
OPERATOR_SHIFT = 0.001
SEPARATION = 5
COEFFICIENT_VALUES = [0.5, 1.0, 2.0, 3.0]
EARLY_START = 2
EARLY_END = 8


# ── lattice setup (open BC) ────────────────────────────────────────────
pos = np.zeros((N, 3))
adj: dict[int, list[int]] = {}

for x in range(SIDE):
    for y in range(SIDE):
        for z in range(SIDE):
            i = x * SIDE**2 + y * SIDE + z
            pos[i] = [x, y, z]
            adj[i] = []
            for dx, dy, dz in (
                (1, 0, 0),
                (-1, 0, 0),
                (0, 1, 0),
                (0, -1, 0),
                (0, 0, 1),
                (0, 0, -1),
            ):
                nx, ny, nz = x + dx, y + dy, z + dz
                if 0 <= nx < SIDE and 0 <= ny < SIDE and 0 <= nz < SIDE:
                    adj[i].append(nx * SIDE**2 + ny * SIDE + nz)


def build_laplacian():
    rows, cols, vals = [], [], []
    for i in range(N):
        rows.append(i)
        cols.append(i)
        vals.append(-len(adj[i]))
        for j in adj[i]:
            rows.append(i)
            cols.append(j)
            vals.append(1.0)
    return sparse.csr_matrix((vals, (rows, cols)), shape=(N, N))


LAP = build_laplacian()
FIELD_OP = (
    LAP - OPERATOR_SHIFT * sparse.eye(N) - REG * sparse.eye(N)
).tocsc()


def solve_poisson(rho):
    rhs = -4.0 * np.pi * SOURCE_COUPLING * rho
    return spsolve(FIELD_OP, rhs).real


def build_directed_hopping_hamiltonian(phi, diagonal_coefficient):
    rows, cols, vals = [], [], []
    for i in range(N):
        for j in adj[i]:
            if j <= i:
                continue
            rows.append(i)
            cols.append(j)
            vals.append(-0.5j + 0.5 * HOPPING_R)
            rows.append(j)
            cols.append(i)
            vals.append(+0.5j + 0.5 * HOPPING_R)
        diag = diagonal_coefficient + phi[i] + 0.5 * HOPPING_R * len(adj[i])
        rows.append(i)
        cols.append(i)
        vals.append(diag)
    return sparse.csc_matrix((vals, (rows, cols)), shape=(N, N))


def cn_step(psi, hamiltonian):
    half = 1j * hamiltonian * (DT / 2.0)
    eye = sparse.eye(N, format="csc")
    lhs = (eye + half).tocsc()
    rhs = (eye - half).dot(psi)
    psi_new = spsolve(lhs, rhs)
    psi_new /= np.linalg.norm(psi_new)
    return psi_new


def gaussian_wavepacket(center, sigma=SIGMA):
    psi = np.zeros(N, dtype=complex)
    cx, cy, cz = center
    for i in range(N):
        x, y, z = pos[i]
        r2 = (x - cx) ** 2 + (y - cy) ** 2 + (z - cz) ** 2
        psi[i] = np.exp(-r2 / (2 * sigma**2))
    psi /= np.linalg.norm(psi)
    return psi


def center_of_mass_x(psi):
    rho = np.abs(psi) ** 2
    return float(np.sum(rho * pos[:, 0]) / max(np.sum(rho), 1e-30))


def run_pair(mode, center_a, center_b, coefficient_a, coefficient_b):
    psi_a = gaussian_wavepacket(center_a)
    psi_b = gaussian_wavepacket(center_b)

    cx_a = np.zeros(N_STEPS + 1)
    cx_b = np.zeros(N_STEPS + 1)
    cx_a[0] = center_of_mass_x(psi_a)
    cx_b[0] = center_of_mass_x(psi_b)

    for t in range(N_STEPS):
        if mode == "SHARED":
            rho_total = (
                coefficient_a * np.abs(psi_a) ** 2
                + coefficient_b * np.abs(psi_b) ** 2
            )
            phi = solve_poisson(rho_total)
            h_a = build_directed_hopping_hamiltonian(phi, coefficient_a)
            h_b = build_directed_hopping_hamiltonian(phi, coefficient_b)
        elif mode == "SELF_ONLY":
            phi_a = solve_poisson(coefficient_a * np.abs(psi_a) ** 2)
            phi_b = solve_poisson(coefficient_b * np.abs(psi_b) ** 2)
            h_a = build_directed_hopping_hamiltonian(phi_a, coefficient_a)
            h_b = build_directed_hopping_hamiltonian(phi_b, coefficient_b)
        elif mode == "FREE":
            zeros = np.zeros(N)
            h_a = build_directed_hopping_hamiltonian(zeros, coefficient_a)
            h_b = build_directed_hopping_hamiltonian(zeros, coefficient_b)
        else:
            raise ValueError(f"Unknown mode: {mode}")

        psi_a = cn_step(psi_a, h_a)
        psi_b = cn_step(psi_b, h_b)
        cx_a[t + 1] = center_of_mass_x(psi_a)
        cx_b[t + 1] = center_of_mass_x(psi_b)

    return cx_a, cx_b


def velocity_array(cx):
    vel = np.zeros(len(cx))
    vel[1:] = (cx[1:] - cx[:-1]) / DT
    vel[0] = vel[1]
    return vel


def acceleration_array(cx):
    acc = np.zeros(len(cx))
    acc[1:-1] = (cx[2:] - 2 * cx[1:-1] + cx[:-2]) / DT**2
    acc[0] = acc[1]
    acc[-1] = acc[-2]
    return acc


def early_window(arr, start=EARLY_START, end=EARLY_END):
    return arr[start:min(end, len(arr))]


def mutual_metrics(cx_shared, cx_self, coefficient_weight, direction):
    v_shared = velocity_array(cx_shared)
    v_self = velocity_array(cx_self)
    a_shared = acceleration_array(cx_shared)
    a_self = acceleration_array(cx_self)

    dv = v_shared - v_self
    da = a_shared - a_self
    if direction == "left":
        dv = -dv
        da = -da

    proxy = coefficient_weight * float(np.mean(early_window(dv)))
    accel = float(np.mean(early_window(da)))
    return proxy, accel


def linear_fit(xs, ys):
    xs = np.asarray(xs, dtype=float)
    ys = np.asarray(ys, dtype=float)
    slope, intercept = np.polyfit(xs, ys, 1)
    fit = slope * xs + intercept
    ss_res = float(np.sum((ys - fit) ** 2))
    ss_tot = float(np.sum((ys - np.mean(ys)) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 1.0
    return slope, intercept, r2


def coefficient_of_variation(values):
    values = np.asarray(values, dtype=float)
    mean = float(np.mean(values))
    std = float(np.std(values))
    if abs(mean) < 1e-30:
        return float("inf"), mean, std
    return abs(std / mean), mean, std


def main(*, compact: bool = False):
    center = SIDE // 2
    x_a = center - SEPARATION // 2
    x_b = center + (SEPARATION - SEPARATION // 2)
    center_a = (x_a, center, center)
    center_b = (x_b, center, center)

    if compact:
        print("TWO-COEFFICIENT FINITE CENTROID-PROXY DIAGNOSTIC")
        print(
            f"dimensionless graph: side={SIDE} source_coupling={SOURCE_COUPLING:g} "
            f"operator_shift={OPERATOR_SHIFT:g} separation={SEPARATION} "
            f"coefficients={COEFFICIENT_VALUES} early_indices={EARLY_START}..{EARLY_END - 1}"
        )
        print(
            "proxy: P_A=M_A<dv_A>; P_B_in=M_B<-dv_B>; "
            "signed comparator=P_A-P_B_in"
        )
    else:
        print("=" * 92)
        print("ONE-COMPONENT DIRECTED-HOPPING TWO-COEFFICIENT PROXY TEST")
        print("=" * 92)
        print(f"Dimensionless graph: {SIDE}^3 = {N} sites, open boundary")
        print(f"Directed hopping: r={HOPPING_R}, DT={DT}, sigma={SIGMA}")
        print(
            f"Supplied field coefficients: source_coupling={SOURCE_COUPLING}, "
            f"operator_shift={OPERATOR_SHIFT}, REG={REG}"
        )
        print(f"Separation={SEPARATION}, positions A@x={x_a}, B@x={x_b}")
        print(f"Coefficient grid: {COEFFICIENT_VALUES}")
        print()
        print("Observable (a formal centroid proxy, not a momentum operator):")
        print("  P_A^mut = M_A * <v_A^shared - v_A^self>")
        print("  P_B^mut = M_B * <v_B^self - v_B^shared>   (same inward-positive sign)")
        print("  balance proxy uses signed values: P_A^mut - P_B^mut")
        print()

    results = {}
    header = (
        f"{'M_A':>5s} {'M_B':>5s} | "
        f"{'P_A^mut':>12s} {'P_B^mut':>12s} | "
        f"{'a_A':>10s} {'a_B':>10s} | "
        f"{'P_A-P_B_in':>11s} {'PA/MB':>10s} {'PB/MA':>10s}"
    )
    if not compact:
        print(header)
        print("-" * len(header))

    for coefficient_a in COEFFICIENT_VALUES:
        for coefficient_b in COEFFICIENT_VALUES:
            cx_a_sh, cx_b_sh = run_pair(
                "SHARED", center_a, center_b, coefficient_a, coefficient_b
            )
            cx_a_so, cx_b_so = run_pair(
                "SELF_ONLY", center_a, center_b, coefficient_a, coefficient_b
            )

            proxy_a, accel_a = mutual_metrics(
                cx_a_sh, cx_a_so, coefficient_a, direction="right"
            )
            proxy_b_inward, accel_b_inward = mutual_metrics(
                cx_b_sh, cx_b_so, coefficient_b, direction="left"
            )

            signed_proxy_b = -proxy_b_inward

            results[(coefficient_a, coefficient_b)] = {
                "proxy_a": proxy_a,
                "proxy_b_inward": proxy_b_inward,
                "signed_proxy_b": signed_proxy_b,
                "accel_a": accel_a,
                "accel_b_inward": accel_b_inward,
                "signed_comparator": proxy_a + signed_proxy_b,
                "p_a_per_mb": proxy_a / coefficient_b,
                "p_b_per_ma": proxy_b_inward / coefficient_a,
            }

            if not compact:
                print(
                    f"{coefficient_a:5.1f} {coefficient_b:5.1f} | "
                    f"{proxy_a:+12.6e} {proxy_b_inward:+12.6e} | "
                    f"{accel_a:+10.6e} {accel_b_inward:+10.6e} | "
                    f"{proxy_a + signed_proxy_b:+11.3e} "
                    f"{proxy_a / coefficient_b:+10.3e} "
                    f"{proxy_b_inward / coefficient_a:+10.3e}"
                )

    if not compact:
        print()
        print("=" * 92)
        print("ANCHOR SLICE 1: P_A^mut vs M_B  (M_A = 1.0)")
        print("=" * 92)
    mb_vals = []
    pa_vals = []
    for coefficient_b in COEFFICIENT_VALUES:
        value = results[(1.0, coefficient_b)]["proxy_a"]
        mb_vals.append(coefficient_b)
        pa_vals.append(value)
        if not compact:
            print(f"  M_B={coefficient_b:.1f}: P_A^mut = {value:+.6e}")
    slope_a, intercept_a, r2_a = linear_fit(mb_vals, pa_vals)
    print(f"  fit: P_A^mut = {slope_a:+.6e} * M_B + {intercept_a:+.6e}   R^2={r2_a:.6f}")

    if not compact:
        print()
        print("=" * 92)
        print("ANCHOR SLICE 2: P_B^mut vs M_A  (M_B = 1.0)")
        print("=" * 92)
    ma_vals = []
    pb_vals = []
    for coefficient_a in COEFFICIENT_VALUES:
        value = results[(coefficient_a, 1.0)]["proxy_b_inward"]
        ma_vals.append(coefficient_a)
        pb_vals.append(value)
        if not compact:
            print(f"  M_A={coefficient_a:.1f}: P_B^mut = {value:+.6e}")
    slope_b, intercept_b, r2_b = linear_fit(ma_vals, pb_vals)
    print(f"  fit: P_B^mut = {slope_b:+.6e} * M_A + {intercept_b:+.6e}   R^2={r2_b:.6f}")

    if not compact:
        print()
        print("=" * 92)
        print("FULL-GRID NORMALIZATION CHECKS")
        print("=" * 92)
    pa_norm = [results[key]["p_a_per_mb"] for key in results]
    pb_norm = [results[key]["p_b_per_ma"] for key in results]
    pa_cv, pa_mean, pa_std = coefficient_of_variation(pa_norm)
    pb_cv, pb_mean, pb_std = coefficient_of_variation(pb_norm)
    print(f"  P_A^mut / M_B: mean={pa_mean:+.6e}, std={pa_std:.6e}, CV={pa_cv:.3%}")
    print(f"  P_B^mut / M_A: mean={pb_mean:+.6e}, std={pb_std:.6e}, CV={pb_cv:.3%}")

    if not compact:
        print()
        print("=" * 92)
        print("SIGNED-BALANCE PROXY CHECK")
        print("=" * 92)
    signed_comparators = []
    rel_balance = []
    balance_counts = {"PASS": 0, "MARGINAL": 0, "NONPASS": 0}
    for coefficient_a in COEFFICIENT_VALUES:
        for coefficient_b in COEFFICIENT_VALUES:
            row = results[(coefficient_a, coefficient_b)]
            signed_comparators.append(row["signed_comparator"])
            denom = max(
                abs(row["proxy_a"]) + abs(row["proxy_b_inward"]), 1e-30
            )
            rel = abs(row["signed_comparator"]) / denom
            rel_balance.append(rel)
            status = "PASS" if rel < 0.10 else ("MARGINAL" if rel < 0.25 else "NONPASS")
            balance_counts[status] += 1
    rel_mean = float(np.mean(rel_balance))
    rel_max = float(np.max(rel_balance))
    print(
        "  row counts at the declared relative-imbalance thresholds: "
        f"PASS={balance_counts['PASS']} MARGINAL={balance_counts['MARGINAL']} "
        f"NONPASS={balance_counts['NONPASS']}"
    )
    print(f"  mean relative imbalance = {rel_mean:.3%}")
    print(f"  max  relative imbalance = {rel_max:.3%}")

    if not compact:
        print()
        print("=" * 92)
        print("SUMMARY")
        print("=" * 92)
        print(f"1. Anchor slice P_A^mut vs M_B: R^2={r2_a:.6f}")
        print(f"2. Anchor slice P_B^mut vs M_A: R^2={r2_b:.6f}")
        print(f"3. Full-grid CV for P_A^mut/M_B: {pa_cv:.3%}")
        print(f"4. Full-grid CV for P_B^mut/M_A: {pb_cv:.3%}")
        print(f"5. Mean signed-balance-proxy imbalance: {rel_mean:.3%}")

    pass_anchor = r2_a > 0.95 and r2_b > 0.95
    pass_grid = pa_cv < 0.15 and pb_cv < 0.15
    pass_reaction = rel_mean < 0.10 and rel_max < 0.25

    print("\nDECLARED FINITE CENTROID-PROXY CRITERIA")
    print(f"  anchor linearity R^2>0.95 on both slices: {'PASS' if pass_anchor else 'NONPASS'}")
    print(f"  normalized-grid CV<15% on both channels: {'PASS' if pass_grid else 'NONPASS'}")
    print(f"  balance mean<10% and max<25%: {'PASS' if pass_reaction else 'NONPASS'}")
    print(
        "  diagnostic outcome: "
        + (
            "all declared criteria pass"
            if pass_anchor and pass_grid and pass_reaction
            else "this sampled centroid proxy does not satisfy the full comparator set"
        )
    )
    print(
        "  boundary: no physical interpretation, alternate observable, parameter "
        "surface, or universal no-go was tested"
    )

    certificate_checks = {
        "B1 complete 4x4 coefficient grid": len(results) == 16,
        "B2 both anchor fits are finite": np.isfinite(r2_a) and np.isfinite(r2_b),
        "B3 both normalization CVs are finite": np.isfinite(pa_cv) and np.isfinite(pb_cv),
        "B4 every displayed balance row was classified": sum(balance_counts.values()) == 16,
        "B5 displayed anchor R^2 values reproduce the source table": (
            round(r2_a, 6), round(r2_b, 6)
        )
        == (0.944530, 0.940033),
        "B6 displayed normalization CVs reproduce the source table": (
            round(100.0 * pa_cv, 3), round(100.0 * pb_cv, 3)
        )
        == (35.382, 37.501),
        "B7 displayed balance counts reproduce the source table": balance_counts
        == {"PASS": 0, "MARGINAL": 0, "NONPASS": 16},
        "B8 displayed balance mean/max reproduce the source table": (
            round(100.0 * rel_mean, 3), round(100.0 * rel_max, 3)
        )
        == (100.000, 100.000),
        "B9 reported nonpass is exactly the declared finite diagnostic": not (
            pass_anchor and pass_grid and pass_reaction
        ),
    }
    print("\nEXECUTABLE CERTIFICATE")
    for label, passed in certificate_checks.items():
        print(f"[{('PASS' if passed else 'FAIL')}] {label}")
    n_pass = sum(certificate_checks.values())
    n_fail = len(certificate_checks) - n_pass
    print(f"TOTAL: PASS={n_pass} FAIL={n_fail}")
    if n_fail:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
