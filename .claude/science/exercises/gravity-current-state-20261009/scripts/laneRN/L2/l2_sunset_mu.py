"""L2 / lane RN: zero-momentum TT response of onsite phi^4 at O(lambda^2), best free-level design.

Matter: H = sum_x [pi^2/2 + (grad phi)^2/2 + m^2 phi^2/2] + (lam/24) sum_x phi_x^4 on Z^3.
Coupling to a constant TT strain h, 'designed' at the free level: H(h) = U_h H_2 U_h^dag + lam H_4,
U_h = exp(-i h_ij D_ij), D_ij = sum_x x_j P_i(x), P the free pseudo-momentum with one-body symbol f(k)
(f(k)=sin k for the range-1 density -pi grad phi; longer-range f below).  P_2 is exactly conserved by H_2,
so the free vacuum energy is exactly h-independent (free mu = 0 by design); onsite phi^4 is
volume-weighted only (sqrt g = 1 for TT), so H_4 itself is not sheared.
U_h acts on modes as a smooth flow Phi_h of the Brillouin torus (dk/ds = h^T f(k)); phi transported as a
density (Jacobian J), pi as a scalar.  Then exactly
  E^(1)/V = (lam/8) G^2,   G = int dk/(2 omega(k))            (h-independent: checked)
  E^(2)/V = -(lam^2/24) I4(h) - 2 (lam G/4)^2 I2(h)
  I_p(h)  = int_0^inf dt sum_x [g_t(x)]^p,  g_t(k) = J(k) exp(-t w(Phi k)) / (2 w(Phi k)).
In the continuum (Phi linear, det 1) I_p are exactly h-independent; on Z^3 they are not.
mu = d^2 (E/V) / d eps^2 at eps=0, with h = eps*diag(1,-1,0) (E channel) or h_xy=h_yx=eps (T2 channel).
"""
import numpy as np, sys, time
from scipy.integrate import quad

def fsym(R, kind):
    """odd periodic one-body momentum symbol, f'(0)=1, returned as (f, f') callables"""
    if kind == 'sin':
        return (lambda k: np.sin(k)), (lambda k: np.cos(k))
    if kind == 'improved':   # Taylor-improved: f = k + O(k^{2R+1}), range R (standard central-difference weights)
        from numpy.linalg import solve
        n = np.arange(1, R+1)
        # sum_n c_n n^{2j+1} = delta_{j0}, j=0..R-1
        M = np.array([n**(2*j+1) for j in range(R)], float)
        c = solve(M, np.eye(R)[0])
    elif kind == 'fejer':    # Fejer-smoothed sawtooth, renormalised to f'(0)=1
        n = np.arange(1, R+1)
        c = (1 - n/(R+1))*2*(-1.0)**(n+1)/n
        c = c/np.sum(c*n)
    f = lambda k: np.sum(c[:, None]*np.sin(np.outer(n, k)), axis=0).reshape(np.shape(k))
    fp = lambda k: np.sum((c*n)[:, None]*np.cos(np.outer(n, k)), axis=0).reshape(np.shape(k))
    return f, fp

def flow1d(k, eps, f, fp, nsteps=400):
    """dk/ds = eps f(k), s in [0,1]; returns Phi and J = dPhi/dk (variational eq.)"""
    x = k.copy(); J = np.ones_like(k); h = 1.0/nsteps
    for _ in range(nsteps):
        def rhs(x, J): return eps*f(x), eps*fp(x)*J
        a1, b1 = rhs(x, J); a2, b2 = rhs(x+h/2*a1, J+h/2*b1); a3, b3 = rhs(x+h/2*a2, J+h/2*b2); a4, b4 = rhs(x+h*a3, J+h*b3)
        x = x + h/6*(a1+2*a2+2*a3+a4); J = J + h/6*(b1+2*b2+2*b3+b4)
    return x, J

def flow2d_T2(kx, ky, eps, f, nsteps=400):
    """dkx/ds = eps f(ky), dky/ds = eps f(kx): divergence-free, J = 1"""
    x, y = kx.copy(), ky.copy(); h = 1.0/nsteps
    for _ in range(nsteps):
        def rhs(x, y): return eps*f(y), eps*f(x)
        a1, b1 = rhs(x, y); a2, b2 = rhs(x+h/2*a1, y+h/2*b1); a3, b3 = rhs(x+h/2*a2, y+h/2*b2); a4, b4 = rhs(x+h*a3, y+h*b3)
        x = x + h/6*(a1+2*a2+2*a3+a4); y = y + h/6*(b1+2*b2+2*b3+b4)
    return x, y

def w(kx, ky, kz, m):
    return np.sqrt(m**2 + 4*np.sin(kx/2)**2 + 4*np.sin(ky/2)**2 + 4*np.sin(kz/2)**2)

def build(L, m, eps, channel, f, fp):
    k1 = 2*np.pi*np.fft.fftfreq(L)            # grid in [-pi,pi)
    KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij')
    if channel == 'E':
        px, jx = flow1d(k1, eps, f, fp); py, jy = flow1d(k1, -eps, f, fp)
        PX = px[:, None, None]*np.ones((1, L, L)); PY = py[None, :, None]*np.ones((L, 1, L)); PZ = KZ
        J = jx[:, None, None]*jy[None, :, None]*np.ones((1, 1, L))
    else:
        ax, ay = np.meshgrid(k1, k1, indexing='ij'); fx, fy = flow2d_T2(ax, ay, eps, f)
        PX = fx[:, :, None]*np.ones((1, 1, L)); PY = fy[:, :, None]*np.ones((1, 1, L)); PZ = KZ
        J = np.ones((L, L, L))
    W = w(PX, PY, PZ, m)
    return J, W

def Ip(J, W, p):
    def integrand(t):
        g = J*np.exp(-t*W)/(2*W)
        gx = np.fft.ifftn(g).real            # (1/L^3) sum_k e^{ikx} g(k)
        return np.sum(gx**p)
    val, err = quad(integrand, 0, np.inf, epsabs=0, epsrel=1e-13, limit=400)
    return val

def energies(L, m, eps, channel, f, fp):
    J, W = build(L, m, eps, channel, f, fp)
    G = np.mean(J/(2*W))
    I4 = Ip(J, W, 4); I2 = Ip(J, W, 2)
    return G, I4, I2

def mu(L, m, channel, f, fp, eps=0.08):
    vals = {}
    for e in [-eps, -eps/2, 0, eps/2, eps]:
        vals[e] = energies(L, m, e, channel, f, fp)
    out = {}
    for name, idx in [('G', 0), ('I4', 1), ('I2', 2)]:
        D = lambda e: (vals[e][idx] + vals[-e][idx] - 2*vals[0][idx])/e**2
        out[name] = (4*D(eps/2) - D(eps))/3     # Richardson
        out[name+'0'] = vals[0][idx]
    G0 = out['G0']
    # E/V = (lam/8) G^2 - (lam^2/24) I4 - 2 (lam G/4)^2 I2 ; G'' = 0 expected
    out['muE1_per_lam'] = (1/4)*G0*out['G']            # d^2/de^2 of G^2/8 at stationary point
    out['mu2_per_lam2'] = -(1/24)*out['I4'] - (G0**2/8)*out['I2']
    out['mu2_I4part'] = -(1/24)*out['I4']; out['mu2_I2part'] = -(G0**2/8)*out['I2']
    return out

if __name__ == '__main__':
    t0 = time.time()
    m = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
    print(f"onsite phi^4, m={m}; E^(2)/V = -(lam^2/24) I4 - 2(lam G/4)^2 I2; mu = d^2(E/V)/d eps^2")
    f, fp = fsym(1, 'sin')
    for ch in ['E', 'T2']:
        for L in [16, 24, 32]:
            o = mu(L, m, ch, f, fp)
            print(f"[f=sin k, range 1] channel {ch:2s} L={L:2d}: G={o['G0']:.10f} G''={o['G']:.2e} | I4={o['I40']:.6e} I4''={o['I4']:.6e} "
                  f"I2''={o['I2']:.6e} | mu1/lam={o['muE1_per_lam']:.2e}  mu2/lam^2={o['mu2_per_lam2']:.6e} "
                  f"(I4 part {o['mu2_I4part']:.3e}, I2 part {o['mu2_I2part']:.3e})  [{time.time()-t0:.0f}s]")
            sys.stdout.flush()
    L = 24
    for kind, Rl in [('improved', [2, 3, 4]), ('fejer', [4, 8, 16])]:
        for R in Rl:
            f, fp = fsym(R, kind)
            for ch in (['E', 'T2'] if (kind == 'improved' and R == 2) else ['E']):
                o = mu(L, m, ch, f, fp)
                print(f"[f={kind} R={R}] channel {ch:2s} L={L}: G''={o['G']:.2e}  mu2/lam^2={o['mu2_per_lam2']:.6e} "
                      f"(I4 part {o['mu2_I4part']:.3e}, I2 part {o['mu2_I2part']:.3e})  [{time.time()-t0:.0f}s]")
                sys.stdout.flush()
