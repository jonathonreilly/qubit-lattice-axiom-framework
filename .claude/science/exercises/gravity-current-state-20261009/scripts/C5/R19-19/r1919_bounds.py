"""R19-19 (b),(d): (1) Lemma G applied to the checked NN/U rows (which rows are Ward violations);
(2) size of the O(p^4) remainder left by (S**) against GW170817 and a Fermi-LAT-type quadratic bound (RECALLED comparators).
Inputs: r1919_taylor.out (checked here), R9-9 normalization c^2 - 1 = (2/M^2) X with 2/M^2 = 16 pi at a = l_P
(C5_R9-9_report.md:186, C5_R16-3_report.md:276)."""
import numpy as np
# (1) checked rows, NN scalar, U vertex (E1), from r1919_taylor.out
rows = {1.0: (-6.883236565e-05, -2.289166114e-04, -1.245452929e-04, -2.289166108e-04),
        0.5: (-1.053446437e-04, -3.246914074e-04, -1.870877215e-04, -3.246914054e-04),
        0.3: (-1.185998667e-04, -3.553730682e-04, -2.086261490e-04, -3.553730646e-04)}
print('Lemma G (r1919_gauge.out): spatially Ward-exact local kernels have face2 = T2g, face1 = (3 Eg + T2g)/4, mu = 0;')
print('4D Ward-exact ones have all four Xi equal and mu = 0.')
for m, (eg, t2, f1, f2) in rows.items():
    print(' m=%.1f  face2 - T2g = %+.1e   face1 - (3Eg+T2g)/4 = %+.4e   Eg - T2g = %+.4e  (isotropic part (2Eg+3T2g)/5 = %+.4e)'
          % (m, f2 - t2, f1 - (3*eg + t2)/4, eg - t2, (2*eg + 3*t2)/5))
# (2) remainder sizes
c4 = {1.0: 1.61e-5, 0.5: 2.88e-5, 0.3: 3.45e-5}   # max |on-shell R/s^4| over the four rows (r1919_taylor.out, s = 0.05)
lP = 1.616e-35; MP_GeV = 1.22e19; c = 2.998e8
for label, Nsp, boost in [('per NN scalar, m = 0.3', 1, 1.0),
                          ('SM-like count ~100 fields, x30 margin for vertex/edge/log(1/ma) (suggested envelope)', 100, 30.0)]:
    alpha = 16*np.pi*c4[0.3]*Nsp*boost      # omega^2 = q^2 (1 + alpha (q a)^2), a = l_P
    q = 2*np.pi*100.0/c                     # GW170817 band, ~100 Hz
    dv = 0.5*alpha*(q*lP)**2
    EQG2 = MP_GeV/np.sqrt(alpha)
    dv_TeV = 0.5*alpha*(1e3/MP_GeV)**2
    print('\n%s: alpha = %.3e' % (label, alpha))
    print('  GW170817 (f = 100 Hz, q a = %.2e): |dc/c| = %.1e   [comparator, RECALLED: -3e-15 <= dc/c <= 7e-16]' % (q*lP, dv))
    print('  quadratic scale E_QG,2 = M_P/sqrt(alpha) = %.1e GeV   [Fermi-LAT-type photon comparator, RECALLED: E_QG,2 >~ 1e11 GeV]' % EQG2)
    print('  |dc/c| at E = 1 TeV: %.1e' % dv_TeV)
