"""R7-5 script 3: (i) class-P tunability scan (Wilson r and box shape): can XI_P cross zero?
(ii) fermion loop with the invariant-mass factor F(M^2) put on the Feynman integrand (both orderings):
     is J_f(w, p) a function of w^2 + p^2 alone?  (scalar loop: yes, script 1 (D)); spinor numerators carry
     instantaneous pieces 1/(2E) that are not of dispersive form.
(iii) the same fermion loop through its spectral (BT mass-squared) form: Lorentz invariant by construction;
     verify by computing Im-part density and the dispersive integral at several p (identity check)."""
import numpy as np, sys
sys.path.insert(0, '.')
from r75_oneloop import run_box, radial_nodes, plateau, ferm_integrand, OUT, pr
from numpy.polynomial.legendre import leggauss
pr('== (i) class P: scan of the Wilson coefficient r and box shape (m = 0.02, N = 128) ==')
for r in (1.5, 2.0, 3.0, 5.0):
    run_box('f', 2.0, 3.0, 0.02, r, None, N=128, r1=0.4, r2=0.9, label='P ')
for (b1, b2) in ((0.6, 2.4), (1.0, 3.0)):
    run_box('f', b1, b2, 0.02, 1.0, None, N=128, r1=0.2, r2=0.45, label='P ')
pr('== (ii) fermion loop x F(M^2)^2 on the Feynman integrand (both time orderings), continuum, m = 0.2 ==')
m = 0.2; Lam1, Lam2 = 1.0, 1.6
F = lambda M2: plateau(np.sqrt(np.maximum(M2, 0)), Lam1, Lam2)
k, wk = radial_nodes(3.0, m, nper=96); c, wc = leggauss(256)
K, C = np.meshgrid(k, c, indexing='ij'); WK = np.outer(wk*k**2, wc)*2*np.pi/(2*np.pi)**3
def Jf(w, p, drop_inst=False):
    E1 = np.sqrt(K*K + m*m); E2 = np.sqrt(K*K + 2*K*p*C + p*p + m*m)
    W = E1 + E2; M2 = W*W - p*p
    ss = K*K + K*p*C
    I0 = W/(2*E1*E2*(W*W + w*w))
    I2 = 0.5*((0.0 if drop_inst else 1/(2*E1) + 1/(2*E2)) - (w*w + E1*E1 + E2*E2)*I0)
    return np.sum(WK*F(M2)**2*4*((m*m - ss)*I0 - I2))
for a in (0.3, 0.6):
    vals = [Jf(a, 0.0), Jf(0.0, a), Jf(a/np.sqrt(2), a/np.sqrt(2))]
    vd = [Jf(a, 0.0, True), Jf(0.0, a, True), Jf(a/np.sqrt(2), a/np.sqrt(2), True)]
    pr(f'  w^2+p^2 = {a*a:.2f}: J_f (w,0),(0,p),(diag) = {vals[0]:.10f}, {vals[1]:.10f}, {vals[2]:.10f}; spread {max(vals)-min(vals):.2e}')
    pr(f'      without the instantaneous 1/(2E) pieces: {vd[0]:.10f}, {vd[1]:.10f}, {vd[2]:.10f}; spread {max(vd)-min(vd):.2e}')
with open('r75_extra.out', 'w') as fh:
    fh.write('\n'.join(OUT) + '\n')
