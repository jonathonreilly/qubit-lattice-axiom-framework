"""R11-6: where does the near-null vector of A_S3 live?  Conjugate-position profile (FFT over the master (p3, q12) grid):
x3 = spectator-pair separation conjugate to p3, x12 = pair separation conjugate to q12 (ring period L in each)."""
import numpy as np, sys
from r116_core import *
args = dict(a.split('=') for a in sys.argv[1:])
L = int(args.get('L', 240)); P = float(args.get('P', 0.4))
F = Fibre(L, P, 0.55, 0.55).build()
A = np.eye(F.N) + sum(F.Bm1)
U, S, Vh = np.linalg.svd(A)
out = []
for idx in (-1, -2, -3):
    v = Vh[idx].conj().reshape(F.Np, F.Nq)
    # zero-pad to the ring period and FFT -> conjugate positions
    n = int(round(2*np.pi/F.h))
    Vp = np.zeros((n, n), complex); Vp[:F.Np, :F.Nq] = v
    X = np.fft.fftshift(np.abs(np.fft.fft2(Vp))**2); X /= X.sum()
    xs = np.fft.fftshift(np.fft.fftfreq(n, d=1.0/n))
    X3, X12 = np.meshgrid(xs, xs, indexing='ij')
    def w(cond): return X[cond].sum()
    s = ('L=%d P=%.1f sing.value %.3e: weight |x3|<L/8: %.3f, L/8<|x3|<L/4: %.3f, |x3|>L/4: %.3f ; |x12|<L/8: %.3f, |x12|>L/4: %.3f ; '
         'mean |x3| = %.1f, mean |x12| = %.1f'
         % (L, P, S[idx], w(np.abs(X3) < n/8), w((np.abs(X3) >= n/8) & (np.abs(X3) < n/4)), w(np.abs(X3) >= n/4),
            w(np.abs(X12) < n/8), w(np.abs(X12) >= n/4), np.sum(np.abs(X3)*X), np.sum(np.abs(X12)*X)))
    print(s, flush=True); out.append(s)
open('r116_nullvec_L%d_P%.1f.out' % (L, P), 'w').write('\n'.join(out) + '\n')
