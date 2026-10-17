"""(c) Settle the C8 pair test for all 108 BKSF (code, C2) pairs, with emphasis on
the 36 uncovered ones, by the dressing-independent method of pairspace.py:
lambda is computed on the ENTIRE affine space of admissible (flux-dressed) pair
creators in an R-invariant window, and proven constant there by the quadratic
form criterion.  Also: does a CLEAN creator with a clean image exist?"""
import sys, pickle, itertools, time
from collections import Counter
import numpy as np
import mpd_core
from mpd_core import Tableau, apply
from bksf_core import BKSF, edge_perm_map, permute, kind
import pairspace as ps

L = int(sys.argv[1]) if len(sys.argv) > 1 else 10
only_unc = (len(sys.argv) > 2 and sys.argv[2] == "unc")
MARGIN = int(sys.argv[3]) if len(sys.argv) > 3 else 2
SEPS = tuple(int(t) for t in sys.argv[4].split(",")) if len(sys.argv) > 4 else (2, 3)
D = pickle.load(open("c8_pairs.pkl", "rb"))
reps, pairs, covered = D["reps"], D["pairs"], D["covered"]
nbytes = (3 * L ** 3 + 7) // 8


def bits(i):
    return np.unpackbits(np.frombuffer(i.to_bytes(nbytes, "little"), np.uint8), bitorder="little")


def comm_row_fast(Q, W, Wa):
    return np.concatenate([bits(Q[1])[Wa], bits(Q[0])[Wa]])




def make_comm_row(Wa):
    def f(Q, W):
        return np.concatenate([bits(Q[1])[Wa], bits(Q[0])[Wa]])
    return f


def linf(p, q):
    return max(abs(p[i] - q[i]) for i in range(3))


def wrapv(p):
    return tuple(((c + L // 2) % L) - L // 2 for c in p)


tabs, gen_cache = {}, {}
def get(code, s):
    if (code, s) not in tabs:
        b = BKSF(L, reps[code])
        gs = b.gens(s)
        T = Tableau(b.n)
        for g in gs:
            T.insert(g[3])
        assert T.consistent and b.n - T.rank() == 3
        tabs[(code, s)] = T
        gen_cache[(code, s)] = gs
    return tabs[(code, s)], gen_cache[(code, s)]


def choose_xs(M):
    cands = []
    for x in itertools.product(range(-2, 3), repeat=3):
        y = apply(M, x)
        d = linf(x, y)
        if d in SEPS:
            cands.append((d, sum(abs(c) for c in x), x))
    cands.sort()
    out = []
    for want in SEPS:
        for d, _, x in cands:
            if d == want:
                out.append(x)
                break
    return out


results = Counter()
detail = []
t0 = time.time()
for (code, M) in pairs:
    cov = covered[(code, M)] is not None
    if only_unc and cov:
        continue
    img = edge_perm_map(L, M)
    rot = lambda P, img=img: permute(P, img)
    b = BKSF(L, reps[code])
    for x in choose_xs(M):
        y = apply(M, x)
        lo = [min(x[i], y[i]) - MARGIN for i in range(3)]
        hi = [max(x[i], y[i]) + MARGIN for i in range(3)]
        box = set(itertools.product(*[range(lo[i], hi[i] + 1) for i in range(3)]))
        W = sorted({b.q(v, a) for v in box for a in range(3)
                    if b.add(v, mpd_core.DIRS[a]) in box})
        Wa = np.array(W)
        wmask = 0
        for q in W:
            wmask |= 1 << q
        assert all(img[q] in set(W) for q in W)
        ps.comm_row = make_comm_row(Wa)
        for s in (1, -1):
            T, gs = get(code, s)
            touching = [((lab, v, c), P) for (lab, v, c, P) in gs
                        if ((P[0] | P[1]) & wmask) or ((rot(P)[0] | rot(P)[1]) & wmask)]
            xs_w = {wrapv(x), wrapv(y)}

            def near(lab):
                _, v, c = lab
                a, bb = [k for k in range(3) if k != c]
                corners = [v, b.add(v, mpd_core.DIRS[a]), b.add(v, mpd_core.DIRS[bb]),
                           b.add(b.add(v, mpd_core.DIRS[a]), mpd_core.DIRS[bb])]
                return any(linf(wrapv(cn), u) <= 1 for cn in corners for u in xs_w)

            Bflip = lambda lab: 1 if wrapv(lab[1]) in xs_w else 0
            res = ps.analyse(W, touching, near, Bflip, rot, T)
            resc = ps.analyse(W, touching, lambda lab: False, Bflip, rot, T)
            clean = resc["status"] == "ok"
            key = ("covered" if cov else "UNCOVERED", kind(M), res.get("lam0"), res.get("constant"), "clean-exists" if clean else "no-clean")
            results[key] += 1
            detail.append((code, M, x, s, res.get("lam0"), res.get("dim"), res.get("Fbad"), res.get("Kbad"),
                           clean, resc.get("lam0")))
            print(code, kind(M), "cov" if cov else "UNC", x, "s=%+d" % s, "lam0=%s dim=%s Fbad=%s Kbad=%s constant=%s | clean: %s lam=%s  (%.0fs)"
                  % (res.get("lam0"), res.get("dim"), res.get("Fbad"), res.get("Kbad"), res.get("constant"),
                     clean, resc.get("lam0"), time.time() - t0), flush=True)
print("SUMMARY (class, C2 kind, lambda, constant over full creator space, clean creator exists): count")
for k, v in sorted(results.items(), key=str):
    print("  ", k, v)
pickle.dump(detail, open("c8_pairtest_L%d%s_m%d.pkl" % (L, "_unc" if only_unc else "", MARGIN), "wb"))
