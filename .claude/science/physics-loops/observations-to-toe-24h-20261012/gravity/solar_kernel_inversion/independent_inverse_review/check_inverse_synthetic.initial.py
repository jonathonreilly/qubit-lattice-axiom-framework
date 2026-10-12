#!/usr/bin/env python3
"""Narrow independent controls of frozen inverse sources; synthetic data only."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import sys
sys.dont_write_bytecode = True
import datetime
import hashlib
import json
import math
from pathlib import Path
import resource
import time
import types

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad

HERE = Path(__file__).resolve().parent
RUNTIME = Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
OUT = RUNTIME/'gravity/response_inverse/independent_inverse_review'
MANIFEST = json.loads((OUT/'snapshot_manifest_v1.json').read_text())
SOURCES = {Path(r['original']).name:r for r in MANIFEST['sources']}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def guard():
    assert time.time() < json.loads((RUNTIME/'DEADLINE.json').read_text())['packaging_epoch']
    assert not any((RUNTIME/p).exists() for p in
                   ['STOP_REQUESTED.json', 'USER_STOP_REQUESTED', 'STOP_CAMPAIGN.json'])
    for row in SOURCES.values():
        assert sha(row['original']) == sha(row['snapshot']) == row['sha256']


def subject(name):
    """Execute pinned bytes with original path semantics; never run main."""
    row = SOURCES[name+'.py']
    module = types.ModuleType(name)
    module.__file__ = row['original']
    sys.modules[name] = module
    exec(compile(Path(row['snapshot']).read_text(), row['original'], 'exec'), module.__dict__)
    return module


def own_ramp(a, lo, hi):
    if a <= lo:
        return 1.
    if a >= hi:
        return 0.
    return (math.log(hi)-math.log(a))/(math.log(hi)-math.log(lo))


def solar_reference(lo, hi):
    # Independent 65-digit square-root difference; no rationalized author kernel.
    mp.mp.dps = 65
    low, high = mp.mpf(str(lo)), mp.mpf(str(hi))
    def integrand(u):
        s = mp.exp(u)
        plus = 4*s**4+2*s**3+3*s*s+2*s+4
        minus = 4*s**4-2*s**3+3*s*s-2*s+4
        return mp.mpf(8)/105*(minus*mp.sqrt(1+s)-plus*mp.sqrt(abs(1-s)))
    edges = [mp.log(low), mp.log(high)]
    if low < 1 < high:
        edges.insert(1, mp.mpf(0))
    return float(mp.mpf(9)/(8*mp.log(high/low))*mp.quad(integrand, edges))


def check_projection(op):
    scored = np.array([.2, .5, 1., 2., 5., 10.])
    r = np.unique(np.r_[np.geomspace(1e-5, 60., 1536), scored])
    x, w = leggauss(32)
    c, angular = (1+x)/2, w/2
    sine = np.sqrt(1-c*c)
    # A manufactured vector: A_r=r exp(-r) P_2(c), A_theta=0.
    radial = r[:, None]*np.exp(-r[:, None])*(3*c*c-1)/2
    g = dict(radius=r, cosine=c, angular_weights=angular, ur=radial*sine,
             uz=radial*c, mr=-scored*np.exp(-scored)/2, mz=np.zeros_like(scored),
             R=scored, lmax=np.array(4), nr=np.array(len(r)), nc=np.array(32))
    got = op.LinearProjection(g).project(1., 1.)
    # div A=(3-r)e^-r P_2. Differentiate the independent Green solution.
    expected = []
    for radius in scored:
        inner = quad(lambda t:t**4*(3-t)*math.exp(-t), 0., radius,
                     epsabs=1e-12, epsrel=2e-13)[0]
        outer = quad(lambda t:(3-t)*math.exp(-t)/t, radius, math.inf,
                     epsabs=1e-12, epsrel=2e-13)[0]
        expected.append(-.5*(3*radius**-4*inner-2*radius*outer)/5)
    expected = np.array(expected)
    error = float(np.max(np.abs(got-expected)/np.maximum(abs(expected), .001)))
    assert error < 2e-4, error
    zero_correction_error = float(np.max(abs(g['mr']-expected)))
    assert zero_correction_error > .05

    # Spherical source has exact P[b(|U|)U]=b(|U|)U for every radial b.
    # Force amplitude was specified independently in SI, then converted once.
    acc = 1e6/3.085677581491367e19
    assert abs(acc/op.field.ACC-1) < 1e-14
    norm = 1e-10/(1+r*r)/acc
    mid = 1e-10/(1+scored*scored)/acc
    g.update(ur=norm[:, None]*sine, uz=norm[:, None]*c, mr=mid)
    p = op.LinearProjection(g)
    indices = [8, 10, 11, 12]
    si_checks = []
    for j in indices:
        wanted = mid*np.array([own_ramp(1e-10/(1+rr*rr), op.KNOTS[j], op.KNOTS[j+1])
                               for rr in scored])
        actual = p.column(op.KNOTS[j], op.KNOTS[j+1])
        difference = float(np.max(abs(actual-wanted)/mid))
        assert difference < 1e-11
        si_checks.append({'basis':j, 'absolute_error_over_Newtonian':difference})
    weights = np.arange(1, 21)/73
    columns = np.stack([p.column(lo, hi) for lo, hi in zip(op.KNOTS[:-1], op.KNOTS[1:])], axis=1)
    additivity = float(np.max(abs(p.combined(weights)-(p.project(1., 1.)+columns@weights))/mid))
    assert additivity < 1e-11
    return {'non_gradient_max_scaled_error':error, 'zero_correction_mutation_error':zero_correction_error,
            'SI_basis_checks':si_checks, 'synthetic_superposition_error_over_Newtonian':additivity}


def check_rectangles(fit, op):
    # Exercise the author's actual row reader against tiny artificial NPZ files.
    # None of the campaign's velocity files is opened here.
    fake = OUT/'synthetic_row_reader_inputs'
    fake.mkdir(exist_ok=True)
    source, target = {}, {}
    for name in fit.NAMES:
        source[name+'_score_mask'] = np.array([True, True, False, True])
        source[name+'_R'] = np.array([1., 2., 0., 4.])
        target[name+'_v'] = np.array([3., 2., -99., 1.])
        target[name+'_error'] = np.array([0., 2., -1., .25])
        record = {'source_sha256':sha(op.__file__), 'protocol_sha256':op.PROTOCOL_HASH,
                  'solver_sha256':op.SOLVER_HASH, 'R_kpc':[1., 2., 4.],
                  'knots_SI':op.KNOTS.tolist(), 'g_N':[1., 1., 1.], 'K':np.zeros((3,20)).tolist()}
        (fake/f'operator_{name}_v1.json').write_text(json.dumps(record)+'\n')
    np.savez(fake/'baryonic_forward_64.npz', **source)
    np.savez(fake/'sealed_targets.npz', **target)
    (fake/'operator_controls_v1.json').write_text(json.dumps({'passed':True,'source_sha256':sha(op.__file__)})+'\n')
    original_out, original_data = op.OUT, op.field.DATA
    try:
        op.OUT = op.field.DATA = fake
        rows = fit.training_rows()
    finally:
        op.OUT, op.field.DATA = original_out, original_data
    for row in rows:
        np.testing.assert_array_equal(row['A'], [9., 2., .25])
        np.testing.assert_array_equal(row['low'], [9., 0., .0625])
        np.testing.assert_array_equal(row['high'], [9., 18., .5625])
    return {'synthetic_names':fit.NAMES, 'A':[9.,2.,.25], 'L':[9.,0.,.0625],
            'H':[9.,18.,.5625], 'zero_error_retained':True, 'lower_velocity_clipped_before_square':True}


def fixture(A, g, first_column):
    A = np.array(A, dtype=float)
    k = np.zeros((len(A),20))
    k[:,0] = first_column
    return [{'A':A, 'low':A.copy(), 'high':A.copy(), 'g_N':np.array(g,dtype=float), 'K':k}]


def check_lp_and_d(fit, op):
    controls = []
    for label, rows, expected_t, expected_weight in [
        ('one_exact_force',fixture([3],[1],[1]),0.,2.-3e-8),
        ('conflicting_fractional_forces',fixture([2,4],[1,1],[1,1]),1/3,5/3-4e-8),
        ('signed_negative_column',fixture([1],[2],[-1]),0.,1.-1e-8)]:
        result = fit.solve(rows, False)
        assert result['status'] == 0
        assert abs(result['primary_minimum_t']-expected_t) < 2e-10
        assert abs(result['weights'][0]-expected_weight) < 2e-9
        assert max(abs(x) for x in result['weights'][1:]) < 1e-12
        controls.append({'label':label, 'expected_primary_t':expected_t,
                         'expected_lexicographic_weight':expected_weight, 'actual':result})

    # Exact one-sided derivative of A*N at every interval's upper edge.
    empty_rows = fixture([1],[1],[0])
    matrix, bound, _ = fit.constraints(empty_rows, differential=True)
    d = np.log(op.KNOTS[1:]/op.KNOTS[:-1])
    weights = np.linspace(.01, 1.3, 20)
    own_min_derivative = np.array([1+sum(weights[j+1:])-weights[j]/d[j] for j in range(20)])
    author_slacks = bound[-20:] - matrix[-20:,:20]@weights
    np.testing.assert_allclose(author_slacks, own_min_derivative, rtol=2e-14, atol=2e-14)
    threshold = d[-1]
    acceptance = []
    for multiple in [.999, 1., 1.001]:
        w = np.zeros(20);w[-1]=multiple*threshold
        slacks = bound[-20:]-matrix[-20:,:20]@w
        acceptance.append({'threshold_multiple':multiple, 'min_D_slack':float(min(slacks)),
                           'own_min_derivative':1-multiple})
    assert acceptance[0]['min_D_slack'] > 0 and acceptance[2]['min_D_slack'] < 0
    return {'analytic_LP_cases':controls, 'D_max_absolute_slack_difference':float(max(abs(author_slacks-own_min_derivative))),
            'D_boundary_controls':acceptance}


def check_external(fit, op):
    rows = fixture([2,4],[1,1],[1,1])
    weights = np.linspace(.01, .07, 20)
    results = []
    for external in [float(fit.EXTERNAL[0]/101), 3.73e-11, float(fit.EXTERNAL[1])]:
        guard()
        matrix, bound, q = fit.constraints(rows, False, external, True)
        eigene = external*(1+sum(w*own_ramp(external,lo,hi)
                     for w,lo,hi in zip(weights, op.KNOTS[:-1], op.KNOTS[1:])))
        value = np.r_[weights, .123]
        actual_external_slacks = bound[-3:-1]-matrix[-3:-1]@value
        expected_external_slacks = np.array([(fit.EXTERNAL[1]-eigene)/external,
                                             (eigene-fit.EXTERNAL[0])/external])
        np.testing.assert_allclose(actual_external_slacks, expected_external_slacks, rtol=2e-13, atol=2e-13)
        qs = []
        for lo,hi in zip(op.KNOTS[:-1], op.KNOTS[1:]):
            qs.append(external**1.5/math.sqrt(1.32712440018e20)*solar_reference(lo/external,hi/external))
        qs = np.array(qs)
        rel = float(np.max(abs(q-qs)/qs))
        assert rel < 2e-10, rel
        assert abs((bound[-1]-matrix[-1]@value) - (1-qs@weights/5.2e-27)) < 2e-10
        results.append({'E_SI':external, 'own_physical_external_SI':eigene,
                        'max_solar_column_relative_to_65_digit_reference':rel,
                        'smallest_q_s_minus2':float(min(qs)), 'largest_q_s_minus2':float(max(qs)),
                        'external_rows_max_absolute_difference':float(max(abs(actual_external_slacks-expected_external_slacks)))})
    return results


def check_search(fit):
    grid = np.geomspace(fit.EXTERNAL[0]/101, fit.EXTERNAL[1], 129)
    selected = [16,64,112]
    step = math.log(grid[1]/grid[0])
    original_solve = fit.solve
    def fake(rows, differential, external, solar_limit):
        if external in [float(grid[0]), float(grid[-1])]:
            return {'status':2,'external_newtonian_SI':external}
        score = min((math.log(external/grid[j])/step)**2 for j in selected)
        return {'status':0, 'primary_minimum_t':score, 'total_weight':0., 'external_newtonian_SI':external}
    try:
        fit.solve = fake
        scan = fit.external_scan([],False,False)
        expected_nodes = set(map(float,grid))
        for j in selected:
            for a,b in [(j-1,j),(j,j+1)]:
                for fraction in np.arange(1,16)/16:
                    expected_nodes.add(float(math.exp((1-fraction)*math.log(grid[a])+fraction*math.log(grid[b]))))
        actual_nodes = np.array([r['external_newtonian_SI'] for r in scan['samples']])
        desired_nodes = np.array(sorted(expected_nodes))
        assert len(actual_nodes) == len(desired_nodes) == 219
        assert max(abs(actual_nodes/desired_nodes-1)) < 1e-14
        assert sum(r['status'] != 0 for r in scan['samples']) == 2
        assert scan['best_sampled'] == min((r for r in scan['samples'] if r['status']==0), key=fit.rank)
        fit.solve = lambda rows,differential,external,solar_limit:{'status':2,'external_newtonian_SI':external}
        failed = fit.external_scan([],True,True)
        assert failed['best_sampled'] is None and failed['evaluated_nodes'] == 129
    finally:
        fit.solve = original_solve
    return {'synthetic_successful_scan_nodes':len(actual_nodes), 'retained_infeasible_nodes':2,
            'all_infeasible_scan_nodes':129, 'best_is_sampled_lexicographic_minimum':True,
            'log_node_reference_max_relative_difference':float(max(abs(actual_nodes/desired_nodes-1))),
            'continuous_optimality_claimed':scan['continuous_external_optimality_claimed']}


def main():
    guard()
    started = time.time()
    op = subject('direct_galaxy_response_operator')
    subject('direct_response_basis')
    fit = subject('direct_shared_response_fit')
    result = {'projection':check_projection(op), 'rectangles':check_rectangles(fit,op),
              'LP_and_D':check_lp_and_d(fit,op), 'external_and_solar':check_external(fit,op),
              'sampled_search':check_search(fit)}
    guard()
    result.update(at=datetime.datetime.now(datetime.timezone.utc).isoformat(), passed=True,
                  script_sha256=sha(__file__), snapshot_manifest_sha256=sha(OUT/'snapshot_manifest_v1.json'),
                  reviewed_sources={name:r['sha256'] for name,r in SOURCES.items()},
                  elapsed_seconds=time.time()-started, max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  empirical_inputs_read=False, heavy_field_or_empirical_fit_run=False)
    with (OUT/'synthetic_checks_v1.json').open('x') as stream:
        json.dump(result,stream,indent=2);stream.write('\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
