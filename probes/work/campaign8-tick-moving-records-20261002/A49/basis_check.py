"""A49 basis_check: build the soldered-covariant, Hermitian, T-even operator basis; report n per class; check
covariance under all 24 exact soldered turns; check the count against group averages of ALL Pauli seeds of each
support; check that the four-spin terms are Klein duals of dual-frame SU(2)-invariant operators (A44 (iii))."""
import sys, signal, itertools, numpy as np
signal.alarm(280)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a49lib import *

def rank_of(ops):
    keys = sorted(set().union(*[set(o) for o in ops]))
    M = np.array([[o.get(k, 0.) for k in keys] for o in ops])
    sv = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(sv > 1e-9 * sv.max())), M, keys

B2 = bilinear_basis()
print("== bilinears (soldered frame, per-site HS-normalized) ==")
for nm, cls, op in B2:
    print(f"  {nm:4s} {cls}: {len(op):3d} canonical strings; covariance defect {cov_defect(op):.1e}; "
          f"all coefficients real: {all(isinstance(v, float) for v in op.values())}")
print("== completeness: rank of group averages of all 9 Pauli seeds per bond class vs named operators ==")
for nm_cls, d, names in (("NN", (1, 0, 0), ("J1", "K1", "D1")), ("FD", (1, 1, 0), ("J2", "Kn2", "Kd2", "D2")),
                          ("A2", (2, 0, 0), ("J3", "K3", "D3")), ("BD", (1, 1, 1), ("J4", "Kd4", "D4"))):
    allseeds = [gavg(bilinear(d, np.outer(E3[a], E3[b]))) for a in range(3) for b in range(3)]
    allseeds = [o for o in allseeds if o]
    r_all, _, _ = rank_of(allseeds)
    named = [op for nm, cls, op in B2 if nm in names]
    r_named, _, _ = rank_of(named); r_both, _, _ = rank_of(allseeds + named)
    print(f"  {nm_cls}: rank(all seeds) = {r_all}; rank(named) = {r_named}; rank(union) = {r_both}")

F4 = four_basis()
print("== four-spin terms: Klein duals of dual-frame SU(2)-invariant (s.s)(s.s) ==")
for nm, cls, d4, sold in F4:
    # check: soldered group average of the Klein image of ONE seed equals the Klein image of the position average
    shape = nm.rstrip("0123"); pi = int(nm[len(shape):]); sites = SHAPES[shape][1]
    (i, j), (k, l) = PAIRINGS[pi]
    seed = {}
    for a in range(3):
        for b in range(3):
            add(seed, canon([(tuple(sites[i]), a), (tuple(sites[j]), a), (tuple(sites[k]), b), (tuple(sites[l]), b)]), 1.)
    ga = gavg(klein_rel(seed)); nrm = np.sqrt(hs(ga, ga)); ga = {q: v / nrm for q, v in ga.items()}
    dif = max(abs(ga.get(q, 0) - sold.get(q, 0)) for q in set(ga) | set(sold))
    print(f"  {nm:4s} {cls}: {len(sold):4d} strings; covariance defect {cov_defect(sold):.1e}; "
          f"|gavg(Klein seed) - Klein(posavg seed)| = {dif:.1e}")
for shape, (cls, sites) in SHAPES.items():
    ops = [klein_rel(strings4(posavg4(sites, pr))) for pr in PAIRINGS]
    r, _, _ = rank_of(ops)
    # full covariant count on this support: group averages of all 81 Pauli seeds
    allseeds = []
    for bs in itertools.product(range(3), repeat=4):
        o = gavg({canon([(tuple(sites[q]), bs[q]) for q in range(4)]): 1.})
        if o: allseeds.append(o)
    ra, _, _ = rank_of(allseeds)
    print(f"  shape {shape} ({cls}): dual SU(2)-invariant pairings rank {r}; ALL covariant weight-4 operators on this support: {ra}")
n1 = sum(1 for o in B2 if o[1] == "S1") + sum(1 for o in F4 if o[1] == "S1")
n2 = sum(1 for o in B2 if o[1] == "S2") + sum(1 for o in F4 if o[1] == "S2")
print(f"n(S1) = {n1} (bilinear {sum(1 for o in B2 if o[1]=='S1')}, four-spin {sum(1 for o in F4 if o[1]=='S1')}); "
      f"n(S2 extra) = {n2}; n(S1 u S2) = {n1 + n2}")
# Klein dual of SU(2) dot products at each separation, in the soldered basis (A44 check)
print("== Klein duals of dual-frame s.s per separation, expanded on the soldered basis ==")
for d, names in (((1, 0, 0), ("J1", "K1")), ((1, 1, 0), ("J2", "Kn2")), ((2, 0, 0), ("J3", "K3")), ((1, 1, 1), ("J4",))):
    du = normalize(klein_rel(gavg(bilinear(d, np.eye(3)))))
    basis = [op for nm, cls, op in B2 if nm in names]
    G = np.array([[hs(a, b) for b in basis] for a in basis]); v = np.array([hs(a, du) for a in basis])
    c = np.linalg.solve(G, v); res = hs(du, du) - v @ c
    print(f"  d={d}: dual s.s = " + " + ".join(f"{ci:+.4f} {nm}" for ci, nm in zip(c, names)) + f"  (residual {res:.1e})")
