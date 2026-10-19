"""Reviewer probe: automorphism (QCA) range of alpha = Ad U vs. the CA radius (sparse, exact on Z^3).

For the permutation QCA U|d> = |F d>, alpha(X_x) acts as d -> G(d) = F(F^{-1}(d) xor {x}).
Support of alpha(X_x) = (sites G may modify) ∪ (sites the modification M(d) = G(d) xor d depends on).
alpha(Z_x) is diagonal, (F^{-1} d)_x: support = dependence set of F^{-1} at x (CA radius of U^{-1}).
A dependence witness (d, z) — flipping d at z changes M(d) — at distance R from x proves
range(alpha) >= R exactly (finite configurations on Z^3).  Upper bound (NOTE): 2r + r' = 18.
Search: clusters rich in face pairs (the only movers) near x; z at distance 4..12.
"""
import os, sys, time, random
import rv_core as C

HERE = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(HERE, 'logs', 'qca_range.txt'), 'w')
ck = C.Check(f)
rng = random.Random(5)
budget = float(sys.argv[1]) if len(sys.argv) > 1 else 600
O = (0, 0, 0)
SH = []
for a, b in C.PLANES:
    for s in (1, -1):
        v = [0, 0, 0]; v[a] = 1; v[b] = s
        SH.append(tuple(v))


def M(d, F, Finv):
    e = Finv(d) ^ {O}
    return F(e) ^ d


def rand_cluster(R):
    c = set()
    for _ in range(rng.randint(1, 5)):
        x = tuple(rng.randint(-R, R) for _ in range(3))
        c |= {x, C.add(x, rng.choice(SH))}
    for _ in range(rng.randint(0, 3)):
        c.add(tuple(rng.randint(-R, R) for _ in range(3)))
    return frozenset(c)


for name, F, Finv in (('alpha', C.U, C.Uinv), ('alpha^-1', C.Uinv, C.U)):
    t0 = time.time()
    best_w = 0; best_dep = 0; wit = None; n = 0
    hist = {}
    while time.time() - t0 < budget / 2:
        R = rng.choice([3, 5, 7])
        d = rand_cluster(R)
        m0 = M(d, F, Finv)
        if m0:
            best_w = max(best_w, max(C.cheb(y, O) for y in m0))
        for _ in range(6):
            r = rng.randint(max(4, best_dep), 12)
            # z at Chebyshev distance exactly r, preferably near the cluster
            base = rng.choice(sorted(d)) if rng.random() < 0.7 else O
            for _ in range(20):
                z = tuple(base[i] + rng.randint(-3, 3) for i in range(3))
                if C.cheb(z, O) == r:
                    break
            else:
                z = list(rng.choice(sorted(d))); z[rng.randint(0, 2)] = r * rng.choice([-1, 1]); z = tuple(z)
            rr = C.cheb(z, O)
            n += 1
            if M(d ^ {z}, F, Finv) != m0:
                hist[rr] = hist.get(rr, 0) + 1
                if rr > best_dep:
                    best_dep = rr; wit = (sorted(d), z)
    ck.info(f"{name}(X_0): {n} probes in {time.time()-t0:.0f}s; max modified-site distance {best_w}; max dependence distance {best_dep}; hist {dict(sorted(hist.items()))}; witness {wit}")
    # re-verify witness exactly
    if wit is not None:
        d = frozenset(wit[0]); z = wit[1]
        ok = M(d, F, Finv) != M(d ^ {z}, F, Finv)
        ck(ok, f"{name}: exact witness: range of {name} >= {C.cheb(z, O)} (vs CA radius bound 6, automorphism bound 18)")
ck.total()
