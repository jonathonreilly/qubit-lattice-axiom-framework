"""R13-4 (iii): maximal group velocity over the whole zone, and commutator leakage
outside the c = 1 light cone, for the box laws (R7-1 / R9-5 matter; R8-5 photon; R8-5
Wilson-box Dirac), against NN comparators.

Subtraction (named before the run, R9-3 rule): the leakage is the free Klein-Gordon
commutator function  D(r,t) = (1/2pi) int cos(k r) sin(E(k) t)/E(k) dk  of the law's
dispersion.  The continuum comparator D_cont vanishes identically for r > t, so the
subtracted quantity D - D_cont equals D itself outside the cone.  No channel limit is
subtracted.  d = 1 (axis profile); the d-dim group velocities are maximized on grids.
"""
import numpy as np
np.set_printoptions(linewidth=160)

def sstep(x):   # R7-1's Gevrey-2 step (r71_box_poincare_free.py:20-26), 0 at x<=0, 1 at x>=1
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)

def wrap(k):
    return -(((-k) + np.pi) % (2*np.pi) - np.pi)

def s_box(b, b2):
    def s(k):
        k = wrap(k); r = sstep((b2 - np.abs(k))/(b2 - b))
        return r*k + (1-r)*np.sin(k)
    return s

def d_photon(c1, c2):        # R8-5 photon symbol (r85_box_qed.py:38-58): rho q + (1-rho) 2 sin(q/2)
    def d(q):
        q = wrap(q); r = 1.0 - sstep((np.abs(q) - c1)/(c2 - c1))
        return r*q + (1-r)*2*np.sin(q/2)
    return d

def W_box(b, b2, rr):
    def W(k):
        k = wrap(k); r = sstep((b2 - np.abs(k))/(b2 - b))
        return rr*(1-r)*(1-np.cos(k))
    return W

def deriv(f, k, h=1e-5):
    return (f(k+h) - f(k-h))/(2*h)

def vmax_scalar(s, m, d, N):
    """max |grad E| over T^d, E = sqrt(m^2 + sum s(k_i)^2)."""
    k = np.linspace(-np.pi, np.pi, N, endpoint=False) + np.pi/N
    sv, dv = s(k), deriv(s, k)
    best = 0.0; arg = None
    if d == 1:
        E = np.sqrt(m*m + sv**2); v = np.abs(sv*dv)/E
        i = np.argmax(v); return v[i], (k[i],)
    if d == 2:
        S2 = sv[:, None]**2 + sv[None, :]**2
        E = np.sqrt(m*m + S2)
        g = np.sqrt((sv*dv)[:, None]**2 + (sv*dv)[None, :]**2)/E
        i = np.unravel_index(np.argmax(g), g.shape); return g[i], (k[i[0]], k[i[1]])
    for a in range(N):   # d = 3, sliced
        S2 = sv[a]**2 + sv[:, None]**2 + sv[None, :]**2
        E = np.sqrt(m*m + S2)
        g = np.sqrt((sv[a]*dv[a])**2 + (sv*dv)[:, None]**2 + (sv*dv)[None, :]**2)/E
        j = np.unravel_index(np.argmax(g), g.shape)
        if g[j] > best: best, arg = g[j], (k[a], k[j[0]], k[j[1]])
    return best, arg

def vmax_wilson_dirac(S, W, m, d, N):
    """E^2 = (m + sum W)^2 + sum S^2 (R8-5 Wilson-box Dirac, one band)."""
    k = np.linspace(-np.pi, np.pi, N, endpoint=False) + np.pi/N
    Sv, dS, Wv, dW = S(k), deriv(S, k), W(k), deriv(W, k)
    if d == 2:
        Mw = m + Wv[:, None] + Wv[None, :]
        E = np.sqrt(Mw**2 + Sv[:, None]**2 + Sv[None, :]**2)
        gx = (Mw*dW[:, None] + (Sv*dS)[:, None])/E
        gy = (Mw*dW[None, :] + (Sv*dS)[None, :])/E
        g = np.sqrt(gx**2 + gy**2)
        i = np.unravel_index(np.argmax(g), g.shape); return g[i], (k[i[0]], k[i[1]])
    best = 0; arg = None
    for a in range(N):
        Mw = m + Wv[a] + Wv[:, None] + Wv[None, :]
        E = np.sqrt(Mw**2 + Sv[a]**2 + Sv[:, None]**2 + Sv[None, :]**2)
        gx = (Mw*dW[a] + Sv[a]*dS[a])/E
        gy = (Mw*dW[:, None] + (Sv*dS)[:, None])/E
        gz = (Mw*dW[None, :] + (Sv*dS)[None, :])/E
        g = np.sqrt(gx**2 + gy**2 + gz**2)
        j = np.unravel_index(np.argmax(g), g.shape)
        if g[j] > best: best, arg = g[j], (k[a], k[j[0]], k[j[1]])
    return best, arg

out = []
def pr(*a):
    s_ = " ".join(str(x) for x in a); print(s_); out.append(s_)

pr("(A) maximal group velocity over the whole zone (c = 1 inside every box)")
laws = [("R7-1/R9-5 matter b=2.0,b2=3.1,m=0.3", s_box(2.0, 3.1), 0.3),
        ("R7-1 matter (script 2) b=2.6,b2=3.0,m=0.3", s_box(2.6, 3.0), 0.3),
        ("R7-1 matter b=2.0,b2=3.1, m=0.01", s_box(2.0, 3.1), 0.01),
        ("NN naive matter s=sin k, m=0.3", np.sin, 0.3),
        ("NN KG matter s=2sin(k/2), m=0.3", lambda k: 2*np.sin(wrap(k)/2), 0.3),
        ("R8-5 photon d, plateau (1,2), m=0", d_photon(1.0, 2.0), 0.0),
        ("R8-5 photon d, plateau (2,3), m=0", d_photon(2.0, 3.0), 0.0),
        ("Yee photon 2sin(q/2), m=0", lambda k: 2*np.sin(wrap(k)/2), 0.0)]
for name, s, m in laws:
    v1, a1 = vmax_scalar(s, m, 1, 20000)
    v2, a2 = vmax_scalar(s, m, 2, 1200)
    v3, a3 = vmax_scalar(s, m, 3, 240)
    pr(f"  {name:45s} v_max d=1: {v1:.4f} at k={np.round(a1,3)} | d=2: {v2:.4f} | d=3: {v3:.4f} at {np.round(a3,3)}")
# photon with the R8-5 midpoint phase: the symbol |D_j| = |d(q_j)| is 2pi-periodic in |.|; its 1D 'dispersion'
# |d(q)| is evaluated directly above (wrap to (-pi,pi], d odd => |d| even).
for (b1, b2, rr, m) in [(2.0, 3.0, 1.0, 0.1), (0.8, 2.0, 1.0, 0.3)]:
    S = s_box(b1, b2); W = W_box(b1, b2, rr)
    v2, a2 = vmax_wilson_dirac(S, W, m, 2, 1200); v3, a3 = vmax_wilson_dirac(S, W, m, 3, 200)
    pr(f"  R8-5 Wilson-box Dirac b1={b1},b2={b2},r={rr},m={m}: v_max d=2: {v2:.4f} | d=3: {v3:.4f} at {np.round(a3,3)}")

pr("\n(B) Lemma V (mean-value bound): any C^1 odd 2pi-periodic s with s(k)=k on |k|<=b has, along an axis,")
pr("    max |dE/dk| >= (sqrt(m^2+b^2) - m)/(pi - b)  (since s(pi)=0).  Threshold b*(m) where the bound = 1:")
for m in [0.0, 0.01, 0.1, 0.3, 0.5]:
    lo, hi = 0.1, 3.1
    for _ in range(80):
        mid = 0.5*(lo+hi)
        if (np.sqrt(m*m+mid*mid) - m)/(np.pi - mid) > 1: hi = mid
        else: lo = mid
    pr(f"    m={m:4.2f}: b* = {lo:.5f}   bound at b=2.0: {(np.sqrt(m*m+4)-m)/(np.pi-2):.4f}, at b=2.6: {(np.sqrt(m*m+2.6**2)-m)/(np.pi-2.6):.4f}")

pr("\n(C) subluminal box laws exist for b < b*: scan of v_max (d=3) for s_box(b, b2=3.1)")
for m in [0.3, 0.01]:
    for b in [1.0, 1.2, 1.4, 1.5, 1.6, 1.7]:
        v3, a3 = vmax_scalar(s_box(b, 3.1), m, 3, 160)
        v1, _ = vmax_scalar(s_box(b, 3.1), m, 1, 20000)
        pr(f"    m={m}, b={b}: v_max d=1 {v1:.4f}, d=3 {v3:.4f}")

# ---------------------------------------------------------------- (D) leakage outside the c=1 cone
pr("\n(D) KG commutator D(r,t) outside the c=1 cone, d=1 (subtraction: D_cont = 0 for r>t)")
NQ = 2**21
kq = (np.arange(NQ) + 0.5)*2*np.pi/NQ - np.pi
def Dfun(E, r, t):
    w = np.sin(E*t)/np.where(E > 0, E, 1.0); w = np.where(E > 0, w, t)
    return np.array([np.sum(np.cos(kq*ri)*w)/NQ for ri in r])
cases = [("R7-1 matter b=2,b2=3.1,m=0.3", np.sqrt(0.09 + s_box(2.0, 3.1)(kq)**2)),
         ("subluminal box b=1.5,b2=3.1,m=0.3", np.sqrt(0.09 + s_box(1.5, 3.1)(kq)**2)),
         ("NN KG m=0.3", np.sqrt(0.09 + 4*np.sin(kq/2)**2)),
         ("R8-5 photon (1,2)", np.abs(d_photon(1.0, 2.0)(kq))),
         ("Yee photon", np.abs(2*np.sin(kq/2)))]
for t in [100, 400]:
    xs = np.array([1, 2, 5, 10, 20, 40, 80, 160, 320, 640])
    pr(f"  t = {t}: x = r - t = {list(xs)}")
    for name, E in cases:
        # max |D| over a window of 4 sites at each distance (oscillatory)
        vals = []
        for x in xs:
            r = t + x + np.arange(0, 4)
            vals.append(np.max(np.abs(Dfun(E, r, t))))
        pr(f"    {name:36s} " + " ".join(f"{v:.1e}" for v in vals))
pr("  in-cone reference |D| at r = t/2: " + " ".join(
    f"{name.split()[0]}:{np.max(np.abs(Dfun(E, np.arange(200, 204), 400))):.1e}" for name, E in cases))

pr("\n(E) power law inside the superluminal window: R7-1 law, |D| max over r in [1.2t, 1.3t]")
E = cases[0][1]
for t in [50, 100, 200, 400, 800]:
    r = np.arange(int(1.2*t), int(1.3*t) + 1)
    v = np.max(np.abs(Dfun(E, r, t)))
    pr(f"    t={t:4d}: {v:.3e}   t^0.5*|D| = {v*np.sqrt(t):.3f}")
with open(__file__.replace('.py', '.out'), 'w') as f:
    f.write("\n".join(out) + "\n")
