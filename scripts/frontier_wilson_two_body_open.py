#!/usr/bin/env python3
"""
Open-boundary Wilson two-body mutual-channel probe.

Goal:
  remove periodic-image contamination from frontier_wilson_two_body.py
  and test whether the clean G=5 mutual-attraction window survives on a
  larger open 3D Wilson lattice.

Protocol:
  - two separate orbitals
  - SHARED, SELF_ONLY, FREE, FROZEN controls
  - early mutual acceleration from separation(t)
  - symmetric placement around the lattice center to suppress boundary drift
"""

from __future__ import annotations

import time

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import expm_multiply, spsolve


MASS = 0.30
WILSON_R = 1.0
DT = 0.08
REG = 1e-3
N_STEPS = 20
SIGMA = 1.0


class OpenWilsonLattice:
    def __init__(self, side: int):
        self.side = side
        self.n = side**3
        self.pos = np.zeros((self.n, 3))
        self.adj: dict[int, list[int]] = {}
        for x in range(side):
            for y in range(side):
                for z in range(side):
                    i = self.site_index(x, y, z)
                    self.pos[i] = [x, y, z]
                    self.adj[i] = []
                    for dx, dy, dz in (
                        (1, 0, 0),
                        (-1, 0, 0),
                        (0, 1, 0),
                        (0, -1, 0),
                        (0, 0, 1),
                        (0, 0, -1),
                    ):
                        nx, ny, nz = x + dx, y + dy, z + dz
                        if 0 <= nx < side and 0 <= ny < side and 0 <= nz < side:
                            self.adj[i].append(self.site_index(nx, ny, nz))
        self.lap = self.build_laplacian()

    def site_index(self, x: int, y: int, z: int):
        return x * self.side**2 + y * self.side + z

    def gaussian_wavepacket(self, center, sigma=SIGMA):
        psi = np.zeros(self.n, dtype=complex)
        cx, cy, cz = center
        for i in range(self.n):
            x, y, z = self.pos[i]
            r2 = (x - cx) ** 2 + (y - cy) ** 2 + (z - cz) ** 2
            psi[i] = np.exp(-r2 / (2 * sigma**2))
        psi /= np.linalg.norm(psi)
        return psi

    def build_laplacian(self):
        rows, cols, vals = [], [], []
        for i in range(self.n):
            rows.append(i)
            cols.append(i)
            vals.append(-len(self.adj[i]))
            for j in self.adj[i]:
                rows.append(i)
                cols.append(j)
                vals.append(1.0)
        return sparse.csr_matrix((vals, (rows, cols)), shape=(self.n, self.n))

    def solve_poisson(self, rho, G, mu2):
        A = self.lap - mu2 * sparse.eye(self.n) - REG * sparse.eye(self.n)
        rhs = -4.0 * np.pi * G * rho
        return spsolve(A.tocsc(), rhs).real

    def build_wilson_hamiltonian(self, phi):
        rows, cols, vals = [], [], []
        for i in range(self.n):
            for j in self.adj[i]:
                if j <= i:
                    continue
                rows.append(i)
                cols.append(j)
                vals.append(-0.5j + 0.5 * WILSON_R)
                rows.append(j)
                cols.append(i)
                vals.append(+0.5j + 0.5 * WILSON_R)
            diag = MASS + phi[i] + 0.5 * WILSON_R * len(self.adj[i])
            rows.append(i)
            cols.append(i)
            vals.append(diag)
        return sparse.csr_matrix((vals, (rows, cols)), shape=(self.n, self.n))

    def center_of_mass_x(self, psi):
        rho = np.abs(psi) ** 2
        return float(np.sum(rho * self.pos[:, 0]) / max(np.sum(rho), 1e-30))

    def evolve_step(self, psi, H):
        return expm_multiply(-1j * DT * H, psi)

    def run_mode(
        self,
        mode,
        G_val,
        mu2_val,
        center_a,
        center_b,
        sigma=SIGMA,
        source_mass_a=1.0,
        source_mass_b=1.0,
    ):
        psi_a = self.gaussian_wavepacket(center_a, sigma)
        psi_b = self.gaussian_wavepacket(center_b, sigma)

        seps = np.zeros(N_STEPS + 1)
        seps[0] = self.center_of_mass_x(psi_b) - self.center_of_mass_x(psi_a)

        phi_frozen = None
        if mode == "FROZEN":
            rho_total = source_mass_a * np.abs(psi_a) ** 2 + source_mass_b * np.abs(psi_b) ** 2
            phi_frozen = self.solve_poisson(rho_total, G_val, mu2_val)

        for t in range(N_STEPS):
            if mode == "FREE":
                phi_a = np.zeros(self.n)
                phi_b = np.zeros(self.n)
            elif mode == "SHARED":
                rho_total = source_mass_a * np.abs(psi_a) ** 2 + source_mass_b * np.abs(psi_b) ** 2
                phi_shared = self.solve_poisson(rho_total, G_val, mu2_val)
                phi_a = phi_shared
                phi_b = phi_shared
            elif mode == "SELF_ONLY":
                phi_a = self.solve_poisson(source_mass_a * np.abs(psi_a) ** 2, G_val, mu2_val)
                phi_b = self.solve_poisson(source_mass_b * np.abs(psi_b) ** 2, G_val, mu2_val)
            else:
                phi_a = phi_frozen
                phi_b = phi_frozen

            H_a = self.build_wilson_hamiltonian(phi_a)
            H_b = self.build_wilson_hamiltonian(phi_b)
            psi_a = self.evolve_step(psi_a, H_a)
            psi_b = self.evolve_step(psi_b, H_b)
            psi_a /= np.linalg.norm(psi_a)
            psi_b /= np.linalg.norm(psi_b)
            seps[t + 1] = self.center_of_mass_x(psi_b) - self.center_of_mass_x(psi_a)

        return seps


def acceleration(sep):
    a = np.zeros(len(sep))
    a[1:-1] = (sep[2:] - 2 * sep[1:-1] + sep[:-2]) / DT**2
    a[0] = a[1]
    a[-1] = a[-2]
    return a


def run_config(side: int, G_val: float, mu2_val: float, d: int, source_mass_a: float = 1.0, source_mass_b: float = 1.0):
    lat = OpenWilsonLattice(side)
    center = side // 2
    x_a = center - d // 2
    x_b = center + (d - d // 2)
    center_a = (x_a, center, center)
    center_b = (x_b, center, center)

    seps = {}
    for mode in ("SHARED", "SELF_ONLY", "FREE", "FROZEN"):
        seps[mode] = lat.run_mode(
            mode,
            G_val,
            mu2_val,
            center_a,
            center_b,
            source_mass_a=source_mass_a,
            source_mass_b=source_mass_b,
        )

    a_mut = acceleration(seps["SHARED"]) - acceleration(seps["SELF_ONLY"])
    early = slice(2, min(11, N_STEPS + 1))
    mean = float(np.mean(a_mut[early]))
    std = float(np.std(a_mut[early]))
    snr = abs(mean) / (std + 1e-12)
    return {
        "side": side,
        "G": G_val,
        "mu2": mu2_val,
        "d": d,
        "source_mass_a": source_mass_a,
        "source_mass_b": source_mass_b,
        "a_mutual_early_mean": mean,
        "a_mutual_early_std": std,
        "snr": snr,
        "dsep_shared": float(seps["SHARED"][-1] - seps["SHARED"][0]),
        "dsep_self": float(seps["SELF_ONLY"][-1] - seps["SELF_ONLY"][0]),
        "dsep_free": float(seps["FREE"][-1] - seps["FREE"][0]),
    }


def label(mean, snr):
    signal = "ATTRACT" if mean < -1e-6 else ("REPEL" if mean > 1e-6 else "NULL")
    quality = "CLEAN" if snr > 2.0 else ("MARGINAL" if snr > 1.0 else "NOISY")
    return signal, quality


# --- PASS/FAIL infrastructure (pattern follows scripts/retardation_discriminator.py) ---
_PASS = 0
_FAIL = 0


def _check_close(label_str: str, got: float, expected: float, rel_tol: float) -> None:
    global _PASS, _FAIL
    denom = max(abs(expected), 1e-30)
    rel = abs(got - expected) / denom
    ok = rel <= rel_tol
    status = "PASS" if ok else "FAIL"
    if ok:
        _PASS += 1
    else:
        _FAIL += 1
    print(
        f"  [{status}] {label_str}: got={got:+.4f} expected={expected:+.4f} "
        f"rel_err={rel*100:.2f}% tol={rel_tol*100:.1f}%"
    )


def _check_sign(label_str: str, got: float, expected_sign: int) -> None:
    global _PASS, _FAIL
    if expected_sign > 0:
        ok = got > 0
    elif expected_sign < 0:
        ok = got < 0
    else:
        ok = got == 0
    status = "PASS" if ok else "FAIL"
    if ok:
        _PASS += 1
    else:
        _FAIL += 1
    print(f"  [{status}] {label_str}: got={got:+.6f} expected_sign={expected_sign:+d}")


def run_screening_mass_sweep():
    """Reproduce the source note's §"Screening-Mass Addendum" mu^2 sweep.

    For each mu^2 in the note's table, sweep d in {3,4,5,6} at side=13, G=5,
    fit log|a_mut| = alpha * log(d) + b, and assert alpha matches the
    note's quoted exponent within tolerance.

    Note's quoted values (from docs/WILSON_TWO_BODY_OPEN_NOTE_2026-04-11.md
    §"Screening-Mass Addendum"):
      mu^2=0.22  -> alpha = -3.315
      mu^2=0.05  -> alpha = -2.392
      mu^2=0.01  -> alpha = -1.992
      mu^2=0.005 -> alpha = -1.927
      mu^2=0.001 -> alpha = -1.871
    """
    print()
    print("=" * 88)
    print("SCREENING-MASS ADDENDUM: alpha(mu^2) sweep")
    print("=" * 88)
    print("Surface: side=13, G=5, d in {3,4,5,6}; fit log|a_mut| = alpha * log(d) + b")
    print()

    # (mu^2, expected_alpha) from source note's §"Screening-Mass Addendum" table
    expected = [
        (0.22,  -3.315),
        (0.05,  -2.392),
        (0.01,  -1.992),
        (0.005, -1.927),
        (0.001, -1.871),
    ]
    d_list = [3, 4, 5, 6]

    # Tolerances. The note quotes 3-decimal-place alphas; our reproduction
    # matched all five within < 1% (max 0.9% at mu2=0.001). We assert 2.5%
    # to give Monte Carlo / sparse-solve noise a bit of headroom while still
    # catching any genuine drift in the runner's surface parameters.
    rel_tol_alpha = 0.025

    results = []
    for mu2, exp_alpha in expected:
        t0 = time.time()
        ds = []
        a_vals = []
        per_d_means = []
        for d in d_list:
            row = run_config(side=13, G_val=5, mu2_val=mu2, d=d)
            mean = row["a_mutual_early_mean"]
            per_d_means.append((d, mean))
            if mean < -1e-9:
                ds.append(d)
                a_vals.append(abs(mean))

        if len(ds) < 2:
            print(
                f"mu2={mu2:g}: insufficient ATTRACT points "
                f"({len(ds)}/{len(d_list)}); cannot fit alpha"
            )
            results.append((mu2, exp_alpha, None, per_d_means, time.time() - t0))
            global _FAIL
            _FAIL += 1
            print(f"  [FAIL] mu2={mu2:g} alpha-fit: < 2 attract points to fit")
            continue

        log_d = np.log(np.array(ds, dtype=float))
        log_a = np.log(np.array(a_vals, dtype=float))
        alpha, intercept = np.polyfit(log_d, log_a, 1)
        elapsed = time.time() - t0

        # per-d summary line
        means_str = " ".join(f"d={d}:{m:+.4f}" for d, m in per_d_means)
        print(f"mu2={mu2:<6g} [{elapsed:4.1f}s] {means_str}")
        # alpha check: each alpha sign-check + closeness-to-quoted-value
        _check_sign(f"mu2={mu2:g} alpha < 0 (attract softens with d)", alpha, -1)
        _check_close(f"mu2={mu2:g} alpha vs note", float(alpha), exp_alpha, rel_tol_alpha)
        results.append((mu2, exp_alpha, float(alpha), per_d_means, elapsed))

    # Trend check: alpha should soften (move toward 0 / -2) as mu^2 decreases.
    # The note's claim is "the steep exponent is screening-controlled and
    # softens toward Newton-compatible scaling as mu^2 is reduced."
    valid = [(mu2, a) for mu2, _, a, _, _ in results if a is not None]
    if len(valid) >= 2:
        # sorted descending in mu^2 => alpha should be monotonically increasing
        # (less negative) as mu^2 decreases
        valid_sorted = sorted(valid, key=lambda x: -x[0])
        alphas_sorted = [a for _, a in valid_sorted]
        # monotonic non-decreasing within numerical noise
        monotone = all(
            alphas_sorted[i + 1] >= alphas_sorted[i] - 1e-3
            for i in range(len(alphas_sorted) - 1)
        )
        global _PASS
        if monotone:
            _PASS += 1
            print(
                f"  [PASS] alpha softens monotonically as mu^2 decreases: "
                f"{[round(a, 3) for a in alphas_sorted]}"
            )
        else:
            _FAIL += 1
            print(
                f"  [FAIL] alpha NOT monotone as mu^2 decreases: "
                f"{[round(a, 3) for a in alphas_sorted]}"
            )

    return results


def main():
    print("=" * 88)
    print("OPEN-BOUNDARY WILSON TWO-BODY TEST")
    print("=" * 88)
    print(f"MASS={MASS}, WILSON_R={WILSON_R}, DT={DT}, REG={REG}, N_STEPS={N_STEPS}")
    print("Test surface: side in {11,13}, G=5, mu2=0.22, d in {3,4,5,6}")
    print()

    rows = []
    for side in (11, 13):
        for d in (3, 4, 5, 6):
            t0 = time.time()
            row = run_config(side, 5, 0.22, d)
            elapsed = time.time() - t0
            signal, quality = label(row["a_mutual_early_mean"], row["snr"])
            rows.append(row)
            print(
                f"side={side:2d} d={d}: "
                f"a_mut={row['a_mutual_early_mean']:+.6f} +/- {row['a_mutual_early_std']:.6f} "
                f"(SNR={row['snr']:.2f}) [{signal}] [{quality}] "
                f"dsep SH={row['dsep_shared']:+.4f} SELF={row['dsep_self']:+.4f} FREE={row['dsep_free']:+.4f} "
                f"({elapsed:.1f}s)"
            )

    print("\nSummary")
    print("-" * 88)
    clean = [r for r in rows if r["snr"] > 2.0]
    attract = [r for r in rows if r["a_mutual_early_mean"] < -1e-6]
    print(f"configs={len(rows)} attract={len(attract)}/{len(rows)} clean={len(clean)}/{len(rows)}")

    # Screening-mass addendum sweep (covers the source note's §"Screening-Mass Addendum").
    run_screening_mass_sweep()

    # Final PASS/FAIL summary
    print()
    print("=" * 88)
    print(f"WILSON TWO-BODY OPEN: PASS={_PASS}  FAIL={_FAIL}")
    print("=" * 88)
    return 0 if _FAIL == 0 else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
