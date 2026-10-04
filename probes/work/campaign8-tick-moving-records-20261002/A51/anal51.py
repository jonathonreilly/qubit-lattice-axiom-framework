"""A51 anal51: lowest relative variance lam = c^T C c / c^T G c versus reach (|d|^2 cutoff), per L and state, with
16-block jackknife errors and bias correction.  Two metrics: plain per-site HS Gram G, and the Casimir-removed
G' = G - g g^T / ||Cas||^2 (g_c = <O_c, Cas>/N).  Sets: B(R) = class sums with |d|^2 <= R; B4(R) = B(R) + 8 star
four-spin terms; B4p(R) = B(R) + all 10 four-spin terms.  Usage: anal51.py L spec[,spec...] [mode]
mode: 'reach' (default) | 'quick' (selected cutoffs only)."""
import sys, glob, signal, numpy as np
signal.alarm(280)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a51lib import *


def class_counts(L):
    ks = class_list(L); lab = {k: n for n, k in enumerate(ks)}
    g = np.array(list(itertools.product(range(L), repeat=3)))[1:]
    f = np.sort(fold(g, L), axis=1)
    m = np.bincount([lab[tuple(r)] for r in f], minlength=len(ks))
    return ks, m


def qorbit_vectors(L, ks):
    """p_Q[c] = sum_{q in orbit Q} cos(q.d_c) for every q-orbit Q (keys as classes, plus (0,0,0) first)."""
    qk = [(0, 0, 0)] + list(ks); lab = {k: i for i, k in enumerate(qk)}
    grid = np.array(list(itertools.product(range(L), repeat=3)))
    ql = np.array([lab[tuple(r)] for r in np.sort(fold(grid, L), axis=1)])
    K = np.array(ks, float); F = np.zeros((len(qk), len(ks)))
    for c in range(len(ks)):
        F[:, c] = np.bincount(ql, weights=np.cos(2 * np.pi * grid @ K[c] / L), minlength=len(qk))
    return qk, F


def proj_metric(G, W):
    """norm modulo span(W): G - G W (W^T G W)^-1 W^T G"""
    GW = G @ W; return G - GW @ np.linalg.solve(W.T @ GW, GW.T)


def metrics(L, lw=False):
    ks, m = class_counts(L); F4, G4 = four_ops(); nc = len(ks); n = nc + len(F4)
    G = np.zeros((n, n)); G[:nc, :nc] = np.diag(1.5 * m); G[nc:, nc:] = G4
    g = np.zeros(n); g[:nc] = 1.5 * m; Gm = G - np.outer(g, g) / g.sum()
    if not lw:
        return ks, m, F4, G, Gm
    qk, F = qorbit_vectors(L, ks); qn = 2 * np.pi * np.sqrt((np.array(qk, float) ** 2).sum(1)) / L
    rem = [i for i in range(len(qk)) if qn[i] <= np.pi / 2 + 1e-9]
    W = np.zeros((n, len(rem))); W[:nc] = F[rem].T
    return ks, m, F4, G, Gm, proj_metric(G, W), [qk[i] for i in rem]


def load(L, spec):
    fs = sorted(glob.glob(f"s51_{L}_{spec}_*.npy"))
    return (np.concatenate([np.load(f) for f in fs]), len(fs)) if fs else (None, 0)


def covm(S, N):
    m = S.mean(0); C = (S.conj().T @ S) / len(S) - np.outer(m.conj(), m)
    return C.real / N


def releig_q(C, G, tol=1e-9):
    """min c^T C c / c^T G c over the quotient by null(G): null components are chosen to minimise the variance
    (Schur complement), so rules differing by a zero-norm operator (Casimir, removed q-orbits) count as one."""
    w, U = np.linalg.eigh(G); keep = w > tol * w.max()
    Ur, Un = U[:, keep], U[:, ~keep]
    if Un.shape[1] == 0:
        return releig(C, G, tol)
    Crr = Ur.T @ C @ Ur; Crn = Ur.T @ C @ Un; Cnn = Un.T @ C @ Un
    e, Z = np.linalg.eigh(Cnn); cut = 1e-9 * max(np.abs(np.diag(C)).max(), 1e-300)
    P = (Z[:, e > cut] / e[e > cut]) @ Z[:, e > cut].T          # pseudo-inverse with an absolute cut (C scale)
    Ceff = Crr - Crn @ P @ Crn.T
    T = 1. / np.sqrt(w[keep])
    lam, Y = np.linalg.eigh((T[:, None] * Ceff) * T[None, :])
    Yr = T[:, None] * Y
    return lam, Ur @ Yr - Un @ (P @ (Crn.T @ Yr))


def lam_jk(S, N, idx, G, nb=16, nvec=False):
    """lowest eigenvalue (and vector) with jackknife error and bias correction"""
    idx = np.asarray(idx); Gs = G[np.ix_(idx, idx)]
    lam, V = releig_q(covm(S[:, idx], N), Gs)
    bl = np.array_split(np.arange(len(S)), nb); jk = []; vj = []
    for b in bl:
        Sb = np.delete(S[:, idx], b, axis=0); l, Vb = releig_q(covm(Sb, N), Gs); jk.append(l[:2]); vj.append(Vb[:, 0])
    jk = np.array([np.r_[j, np.nan][:2] for j in jk]); err = np.sqrt((nb - 1) / nb * ((jk - jk.mean(0)) ** 2).sum(0)); corr = nb * lam[:2] - (nb - 1) * jk.mean(0)
    if len(lam) < 2:
        lam = np.r_[lam, np.nan]; err = np.r_[err, np.nan]; corr = np.r_[corr, np.nan]
    out = dict(lam=lam[0], err=err[0], corr=corr[0], lam2=lam[1], err2=err[1], vec=V[:, 0])
    if nvec:
        v0 = V[:, 0]; vj = np.array([v * np.sign(v @ (Gs @ v0)) for v in vj])
        out["vec_err"] = np.sqrt((nb - 1) / nb * ((vj - vj.mean(0)) ** 2).sum(0)); out["vj"] = vj
    return out


def subsets(ks, nc, r2):
    b = [c for c, k in enumerate(ks) if sum(x * x for x in k) <= r2]
    return {"B": b, "B4": b + list(range(nc, nc + 8)), "B4p": b + list(range(nc, nc + 10))}


if __name__ == "__main__":
    L = int(sys.argv[1]); specs = sys.argv[2].split(","); mode = sys.argv[3] if len(sys.argv) > 3 else "reach"
    ks, m, F4, G, Gm, Gw, rem = metrics(L, lw=True); nc = len(ks); N = L ** 3
    print(f"L={L}: long-wavelength metric removes q-orbits {rem} (|q| <= pi/2) and the Casimir")
    shells = sorted(set(sum(x * x for x in k) for k in ks))
    if mode == "quick":
        shells = [r for r in shells if r in (1, 2, 3, 4, 6, 9, 12, 16, 27, 48)] + [shells[-1]]
        shells = sorted(set(shells))
    res = {}
    for spec in specs:
        S, nf = load(L, spec)
        if S is None:
            print(f"L={L} {spec}: no samples"); continue
        print(f"\n== L={L} {spec}: {len(S)} samples ({nf} files); <s.s>_NN/bond {S[:, 0].real.mean()/N/3:+.4f} ==")
        a49 = [ks.index(k) for k in ((0, 0, 1), (0, 1, 1), (0, 0, 2))]
        xs = [("S1b-inv(3)", a49), ("S1inv(11)", a49 + list(range(nc, nc + 8))),
              ("S1uS2inv(14)", a49 + [ks.index((1, 1, 1))] + list(range(nc, nc + 10)))]
        xo = [lam_jk(S, N, ix_, G) for nm, ix_ in xs]
        print("  A49 sets, plain metric: " + "; ".join(f"{nm} {o['lam']:.4g}({o['err']:.1g})" for (nm, _), o in zip(xs, xo)))
        print(" R^2 ncls |  B mod           B4 mod          |  B LW            B4 LW           | B4 mod bias-corr")
        for r2 in shells:
            sub = subsets(ks, nc, r2); row = []
            for key, Gx, tag in (("B", Gm, "mod"), ("B4", Gm, "mod"), ("B", Gw, "lw"), ("B4", Gw, "lw")):
                o = lam_jk(S, N, sub[key], Gx); row.append(o); res[(spec, r2, key, tag)] = o
            print(f" {r2:3d} {len(sub['B']):3d} | " + " ".join(f"{o['lam']:.4g}({o['err']:.1g})".ljust(15) for o in row[:2]) + " | " +
                  " ".join(f"{o['lam']:.4g}({o['err']:.1g})".ljust(15) for o in row[2:4]) + f" | {row[1]['corr']:.4g}", flush=True)
    np.save(f"anal51_{L}_{'_'.join(specs)}_{mode}.npy", np.array([res], dtype=object))
