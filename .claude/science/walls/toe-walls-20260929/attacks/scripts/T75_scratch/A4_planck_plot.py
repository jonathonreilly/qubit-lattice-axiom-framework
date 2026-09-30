"""Sharper diagnostic than the Frobenius residual: the 'Planck plot'.
For each eigenmode l of the segment's correlation matrix C (occupation nu_l, entanglement energy
eps_l = ln((1-nu_l)/nu_l)), compute the clock energy E_l = <l|H_w|l> for a framework clock H_w.
A thermal state at inverse temperature beta for H_w has eps_l = beta E_l (straight line through
the origin).  Only 'active' modes |eps| < 25 are used (the others are saturated at 0/1).
"""
import numpy as np
from A3_diamond import vacuum_C, tri, onsite_H

def planck(C, H, emax=25.0):
    nu, U = np.linalg.eigh(C)
    ok = (nu > 1e-13) & (nu < 1 - 1e-13)
    eps = np.log((1 - nu[ok]) / nu[ok]); Uo = U[:, ok]
    E = np.einsum("il,ij,jl->l", Uo, H, Uo)
    m = np.abs(eps) < emax
    eps, E = eps[m], E[m]
    # fit through origin (particle-hole symmetry of half filling), and R^2 of that fit
    beta = (eps @ E) / (E @ E)
    dev = eps - beta * E
    r2 = 1 - (dev @ dev) / (eps @ eps)
    return beta, r2, np.max(np.abs(dev)), len(eps), eps, E

if __name__ == "__main__":
    import json
    out = []
    print("Planck plot: eps_l = beta E_l  (through origin), active modes |eps|<25")
    print("  N  profile            beta/pi     R^2     max|dev|   n_modes")
    for N in (100, 200, 400, 800):
        C = vacuum_C(N)
        j = np.arange(1, N + 1, dtype=float)
        profiles = {}
        w = (j - 0.5) * (N + 0.5 - j) / N
        profiles["linear(half-site zero)"] = tri(np.sqrt(w[:-1] * w[1:]))
        w = j * (N - j + 1.0) / N
        profiles["linear(site zero)"] = tri(np.sqrt(w[:-1] * w[1:]))
        w2 = (N / 4.0) * (4 * (j - 0.5) * (N + 0.5 - j) / N**2) ** 2
        profiles["double zero"] = tri(np.sqrt(w2[:-1] * w2[1:]))
        profiles["on-site ramp"] = onsite_H(N, 1.0)
        for name, H in profiles.items():
            b, r2, md, n, eps, E = planck(C, H)
            print(f" {N:4d} {name:22s} {b/np.pi:8.4f} {r2:9.5f} {md:9.3f} {n:6d}")
            out.append(dict(N=N, profile=name, beta_over_pi=b/np.pi, r2=r2, maxdev=md, nmodes=n))
    json.dump(out, open("A4_results.json", "w"), indent=1)
    # show the actual central levels for N=400 linear profile
    N = 400; C = vacuum_C(N); j = np.arange(1, N + 1, dtype=float)
    w = (j - 0.5) * (N + 0.5 - j) / N
    b, r2, md, n, eps, E = planck(C, tri(np.sqrt(w[:-1] * w[1:])))
    idx = np.argsort(np.abs(eps))[:10]
    print("\nN=400 linear clock, ten lowest |eps| levels: eps, E, eps/(pi E)")
    for k in idx: print(f"  {eps[k]:9.4f} {E[k]:9.4f} {eps[k]/(np.pi*E[k]):8.4f}")
