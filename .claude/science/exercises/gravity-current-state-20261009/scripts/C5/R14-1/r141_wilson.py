"""R14-1 (E): is a subluminal Wilson-box Dirac possible?  Two-band law (R8-5 form):
  D(k) = sum_i gamma_i s(k_i) + (m + sum_i W(k_i)),  E^2 = (m + sum W)^2 + sum s^2   (each band doubly degenerate).
Box: |k_i| <= b with s = k, W = 0 -> E = sqrt(m^2 + k^2) exactly.
Design D1(r): s = R13-4 odd symbol S(b) (|s'| <= 1); W' = r sqrt(1 - s'^2) >= 0 on [b, pi-b] (W flat elsewhere), W even.
  On each axis the curve (W, s) then has speed sqrt(W'^2 + s'^2) <= 1 (r <= 1).  Corner doublers get mass m + n W_pi.
Checks: whole-zone v_max (d = 1 axis, d = 3 grid + lines), box exactness, corner masses, kernel decay of W.
"""
import numpy as np
from sublum import sstep, wrap, SymS
out = []
def pr(*a):
    l = ' '.join(str(x) for x in a); print(l, flush=True); out.append(l)
xg, wg = np.polynomial.legendre.leggauss(8)
def make(b, r):
    A = SymS(b); w = A.w
    # W(k) = r * int_b^|k| sqrt(1 - sigma^2), tabulated accurately; W' analytic
    edges = np.linspace(0, 1, 20001); mid = 0.5*(edges[1:]+edges[:-1]); half = 0.5*(edges[1]-edges[0])
    sig = lambda x: 1 - 2*sstep(x)
    cell = (np.sqrt(np.maximum(0, 1 - sig(mid[:, None] + half*xg[None, :])**2))*wg).sum(1)*half
    tab = np.concatenate([[0.0], np.cumsum(cell)])*w*r
    def W(k):
        a = np.abs(wrap(k)); x = np.clip((a - b)/w, 0, 1); return np.interp(x, edges, tab)
    def dW(k):
        k = wrap(k); a = np.abs(k); x = (a - b)/w
        return np.sign(k)*r*np.sqrt(np.maximum(0, 1 - (1 - 2*sstep(x))**2))
    return A, W, dW, tab[-1]
N1 = 400000; k1 = np.linspace(-np.pi, np.pi, N1, endpoint=False) + np.pi/N1
N3 = 160; k3 = np.linspace(-np.pi, np.pi, N3, endpoint=False) + np.pi/N3
for b in (1.4, 1.2, 1.0):
    for m in (0.1, 0.3):
        for r in (1.0, 0.7, 1/np.sqrt(3), 0.5):
            A, W, dW, Wpi = make(b, r)
            s1, ds1, W1, dW1 = A.s(k1), A.ds(k1), W(k1), dW(k1)
            M1 = m + W1; E1 = np.sqrt(M1**2 + s1**2); v1 = np.max(np.abs(M1*dW1 + s1*ds1)/E1)
            sv, dsv, Wv, dWv = A.s(k3), A.ds(k3), W(k3), dW(k3); best = 0
            for a in range(N3):
                M = m + Wv[a] + Wv[:, None] + Wv[None, :]
                E = np.sqrt(M**2 + sv[a]**2 + sv[:, None]**2 + sv[None, :]**2)
                gx = (M*dWv[a] + sv[a]*dsv[a])/E; gy = (M*dWv[:, None] + (sv*dsv)[:, None])/E; gz = (M*dWv[None, :] + (sv*dsv)[None, :])/E
                best = max(best, np.sqrt(gx**2 + gy**2 + gz**2).max())
            # lines: (k,k,0), (k,k,k), and (k, k', k') with k' in slab centre
            lines = []
            for n in (2, 3):
                M = m + n*W1; E = np.sqrt(M**2 + n*s1**2); lines.append(np.max(np.sqrt(n)*np.abs(M*dW1 + s1*ds1)/E))
            inb = np.abs(k1) <= b
            pr('b=%.1f m=%.1f r=%.3f: W_pi = %.4f; corner masses m+W_pi, m+2W_pi, m+3W_pi = %.3f %.3f %.3f; v_max d=1 %.4f, d=3 grid %.4f, lines %.4f %.4f; box: max|W| %.1e max|s-k| %.1e'
               % (b, m, r, Wpi, m+Wpi, m+2*Wpi, m+3*Wpi, v1, best, *lines, np.max(np.abs(W1[inb])), np.max(np.abs(s1[inb]-k1[inb]))))
# kernel decay of W and s (b = 1.4, r = 1)
A, W, dW, Wpi = make(1.4, 1.0)
Nf = 8192; kf = 2*np.pi*np.fft.fftfreq(Nf)
Wr = np.abs(np.fft.ifft(W(kf))); sr = np.abs(np.fft.ifft(A.s(kf)))
pr('kernel |W|(r) (odd r; W - W_pi/2 is pi-antiperiodic so even r vanish): ' + ' '.join('r=%d:%.1e' % (r, Wr[r]) for r in [1, 9, 33, 65, 129, 257, 513]))
pr('kernel |s|(r) (odd r; s(k+pi) = -s(k)): ' + ' '.join('r=%d:%.1e' % (r, sr[r]) for r in [1, 9, 33, 65, 129, 257, 513]))
pr('note: W has a sqrt-type C^inf profile (sqrt(4 st(1-st)) of a Gevrey step); its kernel is the check of quasi-locality.')
with open(__file__.replace('.py', '.out'), 'w') as f: f.write('\n'.join(out) + '\n')
