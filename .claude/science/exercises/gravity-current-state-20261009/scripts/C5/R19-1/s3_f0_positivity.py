"""R19-1 s3: ingredients of the proof that f_TT(k->0) >= c(bU) > 0 uniformly in V at every finite bU (Lemma 3).
For each pattern type p and each TT/V/S polarization along axis/face/body: (i) mu(p,eps) = the set of values of
eps:M0(sigma|_p) over sign patterns sigma in {+-1}^p (is a nonzero value possible?); (ii) a 'single-overlap' move q:
a pattern translate sharing exactly ONE slot s0 with p, with c_{s0}(eps) != 0 (then n -> n xor q maps the zero set
{eps:M0 = 0} injectively into its complement); (iii) Delta_max: max |change of sum gamma^2| under one move (bounded)."""
import numpy as np, itertools, sys
sys.path.insert(0, '.')
from common import *
from mc import channel_pols, cvec
pats = [[(tuple(d), t) for d, t in p] for p in PATTERNS]
names = ["cube", "mu8a", "mu8b", "mu8c"]
def slots_at(p, x): return [(tuple(np.array(d) + np.array(x)), t) for d, t in p]
dirs = {"axis": (0, 0, 1), "face": (1, 1, 0), "body": (1, 1, 1)}
for dn, kv in dirs.items():
    pols = channel_pols(np.array(kv, float))
    for ch in ["TT", "V", "S"]:
        for ie, eps in enumerate(pols[ch]):
            c = cvec(eps); line = []
            for a, p in enumerate(pats):
                cs = np.array([c[t] for d, t in p])
                vals = set()
                for sg in itertools.product([1, -1], repeat=len(p)):
                    vals.add(round(float(np.dot(cs, sg)), 9))
                nonzero = any(abs(v) > 1e-9 for v in vals); haszero = any(abs(v) < 1e-9 for v in vals)
                # single-overlap moves
                S0 = set(slots_at(p, (0, 0, 0))); good = 0
                for b, q in enumerate(pats):
                    for x in itertools.product(range(-4, 5), repeat=3):
                        Q = set(slots_at(q, x)); I = S0 & Q
                        if len(I) == 1:
                            (d0, t0), = I
                            if abs(c[t0]) > 1e-12: good += 1
                line.append("%s: nonzero=%s zero-possible=%s single-overlap moves=%d" % (names[a], nonzero, haszero, good))
            print("%s %s%d: " % (dn, ch, ie + 1) + " | ".join(line))
# Delta_max: max change of sum gamma^2 from one move, over random configurations (bounded by #edges touched x 1)
L = 6; G = G_matrix(L); P = pattern_vectors(L)
edges_touched = [(np.abs(G @ p) > 0).sum() for p in P[::L**3]]
print("edges touched per move type (bound on |Delta sum gamma^2|, since gamma^2 in {0,1}):", edges_touched)
