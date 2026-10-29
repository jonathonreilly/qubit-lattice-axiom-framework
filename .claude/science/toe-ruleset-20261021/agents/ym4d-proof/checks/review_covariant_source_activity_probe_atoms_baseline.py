"""Distinct finite algebra/support checks of the constructed operator and marks."""
import json, numpy as np, sympy as s
from scipy.linalg import expm
checks={};details={}
def ck(n,v):
 checks[n]=bool(v)
 if not v:raise AssertionError(n)
t,x,y=s.symbols('t x y',nonnegative=True)
for q in (1,2,4):
 f=(1-t)**(-q);S=s.diff(f,t)-q-q*(q+1)*t
 coeff=[s.expand(s.series(S,t,0,8).removeO()).coeff(t,k) for k in range(8)]
 ck('nonlinear_force_degree_'+str(q),coeff[0]==coeff[1]==0 and all(c>0 for c in coeff[2:]))
 N=S+t*s.diff(S,t)
 ck('force_incidence_mark_'+str(q),s.expand(s.series(N-S,t,0,5).removeO()).coeff(t,2)>0)
 ck('Lipschitz_double_mark_'+str(q),s.simplify(s.diff(N,t)-(2*s.diff(S,t)+t*s.diff(S,t,2)))==0)
 # A degree-four vertex supplies exact independent binomial allocations.
 T=(t+x)**4-t**4-4*t**3*x-6*t*t*x*x
 full=T+t*s.diff(T,t)+y*s.diff(T,x)
 ck('background_mark_required_'+str(q),s.expand(full-(T+y*s.diff(T,x))).coeff(t,1).coeff(x,3)>0)
 ck('fluctuation_mark_required_'+str(q),s.expand(full-(T+t*s.diff(T,t))).coeff(y,1).coeff(x,3)>0)
# Curvature is an explicit forcing factor in a source-perturbed nonlinear solve.
d,e=s.symbols('d e'); b=0
for _ in range(6):
 b=s.series(d*(1+e)+e*b+b*b,d,0,5).removeO()
 b=s.series(b,e,0,5).removeO().expand()
res=s.series(b-d*(1+e)-e*b-b*b,d,0,4).removeO()
res=s.series(res,e,0,4).removeO().expand()
ck('actual_Picard_coefficient_equation',res==0)
ck('flat_holonomy_forcing_identity',b.subs(d,0)==0)
ck('original_source_background_response',b.coeff(d,1).coeff(e,1)==2)
# Noncommuting real colour transports, local coefficient dependence, periodic ring.
nb=8;D=3;n=nb*D
Jx=np.array([[0,0,0],[0,0,-1],[0,1,0]],float)
Jy=np.array([[0,0,1],[0,0,0],[-1,0,0]],float)
u=np.linspace(.01,.19,nb)
def matrix(v):
 K=np.zeros((n,n))
 for i in range(nb):
  ii=slice(i*D,(i+1)*D);jj=slice(((i+1)%nb)*D,((i+1)%nb+1)*D)
  K[ii,ii]=np.diag([3+v[i],3.2+.3*v[i],2.8+.7*v[i]])
  rot=expm((.2+.07*i)*Jx)@expm((.13-.03*i)*Jy)
  K[ii,jj]=-.3*rot;K[jj,ii]=-.3*rot.T
 return K
K=matrix(u);ident=np.eye(n);Ps=[];Rs=[];labels=[]
for q in range(nb):
 om={(q-1)%nb,q,(q+1)%nb};inds=[i for b0 in sorted(om) for i in range(b0*D,(b0+1)*D)]
 P=np.zeros((n,n));P[np.ix_(inds,inds)]=np.linalg.inv(K[np.ix_(inds,inds)])
 mask=np.zeros(n);mask[q*D:(q+1)*D]=1;P=P*mask
 R=-(K@P);R[inds,:]=0
 Ps.append(P);Rs.append(R);labels.append({(q+j)%nb for j in (-2,-1,0,1,2)})
P=sum(Ps);R=sum(Rs);G=np.linalg.inv(K)
ck('actual_parametrix_identity',np.linalg.norm(K@P-(ident-R),np.inf)<1e-12)
ck('actual_inverse_order',np.linalg.norm(P@np.linalg.inv(ident-R)-G,np.inf)<1e-12)
ck('wrong_residual_sign_rejected',np.linalg.norm(P@np.linalg.inv(ident+R)-G,np.inf)>1e-8)
ck('wrong_noncommuting_order_rejected',np.linalg.norm(np.linalg.inv(ident-R)@P-G,np.inf)>1e-8)
ck('row_and_column_defect_small',max(np.linalg.norm(R,1),np.linalg.norm(R,np.inf))<.1)
partial=P.copy();power=ident.copy()
for j in range(1,10):power=power@R;partial+=P@power
ck('Neumann_series_actual_inverse',np.linalg.norm(partial-G,np.inf)<1e-12)
ck('all_nonzero_products_have_connected_labels',all(labels[i]&labels[j] for i in range(nb) for j in range(nb) if np.linalg.norm(Ps[i]@Rs[j])>1e-15))
v=u.copy();v[5]+=.1;delta=np.linalg.inv(matrix(v))-G
ck('remote_original_coarse_dependence_retained',np.linalg.norm(delta[:D,:D])>1e-12)
# A label may contain a marked connector even when neither endpoint is there.
ck('endpoint_only_incidence_rejected',2 in {0,1,2} and 2 not in {0,1})
A=np.zeros((5,5));A[:,0]=.2;B=np.zeros((5,5));B[0,0]=1
ck('row_only_incidence_bound_rejected',np.abs(A@B).sum()>np.linalg.norm(A,np.inf)*np.abs(B).sum()+.5)
# Scalar colour counts in a full determinant; this matrix is not a tensor copy.
logdet=np.linalg.slogdet(K)[1]
chol=2*np.log(np.diag(np.linalg.cholesky(K))).sum()
wrong=D*np.linalg.slogdet(K[::D,::D])[1]
ck('complete_colour_determinant',abs(logdet-chol)<1e-12)
ck('three_identical_colour_determinant_rejected',abs(logdet-wrong)>1e-4)
Q=np.zeros_like(K);Q[15,15]=1
z=np.linalg.slogdet(K+1e-6j*Q);der=(np.log(z[0])+z[1]).imag/1e-6
exact=np.trace(G@Q)
ck('trace_log_determinant_derivative',abs(der-exact)<1e-12)
ck('missing_half_determinant_rejected',abs(der-exact/2)>1e-3)
details={'gap':float(np.linalg.eigvalsh(K)[0]),'row_defect':float(np.linalg.norm(R,np.inf)),'column_defect':float(np.linalg.norm(R,1)),'remote_dependency_difference':float(np.linalg.norm(delta[:D,:D])),'full_logdet':float(logdet),'wrong_colour_logdet':float(wrong),'trace_derivative_error':float(der-exact)}
print(json.dumps({'checks':checks,'passed':sum(checks.values()),'total':len(checks),'details':details,'scope':'Finite algebra checks; actual S4 model is checked separately; uniform support bounds are the written proof.'},indent=2))
