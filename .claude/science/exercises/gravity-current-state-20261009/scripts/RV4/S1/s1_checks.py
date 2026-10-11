"""RV4 probe S1: numerical checks for the shear-term theorems.

Conventions (RN-L1 normalization, as P1):
  bulk-flow coupling, flow velocity v = (1/2) h grad u, u = omega^2/2 (P = energy current => p = grad u)
  mu_h = -< grad eps . v (div v) >_BZ = -(1/8) < (grad u . h grad u)(h : Hess u) / omega >   (bosons, eps = omega/2)
  E channel  h = diag(1,-1,0);  T2 channel h_xy = h_yx = 1  (equal Frobenius norm)
"""
import numpy as np
from scipy.optimize import fsolve
from numpy.polynomial.legendre import leggauss

np.set_printoptions(precision=10)

def grid(N, d=3):
    k = 2*np.pi*(np.arange(N)+0.5)/N - np.pi   # midpoint periodic grid (spectral for analytic periodic integrands)
    return np.meshgrid(*([k]*d), indexing='ij')

# ---------------------------------------------------------------- family of cubic symbols
# u = m^2/2 + sum_i c_i + a sum_i c_i^2 + b sum_{i<j} c_i c_j + g * (1 - cos x cos y cos z)  - g*0, c = 1 - cos k
# (g term = body-diagonal hopping; IR: 1 - cos x cos y cos z ~ k^2/2, so the IR normalization is (1+g) k^2/2;
#  we divide the kinetic part by (1+g) to keep u ~ k^2/2.)
def symbol(K, a=0.0, b=0.0, g=0.0):
    x, y, z = K
    s = [np.sin(x), np.sin(y), np.sin(z)]
    co = [np.cos(x), np.cos(y), np.cos(z)]
    c = [1-co[0], 1-co[1], 1-co[2]]
    P = co[0]*co[1]*co[2]
    u = c[0]+c[1]+c[2] + a*(c[0]**2+c[1]**2+c[2]**2) + b*(c[0]*c[1]+c[1]*c[2]+c[0]*c[2]) + g*(1-P)
    gu = []
    for i in range(3):
        j, l = [q for q in range(3) if q != i]
        gi = s[i]*(1 + 2*a*c[i] + b*(c[j]+c[l])) + g*s[i]*co[j]*co[l]
        gu.append(gi)
    H = [[None]*3 for _ in range(3)]
    for i in range(3):
        j, l = [q for q in range(3) if q != i]
        H[i][i] = co[i]*(1 + 2*a*c[i] + b*(c[j]+c[l])) + 2*a*s[i]**2 + g*P
        for j2 in range(3):
            if j2 != i:
                l2 = 3 - i - j2
                H[i][j2] = b*s[i]*s[j2] - g*s[i]*s[j2]*co[l2]
    nrm = 1.0 + g
    u = u/nrm; gu = [q/nrm for q in gu]; H = [[q/nrm for q in row] for row in H]
    return u, gu, H

def mu_channels(m, N=64, a=0.0, b=0.0, g=0.0, fermion=False):
    K = grid(N)
    u, gu, H = symbol(K, a, b, g)
    om = np.sqrt(m*m + 2*u)
    # E: h = diag(1,-1,0)
    phiE = gu[0]**2 - gu[1]**2
    psiE = H[0][0] - H[1][1]
    # T2: h_xy = h_yx = 1
    phiT = 2*gu[0]*gu[1]
    psiT = 2*H[0][1]
    sgn = -1.0 if fermion else 1.0
    muE = -sgn*np.mean(phiE*psiE/om)/8
    muT = -sgn*np.mean(phiT*psiT/om)/8
    return muE, muT

def umin(a, b, g, N=48):
    u, _, _ = symbol(grid(N), a, b, g)
    return u.min()

out = []
def P(*s):
    line = ' '.join(str(q) for q in s)
    print(line); out.append(line)

P('=== 0. reproduce F(1) (P1/V3 referee: 1.970388642e-3) ===')
for N in (48, 64, 96):
    P(N, mu_channels(1.0, N))

P('\n=== 1. Theorem A, Fourier rank check: n (x) a + a (x) n traceless-sym = 0  => a = 0 for n != 0 ===')
def tl_sym_map(n, d):
    # linear map a -> traceless symmetric part of n a^T + a n^T, as matrix (d*d x d)
    M = np.zeros((d*d, d))
    for q in range(d):
        a = np.zeros(d); a[q] = 1
        S = np.outer(n, a) + np.outer(a, n)
        S = S - np.trace(S)/d*np.eye(d)
        M[:, q] = S.ravel()
    return M
for d in (2, 3):
    rmin = d
    for n in np.ndindex(*([7]*d)):
        n = np.array(n) - 3
        if not n.any():
            continue
        r = np.linalg.matrix_rank(tl_sym_map(n, d))
        rmin = min(rmin, r)
    P(f'd={d}: minimal rank over n in [-3,3]^d minus 0 = {rmin} (= d means trivial kernel)')
P('gradient case p = grad u: mode n contributes u_n (n n^T)_traceless, zero iff n = 0 (d>=2).')
P('Lattice form: E_g protected pointwise <=> only |n_x|=|n_y|=|n_z| modes (body-diagonal hopping);')
P('              T_2g protected pointwise <=> only modes with one nonzero component (axis hopping);')
P('              both <=> u constant.')

P('\n=== 2. the two pointwise-protected classes and their unprotected channel (m = 1) ===')
P('axis-only (separable nn): muE, muT2 =', mu_channels(1.0, 64))
P('body-diagonal-only (u = 1 - cos x cos y cos z): muE, muT2 =', mu_channels(1.0, 64, g=1e9) )
# g -> large approximates pure body-diagonal after normalization; do it exactly:
def mu_bcc(m, N=64):
    K = grid(N); x, y, z = K
    co = [np.cos(x), np.cos(y), np.cos(z)]; s = [np.sin(x), np.sin(y), np.sin(z)]
    Pp = co[0]*co[1]*co[2]
    u = 1 - Pp
    gu = [s[0]*co[1]*co[2], co[0]*s[1]*co[2], co[0]*co[1]*s[2]]
    Hxx = Pp; Hyy = Pp; Hxy = -s[0]*s[1]*co[2]
    om = np.sqrt(m*m + 2*u)
    muE = -np.mean((gu[0]**2-gu[1]**2)*(Hxx-Hyy)/om)/8
    muT = -np.mean((2*gu[0]*gu[1])*(2*Hxy)/om)/8
    return muE, muT, u.min(), np.sum(np.isclose(u, 0, atol=1e-12))
P('exact body-diagonal symbol: muE, muT2, min u =', mu_bcc(1.0)[:3])
P('  note: zeros of u at (0,0,0),(pi,pi,0),(pi,0,pi),(0,pi,pi): 4 decoupled sublattices (doubling)')

P('\n=== 3. SLAC as limit of local symbols (separable, g_r -> k^2/2 sawtooth-squared) ===')
def slac_limit_formula(m, nq=200):
    # mu_E -> (1/(16 pi^2)) * Int_{[-pi,pi]^2} (pi^2/3 - t^2)/sqrt(m^2 + pi^2 + t^2 + s^2) dt ds
    xg, wg = leggauss(nq); t = np.pi*xg; w = np.pi*wg
    T, S = np.meshgrid(t, t, indexing='ij'); W = np.outer(w, w)
    I_reg = np.sum(W*(np.pi**2/3 - T**2)/np.sqrt(m*m + np.pi**2 + T**2 + S**2))
    I_naive = np.sum(W*(np.pi**2 - T**2)/np.sqrt(m*m + np.pi**2 + T**2 + S**2))
    return I_reg/(16*np.pi**2), I_naive/(16*np.pi**2)
def mu_sep(m, gfun, N):
    # separable: u = sum g(k_i); E channel only (T2 = 0 identically)
    k = 2*np.pi*(np.arange(N)+0.5)/N - np.pi
    g0, g1, g2 = gfun(k)
    muE = 0.0
    # loop over z to save memory
    GX, GY = np.meshgrid(g0, g0, indexing='ij')
    D1X, D1Y = np.meshgrid(g1, g1, indexing='ij')
    D2X, D2Y = np.meshgrid(g2, g2, indexing='ij')
    phi = D1X**2 - D1Y**2; psi = D2X - D2Y
    acc = 0.0
    for gz in g0:
        om = np.sqrt(m*m + 2*(GX + GY + gz))
        acc += np.sum(phi*psi/om)
    return -acc/N**3/8
def g_saw(r, sigma='lanczos'):
    n = np.arange(1, r+1)
    if sigma == 'lanczos':
        sg = np.sinc(n/(r+1))
    elif sigma == 'fejer':
        sg = 1 - n/(r+1)
    else:
        sg = np.ones_like(n, dtype=float)
    cn = 2*(-1.0)**(n+1)*sg/n**2      # g = sum cn (1 - cos n k), g' = sum cn n sin nk ~ sawtooth
    def f(k):
        K = np.outer(k, n)
        return (np.sum(cn*(1-np.cos(K)), 1), np.sum(cn*n*np.sin(K), 1), np.sum(cn*n*n*np.cos(K), 1))
    return f
for m in (1.0, 0.5):
    lim, naive = slac_limit_formula(m)
    P(f'm={m}: limit formula (any bounded regularization) = {lim:.6e};  naive open-cube SLAC value = {naive:.6e}')
    for r in (4, 8, 16, 32, 64):
        N = max(64, 12*r)
        P(f'   r={r:3d} N={N}: lanczos muE = {mu_sep(m, g_saw(r), N):.6e}   fejer muE = {mu_sep(m, g_saw(r,"fejer"), N):.6e}')
P('  nn reference g = 1 - cos k (should equal F(1)):', mu_sep(1.0, lambda k: (1-np.cos(k), np.sin(k), np.cos(k)), 96))

P('\n=== 4. tuning: 2-parameter non-separable family, zero both channels at m = 1 ===')
def F2(x, m=1.0, N=48):
    return mu_channels(m, N, a=x[0], b=x[1])
for a0, b0 in ((0.0, 0.0), (-0.05, 0.1), (0.1, -0.1)):
    sol, info, ier, msg = fsolve(F2, [a0, b0], full_output=True)
    if ier == 1:
        break
P('root (a*, b*) =', sol, ' residual at N=48:', F2(sol), ' at N=96:', mu_channels(1.0, 96, a=sol[0], b=sol[1]))
P('min u on grid (positivity):', umin(sol[0], sol[1], 0.0))
P('mass dependence of the tuned symbol (muE, muT2):')
for m in (0.1, 0.3, 0.5, 1.0, 2.0, 4.0):
    N = 128 if m < 0.4 else 64
    P(f'   m={m}: {mu_channels(m, N, a=sol[0], b=sol[1])}   fermion-sign same symbol: {mu_channels(m, N, a=sol[0], b=sol[1], fermion=True)}')
# critical-point Hessians at TRIM points for tuned symbol
def hess_at(pt, a, b, g=0.0):
    K = [np.array([[[pt[0]]]]), np.array([[[pt[1]]]]), np.array([[[pt[2]]]])]
    u, gu, H = symbol(K, a, b, g)
    return float(u.ravel()[0]), np.array([[float(H[i][j].ravel()[0]) for j in range(3)] for i in range(3)])
P('TRIM Hessians for tuned symbol (van Hove argument needs Hess ~ I at every critical point):')
for name, pt in (('G', (0, 0, 0)), ('X', (np.pi, 0, 0)), ('M', (np.pi, np.pi, 0)), ('R', (np.pi, np.pi, np.pi))):
    uu, HH = hess_at(pt, sol[0], sol[1])
    ev = np.linalg.eigvalsh(HH)
    P(f'   {name}: u={uu:.4f} Hess eig = {ev}  psi_E(diag(1,-1,0)) = {HH[0,0]-HH[1,1]:+.4f}  psi_E(diag(1,1,-2)/sqrt3) = {(HH[0,0]+HH[1,1]-2*HH[2,2])/np.sqrt(3):+.4f}')

P('\n=== 5. second-order DOS change nu_h = pushforward of J"_h dk under u (must vanish for mass-independent mu=0) ===')
def dos2(a, b, N=96, nb=24, h='E'):
    K = grid(N); u, gu, H = symbol(K, a, b, 0.0)
    if h == 'E':
        phi = gu[0]**2 - gu[1]**2; psi = H[0][0] - H[1][1]
    else:
        phi = 2*gu[0]*gu[1]; psi = 2*H[0][1]
    # J'' = div(v div v); its pushforward pairs with G(u) as  int G(u) J'' = - int G'(u) phi psi /4 (v = h grad u /2)
    # so the density of nu w.r.t. dE is d/dE of  -(1/4) int_{u<E} phi psi  ... report cumulative C(E) = -(1/4) <phi psi 1[u<E]>
    edges = np.linspace(u.min(), u.max(), nb+1)
    C = np.array([-(1/4)*np.mean(phi*psi*(u < e)) for e in edges[1:]])
    return edges[1:], C
for lab, (a, b) in (('nn', (0.0, 0.0)), ('tuned', (sol[0], sol[1]))):
    for h in ('E', 'T2'):
        e, C = dos2(a, b, h=h)
        P(f'{lab:6s} {h:2s}: C(E) = -(1/4)<phi psi 1[u<E]> at 8 levels:', np.array2string(C[2::3], precision=3))

P('\n=== 6. density-weight family: transport eps as weight-w density, mu^(w) = (1-w) mu_0 - w(1-w) <eps (div v)^2> ===')
K = grid(64); x, y, z = K
om = np.sqrt(1 + 2*(3 - np.cos(x) - np.cos(y) - np.cos(z)))
divvE = 0.5*(np.cos(x) - np.cos(y))
mu0 = mu_channels(1.0, 64)[0]
q2 = np.mean(0.5*om*divvE**2)
for w in (0.0, 0.25, 0.5, 0.75, 1.0):
    P(f'  w={w}: muE = {(1-w)*mu0 - w*(1-w)*q2:+.6e}   (muT2 = 0 for separable, all w)')
P('  root of mu^(w)=0 in (0,1):', mu0/(mu0+q2), ' (a tuned weight, mass dependent)')
P('  linear term of weight-w transport: T1 = -(L_v eps) - w eps div v; extra per-quantum symbol -w omega (h:Hess u)/2 is not')
P('  a conserved-stress term (nonzero uniform total) -> breaks RN-L1 exact stress unless w = 0 on the operator.')

with open(__file__.replace('.py', '.out'), 'w') as f:
    f.write('\n'.join(out) + '\n')
