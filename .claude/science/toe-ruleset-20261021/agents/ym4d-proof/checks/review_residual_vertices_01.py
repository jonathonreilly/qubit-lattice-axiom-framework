"""Independent actual S4-prime/Wilson flat-Cartan charged-sector vertex controls.
All paths, transports, curl rows and covariant frames are built directly.
"""
import numpy as np
from itertools import product,permutations,combinations
from collections import defaultdict
import json,sys
from datetime import datetime,timezone
ell=3;d=4;nv=81;nf=324;kappa=1.5;r=80;alpha=9
sites=list(product(range(-1,2),repeat=d));idx={x:i for i,x in enumerate(sites)};root=idx[(0,0,0,0)]
J=np.eye(nv)[:,root:root+1];Pint=np.eye(nv)-J@J.T
vv=J[:,0]-np.ones(nv)/9;shape=np.eye(nv)-2*np.outer(vv,vv)/np.dot(vv,vv);shape4=np.kron(shape,np.eye(4))
low=list(range(4*root,4*root+4));high=[j for j in range(nf) if j not in low]
checks={};samples=[];started=datetime.now(timezone.utc).isoformat()
def ck(n,v):checks[n]=bool(v)
def locate(p):
 c=tuple((int(z)+1)//ell for z in p);q=tuple(int(p[j])-ell*c[j] for j in range(d));return idx[q],c
rows=[defaultdict(int) for _ in range(d)]
def edge(row,p,mu,sign,shift=(0,0,0,0)):
 q=tuple(p[j]+shift[j] for j in range(d));i,c=locate(q);row[(4*i+mu,c)]+=sign
for mu in range(d):
 for y in sites:
  for order in permutations(range(d)):
   p=[0]*d;path=[]
   for nu in order:
    sg=1 if y[nu]>=0 else -1
    for _ in range(abs(y[nu])):
     q=p.copy()
     if sg<0:q[nu]-=1
     path.append((tuple(q),nu,sg));p[nu]+=sg
   for q,nu,sg in path:edge(rows[mu],q,nu,sg)
   p=list(y)
   for _ in range(ell):edge(rows[mu],p,mu,1);p[mu]+=1
   shift=tuple(ell if j==mu else 0 for j in range(d))
   for q,nu,sg in reversed(path):edge(rows[mu],q,nu,-sg,shift)
def geometry(K,A):
 K=np.asarray(K,float);A=np.asarray(A,float);a=A/ell
 D=np.zeros((nf,nv),complex)
 for p in sites:
  i=idx[p]
  for mu in range(d):
   q=list(p);q[mu]+=1;j,c=locate(q)
   D[4*i+mu,i]+=np.exp(-1j*a[mu]);D[4*i+mu,j]-=np.exp(1j*np.dot(K,c))
 pairs=list(combinations(range(d),2));curl=np.zeros((6*nv,nf),complex)
 for p in sites:
  i=idx[p]
  for ip,(mu,nu) in enumerate(pairs):
   row=6*i+ip;q=list(p);q[mu]+=1;j,c=locate(q)
   curl[row,4*i+mu]+=np.exp(1j*a[mu]);curl[row,4*j+nu]+=np.exp(1j*(a[mu]+a[nu]+np.dot(K,c)))
   q=list(p);q[nu]+=1;j,c=locate(q)
   curl[row,4*j+mu]-=np.exp(1j*(a[mu]+a[nu]+np.dot(K,c)));curl[row,4*i+nu]-=np.exp(1j*a[nu])
 M=np.zeros((d,nf),complex)
 for mu,row in enumerate(rows):
  endcoarse=np.zeros(d);endcoarse[mu]=ell
  for (j,c),count in row.items():
   x=np.asarray(sites[j//4],float)+ell*np.asarray(c);x[j%4]+=1
   M[mu,j]+=count*np.exp(1j*np.dot(K,c)-1j*np.dot(a,endcoarse-x))/(24*nv)
 dc=(np.exp(-1j*A)-np.exp(1j*K)).reshape(d,1);H=curl.conj().T@curl
 phase=[]
 for p in sites:
  for mu in range(d):q=np.asarray(p,float).copy();q[mu]+=1;phase.append(np.exp(-1j*np.dot(a,q)))
 frame=np.asarray(phase)[:,None]*shape4
 Rc=1/(1+float(np.vdot(dc,dc).real)/kappa)
 return D,M,dc,H,frame,Rc
def schur(D,M,dc,H,frame,Rc,u,v,du,dv):
 rootfix=u*(J.T@D.conj().T)+v*np.sqrt(Rc)*dc.conj().T@M
 F=Pint@D.conj().T+J@rootfix
 dotf=du*(J.T@D.conj().T)+dv*np.sqrt(Rc)*dc.conj().T@M
 Q=H+F.conj().T@F;E0=frame[:,low];EH=frame[:,high];B=EH.conj().T@Q@E0;C=EH.conj().T@Q@EH
 E=E0-EH@np.linalg.solve(C,B);q=E0.conj().T@Q@E0-B.conj().T@np.linalg.solve(C,B)
 return E,q,dotf@E,F,Q
D,M,dc,H,frame,Rc=geometry(np.zeros(4),np.zeros(4))
Z=H+kappa*M.conj().T@M+D@Pint@D.conj().T
ck('actual_unminimized_internal_gap_at_zero',np.linalg.eigvalsh(Z)[0]>1e-6)
ck('covariant_frame_unitary',np.linalg.norm(frame.conj().T@frame-np.eye(nf))<1e-10)
ck('constant_contour_normalization',np.linalg.norm(M@frame[:,low]-np.eye(4)/3)<1e-10)
directions=[np.array([1.,0,0,0]),np.array([1.,2,-1,3])/np.sqrt(15)]
for u in [.25,.5,.75]:
 aa=np.sqrt(1+r*u*u);v=aa-alpha*u;dv=r*u/aa-alpha
 for mode in ['free_momentum','constant_Cartan_background']:
  for idir,omega in enumerate(directions):
   knorms=[]
   for scale in [.04,.02,.01]:
    K=scale*omega if mode=='free_momentum' else np.zeros(4);A=np.zeros(4) if mode=='free_momentum' else scale*omega
    D,M,dc,H,frame,Rc=geometry(K,A);E,q,k,F,Q=schur(D,M,dc,H,frame,Rc,u,v,1,dv)
    tag=f'{u}_{mode}_{idir}_{scale}'
    ck('actual_MD_covariance_'+tag,np.linalg.norm(M@D-dc@J.T)<1e-10)
    ck('actual_Wilson_gauge_row_'+tag,np.linalg.norm(H@D)<1e-10)
    err=float(np.linalg.norm(q/scale**2-np.eye(4)/9,2));kn=float(np.linalg.norm(k));knorms.append(kn)
    ck('tuned_low_principal_'+tag,err<=2*scale)
    ck('partial_dotF_double_zero_'+tag,kn<=10*scale**2)
    samples.append({'u':u,'mode':mode,'direction':idir,'scale':scale,'principal_error':err,'partial_dotF_norm':kn,'norm_over_scale2':kn/scale**2})
   ck(f'double_zero_convergence_{u}_{mode}_{idir}',knorms[-1]<.4*knorms[-2] or max(knorms[-2:])<1e-10)
# Explicit wrong-path and wrong-differentiation controls at the declared midpoint.
scale=.01;D,M,dc,H,frame,Rc=geometry(np.array([scale,0,0,0]),np.zeros(4))
E,q,k,F,Q=schur(D,M,dc,H,frame,Rc,.5,.5,-1,1)
ck('straight_path_partial_dotF_control',np.linalg.norm(k)/scale>1e-3)
ck('straight_path_wrong_principal_control',np.linalg.norm(q/scale**2-np.eye(4)/9,2)>.01)
u=.5;step=1e-5
values=[]
for w in [u-step,u+step]:
 aa=np.sqrt(1+r*w*w);v=aa-alpha*w;dv=r*w/aa-alpha
 E,q,k,F,Q=schur(D,M,dc,H,frame,Rc,w,v,1,dv);values.append(J.T@F@E)
total=(values[1]-values[0])/(2*step)
ck('total_derivative_is_not_partial_dotF_control',np.linalg.norm(total)/scale>1e-3)
print(json.dumps({'started_utc':started,'finished_utc':datetime.now(timezone.utc).isoformat(),'scope':'actual one-step d=4 free/flat-Cartan contour and Wilson Hessian; numerical controls, not a proof of arbitrary off-shell jets or limits','checks':checks,'passed':sum(checks.values()),'total':len(checks),'samples':samples,'wrong_total_derivative_over_scale':float(np.linalg.norm(total)/scale)},indent=2,sort_keys=True));sys.exit(0 if all(checks.values()) else 1)
