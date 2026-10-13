"""R19-12: the photon shift Sigma = 8 G_1/2 (SM Dirac content, Lemma Q) along R18-9's window-model gravity family
(rows copied from P/scripts/C5/R18-9/window_model.out, model-interpolated N=160 photon nodes; R18-9 sec. 3.6),
plus the directly solved roots (main refined vR18-9; W2). G_1/2 at m = 0.0025 and 0.005 (N = 192), linear m -> 0 extrapolation.
Also G_0 of the family's scalar edge (for the charged-Higgs variant Sigma' = 8 G_1/2 + G_0)."""
import time, numpy as np
from r1912_lib import *
t0 = time.time()
fam = [  # (b_s, fr, b_g*, b_f, r)  window_model.out
 (2.90, 1.00, 2.94688, 0.94281, 0.57390), (2.80, 1.00, 2.94600, 0.93327, 0.56859), (2.60, 1.00, 2.94434, 0.91550, 0.55898),
 (2.40, 1.00, 2.94284, 0.89942, 0.55058), (2.20, 1.00, 2.94148, 0.88492, 0.54323), (2.00, 1.00, 2.94026, 0.87191, 0.53681),
 (1.50, 1.00, 2.93781, 0.84532, 0.52418), (1.00, 1.00, 2.93613, 0.82590, 0.51534), (1.00, 0.02, 2.94159, 0.79041, 0.49995),
 (0.50, 0.02, 2.94501, 0.79642, 0.50249)]
fam += [(ROOT['bs'], 1.0, 2.9435, ROOT['bf'], ROOT['r']), (1.53359542, 1.0, 2.9378, 0.84663498, 0.52479543)]
for bs, fr, bg, bf, r in fam:
    g1 = G_dirac(bf, r, 0.0025, 192); g2 = G_dirac(bf, r, 0.005, 192); G0 = 2*g1 - g2
    print('b_s %.4f fr %.2f b_g %.5f | b_f %.5f r %.5f | G12(0.0025) %+.5f G12(0+) %+.5f | Sigma_SM = 8G12 %+.4f  (%.0fs)'
          % (bs, fr, bg, bf, r, g1, G0, 8*G0, time.time()-t0), flush=True)
print('elapsed %.1fs' % (time.time() - t0))
