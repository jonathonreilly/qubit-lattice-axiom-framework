"""A55 c5: (i) uniform flux phi through every plaquette, field along the record diagonal f0=(1,1,1) (gauge
theta = (0, phi x, phi (y - x)), magnetic cell q x q x 1): half-filling direct gap and nodes for phi = pi/2, 2pi/3,
pi/3 (and checks phi = 0, pi); (ii) band-bottom effective masses (empty vacuum) for zero and pi flux;
(iii) mean-field critical nearest-neighbour repulsion for a spontaneous staggered (CDW) mass in pi flux."""
import signal, itertools
signal.alarm(100)
import numpy as np
from scipy.optimize import minimize

def bloch(phi, q, ks):
    n = q * q; S = [(x, y) for x in range(q) for y in range(q)]; I = {s: i for i, s in enumerate(S)}
    H = np.zeros((len(ks), n, n), complex)
    for (x, y) in S:
        a = I[(x, y)]
        for e, th in [((1, 0, 0), 0.0), ((0, 1, 0), phi * x), ((0, 0, 1), phi * (y - x))]:
            b = I[((x + e[0]) % q, (y + e[1]) % q)]
            ph = np.exp(1j * th) * np.exp(1j * ks @ np.array(e))
            H[:, b, a] += -ph
            H[:, a, b] += -np.conj(ph)
    return H
print("(i) uniform flux phi per plaquette, B along (1,1,1) (covariant given uniform records f0):")
for (p, q) in [(0, 1), (1, 2), (1, 4), (1, 3), (1, 6)]:
    phi = 2 * np.pi * p / q; n = q * q
    g = np.linspace(0, 2 * np.pi / q, 13, endpoint=False); gz = np.linspace(0, 2 * np.pi, 25, endpoint=False)
    KG = np.array([[a, b, c] for a in g for b in g for c in gz])
    E = np.linalg.eigvalsh(bloch(phi, q, KG))
    if n % 2:
        Ef = np.sort(E.ravel())[E.size // 2]
        print("  phi=2pi*%d/%d: %d bands per cell, half filling = %.1f bands -> partly filled band (metal); E_F~%.3f" % (p, q, n, n / 2, Ef))
        continue
    h = n // 2
    dg = E[:, h] - E[:, h - 1]; ig = E[:, h].min() - E[:, h - 1].max()
    k0 = KG[np.argmin(dg)]
    f = lambda k: (lambda e: e[h] - e[h - 1])(np.linalg.eigvalsh(bloch(phi, q, k[None, :])[0]))
    r = minimize(f, k0, method='Nelder-Mead', options={'xatol': 1e-11, 'fatol': 1e-14, 'maxiter': 3000})
    # dispersion at the minimum: linear (node) or quadratic?
    kk = r.x; e0 = r.fun
    slope = []
    for dvec in np.eye(3):
        e1 = f(kk + 1e-3 * dvec); e2 = f(kk + 2e-3 * dvec)
        slope.append(round(float(np.log(max(e2, 1e-15) / max(e1, 1e-15)) / np.log(2)), 2))
    print("  phi=2pi*%d/%d: %2d bands; half-filling direct gap grid %.4f -> refined %.2e at k=%s; indirect %.4f; "
          "growth exponent of the splitting near the minimum along x,y,z: %s" % (p, q, n, dg.min(), r.fun, np.round(kk, 4), ig, slope))

# (ii) band bottoms (empty vacuum, one charge), t = 1, coarse spacing 1
d = 1e-3
E0 = lambda k: -2 * np.cos(k).sum()
Epi = lambda k, m=0: -np.sqrt(4 * (np.cos(k) ** 2).sum() + m * m)
for name, fn in [('zero flux', E0), ('pi flux', Epi), ('pi flux, m=1', lambda k: Epi(k, 1.0))]:
    curv = [(fn(d * np.array(v)) - fn(0 * np.array(v))) / d ** 2 for v in [(1, 0, 0), (1, 1, 0) / np.sqrt(2), (1, 1, 1) / np.sqrt(3)]]
    print("(ii) %-13s bottom E=%.4f, E-E0 ~ k^2/(2 m*): m* = %s (isotropic)" % (name, fn(np.zeros(3)), [round(1 / (2 * c), 4) for c in curv]))
print("     formulas: zero flux m*=1/(2t); pi flux m*=sqrt(12t^2+m^2)/(4t^2) -> sqrt3/2 at m=0")

# (iii) mean-field CDW: 1 = (V z / 2) <1/E_k(Delta)>_BZ, E = sqrt(4 sum cos^2 k + Delta^2), z = 6
M = 160
g = (np.arange(M) + 0.5) * 2 * np.pi / M
c2 = np.cos(g) ** 2
S = (c2[:, None, None] + c2[None, :, None] + c2[None, None, :])
for Dl in [0.0, 0.5, 1.0]:
    I = np.mean(1 / np.sqrt(4 * S + Dl * Dl))
    print("(iii) Delta=%.1f: <1/E> = %.4f -> V needed = 2/(6 <1/E>) = %.4f t" % (Dl, I, 2 / (6 * I)))
print("done")
