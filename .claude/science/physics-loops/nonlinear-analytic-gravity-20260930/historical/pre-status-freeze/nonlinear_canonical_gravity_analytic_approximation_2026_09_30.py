#!/usr/bin/env python3
"""Author controls for a supplied nonlinear canonical gravity approximation.

Exact sparse samples and floating variation/trajectory diagnostics support the
self-contained analytic proof. All canonical modes are retained. This primary
reuses development engines and is not independent review. No campaign file,
external scientific data, native model or rotor process is read at runtime.
The execution envelope separately binds this source and its declared note.
"""
import argparse
import json
import os
import resource
import signal
import time

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = [
    "docs/NONLINEAR_CANONICAL_GRAVITY_ANALYTIC_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-30.md",
]
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[key] = "1"


def exact_controls(case):
    from sympy.polys.domains import QQ, QQ_I
    J=3 if case=='alias' else 5
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
    if case=='alias':
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
        axis=(1,0,0);second=(1,0,0)if case=='axial' else (0,1,0)
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
    result={'case':case,'J':J,'n':n,'B':None if case=='alias' else 1,'coefficient_domain':'QQ(i)','parameters':{'a':2,'K':3,'s':6,'m_squared':5},'checks':checks,'seconds':round(time.time()-start,3),'scope':'Exact sparse samples; analytic coefficient-transfer proof supplies universal identity.'}
    return result


def full_variation_controls():
    import numpy as np
    pairs = [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]
    a, K, eps = 1.3, .7, 1e-24

    def matrix(x, momentum=False):
        y = np.zeros(x.shape[:-1]+(3,3), dtype=x.dtype)
        for t,(i,j) in enumerate(pairs):
            v = x[...,t] / (2 if momentum and i != j else 1)
            y[...,i,j] = y[...,j,i] = v
        return y

    def local(g, p, q, r):
        G = matrix(g)
        Q = matrix(q)
        inv = np.linalg.inv(G)
        s = np.sqrt(np.linalg.det(G))
        B = s[...,None,None]*inv
        pi = matrix(p, True)
        tr = np.einsum('...ij,...ji->...',G,pi)
        gp = np.einsum('...ij,...jk->...ik',G,pi)
        T = a/s*(np.einsum('...ij,...ji->...',gp,gp)-.5*tr*tr)
        gam = np.zeros(G.shape[:-2]+(3,3,3),dtype=np.result_type(g,p,q,r))
        for k in range(3):
            for i in range(3):
                for j in range(3):
                    for l in range(3):
                        gam[...,k,i,j] += .5*inv[...,k,l]*(Q[...,i,j,l]+Q[...,j,i,l]-Q[...,l,i,j])
        V = np.zeros_like(T,dtype=np.result_type(g,p,q,r))
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    V += K*(r[...,k,i,j]*gam[...,k,i,j]-r[...,j,i,j]*gam[...,k,i,k])
                    for l in range(3):
                        V -= K*B[...,i,j]*(gam[...,k,k,l]*gam[...,l,i,j]-gam[...,k,j,l]*gam[...,l,i,k])
        return T,V,B,gam

    def make_derivative(n):
        xs = 2*np.pi*np.arange(n)/n
        delta = xs[:,None]-xs[None,:]
        D = sum(-2*k/n*np.sin(k*delta) for k in range(1,(n+1)//2))
        def diff(f,j):
            return np.moveaxis(np.tensordot(D,f,axes=(1,j)),0,j)
        return D,diff

    def fields(n):
        x,y,z = np.meshgrid(*(2*np.pi*np.arange(n)/n for _ in range(3)),indexing='ij')
        g = np.stack([1+.02*np.cos(x)+.005*np.sin(y+z),1+.014*np.sin(y),1+.018*np.cos(z),
                      .004*np.cos(x+y),.003*np.sin(y-z),.005*np.cos(z+x)],axis=-1)
        p = np.stack([.08+.03*np.sin(x),-.06+.02*np.cos(y+z),.04+.01*np.sin(z),
                      .023*np.cos(x-z),.016*np.sin(y+x),-.018*np.cos(z-y)],axis=-1)
        return g,p

    def original_H(g,p,diff):
        q = np.stack([diff(g,j) for j in range(3)],axis=-2)
        dummy = np.zeros(g.shape[:-1]+(3,3,3),dtype=g.dtype)
        T,_,B,gam = local(g,p,q,dummy)
        R = np.zeros_like(B)
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    R[...,i,j] += diff(gam[...,k,i,j],k)-diff(gam[...,k,i,k],j)
                    for l in range(3):
                        R[...,i,j] += gam[...,k,k,l]*gam[...,l,i,j]-gam[...,k,j,l]*gam[...,l,i,k]
        return np.mean(T-K*np.einsum('...ij,...ij->...',B,R))

    def adjoint_gradient(g,p,diff):
        q = np.stack([diff(g,j) for j in range(3)],axis=-2)
        dummy = np.zeros(g.shape[:-1]+(3,3,3))
        B = local(g,p,q,dummy)[2]
        r = np.stack([diff(B,j) for j in range(3)],axis=-3)
        T,V,_,_ = local(g,p,q,r)
        Tg,Vg,Tp = (np.zeros_like(g) for _ in range(3))
        Vq,Vr = np.zeros_like(q),np.zeros_like(r)
        for t in range(6):
            gc = g.astype(complex); gc[...,t] += 1j*eps
            tt,vv,_,_ = local(gc,p,q,r)
            Tg[...,t],Vg[...,t] = tt.imag/eps,vv.imag/eps
            pc = p.astype(complex); pc[...,t] += 1j*eps
            Tp[...,t] = local(g,pc,q,r)[0].imag/eps
        for j in range(3):
            for t in range(6):
                qc = q.astype(complex); qc[...,j,t] += 1j*eps
                Vq[...,j,t] = local(g,p,qc,r)[1].imag/eps
            for u in range(3):
                for v in range(3):
                    rc = r.astype(complex); rc[...,j,u,v] += 1j*eps
                    Vr[...,j,u,v] = local(g,p,q,rc)[1].imag/eps
        inv = np.linalg.inv(matrix(g)); s = np.sqrt(np.linalg.det(matrix(g)))
        Bg = np.zeros(g.shape[:-1]+(6,3,3))
        for t,(u,v) in enumerate(pairs):
            E = np.zeros((3,3)); E[u,v] = E[v,u] = 1
            trace = np.einsum('...ij,ji->...',inv,E)
            Bg[...,t,:,:] = s[...,None,None]*(.5*trace[...,None,None]*inv-np.einsum('...ij,jk,...kl->...il',inv,E,inv))
        grad_no_r = Tg+Vg-sum(diff(Vq[...,j,:],j) for j in range(3))
        r_adj = np.einsum('...tij,...ij->...t',Bg,sum(diff(Vr[...,j,:,:],j) for j in range(3)))
        grad = grad_no_r-r_adj
        r_wrong = np.einsum('...tij,...kt->...kij',Bg,q)
        false_H = np.mean(T+local(g,p,q,r_wrong)[1])
        pi,G = matrix(p,True),matrix(g)
        tr = np.einsum('...ij,...ji->...',G,pi)
        explicit_Tp = 2*a/s[...,None,None]*(np.einsum('...ij,...jk,...kl->...il',G,pi,G)-.5*G*tr[...,None,None])
        exp6 = np.stack([explicit_Tp[...,i,j] for i,j in pairs],axis=-1)
        diagnostics = {
            'original_vs_augmented_H': float(abs(original_H(g,p,diff)-np.mean(T+V))),
            'explicit_Tp_error': float(np.max(abs(Tp-exp6))),
            'false_chain_rule_r_max_error': float(np.max(abs(r-r_wrong))),
            'false_chain_rule_H_error': float(abs(original_H(g,p,diff)-false_H)),
            'omitted_r_adjoint_max_error': float(np.max(abs(r_adj))),
            'minimum_metric_eigenvalue': float(np.linalg.eigvalsh(G).min())}
        return grad,Tp,diagnostics

    output = {'description':'Author reuse of previously independent 3D variation control; this integrated primary is not independent review.',
              'couplings':{'a':a,'K':K},'epsilon':eps,'grids':[]}
    for n in (3,5):
        D,diff = make_derivative(n)
        g,p = fields(n)
        hg,hp,record = adjoint_gradient(g,p,diff)
        errors=[]
        if n == 3:
            for var,expected in ((0,hg),(1,hp)):
                for index in np.ndindex(g.shape):
                    gc,pc = g.astype(complex),p.astype(complex)
                    (gc if var==0 else pc)[index] += 1j*eps
                    actual = original_H(gc,pc,diff).imag/eps*n**3
                    errors.append(float(abs(actual-expected[index])))
            record['checked_coordinate_derivatives'] = len(errors)
        else:
            rng = np.random.default_rng(9302026)
            for _ in range(24):
                dg,dp = rng.standard_normal(g.shape),rng.standard_normal(p.shape)
                actual = original_H(g+1j*eps*dg,p+1j*eps*dp,diff).imag/eps
                expected = np.mean(np.sum(hg*dg+hp*dp,axis=-1))
                errors.append(float(abs(actual-expected)))
            record['checked_dense_tangent_directions'] = len(errors)
        record.update(n=n,sites=n**3,max_gradient_error=max(errors),derivative_skew_error=float(np.max(abs(D+D.T))))
        assert record['max_gradient_error'] < 2e-11, record
        assert record['explicit_Tp_error'] < 2e-11, record
        assert record['original_vs_augmented_H'] < 2e-12, record
        assert record['false_chain_rule_r_max_error'] > 1e-8, record
        assert record['omitted_r_adjoint_max_error'] > 1e-4, record
        output['grids'].append(record)
    return output


def scalar_controls():
    started=time.monotonic()
    import numpy as np
    import sympy as sp
    from scipy.integrate import solve_ivp
    A, B, C = gs = sp.symbols("A B C", positive=True)
    pa, pb, pc = ps = sp.symbols("pa pb pc")
    qa, qb, qc = qs = sp.symbols("qa qb qc")
    ra, rb, rc = rs = sp.symbols("ra rb rc")
    S = sp.sqrt(A * B * C)
    W = [S / x for x in gs]
    u, b, c, v, w = qa / (2*A), qb / (2*B), qc / (2*C), -qb / (2*A), -qc / (2*A)
    potential = (-ra*(b+c) + rb*v + rc*w
                 - W[0]*(u*(b+c)-b*b-c*c)
                 - W[1]*v*(u-b+c) - W[2]*w*(u+b-c))
    trace = sum(x*y for x, y in zip(gs, ps))
    kinetic = (sum((x*y)**2 for x, y in zip(gs, ps)) - trace**2/2)/S
    arguments = (*gs, *ps, *qs, *rs)
    exprs = ([sp.diff(kinetic, x) for x in ps]
             + [-sp.diff(kinetic+potential, x) for x in gs]
             + [sp.diff(potential, x) for x in qs]
             + [sp.diff(potential, x) for x in rs]
             + [sp.diff(x, y) for x in W for y in gs])
    local = sp.lambdify(arguments, exprs, "numpy", cse=True)



    def derivative(n):
        assert n % 2 == 1
        k = np.arange(n)[:, None] - np.arange(n)[None, :]
        out = np.zeros((n, n))
        mask = k != 0
        out[mask] = (-1.0)**k[mask] / (2*np.sin(np.pi*k[mask]/n))
        return out


    def original(g, p, D):
        """Literal scalar curvature with spectral derivatives left unexpanded."""
        aa, bb, cc = g
        qa_, qb_, qc_ = g @ D.T
        u_, b_, c_ = qa_/(2*aa), qb_/(2*bb), qc_/(2*cc)
        v_, w_ = -qb_/(2*aa), -qc_/(2*aa)
        rxx = -D @ (b_+c_) + u_*(b_+c_)-b_*b_-c_*c_
        ryy = D @ v_ + v_*(u_-b_+c_)
        rzz = D @ w_ + w_*(u_+b_-c_)
        sqrtg = np.sqrt(aa*bb*cc)
        gp = g*p
        td = (np.sum(gp*gp, axis=0)-np.sum(gp, axis=0)**2/2)/sqrtg
        cd = td - sqrtg*(rxx/aa+ryy/bb+rzz/cc)
        jd = np.sum(p*(g @ D.T), axis=0)-2*(D @ (aa*p[0]))
        return np.mean(cd), cd, jd


    def rhs(t, state, D):
        n = D.shape[0]
        g, p = state.reshape(2, 3, n)
        q = g @ D.T
        sqrtg = np.sqrt(np.prod(g, axis=0))
        ww = sqrtg/g
        r = ww @ D.T
        values = local(*g, *p, *q, *r)
        z = np.asarray([np.broadcast_to(x, (n,)) for x in values])
        dg = z[:3]
        dp = z[3:6]+z[6:9] @ D.T
        dw = z[9:12] @ D.T
        wgrad = z[12:].reshape(3, 3, n)
        dp += np.einsum("ijn,in->jn", wgrad, dw)
        return np.stack([dg, dp]).reshape(-1)



    # Dense spatial derivative at most 257^2; the primary price covers this shared author engine.
    # This intentionally reuses the author vacuum engine; it is not independent.
    from fractions import Fraction as Fr

    def centered(n):
        eps=2*np.pi/n
        D=np.zeros((n,n))
        for i in range(n):
            D[i,(i+1)%n]+=1/(2*eps);D[i,(i-1)%n]-=1/(2*eps)
        return D

    # Direct position-space action and exact single-mode symbol are independent
    # comparators for the assembled derivative matrix. Include the one-site grid.
    operator_controls=[]
    for n in (1,3,7):
        eps=2*np.pi/n;D=centered(n)
        basis=np.eye(n)
        literal=(np.roll(basis,-1,axis=0)-np.roll(basis,1,axis=0))/(2*eps)
        action_error=float(np.max(abs(D@basis-literal)))
        k=np.arange(-(n//2),n//2+1)
        phase=np.exp(1j*np.outer(np.arange(n)*eps,k))
        symbol_error=float(np.max(abs(D@phase-phase*(1j*np.sin(eps*k)/eps))))
        assert action_error < 1e-13, ('centered_action',n,action_error)
        assert symbol_error < 1e-13, ('centered_symbol',n,symbol_error)
        operator_controls.append({'n':n,'all_basis_action_error':action_error,'all_mode_symbol_error':symbol_error})

    def unpack(y,n):
        return y[:3*n].reshape(3,n), y[3*n:6*n].reshape(3,n), y[6*n:7*n], y[7*n:]

    def original_total(y,D):
        g,p,phi,w=unpack(y,len(D))
        energy,cd,jd=original(g,p,D)
        sqrtg=np.sqrt(np.prod(g,axis=0));z=D@phi
        matter=w*w/(2*sqrtg)+sqrtg*z*z/(2*g[0])
        return energy+np.mean(matter),cd+matter,jd+w*z

    def rhs_total(t,y,D):
        n=len(D);g,p,phi,w=unpack(y,n)
        base=rhs(t,np.stack([g,p]).reshape(-1),D).reshape(2,3,n)
        sqrtg=np.sqrt(np.prod(g,axis=0));z=D@phi
        metric_derivative=-w*w/(4*sqrtg*g)+sqrtg*z*z/(4*g[0]*g)
        metric_derivative[0]-=sqrtg*z*z/(2*g[0]*g[0])
        base[1]-=metric_derivative
        return np.concatenate([base.reshape(-1),w/sqrtg,D@(sqrtg*z/g[0])])

    # All canonical directions in a generic truly aliased diagonal fixture.
    controls=[]
    for label,operator in [('spectral',derivative),('centered',centered)]:
        n=7;x=np.arange(n)*2*np.pi/n;D=operator(n)
        g=np.array([1+.04*np.cos(x)+.01*np.sin(2*x),1+.03*np.sin(x),1-.02*np.cos(2*x)])
        p=np.array([.08+.03*np.sin(x),.04+.02*np.cos(x),-.03+.01*np.sin(2*x)])
        phi=.06*np.cos(x)+.03*np.sin(2*x);w=.2+.01*np.cos(2*x)
        y=np.concatenate([g.reshape(-1),p.reshape(-1),phi,w]);gradient=np.empty_like(y)
        for j in range(len(y)):
            trial=y.astype(complex);trial[j]+=1e-24j
            gradient[j]=n*original_total(trial,D)[0].imag/1e-24
        expected=np.concatenate([gradient[3*n:6*n],-gradient[:3*n],gradient[7*n:],-gradient[6*n:7*n]])
        error=float(np.max(abs(rhs_total(0,y,D)-expected)))
        assert error<1e-11
        controls.append({'derivative':label,'n':n,'directions':len(y),'gradient_error':error})

    # General symmetric metric variation of the scalar local source; all six slots.
    rng=np.random.default_rng(19030);matrix_error=0.
    for case in range(17):
        perturb=.02*rng.normal(size=(3,3));g=np.eye(3)+(perturb+perturb.T)/2
        z=rng.normal(size=3);w=float(rng.normal());s=1.7
        inv=np.linalg.inv(g);sqrtg=np.sqrt(np.linalg.det(g));v=inv@z
        S=-w*w*inv/(4*sqrtg)+s*sqrtg*(z@v)*inv/4-s*sqrtg*np.outer(v,v)/2
        def scalar_local(gg):
            ss=np.sqrt(np.linalg.det(gg))
            return w*w/(2*ss)+s*ss*(z@np.linalg.solve(gg,z))/2
        for i in range(3):
          for j in range(i,3):
            gg=g.astype(complex);gg[i,j]+=1e-24j
            if i!=j:gg[j,i]+=1e-24j
            expected=S[i,j]*(1 if i==j else 2)
            matrix_error=max(matrix_error,float(abs(scalar_local(gg).imag/1e-24-expected)))
    assert matrix_error<1e-11

    # Exact rational majorant hypothesis for f=cos x, sigma0=1/20, amplitude1/10.
    # q=sin^2 x has norm(1+exp(1/5))/2 <=(1+5/4)/2=9/8.
    r=Fr(1,128);R=1+r;d=2-R**5;A=R+R**6/d;L=1+6*R**5/d+5*R**10/d**2
    lam=Fr(1,1600);Bbound=Fr(9,8)
    assert d>0 and lam*Bbound<=min(r/(2*A),1/(2*L))
    assert 3*(R**4-1)<Fr(1,8)
    # An additional diagnostic, not a continuum or interval certificate.
    # Direct literal finite constraints below separately expose the H^2 coefficient.
    # Floating discretization of the continuum iteration, explicitly not its proof.
    nref=257;x=np.arange(nref)*2*np.pi/nref;k=np.fft.fftfreq(nref,d=1/nref)
    u=np.zeros(nref);q=np.sin(x)**2
    changes=[]
    for iteration in range(16):
        psi=1+u;c=np.mean(q*psi)/np.mean(psi**5)
        force=q*psi-c*psi**5
        coeff=np.fft.fft(force)/nref;coeff[0]=0
        inverse=np.zeros_like(coeff);mask=k!=0;inverse[mask]=-coeff[mask]/(k[mask]**2)
        new=(-float(lam)*np.fft.ifft(inverse*nref)).real
        changes.append(float(np.max(abs(new-u))));u=new
    psi=1+u;c=float(np.mean(q*psi)/np.mean(psi**5));H2=.1**2*c/12;H=np.sqrt(H2)
    psihat=np.fft.fft(psi)/nref
    lap=np.fft.ifft(-(k*k)*psihat*nref).real
    residual=float(np.max(abs(lap+float(lam)*(q*psi-c*psi**5))))
    rows=[]
    for label,operator,grids in [('spectral',derivative,(5,7,9,13,17)),('centered',centered,(17,33,65,129))]:
     for n in grids:
        xx=np.arange(n)*2*np.pi/n
        sampled=(np.exp(1j*np.outer(xx,k))@psihat).real
        g=np.array([sampled**4]*3);p=np.array([-2*H*sampled**2]*3)
        phi=.1*np.cos(xx);w=np.zeros(n);y=np.concatenate([g.reshape(-1),p.reshape(-1),phi,w])
        en,cd,jd=original_total(y,operator(n))
        rows.append({'derivative':label,'n':n,'C_sup':float(np.max(abs(cd))),
                     'Jx_sup':float(np.max(abs(jd))),'energy':float(en)})

    # Numerical normalization check against the independently evaluated literal H.
    # This fixed diagnostic tolerance is well above rounding and is not a theorem bound.
    assert residual < 1e-8, residual
    finest_spectral=next(row for row in rows if row['derivative']=='spectral' and row['n']==17)
    assert finest_spectral['C_sup'] < 1e-8, finest_spectral

    # Exact massless-scalar Kasner continuum solution, pulled back by X=x+eta sin x.
    # Kasner exponent_i=1/3, scalar coefficient 2/sqrt3; constraint sum pi_i^2=1-c_scalar^2/2.
    trajectory=[];eta=.05;cc=2/np.sqrt(3);duration=.01;power=np.array([1/3]*3)
    for label,operator,grids in [('spectral',derivative,(5,7,9,13,17)),('centered',centered,(17,33,65,129))]:
     for n in grids:
        xx=np.arange(n)*2*np.pi/n;f=1+eta*np.cos(xx);D=operator(n)
        def exact(t):
            scales=t**(2*power)
            g=np.array([scales[0]*f*f,scales[1]+0*f,scales[2]+0*f])
            sqrtg=t*f
            p=np.array([(power[i]-1)*sqrtg/(t*g[i]) for i in range(3)])
            phi=cc*np.log(t)+0*f;w=cc*f
            return np.concatenate([g.reshape(-1),p.reshape(-1),phi,w])
        initial=exact(1);e0,c0,j0=original_total(initial,D)
        solution=solve_ivp(lambda t,y:rhs_total(t,y,D),(0,duration),initial,method='DOP853',rtol=2e-12,atol=2e-14)
        assert solution.success
        final=solution.y[:,-1];ef,cf,jf=original_total(final,D)
        trajectory.append({'derivative':label,'n':n,'rhs_evaluations':solution.nfev,
                           'initial_C_sup':float(np.max(abs(c0))),'initial_Jx_sup':float(np.max(abs(j0))),
                           'state_error_sup':float(np.max(abs(final-exact(1+duration)))),
                           'final_C_sup':float(np.max(abs(cf))),'final_Jx_sup':float(np.max(abs(jf))),
                           'energy_drift':float(abs(ef-e0))})
    result={'scope':'Author floating diagnostics and exact rational hypothesis checks; no interval/continuum solve certification, independent computation, or theorem from samples. Duration not certified by majorant T.',
            'centered_operator_controls':operator_controls,'canonical_gradient_controls':controls,'general_symmetric_scalar_metric_derivatives':{'cases':17,'directions_each':6,'max_error':matrix_error},
            'contraction_rational_hypotheses':{'radius':str(r),'q_norm_upper':str(Bbound),'lambda':str(lam),'mapping_bound':str(lam*Bbound*A),'contraction_bound':str(lam*Bbound*L),'metric_bound':str(3*(R**4-1))},
            'conformal_iteration':{'reference_n':nref,'amplitude':.1,'sigma0':.05,'iterations':16,'iterate_changes_sup':changes,'H_squared':float(H2),'H':float(H),'reference_equation_residual':residual,'finite_constraint_rows':rows},
            'scalar_Kasner':{'duration':duration,'scalar_log_coefficient':float(cc),'rows':trajectory},
            'seconds':time.monotonic()-started,'max_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    for scheme in ('spectral','centered'):
        observed=[row for row in trajectory if row['derivative']==scheme]
        assert observed[-1]['state_error_sup'] < observed[0]['state_error_sup']/4, observed
    return result


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--family',choices=('all','exact','variation','scalar'),default='all')
    parser.add_argument('--case',choices=('all','axial','mixed','alias'),default='all')
    args=parser.parse_args()
    signal.alarm(AUDIT_TIMEOUT_SEC)
    resource.setrlimit(resource.RLIMIT_CPU,(90,95))
    started=time.monotonic()
    results={}
    failures={}
    calls=[]
    if args.family in ('all','exact'):
        cases=('axial','mixed','alias') if args.case=='all' else (args.case,)
        calls += [('exact_'+case,lambda case=case:exact_controls(case)) for case in cases]
    if args.family in ('all','variation'):
        calls.append(('full_3d_variation',full_variation_controls))
    if args.family in ('all','scalar'):
        calls.append(('coupled_scalar',scalar_controls))
    for name,call in calls:
        print('BEGIN '+name,flush=True)
        try:
            results[name]=call()
            print('PASS '+name,flush=True)
        except Exception as exc:
            failures[name]=repr(exc)
            print('FAIL '+name+': '+repr(exc),flush=True)
    report={'scope':'Exact samples and floating diagnostics for the supplied law; the note proves the general theorem. No formal review or audit status.',
            'results':results,'failures':failures,'wall_seconds':time.monotonic()-started,
            'cpu_seconds':time.process_time(),'max_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    print(json.dumps(report,sort_keys=True))
    print('per_element: Canonical coordinate variations and metric stress are tested at declared finite fixtures.')
    print('per_site: Full three-dimensional finite-grid variations retain every six-slot metric component.')
    print('per_mode: Exact circular Fourier contractions include generated modes and a stated wrapped-mode example.')
    print('per_block: Floating trajectories and conformal samples use the actual declared finite Hamiltonians.')
    print('lattice_wide: Universal analytic and coefficient-transfer claims are proved in the source note, not inferred from samples.')
    print(f'TOTAL: PASS={len(results)} FAIL={len(failures)}')
    return bool(failures)


if __name__=='__main__':
    raise SystemExit(main())
