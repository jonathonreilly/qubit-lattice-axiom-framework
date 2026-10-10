# Dilemma arithmetic (suggested): KR/bilayer window vs TT response of the action variance.
# Inputs: G-A (refereed bound): Var S_BD >= (l/l_p)^4 (16/6) I_BD, I_BD = 0.0191 (L/l)^6, l_p^2 = 8 pi G.
#         smeared BD: prefactor (l/l_p)^2 (4/sqrt6) sqrt(eps), kernel E_eps(s) = eps E_1(s sqrt eps) -> Var ~ eps^{5/2}.
#         N1 (same family): long-baseline TT response of the second-chaos term = (I0(h)^{1/2}-1) ~ h^2/8.
#         S_kin = h^2 w^2 V / (64 pi G) with w = 2pi/L, V = L^4 (G-A's generous comparator).
import math
c = 4/math.sqrt(6); IBD = 0.0191
def R(phi_l, L_over_lk):
    # R = (h^2/8) Var / S_kin, eliminating l/l_p via phi_l = c (l/l_p)^2 eps^{3/2}
    # Var = (16/6) IBD (l/l_p)^4 eps^{5/2} (L/l)^6 ; S_kin = (pi/16) h^2 (L/sqrt G)^2 = (pi^2/2) h^2 (L/l_p)^2
    pref = (16/6)*IBD/8 / (math.pi**2/2) * (6/16) / (1/c)   # collects constants -> coefficient * phi_l * (L/l_k)^4
    return pref*phi_l*L_over_lk**4, pref
r, pref = R(1.0, 1.0)
print(f"R = {pref:.3e} * phi_l * (L/l_k)^4")
phi_min = 2*math.pi/3
print(f"with phi_l >= 2pi/3: R >= {pref*phi_min:.3e} (L/l_k)^4 ; R<=1 needs L <= {(1/(pref*phi_min))**0.25:.2f} l_k")
# cross-check against direct numbers: local BD, l/l_p = 1.2, L = 1e6 m, h = 1e-21
G = 6.674e-11*1.055e-34/(2.998e8)**3  # G hbar / c^3 = l_Planck^2 (m^2)
lp = math.sqrt(8*math.pi*G); l = 1.2*lp; L = 1e6; h = 1e-21
Var = (16/6)*IBD*(l/lp)**4*(L/l)**6
Skin = h**2*(2*math.pi/L)**2*L**4/(64*math.pi*G)
print(f"direct: Var >= {Var:.2e}, S_kin = {Skin:.2e} hbar, R = {(h*h/8)*Var/Skin:.2e}; formula: {pref*c*1.44*(L/l)**4:.2e}")
for name, lam in [("LIGO", 1e6), ("PTA", 1e16), ("CMB tensor", 1e25)]:
    print(f"{name:10s} L={lam:.0e} m: R<=1 needs l_k >= {lam*(pref*phi_min)**0.25:.1e} m (EH mean needs l_k << L)")
# propagation version: amplitude damping per cycle ~ R ; over D/lambda cycles (1 Gpc LIGO) need R <~ lambda/D
D = 3.086e25; lam = 1e6
print(f"1 Gpc propagation at lambda=1e6 m: R <~ {lam/D:.1e} -> l_k >= {lam*(pref*phi_min*D/lam)**0.25:.1e} m")
