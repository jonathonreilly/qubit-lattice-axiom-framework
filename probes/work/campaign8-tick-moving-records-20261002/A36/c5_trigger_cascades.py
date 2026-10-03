"""
A36 check C5: ticks set by neighbouring record events with zero delay (no shared clock, no memory).

Rule (supplied toy): when a record forms, every empty neighbour fires its formation instrument at that same
instant (a set time that needs no clock); a site fires at most once per cascade (one instrument per site
per instant, A28 Step 0 / I2) and forms with chance F. A formation triggers its own empty neighbours, so a
cascade is a site-percolation cluster grown from the seed, all at ONE instant of the change.
Reported: the reach of the cascade (lattice distance from the seed) at zero elapsed time, in 1D (exact:
P(reach >= d) = F^d per side) and on a 3D box of half-width 30 (Monte Carlo via cluster labelling).
"""
import signal, time
import numpy as np
from scipy import ndimage
signal.alarm(55)
t0 = time.time()
rng = np.random.default_rng(5)

print("C5a. 1D: P(cascade reaches >= d sites to the right) vs F^d")
for F in (0.3, 0.6):
    runs = 200000
    # reach to the right = number of consecutive successes
    u = rng.random((runs, 12)) < F
    reach = np.argmin(np.concatenate([u, np.zeros((runs, 1), bool)], axis=1), axis=1)
    for d in (1, 3, 6):
        print(f"  F={F} d={d}: MC {np.mean(reach >= d):.5f}  exact F^d {F**d:.5f}")

print("\nC5b. 3D box (61^3), seed at the centre; cascade = open cluster (site chance F) touching the seed.")
print("     F       mean sites   P(reach>=10)  P(reach>=20)  P(hits box edge, 30)")
R = 30
shape = (2 * R + 1,) * 3
g = np.indices(shape) - R
l1 = np.abs(g).sum(axis=0)
linf = np.abs(g).max(axis=0)
struct = ndimage.generate_binary_structure(3, 1)
for F, runs in ((0.10, 30), (0.20, 30), (0.25, 30), (0.30, 30), (0.35, 30), (0.45, 20)):
    sizes, r10, r20, edge = [], 0, 0, 0
    for _ in range(runs):
        op = rng.random(shape) < F
        op[R, R, R] = True                     # the seed record itself
        lab, n = ndimage.label(op, structure=struct)
        cl = lab == lab[R, R, R]
        sizes.append(int(cl.sum()) - 1)
        rmax = int(l1[cl].max())
        r10 += rmax >= 10; r20 += rmax >= 20
        edge += int(linf[cl].max()) >= R
    print(f"     {F:<7} {np.mean(sizes):<12.1f} {r10/runs:<13.2f} {r20/runs:<13.2f} {edge/runs:.2f}")
    if time.time() - t0 > 45:
        print("     [stopped early for the time budget]")
        break
print(f"  [elapsed {time.time()-t0:.1f}s]  (site-percolation threshold on the simple cubic lattice is about 0.3116: COMPARATOR)")
