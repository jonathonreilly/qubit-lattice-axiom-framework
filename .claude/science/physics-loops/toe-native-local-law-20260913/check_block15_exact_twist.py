"""Exact rational enclosures of the supplied 3^3 mixed-carrier twist energy.

Integer square-root brackets certify a strict comparison, not a global minimum.
"""
from fractions import Fraction as Q
from itertools import product
from math import isqrt
from pathlib import Path
import json

checks=0


def check(ok,label):
    global checks
    assert ok,label
    checks+=1


def sqrt_interval(value,scale=10**35):
    check(value>=0,'nonnegative exact radicand')
    k=isqrt(value.numerator*scale*scale//value.denominator)
    lo,hi=Q(k,scale),Q(k+1,scale)
    check(lo*lo<=value<=hi*hi,'integer-certified square-root enclosure')
    return lo,hi


def energy_interval(twist_y):
    periodic=[(Q(1),Q(0)),(Q(-1,2),Q(1,2)),(Q(-1,2),Q(-1,2))]
    antiperiodic=[(Q(1,2),Q(1,2)),(Q(-1),Q(0)),(Q(1,2),Q(-1,2))]
    lower=Q(0);upper=Q(0);records=[]
    for (cx,sx),(cy,sy),(cz,sz) in product(periodic,antiperiodic if twist_y else periodic,periodic):
        # Sines are the second coordinate times sqrt(3), which squares exactly.
        a=-Q(4,5)*cx;b=Q(3,5)*sx
        c=Q(13,5)-Q(3,5)*cx-cy-cz;d=-Q(4,5)*sx
        m1,m3=Q(4,25),Q(3,25)
        S=3*sy*sy+a*a+3*b*b+c*c+3*d*d+Q(1,25)
        U=3*(a*b+c*d)**2+(a*m1+c*m3)**2+3*(b*m3-d*m1)**2
        ulo,uhi=sqrt_interval(U)
        pluslo,_=sqrt_interval(S+2*ulo);_,plushi=sqrt_interval(S+2*uhi)
        minuslo,_=sqrt_interval(S-2*uhi);_,minushi=sqrt_interval(S-2*ulo)
        lower-=plushi+minushi;upper-=pluslo+minuslo
        check(S*S-4*U>0,'two strictly negative occupied bands on this finite grid')
        records.append(dict(cosines=[str(cx),str(cy),str(cz)],S=str(S),U=str(U)))
    return lower,upper,records


zero=energy_interval(False);twist=energy_interval(True)
difference=(twist[0]-zero[1],twist[1]-zero[0])
check(difference[1]<Q(-14424,10000),'nonidentity flat twist lowers energy by more than 1.4424')
check(difference[0]>Q(-14425,10000),'strict difference lies above -1.4425')
check(zero[1]-zero[0]<Q(1,10**30),'identity interval narrow by exact rational comparison')
check(twist[1]-twist[0]<Q(1,10**30),'twisted interval narrow by exact rational comparison')
out=dict(checks=checks,identity_interval=list(map(str,zero[:2])),twisted_interval=list(map(str,twist[:2])),
         difference_interval=list(map(str,difference)),difference_decimal_display=list(map(float,difference)),
         identity_radicals=zero[2],twist_radicals=twist[2],
         claim='Strict two-twist energy comparison only; no global minimum, interacting phase, or volume-uniform rate.')
p=Path(__file__).resolve().parent;(p/'BLOCK15_EXACT_TWIST_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if not k.endswith('radicals')},indent=2))
print(f'TOTAL: PASS={checks} FAIL=0')
