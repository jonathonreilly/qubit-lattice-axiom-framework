"""F1 part 2: the Killing-sector projection P~[(W1,W1)] for BV-forced first-moment rotations.

BV locality forces: translation ghost -> F_rho = multiplication by i f_rho(k) (convolution);
rotation ghost omega -> L_J = x.J.F + Y (first moment of the SAME f, plus a convolution Y).
On shell S={A=0} (trivial symmetries vanish there):
   tangency (L_J is a symmetry):    (J f) . grad A = 0          on S, all antisymmetric J
   closure  (P~ = 0):               Df (J f) - c J f = 0         on S, all J
Theorem T1 (F1): with A a nonzero trigonometric polynomial these imply S_0 inside a complex
quadric (c != 0) or a hyperplane (c = 0, Carroll), impossible unless A depends on one linear
combination of k only.  This script checks the ingredients exactly (sympy) on the K2 scalar,
the K2 naive/staggered fermion, improved stencils, SLAC (escape) and the line lemma.
"""
import sympy as sp, itertools, numpy as np
k = sp.symbols('k0:4'); m2 = sp.Rational(3, 4)
J = sp.Matrix(4, 4, lambda i, j: 0)
def Jmat(a, b):
    M = sp.zeros(4, 4); M[a, b] = 1; M[b, a] = -1; return M
planes = [(a, b) for a in range(4) for b in range(a+1, 4)]

def check(name, A, f, shell_pt=None):
    f = sp.Matrix(f); gA = sp.Matrix([sp.diff(A, ki) for ki in k])
    Df = f.jacobian(k)
    tang = [sp.simplify(sp.expand_trig((Jmat(a, b)*f).dot(gA))) for a, b in planes]
    defect = [sp.simplify(Df*(Jmat(a, b)*f) - Jmat(a, b)*f) for a, b in planes]
    print(f"--- {name}")
    print("   tangency (Jf).gradA identically zero for all 6 planes:", all(t == 0 for t in tang))
    print("   closure defect, plane (0,1):", list(defect[0][:2]))
    if shell_pt is not None:
        vals = {ki: v for ki, v in zip(k, shell_pt)}
        Aval = sp.N(A.subs(vals), 30)
        dv = [sp.N(d.subs(vals), 20) for d in defect[0][:2]]
        print(f"   exact complex shell point {shell_pt}: |A| = {float(abs(Aval)):.2e}; defect(0,1) components = {dv}")
    return defect

# K2 scalar
A_s = sum(2 - 2*sp.cos(ki) for ki in k) + m2
f_s = [sp.sin(ki) for ki in k]
# shell point: k0=k1=1 real, k2=0, k3 = i*arccosh(1 + (m2 + 4 - 4cos1)/2)
k3 = sp.I*sp.acosh(1 + (m2 + 4 - 4*sp.cos(1))/2)
check("K2 scalar, f = sin k (L1 / K2 Lie derivative restricted to Killing)", A_s, f_s, (1, 1, 0, k3))

# K2 naive fermion: characteristic a = sum sin^2 + m^2, two-step translation f = sin(2k)/2
a_f = sum(sp.sin(ki)**2 for ki in k) + m2
f_f = [sp.sin(2*ki)/2 for ki in k]
k3f = sp.I*sp.asinh(sp.sqrt(m2 + 2*sp.sin(1)**2))   # sin(i y)^2 = -sinh^2 y
check("K2 naive/staggered fermion, f = sin(2k)/2", a_f, f_f, (1, 1, 0, k3f))

# improved scalar stencils u_r = IR-improved (u ~ k^2/2 + O(k^{2r+2})), f = grad u (tangency built in)
x = sp.symbols('x')
def improved_u1d(r):
    # u(x) = sum_{j=1..r} c_j (1 - cos(j x)) with u = x^2/2 + O(x^{2r+2})
    cs = sp.symbols('c1:%d' % (r+1))
    u = sum(c*(1 - sp.cos((j+1)*x)) for j, c in enumerate(cs))
    ser = sp.series(u, x, 0, 2*r+2).removeO()
    eqs = [sp.expand(ser).coeff(x, 2) - sp.Rational(1, 2)] + [sp.expand(ser).coeff(x, 2*i) for i in range(2, r+1)]
    sol = sp.solve(eqs, cs)
    return sp.simplify(u.subs(sol))
for r in (1, 2, 3):
    u1 = improved_u1d(r)
    A = sum(2*u1.subs(x, ki) for ki in k) + m2
    f = [sp.diff(u1, x).subs(x, ki) for ki in k]
    d = sp.diff(u1, x, 2) - 1
    print(f"--- improved scalar r_m={r}: u''(x)-1 = {sp.series(d, x, 0, 2*r+3)}  (closure defect factor, IR order x^{2*r})")
    print("    defect factor at the zone edge u''(pi)-1 =", sp.nsimplify(d.subs(x, sp.pi)))

# SLAC escape: f = k, A = k.k + m^2 (not periodic): defect vanishes identically
A_slac = sum(ki**2 for ki in k) + m2
d = check("SLAC (non-local, not periodic): f = k, A = k^2 + m^2", A_slac, list(k))
print("   SLAC defect identically zero:", all(all(sp.simplify(c) == 0 for c in dd) for dd in d))

# Line lemma: a nonzero trig polynomial cannot vanish on a complex null line k0 + t v (generic null v)
v = np.array([1.0, 1j*0.6, 1j*0.8, 0.0])         # v.v = 1 - 0.36 - 0.64 = 0
print("null v . v =", np.dot(v, v))
rng = np.random.default_rng(3)
ns = list(itertools.product(range(-2, 3), repeat=4))
ex = np.array([np.dot(n, v) for n in ns])
dmin = min(abs(ex[i]-ex[j]) for i in range(len(ns)) for j in range(i+1, len(ns)) if True) if False else None
vals = np.array(sorted(set(np.round(ex, 12))))
print(f"line lemma: {len(ns)} frequencies n in [-2,2]^4 give {len(vals)} distinct exponents n.v on this null line "
      f"(all distinct => every coefficient must vanish)" if len(vals) == len(ns) else
      f"line lemma: collisions present for this v ({len(vals)} of {len(ns)}); pick another generic v")
v2 = np.array([1.0, 1j*np.cos(0.3), 1j*np.sin(0.3)*np.cos(0.7), 1j*np.sin(0.3)*np.sin(0.7)])
ex2 = np.array([np.dot(n, v2) for n in ns]); vals2 = set(np.round(ex2, 10))
print(f"generic null v2 (v2.v2 = {np.dot(v2, v2):.1e}): {len(vals2)} distinct exponents of {len(ns)}")
