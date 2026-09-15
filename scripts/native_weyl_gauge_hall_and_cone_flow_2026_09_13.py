"""Author challenges for one-loop cone and photon-medium coefficients.

This checks formal perturbative coefficients of a supplied model, not the
existence of its interacting continuum or a native qubit photon phase.
"""
from pathlib import Path
import hashlib,json,time
from itertools import product
import numpy as np
import sympy as s
from numpy.polynomial.legendre import leggauss
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = ("docs/NATIVE_WEYL_GAUGE_HALL_AND_CONE_FLOW_BOUNDED_THEOREM_NOTE_2026-09-13.md",)
HERE=Path(__file__).resolve().parent
SIG=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1]).astype(complex)]
GAM=[np.kron(SIG[0],np.eye(2))]+[-np.kron(SIG[1],p) for p in SIG]
rows=[]
def check(name,ok,**detail):
 assert bool(ok),(name,detail)
 rows.append(dict(name=name,**detail))
def close(name,a,b,tol=1e-10,**detail):
 err=float(np.max(np.abs(np.asarray(a)-np.asarray(b))));check(name,err<tol,error=err,**detail)
def tf(A):return A-np.eye(len(A))*np.trace(A)/len(A)
def sym(A):return (A+A.T)/2
def slash(x):return sum((a*g for a,g in zip(x,GAM)),np.zeros((4,4),complex))
def sphere_grid(nx=32,nz=20,nphi=40):
 j=np.arange(1,nx+1);x=np.cos(np.pi*j/(nx+1));wx=2*np.sin(np.pi*j/(nx+1))**2/(nx+1)
 z,wz=leggauss(nz);phi=2*np.pi*np.arange(nphi)/nphi
 X,Z,P=np.meshgrid(x,z,phi,indexing='ij');rad=np.sqrt(1-X*X)
 n=np.stack([X,rad*np.sqrt(1-Z*Z)*np.cos(P),rad*np.sqrt(1-Z*Z)*np.sin(P),rad*Z],axis=-1).reshape(-1,4)
 w=np.broadcast_to(wx[:,None,None]*wz[None,:,None]/(2*nphi),X.shape).reshape(-1)
 return n,w
def parameter_matrix(E,count=96):
 x,w=leggauss(count);x=(x+1)/2;w=w/2;lam,Q=np.linalg.eigh(E);square=lam*lam
 A=x[:,None]+(1-x[:,None])*square[None,:]
 vals=-np.sum((w*x/np.sqrt(np.prod(A,axis=1)))[:,None]*(2*square-np.sum(square))[None,:]*lam[None,:]/A,axis=0)
 return (Q*vals)@Q.T
def angular_matrix(E,n,w):
 En=n@E.T;q2=np.sum(En*En,axis=1);metric=E.T@E
 avg=np.einsum('n,ni,nj->ij',w/q2**2,n,n)
 inside=E*np.sum(w/q2)-2*E@avg@metric
 return -(2*E@E.T-np.trace(E@E.T)*np.eye(4))@inside
def curl(k):
 x,y,z=k;return np.array([[0,-z,y],[z,0,-x],[-y,x,0]])
def medium_kernel(n,W):
 k=n[1:];out=np.zeros((4,4));out[0,0]=k@W@k;out[0,1:]=-n[0]*(W@k);out[1:,0]=out[0,1:]
 C=curl(k);out[1:,1:]=n[0]**2*W+C.T@W@C
 return out
def metric_medium(V):
 det=np.linalg.det(V);M=V.T@V
 return M/det,det*np.linalg.inv(M)
def native_h(k,zeta=.7):
 return np.sin(k[0])*SIG[0]+np.sin(k[1])*SIG[1]+(2+zeta-np.cos(k[0])-np.cos(k[1])-np.cos(k[2]))*SIG[2]
def native_vertex(k,i,zeta=.7):
 vel=np.sqrt(1-zeta*zeta);D=np.array([1,1,vel]);return ((SIG[i]*np.cos(k[i]) if i<2 else 0)+SIG[2]*np.sin(k[i]))/D[i]

def dvector(k,zeta):return np.stack([np.sin(k[...,0]),np.sin(k[...,1]),2+zeta-np.cos(k[...,0])-np.cos(k[...,1])-np.cos(k[...,2])],axis=-1)
def pauli(v):return np.einsum('...i,ijk->...jk',v,np.array(SIG))
def first(k,axis):
 out=np.zeros(k.shape);out[...,2]=np.sin(k[...,axis])
 if axis<2:out[...,axis]=np.cos(k[...,axis])
 return pauli(out)
def second(k,axis):
 out=np.zeros(k.shape);out[...,2]=np.cos(k[...,axis])
 if axis<2:out[...,axis]=-np.sin(k[...,axis])
 return pauli(out)
def native_shell(radius,ratio,n,w,zeta=.7):
 vel=np.sqrt(1-zeta*zeta);D=np.array([1,1,vel]);momentum=radius*n[:,1:]/D;omega=radius*n[:,0];I=np.eye(2,dtype=complex)
 denominator=omega**2+np.sum((2*D*np.sin(momentum/2))**2,axis=1)
 self_rows=[];electric=np.zeros(3,complex);magnetic=np.zeros((3,3),complex)
 for chir in [-1,1]:
  node=np.array([0,0,chir*np.arccos(zeta)]);internal=node-momentum;mid=node-momentum/2
  h=pauli(ratio*dvector(internal,zeta));G=(1j*omega[:,None,None]*I+h)/(omega**2+np.sum((ratio*dvector(internal,zeta))**2,axis=1))[:,None,None]
  vertices=[1j*I]+[ratio/D[i]*first(mid,i) for i in range(3)]
  correction_time=sum((V@G@(1j*G)@V for V in vertices),np.zeros_like(G))
  z0=np.sum(w*radius**4/denominator*np.trace(correction_time,axis1=-2,axis2=-1)/(2j))
  zs=[]
  for axis in range(3):
   derivative=ratio/D[axis]*first(internal,axis);corr=sum((V@G@derivative@G@V for V in vertices),np.zeros_like(G))
   dV=ratio/D[axis]**2*second(mid,axis);V=vertices[axis+1];corr-=dV@G@V+V@G@dV
   alpha=SIG[axis]*(chir if axis==2 else 1)
   # The two-photon Peierls contact also contributes to the inverse
   # fermion propagator. Its velocity shell is O(radius^2).
   tadpole=-np.sum(w*radius**4/denominator)/(2*D[axis]**2)
   zs.append(np.sum(w*radius**4/denominator*np.trace(alpha@corr,axis1=-2,axis2=-1)/(2*ratio))+tadpole)
  self_rows.append([z0,*zs])
  # Fermion-only photon loop, with no extra photon propagator.
  current=[ratio/D[i]*first(internal,i) for i in range(3)]
  for i in range(3):
   Vi=current[i];electric[i]+=np.sum(w*radius**4*(-np.trace(Vi@G@Vi@G@G@G,axis1=-2,axis2=-1)))
   for j in range(3):
    if i==j:continue
    Wj=current[j];Tj=ratio/D[j]**2*second(internal,j)
    second_G=G@Wj@G@Wj@G-.5*G@Tj@G
    magnetic[i,j]+=np.sum(w*radius**4*np.trace(Vi@G@Vi@second_G,axis1=-2,axis2=-1))
 return np.array(self_rows),electric,magnetic

def gauge_hess(L=3,seed=73):
 rng=np.random.default_rng(seed);theta=rng.normal(size=(L,L,L));size=2*L**3
 mats=[np.zeros((size,size),complex) for _ in range(3)];test=np.zeros((size,size),complex)
 hop=[-SIG[2]/2-1j*SIG[i]/2 for i in range(2)]+[-SIG[2]/2]
 def sl(x):
  idx=np.ravel_multi_index(tuple(x),(L,L,L));return slice(2*idx,2*idx+2)
 for idx in np.ndindex(L,L,L):
  p=np.array(idx);sp=sl(p);mats[0][sp,sp]+=(2+.7)*SIG[2];test[sp,sp]+=(2+.7)*SIG[2]
  for axis in range(3):
   q=(p+np.eye(3,dtype=int)[axis])%L;sq=sl(q);delta=theta[tuple(q)]-theta[idx]
   for j in range(3):
    val=(1j*delta)**j*hop[axis];mats[j][sp,sq]+=val;mats[j][sq,sp]+=val.conj().T
   val=np.exp(.37j*delta)*hop[axis];test[sp,sq]+=val;test[sq,sp]+=val.conj().T
 H,H1,H2=mats;energy,U=np.linalg.eigh(H);occ=energy<0;gap=min(abs(energy));pert=U.conj().T@H1@U;contact=np.trace((U[:,occ].conj().T@H2@U[:,occ])).real
 bubble=2*np.sum(abs(pert[np.ix_(occ,~occ)])**2/(energy[occ,None]-energy[None,~occ])).real
 return dict(seed=seed,gap=gap,contact=contact,bubble=bubble,sum=contact+bubble,spectrum_error=float(np.max(abs(np.linalg.eigvalsh(test)-energy))),matrix_hermiticity=max(float(np.max(abs(A-A.conj().T))) for A in mats))

def native_source(k,a,j,zeta=.7):
 vel=np.sqrt(1-zeta*zeta);D=np.array([1,1,vel])
 if a<2 and j<2:value=np.sin(k[j])
 elif a<2:value=(zeta-np.cos(k[2]))*np.sin(k[2])/vel**2
 elif j<2:value=np.sin(k[2])*np.sin(k[j])/vel
 else:value=(zeta-np.cos(k[2]))/vel
 return D[j]*SIG[a]*value

def chern_slice(M,N):
 k=np.arange(N)*2*np.pi/N-np.pi;X,Y=np.meshgrid(k,k,indexing='ij');d=np.stack([np.sin(X),np.sin(Y),M-np.cos(X)-np.cos(Y)],axis=-1)
 h=np.einsum('...a,aij->...ij',d,np.array(SIG));energies,U=np.linalg.eigh(h);u=U[...,0]
 def link(axis):
  overlap=np.sum(u.conj()*np.roll(u,-1,axis=axis),axis=-1);return overlap/abs(overlap),float(abs(overlap).min())
 Ux,mx=link(0);Uy,my=link(1);flux=np.angle(Ux*np.roll(Uy,-1,axis=0)/(np.roll(Ux,-1,axis=1)*Uy))
 # Direct differentiated projector/Kubo curvature, independent of eigenvector
 # phases and of the four-corner topological formula.
 dx=np.stack([np.cos(X),np.zeros_like(X),np.sin(X)],axis=-1);dy=np.stack([np.zeros_like(X),np.cos(Y),np.sin(Y)],axis=-1)
 berry=-np.sum(d*np.cross(dx,dy),axis=-1)/(2*np.linalg.norm(d,axis=-1)**3)
 direct=float(np.mean(berry)*2*np.pi)
 return dict(M=M,N=N,link_C=float(np.sum(flux)/(2*np.pi)),Kubo_C=direct,min_overlap=min(mx,my),gap=float(np.min(abs(energies))))

def run():
 start=time.monotonic();rng=np.random.default_rng(2026091310);n,w=sphere_grid()
 close('sphere_measure',w.sum(),1)
 close('sphere_second_moments',np.einsum('n,ni,nj->ij',w,n,n),np.eye(4)/4)
 fourth=np.einsum('n,ni,nj,nk,nl->ijkl',w,n,n,n,n);delta=np.eye(4)
 target=(np.einsum('ij,kl->ijkl',delta,delta)+np.einsum('ik,jl->ijkl',delta,delta)+np.einsum('il,jk->ijkl',delta,delta))/24
 close('sphere_fourth_moments',fourth,target)
 for i,j in product(range(4),repeat=2):close('Clifford_'+str((i,j)),GAM[i]@GAM[j]+GAM[j]@GAM[i],2*np.eye(4)*int(i==j))
 x,r=s.symbols('x r',positive=True);A=x+(1-x)*r*r
 # Substitution t=sqrt(A) gives elementary rational antiderivatives,
 # evaluated here without numerical parameter fitting.
 t=s.symbols('t',positive=True)
 I0=s.simplify(s.integrate(2*(t*t-r*r)/((1-r*r)**2*t*t),(t,r,1)))
 Is=s.simplify(s.integrate(2*(t*t-r*r)/((1-r*r)**2*t**4),(t,r,1)))
 check('time_parameter_integral',s.factor(I0-2/(1+r)**2)==0)
 check('space_parameter_integral',s.factor(Is-2*(2+r)/(3*r*(1+r)**2))==0)
 vd=s.factor(r*((1+r*r)*Is+(1-3*r*r)*I0)/8)
 check('scalar_speed_coefficient',s.factor(vd-(1-r)*(4*r*r+3*r+1)/(6*(1+r)**2))==0)
 cd=(r-1/r)/12;rd=s.factor(vd-r*cd)
 check('scalar_ratio_flow',s.factor(rd+(r-1)*(r**3+11*r*r+9*r+3)/(12*(r+1)**2))==0)
 check('scalar_relative_eigenvalue',s.limit(rd/(r-1),r,1)==-s.Rational(1,2))
 for ratio in [.6,.8,1.,1.3,1.8]:
  E=np.diag([1,ratio,ratio,ratio]);m=parameter_matrix(E)
  expected=np.diag([-(1-3*ratio**2)*2/(1+ratio)**2]+[(1+ratio**2)*2*(2+ratio)/(3*(1+ratio)**2)]*3)
  close('scalar_parameter_matrix_'+str(ratio),m,expected,2e-11)
  close('scalar_angular_matrix_'+str(ratio),angular_matrix(E,n,w),m,2e-8)
 for trial in range(8):
  C=sym(rng.normal(size=(4,4)));C/=np.linalg.norm(C);E=np.eye(4)+.3*C
  close('generic_parameter_angular_'+str(trial),parameter_matrix(E),angular_matrix(E,n,w),2e-10)
  errs=[]
  derivative=-5*C/3+2*np.trace(C)*np.eye(4)/3
  for step in [.008,.004,.002]:
   fd=(parameter_matrix(np.eye(4)+step*C)-parameter_matrix(np.eye(4)-step*C))/(2*step)
   errs.append(float(np.linalg.norm(fd-derivative)))
  check('generic_coframe_derivative_'+str(trial),errs[2]<1e-5 and errs[1]<.27*errs[0] and errs[2]<.27*errs[1],errors=errs)
  # Ward longitudinal insertion is pointwise proportional to the full
  # coframe, so it changes the wavefunction but not the relative metric.
  vec=rng.normal(size=4);vec/=np.linalg.norm(vec);q=E@vec;qs=slash(q);q2=q@q
  for j in range(4):
   deriv=slash(E[:,j])/q2-2*qs*(E.T@E@vec)[j]/q2**2
   close('longitudinal_Ward_'+str((trial,j)),qs@deriv@qs,-slash(E[:,j]),2e-11)
  for j in range(4):
   contracted=sum((slash(E[:,mu])@GAM[j]@slash(E[:,mu]) for mu in range(4)),np.zeros((4,4),complex))
   close('coframe_Clifford_map_'+str((trial,j)),contracted,slash((2*E@E.T-np.trace(E@E.T)*np.eye(4))[:,j]),2e-11)
 # The bubble coefficient is derived from its trace and dimensionally
 # regulated radial integration-by-parts identity.
 d,Delta=s.symbols('d Delta');check('bubble_radial_cancellation',s.simplify((2/d-1)*d/2*(-2*Delta/(d-2))-Delta)==0)
 check('bubble_transverse_coefficient',8*s.integrate(x*(1-x),(x,0,1))/8==s.Rational(1,6))
 for trial in range(6):
  q=rng.normal(size=4);p=rng.normal(size=4)
  trace=np.array([[np.trace(GAM[mu]@slash(q)@GAM[nu]@slash(q+p)) for nu in range(4)] for mu in range(4)])
  close('bubble_gamma_trace_'+str(trial),trace,4*(np.outer(q,q+p)+np.outer(q+p,q)-np.eye(4)*np.dot(q,q+p)),2e-11)
  V=np.eye(3)+.2*sym(rng.normal(size=(3,3)));assert np.linalg.eigvalsh(V).min()>.2
  E=np.zeros((4,4));E[0,0]=1;E[1:,1:]=V;ef,bf=metric_medium(V)
  electric=rng.normal(size=3);magnetic=rng.normal(size=3);F=np.zeros((4,4));F[0,1:]=electric;F[1:,0]=-electric;F[1:,1:]=-curl(magnetic)
  transformed=E@F@E.T;direct=np.sum(transformed**2)/(4*np.linalg.det(E));medium=(electric@ef@electric+magnetic@bf@magnetic)/2
  close('induced_metric_medium_'+str(trial),direct,medium,2e-11)
  close('single_metric_no_birefringence_'+str(trial),ef@bf,np.eye(3),2e-11)
 # All five parity-even birefringent directions have no fermion metric
 # logarithm at linear order. Challenge the tensor and Clifford calculations.
 wbas=[np.diag([1,-1,0]),np.diag([1,1,-2])]
 for i,j in [(0,1),(0,2),(1,2)]:
  W=np.zeros((3,3));W[i,j]=W[j,i]=1;wbas.append(W)
 for idx,W in enumerate(wbas):
  Kavg=np.zeros((4,4))
  # Quadratic kernels are integrated exactly using second moments through
  # a small signed-axis rule independent of the general sphere quadrature.
  for a in range(4):
   vec=np.eye(4)[a];K=medium_kernel(vec,W);Kavg+=K/4
   close('birefringent_transverse_'+str((idx,a)),K@vec,np.zeros(4))
   close('birefringent_trace_'+str((idx,a)),np.trace(K),0)
  close('birefringent_kernel_mean_'+str(idx),Kavg,np.zeros((4,4)))
  for trial in range(2):
   vec=rng.normal(size=4);vec/=np.linalg.norm(vec);K=medium_kernel(vec,W)
   for j in range(4):
    inner=GAM[j]-2*slash(vec)*vec[j]
    actual=sum((K[mu,nu]*GAM[mu]@inner@GAM[nu] for mu,nu in product(range(4),repeat=2)),np.zeros((4,4),complex))
    close('birefringent_Clifford_insertion_'+str((idx,trial,j)),actual,2*slash(K[j]),2e-11)
 # A finite shear produces two different physical photon polarizations.
 shear,weight=s.symbols('shear weight',real=True);V=s.diag(1+shear,1-shear,1);ef=V**2/V.det();bf=V.det()*V.inv()**2
 speed_y=(1+weight*bf[2,2])/(1+weight*ef[1,1]);speed_z=(1+weight*bf[1,1])/(1+weight*ef[2,2])
 split=s.factor(s.diff(speed_y-speed_z,weight).subs(weight,0))
 check('induced_birefringence_exact_split',s.factor(split+shear**2*(4-shear**2)/(1-shear**2))==0)
 for sh in [.1,.2,.4]:
  epsilon=np.eye(3)+.03*np.array(ef.subs(shear,sh)).astype(float);b=np.eye(3)+.03*np.array(bf.subs(shear,sh)).astype(float)
  matrix=-np.linalg.solve(epsilon,curl([1,0,0])@b@curl([1,0,0]));eig=np.linalg.eigvals(matrix).real;positive=np.sort(eig[eig>1e-10])
  expected=np.sort([float(speed_y.subs({shear:sh,weight:.03})),float(speed_z.subs({shear:sh,weight:.03}))])
  close('physical_photon_polarizations_'+str(sh),positive,expected,2e-12)
  check('physical_photon_split_'+str(sh),positive[1]-positive[0]>1e-4, squared_speeds=positive.tolist())
 # Solving the derived truncated RG equations is algebra, separate from
 # the coefficient derivation and not an all-orders interacting theorem.
 ell,e0=s.symbols('ell e0',positive=True);z=1+e0*ell/(6*s.pi**2);charge=e0/z;R=z**-3;W=s.Rational(2,5)*(z**-1-z**-6)
 check('running_charge_equation',s.simplify(s.diff(charge,ell)+charge**2/(6*s.pi**2))==0)
 check('running_relative_metric_equation',s.simplify(s.diff(R,ell)+charge*R/(2*s.pi**2))==0)
 check('running_birefringence_equation',s.simplify(s.diff(1/z,ell)+charge/(6*s.pi**2*z))==0)
 check('generated_shear_memory_equation',s.simplify(s.diff(W,ell)+charge*W/(6*s.pi**2)-2*charge*R**2/(6*s.pi**2))==0)
 # Exact finite-spacing Peierls Ward identity for the specified Wilson
 # matter. Gauge momentum is the link-incidence symbol, not continuum q.
 vel=np.sqrt(1-.7**2);D=np.array([1,1,vel])
 for trial in range(10):
  k=rng.uniform(-np.pi,np.pi,size=3);qmom=rng.uniform(-2,2,size=3);a=.37
  contraction=sum(((2*D[i]/a*np.sin(qmom[i]/2))*native_vertex(k,i) for i in range(3)),np.zeros((2,2),complex))
  close('native_Peierls_Ward_'+str(trial),contraction,(native_h(k+qmom/2)-native_h(k-qmom/2))/a,2e-11)
 # A one-parameter link variation checks the required quadratic contact.
 for axis in range(3):
  k=np.array([.31,-.27,.43]);step=.0005;direction=np.eye(3)[axis]/D[axis]
  fd=(native_h(k+step*direction)-2*native_h(k)+native_h(k-step*direction))/step**2
  target=((-np.sin(k[axis])*SIG[axis] if axis<2 else 0)+np.cos(k[axis])*SIG[2])/D[axis]**2
  close('native_quadratic_Peierls_contact_'+str(axis),fd,target,2e-7)
 # Exact exception classification controls, using polarization eigenvalues
 # along arbitrary directions after rotating the common eigenbasis.
 for trial in range(5):
  Q,_=np.linalg.qr(rng.normal(size=(3,3)));u=.13+.07*trial
  for label,V in [('scalar',np.eye(3)*(1.2+.1*trial)),('rank_one',Q@np.diag([1,1,1.3+.1*trial])@Q.T)]:
   ef,bf=metric_medium(V);eps=np.eye(3)+u*ef;b=np.eye(3)+u*bf;Z2=np.trace(eps@b)/3
   close('exact_metric_mixture_escape_'+str((trial,label)),eps@b,Z2*np.eye(3),2e-11)
   vals,U=np.linalg.eigh(eps);root=(U*np.sqrt(vals))@U.T;Vnew=np.sqrt(Z2)*root/np.sqrt(np.linalg.det(eps))
   em,bm=metric_medium(Vnew)
   close('escape_metric_reconstruction_electric_'+str((trial,label)),np.sqrt(Z2)*em,eps,2e-11)
   close('escape_metric_reconstruction_magnetic_'+str((trial,label)),np.sqrt(Z2)*bm,b,2e-11)
   direction=rng.normal(size=3);direction/=np.linalg.norm(direction)
   eigen=np.linalg.eigvals(-np.linalg.solve(eps,curl(direction)@b@curl(direction))).real;pos=np.sort(eigen[eigen>1e-10])
   close('escape_degenerate_polarizations_'+str((trial,label)),pos[0],pos[1],2e-11)
 # A second derivation of the quadratic memory integrates the full Maxwell
 # tensors in fixed coordinates, then removes their common metric curvature.
 zz,tt=s.symbols('zz tt',positive=True);f=(1+2*tt**-3)/3
 mean=s.integrate(f,(tt,1,zz))/zz;mean2=s.integrate(f*f,(tt,1,zz))/zz
 check('integrated_photon_metric_mean',s.simplify(mean-(1-zz**-3)/3)==0)
 check('quadratic_shear_memory_from_Maxwell_variance',s.simplify(2*(mean2-mean**2)-s.Rational(2,5)*(zz**-1-zz**-6))==0)
 # The second-order source follows directly from differentiating the exact
 # constitutive product, not from assigning a name to nonlinear coordinates.
 t0,u0=s.symbols('t0 u0');diag=s.diag(s.Rational(1,5),s.Rational(-1,7),s.Rational(2,9));VV=s.eye(3)+t0*diag
 efs=VV**2/VV.det();bfs=VV.det()*VV.inv()**2
 generator=s.diff((s.eye(3)+u0*efs)*(s.eye(3)+u0*bfs),u0).subs(u0,0)
 quadratic=s.simplify(generator.diff(t0,2).subs(t0,0)/4)
 wanted=2*(diag**2-s.trace(diag)*diag)
 residual=quadratic-wanted;check('constitutive_quadratic_shear_source',s.simplify(residual-s.eye(3)*s.trace(residual)/3)==s.zeros(3))
 # Actual finite Peierls hoppings: occupied-band energy curvature cancels
 # the nonzero bubble against the independently built second derivative.
 for seed in [73,91,127]:
  g=gauge_hess(seed=seed)
  check('finite_Peierls_gauge_curvature_'+str(seed),abs(g['sum'])<2e-10 and abs(g['contact'])>1 and abs(g['bubble'])>1,**g)
  check('finite_Peierls_gauge_spectrum_'+str(seed),g['spectrum_error']<2e-11,**g)
 # Common coframe jets at both actual nodes, including off-diagonal sources.
 for chir in [-1,1]:
  node=np.array([0,0,chir*np.arccos(.7)])
  for a,j in product(range(3),repeat=2):
   close('native_coframe_node_value_'+str((chir,a,j)),native_source(node,a,j),np.zeros((2,2)),2e-12)
   for i in range(3):
    step=2e-5;direction=np.eye(3)[i]/D[i]
    fd=(native_source(node+step*direction,a,j)-native_source(node-step*direction,a,j))/(2*step)
    target=SIG[a]*(chir if a==2 else 1)*int(i==j)
    close('native_coframe_node_jet_'+str((chir,a,j,i)),fd,target,2e-9)
 # These finite shell thresholds were selected after exploratory runs; they
 # are diagnostics for the written O(radius^2) proof, not a certified bound.
 for ratio in [.8,1.2]:
  target=np.array([-(1-3*ratio**2)*2/(1+ratio)**2]+[(1+ratio**2)*2*(2+ratio)/(3*ratio*(1+ratio)**2)]*3);previous=None
  for radius in [.2,.1,.05,.025]:
   sf,el,mag=native_shell(radius,ratio,n,w)
   errs=np.array([np.max(abs(sf-target)),np.max(abs(el-4/(3*ratio))),max(abs(mag[i,j]-4*ratio/3) for i in range(3) for j in range(3) if i!=j)])
   check('native_logarithmic_shell_'+str((ratio,radius)),np.max(errs)<3*radius**2,errors=errs.tolist(),self_coefficients=sf.real.tolist(),electric=el.real.tolist(),magnetic=mag.real.tolist())
   if previous is not None:check('native_shell_refinement_'+str((ratio,radius)),np.max(errs/previous)<.28,ratios=(errs/previous).tolist())
   previous=errs
 # The full native band response contains a Hall term missed by a
 # Maxwell-only cone calculation. Fix the Chern orientation explicitly.
 for mass in [.7,1.4,1.8,2.2,2.8,3.7]:
  corners=np.array([mass-2,mass,mass,mass+2]);orientation=np.array([1,-1,-1,1]);degree=np.sum(orientation[corners>0]);index=-degree
  check('slice_corner_degree_'+str(mass),index==int(mass<2),degree=int(degree),index=int(index))
  for count in [24,48,96]:
   row=chern_slice(mass,count)
   check('native_slice_Chern_links_'+str((mass,count)),abs(row['link_C']-index)<1e-11 and row['min_overlap']>.8,**row)
   if count==96:check('native_slice_Kubo_integral_'+str(mass),abs(row['Kubo_C']-index)<5e-8,**row)
 # Check the spectral Kubo numerator against the differentiated projector
 # curvature at generic momenta, without a topological target value.
 for trial in range(12):
  k=rng.uniform(-np.pi,np.pi,size=3);d=dvector(k,.7);hh=pauli(d);energy,U=np.linalg.eigh(hh);minus=U[:,0];plus=U[:,1]
  vx=first(k,0);vy=first(k,1);spectral=2*np.imag((minus.conj()@vx@plus)*(plus.conj()@vy@minus))/(energy[1]-energy[0])**2
  dx=np.array([np.cos(k[0]),0,np.sin(k[0])]);dy=np.array([0,np.cos(k[1]),np.sin(k[1])]);geometric=-np.dot(d,np.cross(dx,dy))/(2*np.linalg.norm(d)**3)
  close('spectral_Kubo_projector_'+str(trial),spectral,geometric,2e-11)
  close('native_inversion_symmetry_'+str(trial),native_h(-k),SIG[2]@native_h(k)@SIG[2],2e-11)
 # Hall response and integer-stack escape boundary at several fixed nodes.
 for zeta in [.51,.7,.9,.99]:
  kappa=np.arccos(zeta);vel=np.sqrt(1-zeta*zeta);spacing=.43;charge2=.17;H=charge2*kappa*vel/(2*np.pi**2*spacing)
  width=2*kappa*vel/spacing;integrated=charge2*width/(2*np.pi)**2
  close('physical_Hall_slice_measure_'+str(zeta),H,integrated)
  check('gapped_integer_stack_cannot_cancel_'+str(zeta),0<kappa/np.pi<1/3 and min(abs(kappa/np.pi+m) for m in range(-3,4))>0,fraction=float(kappa/np.pi))
 # The Maxwell/Hall wave equation, built from Ampere and Faraday, yields
 # two physical roots after the nondynamical omega^2 factor is removed.
 om,kx,ky,kz,H=s.symbols('om kx ky kz H',real=True);kk=s.Matrix([kx,ky,kz]);k2=(kk.T*kk)[0];Cz=s.Matrix([[0,-1,0],[1,0,0],[0,0,0]])
 matrix=(om**2-k2)*s.eye(3)+kk*kk.T+s.I*om*H*Cz
 det=s.factor(matrix.det());physical=(om**2-k2)**2-H**2*(om**2-kx**2-ky**2)
 check('Maxwell_Hall_physical_polynomial',s.factor(det-om**2*physical)==0)
 hp,qp=s.symbols('hp qp',positive=True);soft=(s.sqrt(hp**2+4*qp**2)-hp)/2;hard=(s.sqrt(hp**2+4*qp**2)+hp)/2
 check('Hall_axis_soft_quadratic',s.limit(soft/qp**2,qp,0)==1/hp)
 check('Hall_axis_hard_gap',s.limit(hard,qp,0)==hp)
 check('Hall_axis_polarization_roots',s.simplify((soft**2-qp**2)**2-hp**2*soft**2)==0 and s.simplify((hard**2-qp**2)**2-hp**2*hard**2)==0)
 for trial in range(6):
  kv=rng.normal(size=3)*.2;hall=.3+.1*trial;square=kv@kv
  roots=[square+hall**2/2-sign*np.sqrt(hall**4/4+hall**2*kv[2]**2) for sign in [1,-1]]
  for idx,root in enumerate(roots):
   freq=np.sqrt(root);mat=(root-square)*np.eye(3)+np.outer(kv,kv)+1j*freq*hall*curl([0,0,1]);sv=np.linalg.svd(mat,compute_uv=False)
   check('physical_Hall_wave_mode_'+str((trial,idx)),root>0 and sv[-1]<2e-12 and sv[-2]>1e-5,squared_frequency=float(root),singular_values=sv.tolist())
 # A time-reversed copy is a real escape from the two-node restriction.
 # Its projector curvature cancels pointwise after momentum inversion.
 for trial in range(6):
  k=rng.uniform(-np.pi,np.pi,size=3);d=dvector(k,.7);v1=first(k,0);v2=first(k,1)
  def curvature(h,a,b):
   en,u=np.linalg.eigh(h);lo,hi=u[:,0],u[:,1];return 2*np.imag((lo.conj()@a@hi)*(hi.conj()@b@lo))/(en[1]-en[0])**2
  original=curvature(pauli(d),v1,v2)
  reversed_copy=curvature(native_h(-k).conj(),-first(-k,0).conj(),-first(-k,1).conj())
  close('time_reversed_copy_Hall_cancellation_'+str(trial),original+reversed_copy,0,2e-11)
 result=dict(status='ok',check_count=len(rows),checks=rows,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),elapsed_seconds=time.monotonic()-start,scope='Native free-band Hall response, leading Maxwell/Hall dispersion, and conditional Hall-subtracted one-loop coefficients. No full gauge phase, higher-loop or axiom-selection theorem.')
 assert len({r['name'] for r in rows})==len(rows)
 print('per_element: Clifford, constitutive and occupied-projector identities are executed with independent matrix and integration paths.')
 print('per_site: finite Peierls link vertices, node jets and pure-gauge contact curvature are executed on the selected band model.')
 print('per_mode: physical Hall and birefringent polarization roots and native logarithmic shells are executed; no full interacting spectrum is claimed.')
 print('per_block: occupied and empty band blocks and both native Weyl-node contributions are executed with their declared trace factors.')
 print('lattice_wide: gapped Brillouin-slice Chern numbers and a finite torus gauge spectrum are executed; thermodynamic gauge-phase existence is not established.')
 print(json.dumps(result,indent=2))
 print('TOTAL: PASS='+str(result['check_count'])+' FAIL=0')
if __name__=='__main__':run()
