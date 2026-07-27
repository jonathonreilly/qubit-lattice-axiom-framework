"""Bounded diagnostics for the minimum-time/lattice-edge identification gate.

The runner checks only a chosen 6-neighbor relation, a chosen 26-neighbor
comparison, their finite BFS reachability, and a separate dispersion-model
group-velocity grid. It does not identify an update tick with a record tick or
physical elapsed time, prove that every allowed neighbor changes, derive a
physical speed or time/edge ratio, or set an absolute scale.

Memory-safe: BFS on a small open lattice; no large matrices.
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
print("A1. chosen 6-neighbor relation: one-step combinatorial support")
print("=" * 78)
_, s6 = reach(NN6, 1)
one_tick_one_edge = (s6.get(1, 0) == 6)                                              # the 6 nearest neighbors
maxeuclid6 = max(np.sqrt(dx*dx+dy*dy+dz*dz) for dx, dy, dz in NN6)
print(f"   6-NN: the chosen relation has {s6.get(1,0)} graph-distance-1 successors")
print(f"   max Euclidean radius of those relation edges = {maxeuclid6:.3f} lattice edge")
check("chosen 6-NN relation has six successors at Euclidean edge radius 1",
      one_tick_one_edge and abs(maxeuclid6 - 1.0) < 1e-9,
      "combinatorial relation fact only")

print()
print("=" * 78)
print("A2. chosen 26-neighbor comparison includes face and body diagonals")
print("=" * 78)
_, s26 = reach(NN26, 1)
maxeuclid26 = max(np.sqrt(dx*dx+dy*dy+dz*dz) for dx, dy, dz in NN26)
diagonals_decouple = (s26.get(1, 0) == 26) and maxeuclid26 > 1.5                     # reaches body diagonal sqrt3
print(f"   26-neighbor relation: {s26.get(1,0)} graph-distance-1 successors, max Euclidean radius {maxeuclid26:.3f}")
check("chosen 26-neighbor comparison reaches body-diagonal radius sqrt(3)",
      one_tick_one_edge and diagonals_decouple,
      "comparison of declared relations, not a physical time statement")

print()
print("=" * 78)
print("A3. chosen 6-neighbor cumulative reachability has graph radius five at step five")
print("=" * 78)
_, s6k = reach(NN6, 5)
max_dist_reached = max(s6k.keys())
# The finite BFS reaches every graph-distance shell through five.
front_per_tick = all(k in s6k for k in range(max_dist_reached + 1)) and max_dist_reached == 5
print(f"   chosen 6-NN relation: maximum graph distance after five recurrences = {max_dist_reached}")
check("chosen 6-NN cumulative relation reaches graph radius five at step five",
      front_per_tick,
      "potential relation support only; not guaranteed realized differences")

print()
print("=" * 78)
print("A4. separate dispersion-model finite-grid group-velocity diagnostic")
print("=" * 78)
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
print(f"   separate model max|grad E| on the finite grid = {vmax:.4f}")
check("separate dispersion model has sampled max|grad E| <= 1",
      vmax <= 1.0 + 1e-6,
      "model diagnostic only; not a Lieb-Robinson or physical-speed theorem")

print()
print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"per_element: checked — one chosen 6-neighbor relation edge has Euclidean radius {maxeuclid6:.6f} and exactly {s6.get(1,0)} successors.")
print(f"per_site: checked — the center site has 6 chosen nearest neighbors versus {s26.get(1,0)} neighbors in the explicit diagonal comparison.")
print(f"per_mode: checked — the separate 25^3 momentum-grid dispersion diagnostic has sampled max |grad E|={vmax:.6f}.")
print(f"per_block: checked — five cumulative BFS recurrences reach every graph shell through radius {max_dist_reached}; front completeness={front_per_tick}.")
print(f"lattice_wide: checked — the L={L} finite relation supports only combinatorial reachability, not a physical tick/edge identification; PASS={PASS}, FAIL={FAIL}.")
if FAIL:
    raise SystemExit(1)
