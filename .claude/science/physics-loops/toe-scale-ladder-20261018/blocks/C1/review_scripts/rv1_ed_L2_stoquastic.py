#!/usr/bin/env python3
"""Reviewer check R1 (independent of the block's lattice.py / qmc.py / driver.py / step1_stoquastic.py).

Own conventions: vertex id = x + L*y + L^2*z; link id = a*Nv + vid (link from v to v+e_a); spin b in {0,1},
sigma = 2b-1, E = sigma/2.  Gauss law with background rho: (#out-up - #in-up) = rho_v  (div E = rho).
Plaquette (a,b) at v, links (v,a)+, (v+e_a,b)+, (v+e_b,a)-, (v,b)-; flippable iff circulation = +-4.
H(g,V) = -g sum_p (U_p + U_p^dag) + V sum_p n_p on the Gauss-legal sigma^z basis.

Checks at L=2 by brute force over all 2^24 link configurations, for rho = 0 and for a staggered background
rho_v = (-1)^(x+y+z):
  - Gauss census, flip components, winding sectors;
  - every off-diagonal element of H(g) equals -g exactly (no multiplicity);
  - for g = -1 the ungauged H has positive off-diagonals; D H(g) D (D = prod_{Lambda} sigma^z) has all
    off-diagonals <= 0 for both signs of g, and D H(g) D == H(-g) exactly;
  - spectra of H(g), D H(g) D and H(-g) agree per flip component and per winding sector;
  - E0 of the canonical component and of the line-reversed (W=1) component.
Gauge Lambda: (a) the block's set {x-links y+z even} U {y-links z even}; (b) an independent GF(2) solution.
Odd-count property for L = 2..16 and GF(2) (in)solvability of delta(Lambda) = 1 for L = 2..7.
"""
import sys, time
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components

RES = []


def check(name, ok, detail=""):
    RES.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""), flush=True)


class Geo:
    def __init__(self, L):
        self.L = L
        self.Nv = L ** 3
        self.Nl = 3 * self.Nv
        self.co = np.array([(v % L, (v // L) % L, v // L ** 2) for v in range(self.Nv)])
        e = np.eye(3, dtype=int)
        self.vid = lambda c: int((c[0] % L) + L * (c[1] % L) + L * L * (c[2] % L))
        self.lid = lambda v, a: a * self.Nv + v
        pl, ori = [], []
        for v in range(self.Nv):
            c = self.co[v]
            for (a, b) in ((0, 1), (1, 2), (2, 0)):  # own orientation choice (zx instead of xz)
                pl.append([self.lid(v, a), self.lid(self.vid(c + e[a]), b), self.lid(self.vid(c + e[b]), a), self.lid(v, b)])
                ori.append((a, b))
        self.pl = np.array(pl)
        self.ori = ori
        self.sg = np.array([1, 1, -1, -1])
        self.out = [[self.lid(v, a) for a in range(3)] for v in range(self.Nv)]
        self.inn = [[self.lid(self.vid(self.co[v] - e[a]), a) for a in range(3)] for v in range(self.Nv)]

    def lam_block(self):
        lam = np.zeros(self.Nl, bool)
        for v in range(self.Nv):
            x, y, z = self.co[v]
            lam[self.lid(v, 0)] = (y + z) % 2 == 0
            lam[self.lid(v, 1)] = z % 2 == 0
        return lam


def gf2_solve(M, rhs):
    """Solve M x = rhs over GF(2); return x or None."""
    M = M.copy().astype(np.uint8) % 2
    r = rhs.copy().astype(np.uint8) % 2
    m, n = M.shape
    piv = []
    row = 0
    for col in range(n):
        if row >= m:
            break
        nz = np.flatnonzero(M[row:, col])
        if len(nz) == 0:
            continue
        k = row + nz[0]
        if k != row:
            M[[row, k]] = M[[k, row]]
            r[[row, k]] = r[[k, row]]
        hit = np.flatnonzero(M[:, col])
        hit = hit[hit != row]
        M[hit] ^= M[row]
        r[hit] ^= r[row]
        piv.append(col)
        row += 1
    if np.any(r[row:]):
        return None, row
    x = np.zeros(n, np.uint8)
    for i, col in enumerate(piv):
        x[col] = r[i]
    return x, row


# ---------------- combinatorial part, L = 2..16 ----------------
for L in range(2, 17):
    G = Geo(L)
    sets = {tuple(sorted(p)) for p in G.pl}
    distinct = len(sets) == len(G.pl)
    if L % 2 == 0:
        lam = G.lam_block()
        cnt = lam[G.pl].sum(axis=1)
        check(f"L={L}: plaquette link sets distinct, block Lambda meets every plaquette an odd number of times",
              distinct and np.all(cnt % 2 == 1), f"{len(G.pl)} plaquettes, counts {sorted(set(cnt.tolist()))}")
    else:
        check(f"L={L}: plaquette link sets distinct", distinct)
for L in range(2, 8):
    G = Geo(L)
    M = np.zeros((len(G.pl), G.Nl), np.uint8)
    for i, p in enumerate(G.pl):
        M[i, p] = 1
    x, rk = gf2_solve(M, np.ones(len(G.pl), np.uint8))
    if L % 2 == 0:
        ok = x is not None and np.all(M.astype(int) @ x % 2 == 1)
        check(f"L={L}: independent GF(2) solve of delta(Lambda)=1 succeeds (even L)", ok, f"rank {rk}")
    else:
        check(f"L={L}: GF(2) delta(Lambda)=1 has no solution (odd L)", x is None, f"rank {rk}")

# ---------------- exact L = 2 ----------------
L = 2
G = Geo(L)
t0 = time.time()
allc = np.arange(2 ** G.Nl, dtype=np.uint32)
bits = [((allc >> np.uint32(l)) & np.uint32(1)).astype(np.int8) for l in range(G.Nl)]


def gauss_states(rho):
    ok = np.ones(len(allc), bool)
    for v in range(G.Nv):
        d = sum(bits[l] for l in G.out[v]) - sum(bits[l] for l in G.inn[v])
        ok &= d == rho[v]
    return allc[ok]


def sig_of(states):
    return np.array([((states >> np.uint32(l)) & np.uint32(1)).astype(np.int64) * 2 - 1 for l in range(G.Nl)]).T


def build(states):
    S = sig_of(states)
    circ = (S[:, G.pl] * G.sg).sum(axis=2)
    flip = np.abs(circ) == 4
    masks = np.array([sum(1 << int(l) for l in p) for p in G.pl], dtype=np.uint32)
    rows, cols = [], []
    for p in range(len(G.pl)):
        i = np.flatnonzero(flip[:, p])
        t = states[i] ^ masks[p]
        j = np.searchsorted(states, t)
        assert np.all(states[j] == t)  # flips preserve Gauss law
        rows.append(i)
        cols.append(j)
    rows = np.concatenate(rows)
    cols = np.concatenate(cols)
    A = coo_matrix((np.ones(len(rows)), (rows, cols)), shape=(len(states), len(states))).tocsr()
    A.sum_duplicates()
    Nf = flip.sum(axis=1).astype(float)
    W = np.array([[S[:, [G.lid(v, a) for v in range(G.Nv) if G.co[v][a] == 0]].sum(axis=1)] for a in range(3)])[:, 0].T
    return S, A, Nf, W


def lam_gf2():
    M = np.zeros((len(G.pl), G.Nl), np.uint8)
    for i, p in enumerate(G.pl):
        M[i, p] = 1
    x, _ = gf2_solve(M, np.ones(len(G.pl), np.uint8))
    return x.astype(bool)


lams = {"block Lambda": G.lam_block(), "own GF(2) Lambda": lam_gf2()}
canon = np.zeros(G.Nl, int)
for v in range(G.Nv):
    x, y, z = G.co[v]
    canon[G.lid(v, 0)] = (-1) ** y
    canon[G.lid(v, 1)] = (-1) ** x
    canon[G.lid(v, 2)] = (-1) ** x
w1 = canon.copy()
for x in range(L):
    w1[G.lid(G.vid((x, 0, 0)), 0)] *= -1


def code(sig):
    return np.uint32(sum(1 << l for l in range(G.Nl) if sig[l] == 1))


for bgname, rho in (("rho=0", np.zeros(G.Nv, int)),
                    ("staggered rho=(-1)^(x+y+z)", np.array([(-1) ** int(c.sum()) for c in G.co]))):
    st = gauss_states(rho)
    S, A, Nf, W = build(st)
    ncomp, lab = connected_components(A, directed=False)
    sizes = np.bincount(lab)
    sectors = {tuple(w) for w in W}
    Ac = A.tocoo()
    offd = Ac.row != Ac.col
    offvals = set(np.unique(Ac.data[offd]).tolist())
    diag_zero = not np.any(Ac.row == Ac.col)
    check(f"L=2 {bgname}: census", True, f"{len(st)} Gauss states, {ncomp} flip components, largest {sizes.max()}, "
          f"{len(sectors)} winding sectors (sigma-flux)")
    check(f"L=2 {bgname}: adjacency entries in {{0,1}} (no multiplicity), symmetric, no diagonal",
          offvals <= {1.0} and abs(A - A.T).max() == 0 and diag_zero, f"values {sorted(offvals)}")
    wconst = all(len({tuple(w) for w in W[lab == c]}) == 1 for c in range(ncomp))
    check(f"L=2 {bgname}: winding constant on every flip component", wconst)
    blocks = [np.flatnonzero(lab == c) for c in range(ncomp)]
    sblocks = [np.flatnonzero(np.all(W == np.array(sct), axis=1)) for sct in sectors]
    for lname, lam in lams.items():
        dsign = np.prod(np.where(lam[None, :], S, 1), axis=1).astype(float)  # D = prod_{l in Lambda} sigma^z_l
        prod_edges = dsign[Ac.row] * dsign[Ac.col]
        for V in (0.0, 0.5, 0.9):
            worst_off = []
            maxspec = 0.0
            for g in (1.0, -1.0):
                off_orig = -g * Ac.data            # off-diagonal elements of H(g)
                off_gauged = -g * Ac.data * prod_edges  # off-diagonal elements of D H(g) D
                off_minus = +g * Ac.data           # off-diagonal elements of H(-g)
                worst_off.append((g, off_orig.max(), off_gauged.max(), np.abs(off_gauged - off_minus).max()))
                for idx in blocks + sblocks:
                    Ab = A[idx][:, idx].toarray()
                    H = V * np.diag(Nf[idx]) - g * Ab
                    db = dsign[idx]
                    Hg = db[:, None] * H * db[None, :]
                    Hm = V * np.diag(Nf[idx]) + g * Ab
                    e1 = np.linalg.eigvalsh(H); e2 = np.linalg.eigvalsh(Hg); e3 = np.linalg.eigvalsh(Hm)
                    maxspec = max(maxspec, np.abs(e1 - e2).max(), np.abs(e1 - e3).max())
            gneg = [w for w in worst_off if w[0] < 0][0]
            maxdiff = max(w[3] for w in worst_off)
            ok = all(w[2] <= 0 for w in worst_off) and gneg[1] > 0 and maxdiff == 0.0 and maxspec < 1e-10
            check(f"L=2 {bgname} {lname} V={V}: D H(g) D has all off-diagonals <= 0 for g=+-1; ungauged H(-1) has "
                  f"max off-diagonal {gneg[1]:+.0f}; D H(g) D == H(-g) exactly; spectra equal per component and per sector",
                  ok, f"max off-diag of DH(g)D for g=+1,-1: {[w[2] for w in worst_off]}, max|DHD-H(-g)| {maxdiff}, max |dE| {maxspec:.1e}")
    if bgname == "rho=0":
        ic = np.searchsorted(st, code(canon))
        iw = np.searchsorted(st, code(w1))
        assert st[ic] == code(canon) and st[iw] == code(w1)
        res = {}
        for V in (0.0, 0.5, 0.9):
            out = []
            for i in (ic, iw):
                idx = np.flatnonzero(lab == lab[i])
                H = V * np.diag(Nf[idx]) - A[idx][:, idx].toarray()
                out.append((len(idx), np.linalg.eigvalsh(H)[0], tuple(W[i])))
            res[V] = out
            sec0 = np.flatnonzero(np.all(W == W[ic], axis=1))
            e_sec = np.linalg.eigvalsh(V * np.diag(Nf[sec0]) - A[sec0][:, sec0].toarray())[0]
            print(f"[INFO] V={V}: canonical comp size {out[0][0]} W={out[0][2]} E0={out[0][1]:.10f}; "
                  f"line-reversed comp size {out[1][0]} W={out[1][2]} E0={out[1][1]:.10f}; dE={out[1][1]-out[0][1]:.10f}; "
                  f"whole W=0 sector ({len(sec0)} states) E0={e_sec:.10f}", flush=True)
        check("L=2 rho=0: canonical component 864 states, E0(V=0) = -9.0267209135; W=1 component 464, E0 = -7.3991109799",
              res[0.0][0][0] == 864 and abs(res[0.0][0][1] + 9.0267209135) < 1e-9 and res[0.0][1][0] == 464
              and abs(res[0.0][1][1] + 7.3991109799) < 1e-9 and res[0.0][0][2] != res[0.0][1][2])
        check("L=2 rho=0: exact dE(V=0.5) = 0.7314577591 (block value)", abs(res[0.5][1][1] - res[0.5][0][1] - 0.7314577591) < 1e-9)
print(f"elapsed {time.time()-t0:.1f}s")
print(f"TOTAL: PASS={sum(RES)} FAIL={len(RES)-sum(RES)}")
