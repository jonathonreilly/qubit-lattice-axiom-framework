"""T53 Test C: label-free content over the NuFIT-6.1 rectangle + parity identity + data-implied labels. Float only."""
import numpy as np, math, json
from chart import obs, preimage, SQ, H
S12 = np.linspace(0.2893, 0.3295, 21)
S13 = np.linspace(0.02070, 0.02420, 21)
rec = []
for a in S12:
    for b in S13:
        roots = preimage(a, b)
        assert len(roots) == 1, (a, b, len(roots))
        m, d = roots[0]; q = SQ - d
        o = obs(m, d, q)
        rec.append((a, b, m, d, o['s23'], o['dcp'], o['sind'], o['cosd']))
rec = np.array(rec)
print('grid 21x21 of NuFIT-6.1 rectangle; unique Basin-1 chamber-boundary preimage at all', len(rec), 'points')
print('preimage (m,d) range: m [%.4f,%.4f] d [%.4f,%.4f]' % (rec[:, 2].min(), rec[:, 2].max(), rec[:, 3].min(), rec[:, 3].max()))
print('sheet (g+,210) dCP band  : [%.3f, %.3f] deg   (repo interval certificate over 5.3 rect: [251.86,270.00])' % (rec[:, 5].min(), rec[:, 5].max()))
print('s23^2 = threshold t      : [%.4f, %.4f]   (repo 5.3-rect surface [0.5335,0.5476])' % (rec[:, 4].min(), rec[:, 4].max()))
print('|sin d| range            : [%.4f, %.4f]' % (abs(rec[:, 6]).min(), abs(rec[:, 6]).max()))
print('|cos d| max              : %.4f  -> delta within %.2f deg of +-90' % (abs(rec[:, 7]).max(), math.degrees(math.asin(abs(rec[:, 7]).max()))))
print('label-free gap in s23^2  : |s23^2-1/2| >= %.4f (min over rect); at centre %.4f' % (rec[:, 4].min() - 0.5, 0.540969818 - 0.5))
# band per surviving J<0 sheet
band_A = (rec[:, 5].min(), rec[:, 5].max())
band_B = (360 - band_A[1] + 180 - 180 + 0, 0)  # placeholder
# sheet (g-,201): dCP = 360 - (180 - dCP_A) ... verified numerically below
dB = []
for a, b, m, d, s23, dcpA, sd, cd in rec:
    o = obs(m, d, SQ - d, -0.5, (2, 0, 1)); dB.append(o['dcp'])
dB = np.array(dB)
print('sheet (g-,201) dCP band  : [%.3f, %.3f] deg; s23^2 in [%.4f,%.4f]' % (dB.min(), dB.max(), 1 - rec[:, 4].max(), 1 - rec[:, 4].min()))
print('J<0 union of both sheets : [%.2f, %.2f] deg  i.e. 270 +- %.1f' % (band_A[0], dB.max(), max(270 - band_A[0], dB.max() - 270)))

# parity identity J_sigma = parity(sigma) I_src / Delta on the four sheets at the pin
pin = (0.657061342210, 0.933806343759, 0.715042329587)
print('\nParity identity check J = parity(sigma) * I_src / Delta (I_src = Im(H12 H23 H31), Delta = (l1-l2)(l2-l3)(l3-l1), ascending l)')
import itertools
for g in (0.5, -0.5):
    Hm = H(*pin, g)
    w, V = np.linalg.eigh(Hm); o = np.argsort(w.real); w = w[o].real; V = V[:, o]
    Isrc = (Hm[0, 1] * Hm[1, 2] * Hm[2, 0]).imag
    Delta = (w[0] - w[1]) * (w[1] - w[2]) * (w[2] - w[0])
    for perm in [(2, 1, 0), (2, 0, 1)]:
        oo = obs(*pin, g, perm)
        # parity of perm as permutation of (0,1,2) rows
        par = np.linalg.det(np.eye(3)[list(perm), :])
        # J_basis = Im(V11 V22 V12* V21*) in 1-indexed = Im(V[0,0] V[1,1] conj(V[0,1]) conj(V[1,0]))
        Jb = (V[0, 0] * V[1, 1] * np.conj(V[0, 1]) * np.conj(V[1, 0])).imag
        print('gamma=%+.1f perm=%s  J=%+.6f  parity*Isrc/Delta=%+.6f   (Isrc=%+.5f Delta=%+.5f parity=%+d)' % (g, perm, oo['J'], par * Isrc / Delta, Isrc, Delta, par))
# data-implied labels: NuFIT-6.1 best fit has J<0 (dCP 207/212 -> sin<0) and lower octant (0.470)
print('\nData-implied labels (reading): sgn J = gamma_hat * sigma_hat_parity ; octant side = sigma. Best fit sin d<0, s23^2=0.470<1/2 -> sigma=(2,0,1) and gamma<0 (A13<0).')
json.dump(dict(band_A=[float(band_A[0]), float(band_A[1])], band_B=[float(dB.min()), float(dB.max())],
               t_range=[float(rec[:, 4].min()), float(rec[:, 4].max())], sind_abs_min=float(abs(rec[:, 6]).min()),
               cosd_abs_max=float(abs(rec[:, 7]).max())), open('testC_result.json', 'w'), indent=1)
