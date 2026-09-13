"""Exact rational arithmetic for the elementary native scalar witness.

Every radial supplier comes from exact counts and explicit series tails.
The infinite operator and physical-scope arguments are in the source note.
"""
import ast
from collections import Counter
from itertools import combinations
from fractions import Fraction as F
from math import comb,isqrt
from pathlib import Path
import hashlib,json,time,resource,sys
AUDIT_TIMEOUT_SEC = 60
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'.claude/science/physics-loops/native-positive-ward-scalar-20260913'
NOTE=ROOT/'docs/NATIVE_POSITIVE_WARD_SCALAR_BOUNDED_THEOREM_NOTE_2026-09-13.md'
VARIABLES=('A0','C0','L1','L3','L5','L7','L9');ZERO=(0,)*len(VARIABLES)


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):
    values=[a[0]*b[0],a[1]*b[1]];return min(values),max(values)
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




def elementary_scalars(N=256):
    assert N==256;probabilities=[F(comb(2*n,n)*sum(comb(n,j)**2*comb(2*j,j) for j in range(n+1)),36**n) for n in range(N+1)]
    total=sum(probabilities);nroot=isqrt(N);assert nroot*nroot==N
    tail=F(2,nroot);assert tail>0 and tail*tail*N==4
    assert probabilities[0]==1 and probabilities[1]==F(1,6) and probabilities[2]==F(5,72)
    env={'A0':(total/6,(total+tail)/6)}
    root_hi=root(F(6));root_lo=root_hi-F(1,1<<128);assert root_lo**2<=6<=root_hi**2
    rows=[]
    for r in (-1,1,3,5,7,9):
        exponent=F(r,2);coef=F(1);weighted=F(1)
        for n in range(1,N+2):
            m=2*n-2;coef=coef*(exponent-m)*(exponent-m-1)/((m+1)*(m+2))
            if n<=N:weighted+=coef*probabilities[n]
        omitted=coef;assert 0<(exponent-2*N-2)*(exponent-2*N-3)/((2*N+3)*(2*N+4))<1
        lo=weighted+min(F(0),omitted*tail);hi=weighted+max(F(0),omitted*tail)
        # 6^(r/2)=6^((r-1)/2)*sqrt6, with r=-1 handled exactly.
        prefactor=F(6)**((r-1)//2);value=(prefactor*root_lo*lo,prefactor*root_hi*hi)
        assert value[0]>0 and value[0]<=value[1]
        env['C0' if r==-1 else 'L'+str(r)]=value
        rows.append({'r':r,'last_coefficient':str(omitted),'interval':[str(v) for v in value]})
    return env,{'N':N,'return_partial_sum':str(total),'return_tail_upper':str(tail),'rows':rows}




def gap_bounds(env):
    start=time.monotonic();a=F(17,60)
    assert env['A0'][1]<a
    # Polynomial division proves the elementary positive-integral pi bound.
    remainder=[F(0)]*4+[F(1),F(-4),F(6),F(-4),F(1)];quotient=[F(0)]*7
    for j in range(8,1,-1):
        quotient[j-2]=remainder[j];remainder[j-2]-=remainder[j];remainder[j]=0
    assert remainder[:2]==[-4,0] and not any(remainder[2:])
    assert sum(c/F(j+1) for j,c in enumerate(quotient))==F(22,7)
    assert 27*F(22,7)**3<1024
    assert F(177,686)>F(1,4)
    P=[F(1,9),F(0),4*a/9+8*a*a,F(0),4*a*a/9]
    assert sum(P)<1
    w=[1-P[0]]+[-v for v in P[1:]];poly=[F(1)];local=F(0)
    for n in range(1,13):
        poly=convolution(poly,w);local+=sum(c/F(j+1) for j,c in enumerate(poly))/n
    local*=F(7,44)
    tail=F(7,44)*sum(F(1,16)*(24-8/F(j,16)**2)/(F(j+1,16)**2+7)**2 for j in range(16,320))
    total=local+tail;assert total>F(1,4)
    # Removing the tail does not prove the claimed1/4 gap in this certificate.
    assert local<F(1,4)
    return {'status':'exact_gap_inequalities_passed','P_local':str(local),'P_tail':str(tail),'P_total':str(total),
            'O_lower':'177/686','A0_elementary_upper':str(env['A0'][1]),
            'omitted_positive_tail_competitor_rejected':True,'seconds':time.monotonic()-start,
            'source_sha256':sha(__file__),'derivation_sha256':sha(NOTE),
            'scope':'finite rational inequalities; determinant, GNS convergence and core arguments are analytical proof obligations in the note'}


def run():
    start=time.monotonic()
    assert mul((F(-2),F(3)),(F(-5),F(7)))==(F(-15),F(21))
    test_env={name:(F(0),F(0)) for name in VARIABLES}
    test_env.update(A0=(F(1),F(2)),C0=(F(3),F(4)),L1=(F(2),F(3)),L3=(F(5),F(6)))
    assert parse('A0*(L1-L3)').interval(test_env)==(F(-8),F(-2))
    env,scalar_record=elementary_scalars()
    witness=json.loads((HERE/'WITNESS.json').read_text())
    witness={name:{kind:[F(v) for v in values] for kind,values in witness[name].items()} for name in ('p','q')}
    gap_result=gap_bounds(env)
    raw=json.loads((HERE/'MOMENT_FORMULAS.json').read_text())['moments']
    formulas=json.loads((HERE/'TRIAL_FORMULAS.json').read_text())
    Q=envelope(F(1,4),F(4),F(8));E2=F(0);F2=F(0);a2=F(0);b2=F(0);rows={}
    for kind in ('P','O'):
        errors={}
        for source,p in (('vacuum',witness['p'][kind]),('ward',witness['q'][kind])):
            m=[parse(z) for z in raw[kind][source]];d=convolution([F(1)]+[-v for v in p],[F(1)]+[-v for v in p])
            expr=Polynomial.constant(0)
            for j,c in enumerate(Q):
                for k,e in enumerate(d):expr=expr+m[j+k].scale(c*e)
            interval=expr.interval(env);assert interval[1]>=0
            errors[source]=root(interval[1])
        E=errors['vacuum'];Y=errors['ward'];w=root(72*env['A0'][1] if kind=='P' else F(12))
        count=12 if kind=='P' else 3;E2+=count*E**2;F2+=count*(Y+w*E)**2
        vals=coefficients(witness['p'][kind],'p')|coefficients(witness['q'][kind],'q')
        nx,nv=[parse(z,vals).interval(env) for z in formulas['norms'][kind]]
        assert nx[1]>=0 and nv[1]>=0;a2+=count*nx[1];b2+=count*nv[1]
        rows[kind]={'E':str(E),'Y':str(Y),'W':str(w),'nx':list(map(str,nx)),'nv':list(map(str,nv))}
    vals=coefficients(witness['p']['P'],'p')|coefficients(witness['p']['O'],'r')|coefficients(witness['q']['P'],'q')|coefficients(witness['q']['O'],'u')
    nominal=parse(formulas['complete_nominal'],vals).interval(env)
    a,b,E,FF=map(root,(a2,b2,E2,F2));err=6*(E*(2*a+E+b+FF)+a*FF)
    alpha=((nominal[0]-err)/8,(nominal[1]+err)/8)
    coarse=(F(1871,200),F(2724,125),F(1473,1000),F(1761,125))
    assert all(x<y for x,y in zip((a,b,E,FF),coarse))
    aa,bb,ee,ff=coarse;coarse_error=6*(ee*(2*aa+ee+bb+ff)+aa*ff)
    assert 1345<nominal[0]<=nominal[1]<1347 and coarse_error<1287
    assert (1345-coarse_error)/8>7 and (1347+coarse_error)/8<330
    seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes=rss if sys.platform=='darwin' else rss*1024
    assert seconds<60 and rss_bytes<=384*1024**2
    return {'status':'conditional_positive_native_ward_scalar' if alpha[0]>0 else 'inconclusive_elementary_candidate','alpha':list(map(str,alpha)),
            'p':{k:list(map(str,v)) for k,v in witness['p'].items()},'q':{k:list(map(str,v)) for k,v in witness['q'].items()},
            'norms':{k:str(v) for k,v in zip(('a','b','E','F'),(a,b,E,FF))},'nominal':list(map(str,nominal)),
            'error':str(err),'source_rows':rows,'coarse_interval':['7','330'],'coarse_error':str(coarse_error),
            'peak_rss_bytes':rss_bytes,'scalar_certificate':scalar_record,
            'seconds':seconds,'source_sha256':sha(__file__),'note_sha256':sha(NOTE),
            'gap_bounds':gap_result,
            'dependencies_sha256':{n:sha(HERE/n) for n in ('WITNESS.json','MOMENT_FORMULAS.json','TRIAL_FORMULAS.json')},
            'scope':'elementary exact rational witness for the supplied native model; infinite analytical arguments are in the note; physical Dirac interpretation is a separate bridge'}
