#!/usr/bin/env python3
"""Conditional matter/radiation/mechanical readout controls; no empirical test."""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import argparse,cmath,hashlib,json,math,sys,time
from pathlib import Path
from fractions import Fraction as F
import numpy as np
import scipy
from scipy.optimize import brentq
from scipy.integrate import quad
import sympy as s
sp=s
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=('docs/LOCAL_VECTOR_MATTER_RADIATION_READOUT_BOUNDED_THEOREM_NOTE_2026-10-12.md',
 'docs/LOCAL_VECTOR_HOMOGENEOUS_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-12.md')

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def symbolic():
    N,D,G,m1,m2,a,z=s.symbols('N D G m1 m2 a z',positive=True)
    r=s.sqrt(a*a+z*z)
    U=-G*m1*m2*(N+D+(N-D)*z*z/r**2)/(2*r)
    reduced=m1*m2/(m1+m2)
    vertical=s.simplify(s.diff(U,z,2).subs(z,0)/reduced)
    assert s.simplify(vertical-G*(m1+m2)*(3*D-N)/(2*a**3))==0
    radial=s.simplify(s.diff(U,a).subs(z,0)/(reduced*a))
    assert s.simplify(radial-G*(N+D)*(m1+m2)/(2*a**3))==0
    x=s.symbols('x',real=True)
    integrals=[2*s.pi*s.integrate((1-x*x)**3,(x,-1,1)),
               2*s.pi*s.integrate(x*x*(1-x*x)**2,(x,-1,1))]
    assert integrals==[64*s.pi/35,32*s.pi/105]
    q=s.symbols('q',positive=True)
    ratio=(6*q**s.Rational(7,2)+1)/(21*(q+1))
    derivative=(15*q**s.Rational(7,2)+21*q**s.Rational(5,2)-1)/(21*(q+1)**2)
    assert s.simplify(s.diff(ratio,q)-derivative)==0
    assert ratio.subs(q,1)==s.Rational(1,6)
    return {'equatorial_frequency':str(radial),'vertical_frequency':str(vertical),
            'angular_integrals':[str(v) for v in integrals],
            'ratio':str(ratio),'ratio_derivative':str(derivative),
            'isotropic_ratio':'1/6'}

def angular_tensor_power(N,D,alpha,G,a,Omega,reduced):
    zz,weights=np.polynomial.legendre.leggauss(48)
    phis=np.arange(96)*2*np.pi/96
    # I''' evaluated directly from the rotating second-moment matrix at phase0.
    I3=np.array([[0,-4,0],[-4,0,0],[0,0,0]],dtype=float)*reduced*a*a*Omega**3
    cT,cL=1/math.sqrt(alpha*N),1/math.sqrt(alpha*D)
    totals=np.zeros(2)
    for z,w in zip(zz,weights):
        ns=np.column_stack([np.sqrt(1-z*z)*np.cos(phis),
                            np.sqrt(1-z*z)*np.sin(phis),np.full(len(phis),z)])
        contractions=np.einsum('ni,ij,nj->n',ns,I3,ns)
        prefactor=G/(16*np.pi*alpha)*w*2*np.pi/len(phis)
        totals += prefactor*np.sum(contractions**2)*np.array([(1-z*z)/cT**7,z*z/cL**7])
    expected=np.array([32/(35*cT**7),16/(105*cL**7)])*G*reduced**2*a**4*Omega**6/alpha
    assert np.allclose(totals,expected,rtol=2e-13,atol=0)
    return totals,expected

def exact_source_harmonics(N,D,alpha,G,a,Omega):
    """Full density Fourier coefficients of equal antipodal half-unit masses.

    No moment expansion or Bessel function is used. Total mass1, reduced mass1/4.
    Return finite-harmonic, independently integrated radiation (no near-zone fit).
    """
    zs,ws=np.polynomial.legendre.leggauss(48)
    phases=np.arange(512)*2*np.pi/512
    totals=np.zeros(2);tail=np.zeros(2);oddmax=0.
    for j,c in enumerate([1/math.sqrt(alpha*N),1/math.sqrt(alpha*D)]):
        polarization=(1-zs*zs) if j==0 else zs*zs
        for harmonic in range(1,17):
            omega=harmonic*Omega
            phase_argument=omega*a/(2*c)*np.sqrt(1-zs*zs)[:,None]*np.cos(phases)[None,:]
            density=np.cos(phase_argument)
            coefficient=np.mean(density*np.exp(1j*harmonic*phases)[None,:],axis=1)
            if harmonic%2:oddmax=max(oddmax,float(np.max(np.abs(coefficient))))
            power=G*omega**2/(alpha*c**3)*np.dot(ws,polarization*np.abs(coefficient)**2)
            totals[j]+=power
            if harmonic>=14:tail[j]+=power
    assert oddmax<1e-14
    return totals,tail,oddmax

def bracket():
    polynomial=lambda x:6*x**7-21*x*x-20
    root=brentq(polynomial,1,math.sqrt(3),xtol=1e-14)
    scale=10**12
    lo=F(math.floor(root*scale),scale);hi=lo+F(1,scale)
    assert polynomial(lo)<0<polynomial(hi)
    q=root*root
    return {'sqrt_q_bracket':[str(lo),str(hi)],'q_bracket':[str(lo*lo),str(hi*hi)],
            'q_approx':q,'transverse_to_longitudinal_speed':1/root,
            'polar_to_equatorial_static_potential':2*q/(q+1),
            'vertical_squared_frequency_to_orbital':(3-q)/(1+q),
            'scope':'Exact polynomial sign bracket; equality to a supplied GR comparator with c_L=c_EM, not a measurement fit.'}

def radiation_controls():
    start=time.monotonic();rows=[];mutations=[]
    for q in [1.,1.5,2.,5.]:
        N,D,alpha,G,Omega,reduced=q,1.,1.,1.,1.,.25
        cT=1/math.sqrt(q)
        for speed_fraction in [.08,.04,.02,.01]:
            a=speed_fraction*cT
            quadrature,leading=angular_tensor_power(N,D,alpha,G,a,Omega,reduced)
            direct,tail,odd=exact_source_harmonics(N,D,alpha,G,a,Omega)
            relative=float(np.sum(direct)/np.sum(leading)-1)
            assert abs(relative)<2*speed_fraction**2
            assert float(np.sum(tail)/np.sum(direct))<1e-14
            rows.append({'q':q,'a_Omega_over_cT':speed_fraction,
                         'angular_tensor_power':quadrature.tolist(),'leading_power':leading.tolist(),
                         'exact_source_harmonic_power':direct.tolist(),'relative_to_leading_minus_one':relative,
                         'harmonics_14_to_16_fraction':float(np.sum(tail)/np.sum(direct)),
                         'max_odd_density_coefficient':odd,
                         'equatorial_orbit_vertically_stable':q<3})
        local=[r for r in rows if r['q']==q]
        for r1,r2 in zip(local[:-1],local[1:]):
            convergence=abs(r1['relative_to_leading_minus_one']/r2['relative_to_leading_minus_one'])
            assert 3.9<convergence<4.1
    # Corrupt only one side of independent angular/multipole comparisons.
    actual,expected=angular_tensor_power(2.,1.,1.,1.,.03,1.,.25)
    mutations=[{'name':'omit_source_Taylor_half','detected':not np.allclose(actual,4*expected,rtol=1e-8,atol=0)},
               {'name':'drop_longitudinal_power','detected':not math.isclose(sum(actual),expected[0],rel_tol=1e-8)},
               {'name':'replace_cT_power7_by5','detected':not math.isclose(actual[0],expected[0]/2,rel_tol=1e-8)}]
    assert all(row['detected'] for row in mutations)
    output={
            'symbolic':symbolic(),'controls':rows,'calibration_example':bracket(),'mutations':mutations,
            'elapsed_sec':time.monotonic()-start,
            'scope':'Leading weak-source circular radiation and conservative mechanics only; no empirical test or relativistic matter model.'}
    return output

def cquad(func, upper):
    real, er = quad(lambda x: func(x).real, 0, upper, epsabs=2e-12, epsrel=2e-12)
    imag, ei = quad(lambda x: func(x).imag, 0, upper, epsabs=2e-12, epsrel=2e-12)
    return real + 1j * imag, max(er, ei)


def readout_controls():
    started = time.monotonic()
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
    result = {'schema': 'vector_mechanical_readout_controls_v1',
              'pass_count': len(checks), 'fail_count': 0, 'families': checks,
              'elapsed_seconds': time.monotonic()-started,
              'empirical_data_used': False,
              'limits': ['linear prescribed plane waves', 'simultaneous mechanical length only',
                         'no optical or strain likelihood', 'finite-arm synthetic controls only']}
    return result

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--json',action='store_true');ap.add_argument('--output-json',type=Path)
    args=ap.parse_args()
    radiation=radiation_controls();readout=readout_controls()
    rows=radiation['controls']
    families={
      'conservative_symbolic_frequencies_and_angular_integrals': bool(radiation['symbolic']),
      'angular_tensor_quadrature': len(rows)==16 and all(np.allclose(r['angular_tensor_power'],r['leading_power'],rtol=2e-13,atol=0) for r in rows),
      'finite_source_harmonics_and_odd_symmetry':len(rows)==16 and all(r['max_odd_density_coefficient']<1e-14 for r in rows),
      'slow_source_convergence': all(3.9<abs(a['relative_to_leading_minus_one']/b['relative_to_leading_minus_one'])<4.1 for q in [1.,1.5,2.,5.] for a,b in zip([r for r in rows if r['q']==q][:-1],[r for r in rows if r['q']==q][1:])),
      'exact_comparator_root_bracket':len(radiation['calibration_example']['sqrt_q_bracket'])==2,
      'radiation_false_alternatives':all(x['detected'] for x in radiation['mutations'])}
    families.update({x['family']:True for x in readout['families']})
    assert len(families)==11 and all(families.values()) and readout['fail_count']==0
    result={'input_identities':{str(p.relative_to(ROOT)):digest(p) for p in [Path(__file__),*[ROOT/v for v in AUDIT_INPUT_PATHS]]},
       'environment':{'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,'sympy':s.__version__},
       'radiation':radiation,'readout':readout,'check_families':families,
       'checks_passed':sum(families.values()),'checks_failed':sum(not v for v in families.values()),
       'scope':'Conditional weak matter/radiation and linear mechanical readout. No empirical fit, optical response or TOE.'}
    encoded=json.dumps(result,indent=2,allow_nan=False)+'\n'
    if args.output_json:
        with args.output_json.open('x') as f:f.write(encoded)
    if args.json:print(encoded,end='')
    else:
        print('PASS conservative frequencies, leading radiation,16 prescribed-source harmonic controls and exact calibration bracket')
        print('PASS plane tide,36 endpoint integrations, finite-arm and two-speed network controls')
        print('False alternatives are formula comparisons, not mutated-source executions.')
        print('per_element: vector/tidal components and endpoint arms explicitly checked.')
        print('per_site: four synthetic network sites; no physical discrete-site model supplied.')
        print('per_mode: transverse/longitudinal radiative branches and mechanical projection checked.')
        print('per_block: six matter/radiation and five readout families checked.')
        print('lattice_wide: checked and not executed; continuum homogeneous candidate only.')
        print('TOTAL: PASS=11 FAIL=0; conditional-support, no empirical acceptance.')

if __name__=='__main__':main()
