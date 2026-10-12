"""R7-4 part 2b: same boost-flow shell test for the ordinary nearest-neighbour lattice KG band
omega^2 = m^2 + sum_i 4 sin^2(k_i/2) (d = 2), plus the x-periods tau(k_y) = closed-loop integral dk_x/omega
of the four legs (distinct, generically rationally independent periods => the x-flow cannot keep
E_in(s) = E_out(s) unless omega is flat along the legs' lines)."""
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import quad
rng = np.random.default_rng(5); m = 1.0
def om(k): return np.sqrt(m**2 + 4 * np.sin(k[0] / 2)**2 + 4 * np.sin(k[1] / 2)**2)
def sample():
    while True:
        k1 = rng.uniform(-1.2, 1.2, 2); k2 = rng.uniform(-1.2, 1.2, 2); K = k1 + k2; E = om(k1) + om(k2)
        k3x = rng.uniform(-1.2, 1.2)
        g = lambda y: om([k3x, y]) + om(K - np.array([k3x, y])) - E
        ys = np.linspace(-np.pi, np.pi, 400); vals = [g(y) for y in ys]
        for i in range(len(ys) - 1):
            if vals[i] * vals[i + 1] < 0:
                y = brentq(g, ys[i], ys[i + 1], xtol=1e-14); k3 = np.array([k3x, y]); k4 = K - k3
                if min(np.linalg.norm(k3 - k1), np.linalg.norm(k3 - k2)) > 0.05:
                    return [k1, k2], [k3, k4]
def flow(ins, outs, n, smax=12.0, ds=2e-3):
    legs = [k.copy() for k in ins + outs]; n = np.asarray(n, float); s = 0; so = None; md = 0
    while s < smax:
        f = lambda L: [om(k) * n for k in L]
        a1 = f(legs); a2 = f([l + .5 * ds * d for l, d in zip(legs, a1)]); a3 = f([l + .5 * ds * d for l, d in zip(legs, a2)])
        a4 = f([l + ds * d for l, d in zip(legs, a3)])
        legs = [l + ds / 6 * (p + 2 * q + 2 * r + t) for l, p, q, r, t in zip(legs, a1, a2, a3, a4)]; s += ds
        dE = abs(om(legs[0]) + om(legs[1]) - om(legs[2]) - om(legs[3])); md = max(md, dE)
        if so is None and dE > 1e-6: so = s
    return so, md
def tau(ky): return quad(lambda kx: 1 / om([kx, ky]), -np.pi, np.pi, epsabs=1e-13)[0]
out = []
cnt = 0
for t in range(10):
    ins, outs = sample()
    e0 = om(ins[0]) + om(ins[1]) - om(outs[0]) - om(outs[1])
    so, md = flow(ins, outs, (1.0, 0.0))
    taus = [tau(k[1]) for k in ins + outs]
    cnt += so is not None
    out.append(f"config {t}: |E_in-E_out|_0={abs(e0):.1e}; x-flow leaves shell at s={so}, max|dE|={md:.3f}; "
               f"x-periods tau(k_y) of legs = {', '.join(f'{x:.6f}' for x in taus)}")
out.append(f"KG band, non-forward on-shell configs leaving the shell under the x-boost flow: {cnt}/10")
print("\n".join(out))
