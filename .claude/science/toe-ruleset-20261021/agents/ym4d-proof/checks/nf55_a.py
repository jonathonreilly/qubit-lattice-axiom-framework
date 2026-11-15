# nf55_a -- exact checks on the free Maxwell composite :F^a F^a: (criteria: nf55_a_criteria.md, written first).
# Exact arithmetic only: sympy Rational evaluation and python Fraction. No floats in any verdict.
import itertools, sys, time
from fractions import Fraction
import sympy as sp

t0 = time.time()
def log(msg):
    print(msg); sys.stdout.flush()

Z = sp.symbols('z0:4', real=True)
r2 = sum(zi**2 for zi in Z)
Gt = 1/r2                       # G~ = 4 pi^2 G_0
H = sp.log(r2)                  # pure-gauge generator
delta = lambda a, b: 1 if a == b else 0
PAIRS = [(m, n) for m in range(4) for n in range(4) if m != n]   # 12 ordered pairs

def potential(c):
    # <A_a(x) A_b(y)> as a function of z = x - y
    return [[delta(a, b)*Gt + c*sp.diff(H, Z[a], Z[b]) for b in range(4)] for a in range(4)]

def field_corr(P, sign_mode):
    # <F_{mu nu}(x) F_{rho sigma}(y)>, F = d_mu A_nu - d_nu A_mu (sign_mode='anti') or + (sign_mode='sym'),
    # d^x -> d_z, d^y -> -d_z.  Built term by term from the potential correlator.
    s = -1 if sign_mode == 'anti' else 1
    C = {}
    for (m, n) in PAIRS:
        for (r, q) in PAIRS:
            t1 = -sp.diff(P[n][q], Z[m], Z[r])          # d^x_m d^y_r <A_n A_q>
            t2 = -sp.diff(P[n][r], Z[m], Z[q])          # d^x_m d^y_q <A_n A_r>
            t3 = -sp.diff(P[m][q], Z[n], Z[r])          # d^x_n d^y_r <A_m A_q>
            t4 = -sp.diff(P[m][r], Z[n], Z[q])          # d^x_n d^y_q <A_m A_r>
            C[((m, n), (r, q))] = (t1, s*t2, s*t3, s*s*t4)
    return C

def evalC(C, pt, drop4=False):
    sub = {Z[i]: sp.Integer(pt[i]) for i in range(4)}
    out = {}
    for k, (t1, t2, t3, t4) in C.items():
        expr = t1 + t2 + t3 + (0 if drop4 else t4)
        v = sp.nsimplify(sp.simplify(expr.subs(sub)))
        v = sp.Rational(v)
        out[k] = Fraction(int(v.p), int(v.q))
    return out

P0 = potential(0); P1 = potential(1)
C_anti0 = field_corr(P0, 'anti'); C_anti1 = field_corr(P1, 'anti')
C_sym0 = field_corr(P0, 'sym');   C_sym1 = field_corr(P1, 'sym')
log("built correlators %.1fs" % (time.time()-t0))

PTS = {'P1': (1,0,0,0), 'P2': (0,0,0,2), 'P3': (1,1,0,0), 'P4': (1,2,3,4), 'P5': (2,-1,3,5), 'P6': (3,3,3,1)}
results = {}

# ---- A1: gauge independence
a1 = True
for name in ['P3', 'P4', 'P5', 'P6']:
    e0 = evalC(C_anti0, PTS[name]); e1 = evalC(C_anti1, PTS[name])
    ok = all(e0[k] == e1[k] for k in e0)
    log("A1 %s: F-correlator unchanged by pure-gauge term: %s" % (name, ok))
    a1 = a1 and ok
s0 = evalC(C_sym0, PTS['P3']); s1 = evalC(C_sym1, PTS['P3'])
ndiff = sum(1 for k in s0 if s0[k] != s1[k])
a1f = ndiff > 0
log("A1-F (symmetrised F, P3): components changed by pure-gauge term = %d -> control fires: %s" % (ndiff, a1f))
results['A1'] = a1; results['A1-F'] = a1f

# ---- A2: two-point coefficient |z|^8 sum D~^2 = 384
DT = {}
a2 = True
for name, pt in PTS.items():
    D = evalC(C_anti0, pt); DT[pt] = D
    rr = sum(c*c for c in pt)
    val = sum(v*v for v in D.values()) * Fraction(rr)**4
    log("A2 %s: |z|^8 sum D~^2 = %s" % (name, val))
    a2 = a2 and (val == 384)
Dd = evalC(C_anti0, PTS['P3'], drop4=True)
rr = 2
vald = sum(v*v for v in Dd.values()) * Fraction(rr)**4
a2f = (vald != 384)
log("A2-F (fourth term omitted, P3): value = %s -> control fires: %s" % (vald, a2f))
results['A2'] = a2; results['A2-F'] = a2f

# ---- helpers for enumeration
def Dmat(w):
    w = tuple(w)
    if w not in DT:
        DT[w] = evalC(C_anti0, w)
    return DT[w]

def Gscal(w):
    rr = sum(c*c for c in w)
    return Fraction(1, rr)

def diff(p, q):
    return tuple(p[i]-q[i] for i in range(4))

def matchings(slots):
    if not slots:
        yield []
        return
    a = slots[0]
    for i in range(1, len(slots)):
        b = slots[i]
        rest = slots[1:i] + slots[i+1:]
        for m in matchings(rest):
            yield [(a, b)] + m

def enum_tensor(points, connected_only=None):
    # slots: (point index, copy); both copies at a point carry the same index variable
    n = len(points)
    slots = [(p, c) for p in range(n) for c in range(2)]
    allm = [m for m in matchings(slots) if all(a[0] != b[0] for (a, b) in m)]
    def is_conn(m):
        parent = list(range(n))
        def f(x):
            while parent[x] != x:
                x = parent[x]
            return x
        for (a, b) in m:
            parent[f(a[0])] = f(b[0])
        return len(set(f(x) for x in range(n))) == 1
    sel = [m for m in allm if (connected_only is None or is_conn(m) == connected_only)]
    mats = {}
    for m in sel:
        for (a, b) in m:
            key = (a[0], b[0])
            if key not in mats:
                mats[key] = Dmat(diff(points[a[0]], points[b[0]]))
    total = Fraction(0)
    for idx in itertools.product(PAIRS, repeat=n):
        for m in sel:
            prod = Fraction(1)
            for (a, b) in m:
                v = mats[(a[0], b[0])][(idx[a[0]], idx[b[0]])]
                if v == 0:
                    prod = Fraction(0); break
                prod *= v
            total += prod
    return total, len(sel)

def enum_scalar(points):
    n = len(points)
    slots = [(p, c) for p in range(n) for c in range(2)]
    tot = Fraction(0)
    for m in matchings(slots):
        if any(a[0] == b[0] for (a, b) in m):
            continue
        prod = Fraction(1)
        for (a, b) in m:
            prod *= Gscal(diff(points[a[0]], points[b[0]]))
        tot += prod
    return tot

# ---- A3: three-point function, duality prediction T3 = 0
CONF3 = {'Q1': [(0,0,0,0),(1,0,0,0),(0,2,0,0)], 'Q2': [(0,0,0,0),(1,2,0,1),(-1,1,3,0)], 'Q3': [(1,0,0,0),(0,1,1,0),(2,3,-1,1)]}
a3 = True
for name, pts in CONF3.items():
    T3, nm = enum_tensor(pts)
    log("A3 %s: T3 (in units (4pi^2)^-3) = %s  [%d matchings]" % (name, T3, nm))
    a3 = a3 and (T3 == 0)
q = CONF3['Q1']
sc = enum_scalar(q)
pred = 8*Gscal(diff(q[0],q[1]))*Gscal(diff(q[1],q[2]))*Gscal(diff(q[2],q[0]))
a3f = (sc != 0) and (sc == pred)
log("A3-F scalar :phi^2: at Q1: enumeration = %s, 8GGG = %s -> control fires: %s" % (sc, pred, a3f))
results['A3'] = a3; results['A3-F'] = a3f
log("time %.1fs" % (time.time()-t0))

# ---- A4: four-point truncated function nonzero; enumeration vs cycle formula
R1 = [(0,0,0,0),(1,0,0,0),(0,2,0,0),(0,0,1,3)]
T4c, nconn = enum_tensor(R1, connected_only=True)
log("A4 enumeration (connected matchings: %d): T4 = %s" % (nconn, T4c))
def trace4(a, b, c, d):
    M = [Dmat(diff(R1[a], R1[b])), Dmat(diff(R1[b], R1[c])), Dmat(diff(R1[c], R1[d])), Dmat(diff(R1[d], R1[a]))]
    tot = Fraction(0)
    for I in PAIRS:
        for J in PAIRS:
            x1 = M[0][(I, J)]
            if x1 == 0: continue
            for K in PAIRS:
                x2 = M[1][(J, K)]
                if x2 == 0: continue
                for Lp in PAIRS:
                    x3 = M[2][(K, Lp)]
                    if x3 == 0: continue
                    x4 = M[3][(Lp, I)]
                    if x4 == 0: continue
                    tot += x1*x2*x3*x4
    return tot
cyc = 16*(trace4(0,1,2,3) + trace4(0,1,3,2) + trace4(0,2,1,3))
log("A4 cycle formula: 16*sum_3cycles = %s" % cyc)
a4 = (cyc == T4c) and (T4c != 0)
T4d, ndis = enum_tensor(R1, connected_only=False)
a4f = (T4d != 0)
log("A4-F disconnected part (%d matchings) = %s -> control fires: %s" % (ndis, T4d, a4f))
results['A4'] = a4; results['A4-F'] = a4f

log("RESULTS: %s" % results)
gates = all(results[k] for k in ['A1','A2','A3','A4'])
ctrls = all(results[k] for k in ['A1-F','A2-F','A3-F','A4-F'])
log("VERDICT: %s (gates %s, controls %s), time %.1fs" % ("PASS" if (gates and ctrls) else "FAIL", gates, ctrls, time.time()-t0))
