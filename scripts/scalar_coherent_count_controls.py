"""Author ideal coherent two-leg count/adjoint integration controls.

Uses the already supplied synthetic dynamics, with station body0, spacecraft
body1, fixed turnaround factor1.4 and no transponder delay or clock readout.
"""
AUDIT_TIMEOUT_SEC = 180

from pathlib import Path
from datetime import datetime, timezone
import importlib.util
import hashlib
import json
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.linalg import null_space
from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent
HELPER = HERE/'scalar_count_adjoint_controls.py'
spec = importlib.util.spec_from_file_location('proper_adjoint', HELPER)
a = importlib.util.module_from_spec(spec); spec.loader.exec_module(a)
g = a.geo
TURNAROUND = 1.4


def events(s):
    xr = g.ref(s, 0)[0]
    bounce = brentq(lambda t:s-t-np.linalg.norm(xr-g.ref(t, 1)[0]), s-3, s-.5, xtol=1e-14)
    xb = g.ref(bounce, 1)[0]
    emit = brentq(lambda t:bounce-t-np.linalg.norm(xb-g.ref(t, 0)[0]), bounce-3, bounce-.5, xtol=1e-14)
    return np.array([emit, bounce, s])


def endpoint_atoms(s, omit_uplink_factor=False):
    times = events(s); bodies = [0, 1, 0]
    rows = np.zeros((3, 14))
    rows[0, 6] = 1.
    le = g.lapse(times[0], 0)
    product = 1.
    for j in [1, 2]:
        xp, up = g.ref(times[j-1], bodies[j-1])
        xn, un = g.ref(times[j], bodies[j])
        direction = xn-xp; direction /= np.linalg.norm(direction)
        dm, dp = 1-direction@up, 1-direction@un
        factor = 1. if omit_uplink_factor and j == 2 else product
        coeff = le*factor*direction/dm
        rows[j-1, 7*bodies[j-1]:7*bodies[j-1]+3] += coeff
        rows[j, 7*bodies[j]:7*bodies[j]+3] -= coeff
        product *= dp/dm
    rows[2, 6] -= le*product/g.lapse(s, 0)
    return times, rows


def observations(samples, omit_uplink_factor=False):
    taus = np.array([g.clock(s, 0) for s in samples])
    nobs = len(samples)-1; atoms = {}
    for i in range(nobs):
        for j, sign in [(i, -1.), (i+1, 1.)]:
            times, rows = endpoint_atoms(samples[j], omit_uplink_factor)
            for time, row in zip(times, rows):
                if time not in atoms:
                    atoms[time] = np.zeros((nobs, 14))
                atoms[time][i] += sign*TURNAROUND*row/(taus[i+1]-taus[i])
    assert min(atoms)>a.START and max(atoms)<a.END
    return taus, atoms


def nonlinear_counts(sol, samples, taus):
    phases = []
    for sref, tau in zip(samples, taus):
        s = brentq(lambda t:sol(t)[6]-tau, sref-.3, sref+.3, xtol=1e-13)
        xr = sol(s)[:3]
        bounce = brentq(lambda t:s-t-np.linalg.norm(xr-sol(t)[7:10]), s-3, s-.5, xtol=1e-13)
        xb = sol(bounce)[7:10]
        emit = brentq(lambda t:bounce-t-np.linalg.norm(xb-sol(t)[:3]), bounce-3, bounce-.5, xtol=1e-13)
        phases.append(TURNAROUND*sol(emit)[6])
    return np.diff(phases)/np.diff(taus)


def run_checks():
    checks = []
    def close(name, got, expected, tol):
        err = float(np.max(np.abs(got-expected)))
        assert err<tol, (name, err, tol)
        checks.append({'name':name, 'max_absolute_error':err, 'tolerance':tol})
    samples = np.linspace(2., 6.7, 23)
    taus, atoms = observations(samples)
    nobs = len(samples)-1
    z0 = .06*np.sin(np.arange(14)+.4)
    fw = a.forward(z0)
    direct = sum(q@fw(s)[:14] for s, q in atoms.items())
    initial = sum(q@fw(s)[14:].reshape(14, 14) for s, q in atoms.items())
    nadj, segments, jumps = a.adjoint(atoms, nobs)
    close('coherent_initial_response_forward_vs_adjoint', nadj, initial, 2e-10)
    field_response = np.zeros(nobs); const = np.zeros(nobs)
    bybody = np.zeros((nobs, 2, 2))
    nodes, weights = leggauss(20)
    spacecraft_clock_max = 0.
    for lo, hi, fun in segments:
        for s, w in zip(lo+(nodes+1)*(hi-lo)/2, weights*(hi-lo)/2):
            lam = fun(s).reshape(nobs, 14)
            _, forcing = a.linear(s)
            field_response += w*lam@forcing
            const += w*g.ALPHA*(lam[:, 6]*g.lapse(s, 0)+lam[:, 13]*g.lapse(s, 1))
            spacecraft_clock_max = max(spacecraft_clock_max, float(np.max(np.abs(lam[:, 13]))))
            for body in [0, 1]:
                off = 7*body
                bybody[:, body, 0] += w*lam[:, off+3:off+6]@forcing[off+3:off+6]
                bybody[:, body, 1] += w*lam[:, off+6]*forcing[off+6]
    close('coherent_count_from_joint_adjoint', direct, nadj@z0+field_response, 2e-10)
    assert spacecraft_clock_max == 0.
    checks.append({'name':'ideal_coherent_spacecraft_direct_clock_absent', 'max_adjoint_clock':spacecraft_clock_max})
    assert np.max(np.abs(bybody[:, 1, 0]))>.01
    checks.append({'name':'spacecraft_force_response_retained', 'max_count_force_response':float(np.max(np.abs(bybody[:, 1, 0])))})
    nuisance = np.column_stack([np.ones(nobs), (taus[:-1]+taus[1:])/2])
    design = np.column_stack([initial, nuisance, const])
    contrast = null_space(design.T, rcond=1e-13)
    assert contrast.shape[1]>0
    close('coherent_full_initial_nuisance_constant_cancellation', contrast.T@design, np.zeros((contrast.shape[1], design.shape[1])), 1e-11)
    close('coherent_contrast_count_from_field', contrast.T@direct, contrast.T@field_response, 2e-10)
    for body in [0, 1]:
        off = body*7
        jump = max(np.max(np.abs(q[:, off+3:off+6])) for _, q in jumps)
        assert jump == 0
        checks.append({'name':f'coherent_no_force_weight_jump_body_{body}', 'max_jump':float(jump)})
        close(f'coherent_initial_force_trace_body_{body}', contrast.T@nadj[:, off+3:off+6], np.zeros((contrast.shape[1], 3)), 1e-11)
    _, wrong_atoms = observations(samples, omit_uplink_factor=True)
    wrong = sum(q@fw(s)[:14] for s, q in wrong_atoms.items())
    omission = float(np.max(np.abs(wrong-direct)))
    assert omission>.001, omission
    checks.append({'name':'reject_omitted_composed_light_time_factor', 'max_count_error':omission})
    convergence = []
    for eps in [.004, .002, .001]:
        plus = nonlinear_counts(a.nonlinear(eps, z0), samples, taus)
        minus = nonlinear_counts(a.nonlinear(-eps, z0), samples, taus)
        err = float(np.max(np.abs((plus-minus)/(2*eps)-direct)))
        convergence.append({'eps':eps, 'max_count_error':err})
    assert convergence[-1]['max_count_error']<1e-6, convergence
    checks.append({'name':'nonlinear_coherent_link_to_linear_count', 'error':convergence[-1]['max_count_error']})
    for i in range(2):
        ratio = convergence[i]['max_count_error']/convergence[i+1]['max_count_error']
        assert 3.7<ratio<4.3, ratio
        checks.append({'name':f'coherent_second_order_{i}', 'ratio':ratio})
    result = {
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'helper_sha256':hashlib.sha256(HELPER.read_bytes()).hexdigest(),
              'geometry_helper_sha256':hashlib.sha256(a.HELPER.read_bytes()).hexdigest(),
              'checks_passed':len(checks), 'checks':checks, 'convergence':convergence,
              'observation_count':nobs, 'contrast_dimension':contrast.shape[1],
              'design_singular_values':np.linalg.svd(design, compute_uv=False).tolist(),
              'rank_rcond':1e-13, 'turnaround':TURNAROUND,
              'scope':'Synthetic ideal instantaneous coherent station-spacecraft-station link. Shared station clock; no spacecraft oscillator phase. Both orbital force responses retained. Supplied conformal flat propagation and external dynamics; no actual calibration, energy/error budget, massive extension or empirical test. Floating rank and finite-step checks are not certified enclosures.'}
    return result


if __name__ == '__main__':
    print(json.dumps(run_checks(), indent=2))
