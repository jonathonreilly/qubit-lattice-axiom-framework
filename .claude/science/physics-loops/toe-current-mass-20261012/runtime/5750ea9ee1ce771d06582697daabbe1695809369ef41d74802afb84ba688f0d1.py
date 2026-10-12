"""Separate finite Pauli/kernel, differential, quadrature and parity checks."""
import argparse
import importlib.util
import json
import math
from pathlib import Path
import sys

import numpy as np
import mpmath as mp
from numpy.polynomial.hermite import hermgauss
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq
import sympy as sy

ap = argparse.ArgumentParser()
ap.add_argument('candidate')
args = ap.parse_args()
spec = importlib.util.spec_from_file_location('candidate_under_test', args.candidate)
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
rows = []
raw = {}


def clean(x):
    if isinstance(x, np.ndarray):
        return clean(x.tolist())
    if isinstance(x, (np.floating, np.integer)):
        return x.item()
    if isinstance(x, complex):
        return {'real': x.real, 'imag': x.imag}
    if isinstance(x, dict):
        return {str(k): clean(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [clean(v) for v in x]
    return x


def record(name, observed, expected, tolerance, method, details=None):
    err = abs(float(observed)-float(expected))
    rows.append(dict(name=name, observed=float(observed), expected=float(expected),
                     abs_error=err, tolerance=tolerance, accepted=bool(err <= tolerance),
                     method=method, details=clean(details)))


def bound(name, observed, upper, slack, method, details=None):
    rows.append(dict(name=name, observed=float(observed), upper=float(upper),
                     slack=slack, accepted=bool(observed <= upper+slack),
                     method=method, details=clean(details)))


def kernel_energy(q, m, v, a):
    sigma = math.hypot(m/2, v/a)
    g, j = sigma/2+m/4, sigma/2-m/4
    z = g-j*np.exp(-1j*a*q)
    k = np.array([[0, 2j*z], [-2j*z.conjugate(), 0]], dtype=complex)
    return float(np.linalg.eigvalsh(k)[1])


def reference_mass(q, m, v, a):
    es = np.array([kernel_energy(x, m, v, a) for x in q])
    # This symbol is also checked against literal spin matrices below.
    ps = np.sin(a*np.asarray(q))/a
    return float(es.sum()**2-v*v*ps.sum()**2)


def reference_window_excess(q, m, v, a):
    """70-digit determinant of the original 2x2 kernel; no M5 simplification.

    The original float64 eigensolver/root remains in the raw output. This
    resolves cancellation in E^2-v^2*p^2-m^2, not an interval certificate.
    """
    with mp.workdps(70):
        mm,vv,aa,qq = [mp.mpf(str(x)) for x in (m,v,a,q)]
        sigma = mp.sqrt(mm*mm/4+vv*vv/(aa*aa))
        gg,jj = sigma/2+mm/4,sigma/2-mm/4
        kk = aa*qq
        real = 2*(gg-jj*mp.cos(kk))
        imaginary = 2*jj*mp.sin(kk)
        energy_squared = real*real+imaginary*imaginary
        pp = mp.sin(kk)/aa
        return float(energy_squared-vv*vv*pp*pp-mm*mm)


X = np.array([[0, 1], [1, 0]], complex)
Y = np.array([[0, -1j], [1j, 0]], complex)
I = np.eye(2, dtype=complex)


def tensor_word(size, operators):
    mat = np.ones((1, 1), complex)
    for site in range(size):
        mat = np.kron(mat, operators.get(site, I))
    return mat


# Exact algebra, with explicitly independent indeterminates.
e1, e2, p1, p2, vv = sy.symbols('e1 e2 p1 p2 v', real=True)
reverse = sy.expand((e1*e2-vv**2*p1*p2)**2
                    -(e1**2-vv**2*p1**2)*(e2**2-vv**2*p2**2)
                    -vv**2*(e1*p2-e2*p1)**2)
xx, aa, mm = sy.symbols('x a m', nonzero=True, real=True)
one = sy.expand(mm**2+4*vv**2*xx**2/aa**2
                -4*vv**2*xx**2*(1-xx**2)/aa**2
                -(mm**2+4*vv**2*xx**4/aa**2))
cs1, cs2 = sy.symbols('cos1 cos2', real=True)
h, pp = e1+e2, p1+p2
directional = (e1*(2*h*vv**2*p1/e1-2*vv**2*pp*cs1)
               +e2*(2*h*vv**2*p2/e2-2*vv**2*pp*cs2))
bracket = sy.expand(directional-2*vv**2*pp*(h-e1*cs1-e2*cs2))
for name, expression in [('reverse_minkowski_polynomial', reverse),
                         ('one_particle_trig_polynomial', one),
                         ('two_particle_boost_polynomial', bracket)]:
    record(name, int(expression != 0), 0, 0, 'Exact SymPy expansion', str(expression))

# Actual nearest-neighbor Pauli current, tested in one-flip coordinates.
size = 7
indices = [1 << (size-1-x) for x in range(size)]
current_unscaled = sum(tensor_word(size, {x: X, (x+1) % size: Y})
                       -tensor_word(size, {x: Y, (x+1) % size: X})
                       for x in range(size))
fixtures = [(0.91, 1.17, 0.37), (1.2, 0.83, 0.18)]
for fi, (m, v, a) in enumerate(fixtures):
    current_matrix = current_unscaled[np.ix_(indices, indices)]/(4*a)
    fixture_rows = []
    for ell in range(-3, 4):
        k = 2*np.pi*ell/size
        q = k/a
        state = np.exp(1j*k*np.arange(size))/np.sqrt(size)
        actual = np.vdot(state, current_matrix@state)
        predicted = float(c.current(q, m, v, a))
        record(f'pauli_current_{fi}_{ell}', predicted, actual.real, 2e-12,
               'Literal X/Y spin tensors and Fourier eigenvector',
               dict(q=q, actual_imag=actual.imag))
        record(f'pauli_eigenvector_{fi}_{ell}',
               np.linalg.norm(current_matrix@state-predicted*state), 0, 2e-12,
               'Literal current eigenvector residual')
        observed_e = float(c.energy(q, m, v, a))
        actual_e = kernel_energy(q, m, v, a)
        record(f'kernel_energy_{fi}_{ell}', observed_e, actual_e, 2e-12,
               'Hermitian eigenvalue of the actual two-component kernel')
        fixture_rows.append(dict(ell=ell, q=q, current=actual, energy=actual_e))
    raw[f'pauli_fixture_{fi}'] = dict(m=m, v=v, a=a, modes=fixture_rows,
                                      matrix=current_matrix)

m, v, a = fixtures[0]
tuples = [[0.0], [0.71], [-0.001, 0.002], [0.7, -0.4],
          [1.7, 2.1], [-1.4, 0.2, 2.3], [-3.1, -0.8, 0.1, 1.2, 4.7]]
for j, qs in enumerate(tuples):
    n = len(qs)
    exact_ref = reference_mass(qs, m, v, a)
    pred = c.mass_squared(qs, m, v, a)
    record(f'total_mass_{j}', pred, exact_ref, 2e-10,
           'Kernel eigenvalue totals and literal-current symbol', dict(q=qs, n=n))
    bound(f'n_particle_threshold_{j}', n*n*m*m, pred, 2e-10,
          'M7 lower bound at the stated finite tuple', dict(q=qs, n=n))
    qs = np.array(qs, float)
    step = 1e-4
    derivative = 0.0
    for k in range(n):
        direction = np.zeros(n); direction[k] = step
        derivative += kernel_energy(qs[k], m, v, a)*(
            -reference_mass(qs+2*direction, m, v, a)
            +8*reference_mass(qs+direction, m, v, a)
            -8*reference_mass(qs-direction, m, v, a)
            +reference_mass(qs-2*direction, m, v, a))/(12*step)
    record(f'boost_derivative_{j}', c.boost_mass_multiplier(qs, m, v, a),
           derivative, 2e-6, 'Fourth-order directional finite difference of kernel mass',
           dict(q=qs, finite_difference_step=step))

leak_q = [-0.01, 0.01]
leak_mass = reference_mass(leak_q, m, v, a)
raw['threshold_endpoint'] = dict(two_particle_distinct_q=leak_q,
    mass_squared=leak_mass, threshold=4*m*m,
    upper_strictly_above=4*m*m+0.01*m*m,
    endpoint_spectral_atom='Zero by analytic null-set proof, not by this sample')
bound('strict_above_threshold_leak', leak_mass, 4*m*m+0.01*m*m, 0,
      'Distinct opposite momenta give a strict-window leakage witness')
record('geometric_branch_negative_witness',
       float(kernel_energy(np.pi/a, m, v, a)**2-v*v*(np.pi/a)**2 < 0),
       1, 0, 'Wrong branch momentum squared-mass sign', dict(a=a))

# Moving mass windows: direct root of the independent kernel mass.
m, v = 1.0, 0.9
for gamma in [1, 2, 3]:
    table = []
    for a in [0.4, 0.2, 0.1, 0.05, 0.025, 0.0125]:
        delta = m*m*(a*m/v)**gamma
        q_candidate = float(c.window_radius(m, v, a, delta))
        q_float_reference = brentq(lambda q: reference_mass([q], m, v, a)-m*m-delta,
                                   0.0, np.pi/a, xtol=2e-12, rtol=2e-14)
        q_reference = brentq(lambda q: reference_window_excess(q,m,v,a)-delta,
                             0.0, np.pi/a, xtol=2e-12, rtol=2e-14)
        record(f'window_radius_gamma{gamma}_a{a}', q_candidate, q_reference, 2e-7,
               'Root of 70-digit kernel determinant/current mass; unchanged arcsine tolerance')
        capture, quad_error = quad(lambda q: math.exp(-q*q)/math.sqrt(math.pi),
                                   -q_reference, q_reference, epsabs=1e-13, epsrel=1e-13)
        loss = math.erfc(q_candidate)
        record(f'gaussian_loss_gamma{gamma}_a{a}', loss, 1-capture, 2e-11,
               'Direct Gaussian integral versus erfc and candidate support')
        witness_q = (q_reference+np.pi/a)/2
        table.append(dict(a=a, delta=delta, radius_candidate=q_candidate,
                          radius_reference=q_reference, norm_error=math.sqrt(loss),
                          radius_float_kernel=q_float_reference,
                          loss_float_kernel=math.erfc(q_float_reference),
                          capture_direct=capture, reported_quad_error=quad_error,
                          omitted_interior_q=witness_q,
                          omitted_mass=reference_mass([witness_q], m, v, a)))
    raw[f'window_gamma_{gamma}'] = table
raw['window_predicted_limits'] = {'gamma_1': 'P1',
    'gamma_2_radius': (4/v**4)**0.25, 'gamma_3': 'zero'}

# Actual characteristic support, both time signs and endpoint directions.
m, v, R, S = 0.91, 1.17, 0.7, 0.4
support_bound = (R+m/v)*math.exp(v*S)-m/v
for a in [0.2, 0.1, 0.05]:
    delta = m*m*(a*m/v)
    sufficient = v*v*a*a*support_bound**4/4 <= delta
    for initial in [-R, R]:
        for sign in [-1, 1]:
            sol = solve_ivp(lambda t, q: [kernel_energy(q[0], m, v, a)],
                            (0, sign*S), [initial], rtol=2e-12, atol=2e-13)
            end = float(sol.y[0, -1])
            bound(f'flow_bound_a{a}_q{initial}_sign{sign}', abs(end), support_bound,
                  3e-11, 'Kernel characteristic ODE against M15',
                  dict(solver_success=sol.success, nfev=sol.nfev, endpoint=end,
                       delta=delta, support_condition=sufficient))
            if sufficient:
                bound(f'flow_filter_support_a{a}_q{initial}_sign{sign}',
                      reference_mass([end], m, v, a)-m*m, delta, 2e-11,
                      'Only under the separately checked M11 sufficient condition')

# Finite occupation-space transfer and parity diagnostic.
m, v, a, delta, cutoff = 0.91, 1.17, 0.12, 0.2*0.91**2, 2*0.91
qs = np.array([-0.5, 0.2, 0.65, 1.1])
mode_es = np.array([kernel_energy(q, m, v, a) for q in qs])
mode_ps = np.sin(a*qs)/a
bits = np.array([[int(bool(z & (1 << (3-k)))) for k in range(4)] for z in range(16)])
numbers = bits.sum(axis=1)
es, ps = bits@mode_es, bits@mode_ps
parity = np.diag((-1.0)**numbers)
odd = tensor_word(4, {0:X})+0.3*tensor_word(4, {0:X,1:X,2:X})
even = tensor_word(4, {0:X,1:X})+tensor_word(4, {2:X,3:X})
bo = c.filtered_matrix(es, ps, odd, m, v, delta, cutoff)
be = c.filtered_matrix(es, ps, even, m, v, delta, cutoff)
record('odd_seed_parity', np.linalg.norm(parity@odd+odd@parity), 0, 2e-13,
       'Explicit finite occupation parity')
record('even_seed_parity', np.linalg.norm(parity@even-even@parity), 0, 2e-13,
       'Explicit finite occupation parity')
record('filtered_odd_parity', np.linalg.norm(parity@bo+bo@parity), 0, 2e-13,
       'Transfer filter preserves explicit parity')
record('odd_vacuum_column_norm', np.linalg.norm(bo[:,0]), 1, 2e-13,
       'Actual column of finite transfer-filtered spin seed')
record('odd_off_one_particle_column', np.linalg.norm(bo[numbers != 1,0]), 0, 0,
       'Joint total-mass threshold applied to one-plus-three-particle seed')
record('even_vacuum_column', np.linalg.norm(be[:,0]), 0, 0,
       'Even seed has only even occupation sectors')
record('adjoint_vacuum_column', np.linalg.norm(bo[0,:]), 0, 0,
       'Positive-energy transfer, tested as a matrix row')
e_high = 4*cutoff
p_high = math.sqrt(e_high**2-m*m)/v
record('compact_energy_support', float(c.compact_symbol(e_high, p_high, m, v,
                                                       delta, cutoff)), 0, 0,
       'Mass-shell point strictly outside compact energy support')
record('vacuum_symbol', float(c.compact_symbol(0, 0, m, v, delta, cutoff)), 0, 0,
       'Vacuum is excluded by the positive-energy cutoff')
raw['occupation_fixture'] = dict(m=m,v=v,a=a,delta=delta,cutoff=cutoff,q=qs,
                                bits=bits,mode_energy=mode_es,mode_current=mode_ps,
                                energy=es,current=ps,odd_filtered=bo,even_filtered=be)

# General Fourier signs: actual two unitary conjugations, not a round-trip FFT.
e0,p0,sig_t,sig_s = 1.31,0.42,0.45,0.7
seed = (np.arange(256).reshape(16,16)+1j*np.arange(255,-1,-1).reshape(16,16))/256
integrals = {}
for nodes in [32,48]:
    abscissa, weights = hermgauss(nodes)
    weights = weights/math.sqrt(math.pi)
    time_filtered = np.zeros_like(seed)
    for x,w in zip(abscissa,weights):
        t = math.sqrt(2)*sig_t*x
        u = np.diag(np.exp(1j*t*es))
        time_filtered += w*np.exp(-1j*t*e0)*(u@seed@u.conj().T)
    both = np.zeros_like(seed)
    for x,w in zip(abscissa,weights):
        s = math.sqrt(2)*sig_s*x
        u = np.diag(np.exp(1j*s*ps))
        both += w*np.exp(-1j*s*p0)*(u@time_filtered@u.conj().T)
    integrals[nodes] = both
de,dp = es[:,None]-es[None,:], ps[:,None]-ps[None,:]
prediction = c.gaussian_symbol(de,dp,e0,p0,sig_t,sig_s)*seed
for nodes in [32,48]:
    record(f'joint_fourier_sign_{nodes}', np.max(np.abs(prediction-integrals[nodes])),
           0, 2e-11, 'Gauss-Hermite integration of literal energy/current conjugations')
record('joint_fourier_refinement', np.max(np.abs(integrals[48]-integrals[32])), 0,
       2e-11, 'Independent quadrature resolution comparison')
raw['joint_fourier'] = dict(e0=e0,p0=p0,sigma_t=sig_t,sigma_s=sig_s,
                            reference_32=integrals[32],reference_48=integrals[48],
                            candidate=prediction)

resolution = {
 'per_element': 'Finite literal Pauli current and explicit filtered spin-seed matrix elements are checked.',
 'per_site': 'Seven-site current tensors are checked; no thermodynamic or sitewise continuum limit is numerically executed.',
 'per_mode': 'Actual kernel energies, normalized-current modes, mass windows and both Fourier clocks are checked.',
 'per_block': 'Explicit n=1,2,3,5 tuples and a four-mode occupation-space parity/transfer fixture are checked.',
 'lattice_wide': 'Checked and not executed numerically: the infinite-chain locality and full-Fock domain claims rest on the analytic proof.'}
report = dict(candidate=str(Path(args.candidate).resolve()), rows=rows, raw=raw,
              resolution=resolution, failed=[r['name'] for r in rows if not r['accepted']],
              status='finite_controls_accepted' if all(r['accepted'] for r in rows)
                     else 'finite_controls_rejected',
              numerical_scope='float64 diagnostics with a 70-digit kernel-determinant window-root reference; no interval error bounds')
print(json.dumps(clean(report), indent=2, allow_nan=False))
sys.exit(0 if not report['failed'] else 1)
