"""C3: magnitudes. All energies in eV. O(1) normalisation factors flagged.

m_g^2 = 8 mu / M^2 with mu the TT energy density per unit h^2 (Fierz-Pauli normalisation of
L = (M^2/8)(hdot^2 - m^2 h^2)); mu = c2 e^2 a^-4 per cell (K3a'' convention up to O(1)).
"""
import math
M_Pl = 1.22089e28          # eV, non-reduced (scale-reference primitive: a^-1 = M_Pl)
M = 2.435e27               # eV, reduced Planck mass (8 pi G)^-1/2
H0 = 67.4 * 1e3 / 3.0857e22 * 6.582e-16   # eV
OmL = 0.685
rho_L = 3 * OmL * H0**2 * M**2            # eV^4
mg_LVK = 1.27e-23          # eV, GWTC-3 dispersion bound (90%) -- comparator from memory
c2e2 = 1.2e-3              # per cell at alpha = 1/137 (TEST_LOG.md:393)
free_part = 0.3            # O(1) free-level part if NOT tuned (TEST_LOG.md:400: +0.267/+0.592)

print(f"H0 = {H0:.3e} eV; rho_Lambda = {rho_L:.3e} eV^4 = ({rho_L**0.25*1e3:.2f} meV)^4")
cc_cell = rho_L / M_Pl**4
print(f"CC bar per Planck cell (a^-1 = M_Pl):            rho_L * a^4      = {cc_cell:.2e}")
mu_bar_cell = mg_LVK**2 * M**2 / 8 / M_Pl**4
print(f"TT bar per Planck cell from LVK m_g bound:        m_g^2 M^2/8 a^4  = {mu_bar_cell:.2e}")
print(f"  => the TT bar is weaker than the CC bar by ~10^{math.log10(mu_bar_cell/cc_cell):.0f}")
print(f"  K3a'' O(e^2) value {c2e2:.1e} overshoots the TT bar by ~10^{math.log10(c2e2/mu_bar_cell):.0f}")
# framework's own (conditional) Hubble-scale identity m_g^2 = 2 Lambda (GRAVITON_MASS_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md:30-31)
mg_own = math.sqrt(6) * H0
mu_own_cell = mg_own**2 * M**2 / 8 / M_Pl**4
print(f"If the landed conditional identity m_g = sqrt6 H0 = {mg_own:.2e} eV is the target: TT bar per cell = {mu_own_cell:.2e}"
      f" (CC bar {cc_cell:.2e}; ratio {mu_own_cell/cc_cell:.1f})")

print("\nP2: lattice cutoff Lambda = a^-1 free, M independent of the lattice (not induced):")
for mu in (c2e2, free_part):
    Lmax = (mg_LVK**2 * M**2 / (8 * mu))**0.25
    print(f"  mu = {mu:.1e}: need Lambda < {Lmax:.0f} eV  (electron mass 5.11e5 eV; LHC ~1e13 eV)")
print("P2: M induced by the same lattice (Sakharov, M^2 ~ N Lambda^2/(48 pi^2), N ~ 100):")
for mu in (c2e2,):
    ratio = math.sqrt(8 * mu * 48 * math.pi**2 / 100)
    print(f"  m_g ~ {ratio:.2f} Lambda for every Lambda: need Lambda < {mg_LVK/ratio:.1e} eV")

print("\nTarget strength: 'massless' vs 'm_g < 1.27e-23 eV': the required suppression of mu is"
      f" {mu_bar_cell:.1e} per cell in the second case, i.e. the tuning is ~10^{-math.log10(mu_bar_cell/c2e2):.0f}"
      " either way.")
# group-velocity check: massive graviton at LIGO frequency
f = 100.0; E_gw = 2 * math.pi * f * 6.582e-16
print(f"  speed defect at 100 Hz for m_g at the bound: {0.5*(mg_LVK/E_gw)**2:.1e} (GW170817 bar ~1e-15)")
print("\nSUSY-type sea cancellation broken at 1 TeV (scaling estimate, suggested): residual per cell ~ (TeV/M_Pl)^4 ="
      f" {(1e12/M_Pl)**4:.1e}; misses TT bar by ~10^{math.log10((1e12/M_Pl)**4/mu_bar_cell):.0f},"
      f" CC bar by ~10^{math.log10((1e12/M_Pl)**4/cc_cell):.0f}")
