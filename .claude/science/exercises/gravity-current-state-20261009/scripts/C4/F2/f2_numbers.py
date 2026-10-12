"""F2: physical sizes and bound comparisons (arithmetic only; bounds are literature values quoted from memory,
COMPARATOR, not re-verified). Inputs from f2_ir.out / f2_ir_photon.out (m, lam -> 0 fits).
Usage: python f2_numbers.py"""
import numpy as np
dcf = -16.06          # fermion speed shift / (e^2/16pi^2), continuous-time Z^3, staggered = naive per taste
dcg_dirac = -0.671    # photon speed shift per Dirac taste / (e^2/16pi^2)
for ntaste, lab in [(1, "per-Dirac photon loop"), (2, "3D staggered field (2 tastes)"), (4, "4D staggered (4 tastes)")]:
    print(f"Delta_QED [{lab}] = dc_f - dc_gamma = {dcf - ntaste*dcg_dirac:+.2f} e^2/16pi^2")
D = dcf - 2 * dcg_dirac
me, mp = 0.51099895e6, 938.272e6  # eV
for alpha in (1/137.036, 1/128.0, 1/100.0):
    x = alpha / (4 * np.pi)
    d = D * x
    Eth = 2 * me / np.sqrt(2 * abs(d))
    print(f"alpha=1/{1/alpha:6.2f}: e^2/16pi^2={x:.3e}  c_e - c_gamma = {d:+.2e}  -> photon decay gamma->e+e- above {Eth/1e6:.1f} MeV")
Eg = 1.4e15
b_gdecay = 2 * me ** 2 / Eg ** 2
print(f"photon-decay bound from a 1.4 PeV photon (LHAASO 2021; comparator): c_gamma - c_e < 2 m_e^2/E^2 = {b_gdecay:.2e}")
print(f"required cancellation for e/gamma: {b_gdecay/abs(D/(137.036*4*np.pi)):.1e} of the natural one-loop size")
print(f"proton vacuum Cherenkov (c_p > c_gamma) at E = 1e20 eV: c_p - c_gamma < m_p^2/(2E^2) = {mp**2/(2*1e40):.1e}")
print(f"photon -> p pbar (c_gamma > c_p) at 1.4 PeV: c_gamma - c_p < 2 m_p^2/E^2 = {2*mp**2/Eg**2:.1e}")
print("GW170817 (comparator): -3e-15 < c_g - c_gamma < 7e-16")
MPl = 1.22e19  # GeV
for bound in (1e-15, 1e-20, 1e-22):
    Mstar = MPl * np.sqrt(16 * np.pi ** 2 * bound)
    print(f"Pospelov-Shang percolation (dc ~ (M*/M_Pl)^2/16pi^2) < {bound:.0e}  =>  M* < {Mstar:.1e} GeV  (= {Mstar/MPl:.1e} M_Pl)")
L = np.log(MPl / 0.511e-3)
print(f"Chadha-Nielsen-type log running, d(dc)/dln(mu) = b (alpha/pi) dc, from M_Pl to m_e: ln = {L:.1f}; "
      f"suppression factor = exp(-b*{L/(137.036*np.pi):.3f}) = {np.exp(-L/(137.036*np.pi)):.3f} for b = 1")
x = 1/137.036/(4*np.pi)
print(f"tadpole share: fermion tadpole -17.97 vs total -16.06 (e^2/16pi^2); at alpha=1/137: tadpole = {-17.97*x:.2e}")
