"""A49 anal49: lowest relative variances lam = c^T C c / c^T G c (C per site, G per-site Hilbert-Schmidt Gram) from
the VMC samples, with jackknife errors (16 blocks) and jackknife bias correction.
Sets: NN (3), S1b (10 bilinears), S1 (18), S1uS2 (23); invariant subspaces S1inv (11) / S1uS2inv (14) = Klein duals of
dual-frame SU(2)-invariant rules (dual Heisenberg at each separation + the four-spin terms).
neez/colz states (S^z = 0, not singlets) and lam' != 0 partons (sampled in the dominant S^z = 0 sector; odd-sector weight
~1e-4 at 16 sites): only the invariant subspaces are used (rank-0, S^z-conserving operators)."""
import sys, glob, signal, numpy as np
signal.alarm(280)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a49lib import *
B2 = bilinear_basis(); F4 = four_basis()
names = [o[0] for o in B2] + [o[0] for o in F4]; cls = [o[1] for o in B2] + [o[1] for o in F4]
sold = [o[2] for o in B2] + [o[3] for o in F4]; n = len(names)
G = np.array([[hs(a, b) for b in sold] for a in sold])
FOUR = [o[0] for o in F4]                                        # four-spin operator names (T0 ... P1)          # infinite-lattice per-site HS Gram (L >= 5)
ix = lambda sl: [names.index(x) for x in sl]
SETS = {"NN": ix(["J1", "K1", "D1"]), "S1b": ix(["J1", "K1", "D1", "J2", "Kn2", "Kd2", "D2", "J3", "K3", "D3"]),
        "S1": [k for k in range(n) if cls[k] == "S1"], "S1uS2": list(range(n))}
def inv_basis(sub):
    cols = []
    def vec(d):
        v = np.zeros(n)
        for k, c in d.items(): v[names.index(k)] = c
        return v
    cols += [vec({"J1": -1., "K1": 2 / np.sqrt(3)}), vec({"J2": -1., "Kn2": 2 / np.sqrt(3)}), vec({"J3": 1.})]
    if sub == "S1uS2": cols.append(vec({"J4": 1.}))
    cols += [vec({nm: 1.}) for nm, c in zip(names, cls) if nm in FOUR and (c == "S1" or sub == "S1uS2")]
    return np.array(cols).T
BINV = {"S1inv": inv_basis("S1"), "S1uS2inv": inv_basis("S1uS2")}
INVLAB = {"S1inv": ["dJ1", "dJ2", "J3"] + [nm for nm, c in zip(names, cls) if nm in FOUR and c == "S1"],
          "S1uS2inv": ["dJ1", "dJ2", "J3", "J4"] + FOUR}

def lam_of(C, which):
    if which in SETS:
        s = SETS[which]; return releig(C[np.ix_(s, s)], G[np.ix_(s, s)])
    B = BINV[which]; return releig(B.T @ C @ B, B.T @ G @ B)

def analyse(L, spec, files):
    S = np.concatenate([np.load(f) for f in files]); N = L ** 3
    kind = spec.split(":")[0]
    mode = "full" if kind in ("cs", "pol") else "singlet"
    inv_only = kind in ("neez", "colz") or (kind == "lp" and float(spec.split(":")[1]) != 0.)
    def C_of(Ss):
        if inv_only:     # rank-0 block only (valid for S^z-conserving combos)
            E0 = Ss[:, :n]; m = E0.mean(0); C = (E0.conj().T @ E0) / len(E0) - np.outer(m.conj(), m)
            return C.real / N
        return cov_from_samples(Ss, n, mode, N)[0]
    which = (["S1inv", "S1uS2inv"] if inv_only else ["NN", "S1b", "S1", "S1uS2", "S1inv", "S1uS2inv"])
    C = C_of(S); nb = 16; bl = np.array_split(np.arange(len(S)), nb)
    print(f"\n== L={L} {spec}: {len(S)} samples from {len(files)} file(s) ==")
    ex = S[:, :n].real.mean(0) / N
    print("   <h>/site: " + " ".join(f"{nm}:{e:+.4f}" for nm, e in zip(names, ex)))
    out = {}
    for w in which:
        lam, V = lam_of(C, w)
        jk = np.array([lam_of(C_of(np.delete(S, b, axis=0)), w)[0][:3] for b in bl])
        err = np.sqrt((nb - 1) / nb * ((jk - jk.mean(0)) ** 2).sum(0)); corr = nb * lam[:3] - (nb - 1) * jk.mean(0)
        v = V[:, 0] / np.abs(V[:, 0]).max(); lab = [names[k] for k in SETS[w]] if w in SETS else INVLAB[w]
        top = sorted(range(len(v)), key=lambda q: -abs(v[q]))[:5]
        print(f"   {w:9s}: lam1 = {lam[0]:.4g} +- {err[0]:.2g} (bias-corr {corr[0]:.4g}); lam2 = {lam[1]:.4g} +- {err[1]:.2g}; "
              f"lam3 = {lam[2]:.4g} +- {err[2]:.2g} | low vec " + " ".join(f"{lab[q]}:{v[q]:+.2f}" for q in top))
        out[w] = (lam[0], err[0], corr[0], V[:, 0])
    return out

if __name__ == "__main__":
    # sanity: the invariant combinations carry no rank-1 / rank-2 parts (checked on a 6^3 table)
    T6 = Tables(cube(6), [(nm, c, "b", op) for nm, c, op in B2] + [(nm, c, "4", d4) for nm, c, d4, s_ in F4])
    B = BINV["S1uS2inv"]
    print(f"rank-1/2 content of the invariant combos: max|W1| {np.abs(np.einsum('kcp,kj->jcp', T6.W1, B)).max():.1e}, "
          f"max|W2| {np.abs(np.einsum('kmp,kj->jmp', T6.W2, B)).max():.1e}; G(6^3 cluster) vs infinite: "
          f"{np.abs(T6.gram([T6.cluster_strings(k) for k in range(n)]) - G).max():.1e}")
    res = {}
    for L in (6, 8):
        for spec in ("lp:0", "lp:0.1", "neez:0.05", "colz:0.1", "cs", "pol"):
            fs = sorted(glob.glob(f"s49_{L}_{spec}_*.npy"))
            if fs: res[(L, spec)] = analyse(L, spec, fs)
    np.save("anal49_res.npy", np.array([res], dtype=object))
