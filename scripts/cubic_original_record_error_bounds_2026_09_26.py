"""Exact rational arithmetic for the proved local error bounds.

This checks numerical inequalities conditional on the analytic locality,
preparation, averaging and capture proofs. It does not prove those hypotheses.
"""
from fractions import Fraction as F
from collections import Counter
from itertools import product
import json,math

def exponential_upper(x):
    s=max(1,math.ceil(x));y=x/s;term=F(1);total=term
    for k in range(1,25):term=term*y/k;total+=term
    return (total+(term*y/25)/(1-y/26))**s

def support_inventory():
    centers={v for v in product(range(-4,5),repeat=3) if sum(map(abs,v))<=4 and sum(v)%2==0}
    displacements={v for v in product(range(-2,3),repeat=3) if sum(map(abs,v))==2}
    pairs={tuple(sorted((a,tuple(x+y for x,y in zip(a,d))))) for a in centers for d in displacements}
    assert len(centers)==85 and len(displacements)==18 and len(pairs)==1038
    return {'intersecting_center_overcount':len(centers),'intersecting_pair_overcount':len(pairs)}

def calculate():
    inventory=support_inventory();l=2048;u=F(1,50);r=F(1,10**33);T=256
    J=1195776+27200*r;c=10368+160*r;z=F(6,7)
    b=l+7+math.ceil(18*J*u)+6*T;a=b-3
    poly=24*(F(a*a)/(1-z)+2*a*z/(1-z)**2+z*(1+z)/(1-z)**3)+2/(1-z)
    E=u*c*poly/F(2**T)
    assert 3*J*u-F(b-l-7,6)<=-T
    nA=((2*b+1)**3+(-1)**b)//2;nB=(2*b+1)**3-nA
    ell=nA*(5184+160*r);epsilon=r*u/400
    R=math.ceil(max(24*nB/epsilon**2,F(22,7)*ell*(1+2*ell*u)/(2*epsilon)))
    assert E<=epsilon and F(24*nB,R)<=epsilon**2
    av=F(22,7)*ell*(1+2*ell*u)/(2*R);assert av<=epsilon
    q=math.ceil(l+4+18*1195776*u);B=(2*q+1)**3+144*q*q+2016*q+13116
    W=((2*l+1)**3+(-1)**l)//2;m=80*W
    weak=160*r*m*u*B+r*m*m*u
    # Use the conservative epsilon bound for each of prep,av,av.
    local=(3*epsilon+4*E)/(r*u)
    n=(l-7)//2+1;x=11728*u
    vector=exponential_upper(x)*x**n/math.factorial(n)
    capture=684*vector*vector
    # This base-volume tail decreases for all larger q>=2047, since x/(q+1)<1.
    qvol=16384//8-1;y=2*14128*u
    volume=1368*exponential_upper(y)*y**qvol/math.factorial(qvol)
    assert capture<F(1,10**200) and volume<F(2,10**9)
    assert y<qvol+1
    total=weak+local+F(1,10**200)+F(2,10**9)
    assert total<F(14,1000)
    Lmin=2*math.ceil(F(4*(b+4)+1,2));assert Lmin>4*(b+4) and Lmin>=16384
    result={'support_inventory':inventory,'l':l,'u_exact':str(u),'r_exact':str(r),'b':b,
      'n_A':nA,'n_B':nB,'R_integer_sufficient':R,'minimum_even_L':Lmin,
      'preparation_and_each_averaging_error_at_most':str(epsilon),
      'truncation_error_upper_approx':float(E),'weak_probe_error_exact':str(weak),
      'local_transfer_error_upper_approx':float(local),
      'capture_error_certified_upper':'1e-200','volume_error_certified_upper':'2e-9',
      'normalized_total_error_certified_upper':'0.014',
      'example_L':10**12,'example_N_r_u':str(F(10**36,2)*r*u),
      'scope':'Fixed finite R,r,u,l,b; uniform over all sufficiently large even L. No sampling or floating propagation error included; not practical experimental scales.'}
    print(json.dumps(result,indent=2),flush=True)
    return result

if __name__=='__main__':calculate()
