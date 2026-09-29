#!/usr/bin/env python3
"""J:falsifier:PR9316 -- independent reconstruction of the cubic one-pair sector of the actual-first-birth band note.

Own code from the note's definitions only (Z^3, A even / B odd, hard-core charges q in {+1, 0, -1} with vacuum q_A = 1, integer fields E_ab on A->B edges, Gauss div E = q - 1_A,
D = sum_{a->b, q_b = 0} E (E - q_a); F_{a->b} moves q_a to an empty neighbour b and lowers E_ab by q_a; H4 = -2 sum over unordered overlapping A pairs of (F_c F_a P)^* (F_c F_a P);
H0 = P0 H4 P0 with P0 the D = 0 projector).  Nothing from the note's runner.  Steps:
  1. breadth-first closure of the coordinate component of the seed word s0 (negative A at 0, positive B at e1, e2, E_(0,e1) = E_(0,e2) = -1) modulo even translations, with all matrix elements of
     H_rel = H0 + 618 N computed exactly from the definition (the far-pair vacuum scalar is subtracted for every interacting pair);
  2. compare with the note: 11,322 relative words (11,292 negative on A, 30 on B), 652,416 directed displacement edges, Hermiticity, nonpositive off-diagonal entries, |E| <= 1, M = 14128,
     771 + 10,551 words by field-edge count, k = 0 ground energy -984.0424902429624 and next gap 483.0003432, band stiffness alpha = 115.61964849312 (Richardson from finite differences),
     first-vector k = 0 weights .05154396 / .02963861 / .07967697, the seven-step fixture entries -2, -4, -2, -186 x 4, the next-birth coefficient -186 and the 3 x 5 matrix giving -372.
"""
import math, sys, time, itertools
from collections import defaultdict
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh
from multiprocessing import Pool

PASS = FAIL = 0; HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1; HITS.append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}", flush=True)

import itertools, sys, time
from collections import defaultdict

DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
def add(s, d): return (s[0] + d[0], s[1] + d[1], s[2] + d[2])
def is_A(s): return (s[0] + s[1] + s[2]) % 2 == 0
def nbrs(s): return [add(s, d) for d in DIRS]
def vac_q(s): return 1 if is_A(s) else 0

class W:
    """word = charges deviating from the vacuum and non-zero fields; immutable tuple form for hashing."""
    __slots__ = ("Q", "E")
    def __init__(self, Q, E): self.Q, self.E = Q, E

def pack(Qd, Ed):
    return (tuple(sorted(Qd.items())), tuple(sorted((k, v) for k, v in Ed.items() if v != 0)))
def unpack(w):
    return dict(w[0]), dict(w[1])
def qget(Qd, s): return Qd.get(s, vac_q(s))
def edge(a, b): return (a, b) if is_A(a) else (b, a)

def F_move(Qd, Ed, a, b):
    """F_{a->b}: requires q_a != 0 and q_b == 0 (a in A, b in B)."""
    qa = qget(Qd, a)
    if qa == 0 or qget(Qd, b) != 0: return False
    Qd[b] = qa; Qd[a] = 0
    Ed[(a, b)] = Ed.get((a, b), 0) - qa
    return True
def F_adj(Qd, Ed, a, b):
    """adjoint: requires q_a == 0 and q_b != 0; moves the particle from b back to a."""
    qb = qget(Qd, b)
    if qget(Qd, a) != 0 or qb == 0: return False
    Qd[a] = qb; Qd[b] = 0
    Ed[(a, b)] = Ed.get((a, b), 0) + qb
    return True
def clean(Qd):
    for s in [s for s, q in Qd.items() if q == vac_q(s)]: del Qd[s]

def D_of(Qd, Ed):
    D = 0
    for (a, b), e in Ed.items():
        if e != 0 and qget(Qd, b) == 0: D += e * (e - qget(Qd, a))
    return D
def valid(Qd, Ed):
    # all A occupied, Gauss law, D = 0
    for s, q in Qd.items():
        if is_A(s) and q == 0: return False
    # Gauss: recompute divergences on the touched sites
    div = defaultdict(int)
    for (a, b), e in Ed.items():
        div[a] += e; div[b] -= e
    sites = set(div) | set(Qd)
    for s in sites:
        q = qget(Qd, s)
        if div.get(s, 0) != q - (1 if is_A(s) else 0): return False
    return D_of(Qd, Ed) == 0

def shared(a, c):
    return len(set(nbrs(a)) & set(nbrs(c)))

def H4_row(word, want_D=False):
    """Returns dict target-word -> coefficient of (H4 - vacuum scalar over interacting pairs) applied to `word`, before the -2, restricted to D=0 targets (P0)."""
    Q0, E0 = unpack(word)
    occB = [s for s, q in Q0.items() if (not is_A(s)) and q != 0]
    neg = [s for s, q in Q0.items() if q == -1]
    Aint = set()
    for s in neg:
        if is_A(s): Aint.add(s)
    for (a, b), e in E0.items(): Aint.add(a)
    for o in occB:
        for n in nbrs(o): Aint.add(n)
    pairs = set()
    for a in Aint:
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                for dz in range(-2, 3):
                    c = (a[0] + dx, a[1] + dy, a[2] + dz)
                    if c != a and is_A(c) and shared(a, c) > 0:
                        pairs.add((a, c) if a < c else (c, a))
    out = defaultdict(int); vac_total = 0
    for (a, c) in pairs:
        vac_total += 36 - shared(a, c)
        Na, Nc = nbrs(a), nbrs(c)
        for b in Na:
            Q1 = dict(Q0); E1 = dict(E0)
            if not F_move(Q1, E1, a, b): continue
            for b2 in Nc:
                Q2 = dict(Q1); E2 = dict(E1)
                if not F_move(Q2, E2, c, b2): continue
                for d2 in Nc:
                    Q3 = dict(Q2); E3 = dict(E2)
                    if not F_adj(Q3, E3, c, d2): continue
                    for d in Na:
                        if d == d2: continue
                        Q4 = dict(Q3); E4 = dict(E3)
                        if not F_adj(Q4, E4, a, d): continue
                        clean(Q4)
                        if valid(Q4, E4): out[pack(Q4, E4)] += 1
    return out, vac_total

E1 = (1, 0, 0)
def translate(w, t):
    Qd, Ed = unpack(w)
    Q2 = {(s[0] - t[0], s[1] - t[1], s[2] - t[2]): q for s, q in Qd.items()}
    E2 = {((a[0] - t[0], a[1] - t[1], a[2] - t[2]), (b[0] - t[0], b[1] - t[1], b[2] - t[2])): e for (a, b), e in Ed.items()}
    return pack(Q2, E2)
def neg_site(w):
    for s, q in w[0]:
        if q == -1: return s
    raise ValueError("no negative particle")
def anchor_of(n):
    return (0, 0, 0) if is_A(n) else E1
def canon(w):
    n = neg_site(w); anc = anchor_of(n)
    t = (n[0] - anc[0], n[1] - anc[1], n[2] - anc[2])
    return translate(w, t), t                     # raw = T_t(canonical)

def row_of(w):
    """canonical word -> {(canonical target, t): stencil coefficient H_rel = -2 (count - vac delta)}"""
    row, vac = H4_row(w)
    out = {}
    for tgt, cnt in row.items():
        cw, t = canon(tgt)
        key = (cw, t)
        if cw == w and t == (0, 0, 0): out[key] = out.get(key, 0) - 2 * (cnt - vac)
        else: out[key] = out.get(key, 0) - 2 * cnt
    if (w, (0, 0, 0)) not in out: out[(w, (0, 0, 0))] = -2 * (0 - vac)
    return out


def main():
    T0 = time.time()
    e1, e2 = (1, 0, 0), (0, 1, 0)
    check("vacuum scalar: 36 - (shared B neighbours) = 35 for A partners at distance 2 along an axis and 34 for face-diagonal partners, so -2 * (N/2) * (6*35 + 12*34) = -618 N",
          all(36 - shared((0, 0, 0), c_) == v for c_, v in (((2, 0, 0), 35), ((1, 1, 0), 34))) and 2 * (6 * 35 + 12 * 34) == 1236 and 1236 // 2 == 618)
    s0 = pack({(0, 0, 0): -1, e1: 1, e2: 1}, {((0, 0, 0), e1): -1, ((0, 0, 0), e2): -1})
    check("the seed word s0 satisfies all A occupied, Gauss and D = 0", valid(*unpack(s0)))
    words = {s0: 0}; order = [s0]; rows = {}; frontier = [s0]; layer = 0
    with Pool(min(9, max(2, (__import__("os").cpu_count() or 4) - 1))) as pool:
        while frontier:
            res = pool.map(row_of, frontier, chunksize=4)
            nxt = []
            for w, r in zip(frontier, res):
                rows[w] = r
                for (cw, t) in r:
                    if cw not in words: words[cw] = len(order); order.append(cw); nxt.append(cw)
            layer += 1
            print(f"   layer {layer}: frontier {len(frontier)} -> new {len(nxt)}; total {len(order)}; {time.time()-T0:.0f}s", flush=True)
            frontier = nxt
    idx = {w: i for i, w in enumerate(order)}; n = len(order)
    nA = sum(1 for w in order if is_A(neg_site(w))); nB = n - nA
    check("the closed quotient has 11322 relative words: 11292 with the negative particle on A and 30 on B", (n, nA, nB) == (11322, 11292, 30), f"{n} = {nA} + {nB}")
    entries = []; edges = 0
    for w, r in rows.items():
        i = idx[w]
        for (cw, t), v in r.items():
            if v == 0: continue
            j = idx[cw]
            if not (i == j and t == (0, 0, 0)): edges += 1
            entries.append((i, j, t, v))
    check("652416 directed displacement edges (including i = j when t != 0)", edges == 652416, f"{edges}")
    lookup = {(i, j, t): v for i, j, t, v in entries}
    check("reverse-displacement Hermitian: H_ij(t) = H_ji(-t) for every entry", all(lookup.get((j, i, (-t[0], -t[1], -t[2]))) == v for (i, j, t), v in lookup.items()))
    check("all off-diagonal real-space hopping coefficients are nonpositive (each is -2 times a nonnegative path count)", all(v <= 0 for (i, j, t), v in lookup.items() if not (i == j and t == (0, 0, 0))))
    check("every word has |E| <= 1 on every edge (invariant box)", max(abs(v) for w in order for k, v in w[1]) == 1)
    nz = [len(w[1]) for w in order]
    check("771 words have at most four nonzero field edges and 10551 have more (the Schur partition P, Q)", (sum(1 for x in nz if x <= 4), sum(1 for x in nz if x > 4)) == (771, 10551))
    absrow = np.zeros(n)
    for i, j, t, v in entries: absrow[i] += abs(v)
    check("maximum absolute row sum of the full stencil M = 14128", absrow.max() == 14128, f"{absrow.max():.0f}")
    r_ = [e[0] for e in entries]; c_ = [e[1] for e in entries]; v_ = [e[3] for e in entries]
    A0 = sp.csr_matrix((v_, (r_, c_)), shape=(n, n), dtype=float)
    ev, vec = eigsh(A0, k=3, which="SA", tol=1e-13); order_ = np.argsort(ev); ev = ev[order_]; vec = vec[:, order_]
    check("k = 0 fiber: lowest eigenvalue -984.0424902429624 (to 1e-9) and next gap 483.0003432", abs(ev[0] + 984.0424902429624) < 1e-9 and abs((ev[1] - ev[0]) - 483.0003432) < 5e-8, f"{ev[0]:.13f}, next {ev[1]:.7f}, gap {ev[1]-ev[0]:.7f}")
    v0 = vec[:, 0] / np.linalg.norm(vec[:, 0]); v0 = v0 * np.sign(v0[0])
    check("the ground vector is strictly positive (Perron-Frobenius)", bool((v0 > 0).all()))
    def lam(k):
        ph = np.array([np.exp(1j * (k[0] * t[0] + k[1] * t[1] + k[2] * t[2])) for i, j, t, v in entries])
        return eigsh(sp.csr_matrix((np.array(v_) * ph, (r_, c_)), shape=(n, n), dtype=complex), k=1, which="SA", tol=1e-13)[0][0].real
    f = {d: (lam((d, 0, 0)) - ev[0]) / d ** 2 for d in (0.02, 0.01)}
    fd = {d: (lam((d / math.sqrt(3),) * 3) - ev[0]) / d ** 2 for d in (0.02, 0.01)}
    alpha_x = (4 * f[0.01] - f[0.02]) / 3; alpha_d = (4 * fd[0.01] - fd[0.02]) / 3
    check("band stiffness alpha = 115.61964849312 (Richardson extrapolation of (lambda(k)-lambda0)/k^2 to 5e-5), isotropic between the axis and the body diagonal", abs(alpha_x - 115.61964849312) < 5e-5 and abs(alpha_d - alpha_x) < 5e-5, f"axis {alpha_x:.6f}, body diagonal {alpha_d:.6f}")
    # first-vector weights
    O = (0, 0, 0)
    def first_branches(sigma):
        out = []
        for bd in nbrs(O):
            if bd == e1: continue
            Qd, Ed = {}, {}
            assert F_move(Qd, Ed, O, bd)
            Qd[O] = sigma; Qd[e1] = -sigma; Ed[(O, e1)] = Ed.get((O, e1), 0) + sigma
            clean(Qd); out.append(pack(Qd, Ed))
        return out
    vecs = {}
    for sg, nm in ((-1, "minus"), (1, "plus")):
        cw = [canon(w)[0] for w in first_branches(sg)]
        vv = np.zeros(n); vv[[idx[c] for c in cw]] = 1 / math.sqrt(5); vecs[nm] = vv
    wm, wp, wc = (v0 @ vecs["minus"]) ** 2, (v0 @ vecs["plus"]) ** 2, (v0 @ ((vecs["minus"] + vecs["plus"]) / math.sqrt(2))) ** 2
    check("k = 0 lowest-fiber weights of the first vectors: .05154396 (minus), .02963861 (plus), .07967697 (coherent)", abs(wm - .05154396) < 5e-9 and abs(wp - .02963861) < 5e-9 and abs(wc - .07967697) < 5e-9, f"{wm:.8f}, {wp:.8f}, {wc:.8f}")
    # fixture path
    def step(states, coef):
        out = set()
        for (w, t) in states:
            for (cw, dt), v in rows[w].items():
                if v == coef and not (cw == w and dt == (0, 0, 0)): out.add((cw, (t[0] + dt[0], t[1] + dt[1], t[2] + dt[2])))
        return out
    def bstep(states, coef):
        out = set()
        for (w, t) in states:
            for (cw, dt), v in rows[w].items():
                if v == coef and not (cw == w and dt == (0, 0, 0)): out.add((cw, (t[0] - dt[0], t[1] - dt[1], t[2] - dt[2])))
        return out
    Fw = {(s0, (0, 0, 0))}
    for coef in (-2, -4, -2): Fw = step(Fw, coef)
    Bw = {(s0, (1, 1, 0))}
    for _ in range(4): Bw = bstep(Bw, -186)
    check("a seven-step path s0 -> T_(1,1,0) s0 with matrix entries -2, -4, -2, -186, -186, -186, -186 exists (meeting-in-the-middle over the quotient)", len(Fw & Bw) > 0, f"{len(Fw & Bw)} meeting states")
    # next-birth channel and -372
    a, b, d, c, p, ell, h = O, e1, e2, (1, 1, 0), (1, 2, 0), (2, 1, 0), (1, 1, 1)
    br = first_branches(-1); s0w = br[[bd for bd in nbrs(O) if bd != e1].index(e2)]
    check("first_branches(-1)[e2] is the seed word s0", s0w == s0)
    row, vac = H4_row(s0)
    Qs = {a: -1, d: 1, p: 1}; Es = {(a, b): -1, (a, d): -1, (c, b): 1, (c, p): -1}
    check("H0 from s0 to the word s (q_a = -1, q_d = q_p = +1, E_(a,b) = E_(a,d) = -1, E_(c,b) = +1, E_(c,p) = -1) is -186", valid(Qs, Es) and -2 * row.get(pack(Qs, Es), 0) == -186)
    Qy, Ey = dict(Qs), dict(Es)
    assert F_move(Qy, Ey, c, h)
    Qy[c] = -1; Qy[ell] = 1; Ey[(c, ell)] = Ey.get((c, ell), 0) - 1; clean(Qy)
    check("the output y of B_(c,ell,-) with outward destination h has D = 2, q_a = q_c = -1 and four positive occupied B sites", D_of(Qy, Ey) == 2 and qget(Qy, a) == -1 and qget(Qy, c) == -1 and sorted(s for s, q in Qy.items() if not is_A(s) and q == 1) == sorted([d, p, ell, h]))
    pre = []
    for dest in nbrs(c):
        Q1, E1 = dict(Qy), dict(Ey)
        Q1[c] = 0; Q1[ell] = 0; E1[(c, ell)] = E1.get((c, ell), 0) + 1
        if not F_adj(Q1, E1, c, dest): continue
        clean(Q1)
        if qget(Q1, ell) == 0 and valid(Q1, E1): pre.append(pack(Q1, E1))
    M35 = np.zeros((len(pre), 5))
    for jj, bw in enumerate(br):
        rb, _ = H4_row(bw)
        for ii, pw in enumerate(pre): M35[ii, jj] = -2 * rb.get(pw, 0)
    check("y has exactly three D = 0 preimages under B2; the 3 x 5 matrix has exactly two entries -186, both in the first branch with outward destination e2, and sums to -372",
          len(pre) == 3 and sorted(M35[np.nonzero(M35)].tolist()) == [-186.0, -186.0] and set(np.nonzero(M35)[1].tolist()) == {1} and M35.sum() == -372, f"nonzero {[(int(i), int(j), float(M35[i, j])) for i, j in zip(*np.nonzero(M35))]}, sum {M35.sum():.0f}")
    print(f"   total {time.time()-T0:.0f}s")
    if not HITS:
        print(f"SUMMARY: no falsifier fires: an independent implementation of the cubic one-pair sector from the definitions reproduces the note's closed quotient exactly (11322 words = 11292 + 30, 652416 directed displacement edges, M = 14128, 771/10551 split, |E| <= 1), the k = 0 ground energy {ev[0]:.10f} and gap {ev[1]-ev[0]:.7f}, the stiffness alpha = {alpha_x:.5f}, the first-vector weights {wm:.8f}/{wp:.8f}/{wc:.8f}, the fixture path, the -186 next-birth coefficient and the -372 matrix; {PASS} checks pass")
    else:
        print("SUMMARY: failed: " + "; ".join(HITS))
        print("HIT: independent reconstruction differs from the note on: " + "; ".join(HITS))
    sys.exit(0)

if __name__ == "__main__":
    main()
