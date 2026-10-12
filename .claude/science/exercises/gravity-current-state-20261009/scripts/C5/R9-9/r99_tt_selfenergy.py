"""C5 R9-9 part C: one-loop TT self-energy of the box graviton from PAIR-CREATING box matter.

Matter: free real scalar field (KG) with eps(k)^2 = m^2 + sum_i u(k_i), u from r99_profiles (L, G, NN control).
Graviton: TT polarization with q along z:  T_2g (h_xy = h)  or  E_g (h_xx = -h_yy = h).
GR normalisation:  L = (M^2/4)(hdot^2 - (grad h)^2) - (1/2) Pi h^2  ->  (M^2/2)(w^2 - q^2) = Pi(w, q).
Vertices (TT, q along z), with |V_s|^2 a function of the TRANSVERSE pair momenta only:
  M ("metric", from sqrt(g) g^{ij} grad_i phi grad_j phi):  T_2g |V|^2 = 4 u_x u_y,    E_g |V|^2 = (u_x - u_y)^2
  U ("universal", forward value eps v_i v_j = R8-2's F^{ij}(k,k)): p = u'/2;  T_2g 4 p_x^2 p_y^2, E_g (p_x^2-p_y^2)^2
Paramagnetic one loop (per volume):  Pi_para(w,q) = -(1/4) <|V|^2/(eps eps') * E/(E^2 - w^2)>_k ,  eps' = eps(k_x,k_y,k_z-q), E = eps+eps'.
  beta  = dPi/d(w^2)  = -(1/32) <|V|^2/eps^5>
  alpha = dPi(0,q)/d(q^2)  (computed DIRECTLY by grid shifts + Richardson)
  Xi = alpha + beta  ->  c_T^2 - 1 = (2/M^2) Xi   (any q-independent, i.e. ultralocal, seagull drops out)
Identity tested here:  Xi = (1/32) < |V|^2 A_zz / eps^5 >,  A_zz = u''(k_z)/2 - 1  (R8-2's anomaly).
Also: metric-seagull TT mass anisotropy mu_E - mu_T2 (cosmological-constant independent), vertex M.
"""
import numpy as np, sys, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r99_profiles import profile, B
T0 = time.time()

def run(name, m, N):
    k = 2*np.pi*(np.arange(N) - N//2)/N
    u, up, upp = profile(name, k)
    p = up/2
    A = upp/2 - 1.0                               # A_zz as a function of k_z
    ux, uy, uz = u[:, None, None], u[None, :, None], u[None, None, :]
    px, py = p[:, None, None], p[None, :, None]
    e2 = m*m + ux + uy + uz
    eps = np.sqrt(e2)
    res = {}
    for vname, V2 in [('M,T2g', 4*ux*uy), ('M,Eg', (ux-uy)**2), ('U,T2g', 4*px**2*py**2), ('U,Eg', (px**2-py**2)**2)]:
        V2b = np.broadcast_to(V2, eps.shape)
        beta = -(1/32)*np.mean(V2b/eps**5)
        def Pi0(n):                               # static Pi at q = n * 2pi/N (exact grid shift along z)
            epsp = np.roll(eps, n, axis=2)        # eps(k_z - q)
            return -0.25*np.mean(V2b/(eps*epsp*(eps+epsp)))
        dq = 2*np.pi/N
        P0, P1, P2 = Pi0(0), Pi0(1), Pi0(2)
        alpha = (16*(P1-P0) - (P2-P0))/(12*dq*dq)
        Xi_direct = alpha + beta
        Xi_formula = (1/32)*np.mean(V2b*A[None, None, :]/eps**5)
        box = (np.abs(k) <= B - 1e-9)
        Xi_boxpart = (1/32)*np.mean((V2b*A[None, None, :]/eps**5)[:, :, box])*box.mean()
        res[vname] = (alpha, beta, Xi_direct, Xi_formula, Xi_boxpart)
    # metric-seagull TT masses (vertex M): seagull = (1/4)<(2u_x+2u_y)/eps> for both channels (ultralocal)
    sg = 0.25*np.mean((2*ux+2*uy)/eps + 0*uz)
    muT2 = sg - 0.125*np.mean(np.broadcast_to(4*ux*uy, eps.shape)/eps**3)
    muE = sg - 0.125*np.mean(np.broadcast_to((ux-uy)**2, eps.shape)/eps**3)
    # split of the anisotropy into box (all |k_i|<=B) and the rest
    integrand = -0.125*np.broadcast_to(ux**2+uy**2-6*ux*uy, eps.shape)/eps**3
    allbox = (np.abs(k)[:, None, None] <= B) & (np.abs(k)[None, :, None] <= B) & (np.abs(k)[None, None, :] <= B)
    dmu_box = np.sum(integrand*allbox)/integrand.size
    return res, muE, muT2, dmu_box

def IB(name, Bv, n=20001):
    """I(B) = int dk_z A_zz(k_z) (B + u(k_z))^{-5/2} over the zone (trapezoid, periodic)."""
    k = np.linspace(-np.pi, np.pi, n)[:-1]
    u, up, upp = profile(name, k)
    return np.sum((upp/2-1)/(Bv+u)**2.5)*(2*np.pi/len(k))

print('=== C5 R9-9 (C): TT self-energy from pair-creating box matter (free KG field) ===')
print('Xi = alpha + beta (lattice units, per scalar species);  c_T^2 - 1 = (2/M^2) Xi = 16 pi Xi (l_P/a)^2 (reduced-Planck GR normalisation)')
for name in ['NN', 'G', 'L']:
    for m in [1.0, 0.3]:
        for N in [64, 128]:
            if name == 'NN' and m == 0.3 and N == 64: continue
            res, muE, muT2, dmu_box = run(name, m, N)
            print('[%s, m=%.1f, N=%d]  (%.0fs)' % (name, m, N, time.time()-T0))
            for vn, (al, be, xd, xf, xb) in res.items():
                print('   %-6s alpha=%+.6e beta=%+.6e | Xi direct=%+.6e  formula <|V|^2 A_zz/eps^5>/32=%+.6e  (diff %.1e) | box(|k_z|<=B) part=%+.1e'
                      % (vn, al, be, xd, xf, xd-xf, xb))
            print('   metric seagull: mu_T2=%+.6e mu_E=%+.6e  mu_E-mu_T2=%+.6e (all-box part %+.3e)' % (muT2, muE, muE-muT2, dmu_box))
print('\n=== sign of I(B) = int A_zz (B+u)^{-5/2} dk_z over B in [m^2, m^2+2 max u] (weights of every TT vertex with |V|^2>=0) ===')
for name in ['NN', 'G', 'L']:
    k = np.linspace(-np.pi, np.pi, 4001)[:-1]
    u, up, upp = profile(name, k)
    Amax = (upp/2-1).max(); Amin = (upp/2-1).min()
    for m in [1.0, 0.3]:
        Bs = np.linspace(m*m, m*m + 2*u.max(), 60)
        I = np.array([IB(name, b) for b in Bs])
        print('  %-2s m=%.1f: A_zz range on zone [%+.3f, %+.3f]; I(B) range [%+.4e, %+.4e]; sign-definite: %s'
              % (name, m, Amin, Amax, I.min(), I.max(), bool(I.max() < 0 or I.min() > 0)))
print('done %.0fs' % (time.time()-T0))
