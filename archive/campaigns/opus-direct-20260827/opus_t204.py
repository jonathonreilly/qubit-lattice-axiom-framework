"""
T204 - the T202 exact-continuum instrument applied to BOTH channels, for a
general diagonal metric g = diag(g0,g1,g2,g3)(x0).

  conformal : g = (1+eps*cos(k x0)) * I        (tr g varies -> R89 coefficient)
  traceless : g = diag(1+eps*psi, 1-eps*psi, 1, 1)   (tr g == 4 pointwise)

For each channel it computes
  Rcont(x) : exact continuum ratio, plane-wave diagonalisation, no series
  Rlat(x)  : divergence-form lattice operator, plain and Symanzik-improved
  b1,b2    : the true a1 / a2 coefficients, FITTED from Rcont at small x
             (cross-checked against the hand-derived 1/4, 1/8 for conformal)
  IDEAL(x) : what the a2-subtracting diagnostic reports at ZERO lattice error
             = (Rcont - 1 - b2 x^2)/(b1 x)

Bilinear form for a diagonal metric:
   stiffness weight in direction mu :  sqrt(g) g^{mu mu}
   mass weight                      :  sqrt(g)
"""
import numpy as np, sys, time
from collections import Counter
from numpy.polynomial.legendre import leggauss

XS, WS = leggauss(40)

def integ(fun, lo, hi):
    lo = np.asarray(lo, float); hi = np.asarray(hi, float)
    pts = 0.5*(lo+hi)[:, None] + 0.5*(hi-lo)[:, None]*XS[None, :]
    return 0.5*(hi-lo)*np.sum(WS[None, :]*fun(pts), axis=1)

def channel(name, eps, kappa):
    """returns (weights[4], sqrtg, trg_over_4) as callables of x"""
    psi = lambda x: np.cos(kappa*x)
    if name == "conformal":
        g = lambda x, m: 1.0 + eps*psi(x)
        trg4 = lambda x: 1.0 + eps*psi(x)
    elif name == "traceless":
        def g(x, m):
            if m == 0: return 1.0 + eps*psi(x)
            if m == 1: return 1.0 - eps*psi(x)
            return np.ones_like(np.asarray(x, float))
        trg4 = lambda x: np.ones_like(np.asarray(x, float))
    else:
        raise ValueError(name)
    sg = lambda x: np.sqrt(np.prod([g(x, m) for m in range(4)], axis=0))
    W = [(lambda x, m=m: sg(x)/g(x, m)) for m in range(4)]
    return W, sg, trg4

# ---------------------------------------------------------------- continuum
def fourier(fun, L, Ngrid=8192):
    x = np.arange(Ngrid)*L/Ngrid
    return np.fft.fft(fun(x))/Ngrid

def cont_heat(L, eps, n, svals, J, name):
    tp = 2*np.pi/L
    W, sg, _ = channel(name, eps, tp*n)
    FW = [fourier(w, L) for w in W]
    FR = fourier(sg, L)
    Ng = len(FR)
    sv = np.asarray(svals, float)
    out = np.zeros(len(sv))
    # transverse directions with identical weight functions may be grouped
    keys = [np.round(np.abs(FW[m][:8]), 12).tobytes() for m in range(4)]
    groups = {}
    for m in (1, 2, 3):
        groups.setdefault(keys[m], []).append(m)
    glist = list(groups.values())
    j1 = np.arange(-J, J+1)
    def sq_hist(k):
        c = Counter((j1*j1).tolist())
        r = Counter({0: 1})
        for _ in range(k):
            nr = Counter()
            for a, na in r.items():
                for b, nb in c.items():
                    nr[a+b] += na*nb
            r = nr
        return r
    hists = [sq_hist(len(g)) for g in glist]
    combos = [({}, 1)]
    acc = [((), 1)]
    for h in hists:
        acc = [(t+(v,), m*mm) for (t, m) in acc for v, mm in h.items()]
    for r in range(n):
        j0 = np.array([v for v in range(-J, J+1) if (v-r) % n == 0], dtype=float)
        k0 = j0*tp; nb = len(k0)
        d = (np.arange(nb)[:, None]-np.arange(nb)[None, :])*n
        M = np.real(FR[d % Ng])
        W0 = np.real(FW[0][d % Ng])
        Wg = [np.real(FW[g[0]][d % Ng]) for g in glist]
        A0 = (k0[:, None]*k0[None, :])*W0
        ev, U = np.linalg.eigh(M); Mih = (U/np.sqrt(ev)) @ U.T
        for tup, mult in acc:
            A = A0.copy()
            for gi, q2i in enumerate(tup):
                A += (q2i*tp*tp)*Wg[gi]
            B = Mih @ A @ Mih; B = 0.5*(B+B.T)
            lam = np.linalg.eigvalsh(B); np.maximum(lam, 0.0, out=lam)
            out += mult*np.exp(-np.outer(sv, lam)).sum(axis=1)
    return out

# ------------------------------------------------------------------ lattice
def lat_heat(L, eps, n, svals, J_unused, name, improved=True):
    kappa = 2*np.pi*n/L
    W, sg, trg4 = channel(name, eps, kappa)
    t = np.arange(L, dtype=float)
    w0 = integ(W[0], t, t+1.0)
    wt = [integ(W[m], t-0.5, t+0.5) for m in (1, 2, 3)]
    m_ = integ(sg, t-0.5, t+0.5)
    C = trg4(t)
    isq = 1.0/np.sqrt(m_); idx = np.arange(L)
    K0 = np.zeros((L, L))
    K0[idx, idx] += w0 + np.roll(w0, 1)
    jp = (idx+1) % L
    K0[idx, jp] -= w0; K0[jp, idx] -= w0
    groups = {}
    for i, v in enumerate(wt):
        groups.setdefault(np.round(v, 12).tobytes(), []).append(i)
    glist = list(groups.values())
    e1 = 2*(1-np.cos(2*np.pi*np.arange(L)/L))
    def hist(k):
        c = Counter(np.round(e1, 12).tolist()); r = Counter({0.0: 1})
        for _ in range(k):
            nr = Counter()
            for a, na in r.items():
                for b, nb in c.items():
                    nr[round(a+b, 12)] += na*nb
            r = nr
        return r
    acc = [((), 1)]
    for g in glist:
        h = hist(len(g))
        acc = [(tp_+(v,), m*mm) for (tp_, m) in acc for v, mm in h.items()]
    sv = np.asarray(svals, float); out = np.zeros(len(sv))
    wgs = [wt[g[0]] for g in glist]
    for tup, mult in acc:
        K = K0.copy()
        dg = np.zeros(L)
        for gi, ev in enumerate(tup):
            dg += ev*wgs[gi]
        K[idx, idx] += dg
        B = (isq[:, None]*K)*isq[None, :]
        if improved:
            B = B + ((B*C[None, :]) @ B)/24.0; B = 0.5*(B+B.T)
        lam = np.linalg.eigvalsh(B); np.maximum(lam, 0.0, out=lam)
        out += mult*np.exp(-np.outer(sv, lam)).sum(axis=1)
    return out

def eps2(fn, h, *a, **k):
    f = {e: fn(*a, eps=e*h, **k) if False else None for e in ()}
    vals = {}
    for e in (-2, -1, 0, 1, 2):
        vals[e] = fn(e*h, *a, **k)
    d2 = (-vals[2] + 16*vals[1] - 30*vals[0] + 16*vals[-1] - vals[-2])/(12*h*h)
    return 0.5*d2, vals[0]

if __name__ == "__main__":
    L = int(sys.argv[1]) if len(sys.argv) > 1 else 64
    n = 2; J = 22
    kappa = 2*np.pi*n/L; k2 = kappa**2
    xs = np.array([0.05, 0.1, 0.15, 0.25, 0.4, 0.6, 0.8, 1.0, 1.4, 2.0, 3.0])
    sv = xs/k2
    print(f"=== L={L} n={n} kappa^2={k2:.6f} ===")
    print("x        : " + " ".join(f"{q:8.2f}" for q in xs))
    for name, V2 in (("conformal", L**4/2.0), ("traceless", -L**4/4.0)):
        t0 = time.time()
        c2, _ = eps2(lambda e: cont_heat(L, e, n, sv, J, name), 0.05)
        Rc = (4*np.pi*sv)**2*c2/V2
        # fit b1,b2 (the true a1,a2 coefficients) on the smallest x points
        msk = xs <= 0.25
        Vd = np.vstack([xs[msk], xs[msk]**2, xs[msk]**3]).T
        b1, b2, b3 = np.linalg.lstsq(Vd, Rc[msk]-1.0, rcond=None)[0]
        ideal = (Rc-1.0-b2*xs**2)/(b1*xs)
        print(f"\n-- {name}  Vol2={V2:.4g}   fitted b1={b1:.6f}  b2={b2:.6f}  b3={b3:.6f}"
              f"   |b3|/b1={abs(b3)/b1:.4f}   [{time.time()-t0:.1f}s]")
        if name == "conformal":
            print(f"   hand-derived prediction:  b1=0.250000  b2=0.125000  "
                  f"-> err {abs(b1-0.25):.2e}, {abs(b2-0.125):.2e}")
        print("   Rcont  : " + " ".join(f"{q:8.5f}" for q in Rc))
        print("   IDEAL  : " + " ".join(f"{q:8.4f}" for q in ideal))
        for imp in (True, False):
            lk2, _ = eps2(lambda e: lat_heat(L, e, n, sv, J, name, imp), 0.05)
            Rl = (4*np.pi*sv)**2*lk2/V2
            tag = "IMPR " if imp else "plain"
            print(f"   {tag} lat-cont : " + " ".join(f"{q:8.1e}" for q in Rl-Rc))
            print(f"   {tag} OLDDIAG  : " + " ".join(f"{q:8.4f}" for q in (Rl-1.0-b2*xs**2)/(b1*xs)))
