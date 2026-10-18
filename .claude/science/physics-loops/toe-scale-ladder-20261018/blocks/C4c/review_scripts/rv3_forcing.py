"""Independent forced-site classification (Lemma V / Cor C coverage) for the supports named in NOTE."""
import itertools, numpy as np
from rv_common import check, total
def forced(S):
    S = [tuple(p) for p in S]; Sset = set(S); F = set()
    diffs = {tuple(np.subtract(a, b)) for a in S for b in S if a != b}
    for t in diffs:
        ov = {tuple(np.add(p, t)) for p in S} & Sset
        if len(ov) == 1:
            s = ov.pop(); F.add(s); F.add(tuple(np.subtract(s, t)))
    return F
def unforced(S): return set(map(tuple, S)) - forced(S)
def vertices(S):
    # p is a vertex iff some linear functional has unique max at p (brute-force over integer directions)
    S = [np.array(p) for p in S]; V = set()
    dirs = [np.array(d) for d in itertools.product(range(-7, 8), repeat=3) if any(d)]
    for d in dirs:
        vals = [int(d @ p) for p in S]; m = max(vals)
        if vals.count(m) == 1: V.add(tuple(S[vals.index(m)]))
    return V
cube = list(itertools.product((0, 1), repeat=3))
subs = [s for k in range(2, 9) for s in itertools.combinations(cube, k)]
check("all 247 cube subsets with |S|>=2 fully forced", all(not unforced(s) for s in subs), len(subs))
check("every conv-hull vertex is forced (cube subsets)", all(vertices(s) <= forced(s) for s in subs))
for d in [(1,0,0),(1,1,0),(1,1,1),(2,1,0)]:
    d = np.array(d)
    for (a, b) in [(1, 2), (1, 3), (2, 3), (1, 4)]:
        S = [tuple(0*d), tuple(a*d), tuple(b*d)]
        assert len(unforced(S)) <= 1
check("collinear triples {0,a d,b d}: <=1 unforced (sampled directions/spacings)", True)
bonds = [[(0,0,0), d] for d in itertools.product(range(-3,4), repeat=3) if any(d)]
check("all 2-site bonds up to range 3 fully forced", all(not unforced(b) for b in bonds))
star = [(0,0,0)] + [tuple(s*np.eye(3,dtype=int)[i]) for i in range(3) for s in (1,-1)]
check("7-site star: exactly the centre unforced", unforced(star) == {(0,0,0)})
sq = [(x, y, 0) for x in range(3) for y in range(3)]
check("3x3 square: 5 unforced", len(unforced(sq)) == 5)
c27 = list(itertools.product(range(3), repeat=3))
check("27-cell: 19 unforced", len(unforced(c27)) == 19)
# collinear 4-point sets {0<a<b<c}: which have >=2 unforced?
bad = [(a,b,c) for c in range(3, 13) for a in range(1, c) for b in range(a+1, c)
       if len(unforced([(0,0,0),(a,0,0),(b,0,0),(c,0,0)])) >= 2]
print("collinear 4-sets 0<a<b<c<=12 with >=2 unforced:", bad)
check("only equally spaced collinear 4-sets have 2 unforced (so S4 + scaling covers 'collinear 4-site segments')",
      all(b - a == a and c - b == a for a, b, c in bad))
import random
def sample(kmax, seed):
    random.seed(seed); cnt = {0: 0, 1: 0, 2: 0}
    for _ in range(300):
        k = random.randint(2, kmax); S = random.sample(c27, k)
        cnt[min(len(unforced(S)), 2)] += 1
    return cnt
cA = sample(12, 7); cB = sample(27, 11)
print("300 random 27-cell subsets, |S| uniform in [2,12] (author's distribution): unforced 0/1/>=2 =", cA)
print("300 random 27-cell subsets, |S| uniform in [2,27]: unforced 0/1/>=2 =", cB)
check("|S|<=12 sampling reproduces the NOTE's ~296/300 covered rate (>=285)", cA[0] + cA[1] >= 285, cA)
check("NOTE's 296/300 does NOT survive |S| up to 27 (covered < 60%): coverage statistic is size-distribution dependent",
      cB[0] + cB[1] < 180, cB)
total()
