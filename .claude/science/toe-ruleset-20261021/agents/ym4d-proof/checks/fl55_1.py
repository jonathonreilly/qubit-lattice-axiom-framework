#!/usr/bin/env python3
"""fl55_1 -- the leading-coefficient chain, exact arithmetic.  Criteria: checks/fl55_1_criteria.md (written first).
Plain python + sympy exact arithmetic only (no numpy, no floats in verdicts)."""
import random
import sympy as sp

results = []          # (line, ok)  ok=True PASS, False FAIL
controls = []         # (line, fired)

def verdict(name, ok, detail=""):
    results.append((name, ok))
    print(f"{name}: {'PASS' if ok else 'FAIL'}  {detail}")

def control(name, fired, detail=""):
    controls.append((name, fired))
    print(f"{name}: {'control fires' if fired else 'CONTROL DOES NOT FIRE'}  {detail}")

I = sp.I
# ---------------------------------------------------------------- Part A
def generators(N):
    if N == 2:
        s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -I], [I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
        return [m / 2 for m in (s1, s2, s3)]
    if N == 3:
        l = [None] * 8
        l[0] = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
        l[1] = sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]])
        l[2] = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
        l[3] = sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]])
        l[4] = sp.Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]])
        l[5] = sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
        l[6] = sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]])
        l[7] = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / sp.sqrt(3)
        return [m / 2 for m in l]
    raise ValueError

def structure_constants(T):
    n = len(T)
    f = {}
    for a in range(n):
        for b in range(n):
            comm = T[a] * T[b] - T[b] * T[a]
            for c in range(n):
                f[(a, b, c)] = sp.nsimplify(sp.simplify(-2 * I * (comm * T[c]).trace()))
    return f

def partA(N, s_spin, rng):
    T = generators(N); n = len(T)
    # normalisation checks: tr(T^a T^b) = delta/2
    for a in range(n):
        for b in range(n):
            if sp.simplify((T[a] * T[b]).trace() - (sp.Rational(1, 2) if a == b else 0)) != 0:
                raise RuntimeError("generator normalisation")
    f = structure_constants(T)
    ad = []
    for a in range(n):
        M = sp.zeros(n, n)
        for b in range(n):
            for c in range(n):
                M[c, b] = f[(a, b, c)]
        ad.append(M)
    # A0
    A0 = True
    for a in range(n):
        for b in range(n):
            s = sum(f[(a, c, d)] * f[(b, c, d)] for c in range(n) for d in range(n))
            if sp.simplify(s - (N if a == b else 0)) != 0:
                A0 = False
    # field strength
    F = {}
    for a in range(n):
        for mu in range(4):
            for nu in range(mu + 1, 4):
                val = sp.Rational(rng.randint(-9, 9), rng.randint(1, 7))
                F[(a, mu, nu)] = val; F[(a, nu, mu)] = -val
            F[(a, mu, mu)] = 0
    S = sum(F[(a, mu, nu)] ** 2 for a in range(n) for mu in range(4) for nu in range(4))
    Om = {}
    for mu in range(4):
        for nu in range(4):
            M = sp.zeros(n, n)
            for a in range(n):
                if F[(a, mu, nu)] != 0:
                    M += F[(a, mu, nu)] * ad[a]
            Om[(mu, nu)] = M
    trOmOm = sum((Om[(mu, nu)] * Om[(mu, nu)]).trace() for mu in range(4) for nu in range(4))
    trOmOm = sp.nsimplify(sp.simplify(trOmOm))
    X_gh = sp.Rational(1, 12) * trOmOm
    tr_vec_curv = 4 * trOmOm                     # tr over Lorentz (x) adjoint of 1_4 (x) Om Om
    # E^vec has Lorentz blocks E_(mu),(nu) = s * Om_{mu nu};  tr(E^2) = sum_{mu,nu} tr(E_{mu nu} E_{nu mu})
    trE2 = sum((s_spin * Om[(mu, nu)] * s_spin * Om[(nu, mu)]).trace() for mu in range(4) for nu in range(4))
    trE2 = sp.nsimplify(sp.simplify(trE2))
    X_vec = sp.Rational(1, 12) * tr_vec_curv + sp.Rational(1, 2) * trE2
    ratio = sp.nsimplify(sp.simplify((sp.Rational(1, 2) * X_vec - X_gh) / (-X_gh)))
    D = sp.nsimplify(sp.simplify((sp.Rational(1, 2) * sp.Rational(1, 12) * tr_vec_curv - X_gh) / (-X_gh)))
    P = sp.nsimplify(sp.simplify(sp.Rational(1, 2) * sp.Rational(1, 2) * trE2 / (-X_gh)))
    A3 = sp.simplify(X_gh + sp.Rational(N, 12) * S) == 0
    return A0, ratio, D, P, A3, X_gh, S

print("=== fl55_1 Part A ===")
for N in (2, 3):
    rng = random.Random(5501)
    A0, ratio, D, P, A3, X_gh, S = partA(N, 2, rng)
    verdict(f"A0 SU({N}) sum f f = N delta", A0)
    verdict(f"A1 SU({N}) (1/2 X_vec - X_gh)/(-X_gh) = 11", ratio == 11, f"ratio={ratio}")
    verdict(f"A2 SU({N}) diamagnetic D = -1 and paramagnetic P = 12", D == -1 and P == 12, f"D={D}, P={P}")
    verdict(f"A3 SU({N}) X_gh = -(N/12) S", A3, f"X_gh={X_gh}, S={S}")
    rng = random.Random(5501)
    _, ratio_c, _, _, _, _, _ = partA(N, 1, rng)
    control(f"A-c SU({N}) spin coefficient 1 gives ratio != 11", ratio_c != 11, f"ratio(s=1)={ratio_c}")

# ---------------------------------------------------------------- Part B
print("=== fl55_1 Part B ===")
t = sp.symbols('t', real=True)
def b1(X, N):
    # series of exp(i t X) to order 5 via the matrix power series (exact)
    E = sp.eye(N); term = sp.eye(N); acc = sp.eye(N)
    for k in range(1, 6):
        term = term * (I * t * X) / k
        acc = acc + term
    tr_poly = sp.Poly(sp.expand(acc.trace()), t)
    re_tr = sum(sp.re(sp.nsimplify(cf)) * t ** k for (k,), cf in tr_poly.terms())
    expr = sp.expand(1 - re_tr / N)
    c2 = sp.simplify(expr.coeff(t, 2)); c3 = sp.simplify(expr.coeff(t, 3))
    target = sp.simplify((X * X).trace() / (2 * N))
    return sp.simplify(c2 - target) == 0 and c3 == 0, c2, target
X2 = sp.Matrix([[1, 2 - I], [2 + I, -1]])
X3 = sp.Matrix([[1, 1 + I, 0], [1 - I, 2, 2], [0, 2, -3]])
ok2, c2a, ta = b1(X2, 2); ok3, c2b, tb = b1(X3, 3)
verdict("B1 t^2 coefficient = tr(X^2)/(2N), t^3 coefficient 0 (N=2,3)", ok2 and ok3, f"N2: {c2a} vs {ta}; N3: {c2b} vs {tb}")
Nsym = sp.symbols('N', positive=True)
b0 = 11 * Nsym / (48 * sp.pi ** 2)
verdict("B2 2N*2b0 = 11N^2/(12 pi^2)", sp.simplify(2 * Nsym * 2 * b0 - 11 * Nsym ** 2 / (12 * sp.pi ** 2)) == 0)
B3a = sp.simplify(2 * (1 / (48 * sp.pi ** 2)) / (11 / (12 * sp.pi ** 2)) - sp.Rational(1, 22)) == 0
B3b = sp.simplify(sp.Rational(1, 22) * 11 * Nsym ** 2 / (12 * sp.pi ** 2) - Nsym ** 2 / (24 * sp.pi ** 2)) == 0
B3c = (sp.Rational(-20, 2) - 1 == -11) and (sp.Rational(-20, 2) - sp.Rational(1, 2) == sp.Rational(-21, 2)) and \
      (sp.Rational(-21, 2) / (-11) == sp.Rational(21, 22))
verdict("B3 1/22, N^2/(24pi^2), -11, -21/2, 21/22", B3a and B3b and B3c, f"{B3a},{B3b},{B3c}")
control("B-c wrong conversion 2N*b0 != 11N^2/(12pi^2)", sp.simplify(2 * Nsym * b0 - 11 * Nsym ** 2 / (12 * sp.pi ** 2)) != 0)

# ---------------------------------------------------------------- Part C
print("=== fl55_1 Part C ===")
x1, x2, x3, x4 = sp.symbols('x1 x2 x3 x4', real=True)
def gauss_moment(poly):
    w = sp.exp(-(x1 ** 2 + x2 ** 2 + x3 ** 2 + x4 ** 2) / 2) / (2 * sp.pi) ** 2
    val = poly * w
    for v in (x1, x2, x3, x4):
        val = sp.integrate(val, (v, -sp.oo, sp.oo))
    return sp.simplify(val)
r2 = x1 ** 2 + x2 ** 2 + x3 ** 2 + x4 ** 2
m12 = gauss_moment(x1 ** 2 * x2 ** 2); m14 = gauss_moment(x1 ** 4); m1 = gauss_moment(x1 ** 2)
mr4 = gauss_moment(r2 ** 2); mr2 = gauss_moment(r2)
n12 = sp.simplify(m12 / mr4); n14 = sp.simplify(m14 / mr4); n1 = sp.simplify(m1 / mr2)
verdict("C1 <n1^2 n2^2> = 1/24, <n1^4> = 1/8, <n1^2> = 1/4", n12 == sp.Rational(1, 24) and n14 == sp.Rational(1, 8) and n1 == sp.Rational(1, 4),
        f"moments: E x1^2x2^2={m12}, E x1^4={m14}, E|x|^4={mr4}; averages {n12},{n14},{n1}")
def c2_total(avg12, avg1):
    return -32 * avg12 + 4 * avg1 + 4 * avg1 - 1
tot = c2_total(n12, n1)
shell = sp.simplify(2 * sp.pi ** 2 / (2 * sp.pi) ** 4)
d12F = sp.simplify(tot * shell)
beta = -d12F
okC2 = (tot == sp.Rational(-1, 3)) and sp.simplify(shell - 1 / (8 * sp.pi ** 2)) == 0 and \
       sp.simplify(beta - 1 / (24 * sp.pi ** 2)) == 0 and sp.simplify(beta / 2 - 2 * (1 / (96 * sp.pi ** 2))) == 0 and \
       sp.simplify((2 * sp.pi ** 2 / 24) / (2 * sp.pi) ** 4 - 1 / (192 * sp.pi ** 2)) == 0 and \
       sp.simplify(4 / (192 * sp.pi ** 2) - 1 / (48 * sp.pi ** 2)) == 0
verdict("C2 angular total -1/3, shell 1/(8pi^2), beta = 1/(24pi^2), c_Gamma = 2c_g, 1/(192pi^2), 4/(192pi^2)=1/(48pi^2)", okC2,
        f"total={tot}, shell={shell}, beta={beta}")
control("C-c product-of-marginals <n1^2 n2^2> = 1/16 gives total != -1/3", c2_total(sp.Rational(1, 16), n1) != sp.Rational(-1, 3),
        f"total(1/16)={c2_total(sp.Rational(1, 16), n1)}")

# ---------------------------------------------------------------- overall
allpass = all(ok for _, ok in results)
allfire = all(fi for _, fi in controls)
print("=== fl55_1 SUMMARY ===")
print(f"verdict lines: {sum(ok for _, ok in results)}/{len(results)} PASS; controls fired: {sum(fi for _, fi in controls)}/{len(controls)}")
print("OVERALL:", "PASS" if (allpass and allfire) else ("INVALID (a control did not fire)" if allpass else "FAIL"))
