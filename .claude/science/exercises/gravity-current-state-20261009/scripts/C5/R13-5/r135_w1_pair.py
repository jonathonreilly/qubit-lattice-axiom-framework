"""C5 R13-5 (a): first-order Ward (W1) completion of the PAIR-CREATING stress of a free real box scalar.

Matter: eps(k)^2 = m^2 + sum_i u(k_i), profiles G (gapped) and L (literal) of R8-2/R9-9 (box |k_i| <= B = 2).
Graviton divergence symbol (R9-9): D_j(q) = d(q_j) exp(i q_j/2), d = rho q + (1-rho) 2 sin(q/2), rho = 1 on |q|<=1, 0 on |q|>=2.5.
W1 (R8-2 convention), per channel:  omega_ch F^{0 nu} = sum_j D_j F^{j nu},  omega_ch = (created energy) - (destroyed energy).
  scattering a^dag_{k+q} a_k : omega = eps(k+q) - eps(k)   (R8-2 Construction A; not redone here)
  pair creation a^dag_{k1} a^dag_{k2}, k1 + k2 = q : omega = eps1 + eps2 >= 2m > 0
  pair annihilation (Hermitian conjugate, in T(-q)) : omega = -(eps1 + eps2)
COMPLETION (proved in the report): given ANY smooth symmetric spatial pair kernel F^{ij}(k1,k2),
  F^{0j} := sum_i D_i F^{ij} / omega,   F^{00} := sum_j D_j F^{0j} / omega.
Spatial members (vector w(k) replaces the continuum k in  T^{ij} = d_i phi d_j phi + delta_ij L ):
  F^{ij} = e^{-i(q_i+q_j)/2} [ -(w_i(k1) w_j(k2) + w_j(k1) w_i(k2)) + delta_ij(-eps1 eps2 + w(k1).w(k2) - m^2) ] / (2 sqrt(eps1 eps2))
  U : w = p = u'/2 (smooth, odd, p(pi) = 0 on both edges);   M : w = s with s^2 = u (smooth on L; on G s = sign(k) sqrt(u) jumps at the face)
Checks: (1) W1 residual both pair channels; (2) Hermiticity condition D(-q) = -D(q)^*; (3) on box pairs the completed time
components equal the continuum pi*grad(phi) kernels (box exactness kept); (4) F^{0 nu}_pair -> 0 as q -> 0 (so int T^00 = H);
(5) TT components at q || z are untouched: |V|^2 = 4 w_x^2 w_y^2 (T2g), (w_x^2-w_y^2)^2 (E_g); (6) locality: 2D Fourier decay of
F^{00}_pair(k1,k2) in d = 1 for U (G, L) and M (G: expected power-law because s_G jumps).
"""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r99_profiles_copy import profile, B, sstep, wrap, plateau, s_L

rng = np.random.default_rng(13505)

def dsym(q):
    qw = wrap(q); r = sstep((2.5 - np.abs(qw))/(2.5 - 1.0))
    return r*qw + (1-r)*2*np.sin(qw/2)

def Dsym(q):
    return dsym(q)*np.exp(1j*wrap(q)/2)

def wvec(member, name, k):
    u, up, upp = profile(name, k)
    if member == 'U':
        return up/2
    if name == 'L':
        return s_L(k)
    return np.sign(wrap(k))*np.sqrt(u)          # M on G: discontinuous at the face

def eps(name, m, k):                             # k shape (..., 3)
    u = sum(profile(name, k[..., i])[0] for i in range(k.shape[-1]))
    return np.sqrt(m*m + u)

def pair_kernel(member, name, m, k1, k2):
    """returns F (..., 4, 4) for pair creation a^dag_{k1} a^dag_{k2}, q = k1 + k2, plus omega and D."""
    d = k1.shape[-1]
    q = wrap(k1 + k2)
    e1, e2 = eps(name, m, k1), eps(name, m, k2)
    w1 = np.stack([wvec(member, name, k1[..., i]) for i in range(d)], -1)
    w2 = np.stack([wvec(member, name, k2[..., i]) for i in range(d)], -1)
    ph = np.exp(-1j*q/2)
    nrm = 2*np.sqrt(e1*e2)
    F = np.zeros(k1.shape[:-1] + (d+1, d+1), complex)
    tr = (-e1*e2 + np.sum(w1*w2, -1) - m*m)
    for i in range(d):
        for j in range(d):
            F[..., 1+i, 1+j] = ph[..., i]*ph[..., j]*(-(w1[..., i]*w2[..., j] + w1[..., j]*w2[..., i]) + (i == j)*tr)/nrm
    D = Dsym(q)
    om = e1 + e2
    for j in range(d):
        F[..., 0, 1+j] = np.sum(D*F[..., 1:, 1+j], -1)/om
        F[..., 1+j, 0] = F[..., 0, 1+j]
    F[..., 0, 0] = np.sum(D*F[..., 0, 1:], -1)/om
    return F, om, D, q, e1, e2

def w1_res(F, om, D):
    r = []
    for nu in range(F.shape[-1]):
        r.append(np.abs(om*F[..., 0, nu] - np.sum(D*F[..., 1:, nu], -1)))
    return np.max(r)

print('=== R13-5 (a): W1 completion of the pair-creating stress (d = 3) ===')
for name in ['G', 'L']:
    for member in (['U', 'M'] if name == 'L' else ['U', 'M']):
        for m in [1.0, 0.3]:
            n = 20000
            k1 = rng.uniform(-np.pi, np.pi, (n, 3)); k2 = rng.uniform(-np.pi, np.pi, (n, 3))
            F, om, D, q, e1, e2 = pair_kernel(member, name, m, k1, k2)
            res_c = w1_res(F, om, D)
            # annihilation channel = Hermitian conjugate in T(-q): omega -> -omega, D(-q) = -D(q)^*
            Fa = np.conj(F); Da = Dsym(-q); oma = -om
            res_a = w1_res(Fa, oma, Da)
            herm = np.max(np.abs(Dsym(-q) + np.conj(Dsym(q))))
            sym = np.max(np.abs(F - np.swapaxes(F, -1, -2)))
            # box pairs: compare with continuum kernels
            kb1 = rng.uniform(-1.5, 1.5, (n, 3)); kb2 = -kb1 + rng.uniform(-0.9, 0.9, (n, 3))
            ok = np.all(np.abs(kb2) <= 1.9, -1); kb1, kb2 = kb1[ok], kb2[ok]
            Fb, omb, Db, qb, b1, b2 = pair_kernel(member, name, m, kb1, kb2)
            ph = np.exp(-1j*qb/2)
            F0j_c = -(b1[:, None]*kb2 + b2[:, None]*kb1)/(2*np.sqrt(b1*b2))[:, None]*ph
            F00_c = -(np.sum(kb1*kb2, -1) + b1*b2 - m*m)/(2*np.sqrt(b1*b2))
            dev0 = max(np.max(np.abs(Fb[:, 0, 1:] - F0j_c)), np.max(np.abs(Fb[:, 0, 0] - F00_c)))
            # q -> 0 limit: k2 = -k1 + q, |q| = delta
            out = []
            for delta in [1e-2, 1e-3, 1e-4]:
                kk = rng.uniform(-np.pi, np.pi, (2000, 3)); qq = delta*rng.normal(size=(2000, 3))
                Fq, *_ = pair_kernel(member, name, m, kk, wrap(-kk + qq))
                out.append(np.max(np.abs(Fq[:, 0, :])))
            print('[%s %s m=%.1f] W1 residual: creation %.1e, annihilation %.1e | D(-q)+D(q)* %.1e | mu-nu symmetry %.1e | box pairs: |F^{0nu} - continuum| = %.1e (%d pairs) | max|F^{0nu}| at |q|=1e-2,1e-3,1e-4: %.1e %.1e %.1e'
                  % (name, member, m, res_c, res_a, herm, sym, dev0, ok.sum(), *out))
    # (5) TT components at q || z
    kx, ky, kz, qz = rng.uniform(-np.pi, np.pi, (4, 4000))
    k1 = np.stack([kx, ky, kz], -1); k2 = np.stack([-kx, -ky, wrap(-kz + qz)], -1)
    for member in ['U', 'M']:
        F, om, D, q, e1, e2 = pair_kernel(member, name, 1.0, k1, k2)
        wx, wy = wvec(member, name, kx), wvec(member, name, ky)
        V_T2 = F[:, 1, 2]*2*np.sqrt(e1*e2)*np.exp(1j*0)       # q_x = q_y = 0 -> no transverse phases
        V_E = (F[:, 1, 1] - F[:, 2, 2])*np.sqrt(e1*e2)
        print('   TT at q||z, %s: max| |V_T2g|^2 - 4 w_x^2 w_y^2 | = %.1e ; max| |V_Eg|^2 - (w_x^2-w_y^2)^2 | = %.1e  (completion does not touch TT)'
              % (member, np.max(np.abs(np.abs(V_T2)**2 - 4*wx**2*wy**2)), np.max(np.abs(np.abs(V_E)**2 - (wx**2-wy**2)**2))))

print('\n=== (6) locality, d = 1: Fourier coefficients of F^{00}_pair(k1,k2) on T^1 x T^1 (N = 512), max |c| at sup-distance r ===')
N = 512
k = 2*np.pi*(np.arange(N) - N//2)/N
K1, K2 = np.meshgrid(k, k, indexing='ij')
for name, member in [('G', 'U'), ('L', 'U'), ('L', 'M'), ('G', 'M')]:
    F, *_ = pair_kernel(member, name, 0.3, K1[..., None], K2[..., None])
    c = np.fft.fft2(F[..., 0, 0])/N**2
    idx = np.minimum(np.arange(N), N - np.arange(N))
    R = np.maximum(idx[:, None], idx[None, :])
    vals = [np.max(np.abs(c[R == r])) for r in [1, 10, 40, 100, 200]]
    print('  %s %s: r=1 %.1e | r=10 %.1e | r=40 %.1e | r=100 %.1e | r=200 %.1e' % (name, member, *vals))
