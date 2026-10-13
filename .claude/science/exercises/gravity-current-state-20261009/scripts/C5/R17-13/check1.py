"""R17-13 check1: independent mu_T2^F (form P and IBP form I, two resolutions) vs archived dfam.evaluate (R16-13/R17-9 'ferm')."""
import sys, time, numpy as np
sys.path.insert(0, sys.argv[1]); sys.path.insert(0, '.')
import lib13 as L
from content3 import ferm
cases = [(1.4, 0.3, 0.01, 'R16-13 table / referee -1.15955e-6'), (1.4, 0.3, 0.3, 'R16-13 table +4.4e-7'),
         (1.4, 1/np.sqrt(3), 0.01, 'R16-13 table -1.28e-5'), (1.313474886012, 0.572783392213, 0.01, 'vR16-13 retuned root, -3.52766e-5'),
         (0.38483254, 0.55962727, 0.01, 'R17-9 VM root: total +0.106083/22.5 = +4.7148e-3')]
for b, r, m, note in cases:
    t0 = time.time(); law = L.D1law(b, r)
    P1 = L.muT2(law, m, 4, 12); P2 = L.muT2(law, m, 8, 16); I2 = L.muT2(law, m, 8, 16, form='I')
    arch = ferm(b, r, m)[0][3]
    print('D1(%.6f,%.6f) m=%g: P(4x12) %+.10e  P(8x16) %+.10e  I(8x16) %+.10e | archived dfam %+.6e | %s (%.0fs)' % (b, r, m, P1, P2, I2, arch, note, time.time()-t0), flush=True)
