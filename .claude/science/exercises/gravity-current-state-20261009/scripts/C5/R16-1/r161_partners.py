"""R16-1 (d): Q_W^P. R13-1's (refereed-as-numbers) partner legs, unmodified, on D1(1.4, 1/sqrt3) (naive photon, so the
photino is R13-1's Majorana-Wilson one with Sg = sin q): (i) two matched selectrons' photon coefficient
(r131_photon_sqed.selectron); (ii) the selectron-photino (Yukawa y^2 = 2e^2) loop in dc_e (r131_electron_sqed.dc_partner).
Question: do the partners change the LINEAR-in-m coefficient L of dc_e (Theorem W)?  Uniform N^3 grids (R13-1's runners):
the D1 slab is under-resolved, so only the m-scaling is read, not the values."""
import sys, time; sys.path.insert(0, '.')
import numpy as np
from r161_laws import D1Law, BQLaw
from r131_photon_sqed import selectron
from r131_electron_sqed import dc_partner
U = 16 * np.pi ** 2; t0 = time.time()
for lab, mk in (('D1(1.4,1/sqrt3) naive', lambda m: D1Law(1.4, 1 / np.sqrt(3), m)),
                ('BQ S3 r=1 naive photon', lambda m: BQLaw(2.0, 3.0, 1.0, m, 'naive'))):
    for N in (32, 48):
        for m in (0.4, 1.6, 6.4, 25.6, 102.4):
            law = mk(m)
            dS, _ = selectron(law, N)
            pa = 2.0 * dc_partner(law, N)
            print('%-24s N=%2d m=%7.2f: 2 selectrons dc_gamma*U = %+.5e (x m^2: %+.4f) | partner-loop dc_e*U = %+.5f (/m: %+.2e)  [%.0fs]'
                  % (lab, N, m, 2 * dS * U, 2 * dS * U * m * m, pa * U, pa * U / m, time.time() - t0), flush=True)
