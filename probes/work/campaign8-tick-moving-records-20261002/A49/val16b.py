"""A49 val16b: split the singlet-mode check into (i) the Wigner-Eckart decomposition (exact vectors, all S^z=0
configurations) and (ii) the estimator code (exact vectors masked to supp(psi) vs exact enumeration); plus a generic
singlet (random spin-independent hopping) with full S^z=0 support; plus the amplitude-zero census of the projected
pi-flux singlet at 16 sites and on random S^z=0 configurations at L = 4, 6, 8."""
import sys, signal, time, numpy as np
signal.alarm(285)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a49lib import *
t0 = time.time()
cl = Cluster([[2, 2, 0], [2, 0, 2], [0, 2, 2]]); N = cl.N
ops = [(nm, cls, "b", op) for nm, cls, op in bilinear_basis()] + [(nm, cls, "4", d4) for nm, cls, d4, sold in four_basis()]
T = Tables(cl, ops); names = T.names; n = len(names)
strs = [T.cluster_strings(k) for k in range(n)]
Z = zarrays(N); bits = bits_table(N); nup = N - bits.sum(1); S0 = nup == N // 2

def q0_strings():
    """q = 0 operators of the Wigner-Eckart split: rank-0 parts (incl. four-spin), O1_{k,c}, O2_{k,m}."""
    O0, O1, O2 = [], [], []
    for k in range(n):
        d0 = {}
        for p in range(T.np_):
            i, j = int(T.pi[p]), int(T.pj[p]); w0 = T.W0[k, p]
            if w0:
                for a in range(3): add(d0, ((i, a), (j, a)), w0)
        for q in range(T.ns):
            S = T.sets[q]
            for pi in range(3):
                w = T.W4[k, q, pi]
                if w == 0: continue
                (u, v), (x, y) = PAIRINGS[pi]
                for a in range(3):
                    for b in range(3):
                        add(d0, tuple(sorted(((int(S[u]), a), (int(S[v]), a), (int(S[x]), b), (int(S[y]), b)))), w)
        O0.append(clean(d0))
        for c in range(3):
            d = {}
            for p in range(T.np_):
                i, j = int(T.pi[p]), int(T.pj[p]); w = T.W1[k, c, p]
                if w: add(d, ((i, 0), (j, 1)), w); add(d, ((i, 1), (j, 0)), -w)
            O1.append(clean(d))
        for m in range(5):
            d = {}
            for p in range(T.np_):
                i, j = int(T.pi[p]), int(T.pj[p]); w = T.W2[k, m, p]
                if w:
                    add(d, ((i, 2), (j, 2)), w * 2 / 3)
                    for a in (0, 1): add(d, ((i, a), (j, a)), -w / 3)
            O2.append(clean(d))
    return O0, O1, O2
O0, O1, O2 = q0_strings()

def we_C(psi, mask):
    f = lambda O: np.array([apply_strings(o, psi, Z) * mask for o in O])
    P0, P1, P2 = f(O0), f(O1).reshape(n, 3, -1), f(O2).reshape(n, 5, -1)
    m0 = P0.conj() @ psi
    C = P0.conj() @ P0.T - np.outer(m0.conj(), m0) + np.einsum('icx,jcx->ij', P1.conj(), P1) + 1.5 * np.einsum('imx,jmx->ij', P2.conj(), P2)
    return C.real / N

def enum_C(Phi, psi):
    w = np.abs(psi) ** 2; sel = np.flatnonzero(w > 1e-28 * w.max()); S = []
    for k in sel:
        s = bits[k].astype(int); Q = np.linalg.inv(Phi[T.rows0 + s]); S.append(pack(estimators(T, Phi, Q, s, "singlet"), "singlet"))
    return cov_from_samples(np.array(S), n, "singlet", N, w[sel] / w[sel].sum())[0], len(sel)

rng = np.random.default_rng(7)
A = rng.normal(size=(N, N)); h0 = (A + A.T) / 2
ev, U = np.linalg.eigh(h0); Phi_r = np.kron(U[:, :N // 2], np.eye(2)).reshape(2 * N, N)   # rows 2i+spin
for tag, Phi in (("pi-flux singlet (lam'=0)", mf_state(cl)[0]), ("random-hopping singlet", Phi_r)):
    psi = projected_vector(Phi, bits); psi /= np.linalg.norm(psi)
    Cx = exact_C(strs, psi, Z, N)[0]
    sup = (np.abs(psi) ** 2 > 1e-28 * np.max(np.abs(psi) ** 2)).astype(float)
    Cwe = we_C(psi, S0.astype(float)); Cwe_m = we_C(psi, sup)
    Ce, ns = enum_C(Phi, psi)
    print(f"{tag}: S^z=0 configs with psi=0: {int(S0.sum() - (sup*S0).sum())} of {int(S0.sum())}; S^2 check <psi|S^z-sector> ok", flush=True)
    print(f"   (i)  Wigner-Eckart on all S^z=0 configs vs exact C: max diff {np.abs(Cwe - Cx).max():.2e}", flush=True)
    print(f"   (ii) estimator enumeration vs WE masked to supp(psi): max diff {np.abs(Ce - Cwe_m).max():.2e}", flush=True)
    print(f"   (iii) support loss: max|C_masked - C_exact| = {np.abs(Cwe_m - Cx).max():.2e}; lowest lam S1 exact vs masked: "
          f"{releig(Cx[:18,:18], np.load('ed16_C.npz')['G'][:18,:18])[0][0]:.4g} vs {releig(Cwe_m[:18,:18], np.load('ed16_C.npz')['G'][:18,:18])[0][0]:.4g}  [{time.time()-t0:.0f}s]", flush=True)

# zero census at larger sizes: random S^z=0 configurations, log|psi| relative to the median
for L in (4, 6, 8):
    c = cube(L); Phi, gap = mf_state(c); M = c.N; vals = []
    for t in range(300 if L < 8 else 120):
        s = rng.permutation(np.r_[np.zeros(M // 2, int), np.ones(M // 2, int)])
        sv = np.linalg.svd(Phi[2 * np.arange(M) + s], compute_uv=False)
        vals.append(np.log10(sv[-1] / sv[0]))
    vals = np.array(vals)
    print(f"L={L}: log10(smallest/largest singular value) over random S^z=0 configs: min {vals.min():.1f}, median {np.median(vals):.1f}; "
          f"exactly singular (< -12): {np.sum(vals < -12)}/{len(vals)}  [{time.time()-t0:.0f}s]", flush=True)
