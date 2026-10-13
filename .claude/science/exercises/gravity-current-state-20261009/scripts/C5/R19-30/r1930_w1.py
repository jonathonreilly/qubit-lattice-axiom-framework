"""R19-30 probe (d): W1 after the re-placement, with the completions of R19-5 rebuilt around the re-placed pair kernels.
Dirac: R19-5's construction (r195copy/r195_dirac_exact.py `near`, and `far`/`glued` copied verbatim from
r195_dirac_exact2.py) run on the ANALYTIC D1 law (lib1930.Dirac passed as R19-5's `law`), with R19-5's own pair block
switched off (UD -> 0) and replaced by the re-placed pair kernel
   G^{ij} = e^{-iq.p_ij} [P+(k1) X^{ij} P-(k2) + P-(k1) X^{ij} P+(k2)],  X^{ij} = parity-resolved re-placed UD(kbar),
with R19-5's P1 time components  M^{0i} = +-sum_j D_j M^{ji}/(E1+E2),  M^{00} = +-sum_j D_j M^{0j}/(E1+E2).
Scalar: R13-5's P1 (r135_w1_pair.py formula) on (a) R13-5's per-leg U with F(q_i)F(q_j) and (b) the E1 midpoint U with
the parity-resolved re-placement (+ R13-5's per-leg trace part on the diagonal).
Residuals are max-abs over all nu = 0..3 and all four blocks.  Also: Fourier tails of the completed TIME components."""
import sys, os, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'r195copy'))
import lib1930 as L
import r195_dirac_exact as R5
from r99_profiles import plateau
t0 = time.time()
m = 0.01
DI = L.Dirac(m=m); SC = L.Scalar(m=m)
band = R5.Band(DI, m)                       # R19-5's Band on the analytic law
_UD0 = R5.UD
R5.UD = lambda band, k, i, j: np.zeros((4, 4), complex)     # switch R19-5's own pair block off (scattering only)

C1, C2 = 1.0, 2.5                           # ---- copied verbatim from r195_dirac_exact2.py ----
def dsym(q):
    q = L.wrap(q); r = plateau(q, C1, C2); return r*q + (1-r)*2*np.sin(q/2)
def Dfull(q): q = L.wrap(np.asarray(q, float)); return dsym(q)*np.exp(0.5j*q)
def far(band, k2, q):
    k1 = k2 + q; D = Dfull(q); Dc = D.conj(); n2 = (np.abs(D)**2).sum()
    E1, E2 = band.E(k1), band.E(k2)
    Pp1, Pm1, Pp2, Pm2 = band.proj(k1, 1), band.proj(k1, -1), band.proj(k2, 1), band.proj(k2, -1)
    M = [[np.zeros((4, 4), complex) for _ in range(4)] for _ in range(4)]
    for sgn, Pa, Pb in ((1, Pp1, Pp2), (-1, Pm1, Pm2)):
        PP = Pa @ Pb; w = sgn*(E1 - E2)
        M00 = sgn*0.5*(E1 + E2)*PP
        M0 = [Dc[j]*w*M00/n2 for j in range(3)]
        V = [w*M0[i] for i in range(3)]
        DV = sum(D[l]*V[l] for l in range(3))
        M[0][0] += M00
        for i in range(3):
            M[0][i+1] += M0[i]
            for j in range(3):
                M[i+1][j+1] += (V[i]*Dc[j] + Dc[i]*V[j])/n2 - DV*Dc[i]*Dc[j]/n2**2
    for j in range(1, 4): M[j][0] = M[0][j]
    return M
def glued(band, k2, q):
    qi = np.abs(L.wrap(np.asarray(q, float))).max()
    chi = float(plateau(np.array([qi]), 0.5, 0.9)[0])
    if chi == 0.0: return far(band, k2, q)
    Mn = R5.near(band, k2, L.wrap(np.asarray(q, float)))
    if chi == 1.0: return Mn
    Mf = far(band, k2, q)
    return [[chi*Mn[a][b] + (1-chi)*Mf[a][b] for b in range(4)] for a in range(4)]
# ---- end of copy ----

def pair_block(k2, q, mode='PR', conv='rows'):
    """re-placed pair kernel with P1 time components (site-label), as 4x4 list of 4x4."""
    k1 = k2 + q; qw = L.wrap(q); kb = k2 + qw/2
    D = Dfull(q); E1, E2 = band.E(k1), band.E(k2)
    Pp1, Pm1, Pp2, Pm2 = band.proj(k1, 1), band.proj(k1, -1), band.proj(k2, 1), band.proj(k2, -1)
    X = {}
    for i in range(3):
        for j in range(i, 3):
            c = L.tilde_component(lambda kk: DI.UDcoef(kk, i, j), kb[None, :], qw[None, :], i, j, mode)[0]
            ph = L.place_phase(qw[None, :], i, j)[0] if conv == 'rows' else 1.0
            X[(i, j)] = X[(j, i)] = ph*np.einsum('a,aij->ij', c, L.GAM)
    M = [[np.zeros((4, 4), complex) for _ in range(4)] for _ in range(4)]
    for sgn, Pa, Pb in ((1, Pp1, Pm2), (-1, Pm1, Pp2)):
        Mij = [[Pa @ X[(i, j)] @ Pb for j in range(3)] for i in range(3)]
        M0i = [sgn*sum(D[j]*Mij[j][i] for j in range(3))/(E1 + E2) for i in range(3)]
        M[0][0] += sgn*sum(D[j]*M0i[j] for j in range(3))/(E1 + E2)
        for i in range(3):
            M[0][i+1] += M0i[i]; M[i+1][0] += M0i[i]
            for j in range(3): M[i+1][j+1] += Mij[i][j]
    return M

def full(k2, q, mode='PR'):
    S = glued(band, k2, q); P = pair_block(k2, q, mode)
    return [[S[a][b] + P[a][b] for b in range(4)] for a in range(4)]

rng = np.random.default_rng(193004)
print('R19-30 (d) W1 after the re-placement; analytic D1(%.9f, %.9f), m = %g' % (DI.b, DI.r, m))
for label, gen in (('generic, |q|_inf in (0.05, pi)', lambda: (rng.uniform(-np.pi, np.pi, 3), rng.uniform(-1, 1, 3)*rng.choice([0.6, 1.0, 3.1]))),
                   ('near region |q_j| <= 0.5, no zero component', lambda: (rng.uniform(-np.pi, np.pi, 3), rng.uniform(0.01, 0.5, 3)*rng.choice([-1, 1], 3))),
                   ('at the cut, q_x = pi - 1e-9', lambda: (rng.uniform(-np.pi, np.pi, 3), np.array([np.pi - 1e-9, *rng.uniform(-np.pi, np.pi, 2)]))),
                   ('at the cut, q_x = -pi + 1e-9', lambda: (rng.uniform(-np.pi, np.pi, 3), np.array([-np.pi + 1e-9, *rng.uniform(-np.pi, np.pi, 2)])))):
    rmax = smax = 0.0; n = 0
    for t in range(150):
        k2, q = gen()
        if np.abs(L.wrap(q)).min() < 1e-6 and np.abs(L.wrap(q)).max() < 0.9: continue    # R19-5 near-chart planes (vR19-5 item 4)
        M = full(k2, q)
        r, s = R5.residual(band, M, k2, q, Dfull); rmax = max(rmax, r); smax = max(smax, s); n += 1
    print('  Dirac full kernel (R19-5 scattering + re-placed pair, PR): %-45s n=%3d  W1 max %.2e  mu-nu symmetry %.2e' % (label, n, rmax, smax), flush=True)

# pair block alone at the cut from both sides: continuity of the completed TIME components (site-label)
jm = 0.0; sz = 0.0
for t in range(100):
    k2 = rng.uniform(-np.pi, np.pi, 3); qo = rng.uniform(-np.pi, np.pi, 3); l = t % 3
    qa, qb = qo.copy(), qo.copy(); qa[l] = np.pi - 1e-8; qb[l] = -np.pi + 1e-8
    Pa, Pb = pair_block(k2, qa), pair_block(k2, qb)
    for a in range(4):
        jm = max(jm, np.abs(Pa[0][a] - Pb[0][a]).max()); sz = max(sz, np.abs(Pa[0][a]).max())
print('  Dirac pair block, time components M^{0nu} across q_l = +-pi (eps = 1e-8): max jump %.2e (|M^{0nu}| up to %.2f)' % (jm, sz))
# Fourier tail of a completed time component along a full k1_x line (convention-free locality of M^{0x}, M^{00})
N = 2048; r2 = np.random.default_rng(7); k2 = r2.uniform(-np.pi, np.pi, 3); k1o = r2.uniform(-np.pi, np.pi, 3)
for conv_mode, lab in ((('PR', 'rows'), 'PR re-placed'), (('raw', 'rows'), 'raw UD at R9-9 placement')):
    g = []
    for tt in 2*np.pi*np.arange(N)/N - np.pi:
        k1 = k1o.copy(); k1[0] = tt; P = pair_block(k2, k1 - k2, *conv_mode)
        g.append(np.concatenate([P[0][1].ravel(), P[0][0].ravel()]))
    c = np.abs(np.fft.fft(np.array(g), axis=0)).max(1)/N; idx = np.minimum(np.arange(N), N - np.arange(N))
    print('  Dirac M^{0x}, M^{00} (%s) Fourier max|c_n| n=[32,64) %.1e [128,256) %.1e [512,1024) %.1e' % (lab, *[c[(idx >= a) & (idx < b)].max() for a, b in ((32, 64), (128, 256), (512, 1024))]), flush=True)

# ---------------- scalar: R13-5's P1 on the re-placed kernels ------------------------------------------------------
def Dsym(q): return dsym(q)*np.exp(0.5j*L.wrap(q))
def scal_F(kind, k1, k2):
    q = L.wrap(k1 + k2); e1, e2 = SC.eps(k1), SC.eps(k2); nrm = 2*np.sqrt(e1*e2)
    w1, w2 = SC.f(k1), SC.f(k2)
    F = np.zeros(k1.shape[:-1] + (4, 4), complex)
    tr = -e1*e2 + (w1*w2).sum(-1) - m*m
    for i in range(3):
        for j in range(3):
            if kind == 'Upl':
                t = -(w1[..., i]*w2[..., j] + w1[..., j]*w2[..., i])/nrm
                if i != j: t = t*L.Fplace(q[..., i])*L.Fplace(q[..., j])
            else:
                K = k1 - q/2
                t = 2*L.tilde_component(lambda kb: (SC.f(kb[..., i])*SC.f(kb[..., j]))[..., None], K, q, i, j, 'PR')[..., 0]/nrm
            if i == j: t = t + tr/nrm
            F[..., 1+i, 1+j] = L.place_phase(q, i, j)*t
    D = Dsym(q); om = e1 + e2
    for j in range(3):
        F[..., 0, 1+j] = np.sum(D*F[..., 1:, 1+j], -1)/om; F[..., 1+j, 0] = F[..., 0, 1+j]
    F[..., 0, 0] = np.sum(D*F[..., 0, 1:], -1)/om
    return F, om, D
for kind in ('Upl', 'E1'):
    k1 = rng.uniform(-np.pi, np.pi, (4000, 3)); k2 = rng.uniform(-np.pi, np.pi, (4000, 3))
    F, om, D = scal_F(kind, k1, k2)
    rc = max(np.abs(om*F[..., 0, nu] - np.sum(D*F[..., 1:, nu], -1)).max() for nu in range(4))
    ra = max(np.abs(-om*np.conj(F[..., 0, nu]) - np.sum(Dsym(-L.wrap(k1 + k2))*np.conj(F[..., 1:, nu]), -1)).max() for nu in range(4))
    # Fourier tail of F^{00} along a k1_x line (pair channel), both time components inherit locality
    N = 4096; tt = 2*np.pi*np.arange(N)/N - np.pi; kk2 = np.tile(np.array([0.41, -1.3, 2.2]), (N, 1))
    kk1 = np.tile(np.array([0.0, 0.77, -0.4]), (N, 1)); kk1[:, 0] = tt
    Fl, *_ = scal_F(kind, kk1, kk2); g = Fl[..., 0, :].reshape(N, -1)
    c = np.abs(np.fft.fft(g, axis=0)).max(1)/N; idx = np.minimum(np.arange(N), N - np.arange(N))
    print('  scalar %-4s (%s): P1 W1 residual creation %.2e annihilation %.2e (4000 random pairs, whole torus) | F^{0nu} Fourier n=[128,256) %.1e [1024,2048) %.1e'
          % (kind, 'F(q_i)F(q_j)' if kind == 'Upl' else 'parity-resolved', rc, ra, c[(idx >= 128) & (idx < 256)].max(), c[(idx >= 1024) & (idx < 2048)].max()))
print('time %.1f s' % (time.time() - t0))
