"""F1 (a) locality (D1 symbols have the mirror symmetry s(pi-k)=s(k): even harmonics vanish at t=0, so TAIL maxima are reported): position-space hopping amplitudes of the SF-strained Dirac operator D_t = D o Phi^F_t and photon symbol d_t^2,
by FFT on a full-zone periodic grid. Reports max |amplitude| on shells |x|_inf = R, at t = 0 and t = 0.2 (10x the FD steps)."""
import numpy as np
from f1_lib import *
F = Ferm(*ROOT, mflow=0.01); G = Phot(CPH)
N = 96
k = (np.arange(N))*2*np.pi/N; k = np.where(k > np.pi, k - 2*np.pi, k)
def full_flowF(t):
    X, Y, Z = np.meshgrid(k, k, k, indexing='ij')
    sgx, sgy = np.sign(X), np.sign(Y)
    ax, ay = np.abs(X), np.abs(Y)
    fx, fy = flowF(F, ax, ay, F.W(Z), t, 8)   # flow commutes with reflections: flow |k| then restore signs
    return sgx*fx, sgy*fy, Z
def shells(A):
    a = np.abs(np.fft.fftn(A))/A.size
    idx = np.minimum(np.arange(N), N - np.arange(N))
    R = np.maximum(np.maximum(idx[:, None, None], idx[None, :, None]), idx[None, None, :])
    return [a[R >= r].max() for r in range(0, N//2 + 1)]        # TAIL max over |x|_inf >= r
for t in (0.0, 0.2):
    fx, fy, Z = full_flowF(t)
    M = F.W(fx) + F.W(fy) + F.W(Z)
    cx = F.s(fx)
    sm, sc = shells(M), shells(cx)
    print('t = %.1f   D_t mass part M_t: tail max|hop| for |x|>=R, R = 1,3,5,9,13,17,25,31: %s' % (t, ' '.join('%.1e' % sm[r] for r in (1, 3, 5, 9, 13, 17, 25, 31))))
    print('          D_t gamma_x part : tail max|hop| for |x|>=R, R = 1,3,5,9,13,17,25,31: %s' % ' '.join('%.1e' % sc[r] for r in (1, 3, 5, 9, 13, 17, 25, 31)))
    for sg in (+1, -1):
        q = np.abs(k); qq = flowG1(G, q, sg, t, 8)
        d2 = G.d(qq)**2
        a = np.abs(np.fft.fft(d2))/N; idx = np.minimum(np.arange(N), N - np.arange(N))
        print('          photon d_t^2 (axis sgn %+d): tail max|hop| R = 1,3,5,9,17,25,31: %s' % (sg, ' '.join('%.1e' % a[idx >= r].max() for r in (1, 3, 5, 9, 17, 25, 31))))
    dodd = np.sign(k)*G.d(np.abs(k))
    a = np.abs(np.fft.fft(dodd))/N; idx = np.minimum(np.arange(N), N - np.arange(N))
    if t == 0.0:
        print('   root photon ODD symbol d (gauge-transformation kernel), t = 0: |hop| at R = 1,2,4,8,16,31: %s  (face jump d(pi) = %.4f: power-law tail, pre-existing)'
              % (' '.join('%.1e' % a[idx == r].max() for r in (1, 2, 4, 8, 16, 31)), G.d(np.pi)))
