"""Personal finite-perturbation test of actual one-way proper-time endpoints.

The trajectories, constant source frequency, conformal flat patch and free
plane-wave probes are synthetic supplied premises. Plane waves test local
variation, not a finite global energy assertion or an actual radio data fit.
"""
AUDIT_TIMEOUT_SEC = 180

from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

AB = 1.2
ALPHA = .3
START = -4.
N1 = np.array([1., 2., -.5]); N1 /= np.linalg.norm(N1)
N2 = np.array([-.3, .4, 1.]); N2 /= np.linalg.norm(N2)


def ref(s, body):
    if body == 0:
        x = np.array([.03*s+.04*np.sin(.9*s), .06*np.cos(.8*s), .02*np.sin(1.3*s)])
        u = np.array([.03+.036*np.cos(.9*s), -.048*np.sin(.8*s), .026*np.cos(1.3*s)])
    else:
        x = np.array([2+.04*s+.05*np.sin(.5*s), .6+.06*np.sin(.7*s), -.2+.02*s+.03*np.cos(.9*s)])
        u = np.array([.04+.025*np.cos(.5*s), .042*np.cos(.7*s), .02-.027*np.sin(.9*s)])
    return x, u


def variation(s, body):
    if body == 0:
        xi = np.array([.24*np.sin(.8*s), .17*np.cos(1.1*s), -.14*np.sin(.6*s)])
        du = np.array([.192*np.cos(.8*s), -.187*np.sin(1.1*s), -.084*np.cos(.6*s)])
    else:
        xi = np.array([-.21*np.cos(.7*s), .26*np.sin(.6*s), .18*np.cos(.9*s)])
        du = np.array([.147*np.sin(.7*s), .156*np.cos(.6*s), -.162*np.sin(.9*s)])
    return xi, du


def field(s, x):
    return .6*np.cos(.9*(s-N1@x)+.3)+.4*np.sin(1.3*(s-N2@x)-.2)


def lapse(s, body, eps=0.):
    x, u = ref(s, body)
    xi, du = variation(s, body)
    ue = u+eps*du
    return AB*np.exp(eps*ALPHA*field(s, x+eps*xi))*np.sqrt(1-ue@ue)


def clock(s, body, eps=0.):
    initial = [.2, -.1][body]+eps*[.13, -.09][body]
    return initial+quad(lambda v:lapse(v, body, eps), START, s,
                        epsabs=2e-12, epsrel=2e-12)[0]


def clock_variation(s, body):
    def rhs(v):
        x, u = ref(v, body)
        _, du = variation(v, body)
        root = np.sqrt(1-u@u)
        return ALPHA*AB*root*field(v, x)-AB*(u@du)/root
    return [.13, -.09][body]+quad(rhs, START, s, epsabs=2e-12, epsrel=2e-12)[0]


def light_time(s, eps=0.):
    xr = ref(s, 1)[0]+eps*variation(s, 1)[0]
    def f(t):
        xe = ref(t, 0)[0]+eps*variation(t, 0)[0]
        return s-t-np.linalg.norm(xr-xe)
    return brentq(f, s-4, s-.2, xtol=1e-14)


def observed_phase(tau, seed, eps):
    s = brentq(lambda v:clock(v, 1, eps)-tau, seed-.4, seed+.4, xtol=1e-14)
    t = light_time(s, eps)
    return clock(t, 0, eps), s, t


def predicted_chi(s, omit_receiver_clock=False, reverse_geometry=False):
    t = light_time(s)
    xe, ue = ref(t, 0); xr, ur = ref(s, 1)
    n = xr-xe; n /= np.linalg.norm(n)
    de = 1-n@ue; dr = 1-n@ur
    le, lr = lapse(t, 0), lapse(s, 1)
    er = 0. if omit_receiver_clock else clock_variation(s, 1)
    geom = le/de*n@(variation(t, 0)[0]-variation(s, 1)[0])
    return clock_variation(t, 0)-le*dr/(lr*de)*er+(-geom if reverse_geometry else geom)


def run_checks():
    checks = []
    samples = np.array([.5, 1.4, 2.9, 4.2])
    taus = np.array([clock(s, 1) for s in samples])
    expected = np.array([predicted_chi(s) for s in samples])
    count_expected = np.diff(expected)/np.diff(taus)
    convergence = []
    for eps in [.05, .025, .0125, .00025]:
        plus = np.array([observed_phase(tau, s, eps) for tau, s in zip(taus, samples)])
        minus = np.array([observed_phase(tau, s, -eps) for tau, s in zip(taus, samples)])
        derivative = (plus[:, 0]-minus[:, 0])/(2*eps)
        count = np.diff(derivative)/np.diff(taus)
        err = float(np.max(np.abs(derivative-expected)))
        count_err = float(np.max(np.abs(count-count_expected)))
        convergence.append({'eps':eps, 'phase_error':err, 'count_error':count_err})
        if eps == .00025:
            assert err<3e-8 and count_err<3e-8, (err, count_err)
            checks.append({'name':'full_fixed_proper_endpoint_phase', 'max_error':err, 'tolerance':3e-8})
            checks.append({'name':'finite_count_from_actual_null_intersections', 'max_error':count_err, 'tolerance':3e-8})
            ds = (plus[:, 1]-minus[:, 1])/(2*eps)
            ds_expected = np.array([-clock_variation(s, 1)/lapse(s, 1) for s in samples])
            serr = float(np.max(np.abs(ds-ds_expected)))
            assert serr<3e-8, serr
            checks.append({'name':'receiver_coordinate_shift_at_fixed_proper_time', 'max_error':serr})
    for i in range(2):
        ratio = convergence[i]['phase_error']/convergence[i+1]['phase_error']
        assert 3.8<ratio<4.2, ratio
        checks.append({'name':f'central_difference_second_order_{i}', 'error_ratio':ratio})
    for name, options in [('omit_receiver_clock', {'omit_receiver_clock':True}),
                          ('reverse_retarded_position_term', {'reverse_geometry':True})]:
        wrong = np.array([predicted_chi(s, **options) for s in samples])
        err = float(np.max(np.abs(np.diff(wrong)/np.diff(taus)-count_expected)))
        assert err>.01, (name, err)
        checks.append({'name':'reject_'+name, 'count_error':err})
    eps = .0005
    for body in [0, 1]:
        errs = [abs((clock(s, body, eps)-clock(s, body, -eps))/(2*eps)-clock_variation(s, body)) for s in samples]
        assert max(errs)<2e-8, errs
        checks.append({'name':f'proper_lapse_variation_body_{body}', 'max_error':max(errs)})
    result = {
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'checks_passed':len(checks), 'checks':checks, 'convergence':convergence,
              'reference_receiver_coordinate_times':samples.tolist(),
              'fixed_receiver_proper_times':taus.tolist(), 'phase_variation':expected.tolist(),
              'normalized_count_variation':count_expected.tolist(),
              'scope':'Synthetic one-way conformal-flat patch; no empirical data, no transponder/media/electronics, no finite-energy statement for the plane-wave probes. First-order numerical convergence is not a nonlinear uniform remainder bound.'}
    return result


if __name__ == '__main__':
    print(json.dumps(run_checks(), indent=2))
