#!/usr/bin/env python3
"""Exact sparse FULL-carrier spectral brackets by directional differentiation.

No low-band projection. Fourier products wrap at the declared odd n.
The automatic tangent includes modes absent in the input fields.
Sympy is used only for its exact Gaussian-rational coefficient domain.
"""
import argparse, json, os, signal, time
from pathlib import Path
from sympy.polys.domains import QQ, QQ_I

ROOT=Path(__file__).resolve().parent
RUN=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (RUN/'STOP_REQUESTED.json').exists()
assert time.time()<json.loads((RUN/'DEADLINE.json').read_text())['deadline_epoch']
signal.alarm(180)
args=argparse.ArgumentParser();args.add_argument('--case',choices=['axial','mixed','alias'],default='axial');args=args.parse_args()
J=3 if args.case=='alias' else 5
n=2*J+1
MAX=4
I=QQ_I.dtype(QQ(0),QQ(1)); ONE=QQ_I.one
def q(x): return QQ_I.convert(x)
def wrap(k): return tuple((v+J)%n-J for v in k)
class P:
    def __init__(self,d=None): self.d={k:q(v) for k,v in (d or {}).items() if v}
    def __add__(a,b):
        b=poly(b); d=a.d.copy()
        for k,v in b.d.items():
            d[k]=d.get(k,QQ_I.zero)+v
            if not d[k]: del d[k]
        return P(d)
    __radd__=__add__
    def __neg__(a): return P({k:-v for k,v in a.d.items()})
    def __sub__(a,b): return a+-poly(b)
    def __rsub__(a,b): return poly(b)+-a
    def __mul__(a,b):
        if isinstance(b,T): return b*a
        b=poly(b); d={}
        for (da,*ka),va in a.d.items():
            for (db,*kb),vb in b.d.items():
                if da+db>MAX: continue
                key=(da+db,)+wrap(tuple(x+y for x,y in zip(ka,kb)))
                d[key]=d.get(key,QQ_I.zero)+va*vb
        return P(d)
    __rmul__=__mul__
    def D(a,j): return P({k:v*I*k[j+1] for k,v in a.d.items()})
    def mean(a): return P({k:v for k,v in a.d.items() if k[1:]==(0,0,0)})
    def upto(a,r): return P({k:v for k,v in a.d.items() if k[0]<=r})
def poly(x): return x if isinstance(x,P) else P({(0,0,0,0):x})
class T:
    def __init__(self,v=0,t=0):self.v=poly(v);self.t=poly(t)
    def __add__(a,b):
        b=dual(b);return T(a.v+b.v,a.t+b.t)
    __radd__=__add__
    def __neg__(a): return T(-a.v,-a.t)
    def __sub__(a,b):return a+-dual(b)
    def __rsub__(a,b):return dual(b)+-a
    def __mul__(a,b):
        b=dual(b);return T(a.v*b.v,a.t*b.v+a.v*b.t)
    __rmul__=__mul__
    def D(a,j):return T(a.v.D(j),a.t.D(j))
    def mean(a):return T(a.v.mean(),a.t.mean())
def dual(x):return x if isinstance(x,T) else T(x)
def mat(f):return [[f(i,j) for j in range(3)]for i in range(3)]
def mm(a,b):return mat(lambda i,j:sum(a[i][k]*b[k][j] for k in range(3)))
def tr(a):return sum(a[i][i] for i in range(3))
def series(h):
    ident=mat(lambda i,j:T(int(i==j)))
    pw=ident; inv=ident
    for r in range(1,5):
        pw=mm(pw,h);inv=mat(lambda i,j:inv[i][j]+(-1)**r*pw[i][j])
    g=mat(lambda i,j:ident[i][j]+h[i][j])
    # Three by three determinant; binomial expansion is exact to needed degree.
    det=g[0][0]*(g[1][1]*g[2][2]-g[1][2]*g[2][1])-g[0][1]*(g[1][0]*g[2][2]-g[1][2]*g[2][0])+g[0][2]*(g[1][0]*g[2][1]-g[1][1]*g[2][0])
    z=det-1; pw=T(1); sq=T(1); isq=T(1)
    for cs,ci in [(QQ(1,2),QQ(-1,2)),(QQ(-1,8),QQ(3,8)),(QQ(1,16),QQ(-5,16)),(QQ(-5,128),QQ(35,128))]:
        pw=pw*z;sq=sq+cs*pw;isq=isq+ci*pw
    return g,inv,sq,isq
def scalar(h,p,N,phi=None,sp=None):
    g,iv,sq,isq=series(h)
    gam=[mat(lambda i,j:sum(iv[k][l]*(h[j][l].D(i)+h[i][l].D(j)-h[i][j].D(l))for l in range(3))*QQ(1,2))for k in range(3)]
    ric=mat(lambda i,j:sum(gam[k][i][j].D(k)-gam[k][i][k].D(j)+sum(gam[k][k][l]*gam[l][i][j]-gam[k][j][l]*gam[l][i][k]for l in range(3))for k in range(3)))
    R=sum(iv[i][j]*ric[i][j]for i in range(3)for j in range(3))
    gp=mm(g,p)
    # Fixed diagnostic coefficients a=2, K=3, s=6, m^2=5.
    ans=2*isq*(tr(mm(gp,gp))-QQ(1,2)*tr(gp)*tr(gp))-3*sq*R
    if phi is not None:
        ans=ans+QQ(1,2)*isq*sp*sp+3*sq*sum(iv[i][j]*phi.D(i)*phi.D(j)for i in range(3)for j in range(3))+QQ(5,2)*sq*phi*phi
    return (N*ans).mean()
def velocities(h,p,N,phi=None,sp=None):
    g,iv,sq,isq=series(h);gpg=mm(mm(g,p),g);t=tr(mm(g,p))
    return mat(lambda i,j:(4*N*isq*(gpg[i][j]-QQ(1,2)*g[i][j]*t)).v), None if sp is None else (N*isq*sp).v
def lie(h,p,X,phi=None,sp=None):
    g=mat(lambda i,j:h[i][j]+int(i==j))
    dh=mat(lambda i,j:sum(X[k]*g[i][j].D(k)+g[i][k]*X[k].D(j)+g[j][k]*X[k].D(i)for k in range(3)))
    dp=mat(lambda i,j:sum((X[k]*p[i][j]).D(k)-p[k][j]*X[i].D(k)-p[i][k]*X[j].D(k)for k in range(3)))
    return dh,dp,None if phi is None else sum(X[k]*phi.D(k)for k in range(3)),None if sp is None else sum((X[k]*sp).D(k)for k in range(3))
def spatial(h,p,X,phi=None,sp=None):
    dh,_,_,_=lie(h,p,X)
    ans=sum(p[i][j]*dh[i][j]for i in range(3)for j in range(3))
    if phi is not None:ans=ans+sp*sum(X[k]*phi.D(k)for k in range(3))
    return ans.mean()
def tangent(h,p,dh=None,dp=None):
    return mat(lambda i,j:T(h[i][j].v,0 if dh is None else dual(dh[i][j]).v)),mat(lambda i,j:T(p[i][j].v,0 if dp is None else dual(dp[i][j]).v))
def mode(k,degree=0,coef=1):return P({(degree,)+tuple(k):coef})
def cosine(k,d=0,c=1):return mode(k,d,q(c)/q(2))+mode(tuple(-z for z in k),d,q(c)/q(2))
def sine(k,d=0,c=1):return mode(k,d,-I*q(c)/q(2))+mode(tuple(-z for z in k),d,I*q(c)/q(2))
def out(p):return {str(k):str(v)for k,v in sorted(p.d.items())}

start=time.time(); checks={}
if args.case=='alias':
    h=mat(lambda i,j:T(cosine((1,0,0),1)if i==j==1 else 0))
    p=mat(lambda i,j:T(cosine((3,0,0),1)if i==j==1 else 0))
    X=[T(1),T(),T()];Y=[T(cosine((3,0,0))),T(),T()]
    dh,dp,_,_=lie(h,p,Y);ht,pt=tangent(h,p,dh,dp)
    bracket=spatial(ht,pt,X).t
    XY=[sum(X[k]*Y[j].D(k)-Y[k]*X[j].D(k)for k in range(3))for j in range(3)]
    defect=bracket-spatial(h,p,XY).v
    checks['full_zone_GG_defect']=out(defect)
    assert defect.d=={(2,0,0,0):q(QQ(7,4))}
else:
    axis=(1,0,0);second=(1,0,0)if args.case=='axial' else (0,1,0)
    h=mat(lambda i,j:T(cosine(axis,1,1+i+j)+sine(second,1,i+j+1)))
    p=mat(lambda i,j:T(cosine(second,1,2+i+j)+sine(axis,1,i+j-1)))
    phi=T(cosine(axis,1)+sine(second,1,2));sp=T(cosine(second,1,3)-sine(axis,1))
    N=T(1+cosine(axis)+sine(second));M=T(2+sine(axis)-cosine(second))
    X=[T(cosine(axis,c=j+1)+sine(second,c=2-j))for j in range(3)]
    Y=[T(sine(axis,c=j+2)-cosine(second,c=j))for j in range(3)]
    for matter in (False,True):
        ph,ps=(phi,sp)if matter else(None,None);tag='scalar'if matter else'vacuum'
        qm,sm=velocities(h,p,M,ph,ps);qn,sn=velocities(h,p,N,ph,ps)
        hm,pm=tangent(h,p,qm);hn,pn=tangent(h,p,qn)
        ccn=scalar(hm,pm,N,None if ph is None else T(ph.v,sm),ps).t
        ccm=scalar(hn,pn,M,None if ph is None else T(ph.v,sn),ps).t
        _,iv,_,_=series(h)
        F=[sum(6*iv[i][j]*(N*M.D(j)-M*N.D(j))for j in range(3))for i in range(3)]
        cc=(ccn-ccm-spatial(h,p,F,ph,ps).v).upto(3)
        assert not cc.d,(tag,'CC',out(cc))
        checks[tag+'_CC_through3']=out(cc)
        dh,dp,dph,dps=lie(h,p,X,ph,ps);ht,pt=tangent(h,p,dh,dp)
        gc=-scalar(ht,pt,N,None if ph is None else T(ph.v,dph.v),None if ps is None else T(ps.v,dps.v)).t
        U=sum(X[k]*N.D(k)for k in range(3))
        gc=(gc-scalar(h,p,U,ph,ps).v).upto(3)
        assert not gc.d,(tag,'GC',out(gc))
        checks[tag+'_GC_through3']=out(gc)
        dh,dp,dph,dps=lie(h,p,Y,ph,ps);ht,pt=tangent(h,p,dh,dp)
        gg=spatial(ht,pt,X,None if ph is None else T(ph.v,dph.v),None if ps is None else T(ps.v,dps.v)).t
        XY=[sum(X[k]*Y[j].D(k)-Y[k]*X[j].D(k)for k in range(3))for j in range(3)]
        gg=(gg-spatial(h,p,XY,ph,ps).v).upto(2)
        assert not gg.d,(tag,'GG',out(gg))
        checks[tag+'_GG_through2']=out(gg)
result={'case':args.case,'J':J,'n':n,'B':None if args.case=='alias' else 1,'coefficient_domain':'QQ(i)','parameters':{'a':2,'K':3,'s':6,'m_squared':5},'checks':checks,'seconds':round(time.time()-start,3),'scope':'Exact sparse samples; analytic coefficient-transfer proof supplies universal identity.'}
(ROOT/(args.case+'.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
