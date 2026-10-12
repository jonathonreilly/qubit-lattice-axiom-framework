"""R9-5 script 4: explicit tail constants for the spin law's coefficients M(r) via exact derivative jets.

|M(r)| <= C_p / |r|_inf^p,  C_p = max_j (2pi)^-2 int_{T^2} |d_j^p eps| d^2k   (integration by parts; periodic).
d_1^p eps is computed by truncated Taylor-series (jet) arithmetic through the explicit formula
  eps = sqrt(m^2 + s(k1)^2 + s(k2)^2), s = rho k + (1-rho) sin k, rho = sstep((B2-|k|)/(B2-B)),
  sstep(x) = e^{-1/x} / (e^{-1/x} + e^{-1/(1-x)}),
so no Fourier data and no roundoff amplification by r^p enter (unlike r95_tails.py's spectral C_8,
which is roundoff-dominated and is superseded here).  Quadrature: nonuniform k1 grid, dense on the
transition shells B <= |k1| <= B2; label: checked (floating point, not interval arithmetic).
Then the F_n-norm tail beyond |r|_inf > R0 is bounded with min_p C_p rho^-p."""
import numpy as np, sys, time, math
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r95_common import *
out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)
t0 = time.time()
P = 40
def mul(a, b):
    c = np.zeros_like(a)
    for i in range(P+1):
        c[i:] += a[i]*b[:P+1-i]
    return c
def recip(a):
    b = np.zeros_like(a); b[0] = 1/a[0]
    for n in range(1, P+1):
        b[n] = -np.sum(a[1:n+1]*b[n-1::-1][:n], axis=0)/a[0]
    return b
def expo(a):
    b = np.zeros_like(a); b[0] = np.exp(a[0])
    for n in range(1, P+1):
        j = np.arange(1, n+1).reshape(-1, *([1]*(a.ndim-1)))
        b[n] = np.sum(j*a[1:n+1]*b[n-1::-1][:n], axis=0)/n
    return b
def sqrt_(a):
    b = np.zeros_like(a); b[0] = np.sqrt(a[0])
    for n in range(1, P+1):
        acc = a[n] - np.sum(b[1:n]*b[n-1:0:-1], axis=0) if n > 1 else a[n]
        b[n] = acc/(2*b[0])
    return b
def const(v, npts):
    a = np.zeros((P+1, npts)); a[0] = v; return a
def s_jet(k0):
    """Taylor jet of s at points k0 (in (-pi, pi]), in t: s(k0 + t)."""
    npts = len(k0)
    sinj = np.zeros((P+1, npts))
    for j in range(P+1): sinj[j] = np.sin(k0 + j*np.pi/2)/math.factorial(j)
    kj = const(k0, npts); kj[1] = 1.0
    # rho jet
    ak = np.abs(k0); sg = np.sign(k0)
    x0 = (B2 - ak)/(B2 - Bbox)
    xj = const(x0, npts); xj[1] = -sg/(B2 - Bbox)
    rhoj = np.zeros((P+1, npts))
    inner = x0 >= 1; outer = x0 <= 0; mid = ~(inner | outer)
    rhoj[0, inner] = 1.0
    if mid.any():
        xm = xj[:, mid]
        e1 = expo(-recip(xm))
        e2 = expo(-recip(const(1.0, mid.sum()) - xm))
        rhoj[:, mid] = mul(e1, recip(e1 + e2))
    one = const(1.0, npts)
    return mul(rhoj, kj) + mul(one - rhoj, sinj)
# k1 grid: dense on transition shells, coarse elsewhere (open intervals; endpoints have measure 0)
def grid(a, b, n):
    h = (b - a)/n; return a + h*(np.arange(n) + 0.5), np.full(n, h)
pieces = [grid(-np.pi, -B2, 512), grid(-B2, -Bbox, 2**15), grid(-Bbox, Bbox, 2048), grid(Bbox, B2, 2**15), grid(B2, np.pi, 512)]
k1 = np.concatenate([p_[0] for p_ in pieces]); w1 = np.concatenate([p_[1] for p_ in pieces])
sj1 = s_jet(k1)
s1sq = mul(sj1, sj1)
k2 = 2*np.pi*(np.arange(256) + 0.5)/256 - np.pi
s2 = s(k2)
Cp = np.zeros(P+1)
for q, sv in enumerate(s2):
    e = sqrt_(s1sq + const(MASS**2 + sv**2, len(k1)))
    for p in range(P+1):
        Cp[p] += np.sum(np.abs(e[p])*w1)*math.factorial(p)
Cp /= (2*np.pi)*256          # (2pi)^-2 * int dk1 dk2 with dk2 quadrature 2pi/256
pr('jet order P = %d; k1 grid %d points (dense on B<=|k|<=B2); k2 grid 256' % (P, len(k1)))
pr('sanity: C_0 = mean eps = %.6f (M(0) = 1.735523 from FFT)' % Cp[0])
pr('C_p for p = 2,4,...,40: ' + ' '.join('%d:%.2e' % (p, Cp[p]) for p in range(2, P+1, 2)))
# optimal envelope bound and comparison with the FFT coefficients
Mfft, _ = hopping_M(1024)
r = np.fft.fftfreq(1024, 1/1024).astype(int); R1, R2 = np.meshgrid(r, r, indexing='ij'); Rinf = np.maximum(abs(R1), abs(R2))
def bound(rho): return min(Cp[p]*float(rho)**(-p) for p in range(1, P+1))
for rho in [16, 32, 64, 128, 256, 400, 512]:
    pr('  rho=%3d: shell max |M| (FFT) = %.2e  <=  bound min_p C_p rho^-p = %.2e' % (rho, np.abs(Mfft[Rinf == rho]).max(), bound(rho)))
def lpath(a, b):
    same = (a*b > 0); pairs = np.where(same, np.maximum(abs(a), abs(b)), abs(a) + abs(b)); return 2*pairs + 1
Lp = lpath(R1, R2)
for R0 in [400, 512]:
    mask = Rinf <= R0
    for n in [0, 1, 2, 4, 8]:
        fin = np.sum(0.5*np.abs(Mfft[mask])*(Lp[mask] + 1)*(1.0 + Lp[mask])**n)
        tail = 0.0
        rho = R0 + 1
        while True:
            tb = 8*rho*0.5*bound(rho)*(4*rho + 2)**(n+1)
            tail += tb
            if rho > R0 + 50 and tb < 1e-30: break
            rho += 1
            if rho > 10**6: tail = np.inf; break
        pr('  ||Phi||_{F_n}, F_n(d)=(1+d)^%d : finite part (|r|_inf<=%d, FFT) = %.4e ; tail bound = %.2e ; total <= %.4e'
           % (n, R0, fin, tail, fin + tail))
pr('runtime %.1f s' % (time.time() - t0))
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out) + '\n')
