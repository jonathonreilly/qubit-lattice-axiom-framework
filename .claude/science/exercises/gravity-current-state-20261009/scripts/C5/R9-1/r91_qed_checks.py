"""C5 R9-1: arithmetic for (i) 7 charged mass-m_e copies (profile L under G-out, Dirac sea): Z width, a_e, alpha(MZ);
(ii) electron free-fall weight under G-out from R8-5's (unrefereed) delta c_e via O2 Lemma F (beta = c^2);
(iii) BK18 inflation bound on T_max.  Formulas RECALLED (standard QED/cosmology); inputs labelled in the report."""
import math
out = []
def pr(s): print(s); out.append(s)
al = 1/137.035999
A2vp = 119/36 - math.pi**2/3            # same-mass vacuum-polarization coefficient of a_e at (alpha/pi)^2 (RECALLED)
pr('A2 VP same-mass coefficient = %.6f ; 7 copies: delta a_e = %.3e ; exp. sigma 1.3e-13 (Fan et al. 2023) -> %.2e sigma'
   % (A2vp, 7*A2vp*(al/math.pi)**2, 7*A2vp*(al/math.pi)**2/1.3e-13))
MZ = 91.1876; me = 0.000510999
dal = al/(3*math.pi)*(math.log(MZ**2/me**2) - 5/3)
pr('Delta alpha per e-copy at MZ = %.4f ; 7 copies = %.4f ; alpha^-1(MZ) -> %.1f (SM ~128.95, RECALLED)' % (dal, 7*dal, 1/al*(1-0.0590-7*dal)))
pr('Gamma_Z extra = 7*83.91 MeV = %.0f MeV vs Gamma_Z = 2495.2 +- 2.3 MeV (PDG, RECALLED) -> %.0f sigma' % (7*83.91, 7*83.91/2.3))
for x in (5.6, 6.5, 13.3):
    dce = -x*4*math.pi*al/(16*math.pi**2)
    dZA = 22/47.867 - 78/195.08
    pr('dc_e*16pi^2=-%.1f: beta_e-1 = %.2e ; eta_TiPt (electron share only) ~ %.2e' % (x, 2*dce, dZA*5.4858e-4*abs(2*dce)))
As = 2.1e-9; r = 0.036; Mred = 2.435e18
V14 = (1.5*math.pi**2*As*r)**0.25*Mred
Trh = (30/(math.pi**2*106.75))**0.25*V14
H = math.pi*Mred*math.sqrt(As*r/2)
pr('V^1/4 < %.3g GeV ; T_RH(instant) < %.3g GeV ; H_inf < %.3g GeV' % (V14, Trh, H))
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out) + '\n')
