"""BLEAK-1 comparator: massless Wilson fermion (r = 1) through the same kernels (covariant D_GR vs foliated TT + bridge).

COMPARATOR ONLY: no RP bridge for fermions exists on record (R19-33 is scalar-only), and the Wilson fermion has no exactly
conserved symmetric stress (K2). Stress used (a choice, W(B4)-covariant):
  site bilinear t_mn(p_out, p_in) = (i/4)[g_m (sb_n(p_in)+sb_n(p_out)) + g_n (sb_m(p_in)+sb_m(p_out))]  (sb = sin p)
  minus delta_mn * L,  L = (i/2) g.(sb(p_in)+sb(p_out)) + (M(p_in)+M(p_out))/2,  M(p) = (r/2) shat(p)^2  (Wilson term)
  off-diagonals put on face centres by averaging the 4 corners: factor cos(k_m/2) cos(k_n/2), k = p_in - p_out.
Action D(p) = i g.sb(p) + M(p); propagator S = D^-1.
One loop (Wick, Dirac): Sigma_f(p) = -2c int_k K_AB(k) G_A(p, p-k) S(p-k) G_B(p-k, p),  c = 4 pi G  (S_int = -c int T K T).
Sigma_f(p) = Sigma_0 + i g_a p_a dZ_a + ...; fermion speed c = (1+dZ_s)/(1+dZ_4) -> delta c = dZ_s - dZ_4.
dZ_a = tr(g_a dSigma/dp_a)/(4i) at p = 0, by a central difference (eps = 1e-4) of the integrand at fixed k.
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from b1_core import shat, kernel_parts, iter_chunks

s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]], complex)
Z2 = np.zeros((2, 2)); I2 = np.eye(2)
gam = [np.block([[Z2, -1j * s], [1j * s, Z2]]) for s in (s1, s2, s3)] + [np.block([[Z2, I2], [I2, Z2]]).astype(complex)]
gam = np.array(gam)  # (4,4,4) mu,a,b
R_W = 1.0

def kernel_matrix(k):
    """K[m,n,r,s,pt] for D_GR and D_fol via polarization on symmetric basis E^{mn}."""
    n = k.shape[1]
    E = {}
    for m in range(4):
        for nn in range(m, 4):
            e = np.zeros((4, 4, n)); e[m, nn] += 0.5; e[nn, m] += 0.5
            E[(m, nn)] = e
    Kgr = np.zeros((4, 4, 4, 4, n)); Kfo = np.zeros((4, 4, 4, 4, n))
    keys = list(E.keys())
    for i, A in enumerate(keys):
        for B in keys[i:]:
            WTT, Wi, WGR = kernel_parts(E[A], E[B], k)
            for (m, nn) in {A, A[::-1]}:
                for (r, s) in {B, B[::-1]}:
                    Kgr[m, nn, r, s] = WGR; Kgr[r, s, m, nn] = WGR
                    Kfo[m, nn, r, s] = WTT + Wi; Kfo[r, s, m, nn] = WTT + Wi
    return Kgr, Kfo

def vertex_f(pout, pin):
    """G_mn(pout, pin): (4,4,4,4,n) [m,n,a,b]."""
    kk = pin - pout
    sb = np.sin(pin) + np.sin(pout)
    Mw = 0.25 * R_W * (np.sum(shat(pin) ** 2, 0) + np.sum(shat(pout) ** 2, 0))   # (M(pin)+M(pout))/2
    n = pin.shape[1]
    G = np.zeros((4, 4, 4, 4, n), complex)
    Lmat = 0.5j * np.einsum('mab,mn->abn', gam, sb) + Mw[None, None, :] * np.eye(4)[:, :, None]
    for m in range(4):
        for nn in range(4):
            t = 0.25j * (gam[m][:, :, None] * sb[nn][None, None, :] + gam[nn][:, :, None] * sb[m][None, None, :])
            if m != nn:
                t = t * (np.cos(kk[m] / 2) * np.cos(kk[nn] / 2))[None, None, :]
            else:
                t = t - Lmat
            G[m, nn] = t
    return G

def prop(p):
    sb = np.sin(p); Mw = 0.5 * R_W * np.sum(shat(p) ** 2, 0)
    den = np.sum(sb ** 2, 0) + Mw ** 2
    return (-1j * np.einsum('mab,mn->abn', gam, sb) + Mw[None, None, :] * np.eye(4)[:, :, None]) / den

def sigma_integrand(p, k, K):
    pk = p - k
    Ga = vertex_f(p, pk); Gb = vertex_f(pk, p); S = prop(pk)
    X = np.einsum('mnrsk,rsbck->mnbck', K, Gb)
    Y = np.einsum('mnabk,bck->mnack', Ga, S)
    return np.einsum('mnack,mncdk->adk', Y, X)

def run(N, eps=1e-4, chunk=1 << 12):
    acc = np.zeros((2, 4), complex)   # [GR/fol, alpha] of tr(g_a dSigma/dp_a)/(4i)
    sig0 = np.zeros(2, complex); cnt = 0
    for k in iter_chunks(N, chunk=chunk, lo=-np.pi, hi=np.pi):
        n = k.shape[1]
        Kgr, Kfo = kernel_matrix(k)
        for j, K in enumerate((Kgr, Kfo)):
            s0 = sigma_integrand(np.zeros((4, n)), k, K)
            sig0[j] += np.einsum('aak->', s0) / 4
            for a in range(4):
                e = np.zeros((4, 1)); e[a] = eps
                dS = (sigma_integrand(np.zeros((4, n)) + e, k, K) - sigma_integrand(np.zeros((4, n)) - e, k, K)) / (2 * eps)
                acc[j, a] += np.einsum('ab,bak->', gam[a], dS) / (4j)
        cnt += n
    c = 4 * np.pi
    return -2 * c * acc / cnt, -2 * c * sig0 / cnt

if __name__ == '__main__':
    Ns = [int(x) for x in sys.argv[1:]] or [8, 12, 16]
    print("Wilson fermion r=1, m=0. dZ_a = tr(g_a dSigma/dp_a)/(4i) (G = a = 1); delta c = dZ_s - dZ_4")
    for N in Ns:
        t0 = time.time()
        dZ, s0 = run(N)
        print("N=%3d (%.0fs)  GR: dZ=(%s) row=%+.3e | fol: dZ=(%s) row dZ_s-dZ_4=%+.6f | Sigma_0 GR %.4f fol %.4f | max imag %.1e" % (
            N, time.time() - t0, ", ".join("%+.5f" % z.real for z in dZ[0]), (dZ[0, 0] - dZ[0, 3]).real,
            ", ".join("%+.5f" % z.real for z in dZ[1]), (dZ[1, 0] - dZ[1, 3]).real, s0[0].real, s0[1].real,
            np.abs(dZ.imag).max()), flush=True)
