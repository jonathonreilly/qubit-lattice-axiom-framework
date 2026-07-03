#!/usr/bin/env python3
"""Class-A exact verification for the source note

    docs/D3_TRUNCATED_CLOSURE_RECURS_BOUNDED_THEOREM_NOTE_2026-06-12.md

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_d3_truncated_closure_recurs_2026_06_12.py
"""
import sys
from dataclasses import dataclass

import numpy as np


# S4 frozen constants.  These are labels for the gates, not values learned
# from a run.
D = 3
L_VALUES = (8, 12)
STEPS = 3
E0 = 0.0

TOL_ZERO_BLOCK = 1.0e-14
TOL_EQUAL = 1.0e-12
TOL_SHELL_SPREAD = 1.0e-12
TOL_BUDGET = 1.0e-12

INITIAL_DIAG = 2.0 * D
INITIAL_NN = -1.0

EXPECTED_STEP_DIAG = 5.0
EXPECTED_STEP_C2 = -1.0 / 3.0
EXPECTED_STEP_C4 = -1.0 / 6.0
EXPECTED_C2_OVER_DIAG = -1.0 / 15.0
EXPECTED_C4_OVER_DIAG = -1.0 / 30.0
EXPECTED_C4_OVER_C2 = 0.5

EXPECTED_SHELL2_COUNT = 12
EXPECTED_SHELL4_COUNT = 6

SCHUR_RMS_BUDGET_L12_CEILING = 1.5811388310
SCHUR_RMS_RATIO_L8_OVER_L12 = 1.0
IDENTITY_CONTROL_DIAG = 1.0


PASS = 0
FAIL = 0


def check(name, condition, detail=""):
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


@dataclass(frozen=True)
class Couplings:
    diag: float
    c2: float
    c4: float
    spread_diag: float
    spread_c2: float
    spread_c4: float


def lattice_coords(L):
    return np.array(
        [(x, y, z) for x in range(L) for y in range(L) for z in range(L)],
        dtype=np.int16,
    )


def site_index(coord, L):
    x, y, z = coord
    return (int(x) * L + int(y)) * L + int(z)


def parity_indices(coords):
    parity = np.sum(coords, axis=1) & 1
    keep = np.flatnonzero(parity == 0)
    drop = np.flatnonzero(parity == 1)
    return keep, drop


def torus_sqdist(a_coords, b_coords, L):
    delta = b_coords[None, :, :].astype(np.int16) - a_coords[:, None, :].astype(np.int16)
    delta = (delta + (L // 2)) % L - (L // 2)
    return np.sum(delta.astype(np.int32) * delta.astype(np.int32), axis=2)


def max_abs(a):
    if a.size == 0:
        return 0.0
    return float(np.max(np.abs(a)))


def initial_laplacian(L, coords):
    n = L**D
    h = np.zeros((n, n), dtype=np.float64)
    np.fill_diagonal(h, INITIAL_DIAG)
    for coord in coords:
        i = site_index(coord, L)
        for axis in range(D):
            for step in (-1, 1):
                nb = coord.astype(np.int16).copy()
                nb[axis] = (int(nb[axis]) + step) % L
                j = site_index(nb, L)
                h[i, j] = INITIAL_NN
    return h


def stencil_matrix(L, coords, diag, c2, c4):
    sq = torus_sqdist(coords, coords, L)
    h = np.zeros((coords.shape[0], coords.shape[0]), dtype=np.float64)
    h[sq == 0] = diag
    h[sq == 2] = c2
    h[sq == 4] = c4
    return h


def shell_counts(coords_a, coords_b, L, shell):
    sq = torus_sqdist(coords_a, coords_b, L)
    return np.sum(sq == shell, axis=1)


def shell_values(block, coords, L, shell):
    sq = torus_sqdist(coords, coords, L)
    return block[sq == shell]


def shell_mean_and_spread(block, coords, L, shell):
    vals = shell_values(block, coords, L, shell)
    mean = float(np.mean(vals))
    spread = max_abs(vals - mean)
    return mean, spread


def extract_couplings(block, coords, L):
    diag, spread_diag = shell_mean_and_spread(block, coords, L, 0)
    c2, spread_c2 = shell_mean_and_spread(block, coords, L, 2)
    c4, spread_c4 = shell_mean_and_spread(block, coords, L, 4)
    return Couplings(diag, c2, c4, spread_diag, spread_c2, spread_c4)


def project_block_to_kept_shells(block, coords, L, couplings):
    sq = torus_sqdist(coords, coords, L)
    out = np.zeros_like(block)
    out[sq == 0] = couplings.diag
    out[sq == 2] = couplings.c2
    out[sq == 4] = couplings.c4
    return out


def exact_checkerboard_step(h, keep, drop):
    hkk = h[np.ix_(keep, keep)]
    hkd = h[np.ix_(keep, drop)]
    hdk = h[np.ix_(drop, keep)]

    if np.count_nonzero(hkd) == 0:
        correction = np.zeros_like(hkk)
        return hkk.copy(), hkd, correction

    hdd = h[np.ix_(drop, drop)] - E0 * np.eye(drop.size, dtype=np.float64)
    correction = hkd @ np.linalg.solve(hdd, hdk)
    return hkk - correction, hkd, correction


def print_coupling_line(L, step, couplings):
    c2_over_diag = couplings.c2 / couplings.diag
    c4_over_diag = couplings.c4 / couplings.diag
    c4_over_c2 = couplings.c4 / couplings.c2
    print(
        "S4b kept couplings "
        f"L={L} step={step}: "
        f"diag={couplings.diag:.16g} "
        f"c2={couplings.c2:.16g} "
        f"c4={couplings.c4:.16g} "
        f"c2/diag={c2_over_diag:.16g} "
        f"c4/diag={c4_over_diag:.16g} "
        f"c4/c2={c4_over_c2:.16g}"
    )


def wraparound_and_anchor_gates(L, coords, keep):
    n = coords.shape[0]
    counts2_all = shell_counts(coords, coords, L, 2)
    counts4_all = shell_counts(coords, coords, L, 4)
    check(
        f"S4 wraparound/size probe L={L}: full shell d2=2 has 12 sites per row",
        int(np.min(counts2_all)) == EXPECTED_SHELL2_COUNT
        and int(np.max(counts2_all)) == EXPECTED_SHELL2_COUNT,
        f"min={int(np.min(counts2_all))} max={int(np.max(counts2_all))}",
    )
    check(
        f"S4 wraparound/size probe L={L}: full shell d2=4 has 6 sites per row",
        int(np.min(counts4_all)) == EXPECTED_SHELL4_COUNT
        and int(np.max(counts4_all)) == EXPECTED_SHELL4_COUNT,
        f"min={int(np.min(counts4_all))} max={int(np.max(counts4_all))}",
    )

    kept_coords = coords[keep]
    counts2_keep = shell_counts(kept_coords, kept_coords, L, 2)
    counts4_keep = shell_counts(kept_coords, kept_coords, L, 4)
    check(
        f"S4 wraparound/size probe L={L}: kept shell d2=2 has 12 sites per row",
        int(np.min(counts2_keep)) == EXPECTED_SHELL2_COUNT
        and int(np.max(counts2_keep)) == EXPECTED_SHELL2_COUNT,
        f"min={int(np.min(counts2_keep))} max={int(np.max(counts2_keep))}",
    )
    check(
        f"S4 wraparound/size probe L={L}: kept shell d2=4 has 6 sites per row",
        int(np.min(counts4_keep)) == EXPECTED_SHELL4_COUNT
        and int(np.max(counts4_keep)) == EXPECTED_SHELL4_COUNT,
        f"min={int(np.min(counts4_keep))} max={int(np.max(counts4_keep))}",
    )

    h0 = initial_laplacian(L, coords)
    diag_ok = max_abs(np.diag(h0) - INITIAL_DIAG) <= TOL_EQUAL
    row_sum_ok = max_abs(np.sum(h0, axis=1)) <= TOL_EQUAL
    nn_count = np.sum(np.isclose(h0, INITIAL_NN), axis=1)
    check(
        f"S4 anchor L={L}: free cubic Laplacian has diag=6, six NN links, zero row sum",
        diag_ok and row_sum_ok and int(np.min(nn_count)) == 6 and int(np.max(nn_count)) == 6,
        f"diag_maxerr={max_abs(np.diag(h0) - INITIAL_DIAG):.3e} "
        f"rowsum={max_abs(np.sum(h0, axis=1)):.3e} "
        f"nn_min={int(np.min(nn_count))} nn_max={int(np.max(nn_count))}",
    )


def run_truncated_flow(L):
    coords = lattice_coords(L)
    keep, drop = parity_indices(coords)
    kept_coords = coords[keep]
    wraparound_and_anchor_gates(L, coords, keep)

    h = initial_laplacian(L, coords)
    records = []
    accumulated_schur_rms = 0.0
    accumulated_retained_residual_rms = 0.0

    for step in range(1, STEPS + 1):
        exact_retained, input_hkd, correction = exact_checkerboard_step(h, keep, drop)
        couplings = extract_couplings(exact_retained, kept_coords, L)
        projected = project_block_to_kept_shells(exact_retained, kept_coords, L, couplings)
        retained_residual = exact_retained - projected
        retained_residual_rms = float(
            np.linalg.norm(retained_residual, ord="fro") / np.sqrt(exact_retained.shape[0])
        )
        schur_rms = float(np.linalg.norm(correction, ord="fro") / np.sqrt(exact_retained.shape[0]))
        accumulated_schur_rms += schur_rms
        accumulated_retained_residual_rms += retained_residual_rms

        h_trunc = stencil_matrix(L, coords, couplings.diag, couplings.c2, couplings.c4)
        truncated_hkd = h_trunc[np.ix_(keep, drop)]
        truncated_hkd_norm = max_abs(truncated_hkd)

        print_coupling_line(L, step, couplings)
        print(
            "S4c budgets "
            f"L={L} step={step}: "
            f"schur_rms={schur_rms:.16g} "
            f"retained_residual_rms={retained_residual_rms:.16g}"
        )

        check(
            f"S4a d=3 parity lemma: truncated kept-to-decimated block zero L={L} step={step}",
            truncated_hkd_norm <= TOL_ZERO_BLOCK,
            f"max_abs_Hkd={truncated_hkd_norm:.3e}; shells d2=2,4 have even coordinate parity",
        )
        check(
            f"S4 anti-fabrication L={L} step={step}: shell values are translation-invariant before mirroring",
            couplings.spread_diag <= TOL_SHELL_SPREAD
            and couplings.spread_c2 <= TOL_SHELL_SPREAD
            and couplings.spread_c4 <= TOL_SHELL_SPREAD,
            f"spreads diag={couplings.spread_diag:.3e} "
            f"c2={couplings.spread_c2:.3e} c4={couplings.spread_c4:.3e}",
        )
        check(
            f"S4 anti-fabrication L={L} step={step}: retained block has no out-of-family shell residual",
            retained_residual_rms <= TOL_BUDGET,
            f"retained_residual_rms={retained_residual_rms:.3e}",
        )

        if step == 1:
            check(
                f"S4 anchor L={L}: step-1 exact Schur couplings land on diag=5,c2=-1/3,c4=-1/6",
                abs(couplings.diag - EXPECTED_STEP_DIAG) <= TOL_EQUAL
                and abs(couplings.c2 - EXPECTED_STEP_C2) <= TOL_EQUAL
                and abs(couplings.c4 - EXPECTED_STEP_C4) <= TOL_EQUAL,
                f"diag={couplings.diag:.16g} c2={couplings.c2:.16g} c4={couplings.c4:.16g}",
            )

        records.append(
            {
                "step": step,
                "couplings": couplings,
                "input_hkd_norm": max_abs(input_hkd),
                "truncated_hkd_norm": truncated_hkd_norm,
                "schur_rms": schur_rms,
                "retained_residual_rms": retained_residual_rms,
            }
        )
        h = h_trunc

    c = [r["couplings"] for r in records]
    step2_step3_delta = max(
        abs(c[2].diag - c[1].diag),
        abs(c[2].c2 - c[1].c2),
        abs(c[2].c4 - c[1].c4),
    )
    step1_to_later_delta = max(
        abs(c[i].diag - c[0].diag)
        for i in range(1, STEPS)
    )
    step1_to_later_delta = max(
        step1_to_later_delta,
        max(abs(c[i].c2 - c[0].c2) for i in range(1, STEPS)),
        max(abs(c[i].c4 - c[0].c4) for i in range(1, STEPS)),
    )
    ratios = (
        c[0].c2 / c[0].diag,
        c[0].c4 / c[0].diag,
        c[0].c4 / c[0].c2,
    )
    check(
        f"S4b d=3 recurrence: exact post-step-2 invariance recurs because H_kd=0 forces no Schur update L={L}",
        step2_step3_delta <= TOL_EQUAL,
        f"max_step3_minus_step2={step2_step3_delta:.3e}",
    )
    check(
        f"S4b stronger fixed pattern: all three truncated steps share the landed couplings L={L}",
        step1_to_later_delta <= TOL_EQUAL,
        f"max_later_minus_step1={step1_to_later_delta:.3e}",
    )
    check(
        f"S4b fixed ratio pattern L={L}: c2/diag=-1/15, c4/diag=-1/30, c4/c2=1/2",
        abs(ratios[0] - EXPECTED_C2_OVER_DIAG) <= TOL_EQUAL
        and abs(ratios[1] - EXPECTED_C4_OVER_DIAG) <= TOL_EQUAL
        and abs(ratios[2] - EXPECTED_C4_OVER_C2) <= TOL_EQUAL,
        f"ratios=({ratios[0]:.16g}, {ratios[1]:.16g}, {ratios[2]:.16g})",
    )

    return {
        "records": records,
        "accumulated_schur_rms": accumulated_schur_rms,
        "accumulated_retained_residual_rms": accumulated_retained_residual_rms,
    }


def identity_truncation_control(L):
    coords = lattice_coords(L)
    keep, drop = parity_indices(coords)
    kept_coords = coords[keep]
    h = IDENTITY_CONTROL_DIAG * np.eye(coords.shape[0], dtype=np.float64)
    worst = 0.0
    for _ in range(STEPS):
        exact_retained, _, _ = exact_checkerboard_step(h, keep, drop)
        couplings = extract_couplings(exact_retained, kept_coords, L)
        worst = max(
            worst,
            abs(couplings.diag - IDENTITY_CONTROL_DIAG),
            abs(couplings.c2),
            abs(couplings.c4),
            couplings.spread_diag,
            couplings.spread_c2,
            couplings.spread_c4,
        )
        h = stencil_matrix(L, coords, couplings.diag, couplings.c2, couplings.c4)
    check(
        f"S4d identity-truncation control L={L}: tautological sanity at 1e-12",
        worst <= TOL_EQUAL,
        f"worst_identity_deviation={worst:.3e}",
    )


def main():
    flows = {}
    for L in L_VALUES:
        flows[L] = run_truncated_flow(L)
        identity_truncation_control(L)

    budget_l8 = flows[8]["accumulated_schur_rms"]
    budget_l12 = flows[12]["accumulated_schur_rms"]
    retained_l8 = flows[8]["accumulated_retained_residual_rms"]
    retained_l12 = flows[12]["accumulated_retained_residual_rms"]
    ratio = budget_l8 / budget_l12

    print(
        "S4c accumulated retained-block Schur/resolvent RMS budgets: "
        f"L=8 {budget_l8:.16g}; L=12 {budget_l12:.16g}; ratio {ratio:.16g}"
    )
    print(
        "S4c accumulated retained-block residual-vs-fully-exact RMS budgets: "
        f"L=8 {retained_l8:.16g}; L=12 {retained_l12:.16g}"
    )
    check(
        "S4c L=12 accumulated retained-block Schur/resolvent RMS budget under frozen regression ceiling",
        budget_l12 <= SCHUR_RMS_BUDGET_L12_CEILING,
        f"budget_l12={budget_l12:.16g} ceiling={SCHUR_RMS_BUDGET_L12_CEILING:.16g}",
    )
    check(
        "S4c fixed measured size pattern: L=8/L=12 Schur/resolvent RMS budget ratio is 1",
        abs(ratio - SCHUR_RMS_RATIO_L8_OVER_L12) <= TOL_EQUAL,
        f"ratio={ratio:.16g}",
    )
    check(
        "S4c L=12 retained block residual vs fully-exact is roundoff-zero under frozen ceiling",
        retained_l12 <= TOL_BUDGET,
        f"retained_l12={retained_l12:.3e}",
    )
    check(
        "S4c fixed measured retained residual size pattern: L=8 and L=12 both roundoff-zero",
        retained_l8 <= TOL_BUDGET and retained_l12 <= TOL_BUDGET,
        f"retained_l8={retained_l8:.3e} retained_l12={retained_l12:.3e}",
    )

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        sys.exit(1)


if __name__ == "__main__":
    main()
