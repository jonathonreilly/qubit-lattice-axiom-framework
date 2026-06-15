#!/usr/bin/env python3
"""Class-A exact verification for the source note

    docs/D3_CHECKERBOARD_STEP1_CLOSED_FORM_PARITY_LEMMA_BOUNDED_THEOREM_NOTE_2026-06-12.md

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_d3_checkerboard_step1_parity_lemma_2026_06_12.py
"""
import sys

import numpy as np


MU = 4.0
T = 0.5
E0 = 0.0
E_PROBE = 0.3

L_ANCHOR = 6
L_WRAP = 8

TOL_HOO = 1.0e-14
TOL_COUP = 1.0e-12
TOL_PARITY = 1.0e-14
TOL_RESOLVENT = 1.0e-10
MIN_NONZERO = 1.0e-9

D2_FACE = 2
D2_AXIAL = 4
PATHS_DIAG = 6
PATHS_FACE = 2
PATHS_AXIAL = 1
EXPECTED_STEP_NEIGHBORS = 18

DIRECTIONS = np.array(
    [
        [1, 0, 0],
        [-1, 0, 0],
        [0, 1, 0],
        [0, -1, 0],
        [0, 0, 1],
        [0, 0, -1],
    ],
    dtype=int,
)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name, condition):
    global PASS_COUNT, FAIL_COUNT
    ok = bool(condition)
    if ok:
        PASS_COUNT += 1
        print(f"PASS: {name}")
    else:
        FAIL_COUNT += 1
        print(f"FAIL: {name}")


def max_abs(a):
    return float(np.max(np.abs(a)))


def site_index(x, y, z, L):
    return (z * L + y) * L + x


def lattice_coords(L):
    return np.array(
        [(x, y, z) for z in range(L) for y in range(L) for x in range(L)],
        dtype=int,
    )


def build_hamiltonian(L):
    coords = lattice_coords(L)
    n = L**3
    h = np.zeros((n, n), dtype=float)
    np.fill_diagonal(h, MU)
    for i, xyz in enumerate(coords):
        for dxyz in DIRECTIONS:
            nbr = (xyz + dxyz) % L
            j = site_index(int(nbr[0]), int(nbr[1]), int(nbr[2]), L)
            h[i, j] = -T
    return h, coords


def periodic_d2(coords, L):
    delta = coords[None, :, :] - coords[:, None, :]
    delta = (delta + (L // 2)) % L - (L // 2)
    return np.sum(delta * delta, axis=2)


def decimation_data(L, energy):
    h, coords = build_hamiltonian(L)
    parity = np.sum(coords, axis=1) % 2
    even = np.flatnonzero(parity == 0)
    odd = np.flatnonzero(parity == 1)

    h_ee = h[np.ix_(even, even)]
    h_eo = h[np.ix_(even, odd)]
    h_oe = h[np.ix_(odd, even)]
    h_oo = h[np.ix_(odd, odd)]

    odd_resolvent_den = energy * np.eye(len(odd), dtype=float) - h_oo
    h_eff = h_ee + h_eo @ np.linalg.inv(odd_resolvent_den) @ h_oe
    path_counts = (np.abs(h_eo) > 0.0).astype(int) @ (np.abs(h_oe) > 0.0).astype(int)
    d2 = periodic_d2(coords[even], L)

    diag_mask = np.eye(len(even), dtype=bool)
    face_mask = (~diag_mask) & (d2 == D2_FACE)
    axial_mask = (~diag_mask) & (d2 == D2_AXIAL)
    beyond_mask = (~diag_mask) & (d2 != D2_FACE) & (d2 != D2_AXIAL)

    return {
        "L": L,
        "energy": energy,
        "h": h,
        "coords": coords,
        "parity": parity,
        "even": even,
        "odd": odd,
        "h_oo": h_oo,
        "h_eff": h_eff,
        "path_counts": path_counts,
        "d2": d2,
        "diag_mask": diag_mask,
        "face_mask": face_mask,
        "axial_mask": axial_mask,
        "beyond_mask": beyond_mask,
    }


def expected_step_matrix(data):
    denom = MU - data["energy"]
    expected = np.zeros_like(data["h_eff"])
    expected[data["diag_mask"]] = MU - PATHS_DIAG * T * T / denom
    expected[data["face_mask"]] = -PATHS_FACE * T * T / denom
    expected[data["axial_mask"]] = -PATHS_AXIAL * T * T / denom
    return expected


def expected_path_matrix(data):
    expected = np.zeros_like(data["path_counts"])
    expected[data["diag_mask"]] = PATHS_DIAG
    expected[data["face_mask"]] = PATHS_FACE
    expected[data["axial_mask"]] = PATHS_AXIAL
    return expected


def shell_signature(data):
    h_eff = data["h_eff"]
    paths = data["path_counts"].astype(float)
    diag = h_eff[data["diag_mask"]]
    face = -h_eff[data["face_mask"]]
    axial = -h_eff[data["axial_mask"]]
    beyond = h_eff[data["beyond_mask"]]
    diag_paths = paths[data["diag_mask"]]
    face_paths = paths[data["face_mask"]]
    axial_paths = paths[data["axial_mask"]]
    beyond_paths = paths[data["beyond_mask"]]
    return np.array(
        [
            np.min(diag),
            np.max(diag),
            np.min(face),
            np.max(face),
            np.min(axial),
            np.max(axial),
            np.max(np.abs(beyond)),
            np.min(diag_paths),
            np.max(diag_paths),
            np.min(face_paths),
            np.max(face_paths),
            np.min(axial_paths),
            np.max(axial_paths),
            np.max(np.abs(beyond_paths)),
        ],
        dtype=float,
    )


def anchor_reproduction_ok(data):
    h = data["h"]
    n = h.shape[0]
    offdiag = np.abs(h) > 0.0
    np.fill_diagonal(offdiag, False)
    degree = np.sum(offdiag, axis=1)
    split_size = np.array([len(data["even"]), len(data["odd"])], dtype=int)
    expected_split = np.array([n // 2, n // 2], dtype=int)
    degree_ok = np.array_equal(degree, np.full(n, PATHS_DIAG, dtype=int))
    split_ok = np.array_equal(split_size, expected_split)
    symmetry_ok = max_abs(h - h.T) <= TOL_HOO
    return degree_ok and split_ok and symmetry_ok


def algebraic_parity_lemma_ok():
    vals = np.arange(-4, 5, dtype=int)
    disps = np.array([(x, y, z) for x in vals for y in vals for z in vals], dtype=int)
    lhs = np.sum(disps * disps, axis=1) % 2
    rhs = np.sum(disps, axis=1) % 2
    return np.array_equal(lhs, rhs)


def even_shell_next_checkerboard_block_norm(data):
    L = data["L"]
    h_full, coords = build_hamiltonian(L)
    n = h_full.shape[0]
    parity = np.sum(coords, axis=1) % 2
    even = np.flatnonzero(parity == 0)
    odd = np.flatnonzero(parity == 1)

    retained_h = data["h_eff"]
    diag_coeff = float(np.mean(retained_h[data["diag_mask"]]))
    face_coeff = float(np.mean(retained_h[data["face_mask"]]))
    axial_coeff = float(np.mean(retained_h[data["axial_mask"]]))

    d2_full = periodic_d2(coords, L)
    diag_full = np.eye(n, dtype=bool)
    face_full = (~diag_full) & (d2_full == D2_FACE)
    axial_full = (~diag_full) & (d2_full == D2_AXIAL)

    truncated = np.zeros((n, n), dtype=float)
    truncated[diag_full] = diag_coeff
    truncated[face_full] = face_coeff
    truncated[axial_full] = axial_coeff
    return max_abs(truncated[np.ix_(even, odd)])


def retained_resolvent_error(data):
    h = data["h"]
    energy = data["energy"]
    n = h.shape[0]
    retained = data["even"]
    full_resolvent = np.linalg.inv(energy * np.eye(n, dtype=float) - h)
    retained_full = full_resolvent[np.ix_(retained, retained)]
    h_eff = data["h_eff"]
    effective_resolvent = np.linalg.inv(
        energy * np.eye(h_eff.shape[0], dtype=float) - h_eff
    )
    return max_abs(retained_full - effective_resolvent)


def main():
    data0 = decimation_data(L_ANCHOR, E0)
    data_wrap = decimation_data(L_WRAP, E0)
    data_probe = decimation_data(L_ANCHOR, E_PROBE)

    check(
        "ANCHOR reproduction: periodic cubic NN degree and parity split",
        anchor_reproduction_ok(data0),
    )

    offdiag0 = np.array(data0["h_eff"], copy=True)
    offdiag0[data0["diag_mask"]] = 0.0
    nonzero_count = int(np.count_nonzero(np.abs(offdiag0) > TOL_COUP))
    check(
        "anti-fabrication: generated step-1 couplings are nonzero",
        (max_abs(offdiag0) > MIN_NONZERO)
        and (nonzero_count == len(data0["even"]) * EXPECTED_STEP_NEIGHBORS),
    )

    h_oo_expected = MU * np.eye(len(data0["odd"]), dtype=float)
    check(
        "T1a h_oo diagonality on odd sublattice",
        max_abs(data0["h_oo"] - h_oo_expected) <= TOL_HOO,
    )

    expected_paths0 = expected_path_matrix(data0)
    check(
        "T1b path table: diag=6, d2=2 has 2 paths, d2=4 has 1 path",
        np.array_equal(data0["path_counts"], expected_paths0),
    )

    expected0 = expected_step_matrix(data0)
    check(
        "T1b closed form diag prime equals mu - 6 t^2 / mu",
        max_abs(np.diag(data0["h_eff"]) - np.diag(expected0)) <= TOL_COUP,
    )
    check(
        "T1b signed coefficient table for d2=2 and d2=4 shells",
        max_abs((data0["h_eff"] - expected0)[~data0["beyond_mask"]]) <= TOL_COUP,
    )
    check(
        "T1b no generated couplings beyond measured d2=2 and d2=4 shells",
        max_abs(data0["h_eff"][data0["beyond_mask"]]) <= TOL_COUP,
    )

    expected_wrap = expected_step_matrix(data_wrap)
    wrap_matrix_ok = max_abs(data_wrap["h_eff"] - expected_wrap) <= TOL_COUP
    wrap_paths_ok = np.array_equal(data_wrap["path_counts"], expected_path_matrix(data_wrap))
    wrap_signature_ok = max_abs(shell_signature(data0) - shell_signature(data_wrap)) <= TOL_COUP
    check(
        "T1b L=8 vs L=6 wraparound agreement for step-1 shell data",
        wrap_matrix_ok and wrap_paths_ok and wrap_signature_ok,
    )

    check(
        "T1c algebraic d=3 parity lemma for |d|_inf <= 4",
        algebraic_parity_lemma_ok(),
    )
    check(
        "T1c operational next-checkerboard kept-to-decimated block is zero",
        even_shell_next_checkerboard_block_norm(data0) <= TOL_PARITY,
    )

    expected_probe = expected_step_matrix(data_probe)
    check(
        "T1d E-covariance: mu denominator shifts to mu - E at E=0.3",
        max_abs(data_probe["h_eff"] - expected_probe) <= TOL_COUP,
    )

    check(
        "T1e retained-site resolvent is preserved by step-1 Schur complement",
        retained_resolvent_error(data0) <= TOL_RESOLVENT,
    )

    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        sys.exit(1)


if __name__ == "__main__":
    main()
