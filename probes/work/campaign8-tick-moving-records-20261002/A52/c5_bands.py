"""A52 c5: free-fermion bands of the charges on the coarse cubic lattice (spacing 1, hopping t = 1)
with light in the zero-flux and pi-flux sectors (flux defined by the decorated loop operator, c3b)."""
import signal, itertools
signal.alarm(100)
import numpy as np

# zero flux
ks = np.linspace(-np.pi, np.pi, 61)
K = np.array(list(itertools.product(ks, ks, ks)))
E0 = -2 * np.cos(K).sum(axis=1)
print("zero flux: one band, E in [%.3f, %.3f]; bottom at k=0: E = -6 + k^2 (mass 1/2 in units hbar = t = a = 1)" % (E0.min(), E0.max()))
# curvature check at k = 0
d = 1e-3
print("   curvature at k=0 along x, (1,1,0)/sqrt2, (1,1,1)/sqrt3: %s" % [round((-2 * (np.cos(d * n).sum()) + 6) / d**2, 4) for n in [np.array([1, 0, 0]), np.array([1, 1, 0]) / np.sqrt(2), np.ones(3) / np.sqrt(3)]])

# pi flux: gauge u_x = 1, u_y = (-1)^x, u_z = (-1)^(x+y); magnetic cell 2 x 2 x 1 (sites (x mod 2, y mod 2))
sites = [(0, 0), (1, 0), (0, 1), (1, 1)]
sidx = {s: k for k, s in enumerate(sites)}
def Hk(k):
    """Bloch Hamiltonian with positions r = (x, y, z); magnetic cell vectors (2,0,0), (0,2,0), (0,0,1)."""
    H = np.zeros((4, 4), complex)
    for (x, y) in sites:
        a = sidx[(x, y)]; r = np.array([x, y, 0])
        for axis in range(3):
            e = np.zeros(3, int); e[axis] = 1
            u = 1 if axis == 0 else ((-1) ** x if axis == 1 else (-1) ** (x + y))
            r2 = r + e
            b = sidx[(r2[0] % 2, r2[1] % 2)]
            H[b, a] += -u * np.exp(1j * k @ e)
            H[a, b] += -u * np.exp(-1j * k @ e)
    return H
# plaquette fluxes of the gauge
def u(x, y, axis):
    return 1 if axis == 0 else ((-1) ** x if axis == 1 else (-1) ** (x + y))
fl = set()
for x, y in itertools.product(range(2), range(2)):
    fl.add(u(x, y, 0) * u(x + 1, y, 1) * u(x, y + 1, 0) * u(x, y, 1))          # xy
    fl.add(u(x, y, 0) * u(x + 1, y, 2) * u(x, y, 0) * u(x, y, 2))              # xz (u_x independent of z)
    fl.add(u(x, y, 1) * u(x, y + 1, 2) * u(x, y, 1) * u(x, y, 2))              # yz
print("pi flux: plaquette products of the gauge: %s" % fl)
km = np.linspace(-np.pi / 2, np.pi / 2, 41)   # magnetic zone: kx, ky in [-pi/2, pi/2), kz in [-pi, pi)
kz = np.linspace(-np.pi, np.pi, 81)
emin = np.inf; worst = 0.0
for kx in km:
    for ky in km:
        for kzz in kz:
            k = np.array([kx, ky, kzz])
            ev = np.linalg.eigvalsh(Hk(k))
            emin = min(emin, np.abs(ev).min())
            pred = 2 * np.sqrt(np.cos(kx) ** 2 + np.cos(ky) ** 2 + np.cos(kzz) ** 2)
            worst = max(worst, np.abs(np.sort(np.abs(ev)) - pred).max())
print("   bands: |E| = 2 sqrt(cos^2 kx + cos^2 ky + cos^2 kz) on the magnetic grid, max deviation %.1e" % worst)
# nodes: kx, ky = +-pi/2 (same point mod magnetic zone), kz = +-pi/2
for node in [np.array([np.pi / 2, np.pi / 2, np.pi / 2]), np.array([np.pi / 2, np.pi / 2, -np.pi / 2])]:
    ev = np.linalg.eigvalsh(Hk(node))
    sp = []
    for n in [np.array([1, 0, 0]), np.array([0, 0, 1]), np.array([1, 1, 0]) / np.sqrt(2), np.ones(3) / np.sqrt(3), np.array([1, -2, 3]) / np.sqrt(14)]:
        q = 1e-4
        e2 = np.linalg.eigvalsh(Hk(node + q * n))
        sp.append(round(e2.max() / q, 5))
    print("   node %s: energies %s (4-fold => one 4-component Dirac point); cone speeds along x, z, 110, 111, (1,-2,3): %s" % (
        np.round(node / np.pi, 2), np.round(ev, 12), sp))
print("   minimum |E| on the grid: %.2e; nodes per magnetic zone: 2 (KS doubling: 2 Dirac = 4 Weyl, 2 of each hand)" % emin)
print("done")
