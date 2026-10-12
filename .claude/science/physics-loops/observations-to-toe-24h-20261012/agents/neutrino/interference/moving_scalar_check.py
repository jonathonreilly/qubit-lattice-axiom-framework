#!/usr/bin/env python3
"""Conditional closed-current vacuum envelope and explicit Markov rival.

No raw Fein2019 fit or apparatus-specific vacuum exclusion is performed.
All input/selection roles are recorded in FROZEN_PROTOCOL.md.
"""
import os
for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[name] = "1"

from pathlib import Path
import hashlib
import json
import platform
import time
import numpy as np
import scipy
from scipy.constants import G, h, hbar, c, physical_constants
from scipy.integrate import quad
from scipy.special import erf, exp1, gamma, roots_genlaguerre
from numpy.polynomial.legendre import leggauss

CAMPAIGN = Path("/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012")
OUT = CAMPAIGN / "neutrino/interference"
M_U = physical_constants["atomic mass constant"][0]
MASS_DA = 26777.
MASS_KG = MASS_DA*M_U
L = .98
D = 266e-9
V = 261.
ALPHA = 1.


def check_stop():
    for name in ("STOP_REQUESTED", "USER_STOP_REQUESTED"):
        if (CAMPAIGN/name).exists():
            raise SystemExit(name)
    if time.time() >= json.loads((CAMPAIGN/"DEADLINE.json").read_text())["deadline_epoch"]:
        raise SystemExit("Deadline reached")


def moving_amplitude(k, mu, u, duration, separation, drift=0., direction_z=0.):
    """D=integral ds exp(i omega s)*(exp(-i kx X+)-exp(-i kx X-)).

    s has length units. Branches start together, separate symmetrically and
    reunite, with constant speeds b=separation/duration on the two legs.
    This is the specified Hamiltonian current amplitude; no COM approximation
    has yet replaced it by a stationary separation.
    """
    omega = np.sqrt(k*k + mu*mu)
    b = separation/duration
    K = k*u*b
    doppler = omega-k*direction_z*drift
    den = doppler*doppler-K*K
    aa, bb = k*u*separation/2, doppler*duration/2
    cosine_difference = -2*np.sin((aa+bb)/2)*np.sin((aa-bb)/2)
    return -4j*K*np.exp(1j*doppler*duration/2)*cosine_difference/den


def direct_amplitude(k, mu, u, duration, separation, drift=0., direction_z=0.):
    omega = np.hypot(k, mu)
    b = separation/duration
    def integrand(s):
        x = b*min(s, duration-s)
        return np.exp(1j*(omega-k*direction_z*drift)*s)*(-2j*np.sin(k*u*x))
    value = 0j
    error = 0.
    for lo, hi in ((0, duration/2), (duration/2, duration)):
        re, e1 = quad(lambda s: integrand(s).real, lo, hi, epsabs=2e-13, epsrel=2e-13)
        im, e2 = quad(lambda s: integrand(s).imag, lo, hi, epsabs=2e-13, epsrel=2e-13)
        value += re+1j*im
        error += e1+e2
    return value, error


def envelope(g2, duration, separation, width, drift=0.):
    """Upper bound valid for every nonnegative unit-total mass measure.

    Uses |F_internal(k)| <= exp(-width^2*k^2/2), fixed rigid profile,
    and b<1. The proper-time current multiplier <=1 can only lower it.
    """
    b = separation/duration
    A = (1-abs(drift))**2-b*b
    assert 0 <= b < 1 and width > 0 and A > 0
    z = 16*width**2/(duration**2*A)
    return 2*g2*b*b/(3*np.pi**2*A*A)*(1+2*exp1(z))


def continuum_integral(shape, ell, width, duration, separation, order):
    # Natural-length units; q=1. This is a numerical source-current example,
    # not a set of physical parameters fitted to molecular data.
    nr, nk, nu = order
    mass_nodes, mass_weights = roots_genlaguerre(nr, shape-1)
    masses = mass_nodes/ell
    mass_weights = mass_weights/gamma(shape)
    nodes, weights = leggauss(nk)
    kmax = 10/width
    ks, kw = (nodes+1)*kmax/2, weights*kmax/2
    angles, aw = leggauss(nu)
    total = 0.
    for k, wk in zip(ks, kw):
        omega = np.sqrt(k*k+masses*masses)
        amplitude = moving_amplitude(k, masses[:, None], angles[None, :], duration, separation)
        angular = (abs(amplitude)**2) @ aw
        total += wk*k*k*np.exp(-width*width*k*k)*np.dot(mass_weights, angular/omega)
    return float(total/(16*np.pi**2))


def csl_fraction(separation, r_c):
    z = separation/(2*r_c)
    if abs(z) < .001:
        return z*z/3-z**4/10+z**6/42
    return 1-np.sqrt(np.pi)*erf(z)/(2*z)


def main():
    check_stop()
    started = time.time()
    OUT.mkdir(exist_ok=True, parents=True)
    total_time = 2*L/V
    duration = c*total_time
    separation = h*L/(MASS_KG*V*D)
    g2 = 4*np.pi*G/(hbar*c)*ALPHA**2*MASS_KG**2
    b = separation/duration
    planck_l2 = hbar*G/c**3
    cancelled = 4*np.pi**3*ALPHA**2*planck_l2/D**2
    assert np.isclose(g2*b*b, cancelled, rtol=2e-15, atol=0)

    probes=[]
    for k, mu, u, drift, nz in ((.2,0.,.4,0.,0.), (1.,.3,-.7,0.,0.),
                                (5.,2.,.8,0.,0.), (12.,.1,.3,.3,.7), (2.,.7,0.,0.,0.)):
        exact = moving_amplitude(k, mu, u, 1., .2, drift, nz)
        direct, err = direct_amplitude(k, mu, u, 1., .2, drift, nz)
        assert abs(exact-direct) < 2e-13
        omega=np.hypot(k,mu)-k*nz*drift;K=k*u*.2
        # The two pointwise inequalities that yield the integrated bound.
        small_bound=abs(K)/2
        large_bound=8*abs(K)/(omega**2-K**2)
        assert abs(exact) <= min(small_bound,large_bound)+1e-13
        probes.append(dict(k=k,mu=mu,u=u,drift=drift,direction_z=nz,closed=[float(exact.real),float(exact.imag)],
                           direct=[float(direct.real),float(direct.imag)],absolute_error=abs(exact-direct),quad_error=err))

    synthetic=[]
    for shape,ell in ((1.,1.),(3.,.7)):
        low=continuum_integral(shape,ell,.1,1.,.2,(48,256,32))
        high=continuum_integral(shape,ell,.1,1.,.2,(96,512,64))
        bound=envelope(1.,1.,.2,.1)
        assert 0<=high<=bound and abs(low-high)<3e-9
        synthetic.append(dict(shape=shape,ell=ell,width=.1,duration=1.,separation=.2,
                              coarse_chi_per_g2=low,fine_chi_per_g2=high,
                              resolution_difference=abs(high-low),positive_measure_envelope=bound,
                              source_model="declared noncovariant smeared Hamiltonian current for numerical validation"))

    vacuum_rows=[]
    for width in (1e-15,1e-10,1e-9,1e-8):
        bound=envelope(g2,duration,separation,width,V/c)
        vacuum_rows.append(dict(gaussian_width_m=width,chi_upper=bound,
             visibility_loss_upper=bound,includes_longitudinal_doppler_envelope=True))

    rival=[]
    for r_c in (1e-8,1e-7,1e-6):
        fraction=csl_fraction(separation,r_c)
        exposure=MASS_DA**2*total_time*fraction
        direct,qe=quad(lambda t: 1-np.exp(-(h/(MASS_KG*D)*min(t,total_time-t))**2/(4*r_c*r_c)),0,total_time,
                       points=[total_time/2],epsabs=1e-15,epsrel=1e-12)
        assert abs(direct-total_time*fraction)<1e-14
        rival.append(dict(r_c_m=r_c,localization_fraction=fraction,exposure_seconds=exposure,
                          visibility_at_lambda_1e_minus8=np.exp(-1e-8*exposure),
                          visibility_at_lambda_1e_minus16=np.exp(-1e-16*exposure),
                          modal_benchmark_lambda_for_half_visibility=np.log(2)/exposure,
                          modal_benchmark_lambda_for_scale_0_87=-np.log(.87)/exposure))

    # These are declared summary-only algebraic scenarios, not confidence results.
    summary=[]
    for z in (1.,1.96):
        lower=.93-z*.06
        summary.append(dict(z=z,assumed_scale_lower=lower,common_extra_exponent_upper=-np.log(lower),
           status="only if quoted scale uncertainty is Gaussian, complete and calibrated, with independent nonenhancing background factor"))

    outputs=dict(status="conditional moving-current calculation, not a Fein2019 apparatus prediction or new exclusion",
       software=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
       constants=dict(G_SI=G,h_SI=h,hbar_SI=hbar,c_SI=c,atomic_mass_kg=M_U),
       benchmark=dict(mass_Da=MASS_DA,mass_kg=MASS_KG,grating_separation_m=L,period_m=D,velocity_m_s=V,
                      total_flight_time_s=total_time,natural_time_length_m=duration,
                      triangular_relative_separation_m=separation,branch_transverse_speed_over_c=b,
                      longitudinal_speed_over_c=V/c,g_squared=g2,alpha=ALPHA,
                      g2_b2=g2*b*b,planck_length_identity=cancelled),
       direct_time_checks=probes,synthetic_continuum_checks=synthetic,
       vacuum_envelopes=vacuum_rows,markov_rival=rival,summary_scenarios=summary,
       runtime_seconds=time.time()-started)
    (OUT/'moving_scalar_results.json').write_text(json.dumps(outputs,indent=2)+'\n')
    print(json.dumps(outputs,indent=2))
    print('PASS: direct/closed time amplitudes, pointwise envelope, continuum resolution, mass cancellation and Markov time integral checks.')


if __name__=='__main__':
    main()
