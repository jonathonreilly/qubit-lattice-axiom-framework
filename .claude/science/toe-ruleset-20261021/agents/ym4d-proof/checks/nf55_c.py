# nf55_c -- the small-z series of K_1 (A&S 9.6.11) checked against the modified Bessel ODE, and its log structure.
# Criteria: nf55_c_criteria.md (written first). Exact symbolic arithmetic; Euler's constant symbolic (gE). No floats.
import sympy as sp
z, Lg, gE = sp.symbols('z Lg gE')
M = 6
def psi(n):        # psi(n) = -gE + H_{n-1}
    return -gE + sum(sp.Rational(1, k) for k in range(1, n))
def series_Y(half):
    I1 = sum((z/2)**(2*k + 1)/(sp.factorial(k)*sp.factorial(k + 1)) for k in range(M + 1))
    S = sum((psi(k + 1) + psi(k + 2))*(z/2)**(2*k + 1)/(sp.factorial(k)*sp.factorial(k + 1)) for k in range(M + 1))
    return 1/z + Lg*I1 - half*S
def D(expr):       # total z-derivative with d(Lg)/dz = 1/z
    return sp.diff(expr, z) + sp.diff(expr, Lg)/z
def residual_coeffs(Y):
    R = sp.expand(z**2*D(D(Y)) + z*D(Y) - (z**2 + 1)*Y)
    P = sp.Poly(sp.expand(R*z), z, Lg)        # multiply by z to clear the 1/z of Y
    bad = []
    for (n, j), c in P.terms():
        if n - 1 <= 2*M + 1 and sp.simplify(c) != 0:
            bad.append(((n - 1, j), c))
    return bad
res = {}
bad = residual_coeffs(series_Y(sp.Rational(1, 2)))
res['C1'] = (len(bad) == 0)
print("C1: nonzero residual coefficients with order <= 2M+1:", bad[:5], "->", res['C1'])
badf = residual_coeffs(series_Y(sp.Integer(1)))
res['C1-F'] = (len(badf) > 0)
print("C1-F (factor 1 instead of 1/2): nonzero coefficients:", badf[:3], "-> fires:", res['C1-F'])
zY = sp.expand(z*series_Y(sp.Rational(1, 2)))
P = sp.Poly(zY, z, Lg)
maxL = max(j for (n, j) in P.monoms())
const = P.coeff_monomial(1)
c_z2L = P.coeff_monomial(z**2*Lg)
negpow = [m for m in P.monoms() if m[0] < 0]
res['C2'] = (maxL == 1) and (const == 1) and (c_z2L == sp.Rational(1, 2)) and not negpow
print("C2: max Lg power", maxL, "| constant", const, "| coeff z^2 Lg", c_z2L, "->", res['C2'])
cube = sp.expand(zY**3)
Pc = sp.Poly(cube, z, Lg)
lowterms = [(m, c) for m, c in Pc.terms() if m[0] <= 6]
okpow = all(0 <= m[1] <= 3 for m, c in lowterms)
c0 = Pc.coeff_monomial(1)
res['C3'] = okpow and (c0 == 1)
print("C3: Lg powers in {0..3} up to z^6:", okpow, "| z^0 coefficient", c0, "->", res['C3'])
ok = res['C1'] and res['C2'] and res['C3'] and res['C1-F']
print("RESULTS:", res)
print("VERDICT:", "PASS" if ok else "FAIL")
