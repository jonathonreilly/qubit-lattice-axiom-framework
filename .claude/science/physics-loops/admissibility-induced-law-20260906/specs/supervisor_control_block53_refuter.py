"""Block 53 refuting pass (supervisor-run; machinery disjoint from the runner: symbolic solving, a sparse numerical solve, a transform solve, a
simulation).
W1  a general linear nearest-neighbour law with seven symbolic coefficients: covariance under two generating rotations plus the shift symmetry
    leaves only c_0 (u_x - (1/6) sum of neighbours).
W2  the power mean of order p with symbolic p: all first derivatives at the uniform point are 1/6; the second-order term (one neighbour up by d,
    the opposite one down by d) is (p - 1) d^2/6: forced first order, free second order.
W3  the field of one source on a large box with the field held at zero on the walls (sparse solve): u r approaches 6 log(kappa)/(4 pi) and is the
    same along an axis and along a body diagonal within a few per cent (floating point).
W4  twelve records at random on a 16^3 torus (transform solve): the field is the sum of the single fields to rounding, and the pair term is symmetric.
W5  a test record whose hops are timed by the clock of the site it sits on, simulated on a 3x3x3 torus: time spent at a site proportional to 1/w."""
import random
import sys
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

ROOT = Path(__file__).resolve().parents[5]
results = []


def report(tag, ok, msg):
    results.append(ok)
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}")


# ------------------------------------------------------------------------------------------------ W1
c0, cxp, cxm, cyp, cym, czp, czm = sp.symbols("c0 cxp cxm cyp cym czp czm")
coef = {(1, 0, 0): cxp, (-1, 0, 0): cxm, (0, 1, 0): cyp, (0, -1, 0): cym, (0, 0, 1): czp, (0, 0, -1): czm}
rot_z = lambda v: (-v[1], v[0], v[2])                                   # quarter turn about z
rot_x = lambda v: (v[0], -v[2], v[1])                                   # quarter turn about x
eqs = []
for rot in (rot_z, rot_x):
    for e, c in coef.items():
        eqs.append(sp.Eq(coef[rot(e)], c))
eqs.append(sp.Eq(c0 + sum(coef.values()), 0))                           # constants solve the homogeneous law
sol = sp.solve(eqs, [cxp, cxm, cyp, cym, czp, czm], dict=True)
ok = len(sol) == 1 and all(sp.simplify(sol[0][c] + c0 / 6) == 0 for c in coef.values())
report("W1", ok, f"symbolic: covariance under quarter turns about two axes and the shift symmetry force every neighbour coefficient to be {sol[0][cxp] if sol else None}")

# ------------------------------------------------------------------------------------------------ W2
p, d = sp.symbols("p d")
w = sp.symbols("w1:7", positive=True)
mean_p = (sum(x ** p for x in w) / 6) ** (1 / p)
first = [sp.simplify(sp.diff(mean_p, x).subs({y: 1 for y in w})) for x in w]
bumped = mean_p.subs({w[0]: 1 + d, w[1]: 1 - d, w[2]: 1, w[3]: 1, w[4]: 1, w[5]: 1})
second = sp.simplify(sp.series(bumped, d, 0, 3).removeO().coeff(d, 2))
report("W2", all(f == sp.Rational(1, 6) for f in first) and sp.simplify(second - (p - 1) / 6) == 0, f"symbolic power mean of order p: first derivatives at the uniform point {set(first)}; second-order coefficient {second}: it depends on p")

# ------------------------------------------------------------------------------------------------ W3
L = 41
c = L // 2
idx = -np.ones((L, L, L), int)
interior = [(x, y, z) for x in range(1, L - 1) for y in range(1, L - 1) for z in range(1, L - 1)]
for i, s in enumerate(interior):
    idx[s] = i
a = lil_matrix((len(interior), len(interior)))
b = np.zeros(len(interior))
for i, (x, y, z) in enumerate(interior):
    a[i, i] = 1.0
    for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        j = idx[x + dx, y + dy, z + dz]
        if j >= 0:
            a[i, j] = -1.0 / 6
log_kappa = -0.3
b[idx[c, c, c]] = log_kappa
u = spsolve(a.tocsr(), b)
val = lambda v: u[idx[c + v[0], c + v[1], c + v[2]]]
target = 6 * log_kappa / (4 * np.pi)
# the walls shift the field near the centre by a nearly constant amount, so compare DIFFERENCES of the field with differences of 1/r
slope_axis = (val((5, 0, 0)) - val((10, 0, 0))) / (1 / 5.0 - 1 / 10.0)
r3, r6 = np.sqrt(27.0), np.sqrt(108.0)
slope_diag = (val((3, 3, 3)) - val((6, 6, 6))) / (1 / r3 - 1 / r6)
ok = abs(slope_axis / target - 1) < 0.06 and abs(slope_diag / target - 1) < 0.06 and abs(slope_axis / slope_diag - 1) < 0.04
report("W3", ok, f"one source on a 41^3 box with zero walls: the field's difference between r = 5 and 10 along an axis, over the difference of 1/r, is {slope_axis:.4f}; between r = 5.20 and 10.39 along a body diagonal {slope_diag:.4f}; against 6 log(kappa)/(4 pi) = {target:.4f} on the infinite lattice; axis over diagonal {slope_axis / slope_diag:.4f} (block 51's creeping wind had 1.30)")

# ------------------------------------------------------------------------------------------------ W4
n = 16
k = 2 * np.pi * np.fft.fftfreq(n)
KX, KY, KZ = np.meshgrid(k, k, k, indexing="ij")
symbol = 1 - (np.cos(KX) + np.cos(KY) + np.cos(KZ)) / 3
symbol[0, 0, 0] = 1.0


def field(src):
    s_hat = np.fft.fftn(src - src.mean())
    s_hat[0, 0, 0] = 0
    return np.real(np.fft.ifftn(s_hat / symbol))


rng = np.random.default_rng(53)
sites = [tuple(rng.integers(0, n, 3)) for _ in range(12)]
singles = []
for s in sites:
    src = np.zeros((n, n, n)); src[s] += log_kappa
    singles.append(field(src))
src = np.zeros((n, n, n))
for s in sites:
    src[s] += log_kappa
together = field(src)
ok = np.max(np.abs(together - sum(singles))) < 1e-12 and abs(singles[0][sites[1]] - singles[1][sites[0]]) < 1e-12
report("W4", ok, f"twelve records on a 16^3 torus: largest difference between the joint field and the sum of single fields {np.max(np.abs(together - sum(singles))):.1e}; pair term symmetric to {abs(singles[0][sites[1]] - singles[1][sites[0]]):.1e}")

# ------------------------------------------------------------------------------------------------ W5
random.seed(53)
side = 3
rate = {(x, y, z): 1 + ((3 * x + 5 * y + 7 * z) % 11) / 13 for x in range(side) for y in range(side) for z in range(side)}
pos = (0, 0, 0)
spent = {s: 0.0 for s in rate}
for _ in range(1500000):
    spent[pos] += random.expovariate(rate[pos])
    e = random.choice(((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)))
    pos = tuple((pos[i] + e[i]) % side for i in range(3))
total = sum(spent.values())
norm = sum(1 / r for r in rate.values())
worst = max(abs(spent[s] / total - (1 / rate[s]) / norm) / ((1 / rate[s]) / norm) for s in rate)
report("W5", worst < 0.03, f"simulation of a test record timed by the local clock (1500000 hops): share of time at each of the 27 sites against 1/w, largest relative difference {worst:.3f}")

print(f"REFUTER TOTAL: PASS={sum(results)} FAIL={len(results) - sum(results)}")
sys.exit(0 if all(results) else 1)
