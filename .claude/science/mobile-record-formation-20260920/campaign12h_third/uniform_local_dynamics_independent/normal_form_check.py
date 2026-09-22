"""Independent finite algebra for the uniform-local-dynamics reconstruction.

No new author module is read. The only local import is the already sealed
independent Gauss-sector builder. A finite square tests coefficients; it is
not a replacement for the uniform locality proof or its torus hypotheses.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
from math import factorial
import importlib.util
import json
import sys
import numpy as np
import sympy as s
from scipy.linalg import expm

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
PRIOR = HERE.parent/'hardcore_live_density_independent'


def identity(path):
    path = Path(path).resolve(); data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': sha256(data).hexdigest()}


def own_builder():
    path = PRIOR/'finite_sector_check.py'
    assert identity(path)['sha256'] == 'c1e6142e632ae77c14fee1b76079c8cba0f2e9c73cf1fed2e40f84f0a3893122'
    spec = importlib.util.spec_from_file_location('sealed_own_sector', path)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


def comm(a, b):
    return a*b-b*a


def normal_form(q, v, order):
    dim = q.rows; zero = s.zeros(dim)
    coefficient = [zero.copy() for _ in range(order+1)]
    coefficient[0] = q; coefficient[1] = v
    generators = []
    checks = []
    for n in range(1, order+1):
        residual = coefficient[n]
        sn = s.zeros(dim)
        for a in range(dim):
            for b in range(dim):
                gap = q[a, a]-q[b, b]
                if gap:
                    sn[a, b] = residual[a, b]/gap
        assert sn.T == -sn
        transformed = [zero.copy() for _ in coefficient]
        for j, term in enumerate(coefficient):
            work = term
            for k in range((order-j)//n+1):
                transformed[j+n*k] += work/s.factorial(k)
                work = comm(sn, work)
        coefficient = transformed
        assert comm(q, coefficient[n]) == zero
        assert coefficient[n].T == coefficient[n]
        if n % 2:
            assert coefficient[n] == zero
        generators.append(sn)
        checks.append({'order': n, 'generator_nonzero_entries': sum(x != 0 for x in sn),
                       'coefficient_nonzero_entries': sum(x != 0 for x in coefficient[n]),
                       'commutes_penalty_exactly': True, 'odd_coefficient_zero': n % 2 == 1})
    return coefficient, generators, checks


def strings(matrix):
    return [[str(x) for x in row] for row in matrix.tolist()]


def square_control(own):
    m = own.build(4, [(i, (i+1) % 4) for i in range(4)], {0, 2}, 0)
    dim = len(m['states']); zero = s.zeros(dim)
    v = -sum(m['hop'], zero)
    number = s.diag(*[int(sum(row)) for row in m['occ']])
    low = [i for i, q in enumerate(m['charges']) if q == [1, 0, 1, 0]]
    original = [i for i, q in enumerate(m['charges']) if all(x >= 0 for x in q)]
    stored = {}; generators = {}
    for name, diagonal in [('sublattice', m['b']), ('star_matter_representative', m['field'])]:
        q = s.diag(*diagonal)
        assert all(q[i, i] == 0 for i in low)
        coefficient, gs, checks = normal_form(q, v, 10)
        assert all(comm(number, g) == zero for g in gs)
        assert coefficient[2].extract(low, low) == -2*s.eye(2)
        assert coefficient[4].extract(low, low) == s.Matrix([[2, -2], [-2, 2]])
        stored[name] = {'penalty_diagonal': list(map(str, diagonal)), 'order_checks': checks,
                        'low_coefficients': {str(k): strings(coefficient[k].extract(low, low)) for k in range(2, 11, 2)},
                        'number_preserving_generators': True}
        generators[name] = (coefficient, gs)
    ca, ga = generators['sublattice']; cb, gb = generators['star_matter_representative']
    assert all(a.extract(original, original) == b.extract(original, original) for a, b in zip(ca, cb))
    assert all(a.extract(original, original) == b.extract(original, original) for a, b in zip(ga, gb))
    cases = []
    eye = np.eye(dim)
    field_z = np.diag([2*(word & 1)-1 for word in m['states']])
    rho0 = np.zeros((dim, dim), complex); rho0[low[0], low[0]] = 1
    birth_ops = [np.array(vv[1]+vv[-1], float) for vv in m['births']]
    for name, diagonal in [('sublattice', m['b']), ('star_matter_representative', m['field'])]:
        coefficient, gs = generators[name]
        for epsilon in (0.16, 0.12, 0.09):
            delta = 1/(2*epsilon**4); tt = epsilon*delta; beta = epsilon**7
            u = np.eye(dim, dtype=complex)
            for n, g in enumerate(gs, 1):
                u = expm(epsilon**n*np.array(g, float)) @ u
            ham = delta*(np.diag(np.array(diagonal, float))+epsilon*np.array(v, float))
            bd = delta*sum((epsilon**k*np.array(a, float) for k, a in enumerate(coefficient)), np.zeros((dim, dim)))
            remainder = np.linalg.norm(u@ham@u.conj().T-bd, 2)
            dressed = u.conj().T@rho0@u
            generator = -1j*(np.kron(eye, ham)-np.kron(ham.T, eye))
            for j in birth_ops:
                loss = j.T@j
                generator += beta*(np.kron(j,j)-.5*np.kron(eye,loss)-.5*np.kron(loss.T,eye))
            for duration in (.25, .75, 1.0):
                state = (expm(duration*generator)@dressed.reshape(-1, order='F')).reshape((dim,dim), order='F')
                actual = float(np.trace(field_z@state).real)
                reference = -float(np.cos(2*duration))
                assert abs(np.trace(state)-1) < 1e-8
                assert np.linalg.eigvalsh((state+state.conj().T)/2).min() > -1e-8
                cases.append({'penalty': name, 'epsilon': epsilon, 'Delta': delta, 't': tt, 'beta': beta,
                              'time': duration, 'prepared_field_expectation': float(np.trace(field_z@dressed).real),
                              'open_field_expectation': actual, 'ring_field_expectation': reference,
                              'absolute_difference': abs(actual-reference),
                              'operator_remainder_norm': float(remainder),
                              'remainder_over_Delta_epsilon11': float(remainder/(delta*epsilon**11)),
                              'trace_error': float(abs(np.trace(state)-1))})
    return {'physical_dimension': dim, 'no_minus_dimension': len(original), 'low_dimension': len(low),
            'exact_series': stored, 'two_penalties_agree_on_original_number_sector': True,
            'finite_open_controls': cases,
            'scope': 'The four-site square is an algebra control. Numerical convergence is not the uniform-volume proof.'}


def onsite_gap_and_signs():
    # Work on the entire three-site matter/link local space, not only on states
    # with a specified remote boundary. Both orientations and charges are tested.
    rows = []
    for tail_A in (True, False):
        ref = (int(tail_A), int(not tail_A))
        for q in (-1, 1):
            before = (q, 0); after = (0, q)
            r_before = sum(s.Rational((z-a)**2,2) for z,a in zip(before,ref))
            r_after = sum(s.Rational((z-a)**2,2) for z,a in zip(after,ref))
            assert abs(r_after-r_before) == 1
            nr_before = int(not tail_A); nr_after = int(tail_A)
            assert abs(nr_after-nr_before) == 1
            charge_before = (0,0); charge_after = (q,-q)
            rb = sum(s.Rational((z-a)**2,2) for z,a in zip(charge_before,ref))
            ra = sum(s.Rational((z-a)**2,2) for z,a in zip(charge_after,ref))
            assert ra-rb in (0,2)
            rows.append({'tail_A': tail_A, 'transported_charge': q, 'star_hop_gap': str(r_after-r_before),
                         'star_birth_gap': str(ra-rb)})
    # Sawtooth homological inverse and its sign, for integer and half-integer spectra.
    theta = s.symbols('theta', real=True)
    inverse = []
    for period in (2*s.pi, 4*s.pi):
        for mode in (-3,-2,-1,1,2,3):
            frequency = 2*s.pi*mode/period
            integral = s.simplify(s.integrate(s.I*(theta-period/2)*s.exp(s.I*frequency*theta),(theta,0,period))/period)
            assert s.simplify(integral-1/frequency) == 0
            inverse.append({'period_over_pi':str(period/s.pi),'frequency':str(frequency),'inverse':str(integral)})
    return {'local_hop_and_birth_gaps': rows, 'sawtooth_inverse': inverse}


def exponent_and_cone_controls():
    exponents = []
    for d in (1,2,3,4):
        order = 2*d+4; birth_power = 2*d+1
        residual = order-3-2*d; birth = birth_power-2*d
        assert residual == birth == 1
        exponents.append({'dimension':d,'normal_form_order':order,'birth_power':birth_power,
                          'normal_form_error_power_after_cone_volume':residual,
                          'birth_error_power_after_cone_volume':birth})
    # Explicit finite-torus cone sums: the proof uses polynomial ball growth,
    # including when the cone is wider than the torus.
    cone = []
    for side in (6,8,12):
        points = np.indices((side,side,side)).reshape(3,-1).T
        distance = np.minimum(points,side-points).sum(axis=1)
        for radius in (0,1,3,7,15):
            count = int(np.count_nonzero(distance <= radius))
            assert count <= (2*radius+1)**3
            clipped = float(np.minimum(1,np.exp(np.minimum(700,radius-distance))).sum())
            cone.append({'side':side,'radius':radius,'ball_size':count,
                         'clipped_exponential_sum':clipped,'divided_by_one_plus_radius_cubed':clipped/(1+radius)**3})
    return {'dimension_exponents':exponents,'finite_torus_cone_controls':cone,
            'limit':'Arithmetic and finite controls only; the analytic shell-sum bound is proved in the report.'}


def main():
    own = own_builder()
    out = {'created_utc':datetime.now(timezone.utc).isoformat(), 'script':identity(__file__),
           'dependency':identity(PRIOR/'finite_sector_check.py'), 'square':square_control(own),
           'onsite':onsite_gap_and_signs(),'scaling':exponent_and_cone_controls(),
           'read_boundary':'No new author transport/ramp/normal-form source or output accessed.'}
    data = json.dumps(out,indent=2)+'\n';(HERE/'NORMAL_FORM_RESULTS.json').write_text(data);print(data,end='')


if __name__ == '__main__':
    main()
