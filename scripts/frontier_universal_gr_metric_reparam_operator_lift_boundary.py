"""Finite-lattice checks for the metric-reparametrized GR stress vertex.

The runner supports a narrow bounded statement:

* the metric-reparametrized momentum argument D(P_eff) has first variation
  matching the conserved velocity-times-momentum vertex used by the stress-Ward
  packet;
* the naive hop-amplitude/vielbein coupling has shear first variation matching
  the bare-sigma shear vertex, not the conserved vertex;
* a selected clean operator-proportionality lift of the cubic contact fails
  across sampled loop momenta.

It does not prove a unique all-orders coupling, a loop-integrated cubic Ward
identity, a continuum limit, or an Einstein-Hilbert normalization.
"""

from __future__ import annotations

import numpy as np
from scipy.linalg import sqrtm

AUDIT_TIMEOUT_SEC = 360

SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)
SIGMA = [SX, SY, SZ]
I2 = np.eye(2, dtype=complex)

results: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    results.append((name, bool(ok)))


def velocity(q: np.ndarray, k: np.ndarray, i: int) -> np.ndarray:
    return 1j * SIGMA[i] * np.cos(q[i] + k[i] / 2)


def midpoint_sine(q: np.ndarray, k: np.ndarray, j: int) -> float:
    return 0.5 * (np.sin(q[j]) + np.sin(q[j] + k[j]))


def conserved_vertex(q: np.ndarray, k: np.ndarray, i: int, j: int) -> np.ndarray:
    return 0.5 * (
        velocity(q, k, i) * midpoint_sine(q, k, j)
        + velocity(q, k, j) * midpoint_sine(q, k, i)
    )


def naive_shear_vertex(q: np.ndarray, k: np.ndarray, i: int, j: int) -> np.ndarray:
    return 0.5 * (
        SIGMA[i] * midpoint_sine(q, k, j)
        + SIGMA[j] * midpoint_sine(q, k, i)
    ) * 1j


def build_lattice(length: int):
    sites = [(x, y, z) for x in range(length) for y in range(length) for z in range(length)]
    site_index = {site: idx for idx, site in enumerate(sites)}
    n_sites = len(sites)
    shifts = []
    for axis in range(3):
        shift = np.zeros((n_sites, n_sites), complex)
        for site in sites:
            neighbor = list(site)
            neighbor[axis] = (neighbor[axis] + 1) % length
            shift[site_index[site], site_index[tuple(neighbor)]] = 1.0
        shifts.append(shift)
    return sites, site_index, n_sites, shifts


def jord(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return 0.5 * (left @ right + right @ left)


def conserved_operator(length: int, mass: float, metric_fn, context) -> np.ndarray:
    """Momentum-argument reparametrization D(P_eff), expanded to second order."""

    sites, site_index, n_sites, shifts = context
    lattice_momenta = [(1 / (2j)) * (shifts[a] - shifts[a].conj().T) for a in range(3)]
    cosine_hops = [0.5 * (shifts[a] + shifts[a].conj().T) for a in range(3)]
    w_matrix = np.zeros((3, 3, n_sites), complex)
    for site in sites:
        w_matrix[:, :, site_index[site]] = sqrtm(np.eye(3) + metric_fn(site)) - np.eye(3)

    def delta(axis: int) -> np.ndarray:
        out = np.zeros((n_sites, n_sites), complex)
        for b in range(3):
            out += jord(np.diag(w_matrix[axis, b]), lattice_momenta[b])
        return out

    operator = np.zeros((2 * n_sites, 2 * n_sites), complex)
    for site in sites:
        idx = site_index[site]
        operator[2 * idx : 2 * idx + 2, 2 * idx : 2 * idx + 2] += mass * I2
    for axis in range(3):
        d_axis = delta(axis)
        spatial = (
            lattice_momenta[axis]
            + jord(cosine_hops[axis], d_axis)
            - 0.5 * jord(lattice_momenta[axis], jord(d_axis, d_axis))
        )
        block_coeffs = 1j * spatial
        for site in sites:
            site_row = block_coeffs[site_index[site]]
            for target in np.nonzero(np.abs(site_row) > 1e-14)[0]:
                row = slice(2 * site_index[site], 2 * site_index[site] + 2)
                col = slice(2 * target, 2 * target + 2)
                operator[row, col] += SIGMA[axis] * site_row[target]
    return operator


def naive_hop_operator(length: int, mass: float, metric_fn, context) -> np.ndarray:
    """Naive hop-amplitude/vielbein coupling used as a contrast control."""

    sites, site_index, n_sites, _ = context
    vielbein = {site: np.real(sqrtm(np.eye(3) + metric_fn(site))) for site in sites}
    operator = np.zeros((2 * n_sites, 2 * n_sites), complex)
    for site in sites:
        idx = site_index[site]
        operator[2 * idx : 2 * idx + 2, 2 * idx : 2 * idx + 2] += mass * I2
        for hop_axis in range(3):
            plus = list(site)
            plus[hop_axis] = (plus[hop_axis] + 1) % length
            plus = tuple(plus)
            minus = list(site)
            minus[hop_axis] = (minus[hop_axis] - 1) % length
            minus = tuple(minus)
            for frame_axis in range(3):
                e_plus = 0.5 * (
                    vielbein[site][frame_axis, hop_axis]
                    + vielbein[plus][frame_axis, hop_axis]
                )
                e_minus = 0.5 * (
                    vielbein[site][frame_axis, hop_axis]
                    + vielbein[minus][frame_axis, hop_axis]
                )
                row = slice(2 * idx, 2 * idx + 2)
                col_plus = slice(2 * site_index[plus], 2 * site_index[plus] + 2)
                col_minus = slice(2 * site_index[minus], 2 * site_index[minus] + 2)
                operator[row, col_plus] += 0.5 * SIGMA[frame_axis] * e_plus
                operator[row, col_minus] += -0.5 * SIGMA[frame_axis] * e_minus
    return operator


def project(operator: np.ndarray, q_in: np.ndarray, q_out: np.ndarray, context) -> np.ndarray:
    sites, site_index, n_sites, _ = context
    out = np.zeros((2, 2), complex)
    for site in sites:
        row_block = operator[2 * site_index[site] : 2 * site_index[site] + 2]
        for target in sites:
            block = row_block[:, 2 * site_index[target] : 2 * site_index[target] + 2]
            if not np.any(np.abs(block) > 1e-13):
                continue
            out += (
                np.exp(-1j * q_out @ np.array(site))
                * np.exp(1j * q_in @ np.array(target))
                * block
            )
    return out / n_sites


def extract_vertex(operator_builder, length, mass, i, j, k_vec, q_vec, context, tau=1e-5):
    polarization = np.zeros((3, 3))
    polarization[i, j] = 1.0
    polarization[j, i] = polarization[i, j]
    if i == j:
        polarization[i, j] = 1.0

    def metric(sign: int):
        return lambda site: polarization * sign * tau * 2 * np.cos(k_vec @ np.array(site))

    derivative = (
        operator_builder(length, mass, metric(+1), context)
        - operator_builder(length, mass, metric(-1), context)
    ) / (2 * tau)
    return project(derivative, q_vec, q_vec + k_vec, context)


def check_first_variations() -> None:
    length = 6
    mass = 1.0
    context = build_lattice(length)
    k_vec = np.array([1, 0, 0]) * 2 * np.pi / length
    q_vec = np.array([1, 2, 1]) * 2 * np.pi / length

    conserved_err = 0.0
    for i, j in [(0, 0), (0, 1), (1, 2)]:
        extracted = extract_vertex(conserved_operator, length, mass, i, j, k_vec, q_vec, context)
        conserved_err = max(
            conserved_err,
            np.abs(extracted - conserved_vertex(q_vec, k_vec, i, j)).max(),
        )

    naive_err = 0.0
    distinct = 0.0
    for i, j in [(0, 1), (1, 2)]:
        extracted = extract_vertex(naive_hop_operator, length, mass, i, j, k_vec, q_vec, context)
        conserved = conserved_vertex(q_vec, k_vec, i, j)
        naive = naive_shear_vertex(q_vec, k_vec, i, j)
        naive_err = max(naive_err, np.abs(extracted - naive).max())
        distinct = max(distinct, np.abs(conserved - naive).max())

    assert abs(conserved_err) < 1e-3
    assert abs(naive_err) < 1e-3
    assert distinct > 0.1
    check(
        "conserved momentum-reparametrized first variation matches velocity-times-momentum vertex "
        f"(err={conserved_err:.1e})",
        conserved_err < 1e-3,
    )
    check(
        "naive hop-amplitude shear variation matches bare-sigma shear vertex "
        f"(err={naive_err:.1e}; distance from conserved={distinct:.2f})",
        naive_err < 1e-3 and distinct > 0.1,
    )


def extract_second_variation(length, mass, pol1, k1, pol2, k2, q_vec, context, tau=2e-3):
    def operator(a1, a2):
        return conserved_operator(
            length,
            mass,
            lambda site: (
                a1 * pol1 * 2 * np.cos(k1 @ np.array(site))
                + a2 * pol2 * 2 * np.cos(k2 @ np.array(site))
            ),
            context,
        )

    second = (
        operator(tau, tau)
        - operator(tau, -tau)
        - operator(-tau, tau)
        + operator(-tau, -tau)
    ) / (4 * tau * tau)
    return project(second, q_vec, q_vec + k1 + k2, context)


def check_selected_operator_lift_boundary() -> None:
    length = 6
    mass = 1.0
    context = build_lattice(length)
    k1 = np.array([1, 0, 0]) * 2 * np.pi / length
    k2 = np.array([0, 1, 0]) * 2 * np.pi / length
    xi = np.array([0.3, 1.0, 0.6])
    sine_k1 = np.array([2 * np.sin(k1[i] / 2) for i in range(3)])
    longitudinal_pol = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            longitudinal_pol[i, j] = sine_k1[i] * xi[j] + sine_k1[j] * xi[i]

    transverse_pol = np.zeros((3, 3))
    transverse_pol[0, 2] = transverse_pol[2, 0] = 1.0

    def polarized_vertex(q_val, k_val, polarization):
        out = np.zeros((2, 2), complex)
        for i in range(3):
            for j in range(3):
                if abs(polarization[i, j]) < 1e-15:
                    continue
                out += polarization[i, j] * conserved_vertex(q_val, k_val, i, j)
        return out

    ratios = []
    for q_index in [(1, 2, 1), (0, 3, 2), (1, 1, 1)]:
        q_vec = np.array(q_index) * 2 * np.pi / length
        second = extract_second_variation(
            length,
            mass,
            longitudinal_pol,
            k1,
            transverse_pol,
            k2,
            q_vec,
            context,
        )
        vertex_delta = 0.5 * (
            polarized_vertex(q_vec + k1, k2, transverse_pol)
            - polarized_vertex(q_vec, k2, transverse_pol)
        )
        if abs(vertex_delta[0, 1]) > 1e-6:
            ratios.append(second[0, 1] / vertex_delta[0, 1])

    spread = max(abs(r1 - r2) for r1 in ratios for r2 in ratios)
    assert abs(spread) > 0.1
    check(
        "selected clean operator-proportionality lift fails: second-variation "
        f"ratio is non-constant across sampled loop momenta (spread={spread:.2f})",
        spread > 0.1,
    )


check_first_variations()
check_selected_operator_lift_boundary()

pass_count = sum(1 for _, ok in results if ok)
fail_count = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("Finite-lattice verdict: the momentum-reparametrized coupling matches the")
print("conserved stress vertex at first variation; the naive hop-amplitude shear")
print("matches the bare-sigma shear vertex and differs from the conserved one;")
print("the tested clean operator-proportionality lift of the cubic contact fails.")
print("No loop-integrated Ward identity, continuum limit, uniqueness, or")
print("Einstein-Hilbert normalization is claimed.")
print(f"TOTAL: PASS={pass_count} FAIL={fail_count}")
if fail_count:
    raise SystemExit(1)
