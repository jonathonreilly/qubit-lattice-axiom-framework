"""Vectorised reconstruction of the 2026-06-08 staggered Kahler-Dirac induced-graviton bubble.

Source definitions copied (formula-for-formula) from
  scripts/frontier_universal_gr_graviton_dispersion_lorentz_isotropy.py   (vertex 'D': mom = sin(Pbar))
  scripts/frontier_universal_gr_cubic_diffeo_ward_operator_telescope.py   (same vertex 'D', exact op-Ward)
  scripts/frontier_universal_gr_graviton_isotropy_staggered.py            (vertex 'S': mom = sin(Pbar/2))
  scripts/frontier_universal_gr_staggered_tt_stiffness_positive.py        (vertex 'S')

  D(P)        16x16 hypercube-block staggered operator, block momentum P in [-pi,pi)^4
  Vel_mu(P)   = dD/dP_mu
  V_munu(P,K) = 1/2 [Vel_mu(Pbar) f_nu(Pbar) + Vel_nu(Pbar) f_mu(Pbar)],  Pbar = P + K/2
  Pi_{munu,rhosig}(K) = (1/N^4) sum_P tr[ G(P) V_munu G(P+K) V_rhosig ],  G = D^{-1}
(V(P+K,-K) has the same midpoint Pbar, so both insertions are the same matrix.)

The runners use the subtracted kernel  Pi(K) - Pi(0)  (bubble only, no seagull).
This is an independent vectorised implementation (not a re-run of the runner loops).
"""
import itertools
import numpy as np

CORNERS = list(itertools.product([0, 1], repeat=4))
CIDX = {A: i for i, A in enumerate(CORNERS)}


def _eta(A, mu):
    return (-1) ** sum(A[nu] for nu in range(mu))


def _flip(A, mu):
    B = list(A)
    B[mu] ^= 1
    return tuple(B)


# D(P) = m I + sum_mu [H0_mu + Hm_mu e^{-iP_mu} + Hp_mu e^{+iP_mu}]
H0 = np.zeros((4, 16, 16))
Hm = np.zeros((4, 16, 16))
Hp = np.zeros((4, 16, 16))
for A in CORNERS:
    a = CIDX[A]
    for mu in range(4):
        b = CIDX[_flip(A, mu)]
        e = _eta(A, mu)
        if A[mu] == 0:
            H0[mu, a, b] += 0.5 * e
            Hm[mu, a, b] += -0.5 * e
        else:
            Hp[mu, a, b] += 0.5 * e
            H0[mu, a, b] += -0.5 * e
I16 = np.eye(16)
PAIRS = [(mu, nu) for mu in range(4) for nu in range(mu, 4)]  # 10 symmetric pairs


def Dmat(P, m):
    """P: (n,4) -> (n,16,16)."""
    em = np.exp(-1j * P)
    ep = np.exp(1j * P)
    D = m * I16[None].astype(complex) + H0.sum(0)[None]
    D = D + (em @ Hm.reshape(4, 256)).reshape(-1, 16, 16) + (ep @ Hp.reshape(4, 256)).reshape(-1, 16, 16)
    return D


def Ginv(P, m):
    """D^{-1} = D^dagger / Delta, Delta = m^2 + sum sin^2(P/2) (exact: D D^dag = Delta 1; checked in runner)."""
    D = Dmat(P, m)
    Delta = m * m + np.sum(np.sin(0.5 * P) ** 2, axis=1)
    return np.conj(np.transpose(D, (0, 2, 1))) / Delta[:, None, None]


def Vel(P):
    """(n,4) -> (4,n,16,16) dD/dP_mu."""
    em = np.exp(-1j * P)
    ep = np.exp(1j * P)
    return (np.einsum('nm,mab->mnab', -1j * em, Hm) + np.einsum('nm,mab->mnab', 1j * ep, Hp))


def mom(Pbar, variant):
    if variant == 'D':
        return np.sin(Pbar)
    if variant == 'S':
        return np.sin(0.5 * Pbar)
    raise ValueError(variant)


def vertices(Pbar, variant):
    """(10,n,16,16) symmetric stress vertices at midpoint Pbar."""
    Vl = Vel(Pbar)
    f = mom(Pbar, variant)
    out = []
    for (mu, nu) in PAIRS:
        out.append(0.5 * (Vl[mu] * f[:, nu, None, None] + Vl[nu] * f[:, mu, None, None]))
    return np.array(out)


def grid(N):
    p = np.linspace(-np.pi, np.pi, N, endpoint=False)
    return np.array(list(itertools.product(p, p, p, p)))


def Pi_tensor_fast(K, N, m, variant, chunk=1024, Pgrid=None):
    """Full 4x4x4x4 kernel via J_{mu rho}(P) = tr[G(P) Vel_mu(Pbar) G(P+K) Vel_rho(Pbar)]:
    Pi_{mu nu,rho sig} = 1/4 <f_nu f_sig J_mu rho + f_nu f_rho J_mu sig + f_mu f_sig J_nu rho + f_mu f_rho J_nu sig>."""
    K = np.asarray(K, float)
    if Pgrid is None:
        Pgrid = grid(N)
    W = np.zeros((4, 4, 4, 4), complex)   # W[mu,rho,nu,sig] = sum_P J_{mu rho} f_nu f_sig
    for s in range(0, len(Pgrid), chunk):
        P = Pgrid[s:s + chunk]
        Pb = P + 0.5 * K
        G0 = Ginv(P, m)
        G1 = Ginv(P + K, m)
        Vl = Vel(Pb)
        X = np.matmul(G0[None], Vl)
        Y = np.matmul(G1[None], Vl)
        J = np.einsum('anij,bnji->nab', X, Y, optimize=True)
        f = mom(Pb, variant)
        W += np.einsum('nab,nc,nd->abcd', J, f, f, optimize=True)
    W /= len(Pgrid)
    T = 0.25 * (np.einsum('mrns->mnrs', W) + np.einsum('msnr->mnrs', W)
                + np.einsum('nrms->mnrs', W) + np.einsum('nsmr->mnrs', W))
    return T


def Pi_pairs(K, N, m, variant, Pgrid=None):
    T = Pi_tensor_fast(K, N, m, variant, Pgrid=Pgrid)
    return np.array([[T[a + b] for b in PAIRS] for a in PAIRS])


def tadpole(N, m, variant):
    """one-point <V_munu(P,0)> = (1/N^4) sum tr[G V]."""
    Pg = grid(N)
    G0 = Ginv(Pg, m)
    V = vertices(Pg, variant)
    t = np.einsum('nij,anji->a', G0, V) / len(Pg)
    return pairs_to_vec(t)


def pairs_to_tensor(M):
    T = np.zeros((4, 4, 4, 4), complex)
    for a, (mu, nu) in enumerate(PAIRS):
        for b, (rh, si) in enumerate(PAIRS):
            for (x, y) in {(mu, nu), (nu, mu)}:
                for (z, w) in {(rh, si), (si, rh)}:
                    T[x, y, z, w] = M[a, b]
    return T


def pairs_to_vec(t):
    T = np.zeros((4, 4), complex)
    for a, (mu, nu) in enumerate(PAIRS):
        T[mu, nu] = T[nu, mu] = t[a]
    return T


def Pi_tensor(K, N, m, variant, Pgrid=None):
    return Pi_tensor_fast(K, N, m, variant, Pgrid=Pgrid)


def quad(T, h1, h2=None):
    """h1_{mn} T_{mnrs} h2_{rs}."""
    if h2 is None:
        h2 = h1
    return np.einsum('ab,abcd,cd->', h1, T, h2)


# ---------------------------------------------------------------------------
# B4-invariant 6-index tensors T_{mu nu, rho sig, al be} (symbol h T k k h)
# ---------------------------------------------------------------------------
def _set_partitions(items):
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for p in _set_partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i + 1:]
        yield [[first]] + p


def _pattern_tensor(blocks):
    T = np.zeros((4,) * 6)
    for idx in itertools.product(range(4), repeat=6):
        if all(len({idx[p] for p in b}) == 1 for b in blocks):
            T[idx] = 1.0
    return T


_SYM_PERMS = []
for s01 in (False, True):
    for s23 in (False, True):
        for s45 in (False, True):
            for swap in (False, True):
                perm = [0, 1, 2, 3, 4, 5]
                if s01:
                    perm[0], perm[1] = perm[1], perm[0]
                if s23:
                    perm[2], perm[3] = perm[3], perm[2]
                if s45:
                    perm[4], perm[5] = perm[5], perm[4]
                if swap:
                    perm = [perm[2], perm[3], perm[0], perm[1], perm[4], perm[5]]
                _SYM_PERMS.append(perm)


def symmetrize6(T):
    return sum(np.transpose(T, p) for p in _SYM_PERMS) / len(_SYM_PERMS)


def b4_basis():
    """Returns (basis list, labels, is_lorentz flags), linearly independent."""
    cand = []
    for part in _set_partitions(list(range(6))):
        if all(len(b) % 2 == 0 for b in part):
            cand.append(part)
    vecs, labels, lor = [], [], []
    for part in cand:
        T = symmetrize6(_pattern_tensor(part))
        v = T.ravel()
        trial = np.array(vecs + [v])
        if np.linalg.matrix_rank(trial, tol=1e-9) > len(vecs):
            vecs.append(v)
            labels.append(str(part))
            lor.append(all(len(b) == 2 for b in part))
    # order Lorentz first
    order = sorted(range(len(vecs)), key=lambda i: (not lor[i]))
    return ([vecs[i].reshape((4,) * 6) for i in order], [labels[i] for i in order], [lor[i] for i in order])


def symbol_from_T6(T6, k):
    return np.einsum('abcdef,e,f->abcd', T6, k, k)


def EH_T6():
    """Linearised Einstein-Hilbert symbol:  1/2 k^2 h.h - (k.h)^2 + h (k h k) - 1/2 k^2 h^2  (in h T k k h form)."""
    d = np.eye(4)
    T = (0.5 * np.einsum('ac,bd,ef->abcdef', d, d, d)
         - np.einsum('ae,cf,bd->abcdef', d, d, d)
         + 0.5 * (np.einsum('ab,ce,df->abcdef', d, d, d) + np.einsum('cd,ae,bf->abcdef', d, d, d))
         - 0.5 * np.einsum('ab,cd,ef->abcdef', d, d, d))
    return symmetrize6(T)
