#!/usr/bin/env python3
"""Standard-library rational verifier of a frozen native sign witness.

No SymPy, NumPy, optimizer, imported certification helper or Fock solver.
The physical identities and supplied scalar certificates remain hypotheses.
"""
import ast
from collections import Counter
from itertools import combinations
from fractions import Fraction as F
from math import comb,isqrt
from pathlib import Path
import hashlib,json,time
HERE=Path(__file__).resolve().parent
VARIABLES=('A0','C0','L1','L3','L5','L7','L9');ZERO=(0,)*len(VARIABLES)


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):
    values=[x*y for x in a for y in b];return min(values),max(values)
def power(a,n):
    out=(F(1),F(1))
    for _ in range(n):out=mul(out,a)
    return out


def root(q):
    assert q>=0;scale=1<<128;n=isqrt((q.numerator*scale*scale)//q.denominator)
    if F(n*n,scale*scale)<q:n+=1
    result=F(n,scale);assert result**2>=q
    return result


class Polynomial:
    def __init__(self,terms):self.terms={k:F(v) for k,v in terms.items() if v}
    @staticmethod
    def constant(c):return Polynomial({ZERO:F(c)})
    def __add__(self,b):
        out=dict(self.terms)
        for k,v in b.terms.items():out[k]=out.get(k,F(0))+v
        return Polynomial(out)
    def __neg__(self):return Polynomial({k:-v for k,v in self.terms.items()})
    def __sub__(self,b):return self+-b
    def __mul__(self,b):
        out={}
        for a,c in self.terms.items():
            for d,e in b.terms.items():
                k=tuple(x+y for x,y in zip(a,d));out[k]=out.get(k,F(0))+c*e
        return Polynomial(out)
    def scale(self,c):return Polynomial({k:v*c for k,v in self.terms.items()})
    def __pow__(self,n):
        assert 0<=n<=20;out=Polynomial.constant(1)
        for _ in range(n):out=out*self
        return out
    def interval(self,env):
        # Collect the whole coefficient of each Green scalar before bounding it.
        groups={}
        for powers,c in self.terms.items():
            assert powers[0]+powers[1]<=1
            z=(c,c)
            for variable,n in zip(VARIABLES[2:],powers[2:]):z=mul(z,power(env[variable],n))
            key=powers[:2];groups[key]=add(groups.get(key,(F(0),F(0))),z)
        out=(F(0),F(0))
        for (a,c),value in groups.items():out=add(out,mul(value,mul(power(env['A0'],a),power(env['C0'],c))))
        return out


def parse(text,constants=None):
    constants={} if constants is None else constants
    def visit(node):
        if isinstance(node,ast.Constant):
            assert isinstance(node.value,int);return Polynomial.constant(node.value)
        if isinstance(node,ast.Name):
            if node.id in constants:return Polynomial.constant(constants[node.id])
            assert node.id in VARIABLES,node.id
            powers=[0]*len(VARIABLES);powers[VARIABLES.index(node.id)]=1
            return Polynomial({tuple(powers):1})
        if isinstance(node,ast.UnaryOp):
            assert isinstance(node.op,(ast.UAdd,ast.USub));v=visit(node.operand)
            return v if isinstance(node.op,ast.UAdd) else -v
        assert isinstance(node,ast.BinOp)
        a=visit(node.left)
        if isinstance(node.op,ast.Pow):
            assert isinstance(node.right,ast.Constant) and isinstance(node.right.value,int)
            return a**node.right.value
        b=visit(node.right)
        if isinstance(node.op,ast.Add):return a+b
        if isinstance(node.op,ast.Sub):return a-b
        if isinstance(node.op,ast.Mult):return a*b
        assert isinstance(node.op,ast.Div) and set(b.terms)=={ZERO}
        return a.scale(1/b.terms[ZERO])
    return visit(ast.parse(text,mode='eval').body)


def convolution(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,c in enumerate(a):
        for j,d in enumerate(b):out[i+j]+=c*d
    return out


def envelope(delta,t,u):
    prod=[F(1)]
    for point in (delta,t,t,u,u):prod=convolution(prod,[-point,F(1)])
    b=1/(delta*t*t*u*u);a=b*(1/delta+2/t+2/u)
    numerator=convolution(prod,[b,a]);numerator[0]+=1
    assert numerator[:2]==[0,0] and delta>0 and t>0 and u>0 and a>0 and b>0
    # This establishes x²Q(x)-1=(x-delta)(x-t)²(x-u)²(ax+b).
    return numerator[2:]


def coefficients(values,prefix):return {prefix+str(j):F(v) for j,v in enumerate(values)}


def load(witness):
    for name,value in witness['dependencies'].items():assert sha(HERE/name)==value
    manifest=json.loads((HERE/'BLOCK12_INPUT_MANIFEST.json').read_text())
    for row in manifest['sources']:assert sha(HERE/row['copy'])==row['sha256']
    green_manifest=json.loads((HERE/'BLOCK12_GREEN_INPUT_MANIFEST.json').read_text())
    assert sha(HERE/green_manifest['copy'])==green_manifest['sha256']
    green=json.loads((HERE/green_manifest['copy']).read_text())
    row=next(r for r in green['rows'] if r['s']=='0');assert row['status']=='CERTIFIED_TARGET'
    env={'A0':tuple(map(F,row['A']))}
    supplied=json.loads((HERE/'block12_inputs/quartic_inputs.json').read_text())
    rows=supplied['variational']['rows']
    for kind in ('P','O'):assert witness['p'][kind]==rows[kind]['p']
    m1=tuple(map(F,rows['P']['moments'][1]));m3=tuple(map(F,rows['O']['moments'][3]))
    env['L1']=(3*m1[0],3*m1[1])
    env['L3']=(3*m3[0]-4*env['L1'][1],3*m3[1]-4*env['L1'][0])
    fifth=json.loads((HERE/'block12_inputs/omega5_result.json').read_text());assert fifth['status']=='CERTIFIED_TARGET'
    env['L5']=tuple(map(F,fifth['interval']))
    high=json.loads((HERE/'block12_inputs/omega79_result.json').read_text());assert high['status']=='COMPLETE_NEW_OMEGA79'
    for row in high['rows']:
        assert row['status']=='CERTIFIED_TARGET';env['L'+row['observable'][5:]]=tuple(map(F,row['interval']))
    N=witness['return_series_N'];assert N==256;total=F(0);weighted=F(0)
    for n in range(N+1):
        probability=F(comb(2*n,n)*sum(comb(n,j)**2*comb(2*j,j) for j in range(n+1)),36**n)
        total+=probability;weighted+=F(comb(4*n,2*n),16**n)*probability
    tail=6*env['A0'][1]-total;assert tail>=0
    upper=root(F(1,6));lower=upper-F(1,1<<128)
    assert lower**2<=F(1,6)<=upper**2
    env['C0']=(lower*weighted,upper*(weighted+F(comb(4*N+4,2*N+2),16**(N+1))*tail))
    # Coarsen outward to simple decimal rational suppliers; never use midpoints.
    scale=10**16
    env={name:(F((lo*scale).numerator//(lo*scale).denominator,scale),
               F(-((-hi*scale).numerator//(-hi*scale).denominator),scale)) for name,(lo,hi) in env.items()}
    return env


def verify():
    started=time.monotonic();witness=json.loads((HERE/'BLOCK12_SIGN_WITNESS.json').read_text());env=load(witness)
    raw=json.loads((HERE/'BLOCK12_MOMENT_FORMULAS.json').read_text())['moments']
    formulas=json.loads((HERE/'BLOCK12_SEPARATE_FORMULAS.json').read_text())
    Q=envelope(*[F(witness['envelope'][key]) for key in ('delta','t','u')])
    E2=F(0);F2=F(0);a2=F(0);b2=F(0);source_bounds={}
    for kind in ('P','O'):
        errors={}
        for source,coeff in (('vacuum',witness['p'][kind]),('ward',witness['q'][kind])):
            moments=[parse(expr) for expr in raw[kind][source]]
            r=[F(1)]+[-F(z) for z in coeff];d=convolution(r,r)
            expression=Polynomial.constant(0)
            for j,c in enumerate(Q):
                for k,e in enumerate(d):expression=expression+moments[j+k].scale(c*e)
            interval=expression.interval(env);assert interval[1]>=0
            errors[source]=(interval,root(interval[1]))
        E=errors['vacuum'][1];Y=errors['ward'][1];w=root(72*env['A0'][1] if kind=='P' else F(12))
        count=12 if kind=='P' else 3;E2+=count*E**2;F2+=count*(Y+w*E)**2
        constants=coefficients(witness['p'][kind],'p')|coefficients(witness['q'][kind],'q')
        nx,nv=[parse(expr,constants).interval(env) for expr in formulas['norms'][kind]]
        assert nx[1]>=0 and nv[1]>=0;a2+=count*nx[1];b2+=count*nv[1]
        source_bounds[kind]={'E_upper':str(E),'Y_upper':str(Y),'x_squared_upper':str(nx[1]),'v_squared_upper':str(nv[1])}
    constants=coefficients(witness['p']['P'],'p')|coefficients(witness['p']['O'],'r')|coefficients(witness['q']['P'],'q')|coefficients(witness['q']['O'],'u')
    nominal_poly=parse(formulas['complete_nominal'],constants)
    pairs=list(combinations(range(6),2));counts=Counter()
    for A in pairs:
        for C in pairs:
            if set(A)&set(C):continue
            ka='O' if A[0]//2==A[1]//2 else 'P'
            kc='O' if C[0]//2==C[1]//2 else 'P'
            opposite=sum(a//2==c//2 for a in A for c in C)
            counts[(ka,kc,opposite)]+=1
    assert counts==Counter({(r['A'],r['C'],r['opposites']):r['multiplicity'] for r in formulas['kernels']})
    assert sum(counts.values())==90
    weighted=Polynomial.constant(0)
    for row in formulas['kernels']:
        local=coefficients(witness['p'][row['A']],'p')|coefficients(witness['p'][row['C']],'r')|coefficients(witness['q'][row['A']],'q')
        weighted=weighted+parse(row['expression'],local).scale(row['multiplicity'])
    assert not (nominal_poly-weighted).terms
    nominal=nominal_poly.interval(env)
    actual={'a':root(a2),'b':root(b2),'E':root(E2),'F':root(F2)}
    bounds={k:F(v) for k,v in witness['rounded_bounds'].items() if k!='nominal'}
    for name,value in actual.items():assert value<bounds[name],(name,float(value),float(bounds[name]))
    nlo,nhi=map(F,witness['rounded_bounds']['nominal']);assert nlo<nominal[0]<=nominal[1]<nhi
    a,b,E,FF=(bounds[key] for key in ('a','b','E','F'))
    error=6*(E*(2*a+E+b+FF)+a*FF)
    assert error<891
    alpha=((nlo-error)/8,(nhi+error)/8);clo,chi=map(F,witness['certificate_interval'])
    assert clo<alpha[0]<=alpha[1]<chi and clo>0
    return {'status':'conditional_positive_sign_witness_verified','interval':[str(clo),str(chi)],
            'units':'h^2 alpha','rounded_comparison_error':str(error),'rounded_alpha_enclosure':[str(z) for z in alpha],
            'computed_norm_bounds':{k:str(v) for k,v in actual.items()},'computed_nominal':[str(z) for z in nominal],
            'source_bounds':source_bounds,'coarsened_scalar_intervals':{k:[str(v) for v in z] for k,z in env.items()},
            'seconds':time.monotonic()-started,'source_sha256':sha(__file__),'witness_sha256':sha(HERE/'BLOCK12_SIGN_WITNESS.json'),
            'scope':'stdlib rational arithmetic and coefficient consistency; native algebra, gap and supplied source certificates remain conditional, independent source review pending'}


if __name__=='__main__':
    result=verify();(HERE/'BLOCK12_SIGN_WITNESS_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result['status'],result['units'],result['interval'],'error',float(F(result['rounded_comparison_error'])),'seconds',result['seconds'])
