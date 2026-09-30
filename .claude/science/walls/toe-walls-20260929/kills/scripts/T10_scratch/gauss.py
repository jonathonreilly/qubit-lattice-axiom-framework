"""Exact Holevo information of fermionic Gaussian (number-conserving) fragment states.
Convention: D[x,y] = <c_x^dag c_y>.  Fragment state rho_F is Gaussian with one-body matrix D_F.
Natural orbitals: D_F = W diag(nu) W^dag, mode a_k = sum_y W[y,k] c_y, a_k^dag = sum_x conj(W[x,k]) c_x^dag.
Fock state with modes B occupied: sum_A det(conj(W)[A,B]) |A>, A = sorted site subsets.
"""
import itertools
import numpy as np

_CACHE = {}


def _subsets(m, n):
    key = (m, n)
    if key not in _CACHE:
        if n == 0:
            _CACHE[key] = np.zeros((1, 0), dtype=int)
        else:
            _CACHE[key] = np.array(list(itertools.combinations(range(m), n)), dtype=int).reshape(-1, n)
    return _CACHE[key]


def _blocks(D):
    """Return {n: (weights w_B, unitary M_{A,B})} for the Gaussian state with one-body matrix D."""
    m = D.shape[0]
    nu, W = np.linalg.eigh((D + D.conj().T) / 2)
    nu = np.clip(nu, 0.0, 1.0)
    V = W.conj()
    out = {}
    for n in range(m + 1):
        S = _subsets(m, n)
        if n == 0:
            M = np.ones((1, 1), dtype=complex)
        else:
            Aidx = S[:, None, :, None]
            Bidx = S[None, :, None, :]
            sub = V[Aidx, Bidx]
            M = np.linalg.det(sub)
        occ = np.zeros((len(S), m), dtype=bool)
        for i, b in enumerate(S):
            occ[i, b] = True
        w = np.prod(np.where(occ, nu[None, :], 1.0 - nu[None, :]), axis=1)
        out[n] = (w, M)
    return out


def _H(p):
    p = p[p > 1e-14]
    return float(-np.sum(p * np.log2(p)))


def holevo(Dup, Ddn):
    """chi = S(avg) - avg S for two Gaussian states with equal prior; bits."""
    bu, bd = _blocks(Dup), _blocks(Ddn)
    Sup = Sdn = Sav = 0.0
    m = Dup.shape[0]
    for n in range(m + 1):
        wu, Mu = bu[n]
        wd, Md = bd[n]
        Sup += _H(wu)
        Sdn += _H(wd)
        rho = 0.5 * (Mu * wu[None, :]) @ Mu.conj().T + 0.5 * (Md * wd[None, :]) @ Md.conj().T
        ev = np.linalg.eigvalsh((rho + rho.conj().T) / 2)
        Sav += _H(np.clip(ev, 0, None))
    return Sav - 0.5 * (Sup + Sdn)


def bruteforce_holevo(Dup, Ddn):
    """Independent check: build rho via Jordan-Wigner exponentials in full Fock space (m small)."""
    import scipy.linalg as sl
    m = Dup.shape[0]
    cdag = np.array([[0, 0], [1, 0]], dtype=complex)
    Z = np.diag([1.0, -1.0]).astype(complex)
    I2 = np.eye(2, dtype=complex)

    def cop(j):
        mats = [Z] * j + [cdag.conj().T] + [I2] * (m - j - 1)  # annihilator
        M = np.array([[1.0]], dtype=complex)
        for a in mats:
            M = np.kron(M, a)
        return M

    C = [cop(j) for j in range(m)]

    def rho_of(D):
        nu, W = np.linalg.eigh((D + D.conj().T) / 2)
        nu = np.clip(nu, 1e-12, 1 - 1e-12)
        # H = sum_{xy} h_{xy} c_x^dag c_y with h = log(nu/(1-nu)) in the D-eigenbasis (h = W diag(l) W^dag transposed appropriately)
        l = np.log(nu / (1 - nu))
        hmat = W @ np.diag(l) @ W.conj().T  # acts as c_x^dag h[x,y] c_y ; <c_x^dag c_y> = D[x,y] => h = f(D)^T
        hmat = hmat.T
        Hq = sum(hmat[x, y] * C[x].conj().T @ C[y] for x in range(m) for y in range(m))
        R = sl.expm(Hq)
        return R / np.trace(R)

    ru, rd = rho_of(Dup), rho_of(Ddn)

    def S(r):
        ev = np.linalg.eigvalsh((r + r.conj().T) / 2)
        return _H(np.clip(ev, 0, None))

    return S(0.5 * ru + 0.5 * rd) - 0.5 * (S(ru) + S(rd)), ru, C


if __name__ == "__main__":
    rng = np.random.default_rng(1)
    for m in (2, 3, 4):
        def rd():
            A = rng.normal(size=(m, m)) + 1j * rng.normal(size=(m, m))
            Q, _ = np.linalg.qr(A)
            nu = rng.uniform(0.1, 0.9, size=m)
            return Q @ np.diag(nu) @ Q.conj().T
        Du, Dd = rd(), rd()
        a = holevo(Du, Dd)
        b, ru, C = bruteforce_holevo(Du, Dd)
        # also check <c_x^dag c_y> from ru equals D
        ok = max(abs(np.trace(ru @ C[x].conj().T @ C[y]) - Du[x, y]) for x in range(m) for y in range(m))
        print(f"m={m} chi(minors)={a:.10f} chi(brute)={b:.10f} diff={abs(a-b):.2e} corr_check={ok:.2e}")
