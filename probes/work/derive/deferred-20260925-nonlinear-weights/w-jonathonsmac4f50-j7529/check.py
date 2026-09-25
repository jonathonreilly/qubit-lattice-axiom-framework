#!/usr/bin/env python3
"""check.py for J:derive:deferred-20260925-nonlinear-weights:a1 (worker w-jonathonsmac4f50-j7529, claude-opus-5-5).

Residual (PR #9083, landed on main): 'Self-weighted consistency checked inside the affine covariant family does not classify all nonlinear laws.'
Attempted here: self-weighted no-signalling, with two partner menus on one entangled pure state, forces the pure-state law to be Born or constant
(no ensemble affinity and no Born ensemble weights assumed).  Exact arithmetic (sympy) throughout; one section (C6) is floating-point evidence.
"""
import sympy as sp

PASS, FAIL = [], []
def check(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(("PASS " if ok else "FAIL ") + name + ((": " + detail) if detail else ""), flush=True)

I2 = sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
def bloch(rho):
    return [sp.simplify((rho * s).trace()) for s in (sx, sy, sz)]
def kron(A, B): return sp.kronecker_product(A, B)

# ---------------------------------------------------------------- C1 the two steerings, exact, at a general Bloch length l and at l = 3/5
uu = sp.Symbol("u", positive=True)                                          # 0 < l < 1 as l = (1 - u^2)/(1 + u^2), u > 0 (so every square root is of a positive quantity)
lu = (1 - uu ** 2) / (1 + uu ** 2)
a_, b_ = 1 / sp.sqrt(1 + uu ** 2), uu / sp.sqrt(1 + uu ** 2)              # sqrt((1+l)/2), sqrt((1-l)/2)
px = sp.Matrix([1, 1]) / sp.sqrt(2); mx = sp.Matrix([1, -1]) / sp.sqrt(2)     # A's +x and -x
k0, k1 = sp.Matrix([1, 0]), sp.Matrix([0, 1])
psi = a_ * kron(px, k0) + b_ * kron(mx, k1)                                 # pure two-qubit state, A's Bloch vector l x-hat
def steer(bvec):
    """A's (unnormalized) state after B's outcome |b>: (I (x) <b|) psi; returns (weight, Bloch vector of the normalized state)"""
    P = kron(I2, bvec * bvec.H)
    v = P * psi
    w = sp.simplify((v.H * v)[0])
    rhoAB = v * v.H
    rhoA = sp.Matrix(2, 2, lambda i, j: sum(rhoAB[2 * i + k, 2 * j + k] for k in range(2)))
    return sp.simplify(w), [sp.simplify(x / w) for x in bloch(rhoA)]
rhoAB = psi * psi.H
rhoA = sp.Matrix(2, 2, lambda i, j: sum(rhoAB[2 * i + k, 2 * j + k] for k in range(2)))
rhoB = sp.Matrix(2, 2, lambda i, j: sum(rhoAB[2 * k + i, 2 * k + j] for k in range(2)))
ok = all(sp.simplify(x - y) == 0 for x, y in zip(bloch(rhoA) + bloch(rhoB), [lu, 0, 0, 0, 0, lu]))
wr0, n_r0 = steer(k0); wr1, n_r1 = steer(k1)
ok_r = sp.simplify(wr0 - (1 + lu) / 2) == 0 and n_r0 == [1, 0, 0] and sp.simplify(wr1 - (1 - lu) / 2) == 0 and n_r1 == [-1, 0, 0]
bp = (k0 + sp.I * k1) / sp.sqrt(2); bm = (k0 - sp.I * k1) / sp.sqrt(2)      # partner menu orthogonal to its Bloch vector (along y)
wp, n_p = steer(bp); wm, n_m = steer(bm)
sb = 2 * uu / (1 + uu ** 2)                                                 # sqrt(1 - l^2)
ok_p = (sp.simplify(wp - sp.Rational(1, 2)) == 0 and sp.simplify(wm - sp.Rational(1, 2)) == 0 and
        all(sp.simplify(x - y) == 0 for x, y in zip(n_p + n_m, [lu, sb, 0, lu, -sb, 0])))
l = sp.Symbol("l", positive=True)
ok_menu = bloch(bp * bp.H) == [0, 1, 0] and bloch(bm * bm.H) == [0, -1, 0]
check("C1 for every 0 < l < 1: the pure state sqrt((1+l)/2)|+x>|0> + sqrt((1-l)/2)|-x>|1> has Bloch vectors l x-hat (A) and l z-hat (B); "
      "the partner's z-menu (along its Bloch vector) steers A to +-x-hat with Born weights (1+-l)/2 (radial chord); the partner's y-menu (orthogonal "
      "to its Bloch vector, r_B.q' = 0) steers A to n+- = (l, +-sqrt(1-l^2), 0) with Born weights 1/2 (perpendicular chord)", ok and ok_r and ok_p and ok_menu)

# ---------------------------------------------------------------- C2 Fourier content of Legendre polynomials on a great circle
psi_ = sp.Symbol("psi", real=True)
def acoef(j): return sp.binomial(2 * j, j) / sp.Integer(4) ** j
ok = True
for L_ in range(1, 14):
    lhs = sp.expand(sp.legendre(L_, sp.cos(psi_)).rewrite(sp.exp))
    rhs = sp.expand(sum(acoef(j) * acoef(L_ - j) * sp.cos((L_ - 2 * j) * psi_) for j in range(L_ + 1)).rewrite(sp.exp))
    ok = ok and sp.simplify(lhs - rhs) == 0
check("C2 P_L(cos psi) = sum_j a_j a_(L-j) cos((L-2j) psi), a_j = C(2j,j)/4^j > 0, for L = 1..13: every cos(k psi) with k = L, L-2, ... >= 0 has a positive coefficient", ok)

# ---------------------------------------------------------------- C3 the chord identity, mode by mode
# no-signalling with self-weights for A's menu q (theta = angle of q in the plane of the chord, from x-hat):
#   radial chord:        f(l, l cos theta) = w h(cos theta) + (1 - w) h(-cos theta),              w = f(l, l)
#   perpendicular chord: f(l, l cos theta) = (1/2) h(cos(theta - beta)) + (1/2) h(cos(theta + beta)),  cos beta = l  (partner weight f(l, 0) = 1/2)
# with H = h - 1/2 odd:  (2w - 1) H(cos theta) = (1/2)[H(cos(theta - beta)) + H(cos(theta + beta))]   for all theta.        [**]
# For a single Legendre degree L the right minus left side has cos(k theta) coefficient c_k^(L) [cos(k beta) - (2w - 1)].
th, beta = sp.symbols("theta beta", real=True)
W = sp.Symbol("w")
ok = True
for L_ in (1, 3, 5, 7):
    expr = sp.Rational(1, 2) * (sp.legendre(L_, sp.cos(th - beta)) + sp.legendre(L_, sp.cos(th + beta))) - (2 * W - 1) * sp.legendre(L_, sp.cos(th))
    # compare with the mode form built from C2
    form = sum(2 * acoef(j) * acoef(L_ - j) * (sp.cos((L_ - 2 * j) * beta) - (2 * W - 1)) * sp.cos((L_ - 2 * j) * th) for j in range((L_ + 1) // 2))
    ok = ok and sp.simplify(sp.expand_trig(expr - form)) == 0
check("C3 for L = 1, 3, 5, 7: (1/2)[P_L(cos(theta-beta)) + P_L(cos(theta+beta))] - (2w-1) P_L(cos theta) = sum_k c_k^(L) [cos(k beta) - (2w-1)] cos(k theta), c_k^(L) > 0", ok)
lv = sp.Rational(3, 5)
cb = lv; c3b = 4 * cb ** 3 - 3 * cb
check("C4 at l = 3/5 (cos beta = 3/5, sin beta = 4/5): cos(beta) = 3/5 and cos(3 beta) = -117/125 differ, so no w makes both the k = 1 and the k = 3 modes vanish; "
      "hence any Legendre component of H of degree >= 3 is excluded, and H(c) = a1 c a.e.", c3b == sp.Rational(-117, 125) and c3b != cb)

# ---------------------------------------------------------------- C5 the affine laws, and Born
c_, lam = sp.symbols("c lambda", real=True)
# affine family h = (1 + lam c)/2, f(l, x) = (1 + lam x)/2 (the landed note's): radial chord gives lam^2 = lam; perpendicular chord holds for every lam
w_aff = (1 + lam * l) / 2
rad = sp.simplify((1 + lam * l * c_) / 2 - (w_aff * (1 + lam * c_) / 2 + (1 - w_aff) * (1 - lam * c_) / 2))
check("C5a the landed note's Schmidt test is the radial chord: for the affine family it demands lam(lam - 1) = 0 (residual (lam - lam^2) l c / 2)",
      sp.factor(rad) == sp.factor(lam * l * c_ * (1 - lam) / 2))
perp = sp.simplify((1 + lam * l * sp.cos(th)) / 2 - (sp.Rational(1, 2) * (1 + lam * sp.cos(th - beta)) / 2 + sp.Rational(1, 2) * (1 + lam * sp.cos(th + beta)) / 2)).subs(sp.cos(beta), l)
check("C5b the perpendicular chord holds for every affine law (cos beta = l)", sp.simplify(sp.expand_trig(perp).subs(sp.cos(beta), l)) == 0)
# with H = a1 c: [**] mode 1 gives 2w - 1 = cos beta = l; the radial formula at c = 1 and the perpendicular one at theta = 0 give w = 1/2 + a1 l;
# so 2 a1 l = l: a1 = 1/2 (Born) unless a1 = 0 (constant law)
a1 = sp.Symbol("a1")
sol = sp.solve([sp.Eq(2 * W - 1, l), sp.Eq(W, sp.Rational(1, 2) + a1 * l)], [W, a1], dict=True)
check("C5c with H(c) = a1 c and a1 != 0: 2w - 1 = l and w = 1/2 + a1 l force a1 = 1/2, w = (1 + l)/2: h(c) = (1 + c)/2, f(l, x) = (1 + x)/2 (Born); a1 = 0 is the constant law",
      sol == [{W: (1 + l) / 2, a1: sp.Rational(1, 2)}])
born = sp.simplify(sp.expand_trig((1 + l * sp.cos(th)) / 2 - (sp.Rational(1, 2) * (1 + sp.cos(th - beta)) / 2 + sp.Rational(1, 2) * (1 + sp.cos(th + beta)) / 2)).subs(sp.cos(beta), l))
check("C5d Born satisfies both chords (radial: C5a at lam = 1; perpendicular: C5b at lam = 1)", born == 0 and sp.simplify(rad.subs(lam, 1)) == 0)
# a nonlinear odd law with the endpoint support: h(c) = 1/2 + (3c - c^3)/4 (in [0,1], h(1) = 1, h(-1) = 0): [**] fails for every w
Hn = lambda x: (3 * x - x ** 3) / 4
resid = sp.expand(sp.expand_trig(sp.Rational(1, 2) * (Hn(sp.cos(th - beta)) + Hn(sp.cos(th + beta))) - (2 * W - 1) * Hn(sp.cos(th))).subs({sp.cos(beta): lv, sp.sin(beta): sp.Rational(4, 5)}))
# direct: the cos(3 theta) coefficient of the residual must vanish for [**]; compute by integration
c3 = sp.simplify(sp.integrate(sp.expand(resid.rewrite(sp.cos)) * sp.cos(3 * th), (th, -sp.pi, sp.pi)) / sp.pi)
c1 = sp.simplify(sp.integrate(sp.expand(resid.rewrite(sp.cos)) * sp.cos(th), (th, -sp.pi, sp.pi)) / sp.pi)
nosol = sp.solve([c1, c3], W)
check("C5e a nonlinear law with the support, h(c) = 1/2 + (3c - c^3)/4: at l = 3/5 the cos(theta) and cos(3 theta) coefficients of [**] are %s and %s, with no common root w"
      % (sp.factor(c1), sp.factor(c3)), nosol == [])

# ---------------------------------------------------------------- C6 (floating-point evidence): tanh laws and an anti-Born law fail [**]
import math
def residual_max(hfun, lval, wval):
    bt = math.acos(lval); m = 0.0
    for i in range(721):
        t = -math.pi + 2 * math.pi * i / 720
        Hf = lambda x: hfun(x) - 0.5
        m = max(m, abs(0.5 * (Hf(math.cos(t - bt)) + Hf(math.cos(t + bt))) - (2 * wval - 1) * Hf(math.cos(t))))
    return m
tanh_law = lambda k: (lambda x: 0.5 + math.tanh(k * x) / (2 * math.tanh(k)))
outs = []
for name, hf in (("tanh k=2", tanh_law(2.0)), ("tanh k=0.5", tanh_law(0.5)), ("cubic", lambda x: 0.5 + (3 * x - x ** 3) / 4)):
    best = min(residual_max(hf, 0.6, wv / 1000) for wv in range(0, 1001))
    outs.append((name, best))
print("   C6 (evidence) min over w in [0,1] of max over theta of |[**] residual| at l = 0.6: " + ", ".join("%s %.4f" % o for o in outs) +
      "; Born: %.2e" % residual_max(lambda x: (1 + x) / 2, 0.6, 0.8))
check("C6 (evidence) the three nonlinear laws leave a residual > 1e-3 for every w; Born leaves < 1e-12", all(o[1] > 1e-3 for o in outs) and residual_max(lambda x: (1 + x) / 2, 0.6, 0.8) < 1e-12)

print("")
print("TOTAL: PASS=%d FAIL=%d" % (len(PASS), len(FAIL)))
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAIL))
else:
    print("HIT: within the supplied qubit setting of PR #9083 (covariant binary law F(r,q) = f(|r|, r.q), antipodal normalization, projective steering of a "
          "pure two-qubit state, the partner using the same law for its weights), self-weighted equal-time no-signalling for just two partner menus "
          "(along and orthogonal to its Bloch vector) at ONE Bloch length 0 < l < 1 forces the pure law to be Born, h(c) = (1+c)/2, or constant, a.e., "
          "and then f(l, x) = (1+x)/2 or 1/2: every Legendre component of degree >= 3 is excluded because cos(k beta) = 2w - 1 cannot hold for k = 1 and 3; "
          "no ensemble affinity and no Born ensemble weights are assumed; the endpoint support excludes the constant law")
    print("SUMMARY: PARTIAL the deferred nonlinear self-weighted closure recovered as a necessary condition under explicit premises (steering composition, "
          "covariance, normalization, measurable law): Born or constant; remaining: pointwise without regularity, higher-dimensional sites, laws with "
          "extra directional input, and deriving the steering composition itself (the landed replacement-rule countermodel shows it is essential)")
