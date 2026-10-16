"""M17 author working controls. Mathematical development, no observational fit."""
import sympy as S
checks = []

def eq(name, left, right=0):
    difference = S.factor(S.simplify(left - right))
    checks.append({'name': name, 'pass': difference == 0, 'difference': str(difference)})
    return difference

def test(name, truth, **data):
    checks.append({'name': name, 'pass': bool(truth), **data})

def run():
    checks.clear()
    z, a, s, k, Q, H, nu, x, y, rx, ry = S.symbols('z a s k Q H nu x y rx ry', positive=True)
    E = 1 / z ** 2
    F = 1 + s * E
    J = 1 + (1 - 3 * a) * s * E
    C = (1 + s) * E / F
    D = 1 + 2 * (1 + k) * (x * x + y * y) / 3
    K = J / F ** 2
    ell_u = S.sqrt(a) / F
    Z = Q * (1 - 3 * a) / (a * (1 + s))
    lam = a / (1 - 3 * a)
    f0 = Q / (1 + s)
    du_dz = -1 / (S.sqrt(a) * z)
    eq('Weyl radial kinetic constant', Q / C * (K - 3 * ell_u ** 2) * du_dz ** 2, Z)
    eq('physical gravitational coefficient', Q / C, f0 * (s + z * z))
    eq('full transverse x kinetic', Q / C * (1 + s) * 4 * k / (9 * F * D), 4 * Q * k * z * z / (9 * D))
    eq('full transverse y kinetic', Q / C * (1 + s) * k / (3 * F * D), Q * k * z * z / (3 * D))
    Ubase = S.Rational(3, 2) + 3 * s * (E - 1) ** 2 / (2 * F ** 2)
    Ureg = nu * (1 + s) * S.log(z) ** 2 / (2 * a * F ** 2)
    Ux = k * x * x * z ** rx / 2
    Uy = k * y * y * z ** ry / 3
    Vbase = 3 * Q * H ** 2 * (s + z ** 4) / (1 + s)
    Vreg = Q * H ** 2 * nu * z ** 4 * S.log(z) ** 2 / (a * (1 + s))
    Vx = Q * H ** 2 * k * x * x * (s + z * z) ** 2 * z ** rx / (1 + s) ** 2
    Vy = 2 * Q * H ** 2 * k * y * y * (s + z * z) ** 2 * z ** ry / (3 * (1 + s) ** 2)
    eq('physical base quartic', 2 * Q * H ** 2 * Ubase / C ** 2, Vbase)
    eq('physical regulator', 2 * Q * H ** 2 * Ureg / C ** 2, Vreg)
    eq('physical x potential', 2 * Q * H ** 2 * Ux / C ** 2, Vx)
    eq('physical y potential', 2 * Q * H ** 2 * Uy / C ** 2, Vy)
    eq('regulator derivative sign factor', S.diff(z ** 4 * S.log(z) ** 2, z), z ** 3 * (4 * S.log(z) ** 2 + 2 * S.log(z)))
    eq('transverse derivative positive factors', S.diff((s + z * z) ** 2 * z ** rx, z), z ** (rx - 1) * (s + z * z) * (rx * (s + z * z) + 4 * z * z))
    eq('coupling norm', a / J, a * z * z / (z * z + (1 - 3 * a) * s))
    ak = (1 - k) * (1 + 3 * k) / 4
    sk = (1 + k) / (k * (1 - 3 * k))
    eq('positive kinetic domain', 1 - 3 * ak, (1 - 3 * k) ** 2 / 4)
    eq('vacuum coupling', (a / J).subs({z: 1, a: ak, s: sk}), k)
    eq('curvature coefficient', f0 / Z, lam)
    R, lap, gx, gy, gradz = S.symbols('R lap gx gy gradz')
    Tx = 4 * Q * k * z * z / (9 * D)
    Ty = Q * k * z * z / (3 * D)
    V = Vbase + Vreg + Vx + Vy
    euler = 2 * Z * lap + S.diff(f0 * (s + z * z), z) * R / 2 - S.diff(Tx, z) * gx - S.diff(Ty, z) * gy - S.diff(V, z)
    rhs = -lam * R * z / 2 + (Q * z * (4 * k * gx / (9 * D) + k * gy / (3 * D)) + S.diff(V, z) / 2) / Z
    eq('Euler variation all static channels', euler, 2 * Z * (lap - rhs))
    eq('exact vacuum curvature balance', rhs.subs({R: 12 * H * H, z: 1, x: 0, y: 0, gx: 0, gy: 0}), 0)
    eq('absolute scale Q cancels', S.diff(rhs, Q), 0)
    q = a * z * z / (z * z + (1 - 3 * a) * s)
    eq('coupling monotonicity', S.diff(q, z), 2 * a * (1 - 3 * a) * s * z / (z * z + (1 - 3 * a) * s) ** 2)
    p, b = S.symbols('p b', nonnegative=True)
    bound = b / (1 - lam * p)
    eq('bootstrap equality', bound, b + lam * p * bound)
    t = S.symbols('t', real=True)
    ratio = (s + (b / (1 - t)) ** 2) / (s + b * b)
    eq('conformal ratio upper envelope remainder', 1 / (1 - t) ** 2 - ratio, s * t * (2 - t) / ((1 - t) ** 2 * (s + b * b)))
    qb = S.symbols('qb', positive=True)
    zcap2 = qb * (1 - 3 * a) * s / ((a - qb) * (1 - t) ** 2)
    eq('boundary coupling propagation', a * zcap2 / (zcap2 + (1 - 3 * a) * s), a * qb / (qb + (a - qb) * (1 - t) ** 2))
    ll = S.symbols('ll', real=True)
    eq('radial potential derivative below boundary domain', S.diff(Vbase + Vreg, z), Q * H ** 2 * z ** 3 / (a * (1 + s)) * (12 * a + nu * (4 * S.log(z) ** 2 + 2 * S.log(z))))
    eq('regulator sign-domain exact minimum', 4 * ll ** 2 + 2 * ll, 4 * (ll + S.Rational(1, 4)) ** 2 - S.Rational(1, 4))
    test('unrestricted positive-z sign claim fails', (12 * a + 100 * a * (4 * ll ** 2 + 2 * ll)).subs(ll, -S.Rational(1, 4)) == -13 * a)
    threshold = 12 * H ** 2 * z ** 2 + 2 * nu * H ** 2 / a * z ** 2 * S.log(z) * (2 * S.log(z) + 1)
    eq('potential maximum threshold', S.diff(Vbase + Vreg, z) / (Z * lam * z), threshold)
    eq('strictly increasing regulator threshold', S.diff(threshold, z), 24 * H ** 2 * z + 2 * nu * H ** 2 / a * z * (4 * S.log(z) ** 2 + 6 * S.log(z) + 1))
    eq('threshold vacuum endpoint', threshold.subs(z, 1), 12 * H ** 2)
    return checks

def controls():
    rows = run()
    return {'checks': [{'name': r['name'], 'passed': r['pass'], **{k: v for k, v in r.items() if k not in ('name', 'pass')}} for r in rows], 'scope': 'Exact transformation, full variation, conformal/coupling bounds and domain controls.'}
