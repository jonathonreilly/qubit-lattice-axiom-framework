"""B1 check c1: what the graviton-mass bound demands of the vacuum's TT (shear) modulus,
and how that compares with the cosmological constant.

Normalisation (GR, reduced Planck mass M): S_TT = (M^2/8) int (hdot^2 - (grad h)^2) - (1/2) int mu h_ij h_ij
=> m_g^2 = 4 mu / M^2  (same as kill_F1a referee item 4).
Inputs (comparator values, quoted from memory, not re-fetched):
  m_g <= 1.27e-23 eV (GWTC-3, 90% CL); Planck 2018: H0 = 67.36 km/s/Mpc, Omega_L = 0.6847.
"""
import math
hbar_eVs = 6.582119569e-16
hbarc_eVm = 1.973269804e-7
M_red = 2.435e27      # reduced Planck mass, eV
M_Pl = 1.220890e28    # Planck mass, eV
m_g = 1.27e-23        # eV

mu_max = m_g**2 * M_red**2 / 4.0
print(f"mu_max = m_g^2 M^2/4 = {mu_max:.3e} eV^4 = ({mu_max**0.25:.1f} eV)^4")
print(f"  in reduced-Planck units mu/M^4 = {mu_max/M_red**4:.3e}")
print(f"  per Planck cell (l_P = 1/M_Pl):  mu/M_Pl^4 = {mu_max/M_Pl**4:.3e}")

H0 = 67.36 * 1e3 / 3.0857e22          # s^-1
H0_eV = H0 * hbar_eVs
rho_crit = 3 * H0_eV**2 * M_red**2
rho_L = 0.6847 * rho_crit
print(f"rho_Lambda = {rho_L:.3e} eV^4 = ({rho_L**0.25*1e3:.3f} meV)^4 ; rho_L/M_Pl^4 = {rho_L/M_Pl**4:.3e}")
print(f"ratio mu_max / rho_Lambda = {mu_max/rho_L:.3e}  (shear bar is this much looser than the CC bar)")

print("\nRequired suppression of the vacuum TT modulus, mu/Lambda_c^4, if natural size is Lambda_c^4:")
for name, Lc in [("2 TeV (1e-19 m bar)", hbarc_eVm/1e-19), ("10 TeV", 1e13), ("1e16 GeV", 1e25), ("M_Pl", M_Pl)]:
    print(f"  Lambda_c = {name:22s} {Lc:.3e} eV : mu/Lambda_c^4 <= {mu_max/Lc**4:.3e}")

print("\nUnprotected solid substrate: mu = c * a^-4. Largest allowed cutoff a^-1:")
for c, lab in [(1.2e-3, "K3a'' O(e^2) at alpha=1/137"), (0.27, "free-level natural coupling (K3a)"), (1.0, "O(1)")]:
    ainv = (mu_max / c) ** 0.25
    print(f"  c = {c:<8g} ({lab}): a^-1 <= {ainv:.0f} eV  (a >= {hbarc_eVm/ainv:.2e} m)")

print("\nInduced m_g for an unprotected solid at a = l_P (a^-1 = M_Pl):")
for c in [1.2e-3, 0.27]:
    mg = math.sqrt(4 * c * M_Pl**4 / M_red**2)
    print(f"  c = {c:g}: m_g = {mg:.2e} eV  = {mg/m_g:.1e} x bound")
