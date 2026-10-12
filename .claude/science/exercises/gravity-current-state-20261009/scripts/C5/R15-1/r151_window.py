"""R15-1 (b), step 4: map the unhealthy region of the scalar-matter test in (y = g/H^2, x = chidot^2/H^2),
frozen background, V' = V'' = gdot = 0 (and a V'' > 0 variant), a = H = 1, k in units of aH.
Unhealthy = A(k) < 0 (ghost) or omega^2 = M/A < -H^2 (tachyon faster than Hubble) for some k in [1e-3, 1e3].
"""
import pickle, numpy as np, sympy as sp
d = pickle.load(open('r151_dispersion.pkl', 'rb'))
A, M = d['A'], d['M']
fs = {s.name: s for s in (A.free_symbols | M.free_symbols)}
names = ('k', 'aa', 'H', 'chidot', 'g', 'gdot', 'Vp', 'Vpp')
args = [fs.get(n, sp.Symbol(n)) for n in names]
fA = sp.lambdify(args, A, 'numpy'); fM = sp.lambdify(args, M, 'numpy')
ks = np.logspace(-3, 3, 601)
for Vpp in [0.0, 1.0]:
    print(f"V'' = {Vpp} H^2")
    for x in [0.1, 1.0, 3.0]:
        row = []
        for y in [-1000, -100, -10, -3, -1, 0, 0.5, 1, 2, 3, 4, 5, 5.9, 6.1, 10, 100]:
            Av = fA(ks, 1., 1., np.sqrt(x), y, 0., 0., Vpp); Mv = fM(ks, 1., 1., np.sqrt(x), y, 0., 0., Vpp)
            w2 = Mv/Av
            ghost = np.any(Av < 0); tach = np.nanmin(w2) < -1.0
            tag = 'G' if ghost else ('T' if tach else '.')
            row.append(f"{y:+g}:{tag}(min w2={np.nanmin(w2):+.1e})")
        print(f"  x = chidot^2/H^2 = {x}: " + "  ".join(row))
