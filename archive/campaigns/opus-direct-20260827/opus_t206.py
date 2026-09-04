"""
T206 - exact-continuum instrument (T202) + analytic Seeley-DeWitt coefficients
(T205), applied to the conformal channel and the transverse-traceless channel.

Answers directly: why did the traceless channel plateau at 1.000 while the
conformal channel did not?  Both lanes used the diagnostic
      OLDDIAG(x) = (Rlat - 1 - b2 x^2)/(b1 x)
which subtracts a TRUNCATED series.  IDEAL(x) is the same expression evaluated
on the EXACT continuum ratio, i.e. what the diagnostic reports at zero lattice
error.  Any departure of IDEAL from 1 is pure diagnostic artefact.
"""
import numpy as np, sys, time
from collections import Counter
from numpy.polynomial.legendre import leggauss
from opus_t205 import coeffs

XS, WS = leggauss(40)
def integ(fun, lo, hi):
    lo = np.asarray(lo, float); hi = np.asarray(hi, float)
    p = 0.5*(lo+hi)[:, None] + 0.5*(hi-lo)[:, None]*XS[None, :]
    return 0.5*(hi-lo)*np.sum(WS[None, :]*fun(p), axis=1)

def weights(chan, eps, kappa):
    psi = lambda x: np.cos(kappa*x)
    def gm(x, m):
        o = np.ones_like(np.asarray(x, float))
        return o + chan[m]*eps*psi(x) if m in chan else o
    sg = lambda x: np.sqrt(np.prod([gm(x, m) for m in range(4)], axis=0))
    W = [(lambda x, m=m: sg(x)/gm(x, m)) for m in range(4)]
    trg4 = lambda x: sum(gm(x, m) for m in range(4))/4.0
    return W, sg, trg4

def sqhist(J, k):
    j = np.arange(-J, J+1); c = Counter((j*j).tolist()); r = Counter({0: 1})
    for _ in range(k):
        nr = Counter()
        for a, na in r.items():
            for b, nb in c.items(): nr[a+b] += na*nb
        r = nr
    return r

def cont_heat(L, chan, eps, n, sv, J):
    tp = 2*np.pi/L; W, sg, _ = weights(chan, eps, tp*n)
    x = np.arange(8192)*L/8192
    FW = [np.fft.fft(w(x))/8192 for w in W]; FR = np.fft.fft(sg(x))/8192
    Ng = len(FR)
    grp = {}
    for m in (1, 2, 3): grp.setdefault(np.round(np.real(FW[m][:16]), 12).tobytes(), []).append(m)
    gl = list(grp.values())
    acc = [((), 1)]
    for g in gl:
        h = sqhist(J, len(g))
        acc = [(t+(v,), mm*m2) for (t, mm) in acc for v, m2 in h.items()]
    out = np.zeros(len(sv))
    for r in range(n):
        j0 = np.array([v for v in range(-J, J+1) if (v-r) % n == 0], float)
        k0 = j0*tp; nb = len(k0)
        d = (np.arange(nb)[:, None]-np.arange(nb)[None, :])*n
        M = np.real(FR[d % Ng]); A0 = (k0[:, None]*k0[None, :])*np.real(FW[0][d % Ng])
        Wg = [np.real(FW[g[0]][d % Ng]) for g in gl]
        ev, U = np.linalg.eigh(M); Mih = (U/np.sqrt(ev)) @ U.T
        for tup, mult in acc:
            A = A0.copy()
            for gi, q2i in enumerate(tup): A += (q2i*tp*tp)*Wg[gi]
            B = Mih @ A @ Mih; B = 0.5*(B+B.T)
            lam = np.linalg.eigvalsh(B); np.maximum(lam, 0.0, out=lam)
            out += mult*np.exp(-np.outer(sv, lam)).sum(axis=1)
    return out

def lat_heat(L, chan, eps, n, sv, improved):
    kap = 2*np.pi*n/L; W, sg, trg4 = weights(chan, eps, kap)
    t = np.arange(L, dtype=float)
    w0 = integ(W[0], t, t+1.0); wt = [integ(W[m], t-.5, t+.5) for m in (1, 2, 3)]
    m_ = integ(sg, t-.5, t+.5); C = trg4(t)
    isq = 1/np.sqrt(m_); idx = np.arange(L)
    K0 = np.zeros((L, L)); K0[idx, idx] += w0 + np.roll(w0, 1)
    jp = (idx+1) % L; K0[idx, jp] -= w0; K0[jp, idx] -= w0
    grp = {}
    for i, v in enumerate(wt): grp.setdefault(np.round(v, 12).tobytes(), []).append(i)
    gl = list(grp.values())
    e1 = 2*(1-np.cos(2*np.pi*np.arange(L)/L))
    def h1(k):
        c = Counter(np.round(e1, 12).tolist()); r = Counter({0.0: 1})
        for _ in range(k):
            nr = Counter()
            for a, na in r.items():
                for b, nb in c.items(): nr[round(a+b, 12)] += na*nb
            r = nr
        return r
    acc = [((), 1)]
    for g in gl:
        h = h1(len(g)); acc = [(t2+(v,), mm*m2) for (t2, mm) in acc for v, m2 in h.items()]
    wgs = [wt[g[0]] for g in gl]; out = np.zeros(len(sv))
    for tup, mult in acc:
        K = K0.copy(); dgv = np.zeros(L)
        for gi, ev in enumerate(tup): dgv += ev*wgs[gi]
        K[idx, idx] += dgv
        B = (isq[:, None]*K)*isq[None, :]
        if improved:
            B = B + ((B*C[None, :]) @ B)/24.0; B = 0.5*(B+B.T)
        lam = np.linalg.eigvalsh(B); np.maximum(lam, 0.0, out=lam)
        out += mult*np.exp(-np.outer(sv, lam)).sum(axis=1)
    return out

def e2(fn, h=0.05):
    v = {e: fn(e*h) for e in (-2, -1, 0, 1, 2)}
    return 0.5*(-v[2]+16*v[1]-30*v[0]+16*v[-1]-v[-2])/(12*h*h)

if __name__ == "__main__":
    L = int(sys.argv[1]) if len(sys.argv) > 1 else 64
    n = 2; kap = 2*np.pi*n/L; k2 = kap**2
    xs = np.array([0.25, 0.4, 0.6, 0.8, 1.0, 1.4, 2.0, 3.0]); sv = xs/k2
    J = 30
    CH = {"CONFORMAL": {0: 1, 1: 1, 2: 1, 3: 1}, "TRACELESS-TT": {1: 1, 2: -1}}
    print(f"=== L={L} n={n} J={J} ===")
    print("x               : " + " ".join(f"{q:8.2f}" for q in xs))
    for name, ch in CH.items():
        t0 = time.time()
        V2c, b1, b2 = coeffs(ch, L, n)
        V2 = V2c*L**3
        Rc = (4*np.pi*sv)**2*e2(lambda e: cont_heat(L, ch, e, n, sv, J))/V2
        ideal = (Rc-1.0-b2*xs**2)/(b1*xs)
        print(f"\n-- {name}   b1={b1:.6f}  b2={b2:.6f}  |b2/b1|={abs(b2/b1):.4f}  [{time.time()-t0:.0f}s]")
        print("   Rcont        : " + " ".join(f"{q:8.5f}" for q in Rc))
        print("   IDEAL (no a) : " + " ".join(f"{q:8.4f}" for q in ideal))
        for imp in (True, False):
            Rl = (4*np.pi*sv)**2*e2(lambda e: lat_heat(L, ch, e, n, sv, imp))/V2
            tag = "IMPR " if imp else "plain"
            print(f"   {tag} lat-cont: " + " ".join(f"{q:8.1e}" for q in Rl-Rc))
            print(f"   {tag} OLDDIAG : " + " ".join(f"{q:8.4f}" for q in (Rl-1.0-b2*xs**2)/(b1*xs)))
