"""A30 q1_graded: 1D graded capture layer in front of a recorded wall (supplied toy).

Idealization of a porous jam surface seen at normal incidence (effective medium): capture
rate Gam_j on the last L unrecorded sites, rising toward the wall,
  Gam_j = Gmax * ((L + 1 - j) / L)**p,  j = 1..L  (site 1 touches the wall).
Rate model, exact transfer matrix.  Reports the band window where the layer is near-black,
and the slow-wave threshold law A ~ c k (which no finite layer escapes).
"""
import signal
import numpy as np

signal.alarm(55)
t = 1.0


def refl(k, gam):
    """Vectorized in k. Exact for the half chain with psi_0 = 0 and capture rates gam on sites 1..L."""
    k = np.atleast_1d(np.asarray(k, dtype=float))
    E = -2 * t * np.cos(k)
    L = len(gam)
    psi_prev = np.zeros_like(k, dtype=complex)
    psi = np.ones_like(k, dtype=complex)
    for jj in range(1, L + 1):
        V = -0.5j * gam[jj - 1]
        psi_next = ((V - E) * psi - t * psi_prev) / t
        psi_prev, psi = psi, psi_next
    # now psi_prev = psi_L, psi = psi_{L+1}
    z = np.exp(1j * k)
    det = z ** (-L) * z ** (L + 1) - z ** L * z ** (-L - 1)
    A = (psi_prev * z ** (L + 1) - z ** L * psi) / det
    B = (z ** (-L) * psi - z ** (-L - 1) * psi_prev) / det
    out = B / A
    return out if out.size > 1 else out[0]


# self-check against the single-site closed form R = -(t + V e^{-ik})/(t + V e^{ik})
_k = np.linspace(0.1, 3.0, 7)
_V = -0.5j * 2.0
assert np.max(np.abs(refl(_k, [2.0]) + (t + _V * np.exp(-1j * _k)) / (t + _V * np.exp(1j * _k)))) < 1e-12


ks = np.linspace(0.002, np.pi - 0.002, 1500)
print("single surface site, Gam=2: k-window with A>0.99:", end=" ")
A1 = 1 - np.abs(refl(ks, [2.0])) ** 2
w = ks[A1 > 0.99]
print(f"[{w.min():.3f},{w.max():.3f}]  fraction of band (in k) = {len(w)/len(ks):.3f}")

print("\n L   p  Gmax_best  k-window(A>0.99)    band frac  A>0.9 frac   A(k=0.05)  A(k=0.01)/0.01")
for L in [2, 4, 8, 16, 32, 64]:
    for p in [1, 2]:
        best = None
        for Gmax in np.geomspace(0.05, 8.0, 60):
            gam = Gmax * ((L + 1 - np.arange(1, L + 1)) / L) ** p
            A = 1 - np.abs(refl(ks[::5], gam)) ** 2
            frac = np.mean(A > 0.99)
            if best is None or frac > best[0]:
                best = (frac, Gmax)
        Gmax = best[1]
        gam = Gmax * ((L + 1 - np.arange(1, L + 1)) / L) ** p
        A = 1 - np.abs(refl(ks, gam)) ** 2
        w = ks[A > 0.99]
        win = f"[{w.min():.3f},{w.max():.3f}]" if len(w) else "none"
        a05 = 1 - abs(refl(0.05, gam)) ** 2
        a01 = 1 - abs(refl(0.01, gam)) ** 2
        print(f"{L:3d}  {p}  {Gmax:8.3f}   {win:18s}  {np.mean(A>0.99):.3f}      {np.mean(A>0.9):.3f}     {a05:.4f}    {a01/0.01:.3f}")

print("\nlower window edge k_min(A>0.99) times L (p=2, best Gmax): checks k_min ~ c/L")
for L in [8, 16, 32, 64, 128]:
    best = None
    for Gmax in np.geomspace(0.05, 8.0, 40):
        gam = Gmax * ((L + 1 - np.arange(1, L + 1)) / L) ** 2
        A = 1 - np.abs(refl(ks[::3], gam)) ** 2
        frac = np.mean(A > 0.99)
        if best is None or frac > best[0]:
            best = (frac, Gmax)
    gam = best[1] * ((L + 1 - np.arange(1, L + 1)) / L) ** 2
    A = 1 - np.abs(refl(ks, gam)) ** 2
    w = ks[A > 0.99]
    print(f"L={L:4d}: Gmax={best[1]:.3f}  k_min={w.min():.4f}  k_min*L={w.min()*L:.2f}  k_max={w.max():.4f}  pi-k_max={np.pi-w.max():.4f}")
