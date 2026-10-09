"""Independent, non-mutating checks for the W1 referee report."""
import itertools

import numpy as np

import w1_geom as wg
import w1_lib
from w1_lib import E_parts, S0, VEC, fermion_G, lengths_metric, photon_modes_w1


def circumcenter(T):
    """Euclidean circumcenter of one tetrahedron."""
    A = 2.0 * (T[1:] - T[0])
    b = np.sum(T[1:] ** 2, axis=1) - np.sum(T[0] ** 2)
    return np.linalg.solve(A, b)


def geometry_checks():
    centers = np.array([circumcenter(T) for T in wg.TETS])
    cell = wg.build_cell(S0)
    metric = np.array([[1.2, 0.11, -0.07], [0.11, 0.9, 0.08], [-0.07, 0.08, 1.1]])
    squared_lengths = np.array([v @ metric @ v for v in VEC])
    metric_errors, metric_volumes = [], []
    for T in wg.TETS:
        Lam, volume, _ = wg.tet_geometry(T, squared_lengths)
        metric_errors.append(np.max(np.abs(Lam @ Lam - metric)))
        metric_volumes.append(volume)
    Q = np.array([[0.173, 0.271, 0.319], [1.2, 2.1, 0.7]])
    M1, M2, D1, D0 = wg.bloch(cell, Q)
    chain = np.max(np.abs(np.einsum("nij,nj->ni", D1, D0)))
    herm = max(
        np.max(np.abs(M1 - np.conj(M1.swapaxes(1, 2)))),
        np.max(np.abs(M2 - np.conj(M2.swapaxes(1, 2)))),
    )
    mineig = min(np.linalg.eigvalsh(M1).min(), np.linalg.eigvalsh(M2).min())
    continuum_symbol = fermion_G(cell) @ VEC
    assert np.max(np.abs(centers - 0.5)) < 1e-14
    assert max(metric_errors) < 1e-14
    assert abs(sum(metric_volumes) - np.sqrt(np.linalg.det(metric))) < 1e-14
    assert chain < 1e-14 and herm < 1e-14 and mineig > 0
    assert np.max(np.abs(continuum_symbol - np.eye(3))) < 1e-14
    print("circumcenters", centers[0], "spread", np.ptp(centers, axis=0))
    print("constant-metric reconstruction", max(metric_errors), "cell volume", sum(metric_volumes))
    print("cell volume", cell["V"], "chain", chain, "Hermitian", herm, "min Hodge eig", mineig)
    print("linear fermion symbol G@V\n", continuum_symbol)


def photon_ir_check():
    cell = wg.build_cell(S0)
    q = np.array([[0.01, 0.007, -0.004]])
    omega, _, _ = photon_modes_w1(cell, q)
    ratio = omega[0, :2] ** 2 / np.sum(q[0] ** 2)
    print("photon omega^2", omega[0] ** 2)
    print("gapless omega^2/q^2", ratio)


def fermion_node_check():
    """Exhibit 18 exact simple zeros of the undeformed P1 symbol."""
    G = fermion_G(wg.build_cell(S0))
    nodes = []
    # Eight reciprocal-lattice time-reversal-invariant momenta.
    nodes.extend(np.array(p, float) for p in itertools.product((0.0, -np.pi), repeat=3))
    # Eight further zeros: equal-sign 2pi/3 in any two or all three slots.
    for sign in (-1.0, 1.0):
        a = sign * 2.0 * np.pi / 3.0
        nodes.extend((np.array([a, a, 0.0]), np.array([a, 0.0, a]), np.array([0.0, a, a]), np.array([a, a, a])))
    # The pair mentioned in the worker summary.
    nodes.extend((np.full(3, -np.pi / 2.0), np.full(3, np.pi / 2.0)))
    residuals, determinants = [], []
    for p in nodes:
        residuals.append(np.linalg.norm(G @ np.sin(VEC @ p)))
        J = G @ (np.cos(VEC @ p)[:, None] * VEC)
        determinants.append(np.linalg.det(J))
    assert len(nodes) == 18
    assert max(residuals) < 1e-14
    assert min(np.abs(determinants)) > 1e-3
    print("exhibited fermion nodes", len(nodes), "max residual", max(residuals))
    print("minimum |det velocity Jacobian|", min(np.abs(determinants)))


def d5_second(E, eps, h):
    vals = {j: E(eps, j * h) for j in (-2, -1, 0, 1, 2)}
    return (-vals[2] + 16 * vals[1] - 30 * vals[0] + 16 * vals[-1] - vals[-2]) / (12 * h * h)


def direct_geodesic_check(L=12):
    """Direct five-point derivatives, bypassing run_hess/analyze2."""
    r2 = 1.0 / np.sqrt(2.0)
    Ed = np.diag([r2, -r2, 0.0])
    # Same S3-E orientation paired with Ed in out_summary_w1.txt.
    Eo = np.array([[0.0, 0.0, 0.5], [0.0, 0.0, -0.5], [0.5, -0.5, 0.0]])
    cache = {}

    def energy(eps, t):
        key = (tuple(eps.ravel()), t)
        if key not in cache:
            cache[key] = E_parts(L, lengths_metric(eps, t, "exp"))["tot"]
        return cache[key]

    for h in (0.05, 0.025):
        a = d5_second(energy, Ed, h)
        b = d5_second(energy, Eo, h)
        ab = (d5_second(energy, Ed + Eo, h) - a - b) / 2.0
        block = np.array([[a, ab], [ab, b]])
        print("direct L", L, "h", h, "E block\n", block, "eigs", np.linalg.eigvalsh(block))


def cached_hessian_breakdown(L=24):
    """Separate fermion/photon O(e^0) geodesic Hessians in the cached data."""
    z = np.load(f"hess_L{L}.npz")
    r2, r6 = 1.0 / np.sqrt(2.0), 1.0 / np.sqrt(6.0)
    basis = [np.diag([r2, -r2, 0]), np.diag([r6, r6, -2 * r6])]
    for i, j in ((0, 1), (0, 2), (1, 2)):
        m = np.zeros((3, 3))
        m[i, j] = m[j, i] = r2
        basis.append(m)

    def coords(m):
        return np.array([m[0, 0], m[1, 1], m[2, 2], np.sqrt(2) * m[0, 1], np.sqrt(2) * m[0, 2], np.sqrt(2) * m[1, 2], 0.0])

    def spectrum(columns):
        H = z["H"][:, :, columns].sum(2)
        grad = z["grad"][:, columns].sum(1)
        M = np.array([[coords(a) @ H @ coords(b) + grad @ coords((a @ b + b @ a) / 2) for b in basis] for a in basis])
        return np.linalg.eigvalsh(M)

    print("cached O(e0) fermion eigs", spectrum([0]))
    print("cached O(e0) photon eigs", spectrum([1]))
    print("cached O(e0) total eigs", spectrum([0, 1]))
    print("cached O(e2) total eigs", spectrum([5]))


def two_lowest_photon_band_diagnostic(L=12, h=0.025):
    """Diagnostic only: omit the four gapped bands, without calling this a local alternative Hodge."""
    original = w1_lib.photon_modes_w1

    def lowest_two(cell, Q):
        omega, amplitude, coulomb = original(cell, Q)
        return omega[:, :2], amplitude[:, :2], coulomb

    w1_lib.photon_modes_w1 = lowest_two
    r2 = 1.0 / np.sqrt(2.0)
    Ed = np.diag([r2, -r2, 0.0])
    Eo = np.array([[0.0, 0.0, 0.5], [0.0, 0.0, -0.5], [0.5, -0.5, 0.0]])
    cache = {}

    def energy(eps, t, key):
        cache_key = (tuple(eps.ravel()), t)
        if cache_key not in cache:
            cache[cache_key] = E_parts(L, lengths_metric(eps, t, "exp"))
        return cache[cache_key][key]

    def block(key):
        derivative = lambda eps: d5_second(lambda e, t: energy(e, t, key), eps, h)
        a, b = derivative(Ed), derivative(Eo)
        ab = (derivative(Ed + Eo) - a - b) / 2.0
        return np.array([[a, ab], [ab, b]])

    try:
        photon = block("free_g")
        interaction = block("tot")
    finally:
        w1_lib.photon_modes_w1 = original
    print("two-lowest-band O(e0) photon E block eigs", np.linalg.eigvalsh(photon))
    print("two-lowest-band O(e2) E block eigs", np.linalg.eigvalsh(interaction))


def continuum_window_check():
    """Analytic small-K0 coefficient for a fixed isotropic coordinate-momentum Gaussian."""
    # For tr(eps)=0, tr(eps^2)=1: <d^2 |exp(t eps/2) k|/dt^2>_angles = 2|k|/15.
    # Also integral d^3k/(2pi)^3 |k| exp(-k^2/K0^2) = K0^4/(4pi^2).
    fixed = -1.0 / (60.0 * np.pi ** 2)
    moving = 0.0  # exact after k_proper = exp(t eps/2) k and det(exp(t eps/2))=1.
    print("continuum d2E/K0^4 fixed-index", fixed, "proper-moving", moving)


if __name__ == "__main__":
    geometry_checks()
    photon_ir_check()
    fermion_node_check()
    direct_geodesic_check()
    cached_hessian_breakdown()
    two_lowest_photon_band_diagnostic()
    continuum_window_check()
