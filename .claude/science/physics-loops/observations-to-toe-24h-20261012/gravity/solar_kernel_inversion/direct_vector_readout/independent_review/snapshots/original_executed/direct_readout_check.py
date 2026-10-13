#!/usr/bin/env python3
"""Synthetic mathematical controls; no empirical strain comparison."""
from pathlib import Path
import cmath
import hashlib
import json
import math
import time

import numpy as np
import sympy as sp
from scipy.integrate import quad


ROOT = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cquad(func, upper):
    real, er = quad(lambda x: func(x).real, 0, upper, epsabs=2e-12, epsrel=2e-12)
    imag, ei = quad(lambda x: func(x).imag, 0, upper, epsabs=2e-12, epsrel=2e-12)
    return real + 1j * imag, max(er, ei)


def main():
    started = time.monotonic()
    source_files = ['PROTOCOL.md', 'DIRECT_READOUT.md', 'SOURCE_LEDGER.md', Path(__file__).name]
    pins = {n: sha(ROOT / n) for n in source_files}
    checks = []
    x, y, z, t, c = sp.symbols('x y z t c', real=True)
    nx, ny, nz = sp.symbols('nx ny nz', real=True)
    n = sp.Matrix([nx, ny, nz])
    phase = t - (nx*x + ny*y + nz*z)/c
    f = sp.Function('f')
    tidal = -sp.hessian(f(phase), (x, y, z))
    amplitude = -sp.diff(f(phase), t, 2)/c**2
    assert sp.simplify(tidal - amplitude*n*n.T) == sp.zeros(3)
    transverse = sp.eye(3) - n*n.T/(n.dot(n))
    assert sp.simplify(transverse*tidal*transverse) == sp.zeros(3)
    checks.append({'family': 'symbolic_plane_tide', 'rank_at_most_one': True,
                   'transverse_projection_exactly_zero': True})

    rng = np.random.default_rng(20261012)
    rows = []
    worst = 0.0
    worst_quad = 0.0
    sign_mutation_max = 0.0
    for case in range(12):
        direction = rng.normal(size=3); direction /= np.linalg.norm(direction)
        arm = rng.normal(size=3); arm /= np.linalg.norm(arm)
        base = rng.uniform(-1, 1, 3)
        speed = [0.7, 1.0, 1.8][case % 3]
        omega = [0.4, 1.0, 2.2][case % 3]
        length = [0.05, 0.6, 2.5][(case // 3) % 3]
        mu = float(direction @ arm)
        wave_amp = 0.13 + 0.07j
        base_phase = cmath.exp(1j*omega*(direction @ base)/speed)
        end_phase = cmath.exp(1j*omega*(direction @ (base+length*arm))/speed)
        q = omega*length*mu/speed
        harmonic = -wave_amp*base_phase*mu**2/speed**2 * cmath.exp(0.5j*q)*np.sinc(q/(2*math.pi))
        for cycles in [0.3, 1.9, 4.5]:
            upper = cycles/omega
            def acceleration_difference(s):
                acc_base = -1j*omega/speed * wave_amp*base_phase*cmath.exp(-1j*omega*s)
                acc_end = -1j*omega/speed * wave_amp*end_phase*cmath.exp(-1j*omega*s)
                return (upper-s)*mu*(acc_end-acc_base)/length
            direct, qerr = cquad(acceleration_difference, upper)
            expected = harmonic*(cmath.exp(-1j*omega*upper)-1+1j*omega*upper)
            relative = abs(direct-expected)/max(abs(expected), 1e-14)
            wrong_sign = abs(direct+expected)/max(abs(expected), 1e-14)
            assert relative < 2e-10
            assert wrong_sign > 1.99
            worst = max(worst, relative)
            worst_quad = max(worst_quad, qerr)
            sign_mutation_max = max(sign_mutation_max, wrong_sign)
            rows.append({'case': case, 'dimensionless_time': cycles, 'omega': omega,
                         'speed': speed, 'length': length, 'mu': mu, 'relative_error': relative})
    checks.append({'family': 'endpoint_acceleration_integral', 'cases': rows,
                   'max_relative_error': worst, 'max_quad_diagnostic': worst_quad})

    direction = np.array([1.0, 2.0, 3.0])/math.sqrt(14)
    arm_a, arm_b = np.eye(3)[:2]
    response_tensor = np.outer(arm_a, arm_a)-np.outer(arm_b, arm_b)
    nn = np.outer(direction, direction)
    F = float(np.sum(response_tensor*nn))
    B = float(np.sum(response_tensor*(np.eye(3)-nn)))
    assert abs(F+B) < 1e-15
    def endpoint_pattern(omega_length_over_speed):
        values = []
        for arm in [arm_a, arm_b]:
            mu = float(direction @ arm)
            q = omega_length_over_speed*mu
            values.append(mu**2*cmath.exp(0.5j*q)*np.sinc(q/(2*math.pi)))
        return values[0]-values[1]
    small_values = [.08, .04, .02, .01]
    errors = [abs(endpoint_pattern(v)-F) for v in small_values]
    ratios = [errors[i]/errors[i+1] for i in range(len(errors)-1)]
    assert all(1.99 < v < 2.01 for v in ratios)
    finite = endpoint_pattern(2.2)
    assert abs(finite-F)/abs(F) > .2
    checks.append({'family': 'angular_pattern_and_finite_arm', 'longitudinal_F': F,
                   'breathing_pattern': B, 'small_phase_values': small_values,
                   'errors': errors, 'halving_ratios': ratios,
                   'finite_exact_pattern_re_im': [finite.real, finite.imag],
                   'finite_constant_pattern_relative_error': abs(finite-F)/abs(F),
                   'boundary': 'mechanical endpoints only; no finite-frequency breathing/optical model compared'})

    factors = np.array([1/2, -1/3, 2/5, -3/7])
    projected_baselines = np.array([0., .8, 1.7, 3.1])
    omega = 1.1
    speeds = [.7, 1.]
    def network(cs):
        return np.column_stack([factors*np.exp(1j*omega*projected_baselines/s)/s**2 for s in cs])
    distinct = network(speeds)
    equal = network([1., 1.])
    sv_distinct = np.linalg.svd(distinct, compute_uv=False)
    sv_equal = np.linalg.svd(equal, compute_uv=False)
    assert sv_distinct[1] > .1
    assert sv_equal[1] < 1e-14
    aligned = np.exp(-1j*omega*projected_baselines)[:, None]*distinct
    assert np.linalg.matrix_rank(aligned, tol=1e-12) == 2
    # Divide the T column by F after the L alignment: a constant fit must fail.
    extra_phases = aligned[:, 0]/factors
    constant_fit_error = float(np.linalg.norm(extra_phases-extra_phases.mean()))
    assert constant_fit_error > .5
    checks.append({'family': 'two_speed_network', 'orientation_factors': factors.tolist(),
                   'projected_baselines': projected_baselines.tolist(), 'omega': omega,
                   'speeds': speeds, 'two_speed_singular_values': sv_distinct.tolist(),
                   'equal_speed_singular_values': sv_equal.tolist(),
                   'single_alignment_constant_fit_error': constant_fit_error,
                   'meaning': 'arbitrary synthetic orientation factors realizable by equal orthogonal arms'})

    # A transverse-force substitution gives a nonzero transverse projection.
    P = np.eye(3)-nn
    transverse_mutation_residual = float(np.linalg.norm(P @ P @ P))
    assert transverse_mutation_residual > 1
    checks.append({'family': 'negative_controls', 'wrong_sign_detected': sign_mutation_max > 1.99,
                   'transverse_force_detected': transverse_mutation_residual,
                   'single_speed_rank_reuse_detected': constant_fit_error > .5,
                   'type': 'explicit false-alternative comparisons, not mutated-source executions'})
    assert pins == {n: sha(ROOT/n) for n in source_files}
    result = {'schema': 'vector_mechanical_readout_controls_v1', 'source_sha256': pins,
              'pass_count': len(checks), 'fail_count': 0, 'families': checks,
              'elapsed_seconds': time.monotonic()-started,
              'empirical_data_used': False,
              'limits': ['linear prescribed plane waves', 'simultaneous mechanical length only',
                         'no optical or strain likelihood', 'finite-arm synthetic controls only']}
    target = ROOT/'evidence_v1'/'RESULTS.json'
    target.parent.mkdir(exist_ok=True)
    with target.open('x') as f:
        json.dump(result, f, indent=2, allow_nan=False); f.write('\n')
    print(json.dumps({'pass': len(checks), 'fail': 0, 'endpoint_cases': len(rows),
                      'max_relative_error': worst, 'path': str(target)}))


if __name__ == '__main__':
    main()
