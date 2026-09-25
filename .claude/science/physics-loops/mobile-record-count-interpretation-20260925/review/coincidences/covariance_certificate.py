"""Exact rational enclosure of the actual side-12 translated xy covariance.

All square roots are enclosed with integer arithmetic. No floating library,
trigonometric numerical routine, author source or parent runner is used.
"""
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
from datetime import datetime, timezone
import hashlib
import json


SCALE=10**40


def sqrt_bounds(x):
    assert x>=0
    n=isqrt(x.numerator*SCALE*SCALE//x.denominator)
    lo=F(n,SCALE);hi=F(n+1,SCALE)
    assert lo*lo<=x<hi*hi
    return lo,hi


SQRT3=sqrt_bounds(F(3))


def algebraic_bounds(A,B):
    a,b=SQRT3
    return (A+B*a,A+B*b) if B>=0 else (A+B*b,A+B*a)


def divide_bounds(numer,denom):
    assert denom[0]>0
    values=[x/y for x in numer for y in denom]
    return min(values),max(values)


def decimal_out(x,upper=False,digits=30):
    unit=10**digits
    n=(x.numerator*unit)//x.denominator
    if upper and F(n,unit)<x:n+=1
    sign='-' if n<0 else '';n=abs(n)
    return f'{sign}{n//unit}.{n%unit:0{digits}d}'


def covariance(direction):
    # Exact 4 sin^2(pi n/12), n=0,...,11, from half-angle identities.
    values=[(0,0),(2,-1),(1,0),(2,0),(3,0),(2,1),(4,0),(2,1),(3,0),(2,0),(1,0),(2,-1)]
    groups=defaultdict(lambda:[0,0,0])
    for i in range(12):
        for j in range(12):
            for k in range(12):
                if i==j==k==0:continue
                x,y,z=values[i],values[j],values[k]
                key=(x[0]+y[0]+z[0],x[1]+y[1]+z[1])
                # Translation by six links: exp(i k.R)=(-1)^n exactly.
                phase=(-1)**((i,j,k)[direction])
                groups[key][0]+=phase*(x[0]+y[0])
                groups[key][1]+=phase*(x[1]+y[1])
                groups[key][2]+=1
    lower=F(0);upper=F(0);rows=[]
    for (A,B),(N,M,count) in sorted(groups.items()):
        lo,hi=algebraic_bounds(A,B);assert lo>0
        denominator=(sqrt_bounds(lo)[0],sqrt_bounds(hi)[1])
        term=divide_bounds(algebraic_bounds(N,M),denominator)
        lower+=term[0];upper+=term[1]
        rows.append({'D_A':A,'D_B':B,'weighted_Dxy_A':N,'weighted_Dxy_B':M,'momenta':count})
    lower/=2*12**3;upper/=2*12**3
    assert sum(row['momenta'] for row in rows)==12**3-1
    assert (upper<0) if direction==0 else (lower>0)
    absolute=max(abs(lower),abs(upper))
    assert absolute<F(1,1000)
    # The exact parent-free plaquette estimate v>=1/sqrt(3) bounds |c|/v.
    normalized_upper=absolute*SQRT3[1]
    assert normalized_upper<F(2,3)
    return {'L':12,'separation_axis':direction,'translation_length':6,
            'exact_group_rows':rows,'covariance_lower_outward_decimal':decimal_out(lower),
            'covariance_upper_outward_decimal':decimal_out(upper,True),
            'normalized_abs_covariance_upper_outward_decimal':decimal_out(normalized_upper,True),
            'strictly_nonzero_and_abs_normalized_below_two_thirds':True,
            'interval_width_upper_outward_decimal':decimal_out(upper-lower,True,45)}


def main():
    result={'scope':'Exact rational finite Fourier enclosure: actual even side12, xy plaquettes translated by6 along x or z. This is a static sign/size certificate, not a dynamics or laboratory certificate.',
            'sqrt3_bounds_outward_decimal':[decimal_out(SQRT3[0]),decimal_out(SQRT3[1],True)],
            'rows':[covariance(0),covariance(2)],
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'completed_utc':datetime.now(timezone.utc).isoformat()}
    text=json.dumps(result,indent=2)+'\n'
    Path(__file__).with_name('COVARIANCE_CERTIFICATE.json').write_text(text)
    print(text,end='')


if __name__=='__main__':main()
