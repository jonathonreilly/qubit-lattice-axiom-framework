"""R18-1 s1b (written before running). Covariance of the weight and of the sampled sector.
(i) Natural (pure permutation) action vs shift action (n -> 1-n on slots whose tensor sign flips): is
    W(n) = sum_edges gamma^2 invariant? (random n in ker, L=4, all 24 rotations about a site)
(ii) Are the shift flips f_g (and F_all) in span(moves)? i.e. does the trivial coset map to itself?"""
import numpy as np, itertools
from common import *
L = 4; V = L**3; G = G_matrix(L); P = pattern_vectors(L); B = f2_basis(P); rB = B.shape[0]
rng = np.random.default_rng(3)
def site(x): x = np.mod(x, L); return (x[0]*L + x[1])*L + x[2]
def act(R, n, shift):
    out = np.zeros_like(n)
    for x in itertools.product(range(L), repeat=3):
        for t in range(6):
            i, j = TYPES[t]; p = R @ pos(x, t)
            ii = int(np.argmax(np.abs(R[:, i]))); jj = int(np.argmax(np.abs(R[:, j])))
            sgn = int(R[ii, i]*R[jj, j]); tt = TIDX[tuple(sorted((ii, jj)))]
            base = p - (0.5*(E3[ii] + E3[jj]) if ii != jj else 0)
            v = n[t*V + site(np.round(base).astype(int))]
            val = n[t*V + site(np.array(x))]
            out[tt*V + site(np.round(base).astype(int))] = (1 - val) if (shift and sgn < 0) else val
    return out
def W(n): g = G @ n; return int(((g//2)**2).sum()), bool(np.all(g % 2 == 0))
# random n in the trivial coset
ns = [(rng.integers(0, 2, len(P)) @ P) % 2 for _ in range(5)]
res = {False: 0, True: 0}; inspan = {False: 0, True: 0}
for R in rot_mats():
    for shift in [False, True]:
        ok = all(W(act(R, n, shift))[0] == W(n)[0] for n in ns)
        res[shift] += ok
        img = act(R, np.zeros(6*V, dtype=np.int64), shift)   # image of n = 0 = the flip set f_g
        inspan[shift] += (f2_rank(np.vstack([B, img])) == rB)
print("rotations about a site: 24")
print("weight invariant on 5 random coset states: natural action %d/24, shift action %d/24" % (res[False], res[True]))
print("image of n=0 lies in span(moves) (trivial coset preserved): natural %d/24, shift %d/24" % (inspan[False], inspan[True]))
Fall = np.ones(6*V, dtype=np.int64)
print("F_all in span(moves):", f2_rank(np.vstack([B, Fall])) == rB, "; W(F_all n) == W(n):", all(W((Fall + n) % 2)[0] == W(n)[0] for n in ns))
for t in range(6):
    v = np.zeros(6*V, dtype=np.int64); v[t*V:(t+1)*V] = 1
    print("  all-ones on slot type %s in span(moves): %s" % (TYPES[t], f2_rank(np.vstack([B, v])) == rB))
