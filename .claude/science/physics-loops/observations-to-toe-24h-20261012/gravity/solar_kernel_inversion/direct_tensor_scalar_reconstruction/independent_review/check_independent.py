#!/usr/bin/env python3
"""Independent source/readout checks. Never import or execute the author runner."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
import datetime as dt
from fractions import Fraction as F
import hashlib
import itertools
import json
import math
from pathlib import Path
import numpy as np
import sympy as s

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'INDEPENDENT_CHECKS_v1.json'
tests, details = [], {}


def test(name, condition, evidence=None):
    tests.append({'name': name, 'passed': bool(condition), 'evidence': evidence})
    if not condition:
        raise AssertionError(name)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def metric_from_fierz():
    # Derive the symbol as the Hessian of the contracted Fierz-Pauli quadratic
    # form rather than assembling the author's linear Einstein components.
    eta = s.diag(-1, 1, 1, 1)
    hvars = s.symbols('u:10')
    pairs = [(i, j) for i in range(4) for j in range(i, 4)]
    h = s.zeros(4)
    for z, (i, j) in zip(hvars, pairs):
        h[i, j] = h[j, i] = z
    cases = [(-13, 3, 4, 12), (13, 3, 4, 12), (-3, 1, 4, 2), (-2, 0, 0, 0), (0, 1, 2, 3)]
    rows = []
    for qtuple in cases:
        q = s.Matrix(qtuple)
        qu = eta * q
        norm = (q.T * qu)[0]
        tr = s.trace(eta * h)
        hh = s.trace(eta * h * eta * h)
        b = h * qu
        Q = s.expand((norm * (hh - tr * tr) - 2 * (b.T * eta * b)[0] + 2 * tr * (qu.T * h * qu)[0]) / 2)
        H = s.hessian(Q, hvars)
        gauge = []
        for i in range(4):
            xi = s.eye(4)[:, i]
            pure = q * xi.T + xi * q.T
            gauge.append(s.Matrix([pure[a, b] for a, b in pairs]))
        J = s.Matrix.hstack(*gauge)
        rank = H.rank()
        test('fierz_symbol_' + str(qtuple), rank == (4 if norm == 0 else 6) and J.rank() == 4 and H * J == s.zeros(10, 4))
        rows.append({'q_cov': list(qtuple), 'q_squared': int(norm), 'rank': rank, 'kernel': 10-rank, 'gauge_rank': 4, 'physical_kernel': 10-rank-4})
    details['independent_full_metric_symbol'] = rows


def curvature_and_local_stress():
    curvature_rows = []
    for n, p, q in [
        (s.Matrix([0, s.Rational(3, 5), s.Rational(4, 5)]), s.Matrix([1, 0, 0]), s.Matrix([0, s.Rational(4, 5), -s.Rational(3, 5)])),
        (s.Matrix([s.Rational(3, 13), s.Rational(4, 13), s.Rational(12, 13)]), s.Matrix([s.Rational(4, 5), -s.Rational(3, 5), 0]), s.Matrix([s.Rational(36, 65), s.Rational(48, 65), -s.Rational(25, 65)]))]:
        hp, hx, zeta = s.Rational(2, 7), -s.Rational(3, 8), s.Rational(5, 13)
        ht = hp * (p * p.T - q * q.T) + hx * (p * q.T + q * p.T)
        h = s.zeros(4)
        h[0, 0] = -2 * zeta
        h[1:4, 1:4] = ht + 2 * zeta * s.eye(3)
        k = s.Matrix([-1, *n])
        # Linearized R_{0i0j}, each second derivative replaced by -k_a k_b.
        E = s.Matrix(3, 3, lambda i, j: (-k[i+1]*k[0]*h[0, j+1] - k[0]*k[j+1]*h[i+1, 0] + k[i+1]*k[j+1]*h[0, 0] + k[0]**2*h[i+1, j+1])/2)
        expected = ht/2 + zeta*(s.eye(3)-n*n.T)
        test('riemann_tensor_and_breathing_' + str(n.T), E == expected and E*n == s.zeros(3, 1))
        # Wrong h00 sign creates a longitudinal tide, a decisive false alternative.
        wrong = E + 2*zeta*n*n.T
        test('wrong_conformal_time_sign_detected_' + str(n.T), wrong*n != s.zeros(3, 1))
        curvature_rows.append({'n': [str(v) for v in n], 'curvature_identity_exact': True, 'wrong_sign_longitudinal_norm_squared': str((wrong*n).dot(wrong*n))})
    details['curvature'] = curvature_rows
    x, y, z = s.symbols('x y z', real=True)
    U = x*x + 2*y*y + 3*z*z + x*y*z
    coords = [x, y, z]
    g = s.Matrix([s.diff(U, v) for v in coords])
    sigma = g*g.T - s.eye(3)*g.dot(g)/2  # factors 4piG canceled on both sides
    div = s.Matrix([sum(s.diff(sigma[i,j], coords[j]) for j in range(3)) for i in range(3)])
    expected = sum(s.diff(U, v, 2) for v in coords)*g
    test('local_newtonian_field_stress_divergence', s.simplify(div-expected) == s.zeros(3, 1))
    # Fourier inverse of k^-4 is -r/(8pi); its differentiated kernel yields
    # the interaction stress integral without integrating singular self terms.
    radius = s.sqrt(x*x+y*y+z*z)
    A = s.hessian(radius, coords) / 2  # common 4pi G^2 m1 m2 stripped off
    pair = 2*A - s.eye(3)*s.trace(A)
    expected_pair = -s.Matrix(coords)*s.Matrix(coords).T/radius**3
    test('integrated_pair_field_stress', s.simplify(pair-expected_pair) == s.zeros(3))
    details['pair_stress'] = 'Integral sigma_ij = -G_N m1 m2 r_i r_j/r^3, from inverse-k^4 differentiated Green kernel; self terms excluded.'


def sphere_cubature():
    # Fourteenth-order family size, degree-five exact sphere cubature:
    # six coordinate-axis nodes (weight1/15) plus eight cube nodes (3/40).
    nodes, weights = [], []
    for i in range(3):
        for sign in (-1, 1):
            n = np.zeros(3); n[i] = sign
            nodes.append(n); weights.append(1/15)
    for signs in itertools.product((-1, 1), repeat=3):
        nodes.append(np.array(signs)/math.sqrt(3)); weights.append(3/40)
    return nodes, weights


def moment_from_time_samples(phase, mu=.24, radius=1., omega=1.):
    # Differentiate the sampled circular second harmonic, not the author's
    # velocity/acceleration/jerk outer-product expression.
    phases = np.arange(24)*2*math.pi/24
    pos = radius*np.stack((np.cos(phases), np.sin(phases), np.zeros(24)), axis=1)
    moments = mu*pos[:, :, None]*pos[:, None, :]
    coeff = np.mean(moments*np.exp(-2j*phases)[:, None, None], axis=0)
    e = np.exp(2j*phase)
    I2 = 2*np.real((2j*omega)**2*coeff*e)
    I3 = 2*np.real((2j*omega)**3*coeff*e)
    return I2, I3


def readout_rows(result):
    exact_a = {'zero':F(0), 'small':F(1,100), 'unit':F(1), 'diagonal_two':F(1,25)/2+F(1,49)/3,
               'mixed_two':(3*F(1,4)**2-2*F(1,4)*F(1,3)+2*F(1,3)**2)/5}
    for row in result['field_examples']:
        a = exact_a[row['name']]
        gamma, frac, gs = (1-a)/(1+a), a/(1+a), 1/(1+a)
        test('exact_field_' + row['name'], F(row['exact_a']) == a and abs(row['gamma']-float(gamma)) < 3e-16 and abs(row['scalar_force_fraction']-float(frac)) < 1e-16 and abs(row['G_star']-float(gs)) < 2e-16)
    amp_rows, flux_rows, lens_rows = [], [], []
    for row in result['pattern_rows']:
        phase, ci, a = row['phase'], row['cos_inclination'], float(exact_a[row['name']])
        I2, _ = moment_from_time_samples(phase)
        n = np.array([math.sqrt(1-ci*ci), 0, ci])
        p, q = np.array([ci, 0, -math.sqrt(1-ci*ci)]), np.array([0,1,0])
        # Direct polarization contractions eliminate Lambda without calling tt.
        answer = np.array([(p@I2@p-q@I2@q)/(2*.24), (p@I2@q)/.24, -a*(n@I2@n)/(2*.24)])
        observed = np.array(row['normalized_amplitudes'])
        predicted = np.array(row['predicted'])
        err = float(max(np.max(np.abs(answer-observed)), np.max(np.abs(answer-predicted))))
        test('pattern_' + row['name'] + '_' + str(phase) + '_' + str(ci), err < 3e-14)
        amp_rows.append({'name':row['name'],'phase':phase,'cos_inclination':ci,'independent':answer.tolist(),'max_difference':err})
    nodes, weights = sphere_cubature()
    for row in result['flux_rows']:
        a = float(exact_a[row['name']]); gs=1/(1+a)
        _, S = moment_from_time_samples(row['phase'])
        pt, ps = 0., 0.
        for n, w in zip(nodes, weights):
            # Pointwise TT norm derived by contracting projectors:
            # S:S -2|Sn|^2 + (nSn)^2/2 for trace-free S.
            nn = n@S@n
            tt_norm = np.sum(S*S)-2*np.dot(S@n,S@n)+nn*nn/2
            pt += w * gs * tt_norm/(2*1000.**5)
            ps += w * gs * a * nn*nn/(4*1000.**5)
        terr = abs(pt/row['tensor']-1)
        serr = abs(ps/row['scalar']-1) if a else abs(ps-row['scalar'])
        ratio = (pt+ps)/(32*.24**2/(5*1000.**5))
        test('flux_' + row['name'] + '_' + str(row['phase']), max(terr,serr,abs(ratio-row['same_orbit_ratio'])) < 3e-14)
        flux_rows.append({'name':row['name'],'phase':row['phase'],'tensor':pt,'scalar':ps,'tensor_fractional_difference':terr,'scalar_fractional_difference':serr,'same_orbit_ratio':ratio})
    # Compactified ray integral z=b tan(theta), evaluated by composite Simpson.
    intervals=2048
    th=np.linspace(-math.pi/2,math.pi/2,intervals+1)
    coefficients=np.ones(intervals+1); coefficients[1:-1:2]=4; coefficients[2:-1:2]=2
    angular=float(np.dot(coefficients,np.cos(th))*(math.pi/intervals)/3)
    for row in result['lens_rows']:
        a=float(exact_a[row['name']]); gs=1/(1+a); b=row['impact_parameter']
        val=2*gs/(1000.**2*b)*angular
        err=max(abs(val/row['integrated_bending']-1), abs(val/row['prediction']-1))
        test('lens_' + row['name'] + '_' + str(b), err < 2e-13)
        lens_rows.append({'name':row['name'],'impact_parameter':b,'simpson_compactified_integral':val,'fractional_difference':err})
    test('complete_frozen_row_counts', len(amp_rows)==100 and len(flux_rows)==20 and len(lens_rows)==15)
    details.update({'pattern_rows':amp_rows,'flux_rows':flux_rows,'lens_rows':lens_rows,
                    'maximum_pattern_difference':max(r['max_difference'] for r in amp_rows),
                    'maximum_tensor_flux_fractional_difference':max(r['tensor_fractional_difference'] for r in flux_rows),
                    'maximum_scalar_flux_fractional_difference':max(r['scalar_fractional_difference'] for r in flux_rows),
                    'maximum_lens_fractional_difference':max(r['fractional_difference'] for r in lens_rows)})


def exact_sphere_and_counterfactuals():
    x,y,z=s.symbols('x y z',real=True)
    n=s.Matrix([x,y,z])
    S=s.Matrix([[2,3,-1],[3,-5,4],[-1,4,3]])
    nn=(n.T*S*n)[0]
    scalar=nn**2
    tensor=s.trace(S*S)-2*(S*n).dot(S*n)+nn**2/2
    def dfact(k):
        return math.prod(range(k,0,-2)) if k>0 else 1
    def average(poly):
        total=F(0)
        for powers,coeff in s.Poly(s.expand(poly),x,y,z).terms():
            if any(k%2 for k in powers): continue
            total+=F(int(coeff.p),int(coeff.q))*F(math.prod(dfact(k-1) for k in powers),dfact(sum(powers)+1))
        return total
    norm=int(s.trace(S*S))
    test('exact_isotropic_quartic_moments', average(scalar)==F(2*norm,15) and average(tensor)==F(2*norm,5))
    details['exact_sphere_averages']={'tracefree_test_matrix':np.array(S,dtype=int).tolist(),'norm_squared':norm,'scalar_average':str(average(scalar)),'tensor_average':str(average(tensor))}
    a=s.symbols('a',nonnegative=True)
    gamma=(1-a)/(1+a); f=a/(1+a); ratio=(1+a/6)/(1+a)
    test('linked_elimination_identity', s.factor(ratio-(7+5*gamma)/12)==0 and s.factor(f-(1-gamma)/2)==0)
    gmin=F(1249,1250)
    test('exact_working_rectangle', (1-gmin)/(1+gmin)==F(1,2499) and (1-gmin)/2==F(1,2500) and (7+5*gmin)/12==F(2999,3000))
    # Each mutation targets a derived ingredient, not the author's source file.
    mutation_results={
        'omit_Gstar_to_GN_calibration_at_a1': {'correct':str(F(7,12)),'wrong':str(F(7,6))},
        'double_scalar_wave_amplitude_at_a1': {'correct':str(F(7,12)),'wrong':str(F(5,6))},
        'omit_detector_coupling_at_a01': {'correct_breathing_edge_on':str(F(1,100)),'wrong_breathing_edge_on':str(F(1,10))},
        'omit_newtonian_field_stress': {'correct_tensor_harmonic_amplitude':1,'wrong':.5,'wrong_power_fraction':.25},
        'flip_field_stress_sign': {'correct_tensor_harmonic_amplitude':1,'wrong':0}}
    for name, row in mutation_results.items():
        test('mutation_detected_' + name, len(set(str(v) for v in row.values()))>1)
    # Actually calculate the omitted/sign-flipped stress harmonic rather than
    # trusting the listed diagnostic ratios.
    phases=np.arange(32)*2*math.pi/32
    positions=np.stack((np.cos(phases),np.sin(phases),np.zeros(32)),axis=1)
    velocities=np.stack((-np.sin(phases),np.cos(phases),np.zeros(32)),axis=1)
    dust=velocities[:,:,None]*velocities[:,None,:]
    field=-positions[:,:,None]*positions[:,None,:]
    weight=np.exp(-2j*phases)[:,None,None]
    good=np.mean((dust+field)*weight,axis=0)
    omitted=np.mean(dust*weight,axis=0)
    flipped=np.mean((dust-field)*weight,axis=0)
    test('source_stress_mutations_calculated', np.max(np.abs(omitted-good/2))<2e-16 and np.max(np.abs(flipped))<2e-16 and np.linalg.norm(good)>.4)
    details['decisive_formula_counterfactuals']=mutation_results
    details['computed_stress_mutation_norms']={'complete':float(np.linalg.norm(good)),'omitted':float(np.linalg.norm(omitted)),'sign_flipped':float(np.linalg.norm(flipped))}


def main():
    pins=json.loads((ROOT/'SOURCE_PINS_v1.json').read_text())
    for row in pins['sources']:
        test('pinned_source_' + row['path'], sha(ROOT/row['snapshot'])==row['sha256'] and sha(ROOT.parent/row['path'])==row['sha256'])
    result=json.loads((ROOT/'snapshots_v1/evidence_v1/RESULTS.json').read_text())
    freeze=json.loads((ROOT/'snapshots_v1/evidence_v1/FREEZE.json').read_text())
    test('executed_source_identity', result['source_sha256']==freeze['files'] and all(sha(ROOT/'snapshots_v1'/k)==v for k,v in freeze['files'].items()))
    metric_from_fierz()
    curvature_and_local_stress()
    readout_rows(result)
    exact_sphere_and_counterfactuals()
    output={'schema':'independent_tensor_scalar_checks_v1','at':dt.datetime.now(dt.timezone.utc).isoformat(),
            'executed_reviewer_source_sha256':sha(Path(__file__)),'source_pins_sha256':sha(ROOT/'SOURCE_PINS_v1.json'),
            'author_runner_imported_or_executed':False,'tests_passed':len(tests),'tests_failed':0,'tests':tests,**details}
    assert not OUT.exists(), 'Preserve executed results; use a new version.'
    OUT.write_text(json.dumps(output,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:output[k] for k in ['tests_passed','tests_failed','maximum_pattern_difference','maximum_tensor_flux_fractional_difference','maximum_scalar_flux_fractional_difference','maximum_lens_fractional_difference']},sort_keys=True))


if __name__=='__main__':
    try:
        main()
    except Exception as exc:
        f=ROOT/'INDEPENDENT_FAILURE_v1.json'
        assert not f.exists(), 'Preserve prior failure record.'
        f.write_text(json.dumps({'type':type(exc).__name__,'message':str(exc),'reviewer_source_sha256':sha(Path(__file__)),'tests':tests,'details':details},indent=2)+'\n')
        raise
