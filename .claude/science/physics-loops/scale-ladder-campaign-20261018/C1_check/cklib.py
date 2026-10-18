"""Shared helpers for the C1 checker: pairing channels, node data, Floquet BdG.  Built only on ckmodel.py."""
from ckmodel import *

KST = np.array([1, -1, 1]) * np.pi / 2          # located in ckmodel probe: the two isotropic cube points are +-KST
QR = np.pi * np.ones(3); Q0 = np.zeros(3)
NODES = {}
for k in CUBE:
    n = tuple(int(x) for x in np.round(np.mod((k - KST) / np.pi, 2)).astype(int) % 2)
    NODES[n] = k                                 # label: n in {0,1}^3 with K = k* + pi n (mod 2pi)
DOUB = [n for n in NODES if n not in ((0, 0, 0), (1, 1, 1))]
NAME = {n: ('k*' if n == (0, 0, 0) else '-k*' if n == (1, 1, 1) else f'k*+pi{n}') for n in NODES}

# ---------- range-r pairing blocks at pair momentum Q ----------
# D_{(v,a),(v+d,b)} = e^{iQ.v} A_d[a,b];  Fermi:  A_{-d} = -e^{-iQ.d} A_d^T;  symmetry (character chi):
# chi(g) A_{Md} = (-1)^{lam.d} U A_d U^T.  Momentum form: pair term sum_k c_k^T Delta(k) c_{-Q-k}, Delta(k) = sum_d A_d e^{-i(Q+k).d}.
def fermi(bl, Q):
    out = {}
    for d, h in bl.items():
        add(out, d, 0.5 * h)
        add(out, neg(d), -0.5 * np.exp(-1j * np.dot(Q, d)) * h.T)
    return out
def rand_blocks(rng, r=1):
    return {d: rng.normal(size=(12, 12)) + 1j * rng.normal(size=(12, 12)) for d in itertools.product(range(-r, r + 1), repeat=3)}
def sym_pair(bl, chi, Q, idx=PROPER):
    return sym_blocks(fermi(bl, Q), idx, chi)
def Delta(bl, Q, ks):
    ks = np.atleast_2d(np.asarray(ks, float)); out = np.zeros((len(ks), 12, 12), complex)
    for d, h in bl.items(): out += np.exp(-1j * (ks + Q) @ np.array(d, float))[:, None, None] * h[None]
    return out
def check_sym(bl, chi, Q, idx=PROPER, ntest=3, rng=None):
    rng = rng or np.random.default_rng(0); ok = True
    for k in rng.uniform(-np.pi, np.pi, (ntest, 3)):
        Dk = Delta(bl, Q, k)[0]
        ok &= np.allclose(Dk, -Delta(bl, Q, -Q - k)[0].T, atol=1e-10)               # Fermi antisymmetry
        for g in idx:
            ok &= np.allclose(UF[g] @ Dk @ UF[g].T, chi[g] * Delta(bl, Q, gk(g, k))[0], atol=1e-10)
    return ok

# ---------- on-site antisymmetric channel spaces ----------
ASB = []
for i in range(12):
    for j in range(i + 1, 12):
        X = np.zeros((12, 12)); X[i, j] = 1; X[j, i] = -1; ASB.append(X)
def onsite_channel(chi, idx=PROPER, tol=1e-9):
    rows = []
    for g in idx:
        rows.append(np.array([(UF[g] @ X @ UF[g].T - chi[g] * X)[np.triu_indices(12, 1)] for X in ASB]).T)
    Mx = np.vstack(rows); _, s, Vh = np.linalg.svd(Mx); s = np.concatenate([s, np.zeros(Vh.shape[0] - len(s))])
    return [sum(c * X for c, X in zip(v.conj(), ASB)) for v in Vh[s < tol]]

# ---------- node doublets ----------
def node_doublet(n, E=np.pi / 2): return level_at(NODES[n], E)
def singlet(Qm, Dm):
    """BdG coupling of the particle doublet to its own hole doublet: psi1^dag Dm psi2^* (antisymmetric part)."""
    M = Qm.conj().T @ Dm @ Qm.conj(); return 0.5 * (M[0, 1] - M[1, 0])

# ---------- Floquet BdG ----------
def bdg_U(ks, Dfun, tau, Q, mu=np.pi / 2):
    ks = np.atleast_2d(np.asarray(ks, float)); n = len(ks)
    D = Dfun(ks); Da = D - np.transpose(Dfun(-Q - ks), (0, 2, 1))
    h = np.zeros((n, 24, 24), complex); h[:, :12, 12:] = Da; h[:, 12:, :12] = np.conj(np.transpose(Da, (0, 2, 1)))
    w, V = np.linalg.eigh(h); P = (V * np.exp(-1j * tau * w)[:, None, :]) @ np.conj(np.transpose(V, (0, 2, 1)))
    N = np.zeros((n, 24, 24), complex); N[:, :12, :12] = np.exp(-1j * mu) * Wb(ks); N[:, 12:, 12:] = np.exp(1j * mu) * np.conj(Wb(-Q - ks))
    return P @ N
def bdg_eps(ks, Dfun, tau, Q):
    return np.angle(np.linalg.eigvals(bdg_U(ks, Dfun, tau, Q)))
def gap0(ks, Dfun, tau, Q): return np.min(np.abs(bdg_eps(ks, Dfun, tau, Q)), axis=-1)
def gappi(ks, Dfun, tau, Q): return np.min(np.abs(wrap(bdg_eps(ks, Dfun, tau, Q) - np.pi)), axis=-1)
def grid_min(Dfun, tau, Q, N=20, exclude=(), r_ex=0.0, chunk=1500):
    g = 2 * np.pi * np.arange(N) / N - np.pi + 1e-3
    K = np.array(list(itertools.product(g, g, g)))
    if exclude:
        keep = np.ones(len(K), bool)
        for e in exclude: keep &= np.linalg.norm(wrap(K - e), axis=1) >= r_ex
        K = K[keep]
    b0 = np.inf; bp = np.inf; k0 = kp = None
    for i in range(0, len(K), chunk):
        ev = bdg_eps(K[i:i + chunk], Dfun, tau, Q)
        a0 = np.min(np.abs(ev), axis=1); ap = np.min(np.abs(wrap(ev - np.pi)), axis=1)
        j = np.argmin(a0); j2 = np.argmin(ap)
        if a0[j] < b0: b0, k0 = a0[j], K[i + j]
        if ap[j2] < bp: bp, kp = ap[j2], K[i + j2]
    return (b0, k0), (bp, kp)
