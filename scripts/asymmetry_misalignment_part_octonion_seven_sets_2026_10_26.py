#!/usr/bin/env python3
"""Sharpened T1: invariant maximal anticommuting 7-sets (Cl(0,7) / octonion left-multiplication sets) of
logical Paulis under G (168) and under the qubit stabiliser F21 (21); count all such 7-sets for reference."""
import itertools, collections
exec(__import__('pathlib').Path(__file__).with_name('asymmetry_misalignment_part_logical_orbits_2026_10_26.py').read_text().split("orb = []")[0])   # reuse: G, S, N, canon, reps, zero, act, FR, symp, mul
nz = [r for r in reps if r != zero]
# all maximal anticommuting 7-sets among the 63 nonzero logical classes (3 logical qubits => max size 7)
adj = {a: {b for b in nz if b != a and symp(a, b) == 1} for a in nz}
sets7 = set()
def grow(cur, cand):
    if len(cur) == 7: sets7.add(frozenset(cur)); return
    for c in sorted(cand):
        if cur and c < max(cur): continue
        grow(cur + [c], cand & adj[c])
grow([], set(nz))
print("maximal anticommuting 7-sets of logical classes:", len(sets7))
def img(Sset, g): return frozenset(canon(act(a, g[0], FR[g[1]])) for a in Sset)
inv_G = [s for s in sets7 if all(img(s, g) == s for g in G)]
F21 = [g for g in G if g[0][0] == 0]
assert len(F21) == 21
inv_F21 = [s for s in sets7 if all(img(s, g) == s for g in F21)]
Z7 = [g for g in F21 if g[1] == 'id']
inv_Z7 = [s for s in sets7 if all(img(s, g) == s for g in Z7)]
print("G-invariant 7-sets:", len(inv_G), "; F21(qubit-0 stabiliser)-invariant:", len(inv_F21), "; Z7-invariant:", len(inv_Z7))
# for comparison: the Lagrangian (commuting) 7-sets invariant under F21
lag = set()
for a, b in itertools.combinations(nz, 2):
    if symp(a, b): continue
    for c in nz:
        if c in (a, b) or symp(a, c) or symp(b, c): continue
        sp = {canon(mul(mul(a if i & 1 else zero, b if i & 2 else zero), c if i & 4 else zero)) for i in range(8)}
        if len(sp) == 8: lag.add(frozenset(sp - {zero}))
print("Lagrangians (3-dim isotropic) of the logical space:", len(lag), "; G-invariant:", sum(all(img(s, g) == s for g in G) for s in lag),
      "; F21-invariant:", sum(all(img(s, g) == s for g in F21) for s in lag))
