"""C5 R8-2: the edge-mode universality problem in R7-1's box-confined Poincare law.

Parts
 (A) edge spectrum of R7-1's literal law (s = rho k + (1-rho) sin k) and of a gapped variant
     (eps^2 = m^2 + sum u(k_i), u increasing on [0, pi]); doublers; EP anomaly A = Hess(eps^2/2) - I
     on the edge (zone mean, energy-weighted means, values at rest points).
 (B) option (a): a universal, symmetric, Hermitian, exactly conserved one-body stress kernel
     F^{mu nu}(k+q, k) on the WHOLE torus (box + edge), d = 2, equal to the continuum on-shell kernel
     on box pairs with small transfer and of "dust" form F00 u u (u = (1, Delta), D.Delta = omega)
     elsewhere.  Lattice divergence symbol D(q) = s_c(q) + i psi(q) (generalised forward difference;
     only zero at q = 0; D = q on |q| <= 1).  Residuals of the Ward identity omega F^{0nu} = sum_j D_j F^{j nu},
     Hermiticity, forward values, Lemma U (box-edge matrix elements at the box face).
 (C) locality (d = 1): Fourier decay of the conserved kernels; contrast with the real odd symbol D = s.
 (D) Theorem E check (d = 1): wavepacket free fall in a uniform lapse field H = eps + g {X, eps}/2:
     a = -(Hess(eps^2/2)) g at rest points (box rest, R7-1 doubler, R7-1 s-maximum, gapped edge top).
"""
import numpy as np, time
np.set_printoptions(linewidth=150)
T0 = time.time()
out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)

def sstep(x):                      # C^inf (Gevrey-2) step: 0 for x<=0, 1 for x>=1
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)

def wrap(k):
    return -(((-k) + np.pi) % (2*np.pi) - np.pi)

def plateau(k, a, b):              # even, periodic: 1 on |k|<=a, 0 on |k|>=b
    return sstep((b - np.abs(wrap(k)))/(b - a))

B, B2, M = 2.0, 3.1, 0.3           # R7-1 script-1 parameters

# ---------------- the two one-dimensional profiles g(k), eps^2 = m^2 + sum_i g(k_i) ----------------
def s_r71(k):
    k = wrap(k); r = plateau(k, B, B2)
    return r*k + (1-r)*np.sin(k)
def g_r71(k):                      # R7-1: g = s^2
    return s_r71(k)**2

# gapped variant: u'(k) = rho(k) 2k + (1-rho(k)) C sin k  (odd, periodic, >0 on (0,pi)), u = int u'
Cg = 2*B/np.sin(B)
NG = 200001
kg = np.linspace(0, np.pi, NG)
up = plateau(kg, B, B2)*2*kg + (1-plateau(kg, B, B2))*Cg*np.sin(kg)
ug = np.concatenate([[0.0], np.cumsum(0.5*(up[1:]+up[:-1])*np.diff(kg))])
from scipy.interpolate import CubicSpline
_ucs = CubicSpline(kg, ug)
def g_gap(k):                      # exact k^2 on the box; cubic spline of the exact integral outside
    k = np.abs(wrap(k))
    return np.where(k <= B, k*k, _ucs(np.minimum(k, np.pi)))
def up_gap(k):                     # analytic u'(k), odd and periodic
    kw = wrap(k); ka = np.abs(kw); r = plateau(ka, B, B2)
    return np.sign(kw)*(r*2*ka + (1-r)*Cg*np.sin(ka))

def num_d1(f, k, h=1e-5):
    return (f(k+h) - f(k-h))/(2*h)
def num_d2(f, k, h=1e-4):
    if f is g_gap:
        return (up_gap(k+h) - up_gap(k-h))/(2*h)
    return (f(k+h) - 2*f(k) + f(k-h))/h**2

# ================= (A) edge spectrum, doublers, EP anomaly =================
pr('=== (A) edge spectrum and EP anomaly A = Hess(eps^2/2) - I (separable: A_ii = g\'\'(k_i)/2 - 1) ===')
kk = np.linspace(-np.pi, np.pi, 2001)[:-1]
for name, g in [('R7-1 literal (s = rho k + (1-rho) sin k)', g_r71), ('gapped (u increasing on [0,pi])', g_gap)]:
    gk = g(kk); A1 = num_d2(g, kk)/2 - 1.0
    inb = np.abs(kk) <= B
    pr('[%s]' % name)
    pr('  max |g - k^2| on box = %.2e ; max |A| on box (|k|<B-1e-3) = %.2e ; zone mean of A_11 = %.6f'
       % (np.max(np.abs(gk[inb]-kk[inb]**2)), np.max(np.abs(A1[np.abs(kk) < B-1e-3])), A1.mean()))
    for d in (2, 3):
        # d-dim grid by separability: eps^2 = m^2 + sum g(k_i)
        kd = kk[::4]
        G = np.meshgrid(*([kd]*d), indexing='ij')
        E = np.sqrt(M*M + sum(g(x) for x in G))
        edge = np.zeros(E.shape, bool)
        for x in G: edge |= (np.abs(x) > B)
        Ad = [num_d2(g, x)/2 - 1.0 for x in G]       # diagonal anomaly components
        trA = sum(Ad)/d
        pr('  d=%d: min eps on box = %.4f ; min eps on edge = %.4f (box-face value sqrt(m^2+B^2) = %.4f)'
           % (d, E[~edge].min(), E[edge].min(), np.sqrt(M*M+B*B)))
        pr('        zone mean of tr(A)/d = %.6f ; edge mean = %.4f ; energy-weighted edge mean = %.4f ; edge fraction of zone = %.4f'
           % (trA.mean(), trA[edge].mean(), (E[edge]*trA[edge]).sum()/E[edge].sum(), edge.mean()))
        # Boltzmann-weighted (lowest edge states) mean anomaly: what a thermal/virtual edge population would carry
        for Tb in (0.1, 1.0):
            w = np.exp(-(E[edge]-E[edge].min())/Tb)
            pr('        edge mean of tr(A)/d weighted exp(-(eps-eps_min)/T), T=%.1f : %.4f' % (Tb, (w*trA[edge]).sum()/w.sum()))
    # rest points in 1D profile: g'(k) = 0
    gp = num_d1(g, kk)
    idx = np.where(np.sign(gp[:-1]) != np.sign(gp[1:]))[0]
    rp = []
    for i in idx:
        a, b_ = kk[i], kk[i+1]
        for _ in range(60):
            c = 0.5*(a+b_)
            if np.sign(num_d1(g, np.array([a]))[0]) == np.sign(num_d1(g, np.array([c]))[0]): a = c
            else: b_ = c
        rp.append(0.5*(a+b_))
    rp = sorted(set(np.round(rp, 6)))
    pr('  1D rest points k (g\'=0) and A_11 = g\'\'/2 - 1 there, sqrt(m^2+g):')
    for r in rp:
        pr('     k = %+.5f : A = %+.4f ; free-fall weight beta = A+1 = %+.4f ; eps_1D = %.4f' %
           (r, num_d2(g, np.array([r]))[0]/2-1, num_d2(g, np.array([r]))[0]/2, np.sqrt(M*M+g(np.array([r]))[0])))
pr('  doublers of the literal law: eps at corners k_i in {0, pi} (d=3):')
for c in [(0,0,0), (np.pi,0,0), (np.pi,np.pi,0), (np.pi,np.pi,np.pi)]:
    e = np.sqrt(M*M + sum(g_r71(np.array([x]))[0] for x in c))
    eg = np.sqrt(M*M + sum(g_gap(np.array([x]))[0] for x in c))
    pr('     corner %s : eps(R7-1) = %.6f ; eps(gapped) = %.4f' % (tuple(np.round(c, 3)), e, eg))

# ================= (B) universal conserved stress on box + edge, d = 2 =================
pr('\n=== (B) option (a): universal symmetric conserved stress on the whole torus (d = 2) ===')
CD1, CD2 = 1.0, 2.5                 # D = q on |q|<=CD1
PS1, PS2 = 1.0, 2.0                 # psi = 0 on |q|<=PS1
def Dsym(q):                        # generalised forward-difference symbol, zero only at q = 0 (mod 2 pi)
    q = wrap(q); r = plateau(q, CD1, CD2)
    sc = r*q + (1-r)*np.sin(q)
    psi = (1 - plateau(q, PS1, PS2))*(1 - np.cos(q))
    return sc + 1j*psi
qq = np.linspace(-np.pi, np.pi, 20001)
pr('  min |D(q)| over |q| >= 0.05 : %.4f ; max |D(q) - q| on |q|<=1 : %.2e' %
   (np.min(np.abs(Dsym(qq[np.abs(qq) >= 0.05]))), np.max(np.abs(Dsym(qq[np.abs(qq) <= 1.0]) - qq[np.abs(qq) <= 1.0]))))

def make_eps(g):
    return lambda k: np.sqrt(M*M + g(k[..., 0]) + g(k[..., 1]))

def divdiff(f, a, j, qj):           # [f(a + qj e_j) - f(a)] / D(qj), with derivative limit at qj -> 0
    e = np.zeros_like(a); e[..., j] = qj
    num = f(a + e) - f(a)
    den = Dsym(qj)
    small = np.abs(qj) < 1e-7
    h = 1e-6; eh = np.zeros_like(a); eh[..., j] = h
    der = (f(a + eh) - f(a - eh))/(2*h)
    return np.where(small, der, num/np.where(small, 1.0, den))

def Delta(f, k, q):                 # symmetrised staircase, d = 2
    e0 = np.zeros_like(k); e0[..., 0] = q[..., 0]
    e1 = np.zeros_like(k); e1[..., 1] = q[..., 1]
    d0 = 0.5*(divdiff(f, k, 0, q[..., 0]) + divdiff(f, k + e1, 0, q[..., 0]))
    d1 = 0.5*(divdiff(f, k + e0, 1, q[..., 1]) + divdiff(f, k, 1, q[..., 1]))
    return np.stack([d0, d1], -1)

B1in, B1out = 1.6, 1.9              # chi1: 1 on |k_i|<=1.6, 0 beyond 1.9 (inside the exact box |k_i|<=2)
Q1in, Q1out = 0.5, 0.9              # eta: 1 on |q_i|<=0.5, 0 beyond 0.9 (inside D = q region)

def F_all(f, k, q):
    """returns F[..., mu, nu] for transition k -> k' = k + q (lattice momenta), d = 2"""
    kp = k + q
    e, ep = f(k), f(kp)
    om = ep - e
    Fd00 = 0.5*(e + ep)
    Dl = Delta(f, k, q)
    u = np.concatenate([np.ones(k.shape[:-1] + (1,)), Dl], -1)
    Fdust = Fd00[..., None, None]*u[..., :, None]*u[..., None, :]
    # continuum on-shell kernel on box pairs with small transfer
    kw, kpw = wrap(k), wrap(kp)
    qw = wrap(q)
    phi = np.prod(plateau(kw, B1in, B1out), -1)*np.prod(plateau(kpw, B1in, B1out), -1)*np.prod(plateau(qw, Q1in, Q1out), -1)
    ec = np.sqrt(M*M + (kw**2).sum(-1)); epc = np.sqrt(M*M + (kpw**2).sum(-1))
    K4 = np.concatenate([ec[..., None], kw], -1); Kp4 = np.concatenate([epc[..., None], kpw], -1)
    dot = ec*epc - (kw*kpw).sum(-1)
    eta = np.diag([1.0, -1.0, -1.0])
    Fc = (Kp4[..., :, None]*K4[..., None, :] + K4[..., :, None]*Kp4[..., None, :]
          - eta*(dot - M*M)[..., None, None])/(2*np.sqrt(ec*epc))[..., None, None]
    F = phi[..., None, None]*Fc + (1-phi)[..., None, None]*Fdust
    return F, om, phi

rng = np.random.default_rng(82)
for name, g in [('R7-1 literal', g_r71), ('gapped', g_gap)]:
    f = make_eps(g)
    pr('[%s]' % name)
    sets = {
      'random (k, q) on torus': (rng.uniform(-np.pi, np.pi, (4000, 2)), rng.uniform(-np.pi, np.pi, (4000, 2))),
      'box pairs, small q (phi=1 region)': (rng.uniform(-1.2, 1.2, (4000, 2)), rng.uniform(-0.4, 0.4, (4000, 2))),
      'box -> edge across the face': (np.stack([rng.uniform(1.7, 2.0, 4000), rng.uniform(-1, 1, 4000)], -1),
                                      np.stack([rng.uniform(0.2, 0.8, 4000), rng.uniform(-0.3, 0.3, 4000)], -1)),
      'edge -> edge': (rng.uniform(2.1, np.pi, (4000, 2))*rng.choice([-1, 1], (4000, 2)), rng.uniform(-np.pi, np.pi, (4000, 2))),
    }
    for sname, (k, q) in sets.items():
        F, om, phi = F_all(f, k, q)
        Dq = Dsym(q)
        res = [np.abs(om*F[:, 0, nu] - (Dq[:, 0]*F[:, 1, nu] + Dq[:, 1]*F[:, 2, nu])) for nu in range(3)]
        scale = np.abs(om)[:, None]*np.abs(F[:, 0, :]).max(-1, keepdims=True) + 1e-300
        rel = max(np.max(r/scale[:, 0]) for r in res)
        absres = max(np.max(r) for r in res)
        # Hermiticity: F(k+q <- k) vs conj F(k <- k+q)
        Fr, _, _ = F_all(f, k + q, -q)
        herm = np.max(np.abs(F - np.conj(Fr)))
        sym = np.max(np.abs(F - np.swapaxes(F, -1, -2)))
        pr('  %-36s Ward |res| max = %.2e (rel %.2e) ; Hermiticity %.2e ; symmetry %.2e ; phi range [%.2f, %.2f] ; max|F00| = %.3f'
           % (sname, absres, rel, herm, sym, phi.min(), phi.max(), np.abs(F[:, 0, 0]).max()))
    # forward values: F(k,k) = eps (1, v, v v)
    k = rng.uniform(-np.pi, np.pi, (2000, 2)); q = np.full_like(k, 1e-9)
    F, _, _ = F_all(f, k, q)
    h = 1e-6
    v = np.stack([(f(k + [h, 0]) - f(k - [h, 0]))/(2*h), (f(k + [0, h]) - f(k - [0, h]))/(2*h)], -1)
    e = f(k)
    target = e[:, None, None]*np.concatenate([np.ones((len(k), 1)), v], -1)[:, :, None]*np.concatenate([np.ones((len(k), 1)), v], -1)[:, None, :]
    pr('  forward values: max |F(k,k) - eps (1,v)(1,v)^T| over random k = %.2e (sum_k F00 = H, sum_k F0i = sum eps v_i = J_E)' % np.max(np.abs(F - target)))
    # Lemma U: box state just inside the face couples to edge state just outside
    for dlt in (0.05, 0.01, 0.001):
        kin = np.array([[B - dlt, 0.3]]); qx = np.array([[2*dlt, 0.0]])
        F, _, _ = F_all(f, kin, qx)
        pr('  Lemma U: F00(k_in=(B-%.3f,0.3) -> k_out=(B+%.3f,0.3)) = %.5f   [eps at face = %.5f]' % (dlt, dlt, F[0, 0, 0].real, f(np.array([[B, 0.3]]))[0]))

# ================= (C) locality, d = 1 =================
pr('\n=== (C) locality of the conserved kernels, d = 1 (Fourier coefficients of F(k\', k) on an N x N grid) ===')
N = 512
kn = 2*np.pi*np.arange(N)/N - np.pi
KP, KK = np.meshgrid(kn, kn, indexing='ij')
for name, g in [('R7-1 literal', g_r71), ('gapped', g_gap)]:
    f1 = lambda k: np.sqrt(M*M + g(k))
    e, ep = f1(KK), f1(KP)
    qv = wrap(KP - KK)
    small = np.abs(qv) < 1e-12
    der = (f1(KK + 1e-6) - f1(KK - 1e-6))/2e-6
    Dl = np.where(small, der, (ep - e)/np.where(small, 1.0, Dsym(qv)))
    F00 = 0.5*(e + ep); F01 = F00*Dl; F11 = F00*Dl**2
    for lab, Fk in [('F00', F00), ('F01', F01), ('F11', F11)]:
        c = np.abs(np.fft.fft2(Fk))/N**2
        c = np.fft.fftshift(c)
        idx = np.arange(N) - N//2
        A_, Bb = np.meshgrid(idx, idx, indexing='ij')
        R = np.maximum(np.abs(A_), np.abs(Bb))
        env = [c[R == r].max() for r in (1, 8, 32, 64, 128, 200)]
        pr('  [%s] %s : max coeff at sup-distance r = 1, 8, 32, 64, 128, 200 : %s' % (name, lab, ['%.1e' % x for x in env]))
    # contrast: real odd symbol D = s (zero at q = pi): divided difference blows up near q = pi
    sreal = s_r71(qv)
    with np.errstate(divide='ignore', invalid='ignore'):
        Dl_r = np.where(small, der, (ep - e)/sreal)
    near = (np.abs(np.abs(qv) - np.pi) < 0.05)
    pr('  [%s] contrast, real odd symbol D = s(q): max |Delta| for |q| within 0.05 of pi = %.2e (generalised forward D: %.2f)'
       % (name, np.nanmax(np.abs(Dl_r[near])), np.max(np.abs(Dl[near]))))

# ================= (D) Theorem E: free fall in a uniform lapse field, d = 1 =================
pr('\n=== (D) free fall, H = eps(K) + g {X, eps(K)}/2 (first moment of the universal T00), d = 1 ===')
L = 1024; gacc = 5e-4
x = np.arange(L) - L//2
kl = 2*np.pi*np.fft.fftfreq(L)
Fm = np.fft.fft(np.eye(L), axis=0)/np.sqrt(L)          # unitary DFT matrix: psi_k = Fm psi_x
for name, g in [('R7-1 literal', g_r71), ('gapped', g_gap)]:
    ek = np.sqrt(M*M + g(kl))
    Hk = (Fm.conj().T*ek) @ Fm                         # eps(K) in position basis
    Hk = 0.5*(Hk + Hk.conj().T)
    X = np.diag(x.astype(float))
    H = Hk + gacc*0.5*(X @ Hk + Hk @ X)
    w, V = np.linalg.eigh(H)
    ts = np.linspace(0, 4, 17)
    for k0lab, k0 in [('box rest k=0', 0.0)] + ([('doubler rest k=pi', np.pi)] if name.startswith('R7') else []) + \
                     ([('s-maximum rest k*', None)] if name.startswith('R7') else [('edge top k=pi', np.pi)]):
        if k0 is None:   # locate k* = argmax s on (B, B2)
            kt = np.linspace(B, B2, 20001); k0 = kt[np.argmax(s_r71(kt))]
        sig = 40.0
        psi = np.exp(-x**2/(4*sig**2) + 1j*k0*x); psi /= np.linalg.norm(psi)
        c = V.conj().T @ psi
        xs = []
        for t in ts:
            pt = V @ (np.exp(-1j*w*t)*c)
            xs.append(np.real(np.vdot(pt, x*pt)))
        xs = np.array(xs)
        a_fit = 2*np.polyfit(ts, xs, 2)[0]
        # semiclassical prediction averaged over |psi(k)|^2 at t=0: a(k) = 2 g v^2 - g g''(k)/2 (1D, x ~ 0)
        pk = np.abs(np.fft.fft(psi))**2; pk /= pk.sum()
        v = num_d1(lambda kq: np.sqrt(M*M + g(kq)), kl)
        hess = num_d2(g, kl)/2
        a_pred = np.sum(pk*(2*gacc*v**2 - gacc*hess))
        pr('  [%s] %-20s k0 = %.4f : a_measured/g = %+.5f ; semiclassical <2v^2 - Hess(eps^2/2)> = %+.5f ; Hess(eps^2/2)(k0) = %+.4f'
           % (name, k0lab, k0, a_fit/gacc, a_pred/gacc, num_d2(g, np.array([k0]))[0]/2))

pr('\nruntime %.1f s' % (time.time() - T0))
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out) + '\n')
