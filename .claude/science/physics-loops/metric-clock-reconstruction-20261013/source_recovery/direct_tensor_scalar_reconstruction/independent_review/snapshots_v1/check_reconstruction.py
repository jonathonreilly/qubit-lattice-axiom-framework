#!/usr/bin/env python3
"""Direct action/source/observable checks for the frozen tensor-scalar candidate."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math
import sys

import numpy as np
from scipy.integrate import quad
import sympy as sp

ROOT = Path(__file__).resolve().parent


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def symbolic_operator():
    eta = sp.diag(-1, 1, 1, 1)
    w, k = sp.symbols('w k', real=True)
    q = sp.Matrix([-w, 0, 0, k])
    qu = eta*q
    q2 = (q.T*qu)[0]
    entries = [(i, j) for i in range(4) for j in range(i, 4)]
    hs = sp.symbols('h:10')
    h = sp.zeros(4)
    for z, (i, j) in zip(hs, entries):
        h[i, j] = h[j, i] = z

    def einstein(hh):
        hq = hh*qu
        tr = sp.trace(eta*hh)
        ric = sp.Matrix(4, 4, lambda i, j:
                        (-q[i]*hq[j]-q[j]*hq[i]+q2*hh[i, j]+q[i]*q[j]*tr)/2)
        return sp.simplify(ric-eta*sp.trace(eta*ric)/2)

    gl = einstein(h)
    assert all(sp.expand(z) == 0 for z in qu.T*gl)
    gauge_columns = []
    for a in range(4):
        xi = sp.eye(4)[:, a]
        hg = q*xi.T+xi*q.T
        assert einstein(hg) == sp.zeros(4)
        gauge_columns.append(sp.Matrix([hg[i, j] for i, j in entries]))
    gauges = sp.Matrix.hstack(*gauge_columns)
    mat = sp.Matrix([gl[i, j] for i, j in entries]).jacobian(hs)
    ranks = []
    for frequency, wave_number in [(2, 1), (1, 1), (3, 3), (0, 1)]:
        substitutions = {w: frequency, k: wave_number}
        rank = mat.subs(substitutions).rank()
        gauge_rank = gauges.subs(substitutions).rank()
        expected = 4 if abs(frequency) == abs(wave_number) else 6
        assert rank == expected and gauge_rank == 4
        ranks.append(dict(omega_over_c=frequency, k=wave_number, operator_rank=rank,
                          kernel_dimension=10-rank, gauge_rank=gauge_rank))
    plus = sp.diag(0, 1, -1, 0)
    cross = sp.zeros(4)
    cross[1, 2] = cross[2, 1] = 1
    for ht in [plus, cross]:
        assert sp.simplify(einstein(ht)-q2*ht/2) == sp.zeros(4)
        contraction = sp.trace((eta*ht*eta).T*einstein(ht))
        assert sp.simplify(contraction-q2) == 0
    # Constant field metric: product-rule stress identity, two nontrivial fields.
    coords = sp.symbols('t x y z', real=True)
    fields = [sp.Function('f')(*coords), sp.Function('g')(*coords)]
    K = sp.Matrix([[2, 1], [1, 3]])
    dp = sp.Matrix([[sp.diff(f, x) for x in coords] for f in fields])
    square = sum(K[a, b]*sum(eta[r, r]*dp[a, r]*dp[b, r] for r in range(4))
                 for a in range(2) for b in range(2))
    stress = sp.Matrix(4, 4, lambda i, j:
                       2*sum(K[a, b]*dp[a, i]*dp[b, j]
                             for a in range(2) for b in range(2))-eta[i, j]*square)
    boxes = [sum(eta[r, r]*sp.diff(f, coords[r], 2) for r in range(4)) for f in fields]
    for nu in range(4):
        div = sum(eta[mu, mu]*sp.diff(stress[mu, nu], coords[mu]) for mu in range(4))
        rhs = 2*sum(K[a, b]*boxes[a]*dp[b, nu] for a in range(2) for b in range(2))
        assert sp.expand(div-rhs) == 0
    a, gamma = sp.symbols('a gamma', nonnegative=True)
    gamma_map = (1-a)/(1+a)
    ratio = (1+a/6)/(1+a)
    assert sp.factor(ratio-(7+5*gamma_map)/12) == 0
    assert sp.factor((1-gamma_map)/(1+gamma_map)-a) == 0
    return dict(bianchi=True, four_gauge_nulls=True, full_metric_ranks=ranks,
                TT_quadratic_normalization=True, scalar_stress_divergence=True,
                static_radiation_elimination=True)


def field_examples():
    R = sp.Rational
    examples = [
        ('zero', sp.Matrix([[1]]), sp.Matrix([0])),
        ('small', sp.Matrix([[1]]), sp.Matrix([R(1, 10)])),
        ('unit', sp.Matrix([[1]]), sp.Matrix([1])),
        ('diagonal_two', sp.diag(2, 3), sp.Matrix([R(1, 5), -R(1, 7)])),
        ('mixed_two', sp.Matrix([[2, 1], [1, 3]]), sp.Matrix([R(1, 4), R(1, 3)])),
    ]
    result = []
    for name, K, alpha in examples:
        assert K.is_positive_definite is True
        a = (alpha.T*K.inv()*alpha)[0]
        assert a >= 0
        transforms = [sp.Matrix([[2]]), sp.Matrix([[-3]])] if len(alpha) == 1 else [
            sp.Matrix([[1, 2], [0, 1]]), sp.Matrix([[0, 1], [-2, 1]])]
        for S in transforms:
            kp, ap = S.T*K*S, S.T*alpha
            assert sp.simplify((ap.T*kp.inv()*ap)[0]-a) == 0
        result.append((name, np.array(K, dtype=float), np.array(alpha, dtype=float).ravel(), a))
    return result


def moment(phase, mu, radius, omega):
    r = radius*np.array([math.cos(phase), math.sin(phase), 0.0])
    v = radius*omega*np.array([-math.sin(phase), math.cos(phase), 0.0])
    acc, jerk = -omega**2*r, -omega**2*v
    second = mu*(np.outer(acc, r)+np.outer(r, acc)+2*np.outer(v, v))
    third = mu*(np.outer(jerk, r)+np.outer(r, jerk)
                +3*(np.outer(acc, v)+np.outer(v, acc)))
    integrated_stress = mu*(np.outer(v, v)-omega**2*np.outer(r, r))
    assert np.allclose(second, 2*integrated_stress, rtol=2e-14, atol=1e-15)
    assert abs(np.trace(third)) < 2e-15
    assert abs(np.sum(third*third)/(32*mu**2*radius**4*omega**6)-1) < 3e-15
    return second, third


def tt(S, n):
    P = np.eye(3)-np.outer(n, n)
    return P@S@P-.5*P*np.trace(P@S)


def sphere_flux(S, K, alpha, gs, c, distance, nmu=16, nphi=32):
    v = np.linalg.solve(K, alpha)
    mus, ws = np.polynomial.legendre.leggauss(nmu)
    tensor, scalar = 0.0, 0.0
    for z, wz in zip(mus, ws):
        for az in np.arange(nphi)*2*math.pi/nphi:
            n = np.array([math.sqrt(1-z*z)*math.cos(az), math.sqrt(1-z*z)*math.sin(az), z])
            hd = 2*gs/(c**4*distance)*tt(S, n)
            pd = -gs/(2*c**4*distance)*v*(n@S@n)
            weight = wz*2*math.pi/nphi
            tensor += weight*c**3*distance**2/(32*math.pi*gs)*np.sum(hd*hd)
            scalar += weight*c**3*distance**2/(4*math.pi*gs)*(pd@K@pd)
    return tensor, scalar


def numerical_checks(examples):
    c, gn, mass, radius, mu, omega, distance = 1000., 1., 1., 1., .24, 1., 1e6
    patterns, fluxes, lenses, invariant_rows = [], [], [], []
    phases = [0., .37, 1.2, 2.5]
    for name, K, alpha, exact_a in examples:
        a = float(exact_a)
        gs = gn/(1+a)
        gamma = (1-a)/(1+a)
        invariant_rows.append(dict(name=name, K=K.tolist(), alpha=alpha.tolist(),
                                   exact_a=str(exact_a), a=a, gamma=gamma,
                                   scalar_force_fraction=a/(1+a), G_star=gs))
        for phase in phases:
            I2, I3 = moment(phase, mu, radius, omega)
            tensor, scalar = sphere_flux(I3, K, alpha, gs, c, distance)
            pt = gs*np.sum(I3*I3)/(5*c**5)
            ps = a*pt/6
            trerr = abs(tensor/pt-1)
            srerr = abs(scalar/ps-1) if ps else abs(scalar)
            assert trerr < 4e-13 and srerr < 4e-13
            if not ps:
                assert scalar == 0
            comparator = gn*np.sum(I3*I3)/(5*c**5)
            ratio = (tensor+scalar)/comparator
            assert abs(ratio-(7+5*gamma)/12) < 4e-13
            fluxes.append(dict(name=name, phase=phase, tensor=tensor, scalar=scalar,
                               tensor_formula=pt, scalar_formula=ps,
                               tensor_fractional_error=trerr,
                               scalar_fractional_error=srerr if ps else None,
                               same_orbit_ratio=ratio))
            H0 = 2*gs*mu*radius**2*omega**2/(c**4*distance)
            for ci in [-1., -.6, 0., .6, 1.]:
                si = math.sqrt(1-ci*ci)
                n, p, q = np.array([si, 0., ci]), np.array([ci, 0., -si]), np.array([0., 1., 0.])
                h = 2*gs/(c**4*distance)*tt(I2, n)
                field = -gs/(2*c**4*distance)*np.linalg.solve(K, alpha)*(n@I2@n)
                zeta = alpha@field
                observed = np.array([.5*(p@h@p-q@h@q), p@h@q, 2*zeta])/H0
                expected = np.array([-(1+ci*ci)*math.cos(2*phase),
                                     -2*ci*math.sin(2*phase), a*(1-ci*ci)*math.cos(2*phase)])
                err = float(np.max(np.abs(observed-expected)))
                assert err < 5e-14
                # Fourier linear curvature of h00=-2zeta, hij=hTT+2zeta delta.
                spatial_metric = h+2*zeta*np.eye(3)
                curvature = .5*(spatial_metric-2*zeta*np.outer(n, n))
                tide = .5*h+zeta*(np.eye(3)-np.outer(n, n))
                assert np.max(np.abs(curvature-tide))/H0 < 3e-15
                patterns.append(dict(name=name, phase=phase, cos_inclination=ci,
                                     normalized_amplitudes=observed.tolist(),
                                     predicted=expected.tolist(), absolute_normalized_error=err))
        for b in [.7, 2., 10.]:
            value, err = quad(lambda z:2*gs*mass*b/(c*c*(b*b+z*z)**1.5),
                              -np.inf, np.inf, epsabs=1e-18, epsrel=3e-13)
            theory = 2*(1+gamma)*gn*mass/(c*c*b)
            assert abs(value/theory-1) < 2e-12
            lenses.append(dict(name=name, impact_parameter=b, integrated_bending=value,
                               prediction=theory, fractional_error=abs(value/theory-1),
                               quadrature_estimate=err))
    # A different grid checks the last nontrivial mixed-field example.
    name, K, alpha, exact_a = examples[-1]
    S = moment(.37, mu, radius, omega)[1]
    lo = sphere_flux(S, K, alpha, gn/(1+float(exact_a)), c, distance, 8, 16)
    hi = sphere_flux(S, K, alpha, gn/(1+float(exact_a)), c, distance, 16, 32)
    refinements = [abs(x/y-1) for x, y in zip(lo, hi)]
    assert max(refinements) < 4e-13
    return dict(field_examples=invariant_rows, flux_rows=fluxes, pattern_rows=patterns,
                lens_rows=lenses, angular_grid_refinement=refinements,
                declared_orbit=dict(c=c, G_N=gn, total_mass=mass, radius=radius,
                                    reduced_mass=mu, omega=omega, wave_radius=distance,
                                    relative_speed_over_c=radius*omega/c,
                                    potential_scale_over_c_squared=gn*mass/radius/c**2))


def main():
    symbolic = symbolic_operator()
    examples = field_examples()
    numerical = numerical_checks(examples)
    lower = sp.Rational(9992, 10000)
    amax = sp.factor((1-lower)/(1+lower))
    fmax = sp.factor((1-lower)/2)
    rmin = sp.factor((7+5*lower)/12)
    assert amax == sp.Rational(1, 2499) and fmax == sp.Rational(1, 2500)
    assert rmin == sp.Rational(2999, 3000)
    output = dict(created_at=datetime.now(timezone.utc).isoformat(),
                  source_sha256={n:digest(ROOT/n) for n in ['check_reconstruction.py', 'DIRECT_RECONSTRUCTION.md', 'PROTOCOL.md']},
                  symbolic=symbolic, **numerical,
                  illustrative_rectangle=dict(gamma_lower=str(lower), original_gamma_upper='2501/2500',
                                               model_gamma_upper='1', max_a=str(amax),
                                               max_scalar_force_fraction=str(fmax),
                                               circular_ratio_lower=str(rmin),
                                               confidence_interval_claim=False),
                  summary=dict(pattern_rows=len(numerical['pattern_rows']),
                               flux_rows=len(numerical['flux_rows']), lens_rows=len(numerical['lens_rows']),
                               max_pattern_normalized_error=max(x['absolute_normalized_error'] for x in numerical['pattern_rows']),
                               max_tensor_flux_fractional_error=max(x['tensor_fractional_error'] for x in numerical['flux_rows']),
                               max_scalar_flux_fractional_error=max(x['scalar_fractional_error'] or 0 for x in numerical['flux_rows']),
                               max_lens_fractional_error=max(x['fractional_error'] for x in numerical['lens_rows'])),
                  scope='Supplied positive tensor/scalar action, weak circular point limit with zero residual body sensitivities; no empirical fit or compact-star theorem.')
    dest = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT/'evidence_v1/RESULTS.json'
    dest.parent.mkdir(exist_ok=True)
    assert not dest.exists(), 'Preserve previous results; use a new version path.'
    dest.write_text(json.dumps(output, indent=2, allow_nan=False)+'\n')
    print(json.dumps(output['summary'], sort_keys=True))


if __name__ == '__main__':
    main()
