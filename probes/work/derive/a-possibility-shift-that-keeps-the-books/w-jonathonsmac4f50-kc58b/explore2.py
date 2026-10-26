import sympy as sp, random, itertools, time
from explore import *
random.seed(1)
def bonds(dim,lo,hi):
    out=[]
    rng=range(lo,hi+1)
    for x in itertools.product(rng,repeat=dim):
        for a in range(dim):
            y=list(x); y[a]+=1
            if y[a]<=hi: out.append((x,tuple(y)))
    return out
def basis(dim,lo,hi):
    return [((x,c1),(y,c2)) for (x,y) in bonds(dim,lo,hi) for c1 in (0,1) for c2 in (0,1)]
def randherm(B,dens,seed):
    r=random.Random(seed); idx={b:i for i,b in enumerate(B)}
    M={}
    n=len(B)
    for i in range(n):
        for j in range(i,n):
            if r.random()<dens:
                if i==j: v=sp.Rational(r.randint(-5,5),r.randint(1,4))
                else: v=sp.Rational(r.randint(-5,5),r.randint(1,4))+I*sp.Rational(r.randint(-5,5),r.randint(1,4))
                if v!=0:
                    M[(i,j)]=v
                    if i!=j: M[(j,i)]=sp.conjugate(v)
    cols={}
    for (i,j),v in M.items(): cols.setdefault(j,[]).append((i,v))
    return lambda st: cols.get(idx.get(st),[]),idx
def mkV(B,dens,seed,t):
    col,idx=randherm(B,dens,seed)
    def F(v):
        o={}
        for k,a in v.items():
            if k in idx:
                for i,m in col(k):
                    kk=B[i]; o[kk]=sp.expand(o.get(kk,0)+t*m*a)
        return {k:a for k,a in o.items() if a!=0}
    return F
def entry(dim,sign,t,dens=0.15,lo=-2,hi=2,seedV=3,seedD=4):
    B=basis(dim,lo,hi)
    V=mkV(B,dens,seedV,t); 
    VDf=mkV(B,dens,seedD,t)
    p=Pair(dim,sign,V,lambda v,comp: VDf(v))
    a=((0,)*dim,0);b=((1,)+(0,)*(dim-1),0)
    k,sg=p.canon(a,b)
    d=p.defect({k:sg},0)
    target=(((-1,-1)+(0,)*(dim-2),0),((0,)*dim,1))
    return d.get(target,0)
if __name__=="__main__":
    for sign in (-1,1):
        t0=time.time()
        vals=[entry(2,sign,sp.Integer(t)) for t in range(5)]
        print(sign,[sp.simplify(v) for v in vals],time.time()-t0)
        T=sp.symbols('T')
        poly=sp.expand(sp.interpolate(list(zip(range(5),vals)),T))
        print(sp.Poly(poly,T).all_coeffs())
