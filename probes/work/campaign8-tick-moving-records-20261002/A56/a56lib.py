"""A56 library (supplied toys; nothing adopted).  Open blocks made of 2x2x2 cubes under A51's rules (rules51_6.npz),
restricted exactly as A53's t2_blocks: two-place class terms with both sites inside, star four-spin sets with all four
sites inside (a53lib.bilinear_pairs / four_sets with an open index).  Fast kernel: four-sets applied by 4-bit pattern
tables, their single-pair flips merged into the pair coefficients (as a53lib._matvec does for stars); all four-site
flips of one set are the same move.  Cross-checked against a53lib._matvec_gen in chk56.py."""
import sys, itertools, numpy as np
D56 = __file__.rsplit('/', 1)[0]
sys.path.insert(0, D56.rsplit('/', 1)[0] + "/A53")
from a53lib import *                      # noqa  (load_rule, bilinear_pairs, four_sets, Sector, GenHam, paircorr, ...)
from a53lib import _rank, _matvec_gen
import numba as nb

BLOCKS = {                                # cube positions (cube = 2x2x2 sites at 2*pos + {0,1}^3)
    'cube': [(0, 0, 0)],
    'line2': [(0, 0, 0), (0, 0, 1)],      # 2x2x4 (A53's block (2,2,4))
    'line3': [(0, 0, 0), (0, 0, 1), (0, 0, 2)],          # 2x2x6
    'L3': [(0, 0, 0), (1, 0, 0), (0, 1, 0)],             # three cubes in an L
    'edge2': [(0, 0, 0), (1, 1, 0)],      # two cubes sharing an edge
    'corner2': [(0, 0, 0), (1, 1, 1)],    # two cubes sharing a corner
    'far2': [(0, 0, 0), (0, 0, 2)],       # two cubes with one cube-gap between them
    'tri_eee': [(0, 0, 0), (1, 1, 0), (1, 0, 1)],        # three cubes pairwise edge-sharing (around one corner site)
    'bent_fe': [(0, 0, 0), (1, 0, 0), (2, 1, 0)],        # face pair + edge pair, ends uncoupled
    'fek': [(0, 0, 0), (1, 0, 0), (1, 1, 1)],            # face + edge at the middle cube, ends share a corner
    'ee90': [(0, 1, 0), (1, 2, 0), (1, 0, 0)],           # two edge contacts at 90 deg, ends uncoupled
    'ee120': [(1, 0, 0), (2, 1, 0), (0, 0, 1)],          # two edge contacts at 120 deg, ends uncoupled
    'ee180': [(0, 0, 0), (1, 1, 0), (2, 2, 0)],          # two edge contacts collinear, ends uncoupled
}


def block_sites(name):
    cps = BLOCKS[name]; out = []
    for c in cps:
        for o in itertools.product(range(2), repeat=3):
            out.append(np.array([2 * c[a] + o[a] for a in range(3)]))
    return out, [n // 8 for n in range(len(out))]          # sites, cube id of each site


def block_terms(name, L=6, key='B4_inner'):
    ks, J, c4 = load_rule(L, key)
    X, cid = block_sites(name); fo = open_index(X)
    return X, cid, bilinear_pairs(X, fo, ks, J), four_sets(X, fo, c4)


LP6 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


class TabHam:
    def __init__(self, pairs, fours, N):
        allp = dict(pairs)
        for S in fours:
            for a, b in LP6: allp.setdefault((S[a], S[b]), 0.)
        pk = sorted(allp); self.pidx = {p: n for n, p in enumerate(pk)}; self.N = N
        self.pm = np.array([(1 << i) | (1 << j) for i, j in pk], np.int64); self.pJ = np.array([allp[p] for p in pk], float)
        self.Jsum = float(self.pJ.sum())
        fk = sorted(fours); nf = len(fk)
        self.fs = np.array(fk, np.int64).reshape(-1, 4)
        self.gp = np.array([[self.pidx[(S[a], S[b])] for a, b in LP6] for S in fk], np.int64).reshape(-1, 6)
        self.fm = np.array([sum(1 << int(s) for s in S) for S in fk], np.int64)
        TD = np.zeros((nf, 16)); TP = np.zeros((nf, 16, 6)); TF = np.zeros((nf, 16))
        for q, S in enumerate(fk):
            w = fours[S]
            for pat in range(16):
                b = [(pat >> t) & 1 for t in range(4)]; z = [1 - 2 * v for v in b]
                TD[q, pat] = w.sum() * z[0] * z[1] * z[2] * z[3]
                for pi, ((u, v), (x, y)) in enumerate(PAIRINGS):
                    if b[u] != b[v]: TP[q, pat, LP6.index((u, v))] += 2 * w[pi] * z[x] * z[y]
                    if b[x] != b[y]: TP[q, pat, LP6.index((x, y))] += 2 * w[pi] * z[u] * z[v]
                    if b[u] != b[v] and b[x] != b[y]: TF[q, pat] += 4 * w[pi]
        self.TD, self.TP, self.TF = TD, TP, TF


@nb.njit(cache=True)
def _matvec_tab(x, y, confs, offset, idxlo, h, lomask, flip, top, full, pm, pJ, Jsum, fs, gp, fm, TD, TP, TF):
    npair = len(pm); nf = fs.shape[0]; coef = np.empty(npair)
    for k in range(len(confs)):
        c = confs[k]
        for p in range(npair): coef[p] = 2. * pJ[p]
        dg = Jsum; acc = 0.
        for q in range(nf):
            pat = ((c >> fs[q, 0]) & 1) | (((c >> fs[q, 1]) & 1) << 1) | (((c >> fs[q, 2]) & 1) << 2) | (((c >> fs[q, 3]) & 1) << 3)
            dg += TD[q, pat]
            for l in range(6):
                v = TP[q, pat, l]
                if v != 0.: coef[gp[q, l]] += v
            v = TF[q, pat]
            if v != 0.: acc += v * x[_rank(c ^ fm[q], offset, idxlo, h, lomask, flip, top, full)]
        for p in range(npair):
            m = pm[p]; cm = c & m
            if cm != 0 and cm != m:
                dg -= 2. * pJ[p]
                acc += coef[p] * x[_rank(c ^ m, offset, idxlo, h, lomask, flip, top, full)]
        y[k] = acc + dg * x[k]


def make_mv_tab(H, S):
    def mv(x):
        x = np.ascontiguousarray(np.asarray(x, dtype=np.float64).ravel()); y = np.empty_like(x)
        _matvec_tab(x, y, S.confs, S.offset, S.idxlo, S.h, S.lomask, S.flip, S.top, S.full, H.pm, H.pJ, H.Jsum,
                    H.fs, H.gp, H.fm, H.TD, H.TP, H.TF)
        return y
    return mv


@nb.njit(cache=True)
def _add_products(x, sites, amps, offset, idxlo, h, lomask, flip, top, full):
    """x[rank(c)] += amp for every config c of a product of singlet pairs (sites[2k], sites[2k+1]); top-bit-0 reps only."""
    npr = len(sites) // 2
    for r in range(1 << npr):
        c = 0; sg = 1.
        for k in range(npr):
            if (r >> k) & 1:
                c |= 1 << sites[2 * k]; sg = -sg          # first site down
            else:
                c |= 1 << sites[2 * k + 1]
        if flip and (c >> top) & 1: continue
        x[_rank(c, offset, idxlo, h, lomask, flip, top, full)] += sg * amps


def random_singlet(S, K=24, seed=20261004):
    """Sum of K random perfect pairings (products of singlets) with random weights: an exact S = 0 state, generic in
    every spatial symmetry sector.  Normalized."""
    rng = np.random.default_rng(seed); x = np.zeros(S.D)
    for _ in range(K):
        perm = rng.permutation(S.N).astype(np.int64)
        _add_products(x, perm, rng.standard_normal(), S.offset, S.idxlo, S.h, S.lomask, S.flip, S.top, S.full)
    return x / np.linalg.norm(x)


def cube_gs(L, key):
    """Exact S = 0 ground state of the restricted rule on one cube, as a dict {8-bit config: amplitude}; and spectrum."""
    X, cid, pairs, fours = block_terms('cube', L, key)
    S = Sector(8, flip=False); H = TabHam(pairs, fours, 8); mv = make_mv_tab(H, S)
    M = dense_matrix(mv, S.D); w, U = np.linalg.eigh(M)
    sing = [q for q in range(S.D) if abs(paircorr(U[:, q], S).sum()) < 1e-8]
    q0 = sing[0]
    return {int(c): U[k, q0] for k, c in enumerate(S.confs)}, w, sing, w[q0]


@nb.njit(cache=True)
def _cube_product(confs, ncube, ca, out):
    for k in range(len(confs)):
        c = confs[k]; a = 1.
        for b in range(ncube):
            sub = (c >> (8 * b)) & 255
            a *= ca[sub]
            if a == 0.: break
        out[k] = a


def cube_product(S, ncube, gsd):
    ca = np.zeros(256)
    for c, a in gsd.items(): ca[c] = a
    out = np.zeros(S.D); _cube_product(S.confs, ncube, ca, out)
    return out / np.linalg.norm(out)
