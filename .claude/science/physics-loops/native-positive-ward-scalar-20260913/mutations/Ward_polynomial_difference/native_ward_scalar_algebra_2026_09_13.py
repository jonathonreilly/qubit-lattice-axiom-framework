"""Formal Clifford recurrence for native vacuum and Ward-source moments.

The covariance table is algebraic. Rational trial coefficients are supplied
separately as a witness, and finite Fock checks use different machinery.
"""
from __future__ import annotations
AUDIT_TIMEOUT_SEC = 60
from functools import lru_cache
from math import comb, factorial
import sympy as s

A0,C0=s.symbols('A0 C0',real=True)
ODD={r:s.Symbol(f'L{r}',real=True) for r in (1,3,5,7,9,11)}
ODD[-1]=C0


@lru_cache(None)
def radial(n):
    return sum(factorial(n)//(factorial(a)*factorial(b)*factorial(n-a-b))*
               comb(2*a,a)*comb(2*b,b)*comb(2*(n-a-b),n-a-b)
               for a in range(n+1) for b in range(n-a+1))


class Algebra:
    def __init__(self,kind):
        assert kind in ('P','O');self.kind=kind
        self.labels=[('w',0)]+[(typ,j) for j in range(6) for typ in ('a','d')]
        self.lookup={v:i for i,v in enumerate(self.labels)}

    def D(self,n):
        return s.Integer(2*radial(n)) if self.kind=='P' else s.Rational(radial(n+1),3)

    def F(self,r):
        return 2*ODD[r] if self.kind=='P' else ODD[r+2]/3

    @lru_cache(None)
    def table(self,f,g):
        typ,i=self.labels[f];other,j=self.labels[g]
        if typ=='w' and other=='w':return (72*A0 if self.kind=='P' else s.Integer(12)),s.S.Zero
        if other=='w':
            dot,kap=self.table(g,f);return dot,-kap
        if typ=='w':
            if other=='a':
                if j%2==0:return s.Integer(2*(-1)**(j//2)*radial(j//2)),s.S.Zero
                return s.S.Zero,-2*(-1)**((j-1)//2)*ODD[j]
            if j%2:return -6*(-1)**((j-1)//2)*self.D((j-1)//2),s.S.Zero
            return s.S.Zero,-6*(-1)**(j//2)*self.F(j-1)
        if typ=='d' and other=='a':
            dot,kap=self.table(g,f);return dot,-kap
        m=i+j
        if typ==other:
            if m%2==0:return (-1)**(i+m//2)*(s.Integer(radial(m//2)) if typ=='a' else self.D(m//2)),s.S.Zero
            return s.S.Zero,(-1)**(i+(m+1)//2)*(ODD[m] if typ=='a' else self.F(m))
        if m%2:return s.Rational((-1)**(i+(m+1)//2)*radial((m+1)//2),3),s.S.Zero
        return s.S.Zero,(-1)**(i+m//2+1)*ODD[m+1]/3

    @staticmethod
    def collect(items):
        out={}
        for word,value in items:
            out[word]=out.get(word,0)+value
        return {word:s.expand(value) for word,value in out.items() if value!=0}

    @lru_cache(None)
    def left(self,i,word):
        if not word:return {(i,):s.S.One}
        j=word[0]
        if i<j:return {(i,)+word:s.S.One}
        if i==j:return {word[1:]:self.table(i,i)[0]}
        items=[((j,)+w,-value) for w,value in self.left(i,word[1:]).items()]
        items.append((word[1:],2*self.table(i,j)[0]))
        return self.collect(items)

    @lru_cache(None)
    def normal(self,word):
        out={():s.S.One}
        for i in reversed(word):
            out=self.collect((w,x*y) for v,x in out.items() for w,y in self.left(i,v).items())
        return out

    def product(self,a,b,adjoint_first=False):
        return self.collect((v,(s.conjugate(x) if adjoint_first else x)*y*z)
                            for w,x in a.items() for u,y in b.items()
                            for v,z in self.normal((w[::-1] if adjoint_first else w)+u).items())

    def step(self,poly):
        items=[]
        # [H0, .] is an ordinary derivation because H0 is even.
        for word,x in poly.items():
            for position,field in enumerate(word):
                typ,power=self.labels[field]
                new=self.lookup[('d',0)] if typ=='w' else self.lookup[(typ,power+1)]
                factor=6*s.I if typ=='w' else s.I
                rewritten=word[:position]+(new,)+word[position+1:]
                items.extend((w,x*factor*z) for w,z in self.normal(rewritten).items())
        # The defect B_A=i gamma(a)gamma(d) multiplies on the left.
        for word,x in poly.items():
            rewritten=(self.lookup[('a',0)],self.lookup[('d',0)])+word
            items.extend((w,s.I*x*z) for w,z in self.normal(rewritten).items())
        return self.collect(items)

    @lru_cache(None)
    def wick(self,word):
        if not word:return s.S.One
        if len(word)%2:return s.S.Zero
        i=word[0];value=s.S.Zero
        for position in range(1,len(word)):
            j=word[position];dot,kap=self.table(i,j)
            value+=(-1)**(position-1)*(dot+s.I*kap)*self.wick(word[1:position]+word[position+1:])
        return s.expand(value)

    def expectation(self,poly):
        return s.expand(sum(x*self.wick(word) for word,x in poly.items()))

    def moments(self,ward,max_n=10):
        state={(self.lookup[('w',0)],):s.S.One} if ward else {():s.S.One}
        states=[state]
        for _ in range((max_n+1)//2):states.append(self.step(states[-1]))
        values=[]
        for n in range(max_n+1):
            left=n//2;right=n-left
            values.append(self.expectation(self.product(states[left],states[right],adjoint_first=True)))
        return values,[len(x) for x in states]


class CrossAlgebra(Algebra):
    def __init__(self,kindA,kindC,opposites):
        self.kindA=kindA;self.kindC=kindC;self.opposites=opposites
        self.labels=[('a',0),('a',1),('A',0),('A',1),('C',0),('C',1)]
        self.lookup={v:i for i,v in enumerate(self.labels)}

    @lru_cache(None)
    def table(self,f,g):
        typ,i=self.labels[f];other,j=self.labels[g];mu=ODD[1];nu=ODD[3]
        if typ=='a' and other=='a':
            if i==j:return s.Integer(1 if i==0 else 6),s.S.Zero
            return s.S.Zero,(-1 if i==0 else 1)*mu
        if other=='a':
            dot,kap=self.table(g,f);return dot,-kap
        if typ=='a':
            if i+j==1:return s.Integer(2 if i==1 else -2),s.S.Zero
            return s.S.Zero,-(mu if i+j==0 else nu)/3
        if typ==other:
            n=2;m=2 if (self.kindA if typ=='A' else self.kindC)=='O' else 0
        else:n=0;m=self.opposites
        if i==j:return s.Integer(n if i==0 else 6*n+m),s.S.Zero
        z=mu*n+(nu/6-mu)*m
        return s.S.Zero,(-1 if i==0 else 1)*z

    def trials(self,which,p):
        a=self.lookup[('a',0)];k=self.lookup[('a',1)]
        d=self.lookup[(which,0)];kd=self.lookup[(which,1)]
        x=self.collect([((),-p[0]-2*p[2]),((a,d),-s.I*p[1]),
                        ((k,d),p[2]),((a,kd),p[2])])
        v={(d,):-2*s.I*p[1],(kd,):2*p[2]}
        gv=self.product({(a,):s.S.One},v)
        return x,v,gv


def common_kernel(kindA,kindC,opposites,pA,pC):
    alg=CrossAlgebra(kindA,kindC,opposites)
    xA,vA,gvA=alg.trials('A',pA);xC,_,_=alg.trials('C',pC)
    direct=alg.expectation(alg.product(xC,xA,adjoint_first=True))
    mixed=alg.expectation(alg.product(xC,gvA,adjoint_first=True))
    return s.factor(s.re(direct-mixed))


def common_norms(kind,p):
    alg=CrossAlgebra(kind,kind,0)
    x,v,_=alg.trials('A',p)
    return (s.factor(alg.expectation(alg.product(x,x,adjoint_first=True))),
            s.factor(alg.expectation(alg.product(v,v,adjoint_first=True))))


CLASSES=(('O','O',0,6),('O','P',0,12),('P','O',0,12),('P','P',2,12),('P','P',1,48))


class SeparateAlgebra(Algebra):
    def __init__(self,kindA,kindC,opposites):
        self.kindA=kindA;self.kindC=kindC;self.opposites=opposites
        self.local=CrossAlgebra(kindA,kindC,opposites)
        self.labels=[('wA',0),('wC',0)]+self.local.labels
        self.lookup={v:i for i,v in enumerate(self.labels)}

    def nm(self,which,other):
        if which!=other:return 0,self.opposites
        return 2,2 if (self.kindA if which=='A' else self.kindC)=='O' else 0

    @lru_cache(None)
    def table(self,f,g):
        if f>=2 and g>=2:return self.local.table(f-2,g-2)
        if f>=2:
            dot,kap=self.table(g,f);return dot,-kap
        which='A' if f==0 else 'C'
        if g<2:
            n,m=self.nm(which,'A' if g==0 else 'C')
            return 36*((n-m)*A0+s.Rational(m,6)),s.S.Zero
        typ,power=self.labels[g]
        if typ=='a':return (s.Integer(2),s.S.Zero) if power==0 else (s.S.Zero,-2*ODD[1])
        n,m=self.nm(which,typ)
        if power==1:return s.Integer(-6*n),s.S.Zero
        return s.S.Zero,-6*((n-m)*C0+s.Rational(m,6)*ODD[1])

    def local_trials(self,which,p):
        old=self.local.trials(which,p)
        return tuple({tuple(j+2 for j in w):c for w,c in poly.items()} for poly in old)

    def trials(self,which,p,q):
        xp,_,_=self.local_trials(which,p);xq,vq,_=self.local_trials(which,q)
        difference={}
        w={(self.lookup[('w'+which,0)],):s.S.One}
        v=self.collect(list(self.product(w,difference).items())+list(vq.items()))
        g={(self.lookup[('a',0)],):s.S.One}
        return xp,v,self.product(g,v)


def separate_kernel(kindA,kindC,opposites,pA,pC,qA):
    alg=SeparateAlgebra(kindA,kindC,opposites)
    xA,_,gvA=alg.trials('A',pA,qA);xC,_,_=alg.local_trials('C',pC)
    return s.factor(s.re(alg.expectation(alg.product(xC,xA,adjoint_first=True))-alg.expectation(alg.product(xC,gvA,adjoint_first=True))))


def separate_norms(kind,p,q):
    alg=SeparateAlgebra(kind,kind,0);x,v,_=alg.trials('A',p,q)
    return tuple(s.factor(alg.expectation(alg.product(z,z,adjoint_first=True))) for z in (x,v))


from pathlib import Path
import json
DATA=Path(__file__).resolve().parents[1]/'.claude/science/physics-loops/native-positive-ward-scalar-20260913'


def run():
    checks=[]
    from native_ward_scalar_arithmetic_2026_09_13 import envelope,F
    z=s.Symbol('spectral_parameter')
    qcoef=envelope(F(1,4),F(4),F(8))
    majorant=sum(s.Rational(c.numerator,c.denominator)*z**j for j,c in enumerate(qcoef))
    assert s.expand(z*z*majorant-1-(z-s.Rational(1,4))*(z-4)**2*(z-8)**2*(19*z+4)/1024)==0
    checks.append('quartic_majorant_coefficient_identity')
    raw=json.loads((DATA/'MOMENT_FORMULAS.json').read_text())['moments']
    forms=json.loads((DATA/'TRIAL_FORMULAS.json').read_text())
    p=s.symbols('p0:3',real=True);r=s.symbols('r0:3',real=True)
    q=s.symbols('q0:3',real=True);u=s.symbols('u0:3',real=True)
    local={str(x):x for x in [A0,C0]+list(ODD.values())+list(p+r+q+u)}
    for kind in ('P','O'):
        alg=Algebra(kind)
        for source,ward in (('vacuum',False),('ward',True)):
            values,_=alg.moments(ward)
            for n,value in enumerate(values):
                assert s.expand(value-s.sympify(raw[kind][source][n],locals=local))==0,(kind,source,n)
                checks.append(f'{kind}_{source}_moment_{n}')
    total=0
    assert [(x['A'],x['C'],x['opposites'],x['multiplicity']) for x in forms['kernels']]==list(CLASSES)
    for row in forms['kernels']:
        ka,kc,m,count=row['A'],row['C'],row['opposites'],row['multiplicity']
        value=separate_kernel(ka,kc,m,p,r,q)
        assert s.expand(value-s.sympify(row['expression'],locals=local))==0
        assert s.expand(value.subs(dict(zip(q,p)))-common_kernel(ka,kc,m,p,r))==0
        checks.extend([f'{ka}{kc}_{m}_kernel',f'{ka}{kc}_{m}_common_limit'])
        total+=count*separate_kernel(ka,kc,m,p if ka=='P' else r,p if kc=='P' else r,q if ka=='P' else u)
    assert s.expand(total-s.sympify(forms['complete_nominal'],locals=local))==0
    checks.append('complete_signed_nominal')
    for kind in ('P','O'):
        nx,nv=separate_norms(kind,p,q)
        for n,value in enumerate((nx,nv)):
            assert s.expand(value-s.sympify(forms['norms'][kind][n],locals=local))==0
            checks.append(f'{kind}_trial_norm_{n}')
        assert s.expand(nv.subs(dict(zip(q,p)))-common_norms(kind,p)[1])==0
        checks.append(f'{kind}_common_norm_limit')
    return {'status':'passed','checks':checks,'count':len(checks),
             'scope':'exact coefficient identities; finite native Fock checks use separate machinery'}
