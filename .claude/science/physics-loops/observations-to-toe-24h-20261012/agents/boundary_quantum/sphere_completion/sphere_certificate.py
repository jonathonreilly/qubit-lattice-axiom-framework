#!/usr/bin/env python3
"""Exact-rational sign/tail certificates plus non-proving numerical checks.

The sign certificates use Python integers/Fraction and explicit Taylor
remainders, not a black-box transcendental interval library. The analytic
lemmas justifying the arithmetic appear in SPHERE_THEOREM.md.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import json
import math
import time
import hashlib
from datetime import datetime, timezone
from decimal import Decimal, localcontext
from fractions import Fraction as F
from pathlib import Path
import mpmath as mp
import numpy as np
from scipy.special import roots_legendre, eval_legendre

HERE=Path(__file__).resolve().parent
CAMPAIGN=Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
SCALE=10**40

def guard():
    assert time.time()<json.loads((CAMPAIGN/'DEADLINE.json').read_text())['deadline_epoch'], 'Deadline'
    assert not any((CAMPAIGN/n).exists() for n in ('STOP_REQUESTED.json','USER_STOP_REQUESTED.json','STOP_REQUESTED','USER_STOP_REQUESTED')), 'Stop requested'

def decimal(x):
    x=F(x)
    with localcontext() as c:
        c.prec=45
        return str(Decimal(x.numerator)/Decimal(x.denominator))

def rat(x):
    x=F(x)
    return {'numerator':str(x.numerator),'denominator':str(x.denominator),'decimal':decimal(x)}

def atan_fraction_interval(x, terms):
    s=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
    other=s+(-1)**terms*x**(2*terms+1)/F(2*terms+1)
    return min(s,other),max(s,other)

def pi_interval():
    lo5,hi5=atan_fraction_interval(F(1,5),50)
    lo239,hi239=atan_fraction_interval(F(1,239),12)
    # tan(4 atan(1/5) - atan(1/239))=1, with the angle in(0,pi/2).
    return 16*lo5-4*hi239,16*hi5-4*lo239

class IV:
    """Closed fixed-point interval [lo/SCALE,hi/SCALE], outward operations."""
    __slots__=('lo','hi')
    def __init__(self,lo,hi):
        assert lo<=hi
        self.lo=int(lo); self.hi=int(hi)
    @staticmethod
    def bounds(lo,hi=None):
        lo=F(lo); hi=lo if hi is None else F(hi)
        return IV((lo.numerator*SCALE)//lo.denominator,-((-hi.numerator*SCALE)//hi.denominator))
    @staticmethod
    def coerce(x):
        return x if isinstance(x,IV) else IV.bounds(x)
    def __add__(self,other):
        o=self.coerce(other); return IV(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return IV(-self.hi,-self.lo)
    def __sub__(self,other): return self+(-self.coerce(other))
    def __rsub__(self,other): return self.coerce(other)+(-self)
    def __mul__(self,other):
        o=self.coerce(other)
        products=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return IV(min(products)//SCALE,-((-max(products))//SCALE))
    __rmul__=__mul__
    def __truediv__(self,other):
        o=self.coerce(other); assert o.lo>0, 'Only positive denominator intervals are used'
        values=(F(self.lo*SCALE,o.lo),F(self.lo*SCALE,o.hi),F(self.hi*SCALE,o.lo),F(self.hi*SCALE,o.hi))
        low=min(values); high=max(values)
        return IV(low.numerator//low.denominator,-((-high.numerator)//high.denominator))
    def rationals(self): return F(self.lo,SCALE),F(self.hi,SCALE)

def polynomial(x, coefficients):
    ans=IV.bounds(coefficients[-1])
    for coefficient in reversed(coefficients[:-1]): ans=ans*x+coefficient
    return ans

SIN_COEFF=[F((-1)**j,math.factorial(2*j+1)) for j in range(13)]
COS_COEFF=[F((-1)**j,math.factorial(2*j)) for j in range(13)]
EXP_COEFF=[F(1,math.factorial(j)) for j in range(25)]

def sincos_interval(x):
    # For0<=x<=pi/2<2, Lagrange remainders after the next zero term.
    x2=x*x
    sin= x*polynomial(x2,SIN_COEFF)+IV.bounds(-F(2**27,math.factorial(27)),F(2**27,math.factorial(27)))
    cos= polynomial(x2,COS_COEFF)+IV.bounds(-F(2**26,math.factorial(26)),F(2**26,math.factorial(26)))
    return sin,cos

def exp_interval(x):
    # 0<=x<1 and e<3; all omitted positive Taylor terms total <=3/25!.
    assert 0<=x.lo and x.hi<SCALE
    return polynomial(x,EXP_COEFF)+IV.bounds(0,F(3,math.factorial(25)))

def certify_a3(k,n,pi_bounds):
    k=F(k)
    pi=IV.bounds(*pi_bounds)
    total=IV.bounds(0)
    for j in range(n):
        theta=pi*F(2*j+1,4*n)
        sine,c=sincos_interval(theta)
        u=F(1)-F(2*j+1,2*n)
        q=exp_interval(2*k*c)
        g=((1+u)*q-(1-u))/((1+u)*q+(1-u))
        p3=(5*c*c*c-3*c)/2
        total+=g*p3*sine
    est=7*pi*F(1,2*n)*total
    # |[g(theta)P3(cos theta)sin theta]''|<=53 for k<=8/25.
    err=F(7*53*11**3,24*7**3*n*n)
    lo,hi=est.rationals()
    return {'k':rat(k),'n':n,'midpoint_estimate_interval':[rat(lo),rat(hi)],'analytic_quadrature_error_upper':rat(err),'a3_certified_interval':[rat(lo-err),rat(hi+err)],'sign': 'positive' if lo-err>0 else ('negative' if hi+err<0 else 'unresolved')}

def exact_tail_certificates():
    pi_lo,pi_hi=pi_interval()
    assert F(31415,10000)<pi_lo and pi_hi<F(22,7)
    # ln5<1.61 from a positive partial sum for exp1.61.
    exp161_partial=sum((F(161,100)**j/F(math.factorial(j)) for j in range(13)),F(0))
    assert exp161_partial>5
    assert F(2)*F(161,100)/F(31415,10000)<F(41,40)
    x=F(4,5)
    sin_lower=x-x**3/6+x**5/120-x**7/5040
    cos_upper=1-x*x/2+x**4/24
    assert sin_lower>F(41,40)*cos_upper>0
    assert F(4,5)+F(8,25)*F(12,5)<pi_lo/2
    # Elementary positive-series remainder proves exp(16/25)<2.
    exp64=exp_interval(IV.bounds(F(16,25)))
    assert exp64.hi<2*SCALE
    # Lower integral: acosh(x)>=2sqrt(2/5)sqrt(x-1), x in[1,3/2].
    M=10**6
    sqrt25_lower=F(math.isqrt(2*M*M//5),M)
    assert sqrt25_lower**2<F(2,5)
    s=F(0)
    for j in range(32):
        upper_sqrt_j=F(math.isqrt(j*M*M)+1,M)
        lower_sqrt_next=F(math.isqrt((j+1)*M*M),M)
        difference=(j+1)*lower_sqrt_next-j*upper_sqrt_j
        s+=difference*F(64,65+j)**8
    integral_lower=F(4,3)*sqrt25_lower*s/F(512)
    assert integral_lower>F(1,20)
    K=F(8,25)
    pole_upper=2/K*((F(5,12))**8+2*(K/3)**8)
    assert pole_upper<F(3,500)
    return {'pi_interval':[rat(pi_lo),rat(pi_hi)],'exp_1.61_positive_partial_sum':rat(exp161_partial),'tan_.8_lower_bound':rat(sin_lower/cos_upper),'pole_radius_lower':'12/5','K':'8/25','exp_.64_upper':rat(F(exp64.hi,SCALE)),'restricted_integral_algebraic_lower':rat(integral_lower),'restricted_cut_C3_lower':'3/500','pole_P3_upper':rat(pole_upper),'strict_margin_lower':rat(F(3,500)-pole_upper)},(pi_lo,pi_hi)

def taylor_coefficients(k,degree=101):
    count=(degree+1)//2
    u=[(2/mp.pi)*mp.binomial(2*n,n)/(mp.mpf(4)**n*(2*n+1)) for n in range(count)]
    u2=[mp.mpf(0)]+[sum(u[j]*u[n-1-j] for j in range(n)) for n in range(1,count)]
    v=[]
    for n in range(count):
        v.append((2*n+1)*u[n]+sum(u2[j]*v[n-j] for j in range(1,n+1)))
    v[0]+=k
    b=[]; f2=[mp.mpf(0)]
    for n in range(count):
        if n: f2.append(sum(b[j]*b[n-1-j] for j in range(n)))
        b.append((v[n]-sum(f2[j]*v[n-j] for j in range(1,n+1)))/(2*n+1))
    return b

def numerical_scans(values):
    mp.mp.dps=80
    outputs=[]
    for k in values:
        guard()
        km=mp.mpf(str(k))
        b=taylor_coefficients(km)
        checks=mp.taylor(lambda c:mp.tanh(mp.atanh((2/mp.pi)*mp.asin(c))+km*c),0,9)
        taylor_error=max(abs(checks[2*n+1]-b[n]) for n in range(5))
        coeffs={}
        for order in (1024,2048):
            nodes,weights=roots_legendre(order)
            theta=(nodes+1)*np.pi/4
            c=np.cos(theta); u=1-2*theta/np.pi
            g=np.tanh(np.arctanh(u)+k*c)
            base=g*np.sin(theta)*weights*np.pi/4
            coeffs[str(order)]=[(2*l+1)*float(np.dot(base,eval_legendre(l,c))) for l in range(1,102,2)]
        row={'k':k,'taylor_odd_degrees':list(range(1,102,2)),'taylor_coefficients_80dps':[str(t) for t in b],'taylor_independent_degree9_max_difference':str(taylor_error),'minimum_Taylor_degree_at_least5':str(min(b[2:])),'legendre_odd_ell':list(range(1,102,2)),'legendre_by_order':coeffs,'legendre_order_change':float(np.max(np.abs(np.array(coeffs['1024'])-coeffs['2048'])))}
        outputs.append(row)
        print(json.dumps({'k':k,'b3':str(b[1]),'min_degree5up':row['minimum_Taylor_degree_at_least5'],'a3':coeffs['2048'][1]}),flush=True)
    return outputs

def cut_pole_check(k):
    km=mp.mpf(str(k)); count=40
    b=taylor_coefficients(km,9)
    a=lambda y:2*mp.asinh(y)/mp.pi
    bprime=lambda y:(2/mp.pi)/(mp.sqrt(1+y*y)*(1+a(y)**2))
    poles=[]
    for m in range(count):
        lo=mp.pi*m/km; hi=mp.pi*(m+mp.mpf('.5'))/km
        target=mp.pi*(m+mp.mpf('.5'))
        for j in range(180):
            mid=(lo+hi)/2
            if mp.atan(a(mid))+km*mid<target: lo=mid
            else: hi=mid
        y=(lo+hi)/2
        poles.append((y,1/(km+bprime(y))))
    output=[]
    for n in (1,2,3):
        power=2*n+2
        density=lambda x:(2/mp.pi)*mp.acosh(x)*mp.exp(-2*km*x)/(1+(mp.acosh(x)/mp.pi)**2*(1-mp.exp(-2*km*x))**2)
        cut=(2/mp.pi)*mp.quad(lambda x:density(x)/x**power,[1,mp.mpf('1.5'),2,5,mp.inf])
        pole=2*sum(R/y**power for y,R in poles)
        # m=count..infinity, y_m>pi*m/k and R_m<1/k.
        tail=2/km*(km/mp.pi)**power*(mp.mpf(count)**(-power)+mp.mpf(count)**(1-power)/(power-1))
        reconstructed=cut+(-1)**n*pole
        output.append({'odd_degree':2*n+1,'direct_Taylor':str(b[n]),'cut_integral':str(cut),'pole_partial_sum':str(pole),'pole_tail_absolute_bound':str(tail),'cut_plus_signed_poles':str(reconstructed),'difference':str(b[n]-reconstructed),'within_pole_tail_plus_1e-45':bool(abs(b[n]-reconstructed)<tail+mp.mpf('1e-45'))})
    return {'k':k,'pole_count':count,'smallest_pole':str(poles[0][0]),'checks':output}

def main():
    guard()
    started=datetime.now(timezone.utc).isoformat()
    exact,pi_bounds=exact_tail_certificates()
    certificates=[]
    for k,n in ((F(8,25),1024),(F(3183,10000),4096),(F(3184,10000),4096)):
        guard()
        result=certify_a3(k,n,pi_bounds)
        certificates.append(result)
        print('Certified a3',decimal(k),result['sign'],[x['decimal'] for x in result['a3_certified_interval']],flush=True)
    assert [c['sign'] for c in certificates]==['negative','positive','negative']
    frozen=json.loads((HERE/'PRECOMPUTE_FREEZE.json').read_text())
    scans=numerical_scans(frozen['protocol']['exploratory_k'])
    pole_checks=[cut_pole_check(k) for k in (.1,.32)]
    assert all(v['within_pole_tail_plus_1e-45'] for row in pole_checks for v in row['checks'])
    root=mp.findroot(lambda k:7*mp.quad(lambda t:mp.tanh(mp.atanh(1-2*t/mp.pi)+k*mp.cos(t))*mp.legendre(3,mp.cos(t))*mp.sin(t),[0,mp.pi/4,mp.pi/2]),(.318,.319))
    result={'started_at':started,'completed_at':datetime.now(timezone.utc).isoformat(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'exact_rational_tail_certificates':exact,'exact_rational_a3_certificates':certificates,'numerical_scans':scans,'independent_cut_pole_checks':pole_checks,'k3_unique_root_high_precision_numerical':str(root),'k3_rigorous_bracket':['3183/10000','3184/10000'],'k_infinite_sphere_power_threshold_numerical':str((1/mp.pi+8/mp.pi**3)**(mp.mpf(1)/3)-2/mp.pi),'interpretation':'Analytic tail and contour lemmas are required; finite scans alone are not a PSD proof. Exact arithmetic validates declared numerical inequalities conditional on those derived error bounds.'}
    (HERE/'CERTIFICATE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Wrote CERTIFICATE_RESULTS.json',flush=True)

if __name__=='__main__':main()
