"""A49 val16: (a) validate the local-estimator code against the exact covariance on the 16-site cluster by exact
enumeration (weights |psi|^2): 'singlet' mode on the lam'=0 parton, 'full' mode on the same state (expected to FAIL:
support problem), 'full' mode on dual-(111) Neel m=0.1 and the polarized product state;
(b) the lowest relative variance restricted to the dual-SU(2)-invariant subspace (Klein duals of SU(2)-invariant
rules), for every saved 16-site state."""
import sys, signal, time, numpy as np
signal.alarm(285)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a49lib import *
t0 = time.time()
cl = Cluster([[2, 2, 0], [2, 0, 2], [0, 2, 2]]); N = cl.N
ops = [(nm, cls, "b", op) for nm, cls, op in bilinear_basis()] + [(nm, cls, "4", d4) for nm, cls, d4, sold in four_basis()]
T = Tables(cl, ops); names = T.names; n = len(names)
D = np.load("ed16_C.npz"); G = D["G"]
bits = bits_table(N)

def enum_C(Phi, mode, sector=None):
    psi = projected_vector(Phi, bits); w = np.abs(psi) ** 2; w /= w.sum()
    sel = np.flatnonzero(w > 1e-28 * w.max())
    if sector is not None:
        sel = sel[(N - bits[sel].sum(1)) == sector]
    S = []
    for k in sel:
        s = bits[k].astype(int); Q = np.linalg.inv(Phi[T.rows0 + s])
        S.append(pack(estimators(T, Phi, Q, s, mode), mode))
    S = np.array(S); ww = w[sel] / w[sel].sum()
    return cov_from_samples(S, n, mode, N, ww), len(sel)

for tag, Phi, mode, key in (("lp0 singlet-mode", mf_state(cl)[0], "singlet", "lp0.0"),
                             ("lp0 naive full-mode", mf_state(cl)[0], "full", "lp0.0"),
                             ("nee111_0.1 full-mode", mf_state(cl, m=0.1, axis=(1, 1, 1))[0], "full", "nee111_0.1")):
    (C, ex), ns = enum_C(Phi, mode)
    Cx = D[f"C_{key}"]; exx = D[f"ex_{key}"]
    print(f"{tag:22s}: {ns} configs; max|C - C_exact| = {np.abs(C - Cx).max():.2e} (max|C_exact| {np.abs(Cx).max():.2f}); "
          f"max|<h> - exact| = {np.abs(ex - exx).max():.2e}  [{time.time()-t0:.0f}s]", flush=True)
nh = np.array([1., 2., 3.]) / np.sqrt(14.)
pol = [np.array([kR(x, b) * nh[b] for b in range(3)]) for x in cl.sites]
(C, ex), ns = enum_C(product_state(pol), "full")
Cx = D["C_polarized"]
print(f"{'polarized full-mode':22s}: {ns} configs; max|C - C_exact| = {np.abs(C - Cx).max():.2e}  [{time.time()-t0:.0f}s]", flush=True)

# (b) dual-SU(2)-invariant subspace: span of {-J1 + 1.1547 K1, -J2 + 1.1547 Kn2, J3, J4, all four-spin}
def inv_basis(sub):
    rows = []
    def vec(d):
        v = np.zeros(n)
        for k, c in d.items(): v[names.index(k)] = c
        return v
    rows.append(vec({"J1": -1., "K1": 2 / np.sqrt(3)})); rows.append(vec({"J2": -1., "Kn2": 2 / np.sqrt(3)})); rows.append(vec({"J3": 1.}))
    if sub == "S1uS2": rows.append(vec({"J4": 1.}))
    for k, (nm, cls) in enumerate(zip(names, T.cls)):
        if T.cls[k] in ("S1", "S2") and ops[k][2] == "4" and (cls == "S1" or sub == "S1uS2"):
            rows.append(vec({nm: 1.}))
    return np.array(rows).T
print("== lowest relative variance: full set vs dual-SU(2)-invariant subspace (16 sites) ==")
for key in [k for k in D.files if k.startswith("C_")]:
    C = D[key]; line = f"  {key[2:]:12s}"
    for sub, sl in (("S1", [k for k, c in enumerate(T.cls) if c == "S1"]), ("S1uS2", list(range(n)))):
        lam_full = releig(C[np.ix_(sl, sl)], G[np.ix_(sl, sl)])[0]
        B = inv_basis(sub); lam_inv = releig(B.T @ C @ B, B.T @ G @ B)[0]
        line += f" | {sub}: full {lam_full[0]:.3g} / inv {lam_inv[0]:.3g} (2nd {lam_inv[1]:.3g})"
    print(line, flush=True)
print(f"done {time.time()-t0:.0f}s")
