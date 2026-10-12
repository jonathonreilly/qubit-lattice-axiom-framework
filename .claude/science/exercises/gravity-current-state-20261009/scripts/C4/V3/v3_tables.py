"""V3 tables.
(A) converged free-part Jacobian anomaly mu_E (mu_T2 = 0 by Liouville) for the staggered fermion and the KG scalar.
    Validated in v3_free_*_seagull.out: honest local-operator Hessian == Jacobian formula on every grid to <=1e-8 rel.
    Fermion, V1 normalisation (flow velocity eps*hhat*(1/2 sin 2p)):  mu = -1/2 d2/deps2 < omega_s(Phi^{-1} p) >
    Scalar, RN L1 normalisation (velocity eps/2*hhat*sin k):          mu = +1/2 d2/deps2 < omega(Phi^{-1} k) >
(B) staggered 1->3 gap (any band/taste mix: kinematics only through omega_s) and the KG map D3_s(m) = 1/2 D3_KG(2m);
    QED vacuum-creation and gamma <-> e+e- resonance thresholds.
(C) photon-leg tails of the forced O(e) e+e-gamma dressing kernel at fixed pair energy Sigma:
    A-leg  g_A(q) = 1/(2(Sigma+Omega(q))),  E-leg  g_E(q) = 1/(2 Omega(q) (Sigma+Omega(q))),  Omega = sqrt(sum 4 sin^2(q/2));
    massive control Omega_M = sqrt(M^2 + ...).
"""
import numpy as np, sys
from scipy.optimize import minimize

def flow_inv(P, eps, hh, f, nsteps=200):
    x = P.copy(); h = 1.0/nsteps
    def rhs(x): return -eps*np.einsum('ij,...i->...j', hh, f(x))
    for _ in range(nsteps):
        a1 = rhs(x); a2 = rhs(x+h/2*a1); a3 = rhs(x+h/2*a2); a4 = rhs(x+h*a3)
        x = x + h/6*(a1+2*a2+2*a3+a4)
    return x
def hess(F, de=0.02):
    v = {e: F(e) for e in [-de, -de/2, 0, de/2, de]}
    D = lambda e: (v[e]+v[-e]-2*v[0])/e**2
    return (4*D(de/2)-D(de))/3
HH = {'E': np.diag([1., -1., 0.]), 'T2': np.array([[0, 1., 0], [1., 0, 0], [0, 0, 0]])}
def grid(L):
    k = 2*np.pi*(np.arange(L)+0.5)/L
    return np.stack(np.meshgrid(k, k, k, indexing='ij'), -1).reshape(-1, 3)

print('(A) free-part Jacobian anomaly (honest local unitary coupling), per site')
def strained_grid(L, e, ch, f):
    k = 2*np.pi*(np.arange(L)+0.5)/L
    if ch == 'E':
        qx = flow_inv(k[:, None], e, np.array([[1.0]]), f)[:, 0]; qy = flow_inv(k[:, None], -e, np.array([[1.0]]), f)[:, 0]
        return np.meshgrid(qx, qy, k, indexing='ij')
    ax, ay = np.meshgrid(k, k, indexing='ij'); P2 = np.stack([ax, ay], -1)
    Q = flow_inv(P2, e, np.array([[0, 1.0], [1.0, 0]]), f)
    return Q[:, :, 0][:, :, None]*np.ones((1, 1, L)), Q[:, :, 1][:, :, None]*np.ones((1, 1, L)), k[None, None, :]*np.ones((L, L, 1))
for L in [32, 64]:
    for m in [0.0, 0.1, 0.3, 0.5, 1.0]:
        row = []
        for ch in ['E', 'T2']:
            fs = lambda x: 0.5*np.sin(2*x)
            mf = hess(lambda e: -0.5*np.sqrt(m**2 + sum(np.sin(q)**2 for q in strained_grid(L, e, ch, fs))).mean())
            fk = lambda x: 0.5*np.sin(x)
            ms = hess(lambda e: 0.5*np.sqrt(m**2 + sum(4*np.sin(q/2)**2 for q in strained_grid(L, e, ch, fk))).mean())
            row += [mf, ms]
        print(f'  L={L} m={m:.1f}: fermion(V1 norm) mu_E={row[0]:+.6e} mu_T2={row[2]:+.1e} | scalar(RN L1 norm) mu_E={row[1]:+.6e} mu_T2={row[3]:+.1e}'
              f' | fermion in RN-L1 norm mu_E={row[0]/4:+.6e}')
        sys.stdout.flush()

print('(B) gaps')
ws = lambda k, m: np.sqrt(m**2 + (np.sin(k)**2).sum(-1))
wKG = lambda k, M: np.sqrt(M**2 + (4*np.sin(k/2)**2).sum(-1))
rng = np.random.default_rng(1)
for m in [0.1, 0.3, 0.5, 1.0]:
    best = 1e9
    def D3(z):
        k = z.reshape(3, 3); Q = k.sum(0)
        return ws(k, m).sum() - ws(Q, m)
    for _ in range(300):
        r = minimize(D3, rng.uniform(-np.pi, np.pi, 9), method='Nelder-Mead', options={'xatol': 1e-10, 'fatol': 1e-12, 'maxiter': 6000})
        best = min(best, r.fun)
    bound = 0.5*(np.sqrt(36*m*m+108) - np.sqrt(4*m*m+108))
    print(f'  staggered m={m}: min D3 (1 -> 3 quasiparticles, any band/taste) = {best:.6f};  proved KG-map bound 1/2[sqrt(36m^2+108)-sqrt(4m^2+108)] = {bound:.6f};  0->4 gap 4m = {4*m:.3f}; 0->2 = 2m')
# gamma -> e+ e- on-shell resonance: max_q [Omega(q) - min_p (w(p)+w(q-p))]; fermion energies pi-periodic
for m in [0.05, 0.5, 1.0, 1.5, 1.7, 1.75, 2.0]:
    best = -1e9
    def g(z):
        q = z[:3]; p = z[3:]
        return -(np.sqrt((4*np.sin(q/2)**2).sum()) - ws(p, m) - ws(q-p, m))
    for _ in range(200):
        r = minimize(g, rng.uniform(-np.pi, np.pi, 6), method='Nelder-Mead', options={'maxiter': 4000})
        best = max(best, -r.fun)
    print(f'  QED m={m}: max_q,p [Omega(q) - w(p) - w(q-p)] = {best:+.4f}  -> gamma<->e+e- shell {"NON-EMPTY" if best > 0 else "empty"}; e+e-gamma creation denominator inf = 2m = {2*m}')

print('(C) photon-leg tails of the forced O(e) dressing kernel (3D, L=96 torus, along an axis), Sigma = 2m')
L = 96
k = 2*np.pi*np.fft.fftfreq(L)
KX, KY, KZ = np.meshgrid(k, k, k, indexing='ij')
O2 = 4*(np.sin(KX/2)**2 + np.sin(KY/2)**2 + np.sin(KZ/2)**2)
for (lab, Om) in [('massless photon', np.sqrt(O2)), ('massive control M=0.5', np.sqrt(0.25 + O2))]:
    for Sig in [0.2, 1.0]:
        with np.errstate(divide='ignore'):
            gA = 1/(2*(Sig + Om)); gE = 1/(2*Om*(Sig + Om))
        if lab.startswith('massless'): gE[0, 0, 0] = 0.0
        rA = np.fft.ifftn(gA).real[:, 0, 0]; rE = np.fft.ifftn(gE).real[:, 0, 0]
        rs = np.array([4, 8, 12, 16, 24, 32])
        lA = np.log(np.abs(rA[rs])); lE = np.log(np.abs(rE[rs]))
        sA = np.diff(lA)/np.diff(np.log(rs)); sE = np.diff(lE)/np.diff(np.log(rs))
        eA = -np.diff(lA)/np.diff(rs); eE = -np.diff(lE)/np.diff(rs)
        print(f'  {lab}, Sigma={Sig}: A-leg |g|(r=4..32) = ' + ' '.join(f'{abs(v):.2e}' for v in rA[rs]) +
              f'; local power slopes {np.round(sA, 2)}; exp rates {np.round(eA, 3)}')
        print(f'  {"":{len(lab)}}               E-leg |g|(r=4..32) = ' + ' '.join(f'{abs(v):.2e}' for v in rE[rs]) +
              f'; local power slopes {np.round(sE, 2)}; exp rates {np.round(eE, 3)}')
