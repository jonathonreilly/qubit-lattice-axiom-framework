#!/usr/bin/env python3
"""Independent operators for a conditional finite-source gravity inverse.

Synthetic numerical controls only. No measured Doppler residuals or likelihood.
The analytic proof/domain is in the paired finite-range orbit/light-time note.
No external scientific files are read at execution; declared inputs bind the
mathematical premises and note. The sole write is the requested result file.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
from scipy.optimize import brentq

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    "docs/EXPONENTIAL_SCALAR_ORBIT_LIGHT_TIME_BOUNDED_THEOREM_NOTE_2026-10-14.md",
    "docs/EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md",
    "docs/EXPONENTIAL_SCALAR_COMPOSITE_CHARGE_BOUNDED_THEOREM_NOTE_2026-10-14.md",
]


def h(x):
    return (1.0 + x) * np.exp(-x)


def log_interval(mu, a, b):
    """Log integral_a^b s exp(-mu*s) ds, avoiding common exponential loss."""
    if mu * b < 0.05:
        return math.log(quad(lambda s: s * math.exp(-mu*s), a, b,
                             epsabs=1e-13, epsrel=1e-13)[0])
    d = mu * (b-a)
    bracket = (1+mu*a) * (-math.expm1(-d)) - d*math.exp(-d)
    return -mu*a + math.log(bracket) - 2*math.log(mu)


def log_ratio(mu, radii):
    a, b, c = radii
    return log_interval(mu, a, b) - log_interval(mu, b, c)


def invert_ratio(ratio, radii):
    target = math.log(ratio)
    if target <= log_ratio(0.0, radii):
        raise ValueError("ratio does not exceed the positive-mass boundary")
    hi = 1.0 / radii[-1]
    while log_ratio(hi, radii) < target:
        hi *= 2.0
    return brentq(lambda m: log_ratio(m, radii)-target, 0, hi,
                  xtol=2e-13, rtol=2e-13)


def invert_three(K, radii):
    d12, d23 = K[0]-K[1], K[1]-K[2]
    if min(d12, d23) <= 0:
        raise ValueError("strictly positive resolved differences required")
    mu = invert_ratio(d12/d23, radii)
    B = d12 / (h(mu*radii[0])-h(mu*radii[1]))
    M0 = K[0] - B*h(mu*radii[0])
    return float(mu), float(M0), float(B)


def mass_interval(Khat, eps, radii):
    d12, d23 = Khat[0]-Khat[1], Khat[1]-Khat[2]
    e12, e23 = eps[0]+eps[1], eps[1]+eps[2]
    if d12 <= e12 or d23 <= e23:
        return None
    lower, upper = (d12-e12)/(d23+e23), (d12+e12)/(d23-e23)
    boundary = math.exp(log_ratio(0, radii))
    if lower <= boundary:
        return None
    return invert_ratio(lower, radii), invert_ratio(upper, radii)


def profile_green(n, pressure, mu, radius, order=96):
    """Direct radial/angular integration of stress-trace Green potential/force.

    R=1; rho=(1-s^2)^n; pr=p(1-s^2)^(n+2), pt=pr+s pr'/2.
    Finite-radius analytic charge enters only the comparison, not the force.
    """
    nodes, weights = leggauss(order)
    s, ws = (nodes+1)/2, weights/2
    rho = (1-s*s)**n
    pr = pressure*(1-s*s)**(n+2)
    prprime = -2*(n+2)*pressure*s*(1-s*s)**(n+1)
    trace = rho - 3*pr - s*prprime
    energy = 4*math.pi*np.sum(ws*s*s*rho)
    sm = mu*s
    f = np.sinh(sm)/sm if mu else np.ones_like(s)
    sfprime = np.cosh(sm)-f
    charge_trace = 4*math.pi*np.sum(ws*s*s*f*trace)/energy
    charge_virial = 4*math.pi*np.sum(ws*s*s*(f*rho+sfprime*pr))/energy
    dist = np.sqrt(radius**2+s[:,None]**2-2*radius*s[:,None]*nodes[None,:])
    kernel = np.exp(-mu*dist)/dist
    gradient = np.exp(-mu*dist)*(1+mu*dist)*(radius-s[:,None]*nodes[None,:])/dist**3
    measure = ws[:,None]*s[:,None]**2*weights[None,:]*trace[:,None]
    potential = 2*math.pi*np.sum(measure*kernel)/energy
    force = 2*math.pi*np.sum(measure*gradient)/energy
    return charge_trace, charge_virial, potential, force


def position(line,t):
    return np.asarray(line[0])+np.asarray(line[1])*t


def transfer(emitter,receiver,te,tr,mass):
    xe,xr=position(emitter,te),position(receiver,tr)
    re,rr=np.linalg.norm(xe),np.linalg.norm(xr)
    disp=xr-xe;D=np.linalg.norm(disp);S=re+rr;n=disp/D
    de,dr=-np.dot(n,emitter[1]),np.dot(n,receiver[1])
    se,sr=np.dot(xe,emitter[1])/re,np.dot(xr,receiver[1])/rr
    L=math.log((S+D)/(S-D))
    derivatives=[d+2*mass*2*(S*d-D*s)/(S*S-D*D) for d,s in [(de,se),(dr,sr)]]
    return D+2*mass*L,derivatives


def retarded_time(emitter,receiver,tr,mass):
    residual=lambda te: tr-te-transfer(emitter,receiver,te,tr,mass)[0]
    width=2*(1+np.linalg.norm(position(receiver,tr)-position(emitter,tr)))
    for _ in range(30):
        if residual(tr-width)>0:
            return brentq(residual,tr-width,tr,xtol=1e-13,rtol=1e-14)
        width*=2
    raise ValueError('no retarded bracket in declared search')


def events(lines,tr,mass):
    t2=retarded_time(lines[1],lines[2],tr,mass)
    t1=retarded_time(lines[0],lines[1],t2,mass)
    a,b=transfer(lines[0],lines[1],t1,t2,mass)[1]
    c,d=transfer(lines[1],lines[2],t2,tr,mass)[1]
    J=(1-b)/(1+a)*(1-d)/(1+c)
    return t1,t2,J


def clock_rate(line,t,mass,amplitude,mu):
    r=np.linalg.norm(position(line,t));v2=np.dot(line[1],line[1])
    psi=-mass*(1+amplitude*math.exp(-mu*r))/r
    phi=-mass*(1-amplitude*math.exp(-mu*r))/r
    return math.sqrt(1+2*psi-(1-2*phi)*v2)


def proper_time(line,t,mass,amplitude,mu):
    return quad(lambda s:clock_rate(line,s,mass,amplitude,mu),0,t,
                epsabs=1e-12,epsrel=1e-12)[0]


def coherent_phase_checks():
    rows=[]
    def check(name,condition,**evidence):rows.append(dict(name=name,passed=bool(condition),**evidence))
    emitter=((-4.,2.,0.),(.0,.012,.0))
    relay=((7.,1.5,.5),(.002,-.009,.001))
    other=((-3.,2.5,1.),(.001,.007,0.))
    static=tuple((line[0],(0.,0.,0.)) for line in [emitter,relay,emitter])
    for lines,tag in [(static,'static two-way'),((emitter,relay,emitter),'moving two-way'),((emitter,relay,other),'moving three-way')]:
        for tr in [1.,10.,50.]:
            mass=1e-4;amplitude=.3;mu=.4
            t1,t2,J=events(lines,tr,mass);dt=1e-3
            J_fd=(events(lines,tr+dt,mass)[0]-events(lines,tr-dt,mass)[0])/(2*dt)
            check('retarded_phase_jacobian',abs(J-J_fd)<2e-9 and t1<t2<tr,
                  geometry=tag,tr=tr,J=J,J_fd=J_fd,error=abs(J-J_fd))
            # Photon path geometry is checked directly for an exterior segment.
            for i,j,ti,tj in [(0,1,t1,t2),(1,2,t2,tr)]:
                x,y=position(lines[i],ti),position(lines[j],tj);d=y-x
                u=np.clip(-np.dot(x,d)/np.dot(d,d),0,1)
                assert np.linalg.norm(x+u*d)>.5
            for span in [.02,2.]:
                low,high=tr-span/2,tr+span/2;k=1.25;omega=7.;chirp=.03
                tau=lambda line,t:proper_time(line,t,mass,amplitude,mu)
                phase=lambda proper:omega*proper+chirp*proper*proper/2
                t1low=events(lines,low,mass)[0];t1high=events(lines,high,mass)[0]
                duration=tau(lines[2],high)-tau(lines[2],low)
                endpoint_count=k*(phase(tau(lines[0],t1high))-phase(tau(lines[0],t1low)))
                def arrival_count_rate(t):
                    te,_,jac=events(lines,t,mass)
                    return k*(omega+chirp*tau(lines[0],te))*clock_rate(lines[0],te,mass,amplitude,mu)*jac
                integral=quad(arrival_count_rate,low,high,epsabs=1e-10,epsrel=1e-12)[0]
                err=abs(endpoint_count-integral)/duration
                check('finite_proper_count',err<1e-9,geometry=tag,tr=tr,span=span,
                      mean_frequency=endpoint_count/duration,error_hz=err)
    # A stationary same-station coherent link has exact clock-ratio cancellation
    # in this prescribed metric. A moving same-station link is a distinct case.
    t1,t2,J=events(static,10,1e-4)
    ratio=clock_rate(static[0],t1,1e-4,.3,.4)/clock_rate(static[2],10,1e-4,.3,.4)
    check('static_endpoint_clock',abs(ratio-1)<1e-14 and abs(J-1)<1e-14,ratio=ratio)
    moving=(emitter,relay,emitter)
    te,_,jac=events(moving,10,1e-4)
    ys=[]
    for amplitude in [0,.3]:
        ys.append(clock_rate(emitter,te,1e-4,amplitude,.4)/clock_rate(emitter,10,1e-4,amplitude,.4)*jac)
    check('moving_scalar_clock_witness',abs(ys[1]-ys[0])>1e-9,
          scalar_endpoint_frequency_difference=ys[1]-ys[0],fixed_worldlines=True)
    return rows




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("outputs/exponential_scalar_orbit_light_time_results.json"))
    args = parser.parse_args()
    records = []

    def check(name, condition, **evidence):
        records.append(dict(name=name, passed=bool(condition), **evidence))

    # Three different source density profiles and complete conserved stress.
    # Direct angular Green integration is independent of exterior differentiation.
    for n,p,mu,r in itertools.product([0,1,2],[-0.3,0,0.3],[0,.01,.2,1,4],[1.3,2,6]):
        F,Fv,V,g = profile_green(n,p,mu,r)
        wantV, wantg = F*math.exp(-mu*r)/r, F*h(mu*r)/r**2
        error = max(abs(F-Fv),abs(V-wantV),abs(g-wantg))
        boundlo = 1 if mu == 0 else 2*math.sinh(mu)/mu-math.cosh(mu)
        boundhi = math.cosh(mu)
        check("extended_source",error<2e-11 and boundlo-1e-12<=F<=boundhi+1e-12,
              n=n,p=p,mu=mu,r=r,F=F,green_error=error)

    # Quadrature refinement on the closest and shortest-range geometry.
    lo = profile_green(2,-.3,4,1.3,48)
    hi = profile_green(2,-.3,4,1.3,144)
    check("green_refinement",max(abs(a-b) for a,b in zip(lo,hi))<2e-11,
          difference=max(abs(a-b) for a,b in zip(lo,hi)))

    # Light path integral: compare integration along the actual straight segment
    # against the finite-endpoint logarithm, for three exterior geometries.
    for impact,left,right in [(1.1,3,7),(2,9,2),(4,2,12)]:
        integrated = quad(lambda z: 1/math.hypot(impact,z),-left,right,
                          epsabs=1e-12,epsrel=1e-12)[0]
        ra,rb = math.hypot(impact,left),math.hypot(impact,right)
        D = left+right
        L = math.log((ra+rb+D)/(ra+rb-D))
        check("finite_endpoint_light_integral",abs(integrated-L)<1e-12,
              impact=impact,left=left,right=right,error=abs(integrated-L))
        # Extract the first-order coefficient of the full optical ratio of the
        # stated linear metric. Higher powers here are diagnostic, not a 2PN model.
        for mu,amplitude in [(0,.2),(.6,.2),(5,.2)]:
            def excess(e):
                def f(z):
                    r=math.hypot(impact,z)
                    psi=-e*(1+amplitude*math.exp(-mu*r))/r
                    phi=-e*(1-amplitude*math.exp(-mu*r))/r
                    # sqrt(1+u)-1 evaluated stably.
                    u=-2*(psi+phi)/(1+2*psi)
                    return u/(math.sqrt(1+u)+1)
                return quad(f,-left,right,epsabs=1e-13,epsrel=1e-12)[0]/e
            e=1e-5
            extrapolated=2*excess(e/2)-excess(e)
            check("optical_linear_coefficient",abs(extrapolated-2*L)<1e-8,
                  mu=mu,amplitude=amplitude,error=abs(extrapolated-2*L))

    # Synthetic exact-model controls. Radii are shared physical coordinates;
    # these are not planets extracted from a GR ephemeris.
    radii=np.array([1.,2.,4.])
    for mu,M0,B in itertools.product([.03,.1,.5,1,3],[.7,1.3],[.02,.3]):
        K=M0+B*h(mu*radii)
        got=invert_three(K,radii)
        errors=[abs(g-w)/max(1,abs(w)) for g,w in zip(got,(mu,M0,B))]
        check("three_radius_inverse",max(errors)<2e-8,
              input=[mu,M0,B],recovered=list(got),errors=errors)
        # Light mass removes the common mass, two radii remove source amplitude.
        z=B/M0*h(mu*radii)
        ratio=z[1]/z[0]
        f=lambda m: math.log1p(m*radii[1])-math.log1p(m*radii[0])-m*(radii[1]-radii[0])-math.log(ratio)
        mu2=brentq(f,0,100,xtol=1e-12)
        check("two_radius_light_inverse",abs(mu2-mu)<1e-9,
              input_mu=mu,recovered_mu=mu2)

    # Correlated error corners: conservative boxes must enclose the true mass.
    for mu in [.2,.7,2.]:
        K=1+.2*h(mu*radii)
        eps=np.array([1e-7,2e-7,1.5e-7])
        for signs in itertools.product([-1,1],repeat=3):
            Khat=K+eps*np.array(signs)
            interval=mass_interval(Khat,eps,radii)
            check("finite_error_enclosure",interval is not None and interval[0]-1e-11<=mu<=interval[1]+1e-11,
                  mu=mu,signs=signs,interval=interval)
    check("unresolved_zero_mode",mass_interval([1,1,1],[1e-7]*3,radii) is None)

    # Countercontrols prove that a ratio match alone is insufficient.
    badK=-1+10*h(.2*radii)
    badfit=invert_three(badK,radii)
    check("negative_mass_rejected",min(badK)>0 and badfit[1]<0,
          K=list(badK),fitted_mass=badfit[1])
    def supplied_mixture(r):
        return 1+.12*h(.4*r)+.08*h(2*r)
    mixed=supplied_mixture(radii)
    m_eff,M_eff,B_eff=invert_three(mixed,radii)
    r4=3.
    mismatch=abs((M_eff+B_eff*h(m_eff*r4))-supplied_mixture(r4))
    check("multimode_fourth_radius_discriminator",mismatch>1e-5 and M_eff>0,
          fitted=[m_eff,M_eff,B_eff],fourth_radius_error=mismatch,
          light_mass_error=abs(M_eff-1))
    F,_,_,force=profile_green(1,.3,.7,2)
    wrong=F*math.exp(-.7*2)/2**2
    check("missing_force_derivative_mutant_rejected",abs(force-wrong)>1e-3,
          direct_force=force,wrong_potential_coefficient=wrong)
    for mu in [.01,.3,2,8]:
        slope=(log_ratio(mu+1e-5,radii)-log_ratio(mu-1e-5,radii))/2e-5
        means=[]
        for a,b in zip(radii[:-1],radii[1:]):
            i1=quad(lambda r:r*math.exp(-mu*r),a,b)[0]
            i2=quad(lambda r:r*r*math.exp(-mu*r),a,b)[0]
            means.append(i2/i1)
        check("ratio_derivative_identity",slope>0 and abs(slope-(means[1]-means[0]))<2e-8,
              mu=mu,slope=slope,mean_separation=means[1]-means[0])

    records.extend(coherent_phase_checks())

    # Exact rational positivity counterexample, checked without root solving.
    from fractions import Fraction as Q
    lower,upper=Q(149,251),Q(151,249)
    threshold=Q(3,5)*(1+Q(1043,56250))
    upper_bare=Q(50801,500)-Q(149,250)*Q(2499,2500)/Q(3,5000)
    check("finite_error_positive_mass_witness",lower<Q(3,5)<upper<threshold
          and Q(49,50)*Q(38,15)-Q(14,9)==Q(1043,1125)
          and upper_bare==Q(-445667,500),
          ratio_box=[str(lower),str(upper)],bare_mass_upper=str(upper_bare))

    # An already exposed summary, only an idealized comparator calculation.
    delta=2.5e-5
    bound=delta/(2-delta)
    benchmark=[dict(range_over_calibration_radius=l,
                    effective_amplitude_upper=bound/float(h(1/l)))
               for l in [.05,.1,.2,1,10,100]]
    check("benchmark_forward_normalization",abs(-2*bound/(1+bound)+delta)<1e-15,
          gamma_shift=-2*bound/(1+bound),comparator_edge=-delta)
    failed=[r for r in records if not r['passed']]
    result=dict(status="conditional-support",data_role="synthetic development controls; no empirical fit",
                assumptions="one stable source-generated frozen scalar; complete stationary spherical weak source; pointlike weak probes; common coordinates",
                checks=records,benchmark=benchmark,
                total=dict(PASS=len(records)-len(failed),FAIL=len(failed)))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    for name in sorted({r['name'] for r in records}):
        selected=[r for r in records if r['name']==name]
        print(name, 'PASS='+str(sum(r['passed'] for r in selected)), 'FAIL='+str(sum(not r['passed'] for r in selected)))
    print('benchmark',json.dumps(benchmark))
    for fail in failed: print('FAILED',json.dumps(fail))
    print(f"TOTAL: PASS={len(records)-len(failed)} FAIL={len(failed)}")
    print("per_element: checked synthetic radial and finite-count numerical evaluations under the declared operator domain.")
    print("per_site: checked and not executed — no microscopic lattice site or site dynamics is modeled by this runner.")
    print("per_mode: checked one stable scalar mode and a supplied two-mode numerical control; no complete spectrum claim.")
    print("per_block: checked finite spherical sources, exterior optical segments, and ideal coherent links in synthetic examples.")
    print("lattice_wide: checked and not executed — no lattice-wide action selection, state derivation, or empirical acceptance.")
    return bool(failed)


if __name__ == '__main__':
    raise SystemExit(main())
