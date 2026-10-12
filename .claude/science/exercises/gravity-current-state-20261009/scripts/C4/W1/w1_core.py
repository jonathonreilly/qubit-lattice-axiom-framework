"""W1 (lane RW, C4): O(lambda^2) uniform-strain TT response of onsite phi^4 with the most general local
O(lambda) vertex dressing, in the RN L2 design (free part = unitary strain flow of H2, phi transported as a density).

Coupling: H(h) = U_h H2 U_h^dag + lam :H4:_0 + lam*eps*sum_a c_a :O_a:_0 ,
  H4 = (1/24) sum_x phi_x^4 (vertex V(k)=1),  O_a = local quartic operators (vertex b_a(k) on K=0), range <= r,
  projected on the E (h=eps diag(1,-1,0)) or T2 (h_xy=h_yx=eps) cubic channel.  Normal ordering w.r.t. the
  UNSTRAINED free vacuum = tadpole-subtracted design (RN L2); <phi^2> is flow-invariant so no O(lam) term.
Then exactly at O(lam^2):
  E2/V(eps) = -(1/24) int_{K=0} |V + eps d|^2 w_eps,   w_eps(k) = int_0^inf dt prod_i g_{t,eps}(k_i),
  g_{t,eps}(k) = J(k) exp(-t W(Phi k)) / (2 W(Phi k)).
  mu2(c) = d^2/deps^2 = -(1/24) [A + 4 c.L + 2 c^T Q c],
  A = d^2 int V^2 w, L_a = d/deps int V b_a w, Q_ab = int b_a b_b w  (eps=0).
Position space: int_{K=0} prod_i e^{i k_i.a_i} prod g(k_i) = sum_x prod_i g(x+a_i).
"""
import numpy as np, itertools

# ---------------- t quadrature: 1/s = sum_n wt_n exp(-s t_n) on s in [smin, smax]
def tquad(n=28, beta=9.0):
    u, wu = np.polynomial.laguerre.laggauss(n)
    return u/beta, wu*np.exp(u)/beta

def check_tquad(tn, wn, smin, smax):
    s = np.linspace(smin, smax, 2001)
    approx = (wn[None, :]*np.exp(-np.outer(s, tn))).sum(1)
    return np.max(np.abs(approx*s - 1))

# ---------------- flows (copied from RN L2 l2_sunset_mu.py; f = sin k)
def flow1d(k, eps, nsteps=400):
    x = k.copy(); J = np.ones_like(k); h = 1.0/nsteps
    f = np.sin; fp = np.cos
    for _ in range(nsteps):
        def rhs(x, J): return eps*f(x), eps*fp(x)*J
        a1, b1 = rhs(x, J); a2, b2 = rhs(x+h/2*a1, J+h/2*b1); a3, b3 = rhs(x+h/2*a2, J+h/2*b2); a4, b4 = rhs(x+h*a3, J+h*b3)
        x = x + h/6*(a1+2*a2+2*a3+a4); J = J + h/6*(b1+2*b2+2*b3+b4)
    return x, J

def flow2d_T2(kx, ky, eps, nsteps=400):
    x, y = kx.copy(), ky.copy(); h = 1.0/nsteps; f = np.sin
    for _ in range(nsteps):
        def rhs(x, y): return eps*f(y), eps*f(x)
        a1, b1 = rhs(x, y); a2, b2 = rhs(x+h/2*a1, y+h/2*b1); a3, b3 = rhs(x+h/2*a2, y+h/2*b2); a4, b4 = rhs(x+h*a3, y+h*b3)
        x = x + h/6*(a1+2*a2+2*a3+a4); y = y + h/6*(b1+2*b2+2*b3+b4)
    return x, y

def wdisp(kx, ky, kz, m):
    return np.sqrt(m**2 + 4*np.sin(kx/2)**2 + 4*np.sin(ky/2)**2 + 4*np.sin(kz/2)**2)

def strained(L, m, eps, ch):
    k1 = 2*np.pi*np.fft.fftfreq(L)
    KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij')
    if eps == 0:
        return np.ones_like(KX), wdisp(KX, KY, KZ, m)
    if ch == 'E':
        px, jx = flow1d(k1, eps); py, jy = flow1d(k1, -eps)
        PX = px[:, None, None]*np.ones((1, L, L)); PY = py[None, :, None]*np.ones((L, 1, L)); PZ = KZ
        J = jx[:, None, None]*jy[None, :, None]*np.ones((1, 1, L))
    else:
        ax, ay = np.meshgrid(k1, k1, indexing='ij'); fx, fy = flow2d_T2(ax, ay, eps)
        PX = fx[:, :, None]*np.ones((1, 1, L)); PY = fy[:, :, None]*np.ones((1, 1, L)); PZ = KZ
        J = np.ones((L, L, L))
    return J, wdisp(PX, PY, PZ, m)

def gx_from_k(Jk, Wk, tn):
    """g_n(x) for all t-nodes: array (nt, L, L, L)"""
    gk = Jk[None]*np.exp(-tn[:, None, None, None]*Wk[None])/(2*Wk[None])
    return np.fft.ifftn(gk, axes=(1, 2, 3)).real

def gdot_x(L, m, ch, tn):
    """exact first eps-derivative of g_{t,eps}(k) at eps=0, in position space"""
    k1 = 2*np.pi*np.fft.fftfreq(L)
    KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij')
    W = wdisp(KX, KY, KZ, m)
    if ch == 'E':
        Jd = np.cos(KX) - np.cos(KY); Wd = (np.sin(KX)**2 - np.sin(KY)**2)/W
    else:
        Jd = np.zeros_like(KX); Wd = 2*np.sin(KX)*np.sin(KY)/W
    base = np.exp(-tn[:, None, None, None]*W[None])/(2*W[None])
    gdk = base*(Jd[None] - Wd[None]*(tn[:, None, None, None] + 1/W[None]))
    return np.fft.ifftn(gdk, axes=(1, 2, 3)).real

# ---------------- cubic group
def cubic_group():
    G = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product([1, -1], repeat=3):
            R = np.zeros((3, 3), int)
            for i in range(3): R[i, p[i]] = s[i]
            G.append(R)
    return G
GROUP = cubic_group()

def canon(pts):
    pts = sorted(tuple(int(v) for v in p) for p in pts)
    o = pts[0]
    return tuple(sorted(tuple(a-b for a, b in zip(p, o)) for p in pts))

def enumerate_monomials(r):
    """canonical 4-multisets of lattice points with max pairwise l1 distance <= r (mod translation)"""
    ball = [p for p in itertools.product(range(-r, r+1), repeat=3) if sum(map(abs, p)) <= r]
    out = set()
    for comb in itertools.combinations_with_replacement(ball, 4):
        ok = all(sum(abs(a-b) for a, b in zip(p, q)) <= r for p, q in itertools.combinations(comb, 2))
        if ok: out.add(canon(comb))
    return sorted(out)

def act(R, mono):
    return canon([tuple(R @ np.array(p)) for p in mono])

def orbits(monos):
    seen = set(); orbs = []
    for mo in monos:
        if mo in seen: continue
        orb = sorted(set(act(R, mo) for R in GROUP))
        seen.update(orb); orbs.append(orb)
    return orbs

HHAT = {'E': np.diag([1., -1., 0.]), 'T2': np.array([[0, 1., 0], [1., 0, 0], [0, 0, 0]])}
SEEDS = []
for i in range(3):
    for j in range(i, 3):
        T = np.zeros((3, 3)); T[i, j] = T[j, i] = 1.0; SEEDS.append(T)

def channel_functions(orbs, ch):
    """functions f = sum_{g} (R_g T R_g^T : hhat) b_{g m_rep}; returned as dict mono->coef"""
    hh = HHAT[ch]; funcs = []
    for orb in orbs:
        rep = orb[0]
        for T in SEEDS:
            coef = {}
            for R in GROUP:
                c = float(np.sum((R @ T @ R.T)*hh))
                if abs(c) < 1e-12: continue
                mo = act(R, rep); coef[mo] = coef.get(mo, 0.0) + c
            coef = {k: v for k, v in coef.items() if abs(v) > 1e-12}
            if coef: funcs.append(coef)
    return funcs

# ---------------- position-space machinery
class Field:
    def __init__(self, g, wn):
        self.g = g; self.wn = wn; self.cache = {}
    def sh(self, s):
        s = tuple(int(v) for v in s)
        if s not in self.cache:
            self.cache[s] = np.roll(self.g, shift=(-s[0], -s[1], -s[2]), axis=(1, 2, 3))
        return self.cache[s]

class FourPoint:
    """F(a1..a4) = sum_n wn sum_x prod_i g_n(x+a_i) with cubic-invariant g (eps=0): cached by canonical form"""
    def __init__(self, fld, use_sym=True):
        self.f = fld; self.cache = {}; self.use_sym = use_sym
    def key(self, pts):
        c = canon(pts)
        if not self.use_sym: return c
        return min(act(R, c) for R in GROUP)
    def __call__(self, pts):
        k = self.key(pts)
        if k not in self.cache:
            prod = self.f.sh(k[0])*self.f.sh(k[1])*self.f.sh(k[2])*self.f.sh(k[3])
            self.cache[k] = float(np.dot(self.f.wn, prod.reshape(prod.shape[0], -1).sum(1)))
        return self.cache[k]

PERMS = list(itertools.permutations(range(4)))

def inner_mono(F, m1, m2, sign=-1):
    """int b_m1 b_m2^* w (sign=-1) = (1/24) sum_sigma F(r_i - r'_sigma(i))"""
    tot = 0.0
    for s in PERMS:
        tot += F([tuple(np.array(m1[i]) + sign*np.array(m2[s[i]])) for i in range(4)])
    return tot/24.0

def L_mono(fld, fdot, mono):
    """d/deps int e^{i sum k_i r_i} w = sum_i sum_n wn sum_x gdot(x+r_i) prod_{j!=i} g(x+r_j)"""
    tot = 0.0
    for i in range(4):
        prod = fdot.sh(mono[i]).copy()
        for j in range(4):
            if j != i: prod = prod*fld.sh(mono[j])
        tot += float(np.dot(fld.wn, prod.reshape(prod.shape[0], -1).sum(1)))
    return tot

def onsite_I(L, m, eps, ch, tn, wn):
    J, W = strained(L, m, eps, ch)
    g = gx_from_k(J, W, tn)
    return float(np.dot(wn, (g**4).reshape(len(tn), -1).sum(1)))
