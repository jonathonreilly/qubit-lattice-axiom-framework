"""Independent actual periodic d=4 S4-prime controls, L=3,T=2."""
from itertools import product,permutations,combinations
import json,sys,time
import numpy as np
import scipy
from scipy import sparse as sp
from scipy.sparse.linalg import splu,cg,LinearOperator
from scipy.linalg import eigh

started=time.monotonic()
checks=[];details={}
def check(name,condition,detail=None):
    checks.append({'name':name,'passed':bool(condition),'detail':detail})
def norm(x):
    return float(np.max(np.abs(x)))
def logdet_sparse(M):
    lu=splu(sp.csc_matrix(M))
    return float(np.log(np.abs(lu.U.diagonal())).sum())
def lap(side):
    pts=list(product(range(side),repeat=4));idx={p:i for i,p in enumerate(pts)}
    rows=[];cols=[];vals=[]
    for i,x in enumerate(pts):
        for mu in range(4):
            y=list(x);y[mu]=(y[mu]+1)%side
            rows.extend([4*i+mu]*2);cols.extend([i,idx[tuple(y)]]);vals.extend([-1.,1.])
    return pts,idx,sp.csr_matrix((vals,(rows,cols)),shape=(4*len(pts),len(pts)))

L=3;T=2;side=L*T;kappa=1.3
pts,idx,d=lap(side);cpts,cidx,dc=lap(T)
V=len(pts);Vc=len(cpts);nf=4*V;nc=4*Vc
rootids=np.array([idx[tuple(L*t for t in x)] for x in cpts])
interior=np.array([i for i in range(V) if i not in set(rootids)])
J=sp.csc_matrix((np.ones(Vc),(rootids,np.arange(Vc))),shape=(V,Vc))
I=sp.csc_matrix((np.ones(len(interior)),(interior,np.arange(len(interior)))),shape=(V,len(interior)))
Delta=(d.T@d).tocsc();Deltac=(dc.T@dc).toarray()

# Plaquette incidence is constructed directly from its four oriented edges.
crow=[];ccol=[];cval=[]
for i,x in enumerate(pts):
    for pair,(mu,nu) in enumerate(combinations(range(4),2)):
        y=list(x);y[mu]=(y[mu]+1)%side
        z=list(x);z[nu]=(z[nu]+1)%side
        row=6*i+pair
        crow.extend([row]*4);ccol.extend([4*i+mu,4*idx[tuple(y)]+nu,4*idx[tuple(z)]+mu,4*i+nu]);cval.extend([1,1,-1,-1])
curl=sp.csr_matrix((cval,(crow,ccol)),shape=(6*V,nf))
check('actual_incidence_curl_d_zero',(curl@d).nnz==0)

# All relative contour paths, then periodization to every coarse root.
def segment(start,end,order):
    pos=list(start);edges=[]
    for mu in order:
        while pos[mu]!=end[mu]:
            sign=1 if end[mu]>pos[mu] else -1
            if sign<0:pos[mu]-=1
            edges.append((tuple(pos),mu,sign))
            if sign>0:pos[mu]+=1
    return edges
paths=[]
for mu in range(4):
    rows=[]
    otherroot=tuple(L if j==mu else 0 for j in range(4))
    for y in product((-1,0,1),repeat=4):
        yp=tuple(y[j]+(L if j==mu else 0) for j in range(4))
        for order in permutations(range(4)):
            edges=segment((0,0,0,0),y,order)+segment(y,yp,(mu,))
            edges += [(p,m,-sg) for p,m,sg in segment(otherroot,yp,order)]
            rows.append(edges)
    paths.append(rows)
per=24*L**4
rows=[];cols=[];data=[]
for ci,c in enumerate(cpts):
    origin=tuple(L*t for t in c)
    for mu in range(4):
        for pi,edges in enumerate(paths[mu]):
            row=(4*ci+mu)*per+pi
            for p,m,sg in edges:
                x=tuple((origin[j]+p[j])%side for j in range(4))
                rows.append(row);cols.append(4*idx[x]+m);data.append(sg)
P=sp.csr_matrix((data,(rows,cols)),shape=(nc*per,nf),dtype=float)
P.sum_duplicates();P.eliminate_zeros()
averager=sp.csr_matrix((np.full(nc*per,1/per),(np.repeat(np.arange(nc),per),np.arange(nc*per))),shape=(nc,nc*per))
Q=(averager@P).tocsr()
ev=J.T
cov_error=norm((Q@d-dc@ev).toarray())
check('actual_full_periodic_S4_prime_Qd',cov_error<2e-10,cov_error)
check('actual_full_periodic_contour_count',P.shape[0]==16*4*24*81,P.shape)

# Scalar domains and determinant factors, computed in the full periodic space.
A=(I.T@Delta@I).tocsc();alu=splu(A)
B=(I.T@Delta@J).toarray()
Lhar=J.toarray()-I@alu.solve(B)
S=(J.T@Delta@J).toarray()-B.T@alu.solve(B)
sev,sevectors=eigh(S)
Splus=(sevectors[:,1:]/sev[1:])@sevectors[:,1:].T
DL=Delta@Lhar
Qper=np.eye(V)-(DL@Splus)@(DL@Splus).T
expected=np.eye(V)-J@J.T+J@np.full((Vc,Vc),1/Vc)@J.T
qerr=norm(Qper-expected)
check('periodic_harmonic_projection_with_root_mean',qerr<2e-9,qerr)
check('root_mean_omission_is_detected',norm(Qper-(np.eye(V)-J@J.T))>.01)
check('harmonic_lift_constant',norm(Lhar@np.ones(Vc)-np.ones(V))<2e-10)
check('scalar_S_single_constant_kernel',abs(sev[0])<2e-10 and sev[1]>1e-4,sev.tolist())
logA=logdet_sparse(A)
logSp=float(np.log(sev[1:]).sum())
logDeltap=np.log(V)+logdet_sparse(Delta[1:,1:])
gram_error=abs(logDeltap-logA-logSp-np.log(L**4))
check('actual_4D_scalar_ell4_Gram',gram_error<2e-8,gram_error)
check('scalar_Gram_omission_is_detected',abs(logDeltap-logA-logSp)>4)
details['scalar_domains']={'fine_sites':V,'coarse_sites':Vc,'projection_error':qerr,'scalar_log_Gram_error':gram_error,'ell4':L**4}

base=np.array([.023*np.sin(2*np.pi*x[(mu+1)%4]/side)+.017*np.cos(2*np.pi*(x[0]+x[2])/side)*(mu+1)/4 for x in pts for mu in range(4)])
harmfine=np.zeros((nf,4));harmcoarse=np.zeros((nc,4))
for mu in range(4):
    harmfine[mu::4,mu]=1/np.sqrt(V)
    harmcoarse[mu::4,mu]=1/np.sqrt(Vc)
samples=[]
for scale in (0.,.7,1.1):
    a=scale*base
    phase=(P@a).reshape(nc,per)
    mean=np.exp(1j*phase).mean(axis=1)
    weights=np.real(np.exp(1j*phase)/mean[:,None])/per
    M=sp.csr_matrix((weights.ravel(),(np.repeat(np.arange(nc),per),np.arange(nc*per))),shape=(nc,nc*per))@P
    C=1/(kappa*np.abs(mean))
    nonlinear_cov=norm((M@d-dc@ev).toarray())
    harmonic=norm(M@harmfine-(1/L)*harmcoarse)
    Rc=np.eye(Vc)+dc.T@sp.diags(C)@dc
    vals,vec=eigh(np.asarray(Rc))
    Rh=(vec/np.sqrt(vals))@vec.T
    # Fbar*d is assembled from the actual M*d, not covariance substituted.
    rootrows=np.full((Vc,Vc),1/Vc)@(J.T@Delta).toarray()+Rh@dc.T@(M@d).toarray()
    Fd=Delta.tolil(copy=True)
    for j,r in enumerate(rootids):Fd[r,:]=rootrows[j]
    Fd=Fd.tocsc()
    kernel_error=max(norm(np.asarray(Fd.sum(axis=0))),norm(np.asarray(Fd.sum(axis=1))))
    logF=np.log(V)+logdet_sparse(Fd[1:,1:])
    coarse_eig=eigh(Deltac,eigvals_only=True)
    expected_log=np.log(L**4)+logA+np.log(coarse_eig[1:]).sum()-.5*np.log(vals).sum()
    derr=abs(logF-expected_log)
    check(f'actual_nonlinear_neutral_Md_scale_{scale}',nonlinear_cov<2e-10,nonlinear_cov)
    check(f'actual_nonlinear_neutral_harmonic_map_scale_{scale}',harmonic<2e-10,harmonic)
    check(f'completed_ghost_fixed_left_right_kernels_scale_{scale}',kernel_error<2e-10,kernel_error)
    check(f'completed_ghost_ell4_determinant_scale_{scale}',derr<2e-8,derr)
    graph=np.eye(4)+(M@harmfine).T@(M@harmfine)
    harmonic_transfer=harmcoarse.T@(M@harmfine)
    coarse_harmonic_lift=harmfine@np.linalg.inv(harmonic_transfer)
    check(f'fine_harmonic_graph_Gram_scale_{scale}',norm(graph-(1+L**-2)*np.eye(4))<2e-10)
    check(f'coarse_harmonic_graph_Gram_scale_{scale}',norm(np.eye(4)+coarse_harmonic_lift.T@coarse_harmonic_lift-(1+L**2)*np.eye(4))<2e-10)
    samples.append({'scale':scale,'M_gauge_error':nonlinear_cov,'M_harmonic_error':harmonic,'completed_ghost_kernel_error':kernel_error,'logdet_error':derr,'covariance_range':[float(C.min()),float(C.max())]})
details['actual_background_samples']=samples

# The actual one-step linear stationary chain, internal gauge completed.
v=np.array([.4*((-1)**c[1]) if mu==0 else 0 for c in cpts for mu in range(4)])
Z=(curl.T@curl+kappa*Q.T@Q+d@I@I.T@d.T).tocsr()
rhs=kappa*(Q.T@v)
diag=Z.diagonal()
a,info=cg(Z,rhs,rtol=2e-13,atol=1e-14,maxiter=3000,M=LinearOperator(Z.shape,matvec=lambda z:z/diag))
res=float(np.linalg.norm(Z@a-rhs)/np.linalg.norm(rhs))
check('actual_quadratic_stationary_solve',info==0 and res<2e-10,{'info':int(info),'relative_residual':res})
check('actual_stationary_internal_gauge',norm(I.T@d.T@a)<2e-10,norm(I.T@d.T@a))
f=curl@a;theta=(P@a).reshape(nc,per);bar=theta.mean(axis=1);r=v-bar;z=theta-bar[:,None]
parts=[-np.sum(f**4)/24,kappa*np.sum(r*np.mean(z**3,axis=1))/6,-kappa*np.sum(r*r*np.mean(z*z,axis=1))/4,-kappa*np.sum(r**4)/24]
E4=float(sum(parts));E2=float(.5*np.dot(f,f)+.5*kappa*np.dot(r,r))
def energy(af,bf):
    fp=np.asarray(curl@af,dtype=np.longdouble)
    ph=np.asarray((P@af).reshape(nc,per),dtype=np.longdouble)
    bm=np.asarray(bf,dtype=np.longdouble)
    mm=np.exp(1j*ph).mean(axis=1)
    return np.sum(1-np.cos(fp))+np.longdouble(kappa)*np.sum(np.abs(mm)-np.real(np.exp(-1j*bm)*mm))
epsilons=(.15,.075,.0375)
quartics={}
for name,c in [('linear',np.zeros(nf)),('cubic_corrected',.02*base)]:
    values=[]
    for eps in epsilons:
        e=energy(eps*a+eps**3*c,eps*v)
        values.append(float((e-np.longdouble(eps)**2*np.longdouble(E2))/np.longdouble(eps)**4))
    ext=(4*values[-1]-values[-2])/3
    check('actual_normalized_quartic_'+name,abs(ext-E4)<2e-7*(1+abs(E4)),{'direct_values':values,'Richardson':ext,'FC18':E4,'error':abs(ext-E4)})
    quartics[name]={'direct':values,'Richardson':ext}
check('actual_neutral_quartic_is_nonzero',abs(E4)>1e-8,E4)
check('actual_polar_variance_term_is_nonzero',abs(parts[2])>1e-10,parts[2])
details['stationary_quartic']={'E2':E2,'FC18_parts':parts,'E4':E4,'epsilon':epsilons,'samples':quartics}

# Harmonic shift at a nonzero residual, using the exact normalized action.
af=base;theta=(P@af).reshape(nc,per);bf=np.angle(np.exp(1j*theta).mean(axis=1))+.013*np.sin(np.arange(nc))
shift=np.array([.007,-.003,.005,.002])
e0=energy(af,bf);e1=energy(af+np.tile(shift,V),bf+L*np.tile(shift,Vc))
check('exact_action_harmonic_shift_at_nonzero_residual',abs(float(e1-e0))<2e-10,float(e1-e0))
check('harmonic_measure_log_ratio',abs(.5*np.log((1+L**-2)/(1+L**2))+np.log(L))<1e-14)
output={'scope':'Finite numerical d=4 actual S4-prime/Wilson controls, no interval or uniform theorem','passed':sum(c['passed'] for c in checks),'total':len(checks),'checks':checks,'details':details,'seconds':time.monotonic()-started,'versions':{'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__}}
print(json.dumps(output,indent=2))
sys.exit(0 if all(c['passed'] for c in checks) else 1)
