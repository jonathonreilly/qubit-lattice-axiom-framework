"""R9-5 script 1: the spin law's coefficients and a norm certificate for its tails.

Spin law (Route A, flux-free realisation of R7-1's free box law on the dimer lattice):
   H_spin = -(1/2) sum_R sum_r M(r) S_{gamma_r}(A_R -> B_{R+r})   [- Delta_v sum_p W_p, range 6]
with M(r) the real even Fourier coefficients of eps(k) = sqrt(m^2 + s(k1)^2 + s(k2)^2) (R7-1 literal).
Each string S is a product of l(r) Kitaev bond operators, a Pauli string of weight l(r)+1, norm 1.

Certificate.  For any weight F, ||Phi||_F := sup_x sum_{X ni x} ||Phi(X)|| F(diam X)
   <= sum_r (1/2)|M(r)| (l(r)+1) F(l(r))                                  (each site lies on <= l+1 translates)
and |M(r)| <= C_p / |r|_inf^p with C_p = max_j || d_j^p eps ||_{L1(T^2, dk/(2pi)^2)} (integration by parts).
We compute the finite part |r|_inf <= R0 from the FFT and bound the rest with C_p.
"""
import numpy as np, sys, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r95_common import *

t0 = time.time()
out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)

N = 1024
M, im = hopping_M(N)
pr('M(r): N=%d grid; max|Im| = %.1e; M(0) = %.6f; M even: max|M(r)-M(-r)| = %.1e'
   % (N, im, M[0, 0], np.max(np.abs(M - np.roll(M[::-1, ::-1], 1, axis=(0, 1))))))
# box exactness on the dimer lattice
kk = np.linspace(-Bbox, Bbox, 801)
K1, K2 = np.meshgrid(kk, kk, indexing='ij')
pr('eps = sqrt(m^2+k^2) on the closed box |k_i| <= %.1f: max dev = %.1e' % (Bbox, np.max(np.abs(eps(K1, K2) - np.sqrt(MASS**2 + K1**2 + K2**2)))))
# path lengths
r = np.fft.fftfreq(N, 1.0/N).astype(int)
R1, R2 = np.meshgrid(r, r, indexing='ij')
def lpath(a, b):
    a, b = np.asarray(a), np.asarray(b)
    same = (a*b > 0)
    pairs = np.where(same, np.maximum(np.abs(a), np.abs(b)), np.abs(a) + np.abs(b))
    return 2*pairs + 1
L = lpath(R1, R2)
# spot check of the closed form against the explicit path constructor
for (a, b) in [(0, 0), (3, 2), (-4, 1), (5, -5), (-2, -7), (0, -3)]:
    assert len(path((0, 0, 'A'), 'B', (a, b))[1]) == lpath(a, b), (a, b)
pr('path length l(r) = 2*pairs + 1 (checked against explicit constructor); l <= 2|r|_1 + 1')
Rinf = np.maximum(np.abs(R1), np.abs(R2))
pr('|M(r)| on axis r=(rho,0):', ' '.join('%d:%.2e' % (q, abs(M[q, 0])) for q in [0, 1, 2, 4, 8, 16, 32, 64, 128, 256]))
pr('|M(r)| diagonal r=(rho,rho):', ' '.join('%d:%.2e' % (q, abs(M[q, q])) for q in [1, 2, 4, 8, 16, 32, 64, 128]))
# envelope: max over the shell |r|_inf = rho
env = {}
for q in [8, 16, 32, 64, 96, 128, 192, 256, 384]:
    env[q] = np.max(np.abs(M[Rinf == q]))
pr('shell max_{|r|_inf=rho}|M|:', ' '.join('%d:%.2e' % (q, v) for q, v in env.items()))
qs = np.array([16, 32, 64, 96, 128, 192, 256]); vs = np.array([env[q] for q in qs])
# fit log|M| = a - c rho^beta over the resolved range (finite-range evidence only)
best = None
for beta in np.linspace(0.2, 1.0, 81):
    A = np.vstack([np.ones_like(qs, dtype=float), -qs**beta]).T
    coef, res, *_ = np.linalg.lstsq(A, np.log(vs), rcond=None)
    rr = np.sum((A @ coef - np.log(vs))**2)
    if best is None or rr < best[0]: best = (rr, beta, coef)
pr('stretched-exp fit of the shell envelope over rho in [16,256]: beta = %.2f, c = %.3f (finite-range evidence; Gevrey-2 theory: beta = 1/2, RECALLED)'
   % (best[1], best[2][1]))
# derivative bound C_p (spectral differentiation along k1, fine 1D grid; eps symmetric in k1<->k2)
p = 8
N1 = 2**15; k1 = 2*np.pi*np.fft.fftfreq(N1); k2s = 2*np.pi*(np.arange(256) + 0.5)/256 - np.pi
acc = 0.0
for k2 in k2s:
    f = eps(k1, k2*np.ones_like(k1))
    fh = np.fft.fft(f)
    d = np.fft.ifft(fh*(1j*np.fft.fftfreq(N1, 1.0/N1))**p).real
    acc += np.mean(np.abs(d))
Cp = acc/len(k2s)
pr('C_%d = ||d_1^%d eps||_L1 = %.3e (spectral, 2^15 x 256 grid; checked, not interval-certified)' % (p, p, Cp))
# certificate: finite part plus tail
R0 = 400
mask = (Rinf <= R0)
for n in [0, 1, 2, 3, 4]:
    F = (1.0 + L)**n
    fin = np.sum(0.5*np.abs(M[mask])*(L[mask] + 1)*F[mask])
    # tail: shells rho > R0 have 8 rho points, |r|_1 <= 2 rho, l <= 4 rho + 1, |M| <= Cp rho^-p
    rho = np.arange(R0 + 1, 2000000, dtype=float)
    tail = np.sum(8*rho*0.5*Cp*rho**(-p)*(4*rho + 2)*(4*rho + 2)**n)
    pr('||Phi||_{F_n}, F_n(d) = (1+d)^%d : finite part (|r|_inf <= %d) = %.4e ; certified tail bound = %.1e'
       % (n, R0, fin, tail))
pr('aliasing check: |M| at |r|_inf = N/2 = %d : %.1e' % (N//2, np.max(np.abs(M[Rinf == N//2]))))
pr('runtime %.1f s' % (time.time() - t0))
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out) + '\n')
