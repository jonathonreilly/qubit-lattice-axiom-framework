#!/usr/bin/env python3
"""Attempt J:derive:review-20261004-anisotropic-event-coverage:a1 -- checker (self-contained; imports nothing from the repository).

Supplied setting (NOT an axiom of the framework): four-site Bloch matrix H(f) = i M(f) of the u = +1 quadratic Majorana comparator of the landed notes, couplings
(Jx, Jy, Jz) = (6/5, 4/5, 1), odd term kappa > 0.  The 18-term hopping table below is copied as DATA from the source script (ASSUMED, not re-derived here).
Everything else (Pauli-vector field s, its Fourier form, interval evaluation, Krawczyk tests) is rebuilt here.

What is checked:
  A. exact facts about s (identity |dx|^2 det M = s1^2+s2^2+s3^2, |dx|^2 >= 16/25, s real on the torus);
  B. plane event E2 (f2 = 0, kappa^2 = 99/100): the EXACT zero (cos 2 pi f1 = -17/33, cos 2 pi f3 = -1/3, kappa = 3 sqrt(11)/10) is verified in exact arithmetic,
     enclosed by 200-bit interval arithmetic, shown to lie inside the 1e-9 Krawczyk box (and boxes up to 1e-4), whose unique zero it therefore is;
  C. events E3, E4, E5: the Krawczyk boxes are re-derived and enlarged, the exact kappa^2 is shown to lie in the boxes' kappa range; exact (a, b) coordinates NOT enclosed;
  D. pointwise captures near the anisotropic line-node flip kappa_c (exact rational comparison), six resp. two disjoint Krawczyk boxes, plus a recorded limit of the
     naive parametric (kappa-interval) Krawczyk test.
Tiers: EXACT = sympy/Fraction; INTERVAL = mpmath.iv (outward rounded); FLOAT = Newton centres only (no claim attached).
"""
import sys, time, itertools
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
import mpmath as mp

T0 = time.time()
PASS = 0
FAIL = 0

def check(ok, label, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print("%s %s%s" % ("PASS" if ok else "FAIL", label, (": " + detail) if detail else ""), flush=True)

# ============================================================================ supplied data (ASSUMED) and exact model
TERMS = [(0, 1, (-1, 0, 0), "y"), (0, 1, (0, 0, 0), "x"), (0, 3, (0, 0, -1), "z"), (1, 1, (-1, 0, 0), "odd"), (1, 3, (1, 0, -1), "odd"),
         (3, 1, (0, 0, 1), "odd"), (0, 0, (1, 0, 0), "odd"), (0, 2, (-1, 0, 0), "odd"), (2, 0, (0, 0, 0), "odd"), (2, 3, (0, -1, 0), "y"),
         (2, 3, (0, 0, 0), "x"), (2, 1, (0, 0, 0), "z"), (3, 3, (0, -1, 0), "odd"), (3, 1, (0, 1, 0), "odd"), (1, 3, (0, 0, 0), "odd"),
         (2, 2, (0, 1, 0), "odd"), (2, 0, (0, -1, 1), "odd"), (0, 2, (0, 0, -1), "odd")]
kap = sp.symbols("kappa", positive=True)
z1, z2, z3 = sp.symbols("z1 z2 z3")
Jx, Jy, Jz = sp.Rational(6, 5), sp.Rational(4, 5), sp.Integer(1)
amp = {"x": 2 * Jx, "y": 2 * Jy, "z": 2 * Jz, "odd": 2 * kap}
M = sp.zeros(4, 4)
for (a_, b_, n_, kind) in TERMS:
    t_ = amp[kind]
    mon = z1 ** n_[0] * z2 ** n_[1] * z3 ** n_[2]
    M[a_, b_] += t_ * mon
    M[b_, a_] -= t_ / mon
INV = {z1: 1 / z1, z2: 1 / z2, z3: 1 / z3}
conj = lambda e: sp.expand(e.subs(INV, simultaneous=True).subs(sp.I, -sp.I))
SIG = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
dag = lambda X: X.T.applyfunc(conj)
vec = lambda X: [sp.expand((s_ * X).trace() / 2) for s_ in SIG]
hx = M[:2, :2] * sp.I
hy = M[2:, 2:] * sp.I
Wb = M[:2, 2:]
evec = vec(dag(Wb) * hx * Wb)
dxv = vec(hx)
dyv = vec(hy)
dx2 = sp.expand(sum(q * q for q in dxv))
S = [sp.expand(dx2 * dyv[i] - evec[i]) for i in range(3)]          # the Pauli-vector field s (sympy Laurent polynomials in z, kappa)

# ---------------------------------------------------------------- A. exact facts
D = sp.expand(M.det(method="berkowitz"))
ident = sp.expand(dx2 * D - sum(q * q for q in S)) == 0
check(ident, "A1 exact: |d_x|^2 det M = s1^2 + s2^2 + s3^2 as a Laurent-polynomial identity in z1,z2,z3,kappa (so zeros of s = middle-band touchings once |d_x|^2 > 0)")
c_ = sp.symbols("c_")
form = 4 * kap ** 2 * (2 - z1 ** 2 - z1 ** -2) + sp.Rational(208, 25) + sp.Rational(96, 25) * (z1 + 1 / z1)
ok_dx = sp.expand(dx2 - form) == 0
check(ok_dx, "A2 exact: |d_x|^2 = 16 kappa^2 sin^2(2 pi f1) + 208/25 + (192/25) cos(2 pi f1) >= 208/25 - 192/25 = 16/25 > 0 for every real f, kappa (cos >= -1)")

def fourier(expr):
    P = sp.Poly(sp.expand(expr * z1 ** 4 * z2 ** 4 * z3 ** 4), z1, z2, z3)
    out = {}
    for (a, b, c), cf in P.terms():
        pk = sp.Poly(cf, kap)
        d = {}
        for (m,), cc in pk.terms():
            re_, im_ = sp.re(cc), sp.im(cc)
            d[m] = (Fr(int(re_.p), int(re_.q)), Fr(int(im_.p), int(im_.q)))
        out[(a - 4, b - 4, c - 4)] = d
    return out

def real_form(d):
    deg = max(m for v in d.values() for m in v)
    c0 = [Fr(0)] * (deg + 1)
    half = []
    herm = True
    for k, v in d.items():
        mk = tuple(-q for q in k)
        vm = d.get(mk, {})
        for m in range(deg + 1):
            r1, i1 = v.get(m, (Fr(0), Fr(0)))
            r2, i2 = vm.get(m, (Fr(0), Fr(0)))
            herm &= (r1 == r2 and i1 == -i2)
        if k == (0, 0, 0):
            for m, (r, i) in v.items(): c0[m] += r
        elif k > mk:
            A = [Fr(0)] * (deg + 1)
            B = [Fr(0)] * (deg + 1)
            for m, (r, i) in v.items():
                A[m] += 2 * r
                B[m] += -2 * i                 # 2 Re(c e^{i phi}) = 2 r cos(phi) - 2 i sin(phi)
            half.append((k, A, B))
    return c0, half, herm

FAM = []
HERM = True
for q in S:
    c0, half, herm = real_form(fourier(q))
    FAM.append((c0, half))
    HERM &= herm
check(HERM, "A3 exact: every s_i is a Hermitian Laurent family (coefficient of z^-k = conjugate of that of z^k, for every power of kappa): s is REAL on the torus; real Fourier form (cos/sin, rational coefficients polynomial in kappa) built")

# ============================================================================ interval tools
iv = mp.iv
iv.prec = 110

def pev(p, kv):
    acc = iv.mpf(0)
    for c in reversed(p): acc = acc * kv + iv.mpf(c.numerator) / iv.mpf(c.denominator)
    return acc

def dp(p): return [m * p[m] for m in range(1, len(p))] or [Fr(0)]

def eval_iv(f, kv):
    """values s_i, Jacobian ds_i/df_j, ds_i/dkappa as mpmath.iv enclosures for f (3 intervals) and kv (interval)"""
    TP = 2 * iv.pi
    vals, Jf, Jk = [], [], []
    for c0, half in FAM:
        v = pev(c0, kv)
        dk = pev(dp(c0), kv)
        g = [iv.mpf(0)] * 3
        for k, A, B in half:
            phi = TP * (k[0] * f[0] + k[1] * f[1] + k[2] * f[2])
            co, si = iv.cos(phi), iv.sin(phi)
            a = pev(A, kv)
            b = pev(B, kv)
            v = v + a * co + b * si
            dk = dk + pev(dp(A), kv) * co + pev(dp(B), kv) * si
            for j in range(3):
                if k[j]: g[j] = g[j] + TP * k[j] * (b * co - a * si)
        vals.append(v); Jf.append(g); Jk.append(dk)
    return vals, Jf, Jk

def mid(x): return 0.5 * (float(x.a) + float(x.b))

# float evaluation (centres only)
def fcoefs(kv):
    out = []
    for c0, half in FAM:
        P = lambda p: sum(float(c) * kv ** m for m, c in enumerate(p))
        out.append((P(c0), np.array([h[0] for h in half], float), np.array([P(h[1]) for h in half]), np.array([P(h[2]) for h in half])))
    return out

def sJ(f, kv):
    v, J = [], []
    for c0, K, a, b in fcoefs(kv):
        ph = 2 * np.pi * K @ f
        co, si = np.cos(ph), np.sin(ph)
        v.append(c0 + co @ a + si @ b)
        J.append(2 * np.pi * ((-si * a + co * b) @ K))
    return np.array(v), np.array(J)

def nodes(kv, n=300, seed=1):
    rng = np.random.default_rng(seed)
    found = []
    for _ in range(n):
        f = rng.random(3)
        for _it in range(60):
            v, J = sJ(f, kv)
            try: d = np.linalg.solve(J, v)
            except np.linalg.LinAlgError: break
            f = f - d
            if np.linalg.norm(d) < 1e-14: break
        v, J = sJ(f, kv)
        if np.linalg.norm(v) < 1e-11:
            f = f % 1
            if not any(np.linalg.norm(((f - g + .5) % 1) - .5) < 1e-6 for g in found): found.append(f)
    return found

# ---------------------------------------------------------------- plane systems (unknown w = (a, b, kappa), f = F0 + B (a, b))
def plane_sys(F0, B, w):
    f = [iv.mpf(F0[j]) + B[j][0] * w[0] + B[j][1] * w[1] for j in range(3)]
    vals, Jf, Jk = eval_iv(f, w[2])
    J = [[sum(B[j][c] * Jf[i][j] for j in range(3)) for c in range(2)] + [Jk[i]] for i in range(3)]
    return vals, J

def plane_newton(F0, B, w0, it=14):
    w = np.array(w0, float)
    for _ in range(it):
        vals, J = plane_sys(F0, B, [iv.mpf(float(t)) for t in w])
        Jm = np.array([[mid(J[i][j]) for j in range(3)] for i in range(3)])
        vm = np.array([mid(v) for v in vals])
        w = w - np.linalg.solve(Jm, vm)
    return w

def plane_krawczyk(F0, B, c, rho):
    """Krawczyk operator K(X) = c - Y F(c) + (I - Y J(X))(X - c) on X = c +- rho (all three unknowns); K(X) strictly inside X => exactly one zero in X"""
    W = [iv.mpf(float(t)) for t in c]
    v0, J0 = plane_sys(F0, B, W)
    Y = np.linalg.inv(np.array([[mid(J0[i][j]) for j in range(3)] for i in range(3)]))
    X = [iv.mpf([float(c[i]) - rho, float(c[i]) + rho]) for i in range(3)]
    JX = plane_sys(F0, B, X)[1]
    ok = True
    for i in range(3):
        t = W[i]
        for m in range(3): t = t - iv.mpf(float(Y[i, m])) * v0[m]
        for j in range(3):
            e = iv.mpf(1 if i == j else 0)
            for m in range(3): e = e - iv.mpf(float(Y[i, m])) * JX[m][j]
            t = t + e * (X[j] - W[j])
        ok &= bool(t.a > X[i].a and t.b < X[i].b)
    return ok

# ============================================================================ B. event E2, exact point bound to the 1e-9 box
E2_F0, E2_B = (0, 0, 0), ((1, 0), (0, 0), (0, 1))
# exact torus point (conjugate of the source's representative; f -> -f image): z1 = (-17 - 20 sqrt2 i)/33, z2 = 1, z3 = (-1 + 2 sqrt2 i)/3, kappa = 3 sqrt(11)/10
s2, s11 = sp.sqrt(2), sp.sqrt(11)
Z1 = (-17 - 20 * s2 * sp.I) / 33
Z3 = (-1 + 2 * s2 * sp.I) / 3
Zs = {1: Z1, 2: sp.Integer(1), 3: Z3}
K_E2 = 3 * s11 / 10
unit = sp.simplify(sp.expand(Z1 * sp.conjugate(Z1))) == 1 and sp.simplify(sp.expand(Z3 * sp.conjugate(Z3))) == 1
check(unit and sp.simplify(K_E2 ** 2 - sp.Rational(99, 100)) == 0, "B1 exact: |z1| = |z3| = 1 at the stated point, kappa^2 = 99/100 (cos 2 pi f1 = -17/33, cos 2 pi f3 = -1/3, f2 = 0)")

def exact_eval_at_point(expr):
    """exact value of a Laurent polynomial at (Z1, 1, Z3, K_E2); negative powers via the exact conjugates (unit circle)"""
    P = sp.Poly(sp.expand(expr * z1 ** 4 * z2 ** 4 * z3 ** 4), z1, z2, z3)
    tot = 0
    zc = {1: sp.conjugate(Z1), 2: sp.Integer(1), 3: sp.conjugate(Z3)}
    for (a, b, c), cf in P.terms():
        mon = 1
        for idx, p in zip((1, 2, 3), (a - 4, b - 4, c - 4)):
            mon *= Zs[idx] ** p if p >= 0 else zc[idx] ** (-p)
        tot += cf.subs(kap, K_E2) * mon
    return sp.simplify(sp.expand(tot))

vals_exact = [exact_eval_at_point(q) for q in S]
check(all(v == 0 for v in vals_exact), "B2 exact (sympy, radicals Q(i, sqrt2, sqrt11)): s1 = s2 = s3 = 0 at the stated torus point, kappa = 3 sqrt(11)/10 (so it is a middle-band touching)")

# interval enclosures (200 bit) of the exact coordinates (a, b, kappa) in the plane coordinates f = (a, 0, b)
old = iv.prec
iv.prec = 200
a_ex = 1 - iv.atan2(20 * iv.sqrt(iv.mpf(2)), iv.mpf(-17)) / (2 * iv.pi)          # Im z1 < 0; acos(-17/33) = atan2(20 sqrt2, -17)
b_ex = iv.atan2(2 * iv.sqrt(iv.mpf(2)), iv.mpf(-1)) / (2 * iv.pi)                # Im z3 > 0; acos(-1/3) = atan2(2 sqrt2, -1)
k_ex = 3 * iv.sqrt(iv.mpf(11)) / 10
iv.prec = old
vals_enc, _, _ = eval_iv([a_ex, iv.mpf(0), b_ex], k_ex)
check(all(float(v.a) <= 0 <= float(v.b) for v in vals_enc) and max(float(v.b - v.a) for v in vals_enc) < 1e-20,
      "B3 interval: s(f, kappa) evaluated at the 200-bit enclosures of the exact coordinates encloses 0 with width < 1e-20 (consistency of the enclosures with B2)")

seed = (0.663868, 0.304087, 0.9949874)
cE2 = plane_newton(E2_F0, E2_B, seed)
dist = [max(abs(float(e.a) - cE2[i]), abs(float(e.b) - cE2[i])) for i, e in enumerate((a_ex, b_ex, k_ex))]
print("INFO E2 box centre (float Newton) =", [repr(float(t)) for t in cE2], " max |exact - centre| per coordinate =", ["%.2e" % d for d in dist], flush=True)
RHO_LIST = (1e-9, 1e-8, 1e-6, 1e-4)
inbox = {}
for rho in RHO_LIST:
    inbox[rho] = all(float(cE2[i]) - rho < float(e.a) and float(e.b) < float(cE2[i]) + rho for i, e in enumerate((a_ex, b_ex, k_ex)))
    # floats float(e.a)/float(e.b) are rounded; margins are >> 1e-16 (see INFO line), so the strict inequality is not rounding sensitive
kr = {rho: plane_krawczyk(E2_F0, E2_B, cE2, rho) for rho in RHO_LIST}
check(kr[1e-9], "B4 interval: Krawczyk operator maps the box centre +- 1e-9 (all three unknowns a, b, kappa) strictly into its interior: exactly one zero of the plane system s(a, 0, b; kappa) = 0 in the box")
check(inbox[1e-9], "B5 interval/exact: the 200-bit enclosures of the exact (a, b, kappa) of B2 lie strictly inside the 1e-9 box (max distance from centre %.1e = %.1e of the radius)" % (max(dist), max(dist) / 1e-9))
check(kr[1e-9] and inbox[1e-9], "B6 CONSEQUENCE (proved by B2+B4+B5): the exact E2 point is THE unique zero of the Krawczyk 1e-9 box; the floating proximity test is no longer needed for E2")
check(all(kr[r] and inbox[r] for r in RHO_LIST), "B7 interval: the same holds for radii 1e-8, 1e-6 and 1e-4: uniqueness persists on boxes 10^1..10^5 times larger, so even the old 1e-8 proximity would bind E2 to a certified box (Krawczyk certified, coordinates exact)")

# ============================================================================ C. events E3, E4, E5 (box re-derivation; coordinates of the exact point NOT enclosed)
EVENTS = {
    "E3": dict(F0=(-0.5, 0, 0), B=((1, 0), (1, 0), (0, 1)), seed=(0.849182, 0.757161, 0.518998), poly=(625, -302, 36)),
    "E4": dict(F0=(0.5, 0, 0), B=((1, 0), (0, 1), (1, 0)), seed=(0.103127, 0.218810, 0.388850), poly=(825, 530, -99)),
    "E5": dict(F0=(0, 0, 0), B=((1, 0), (0, 1), (0, 1)), seed=(0.632117, 0.184517, 0.461609), poly=(50403125, -11680400, 200376)),
}
CLOSED = {"E3": (151 + sp.sqrt(301)) / 625, "E4": (14 * sp.sqrt(31) - 53) / 165, "E5": (233608 + 9874 * sp.sqrt(394)) / 2016125}   # the closed forms quoted in the source note
for name, ev in EVENTS.items():
    A_, B_, C_ = (sp.Integer(t) for t in ev["poly"])
    roots = sp.solve(A_ * sp.Symbol("u") ** 2 + B_ * sp.Symbol("u") + C_, sp.Symbol("u"))
    u_match = [r for r in roots if sp.simplify(r - CLOSED[name]) == 0]
    c = plane_newton(ev["F0"], ev["B"], ev["seed"])
    oks = {rho: plane_krawczyk(ev["F0"], ev["B"], c, rho) for rho in (1e-9, 1e-6)}
    # kappa^2 of the closed form inside the Krawczyk kappa range (rigorous: 200-bit enclosure of the closed form vs the exact rational box edges)
    iv.prec = 200
    num = {"E3": (151 + iv.sqrt(iv.mpf(301))) / 625, "E4": (14 * iv.sqrt(iv.mpf(31)) - 53) / 165, "E5": (233608 + 9874 * iv.sqrt(iv.mpf(394))) / 2016125}[name]
    iv.prec = old
    kl = Fr(float(c[2]) - 1e-9)
    kh = Fr(float(c[2]) + 1e-9)
    in_range = (iv.mpf(kl.numerator) / kl.denominator) ** 2 < num and num < (iv.mpf(kh.numerator) / kh.denominator) ** 2
    check(len(u_match) == 1 and oks[1e-9] and oks[1e-6] and in_range,
          "C %s interval/exact: quadratic %s has the quoted closed form as a root (exact); Krawczyk unique zero on the box centre +-1e-9 and +-1e-6 (centre kappa = %.12f); exact kappa^2 = %.12f lies inside the 1e-9 box's kappa^2 range (rigorous). Exact (a, b) NOT enclosed: point-to-box binding for %s stays at floating proximity (open)"
          % (name, ev["poly"], c[2], 0.5 * (float(num.a) + float(num.b)), name))

# ============================================================================ D. pointwise captures near the anisotropic line-node flip kappa_c, and a recorded method limit
kc_sq = (18 * sp.sqrt(91) - 108) / 1375
kc = float(sp.sqrt(kc_sq).evalf(30))
k_up = sp.Rational(27, 125)       # 0.216
k_dn = sp.Rational(429, 2000)     # 0.2145
check(bool(kc_sq < k_up ** 2) and bool(kc_sq > k_dn ** 2),
      "D1 exact: kappa_c^2 = (18 sqrt91 - 108)/1375 (kappa_c = %.9f; value quoted from the source note, not re-derived) satisfies (429/2000)^2 < kappa_c^2 < (27/125)^2: the two test couplings lie on opposite sides of the line-node flip" % kc)

def jac_det_sign(Jf):
    d = (Jf[0][0] * (Jf[1][1] * Jf[2][2] - Jf[1][2] * Jf[2][1]) - Jf[0][1] * (Jf[1][0] * Jf[2][2] - Jf[1][2] * Jf[2][0]) + Jf[0][2] * (Jf[1][0] * Jf[2][1] - Jf[1][1] * Jf[2][0]))
    return 1 if d.a > 0 else (-1 if d.b < 0 else 0)

def pdist(a, b): return np.abs(((a - b + .5) % 1) - .5)

def point_capture(kfr, rho):
    kv = iv.mpf(kfr.numerator) / iv.mpf(kfr.denominator)
    kf = float(kfr)
    nd = nodes(kf)
    res = []
    for f in nd:
        W = [iv.mpf(float(t)) for t in f]
        v0, _, _ = eval_iv(W, kv)
        _, Jm = sJ(f, kf)
        Y = np.linalg.inv(Jm)
        X = [iv.mpf([-rho, rho])] * 3
        full = [W[i] + X[i] for i in range(3)]
        _, JX, _ = eval_iv(full, kv)
        ok = True
        for i in range(3):
            t = iv.mpf(0)
            for m in range(3): t = t - iv.mpf(float(Y[i, m])) * v0[m]
            for j in range(3):
                e = iv.mpf(1 if i == j else 0)
                for m in range(3): e = e - iv.mpf(float(Y[i, m])) * JX[m][j]
                t = t + e * X[j]
            ok &= bool(t.a > -rho and t.b < rho)
        res.append((f, ok, jac_det_sign(JX)))
    return res

rho_pt = 1e-5
up = point_capture(Fr(27, 125), rho_pt)
dn = point_capture(Fr(429, 2000), rho_pt)
disjoint_up = all(pdist(up[i][0], up[j][0]).max() > 2 * rho_pt for i in range(len(up)) for j in range(i))
disjoint_dn = all(pdist(dn[i][0], dn[j][0]).max() > 2 * rho_pt for i in range(len(dn)) for j in range(i))
sg_up = [r[2] for r in up]
sg_dn = [r[2] for r in dn]
check(len(up) == 6 and all(r[1] for r in up) and disjoint_up and 0 not in sg_up and sum(sg_up) == 0,
      "D2 interval (POINTWISE, kappa = 27/125 exactly, 0.00075 above kappa_c): >= 6 distinct simple zeros of s, each unique in its own Krawczyk box of radius 1e-5 (boxes pairwise disjoint), certified Jacobian-determinant signs %s sum to 0; NOT a count (no clearing of the rest of the torus), NOT an interval in kappa" % sg_up)
check(len(dn) == 2 and all(r[1] for r in dn) and disjoint_dn and 0 not in sg_dn and sum(sg_dn) == 0,
      "D3 interval (POINTWISE, kappa = 429/2000, 0.00075 below kappa_c): >= 2 distinct simple zeros (the line pair), signs %s; the float search from 300 random starts found no others (FLOAT, no claim)" % sg_dn)

# naive parametric Krawczyk (kappa as an interval parameter, centre path c + v (kappa - km)) -- recorded limit
def node_velocity(f, km):
    h = 1e-6
    sp_, _ = sJ(f, km + h)
    sm_, _ = sJ(f, km - h)
    _, J = sJ(f, km)
    return -np.linalg.solve(J, (sp_ - sm_) / (2 * h))

def kr_path(c, v, rho, k0, k1):
    km = 0.5 * (k0 + k1)
    kv = iv.mpf([k0, k1])
    dkv = kv - iv.mpf(km)
    path = [iv.mpf(float(c[i])) + iv.mpf(float(v[i])) * dkv for i in range(3)]
    v0, _, _ = eval_iv(path, kv)
    _, Jm = sJ(np.array(c, float), km)
    Y = np.linalg.inv(Jm)
    Xp = iv.mpf([-rho, rho])
    full = [path[i] + Xp for i in range(3)]
    _, JX, _ = eval_iv(full, kv)
    ok = True
    for i in range(3):
        t = iv.mpf(0)
        for m in range(3): t = t - iv.mpf(float(Y[i, m])) * v0[m]
        for j in range(3):
            e = iv.mpf(1 if i == j else 0)
            for m in range(3): e = e - iv.mpf(float(Y[i, m])) * JX[m][j]
            t = t + e * Xp
        ok &= bool(t.a > -rho and t.b < rho)
    return ok

def cell_all(k0, k1, rhos):
    km = 0.5 * (k0 + k1)
    nd = nodes(km, 200)
    for rho in rhos:
        if len(nd) == 6 and all(kr_path(f, node_velocity(f, km), rho, k0, k1) for f in nd): return rho
    return None

r_narrow = cell_all(0.2300, 0.2300001, (1e-3, 1e-4))
r_wide = cell_all(0.2300, 0.2301, (3e-3, 1e-3, 3e-4, 1e-4))
check(r_narrow is not None and r_wide is None,
      "D4 interval (recorded METHOD LIMIT, not a physics claim): the naive parametric Krawczyk test (kappa interval enters as an interval parameter, linear centre path) certifies all six nodes on kappa in [0.2300, 0.2300001] (radius %s) but fails on [0.2300, 0.2301] for every radius tried; interval dependency wrapping of kappa limits cell width to ~1e-7, so a census of a kappa interval near kappa_c needs the source's moving-frame/Taylor treatment of kappa" % (r_narrow,))

# ============================================================================ summary
elapsed = time.time() - T0
print("INFO runtime %.1f s" % elapsed, flush=True)
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL), flush=True)
print("SUMMARY: At the anisotropic coupling (6/5, 4/5, 1) the exact E2 touching (cos 2 pi f1 = -17/33, cos 2 pi f3 = -1/3, kappa = 3 sqrt(11)/10) is rigorously enclosed in, and is the unique zero of, the source's 1e-9 Krawczyk box (also certified for boxes up to 1e-4); E3-E5 boxes re-derived but exact coordinates not enclosed; no kappa-interval census near kappa_c was obtained (only pointwise captures at kappa = 27/125 and 429/2000 and a recorded method limit).", flush=True)
if FAIL == 0:
    print("HIT: exact point-to-box binding for plane event E2 at J=(6/5,4/5,1): the exact zero (a,b,kappa) lies inside the 1e-9 Krawczyk box and in boxes up to 1e-4 (all Krawczyk-certified unique), closing the source note's open floating-proximity gap for E2 only (scope: E2; E3-E5 coordinates unenclosed; no kappa census extension).", flush=True)
sys.exit(0 if FAIL == 0 else 1)
