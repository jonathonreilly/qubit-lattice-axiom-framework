import sys; sys.path.insert(0, '.')
import numpy as np
from r161_laws import BQLaw
from r131_photon_sqed import selectron
from r131_electron_sqed import dc_partner
from r161_partner_gl import selectron_gl, dc_partner_gl
U = 16 * np.pi ** 2
N = 32; mid = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi; w = np.full(N, 2 * np.pi / N)
law = BQLaw(2.0, 3.0, 1.0, 0.4, 'naive')
a, _ = selectron(law, N); b, _ = selectron_gl(law, mid, w, mid, w, Nref=N)
print('selectron dc_gamma*U: R13-1 %+.10f  GL-code on midpoint nodes %+.10f' % (a * U, b * U))
law.m = 0.4
a = dc_partner(law, N); b = dc_partner_gl(law, mid, w, mid, w)
print('partner dc_e*U (h=0.02 both since m/8 = 0.05 > 0.02): R13-1 %+.10f  GL-code %+.10f' % (a * U, b * U))
