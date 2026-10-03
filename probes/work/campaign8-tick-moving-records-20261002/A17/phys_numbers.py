"""A17 check C4: physical arithmetic (identification ARGUED: one tick = t_P, spacing = l_P, toy mass phase =
rest energy, pace N = 1 + Phi/c^2).  Comparator experiment values are FROM MEMORY, UNVERIFIED.

Dephasing for branches far apart (Dx >> R):   -ln V = (Mc^2/hbar)^2 * t * S_N   (S_N in seconds)
Per-site Bernoulli pace (A13 3D event rate p = s u (1-u), s = 0.3188):  S_site = (1-p)/p ticks.
Ball-averaged diffusive-carrier pace (kappa = 1/12):  S_ball(R) = [2(1-u)/(u kappa)] * 1.2/(4 pi R) ticks (R in sites).
Ballistic carriers (speed v = 1 site/tick, isotropic, continuum):  S_ball(R) = 9/(8 pi u v R^2) ticks.
"""
import numpy as np

hbar, c, G = 1.054571817e-34, 2.99792458e8, 6.67430e-11
tP, lP, mP = 5.391247e-44, 1.616255e-35, 2.176434e-8
amu, me, mn = 1.66053907e-27, 9.1093837e-31, 1.67492750e-27
s, kap = 0.3188, 1.0 / 12


def rate(M):
    return M * c ** 2 / hbar


print("(a) A13 baseline, per-site Poisson pace with tau_e = t_P:  t_coh = hbar^2/(tau_e M^2 c^4)")
objs = [("electron", me), ("neutron", mn), ("Rb-87", 86.909 * amu), ("100 amu", 100 * amu), ("Cs-133", 132.905 * amu),
        ("25 kDa molecule", 25000 * amu)]
for nm, M in objs:
    print(f"   {nm:16s} Mc^2/hbar = {rate(M):.3e} /s   t_coh = {1/(rate(M)**2*tP):.3e} s   (m = M/m_P = {M/mP:.2e})")

print("\n(b) per-site pace at carrier density u (S_site = (1-p)/p ticks, p = s u(1-u)):")
for u in (0.5, 0.05, 1e-6):
    p = s * u * (1 - u); S = (1 - p) / p
    tc100 = 1 / (rate(100 * amu) ** 2 * S * tP); tc25k = 1 / (rate(25000 * amu) ** 2 * S * tP)
    esc = rate(me) ** 2 * S * tP
    print(f"   u={u:7.1e}: p={p:.3e}, S_site={S:.3e} ticks; t_coh(100 amu)={tc100:.2e} s, t_coh(25 kDa)={tc25k:.2e} s;"
          f" electron within-branch scrambling rate = {esc:.2e} /s")

print("\n(c) comparator demands (from memory, unverified): S_max = 1/((Mc^2/hbar)^2 t_obs), in ticks")
comps = [("neutron, 50 us", mn, 50e-6), ("Rb-87, 2 s", 86.909 * amu, 2.0), ("25 kDa, 10 ms", 25000 * amu, 10e-3)]
Smax = {}
for nm, M, t in comps:
    Smax[nm] = 1 / (rate(M) ** 2 * t) / tP
    print(f"   {nm:15s}: S_max = {Smax[nm]:.2e} ticks  (suppression vs Poisson at one event per tick: {Smax[nm]:.1e})")

print("\n(d) required averaging radius R_min (sites; metres) for S_ball(R) <= S_max:")
print("   diffusive carriers, uniform ball (floor kernel is 1.2x better):")
for u in (0.5, 0.05, 1e-6):
    row = []
    for nm, M, t in comps:
        R = (2 * (1 - u) / (u * kap)) * 1.2 / (4 * np.pi * Smax[nm])
        row.append(f"{nm}: {max(R,1):.1e} ({max(R,1)*lP:.1e} m)")
    print(f"   u={u:7.1e}:  " + ";  ".join(row))
print("   ballistic carriers (v = 1), uniform ball:")
for u in (0.5, 1e-6):
    row = []
    for nm, M, t in comps:
        R = np.sqrt(9 / (8 * np.pi * u * Smax[nm]))
        row.append(f"{nm}: {max(R,1):.1e} ({max(R,1)*lP:.1e} m)")
    print(f"   u={u:7.1e}:  " + ";  ".join(row))

print("\n(e) long-time cross-correlation of the pace at r >> R: C_Phi(r) = A * hbar G / r with A = 2(1-u)/(4 pi u kappa)")
for u in (0.5, 0.05, 1e-6):
    print(f"   u={u:7.1e}: A = {2*(1-u)/(4*np.pi*u*kap):.3e}")
print("   check c^4 t_P l_P / (hbar G) =", f"{c**4*tP*lP/(hbar*G):.6f}")
for r in (1e-9, 1e-6):
    print(f"   diffusive correlation build-up time at r = {r:.0e} m: r^2/(6 kappa) ticks = {(r/lP)**2/(6*kap)*tP:.2e} s")

print("\n(f) grid-scale tail of a sharp-ball kernel: scrambling into grid-scale states ~ (Mc^2/hbar)^2 t_P S_site * 9/R^4")
u = 0.5; p = s * u * (1 - u); S = (1 - p) / p
for nm, M, bound in [("electron", me, 4.8e-37), ("nucleon (as elementary)", mn, 3e-42)]:
    r0 = rate(M) ** 2 * tP * S
    Rmin = (9 * r0 / bound) ** 0.25
    print(f"   {nm:24s}: per-site rate {r0:.2e} /s; rate bound {bound:.0e} /s (from memory) -> R >~ {Rmin:.1e} sites"
          f" ({Rmin*lP:.1e} m)")
print("\n(g) suppression of slow (diffusive) pace noise for particle dynamics at wavevector q: (2 kappa M/m_P)^2")
for nm, M in [("electron", me), ("nucleon", mn), ("25 kDa", 25000 * amu)]:
    print(f"   {nm:8s}: {(2*kap*M/mP)**2:.1e}")
