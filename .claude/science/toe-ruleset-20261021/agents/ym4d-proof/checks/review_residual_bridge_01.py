"""Independent actual d=4, L=3 free-contour controls; numerical samples are not proofs.
The contour map is built by enumerating edges of all 24 ordered root paths.
"""
from itertools import product,permutations,combinations
from collections import defaultdict
from datetime import datetime,timezone
import numpy as np
import json,sys,platform
ell=3;d=4;nv=ell**d;nf=d*nv;kappa=1.5
sites=list(product(range(-1,2),repeat=d));index={p:i for i,p in enumerate(sites)};root=index[(0,)*d]
checks={};details={};started=datetime.now(timezone.utc).isoformat()
def check(n,v):checks[n]=bool(v)
def locate(p):
 shifts=tuple((int(z)+1)//ell for z in p);q=tuple(int(p[j])-ell*shifts[j] for j in range(d))
 return index[q],shifts
def add_edge(row,p,mu,sign,shift=(0,0,0,0)):
 # The link is p -> p+e_mu; sign specifies oriented path integration.
 position=tuple(p[j]+shift[j] for j in range(d));i,c=locate(position);row[(d*i+mu,c)]+=sign
# Compile each complete contour with integer multiplicities; normalize only once.
contour=[defaultdict(int) for _ in range(d)]
for mu in range(d):
 for endpoint in sites:
  for order in permutations(range(d)):
   p=[0]*d;path=[]
   for nu in order:
    step=1 if endpoint[nu]>=0 else -1
    for _ in range(abs(endpoint[nu])):
     origin=p.copy()
     if step<0:origin[nu]-=1
     path.append((tuple(origin),nu,step));p[nu]+=step
   for origin,nu,sign in path:add_edge(contour[mu],origin,nu,sign)
   p=list(endpoint)
   for _ in range(ell):add_edge(contour[mu],p,mu,1);p[mu]+=1
   translated=tuple(ell if j==mu else 0 for j in range(d))
   for origin,nu,sign in reversed(path):add_edge(contour[mu],origin,nu,-sign,translated)
def matrices(K):
 K=np.asarray(K,float);D=np.zeros((nf,nv),complex)
 for p in sites:
  i=index[p]
  for mu in range(d):
   q=list(p);q[mu]+=1;j,c=locate(q);D[d*i+mu,j]+=np.exp(1j*np.dot(K,c));D[d*i+mu,i]-=1
 pairs=list(combinations(range(d),2));curl=np.zeros((len(pairs)*nv,nf),complex)
 for p in sites:
  i=index[p]
  for ip,(mu,nu) in enumerate(pairs):
   row=len(pairs)*i+ip;q=list(p);q[mu]+=1;j,c=locate(q)
   curl[row,d*j+nu]+=np.exp(1j*np.dot(K,c));curl[row,d*i+nu]-=1
   q=list(p);q[nu]+=1;j,c=locate(q)
   curl[row,d*j+mu]-=np.exp(1j*np.dot(K,c));curl[row,d*i+mu]+=1
 M=np.zeros((d,nf),complex)
 for mu,row in enumerate(contour):
  for (j,c),count in row.items():M[mu,j]+=count*np.exp(1j*np.dot(K,c))/(24*nv)
 dc=(np.exp(1j*K)-1).reshape(d,1);Delta=D.conj().T@D;J=np.eye(nv)[:,root:root+1]
 Pint=np.eye(nv)-J@J.T;Rc=1/(1+float(np.vdot(dc,dc).real)/kappa)
 H=curl.conj().T@curl;coarse=M.conj().T@dc*Rc@dc.conj().T@M
 Oh=H+D@Pint@D.conj().T+coarse
 G=J.T@Delta@Delta@J;Qpoint=np.eye(nv)-Delta@J@np.linalg.inv(G)@J.T@Delta
 Op=H+D@Qpoint@D.conj().T+coarse
 aliases=list(product(range(-1,2),repeat=d));F=np.array([[np.exp(1j*np.dot((K+2*np.pi*np.asarray(r))/ell,p))/np.sqrt(nv) for r in aliases] for p in sites])
 U=np.kron(F,np.eye(d));ilow=aliases.index((0,)*d);low=list(range(d*ilow,d*ilow+d));high=[j for j in range(nf) if j not in low]
 return D,Delta,M,dc,H,Oh,Op,U,low,high,G
K0=np.zeros(d);D,Delta,M,dc,H,Oh,Op,U,low,high,G=matrices(K0)
E=U[:,low];evals=np.linalg.eigvalsh(Oh)
check('actual_constant_root_map',np.linalg.norm(M@E-np.eye(d)/ell)<1e-12)
check('zero_Bloch_kernel_exactly_four',np.count_nonzero(np.abs(evals)<1e-9)==4 and evals[4]>1e-5)
check('all_alias_frame_unitary',np.linalg.norm(U.conj().T@U-np.eye(nf))<1e-10)
details['K0_first_eigenvalues']=evals[:8].tolist()
directions=[np.array([1.,0,0,0]),np.array([1.,2,-1,3])/np.sqrt(15)]
samples=[]
for idir,omega in enumerate(directions):
 errors=[]
 for t in [.04,.02,.01]:
  K=t*omega;D,Delta,M,dc,H,Oh,Op,U,low,high,G=matrices(K)
  ev=np.eye(nv)[root:root+1];cov_error=float(np.linalg.norm(M@D-dc@ev));curl_error=float(np.linalg.norm(H@D))
  check(f'actual_covariance_{idir}_{t}',cov_error<1e-10)
  check(f'actual_curl_gauge_row_{idir}_{t}',curl_error<1e-10)
  check(f'point_lift_Gram_72_{idir}_{t}',np.linalg.norm(G-72*np.eye(1))<1e-10)
  transformed=U.conj().T@Oh@U;A=transformed[np.ix_(low,low)];B=transformed[np.ix_(low,high)];C=transformed[np.ix_(high,high)]
  Schur=A-B@np.linalg.solve(C,B.conj().T)
  err=float(np.linalg.norm(Schur/(t*t)-np.eye(d)/(ell*ell),2));rawerr=float(np.linalg.norm(A/(t*t)-np.eye(d)/(ell*ell),2))
  check(f'A7_principal_control_{idir}_{t}',err<=2*t)
  eig=np.linalg.eigvalsh(Oh);check(f'all_mode_sample_simple_pole_{idir}_{t}',eig[0]/(t*t)>.02)
  J=np.eye(nv)[:,root:root+1];a=D@J;ray=float(((a.conj().T@Op@a)/(a.conj().T@a))[0,0].real)
  lambda_c=float(np.vdot(dc,dc).real);expected=lambda_c**2/(8*(1+lambda_c/kappa))
  check(f'point_lift_quartic_quotient_{idir}_{t}',abs(ray-expected)<1e-11)
  errors.append(err);samples.append({'direction':idir,'t':t,'covariance_error':cov_error,'principal_error':err,'unminimized_principal_error':rawerr,'smallest_eigenvalue_over_t2':float(eig[0]/t**2),'point_lift_quotient_over_t4':ray/t**4,'high_block_min':float(np.linalg.eigvalsh(C)[0])})
  if t==.01:check(f'omitted_high_minimization_control_{idir}',rawerr>.05)
 check(f'principal_convergence_control_{idir}',errors[-1]<.7*errors[-2] or max(errors[-2:])<1e-10)
# Non-real sector and its real charged-pair determinant multiplicity.
K=np.array([.31,.52,-.27,.41]);D,Delta,M,dc,H,Oh,Op,U,low,high,G=matrices(K)
realDelta=np.block([[Delta.real,-Delta.imag],[Delta.imag,Delta.real]])
sign,ld=np.linalg.slogdet(Delta);signr,ldr=np.linalg.slogdet(realDelta)
check('charged_pair_real_determinant_multiplicity',sign.real>.99 and signr>0 and abs(ldr-2*ld)<1e-10)
check('omitted_conjugate_root_control',abs(ldr-ld)>1.)
details['samples']=samples;details['charged_pair_logdets']={'one_complex_root':float(ld),'real_pair':float(ldr)}
result={'started_utc':started,'finished_utc':datetime.now(timezone.utc).isoformat(),'python':platform.python_version(),'numpy':np.__version__,'scope':'actual one-step free S4-prime contours, all aliases; numerical controls only; no off-shell vertices or limit interchange','checks':checks,'passed':sum(checks.values()),'total':len(checks),'details':details}
print(json.dumps(result,indent=2,sort_keys=True));sys.exit(0 if all(checks.values()) else 1)
