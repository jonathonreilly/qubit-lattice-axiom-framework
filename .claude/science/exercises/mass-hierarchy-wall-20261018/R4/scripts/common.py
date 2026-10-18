"""Shared data and null models for R4 tests (comparators only)."""
import numpy as np

LN3 = np.log(3.0)

# MZ set (GeV), order within sector: light, middle, heavy
MZ = {
    "u": np.array([1.38e-3, 0.638, 172.1]),
    "d": np.array([2.82e-3, 0.057, 2.86]),
    "e": np.array([0.4866e-3, 0.10272, 1.7462]),
}
LOW = {
    "u": np.array([2.16e-3, 1.27, 172.69]),
    "d": np.array([4.67e-3, 0.0934, 4.18]),
    "e": np.array([0.51099895e-3, 0.1056583755, 1.77686]),
}
CKM = np.array([0.2243, 0.0410, 0.00382])  # Vus, Vcb, Vub
SECTORS = ("u", "d", "e")

# lattice-fixed numbers used on main (g_bare = 1, <P> at beta = 6)
P_PLAQ = 0.5934
U0 = P_PLAQ ** 0.25
ALPHA_BARE = 1.0 / (4.0 * np.pi)
ALPHA_LM = ALPHA_BARE / U0
ALPHA_SV = ALPHA_BARE / U0 ** 2


def null_N1(rng, n):
    """n x 3 sectors x 3 masses, iid log-uniform on [m_e, m_t], sorted per sector."""
    lo, hi = np.log(MZ["e"][0]), np.log(MZ["u"][2])
    y = rng.uniform(lo, hi, size=(n, 3, 3))
    y.sort(axis=2)
    return y  # log masses


def null_N2(rng, n, data=MZ):
    """heaviest fixed at observed; two lighter log-uniform on [1e-6,1] x heaviest."""
    out = np.empty((n, 3, 3))
    for s, key in enumerate(SECTORS):
        y3 = np.log(data[key][2])
        lt = rng.uniform(np.log(1e-6), 0.0, size=(n, 2))
        lt.sort(axis=1)
        out[:, s, 0] = y3 + lt[:, 0]
        out[:, s, 1] = y3 + lt[:, 1]
        out[:, s, 2] = y3
    return out


def obs_logs(data=MZ):
    return np.array([np.log(data[k]) for k in SECTORS])  # 3 x 3
