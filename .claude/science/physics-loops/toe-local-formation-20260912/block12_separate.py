"""Exact enlarged CAR table for distinct vacuum and Ward-source polynomials."""
from functools import lru_cache
import sympy as s
from block12_clifford import Algebra,A0,C0,ODD
from block12_nominal import CrossAlgebra,CLASSES


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
        difference=self.collect(list(xq.items())+[(w,-c) for w,c in xp.items()])
        w={(self.lookup[('w'+which,0)],):s.S.One}
        v=self.collect(list(self.product(w,difference).items())+list(vq.items()))
        g={(self.lookup[('a',0)],):s.S.One}
        return xp,v,self.product(g,v)


def kernel(kindA,kindC,opposites,pA,pC,qA):
    alg=SeparateAlgebra(kindA,kindC,opposites)
    xA,_,gvA=alg.trials('A',pA,qA);xC,_,_=alg.local_trials('C',pC)
    return s.factor(s.re(alg.expectation(alg.product(xC,xA,adjoint_first=True))-alg.expectation(alg.product(xC,gvA,adjoint_first=True))))


def norms(kind,p,q):
    alg=SeparateAlgebra(kind,kind,0);x,v,_=alg.trials('A',p,q)
    return tuple(s.factor(alg.expectation(alg.product(z,z,adjoint_first=True))) for z in (x,v))
