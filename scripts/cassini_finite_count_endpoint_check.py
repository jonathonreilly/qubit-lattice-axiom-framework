#!/usr/bin/env python3
"""Deterministic exact checks of the conditional finite-count endpoint derivation."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
from random import Random

import sympy as sp

from cassini_ramp_phase import NS, Ramp, phase_integral, rational

AUDIT_TIMEOUT_SEC = 120


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args(); checks=[]
    def check(name, ok):
        checks.append({'name':name,'pass':bool(ok)})
        if not ok: raise AssertionError(name)
    def P(rs,a,b):
        return phase_integral(rs,a*NS,b*NS)[0]
    def D(rs,a,b,R,T,k):
        return (R-k*P(rs,a,b))/T

    # Derive the chain with independently chosen nonlinear station clock maps.
    t=sp.symbols('t',positive=True)
    t1=sp.Rational(4,5)*t-sp.Rational(1,5)
    s1=3*t1+t1**2/20
    s3=2*t+t**2/10
    f0,rate,k=sp.symbols('f0 rate k')
    phase=k*(f0*s1+rate*s1**2/2)
    f_received=sp.diff(phase,t)/sp.diff(s3,t)
    clock_chain=k*(f0+rate*s1)*sp.diff(s1,t)/sp.diff(s3,t)
    check('station_clock_chain_symbolic',sp.simplify(f_received-clock_chain)==0)
    received_cycles=sp.integrate(sp.cancel(f_received*sp.diff(s3,t)),(t,1,2))
    check('integrated_clock_chain_symbolic',sp.simplify(received_cycles-(phase.subs(t,2)-phase.subs(t,1)))==0)
    # The same phases differentiated in station time already contain the clock map.
    wrong_frequency=f_received*sp.diff(s1,t)/sp.diff(s3,t)
    check('extra_clock_multiplier_rejected',sp.simplify((wrong_frequency-f_received).subs({t:sp.Rational(3,2),f0:7,rate:2,k:sp.Rational(5,4)}))!=0)

    rng=Random(20261014)
    examples=[]
    for n in range(128):
        f=Q(100+rng.randrange(3,100)); r=Q(rng.randrange(-10,11))
        rr=Ramp(25,-10*NS,10*NS,int((f-10*r)*NS),int(r*NS),True)
        a,b=Q(-3,2),Q(7,4)
        ds,de=Q(rng.randrange(-200,201),1000),Q(rng.randrange(-200,201),1000)
        T=Q(7,2); kval=Q(5,4); ref=Q(100)
        fa,fb=rr.frequency(a*NS),rr.frequency(b*NS)
        actual=D([rr],a-ds,b-de,ref,T,kval)-D([rr],a,b,ref,T,kval)
        linear=kval*(fb*de-fa*ds)/T
        remainder=-kval*r*(de**2-ds**2)/(2*T)
        bound=abs(kval*r)*(de**2+ds**2)/(2*T)
        check(f'affine_endpoint_exact_{n}',actual==linear+remainder)
        check(f'quadratic_bound_{n}',abs(actual-linear)<=bound)
        common,differential=(de+ds)/2,de-ds
        check(f'common_differential_decomposition_{n}',linear==kval*((fb-fa)*common+(fb+fa)*differential/2)/T)
        # Shared reference cancels, including an arbitrary large reference offset.
        shifted=D([rr],a-ds,b-de,ref+10**9,T,kval)-D([rr],a,b,ref+10**9,T,kval)
        check(f'shared_reference_cancellation_{n}',shifted==actual)
        if n<3: examples.append(dict(delta_s=rational(ds),delta_e=rational(de),
                                     exact=rational(actual),linear=rational(linear),bound=rational(bound)))

    # A continuous piecewise-linear ramp is Lipschitz even across a slope change.
    continuous=[Ramp(25,-2*NS,0,8*NS,NS,True),Ramp(25,0,2*NS,10*NS,3*NS,True)]
    a,b=Q(-1),Q(1,10);ds,de=Q(1,20),Q(1,5);T=Q(1);kval=Q(1)
    actual=D(continuous,a-ds,b-de,100,T,kval)-D(continuous,a,b,100,T,kval)
    linear=Q(103,10)*de-Q(9)*ds
    check('continuous_slope_change_bound',abs(actual-linear)<=Q(3,2)*(de**2+ds**2))
    jumps=[Ramp(25,-2*NS,0,10*NS,0,True),Ramp(25,0,2*NS,30*NS,0,True)]
    integral=P(jumps,Q(-1,10),Q(1,10));linear_integral=30*Q(1,5)
    check('jump_exact_integral',integral==4)
    check('slope_only_bound_at_jump_rejected',abs(integral-linear_integral)==2)
    constant=[Ramp(25,-10*NS,10*NS,10*NS,0,True)]
    ramp=[Ramp(25,-10*NS,10*NS,0,NS,True)] # f(s)=10+s
    a,b,delta=Q(1),Q(2),Q(1,10)
    check('common_shift_cancels_constant',D(constant,a-delta,b-delta,0,1,1)==D(constant,a,b,0,1,1))
    check('common_shift_survives_ramp',D(ramp,a-delta,b-delta,0,1,1)-D(ramp,a,b,0,1,1)==delta)
    check('duration_error_retains_carrier',D(constant,a,b-delta,0,1,1)-D(constant,a,b,0,1,1)==1)
    # Signed negative shifts are essential, not an absolute-value substitution.
    actual=D(ramp,a+delta,b,0,1,1)-D(ramp,a,b,0,1,1)
    wrong=D(ramp,a-delta,b,0,1,1)-D(ramp,a,b,0,1,1)
    check('absolute_endpoint_shift_rejected',actual!=wrong)
    check('sign_of_roundtrip_shift_rejected',actual!=-actual)
    # An unknown reference can absorb any phase increment: exhibit the invariance.
    R,P0,h,kval,T=Q(8),Q(5),Q(3,7),Q(5,4),Q(2)
    check('reference_phase_degeneracy',(R-kval*P0)/T==((R+kval*h)-kval*(P0+h))/T)
    # Origin changes transform endpoints and the ramp ledger together.
    epoch=1655517848*NS
    translated=[Ramp(25,r.start_ns+epoch,r.end_ns+epoch,r.frequency_nhz,r.rate_nhz_per_second,r.sky_level) for r in ramp]
    check('clock_origin_is_not_physical_error',phase_integral(translated,epoch+NS,epoch+2*NS)[0]==P(ramp,Q(1),Q(2)))
    # A measurement uses the receive interval; emission interval need not be equal.
    check('emission_duration_denominator_rejected',D(ramp,Q(1),Q(2),100,Q(3,2),1)!=D(ramp,Q(1),Q(2),100,Q(1),1))
    source=Path(__file__)
    result=dict(status='conditional mathematics checked; no empirical gravity fit',
        runner_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
        ramp_helper_sha256=hashlib.sha256(source.with_name('cassini_ramp_phase.py').read_bytes()).hexdigest(),
        checks=checks,passed=sum(c['pass'] for c in checks),failed=sum(not c['pass'] for c in checks),
        rational_examples=examples,
        scope='Synthetic exact/symbolic controls. No data exposure, clock precision, mission mode or scalar model selected.')
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','runner_sha256','ramp_helper_sha256','passed','failed']},indent=2))


if __name__=='__main__': main()
