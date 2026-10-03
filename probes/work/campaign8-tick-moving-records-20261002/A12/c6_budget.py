"""C6: window needed on Planck ticks. Per-tick-per-site vacuum chance p = eps_w / T (windows tiled),
eps_w = exp(-c E T) (c = 1: closed-form Chebyshev, efficiency -> 1; c ~ 2: optimum at efficiency 1/2..0.9),
E = E_phys / E_P (radians per tick). Requirements: p <= 1/N_age (no freezing over the universe's age, A4);
p <= kappa / l^2 (A6 screening length >= l sites, kappa = 1/12) for l = 1 AU and l = Hubble length."""
import numpy as np
tP, lP, EP = 5.391e-44, 1.616e-35, 1.2209e28           # s, m, eV  (E_P = hbar / t_P)
Nage = 13.8e9 * 3.156e7 / tP
reqs = {"age (A4)": 1 / Nage, "1/r to 1 AU (A6)": (1 / 12) / (1.496e11 / lP) ** 2,
        "1/r to Hubble (A6)": (1 / 12) / (1.37e26 / lP) ** 2}
print(f"N_age = {Nage:.3e} ticks; per-tick bounds: " + ", ".join(f"{k}: {v:.2e}" for k, v in reqs.items()))
for name, Eev in (("1 GeV", 1e9), ("1 MeV", 1e6), ("1 eV (optical)", 1.0), ("CMB 6e-4 eV", 6e-4), ("1 ueV (radio)", 1e-6)):
    E = Eev / EP
    out = []
    for rname, pmax in reqs.items():
        for c in (1.0, 2.0):
            T = 100 / (c * E)
            for _ in range(50):                          # solve c E T = ln(1 / (T pmax))
                T = np.log(1 / (T * pmax)) / (c * E)
            out.append((rname, c, T))
    print(f"\n{name}: E = {E:.2e} rad/tick")
    for rname, c, T in out:
        print(f"   {rname:20s} c={c:.0f}: T = {T:.2e} ticks = {T*tP:.2e} s, reach {T*lP:.2e} m, "
              f"E*T = {c and E*T:.1f} rad = {E*T/(2*np.pi):.1f} periods, per-window eps_w = {np.exp(-c*E*T):.1e}")
