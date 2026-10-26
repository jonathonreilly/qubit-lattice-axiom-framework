from fractions import Fraction as F
def padd(p,q,c=F(1)):
    r=dict(p)
    for m,v in q.items():
        nv=r.get(m,F(0))+c*v
        if nv==0: r.pop(m,None)
        else: r[m]=nv
    return r
def pscale(p,c):
    return {m:v*c for m,v in p.items()} if c!=0 else {}
def pmul(p,q):
    r={}
    for m1,v1 in p.items():
        for m2,v2 in q.items():
            m=tuple(sorted(m1+m2)); nv=r.get(m,F(0))+v1*v2
            if nv==0: r.pop(m,None)
            else: r[m]=nv
    return r
def ppow(p,e):
    r={():F(1)}
    for _ in range(e): r=pmul(r,p)
    return r
def divide_linear(p,k,sigma):
    """p = q*(x_k - sigma) + rem, sigma free of x_k. returns q, rem."""
    byexp={}
    for mon,c in p.items():
        e=mon.count(k); rest=tuple(x for x in mon if x!=k)
        byexp.setdefault(e,{})[rest]=c
    xk={(k,):F(1)}
    q={};rem={}
    sp_={0:{():F(1)}}
    for e in range(1,max(byexp)+1 if byexp else 1): sp_[e]=pmul(sp_[e-1],sigma)
    for e,a in byexp.items():
        rem=padd(rem,pmul(a,sp_[e]))
        if e>=1:
            h={}
            for j in range(e):
                h=padd(h,pmul(ppow(xk,j),sp_[e-1-j]))
            q=padd(q,pmul(a,h))
    return q,rem
def evalp(p,pt):
    s=F(0)
    for m,c in p.items():
        t=c
        for v in m: t*=pt[v]
        s+=t
    return s
def degp(p): return max((len(m) for m in p),default=-1)
