"""sp55_kill: exact checks of the stereographic / Killing-field formulas used in SPHERE55 (criteria: sp55_kill_criteria.md).
Pure Python, fractions.Fraction only; derivatives by first-order forward-mode dual numbers over Q (exact)."""
from fractions import Fraction as Fr
import random

class D:
    """first-order dual number over Q with an n-vector of infinitesimal parts"""
    __slots__ = ("v", "g")
    def __init__(self, v, g):
        self.v = Fr(v); self.g = tuple(Fr(t) for t in g)
    @staticmethod
    def c(v, n): return D(v, (0,)*n)
    def _w(self, o): return o if isinstance(o, D) else D.c(o, len(self.g))
    def __add__(self, o): o = self._w(o); return D(self.v+o.v, tuple(a+b for a, b in zip(self.g, o.g)))
    __radd__ = __add__
    def __neg__(self): return D(-self.v, tuple(-a for a in self.g))
    def __sub__(self, o): return self + (-self._w(o))
    def __rsub__(self, o): return self._w(o) - self
    def __mul__(self, o):
        o = self._w(o); return D(self.v*o.v, tuple(self.v*b + o.v*a for a, b in zip(self.g, o.g)))
    __rmul__ = __mul__
    def __truediv__(self, o):
        o = self._w(o); inv = 1/o.v
        return D(self.v*inv, tuple((a*o.v - self.v*b)*inv*inv for a, b in zip(self.g, o.g)))
    def __rtruediv__(self, o): return self._w(o)/self

def seed(x):
    n = len(x); return [D(x[i], tuple(1 if j == i else 0 for j in range(n))) for i in range(n)]
def dot(a, b): return sum((p*q for p, q in zip(a, b)), Fr(0))
def jac(F, x):
    """Jacobian rows=outputs, cols=inputs"""
    out = F(seed(x)); return [list(o.g) for o in out], [o.v for o in out]

def Xmap(R):
    def F(x):
        n2 = dot(x, x); den = n2 + R*R
        return [2*R*R*xi/den for xi in x] + [R*(n2 - R*R)/den]
    return F
def Omega(R, num=2):
    return lambda x: num*R*R/(R*R + dot(x, x))
def vboost(R, c, cprime=None):
    cp = [R*R*ci for ci in c] if cprime is None else cprime
    def F(x):
        cx = dot(c, x); n2 = dot(x, x)
        return [cp[m] + 2*cx*x[m] - n2*c[m] for m in range(4)]
    return F
def vrot(J): return lambda x: [sum((J[m][n]*x[n] for n in range(4)), Fr(0)) for m in range(4)]

rng = random.Random(20261029)
def rq(): return Fr(rng.randint(-40, 40), rng.randint(1, 13))
def rpt(): return [rq() for _ in range(4)]
def sphere_pt(R):
    t = [rq() for _ in range(3)]; s = dot(t, t)
    return [R*2*t[0]/(s+1), R*2*t[1]/(s+1), R*2*t[2]/(s+1), R*(s-1)/(s+1)]

def killing_resid(vF, R, x, num=2):
    Jv, vv = jac(vF, x)                      # Jv[nu][mu] = d_mu v_nu
    Om = Omega(R, num)(seed(x)); dlog = [g/Om.v for g in Om.g]
    vdl = dot(vv, dlog)
    return [[Jv[n][m] + Jv[m][n] + (2*vdl if m == n else 0) for n in range(4)] for m in range(4)]
def is_zero(M): return all(e == 0 for row in M for e in row)

res = {}; NPTS = 40; Rs = [Fr(1), Fr(3, 2), Fr(7)]
ok = {k: True for k in ["K1","K2","K3","K4","K5","K6","K7"]}
fires = {k: False for k in ["C1","C2","C3","C4"]}
lam_found = {}
for R in Rs:
    for _ in range(NPTS):
        x = rpt()
        if dot(x, x) == 0: continue
        # K1
        X = Xmap(R)([*x]); X = [Fr(t) for t in X]
        if dot(X, X) != R*R: ok["K1"] = False
        if (X[4] <= 0) != (dot(x, x) <= R*R): ok["K1"] = False
        # K2
        JX, _ = jac(Xmap(R), x); Om = Omega(R)(x)
        G = [[sum(JX[i][m]*JX[i][n] for i in range(5)) for n in range(4)] for m in range(4)]
        if not all(G[m][n] == (Om*Om if m == n else 0) for m in range(4) for n in range(4)): ok["K2"] = False
        Om3 = Omega(R, 1)(x)
        if not all(G[m][n] == (Om3*Om3 if m == n else 0) for m in range(4) for n in range(4)): pass
        else: fires["C3"] = fires["C3"]  # passes => control did not fire at this point
        if any(G[m][m] != Om3*Om3 for m in range(4)): fires["C3"] = True
        # K3, K4 for boosts with random c; K4 for a random rotation
        c = rpt()
        Jv, vv = jac(vboost(R, c), x)
        div = sum(Jv[m][m] for m in range(4))
        if div != 8*dot(c, x): ok["K3"] = False
        if not all(Jv[n][m] + Jv[m][n] == (div/2 if m == n else 0) for m in range(4) for n in range(4)): ok["K3"] = False
        if not is_zero(killing_resid(vboost(R, c), R, x)): ok["K4"] = False
        A = [[rq() for _ in range(4)] for _ in range(4)]; J = [[A[m][n] - A[n][m] for n in range(4)] for m in range(4)]
        if not is_zero(killing_resid(vrot(J), R, x)): ok["K4"] = False
        # controls C1, C2
        if any(c_ != 0 for c_ in c):
            if not is_zero(killing_resid(lambda y: [R*R*ci + 0*y[0] for ci in c], R, x)): fires["C1"] = True
            if not is_zero(killing_resid(vboost(R, c, [2*R*R*ci for ci in c]), R, x)): fires["C2"] = True
        # K6
        X5 = Xmap(R)(x); X5 = [Fr(t) for t in X5]
        y = [R*X5[i]/(R + X5[4]) for i in range(4)]
        n2 = dot(x, x)
        if y != [R*R*xi/n2 for xi in x]: ok["K6"] = False
        xs_ref = [R*X5[i]/(R - (-X5[4])) for i in range(4)]   # south chart of (X', -X5)
        if xs_ref != y: ok["K6"] = False
        # K7: pushforward of v_c (c = e_i) equals lambda * A(X)
        for i in range(4):
            ci = [Fr(1) if j == i else Fr(0) for j in range(4)]
            vv = vboost(R, ci)(x); JX, Xv = jac(Xmap(R), x)
            push = [sum(JX[k][m]*vv[m] for m in range(4)) for k in range(5)]
            Aamb = [Fr(0)]*5; Aamb[4] = Xv[i]; Aamb[i] = -Xv[4]
            # find lambda from a nonzero component
            idx = next((k for k in range(5) if Aamb[k] != 0), None)
            if idx is None: continue
            lam = push[idx]/Aamb[idx]
            lam_found.setdefault(R, set()).add(lam)
            if push != [lam*a for a in Aamb]: ok["K7"] = False
    # K5 on |x| = R, C4 on |x| = R/2
    for _ in range(NPTS):
        x = sphere_pt(R); c = rpt()
        if dot(x, x) != R*R: raise SystemExit("sphere param bug")
        if vboost(R, c)(x) != [2*dot(c, x)*xm for xm in x]: ok["K5"] = False
        xh = [t/2 for t in x]; e1 = [Fr(1), Fr(0), Fr(0), Fr(0)]
        if vboost(R, e1)(xh) != [2*dot(e1, xh)*xm for xm in xh]: fires["C4"] = True
for R in Rs:
    lam_ok = (lam_found.get(R) == {2*R})
    print(f"K7 lambda at R={R}: {sorted(lam_found.get(R, []))}  (prediction 2R = {2*R}): {'match' if lam_ok else 'MISMATCH'}")
    if not lam_ok: ok["K7"] = False
for k in ok: print(k, "PASS" if ok[k] else "FAIL")
for k in fires: print(k, "fired" if fires[k] else "DID NOT FIRE")
verdict = all(ok.values()) and all(fires.values())
print("VERDICT:", "PASS" if verdict else "FAIL")
