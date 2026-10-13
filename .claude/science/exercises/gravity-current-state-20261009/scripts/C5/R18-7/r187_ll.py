#!/usr/bin/env python3
"""R18-7 [1]-[2]: Landau-Lifshitz field stress of a static weak field, via the exact LL identity
   d_mu d_nu H^{a mu b nu} = 2(-g) G^{ab} + 16 pi G (-g) t_LL^{ab},  H = gG^{ab}gG^{mu nu} - gG^{a nu}gG^{b mu},  gG = sqrt(-g) g^{..}
evaluated for g00 = -(1-2eU), gij = (1+2eU) delta (the O(G) harmonic static metric), kept to O(e^2).
Then the O(M^2) harmonic point-mass metric from tau = Lambda, converted gothic -> g00 (beta).
Units G = c = 1.  Subtraction: none (identity residuals are measured against zero).
"""
import sympy as sp, time
t0 = time.time()
x, y, z, e = sp.symbols('x y z e', real=True)
X = [sp.Symbol('t'), x, y, z]
U = sp.Function('U')(x, y, z)
g = sp.diag(-(1 - 2*e*U), 1 + 2*e*U, 1 + 2*e*U, 1 + 2*e*U)
gi = sp.diag(*[1/g[i, i] for i in range(4)])
detg = sp.prod([g[i, i] for i in range(4)])
sq = sp.sqrt(-detg)

def tr2(expr):
    """truncate to O(e^2)"""
    expr = sp.expand(expr)
    return sum(sp.diff(expr, e, k).subs(e, 0) * e**k / sp.factorial(k) for k in range(3))

def D(f, m):
    return 0 if m == 0 else sp.diff(f, X[m])

gG = [[tr2(sq * gi[a, b]) for b in range(4)] for a in range(4)]
# LHS = d_mu d_nu H^{a mu b nu}
def H(a, m, b, n):
    return gG[a][b]*gG[m][n] - gG[a][n]*gG[b][m]
LHS = {}
for (a, b) in [(0, 0), (1, 1), (1, 2), (2, 2), (3, 3)]:
    s = 0
    for m in range(1, 4):
        for n in range(1, 4):
            s += D(D(H(a, m, b, n), m), n)
    LHS[(a, b)] = tr2(s)
# Einstein tensor
Gam = [[[tr2(sum(gi[a, d]*(D(g[d, b], c) + D(g[d, c], b) - D(g[b, c], d)) for d in range(4))/2)
         for c in range(4)] for b in range(4)] for a in range(4)]
def Ric(b, c):
    s = 0
    for a in range(4):
        s += D(Gam[a][b][c], a) - D(Gam[a][b][a], c)
        for d in range(4):
            s += Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a]
    return tr2(s)
R = sp.Matrix(4, 4, lambda b, c: Ric(b, c))
Rs = tr2(sum(gi[a, a]*R[a, a] for a in range(4)))
Gdn = sp.Matrix(4, 4, lambda a, b: tr2(R[a, b] - g[a, b]*Rs/2))
Gup = lambda a, b: tr2(gi[a, a]*gi[b, b]*Gdn[a, b])
mg = tr2(-detg)
gradU2 = sum(sp.diff(U, v)**2 for v in (x, y, z))
print("[1] LL identity for the static O(G) harmonic metric (G=c=1); runtime so far %.1f s" % (time.time()-t0))
res = {}
for (a, b) in [(0, 0), (1, 1), (1, 2), (2, 2), (3, 3)]:
    tLL16pi = tr2(LHS[(a, b)] - 2*mg*Gup(a, b))
    o1 = sp.simplify(tLL16pi.coeff(e, 1))
    o2 = sp.simplify(tLL16pi.coeff(e, 2))
    res[(a, b)] = o2
    print("    16 pi (-g) t_LL^{%d%d}: O(e) part = %s ; O(e^2) part = %s" % (a, b, o1, sp.factor(o2)))
c00 = sp.simplify(res[(0, 0)] / gradU2)
print("    => (-g) t_LL^{00} = %s |grad U|^2 / (16 pi)  = -(7/8pi)|grad U|^2 ?  %s" % (c00, sp.simplify(c00 + 14) == 0))
trk = sp.simplify((res[(1, 1)] + res[(2, 2)] + res[(3, 3)]) / gradU2)
print("    => (-g) t_LL^{kk} = %s |grad U|^2 / (16 pi)  = -(1/8pi)|grad U|^2 ?  %s" % (trk, sp.simplify(trk + 2) == 0))
c12 = sp.simplify(res[(1, 2)] / (sp.diff(U, x)*sp.diff(U, y)))
print("    => (-g) t_LL^{xy} = %s dxU dyU / (16 pi) = (1/4pi) dxU dyU ?  %s" % (c12, sp.simplify(c12 - 4) == 0))
print("    (static t_H^{ab} is O(U^3): h^{0j}=0, h^{jk}=O(U^2); proved in report)")

# ---------------- [2] O(M^2) point mass in harmonic gauge, beta ----------------
print("\n[2] O(M^2) harmonic point mass from tau = Lambda (outside the source), gothic -> g00")
r, M = sp.symbols('r M', positive=True)
lap = lambda f: sp.diff(r**2*sp.diff(f, r), r)/r**2
Uo = M/r
dU2 = sp.diff(Uo, r)**2
# box h = -16 pi tau  (static: lap h = -16 pi tau)
S00 = -16*sp.pi*(-sp.Rational(7, 8)/sp.pi*dU2)
Skk = -16*sp.pi*(-sp.Rational(1, 8)/sp.pi*dU2)
A, B = sp.symbols('A B')
h00_2 = sp.solve(sp.Eq(lap(A*M**2/r**2), S00), A)[0]*M**2/r**2
hkk_2 = sp.solve(sp.Eq(lap(B*M**2/r**2), Skk), B)[0]*M**2/r**2
print("    h2^{00} = %s ; h2^{kk} = %s  (particular solutions; 1/r homogeneous parts = mass renormalisation)" % (h00_2, hkk_2))
h00 = 4*Uo + h00_2
# g00 = -sqrt((det of spatial gothic)/(1+h00)) with det(delta - h^{jk}) = 1 - h^{kk} + O(h^2) [h^{jk} = O(M^2)]
g00 = -sp.sqrt((1 - hkk_2)/(1 + h00))
ser = sp.series(g00, M, 0, 3).removeO()
print("    g00 to O(M^2) = %s" % sp.simplify(ser))
beta = sp.simplify(-ser.coeff(M, 2)*r**2/2)
print("    => beta = %s (GR: 1)" % beta)
# harmonic Schwarzschild comparator
gS = -(r - M)/(r + M)
print("    harmonic Schwarzschild comparator g00 = %s" % sp.series(gS, M, 0, 3).removeO())
# aside: gothic-linear (no Lambda) vs metric-linear (R16-14 L0)
g00_gl = sp.series(-sp.sqrt(1/(1 + 4*Uo)), M, 0, 3).removeO()
print("    aside: gothic metric LINEAR in records (Lambda = 0): g00 = %s -> beta = %s ; metric-linear L0 (R16-14): beta = 0"
      % (g00_gl, sp.simplify(-g00_gl.coeff(M, 2)*r**2/2)))
print("    (perihelion factor (2+2gamma-beta)/3: beta=3 -> 1/3, beta=0 -> 4/3, beta=1 -> 1)")
print("    runtime %.1f s" % (time.time()-t0))
