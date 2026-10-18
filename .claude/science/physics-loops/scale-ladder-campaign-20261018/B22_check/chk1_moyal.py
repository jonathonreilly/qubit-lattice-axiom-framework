"""B22 check 1 (exact, sympy): the generator-lapse bracket from the EXACT momentum-space matrix elements,
not from a quoted Moyal formula.

For a translation-invariant matrix symbol h(k) (any size, any matrix structure) and complex exponential
lapses N = e^{i a.x}, M = e^{i b.x}, H(N) = (1/2){N, Op(h)} maps |k> -> (1/2)(h(k+a)+h(k)) |k+a>.  Hence
[H(N),H(M)] maps |k> -> E(k;a,b)|k+a+b> with the exact element
   E = 1/4[(h(k+a+b)+h(k+b))(h(k+b)+h(k)) - (h(k+a+b)+h(k+a))(h(k+a)+h(k))].
Weyl symbol of an operator with this element is E evaluated at the midpoint m = k+(a+b)/2.  Dictionary:
(b-a) e^{i(a+b)x}  <->  -i w,  w = N grad M - M grad N;  (a x b) e^{i(a+b)x} <-> -(grad N x grad M).

Checks:
 M1 first order (1D, noncommutative Taylor coefficients h0,h1,h2,h3 of h at m): E = (b-a)(1/2){h0,h1} + ...
    i.e. symbol -i w (1/2) d(h^2): the anticommutator, i.e. exactly (1/2)d(h^2); no commutator piece.
 M2 second order (1D): the only O(2) term is (a^2-b^2) * c [h0,h2] -> a w' [h,h''] term (vanishes for
    uniform w, which is all B22 tested).
 M3 3D Weyl h = sigma.k: E = (b-a).m + (i/2)(a x b).sigma EXACTLY  -> orbital -i(1/2){w,p} plus spin
    -(i/2)(gradN x gradM).sigma = -(i/4)(curl w).sigma (Kosmann term of G[w]).  Not tested by B22
    (its lapses have grad N || grad M).
 M4 general constant triad h = sigma_a e_aj k_j: spin term (i/2) sigma.(cof(e)(a x b)), orbital g = e^T e.
 M5 offset h -> h - E: first-order symbol gains +i E w d h (lapse-weighted current), exact in the
    first-order algebra; momentum offset (node at k*): (1/2)d(h^2) = g(k-k*) gives an extra
    +i (g k*).w density term unless G is built from the momentum relative to the node.
 M6 uniform-w lapses N = cos(q x), M = sin(q x): the bracket is exactly diagonal in k with element
    K(k) = -(i/8)[(h_k+h_{k+q})^2 - (h_k+h_{k-q})^2]  (all k -> k +- 2q elements cancel).
"""
import sympy as sp

PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"\n        {detail}" if detail else ""))

a, b, eps = sp.symbols('a b epsilon')
h0, h1, h2, h3 = sp.symbols('h0 h1 h2 h3', commutative=False)
def hT(d):   # Taylor expansion of h about the midpoint, d = offset from m
    return h0 + d * h1 + d**2 / 2 * h2 + d**3 / 6 * h3
# k = m - (a+b)/2
k_ = -(a + b) / 2
E = sp.Rational(1, 4) * ((hT(k_ + a + b) + hT(k_ + b)) * (hT(k_ + b) + hT(k_)) -
                         (hT(k_ + a + b) + hT(k_ + a)) * (hT(k_ + a) + hT(k_)))
Es = sp.expand(E.subs({a: eps * a, b: eps * b}))
o1 = sp.expand(Es.coeff(eps, 1)); o2 = sp.expand(Es.coeff(eps, 2)); o0 = sp.expand(Es.coeff(eps, 0))
pred1 = sp.expand((b - a) * sp.Rational(1, 2) * (h0 * h1 + h1 * h0))
check("M1 [exact] 1D, arbitrary matrix h: zeroth order vanishes; first-order element = (b-a)(1/2){h,h'}"
      " = (b-a)(1/2)d(h^2)  [symbol -i w (1/2) d_k h^2]", o0 == 0 and sp.expand(o1 - pred1) == 0, f"O(1) = {o1}")
o3 = sp.expand(Es.coeff(eps, 3))
print("        O(3) term:", sp.factor(o3))
check("M2 [exact; corrects the checker's own prior guess of a w'[h,h''] term] 1D, arbitrary matrix h: the O(2) element"
      " vanishes identically; the first correction is O(3) (relative O(q^2), the q^2 scaling seen in B22 P1)",
      o2 == 0 and o3 != 0, "O(2) = %s" % o2)

# ---------------- 3D Weyl, exact
sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
S = [sx, sy, sz]
kv = sp.Matrix(sp.symbols('k1:4')); av = sp.Matrix(sp.symbols('a1:4')); bv = sp.Matrix(sp.symbols('b1:4'))
def hW(k, e):
    v = e * k
    return v[0] * sx + v[1] * sy + v[2] * sz
def Eexact(e):
    hk = lambda k: hW(k, e)
    return sp.expand(sp.Rational(1, 4) * ((hk(kv + av + bv) + hk(kv + bv)) * (hk(kv + bv) + hk(kv)) -
                                          (hk(kv + av + bv) + hk(kv + av)) * (hk(kv + av) + hk(kv))))
m = kv + (av + bv) / 2
I2 = sp.eye(2)
E3 = Eexact(sp.eye(3))
axb = av.cross(bv)
pred3 = ((bv - av).dot(m)) * I2 + sp.I / 2 * (axb[0] * sx + axb[1] * sy + axb[2] * sz)
check("M3 [exact] 3D Weyl h = sigma.k: E = (b-a).m + (i/2)(a x b).sigma exactly: orbital -i(1/2){w,p} and"
      " spin -(i/4)(curl w).sigma (the Kosmann term) -- second order in lapse gradients, absent when grad N || grad M",
      sp.simplify(E3 - pred3) == sp.zeros(2))
e1, e2, e3 = sp.symbols('e1:4', positive=True)
eg = sp.Matrix([[e1, 0, 0], [0, e2, 0], [0, sp.Rational(1, 3), e3]])   # generic lower-triangular constant triad
Eg = Eexact(eg)
g = eg.T * eg
cof = eg.det() * eg.inv().T
sp_ = cof * axb
predg = ((bv - av).T * g * m)[0] * I2 + sp.I / 2 * (sp_[0] * sx + sp_[1] * sy + sp_[2] * sz)
check("M4 [exact] constant triad h = sigma_a e_aj k_j (non-diagonal e): orbital element (b-a).g.m with g = e^T e,"
      " spin (i/2) sigma.(cof(e)(a x b))", sp.simplify(Eg - predg) == sp.zeros(2))

# ---------------- offsets
Eo = sp.symbols('E0')
hoff = lambda d: hT(d) - Eo
Eoff = sp.Rational(1, 4) * ((hoff(k_ + a + b) + hoff(k_ + b)) * (hoff(k_ + b) + hoff(k_)) -
                            (hoff(k_ + a + b) + hoff(k_ + a)) * (hoff(k_ + a) + hoff(k_)))
d1 = sp.expand(sp.expand(Eoff.subs({a: eps * a, b: eps * b})).coeff(eps, 1) - o1)
check("M5a [exact] energy offset h -> h - E0: first-order element gains -(b-a) E0 h'  [symbol +i E0 w d_k h:"
      " lapse-weighted current; dominates (1/2)d(h^2) ~ g k as k -> 0]", sp.expand(d1 + (b - a) * Eo * h1) == 0, f"{d1}")
ks, gg = sp.symbols('kstar g')
hsq = gg * (sp.Symbol('p') - ks)**2 / 1          # (1/2) d (h^2) for omega^2 = g (p-k*)^2
dh = sp.diff(hsq / 2 * 1, sp.Symbol('p'))
check("M5b [exact] node at k* != 0: (1/2) d(omega^2) = g (p - k*): relative to G built from the lattice momentum p"
      " the bracket carries an extra +i g k* w * (density) term; it is geometric only for G built from p - k*",
      sp.expand(dh - gg * (sp.Symbol('p') - ks)) == 0)

# ---------------- M6 uniform-w structure (1D, sympy with generic symbol functions)
q, kk = sp.symbols('q k')
Hf = sp.Function('h', commutative=False)
def A(k0, s):   # amplitude |k0> -> |k0 + s q> for (1/2){e^{isqx}, h}
    return sp.Rational(1, 2) * (Hf(k0 + s * q) + Hf(k0))
# N = (e+ + e-)/2, M = (e+ - e-)/(2i)
cN = {1: sp.Rational(1, 2), -1: sp.Rational(1, 2)}; cM = {1: 1 / (2 * sp.I), -1: -1 / (2 * sp.I)}
el = {}
for s1 in (1, -1):
    for s2 in (1, -1):
        # H(N)H(M): first M (s2) then N (s1)
        t = cN[s1] * cM[s2] * A(kk + s2 * q, s1) * A(kk, s2) - cM[s1] * cN[s2] * A(kk + s2 * q, s1) * A(kk, s2)
        el[s1 + s2] = el.get(s1 + s2, 0) + t
off = [sp.expand(el[2]), sp.expand(el[-2])]
diag = sp.expand(el[0])
predK = sp.expand(-sp.I / 8 * ((Hf(kk) + Hf(kk + q))**2 - (Hf(kk) + Hf(kk - q))**2))
check("M6 [exact] N = cos qx, M = sin qx: k -> k +- 2q elements vanish; diagonal element"
      " K(k) = -(i/8)[(h_k+h_{k+q})^2 - (h_k+h_{k-q})^2]", off == [0, 0] and sp.expand(diag - predK) == 0)
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")

# ---------------- M7 multi-dimensional second order, arbitrary matrix h (2D suffices for the structure)
H0, Hx, Hy, Hxx, Hxy, Hyy = sp.symbols('H0 Hx Hy Hxx Hxy Hyy', commutative=False)
ax_, ay_, bx_, by_ = sp.symbols('ax ay bx by')
def h2d(dx, dy):
    return H0 + dx * Hx + dy * Hy + (dx**2 * Hxx + 2 * dx * dy * Hxy + dy**2 * Hyy) / 2
kx_, ky_ = -(ax_ + bx_) / 2, -(ay_ + by_) / 2
E2d = sp.Rational(1, 4) * ((h2d(kx_ + ax_ + bx_, ky_ + ay_ + by_) + h2d(kx_ + bx_, ky_ + by_)) * (h2d(kx_ + bx_, ky_ + by_) + h2d(kx_, ky_)) -
                           (h2d(kx_ + ax_ + bx_, ky_ + ay_ + by_) + h2d(kx_ + ax_, ky_ + ay_)) * (h2d(kx_ + ax_, ky_ + ay_) + h2d(kx_, ky_)))
E2s = sp.expand(E2d.subs({ax_: eps * ax_, ay_: eps * ay_, bx_: eps * bx_, by_: eps * by_}))
s2 = sp.expand(E2s.coeff(eps, 2))
pred_s2 = sp.expand(sp.Rational(1, 4) * (ax_ * by_ - ay_ * bx_) * (Hx * Hy - Hy * Hx))
check("M7 [exact] multi-D, arbitrary matrix h: the O(2) element is (1/4)(a x b)_z [d_x h, d_y h] -- only the"
      " commutator of the velocity matrices (the spin term; no [h, d d h] piece)", sp.expand(s2 - pred_s2) == 0,
      f"O(2) = {sp.factor(s2)}")
print(f"\nTOTAL (incl. M7): PASS={PASS} FAIL={FAIL}")
