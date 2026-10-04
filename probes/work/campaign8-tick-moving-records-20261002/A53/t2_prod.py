"""A53 t2_prod: EXACT energies of cluster-singlet product states on the L^3 torus under A51's rules.
Tiling by translates of a block (bx,by,bz) (block sizes dividing L).  Every cluster in the same SU(2)-singlet state psi.
For singlet clusters (EXACT algebra):
  - bilinears between different clusters vanish (<s_i^a>_A = 0);
  - four-spin (s_a.s_b)(s_c.s_d) with a 2+2 split over clusters A, B:
        pairing inside the split   -> <s_a.s_b>_A <s_c.s_d>_B
        pairing across the split   -> (1/3) <s_a.s_c>_A <s_b.s_d>_B     (<s^al_a s^be_c> = delta <s_a.s_c>/3)
  - splits 3+1, 2+1+1, 1+1+1+1 vanish.
So E/N = [<H_A> + sum_t m_t C[a_t,b_t] C[c_t,d_t]] / n_block, C = correlation matrix of psi.  psi is optimized
self-consistently: psi <- lowest singlet of H_eff = H_A + sum_ab dE_int/dC_ab s_a.s_b (exact E tracked; best kept).
Brute-force control: the factorization is checked against the exact <H> of the product state on a 16-site open
cluster made of two blocks.  Usage: t2_prod.py L KEY blocks(e.g. 211,221,222)"""
import sys, signal, time, numpy as np, scipy.sparse.linalg as sla
signal.alarm(285)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a53lib import *
t0 = time.time()


def lowest_singlets(pairs, fours, n, k=6):
    """lowest S=0 eigenpairs of the open-cluster rule (pairs/fours in local indices)."""
    H = GenHam(pairs, fours, n); S = Sector(n, flip=(n % 4 == 0)); mv = make_mv_gen(H, S)
    if S.D <= 400:
        w, U = np.linalg.eigh(dense_matrix(mv, S.D)); cand = range(S.D)
    else:
        op = sla.LinearOperator((S.D, S.D), matvec=mv, dtype=float)
        w, U = sla.eigsh(op, k=min(k, S.D - 2), which='SA', tol=1e-10); o = np.argsort(w); w, U = w[o], U[:, o]; cand = range(len(w))
    out = []
    for q in cand:
        C = paircorr(U[:, q], S)
        if abs(C.sum()) < 1e-6: out.append((w[q], U[:, q], C))
        if len(out) >= 2: break
    return out, S, mv


def setup(L, key, block):
    cl = cube(L); X = [np.array(s) for s in cl.sites]; f = periodic_index(cl); N = cl.N
    ks, J, c4 = load_rule(L, key)
    pairs = bilinear_pairs(X, f, ks, J); fours = four_sets(X, f, c4)
    B = np.array(block); nb = int(np.prod(B)); ncl = N // nb
    lc = {o: n for n, o in enumerate(itertools.product(*[range(b) for b in B]))}
    cid = [tuple(np.array(x) // B) for x in cl.sites]; loc = [lc[tuple(np.array(x) % B)] for x in cl.sites]
    HP, HF, inter = {}, {}, {}
    for (i, j), Jv in pairs.items():
        if cid[i] == cid[j]:
            k = (min(loc[i], loc[j]), max(loc[i], loc[j])); HP[k] = HP.get(k, 0.) + Jv / ncl
    for Sg, w in fours.items():
        c = [cid[s] for s in Sg]; l = [loc[s] for s in Sg]
        if len(set(c)) == 1:
            o = sorted(range(4), key=lambda q: l[q]); key4 = tuple(l[q] for q in o); inv = {o[q]: q for q in range(4)}
            acc = HF.setdefault(key4, np.zeros(3))
            for pi, ((u, v), (x, y)) in enumerate(PAIRINGS):
                pr = tuple(sorted(tuple(sorted((inv[a], inv[b]))) for a, b in ((u, v), (x, y))))
                acc[PAIRINGS.index(pr)] += w[pi] / ncl
        elif len(set(c)) == 2 and sorted([c.count(z) for z in set(c)]) == [2, 2]:
            for pi, ((u, v), (x, y)) in enumerate(PAIRINGS):
                if c[u] == c[v]:
                    t = (min(l[u], l[v]), max(l[u], l[v]), min(l[x], l[y]), max(l[x], l[y])); fac = 1.
                else:
                    xa = x if c[x] == c[u] else y; yb = y if xa == x else x
                    t = (min(l[u], l[xa]), max(l[u], l[xa]), min(l[v], l[yb]), max(l[v], l[yb])); fac = 1. / 3.
                inter[t] = inter.get(t, 0.) + fac * w[pi] / ncl
    return HP, HF, inter, nb


def e_int(inter, C):
    return sum(m * C[a, b] * C[c, d] for (a, b, c, d), m in inter.items())


def grad(inter, nb, C):
    G = {}
    for (a, b, c, d), m in inter.items():
        G[(a, b)] = G.get((a, b), 0.) + m * C[c, d]; G[(c, d)] = G.get((c, d), 0.) + m * C[a, b]
    return G


def optimize(HP, HF, inter, nb, iters=40, eta=0.6):
    sing, S, mvA = lowest_singlets(HP, HF, nb)
    E0, psi, C = sing[0]; best = (E0 + e_int(inter, C), E0, psi, C, 0); hist = [best[0]]
    Cm = C.copy()
    for it in range(1, iters + 1):
        G = grad(inter, nb, Cm); P = dict(HP)
        for k, g in G.items(): P[k] = P.get(k, 0.) + g
        s2, S2, _ = lowest_singlets(P, HF, nb)
        if not s2: break
        _, psi2, C2 = s2[0]; Ea = psi2 @ mvA(psi2) / (psi2 @ psi2); Et = Ea + e_int(inter, C2); hist.append(Et)
        if Et < best[0] - 1e-13: best = (Et, Ea, psi2, C2, it)
        Cn = (1 - eta) * Cm + eta * C2
        if np.abs(Cn - Cm).max() < 1e-10: break
        Cm = Cn
    return best, hist, sing


if __name__ == "__main__":
    L, key = int(sys.argv[1]), sys.argv[2]; blocks = [tuple(int(c) for c in b) for b in sys.argv[3].split(",")]
    ref = {(6, "B4_inner"): -1.72680, (8, "B4_inner"): -1.69469, (10, "B4_inner"): -1.66264}.get((L, key))
    print(f"L={L} rule {key}; parton VMC E/N (A51) {ref}", flush=True)
    for blk in blocks:
        HP, HF, inter, nb = setup(L, key, blk)
        best, hist, sing = optimize(HP, HF, inter, nb)
        Ebest, Ea, psi, C, it = best
        print(f" block {blk} (n={nb}): restricted-rule singlet GS E_A/n {sing[0][0]/nb:+.5f} -> product E/N {hist[0]/nb:+.5f}; "
              f"self-consistent best E/N {Ebest/nb:+.6f} (iter {it}; intra {Ea/nb:+.5f}, inter {(Ebest-Ea)/nb:+.5f}); "
              f"n_inter_terms {len(inter)}; E-history/N first..last {hist[0]/nb:+.5f}..{hist[-1]/nb:+.5f} ({len(hist)-1} it)"
              + (f"; vs parton {Ebest/nb - ref:+.5f}" if ref else "") + f"  [{time.time()-t0:.0f}s]", flush=True)
        np.save(f"prod_L{L}_{key}_{''.join(map(str, blk))}.npy", psi)
