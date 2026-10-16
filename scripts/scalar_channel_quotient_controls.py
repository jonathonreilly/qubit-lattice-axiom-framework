"""Exact controls for the stated channel model, not instrument validation."""
AUDIT_TIMEOUT_SEC = 180
from fractions import Fraction as F
from math import gcd, lcm
import json
from pathlib import Path
import sympy as s

K = (F(880,749), F(3344,749), F(14,15))
A,B,C = -3007586755,305348069,2325375360

def rational(x):
    if not isinstance(x,(int,F)) or isinstance(x,bool):
        raise TypeError('exact supplied integer/Fraction required, no float inference')
    return F(x)

def primitive(rho):
    rho=rational(rho)
    if rho<=0: raise ValueError('positive relative frequency required')
    g=gcd(rho.denominator,C)
    return (A*rho.denominator//g,B*rho.denominator//g,C*rho.numerator//g)

def columns(rho,fx=1):
    rho,fx=rational(rho),rational(fx)
    if rho<=0 or fx<=0: raise ValueError('positive frequencies required')
    g=(K[0]*fx,K[1]*fx,K[2]*fx*rho)
    a=(K[0]/fx,K[1]/fx,K[2]/(fx*rho))
    d=tuple(1/x for x in g)
    return g,a,d

def dot(a,b): return sum(x*y for x,y in zip(a,b))

def temporal(rhos):
    """One three-endpoint construction, not the entire lattice."""
    if len(rhos)!=3: raise ValueError('exactly three endpoints required')
    x,y,z=map(rational,rhos)
    raw=(y-z,z-x,x-y)
    scale=lcm(*(v.denominator for v in raw), *((C*r*v).denominator for r,v in zip((x,y,z),raw)))
    return tuple(int(scale*v) for v in raw)

def box_halfwidth(coefficients, bounds):
    if len(coefficients)!=len(bounds): raise ValueError('same size required')
    bounds=tuple(map(rational,bounds))
    if any(x<0 for x in bounds): raise ValueError('negative error allowance')
    return sum(abs(c)*e for c,e in zip(coefficients,bounds))

def run():
    checks=[]
    def ck(name,p):
        assert p,name
        checks.append(name)
    ck('primitive Bezout',gcd(A,B)==1)
    ck('first plasma column identity',sum(n*k for n,k in zip((A,B,C),K))==0)
    ck('second plasma column identity',sum(n/k for n,k in zip((A,B,C),K))==0)
    ck('exact G scale',C*K[2]==2170350336)
    for rho in (F(1),F(2),F(47,10),F(25080,5243),F(7,11)):
        n=primitive(rho); g,a,d=columns(rho,F(23,7));m=F(n[0],A)
        ck(f'{rho} integer primitive',gcd(*n)==1 and all(isinstance(x,int) for x in n))
        ck(f'{rho} simultaneous null',dot(n,a)==dot(n,d)==0)
        ck(f'{rho} surviving G',dot(n,g)==C*K[2]*m*F(23,7)*(rho*rho-1))
    for bad in (4.7,'47/10',s.sqrt(2),True):
        try: primitive(bad)
        except TypeError: ck('reject inexact '+str(bad),True)
        else: raise AssertionError('inexact ratio accepted')
    rhos=(F(2),F(3),F(4)); ms=temporal(rhos)
    ns=[(A*m,B*m,int(C*r*m)) for r,m in zip(rhos,ms)]
    ck('three different ratios offset free',all(sum(n[j] for n in ns)==0 for j in range(3)))
    ck('three ratio signal survives',sum(dot(n,columns(r)[0]) for n,r in zip(ns,rhos))!=0)
    two=s.Matrix([[1,1],[2,3]])
    ck('two unequal ratios zero',two.det()!=0)
    rr=(F(1),F(1),F(2)); mm=temporal(rr)
    ck('nonzero lattice without any G',any(mm) and all(m*(r*r-1)==0 for m,r in zip(mm,rr)))
    phases=[(F(3,7),F(2,9),F(1,13)),(F(1,11),F(2,13),F(5,17)),(F(19,23),F(2,3),F(1,5))]
    lhs=sum(dot(n,p) for n,p in zip(ns,phases))
    counts=[tuple(y-x for x,y in zip(phases[i],phases[i+1])) for i in range(2)]
    weights=[tuple(-sum(ns[i][j] for i in range(k+1)) for j in range(3)) for k in range(2)]
    ck('temporal count representation',lhs==sum(dot(w,d) for w,d in zip(weights,counts)))
    rn,ra,fx=F(47,10),F(47,10)+F(1,10**12),F(7175*10**6)
    nn=primitive(rn); mn=F(nn[0],A); U,D=F(7,11),F(13,19)
    gg,aa,dd=columns(ra,fx)
    ck('ratio leakage exact',dot(nn,aa)*U+dot(nn,dd)*D==C*mn/fx*(rn/ra-1)*(K[2]*U+D/K[2]))
    eps=F(1,2*(abs(A)+abs(B)))
    ck('joint first-two error circle',box_halfwidth((A,B,0),(eps,eps,0))==F(1,2))
    v=(19,-5,0);g,a,d=columns(F(47,10),F(23,7))
    ck('small contrast uplink and G cancel',dot(v,g)==dot(v,a)==0)
    ck('small contrast downlink coefficient',dot(v,d)==F(15729,1045)/F(23,7))
    ck('small contrast primitive',gcd(*v)==1)
    ck('small contrast error amplification',box_halfwidth(v,(F(1,1000),)*3)==F(24,1000))
    cell_width_lower=F(abs(A)*7,33*65535)
    ck('16bit inner cell covers primitive circle',cell_width_lower>1)
    theta=s.pi/10
    ck('averaging pointwise identity',s.simplify(s.exp(5*s.I*theta)**19*s.exp(-19*s.I*theta)**5)==1)
    ck('averaging cosine signs',bool(s.cos(s.pi/4)>0 and s.cos(19*s.pi/20)<0))
    averaged_character=s.exp(s.I*s.pi/4)**19*(-s.exp(-s.I*19*s.pi/20))**5
    ck('averaging exact half cycle',s.simplify(averaged_character)==-1)
    return {'kind':'conditional mathematical controls','count':len(checks),'checks':checks,
            'uniform_first_two_circle_threshold_cycles':str(eps),
            'threshold_is_physical_noise_claim':False,'independent_empirical_tests':0}

if __name__=='__main__':
    print(json.dumps(run(),indent=2))
