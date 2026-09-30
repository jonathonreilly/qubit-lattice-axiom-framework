"""Kill-check T62: number variance of the CHESSBOARD (the attacker's 'ordered' control) in BALL windows with random centres,
versus cube windows.  Cube windows: bounded (s~0).  Ball windows: Var ~ r^2 (lattice-point discrepancy)?"""
import numpy as np
rng = np.random.default_rng(5)
def count_ball(r, centers):
    m = int(np.ceil(r)) + 2
    g = np.arange(-m, m+1)
    X, Y, Z = np.meshgrid(g, g, g, indexing='ij')
    par = ((X+Y+Z) % 2 == 0)
    out = []
    for c in centers:
        d2 = (X-c[0])**2 + (Y-c[1])**2 + (Z-c[2])**2
        out.append(np.count_nonzero((d2 <= r*r) & par))
    return np.array(out)
rs = [3, 4, 6, 8, 12, 16, 24]
res = []
print("ball windows, chessboard, 4000 random continuous centres each (shift of a parity-preserving lattice: centre parity handled by random integer offset)")
for r in rs:
    cen = rng.random((4000, 3)) * 2      # period-2 lattice of the even sublattice is fcc-like; centres uniform in a period cell
    N = count_ball(r, cen)
    res.append((r, N.mean(), N.var()))
    print("r=%-3d mean=%9.2f  var=%8.3f  var/r^2=%6.3f  var/mean=%7.4f" % (r, N.mean(), N.var(), N.var()/r**2, N.var()/N.mean()))
r = np.array([x[0] for x in res], float); v = np.array([x[2] for x in res])
p = np.polyfit(np.log(r[2:]), np.log(v[2:]), 1)
print("local slope Var ~ r^s, s = %.2f (r>=6); cubes give bounded Var (s~0)" % p[0])
