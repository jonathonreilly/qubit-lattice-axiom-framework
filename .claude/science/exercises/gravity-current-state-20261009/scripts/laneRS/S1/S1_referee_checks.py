"""Independent numerical checks for the Lane RS/S1 referee pass.

The null-space checks reuse the submitted physical symbol and vertex, but build
the full sampled design matrix and SVD it directly (no submitted TSQR path).
The one-particle and finite-cluster limiting-distance checks are independent
constructions from the stated real-space Hamiltonian.
"""

import itertools
import numpy as np

from s1_matrix_collision import (
    ALLCH,
    Stag,
    basis,
    block_map_Q,
    residual_rows,
    sample_processes,
)


def independent_one_particle_checks():
    print("== independent one-particle checks")
    rng = np.random.default_rng(81473)
    for d in (2, 3):
        model = Stag(d, 0.5, "nn")
        worst_square = 0.0
        worst_band = 0.0
        for _ in range(20):
            k = rng.uniform(-np.pi / 2, np.pi / 2, d)
            h = model.h(k)
            omega = model.omega(k)[0]
            worst_square = max(
                worst_square,
                np.linalg.norm(h @ h - omega**2 * np.eye(2**d)),
            )
            ev = np.linalg.eigvalsh(h)
            target = np.r_[np.full(2 ** (d - 1), -omega), np.full(2 ** (d - 1), omega)]
            worst_band = max(worst_band, np.max(np.abs(ev - target)))
        print(
            f"d={d}: max ||h^2-omega^2 I||_F={worst_square:.3e}; "
            f"max band error={worst_band:.3e}; generic multiplicities={2**(d-1)}+{2**(d-1)}"
        )
        hcone = Stag(d, 0.0, "nn").h(np.zeros(d))
        print(
            f"d={d}, m=0 cone: ||h(0)||_F={np.linalg.norm(hcone):.3e}; "
            f"exact zero multiplicity={2**d} (floating sin(pi) residue only)"
        )

    # Independent real-space construction and the stated two-link P_x.
    Lx = Ly = 6
    sites = [(x, y) for x in range(Lx) for y in range(Ly)]
    pos = {x: i for i, x in enumerate(sites)}
    h = np.zeros((len(sites), len(sites)), complex)
    p = np.zeros_like(h)
    for x, y in sites:
        i = pos[(x, y)]
        h[i, i] += 0.5 * (-1) ** (x + y)
        for dx, dy, eta in ((1, 0, 1), (0, 1, (-1) ** x)):
            j = pos[((x + dx) % Lx, (y + dy) % Ly)]
            h[i, j] += 0.5j * eta
            h[j, i] -= 0.5j * eta
        j2 = pos[((x + 2) % Lx, y)]
        p[i, j2] += 1 / (4j)
        p[j2, i] -= 1 / (4j)
    print(
        f"real-space 6x6: ||[h,Px]||_F={np.linalg.norm(h@p-p@h):.3e}; "
        f"Hermiticity error={np.linalg.norm(p-p.conj().T):.3e}"
    )
    expected = []
    for nx in range(Lx):
        px = 2 * np.pi * nx / Lx
        expected.extend([0.5 * np.sin(2 * px)] * Ly)
    spectrum_error = np.max(
        np.abs(np.sort(np.linalg.eigvalsh(p)) - np.sort(np.asarray(expected)))
    )
    print(
        f"two-link Fourier symbol max |P|={np.max(np.abs(expected)):.12f}; "
        f"spectrum error={spectrum_error:.3e}"
    )


def shift_symbol(model, k, mu):
    """Reduced-zone symbol of S_mu, independently from the submitted Schur runner."""
    b = np.array([1 if j > mu else 0 for j in range(model.d)])
    r = np.eye(model.d, dtype=int)[mu]
    out = np.zeros((model.n, model.n), complex)
    for a in range(model.n):
        out[model.xor[a, model.idx(b)], a] = np.exp(
            1j * np.dot(k + np.pi * model.As[a], r)
        )
    return out


def sector_ordered_positive_frame(model, k):
    _, up, _ = model.U(k)
    normalized = [
        np.exp(-1j * k[mu]) * shift_symbol(model, k, mu)
        for mu in range(model.d)
    ]
    if model.d == 2:
        z = -1j * normalized[0] @ normalized[1]
    else:
        z = -1j * normalized[0] @ normalized[1] @ normalized[2]
    zband = up.conj().T @ z @ up
    label, vectors = np.linalg.eigh((zband + zband.conj().T) / 2)
    return label, up @ vectors


def forward_amplitude_checks():
    print("\n== sector-resolved forward-amplitude checks")
    cases = (
        (2, 0.5, np.array([0.0, 0.0]), np.array([np.pi / 2, 0.0])),
        (
            3,
            0.0,
            np.array([np.pi / 2, 0.0, 0.0]),
            np.array([0.0, np.pi / 2, 0.0]),
        ),
    )
    for d, mass, k1, k2 in cases:
        for interaction in ("nn", "cube"):
            model = Stag(d, mass, interaction)
            label1, u1 = sector_ordered_positive_frame(model, k1)
            label2, u2 = sector_ordered_positive_frame(model, k2)
            vertex = model.W((k1, k2, k1, k2), (u1, u2, u1, u2))
            norms = []
            for z in (-1, 1):
                i = np.where(np.isclose(label1, z))[0]
                j = np.where(np.isclose(label2, z))[0]
                norms.append(np.linalg.norm(vertex[np.ix_(i, j, i, j)]) ** 2)
            print(
                f"d={d} m={mass:g} {interaction}: same-sector forward "
                f"squared Frobenius norms={norms}"
            )


def direct_svd(model, radius, processes, sector_name, seed):
    rng = np.random.default_rng(seed)
    full, odd, even = basis(model.d, radius)
    sector = odd if sector_name == "odd" else even
    nk = int(3 * len(sector) / (2 * model.D**2)) + 20
    q, block_sv = block_map_Q(model, full, sector, rng, nk)
    rows = []
    wnorm = []
    for process in processes:
        a, wn = residual_rows(model, process, full, sector)
        rows.append(a @ q)
        wnorm.append(wn)
    a = np.vstack(rows)
    sv = np.linalg.svd(a, compute_uv=False) / np.sqrt(len(processes))
    return sv, q.shape[1], np.asarray(wnorm), block_sv


def null_counts(sv):
    return {
        "worker": int(np.sum(sv < 1e-8 + 1e-9 * sv[0])),
        "abs1e-6": int(np.sum(sv < 1e-6)),
        "abs1e-10": int(np.sum(sv < 1e-10)),
    }


def fresh_processes(model, rng, generic, special_each):
    processes = sample_processes(model, generic, ALLCH, rng)
    for total_k in (
        np.zeros(model.d),
        np.full(model.d, np.pi / 2),
        np.array([np.pi / 2] + [0] * (model.d - 1)),
    ):
        processes += sample_processes(
            model, special_each, ALLCH, rng, special=total_k
        )
    return processes


def direct_nullspace_checks():
    print("\n== direct full-matrix SVD checks (fresh seed, no TSQR)")
    rng = np.random.default_rng(927341)
    case_id = 0
    for d, radius, generic, special_each in ((2, 2, 260, 45), (3, 1, 110, 20)):
        for inter in ("nn", "cube"):
            for mass in (0.5, 0.0):
                case_id += 1
                model = Stag(d, mass, inter)
                processes = fresh_processes(model, rng, generic, special_each)
                channels = {p[0] for p in processes}
                residual = max(
                    abs(
                        p[0][0] * model.omega(p[1])[0]
                        + p[0][1] * model.omega(p[2])[0]
                        - p[0][2] * model.omega(p[3])[0]
                        - p[0][3] * model.omega(p[4])[0]
                    )
                    for p in processes
                )
                for sector in ("odd", "even"):
                    sv, ncol, wnorm, block_sv = direct_svd(
                        model, radius, processes, sector, 1000 + case_id
                    )
                    counts = null_counts(sv)
                    nullity = counts["worker"]
                    gap = sv[-nullity - 1] if nullity else sv[-1]
                    largest_null = sv[-1] if nullity else np.nan
                    print(
                        f"d={d} {inter} m={mass:g} R={radius} {sector}: "
                        f"nproc={len(processes)} channels={len(channels)}/16 "
                        f"eres={residual:.2e} cols={ncol} null={counts} "
                        f"svmax={sv[0]:.6e} gap={gap:.6e} ratio={gap/sv[0]:.3e} "
                        f"largest_null={largest_null:.3e} Wzero={np.mean(wnorm<1e-8):.3f} "
                        f"blockmap_tail={block_sv[-1]:.3e}"
                    )

    # Free and one-dimensional controls, including deliberately fixed total K.
    free = Stag(2, 0.5, "zero")
    procs = fresh_processes(free, rng, 80, 15)
    sv, ncol, _, _ = direct_svd(free, 2, procs, "odd", 2991)
    print(
        f"free d=2 R=2 odd: cols={ncol} null={null_counts(sv)} svmax={sv[0]:.3e}"
    )
    for mass in (0.0, 0.5):
        one = Stag(1, mass, "nn")
        procs = fresh_processes(one, rng, 300, 80)
        sv, ncol, wnorm, _ = direct_svd(one, 8, procs, "odd", 3010 + int(10 * mass))
        print(
            f"1D nn m={mass:g} R=8 odd: cols={ncol} null={null_counts(sv)} "
            f"svmax={sv[0]:.6e} gap/nonzero-tail={sv[max(0,ncol-null_counts(sv)['worker']-1)]:.6e} "
            f"Wzero={np.mean(wnorm<1e-8):.3f}"
        )

    band_changing = [s for s in ALLCH if s[0] + s[1] != s[2] + s[3]]
    for mass in (0.0, 0.5):
        model = Stag(3, mass, "nn")
        got = sample_processes(model, 20, band_changing, rng, ball=0.5)
        print(
            f"deliberate d=3 nn m={mass:g} low-ball band-changing target=20 found={len(got)}"
        )
    probe = Stag(3, 0.5, "nn")
    special_cases = (
        ("K=0 e-h flat", np.zeros(3), [(1, -1, 1, -1)]),
        ("K=(pi/2,pi/2,pi/2)", np.full(3, np.pi / 2), ALLCH),
        ("K=(pi/2,0,0)", np.array([np.pi / 2, 0.0, 0.0]), ALLCH),
    )
    for name, total_k, channels in special_cases:
        got = sample_processes(probe, 30, channels, rng, special=total_k)
        residual = max(
            abs(
                p[0][0] * probe.omega(p[1])[0]
                + p[0][1] * probe.omega(p[2])[0]
                - p[0][2] * probe.omega(p[3])[0]
                - p[0][3] * probe.omega(p[4])[0]
            )
            for p in got
        )
        print(
            f"deliberate d=3 nn m=0.5 {name}: found={len(got)} "
            f"channels={len({p[0] for p in got})} max_eres={residual:.2e}"
        )


def group_indices(values, tolerance):
    order = np.argsort(values)
    groups = []
    start = 0
    while start < len(order):
        end = start + 1
        while end < len(order) and abs(values[order[end]] - values[order[start]]) < tolerance:
            end += 1
        groups.append(order[start:end])
        start = end
    return groups


def cluster_first_order_limit():
    print("\n== independent 6x6, N=2 commutant-distance check")
    # Import only the submitted Fock-basis utilities; construct the perturbative
    # projection independently rather than diagonalizing H0+V Hint at small V.
    from s1_cluster_ed import diag_int, fock, nn_pairs, one_body, second_quant

    lx = ly = 6
    sites, pos, h, p1 = one_body(lx, ly, 0.5)
    states, fpos = fock(len(sites), 2)
    h0 = second_quant(h, states, fpos, len(sites))
    p = second_quant(p1, states, fpos, len(sites))
    hint = diag_int(nn_pairs(lx, ly, sites, pos, "nn"), states)
    e0, u0 = np.linalg.eigh(h0)
    pv = u0.conj().T @ p @ u0
    bv = u0.conj().T @ hint @ u0
    comm = bv @ pv - pv @ bv
    same0 = np.abs(e0[:, None] - e0[None, :]) < 1e-9
    onshell = np.where(same0, comm, 0)

    removed_sq = 0.0
    for g in group_indices(e0, 1e-9):
        b = bv[np.ix_(g, g)]
        pg = pv[np.ix_(g, g)]
        beta, v = np.linalg.eigh(b)
        p_beta = v.conj().T @ pg @ v
        same_beta = np.abs(beta[:, None] - beta[None, :]) < 1e-9
        removed_sq += np.linalg.norm(np.where(same_beta, 0, p_beta)) ** 2
    limit = np.sqrt(removed_sq) / np.linalg.norm(p)
    print(
        f"dim={len(states)} on-shell ||[Hint,P]||op={np.linalg.norm(onshell,2):.12f} "
        f"F={np.linalg.norm(onshell):.12f}; first-order dephasing HS lower bound={limit:.12f}"
    )
    for coupling in (1e-5, 1e-4, 1e-3):
        energy, vectors = np.linalg.eigh(h0 + coupling * hint)
        p_exact = vectors.conj().T @ p @ vectors
        # The smallest relevant splitting here is O(V^2); 1e-12 keeps exact
        # symmetry degeneracies while resolving it at V=1e-5.
        same = np.abs(energy[:, None] - energy[None, :]) < 1e-12
        distance = np.linalg.norm(np.where(same, 0, p_exact)) / np.linalg.norm(p)
        print(f"V={coupling:.0e}: exact-commutant HS distance={distance:.12f}")


if __name__ == "__main__":
    independent_one_particle_checks()
    forward_amplitude_checks()
    direct_nullspace_checks()
    cluster_first_order_limit()
