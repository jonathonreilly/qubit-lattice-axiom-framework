import sympy as sp, random, itertools
from fractions import Fraction
I=sp.I
SIG=[sp.eye(2),sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-I],[I,0]]),sp.Matrix([[1,0],[0,-1]])]
class Pair:
    def __init__(s,dim,sign,Vfun=None,VDfun=None):
        s.dim,s.sign=dim,sign; s.Vfun=Vfun; s.VDfun=VDfun
    def canon(s,a,b):
        if a==b: return None,None
        return ((a,b),1) if a<b else ((b,a),s.sign)
    def h1(s,st):
        x,c=st; out=[]
        for a in range(s.dim):
            for sg in (1,-1):
                y=list(x); y[a]-=sg; y=tuple(y)
                for d in (0,1):
                    v=SIG[a+1][d,c]
                    if v!=0: out.append(((y,d),-I*sg*v/2))
        return out
    def add(s,vs):
        o={}
        for v in vs:
            for k,a in v.items():
                n=sp.expand(o.get(k,0)+a)
                if n==0: o.pop(k,None)
                else: o[k]=n
        return o
    def hop(s,v,w=None):
        o={}
        for (a,b),amp in v.items():
            for t,am in s.h1(a):
                k,sg=s.canon(t,b)
                if k:
                    ww=am*(1 if w is None else w(t[0],a[0]))
                    o[k]=sp.expand(o.get(k,0)+amp*ww*sg)
            for t,am in s.h1(b):
                k,sg=s.canon(a,t)
                if k:
                    ww=am*(1 if w is None else w(t[0],b[0]))
                    o[k]=sp.expand(o.get(k,0)+amp*ww*sg)
        return {k:a for k,a in o.items() if a!=0}
    def proj(s,v): return {k:a for k,a in v.items() if k[0][0]!=k[1][0]}
    def H2(s,v,D=None,comp=0):
        pv=s.proj(v)
        if D is None:
            h=s.proj(s.hop(pv)); vv=s.Vfun(pv) if s.Vfun else {}
        else:
            h=s.proj(s.hop(pv,lambda t,x: sp.Rational(t[comp]+x[comp],2))); vv=s.VDfun(pv,comp) if s.VDfun else {}
        return s.add([h,vv])
    def D2(s,v,comp): return s.H2(v,True,comp)
    def J(s,v,comp):
        return {k:sp.expand(I*a) for k,a in s.add([s.H2(s.D2(v,comp)),{k:-a for k,a in s.D2(s.H2(v),comp).items()}]).items()}
    def defect(s,v,comp):
        return s.add([s.H2(s.J(v,comp)),{k:-a for k,a in s.J(s.H2(v),comp).items()}])
