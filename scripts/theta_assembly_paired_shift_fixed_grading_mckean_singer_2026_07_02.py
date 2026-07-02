#!/usr/bin/env python3
import sys

import numpy as np


SEED = 20260702
TINY_ANTICOM = 1e-14
T_L1 = 1e-10
T_LOG = 1e-9
T_PHASE = 1e-10
T_FLUX_PHASE = 1e-12
T_FLUX_TOTAL = 1e-10


def f17(x):
    return f"{float(x):.17e}"


def label_q(q):
    return f"B2Q({q})"


def eta(coords, mu):
    return 1 if (sum(coords[:mu]) % 2 == 0) else -1


def eps_for_dims(dims):
    values = []
    for coords in np.ndindex(*dims):
        values.append(1 if (sum(coords) % 2 == 0) else -1)
    return np.array(values, dtype=float)


def random_links(dims, rng):
    phases = rng.uniform(0.0, 2.0 * np.pi, size=(len(dims),) + tuple(dims))
    return np.exp(1j * phases)


def free_links(dims):
    return np.ones((len(dims),) + tuple(dims), dtype=complex)


def flux_links_2d(l_size, q):
    links = np.ones((2, l_size, l_size), dtype=complex)
    for x in range(l_size):
        for y in range(l_size):
            if x == l_size - 1:
                links[0, x, y] = np.exp(-1j * 2.0 * np.pi * q * y / l_size)
            links[1, x, y] = np.exp(1j * 2.0 * np.pi * q * x / (l_size * l_size))
    return links


def build_staggered_d(dims, links):
    dims = tuple(dims)
    n_sites = int(np.prod(dims))
    d_mat = np.zeros((n_sites, n_sites), dtype=complex)
    for coords in np.ndindex(*dims):
        row = np.ravel_multi_index(coords, dims)
        for mu in range(len(dims)):
            sign = eta(coords, mu)

            fwd = list(coords)
            fwd[mu] = (fwd[mu] + 1) % dims[mu]
            col_fwd = np.ravel_multi_index(tuple(fwd), dims)
            d_mat[row, col_fwd] += 0.5 * sign * links[(mu,) + coords]

            back = list(coords)
            back[mu] = (back[mu] - 1) % dims[mu]
            col_back = np.ravel_multi_index(tuple(back), dims)
            d_mat[row, col_back] += -0.5 * sign * np.conj(links[(mu,) + tuple(back)])
    return d_mat


def plaquette_values_2d(links):
    l_size = links.shape[1]
    vals = np.empty((l_size, l_size), dtype=complex)
    for x in range(l_size):
        for y in range(l_size):
            vals[x, y] = (
                links[0, x, y]
                * links[1, (x + 1) % l_size, y]
                * np.conj(links[0, x, (y + 1) % l_size])
                * np.conj(links[1, x, y])
            )
    return vals


def spectral_data(d_mat):
    h_mat = d_mat.conj().T @ d_mat
    vals, vecs = np.linalg.eigh(h_mat)
    return vals, vecs


def heat_index_from_spectral(vals, vecs, eps_diag, t_val):
    weights = np.sum((np.abs(vecs) ** 2) * eps_diag[:, None], axis=0)
    return float(np.sum(np.exp(-t_val * vals) * weights).real)


def heat_index(d_mat, eps_diag, t_val):
    vals, vecs = spectral_data(d_mat)
    return heat_index_from_spectral(vals, vecs, eps_diag, t_val)


def determinant_ratio(d_mat, eps_diag, alpha, mass):
    ident = np.eye(d_mat.shape[0], dtype=complex)
    twist = np.diag(mass * np.exp(2j * alpha * eps_diag))
    sign_1, log_1 = np.linalg.slogdet(d_mat + twist)
    sign_0, log_0 = np.linalg.slogdet(d_mat + mass * ident)
    return sign_1 / sign_0, float(log_1), float(log_0)


def max_abs_entries(mat):
    return float(np.max(np.abs(mat)))


def toy_background(rng):
    b_mat = rng.normal(size=(3, 2)) + 1j * rng.normal(size=(3, 2))
    d_mat = np.zeros((5, 5), dtype=complex)
    d_mat[:3, 3:] = b_mat
    d_mat[3:, :3] = -b_mat.conj().T
    eps_diag = np.array([1, 1, 1, -1, -1], dtype=float)
    return d_mat, eps_diag


def main():
    rng = np.random.default_rng(SEED)
    rows = []

    def record(gate, quantity, tolerance, measured, passed):
        rows.append(passed)
        status = "PASS" if passed else "FAIL"
        print(f"| {gate} | {quantity} | {tolerance} | {measured} | {status} |")

    print("| Gate | Quantity | Tolerance | Measured | Result |")
    print("|---|---|---:|---:|---|")

    dims4 = (4, 4, 4, 4)
    dims2 = (8, 8)
    backgrounds = {}

    links4_free = free_links(dims4)
    links4_rand = random_links(dims4, rng)
    backgrounds["B4free"] = (build_staggered_d(dims4, links4_free), eps_for_dims(dims4))
    backgrounds["B4rand"] = (build_staggered_d(dims4, links4_rand), eps_for_dims(dims4))

    b2_links = {}
    for q in [0, 1, -1, 2, -2]:
        links = flux_links_2d(8, q)
        b2_links[q] = links
        plaq = plaquette_values_2d(links)
        target = np.exp(1j * 2.0 * np.pi * q / (8 * 8))
        phase_resid = float(np.max(np.abs(plaq - target)))
        total_flux = float(np.sum(np.angle(plaq)))
        total_resid = abs(total_flux - 2.0 * np.pi * q)
        record(
            f"G0[{label_q(q)}]",
            "uniform plaquette phase and total flux",
            f"phase<{T_FLUX_PHASE:.1e}; total<{T_FLUX_TOTAL:.1e}",
            f"phase_resid={f17(phase_resid)}; total_resid={f17(total_resid)}",
            phase_resid < T_FLUX_PHASE and total_resid < T_FLUX_TOTAL,
        )
        backgrounds[label_q(q)] = (build_staggered_d(dims2, links), eps_for_dims(dims2))

    links2_rand = random_links(dims2, rng)
    d2_rand = build_staggered_d(dims2, links2_rand)
    eps2 = eps_for_dims(dims2)

    d_toy, eps_toy = toy_background(rng)
    backgrounds["Btoy"] = (d_toy, eps_toy)

    spectral_cache = {}
    for name, (d_mat, eps_diag) in backgrounds.items():
        eps_mat = np.diag(eps_diag)
        anti_resid = max_abs_entries(eps_mat @ d_mat + d_mat @ eps_mat)
        herm_resid = max_abs_entries(d_mat + d_mat.conj().T)
        record(
            f"G1[{name}]",
            "max anticommutator entry and anti-Hermitian entry",
            f"each<{TINY_ANTICOM:.1e}",
            f"anticom={f17(anti_resid)}; antiherm={f17(herm_resid)}",
            anti_resid < TINY_ANTICOM and herm_resid < TINY_ANTICOM,
        )
        spectral_cache[name] = spectral_data(d_mat)

    for name, (d_mat, eps_diag) in backgrounds.items():
        vals, vecs = spectral_cache[name]
        tr_eps = float(np.sum(eps_diag))
        residuals = []
        measured = []
        for t_val in [0.3, 1.0, 3.0]:
            a_t = heat_index_from_spectral(vals, vecs, eps_diag, t_val)
            residuals.append(abs(a_t - tr_eps))
            measured.append(f"t={t_val}:resid={f17(abs(a_t - tr_eps))}")
        max_resid = max(residuals)
        record(
            f"G2[{name}]",
            "max abs(A_t - tr(eps)) over t=0.3,1.0,3.0",
            f"<{T_L1:.1e}",
            "; ".join(measured) + f"; max={f17(max_resid)}",
            max_resid < T_L1,
        )

    for q in [0, 1, -1, 2, -2]:
        name = label_q(q)
        d_mat, eps_diag = backgrounds[name]
        vals, vecs = spectral_cache[name]
        a_one = heat_index_from_spectral(vals, vecs, eps_diag, 1.0)
        sigma_min = float(np.linalg.svd(d_mat, compute_uv=False)[-1])
        resid = abs(a_one)
        record(
            f"G2b[{name}]",
            "Q-blind A_1 residual; sigma_min diagnostic",
            f"A_1<{T_L1:.1e}; sigma no gate",
            f"A1_resid={f17(resid)}; sigma_min={f17(sigma_min)}",
            resid < T_L1,
        )

    alpha_grid = [(0.3, "0.3"), (0.7, "0.7"), (np.pi / 3.0, "pi/3")]
    mass_grid = [0.1, 0.5]
    g3_names = ["B4free", "B4rand", "B2Q(1)", "Btoy"]

    ratio_cache = {}
    for name in g3_names:
        d_mat, eps_diag = backgrounds[name]
        tr_eps = float(np.sum(eps_diag))
        for alpha, alpha_label in alpha_grid:
            for mass in mass_grid:
                ratio, log_1, log_0 = determinant_ratio(d_mat, eps_diag, alpha, mass)
                log_resid = abs(log_1 - log_0)
                phase_resid = abs(ratio - np.exp(2j * alpha * tr_eps))
                ratio_cache[(name, alpha_label, mass)] = ratio
                record(
                    f"G3[{name},alpha={alpha_label},m={mass}]",
                    "slogdet logabs equality and determinant phase identity",
                    f"log<{T_LOG:.1e}; phase<{T_PHASE:.1e}",
                    f"log_resid={f17(log_resid)}; phase_resid={f17(phase_resid)}",
                    log_resid < T_LOG and phase_resid < T_PHASE,
                )

    for name in g3_names:
        d_mat, eps_diag = backgrounds[name]
        tr_eps = float(np.sum(eps_diag))
        for alpha, alpha_label in alpha_grid:
            for mass in mass_grid:
                ratio = ratio_cache[(name, alpha_label, mass)]
                jac = np.exp(-2j * alpha * tr_eps)
                resid = abs(jac * ratio - 1.0)
                record(
                    f"G4[{name},alpha={alpha_label},m={mass}]",
                    "measure deposit times mass-det shift",
                    f"<{T_PHASE:.1e}",
                    f"invariance_resid={f17(resid)}",
                    resid < T_PHASE,
                )

    toy_ratio_nontrivial = ratio_cache[("Btoy", "0.7", 0.5)]
    toy_nontriv = abs(toy_ratio_nontrivial - 1.0)
    record(
        "G4[Btoy,alpha=0.7,m=0.5,nontriviality]",
        "abs(mass-det shift - 1)",
        ">1.0e-01",
        f"nontriviality={f17(toy_nontriv)}",
        toy_nontriv > 0.1,
    )

    eps_wrong = []
    for coords in np.ndindex(*dims2):
        eps_wrong.append(1 if (coords[0] % 2 == 0) else -1)
    eps_wrong = np.array(eps_wrong, dtype=float)
    eps_wrong_mat = np.diag(eps_wrong)
    wrong_anti = max_abs_entries(eps_wrong_mat @ d2_rand + d2_rand @ eps_wrong_mat)
    record(
        "G5a[B2rand,wrong-eps]",
        "broken-premise anticommutator magnitude",
        ">1.0e-01",
        f"anticom={f17(wrong_anti)}",
        wrong_anti > 0.1,
    )
    wrong_ratio, _, _ = determinant_ratio(d2_rand, eps_wrong, 0.7, 0.5)
    wrong_phase_resid = abs(wrong_ratio - np.exp(2j * 0.7 * float(np.sum(eps_wrong))))
    record(
        "G5a[B2rand,wrong-eps]",
        "wrong-grading determinant identity rejector",
        ">1.0e-03",
        f"phase_resid={f17(wrong_phase_resid)}",
        wrong_phase_resid > 1e-3,
    )
    wrong_a_one = heat_index(d2_rand, eps_wrong, 1.0)
    print(
        "| DIAG[G5a,B2rand,wrong-eps] | A_1(eps') diagnostic | no gate | "
        f"A1_wrong={f17(wrong_a_one)} | INFO |"
    )

    g_diag = rng.normal(0.0, 0.3, size=d2_rand.shape[0])
    d_pert = d2_rand + 1j * np.diag(g_diag)
    a_03 = heat_index(d_pert, eps2, 0.3)
    a_30 = heat_index(d_pert, eps2, 3.0)
    t_dep = abs(a_03 - a_30)
    record(
        "G5b[B2rand,Dpert]",
        "broken-anticommutation heat-index t-dependence",
        ">1.0e-06",
        f"abs(A0.3-A3.0)={f17(t_dep)}",
        t_dep > 1e-6,
    )

    toy_ratio = ratio_cache[("Btoy", "0.7", 0.5)]
    toy_wrong_n = abs(toy_ratio - np.exp(2j * 0.7 * (float(np.sum(eps_toy)) + 1.0)))
    record(
        "G6[Btoy,wrong-n]",
        "reject tr(eps)+1 determinant phase",
        ">1.0e-03",
        f"phase_resid={f17(toy_wrong_n)}",
        toy_wrong_n > 1e-3,
    )

    b2q1_ratio = ratio_cache[("B2Q(1)", "0.7", 0.5)]
    b2q1_wrong_q = abs(b2q1_ratio - np.exp(2j * 0.7 * 1.0))
    record(
        "G6[B2Q(1),wrong-Q-as-n]",
        "reject pretending n is set by Q",
        ">1.0e-03",
        f"phase_resid={f17(b2q1_wrong_q)}",
        b2q1_wrong_q > 1e-3,
    )

    toy_vals, toy_vecs = spectral_cache["Btoy"]
    toy_a_resids = []
    for t_val in [0.3, 1.0, 3.0]:
        a_t = heat_index_from_spectral(toy_vals, toy_vecs, eps_toy, t_val)
        toy_a_resids.append(abs(a_t - 1.0))
    record(
        "G7[Btoy,A_t]",
        "toy A_t exactness over t=0.3,1.0,3.0",
        f"<{T_L1:.1e}",
        f"max_resid={f17(max(toy_a_resids))}",
        max(toy_a_resids) < T_L1,
    )

    toy_det_resids = []
    for alpha, alpha_label in alpha_grid:
        for mass in mass_grid:
            ratio = ratio_cache[("Btoy", alpha_label, mass)]
            toy_det_resids.append(abs(ratio - np.exp(2j * alpha)))
    record(
        "G7[Btoy,det]",
        "toy determinant ratio exactness over G3 grid",
        f"<{T_PHASE:.1e}",
        f"max_resid={f17(max(toy_det_resids))}",
        max(toy_det_resids) < T_PHASE,
    )

    passes = sum(1 for ok in rows if ok)
    failures = len(rows) - passes
    print(f"TOTAL: PASS={passes} FAIL={failures}")
    sys.exit(0 if failures == 0 else 1)


if __name__ == "__main__":
    main()
