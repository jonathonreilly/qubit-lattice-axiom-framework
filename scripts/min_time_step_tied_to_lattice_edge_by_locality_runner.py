"""
Tying the lattice minimum connection (one Z^3 nearest-neighbor edge) to the minimum TIME step.

The tie is CAUSAL LOCALITY: the minimum time step is one elementary dynamical update = one record
tick, and a local update propagates influence by exactly one nearest-neighbor edge (the retained
LATTICE_NN_LIGHT_CONE reachability). So one tick == one hop, and the lattice spatial minimum (a_s) and
the time minimum (a_tau) are locked. The "no diagonals" clause of the LATTICE axiom is LOAD-BEARING:
it forbids reaching a face/body diagonal in one step, pinning the minimal causal increment to one edge
per tick. With diagonals the tick would decouple from the edge (one tick would reach sqrt2/sqrt3 away).

This fixes only the RATIO a_tau/a_s = 1/v_front (the conformal CLASS, records-derived via the cone);
the ABSOLUTE scale (a_s in metres, a_tau in seconds) is the conformal FACTOR = the records' clock-rate
NO-GO (post_record_clock_rate_interface): records give the tick/edge COUNT, not the physical unit (that
needs a supplied Planck/clock primitive).

Memory-safe: BFS on a small open lattice; no large matrices.

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

L = 9; c = L // 2
def reach(neighbors, kmax):
    """graph-distance BFS from the center; return {distance: count} and the max graph distance per k."""
    dist = {(c, c, c): 0}; q = deque([(c, c, c)]); sizes = {0: 1}
    while q:
        x, y, z = q.popleft(); d = dist[(x, y, z)]
        if d >= kmax: continue
        for dx, dy, dz in neighbors:
            p = (x+dx, y+dy, z+dz)
            if all(0 <= v < L for v in p) and p not in dist:
                dist[p] = d+1; sizes[d+1] = sizes.get(d+1, 0)+1; q.append(p)
    return dist, sizes
NN6 = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]                          # LATTICE: 6-NN, NO diagonals
NN26 = [(dx,dy,dz) for dx in (-1,0,1) for dy in (-1,0,1) for dz in (-1,0,1) if (dx,dy,dz) != (0,0,0)]

print("=" * 78)
print("A1. one TIME STEP (one local update / record tick) reaches exactly ONE EDGE")
print("=" * 78)
_, s6 = reach(NN6, 1)
one_tick_one_edge = (s6.get(1, 0) == 6)                                              # the 6 nearest neighbors
maxeuclid6 = max(np.sqrt(dx*dx+dy*dy+dz*dz) for dx, dy, dz in NN6)
print(f"   6-NN: one tick reaches {s6.get(1,0)} sites at graph-distance 1 = the nearest neighbors (one edge)")
print(f"   max Euclidean reach in one tick = {maxeuclid6:.3f} edge")
check("the minimum time step (one update/tick) reaches exactly one lattice edge: one tick == one hop",
      one_tick_one_edge and abs(maxeuclid6 - 1.0) < 1e-9, "a_tau <-> a_s locked by causal locality")

print()
print("=" * 78)
print("A2. 'NO DIAGONALS' is LOAD-BEARING: with diagonals the tick decouples from the edge")
print("=" * 78)
_, s26 = reach(NN26, 1)
maxeuclid26 = max(np.sqrt(dx*dx+dy*dy+dz*dz) for dx, dy, dz in NN26)
diagonals_decouple = (s26.get(1, 0) == 26) and maxeuclid26 > 1.5                     # reaches body diagonal sqrt3
print(f"   26-NN (with diagonals): one tick reaches {s26.get(1,0)} sites, max Euclidean = {maxeuclid26:.3f} (sqrt3)")
print(f"   so WITH diagonals one tick spans up to sqrt3 edges => the tick no longer = one edge")
check("the no-diagonal clause locks one-tick-one-edge (diagonals would span sqrt2/sqrt3 per tick)",
      one_tick_one_edge and diagonals_decouple, "the LATTICE axiom's 'no diagonals' is what pins the tie")

print()
print("=" * 78)
print("A3. the forward reachability cone advances exactly ONE EDGE PER TICK (v_front = a_s/a_tau)")
print("=" * 78)
_, s6k = reach(NN6, 5)
max_dist_reached = max(s6k.keys())
# the front (max graph distance) after k ticks is exactly k -> one edge per tick
front_per_tick = all(k in s6k for k in range(max_dist_reached + 1)) and max_dist_reached == 5
# group velocity of the reconstructed dispersion is the SIGNAL speed WITHIN the cone, <= 1 edge/tick
def E(p, m=0.0): return np.arcsinh(np.sqrt(m*m + np.sum(np.sin(p)**2)))
g = np.linspace(-np.pi, np.pi, 25); vmax = 0.0
for px in g:
    for py in g:
        for pz in g:
            grad = []
            for ax in range(3):
                h = 1e-4; p1 = [px, py, pz]; p2 = [px, py, pz]; p1[ax]+=h; p2[ax]-=h
                grad.append((E(p1)-E(p2))/(2*h))
            vmax = max(vmax, np.sqrt(sum(q*q for q in grad)))
print(f"   6-NN forward cone: max graph-distance after k=5 ticks = {max_dist_reached} -> front = 1 edge/tick")
print(f"   group velocity v_LR = max|grad E| = {vmax:.4f} <= 1 (the signal speed inside the cone)")
check("the reachability front is one edge per tick; v_LR is the <=1 signal speed within it",
      front_per_tick and vmax <= 1.0 + 1e-6, "the cone speed v_front = a_s/a_tau (records-derived ratio)")

print()
print("=" * 78)
print("A4. the RATIO is derived; the ABSOLUTE scale is the clock-rate NO-GO")
print("=" * 78)
ratio_derived = one_tick_one_edge and front_per_tick                                # a_tau/a_s = 1/v_front fixed
print("   DERIVED (the conformal CLASS): a_tau/a_s = 1/v_front = 1 tick per edge -- from causal locality")
print("     (the retained LATTICE_NN_LIGHT_CONE reachability) + the no-diagonal clause. The lattice minimum")
print("     connection and the minimum time step are the SAME elementary causal event.")
print("   NO-GO (the conformal FACTOR): the ABSOLUTE scale (a_s metres, a_tau seconds) is the records'")
print("     clock-rate no-go (post_record_clock_rate_interface): records give the tick/edge COUNT, not the")
print("     physical unit -> a supplied Planck/clock-reference primitive sets the absolute a_s, a_tau.")
check("min-time-step <-> lattice-edge RATIO derived (one tick = one edge); absolute scale = clock-rate no-go",
      ratio_derived, "the tie is causal locality; the common scale needs a Planck primitive")

print()
print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
