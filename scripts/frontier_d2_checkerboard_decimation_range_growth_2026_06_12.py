#!/usr/bin/env python3
"""Class-A exact verification for the source note

    docs/D2_CHECKERBOARD_DECIMATION_STEP1_CLOSED_FORM_STEP2_RANGE_GROWTH_BOUNDED_THEOREM_NOTE_2026-06-12.md

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_d2_checkerboard_decimation_range_growth_2026_06_12.py
"""
import sys

import numpy as np


T = 0.6
MU = 2.75
E_SHIFT = 0.3
L_VALUES = (6, 8)

TOL_HOO = 1.0e-14
TOL_COEFF = 1.0e-12
TOL_RESOLVENT = 1.0e-10
SHELL_ZERO_TOL = 1.0e-12

PASS = 0
FAIL = 0


def check(name, condition, detail):
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS {name}: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {name}: {detail}")


def max_abs(values):
    arr = np.asarray(values)
    if arr.size == 0:
        return 0.0
    return float(np.max(np.abs(arr)))


def site_index(x, y, L):
    return (x % L) * L + (y % L)


def square_coords(L):
    return [(x, y) for x in range(L) for y in range(L)]


def square_hamiltonian(L, t, mu):
    n = L * L
    h = mu * np.eye(n, dtype=float)
    for x, y in square_coords(L):
        i = site_index(x, y, L)
        for dx, dy in ((1, 0), (0, 1)):
            j = site_index(x + dx, y + dy, L)
            h[i, j] = -t
            h[j, i] = -t
    return h


def checkerboard_indices(L):
    black = []
    white = []
    for x, y in square_coords(L):
        idx = site_index(x, y, L)
        if (x + y) % 2 == 0:
            black.append(idx)
        else:
            white.append(idx)
    return black, white


def coords_for_indices(indices, L):
    coords = square_coords(L)
    return [coords[i] for i in indices]


def schur_effective_hamiltonian(h, keep, elim, E=0.0):
    h_kk = h[np.ix_(keep, keep)]
    h_ke = h[np.ix_(keep, elim)]
    h_ek = h[np.ix_(elim, keep)]
    h_ee = h[np.ix_(elim, elim)]
    shifted_elim = h_ee - E * np.eye(len(elim), dtype=float)
    return h_kk - h_ke @ np.linalg.solve(shifted_elim, h_ek)


def periodic_delta(a, b, L):
    d = (b - a) % L
    if d > L // 2:
        d -= L
    return int(d)


def torus_d2(coord_a, coord_b, L):
    dx = periodic_delta(coord_a[0], coord_b[0], L)
    dy = periodic_delta(coord_a[1], coord_b[1], L)
    return dx * dx + dy * dy


def shell_entries(matrix, coords, L, d2):
    values = []
    n = len(coords)
    for i in range(n):
        for j in range(n):
            if i != j and torus_d2(coords[i], coords[j], L) == d2:
                values.append(matrix[i, j])
    return np.array(values, dtype=float)


def beyond_family_entries(matrix, coords, L, allowed_shells):
    values = []
    n = len(coords)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if torus_d2(coords[i], coords[j], L) not in allowed_shells:
                values.append(matrix[i, j])
    return np.array(values, dtype=float)


def path_count_matrix(h, keep, elim):
    incidence = (np.abs(h[np.ix_(keep, elim)]) > 0.0).astype(float)
    return incidence @ incidence.T


def offdiag_part(matrix):
    return matrix - np.diag(np.diag(matrix))


def clustered_magnitudes(values, tol=1.0e-11):
    mags = sorted(float(abs(v)) for v in values)
    clusters = []
    for mag in mags:
        if not clusters or abs(mag - clusters[-1][-1]) > tol:
            clusters.append([mag])
        else:
            clusters[-1].append(mag)
    return [float(max(cluster)) for cluster in clusters]


def nonzero_shell_table(matrix, coords, L, threshold):
    shells = {}
    n = len(coords)
    for i in range(n):
        for j in range(i + 1, n):
            value = matrix[i, j]
            if abs(value) <= threshold:
                continue
            d2 = torus_d2(coords[i], coords[j], L)
            shells.setdefault(d2, []).append(value)
    return {
        d2: {
            "count": len(values),
            "magnitudes": clustered_magnitudes(values),
            "max": float(max(abs(v) for v in values)),
        }
        for d2, values in sorted(shells.items())
    }


def format_magnitudes(magnitudes):
    return "[" + ", ".join(f"{mag:.16e}" for mag in magnitudes) + "]"


def print_shell_table(title, table):
    print(title)
    for d2, data in table.items():
        print(
            "  "
            f"d2={d2:2d} count={data['count']:3d} "
            f"magnitudes={format_magnitudes(data['magnitudes'])}"
        )


def format_new_shells(table, new_shells):
    return "; ".join(
        f"d2={d2} max={table[d2]['max']:.16e} mags={format_magnitudes(table[d2]['magnitudes'])}"
        for d2 in new_shells
    )


def run_y1a_y1b():
    for L in L_VALUES:
        h = square_hamiltonian(L, T, MU)
        black, white = checkerboard_indices(L)
        black_coords = coords_for_indices(black, L)

        h_oo = h[np.ix_(white, white)]
        h_oo_error = max_abs(h_oo - MU * np.eye(len(white), dtype=float))
        check(
            f"Y1a L={L} white-white block is exactly mu*I",
            h_oo_error < TOL_HOO,
            f"max|h_oo-mu*I|={h_oo_error:.3e}",
        )

        h_eff = schur_effective_hamiltonian(h, black, white, E=0.0)
        path_counts = path_count_matrix(h, black, white)
        expected_from_paths = MU * np.eye(len(black), dtype=float) - (T * T / MU) * path_counts
        path_formula_error = max_abs(h_eff - expected_from_paths)
        check(
            f"Y1b L={L} Schur output equals mu*I-(t^2/mu)*P",
            path_formula_error < TOL_COEFF,
            f"max path-formula error={path_formula_error:.3e}",
        )

        expected_diag = MU - 4.0 * T * T / MU
        diag_error = max_abs(np.diag(h_eff) - expected_diag)
        check(
            f"Y1b L={L} diag coefficient is mu-4*t^2/mu",
            diag_error < TOL_COEFF,
            f"measured={float(np.mean(np.diag(h_eff))):.16e} expected={expected_diag:.16e} err={diag_error:.3e}",
        )

        expected_rot_nn = 2.0 * T * T / MU
        rot_nn_amplitudes = -shell_entries(h_eff, black_coords, L, d2=2)
        rot_nn_error = max_abs(rot_nn_amplitudes - expected_rot_nn)
        check(
            f"Y1b L={L} rotated-NN coupling is 2*t^2/mu",
            rot_nn_error < TOL_COEFF,
            f"expected={expected_rot_nn:.16e} maxerr={rot_nn_error:.3e}",
        )

        expected_rot_nnn = T * T / MU
        rot_nnn_amplitudes = -shell_entries(h_eff, black_coords, L, d2=4)
        rot_nnn_error = max_abs(rot_nnn_amplitudes - expected_rot_nnn)
        check(
            f"Y1b L={L} rotated-NNN axial coupling is t^2/mu",
            rot_nnn_error < TOL_COEFF,
            f"expected={expected_rot_nnn:.16e} maxerr={rot_nnn_error:.3e}",
        )

        beyond_error = max_abs(beyond_family_entries(h_eff, black_coords, L, allowed_shells={2, 4}))
        check(
            f"Y1b L={L} no step-1 couplings beyond rotated-NNN",
            beyond_error < TOL_COEFF,
            f"max |off-family entry|={beyond_error:.3e} for d2 not in {{2,4}}",
        )


def run_y1c():
    L = 8
    h = square_hamiltonian(L, T, MU)
    black, white = checkerboard_indices(L)
    black_coords = coords_for_indices(black, L)
    h_step1 = schur_effective_hamiltonian(h, black, white, E=0.0)

    keep2 = []
    elim2 = []
    for i, (x, _y) in enumerate(black_coords):
        if x % 2 == 0:
            keep2.append(i)
        else:
            elim2.append(i)

    h_oo2 = h_step1[np.ix_(elim2, elim2)]
    internal_offdiag = max_abs(offdiag_part(h_oo2))
    check(
        "Y1c rotated eliminated block is NOT diagonal",
        internal_offdiag > TOL_COEFF,
        f"max internal offdiag={internal_offdiag:.16e}",
    )

    h_step2 = schur_effective_hamiltonian(h_step1, keep2, elim2, E=0.0)
    keep2_coords = [black_coords[i] for i in keep2]
    shell_table = nonzero_shell_table(h_step2, keep2_coords, L, SHELL_ZERO_TOL)
    print_shell_table("Y1c step-2 nonzero off-diagonal coupling shell table:", shell_table)

    closed_family_shells_after_step2 = {4, 8}
    new_shells = sorted(d2 for d2 in shell_table if d2 not in closed_family_shells_after_step2)
    measured_max_shell = max(shell_table) if shell_table else 0
    closed_family_max_shell = max(closed_family_shells_after_step2)
    range_growth = measured_max_shell > closed_family_max_shell and len(new_shells) > 0
    check(
        "Y1c range grows in THIS d=2 checkerboard convention: the two-coupling family does NOT close in the L=8 measured shell table",
        range_growth,
        (
            f"max shell d2={measured_max_shell}, closed-family max d2={closed_family_max_shell}; "
            f"new shells: {format_new_shells(shell_table, new_shells)}"
        ),
    )

    # Panel edits, corrected by the wraparound probes themselves: the L=8 shell
    # values are wraparound-contaminated (d2=16: 9.47e-3 at L=8 vs 4.73e-3
    # converged); the TRUE structure is a DENSE step-2 Hamiltonian with
    # exponentially decaying couplings. Reference = L=14; L=12 for convergence.
    def step2_table(L_big):
        h_b = square_hamiltonian(L_big, T, MU)
        black_b, white_b = checkerboard_indices(L_big)
        bc_b = coords_for_indices(black_b, L_big)
        h1_b = schur_effective_hamiltonian(h_b, black_b, white_b, E=0.0)
        keep_b, elim_b = [], []
        for idx, (x, _y) in enumerate(bc_b):
            (keep_b if x % 2 == 0 else elim_b).append(idx)
        h2_b = schur_effective_hamiltonian(h1_b, keep_b, elim_b, E=0.0)
        kc_b = [bc_b[idx] for idx in keep_b]
        return nonzero_shell_table(h2_b, kc_b, L_big, SHELL_ZERO_TOL)

    tab12 = step2_table(12)
    tab14 = step2_table(14)
    print("Y1c L=12 shells:", {d: f"{v['max']:.3e}" for d, v in sorted(tab12.items())})
    print("Y1c L=14 shells:", {d: f"{v['max']:.3e}" for d, v in sorted(tab14.items())})
    check(
        "Y1c the L=8 'd2<=32' table was wraparound-TRUNCATED: L=12/14 show shells "
        "beyond 32 (finite-box range growth; this runner does not prove an "
        "infinite-lattice all-shell theorem -- disclosed)",
        max(tab12) > 32 and max(tab14) > 32,
        f"max shells: L=12 -> {max(tab12)}, L=14 -> {max(tab14)}",
    )
    near = [16, 20, 32]
    near_conv = all(abs(tab12[d]["max"] - tab14[d]["max"]) / tab14[d]["max"] < 0.05
                    for d in near)
    check(
        "Y1c near-shell magnitudes CONVERGE in L (L=12 vs L=14 within 5% relative "
        "on d2=16/20/32) while the far tail remains L-limited (printed)",
        near_conv,
        "; ".join(f"d2={d}: {tab12[d]['max']:.3e} vs {tab14[d]['max']:.3e}" for d in near),
    )
    band1 = [tab14[d]["max"] for d in (16, 20)]
    band2 = [tab14[d]["max"] for d in (32, 36, 40)]
    band3 = [tab14[d]["max"] for d in (52,)]
    band4 = [tab14[d]["max"] for d in (72,)]
    decay_bands = (min(band1) > max(band2) > min(band2) > max(band3) > max(band4)
                   and max(band4) < 1e-5)
    check(
        "Y1c coupling magnitudes DECAY by distance band (L=14): {16,20} > "
        "{32,36,40} > {52} > {72} with the far tail < 1e-5 -- dense, decaying "
        "structure; within-band ordering is anisotropic (diagonal vs axial shells "
        "at similar d2, disclosed: the (32,36) pair is near-degenerate)",
        decay_bands,
        f"bands: {[f'{v:.2e}' for v in band1]} > {[f'{v:.2e}' for v in band2]} > "
        f"{[f'{v:.2e}' for v in band3]} > {[f'{v:.2e}' for v in band4]}",
    )

def run_y1d():
    for L in L_VALUES:
        h = square_hamiltonian(L, T, MU)
        black, white = checkerboard_indices(L)
        black_coords = coords_for_indices(black, L)
        h_eff = schur_effective_hamiltonian(h, black, white, E=E_SHIFT)
        shifted_eff = h_eff - E_SHIFT * np.eye(len(black), dtype=float)
        shifted_mu = MU - E_SHIFT

        expected_shifted_diag = shifted_mu - 4.0 * T * T / shifted_mu
        shifted_diag_error = max_abs(np.diag(shifted_eff) - expected_shifted_diag)
        check(
            f"Y1d L={L} shifted onsite coefficient uses mu-E",
            shifted_diag_error < TOL_COEFF,
            (
                f"measured={float(np.mean(np.diag(shifted_eff))):.16e} "
                f"expected={expected_shifted_diag:.16e} err={shifted_diag_error:.3e}"
            ),
        )

        expected_rot_nn = 2.0 * T * T / shifted_mu
        rot_nn_amplitudes = -shell_entries(h_eff, black_coords, L, d2=2)
        rot_nn_error = max_abs(rot_nn_amplitudes - expected_rot_nn)
        check(
            f"Y1d L={L} E-shifted rotated-NN coupling uses mu-E",
            rot_nn_error < TOL_COEFF,
            f"expected={expected_rot_nn:.16e} maxerr={rot_nn_error:.3e}",
        )

        expected_rot_nnn = T * T / shifted_mu
        rot_nnn_amplitudes = -shell_entries(h_eff, black_coords, L, d2=4)
        rot_nnn_error = max_abs(rot_nnn_amplitudes - expected_rot_nnn)
        check(
            f"Y1d L={L} E-shifted rotated-NNN coupling uses mu-E",
            rot_nnn_error < TOL_COEFF,
            f"expected={expected_rot_nnn:.16e} maxerr={rot_nnn_error:.3e}",
        )

        beyond_error = max_abs(beyond_family_entries(h_eff, black_coords, L, allowed_shells={2, 4}))
        check(
            f"Y1d L={L} E-shifted step-1 has no couplings beyond rotated-NNN",
            beyond_error < TOL_COEFF,
            f"max |off-family entry|={beyond_error:.3e} for d2 not in {{2,4}}",
        )


def run_y1e():
    L = 6
    E = 0.0
    h = square_hamiltonian(L, T, MU)
    black, white = checkerboard_indices(L)
    h_eff = schur_effective_hamiltonian(h, black, white, E=E)

    full_resolvent = np.linalg.inv(E * np.eye(L * L, dtype=float) - h)
    retained_full_resolvent = full_resolvent[np.ix_(black, black)]
    effective_resolvent = np.linalg.inv(E * np.eye(len(black), dtype=float) - h_eff)
    resolvent_error = max_abs(retained_full_resolvent - effective_resolvent)
    check(
        "Y1e L=6 retained-site resolvent is preserved at step 1",
        resolvent_error < TOL_RESOLVENT,
        f"max resolvent error={resolvent_error:.3e}",
    )


def main():
    run_y1a_y1b()
    run_y1c()
    run_y1d()
    run_y1e()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        sys.exit(1)


if __name__ == "__main__":
    main()
