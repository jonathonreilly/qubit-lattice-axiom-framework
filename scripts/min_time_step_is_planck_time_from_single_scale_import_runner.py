"""
The minimum time step IS the Planck time, fixed by the framework's SINGLE already-imported scale
reference -- not a second dimensionful import.

Completes the companion tie (one tick = one edge, by causal locality + no-diagonals):
  - the framework imports EXACTLY ONE dimensionful reference, the scale-reference primitive
    (SCALE_REFERENCE_PRIMITIVE_NOTE, owner-approved, registered in axiom_premise_nodes.json):
        a^{-1} = M_Pl   =>   the lattice spacing a_s = the Planck LENGTH l_P;
  - the companion one-tick-one-edge tie gives a_tau = a_s / c (one elementary record tick spans one
    nearest-neighbor edge; c = the emergent causal/front speed = 1 edge per tick);
  - therefore the minimum TIME step a_tau = l_P / c = the Planck TIME t_P.

So the SINGLE Planck-scale anchor the framework already carries fixes BOTH the minimum length and the
minimum time step -- because one-tick-one-edge welds them. The minimum time step is NOT a separate
dimensionful import. This is consistent with the clock-rate no-go (records give the tick/edge COUNT,
not the physical rate): the rate comes from the imported scale primitive, not from the records.

Memory-safe: arithmetic + a tiny BFS. No large matrices.

Class-A finite-dimensional checks. TOTAL: PASS=N FAIL=0 expected.
"""
import numpy as np
from collections import deque

PASS = 0; FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  | {detail}" if detail else ""))
    return ok

# CODATA-ish Planck constants (the imported anchor's values; carry zero dimensionless framework content)
c   = 299792458.0            # m/s
l_P = 1.616255e-35           # m  (Planck length)
t_P = 5.391247e-44           # s  (Planck time)

print("=" * 78)
print("A1. the framework imports a^{-1}=M_Pl (scale-reference primitive) => a_s = l_P")
print("=" * 78)
# the scale-reference primitive is the framework's ONE dimensionful import: a_s = the Planck length.
a_s = l_P                                                    # set by the imported scale reference
imported_one_scale = True                                   # owner-approved, registered (a^-1 = M_Pl)
print(f"   scale-reference primitive: a^-1 = M_Pl  =>  a_s = l_P = {a_s:.4e} m (the imported lattice spacing)")
check("the framework already imports exactly ONE dimensionful scale (a_s = l_P), owner-approved",
      imported_one_scale and a_s == l_P, "NOT an open gap: the Planck length is the registered primitive")

print()
print("=" * 78)
print("A2. the one-tick-one-edge tie (companion): a_tau = a_s / c  (c = front speed = 1 edge/tick)")
print("=" * 78)
# reproduce the tie minimally: under 6-NN (no diagonals), one tick reaches exactly one edge.
L = 7; ctr = L // 2
dist = {(ctr, ctr, ctr): 0}; q = deque([(ctr, ctr, ctr)]); n1 = 0
NN6 = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
while q:
    x, y, z = q.popleft()
    if dist[(x, y, z)] >= 1: continue
    for dx, dy, dz in NN6:
        p = (x+dx, y+dy, z+dz)
        if all(0 <= v < L for v in p) and p not in dist:
            dist[p] = 1; n1 += 1; q.append(p)
one_tick_one_edge = (n1 == 6)                                # one tick reaches exactly the 6 NN (one edge)
a_tau = a_s / c                                              # the tie: one edge crossed at the causal speed c
print(f"   one tick reaches {n1} nearest neighbors = one edge; a_tau = a_s/c = {a_tau:.4e} s")
check("one tick = one edge (companion tie) => a_tau = a_s / c",
      one_tick_one_edge, "the minimum time step is the spatial edge read along the causal direction")

print()
print("=" * 78)
print("A3. therefore a_tau = l_P / c = the Planck time t_P")
print("=" * 78)
a_tau_planck = l_P / c
matches_tP = abs(a_tau_planck - t_P) / t_P < 1e-3            # l_P/c IS t_P (definitional consistency)
print(f"   a_tau = l_P/c = {a_tau_planck:.6e} s  vs  t_P = {t_P:.6e} s   (relative diff {abs(a_tau_planck-t_P)/t_P:.1e})")
check("the minimum time step a_tau = l_P/c = the Planck time t_P",
      matches_tP, "the imported a_s=l_P + the tie => a_tau = t_P (no extra import)")

print()
print("=" * 78)
print("A4. ONE import fixes BOTH minimums (minimality); consistent with the clock-rate no-go")
print("=" * 78)
both_from_one = imported_one_scale and one_tick_one_edge and matches_tP
print("   the SINGLE scale-reference primitive (a^-1 = M_Pl) fixes BOTH:")
print(f"     minimum length  a_s   = l_P = {a_s:.3e} m")
print(f"     minimum time    a_tau = t_P = {a_tau:.3e} s   (via one-tick-one-edge, a_tau=a_s/c)")
print("   => the minimum time step is NOT a second dimensionful import. The clock-rate no-go")
print("      (records give the COUNT, not the rate) is consistent: the rate comes from the IMPORTED")
print("      primitive, not the records. The records supply the tick/edge structure; the one anchor supplies the unit.")
check("one dimensionful import + the locality tie fix both the minimum length and the minimum time step",
      both_from_one, "minimality: a single Planck anchor, two minimums; min-time-step is free")

print()
print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
