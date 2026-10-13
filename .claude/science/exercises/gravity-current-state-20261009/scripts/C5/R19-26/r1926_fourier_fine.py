"""R19-26 convention-free locality test.  For fixed k2 and (q_y, q_z), the periodic-gauge kernel
    G^{mu nu}(q) = e^{-i q.p_{mu nu}} Phi(k1) M~^{mu nu}(k1, k2) Phi(k2)^{-1},   k1 = wrap(k2 + q),  q_x in (-pi, pi],
Phi(k) = diag(e^{i k.r_a}) with the true field positions r(E_a) = e_a/2, r(B_a) = (e_b + e_c)/2, p_{mu nu} = (e_mu + e_nu)/2,
is representative-independent (the rotated-frame twist T_l cancels against Phi) and is the Fourier symbol of the position-space
stress kernel at fixed k2 along x.  A local (quasi-local) stress needs G smooth and 2 pi-periodic in q_x; a jump anywhere on the
circle (BZ face of k1, or the transfer cut q_x = +-pi) shows up as a 1/n tail of its Fourier coefficients.  No sign rule is used.
Reported: max over (mu, nu, a, b) of |c_n| in bands of n, for the R19-16 kernel and the re-placed kernel; full and physical block."""
import numpy as np, lib1926 as R
L = R.L
import sys
r = 0.1; NP = int(sys.argv[1])
rng = np.random.default_rng(26)
RE = np.array([[.5, 0, 0], [0, .5, 0], [0, 0, .5], [0, .5, .5], [.5, 0, .5], [.5, .5, 0]])   # true positions of E_x..B_z
PP = np.zeros((4, 4, 3))
for mu in range(4):
    for nu in range(4):
        if mu: PP[mu, nu, mu - 1] += .5
        if nu: PP[mu, nu, nu - 1] += .5

def G(q, k2, phys):
    k1 = L.wrap(k2 + q)
    M = L.glued(k1, k2, r)
    if phys:
        P1, P2 = L.projs(k1)[4], L.projs(k2)[4]; M = np.einsum('ab,mnbc,cd->mnad', P1, M, P2)
    ph1 = np.exp(1j*RE @ k1); ph2 = np.exp(-1j*RE @ k2); pq = np.exp(-1j*PP @ q)
    return pq[:, :, None, None]*ph1[None, None, :, None]*M*ph2[None, None, None, :]

bands = [(64, 128), (256, 512), (512, 1024), (1024, 2048)]
def run(tag):
    for line in range(1):
        rs = np.random.default_rng(100 + line)
        k2 = rs.uniform(-np.pi, np.pi, 3); k2 *= np.maximum(1.0, 0.6/np.abs(k2)) * (np.abs(k2) < np.pi - 0.3) + (np.abs(k2) >= np.pi - 0.3)
        qyz = rs.uniform(-np.pi, np.pi, 2)
        qs = -np.pi + 2*np.pi*(np.arange(NP) + 1)/NP          # (-pi, pi]
        for phys in (False,):
            if phys and line > 0: continue
            vals = np.array([G(np.array([qx, qyz[0], qyz[1]]), k2, phys) for qx in qs])
            c = np.fft.fft(vals, axis=0)/NP
            amp = np.abs(c).reshape(NP, -1).max(axis=1)
            nmin1 = min(np.linalg.norm(L.wrap(k2 + np.array([qx, *qyz]))) for qx in qs)
            print('[%s] line %d k2=(%.3f,%.3f,%.3f) q_yz=(%.3f,%.3f) min|k1| %.3f %s: |c_0| %.3e; ' % (
                tag, line, *k2, *qyz, nmin1, 'PHYS' if phys else 'FULL', amp[0]) +
                '; '.join('max|c_n| n in [%d,%d]: %.2e' % (a, b, max(amp[a:b + 1].max(), amp[NP - b:NP - a + 1].max())) for a, b in bands), flush=True)

R.unpatch(); run('R19-16 ')
R.patch(); run('REPLACED')
