"""A50 t2_search: continuous (non-Clifford) covariant product dressings on the axis places
(v, six links, six far corners v +- 2e_a), searched by Levenberg-Marquardt from random starts.
argv: group (O, T, D2, C2z), places (v | far | axis), target (none | T | all), starts.
Only the seeds that feed the chosen places are free (others identity).
Residual: non-scalar part of every per-site word at the chosen non-link places for the T-junctions
(all 20 if target = all); with a target, also theta~(tri) + 1 for those junctions, where
theta~ = link phase (exact formula) * prod over chosen places of tr(W)/2.
Off-axis places cancel in pairs for T-junctions whenever the junction's half-turn is in G.
Falsification test of lemma F'': under O no start may reach zero with target T.
Control: under {1, C2z} the same search should reach zero with theta = -1.
"""
import signal, sys, time, zlib
import numpy as np
from collections import Counter
from scipy.optimize import least_squares
from a50lib import *
signal.alarm(285)
gname, pname, target = sys.argv[1], sys.argv[2], sys.argv[3]
NST = int(sys.argv[4]) if len(sys.argv) > 4 else 40
G = GRP[gname]
rng = np.random.default_rng(zlib.crc32((gname + pname + target).encode()))
FH = FastHops(G, AXSITES)
CHOSEN = {'v': [(0, 0, 0)], 'far': FAR, 'axis': [(0, 0, 0)] + FAR, 'vlinks': [(0, 0, 0)]}[pname]
use_links = pname in ('axis', 'vlinks')
cidx = [FH.nonleg.index(x) for x in CHOSEN]
feed = sorted({e for (i, y, e, g) in FH.entries if e >= 0 and (y in CHOSEN or (use_links and y in LEGLINK))})
struct = [(o, S, stab_type(S) if kind(o) != 1 else ('link', None)) for (o, S) in FH.struct]
blocks = []
for e in feed:
    o, S, st = struct[e]
    blocks.append((e, 1 if kind(o) == 1 or st[0] != 'triv' else 3))
npar = sum(b for _, b in blocks)

def seeds_of(p, branches):
    out = np.broadcast_to(I2, (len(struct), 2, 2)).copy(); q = 0
    for (e, nb), br in zip(blocks, branches):
        o, S, st = struct[e]
        if kind(o) == 1:
            v = np.zeros(3); v[link_axis(o)] = p[q]; out[e] = su2_exp(v)
        elif st[0] == 'triv':
            out[e] = su2_exp(p[q:q + 3])
        else:
            n = st[1]
            if st[0] == 'so2' or br == 0:
                out[e] = su2_exp(p[q] * n)
            else:
                b1 = np.cross(n, [1, 0, 0] if abs(n[0]) < 0.9 else [0, 1, 0]); b1 /= np.linalg.norm(b1)
                out[e] = nsig(np.cos(p[q]) * b1 + np.sin(p[q]) * np.cross(n, b1))
        q += nb
    return out

def link_r(m, k):
    """ratio of a field-diagonal factor m on leg link k: <out-up|m|out-up>/<out-down|m|out-down>."""
    a = AXIS[k]; s = SIGN[k]
    w, v = np.linalg.eigh(s * PAUL[a + 1])
    up, dn = v[:, 1], v[:, 0]
    return (up.conj() @ m @ up) / (dn.conj() @ m @ dn)

TRI_USE = T_TRI if target != 'all' else TRIPLES
ORB = {tuple(sorted(PERM[g][a] for a in (0, 1, 4))) for g in G}
TRI_TGT = [t for t in TRI_USE if t in ORB] if target == 'one' else TRI_USE
def dag(A):
    return np.conj(np.swapaxes(A, -1, -2))
def evaluate(seeds):
    A, L = FH.arrays(seeds)
    A = A[:, cidx]
    res = []; th = {}
    for tri in TRI_USE:
        i, j, k = tri
        W = dag(A[i]) @ A[j] @ dag(A[k]) @ A[i] @ dag(A[j]) @ A[k]
        lam = (W[:, 0, 0] + W[:, 1, 1]) / 2
        D = (W - lam[:, None, None] * I2).reshape(-1)
        res.append(np.concatenate([D.real, D.imag]))
        phi = 1.0
        if use_links:
            r = lambda a, b: link_r(L[a][b], b)
            phi = (r(i, k) * r(k, j) * r(j, i)) / (r(k, i) * r(j, k) * r(i, j))
        th[tri] = phi * np.prod(lam)
    return np.concatenate(res), th

def fun(p, branches):
    r, th = evaluate(seeds_of(p, branches))
    if target in ('T', 'all', 'one'):
        t = np.array([th[tri] + 1 for tri in TRI_TGT])
        r = np.concatenate([r, t.real, t.imag])
    return r

print("group %s, places %s, target %s: %d free seeds, %d params, %d starts"
      % (gname, pname, target, len(blocks), npar, NST))
t0 = time.time(); summary = Counter(); best = np.inf; pats = Counter(); ex = None
for s in range(NST):
    if time.time() - t0 > 230:
        print("   time cap after %d starts" % s); break
    branches = [rng.integers(2) for _ in blocks]
    p0 = rng.uniform(-np.pi, np.pi, size=npar)
    sol = least_squares(fun, p0, args=(branches,), method='lm', xtol=1e-15, ftol=1e-15, max_nfev=(200 if npar < 20 else 40) * npar)
    r, th = evaluate(seeds_of(sol.x, branches))
    best = min(best, np.linalg.norm(fun(sol.x, branches)))
    if np.abs(r).max() < 1e-8:
        vals = Counter(complex(np.round(th[t].real, 5), np.round(th[t].imag, 5)) for t in TRI_USE)
        pats[tuple(sorted(vals.items(), key=lambda z: z[0].real))] += 1
        summary['scalar'] += 1
        if ex is None and any(np.round(th[t].real, 5) == -1 for t in TRI_USE):
            sd = seeds_of(sol.x, branches)
            ex = (s, {NAMES[t[0]] + NAMES[t[1]] + NAMES[t[2]]: complex(np.round(th[t], 4)) for t in TRI_USE},
                  {str(struct[e][0]): np.round(rot_of(sd[e]), 3).tolist() for e, _ in blocks if kind(struct[e][0]) != 1})
    else:
        summary['not scalar'] += 1
print("   outcomes: %s" % dict(summary))
print("   smallest final residual norm (incl. target): %.3e" % best)
print("   theta patterns at scalar optima: %s" % dict(pats))
if ex is not None:
    print("   example with a -1 (start %d): thetas %s" % (ex[0], ex[1]))
    print("      seed rotations (SO(3)) at non-link seed places: %s" % ex[2])
print("   wall %.1f s" % (time.time() - t0))
print("done")
