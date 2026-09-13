"""Exact signed kernels for the new quadratic commutator Ward trial."""
from functools import lru_cache
import sympy as s
from block12_clifford import Algebra,ODD


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


def kernel(kindA,kindC,opposites,pA,pC):
    alg=CrossAlgebra(kindA,kindC,opposites)
    xA,vA,gvA=alg.trials('A',pA);xC,_,_=alg.trials('C',pC)
    direct=alg.expectation(alg.product(xC,xA,adjoint_first=True))
    mixed=alg.expectation(alg.product(xC,gvA,adjoint_first=True))
    return s.factor(s.re(direct-mixed))


def norm_formulas(kind,p):
    alg=CrossAlgebra(kind,kind,0)
    x,v,_=alg.trials('A',p)
    return (s.factor(alg.expectation(alg.product(x,x,adjoint_first=True))),
            s.factor(alg.expectation(alg.product(v,v,adjoint_first=True))))


CLASSES=(('O','O',0,6),('O','P',0,12),('P','O',0,12),('P','P',2,12),('P','P',1,48))
