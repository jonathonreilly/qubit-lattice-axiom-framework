"""R8-1, script 5 (d = 2, on the lattice): the two-body box law with the p-wave doublet channel, at fixed
lattice total momentum P on an L x L torus of relative momenta k1 (k2 = P - k1).
Rep-independent necessary conditions for an exact Poincare algebra WITH rotations:
  the bound doublet's invariant mass sqrt(E^2 - P^2) is the same at every P on the plateau, in every
  direction, and the doublet stays degenerate (rotation: l = +1 and l = -1 partners).
The sector of supp W decouples exactly at fixed P (H0 is diagonal in k1), so eig(H restricted to supp)
gives exact eigenvalues of the lattice H at that P.
Comparator: the same doublet as a Galilean pair potential in lattice relative momentum k1 - P/2.
"""
import numpy as np, sys
from r81_common import sstep, wrap, BoxLaw, BTKernel, lam_for_mass

L = int(sys.argv[1]) if len(sys.argv) > 1 else 128
m, KAP, MU_B, PI1, PI2 = 0.5, 0.8, 0.85, 0.6, 1.2
lam = lam_for_mass(m, KAP, 2, MU_B)
Kk = BTKernel(m, KAP, lam, 2)
law = BoxLaw(m, B=2.6, B2=3.0)
cP = lambda P: sstep((PI2 - np.abs(P))/(PI2 - PI1))
out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)

g = 2*np.pi*np.arange(L)/L
K1x, K1y = np.meshgrid(wrap(g), wrap(g), indexing='ij'); K1x, K1y = K1x.ravel(), K1y.ravel()
def sector(nP, mode):
    P = wrap(2*np.pi*np.array(nP)/L)
    k2x, k2y = wrap(P[0] - K1x), wrap(P[1] - K1y)
    ok = (np.abs(K1x) < 2.0) & (np.abs(K1y) < 2.0) & (np.abs(k2x) < 2.0) & (np.abs(k2y) < 2.0) \
         & (np.abs(K1x + k2x - P[0]) < 1e-9) & (np.abs(K1y + k2y - P[1]) < 1e-9)
    e1 = np.sqrt(m*m + K1x**2 + K1y**2); e2 = np.sqrt(m*m + k2x**2 + k2y**2)
    H0 = law.eps(K1x, K1y) + law.eps(k2x, k2y)
    P2 = P @ P; Hs = e1 + e2; M0 = np.sqrt(np.maximum(Hs**2 - P2, 1e-30))
    Pk = P[0]*K1x + P[1]*K1y
    qx = K1x + P[0]*(Pk/(M0*(Hs + M0)) - e1/M0); qy = K1y + P[1]*(Pk/(M0*(Hs + M0)) - e1/M0)
    w = np.sqrt(m*m + qx**2 + qy**2)
    Jq = (w*w*Hs)/(e1*e2*2*w)               # |det dq/dk1| at fixed P = 1/Jacobian
    if mode == 'BT':
        sel = ok & (qx**2 + qy**2 < KAP**2)
        r = np.sqrt(qx[sel]**2 + qy[sel]**2)
        Om = Kk.Omega(P2, r, r)
        dot = np.outer(qx[sel], qx[sel]) + np.outer(qy[sel], qy[sel])
        bb = Kk.b(r**2)
        W = (2*np.pi/L)**2*cP(np.sqrt(P2))*dot*np.outer(bb, bb)*Om*np.sqrt(np.outer(Jq[sel], Jq[sel]))
    else:                                     # Galilean comparator: same doublet in k_r = k1 - P/2
        krx, kry = wrap(K1x - P[0]/2), wrap(K1y - P[1]/2)
        sel = ok & (krx**2 + kry**2 < KAP**2)
        bb = Kk.b(krx[sel]**2 + kry[sel]**2)
        W = (2*np.pi/L)**2*lam*(np.outer(krx[sel]*bb, krx[sel]*bb) + np.outer(kry[sel]*bb, kry[sel]*bb))
    idx = np.where(sel)[0]
    Hm = np.diag(H0[idx]) + W
    # exchange k1 -> P - k1 within sel
    pos = {i: j for j, i in enumerate(idx)}
    n1 = np.arange(L*L); ix, iy = n1 // L, n1 % L
    partner = ((nP[0] - ix) % L)*L + ((nP[1] - iy) % L)
    X = np.zeros((len(idx), len(idx)))
    for j, i in enumerate(idx): X[pos[partner[i]], j] = 1
    Po = 0.5*(np.eye(len(idx)) - X)
    ev = np.linalg.eigvalsh(Po @ Hm @ Po)
    ev = np.sort(ev[np.abs(ev) > 1e-10])
    return P, ev[:3], len(idx)

pr('L = %d, m = %.2f, kappa = %.2f, lam = %.6f (doublet M_b = %.2f), plateau |P| <= %.2f' % (L, m, KAP, lam, MU_B, PI1))
vecs = [(0, 0), (3, 0), (0, 3), (2, 2), (6, 1), (4, -5), (-7, 3), (9, 4), (11, 0), (8, 8), (14, 3)]
for mode in (['BT'] if len(sys.argv) > 2 else ['BT', 'Galilean']):
    rows = []
    for v in vecs:
        nP = tuple(int(round(c*L/128)) for c in v)
        P, ev, ns = sector(nP, mode)
        Pn = np.sqrt(P @ P)
        Mb = np.sqrt(ev[0]**2 - Pn**2); Mb2 = np.sqrt(ev[1]**2 - Pn**2)
        rows.append((Pn, cP(Pn), Mb, Mb2))
        pr('  %-8s nP = %-9s |P| = %.4f dir = %+6.1f deg  c = %.3f  sqrt(E1^2-P^2) = %.12f  sqrt(E2^2-P^2) = %.12f  (doublet split %.1e; %d pair states)'
           % (mode, str(nP), Pn, np.degrees(np.arctan2(P[1], P[0])) if Pn > 0 else 0.0, cP(Pn), Mb, Mb2, abs(Mb2 - Mb), ns))
    pl = np.array([[r[2], r[3]] for r in rows if r[1] == 1.0])
    pr('  %s: plateau spread of the doublet invariant mass (all P, all directions) = %.2e' % (mode, pl.max() - pl.min()))
with open(__file__.replace('.py', '_L%d.out' % L), 'w') as fh:
    fh.write('\n'.join(out) + '\n')
