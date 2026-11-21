# Row 974 analysis. Usage: python3 -I ana974.py <npz> [<npz> ...]   (several files = concatenated streams)
# Upper bounds on sector energies (library/gap-trajtest-opus.md 2.2, 3.2):
#  G: projected correlator c_v(tau) = v^T C(tau) v, v = top GEVP vector of (C(1), C(0)) on the full sample;
#     E^G(tau) = log c_v(tau)/c_v(tau+1); also single-operator effective energies; also -(1/tau) log lambda_max(tau).
#  F: axis-averaged Polyakov-line correlators per smearing level, and projected on the 2x2 GEVP vector.
# Errors: jackknife over 20 blocks of consecutive configurations.
import sys, numpy as np
TMAX, NB = 6, 20
G = np.concatenate([np.load(f)["G"] for f in sys.argv[1:]]); F = np.concatenate([np.load(f)["F"] for f in sys.argv[1:]])
meta = np.load(sys.argv[1])["meta"]; L, T, beta = int(meta[0]), int(meta[1]), meta[2]
N = len(G); N -= N % NB; G, F = G[:N], F[:N]
def corrs(X):            # X: (n, ops, T) -> per-config M[tau] (n, TMAX+1, ops, ops), means (n, ops)
    m = X.mean(2)
    M = np.stack([np.einsum('nat,nbt->nab', X, np.roll(X, -t, axis=2)) / X.shape[2] for t in range(TMAX + 1)], 1)
    return M, m
def conn(M, m, sub=True):
    C = M.mean(0); mm = m.mean(0)
    if sub: C = C - np.outer(mm, mm)[None]
    return 0.5 * (C + np.swapaxes(C, 1, 2))
def jk(fun, M, m, sub):
    blk = np.arange(len(M)) // (len(M) // NB); out = []
    for b in range(NB):
        k = blk != b; out.append(fun(conn(M[k], m[k], sub)))
    out = np.array(out); full = fun(conn(M, m, sub))
    return full, np.sqrt((NB - 1) / NB * ((out - out.mean(0)) ** 2).sum(0))
def topvec(C, t=1):
    w, V = np.linalg.eigh(C[0]); S = V / np.sqrt(np.abs(w)); A = S.T @ C[t] @ S
    lw, lv = np.linalg.eigh(0.5 * (A + A.T)); return S @ lv[:, -1]
def effs(C, v):
    c = np.array([v @ C[t] @ v for t in range(TMAX + 1)])
    with np.errstate(all='ignore'): return np.log(c[:-1] / c[1:])
def lammax(C):
    w, V = np.linalg.eigh(C[0]); S = V / np.sqrt(np.abs(w)); out = []
    for t in range(1, TMAX + 1):
        A = S.T @ C[t] @ S; lm = np.linalg.eigvalsh(0.5 * (A + A.T))[-1]
        with np.errstate(all='ignore'): out.append(-np.log(lm) / t)
    return np.array(out)
def fmt(v, e): return " ".join(f"{a:6.3f}+-{b:5.3f}" for a, b in zip(v, e))
print(f"L={L} Nt={T} beta={beta} N={N} plaq={np.concatenate([np.load(f)['PL'] for f in sys.argv[1:]])[:N].mean():.5f}")
MG, mG = corrs(G)
vG = topvec(conn(MG, mG))
for name, fun in (("G proj E(tau)", lambda C: effs(C, vG)), ("G -log(lmax)/tau, tau>=1", lammax)):
    v, e = jk(fun, MG, mG, True); print(f"  {name:26s}", fmt(v, e))
for k, nm in enumerate(("plaq n1", "2x2 n1", "plaq n2", "2x2 n2")):
    u = np.zeros(4); u[k] = 1; v, e = jk(lambda C: effs(C, u), MG, mG, True); print(f"  G {nm:24s}", fmt(v, e))
# F: stack axes as extra samples of the same 2-operator family (levels), average correlators over axes
Fx = F.transpose(0, 2, 1, 3).reshape(N, 3 * 2, T)          # (n, axis*level, T)
MF, mF = corrs(Fx)
MF2 = sum(MF[:, :, 2 * a:2 * a + 2, 2 * a:2 * a + 2] for a in range(3)) / 3
mF2 = np.zeros((N, 2))
vF = topvec(conn(MF2, mF2, False))
for name, fun in (("F proj E(tau)", lambda C: effs(C, vF)), ("F lev1 E(tau)", lambda C: effs(C, np.array([1., 0]))),
                  ("F lev2 E(tau)", lambda C: effs(C, np.array([0., 1]))), ("F -log(lmax)/tau", lammax)):
    v, e = jk(fun, MF2, mF2, False); print(f"  {name:26s}", fmt(v, e))
pm = np.abs(F.mean(3)).mean(); print(f"  F: mean |slice-avg Polyakov| per config = {pm:.4f}")
# Diagnostic (added after the first L = 20 look): F with the sample mean subtracted per axis (connected), axis-averaged.
def blockavg(C): return sum(C[:, 2 * a:2 * a + 2, 2 * a:2 * a + 2] for a in range(3)) / 3
vFc = topvec(blockavg(conn(MF, mF, True)))
for name, fun in (("F conn proj E(tau)", lambda C: effs(blockavg(C), vFc)),):
    v, e = jk(fun, MF, mF, True); print(f"  {name:26s}", fmt(v, e))
