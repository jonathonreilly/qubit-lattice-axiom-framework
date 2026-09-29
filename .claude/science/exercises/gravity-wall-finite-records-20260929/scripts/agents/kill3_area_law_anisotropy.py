"""Kill-round check for F4: is the area-law coefficient of a cubic-lattice free-fermion sea a
constant times the Euclidean area?  Jacobson's derivation needs delta S = eta * delta A with one
eta for every orientation of the entangling surface.  Stand-in for the walker's Dirac sea:
4-component Wilson-Dirac fermion on Z^3, h(k) = sum_i sin k_i alpha_i + [m + r sum_i (1-cos k_i)] beta,
lower band filled.  Slab entanglement per unit area for cuts normal to (100) and (110), by the
Peschel correlation-matrix method with transverse momenta as good quantum numbers.
"""
import numpy as np
from numpy.linalg import eigh

sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1.0, -1.0]).astype(complex)
I2 = np.eye(2, dtype=complex)
alpha = [np.kron(sx, s) for s in (sx, sy, sz)]
beta = np.kron(sz, I2)


def hop(i, r):
    # T_i such that T_i e^{ik} + T_i^dag e^{-ik} = sin k alpha_i - r cos k beta
    return -0.5j * alpha[i] - 0.5 * r * beta


def chain_entropy(onsite, M, L, ell, mu=0.0):
    """Periodic chain of L cells (4 orbitals), forward hop matrix M (cell n -> n+1), on-site 'onsite'.
    Entanglement entropy of ell consecutive cells (two cuts) in the state with all E<mu filled."""
    d = 4
    H = np.zeros((d * L, d * L), complex)
    for n in range(L):
        H[d*n:d*n+d, d*n:d*n+d] = onsite
        m = (n + 1) % L
        H[d*m:d*m+d, d*n:d*n+d] += M
        H[d*n:d*n+d, d*m:d*m+d] += M.conj().T
    E, V = eigh(H)
    occ = V[:, E < mu]
    C = occ @ occ.conj().T
    CA = C[:d*ell, :d*ell]
    nu = np.clip(eigh(CA)[0].real, 1e-14, 1 - 1e-14)
    return float(-np.sum(nu * np.log(nu) + (1 - nu) * np.log(1 - nu)))


def slab_entropy_per_area(orientation, m, r, L, ell, Nk):
    """Entropy per unit Euclidean area of ONE cut (slab has two)."""
    Tx, Ty, Tz = (hop(i, r) for i in range(3))
    tot = 0.0
    if orientation == '100':
        ks = 2 * np.pi * np.arange(Nk) / Nk
        for ky in ks:
            for kz in ks:
                onsite = (m + 3 * r) * beta + (np.sin(ky) * alpha[1] - r * np.cos(ky) * beta) + (np.sin(kz) * alpha[2] - r * np.cos(kz) * beta)
                tot += chain_entropy(onsite, Tx, L, ell)
        area_per_site = 1.0
    elif orientation == '110':
        # layers n = x + y; in-layer coordinate u = x - y (spacing 2 -> BZ width pi), z
        ku_s = np.pi * np.arange(Nk) / Nk
        kz_s = 2 * np.pi * np.arange(Nk) / Nk
        for ku in ku_s:
            for kz in kz_s:
                onsite = (m + 3 * r) * beta + (np.sin(kz) * alpha[2] - r * np.cos(kz) * beta)
                M = np.exp(-1j * ku) * Tx + np.exp(1j * ku) * Ty
                tot += chain_entropy(onsite, M, L, ell)
        area_per_site = np.sqrt(2.0)
    else:
        raise ValueError
    return tot / (Nk * Nk * area_per_site) / 2.0


def band_check(m, r):
    """Spot-check the (110) chain reduction against the bulk bands."""
    Tx, Ty, Tz = (hop(i, r) for i in range(3))
    ku, kz, kn = 0.37, 1.1, 0.81
    onsite = (m + 3 * r) * beta + (np.sin(kz) * alpha[2] - r * np.cos(kz) * beta)
    M = np.exp(-1j * ku) * Tx + np.exp(1j * ku) * Ty
    Hk = onsite + M * np.exp(1j * kn) + M.conj().T * np.exp(-1j * kn)
    e_chain = np.sort(eigh(Hk)[0])
    kx, ky = kn - ku, kn + ku
    d = [np.sin(kx), np.sin(ky), np.sin(kz)]
    Mk = m + r * (3 - np.cos(kx) - np.cos(ky) - np.cos(kz))
    e_bulk = np.sort(np.array([-1, -1, 1, 1]) * np.sqrt(sum(di**2 for di in d) + Mk**2))
    return np.max(np.abs(e_chain - e_bulk))


if __name__ == '__main__':
    r = 1.0
    print("band check (110) reduction vs bulk, max |dE| =", f"{band_check(0.3, r):.2e}")
    L, Nk = 40, 40
    for m in (0.5, 0.1, 0.0):
        row = []
        for ell in (10, 20):
            s100 = slab_entropy_per_area('100', m, r, L, ell, Nk)
            s110 = slab_entropy_per_area('110', m, r, L, ell, Nk)
            row.append((ell, s100, s110, s110 / s100))
        for ell, s100, s110, ratio in row:
            print(f"m={m:.1f} r={r} L={L} ell={ell}: S/A (100) = {s100:.4f}   S/A (110) = {s110:.4f}   ratio (110)/(100) = {ratio:.3f}")
