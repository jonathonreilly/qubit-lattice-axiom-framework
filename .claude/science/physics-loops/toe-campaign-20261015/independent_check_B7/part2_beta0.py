"""Part 2i: find a spinorial two-layer walk with beta = 0 (exactly isotropic spin-3/2 cone at linear
order: velocities 3a/2, a/2) by bisection along a path between two random walks with opposite beta
sign. NUMERICAL."""
import numpy as np
from part2_isotropy import alpha_beta
from part2_cone import quat, eff_h, dirs
rng = np.random.default_rng(5)
P = [(rng.normal(size=4), rng.normal(size=4)) for t in range(4)]
x0 = np.concatenate(P[0]); x1 = np.concatenate(P[3])
def ab(s):
    x = (1 - s) * x0 + s * x1
    r = alpha_beta(quat(x[:4]), quat(x[4:]))
    return r[0][1], r[0][2], r[0][0]
for s in np.linspace(0, 1, 11): print(f"s={s:.1f} alpha,beta,omega0 = {np.round(ab(s),5)}")
lo, hi = 0.0, 1.0
blo = ab(lo)[1]
for it in range(50):
    m = (lo + hi) / 2; bm = ab(m)[1]
    if np.sign(bm) == np.sign(blo): lo, blo = m, bm
    else: hi = m
x = (1 - lo) * x0 + lo * x1
al, be, w0 = ab(lo)
print("beta=0 point: s =", lo, " alpha", al, " beta", be, " omega0", w0)
qA, qB = quat(x[:4]), quat(x[4:])
lam, Pp, hs = eff_h(qA, qB)[0]
sp = np.array([np.sort(np.linalg.eigvalsh(sum(n[j] * hs[j] for j in range(3)))) for n in dirs(300)])
print("velocities along 300 directions: min", np.round(sp.min(0), 6), " max", np.round(sp.max(0), 6))
print("qA coeffs", np.round(x[:4] / np.linalg.norm(x[:4]), 6), " qB coeffs", np.round(x[4:] / np.linalg.norm(x[4:]), 6))
