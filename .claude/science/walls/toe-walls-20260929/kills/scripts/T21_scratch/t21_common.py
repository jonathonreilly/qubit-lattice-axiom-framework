"""Shared code for the T21 tests: record gas <-> Ising, Wolff sampler, walker Hamiltonian."""
import numpy as np
from numba import njit

# ---------------------------------------------------------------- lattice helpers
def eps_array(L):
    x, y, z = np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing="ij")
    return ((-1.0) ** (x + y + z)).astype(np.int8).ravel()  # index = (x*L+y)*L+z


@njit(cache=True)
def neighbours(L):
    N = L * L * L
    nb = np.empty((N, 6), dtype=np.int64)
    for x in range(L):
        for y in range(L):
            for z in range(L):
                i = (x * L + y) * L + z
                nb[i, 0] = (((x + 1) % L) * L + y) * L + z
                nb[i, 1] = (((x - 1) % L) * L + y) * L + z
                nb[i, 2] = (x * L + (y + 1) % L) * L + z
                nb[i, 3] = (x * L + (y - 1) % L) * L + z
                nb[i, 4] = (x * L + y) * L + (z + 1) % L
                nb[i, 5] = (x * L + y) * L + (z - 1) % L
    return nb


# ---------------------------------------------------------------- Wolff (ferromagnet in sigma = eps*s)
# Record gas at zeta = g^-3: weight g^(#equal-occupancy bonds / 2).  With s = 2n-1 and sigma_x = eps_x s_x,
# an equal-occupancy bond has sigma_x sigma_y = -1... see t21_A.py for the exact check.  Bonds with
# sigma_x == sigma_y are the "like" (mixed-occupancy) bonds and get relative weight 1; bonds with
# sigma_x != sigma_y get g^(1/2).  So this is a FERROMAGNETIC Ising model in sigma with K_F = ln(1/g)/4.
@njit(cache=True)
def wolff_steps(sig, nb, pbond, nsteps, seed_state):
    N = sig.shape[0]
    stack = np.empty(N, dtype=np.int64)
    inclus = np.zeros(N, dtype=np.uint8)
    tot = 0
    for _ in range(nsteps):
        seed = np.random.randint(0, N)
        s0 = sig[seed]
        sp = 0
        stack[sp] = seed
        sp += 1
        inclus[seed] = 1
        cnt = 1
        members = 0
        while sp > 0:
            sp -= 1
            i = stack[sp]
            for k in range(6):
                j = nb[i, k]
                if inclus[j] == 0 and sig[j] == s0 and np.random.random() < pbond:
                    inclus[j] = 1
                    stack[sp] = j
                    sp += 1
                    cnt += 1
        for i in range(N):
            if inclus[i] == 1:
                sig[i] = -sig[i]
                inclus[i] = 0
        tot += cnt
    return tot


@njit(cache=True)
def seed_numba(s):
    np.random.seed(s)


@njit(cache=True)
def metropolis_sweeps(sig, nb, K, nsweeps):
    """single-spin Metropolis in sigma with weight exp(K sum sigma_i sigma_j), K>0."""
    N = sig.shape[0]
    for _ in range(nsweeps):
        for _i in range(N):
            i = np.random.randint(0, N)
            h = 0
            for k in range(6):
                h += sig[nb[i, k]]
            dE = 2.0 * K * sig[i] * h  # ln(w_old/w_new)
            if dE <= 0 or np.random.random() < np.exp(-dE):
                sig[i] = -sig[i]


def binder_run(L, g, ntherm, nmeas, gap=1, seed=1):
    """Wolff run; returns <|M|>, <M^2>, <M^4>."""
    seed_numba(seed)
    nb = neighbours(L)
    N = L ** 3
    K = np.log(1.0 / g) / 4.0
    pbond = 1.0 - np.exp(-2.0 * K)
    sig = np.ones(N, dtype=np.int8)  # start ordered (A-chessboard)
    wolff_steps(sig, nb, pbond, ntherm, 0)
    m1 = m2 = m4 = 0.0
    for _ in range(nmeas):
        wolff_steps(sig, nb, pbond, gap, 0)
        m = sig.sum() / N
        m1 += abs(m)
        m2 += m * m
        m4 += m ** 4
    return m1 / nmeas, m2 / nmeas, m4 / nmeas


# ---------------------------------------------------------------- walker
def walker_H0(L):
    """H = sum_j sigma_j (x) S_j, S_j = (T_j - T_j^*)/(2i) on the L^3 torus; returns dense (2N,2N) complex."""
    N = L ** 3
    nb = neighbours(L)
    sig = [np.array([[0, 1], [1, 0]], complex),
           np.array([[0, -1j], [1j, 0]], complex),
           np.array([[1, 0], [0, -1]], complex)]
    H = np.zeros((2 * N, 2 * N), complex)
    for j in range(3):
        fwd = nb[:, 2 * j]      # T_j: (T psi)(x) = psi(x+e)
        bwd = nb[:, 2 * j + 1]
        S = np.zeros((N, N), complex)
        idx = np.arange(N)
        S[idx, fwd] += 1.0 / (2j)
        S[idx, bwd] -= 1.0 / (2j)
        H += np.kron(S, sig[j])  # ordering: index = 2*site + coin
    return H


def spectrum(H0, n_occ, c):
    """eigenvalues of H0 + c*diag(n) (n on sites, both coin states)."""
    d = np.repeat(n_occ.astype(float), 2) * c
    H = H0 + np.diag(d)
    return np.linalg.eigvalsh(H)


def gap_metrics(E, c):
    """largest empty interval / c ; fraction of eigenvalues in (0.1c, 0.9c); min |E - c/2|."""
    E = np.sort(E)
    gaps = np.diff(E)
    wmax = gaps.max()
    f_in = np.mean((E > 0.1 * c) & (E < 0.9 * c))
    dmin = np.min(np.abs(E - 0.5 * c))
    return wmax / c, f_in, dmin
