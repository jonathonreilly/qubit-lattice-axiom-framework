"""Truncated exact Holevo information for dilute Gaussian fragments (few particles, many empty modes).
States are sums over subsets of 'partial' natural orbitals (<= K of them), plus 'full' orbitals always occupied.
Mixture spectrum per particle-number sector from the Gram matrix of the two Slater-determinant families
(nonzero eigenvalues of X^dag X, X = [M_u sqrt(W_u), M_d sqrt(W_d)]/sqrt2), where the overlaps of Slater determinants
are determinants of mode overlaps.  Convention: vectors are the columns W of the natural-orbital eigenvectors of D
(the whole calculation is conjugation invariant, see gauss.py for the verified-against-brute-force version)."""
import itertools
import numpy as np


def _H(p):
    p = np.asarray(p)
    p = p[p > 1e-15]
    return float(-np.sum(p * np.log2(p)))


def _modes(D, eps):
    nu, W = np.linalg.eigh((D + D.conj().T) / 2)
    nu = np.clip(nu, 0.0, 1.0)
    full = [k for k in range(len(nu)) if nu[k] > 1 - eps]
    part = [k for k in range(len(nu)) if eps <= nu[k] <= 1 - eps]
    return nu, W, full, part


def _configs(nu, full, part, K):
    """list of (modes tuple, weight). weight = prod over partial modes."""
    base_w = 1.0
    # empty modes and full modes contribute ~1 (their epsilon deviations are neglected but counted in 'lost')
    cfgs = []
    for r in range(0, min(K, len(part)) + 1):
        for B in itertools.combinations(part, r):
            w = 1.0
            for k in part:
                w *= nu[k] if k in B else (1 - nu[k])
            cfgs.append((tuple(full) + B, w))
    return cfgs


def holevo_trunc(Du, Dd, K=4, eps=1e-10, maxpart=12):
    nu_u, W_u, fu, pu = _modes(Du, eps)
    nu_d, W_d, fd, pd = _modes(Dd, eps)
    # cap the number of partial modes (largest nu(1-nu))
    def cap(part, nu):
        if len(part) > maxpart:
            part = sorted(part, key=lambda k: -nu[k] * (1 - nu[k]))[:maxpart]
        return part
    pu, pd = cap(pu, nu_u), cap(pd, nu_d)
    cu = _configs(nu_u, fu, pu, K)
    cd = _configs(nu_d, fd, pd, K)
    lost = max(1 - sum(w for _, w in cu), 1 - sum(w for _, w in cd))
    Ov = W_u.conj().T @ W_d
    # sectors by particle number
    Su = _H([w for _, w in cu])
    Sd = _H([w for _, w in cd])
    nums = sorted(set(len(x) for x, _ in cu) | set(len(x) for x, _ in cd))
    Sav = 0.0
    for n in nums:
        Cu = [(x, w) for x, w in cu if len(x) == n]
        Cd = [(x, w) for x, w in cd if len(x) == n]
        nu_, nd_ = len(Cu), len(Cd)
        T = np.zeros((nu_ + nd_, nu_ + nd_), dtype=complex)
        for i, (x, w) in enumerate(Cu):
            T[i, i] = 0.5 * w
        for j, (y, w) in enumerate(Cd):
            T[nu_ + j, nu_ + j] = 0.5 * w
        if nu_ and nd_:
            wx = np.array([w for _, w in Cu])
            wy = np.array([w for _, w in Cd])
            if n == 0:
                G = np.ones((nu_, nd_), dtype=complex)
            else:
                xi = np.array([x for x, _ in Cu])
                yi = np.array([y for y, _ in Cd])
                G = np.linalg.det(Ov[xi[:, None, :, None], yi[None, :, None, :]])
            blk = 0.5 * np.sqrt(wx[:, None] * wy[None, :]) * G
            T[:nu_, nu_:] = blk
            T[nu_:, :nu_] = blk.conj().T
        ev = np.linalg.eigvalsh(T) if len(T) else np.array([])
        Sav += _H(np.clip(ev, 0, None))
    return Sav - 0.5 * (Su + Sd), lost


if __name__ == "__main__":
    import beam_vs_sea as b
    from gauss import holevo
    L = 300
    h = b.chain_h(L)
    j0 = 110
    Phi0 = b.packets(L, j0, 2, sigma=2.0, spacing=12, first=8)
    Pu = b.evolve(h, j0, 20.0, Phi0, 30.0)
    Pd = b.evolve(h, j0, 0.0, Phi0, 30.0)
    Du, Dd = b.corr(Pu), b.corr(Pd)
    import time
    worst = 0
    for i, m in [(120, 8), (140, 8), (60, 8), (70, 6), (170, 8), (30, 8), (90, 8), (100, 8)]:
        a, c = Du[i:i + m, i:i + m], Dd[i:i + m, i:i + m]
        e = holevo(a, c)
        t0 = time.time()
        f, lost = holevo_trunc(a, c)
        worst = max(worst, abs(e - f))
        print(i, m, round(e, 8), round(f, 8), 'lost', lost, round(time.time() - t0, 3))
    print('worst diff', worst)
