#!/usr/bin/env python3
"""Two tilted records in possibility's odds on the sphere menu (block 103's nonlinear odds, probes/lib/odds_sphere_lattice.solve).

Box L^3 with the boundary layer held at the ordered sea (lean along z).  Records tilted 90 degrees off the lean: record 1 content
(1,0,0), record 2 content (cos a, sin a, 0), a = 0 (like), pi (unlike), pi/2; records aligned with the lean: content (0,0,1).
Separation d along x.  (i) the sideways lean vector (<s_x>, <s_y>) at far sites against the sum of the one-record fields and
against the linear boundary-value prediction  sum_i tilt_i h_i(x)  (block 42 T6; block 103: the turn of the lean has per-neighbour
eigenvalue exactly 1/6, so h_i is the probability that the lattice walk from x reaches record i first, before the held boundary);
(ii) the summed site log normalizer (content-averaged weight, block 42 T4(b)) of the pair minus the two one-record values, against d;
(iii) the same for aligned records.  Floating point throughout (a research library, not a proof).
Usage: run.py [quick]
"""
import os, sys, time
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', 'lib'))
from odds_sphere_lattice import solve

def out(s): print(s, flush=True)
QUICK = len(sys.argv) > 1 and sys.argv[1] == "quick"
CASES = [(1.0, 21), (0.6, 17)] if not QUICK else [(1.0, 13)]
SEPS = (2, 3, 4, 6) if not QUICK else (2, 4)

def hitting(L, targets):
    """h_i(x): probability the simple walk from x hits target i first, before the boundary layer (held) or the other targets."""
    idx = {}
    for x in range(1, L - 1):
        for y in range(1, L - 1):
            for z in range(1, L - 1):
                if (x, y, z) not in targets: idx[(x, y, z)] = len(idx)
    n = len(idx); A = lil_matrix((n, n)); hs = []
    B = [np.zeros(n) for _ in targets]
    for p, k in idx.items():
        A[k, k] = 6.0
        for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
            q = (p[0] + dx, p[1] + dy, p[2] + dz)
            if q in idx: A[k, idx[q]] -= 1.0
            elif q in targets: B[targets.index(q)][k] += 1.0
    A = A.tocsr()
    for b in B:
        sol = spsolve(A, b); h = np.zeros((L, L, L))
        for p, k in idx.items(): h[p] = sol[k]
        hs.append(h)
    for i, t in enumerate(targets): hs[i][t] = 1.0
    return hs

def lean_xy(res):
    P, S, W = res['P'], res['S'], res['W']
    return P @ (W * S[:, 0]), P @ (W * S[:, 1])

def wsum(res, recs, L):
    m = np.zeros((L, L, L), bool); m[1:-1, 1:-1, 1:-1] = True
    for p in recs: m[p] = False
    return float((res['logN'] - res['logNF'])[m].sum())

rows = []
t0 = time.time()
for beta, L in CASES:
    c = L // 2
    out("N beta = %g, box %d^3 (boundary layer held at the ordered sea)" % (beta, L))
    single = {}
    def one(pos, s):
        key = (pos, tuple(np.round(s, 12)))
        if key not in single:
            single[key] = solve(beta, L, {pos: np.asarray(s, float)}, verbose=False)
        return single[key]
    for d in SEPS:
        r1 = (c - d // 2, c, c); r2 = (c - d // 2 + d, c, c)
        far = [(r2[0] + k, c, c) for k in (3, 5) if r2[0] + k < L - 1] + [(c, c + k, c) for k in (3, 5) if c + k < L - 1]
        h1, h2 = hitting(L, [r1, r2])
        hs1 = hitting(L, [r1])[0]; hs2 = hitting(L, [r2])[0]
        for lab, a in (("like", 0.0), ("unlike", np.pi), ("perp", np.pi / 2), ("aligned", None)):
            s1 = np.array([1.0, 0, 0]) if a is not None else np.array([0, 0, 1.0])
            s2 = np.array([np.cos(a), np.sin(a), 0]) if a is not None else np.array([0, 0, 1.0])
            pair = solve(beta, L, {r1: s1, r2: s2}, verbose=False)
            o1, o2 = one(r1, s1), one(r2, s2)
            Eint = wsum(pair, [r1, r2], L) - wsum(o1, [r1], L) - wsum(o2, [r2], L)
            if a is not None:
                tx, ty = lean_xy(pair); ux1, uy1 = lean_xy(o1); ux2, uy2 = lean_xy(o2)
                # amplitude of one record's far field against its own hitting probability (linear boundary-value theory)
                A1 = np.median([ux1[p] / hs1[p] for p in far if hs1[p] > 1e-6])
                lin = [(A1 * (s1[0] * h1[p] + s2[0] * h2[p]), A1 * (s1[1] * h1[p] + s2[1] * h2[p])) for p in far]
                sm = [(ux1[p] + ux2[p], uy1[p] + uy2[p]) for p in far]
                pr = [(tx[p], ty[p]) for p in far]
                scale = max(max(np.hypot(*v) for v in pr), 1e-12)          # normalise by the largest far field (unlike pairs vanish on the bisector)
                err_lin = max(np.hypot(pr[k][0] - lin[k][0], pr[k][1] - lin[k][1]) for k in range(len(far))) / scale
                err_sum = max(np.hypot(pr[k][0] - sm[k][0], pr[k][1] - sm[k][1]) for k in range(len(far))) / scale
                out("N   d=%d %-7s far sideways lean (pair) %s | deviation / largest far field, from sum_i tilt_i h_i: %.3f, from the sum of the one-record fields: %.3f | E_int = %+.6e"
                    % (d, lab, " ".join("(%+.4f,%+.4f)" % v for v in pr), err_lin, err_sum, Eint))
                rows.append((beta, d, lab, Eint, err_lin, err_sum))
            else:
                out("N   d=%d aligned: E_int = %+.6e" % (d, Eint))
                rows.append((beta, d, lab, Eint, None, None))
    out("N elapsed %.0f s" % (time.time() - t0))

print()
lines = []; hit = []
for beta, L in CASES:
    like = [r[3] for r in rows if r[0] == beta and r[2] == "like"]
    unl = [r[3] for r in rows if r[0] == beta and r[2] == "unlike"]
    ali = [r[3] for r in rows if r[0] == beta and r[2] == "aligned"]
    opp = all(np.sign(a) != np.sign(b) for a, b in zip(like, unl))
    lines.append("beta %g: E_int like %s, unlike %s (opposite signs at every d: %s), aligned %s" % (
        beta, " ".join("%+.2e" % v for v in like), " ".join("%+.2e" % v for v in unl), opp, " ".join("%+.2e" % v for v in ali)))
    if not opp: hit.append("beta %g: like and unlike tilts do not differ in sign at every d" % beta)
    if len(ali) >= 3 and abs(ali[-1]) > 0.1 * max(abs(v) for v in like + unl):
        hit.append("beta %g: aligned records keep a d-dependent weight at the largest d (%.2e)" % (beta, ali[-1]))
el = [r[4] for r in rows if r[4] is not None]; es = [r[5] for r in rows if r[5] is not None]
print("SUMMARY: sphere-menu odds, two tilted records: far sideways lean follows sum_i tilt_i h_i (reaching probabilities of the pair; "
      "max rel. deviation %.3f) rather than the sum of one-record fields (%.3f); " % (max(el), max(es)) + "; ".join(lines))
if hit:
    print("HIT: " + "; ".join(hit))
