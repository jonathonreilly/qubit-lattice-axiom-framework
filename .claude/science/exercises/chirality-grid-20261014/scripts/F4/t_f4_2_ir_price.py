# T-F4-2 arithmetic: infrared price of decoupling a gapless mirror without gapping it.
import math
hbar_c_eVm = 1.973269804e-7      # eV*m
l_P = 1.616255e-35               # m
M_Pl_eV = 1.220890e28            # eV (non-reduced Planck mass; a^-1 = M_Pl per scale_reference_primitive)
m_gamma = 1e-18                  # eV, PDG photon-mass upper bound (conservative reference)
lam = hbar_c_eVm / m_gamma       # m
n1 = lam / l_P                   # Planck lengths
print(f"1/m_gamma = {lam:.3e} m = {n1:.3e} Planck lengths (= M_Pl/m_gamma = {M_Pl_eV/m_gamma:.3e})")
print(f"z=1 (light-cone-limited NN recursion): L_min ~ {n1:.2e} layers per site")
for dt in (0.1, 0.25):
    print(f"z=2 (diffusive flow, step dt={dt}): L_min ~ {n1**2/dt:.2e} layers per site")
# softer reference scales for comparison
for name, ell in (("1 m lab", 1.0), ("1 km", 1e3), ("1 AU", 1.496e11)):
    print(f"  reference {name}: z=1 L_min ~ {ell/l_P:.2e}, z=2 ~ {(ell/l_P)**2:.2e}")
# single-barrier toy (layer phase between near photon and far Higgs): m_mirror ~ (t/g)^2 m_gamma^2 / M_Pl
for t, g in ((1.0, 0.3), (1.0, 1.0)):
    mm = (t/g)**2 * m_gamma**2 / M_Pl_eV
    print(f"barrier toy t={t}, g={g}: m_mirror <~ {mm:.2e} eV (needs > ~1e12 eV to evade direct searches)")
print("Reading: PRICE-PROHIBITIVE if L_min > 1e30 ->", "PROHIBITIVE" if n1 > 1e30 else "FINITE")
