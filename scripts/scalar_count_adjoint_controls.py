"""Author full count -> orbit/clock adjoint -> scalar-source controls.

Synthetic externally forced reference trajectories, not a spacecraft fit.
The imported helper supplies independently exercised null/clock geometry.
"""
AUDIT_TIMEOUT_SEC = 180

from pathlib import Path
from datetime import datetime, timezone
import importlib.util
import hashlib
import json
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import solve_ivp
from scipy.linalg import null_space
from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent
HELPER = HERE/'scalar_proper_count_controls.py'
spec = importlib.util.spec_from_file_location('proper_count_geometry', HELPER)
geo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(geo)
START = geo.START
END = 7.2


def acceleration_ref(s, body):
    if body == 0:
        return np.array([-.0324*np.sin(.9*s), -.0384*np.cos(.8*s), -.0338*np.sin(1.3*s)])
    return np.array([-.0125*np.sin(.5*s), -.0294*np.sin(.7*s), -.0243*np.cos(.9*s)])


def matrices(s, body):
    k = np.diag([.035+.01*np.cos(.3*s), .045+.008*np.sin(.4*s), .025+.004*body])
    k[0, 1] = k[1, 0] = .003*np.sin(.5*s)
    d = np.diag([.006, .009, .004])
    return k, d


def source(s, x, u):
    th1, th2 = .9*(s-geo.N1@x)+.3, 1.3*(s-geo.N2@x)-.2
    h = .6*np.cos(th1)+.4*np.sin(th2)
    p1, p2 = -.54*np.sin(th1), .52*np.cos(th2)
    grad = -geo.N1*p1-geo.N2*p2
    ah = -(1-u@u)*(grad+u*(p1+p2))
    return h, ah


def linear(s):
    l = np.zeros((14, 14)); f = np.zeros(14)
    for body in [0, 1]:
        a = 7*body
        x, u = geo.ref(s, body)
        k, d = matrices(s, body)
        h, ah = source(s, x, u)
        root = np.sqrt(1-u@u)
        l[a:a+3, a+3:a+6] = np.eye(3)
        l[a+3:a+6, a:a+3] = -k
        l[a+3:a+6, a+3:a+6] = -d
        l[a+6, a+3:a+6] = -geo.AB*u/root
        f[a+3:a+6] = geo.ALPHA*ah
        f[a+6] = geo.ALPHA*geo.AB*root*h
    return l, f


def observations(samples):
    taus = np.array([geo.clock(s, 1) for s in samples])
    nobs = len(samples)-1
    atoms = {}
    for i in range(nobs):
        span = taus[i+1]-taus[i]
        for j, sign in [(i, -1.), (i+1, 1.)]:
            s = samples[j]; t = geo.light_time(s)
            xe, ue = geo.ref(t, 0); xr, ur = geo.ref(s, 1)
            n = xr-xe; n /= np.linalg.norm(n)
            de, dr = 1-n@ue, 1-n@ur
            le, lr = geo.lapse(t, 0), geo.lapse(s, 1)
            qe = np.zeros(14); qr = np.zeros(14)
            qe[:3] = le*n/de; qe[6] = 1.
            qr[7:10] = -le*n/de; qr[13] = -le*dr/(lr*de)
            for time, q in [(t, qe), (s, qr)]:
                if time not in atoms:
                    atoms[time] = np.zeros((nobs, 14))
                atoms[time][i] += sign*q/span
    assert min(atoms)>START and max(atoms)<END
    return taus, atoms


def forward(z0):
    def rhs(s, yy):
        l, f = linear(s)
        return np.r_[l@yy[:14]+f, (l@yy[14:].reshape(14, 14)).ravel()]
    sol = solve_ivp(rhs, (START, END), np.r_[z0, np.eye(14).ravel()],
                    method='DOP853', rtol=3e-12, atol=3e-14, dense_output=True)
    assert sol.success
    return sol.sol


def adjoint(atoms, nobs):
    knots = sorted({START, END, *atoms.keys()})
    lam = np.zeros((nobs, 14)); segments = []; jumps = []
    for a, b in reversed(list(zip(knots[:-1], knots[1:]))):
        q = atoms.get(b, np.zeros_like(lam))
        jumps.append((b, q.copy()))
        lam = lam+q
        def rhs(s, yy):
            l, _ = linear(s)
            return (-yy.reshape(nobs, 14)@l).ravel()
        sol = solve_ivp(rhs, (b, a), lam.ravel(), method='DOP853',
                        rtol=3e-12, atol=3e-14, dense_output=True)
        assert sol.success
        segments.append((a, b, sol.sol))
        lam = sol.y[:, -1].reshape(nobs, 14)
    return lam, list(reversed(segments)), jumps


def nonlinear(eps, z0):
    initial = np.empty(14)
    for body in [0, 1]:
        a = body*7
        x, u = geo.ref(START, body)
        initial[a:a+3] = x
        initial[a+3:a+6] = u
        initial[a+6] = geo.clock(START, body)
    initial += eps*z0
    def rhs(s, yy):
        out = np.zeros(14)
        for body in [0, 1]:
            a = 7*body; x = yy[a:a+3]; u = yy[a+3:a+6]
            xr, ur = geo.ref(s, body)
            k, d = matrices(s, body)
            h, ah = source(s, x, u)
            out[a:a+3] = u
            out[a+3:a+6] = acceleration_ref(s, body)-k@(x-xr)-d@(u-ur)+eps*geo.ALPHA*ah
            out[a+6] = geo.AB*np.exp(eps*geo.ALPHA*h)*np.sqrt(1-u@u)
        return out
    sol = solve_ivp(rhs, (START, END), initial, method='DOP853',
                    rtol=3e-12, atol=3e-14, dense_output=True)
    assert sol.success
    return sol.sol


def nonlinear_counts(sol, samples, taus):
    phase = []
    for sref, tau in zip(samples, taus):
        s = brentq(lambda v:sol(v)[13]-tau, sref-.3, sref+.3, xtol=1e-13)
        xr = sol(s)[7:10]
        t = brentq(lambda v:s-v-np.linalg.norm(xr-sol(v)[:3]), s-3., s-.5, xtol=1e-13)
        phase.append(sol(t)[6])
    return np.diff(phase)/np.diff(taus)


def run_checks():
    checks = []
    def close(name, a, b, tol):
        err = float(np.max(np.abs(a-b)))
        assert err<tol, (name, err, tol)
        checks.append({'name':name, 'max_absolute_error':err, 'tolerance':tol})
    samples = np.linspace(.5, 6.7, 23)
    taus, atoms = observations(samples)
    nobs = len(samples)-1
    z0 = .06*np.sin(np.arange(14)+.4)
    fw = forward(z0)
    direct = sum(q@fw(s)[:14] for s, q in atoms.items())
    n = sum(q@fw(s)[14:].reshape(14, 14) for s, q in atoms.items())
    nadj, segments, jumps = adjoint(atoms, nobs)
    close('initial_response_forward_vs_adjoint', n, nadj, 2e-10)
    g, gw = leggauss(20)
    by_body = np.zeros((nobs, 2, 2))
    constant_response = np.zeros(nobs)
    for a, b, fun in segments:
        ss = a+(g+1)*(b-a)/2; weights = gw*(b-a)/2
        for s, weight in zip(ss, weights):
            ll = fun(s).reshape(nobs, 14)
            _, f = linear(s)
            constant_response += weight*geo.ALPHA*(ll[:, 6]*geo.lapse(s, 0)+ll[:, 13]*geo.lapse(s, 1))
            for body in [0, 1]:
                off = 7*body
                by_body[:, body, 0] += weight*ll[:, off+3:off+6]@f[off+3:off+6]
                by_body[:, body, 1] += weight*ll[:, off+6]*f[off+6]
    response = by_body.sum(axis=(1, 2))
    close('actual_counts_forward_vs_initial_plus_joint_adjoint', direct, nadj@z0+response, 2e-10)
    assert np.max(np.abs(by_body[:, :, 0].sum(axis=1)))>.001
    assert np.max(np.abs(by_body[:, :, 1].sum(axis=1)))>.001
    checks.append({'name':'clock_and_force_both_present', 'max_force':float(np.max(np.abs(by_body[:, :, 0].sum(axis=1)))), 'max_direct_clock':float(np.max(np.abs(by_body[:, :, 1].sum(axis=1))))})
    nuisance = np.column_stack([np.ones(nobs), (taus[:-1]+taus[1:])/2])
    design = np.column_stack([n, nuisance])
    contrast = null_space(design.T, rcond=1e-13)
    assert contrast.shape[1]>=nobs-design.shape[1]
    close('full_orbital_clock_initial_state_annihilation', contrast.T@n, np.zeros((contrast.shape[1], 14)), 1e-11)
    close('instrument_nuisance_annihilation', contrast.T@nuisance, np.zeros((contrast.shape[1], 2)), 1e-11)
    close('contrast_measurements_equal_joint_field_response', contrast.T@direct, contrast.T@response, 2e-10)
    def constant_rhs(s, zz):
        l, _ = linear(s)
        f = np.zeros(14)
        f[6] = geo.ALPHA*geo.lapse(s, 0)
        f[13] = geo.ALPHA*geo.lapse(s, 1)
        return l@zz+f
    unit = solve_ivp(constant_rhs, (START, END), np.zeros(14), method='DOP853', rtol=3e-12, atol=3e-14, dense_output=True)
    assert unit.success
    constant_direct = sum(q@unit.sol(s) for s, q in atoms.items())
    close('constant_background_column_forward_vs_adjoint', constant_response, constant_direct, 2e-10)
    old_constant_response = float(np.max(np.abs(contrast.T@constant_response)))
    assert old_constant_response>1e-9, old_constant_response
    checks.append({'name':'initial_state_and_nuisance_do_not_automatically_remove_constant', 'response':old_constant_response})
    quotient_design = np.column_stack([design, constant_response])
    quotient_contrast = null_space(quotient_design.T, rcond=1e-13)
    assert quotient_contrast.shape[1]>0
    close('derived_constant_offset_column_annihilation', quotient_contrast.T@constant_direct, np.zeros(quotient_contrast.shape[1]), 2e-10)
    close('quotient_initial_state_annihilation', quotient_contrast.T@n, np.zeros((quotient_contrast.shape[1], 14)), 1e-11)
    close('quotient_instrument_nuisance_annihilation', quotient_contrast.T@nuisance, np.zeros((quotient_contrast.shape[1], 2)), 1e-11)
    close('quotient_observed_counts_equal_joint_field_response', quotient_contrast.T@direct, quotient_contrast.T@response, 2e-10)
    for body in [0, 1]:
        off = 7*body
        jump = max(np.max(np.abs(q[:, off+3:off+6])) for _, q in jumps)
        assert jump == 0
        checks.append({'name':f'position_clock_atoms_have_no_force_weight_jump_body_{body}', 'max_velocity_projection':float(jump)})
        close(f'initial_contrast_force_trace_body_{body}', contrast.T@nadj[:, off+3:off+6], np.zeros((contrast.shape[1], 3)), 1e-11)
        close(f'final_force_trace_body_{body}', segments[-1][2](END).reshape(nobs, 14)[:, off+3:off+6], np.zeros((nobs, 3)), 1e-14)
    # Original physical nonlinear paths and clocks, with receiver proper times fixed.
    convergence = []
    for eps in [.004, .002, .001]:
        yp = nonlinear_counts(nonlinear(eps, z0), samples, taus)
        ym = nonlinear_counts(nonlinear(-eps, z0), samples, taus)
        deriv = (yp-ym)/(2*eps)
        err = float(np.max(np.abs(deriv-direct)))
        convergence.append({'eps':eps, 'max_count_error':err})
    assert convergence[-1]['max_count_error']<5e-7, convergence
    checks.append({'name':'nonlinear_null_clock_orbit_to_linear_count', 'max_error':convergence[-1]['max_count_error']})
    for i in range(2):
        ratio = convergence[i]['max_count_error']/convergence[i+1]['max_count_error']
        assert 3.7<ratio<4.3, (i, ratio, convergence)
        checks.append({'name':f'nonlinear_count_second_order_{i}', 'ratio':ratio})
    wrong = nadj@z0+by_body[:, :, 0].sum(axis=1)
    err = float(np.max(np.abs(direct-wrong)))
    assert err>.001
    checks.append({'name':'reject_omitted_direct_clock_source', 'count_error':err})
    result = {
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'helper_sha256':hashlib.sha256(HELPER.read_bytes()).hexdigest(),
              'checks_passed':len(checks), 'checks':checks,
              'observation_count':nobs, 'initial_state_dimension':14,
              'nuisance_columns':2, 'contrast_dimension':contrast.shape[1],
              'design_singular_values':np.linalg.svd(design, compute_uv=False).tolist(),
              'rank_rcond':1e-13, 'quotient_contrast_dimension':quotient_contrast.shape[1],
              'constant_background_response':constant_response.tolist(),
              'quotient_design_singular_values':np.linalg.svd(quotient_design, compute_uv=False).tolist(),
              'nonlinear_convergence':convergence,
              'direct_count_variation':direct.tolist(), 'force_clock_contributions':by_body.tolist(),
              'scope':'Supplied synthetic two-body external dynamics, conformal flat metric, analytic massless plane-wave probes, one-way constant-proper-frequency source. No actual orbit or observations fit; plane waves do not have finite global energy. Floating nullspace experiment, not a certified exact rank or a nonlinear uniform remainder bound. The theorem states exact contrast conditions separately.'}
    return result


if __name__ == '__main__':
    print(json.dumps(run_checks(), indent=2))
