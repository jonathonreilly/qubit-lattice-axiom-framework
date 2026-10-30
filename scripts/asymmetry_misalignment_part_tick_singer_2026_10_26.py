#!/usr/bin/env python3
"""T2: can the CL-1 cell tick U1(k) or the adopted FREEZE tick U_F(K) (8 cell components = 8 cube sites) commute with
a Singer-type site permutation (order 7, one fixed site), dressed by arbitrary diagonal phases?  Necessary condition:
the elementwise modulus |U| must be invariant under the permutation for every K (internal symmetry), or covariant
under some K -> gK (point-group-like).  Also: which site permutations preserve |U| at all (the tick's own monomial group)."""
import itertools, collections, numpy as np
exec(__import__('pathlib').Path(__file__).with_name('asymmetry_misalignment_part_freeze_tick_rebuild_2026_10_26.py').read_text())        # defines U1, UF, CELL, IDX, rng, ...
Ks = [np.array(v) for v in ([0.37, -1.1, 0.8], [2.2, 0.4, -0.3], [-0.9, 1.7, 2.5], [0.0, 0.0, 0.0])]
def ctype(p):
    seen = set(); c = []
    for i in range(8):
        if i in seen: continue
        L = 0; j = i
        while j not in seen: seen.add(j); j = p[j]; L += 1
        c.append(L)
    return tuple(sorted(c))
perms = list(itertools.permutations(range(8)))
def inv_perms(Uf, Ks, tol=1e-9):
    out = []
    mods = [np.abs(Uf(K)) for K in Ks]
    for p in perms:
        Pm = np.eye(8)[list(p)].T     # Pm e_j = e_p[j]
        if all(np.abs(Pm @ M @ Pm.T - M).max() < tol for M in mods): out.append(p)
    return out
for name, Uf in (("CL-1 U1(k), eps=0.3", lambda K: U1(K)), ("CL-1 U1(k), eps=1.1", lambda K: U1(K, 1.1)), ("FREEZE U_F(K)", UF)):
    ip = inv_perms(Uf, Ks)
    print(f"{name}: site permutations preserving |U(K)| for all test K (internal): {len(ip)}; cycle types {dict(collections.Counter(ctype(p) for p in ip))}")
    # covariant version: |U(gK)| = P |U(K)| P^T with g in signed 3x3 permutations (O_h on momenta); count perms by type
    cov = collections.Counter()
    gs = [np.array(np.eye(3)[list(q)]) @ np.diag(s) for q in itertools.permutations(range(3)) for s in itertools.product([1, -1], repeat=3)]
    found7 = 0
    p7 = [p for p in perms if ctype(p) == (1, 7)]
    MK = [np.abs(Uf(K)) for K in Ks[:2]]                       # moduli computed once (same test as before)
    for g in gs:
        MgK = [np.abs(Uf(g @ K)) for K in Ks[:2]]
        for p in p7:
            Pm = np.eye(8)[list(p)].T
            if all(np.abs(Pm @ a @ Pm.T - b).max() < 1e-9 for a, b in zip(MK, MgK)): found7 += 1
    print(f"   order-7 (Singer-type) site permutations covariant with ANY O_h momentum map: {found7}")
