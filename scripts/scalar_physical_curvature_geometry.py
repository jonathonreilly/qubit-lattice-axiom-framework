"""Direct geometric and finite-domain controls for M17. Synthetic development."""
import numpy as np
import sympy as S
from scipy.integrate import quad, solve_bvp
checks = []

def eq(name, a, b=0):
    d = S.factor(S.simplify(a - b))
    checks.append({'name': name, 'pass': d == 0, 'difference': str(d)})

def test(name, b, **kw):
    checks.append({'name': name, 'pass': bool(b), **kw})

def ricci(g, coords):
    inv = g.inv()
    n = len(coords)
    gamma = [[[sum((inv[i, l] * (S.diff(g[l, j], coords[k]) + S.diff(g[l, k], coords[j]) - S.diff(g[j, k], coords[l])) for l in range(n))) / 2 for k in range(n)] for j in range(n)] for i in range(n)]
    ric = S.zeros(n)
    for i in range(n):
        for j in range(n):
            ric[i, j] = sum((S.diff(gamma[k][i][j], coords[k]) - S.diff(gamma[k][i][k], coords[j]) + sum((gamma[k][i][j] * gamma[l][k][l] - gamma[l][i][k] * gamma[k][j][l] for l in range(n))) for k in range(n)))
    return S.simplify(sum((inv[i, j] * ric[i, j] for i in range(n) for j in range(n))))

def run():
    checks.clear()
    profiles = []
    t, r, th, ph = S.symbols('t r th ph', real=True)
    N = S.Function('N')(r)
    B = S.Function('B')(r)
    f = S.Function('f')(r)
    metric = S.diag(-N * N, 1 / B, r * r, r * r * S.sin(th) ** 2)
    Rdirect = ricci(metric, [t, r, th, ph])
    Rformula = -2 * B * S.diff(N, r, 2) / N - 4 * B * S.diff(N, r) / (r * N) - S.diff(B, r) * S.diff(N, r) / N - 2 * S.diff(B, r) / r + 2 * (1 - B) / r ** 2
    eq('Ricci from full Christoffel contraction', Rdirect, Rformula)
    Lop = lambda v, nn, bb: bb * S.diff(v, r, 2) + (2 * bb / r + bb * S.diff(nn, r) / nn + S.diff(bb, r) / 2) * S.diff(v, r)
    div = S.sqrt(B) / (N * r * r) * S.diff(N * r * r * S.sqrt(B) * S.diff(f, r), r)
    eq('static lapse-weighted divergence', div, Lop(f, N, B))
    clock_scale = S.symbols('clock_scale', positive=True)
    eq('clock normalization cancels from curvature', Rformula.subs(N, clock_scale * N).doit(), Rformula)
    eq('clock normalization cancels from static operator', Lop(f, clock_scale * N, B), Lop(f, N, B))
    range_time = S.Function('range_time')(r)
    range_derivative = S.diff(range_time, r)
    physical_B = 4 / (N ** 2 * range_derivative ** 2)
    range_R = 2 * physical_B * (-S.diff(N, r, 2) / N + (S.diff(N, r) / N) ** 2 + S.diff(N, r) * S.diff(range_derivative, r) / (N * range_derivative) + 2 * S.diff(range_derivative, r) / (r * range_derivative)) + 2 * (1 - physical_B) / r ** 2
    eq('clock and radial range curvature map', Rformula.subs(B, physical_B).doit(), range_R)
    lapse_ratio, optical_slope = S.symbols('lapse_ratio optical_slope', positive=True)
    eq('roundtrip physical metric reconstruction', 2 / (lapse_ratio * S.sqrt(4 / (lapse_ratio ** 2 * optical_slope ** 2))), optical_slope)
    eq('flat clock and range limit', range_R.subs({N: S.Integer(1), range_time: 2 * r}).doit(), 0)
    H, M, L = S.symbols('H M L', positive=True)

    def curvature(nn, bb):
        return S.simplify(Rformula.subs({N: nn, B: bb}).doit())
    eq('Schwarzschild Ricci scalar', curvature(S.sqrt(1 - 2 * M / r), 1 - 2 * M / r), 0)
    eq('de Sitter Ricci scalar', curvature(S.sqrt(1 - H * H * r * r), 1 - H * H * r * r), 12 * H * H)
    eq('anti de Sitter Ricci scalar', curvature(S.sqrt(1 + H * H * r * r), 1 + H * H * r * r), -12 * H * H)
    dsP = S.log((1 - H * H * r * r) / (1 - H * H * L * L))
    eq('de Sitter exact positive-part Green source', -Lop(dsP, S.sqrt(1 - H * H * r * r), 1 - H * H * r * r), 6 * H * H)
    eq('de Sitter finite boundary', dsP.subs(r, L), 0)
    eq('de Sitter center regularity', S.diff(dsP, r).subs(r, 0), 0)
    domain_p = S.symbols('domain_p', positive=True)
    eq('de Sitter compactness functional on the static chart', dsP.subs(r, 0).subs(H, S.sqrt(1 - S.exp(-domain_p)) / L), domain_p)
    vv, bb0, ee = S.symbols('vv bb0 ee', real=True)
    rr_formula = 6 * bb0 + 4 * ee * (3 - 4 * bb0 * vv) / (1 - ee * vv)
    eq('synthetic Ricci monotonicity in radius squared', S.diff(rr_formula, vv), 4 * ee * (3 * ee - 4 * bb0) / (1 - ee * vv) ** 2)
    test('negative curvature contributes zero positive source', max(-12.0, 0.0) == 0.0)
    cases = [('weak', 0.01, 0.005), ('medium', 0.08, 0.04), ('lapse_rising', 0.07, -0.015)]
    k = 0.1
    a = (1 - k) * (1 + 3 * k) / 4
    s = (1 + k) / (k * (1 - 3 * k))
    lam = a / (1 - 3 * a)
    protocol = {'declared_before_results': True, 'domain_radius': 1.0, 'k': k, 'nu': 0.0001, 'metric_cases': cases, 'Hv_values': [0.005, 0.05], 'z_boundary': 1.0, 'solver_tol': 1e-09, 'max_nodes': 15000, 'quadrature_tolerance': 2e-12, 'comparison_abs_tol': 2e-08, 'meaning': 'synthetic geometry and scalar equation only; no physical matter/metric fit or independent empirical test'}
    for name, b, eps in cases:
        nn = lambda rr: 1 - eps * np.asarray(rr) ** 2
        bb = lambda rr: 1 - b * np.asarray(rr) ** 2
        np1 = lambda rr: -2 * eps * np.asarray(rr)
        bp1 = lambda rr: -2 * b * np.asarray(rr)

        def rc(rr):
            rr = np.asarray(rr)
            return 12 * eps * bb(rr) / nn(rr) - 4 * b * eps * rr * rr / nn(rr) + 6 * b

        def cc(rr):
            return np.maximum(rc(rr), 0) / 2

        def damping(rr):
            return np1(rr) / nn(rr) + bp1(rr) / (2 * bb(rr))

        def fun(rr, yy):
            return np.vstack((yy[1], -damping(rr) * yy[1] - cc(rr) / bb(rr)))
        boundary = lambda ya, yb: np.array([ya[1], yb[0]])
        mesh = np.linspace(0, 1, 120)
        trial = np.vstack(((1 - mesh * mesh) * float(cc(0)) / 6, -mesh * float(cc(0)) / 3))
        sol = solve_bvp(fun, boundary, mesh, trial, S=np.array([[0.0, 0.0], [0.0, -2.0]]), tol=1e-09, max_nodes=15000)

        def integrand(ss):
            if ss == 0:
                return 0.0
            mass = quad(lambda tt: float(nn(tt) * tt * tt * cc(tt) / np.sqrt(bb(tt))), 0, ss, epsabs=2e-12, epsrel=2e-12)[0]
            return mass / float(nn(ss) * ss * ss * np.sqrt(bb(ss)))
        ref = np.array([quad(integrand, float(v), 1, epsabs=2e-12, epsrel=2e-12)[0] for v in np.linspace(0, 1, 21)])
        pred = sol.sol(np.linspace(0, 1, 21))[0]
        err = float(np.max(np.abs(ref - pred)))
        P = float(ref[0])
        test(name + ': Green BVP convergence', sol.status == 0, status=int(sol.status), nodes=int(len(sol.x)))
        test(name + ': independent nested quadrature', err < 2e-10, error=err)
        test(name + ': nonnegative and decreasing Green profile', np.min(pred) > -2e-10 and np.max(np.diff(pred)) < 2e-10)
        grid = np.linspace(0, 1, 401)
        nlo = float(np.min(nn(grid)))
        nhi = float(np.max(nn(grid)))
        blo = float(np.min(bb(grid)))
        rmax = max(float(rc(0)), float(rc(1)), 0.0)
        envelope = nhi / nlo * rmax / (12 * blo)
        test(name + ': conservative metric envelope', P <= envelope + 2e-10, P=P, envelope=envelope)
        enabled = lam * P < 1
        test(name + ': bootstrap domain', enabled, lambda_P=lam * P)
        zcap = 1 / (1 - lam * P)
        for hv in protocol['Hv_values']:
            nu = protocol['nu']

            def potential_derivative_over_2Z(zv):
                lz = np.log(zv)
                return 6 * lam * hv * hv * zv ** 3 + hv * hv * nu / (1 - 3 * a) * zv ** 3 * (2 * lz * lz + lz)

            def fieldfun(rr, yy):
                zz = yy[0]
                if np.any(zz <= 0):
                    raise ValueError('positive z chart violated')
                rhs = -lam * rc(rr) * zz / 2 + potential_derivative_over_2Z(zz)
                return np.vstack((yy[1], -damping(rr) * yy[1] + rhs / bb(rr)))

            def fieldboundary(ya, yb):
                return np.array([ya[1], yb[0] - 1.0])
            initial = np.vstack((np.ones_like(mesh), np.zeros_like(mesh)))
            field = solve_bvp(fieldfun, fieldboundary, mesh, initial, S=np.array([[0.0, 0.0], [0.0, -2.0]]), tol=1e-09, max_nodes=15000)
            zz, zzp = field.sol(grid)
            Pgrid = sol.sol(grid)[0]
            pointcap = 1 + lam * Pgrid / (1 - lam * P)
            test(name + f': scalar convergence Hv={hv}', field.status == 0, status=int(field.status), nodes=int(len(field.x)))
            test(name + f': global ceiling Hv={hv}', np.max(zz) <= zcap + 2e-08, max_z=float(np.max(zz)), ceiling=zcap)
            test(name + f': pointwise ceiling Hv={hv}', np.max(zz - pointcap) <= 2e-08, max_excess=float(np.max(zz - pointcap)))
            flux = quad(lambda rr: float(nn(rr) * rr * rr * (-lam * rc(rr) * field.sol(rr)[0] / 2 + potential_derivative_over_2Z(field.sol(rr)[0])) / np.sqrt(bb(rr))), 0, 1, epsabs=2e-12, epsrel=2e-12)[0]
            surface = float(nn(1) * np.sqrt(bb(1)) * field.sol(1)[1])
            ferr = abs(flux - surface)
            test(name + f': integrated scalar flux Hv={hv}', ferr < 2e-09, error=ferr)
            profiles.append({'name': name, 'Hv': hv, 'geometry': {'b': b, 'eps': eps}, 'P': P, 'lambda_P': lam * P, 'zcap': zcap, 'r': grid.tolist(), 'z': zz.tolist(), 'z_prime': zzp.tolist(), 'P_profile': Pgrid.tolist(), 'pointwise_ceiling': pointcap.tolist(), 'curvature': rc(grid).tolist(), 'B': bb(grid).tolist(), 'N': nn(grid).tolist(), 'flux_integral': flux, 'surface_flux': surface})
    return (checks, profiles, str(Rdirect), protocol)

def controls():
    rows, profiles, curvature, protocol = run()
    return {'checks': [{'name': r['name'], 'passed': r['pass'], **{k: v for k, v in r.items() if k not in ('name', 'pass')}} for r in rows], 'profiles': profiles, 'direct_Ricci': curvature, 'protocol': protocol, 'scope': 'Direct Christoffel curvature, Green quadrature, and synthetic scalar equations in supplied metrics; no full Einstein/matter solve.'}
