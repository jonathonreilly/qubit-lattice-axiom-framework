#!/usr/bin/env python3
"""Actual 4D depth-two rectangular SU2 chain; no predecessor imports."""
import itertools,json,time
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import LinearOperator,cg
import torch
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
start=time.time();L=3;d=4;kap=[.7,1.4];shapes=[(18,9,9,9),(6,3,3,3),(2,1,1,1)]
checks=[];solves=[]
def check(name,x,tol=1e-9,positive=False):
    x=float(x);checks.append(dict(name=name,value=x,threshold=tol,positive=positive,passed=x>tol if positive else x<=tol))
def geometry(shape):
    shape=np.array(shape);V=int(np.prod(shape));E=d*V
    sites=np.array(list(itertools.product(*[range(s) for s in shape])),dtype=int)
    def ids(x):return np.ravel_multi_index(tuple((x%shape).T),tuple(shape))
    heads=np.column_stack([ids(sites+np.eye(d,dtype=int)[mu]) for mu in range(d)])
    tails=np.repeat(np.arange(V),d)
    grad=sparse.coo_matrix((np.tile([-1.,1.],E),(np.repeat(np.arange(E),2),np.column_stack([tails,heads.ravel()]).ravel())),shape=(E,V)).tocsr()
    pairs=list(itertools.combinations(range(d),2));pi=[]
    for mu,nu in pairs:
        pi.append(np.column_stack([d*np.arange(V)+mu,d*heads[:,mu]+nu,d*heads[:,nu]+mu,d*np.arange(V)+nu]))
    pi=np.concatenate(pi);ps=np.tile([1.,1.,-1.,-1.],(len(pi),1))
    curl=sparse.coo_matrix((ps.ravel(),(np.repeat(np.arange(len(pi)),4),pi.ravel())),shape=(len(pi),E)).tocsr()
    return dict(shape=shape,V=V,E=E,sites=sites,heads=heads,grad=grad,curl=curl,pi=pi,ps=ps)
gs=[geometry(s) for s in shapes]
def block(g,coarse):
    ns=coarse['V'];patterns=[];lpatterns=[]
    def axial(off,order,root):
        x=np.array(root);out=[]
        for mu in order:
            for k in range(abs(off[mu])):
                sg=int(np.sign(off[mu]))
                if sg<0:x[mu]-=1
                out.append((tuple(x),mu,sg))
                if sg>0:x[mu]+=1
        return out
    for mu in range(d):
        for order in itertools.permutations(range(d)):
            for off in itertools.product(range(-1,2),repeat=d):
                left=axial(off,order,np.zeros(d,dtype=int));x=np.array(off);mid=[]
                for k in range(L):mid.append((tuple(x),mu,1));x[mu]+=1
                endroot=np.zeros(d,dtype=int);endroot[mu]=L
                right=axial(off,order,endroot)
                patterns.append(left+mid+[(p,m,-s) for p,m,s in right[::-1]])
                lpatterns.append(left)
    nt=24*L**d;P=d*nt;le=11
    rel=np.zeros((P,le,d),dtype=int);dirs=np.zeros((P,le),dtype=int);sg=np.zeros((P,le))
    rel_left=np.zeros_like(rel);dirs_left=np.zeros_like(dirs);sg_left=np.zeros_like(sg)
    for j,p in enumerate(patterns):
        for k,(x,mu,s) in enumerate(p):rel[j,k]=x;dirs[j,k]=mu;sg[j,k]=s
    for j,p in enumerate(lpatterns):
        for k,(x,mu,s) in enumerate(p):rel_left[j,k]=x;dirs_left[j,k]=mu;sg_left[j,k]=s
    roots=L*coarse['sites']+1
    def absolute(rr,dd,ss):
        pts=(roots[:,None,None,:]+rr[None,:,:,:])%g['shape']
        idx=(d*np.ravel_multi_index(tuple(pts.reshape(-1,d).T),tuple(g['shape'])).reshape(ns,P,le)+dd).reshape(-1,le)
        signs=np.broadcast_to(ss,(ns,P,le)).reshape(-1,le).copy()
        idx[signs==0]=g['E']
        return idx.astype(np.int32),signs
    ix,sg=absolute(rel,dirs,sg);li,ls=absolute(rel_left,dirs_left,sg_left)
    rows=np.repeat(np.arange(coarse['E']),nt*le)
    Q=sparse.coo_matrix((sg.ravel()/nt,(rows,ix.ravel())),shape=(coarse['E'],g['E']+1)).tocsr()[:,:g['E']];Q.eliminate_zeros()
    alpha4=sparse.coo_matrix((ls.ravel()/nt,(rows,li.ravel())),shape=(coarse['E'],g['E']+1)).tocsr()[:,:g['E']];alpha=alpha4[::d];alpha.eliminate_zeros()
    rid=np.ravel_multi_index(tuple(roots.T),tuple(g['shape']))
    ev=sparse.csr_matrix((np.ones(ns),(np.arange(ns),rid)),shape=(ns,g['V']))
    check('root_covariance',np.max(np.abs((Q@g['grad']-coarse['grad']@ev).data),initial=0))
    return dict(ix=ix,sg=sg,Q=Q,alpha=alpha,ev=ev,nt=nt)
bs=[block(gs[j],gs[j+1]) for j in range(2)]
Q0,Q1=[b['Q'] for b in bs];E0,E1=gs[0]['E'],gs[1]['E'];C=gs[0]['curl']
ev0=bs[0]['ev'];evtop=bs[1]['ev']@ev0
rootids=evtop.indices;keep=np.ones(gs[0]['V'],dtype=bool);keep[rootids]=False
G=sparse.vstack([gs[0]['grad'],gs[1]['grad']@ev0],format='csr')[:,keep]
def hop(x):
    x0,x1=x[:E0],x[E0:];rr=x1-Q0@x0
    return np.concatenate([C.T@(C@x0)-kap[0]*Q0.T@rr,kap[0]*rr+kap[1]*Q1.T@(Q1@x1)])+G@(G.T@x)
diag=np.concatenate([np.asarray(C.power(2).sum(axis=0)).ravel()+kap[0]*np.asarray(Q0.power(2).sum(axis=0)).ravel(),kap[0]+kap[1]*np.asarray(Q1.power(2).sum(axis=0)).ravel()])+np.asarray(G.power(2).sum(axis=1)).ravel()
H=LinearOperator((E0+E1,E0+E1),matvec=hop,dtype=float);P=LinearOperator(H.shape,matvec=lambda x:x/diag,dtype=float)
def solve(rhs):
    z=np.empty_like(rhs)
    for a in range(3):
        iterations=[0]
        def cb(x):iterations[0]+=1
        z[:,a],info=cg(H,rhs[:,a],M=P,rtol=2e-12,atol=1e-14,maxiter=5000,callback=cb)
        err=np.linalg.norm(hop(z[:,a])-rhs[:,a])/max(1,np.linalg.norm(rhs[:,a]))
        solves.append(dict(info=int(info),iterations=iterations[0],relative_error=float(err)));check('solve',err)
    return z
def bch2(a,ix,sg):
    a=torch.cat([a,torch.zeros((1,3))]);ix=torch.tensor(ix,dtype=torch.long);sg=torch.tensor(sg)
    A=torch.zeros((len(ix),3));B=torch.zeros_like(A)
    for j in range(ix.shape[1]):
        v=a[ix[:,j]]*sg[:,j,None];B=B+torch.linalg.cross(A,v,dim=-1);A=A+v
    return A,B
rng=np.random.default_rng(20261030);top=rng.normal(size=(gs[2]['E'],3))*.6
rhs=np.concatenate([np.zeros((E0,3)),kap[1]*Q1.T@top]);linear=solve(rhs)
avec=[linear[:E0],linear[E0:],top]
source=np.zeros_like(linear);means=[];residuals=[];dbsources=[]
# Accumulate each graph separately to keep memory bounded. The derivative with
# respect to the upper field is -kappa Bbar, lower is kappa Q*Bbar-kappa DB* r.
for j in range(2):
    aa=torch.tensor(avec[j],requires_grad=True);A,B=bch2(aa,bs[j]['ix'],bs[j]['sg'])
    A=A.reshape(gs[j+1]['E'],bs[j]['nt'],3).mean(dim=1)
    B=B.reshape(gs[j+1]['E'],bs[j]['nt'],3).mean(dim=1)
    r=torch.tensor(avec[j+1])-A;scalar=-kap[j]*(r*B).sum()
    lower=torch.autograd.grad(scalar,aa)[0].detach().numpy()
    bb=B.detach().numpy();rr=r.detach().numpy();means.append(bb);residuals.append(rr)
    dbsources.append(kap[j]*bs[j]['Q'].T@bb-lower)
    if j==0:source[:E0]+=lower;source[E0:]-=kap[j]*bb
    else:source[E0:]+=lower
    del aa,A,B,r,scalar,lower
aa=torch.tensor(avec[0],requires_grad=True);fa,fb=bch2(aa,gs[0]['pi'],gs[0]['ps']);w3=(fa*fb).sum();source[:E0]+=torch.autograd.grad(w3,aa)[0].detach().numpy()
del aa,fa,fb,w3
check('composite_rootzero_gauge_source',np.max(np.abs(G.T@source)))
second=-solve(source);a2=[second[:E0],second[E0:],np.zeros_like(top)]
qq=[kap[j]*(a2[j+1]-bs[j]['Q']@a2[j]-means[j]) for j in range(2)]
full=Q1.T@qq[1]+dbsources[1]
check('intermediate_exact_q_recursion',np.max(np.abs(qq[0]-full)))
check('reject_omitted_DB_source',np.max(np.abs(qq[0]-Q1.T@qq[1])),1e-6,True)
check('reject_wrong_kappa_ratio',np.max(np.abs(qq[0]-(kap[0]/kap[1])*full)),1e-6,True)
current=[]
for j in range(2):
    coarse=gs[j+1];bracket=2*np.cross(avec[j+1],kap[j]*residuals[j])
    out=bracket.reshape(coarse['V'],d,3).sum(axis=1)
    incoming=np.zeros_like(out)
    for mu in range(d):np.add.at(incoming,coarse['heads'][:,mu],bracket[mu::d])
    div=coarse['grad'].T@qq[j]
    check('log_current_symmetric_bracket',np.max(np.abs(div-(out+incoming)/2)))
    J2=qq[j]-bracket/2
    check('right_current_covariant_divergence',np.max(np.abs(coarse['grad'].T@J2-out)))
    current.append(dict(max_q=float(np.max(np.abs(qq[j]))),max_div_q=float(np.max(np.abs(div))),max_mean_B=float(np.max(np.abs(means[j]))),max_DB_source=float(np.max(np.abs(dbsources[j])))))
Qstr=Q1+gs[2]['grad']@bs[1]['alpha']
funnel=-bs[1]['alpha'].T@(gs[2]['grad'].T@qq[1])
error=dbsources[1]+funnel
check('forced_straight_current_recursion',np.max(np.abs(qq[0]-Qstr.T@qq[1]-error)))
check('reject_omitted_funnel',np.max(np.abs(qq[0]-Qstr.T@qq[1]-dbsources[1])),1e-6,True)
check('reject_funnel_sign',np.max(np.abs(qq[0]-Qstr.T@qq[1]-dbsources[1]+funnel)),1e-6,True)
output=dict(scope='actual d4 rectangular periodic depth2 S4-prime SU2 tree; source control only',geometry=[dict(side=g['shape'].tolist(),links=g['E']) for g in gs],kappas=kap,paths=[len(b['ix']) for b in bs],source_norm=float(np.linalg.norm(source)),exchange=float(-.5*np.sum(source*second)),current=current,max_funnel=float(np.max(np.abs(funnel))),checks=checks,solves=solves,passed=sum(c['passed'] for c in checks),total=len(checks),elapsed_seconds=time.time()-start)
print(json.dumps(output,indent=2,allow_nan=False));raise SystemExit(0 if all(c['passed'] for c in checks) else 1)
