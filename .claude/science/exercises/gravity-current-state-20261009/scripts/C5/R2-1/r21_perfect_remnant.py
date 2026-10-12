"""R2-1 probe (a),(d),(e): the Gaussian-blocked (perfect) free scalar on Z^d.

Blocked lattice field Phi = B phi + noise, B^(p) = exp(-sigma |p|^2 / 2) (O(d)-covariant,
so W(B_d)-covariant), noise width 1/alpha. Then
  G(k)   = 1/alpha + sum_n |B^(k+2 pi n)|^2 / ((k+2 pi n)^2 + m^2)   (lattice propagator)
  S_lat  = 1/2 Phi G^{-1} Phi                                        (perfect action)
  T_mu   = B d_mu Delta B^T G^{-1}  (remnant translation = conditional expectation of B d phi)
  t_mu(k)= [sum_n |B^|^2 i(k+2 pi n)_mu / ((k+2pi n)^2+m^2)] / G(k)

Checks:
 1. exactness: Phi^T G^{-1} T Phi = 0 for random Phi on a periodic L^d lattice (T antisymmetric
    w.r.t. G^{-1}), i.e. the GW-type remnant is an exact symmetry of the free perfect action.
 2. locality: Fourier coefficients of G^{-1} and of t_1 decay exponentially; fitted decay rates.
 3. tower: at fixed spatial k_1 the propagator has a pole in complex k_0 for EVERY n_1 in Z
    (E_n = sqrt(m^2 + (k_1 + 2 pi n_1)^2)), with nonzero residue |B^|^2; at the n-th pole the
    remnant translation acts as i(k_1 + 2 pi n_1)  (continuum momentum), and t_0 -> -E_n.
 d = 2 is used as the Euclidean proxy (one 'time', one 'space' axis); the formulas are
 dimension-blind.
"""
import numpy as np

m, sigma, alpha = 0.5, 0.6, 1.0
NMAX = 8
d = 2

def Bhat2(P):  # |B^(P)|^2, P[..., d] may be complex
    return np.exp(-sigma * np.sum(P * P, axis=-1))

def sums(k):
    """k: array [..., d] (complex allowed). Returns G(k), numerator vector N_mu(k)."""
    G = np.full(k.shape[:-1], 1.0 / alpha, dtype=complex)
    N = np.zeros(k.shape, dtype=complex)
    rng = np.arange(-NMAX, NMAX + 1)
    for n0 in rng:
        for n1 in rng:
            P = k + 2 * np.pi * np.array([n0, n1])
            w = Bhat2(P) / (np.sum(P * P, axis=-1) + m * m)
            G += w
            N += (1j * P) * w[..., None]
    return G, N

print("R2-1 perfect-action remnant check, d=%d, m=%.2f, sigma=%.2f, alpha=%.2f, NMAX=%d" % (d, m, sigma, alpha, NMAX))

# ---- 1. exactness on a periodic lattice
L = 16
ks = 2 * np.pi * np.fft.fftfreq(L)
K0, K1 = np.meshgrid(ks, ks, indexing="ij")
kk = np.stack([K0, K1], axis=-1)
G, N = sums(kk)
t = N / G[..., None]
Dinv = 1.0 / G
rngs = np.random.default_rng(1)
worst = 0.0
for trial in range(5):
    phi = rngs.normal(size=(L, L))
    ph = np.fft.fft2(phi)
    for mu in range(2):
        Tphi = np.fft.ifft2(t[..., mu] * ph)
        Dphi = np.fft.ifft2(Dinv * ph)
        val = np.sum(np.real(Dphi) * np.real(Tphi))  # Phi^T G^{-1} T Phi
        scale = np.sum(np.real(Dphi) ** 2) ** 0.5 * np.sum(np.real(Tphi) ** 2) ** 0.5
        worst = max(worst, abs(val) / scale)
print("1. exactness: max |Phi.G^-1.T Phi| / norms over 5 random Phi, mu=0,1: %.2e" % worst)
print("   (t_mu odd and imaginary, G even and real => T is G^-1-antisymmetric: exact symmetry)")
print("   t real part max: %.1e ; t odd: max|t(k)+t(-k)| = %.1e" % (
    np.max(np.abs(t.real)), np.max(np.abs(t + t[(-np.arange(L)) % L][:, (-np.arange(L)) % L]))))

# ---- 2. locality: couplings in x-space
L = 64
ks = 2 * np.pi * np.fft.fftfreq(L)
K0, K1 = np.meshgrid(ks, ks, indexing="ij")
kk = np.stack([K0, K1], axis=-1)
G, N = sums(kk)
t1 = N[..., 1] / G
Dinv = 1.0 / G
cD = np.real(np.fft.ifft2(Dinv))
ct = np.imag(np.fft.ifft2(t1))  # t1 is i*(real odd) -> coefficients real odd; take imag of ifft
ct = np.fft.ifft2(t1)
print("2. locality (x-space couplings along the axis x=(0,r) and diagonal):")
print("   r   |G^-1(0,r)|      |T_1(0,r)|      |T_1(r,r)|")
for r in [1, 2, 3, 4, 6, 8, 10, 12, 16, 20]:
    print("  %2d  %.3e      %.3e      %.3e" % (r, abs(cD[0, r]), abs(ct[0, r]), abs(ct[r, r])))
def rate(arr, rs):
    y = np.log(np.abs(np.array([arr[0, r] for r in rs])))
    return -np.polyfit(rs, y, 1)[0]
rs = np.arange(6, 18)
print("   fitted decay rate (per lattice unit) along axis: G^-1: %.3f, T_1: %.3f" % (rate(cD, rs), rate(ct, rs)))

# ---- 3. tower of poles and the remnant charge at each pole (60-digit contour integrals)
import mpmath as mp
mp.mp.dps = 60
print("3. tower: fixed real k_1, G has a pole in complex k_0 at k_0 = i E_n for EVERY n_1,")
print("   E_n = sqrt(m^2+(k_1+2 pi n_1)^2). Residues by 60-digit contour integrals (radius 1e-3):")
k1 = mp.mpf('0.7')
def GN(k0):
    G = mp.mpf(1) / alpha; N0 = mp.mpc(0); N1 = mp.mpc(0)
    for n0 in range(-NMAX, NMAX + 1):
        for n1 in range(-NMAX, NMAX + 1):
            P0 = k0 + 2 * mp.pi * n0; P1 = k1 + 2 * mp.pi * n1
            P2 = P0 * P0 + P1 * P1
            w = mp.exp(-sigma * P2) / (P2 + m * m)
            G += w; N0 += 1j * P0 * w; N1 += 1j * P1 * w
    return G, N0, N1
print("   n_1   E_n       Res G          Res N_1 / Res G      i(k1+2 pi n1)    Res N_0/Res G    -E_n")
for n1 in [0, 1, -1, 2]:
    En = mp.sqrt(m * m + (k1 + 2 * mp.pi * n1) ** 2)
    c = 1j * En; r = mp.mpf('1e-3'); M = 48
    rG = mp.mpc(0); rN0 = mp.mpc(0); rN1 = mp.mpc(0)
    for j in range(M):
        th = 2 * mp.pi * j / M; z = c + r * mp.expj(th); dz = 1j * r * mp.expj(th) * 2 * mp.pi / M
        G, N0, N1 = GN(z)
        rG += G * dz; rN0 += N0 * dz; rN1 += N1 * dz
    rG /= 2j * mp.pi; rN0 /= 2j * mp.pi; rN1 /= 2j * mp.pi
    print("   %+d  %8.4f  %s   %s   %+.6fi   %s   %+.6f" % (n1, float(En), mp.nstr(rG, 6), mp.nstr(rN1 / rG, 8),
          float(k1 + 2 * mp.pi * n1), mp.nstr(rN0 / rG, 8), -float(En)))
print("   exact residue of G at the n-th pole: e^{sigma m^2}/(2 i E_n): on shell P^2=-m^2, so the")
print("   O(d)-covariant Gaussian kernel does NOT suppress the alias states at all.")
print("   => one field per site, but a pole (one-particle state) for every n_1: the complete")
print("      reciprocal-lattice tower; the remnant translation acts on the n-th state as i(k_1+2 pi n_1)")
print("      and the time component as -E_n (energy): continuum momentum on the folded continuum.")
for Lam in [5, 10, 20, 40]:
    cnt = sum(1 for n1 in range(-100, 101) if np.sqrt(m * m + (0.7 + 2 * np.pi * n1) ** 2) < Lam)
    print("   poles with E_n < %3d at k_1=0.70: %d" % (Lam, cnt))
