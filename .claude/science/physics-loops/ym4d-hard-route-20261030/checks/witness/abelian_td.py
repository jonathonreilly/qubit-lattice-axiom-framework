#!/usr/bin/env python3
"""W5: reflected flux kernel of the abelian top-down Gaussian on a d = 3 torus.

Fine torus 9 x 9 x 18, blocks of side 3 (the map (B-1) with L = 3, d = 3), reflection t -> -t
through a site plane. On closed currents the free kernel is P(J, J') = J^T G J', G = (-Delta)^-1.
W := span of the coarse closed currents pulled back by Q^T, delta := P-orthogonal projection onto W.
The law with amplitude gamma_c on W and gamma_f on its P-orthogonal complement has kernel
  P_gamma = gamma_f^2 P + (gamma_c^2 - gamma_f^2) delta.
Its reflected kernel on currents in the open half-space must be positive semidefinite for RP.
"""
import itertools, json, os, resource, sys
import numpy as np

LIM = 2 * 1024**3


def guard():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != "darwin":
        rss *= 1024
    if rss > LIM:
        sys.exit("rss limit")


dims = (9, 9, 18)
L = 3
d = 3
N = np.prod(dims)
sid = lambda x: np.ravel_multi_index(tuple(np.mod(x, dims)), dims)


def bond(x, mu):
    return mu * N + sid(x)


nb = d * N
k = [2 * np.pi * np.fft.fftfreq(n) for n in dims]
lam = sum(np.meshgrid(*[4 * np.sin(q / 2) ** 2 for q in k], indexing="ij"))
lam.flat[0] = np.inf


def green(Jmat):
    """G applied to columns of Jmat (nb x m), per direction."""
    m = Jmat.shape[1]
    out = np.empty_like(Jmat)
    for c in range(m):
        for mu in range(d):
            f = Jmat[mu * N : (mu + 1) * N, c].reshape(dims)
            out[mu * N : (mu + 1) * N, c] = np.fft.ifftn(np.fft.fftn(f) / lam).real.ravel()
    return out


def plaquette(x, mu, nu):
    J = np.zeros(nb)
    ex = np.eye(d, dtype=int)
    J[bond(x, mu)] += 1
    J[bond(x + ex[mu], nu)] += 1
    J[bond(x + ex[nu], mu)] -= 1
    J[bond(x, nu)] -= 1
    return J


def reflect(J):
    """Theta on link currents: t -> -t, sending the link (x, t-direction) to its reversed image."""
    out = np.zeros_like(J)
    T = dims[2]
    for mu in range(d):
        f = J[mu * N : (mu + 1) * N].reshape(dims)
        if mu < 2:
            g = np.roll(f[:, :, ::-1], 1, axis=2)
            out[mu * N : (mu + 1) * N] = g.ravel()
        else:
            # link from t to t+1 maps to link from -t to -t-1, i.e. minus the link from -t-1 to -t
            g = -f[:, :, ::-1]
            out[mu * N : (mu + 1) * N] = g.ravel()
    return out


def Qtrans(Jc):
    """Q^T: pull a coarse link current (dict on coarse sites/dirs) back to the fine links."""
    out = np.zeros(nb)
    half = (L - 1) // 2
    w = L ** (-d)
    for (y, mu), v in Jc.items():
        for off in itertools.product(range(-half, half + 1), repeat=d):
            x = np.array(y) * L + np.array(off)
            for s in range(L):
                e = np.zeros(d, dtype=int)
                e[mu] = s
                out[bond(x + e, mu)] += v * w
    return out


def main():
    cd = tuple(n // L for n in dims)
    ex = np.eye(d, dtype=int)
    coarse = []
    for y in itertools.product(*[range(n) for n in cd]):
        y = np.array(y)
        for mu in range(d):
            for nu in range(mu + 1, d):
                cur = {}
                for (s, a, b) in [(1, y, mu), (1, y + ex[mu], nu), (-1, y + ex[nu], mu), (-1, y, nu)]:
                    key = (tuple(np.mod(a, cd)), b)
                    cur[key] = cur.get(key, 0) + s
                coarse.append(Qtrans(cur))
    U = np.array(coarse).T
    guard()
    GU = green(U)
    Y = U.T @ GU
    Yinv = np.linalg.pinv(Y, rcond=1e-10, hermitian=True)
    # half-space plaquettes
    J = []
    Tmax = dims[2] // 2
    for x in itertools.product(range(dims[0]), range(dims[1]), range(1, Tmax)):
        x = np.array(x)
        for (mu, nu) in [(0, 1), (0, 2), (1, 2)]:
            if (nu == 2) and x[2] + 1 >= Tmax:
                continue
            J.append(plaquette(x, mu, nu))
    J = np.array(J).T
    rJ = np.array([reflect(J[:, i]) for i in range(J.shape[1])]).T
    guard()
    GJ = green(J)
    R0 = rJ.T @ GJ
    R0 = 0.5 * (R0 + R0.T)
    # delta(Theta J, J') = (rJ^T G U) Yinv (U^T G J')
    A = rJ.T @ GU
    B = GU.T @ J
    D = A @ Yinv @ B
    D = 0.5 * (D + D.T)
    guard()
    out = {"nplaq": J.shape[1], "rank_coarse": int(np.linalg.matrix_rank(Y, tol=1e-9)), "rows": []}
    for r in [1.0, 1.01, 1.1, 2.0, 0.9, 0.5]:
        Rg = R0 + (r - 1.0) * D
        ev = np.linalg.eigvalsh(Rg)
        rec = dict(ratio=r, min=float(ev[0]), max=float(ev[-1]), rel=float(ev[0] / ev[-1]), n_neg=int((ev < -1e-11 * ev[-1]).sum()))
        out["rows"].append(rec)
        print(rec, flush=True)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "abelian_td.json"), "w") as f:
        json.dump(out, f, indent=1)


if __name__ == "__main__":
    main()
