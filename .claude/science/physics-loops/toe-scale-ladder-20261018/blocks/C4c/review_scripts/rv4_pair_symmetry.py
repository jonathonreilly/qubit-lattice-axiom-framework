"""Independent check of Lemma K counts, Observation M (monomial pair maps) and the Thm N instance."""
import itertools, numpy as np
from rv_common import check, total, groups
O, T = groups()
check("|O|=24, |T|=12", len(O) == 24 and len(T) == 12)
cheb = lambda a, b: int(np.max(np.abs(np.array(a) - np.array(b))))
canon = lambda c: tuple(sorted(tuple(int(x) for x in p) for p in c))
def near_reps(r):
    out = set()
    for rho in itertools.product(range(-r, r + 1), repeat=3):
        if rho != (0, 0, 0): out.add(max(rho, tuple(-x for x in rho)))
    return sorted(out)
for r in (1, 2):
    check(f"d_{r}", len(near_reps(r)) == ((2*r+1)**3 - 1)//2, len(near_reps(r)))
# Lemma K example count: near pairs c' with all cross distances <=1 to {0,e1}
c0 = [(0,0,0),(1,0,0)]
sites = [p for p in itertools.product(range(-2,4), repeat=3) if all(cheb(p,q) <= 1 for q in c0)]
rel = {canon([p,q]) for p,q in itertools.combinations(sites,2) if cheb(p,q) <= 1}
mov = [c for c in rel if tuple(np.sum(c,0)) != (1,0,0)]
check("Lemma K: 89 related near pairs to {0,e1}, 88 with different COM", (len(rel), len(mov)) == (89, 88), (len(rel), len(mov)))
# space-group stabiliser; elements (R, a): x -> R x + a
def stab(c, G):
    a, b = map(np.array, c); out = []
    for R in G:
        for u, v in ((a, b), (b, a)):
            t = u - R @ a
            if np.array_equal(R @ b + t, v): out.append((R, t))
    return out
act = lambda g, c: canon([g[0] @ np.array(p) + g[1] for p in c])
def exceptions(r, G):
    exc = {}
    for rho in near_reps(r):
        c = canon([(0,0,0), rho]); St = stab(c, G)
        box = [p for p in itertools.product(range(-r-1, r+3), repeat=3) if all(cheb(p,q) <= r for q in c)]
        imgs = {canon([p,q]) for p,q in itertools.combinations(box,2) if cheb(p,q) <= r}
        fixed = [d for d in imgs if all(act(g, d) == d for g in St)]
        m = [d for d in fixed if tuple(np.sum(d,0)) != tuple(np.sum(c,0))]
        if m: exc[rho] = (len(St), m)
    return exc
eT1, eO1 = exceptions(1, T), exceptions(1, O)
face = sorted({max(v, tuple(-x for x in v)) for v in itertools.product((-1,0,1), repeat=3) if sum(abs(x) for x in v) == 2})
check("r=1, T: exceptions are exactly the 6 face diagonals", sorted(eT1) == face, sorted(eT1))
check("r=1, T: face-diagonal stabiliser has order 2", all(v[0] == 2 for v in eT1.values()))
check("r=1, O: no exceptions (full action freezes monomial pairs)", len(eO1) == 0)
ex = canon([(0,0,1),(1,1,1)])
check("example {0,e1+e2} -> {e3,(1,1,1)} is a T-allowed COM-moving image", ex in eT1[(1,1,0)][1])
# the edge C2 (x,y,z)->(y,x,-z) is in O\T, fixes {0,e1+e2} and does not fix the image
R = np.array([[0,1,0],[1,0,0],[0,0,-1]])
check("C2' about (1,1,0) is in O but not T, fixes c, moves image",
      any(np.array_equal(R,M) for M in O) and not any(np.array_equal(R,M) for M in T)
      and act((R,np.zeros(3,int)), [(0,0,0),(1,1,0)]) == canon([(0,0,0),(1,1,0)])
      and act((R,np.zeros(3,int)), ex) != ex)
# images listed for (1,1,0): COM displacements
d = sorted({tuple(np.sum(m,0) - np.array([1,1,0])) for m in eT1[(1,1,0)][1]})
check("face-diagonal (1,1,0) moves only along +-e3 (2*dCOM = +-2 e3)", d == [(0,0,-2),(0,0,2)], d)
e2T, e2O = exceptions(2, T), exceptions(2, O)
check("r=2 counts 56 (T) and 36 (O) of 62 (informational)", (len(e2T), len(e2O)) == (56, 36), (len(e2T), len(e2O)))
# Theorem N instance: Ising phases exp(i sum theta_b s_i s_j), vacuum s=-1; pair phase relative to vacuum
th = {1: 0.31, 2: 0.57, 3: 0.23}   # |rho|_1 class: axis/face/body
L = 5
def phase(conf):
    tot = 0.0
    for x in itertools.product(range(L), repeat=3):
        for rho in near_reps(1):
            y = tuple((x[i]+rho[i]) % L for i in range(3))
            tot += th[sum(abs(v) for v in rho)] * conf[x] * conf[y]
    return tot
vac = {x: -1 for x in itertools.product(range(L), repeat=3)}
p0 = phase(vac)
vals = {}
for rho in near_reps(1):
    cf = dict(vac); cf[(0,0,0)] = 1; cf[tuple(v % L for v in rho)] = 1
    ph = (phase(cf) - p0 + np.pi) % (2*np.pi) - np.pi
    vals.setdefault(sum(abs(v) for v in rho), set()).add(round(ph, 4))
print("pair phases by class (axis, face, body):", vals)
check("instance: phases 3.0623 (axis,x3) -2.1809 (face,x6) 2.7423 (body,x4)",
      vals == {1: {3.0623}, 2: {-2.1809}, 3: {2.7423}})
total()
