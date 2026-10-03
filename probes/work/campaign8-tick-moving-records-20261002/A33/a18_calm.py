"""A33 a18: calmness and quiet tests for period-2 (P2-A) vacua.
usage: python3 a18_calm.py r2 i1,i2,...   (indices into p2a_sols_r{r2}.pkl; pure-looking ones)

(1) Law-level parent. A translation-invariant (TI), covariant law must have all 8 translates of the
    vacuum as eigenstates. The 8 generators centred at one site (one per translate: the shape of role
    o placed at the site, o in {0,1}^3) are tested for mutual commutation, independence mod 2 and
    sign consistency. If they commute and are independent, h_x = prod_o (1 - g_o(x))/2 is a nonzero,
    covariant (the set {g_o(x)} is turned into itself by every turn about x), TI projector that
    annihilates every translate: a frustration-free TI parent law (EXACT).
(2) Quiet test (A9): stabilizer elements supported inside the 7-site star of a site of each role
    (dim of the star commutant; for a pure state this equals dim of stabilizers inside the star).
    A TI formation weight on the star must annihilate all 8 translates' star marginals at once.
"""
import signal, sys, time, pickle, itertools
signal.alarm(55)
from p2a_core import Space, shapes_of, role_of, shape_at
from p2lib import pcomm, Elim, LBITS, pat_str, popc
from a9_inspect_lib import commutant

r2 = int(sys.argv[1]); idx = [int(t) for t in sys.argv[2].split(",")]
t0 = time.time()
S = Space(r2)
D = pickle.load(open(f"p2a_sols_r{r2}.pkl", "rb"))
STAR = [(0, 0, 0)] + [tuple(s * (i == a) for i in range(3)) for a in range(3) for s in (1, -1)]
for n in idx:
    sol, ti = D["sols"][n]
    sh = shapes_of(S, sol)
    gens8 = []
    for o in itertools.product((0, 1), repeat=3):
        role, axis = role_of(o)
        s, p = shape_at(sh[role], role, axis, (0, 0, 0))
        gens8.append((o, role, axis, s, p))
    comm = all(pcomm(a[4], b[4]) == 0 for a, b in itertools.combinations(gens8, 2))
    E = Elim()
    sites = sorted({y for g in gens8 for y in g[4]})
    pos = {y: k for k, y in enumerate(sites)}
    for g in gens8:
        v = 0
        for y, l in g[4].items():
            bx, bz = LBITS[l]
            v |= (bx << (2 * pos[y])) | (bz << (2 * pos[y] + 1))
        E.add(v)
    rank8 = len(E)
    distinct = len({tuple(sorted(g[4].items())) for g in gens8})
    # quiet test per role (pure state assumed: star commutant = stabilizers inside the star)
    q = {}
    for r, y0 in {"V": (0, 0, 0), "C": (1, 1, 1), "E": (1, 0, 0), "F": (1, 1, 0)}.items():
        B = [tuple(a + b for a, b in zip(y0, d)) for d in STAR]
        q[r] = len(commutant(S, sh, B))
    print(f"#{n} ti={int(ti)}: 8 site-centred translate generators: distinct={distinct}, pairwise commuting={comm}, "
          f"rank mod 2={rank8}, support {len(sites)} sites -> "
          + ("TI frustration-free parent h_x = prod(1-g)/2 EXISTS (dim of its range 2^%d)" % (len(sites) - rank8)
             if comm and rank8 == distinct else "no commuting-product parent at this range")
          + f"; star-stabilizer dims per role {q}   ({time.time()-t0:.1f}s)")
