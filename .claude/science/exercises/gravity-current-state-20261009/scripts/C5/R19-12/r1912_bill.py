"""R19-12 (a)+(c): charge rows on one law. Usage: python3 r1912_bill.py b_s b_f r b_g label
Natural O(e^2) cones (per u = alpha/4pi): neutral species 0 (no QED vertex), photon Sigma = sum_j n_j q_j^2 G_j,
charge class c: q_c^2 F_1/2(0+) (+ q_c^2 F' m a). SM QED content (R16-2 setting, vR16-2): 9 Dirac flavours on the one D1 edge,
sum n q^2 = 3*1 + 9*(4/9) + 9*(1/9) = 8 (colour counted in the photon loop); W+- excluded; charged-Higgs variant listed separately.
Masses at a = l_P (RECALLED, as R16-2 :84): m_e a 4.2e-23, m_tau a 1.46e-19, m_t a 1.41e-17, m_b a 3.4e-19 (4.18 GeV / 1.221e19 GeV)."""
import sys, time, numpy as np
from r1912_lib import *
bs, bf, r, bg = [float(x) for x in sys.argv[1:5]]; lab = sys.argv[5]
t0 = time.time(); u = u_phys
d, pr = photon_Gw(bg, np.pi - bg)
Fd = F_dirac(bf, r, d, bg, 128)[0]; Fd96 = F_dirac(bf, r, d, bg, 96)[0]
Fm = F_dirac(bf, r, d, bg, 128, m=0.005)[0]; Fp = (Fm - Fd)/0.005
Fs = F_scalar(bs, d, bg, 128)[0]
g1, g2 = G_dirac(bf, r, 0.0025, 192), G_dirac(bf, r, 0.005, 192); G12 = 2*g1 - g2; G12p = (g2 - g1)/0.0025
h1, h2 = G_scalar(bs, 0.0025, 192), G_scalar(bs, 0.005, 192); G0 = 2*h1 - h2
Sig = 8*G12; SigH = Sig + 1*G0
print('[%s] edges: G(b_s=%.6f), D1(b_f=%.6f, r=%.6f), photon gammaG_w(%.5f, fw=1); u = alpha/4pi = %.5e' % (lab, bs, bf, r, bg, u))
print('  F_1/2(0+) = %+.5f (N=128; N=96 %+.5f) ; dF/dm = %+.4f ; F_0(0+) = %+.5f' % (Fd, Fd96, Fp, Fs))
print('  G_1/2(0+) = %+.6f (dG/dm %+.4f) ; G_0(0+) = %+.6f ; Sigma_SM = 8 G_1/2 = %+.5f ; with one charged complex scalar: %+.5f' % (G12, G12p, G0, Sig, SigH))
print('  single-species split F - G (R16-1 convention) = %+.5f  -> x u = %+.4e' % (Fd - G12, u*(Fd - G12)))
print('  natural cones (x u): neutral 0 | photon %+.4e | e-class %+.4e | u-class %+.4e | d-class %+.4e | [phi+ %+.4e]'
      % (u*Sig, u*Fd, u*4/9*Fd, u*1/9*Fd, u*Fs))
for nm, q2 in (('e (q^2=1)', 1.0), ('u (q^2=4/9)', 4/9), ('d (q^2=1/9)', 1/9)):
    print('  split Delta_c(0+) = u(q^2 F - Sigma) [%s] = %+.4e ; to the neutral/graviton cone: kappa_c = %+.4e' % (nm, u*(q2*Fd - Sig), -u*q2*Fd))
print('  photon counterterm needed: kappa_gamma = -u Sigma = %+.4e (zero iff Sigma = 0)' % (-u*Sig))
mt, mtau, mb = 1.41e-17, 1.46e-19, 3.4e-19
print('  residuals with class counterterms set at m -> 0: top %.2e, tau %.2e, bottom %.2e ; photon from G mass slope (top loop) %.2e'
      % (abs(4/9*Fp*mt*u), abs(Fp*mtau*u), abs(1/9*Fp*mb*u), abs(3*4/9*G12p*mt*u)))
print('  comparators (RECALLED): eps* = 2.66e-19 (charged vs photon, R8-5) ; GW170817 ~1e-15 (graviton vs photon) ; SN1987A ~2e-9 (nu vs photon)')
print('elapsed %.1fs' % (time.time() - t0))
