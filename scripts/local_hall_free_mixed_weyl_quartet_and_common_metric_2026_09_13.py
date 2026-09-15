"""Author challenges for a mixed, time-reversal-invariant Weyl quartet.

The domain is the specified finite-range free CAR symbol. No dynamical
native gauge phase or generic preservation of equal metrics is established.
"""
from pathlib import Path
from itertools import product
import hashlib,json,time
import numpy as np
import sympy as sy
from scipy.optimize import root
AUDIT_TIMEOUT_SEC=60
AUDIT_INPUT_PATHS=("docs/LOCAL_HALL_FREE_MIXED_WEYL_QUARTET_AND_COMMON_METRIC_BOUNDED_THEOREM_NOTE_2026-09-13.md",)
SIG=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1]).astype(complex)]
I2=np.eye(2);I4=np.eye(4);S=[np.kron(I2,p) for p in SIG];T=np.kron(SIG[0],I2);PH=S[1]
XZ=np.kron(SIG[2],SIG[0]);ZZ=np.kron(SIG[2],SIG[2]);XX=np.kron(SIG[0],SIG[0]);ZX=np.kron(SIG[0],SIG[2])
rows=[]
def check(name,ok,**detail):
 assert bool(ok),(name,detail)
 rows.append(dict(name=name,**detail))
def close(name,a,b,tol=1e-10,**detail):
 error=float(np.max(abs(np.asarray(a)-np.asarray(b))));check(name,error<tol,error=error,**detail)
def coeff(k,b,zeta,mu,theta):
 x,y,z=k;return (-np.cos(x)*np.sin(b),np.sin(x)*np.cos(b),2+zeta-np.cos(x)*np.cos(b)-np.cos(y)-np.cos(z),-np.sin(x)*np.sin(b),mu*np.sin(theta),mu*np.cos(theta))
def h(k,b,zeta,mu,theta):
 a,b1,c,d,m1,m3=coeff(k,b,zeta,mu,theta)
 return np.sin(k[1])*S[1]+a*S[0]+b1*XZ+c*S[2]+d*ZZ+m1*XX+m3*ZX

def hops(b,zeta,mu,theta):
 onsite=(2+zeta)*S[2]+mu*np.sin(theta)*XX+mu*np.cos(theta)*ZX
 C=[-np.sin(b)*S[0]-np.cos(b)*S[2],-S[2],-S[2]]
 A=[np.cos(b)*XZ-np.sin(b)*ZZ,S[1],np.zeros((4,4))]
 return onsite,[(c-1j*a)/2 for c,a in zip(C,A)]
def derivative(k,b,i):
 x,y,z=k
 if i==0:return np.sin(x)*np.sin(b)*S[0]+np.cos(x)*np.cos(b)*XZ+np.sin(x)*np.cos(b)*S[2]-np.cos(x)*np.sin(b)*ZZ
 if i==1:return np.cos(y)*S[1]+np.sin(y)*S[2]
 return np.sin(z)*S[2]
def squared_energies(k,b,zeta,mu,theta):
 a,b1,c,d,m1,m3=coeff(k,b,zeta,mu,theta)
 total=np.sin(k[1])**2+a*a+b1*b1+c*c+d*d+mu*mu
 split=2*np.sqrt((a*b1+c*d)**2+(a*m1+c*m3)**2+(b1*m3-d*m1)**2)
 return np.array([total-split,total+split])
def roots_formula(b,zeta,mu,theta):
 R2=1-mu*mu*np.sin(2*theta-b)/np.sin(b)
 if R2<=0:return []
 R=np.sqrt(R2);X=(np.cos(b)-mu*mu*np.sin(2*theta)/(2*np.sin(b)))/R
 if abs(X)>1+1e-12:return []
 x=np.arccos(np.clip(X,-1,1));out=[]
 for y in [0,np.pi]:
  Z=2+zeta-np.cos(y)-R
  if abs(Z)<=1+1e-12:
   z=np.arccos(np.clip(Z,-1,1))
   out.extend([np.array([sx*x,y,sz*z]) for sx,sz in product([-1,1],repeat=2)])
 # Endpoint roots are unique on the torus; the tolerance only handles
 # roundoff in these finite fixtures, not a broadened theorem domain.
 unique=[]
 for k in out:
  if not any(np.linalg.norm((k-v+np.pi)%(2*np.pi)-np.pi)<1e-9 for v in unique):unique.append(k)
 return unique

def qdet(k,b,zeta,mu,theta):
 a,b1,c,d,m1,m3=coeff(k,b,zeta,mu,theta)
 return np.linalg.det((c+1j*a)*I2+(d+1j*b1)*SIG[2]+(m3+1j*m1)*SIG[0])
def projected(k,b,zeta,mu,theta):
 e,u=np.linalg.eigh(h(k,b,zeta,mu,theta));v=u[:,1:3]
 reduced=[v.conj().T@derivative(k,b,i)@v for i in range(3)]
 J=np.array([[np.trace(a@s).real/2 for a in reduced] for s in SIG])
 tilt=np.array([np.trace(a).real/2 for a in reduced])
 return e,J,tilt

def metric_formula(k,b,zeta,mu,theta):
 x,y,z=k;L=2+zeta-np.cos(y)-np.cos(z);t=np.cos(x);c=L-t*np.cos(b)
 qx=2*np.sin(x)*L*np.exp(1j*b);qz=2*(c-1j*t*np.sin(b))*np.sin(z)
 gap2=4*(np.sin(b)**2+mu*mu*np.cos(theta)**2)
 q=np.array([qx,0,qz]);G=(q.conj()[:,None]*q[None,:]).real/gap2;G[1,1]=1
 detJ=-np.cos(y)*np.imag(qx.conjugate()*qz)/gap2
 return G,detJ,gap2

def curvature(k,parameters,i,j):
 b,*_=parameters;e,U=np.linalg.eigh(h(k,*parameters));A=U.conj().T@derivative(k,b,i)@U;B=U.conj().T@derivative(k,b,j)@U
 return float(2*np.imag(np.sum(A[:2,2:]*B[2:,:2].T/(e[:2,None]-e[None,2:])**2)))
def occupied(k,parameters):return np.linalg.eigh(h(k,*parameters))[1][:,:2]
def link(u,v):
 d=np.linalg.det(u.conj().T@v);return d/abs(d)
def cube_charge(node,parameters,radius=.035,n=8):
 flux=0.;minimum=1.
 for axis in range(3):
  j=(axis+1)%3;l=(axis+2)%3
  for side in [-1,1]:
   frames={}
   for a,bb in product(range(n+1),repeat=2):
    k=node.copy();k[axis]+=side*radius;k[j]+=radius*(2*a/n-1);k[l]+=radius*(2*bb/n-1);frames[a,bb]=occupied(k,parameters)
   for a,bb in product(range(n),repeat=2):
    u,v,w,z=[frames[idx] for idx in [(a,bb),(a+1,bb),(a+1,bb+1),(a,bb+1)]]
    loop=link(u,v)*link(v,w)*link(w,z)*link(z,u);flux+=side*np.angle(loop)
    minimum=min(minimum,abs(np.linalg.det(u.conj().T@v)))
 return flux/(2*np.pi),minimum

def slice_chern(kz,parameters,n=18):
 pts=np.arange(n)*2*np.pi/n-np.pi;frame={(a,b):occupied(np.array([x,y,kz]),parameters) for a,x in enumerate(pts) for b,y in enumerate(pts)};flux=0.
 for a,b in product(range(n),repeat=2):
  u,v,w,z=[frame[idx] for idx in [(a,b),((a+1)%n,b),((a+1)%n,(b+1)%n),(a,(b+1)%n)]]
  flux+=np.angle(link(u,v)*link(v,w)*link(w,z)*link(z,u))
 return flux/(2*np.pi)

def commutant(parameters):
 mats=[np.kron(a,b) for a,b in product([I2,*SIG],repeat=2)]
 onsite,hop=hops(*parameters)
 coeffs=[onsite,*[a+a.conj().T for a in hop],*[1j*(a-a.conj().T) for a in hop]]
 columns=[np.concatenate([(A@M-M@A).reshape(-1) for A in coeffs]) for M in mats]
 singular=np.linalg.svd(np.array(columns).T,compute_uv=False)
 return int(np.sum(singular<1e-10)),singular.tolist()

def gauge_fixture(parameters,L=3,seed=331):
 rng=np.random.default_rng(seed);chi=rng.normal(size=(L,L,L));onsite,hop=hops(*parameters);size=4*L**3
 H,H1,H2,Hg=[np.zeros((size,size),complex) for _ in range(4)]
 def sl(p):
  q=np.ravel_multi_index(tuple(p),(L,L,L));return slice(4*q,4*q+4)
 for idx in np.ndindex(L,L,L):
  p=np.array(idx);sp=sl(p);H[sp,sp]+=onsite;Hg[sp,sp]+=onsite
  for axis in range(3):
   q=(p+np.eye(3,dtype=int)[axis])%L;sq=sl(q);dc=chi[tuple(q)]-chi[idx]
   for matrix,power in [(H,0),(H1,1),(H2,2)]:
    val=(1j*dc)**power*hop[axis];matrix[sp,sq]+=val;matrix[sq,sp]+=val.conj().T
   val=np.exp(.37j*dc)*hop[axis];Hg[sp,sq]+=val;Hg[sq,sp]+=val.conj().T
 e,U=np.linalg.eigh(H);occ=e<0;A=U.conj().T@H1@U
 contact=np.trace(U[:,occ].conj().T@H2@U[:,occ]).real
 bubble=2*np.sum(abs(A[np.ix_(occ,~occ)])**2/(e[occ,None]-e[None,~occ])).real
 phase=np.repeat(np.exp(-.37j*chi.ravel()),4)
 return dict(gap=float(min(abs(e))),filled=int(sum(occ)),neutral_background=2*L**3,contact=float(contact),bubble=float(bubble),hessian=float(contact+bubble),covariance_error=float(np.max(abs(Hg-phase[:,None]*H*phase.conj()[None,:]))),spectrum_error=float(np.max(abs(np.linalg.eigvalsh(Hg)-e))))

def perturb_fixture(parameters,delta=.013):
 b,*_=parameters
 def hp(k):
  p=np.kron(SIG[1],SIG[2])+.31*np.kron(SIG[2],SIG[1])+(.4*np.cos(k[0])+.23*np.cos(k[1])+.17*np.cos(k[2]))*I4
  return h(k,*parameters)+delta*p
 result=[]
 for node in roots_formula(*parameters):
  ref=np.linalg.eigh(h(node,*parameters))[1][:,1:3]
  def reduced(k):
   u=np.linalg.eigh(hp(k))[1][:,1:3];P=u@u.conj().T;v=P@ref;w,Q=np.linalg.eigh(v.conj().T@v);v=v@(Q/np.sqrt(w))@Q.conj().T;A=v.conj().T@hp(k)@v
   return np.array([np.trace(A@s).real/2 for s in SIG]),np.trace(A).real/2
  sol=root(lambda k:reduced(k)[0],node,tol=1e-10);d,mu=reduced(sol.x);step=1e-5
  differences=[(np.r_[reduced(sol.x+step*e)[0],reduced(sol.x+step*e)[1]]-np.r_[reduced(sol.x-step*e)[0],reduced(sol.x-step*e)[1]])/(2*step) for e in np.eye(3)]
  J=np.array(differences).T[:3];tilt=np.array(differences).T[3];G=J.T@J
  result.append(dict(node=sol.x.tolist(),residual=float(np.linalg.norm(d)),energy=float(mu),det=float(np.linalg.det(J)),type_I_norm=float(tilt@np.linalg.solve(G,tilt))))
 k=np.array([.23,-.47,.86]);tr=float(np.max(abs(T@hp(k).conj()@T-hp(-k))));mz=float(np.max(abs(hp(k)-hp(k*np.array([1,1,-1])))));ph=float(np.linalg.norm(PH@hp(k).conj()@PH+hp(k)))
 return dict(nodes=result,TR=tr,Mz=mz,PH_defect=ph)

def run():
 start=time.monotonic();rng=np.random.default_rng(2026091311)
 a,b1,c,d,m1,m3=sy.symbols('a b1 c d m1 m3',real=True)
 ss=a*a+b1*b1+c*c+d*d+m1*m1+m3*m3
 split=(a*b1+c*d)**2+(a*m1+c*m3)**2+(b1*m3-d*m1)**2
 q=(c+sy.I*a)**2-(d+sy.I*b1)**2-(m3+sy.I*m1)**2
 check('determinant_sum_of_squares',sy.expand(ss**2-4*split-sy.expand_complex(q*sy.conjugate(q)))==0)
 angle,theta,mu,L,t=sy.symbols('angle theta mu L t',real=True)
 qp=L**2-2*L*t*(sy.cos(angle)+sy.I*sy.sin(angle))+sy.cos(2*angle)+sy.I*sy.sin(2*angle)-mu**2*(sy.cos(2*theta)+sy.I*sy.sin(2*theta))
 rotated=sy.expand_complex((sy.cos(angle)-sy.I*sy.sin(angle))*qp)
 check('rotated_q_imaginary',sy.trigsimp(sy.im(rotated)-sy.sin(angle)*(1-L*L)+mu*mu*sy.sin(2*theta-angle))==0)
 check('rotated_q_real',sy.trigsimp(sy.re(rotated)-sy.cos(angle)*(1+L*L)+2*L*t+mu*mu*sy.cos(2*theta-angle))==0)
 check('metric_alignment_angle_identity',sy.trigsimp(sy.cos(angle)*sy.sin(2*theta-angle)-sy.sin(2*theta)/2-sy.sin(2*(theta-angle))/2)==0)
 close('ordinary_TR_square',T@T.conj(),I4);close('spectral_antisymmetry_square',PH@PH.conj(),-I4)
 cases=[(.4,.7,0.,.4),(.4,.7,.2,np.pi/2),(.4,.7,.2,.4),(.8,.6,.5,.8),(.2,.9,.3,.2),(.4,.7,.2,.47),(.6,.7,.2,.6+np.pi/2),(1.3,.7,np.sqrt(8),1.3+np.pi/2)]
 for num,parameters in enumerate(cases):
  b,zeta,mu,theta=parameters
  onsite,hop=hops(*parameters)
  for trial in range(8):
   k=rng.uniform(-np.pi,np.pi,3);H=h(k,*parameters);ef=squared_energies(k,*parameters);expected=np.sort(np.r_[-np.sqrt(ef),np.sqrt(ef)])
   close(f'spectrum_{num}_{trial}',np.linalg.eigvalsh(H),expected,2e-11)
   a,b1,c,d,m1,m3=coeff(k,*parameters);total=np.sin(k[1])**2+a*a+b1*b1+c*c+d*d+mu*mu
   square=total*I4+2*(a*b1+c*d)*np.kron(SIG[2],I2)+2*(a*m1+c*m3)*np.kron(SIG[0],I2)+2*(b1*m3-d*m1)*np.kron(SIG[1],SIG[1])
   close(f'full_H_squared_{num}_{trial}',H@H,square,2e-10)
   close(f'finite_range_symbol_{num}_{trial}',H,onsite+sum((v*np.exp(1j*k[j])+v.conj().T*np.exp(-1j*k[j]) for j,v in enumerate(hop)),np.zeros((4,4),complex)))
   close(f'TR_{num}_{trial}',T@H.conj()@T,h(-k,*parameters));close(f'Mz_{num}_{trial}',H,h(k*np.array([1,1,-1]),*parameters));close(f'spectral_pairing_{num}_{trial}',PH@H.conj()@PH,-H)
   qmom=rng.normal(size=3)*.3;mid=k+qmom/2
   ward=sum((2*np.sin(qmom[j]/2)*derivative(mid,b,j) for j in range(3)),np.zeros((4,4),complex))
   close(f'Peierls_Ward_{num}_{trial}',ward,h(k+qmom,*parameters)-H)
   for i,j in [(0,1),(0,2),(1,2)]:close(f'occupied_Hall_odd_{num}_{trial}_{i}_{j}',curvature(k,parameters,i,j)+curvature(-k,parameters,i,j),0,2e-10)
  nodes=roots_formula(*parameters);check(f'four_nodes_{num}',len(nodes)==4)
  allmetrics=[]
  for index,k in enumerate(nodes):
   e,J,tilt=projected(k,*parameters);G,detJ,gap2=metric_formula(k,*parameters)
   close(f'node_zeros_{num}_{index}',e[1:3],np.zeros(2));close(f'node_spectators_{num}_{index}',e[[0,3]],[-np.sqrt(gap2),np.sqrt(gap2)])
   close(f'projected_metric_{num}_{index}',J.T@J,G);close(f'projected_chirality_{num}_{index}',np.linalg.det(J),detJ);close(f'zero_tilt_{num}_{index}',tilt,np.zeros(3));check(f'simple_node_{num}_{index}',np.linalg.eigvalsh(G).min()>.001)
   allmetrics.append(G)
  if abs(theta-b)<1e-10:
   R=np.sqrt(1-mu*mu);x=abs(nodes[0][0]);z=abs(nodes[0][2]);common=np.diag([R*R,1,R*R*np.sin(b)**2*np.sin(z)**2/np.sin(x)**2])
   close(f'aligned_common_metric_{num}',allmetrics,np.broadcast_to(common,(4,3,3)))
  if mu and abs(theta-b)>.01 and abs(theta-b-np.pi/2)>.01:
   check(f'nonaligned_distinct_metrics_{num}',np.linalg.norm(allmetrics[0]-allmetrics[1])>.001,difference=float(np.linalg.norm(allmetrics[0]-allmetrics[1])))
  nullity,singular=commutant(parameters);check(f'onsite_commutant_{num}',nullity==(2 if mu==0 else 1),nullity=nullity,smallest_nonzero=singular[-(nullity+1)])
 # These topological checks use only occupied eigenvector overlaps on closed
 # surfaces, independently of the determinant and projected-velocity formula.
 for num,parameters in enumerate([cases[1],cases[2],cases[5],cases[7]]):
  for index,k in enumerate(roots_formula(*parameters)):
   C,overlap=cube_charge(k,parameters);target=-np.sign(np.cos(k[1])*np.sin(k[0])*np.sin(k[2]));close(f'occupied_cube_charge_{num}_{index}',C,target,2e-10,min_overlap=overlap);check(f'cube_overlap_{num}_{index}',overlap>.95)
  for kz in [0.,.31,1.2,2.4]:close(f'zero_total_slice_chern_{num}_{kz}',slice_chern(kz,parameters),0,2e-10)
 # A differentiated full projector checks the normalization of the Kubo
 # curvature, independently of its oddness under time reversal.
 for num,parameters in enumerate([cases[1],cases[2],cases[7]]):
  k=np.array([.21,.43,1.17]);step=1e-5;u=occupied(k,parameters);P=u@u.conj().T;dp=[]
  for axis in np.eye(3):
   up=occupied(k+step*axis,parameters);um=occupied(k-step*axis,parameters);dp.append((up@up.conj().T-um@um.conj().T)/(2*step))
  for i,j in [(0,1),(0,2),(1,2)]:
   projector=(np.trace(P@(dp[i]@dp[j]-dp[j]@dp[i]))/1j).real
   close(f'Kubo_projector_normalization_{num}_{i}_{j}',curvature(k,parameters,i,j),projector,2e-8)
 # Boundary and gapped fixtures challenge the complete analytic zero set;
 # a finite momentum scan alone would not establish absence of other zeros.
 b=.4;zeta=.7;critical=np.sqrt(1-zeta*zeta)
 for mu in [critical+.01,1.,1.3]:check(f'aligned_no_root_{mu}',len(roots_formula(b,zeta,mu,b))==0)
 check('sigma1_x_merger_gaps',len(roots_formula(.4,.7,.5,np.pi/2))==0)
 check('large_R_outside_both_planes',len(roots_formula(1.5,.7,5.,1.5+np.pi/2))==0)
 crossing=roots_formula(1.3,.7,np.sqrt(2.7**2-1),1.3+np.pi/2)
 check('both_plane_boundary_unique_roots',len(crossing)==4)
 for index,k in enumerate(crossing):
  ee,jj,_=projected(k,1.3,.7,np.sqrt(2.7**2-1),1.3+np.pi/2);close(f'two_plane_boundary_zero_{index}',ee[1:3],[0,0]);close(f'two_plane_boundary_rank_{index}',np.linalg.det(jj),0)
 boundary=np.array([np.arccos(zeta*np.cos(b)),0.,0.]);e,J,tilt=projected(boundary,b,zeta,critical,b)
 close('boundary_node',e[1:3],[0,0]);close('boundary_loss_of_simple_rank',np.linalg.det(J),0);check('boundary_nonzero_spectator',abs(e[0])>.1)
 for num,parameters in enumerate([cases[1],cases[2]]):
  gauge=gauge_fixture(parameters,seed=331+num);close(f'finite_gauge_covariance_{num}',gauge['covariance_error'],0);close(f'finite_gauge_spectrum_{num}',gauge['spectrum_error'],0);close(f'finite_gauge_contact_cancellation_{num}',gauge['hessian'],0,1e-9,contact=gauge['contact'],bubble=gauge['bubble']);check(f'neutral_filling_{num}',gauge['filled']==gauge['neutral_background'] and gauge['gap']>.01);check(f'contact_is_substantive_{num}',abs(gauge['contact'])>1)
  pert=perturb_fixture(parameters);check(f'generic_perturbation_symmetries_{num}',pert['TR']<1e-12 and pert['Mz']<1e-12 and pert['PH_defect']>.001,**pert)
  energies=[n['energy'] for n in pert['nodes']];close(f'common_shifted_node_energy_{num}',energies,np.mean(energies),1e-10);check(f'PH_not_required_{num}',abs(np.mean(energies))>.001)
  for i,node in enumerate(pert['nodes']):check(f'perturbed_simple_type_I_{num}_{i}',node['residual']<1e-10 and abs(node['det'])>.1 and 0<node['type_I_norm']<.01,**node)
 # At an ordinary T^2=+1 invariant momentum choose T=K. Only the
 # imaginary Hermitian sigma2 can appear in a linear two-band splitting.
 allowed=[s for s in SIG if np.max(abs(s.conj()+s))<1e-12]
 check('spinless_TRIM_linear_rank_bound',len(allowed)==1)
 for label,statement in [
 ('per_element','Checked Pauli, determinant, symmetry and projected metric identities; these are finite matrix challenges.'),
 ('per_site','Checked nearest-neighbor hopping reconstruction and Peierls vertices, including nonzero onsite flavor mixing.'),
 ('per_mode','Checked four simple nodes, their unequal or aligned metrics, local occupied topological charge and type-I perturbations.'),
 ('per_block','Checked the full occupied two-band projector and scalar onsite commutant; flavor sectors are not separately conserved.'),
 ('lattice_wide','Checked gapped slice Chern cancellation and finite torus gauge contacts; a thermodynamic dynamical gauge phase was not executed.')]:print(label+': '+statement)
 result=dict(status='PASS',author_check_count=len(rows),elapsed_seconds=time.monotonic()-start,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Selected free finite-range four-orbital CAR model; no native interacting photon or generic common-metric theorem',rows=rows)
 print(json.dumps(result,indent=2))
 print('TOTAL: PASS='+str(result['author_check_count'])+' FAIL=0')
if __name__=='__main__':run()
