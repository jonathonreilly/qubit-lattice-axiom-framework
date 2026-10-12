"""R13-4 (i): fast high-precision check of Lemma Q (the BF quotient reduction identity) by nested
central differences in mpmath (dps 50, h 1e-18), on the same toys as r134_oneill_check.py:
   H_q omega := 1/2 (Q P_h Q* omega + P_h Q* Q omega)
            ?= P_h H_flat omega - 1/2 P_h sum_st X_s^dag g^-1_st X_t omega,
for basic omega (pullbacks of forms in gauge invariants).  Q = d + dW^, Q* = sum_a iota_a(-d_a + d_a W).
T1: one generator on (A, phi in R^4).  T2: two sites + one link (9 coordinates), so g^-1 has an
off-diagonal (s != t) entry: the 'distant' pair-transfer piece is isolated and its size printed.
Controls: P_h H_flat alone (drops the four-fermion term); flat H_flat (no projection)."""
import mpmath as mp
mp.mp.dps = 50
H = mp.mpf('1e-18')

def wedge1(alpha, form, n):
    out = {}
    for I, c in form.items():
        for a in range(n):
            if a in I or alpha[a] == 0: continue
            pos = sum(1 for i in I if i < a)
            J = tuple(sorted(I + (a,)))
            out[J] = out.get(J, 0) + (-1)**pos * alpha[a]*c
    return out

def iota(v, form):
    out = {}
    for I, c in form.items():
        for p, a in enumerate(I):
            if v[a] == 0: continue
            J = I[:p] + I[p+1:]
            out[J] = out.get(J, 0) + (-1)**p * v[a]*c
    return out

def add(*fs):
    out = {}
    for f in fs:
        for I, c in f.items():
            out[I] = out.get(I, 0) + c
    return out

def scal(f, k):
    return {I: k*c for I, c in f.items()}

def shift(x, a, d):
    y = list(x); y[a] += d; return y

def make(n, Wf, uf, ginvf):
    def dW(x):
        return [(Wf(shift(x, a, H)) - Wf(shift(x, a, -H)))/(2*H) for a in range(n)]
    def Q(f):
        def g(x):
            out = {}; w = dW(x); f0 = f(x)
            for a in range(n):
                fp, fm = f(shift(x, a, H)), f(shift(x, a, -H))
                da = {I: (fp.get(I, 0) - fm.get(I, 0))/(2*H) + w[a]*f0.get(I, 0) for I in set(fp) | set(fm) | set(f0)}
                e = [0]*n; e[a] = 1
                out = add(out, wedge1(e, da, n))
            return out
        return g
    def Qs(f):
        def g(x):
            out = {}; w = dW(x); f0 = f(x)
            for a in range(n):
                fp, fm = f(shift(x, a, H)), f(shift(x, a, -H))
                da = {I: -(fp.get(I, 0) - fm.get(I, 0))/(2*H) + w[a]*f0.get(I, 0) for I in set(fp) | set(fm) | set(f0)}
                e = [0]*n; e[a] = 1
                out = add(out, iota(e, da))
            return out
        return g
    def Ph(f):
        def g(x):
            f0 = f(x); us = uf(x); gi = ginvf(x); out = dict(f0)
            for s in range(len(us)):
                for t in range(len(us)):
                    out = add(out, scal(wedge1(us[s], iota(us[t], f0), n), -gi[s][t]))
            return out
        return g
    def Iu(t, f):
        return lambda x: iota(uf(x)[t], f(x))
    def Wu(s, f):
        return lambda x: wedge1(uf(x)[s], f(x), n)
    def mul(k, f):
        return lambda x: scal(f(x), k(x))
    def plus(*fs):
        return lambda x: add(*[f(x) for f in fs])
    return Q, Qs, Ph, Iu, Wu, mul, plus

def norm(f):
    return max([abs(v) for v in f.values()] + [mp.mpf(0)])

def diffn(f1, f2):
    keys = set(f1) | set(f2)
    return max([abs(f1.get(k, 0) - f2.get(k, 0)) for k in keys] + [mp.mpf(0)])

def R4(th):
    c, s = mp.cos(th), mp.sin(th)
    return [[c, -s, 0, 0], [s, c, 0, 0], [0, 0, c, -s], [0, 0, s, c]]
def mv(M, v): return [sum(M[i][j]*v[j] for j in range(4)) for i in range(4)]
Jm = [[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]]
Km = [[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]]
e = mp.mpf('0.7')

out = []
def pr(*a):
    s_ = " ".join(str(x) for x in a); print(s_, flush=True); out.append(s_)

def report(tag, n, Wf, uf, ginvf, omega, x0, offdiag=None):
    Q, Qs, Ph, Iu, Wu, mul, plus = make(n, Wf, uf, ginvf)
    m = len(uf(x0))
    Hq = plus(mul(lambda x: mp.mpf(1)/2, Q(Ph(Qs(omega)))), mul(lambda x: mp.mpf(1)/2, Ph(Qs(Q(omega)))))
    Hflat = plus(mul(lambda x: mp.mpf(1)/2, Q(Qs(omega))), mul(lambda x: mp.mpf(1)/2, Qs(Q(omega))))
    terms = []
    for s in range(m):
        for t in range(m):
            Xt = plus(Iu(t, Qs(omega)), Qs(Iu(t, omega)))                 # X_t omega
            gX = mul(lambda x, s=s, t=t: ginvf(x)[s][t], Xt)
            XdX = plus(Q(Wu(s, gX)), Wu(s, Q(gX)))                        # X_s^dag (g^-1_st X_t omega)
            terms.append(((s, t), Ph(XdX)))
    L = Hq(x0); P0 = Ph(Hflat)(x0)
    four = add(*[f(x0) for _, f in terms])
    Rr = add(P0, scal(four, -mp.mpf(1)/2))
    hor = max(norm(Iu(t, omega)(x0)) for t in range(m))
    pr(f"{tag}: |iota_u omega| = {mp.nstr(hor, 3)}; |H_q omega| = {mp.nstr(norm(L), 6)}; "
       f"|H_q - RHS| = {mp.nstr(diffn(L, Rr), 3)}; control |H_q - P_h H_flat| = {mp.nstr(diffn(L, P0), 6)}; "
       f"control |H_q - H_flat| = {mp.nstr(diffn(L, Hflat(x0)), 6)}; |iota_u H_q omega| = "
       f"{mp.nstr(max(norm(iota(uf(x0)[t], L)) for t in range(m)), 3)}")
    if m > 1:
        off = add(*[f(x0) for (st, f) in terms if st[0] != st[1]])
        pr(f"   s!=t part (-1/2 P_h X_s^dag g^-1_st X_t, the 'distant' transfer): |.| = {mp.nstr(norm(scal(off, mp.mpf(1)/2)), 6)}; "
           f"g^-1 = {[[mp.nstr(v, 5) for v in row] for row in ginvf(x0)]}")
    # X is algebraic: compare X_t omega with i T contraction computed at x0 only (no derivative needed)
    return L

# ---------------- T1
def y1(x):   # invariants y = R(-eA) phi
    return mv(R4(-e*x[0]), x[1:5])
def dy1(x):
    R = R4(-e*x[0]); ph = x[1:5]
    dA = [-e*v for v in mv(Jm, mv(R, ph))]          # d/dA R(-eA) phi = -e J R phi
    return [[dA[i]] + [R[i][j] for j in range(4)] for i in range(4)]
def W1(x):
    y = y1(x)
    return (y[0]**2 + 2*y[1]**2 + 3*y[2]**2 + y[3]**2/2)/2 + mp.mpf('0.3')*y[0]*y[2] + (y[0]**2 + y[1]**2)*(y[2]**2 + y[3]**2)/10
def u1(x):
    return [[1] + [e*v for v in mv(Jm, x[1:5])]]
def gi1(x):
    return [[1/(1 + e**2*sum(v**2 for v in x[1:5]))]]
def pull(coefs, dyf, n):
    def om(x):
        y = (y1 if n == 5 else None)(x) if n == 5 else None
        D = dyf(x); res = {}
        for cf, idx in coefs:
            f = {(): cf(x)}
            for i in reversed(idx):
                f = wedge1(D[i], f, n)
            res = add(res, f)
        return res
    return om
F1 = [lambda x: (lambda y: mp.exp(-(y[0]**2 + y[1]**2 + y[2]**2 + y[3]**2)/4)*(1 + y[0] + y[1]*y[2] - y[3]**2 + y[0]*y[3]/3))(y1(x)),
      lambda x: (lambda y: mp.exp(-(y[0]**2 + 2*y[1]**2 + y[2]**2 + y[3]**2)/5)*(y[1] - y[2] + 2*y[0]*y[3]))(y1(x)),
      lambda x: (lambda y: mp.exp(-(2*y[0]**2 + y[1]**2 + y[2]**2 + y[3]**2)/6)*(1 - y[3] + y[1]**2))(y1(x))]
