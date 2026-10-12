"""R13-8 script E: tuning depth (decades) per coefficient = log10(natural one-loop size / bound).
Natural sizes and bounds are inputs with their sources (see report); arithmetic only."""
import math
a = 1/137.036; u = a/(4*math.pi)                    # e^2/16pi^2
rows = [
 ("c_e - c_g (F2, Z3xR naive/stagg.)", 8.55e-3, 2.66e-19, "F2 natural; 1.4 PeV photon survival (C4_F2_referee:29,62)"),
 ("c_T - c_g, QED part only (2 tastes x 0.671 e^2/16pi^2)", 2*0.671*u, 7e-16, "GW170817 upper side 7e-16 (C5_O1_referee:78)"),
 ("c_T - c_g, graviton part at a=l_P (R9-9 |dc_T| low end)", 1.3e-2, 7e-16, "R9-9 sizes (C5_R9-9_report:26)"),
 ("TT anisotropy, two-sided, GW170817 direction only", 1.3e-2, 7e-16, "natural ~ R9-9 scale (reading)"),
 ("TT anisotropy, one-sided Cherenkov (galactic CR)", 1.3e-2, 2e-15, "Moore-Nelson 2001 (web abstract)"),
 ("TT anisotropy, one-sided Cherenkov (extragalactic CR)", 1.3e-2, 2e-19, "Moore-Nelson 2001 (web abstract)"),
 ("TT mass^2 (P0 residual)", 1.0, 5.7e-99, "B_referee via PRICE_NOTE (P0)"),
 ("b0 tilde (R6-5 range)", 6.2e16, 1e-26, "R6-5 natural 6e16 GeV; Sun-frame b_T ~1e-26 GeV"),
 ("b0 tilde, boost route", 1.2e18, 1.1e-30, "R6-5 boost route (CMB frame assumed)"),
]
for name, nat, bnd, src in rows:
    print(f"{name:60s} natural {nat:9.2e}  bound {bnd:9.2e}  decades {math.log10(nat/bnd):6.1f}   [{src}]")
# tadpoles: Planck-cutoff vacuum vs rho_Lambda
MPl = 1.221e19; rhoL = 2.52e-47
rho_nat = 0.1*MPl**4
print(f"{'CC tadpole (Lorentz-invariant; 0.1 M_Pl^4 vs rho_L)':60s} natural {rho_nat:9.2e}  bound {rhoL:9.2e}  decades {math.log10(rho_nat/rhoL):6.1f}")
for f in (0.05, 0.1):
    print(f"{'LV tadpole rho+p, |1+w| < %.2f (RECALLED)' % f:60s} natural {rho_nat:9.2e}  bound {f*rhoL:9.2e}  decades {math.log10(rho_nat/(f*rhoL)):6.1f}")
# graviton mass check: GWTC-3 published vs arXiv
for mg in (1.27e-23, 2.42e-23):
    print(f"graviton mass {mg:.2e} eV -> m/M_Pl = {mg/(MPl*1e9):.2e}, (m/M_Pl)^2 = {(mg/(MPl*1e9))**2:.2e}")
