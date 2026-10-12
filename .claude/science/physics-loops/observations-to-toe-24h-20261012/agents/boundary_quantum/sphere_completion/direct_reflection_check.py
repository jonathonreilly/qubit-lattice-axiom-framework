#!/usr/bin/env python3
"""Source-bound exact a3 interval and prospective degree-three witness."""
import argparse
import hashlib
import json
import math
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path

import mpmath as mp
import sphere_certificate as arithmetic

HERE=Path(__file__).resolve().parent
RT=arithmetic.CAMPAIGN/'quantum'/'direct_reflection'

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def atanh_interval(x,n=140):
    IV=arithmetic.IV
    assert 0<=x.lo<=x.hi<arithmetic.SCALE
    power=x
    total=IV.bounds(0)
    for j in range(n):
        total+=power/F(2*j+1)
        power=power*x*x
    upper=F(x.hi,arithmetic.SCALE)
    tail=upper**(2*n+1)/(F(2*n+1)*(1-upper*upper))
    return total+IV.bounds(0,tail)

def exact_k_interval():
    IV=arithmetic.IV
    scale=arithmetic.SCALE
    r=math.isqrt(2*scale*scale)
    assert r*r<2*scale*scale<(r+1)**2
    root=IV.bounds(F(r,scale),F(r+1,scale))
    return root*(atanh_interval(IV.bounds(1)/root)-atanh_interval(IV.bounds(F(1,2))))

def certify(n):
    IV=arithmetic.IV
    pilo,pihi=arithmetic.pi_interval()
    assert F(3)<pilo<pihi<F(22,7)
    pi=IV.bounds(pilo,pihi)
    k=exact_k_interval()
    klo,khi=k.rationals()
    assert 0<klo<khi<F(1,2)
    total=IV.bounds(0)
    for j in range(n):
        if j%128==0:
            arithmetic.guard()
        theta=pi*F(2*j+1,4*n)
        sine,c=arithmetic.sincos_interval(theta)
        u=F(1)-F(2*j+1,2*n)
        q=arithmetic.exp_interval(2*k*c)
        g=((1+u)*q-(1-u))/((1+u)*q+(1-u))
        p3=(5*c*c*c-3*c)/2
        total+=g*p3*sine
    low,high=(7*pi*F(1,2*n)*total).rationals()
    error=F(7*48*11**3,24*7**3*n*n)
    return k,(low-error,high+error),error

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--freeze',action='store_true')
    args=parser.parse_args()
    arithmetic.guard()
    RT.mkdir(parents=True,exist_ok=True)
    files={name:sha(HERE/name) for name in [
        'DIRECT_REFLECTION_WITNESS.md','direct_reflection_check.py','sphere_certificate.py']}
    freeze_path=RT/'FREEZE.json'
    if args.freeze:
        assert not freeze_path.exists()
        freeze_path.write_text(json.dumps({'at':datetime.now(timezone.utc).isoformat(),
            'source_hashes':files,'panels':2048,'visibilities':['9/10','19/20','1'],
            'candidate':'exact sqrt2*(atanh(1/sqrt2)-atanh(1/2))',
            'derivative_bound':48,'fit_data':None},indent=2)+'\n')
        print(freeze_path)
        return
    freeze=json.loads(freeze_path.read_text())
    assert freeze['source_hashes']==files
    output=RT/'RESULTS_v1.json'
    assert not output.exists()
    k,(low,high),error=certify(freeze['panels'])
    assert high<0
    rat=arithmetic.rat
    results=[]
    J=F(111,20)
    # A coarse exact upper bound ln100<5 follows from e^5>100.
    assert sum((F(5)**j/F(math.factorial(j)) for j in range(12)),F(0))>100
    for value in freeze['visibilities']:
        V=F(value)
        blo,bhi=V*(1-2*high),V*(1-2*low)
        gap=blo-1
        sample_bound=None
        if gap>0:
            need=8*J*J*5/(gap*gap)
            sample_bound=-(-need.numerator//need.denominator)
        results.append({'V':rat(V),'B_interval':[rat(blo),rat(bhi)],
            'certified_above_quantum_bound':blo>1,'gap_lower':rat(gap),
            'N_for_each_error_at_most_one_percent_using_ln100_lt_5':sample_bound})
    mp.mp.dps=70
    km=mp.sqrt(2)*(mp.atanh(1/mp.sqrt(2))-mp.atanh(mp.mpf('.5')))
    def integrand(theta):
        if theta==0:
            return mp.mpf('0')
        u=1-2*theta/mp.pi
        t=mp.tanh(km*mp.cos(theta))
        c=mp.cos(theta)
        return 7*(u+t)/(1+u*t)*(5*c**3-3*c)/2*mp.sin(theta)
    numeric=mp.quad(integrand,[0,mp.pi/4,mp.pi/2])
    assert mp.mpf(low.numerator)/low.denominator<numeric<mp.mpf(high.numerator)/high.denominator
    # Independent exact integral via antiderivative at P3 roots 0,+/-sqrt(3/5).
    # F3(c)=5 c^4/8-3 c^2/4; F3(1)=-1/8, F3(sqrt(3/5))=-9/40.
    absolute_integral=2*(F(9,40)+(F(-1,8)+F(9,40)))
    assert absolute_integral==F(13,20)
    assert 1+14*absolute_integral/2==J
    data={'at':datetime.now(timezone.utc).isoformat(),'source_hashes':files,
          'freeze_sha256':sha(freeze_path),'panels':freeze['panels'],
          'k_exact_interval':[rat(x) for x in k.rationals()],
          'a3_interval':[rat(low),rat(high)],'quadrature_error_upper':rat(error),
          'a3_numerical_only':str(numeric),'witnesses':results,
          'witness_critical_visibility_interval':[rat(1/(1-2*low)),rat(1/(1-2*high))],
          'total_absolute_weight':rat(J),'integral_abs_P3':rat(absolute_integral),
          'scope':'Exact rational a3/witness interval under explicit analytic remainder bounds. Ideal quantum correlation test; no apparatus or empirical exclusion. Independent checking is separate.'}
    assert files=={name:sha(HERE/name) for name in files}
    output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))

if __name__=='__main__':
    main()
