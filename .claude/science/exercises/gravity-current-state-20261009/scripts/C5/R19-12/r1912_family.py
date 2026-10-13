"""R19-12 probe (b): charge-row inputs along the gravity root family (can the window's free direction pay a charge row?).
Points: the refined main root (vR18-9), R18-9's second root W2 (root4k_W2_N160.npy), the m = 0.001 root (root4c_m001_N192.npy),
and R18-9's window-model roots (model_root_{2.2,2.6,2.8}_1.0.npy; b_s = 3.0 is excluded there: r > 1/sqrt3).
For each: F_1/2(0+), F_0(0+) with its own photon gammaG_w(b_g, pi - b_g); G_1/2, G_0 at m = 0.005 (N = 192).
A charge row is paid for free only if one of the five natural cone values coincides with another:
  neutral 1 | photon 1 + u Sigma | classes 1 + u q^2 F_1/2 (q^2 = 1, 4/9, 1/9) ; Sigma = 8 G_1/2 (+ G_0 per charged complex scalar)."""
import os, time, numpy as np
from r1912_lib import *
A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'arch', 'R18-9')
t0 = time.time()
pts = [('main (refined, vR18-9)', ROOT['bs'], ROOT['bf'], ROOT['r'], ROOT['bg'])]
w2 = np.load(os.path.join(A, 'root4k_W2_N160.npy')); pts.append(('W2 (R18-9)', w2[0], w2[1], w2[2], w2[5]))
m1 = np.load(os.path.join(A, 'root4c_m001_N192.npy')); pts.append(('m=0.001 root', m1[0], m1[1], m1[2], m1[5]))
for bs in ('2.2', '2.6', '2.8'):
    x = np.load(os.path.join(A, 'model_root_%s_1.0.npy' % bs)); pts.append(('model b_s=%s' % bs, float(bs), x[1], x[2], x[0]))
N = 96
for lab, bs, bf, r, bg in pts:
    d, pr = photon_Gw(bg, np.pi - bg)
    Fd = F_dirac(bf, r, d, bg, N)[0]; Fs = F_scalar(bs, d, bg, N)[0]
    G12 = G_dirac(bf, r, 0.005, 192); G0 = G_scalar(bs, 0.005, 192)
    Sig = 8*G12
    print('%-24s b_s %.4f b_f %.6f r %.6f (r<1/sqrt3: %s) b_g %.5f | F12(0+) %+.4f F0(0+) %+.4f | G12 %+.5f G0 %+.5f | Sigma_SM=8G12 %+.4f | min |nat. gaps| %.3e  (%.0fs)'
          % (lab, bs, bf, r, r < 1/np.sqrt(3), bg, Fd, Fs, G12, G0, Sig,
             min(abs(Sig - q2*Fd) for q2 in (1, 4/9, 1/9)), time.time()-t0), flush=True)
print('elapsed %.1fs' % (time.time() - t0))
