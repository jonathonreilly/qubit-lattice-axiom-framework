"""A30 q4_horizon: when is a jam inside its own horizon? (COMPARATOR arithmetic, constants
from memory).  A jam = ball of radius R with one record per grid cell (spacing a), each
carrying mass-energy m c^2.  GR comparator: inside its horizon when 2GM/(R c^2) >= 1.
  C(R) = 2 G M / (R c^2) = (8 pi / 3) G m R^2 / (a^3 c^2)
  R_h  = sqrt(3 a^3 c^2 / (8 pi G m))  ;  with a = l_P:  R_h = l_P sqrt(3 m_P / (8 pi m))
Also Hawking temperature and lifetime of the corresponding mass (COMPARATOR).
"""
import numpy as np

G = 6.674e-11; c = 2.998e8; hbar = 1.0546e-34; kB = 1.381e-23
mP = np.sqrt(hbar * c / G); lP = np.sqrt(hbar * G / c ** 3); tP = lP / c
m_p = 1.6726e-27; m_e = 9.109e-31
print(f"Planck: m_P={mP:.4e} kg, l_P={lP:.4e} m, t_P={tP:.4e} s, E_P={mP*c**2:.4e} J")
cases = [("electron mass per site", m_e), ("nucleon mass per site", m_p),
         ("Planck mass per site", mP), ("(pi/2) E_P per site (A24 sharp-record depth)", np.pi / 2 * mP)]
a = lP
for name, m in cases:
    Rh = np.sqrt(3 * a ** 3 * c ** 2 / (8 * np.pi * G * m))
    Nh = 4 * np.pi / 3 * (Rh / a) ** 3
    Mh = Nh * m
    rs = 2 * G * Mh / c ** 2
    TH = hbar * c ** 3 / (8 * np.pi * G * Mh * kB)
    tev = 5120 * np.pi * G ** 2 * Mh ** 3 / (hbar * c ** 4)
    rho = m / a ** 3
    print(f"\n{name}: m={m:.4e} kg, density {rho:.3e} kg/m^3")
    print(f"  R_h = {Rh:.4e} m = {Rh/lP:.4e} l_P ; check l_P*sqrt(3 m_P/(8 pi m)) = {lP*np.sqrt(3*mP/(8*np.pi*m)):.4e}")
    print(f"  N_h = {Nh:.4e} sites, M_h = {Mh:.4e} kg, r_s(M_h) = {rs:.4e} m (= R_h)")
    print(f"  Hawking (COMPARATOR) for M_h: T_H = {TH:.4e} K, lifetime ~ {tev:.4e} s")
print("\nScalings: R_h ~ a^(3/2) m^(-1/2); M_h ~ a^(3/2) m^(-1/2) c^3/G^(3/2)... i.e. M_h = (4pi/3)(3/(8pi))^(3/2) m_P^(3/2) m^(-1/2) at a=l_P")
print("prefactor (4pi/3)(3/(8pi))^(3/2) =", 4 * np.pi / 3 * (3 / (8 * np.pi)) ** 1.5)
for name, Mkg in [("Earth", 5.97e24), ("Sun", 1.989e30)]:
    R = (3 * Mkg / (4 * np.pi * (m_p / lP ** 3))) ** (1 / 3)
    print(f"{name}-mass jam at nucleon/site density: R = {R:.3e} m vs r_s = {2*G*Mkg/c**2:.3e} m -> C = {2*G*Mkg/(R*c**2):.3e}")
print("\nLinear field route at the jam (uniform ball): U_surface = C/2, U_centre = 3C/4; lapse N = 1 - U")
for C in [1e-6, 0.1, 0.5, 1.0]:
    print(f"  C={C:7.1e}: N_surface={1-C/2:.4f}, N_centre={1-0.75*C:.4f}  (GR exterior at R: sqrt(1-C)={np.sqrt(max(1-C,0)):.4f})")
