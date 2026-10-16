import re, numpy as np, sympy as sp
from scipy.optimize import least_squares
s = open('nn_min.out').read()
blk = s.split('== component 8')[1]
body = blk.split('\n', 1)[1].split('== component')[0]
body = re.sub(r'_\[\d+\]=', '', body)
gens = [g.strip() for g in body.replace('\n', '').split(',') if g.strip()]
c = sp.symbols('c0:11'); cb = sp.symbols('cb0:11'); loc = {**{f'c{i}': c[i] for i in range(11)}, **{f'cb{i}': cb[i] for i in range(11)}}
G = [sp.sympify(g.replace('^', '**'), locals=loc) for g in gens]
print(len(G), 'generators')
F = sp.lambdify(list(c) + list(cb), G, 'numpy')
def res(x, delta):
    z = x[:11] + 1j * x[11:]
    v = np.array(F(*z, *np.conj(z)), complex)
    mixed = np.sum(np.abs(z[[3, 4, 5, 6]]) ** 2)
    return np.concatenate([v.real, v.imag, [10 * max(0, delta - mixed)]])
rng = np.random.default_rng(0)
for delta in (0.01, 0.1, 0.3):
    best = 1e9
    for t in range(40):
        r = least_squares(res, rng.normal(size=22) * 0.5, args=(delta,), xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=4000)
        best = min(best, np.linalg.norm(r.fun))
    print('delta', delta, 'best residual', best, flush=True)
