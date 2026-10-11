"""G3 part 2: mu at O(lambda^2) for an umklapp-filtered onsite phi^4, split into normal and umklapp classes.
Reuses RN L2's basketball (l2_sunset_mu.py): E^(2)/V = -(lam^2/24) I4, I4 = int dt (1/V^3) sum_{k1+..+k4 = 0 mod 2pi} F^2 prod g_t(k_i),
g_t(k) = J(k) exp(-t w(Phi k)) / (2 w(Phi k)), Phi = strain flow of the momentum symbol f (free part designed unitarily).
Filtered vertex: F = 1 on normal 4-tuples (unwrapped sum = 0), F = eps_U on umklapp (unwrapped sum = 2 pi n, n != 0).
No cross terms (each 4-tuple is in exactly one class), so EXACTLY at this order
  mu(eps_U) = mu_N + eps_U^2 mu_U,   mu_X = -(1/24) d^2 I_X / d eps^2  (per lam^2, per cell).
Split computed by zero-padded (linear) convolution: class K = 0 is normal, K = +-2pi (per axis) umklapp.
Flows: f = sin k (RN L2 design; not conserved by normal collisions) and f = sawtooth (conserved by normal collisions;
T2 channel only: the E-channel sawtooth dilation has no unitary flow, see g3_face.py).
"""
import numpy as np, sys, time
from scipy.integrate import quad_vec
t0 = time.time()
def saw(k): return (k + np.pi) % (2*np.pi) - np.pi
def w_kg(kx, ky, kz, m): return np.sqrt(m**2 + 4*np.sin(kx/2)**2 + 4*np.sin(ky/2)**2 + 4*np.sin(kz/2)**2)

def flow_T2(kx, ky, eps, f, nsteps=400, wrap=False):
    x, y = kx.copy(), ky.copy(); h = 1.0/nsteps
    for _ in range(nsteps):
        def rhs(x, y): return eps*f(y), eps*f(x)
        a1, b1 = rhs(x, y); a2, b2 = rhs(x+h/2*a1, y+h/2*b1); a3, b3 = rhs(x+h/2*a2, y+h/2*b2); a4, b4 = rhs(x+h*a3, y+h*b3)
        x = x + h/6*(a1+2*a2+2*a3+a4); y = y + h/6*(b1+2*b2+2*b3+b4)
        if wrap: x, y = saw(x), saw(y)
    return x, y

def flow_E_sin(k, eps, nsteps=400):
    x = k.copy(); J = np.ones_like(k); h = 1.0/nsteps
    for _ in range(nsteps):
        def rhs(x, J): return eps*np.sin(x), eps*np.cos(x)*J
        a1, b1 = rhs(x, J); a2, b2 = rhs(x+h/2*a1, J+h/2*b1); a3, b3 = rhs(x+h/2*a2, J+h/2*b2); a4, b4 = rhs(x+h*a3, J+h*b3)
        x = x + h/6*(a1+2*a2+2*a3+a4); J = J + h/6*(b1+2*b2+2*b3+b4)
    return x, J

def build(L, m, eps, channel, kind):
    n = np.arange(L) - (L-1)//2                     # odd L: reduced momenta in (-pi, pi), no k = pi
    k1 = 2*np.pi*n/L
    KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij')
    if channel == 'T2':
        ax, ay = np.meshgrid(k1, k1, indexing='ij')
        if kind == 'sin': fx, fy = flow_T2(ax, ay, eps, np.sin)
        else: fx, fy = flow_T2(ax, ay, eps, saw, wrap=True)
        PX = fx[:, :, None]*np.ones((1, 1, L)); PY = fy[:, :, None]*np.ones((1, 1, L)); PZ = KZ; J = np.ones((L, L, L))
    else:
        px, jx = flow_E_sin(k1, eps); py, jy = flow_E_sin(k1, -eps)
        PX = px[:, None, None]*np.ones((1, L, L)); PY = py[None, :, None]*np.ones((L, 1, L)); PZ = KZ
        J = jx[:, None, None]*jy[None, :, None]*np.ones((1, 1, L))
    return J, w_kg(PX, PY, PZ, m), n

def classes(L, m, eps, channel, kind):
    J, W, n = build(L, m, eps, channel, kind)
    M = 4*L
    idx = n % M
    def integrand(t):
        g = J*np.exp(-t*W)/(2*W)
        gp = np.zeros((M, M, M)); gp[np.ix_(idx, idx, idx)] = g
        gx = np.fft.ifftn(gp)
        C = np.fft.fftn(gx**4).real * M**9 / L**9        # (1/V^3) sum over linear class K
        out = []
        # normal: K = 0 ; umklapp: any K with components in {0, +-L}, not all zero
        out.append(C[0, 0, 0])
        tot = 0.0
        for a in (0, L, -L):
            for b in (0, L, -L):
                for c in (0, L, -L):
                    if (a, b, c) != (0, 0, 0): tot += C[a % M, b % M, c % M]
        out.append(tot)
        return np.array(out)
    val, err = quad_vec(integrand, 0, np.inf, epsabs=1e-16, epsrel=1e-10, limit=400)
    return val

def mu_split(L, m, channel, kind, eps=0.08):
    v = {e: classes(L, m, e, channel, kind) for e in [-eps, -eps/2, 0, eps/2, eps]}
    D = lambda e: (v[e] + v[-e] - 2*v[0])/e**2
    I2 = (4*D(eps/2) - D(eps))/3
    return v[0], -(1/24)*I2

if __name__ == '__main__':
    m = 1.0
    print("m=1, KG dispersion; mu per lam^2 per cell; I4 classes at eps=0 [normal, umklapp]")
    for kind, ch in [('sin', 'T2'), ('sin', 'E'), ('saw', 'T2')]:
        for L in [11, 15, 19]:
            I0, mu = mu_split(L, m, ch, kind)
            print(f"  flow f={kind:3s} channel {ch:2s} L={L}: I4_N={I0[0]:.6e} I4_U={I0[1]:.6e} (sum {I0.sum():.6e}) | "
                  f"mu_N={mu[0]:+.4e}  mu_U={mu[1]:+.4e}  mu(eps_U=1)={mu.sum():+.4e}  [{time.time()-t0:.0f}s]")
            sys.stdout.flush()
