#!/usr/bin/env python3
"""Frozen scalar vacuum clock controls; all reported channels are conditional."""
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path
import hashlib
import json
import math
import sys

import mpmath as mp
import numpy as np
from scipy.integrate import quad
from scipy.linalg import expm
from scipy.special import exp1, erf

ROOT = Path(__file__).resolve().parent
mp.mp.dps = 55


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


@lru_cache(maxsize=None)
def F(x):
    z = mp.mpf(str(x))
    return z*z/4*mp.hyper([1, 1], [mp.mpf('1.5'), 2], -z*z/4)


def dawson(z):
    return mp.sqrt(mp.pi)/2*mp.exp(-z*z)*mp.erfi(z)


def H(x):
    z = mp.mpf(str(x))
    return z*F(x)-z+2*dawson(z/2)


def J(d):
    z = mp.mpf(str(d))
    return F(d)-1+2*dawson(z/2)/z if z else mp.mpf(0)


def D(x, d):
    xx, dd = mp.mpf(str(x)), mp.mpf(str(d))
    if not dd:
        return mp.mpf(0)
    return F(x)+J(d)-(H(str(xx+dd))-H(str(xx-dd)))/(2*dd)


def temporal(u, x, echo):
    if echo:
        # Integrate the two half intervals with opposite signs.
        return (2*np.expm1(1j*u*x/2)-np.expm1(1j*u*x))/(1j*u)
    return np.expm1(1j*u*x)/(1j*u)


def direct_channel(x, d, echo=False, nrad=384, nangle=64):
    t, w = np.polynomial.legendre.leggauss(nrad)
    u, wr = 6*(t+1), 6*w
    z, wz = np.polynomial.legendre.leggauss(nangle)
    # Actual two-center phase difference, with no analytic sinc inserted.
    form = (4*np.sin(.5*d*u[:, None]*z[None, :])**2)@(wz/2)
    Y = temporal(u, x, echo)
    return float(.5*np.sum(wr*u*np.exp(-u*u)*abs(Y)**2*form))


def numerical_grid():
    times, distances = [.1, .5, 1., 2., 5., 10., 30.], [0., .1, .5, 1., 2., 5., 10.]
    rows = []
    max_abs, max_fraction = 0., 0.
    for x in times:
        for d in distances:
            values = []
            for echo in [False, True]:
                direct = direct_channel(x, d, echo)
                analytic = 2*(4*D(str(mp.mpf(str(x))/2), d)-D(x, d)) if echo else 2*D(x, d)
                reference = float(analytic)
                error = abs(direct-reference)
                fraction = error/abs(reference) if reference else None
                assert error < 1e-10
                if reference:
                    assert fraction < 3e-9
                else:
                    assert direct == 0
                bound = (16 if echo else 4)*float(J(d))
                assert direct >= 0 and direct <= bound+1e-12
                max_abs, max_fraction = max(max_abs, error), max(max_fraction, fraction or 0)
                values.append(dict(echo=echo, chi_over_kappa_direct=direct,
                                   chi_over_kappa_closed=reference, absolute_error=error,
                                   fractional_error=fraction, analytic_all_time_bound=bound))
            rows.append(dict(x=x, d=d, channels=values))
    refinements = []
    for x, d in [(30., 10.), (.1, .1), (10., 1.)]:
        for echo in [False, True]:
            lo, hi = direct_channel(x, d, echo, 192, 32), direct_channel(x, d, echo)
            err = abs(lo-hi)/hi
            assert err < 4e-10
            refinements.append(dict(x=x, d=d, echo=echo, fractional_change=err))
    singles = []
    for x in times:
        direct, err = quad(lambda u:np.exp(-u*u)*2*np.sin(x*u/2)**2/u if u else 0,
                           0, 12, epsabs=2e-13, epsrel=2e-13, limit=300)
        exact = float(F(x))
        assert abs(direct-exact) < 5e-12
        singles.append(dict(x=x, direct=direct, closed=exact, quadrature_error=err))
    return dict(pair_rows=rows, single_rows=singles, refinements=refinements,
                max_pair_absolute_error=max_abs, max_pair_fractional_error=max_fraction,
                radial_tail_bound_for_all_rows=900*math.exp(-144),
                tail_bound_reason='|Y|<=x<=30; angular form<=4; radial tail x^2 exp(-12^2).')


def plateau_and_static():
    rows = []
    for d in [.1, .5, 1., 2., 5., 10., 30.]:
        value, err = quad(lambda u:np.exp(-u*u)*(1-np.sinc(d*u/np.pi))/u if u else 0,
                           0, 12, epsabs=2e-13, epsrel=2e-13, limit=300)
        closed = float(J(d))
        upper = min(d*d/12, 1/12+float(exp1(1/(d*d))))
        assert abs(value-closed) < 6e-12 and 0 <= closed <= upper
        # Same spatial smearing in the static inverse-Laplacian kernel.
        static, static_err = quad(lambda u:np.exp(-u*u)*np.sinc(d*u/np.pi),
                                 0, 12, epsabs=2e-13, epsrel=2e-13, limit=300)
        static *= 2/math.pi
        static_closed = float(erf(d/2)/d)
        assert abs(static-static_closed) < 4e-13
        # Large time at fixed distance approaches the plateau from this exact formula.
        asymptotic_rows = []
        for x in [100., 300., 1000.]:
            normalized = float(2*D(x, d))
            echo = float(2*(4*D(x/2, d)-D(x, d)))
            asymptotic_rows.append(dict(x=x, ramsey=normalized, echo=echo,
                                       ramsey_plateau=2*closed, echo_plateau=6*closed))
        assert abs(asymptotic_rows[-1]['ramsey']/(2*closed)-1) < .001
        assert abs(asymptotic_rows[-1]['echo']/(6*closed)-1) < .005
        rows.append(dict(d=d, J_direct=value, J_closed=closed, J_upper=upper,
                         J_quad_estimate=err, static_direct=static,
                         static_closed=static_closed, static_quad_estimate=static_err,
                         late_time_rows=asymptotic_rows))
    return rows


def finite_oscillators():
    rows = []
    g = .2
    for dim in [16, 24]:
        a = np.diag(np.sqrt(np.arange(1, dim)), 1)
        vac = np.eye(dim, dtype=complex)[:, 0]
        for omega in [.7, 1.3]:
            h0 = omega*a.T@a
            hp, hm = h0+g*(a+a.T)/2, h0-g*(a+a.T)/2
            for T in [.1, 1., 3., 6.]:
                for echo in [False, True]:
                    if echo:
                        plus = expm(-1j*hm*T/2)@expm(-1j*hp*T/2)@vac
                        minus = expm(-1j*hp*T/2)@expm(-1j*hm*T/2)@vac
                    else:
                        plus, minus = expm(-1j*hp*T)@vac, expm(-1j*hm*T)@vac
                    visibility = abs(np.vdot(minus, plus))
                    Y = temporal(np.array([omega]), T, echo)[0]
                    chi = .5*g*g*abs(Y)**2
                    predicted = math.exp(-chi)
                    error = abs(visibility-predicted)
                    assert error < 2e-12
                    rows.append(dict(dim=dim, omega=omega, T=T, echo=echo,
                                     direct_visibility=float(visibility), predicted=predicted,
                                     absolute_error=float(error), top_level_population=float(abs(plus[-1])**2)))
    return rows


def si_grid():
    G, h, c, fraction = 6.67430e-11, 6.62607015e-34, 299792458., 1/2500
    rows = []
    for nu in [1e9, 1e14, 1e15]:
        kappa = 2*G*h*fraction*nu*nu/c**5
        # Independent dimensional rewrite using hbar and angular frequency.
        second = G*fraction*(h/(2*math.pi))*(2*math.pi*nu)**2/(math.pi*c**5)
        assert abs(kappa/second-1) < 3e-15
        for ell in [1e-9, 1e-6, 1e-3]:
            for L in [1e-2, 1., 1e3]:
                d = L/ell
                upper = min(d*d/12, 1/12+float(exp1(1/(d*d))))
                rows.append(dict(nu_Hz=nu, width_m=ell, separation_m=L, d=d, kappa=kappa,
                                 J_analytic_upper=upper,
                                 all_time_Ramsey_chi_upper=4*kappa*upper,
                                 all_time_echo_chi_upper=16*kappa*upper))
    return dict(constants=dict(G_N=G, G_N_reported_standard_uncertainty=1.5e-15,
                               h_exact=h, c_exact=c, supplied_scalar_fraction_upper=fraction),
                rows=rows, max_Ramsey_upper=max(r['all_time_Ramsey_chi_upper'] for r in rows),
                max_echo_upper=max(r['all_time_echo_chi_upper'] for r in rows),
                empirical_or_confidence_bound=False)


def main():
    output = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                  source_sha256={n:sha(ROOT/n) for n in ['PROTOCOL.md','DIRECT_SCALAR_CLOCK_LINK.md','check_scalar_clock_link.py']},
                  grid=numerical_grid(), plateau=plateau_and_static(),
                  finite_oscillator_rows=finite_oscillators(), illustrative_SI=si_grid(),
                  scope='Scalar-only linear Gaussian vacuum and supplied logical clock sources/readout; no total gravitational decoherence or actual clock likelihood.')
    summary = dict(pair_geometries=len(output['grid']['pair_rows']),
                   channels=2*len(output['grid']['pair_rows']),
                   max_pair_fractional_error=output['grid']['max_pair_fractional_error'],
                   max_pair_absolute_error=output['grid']['max_pair_absolute_error'],
                   finite_oscillator_controls=len(output['finite_oscillator_rows']),
                   max_oscillator_visibility_error=max(r['absolute_error'] for r in output['finite_oscillator_rows']),
                   max_illustrative_Ramsey_bound=output['illustrative_SI']['max_Ramsey_upper'],
                   max_illustrative_echo_bound=output['illustrative_SI']['max_echo_upper'])
    output['summary'] = summary
    dest = Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'evidence_v1/RESULTS.json'
    dest.parent.mkdir(exist_ok=True)
    assert not dest.exists(), 'Preserve historical outputs; use a new version path.'
    dest.write_text(json.dumps(output, indent=2, allow_nan=False)+'\n')
    print(json.dumps(summary, sort_keys=True))


if __name__ == '__main__':
    main()
