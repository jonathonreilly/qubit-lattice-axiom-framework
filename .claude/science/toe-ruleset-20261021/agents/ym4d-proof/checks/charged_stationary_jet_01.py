#!/usr/bin/env python3
"""Actual d=4 SU(2) paired-S4' stationary-chain controls, author implementation.

No predecessor helper imports. Quaternion t_a=-i sigma_a; [t(a),t(b)]=2t(a×b).
Finite floating-point falsifiers, not an all-depth proof.
"""
import itertools, json, time
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import LinearOperator, cg
import torch

torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)
L, T, d, kap = 3, 2, 4, 1.0
nf, nc = L*T, T
Vf, Vc = nf**d, nc**d
Ef, Ec, nt = d*Vf, d*Vc, 24*L**d
checks, details = [], {}

def check(name, value, bound, less=True):
    value, bound = float(value), float(bound)
    ok = value <= bound if less else value > bound
    checks.append(dict(name=name, value=value, bound=bound, direction='le' if less else 'gt', passed=bool(ok)))

def sid(x,n): return int(np.ravel_multi_index(tuple(np.asarray(x)%n),(n,)*d))
def edge(x,mu,n): return d*sid(x,n)+mu
def step(x,mu,sign,n):
    x=np.array(x, dtype=int)
    if sign==1:
        e=edge(x,mu,n); x[mu]+=1
    else:
        x[mu]-=1; e=edge(x,mu,n)
    return x,(e,sign)
def axial(start,delta,order,n):
    x=np.array(start,dtype=int); out=[]
    for mu in order:
        for _ in range(abs(int(delta[mu]))):
            x,e=step(x,mu,int(np.sign(delta[mu])),n); out.append(e)
    return out
def padded(paths):
    z=np.full((len(paths),max(map(len,paths))),Ef,dtype=np.int64)
    s=np.zeros(z.shape,dtype=np.float64)
    for i,p in enumerate(paths):
        for j,(a,b) in enumerate(p): z[i,j]=a; s[i,j]=b
    return z,s
def incidence(n):
    rr=[]; cc=[]; vv=[]
    for x in itertools.product(range(n),repeat=d):
        for mu in range(d):
            e=edge(x,mu,n); y=np.array(x); y[mu]+=1
            rr.extend([e,e]);cc.extend([sid(x,n),sid(y,n)]);vv.extend([-1,1])
    return sparse.csr_matrix((vv,(rr,cc)),shape=(d*n**d,n**d),dtype=float)

start=time.time()
paths=[]; truncated=[]; roots=[]; left_axial=[]
orders=list(itertools.permutations(range(d)))
for X in itertools.product(range(T),repeat=d):
    root=L*np.array(X)+1; roots.append(sid(root,nf))
    for mu in range(d):
        for order in orders:
            for off in itertools.product(range(-1,2),repeat=d):
                delta=np.array(off); y=root+delta
                p=axial(root,delta,order,nf); left_axial.append(p)
                x=y.copy(); mid=[]
                for _ in range(L): x,e=step(x,mu,1,nf);mid.append(e)
                r2=root.copy();r2[mu]+=L
                end=axial(r2,delta,order,nf)
                paths.append(p+mid+[(e,-sg) for e,sg in end[::-1]])
                truncated.append(p+mid)
ind,sign=padded(paths); tind,tsign=padded(truncated)
row=np.repeat(np.arange(Ec),nt)
Q=sparse.coo_matrix((sign.ravel()/nt,(np.repeat(row,ind.shape[1]),ind.ravel())),shape=(Ec,Ef+1)).tocsr()[:,:Ef]
Q.eliminate_zeros()
Qbad=sparse.coo_matrix((tsign.ravel()/nt,(np.repeat(row,tind.shape[1]),tind.ravel())),shape=(Ec,Ef+1)).tocsr()[:,:Ef]
df,dc=incidence(nf),incidence(nc)
ev=sparse.csr_matrix((np.ones(Vc),(np.arange(Vc),roots)),shape=(Vc,Vf))
diff=Q@df-dc@ev
check('all_actual_paths_count',abs(len(paths)-Ec*nt),0)
check('root_covariance',np.max(np.abs(diff.data),initial=0),1e-12)
check('reject_deleted_endpoint',np.max(np.abs((Qbad@df-dc@ev).data)),1e-3,False)
check('reject_wrong_divisor',np.max(np.abs((L*Q@df-dc@ev).data)),1e-3,False)

plaq=[]
for x0 in itertools.product(range(nf),repeat=d):
    for mu in range(d):
        for nu in range(mu+1,d):
            x=np.array(x0);p=[]
            for direction,sg in [(mu,1),(nu,1),(mu,-1),(nu,-1)]:
                x,e=step(x,direction,sg,nf);p.append(e)
            plaq.append(p)
pi,ps=padded(plaq)
C=sparse.coo_matrix((ps.ravel(),(np.repeat(np.arange(len(plaq)),4),pi.ravel())),shape=(len(plaq),Ef)).tocsr()
nonroots=np.ones(Vf,dtype=bool);nonroots[roots]=False
G=df[:,nonroots]
check('curl_gradient',np.max(np.abs((C@df).data),initial=0),1e-12)
diag=np.asarray(C.power(2).sum(axis=0)).ravel()+kap*np.asarray(Q.power(2).sum(axis=0)).ravel()+np.asarray(G.power(2).sum(axis=1)).ravel()
def hop(x):return C.T@(C@x)+kap*Q.T@(Q@x)+G@(G.T@x)
H=LinearOperator((Ef,Ef),matvec=hop,dtype=float)
M=LinearOperator((Ef,Ef),matvec=lambda x:x/diag,dtype=float)
solves=[]
def solve(rhs):
    out=np.empty_like(rhs)
    for a in range(3):
        it=[0]
        def cb(_):it[0]+=1
        out[:,a],info=cg(H,rhs[:,a],M=M,rtol=2e-13,atol=1e-15,maxiter=3000,callback=cb)
        rel=np.linalg.norm(hop(out[:,a])-rhs[:,a])/max(1,np.linalg.norm(rhs[:,a]))
        solves.append(dict(info=int(info),iterations=it[0],relative_residual=float(rel)))
        check('linear_solve',rel,1e-9)
    return out

def bch(field,ix,sg,third=True,backend=np):
    if backend is torch:
        f=torch.cat([field,torch.zeros((1,3))],dim=0)
        ii=torch.tensor(ix); ss=torch.tensor(sg)
        A=torch.zeros((len(ix),3));B=torch.zeros_like(A);D=torch.zeros_like(A)
        cross=lambda a,b:torch.linalg.cross(a,b,dim=-1)
    else:
        f=np.vstack([field,np.zeros((1,3))]);ii=ix;ss=sg
        A=np.zeros((len(ix),3));B=np.zeros_like(A);D=np.zeros_like(A);cross=np.cross
    for j in range(ix.shape[1]):
        x=f[ii[:,j]]*ss[:,j,None]
        if third:D=D+cross(B,x)+(cross(A,cross(A,x))+cross(x,cross(x,A)))/3
        B=B+cross(A,x);A=A+x
    return A,B,D

def parts(a,b,need_grad=False):
    if need_grad:
        aa=torch.tensor(a,requires_grad=True);bb=torch.tensor(b)
        pA,pB,_=bch(aa,pi,ps,False,torch)
        A,B,_=bch(aa,ind,sign,False,torch)
        Ab=A.reshape(Ec,nt,3).mean(dim=1);Bb=B.reshape(Ec,nt,3).mean(dim=1)
        r=bb-Ab
        f3w=(pA*pB).sum();f3s=-kap*(r*Bb).sum()
        val=f3w+f3s
        source=torch.autograd.grad(val,aa)[0].detach().numpy()
        return source,dict(wilson=float(f3w.detach()),soft=float(f3s.detach()),total=float(val.detach()))
    pA,pB,pC=bch(a,pi,ps)
    A,B,D=bch(a,ind,sign)
    A,B,D=[x.reshape(Ec,nt,3) for x in (A,B,D)]
    Ab=A.mean(axis=1);Bb=B.mean(axis=1);V3=(D-(A*A).sum(axis=2)[:,:,None]*A/6).mean(axis=1)
    s2=-(A*A).sum(axis=2).mean(axis=1)/2
    aa=(Ab*Ab).sum(axis=1);bb=(b*b).sum(axis=1);ba=(b*Ab).sum(axis=1)
    soft4=((Ab-b)*V3).sum()+.5*(Bb*Bb).sum()+np.sum((bb-aa)*s2/2-aa*aa/8-bb*bb/24+bb*ba/6)
    wil4=.5*np.sum(pB*pB)+np.sum(pA*pC)-np.sum(np.sum(pA*pA,axis=1)**2)/24
    r=b-Ab
    return dict(F2=float(.5*np.sum(pA*pA)+kap*.5*np.sum(r*r)),F3=float(np.sum(pA*pB)-kap*np.sum(r*Bb)),F4=float(wil4+kap*soft4),wilson4=float(wil4),soft4=float(kap*soft4),soft_square=float(kap*.5*np.sum(Bb*Bb))), (Ab,Bb,r)

def qexp(a):
    mag=np.linalg.norm(a,axis=1)
    return np.column_stack((np.cos(mag),a*np.sinc(mag[:,None]/np.pi)))
def qm(a,b):
    return np.column_stack((a[:,0]*b[:,0]-np.sum(a[:,1:]*b[:,1:],axis=1),a[:,0,None]*b[:,1:]+b[:,0,None]*a[:,1:]+np.cross(a[:,1:],b[:,1:])))
def qpaths(U,ix,sg):
    U=np.vstack([U,np.array([1.,0,0,0])]);out=np.zeros((len(ix),4));out[:,0]=1
    for j in range(ix.shape[1]):
        v=U[ix[:,j]].copy();v[:,1:]*=sg[:,j,None];out=qm(out,v)
    return out
def action(a,b):
    U=qexp(a);V=qexp(b);Wp=qpaths(U,pi,ps)
    means=qpaths(U,ind,sign).reshape(Ec,nt,4).mean(axis=1)
    return float(np.sum(1-Wp[:,0])+kap*np.sum(np.linalg.norm(means,axis=1)-np.sum(V*means,axis=1)))

rng=np.random.default_rng(20261029)
b=rng.normal(size=(Ec,3))*.5
a=solve(kap*Q.T@b)
check('linear_slice_gauge',np.max(np.abs(G.T@a)),1e-9)
S,third=parts(a,b,True)
coef,(Ab,Bb,r)=parts(a,b)
check('BCH_cubic_same_source',abs(third['total']-coef['F3']),1e-10)
check('hidden_source_annihilates_rootzero_gauge',np.max(np.abs(G.T@S)),1e-9)
a2=-solve(S)
exchange=float(.5*np.sum(S*(-a2)))
pred=coef['F4']-exchange
check('noncommuting_exchange_nonzero',exchange,5e-4,False)
check('noncommuting_source_nonzero',np.linalg.norm(S),1e-3,False)
samples=[]
for eps in [.08,.04,.02]:
    plus=action(eps*a+eps**2*a2,eps*b)
    minus=action(-eps*a+eps**2*a2,-eps*b)
    q=((plus+minus)/2-eps**2*coef['F2'])/eps**4
    samples.append(dict(epsilon=eps,plus=plus,minus=minus,quartic_estimate=float(q)))
rich=(4*samples[-1]['quartic_estimate']-samples[-2]['quartic_estimate'])/3
tol=5e-5*max(1,abs(pred))
check('exact_group_stationary_quartic',abs(rich-pred),tol)
for name,p in [('omitted',coef['F4']),('opposite_sign',coef['F4']+exchange),('lost_half',coef['F4']-2*exchange)]:
    check('reject_exchange_'+name,abs(rich-p),10*tol,False)

# Right-trivialized link current; incoming minus Ad_U(outgoing).
J1=kap*r;J2=kap*(-Q@a2-Bb+np.cross(b,Ab))
div2=dc.T@J2
rhs=(2*np.cross(b,J1)).reshape(Vc,d,3).sum(axis=1)
check('second_current_covariant_divergence',np.max(np.abs(div2-rhs)),1e-9)
check('reject_second_current_ordinary_coclosed',np.max(np.abs(div2)),1e-4,False)
check('reject_current_bracket_sign',np.max(np.abs(div2+rhs)),1e-4,False)

# The linear funnel alpha is independently assembled from left axial legs.
li,ls=padded(left_axial)
alpha4=sparse.coo_matrix((ls.ravel()/nt,(np.repeat(row,li.shape[1]),li.ravel())),shape=(Ec,Ef+1)).tocsr()[:,:Ef]
alpha=alpha4[::d]
funnel=alpha.T@div2
check('uncorrected_second_current_funnel_nonzero',np.max(np.abs(funnel)),1e-5,False)

# Gauge null and counting-adjoint mutation on actual operators.
lam=np.zeros(Vf);lam[np.flatnonzero(nonroots)[7]]=1
g=df@lam
check('actual_hidden_hessian_null',np.linalg.norm(C.T@(C@g)+kap*Q.T@(Q@g)),1e-10)
check('reject_invert_null_identity',abs(float(g@g)),1e-3,False)
wrong=C.T@(C@a)+kap/L**d*Q.T@(Q@a)-kap*Q.T@b
check('reject_rescaled_counting_adjoint',np.max(np.abs(wrong)),1e-3,False)

# All-Cartan input: actual source zero, versus noncommuting above.
bc=np.zeros_like(b);bc[:,2]=b[:,2]
ac=solve(kap*Q.T@bc);Sc,tc=parts(ac,bc,True)
check('cartan_cubic_source_zero',np.max(np.abs(Sc)),1e-10)

# Constant noncommuting fields have individual BCH2, but the paired centered
# mean vanishes. This tests the proposed constant-field marginal witness.
constants=np.array([[.4,.1,-.2],[-.1,.3,.2],[.2,-.2,.1],[.1,.15,.35]])
b0=np.tile(constants,(Vc,1));a0=np.tile(constants/L,(Vf,1))
c0,(A0,B0,r0)=parts(a0,b0);S0,t0=parts(a0,b0,True)
_,B_each,_=bch(a0,ind,sign,False)
check('constant_mean_BCH2_zero',np.max(np.abs(B0)),1e-12)
check('constant_individual_BCH2_nonzero',np.max(np.abs(B_each)),1e-3,False)
check('constant_residual_zero',np.max(np.abs(r0)),1e-12)
check('constant_cubic_source_zero',np.max(np.abs(S0)),1e-10)
check('constant_soft_quartic_zero',abs(c0['soft4']),1e-10)
_,Bdeleted,_=bch(a0,tind,tsign,False)
constant_deleted_B=float(np.max(np.abs(Bdeleted.reshape(Ec,nt,3).mean(axis=1))))

# Post-exposure controls, prospectively declared after the preserved first run.
gauge_angles=rng.normal(size=(Vf,3))*.1;gauge_angles[roots]=0
gg=qexp(gauge_angles);Ug=qexp(.2*a)
for x0 in itertools.product(range(nf),repeat=d):
    for mu in range(d):
        x=np.array(x0);y=x.copy();y[mu]+=1;e=edge(x,mu,nf)
        gl=gg[sid(x,nf):sid(x,nf)+1];gr=gg[sid(y,nf):sid(y,nf)+1].copy();gr[:,1:]*=-1
        Ug[e]=qm(qm(gl,Ug[e:e+1]),gr)[0]
Vb=qexp(.2*b)
def action_from_links(U,ix,sg):
    Wp=qpaths(U,pi,ps);means=qpaths(U,ix,sg).reshape(Ec,nt,4).mean(axis=1)
    return float(np.sum(1-Wp[:,0])+kap*np.sum(np.linalg.norm(means,axis=1)-np.sum(Vb*means,axis=1)))
original=action(.2*a,.2*b);gauged=action_from_links(Ug,ind,sign)
deleted=action_from_links(qexp(.2*a),tind,tsign)
deleted_gauged=action_from_links(Ug,tind,tsign)
check('exact_group_rootfixed_gauge_invariance',abs(gauged-original),1e-9)
check('reject_deleted_endpoint_exact_action',abs(deleted-original),1e-6,False)
check('reject_deleted_endpoint_gauge_invariance',abs(deleted_gauged-deleted),1e-6,False)
# With commutators deleted, B=C=0 in the same local polynomial and S=0.
pA,_,_=bch(a,pi,ps,False);A,_,_=bch(a,ind,sign,False);A=A.reshape(Ec,nt,3)
Ab0=A.mean(axis=1);aa=(Ab0*Ab0).sum(axis=1);bb=(b*b).sum(axis=1)
s2=-(A*A).sum(axis=2).mean(axis=1)/2
V30=(-np.sum(A*A,axis=2)[:,:,None]*A/6).mean(axis=1)
abelianized4=-np.sum(np.sum(pA*pA,axis=1)**2)/24+kap*(np.sum((Ab0-b)*V30)+np.sum((bb-aa)*s2/2-aa*aa/8-bb*bb/24+bb*np.sum(b*Ab0,axis=1)/6))
check('reject_deleted_colour_commutators',abs(rich-abelianized4),10*tol,False)

details.update(geometry=dict(d=d,L=L,T=T,finest_side=nf,fine_edges=Ef,top_edges=Ec,paths=len(paths),paths_per_link=nt,max_length=int(ind.shape[1]),plaquettes=len(plaq),gauge_columns=G.shape[1]),coefficients=coef,cubic=third,exchange=exchange,stationary_quartic=pred,exact_group_samples=samples,richardson=rich,current=dict(max_divergence=float(np.max(np.abs(div2))),max_commutator=float(np.max(np.abs(rhs))),funnel_max=float(np.max(np.abs(funnel)))),constant_control=dict(coefficients=c0,source_norm=float(np.linalg.norm(S0)),individual_BCH2_max=float(np.max(np.abs(B_each)))),solves=solves)
out=dict(scope='finite actual normalized SU2 S4-prime tree phase; author check',checks=checks,passed=sum(x['passed'] for x in checks),total=len(checks),details=details,elapsed_seconds=time.time()-start)
out['diagnostics']=dict(failed_initial_constant_endpoint_detector=constant_deleted_B,exact_action=original,gauge_action=gauged,deleted_endpoint_action=deleted,deleted_endpoint_gauge_action=deleted_gauged,commutator_deleted_quartic=float(abelianized4))
print(json.dumps(out,indent=2,allow_nan=False))
raise SystemExit(0 if all(x['passed'] for x in checks) else 1)
