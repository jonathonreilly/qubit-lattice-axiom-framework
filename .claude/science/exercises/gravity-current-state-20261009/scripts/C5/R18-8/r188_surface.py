"""C5 R18-8 (C): the W7 tail at infinity. Surface (ADM boost) integral of the tail field, and Lemma T.

Tail kernel of R16-8 Lemma B (continuum, d = 3), point defect Delta_cb at the origin, fixed c:
  B_ij = Delta_cb * G_ij,b,   G_ij,b = (1/2)[ d_i d_j d_b r / (8 pi) - delta_ij d_b (1/(4 pi r)) ]   (s.B = D, D_c = d_b Delta_cb).
R1(h) = d_i d_j h_ij - lap h_kk.  ADM boost surface functional on a sphere of radius R:
  S_b[h](R) = oint [ x_b (d_j h_ij - d_i h_kk) - (h_ib - delta_ib h_kk) ] n_i dS  ( = int_ball x_b R1(h) ).
Checks:
 (1) R1(B) = 0 off the source (analytic, random points).
 (2) S_b[B](R) = Delta_cb for every R (R-independent; the tail's whole boost charge sits in its 1/r^2 part).
 (3) control: Newtonian field of a point mass M at a, h_ij = delta_ij phi, phi = -M/(8 pi |x - a|) (R1(h) = -T00):
     S_b = -M a_b.
 (4) Lemma T: h_T := B - delta_ij phi_d with phi_d = -(Delta_cb/(8 pi)) d_b(1/r) (field of a mass dipole M a_b = -Delta_cb)
     has vanishing linearised Ricci tensor off the source (so it is pure linearised gauge on R^3 minus a point),
     while B itself has nonzero Ricci ~ 1/r^4.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "2")
import numpy as np
import sympy as sp

X = sp.symbols('x1:4', real=True); r = sp.sqrt(sum(t**2 for t in X))
lines = []
def pr(s):
    print(s); lines.append(s)

def Gker(b):
    return [[sp.Rational(1, 2)*(sp.diff(r, X[i], X[j], X[b])/(8*sp.pi) - (1 if i == j else 0)*sp.diff(1/(4*sp.pi*r), X[b]))
             for j in range(3)] for i in range(3)]

def R1(h):
    return sum(sp.diff(h[i][j], X[i], X[j]) for i in range(3) for j in range(3)) - sum(sp.diff(h[k][k], X[i], X[i]) for i in range(3) for k in range(3))

def Ricci(h):
    tr = sum(h[k][k] for k in range(3))
    return [[sp.Rational(1, 2)*(sum(sp.diff(h[k][j], X[k], X[i]) + sp.diff(h[k][i], X[k], X[j]) for k in range(3))
             - sp.diff(tr, X[i], X[j]) - sum(sp.diff(h[i][j], X[k], X[k]) for k in range(3))) for j in range(3)] for i in range(3)]

def surface_integrand(h):
    tr = sum(h[k][k] for k in range(3))
    # vector V_b,i = x_b (d_j h_ij - d_i tr) - (h_ib - delta_ib tr); integrand V_b,i n_i
    out = []
    for b in range(3):
        Vi = [X[b]*(sum(sp.diff(h[i][j], X[j]) for j in range(3)) - sp.diff(tr, X[i])) - (h[i][b] - (1 if i == b else 0)*tr) for i in range(3)]
        out.append(Vi)
    return out

def sphere_quad(fun_list, R, nth=48, nph=96):
    xg, wg = np.polynomial.legendre.leggauss(nth)       # cos theta nodes
    ph = (np.arange(nph) + 0.5)*2*np.pi/nph
    ct = xg[:, None]*np.ones((1, nph)); st = np.sqrt(1 - ct**2); cp, sph = np.cos(ph)[None, :], np.sin(ph)[None, :]
    n = [st*cp, st*sph, ct*np.ones_like(cp)]
    pts = [R*n[0], R*n[1], R*n[2]]
    w = wg[:, None]*(2*np.pi/nph)*R**2
    res = []
    for Vi in fun_list:
        tot = sum(Vi[i](*pts)*n[i] for i in range(3))
        res.append(float(np.sum(tot*w)))
    return res

rng = np.random.default_rng(188)
Delta = np.diag([-6.91, -0.085, -39.2])    # sample edge defect values quoted in R16-8 s3.4 (rows c = 0,1,2), used as numbers only
pr("(C) tail kernel at infinity; point defect, Delta = diag(%s)" % ", ".join("%.3f" % t for t in np.diag(Delta)))
Gs = [Gker(b) for b in range(3)]
for c in range(3):
    B = [[sum(sp.nsimplify(Delta[c, b])*Gs[b][i][j] for b in range(3)) for j in range(3)] for i in range(3)]
    r1 = sp.lambdify(X, R1(B), 'numpy')
    pts = rng.normal(size=(5, 3))*2
    pr("  c=%d (1) max|R1(B)| at 5 random off-source points: %.1e" % (c, max(abs(r1(*p)) for p in pts)))
    V = [[sp.lambdify(X, Vi, 'numpy') for Vi in Vb] for Vb in surface_integrand(B)]
    for R in (0.5, 3.0, 50.0):
        Sb = sphere_quad(V, R)
        pr("      (2) R=%5.1f  S_b[B_c] = (%+.10f, %+.10f, %+.10f)   expected Delta_c,b = (%+.3f, %+.3f, %+.3f)" % (
            R, *Sb, *Delta[c]))
    # (4) Lemma T
    phid = -sum(sp.nsimplify(Delta[c, b])*sp.diff(1/r, X[b]) for b in range(3))/(8*sp.pi)
    hT = [[B[i][j] - (phid if i == j else 0) for j in range(3)] for i in range(3)]
    Ric_T = sp.lambdify(X, Ricci(hT), 'numpy'); Ric_B = sp.lambdify(X, Ricci(B), 'numpy')
    mT = max(np.max(np.abs(np.array(Ric_T(*p)))) for p in pts); mB = max(np.max(np.abs(np.array(Ric_B(*p)))) for p in pts)
    pr("      (4) Lemma T: max|Ric(B - delta phi_dip)| = %.1e ; max|Ric(B)| = %.3e (same points)" % (mT, mB))
    # Ricci falloff of B along a ray: r^4 |Ric|
    d = np.array([0.36, -0.48, 0.80])
    rr = [np.max(np.abs(np.array(Ric_B(*(R*d)))))*R**4 for R in (2.0, 20.0, 200.0)]
    pr("      r^4 max|Ric(B)| along a ray at r = 2, 20, 200: %.6f %.6f %.6f" % tuple(rr))
# (3) Newtonian control
M, a = 2.0, np.array([0.3, -0.7, 1.1])
phi = -M/(8*sp.pi*sp.sqrt(sum((X[i] - a[i])**2 for i in range(3))))
hN = [[phi if i == j else 0 for j in range(3)] for i in range(3)]
VN = [[sp.lambdify(X, Vi, 'numpy') for Vi in Vb] for Vb in surface_integrand(hN)]
r1N = sp.lambdify(X, R1(hN), 'numpy'); p = np.array([2.0, 1.0, -1.0])
pr("  (3) Newtonian control M=%.1f at a=(%.1f,%.1f,%.1f): R1 off-source = %.1e" % (M, *a, abs(r1N(*p))))
for R in (5.0, 50.0):
    pr("      R=%4.0f  S_b[h_N] = (%+.8f, %+.8f, %+.8f)   expected -M a = (%+.3f, %+.3f, %+.3f)" % (R, *sphere_quad(VN, R), *(-M*a)))
open(os.path.splitext(os.path.abspath(__file__))[0] + ".out", "w").write("\n".join(lines) + "\n")
