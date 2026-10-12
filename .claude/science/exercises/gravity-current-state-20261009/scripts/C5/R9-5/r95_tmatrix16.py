"""R9-5 script 3c: exact one-fermion on-shell T-matrix off the local vison pair (one sigma^z) for the
actual law truncated at RMAX = 16 (vectorised build; cf. r95_visons.py at RMAX = 12).  Box momenta,
non-forward, infinite-volume Green function by BZ quadrature (untruncated eps)."""
import numpy as np, sys, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r95_common import *
out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)
t0 = time.time()
Mfull, _ = hopping_M(512)
RMAX, L = 16, 48
offs = [(a, b) for a in range(-RMAX, RMAX+1) for b in range(-RMAX, RMAX+1)]
zoff = [[(u[0], u[1]) for (u, v, t) in path((0, 0, 'A'), 'B', r)[1] if t == 'z'] for r in offs]
N = L*L
n1, n2 = np.meshgrid(np.arange(L), np.arange(L), indexing='ij'); n1 = n1.ravel(); n2 = n2.ravel(); I = n1*L + n2
def build(Fgrid):
    Mab = np.zeros((N, N))
    for r, zs in zip(offs, zoff):
        m_ = Mfull[r[0] % 512, r[1] % 512]; sg = np.ones(N)
        for (o1, o2) in zs: sg *= 1 - 2*Fgrid[(n1+o1) % L, (n2+o2) % L]
        Mab[I, ((n1+r[0]) % L)*L + (n2+r[1]) % L] += sg*m_
    return Mab
D0 = (L//2, L//2)
F = np.zeros((L, L)); F[D0] = 1
dM = build(F) - build(np.zeros((L, L)))
ii, jj = np.nonzero(dM)
rowsA = np.unique(ii); rowsB = np.unique(jj)
def off(d):
    a, b = divmod(d, L); return ((a - D0[0] + L//2) % L - L//2, (b - D0[1] + L//2) % L - L//2)
pos = [off(d) + (0,) for d in rowsA] + [off(d) + (1,) for d in rowsB]
nA = len(rowsA)
dh = np.zeros((len(pos), len(pos)), complex)
sub = dM[np.ix_(rowsA, rowsB)]
dh[:nA, nA:] = 1j*sub; dh[nA:, :nA] = -1j*sub.T
pr('RMAX=%d: dh support %d A-sites, %d B-sites; max|dh| = %.3f' % (RMAX, nA, len(rowsB), np.abs(dh).max()))
P = np.array(pos)
def G0_region(z, Nk):
    kq = 2*np.pi*np.fft.fftfreq(Nk); Q1, Q2 = np.meshgrid(kq, kq, indexing='ij'); e = eps(Q1, Q2); den = z*z - e*e
    g = {(0, 0): np.fft.ifft2(z/den), (1, 1): np.fft.ifft2(z/den), (0, 1): np.fft.ifft2(1j*e/den), (1, 0): np.fft.ifft2(-1j*e/den)}
    G = np.zeros((len(P), len(P)), complex)
    for sa in (0, 1):
        for sb in (0, 1):
            ia = np.where(P[:, 2] == sa)[0]; ib = np.where(P[:, 2] == sb)[0]
            d1 = (P[ia, 0][:, None] - P[ib, 0][None, :]) % Nk; d2 = (P[ia, 1][:, None] - P[ib, 1][None, :]) % Nk
            G[np.ix_(ia, ib)] = g[(sa, sb)][d1, d2]
    return G
psi = np.array([1.0, -1j])/np.sqrt(2)
def wave(kv): return np.exp(1j*(P[:, 0]*kv[0] + P[:, 1]*kv[1]))*psi[P[:, 2]]
for kin in [np.array([0.5, 0.2]), np.array([1.2, -0.7])]:
    Ein = eps(*kin); kr = np.array([-kin[1], kin[0]])
    outs = {'rot90': kr, 'back': -kin, 'mirror': kin[::-1].copy(), 'fwd': kin}
    for Nk, eta in [(1024, 0.01), (1024, 0.005)]:
        G = G0_region(Ein + 1j*eta, Nk); T = dh @ np.linalg.inv(np.eye(len(P)) - G @ dh); vin = wave(kin)
        pr('  k=(%.2f,%.2f) E=%.4f Nk=%d eta=%.3f: ' % (kin[0], kin[1], Ein, Nk, eta) +
           '; '.join('%s |t|=%.4f' % (nm, abs(wave(kv).conj() @ T @ vin)) for nm, kv in outs.items()))
pr('runtime %.1f s' % (time.time() - t0))
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out) + '\n')
