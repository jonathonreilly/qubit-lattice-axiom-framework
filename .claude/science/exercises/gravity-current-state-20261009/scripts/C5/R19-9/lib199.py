"""R19-9 library: exact W1 completion of the VW photon stress (field basis), glued from three exactly conserved pieces.

Conventions (stated; checked numerically in r199_exact.py):
 * Photon in R17-12's rotated frame (photon.py docstring): continuum Maxwell with momentum vector sigma(k) (antiperiodic).
   Field basis psi(k) = (E(k), B(k)) in C^6, i d/dt psi = h psi, h = [[0, -X],[X, 0]], X v = sigma x v.
 * Stress bilinear T^{mu nu}(q) = sum psi(k1)^dag M^{mu nu}(k1,k2) psi(k2), q = k1 - k2.
 * Graviton (R9-9): D_j(q) = dsym(q_j) e^{i q_j/2}. With T^{0j} placed at the j-link and T^{ij} at (i+j)/2 relative to T^{00},
   the phases cancel (T^{mu nu} = e^{-i q.p_{mu nu}} T~^{mu nu}); in the tilde variables W1 reads
      h(k1) M^{0nu} - M^{0nu} h(k2) = sum_j d_j(q) M^{j nu},  d_j(q) = dsym(q_j)  (real, odd),
   with (H-sym) M^{j0} = M^{0j}. Only the physical (transverse, Gauss-law) block P_T(k1) . P_T(k2) is required.
 * Spatial kernel M^{ij}: SIGN * blockdiag(ME, MB) of R18-13's VWa-geo vertex (generalized here: P, u_d, u_o passed as arrays),
   for the unit symmetric polarization of component ij. SIGN fixed by the continuum W1 check (momentum flux = -Maxwell stress).
Pieces:
   M_C : continuum Maxwell stress (c = 1, P = 1, u = 1; T00 = (E^2+B^2)/2, T0j = Poynting), valid where sigma = k and d = q.
   M_B : channel split (both legs hard): scattering blocks = R8-2 dust kernel g^mu g^nu M00_sc with 1D divided differences;
         pair blocks = VW spatial pair blocks + R13-5 P1 time components (division by w1 + w2).
   M_A : single soft leg: VW spatial kernel in all channels, time components by Sylvester inversion on (full x T2) (left soft)
         or (T1 x full) (right soft); off the scattering shell this is the unique physical solution, and on the full-left
         side it is the analytic Neumann series in h(k1) (smooth through k1 = 0).
 Glue: M = chiC M_C + (1 - chiC)[phiA(|k1|) M_A^L + phiA(|k2|) M_A^R + (1 - phiA(|k1|) - phiA(|k2|)) M_B],
   chiC = phi(|k1|/r) phi(|k2|/r), phi = 1 on [0, 1/2], 0 on [1, inf), C^infty;  phiA(x) = phi(8x/r) (1 below r/16... 0 above r/8).
"""
import os, sys, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'arch18')); sys.path.insert(0, os.path.join(HERE, 'arch18_13'))
sys.path.insert(0, os.path.join(HERE, 'arch99'))
from photon import photonGw, crossmat
from r99_profiles import sstep, wrap, plateau

BG = 2.9435; LAW = photonGw(BG, np.pi - BG)            # R18-9 / R18-13 root photon edge gammaGw(2.9435, 0.198093)
A_R = -0.176095005436                                   # vR18-9 retuned a
WD_R, WO_R = -1.171554, -0.195418                       # R18-13 N = 224 own-direction solve
SIGN = -1.0                                             # fixed by the continuum check (see r199_exact.out)

def dsym(q):                                            # R9-9 r99_graviton.dsym (copied verbatim in form)
    q = wrap(q); r = plateau(q, 1.0, 2.5)
    return r*q + (1-r)*2*np.sin(q/2)

def phi(x):                                             # C^infty: 1 on [0, 1/2], 0 on [1, inf)
    return 1.0 - sstep(2.0*np.asarray(x, float) - 1.0)

_DB = LAW.d(np.array([BG]))[0]
def sig(k):
    """sigma(k) = sgn(k) d(|k|) with d(x) = x EXACTLY on the box |x| <= b (the law's definition; the archived tabulation
    reproduces it only to ~1e-12 relative), and the archived tabulated increment beyond b."""
    k = np.asarray(k, float); ak = np.abs(k)
    return np.sign(k)*np.where(ak <= BG, ak, LAW.d(ak) - _DB + BG)
def cfun(k): return LAW.c(k)
def omega(k): return np.sqrt((sig(k)**2).sum(-1))

def hmat(s):
    X = crossmat(s); Z = np.zeros((3, 3))
    return np.block([[Z, -X], [X, Z]])

def projs(k):
    s = sig(k); w = np.sqrt(s @ s); h = hmat(s); h2 = h @ h
    Pp = (h2 + w*h)/(2*w*w); Pm = (h2 - w*h)/(2*w*w); PT = h2/(w*w); P0 = np.eye(6) - PT
    return h, w, Pp, Pm, PT, P0

def Pstencil(s, a): return (1.0 - a)*np.cos(0.5*s) + a*np.cos(1.5*s)
def ustencil(s, w): return (1.0 - w) + w*np.cos(s)

def vertex(e, c1, c2, P, ud, uo):
    """R18-13 vertex_geo with the per-axis placement P and own-direction u_d, u_o given as arrays (shape (3,))."""
    ME = np.zeros((3, 3)); MB = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            if e[i, j] == 0: continue
            if i != j:
                k = 3 - i - j; U = e[i, j]*uo[i]*uo[j]
                ME[i, j] += U*c1[i]*c2[j]; MB[i, j] += U*c1[j]*c2[i]*P[k]
            else:
                U = e[i, i]*ud[i]; cc = c1[i]*c2[i]; oth = [x for x in range(3) if x != i]
                ME[i, i] += 0.5*U*cc; MB[i, i] += 0.5*U*cc*P[oth[0]]*P[oth[1]]
                for aa in oth:
                    third = 3 - aa - i
                    ME[aa, aa] += -0.5*U*cc*P[aa]; MB[aa, aa] += -0.5*U*cc*P[third]
    return ME, MB

EIJ = {}
for i in range(3):
    for j in range(3):
        e = np.zeros((3, 3)); e[i, j] += 0.5; e[j, i] += 0.5; EIJ[(i, j)] = e   # component T_ij (symmetric)

def spatial_VW(k1, k2, a=A_R, wd=WD_R, wo=WO_R):
    s = k1 - k2; c1, c2 = cfun(k1), cfun(k2)
    P = Pstencil(s, a); ud = ustencil(s, wd); uo = ustencil(s, wo)
    M = np.zeros((3, 3, 6, 6))
    for i in range(3):
        for j in range(3):
            ME, MB = vertex(EIJ[(i, j)], c1, c2, P, ud, uo)
            M[i, j, :3, :3] = SIGN*ME; M[i, j, 3:, 3:] = SIGN*MB
    return M

def continuum(k1, k2):
    """M_C^{mu nu}, 4x4 of 6x6: T00 = (E^2 + B^2)/2, T0j = (E x B)_j, Tij = SIGN*[E_iE_j + B_iB_j - delta (E^2+B^2)/2]."""
    one = np.ones(3)
    M = np.zeros((4, 4, 6, 6))
    for i in range(3):
        for j in range(3):
            ME, MB = vertex(EIJ[(i, j)], one, one, one, one, one)
            M[1+i, 1+j, :3, :3] = SIGN*ME; M[1+i, 1+j, 3:, 3:] = SIGN*MB
    M[0, 0] = 0.5*np.eye(6)
    for j in range(3):
        for a_ in range(3):
            for b_ in range(3):
                eps = np.linalg.det(np.eye(3)[[j, a_, b_]])
                if eps != 0:
                    M[0, 1+j, a_, 3+b_] += 0.5*eps; M[0, 1+j, 3+b_, a_] += 0.5*eps
        M[1+j, 0] = M[0, 1+j]
    return M

def divdiff(k1, k2):
    """Delta_j = (sigma_j(k1)^2 - sigma_j(k2)^2)/d(k1_j - k2_j), removable limit 2 sigma sigma'(kbar)/d'(0) (d'(0) = 1)."""
    s1, s2 = sig(k1), sig(k2); q = wrap(k1 - k2); d = dsym(q)
    out = np.empty(3)
    for j in range(3):
        if abs(q[j]) > 1e-7:
            out[j] = (s1[j]**2 - s2[j]**2)/d[j]
        else:
            kb = k2[j] + 0.5*q[j]
            out[j] = 2*sig(np.array([kb]))[0]*cfun(np.array([kb]))[0]
    return out

def fiber_id(k1, k2):
    """covariant, smooth identification of the leg fibres in the rotated frame (s = k1 - k2): E_a -> cos(s_a/2),
    B_a -> prod_{b != a} cos(s_b/2). Equal to 1 at s = 0 (so (H-E) holds); antiperiodic exactly as the twist requires."""
    c = np.cos(0.5*(k1 - k2))
    return np.diag(np.r_[c, c[1]*c[2], c[0]*c[2], c[0]*c[1]])

def piece_B(k1, k2, Msp):
    """both legs hard. Msp: VW spatial (3,3,6,6) in all blocks; only its pair blocks are kept."""
    h1, w1, Pp1, Pm1, PT1, _ = projs(k1); h2, w2, Pp2, Pm2, PT2, _ = projs(k2)
    d = dsym(wrap(k1 - k2)); W = w1 + w2
    g = np.r_[1.0, divdiff(k1, k2)/W]
    I12 = fiber_id(k1, k2)
    Spp = 0.5*Pp1 @ I12 @ Pp2; Smm = 0.5*Pm1 @ I12 @ Pm2
    M = np.zeros((4, 4, 6, 6), complex)
    for mu in range(4):
        for nu in range(4):
            sgn = 1.0 if (mu == 0) == (nu == 0) else -1.0     # g^mu g^nu with the -- block sign (-1)^{#time indices}
            M[mu, nu] = g[mu]*g[nu]*(Spp + sgn*Smm) if True else 0
    # pair blocks: +- (lambda1 - lambda2 = +W), -+ (= -W)
    for (L, R, lam) in ((Pp1, Pm2, W), (Pm1, Pp2, -W)):
        Sij = np.einsum('ab,ijbc,cd->ijad', L, Msp, R)
        S0j = np.einsum('i,ijab->jab', d, Sij)/lam
        S00 = np.einsum('j,jab->ab', d, S0j)/lam
        M[1:, 1:] += Sij; M[0, 1:] += S0j; M[1:, 0] += S0j; M[0, 0] += S00
    return M

def sylv(R, k1, k2, left_full):
    """solve h1 X - X h2 = R on (full x T2) if left_full else (T1 x full), off the shell (eigen-sum)."""
    h1, w1, Pp1, Pm1, PT1, P01 = projs(k1); h2, w2, Pp2, Pm2, PT2, P02 = projs(k2)
    L = [(Pp1, w1), (Pm1, -w1)] + ([(P01, 0.0)] if left_full else [])
    Rr = [(Pp2, w2), (Pm2, -w2)] + ([] if left_full else [(P02, 0.0)])
    X = np.zeros((6, 6), complex)
    for (A, la) in L:
        for (B, lb) in Rr:
            X += A @ R @ B/(la - lb)
    return X

def neumann_left(R, k1, k2, nmax=200):
    """same solution on (full x T2) as an analytic series in h(k1): X = -sum_n h1^n R (h2^+)^{n+1}; needs w1 < w2."""
    s1 = sig(k1); h1 = hmat(s1); h2, w2, Pp2, Pm2, PT2, _ = projs(k2)
    hp = (Pp2 - Pm2)/w2
    X = np.zeros((6, 6), complex); T = R @ hp
    for n in range(nmax):
        X -= T
        T = h1 @ T @ hp
        if np.abs(T).max() < 1e-300: break
    return X

def piece_A(k1, k2, Msp, left_full, series=False):
    d = dsym(wrap(k1 - k2))
    M = np.zeros((4, 4, 6, 6), complex); M[1:, 1:] = Msp
    solve = (lambda R: neumann_left(R, k1, k2)) if (series and left_full) else (lambda R: sylv(R, k1, k2, left_full))
    for j in range(3):
        R = np.einsum('i,iab->ab', d, Msp[:, j]); M[0, 1+j] = solve(R); M[1+j, 0] = M[0, 1+j]
    R = np.einsum('j,jab->ab', d, M[0, 1:]); M[0, 0] = solve(R)
    return M

def glued(k1, k2, r, a=A_R, wd=WD_R, wo=WO_R, parts=False):
    n1, n2 = np.linalg.norm(wrap(k1)), np.linalg.norm(wrap(k2))
    cC = float(phi(n1/r)*phi(n2/r)); f1 = float(phi(8*n1/r)); f2 = float(phi(8*n2/r))
    M = np.zeros((4, 4, 6, 6), complex); used = []
    if cC > 0:
        M += cC*continuum(k1, k2); used.append('C')
    if cC < 1:
        Msp = spatial_VW(k1, k2, a, wd, wo)
        if f1 > 0: M += (1-cC)*f1*piece_A(k1, k2, Msp, True); used.append('AL')
        if f2 > 0: M += (1-cC)*f2*piece_A(k1, k2, Msp, False); used.append('AR')
        fB = 1 - f1 - f2
        if fB > 0: M += (1-cC)*fB*piece_B(k1, k2, Msp); used.append('B')
    return (M, used, (cC, f1, f2)) if parts else M

def w1_resid(M, k1, k2, dfun=None):
    """physical-block residuals of h1 M^{0nu} - M^{0nu} h2 - sum_j d_j M^{j nu}, nu = 0..3 (abs, and relative to term size)."""
    h1, w1, Pp1, Pm1, PT1, _ = projs(k1); h2, w2, Pp2, Pm2, PT2, _ = projs(k2)
    d = dsym(wrap(k1 - k2)) if dfun is None else dfun(k1, k2)
    out = []
    for nu in range(4):
        lhs = h1 @ M[0, nu] - M[0, nu] @ h2; rhs = np.einsum('j,jab->ab', d, M[1:, nu])
        res = PT1 @ (lhs - rhs) @ PT2
        scale = max(np.abs(PT1 @ h1 @ M[0, nu] @ PT2).max() + np.abs(PT1 @ M[0, nu] @ h2 @ PT2).max()
                    + sum(abs(d[j])*np.abs(PT1 @ M[1+j, nu] @ PT2).max() for j in range(3)), 1e-300)
        out.append((np.abs(res).max(), np.abs(res).max()/scale))   # relative to the size of the terms that cancel
    return out
