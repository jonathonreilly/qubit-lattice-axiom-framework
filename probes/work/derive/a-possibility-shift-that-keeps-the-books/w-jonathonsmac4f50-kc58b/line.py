import sympy as sp, itertools, time
from explore import *
PA=SIG
def make(sign,Msym,toff):
    # line: V = sum over adjacent pairs (lo,lo+1) of M on coins (lo coin first), energy at midpoint + toff
    def Vop(v,wt=None):
        o={}
        for (a,b),amp in v.items():
            (x1,c1),(x2,c2)=a,b
            if abs(x1[0]-x2[0])!=1: continue
            # canonical: a<b so x1<x2
            col=2*c1+c2
            w=1 if wt is None else wt(x1,x2)
            for row in range(4):
                m=Msym[row,col]
                if m==0: continue
                k=((x1,row//2),(x2,row%2))
                o[k]=sp.expand(o.get(k,0)+amp*m*w)
        return {k:a for k,a in o.items() if a!=0}
    return Vop
if __name__=="__main__":
    cs=sp.symbols('c0:16',real=True)
    M=sp.zeros(4,4)
    for b in range(4):
        for c in range(4):
            M+=cs[4*b+c]*sp.kronecker_product(PA[b],PA[c])
    tt=sp.symbols('tt',real=True)
    for sign in (-1,1):
        Vf=make(sign,M,tt)
        p=Pair(1,sign,lambda v:Vf(v),lambda v,comp:Vf(v,lambda x1,x2: sp.Rational(x1[0]+x2[0],2)+tt))
        eqs=set()
        for pos2 in [(1,),(2,),(3,)]:
            for c1,c2 in itertools.product((0,1),repeat=2):
                k,sg=p.canon(((0,),c1),(pos2,c2))
                d=p.defect({k:sg},0)
                for kk,a in d.items():
                    for part in (sp.re(a),sp.im(a)):
                        e=sp.expand(part)
                        if e!=0: eqs.add(e)
        print(sign,len(eqs))
        eqs=list(eqs)
        sol=sp.solve(eqs,list(cs)+[tt],dict=True)
        print(sol[:6], len(sol))
