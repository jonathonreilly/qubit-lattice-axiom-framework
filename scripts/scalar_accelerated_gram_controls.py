"""Author controls: original wave amplitudes versus derived arrival-time Gram.

Synthetic dimensionless fixtures only, anchored massless energy completion.
Finite quadrature comparisons are diagnostics, not certified error enclosures.
"""
AUDIT_TIMEOUT_SEC = 180

from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import numpy as np
from numpy.polynomial.legendre import leggauss


def quad(n, lo=-1., hi=1.):
    x, w = leggauss(n)
    return lo + (x+1)*(hi-lo)/2, w*(hi-lo)/2


def angular(nz, nphi):
    z, wz = leggauss(nz)
    ph = 2*np.pi*np.arange(nphi)/nphi
    ns = np.stack(np.broadcast_arrays(np.sqrt(1-z*z)[:, None]*np.cos(ph),
                  np.sqrt(1-z*z)[:, None]*np.sin(ph), z[:, None]), axis=-1)
    return ns.reshape(-1, 3), np.repeat(wz*2*np.pi/nphi, nphi)


def path(s, mode='curved'):
    s = np.asarray(s)
    if mode == 'rest':
        return (np.zeros(s.shape+(3,)),)*3
    if mode == 'inertial':
        u = np.broadcast_to([.13, -.07, .24], s.shape+(3,))
        return s[..., None]*u, u, np.zeros_like(u)
    x = np.stack([.08*np.sin(2*s), .06*np.sin(3*s)+.02*s,
                  .13*s+.02*np.cos(4*s)], axis=-1)
    u = np.stack([.16*np.cos(2*s), .18*np.cos(3*s)+.02,
                  .13-.08*np.sin(4*s)], axis=-1)
    a = np.stack([-.32*np.sin(2*s), -.54*np.sin(3*s),
                  -.32*np.cos(4*s)], axis=-1)
    return x, u, a


def windows(s, channel=0):
    """Two nonparallel vector windows and two signed direct field weights."""
    s = np.asarray(s)
    w = np.maximum(1-s*s, 0.)**4
    wp = np.where(np.abs(s)<1, -8*s*(1-s*s)**3, 0.)
    if channel == 0:
        v = np.array([1., .2, -.1])+s[..., None]*np.array([.3, -.4, .6])
        vp = np.broadcast_to([.3, -.4, .6], v.shape)
        c = w*(.7+.4*s)
    else:
        v = np.array([-.2, .5, .3])+s[..., None]**2*np.array([.1, .2, .4])
        vp = 2*s[..., None]*np.array([.1, .2, .4])
        c = w*(-.4+.3*s+.2*s*s)
    return c, w[..., None]*v, wp[..., None]*v+w[..., None]*vp


def density(s, n, channel, mode, omit_acceleration=False, reverse_cross=False):
    _, u, a = path(s, mode)
    c, w, wp = windows(s, channel)
    d = 1-u@n
    aa = 1-np.sum(u*u, axis=-1)
    b = aa[..., None]*(n-u)/d[..., None]
    bp = (-2*np.sum(u*a, axis=-1)[..., None]*(n-u)/d[..., None]
          -aa[..., None]*a/d[..., None]
          +aa[..., None]*(n-u)*(a@n)[..., None]/d[..., None]**2)
    derivative = np.sum(b*wp, axis=-1)
    if not omit_acceleration:
        derivative += np.sum(bp*w, axis=-1)
    sign = 1 if reverse_cross else -1
    return c+sign*derivative, d


def time_gram(mode, nt=180, nz=12, nphi=24, **options):
    s, sw = quad(nt)
    ns, nw = angular(nz, nphi)
    result = np.zeros((2, 2))
    for n, aw in zip(ns, nw):
        h = np.array([density(s, n, i, mode, **options)[0] for i in range(2)])
        d = density(s, n, 0, mode)[1]
        result += aw * (h*(sw/d))@h.T
    return result/(8*np.pi*np.pi)


def wave_gram(mode, cutoff=120., nt=360, nk=260, nz=12, nphi=24,
              offsets=None, factors=None):
    s, sw = quad(nt)
    k, kw = quad(nk, 0., cutoff)
    ns, nw = angular(nz, nphi)
    x, u, _ = path(s, mode)
    aa = 1-np.sum(u*u, axis=-1)
    cs = np.array([windows(s, i)[0] for i in range(2)])
    ws = np.array([windows(s, i)[1] for i in range(2)])
    if offsets is None:
        offsets, factors = [np.zeros(3)], [np.ones(2)]
    result = np.zeros((2, 2))
    for n, aw in zip(ns, nw):
        phase = np.exp(1j*k[:, None]*(s-x@n)[None, :])
        force = aa[None, :]*np.einsum('itj,tj->it', ws, n-u)
        direct = (cs*sw)@phase.T
        acceleration = 1j*k[None, :]*((force*sw)@phase.T)
        amplitude = np.zeros_like(direct)
        for offset, factor in zip(offsets, factors):
            amplitude += np.asarray(factor)[:, None]*(direct+acceleration)*np.exp(-1j*k*(n@offset))
        result += aw*np.real((amplitude*kw)@amplitude.conj().T)
    return result/(2*np.pi)**3


def arrival_gram(offsets, factors, mode='curved', nt=180, nz=12, nphi=24,
                 independent_paths=False, equal_coordinate=False):
    ns, nw = angular(nz, nphi)
    total = np.zeros((2, 2))
    for n, aw in zip(ns, nw):
        endpoints = []
        for off in offsets:
            ss = np.array([-1., 1.])
            xx, _, _ = path(ss, mode)
            endpoints += list(ss-(xx+off)@n)
        breaks = np.unique(endpoints)
        for lo, hi in zip(breaks[:-1], breaks[1:]):
            tau, tw = quad(nt, lo, hi)
            pieces = []
            for off, factor in zip(offsets, factors):
                if equal_coordinate:
                    off = np.zeros(3)
                ss = np.clip(tau+n@off, -1., 1.)
                for _ in range(9):
                    xx, uu, _ = path(ss, mode)
                    ss -= (ss-(xx+off)@n-tau)/(1-uu@n)
                active = np.abs(ss)<1
                hh = np.zeros((2, len(tau)))
                for i in range(2):
                    h, d = density(ss[active], n, i, mode)
                    hh[i, active] = factor[i]*h/d
                pieces.append(hh)
            if independent_paths:
                total += aw*sum((h*tw)@h.T for h in pieces)
            else:
                h = sum(pieces)
                total += aw*(h*tw)@h.T
    return total/(8*np.pi*np.pi)


def run_checks():
    checks = []
    values = {}
    def close(name, got, expected, tol):
        err = float(np.max(np.abs(got-expected)))
        assert err<tol, (name, err, tol, got, expected)
        checks.append({'name':name, 'max_absolute_error':err, 'tolerance':tol})
    for mode in ['rest', 'inertial', 'curved']:
        tm = time_gram(mode)
        wave = wave_gram(mode)
        values[mode] = {'time_gram':tm.tolist(), 'original_wave_gram_k120':wave.tolist()}
        close(mode+'_original_wave_vs_time', wave, tm, 2e-8)
        assert np.linalg.eigvalsh(tm).min()>0
        checks.append({'name':mode+'_positive_definite_fixture', 'minimum_eigenvalue':float(np.linalg.eigvalsh(tm).min())})
    refined = time_gram('curved', nt=260, nz=18, nphi=36)
    close('curved_time_angular_refinement', refined, np.array(values['curved']['time_gram']), 1e-12)
    wave_refined = wave_gram('curved', cutoff=180, nt=480, nk=360, nz=12, nphi=24)
    close('curved_original_wave_cutoff_refinement', wave_refined, refined, 2e-9)
    s, sw = quad(100)
    rest = np.empty((2, 2))
    for i in range(2):
        ci, _, wi = windows(s, i)
        for j in range(2):
            cj, _, wj = windows(s, j)
            rest[i, j] = sw@(ci*cj)/(2*np.pi)+sw@np.sum(wi*wj, axis=-1)/(6*np.pi)
    close('stationary_closed_reduction', np.array(values['rest']['time_gram']), rest, 1e-13)
    for label, options in [('reverse_clock_force_sign', {'reverse_cross':True}),
                            ('omit_acceleration_derivative', {'omit_acceleration':True})]:
        bad = time_gram('curved', **options)
        err = float(np.max(np.abs(bad-refined)))
        assert err>1e-3, (label, err)
        checks.append({'name':'reject_'+label, 'max_gram_discrepancy':err})
        values[label] = bad.tolist()
    offsets = [np.zeros(3), np.array([.64, -.29, .21])]
    factors = [np.ones(2), np.array([.7, -.6])]
    arrival = arrival_gram(offsets, factors, nz=18, nphi=36)
    direct = wave_gram('curved', offsets=offsets, factors=factors, nz=18, nphi=36)
    close('separated_paths_common_phase_vs_original_wave', arrival, direct, 3e-8)
    ar2 = arrival_gram(offsets, factors, nt=240, nz=24, nphi=48)
    close('separated_paths_refinement', ar2, arrival, 3e-10)
    for name, opts in [('independent_path_budgets', {'independent_paths':True}),
                       ('equal_coordinate_cross_terms', {'equal_coordinate':True})]:
        wrong = arrival_gram(offsets, factors, **opts)
        err = float(np.max(np.abs(wrong-arrival)))
        assert err>.01, (name, err)
        checks.append({'name':'reject_'+name, 'max_gram_discrepancy':err})
        values[name] = wrong.tolist()
    values['two_paths'] = {'common_phase_gram':arrival.tolist(), 'original_wave_gram':direct.tolist(),
                          'offsets':[o.tolist() for o in offsets], 'factors':[f.tolist() for f in factors]}
    result = {'check_context':'author controls, focused independent evidence separate',

              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'checks_passed':len(checks), 'checks':checks, 'values':values,
              'scope':'Anchored free massless field, prescribed synthetic timelike paths and smooth compact windows. No archive sample, observation fit, independent empirical test, massive field claim, or certified quadrature enclosure.'}
    return result


if __name__ == '__main__':
    print(json.dumps(run_checks(), indent=2))
