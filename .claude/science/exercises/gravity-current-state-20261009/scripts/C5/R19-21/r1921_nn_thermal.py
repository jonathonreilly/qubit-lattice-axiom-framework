"""R19-21 (a)/(c) model check. NN lattice scalar, eps^2 = m^2 + sum 2(1 - cos k), on-site (lambda/4!) phi^4 at first order
(Hartree), thermal state at temperature T. Strain = R9-2/R19-15 SF flow (E_g: k_x -> flow(+t), k_y -> flow(-t); T_2g: coupled flow).
Mass renormalization is a fixed law datum fixed at h = 0 in the LOWEST state: m_b^2 = m_p^2 - (lambda/2) G_vac(0; m_p)  (as r1915_d_hartree.py).
Free energy at O(lambda): F(h) = <eps/2> + <T ln(1 - e^{-eps/T})> + (lambda/8) G_tot(h)^2,  G_tot = <(1 + 2n)/(2 eps)>, all at m_b.
Part 1: direct flow-integrated finite-difference Hessians (uniform midpoint grid) vs the O(lambda) prediction
   H_full - mu_vac(m_p)            = mu_th,free + (lambda/4) G_th(0) [G_vac'' + G_th'']        (what a FIXED lowest-state subtraction leaves)
   H_full - mu_vac(m_eff), m_eff^2 = m_p^2 + (lambda/2) G_th(0):  = mu_th,free + (lambda/4) G_th(0) G_th''   (state-tracking subtraction)
   and the identity d mu_vac / d m^2 = G_vac''/2.
Part 2 (scaling): Lemma-H single-momentum Hessian formula  d^2/dt^2 <g(eps o Phi_t)> = -<(div v)(v . grad g)>  on a graded GL grid,
   T from 0.4 down to 0.0125, m = 0.02 (near massless): G_th(0) -> T^2/12, mu_th,free ~ T^6, cross term ~ T^2.
Units: lattice (a = 1). Canonical-mass reading (conditional, PRICE_NOTE:22): m_g^2 a^2 = 16 pi mu; H^2 a^2 = (8 pi/3)(pi^2/30) g* (T a)^4."""
import numpy as np, time
t0 = time.time()
def nB(e, T):
    return 1.0/np.expm1(e/T)
# ---------------- Part 1: direct flows (copied flow integrators from r1915_d_hartree.py, unmodified logic) -------------
def flowE(kx, ky, t, nst=20):
    F = lambda y: 0.5*np.sin(y)
    def one(x, s):
        h = s/nst
        for _ in range(nst):
            a = F(x); b = F(x + 0.5*h*a); c = F(x + 0.5*h*b); d = F(x + h*c)
            x = x + h*(a + 2*b + 2*c + d)/6
        return x
    return one(kx, t), one(ky, -t)
def flowT(kx, ky, t, nst=20):
    F = lambda y: 0.5*np.sin(y)
    h = t/nst; x, y = kx.copy(), ky.copy()
    for _ in range(nst):
        a1, a2 = F(y), F(x)
        b1, b2 = F(y + 0.5*h*a2), F(x + 0.5*h*a1)
        c1, c2 = F(y + 0.5*h*b2), F(x + 0.5*h*b1)
        d1, d2 = F(y + h*c2), F(x + h*c1)
        x, y = x + h*(a1 + 2*b1 + 2*c1 + d1)/6, y + h*(a2 + 2*b2 + 2*c2 + d2)/6
    return x, y
def make_S(N):
    k = 2*np.pi*(np.arange(N) + 0.5)/N
    KX, KY, KZ = np.meshgrid(k, k, k, indexing='ij')
    cache = {}
    def S(t, chan):
        key = (round(t, 12), chan)
        if key not in cache:
            kx, ky = (KX, KY) if t == 0 else (flowE if chan == 'E' else flowT)(KX, KY, t)
            cache[key] = 6 - 2*np.cos(kx) - 2*np.cos(ky) - 2*np.cos(KZ)
        return cache[key]
    return S
def parts(S, m2, T, t, chan):
    e = np.sqrt(m2 + S(t, chan)); n = nB(e, T)
    return dict(E0=0.5*e.mean(), Fth=(T*np.log(-np.expm1(-e/T))).mean(), Gv=(0.5/e).mean(), Gt=(n/e).mean())
def hess(f, d=0.02):
    return (f(d) - 2*f(0.0) + f(-d))/d**2
print('Part 1: direct SF-flow Hessians, NN scalar, uniform midpoint grid, d = 0.02')
for N in (32, 40):
    S = make_S(N)
    for chan in ('E', 'T'):
        for (mp, T) in ((0.5, 0.3), (0.5, 0.15)):
            P = lambda m2, t, key: parts(S, m2, T, t, chan)[key]
            Gv0 = P(mp**2, 0.0, 'Gv'); Gt0 = P(mp**2, 0.0, 'Gt')
            mu_vac = hess(lambda t: P(mp**2, t, 'E0')); mu_thf = hess(lambda t: P(mp**2, t, 'Fth'))
            Gv2 = hess(lambda t: P(mp**2, t, 'Gv')); Gt2 = hess(lambda t: P(mp**2, t, 'Gt'))
            dm = 1e-3
            dmu_dm2 = (hess(lambda t: P(mp**2 + dm, t, 'E0')) - hess(lambda t: P(mp**2 - dm, t, 'E0')))/(2*dm)
            print(' N=%d chan=%s m_p=%.2f T=%.2f: mu_vac %+.6e  mu_th,free %+.4e  G_th(0) %.5e  G_vac'' %+.5e  G_th'' %+.4e | dmu_vac/dm^2 %+.6e vs G_vac''/2 %+.6e'
                  % (N, chan, mp, T, mu_vac, mu_thf, Gt0, Gv2, Gt2, dmu_dm2, Gv2/2))
            for lam in (0.02, 0.01):
                mb2 = mp**2 - 0.5*lam*Gv0
                def Ffull(t):
                    p = parts(S, mb2, T, t, chan); return p['E0'] + p['Fth'] + lam/8*(p['Gv'] + p['Gt'])**2
                Hf = hess(Ffull)
                fixed = Hf - mu_vac; pred_fixed = mu_thf + lam/4*Gt0*(Gv2 + Gt2)
                meff2 = mp**2 + 0.5*lam*Gt0
                loc = Hf - hess(lambda t: P(meff2, t, 'E0')); pred_loc = mu_thf + lam/4*Gt0*Gt2
                print('   lambda=%.3f  FIXED leaves %+.6e (pred %+.6e, diff %+.1e = O(lambda^2))   STATE-TRACKING leaves %+.6e (pred %+.6e, diff %+.1e)'
                      % (lam, fixed, pred_fixed, fixed - pred_fixed, loc, pred_loc, loc - pred_loc), flush=True)
print('Part 1 time %.0f s' % (time.time() - t0), flush=True)
# ---------------- Part 2: Lemma-H formula on graded Gauss-Legendre grid -------------
br = np.array([0, 0.0025, 0.005, 0.01, 0.02, 0.04, 0.08, 0.16, 0.32, 0.64, 1.28, 2.2, np.pi])
xg, wg = np.polynomial.legendre.leggauss(6)
nodes, wts = [], []
for a, b in zip(br[:-1], br[1:]):
    nodes += list(0.5*(b - a)*xg + 0.5*(b + a)); wts += list(0.5*(b - a)*wg)
nodes = np.array(nodes); wts = np.array(wts)
k1 = np.concatenate([-nodes[::-1], nodes]); w1 = np.concatenate([wts[::-1], wts])/(2*np.pi)
KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij', sparse=True)
W = w1[:, None, None]*w1[None, :, None]*w1[None, None, :]
Sg = 6 - 2*np.cos(KX) - 2*np.cos(KY) - 2*np.cos(KZ)
divv = 0.5*(np.cos(KX) - np.cos(KY)); vgradeps_num = 0.5*(np.sin(KX)**2 - np.sin(KY)**2)   # v.grad eps = vgradeps_num/eps
def avg(x): return float((W*x).sum())
def hessE(gp, e):   # -<(div v) g'(eps) (v.grad eps)>
    return -avg(divv*gp*vgradeps_num/e)
print('Part 2: graded GL grid, %d nodes/axis; check vs closed form: NN m=1 mu_E (V3 +1.970388642e-3)' % len(k1))
e1 = np.sqrt(1.0 + Sg); print('  m=1 zero-point mu_E (Lemma H formula) %+.9e' % hessE(0.5, e1))
m = 0.02; e = np.sqrt(m*m + Sg)
Gv2 = hessE(-0.5/e**2, e); mu0 = hessE(0.5, e)
print('  m=%.3f: mu_vac %+.6e   G_vac'' %+.6e  (UV, T-independent)' % (m, mu0, Gv2))
gstar = 106.75
print('  T        G_th(0)      T^2/12      mu_th,free    mu_th/T^6     cross(lam=1)=G_th*G_vac''/4   m_g^2/H^2 [fixed, lam=1, g*=106.75]   m_g^2/H^2 [state-tracking]')
for T in (0.4, 0.2, 0.1, 0.05, 0.025, 0.0125):
    n = nB(e, T); nprime = -n*(1 + n)/T
    Gt0 = avg(n/e); muth = hessE(n, e)                 # d/deps [T ln(1-e^{-eps/T})] = n
    Gt2 = hessE(nprime/e - n/e**2, e)                    # g = n/eps
    cross = 0.25*Gt0*Gv2; loc_res = muth + 0.25*Gt0*Gt2
    H2 = (8*np.pi/3)*(np.pi**2/30)*gstar*T**4
    print('  %-7.4f  %.5e  %.5e  %+.5e  %+.4e  %+.5e                  %+.3e                          %+.3e'
          % (T, Gt0, T*T/12, muth, muth/T**6, cross, 16*np.pi*(muth + cross)/H2, 16*np.pi*loc_res/H2), flush=True)
print('total time %.0f s' % (time.time() - t0))
