#!/usr/bin/env python3
"""Fixed bounded rational comparison for the two-source Ward trial.

Source scalar certificates are inherited conditional inputs. This program
checks algebra and arithmetic; it does not repeat their quadrature or gap proof.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import isqrt
from pathlib import Path
import hashlib
import json
import resource
import signal
import sys
import time
import sympy as s
from block12_clifford import A0,C0,ODD
from block12_nominal import CLASSES,kernel,norm_formulas

HERE=Path(__file__).resolve().parent
SYMBOLS=[A0,C0]+[ODD[j] for j in (1,3,5,7,9,11)]
LOCALS={str(x):x for x in SYMBOLS}


class I:
    def __init__(self,lo,hi=None):
        self.lo=F(lo);self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,b):
        if not isinstance(b,I):b=I(b)
        return I(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,b):return self+-as_i(b)
    def __mul__(self,b):
        b=as_i(b);z=[self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi]
        return I(min(z),max(z))
    __rmul__=__mul__
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return I(1)
        if n%2:return I(self.lo**n,self.hi**n)
        return I(0 if self.lo<=0<=self.hi else min(self.lo**n,self.hi**n),max(self.lo**n,self.hi**n))
    def pair(self):return [str(self.lo),str(self.hi)]
    def overlap(self,b):return max(self.lo,b.lo)<=min(self.hi,b.hi)


def as_i(x):return x if isinstance(x,I) else I(x)
def frac(x):return F(int(s.numer(x)),int(s.denom(x)))
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def evaluate(expr,env):
    # First collect each inverse-frequency scalar ONCE. Expanding the whole
    # expression into mixed monomials would discard its affine correlation.
    radial_symbols=SYMBOLS[2:]
    outer=s.Poly(s.expand(expr),A0,C0)
    assert outer.total_degree()<=1
    out=I(0)
    for (a_power,c_power),coefficient in outer.terms():
        z=I(0)
        for powers,c in s.Poly(coefficient,*radial_symbols).terms():
            term=I(frac(c))
            for sym,n in zip(radial_symbols,powers):
                if n:term=term*(env[sym]**n)
            z=z+term
        out=out+z*(env[A0]**a_power)*(env[C0]**c_power)
    return out


def root_hi(q,bits=128):
    q=F(q);assert q>=0
    scale=1<<bits
    n=isqrt((q.numerator*scale*scale)//q.denominator)
    if F(n*n,scale*scale)<q:n+=1
    result=F(n,scale)
    assert result*result>=q
    return result


def envelopes():
    x=s.Symbol('x');delta=s.Rational(1,4)
    out=[('gap',[s.Integer(16)])]
    for t,u in combinations_with_replacement((1,2,4,8,16),2):
        prod=(x-delta)*(x-t)**2*(x-u)**2
        b=1/(delta*t*t*u*u);a=b*(1/delta+s.Rational(2,t)+s.Rational(2,u))
        numerator=s.Poly(s.expand(1+prod*(a*x+b)),x)
        assert numerator.nth(0)==numerator.nth(1)==0
        q=[numerator.nth(j+2) for j in range(5)]
        assert s.expand(x*x*sum(c*x**j for j,c in enumerate(q))-1-prod*(a*x+b))==0
        assert a>0 and b>0
        out.append((f'quartic_t{t}_u{u}',q))
    assert len(out)==16
    return out


def load_inputs():
    manifest=json.loads((HERE/'BLOCK12_INPUT_MANIFEST.json').read_text())
    for row in manifest['sources']:assert sha(HERE/row['copy'])==row['sha256']
    inp=json.loads((HERE/'block12_inputs/quartic_inputs.json').read_text())
    fifth=json.loads((HERE/'block12_inputs/omega5_result.json').read_text())
    high=json.loads((HERE/'block12_inputs/omega79_result.json').read_text())
    assert fifth['status']=='CERTIFIED_TARGET' and high['status']=='COMPLETE_NEW_OMEGA79'
    moments={k:[I(*z) for z in inp['residual']['rows'][k]['moments']] for k in ('P','O')}
    for k in moments:
        assert inp['residual']['rows'][k]['moments']==inp['variational']['rows'][k]['moments']
    mu=3*moments['P'][1];nu=3*moments['O'][3]-4*mu
    env={A0:I(F(1,6),F(17,60)),C0:I(F(2,5),F(8,15)),ODD[1]:mu,ODD[3]:nu,ODD[5]:I(*fifth['interval'])}
    for row in high['rows']:
        assert row['status']=='CERTIFIED_TARGET'
        env[ODD[int(row['observable'][5:])]]=I(*row['interval'])
    return inp,moments,env,manifest


def check_formulas(env,accepted):
    formulas=json.loads((HERE/'BLOCK12_MOMENT_FORMULAS.json').read_text())
    assert formulas['helper_sha256']==sha(HERE/'block12_clifford.py')
    assert formulas['source_sha256']==sha(HERE/'derive_block12_moments.py')
    parsed={};comparisons=[]
    for kind in ('P','O'):
        parsed[kind]={source:[s.sympify(expr,locals=LOCALS) for expr in formulas['moments'][kind][source]] for source in ('vacuum','ward')}
        for n,expr in enumerate(parsed[kind]['vacuum']):
            derived=evaluate(expr,env);target=accepted[kind][n]
            if not derived.overlap(target):
                raise AssertionError(('vacuum_moment_disagreement',kind,n,derived.pair(),target.pair()))
            comparisons.append({'class':kind,'order':n,'overlap':True,'defining_input':n==1 or (kind=='O' and n==3)})
    p=s.symbols('p0:3',real=True);q=s.symbols('q0:3',real=True)
    total=0
    for a,c,m,count in CLASSES:
        total+=count*kernel(a,c,m,p if a=='P' else q,p if c=='P' else q)
    mu=ODD[1];nu=ODD[3]
    closed=60*p[0]**2+24*p[0]*q[0]+6*q[0]**2-312*p[2]**2-96*p[2]*q[2]-24*q[2]**2+72*(2*mu-nu/3)*p[1]*p[2]
    assert s.expand(total-closed)==0
    return parsed,comparisons,(p,q,closed)


def certify(scalar_override=None):
    start=time.monotonic();inp,accepted,env,manifest=load_inputs()
    if scalar_override is not None:
        assert set(scalar_override)=={A0,C0}
        env.update(scalar_override)
    formulas,comparisons,nominal_info=check_formulas(env,accepted)
    bounds=envelopes();results={}
    for mode,data in inp.items():
        rows={};a2=I(0);b2=I(0);E2=F(0);F2=F(0);coeffs={}
        for kind in ('P','O'):
            p=[s.Rational(z) for z in data['rows'][kind]['p']];coeffs[kind]=p
            r=[s.S.One,-p[0],-p[1],-p[2]]
            d=[sum(r[j]*r[n-j] for j in range(4) if 0<=n-j<4) for n in range(7)]
            errors={}
            for source in ('vacuum','ward'):
                moments=formulas[kind][source]
                residual=[s.expand(sum(d[k]*moments[k+j] for k in range(7))) for j in range(5)]
                candidates=[]
                for name,q in bounds:
                    value=evaluate(sum(c*residual[j] for j,c in enumerate(q)),env)
                    assert value.hi>=0,('negative_squared_norm_upper',mode,kind,source,name)
                    candidates.append({'name':name,'squared_error_enclosure':value.pair()})
                selected=min(candidates,key=lambda z:F(z['squared_error_enclosure'][1]))
                upper=root_hi(selected['squared_error_enclosure'][1])
                errors[source]={'selected':selected['name'],'squared_error_upper':selected['squared_error_enclosure'][1],
                                'error_upper':str(upper),'candidates':candidates}
            E=F(errors['vacuum']['error_upper']);Y=F(errors['ward']['error_upper'])
            w=root_hi(72*env[A0].hi if kind=='P' else 12);v_error=Y+w*E
            count=12 if kind=='P' else 3
            E2+=count*E*E;F2+=count*v_error*v_error
            normx,normv=(evaluate(z,env) for z in norm_formulas(kind,p))
            assert normx.hi>=0 and normv.hi>=0
            a2+=count*normx;b2+=count*normv
            rows[kind]={'p':[str(z) for z in p],'errors':errors,'Ward_norm_upper':str(w),
                        'v_error_upper':str(v_error),'x_trial_squared_norm':normx.pair(),'v_trial_squared_norm':normv.pair()}
        ps,qs,closed=nominal_info
        nominal=evaluate(closed.subs(dict(zip(ps,coeffs['P']))|dict(zip(qs,coeffs['O']))),env)
        E=root_hi(E2);FF=root_hi(F2);a=root_hi(a2.hi);b=root_hi(b2.hi)
        X=root_hi(240);V=root_hi(30720);chi=min(X,a+E);psi=min(V,b+FF)
        error=6*(E*(a+chi)+min(E*b+chi*FF,E*psi+a*FF))
        alpha=I((nominal.lo-error)/8,(nominal.hi+error)/8)
        results[mode]={'rows':rows,'nominal':nominal.pair(),'a_upper':str(a),'b_upper':str(b),
                       'E_upper':str(E),'F_upper':str(FF),'comparison_error':str(error),'alpha':alpha.pair(),
                       'status':'inconclusive_zero_in_interval' if alpha.lo<=0<=alpha.hi else 'conditional_sign_resolved'}
    seconds=time.monotonic()-start
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes=rss if sys.platform=='darwin' else rss*1024
    assert seconds<=60 and rss_bytes<=384*1024**2,('budget_exceeded',seconds,rss_bytes)
    return {'status':'completed_fixed_first_protocol','scope':'conditional on named native source, gap and supplied scalar certificates; author arithmetic check',
            'seconds':seconds,'peak_rss_bytes':rss_bytes,'source_sha256':sha(__file__),
            'protocol_sha256':sha(HERE/'BLOCK12_TWO_SOURCE_PROTOCOL.md'),
            'helper_sha256':{name:sha(HERE/name) for name in ('block12_clifford.py','block12_nominal.py')},
            'input_manifest':manifest,'scalar_inputs':{str(k):v.pair() for k,v in env.items()},
            'vacuum_moment_comparisons':comparisons,'weighted_nominal_identity':True,'results':results}


if __name__=='__main__':
    def deadline(signum,frame):raise TimeoutError('fixed60secondbudget')
    signal.signal(signal.SIGALRM,deadline);signal.alarm(60)
    result=certify();signal.alarm(0)
    (HERE/'BLOCK12_TWO_SOURCE_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    for mode,row in result['results'].items():
        print(mode,row['status'],'N=',[float(F(x)) for x in row['nominal']],
              'alpha=',[float(F(x)) for x in row['alpha']],
              'E=',float(F(row['E_upper'])),'F=',float(F(row['F_upper'])))
        for kind,data in row['rows'].items():print(kind,{k:(v['selected'],float(F(v['error_upper']))) for k,v in data['errors'].items()})
    print('seconds',result['seconds'],'peak_rss_bytes',result['peak_rss_bytes'])
