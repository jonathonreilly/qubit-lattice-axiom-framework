"""Optional check: single-particle pi-flux hopping on the cubic lattice
(Kogut-Susskind phases eta_x=1, eta_y=(-1)^x, eta_z=(-1)^(x+y): flux pi through
every plaquette), real nearest-neighbour hopping. Magnetic cell 2x2x1 (4 sites).
Count zero-energy points in the magnetic BZ and the number of bands touching."""
import numpy as np, itertools
sites = [(0, 0), (1, 0), (0, 1), (1, 1)]
idx = {s: i for i, s in enumerate(sites)}
def H(k):
    h = np.zeros((4, 4), complex)
    for (x, y) in sites:
        i = idx[(x, y)]
        for mu, d in ((0, (1, 0, 0)), (1, (0, 1, 0)), (2, (0, 0, 1))):
            eta = [1, (-1) ** x, (-1) ** (x + y)][mu]
            X, Y = x + d[0], y + d[1]
            j = idx[(X % 2, Y % 2)]
            R = np.array([X - X % 2, Y - Y % 2, d[2]])
            ph = np.exp(1j * np.dot(k, R))
            h[j, i] += eta * ph
            h[i, j] += eta * np.conj(ph)
    return h
# check flux: plaquette products
def eta(mu, x, y): return [1, (-1) ** x, (-1) ** (x + y)][mu]
for (a, b) in ((0, 1), (0, 2), (1, 2)):
    for x, y in itertools.product(range(2), repeat=2):
        v = [x, y, 0]; va = v.copy(); va[a] += 1; vb = v.copy(); vb[b] += 1
        prod = eta(a, *v[:2]) * eta(b, *va[:2]) * eta(a, *vb[:2]) * eta(b, *v[:2])
        assert prod == -1
print("flux pi on every plaquette: OK")
# spectrum E^2 = 4(cos^2 + ...) ? scan magnetic BZ kx,ky in [0,pi) (cell 2), kz in [0,2pi)
N = 48
zeros = []
for i, j, l in itertools.product(range(N), range(N), range(2 * N)):
    k = np.array([2 * np.pi * i / (2 * N) * 1.0, 2 * np.pi * j / (2 * N), 2 * np.pi * l / (2 * N)])
    k = np.array([np.pi * i / N, np.pi * j / N, np.pi * l / N])
    e = np.linalg.eigvalsh(H(k))
    if np.max(np.abs(e)) < 1e-9:
        zeros.append(tuple(np.round(k / np.pi, 3)))
print("k/pi where all 4 bands vanish (cell momenta kx,ky in [0,pi) after folding):", sorted(set((a % 1, b % 1, c % 2) for a, b, c in zeros)))
k0 = np.array([np.pi / 2, np.pi / 2, np.pi / 2])
for d in np.eye(3):
    e = np.linalg.eigvalsh(H(k0 + 1e-4 * d))
    print("dispersion near node along", d, ":", np.round(e / 1e-4, 4))
# analytic: E = +-2 sqrt(cos^2 kx + cos^2 ky + cos^2 kz) with lattice-momentum kx,ky
ks = np.random.rand(5, 3) * np.pi
for k in ks:
    e = np.sort(np.linalg.eigvalsh(H(k)))
    an = 2 * np.sqrt(np.sum(np.cos(k) ** 2))
    assert np.allclose(np.abs(e), an), (e, an)
print("E = +-2 sqrt(sum cos^2 k), each doubly degenerate: OK")
