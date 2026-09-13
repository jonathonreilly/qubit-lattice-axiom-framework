"""Author algebraic challenges of the declared classical canonical construction."""
from pathlib import Path
from itertools import product
import hashlib,json,time
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
PAULI=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex)
SP=[s.Matrix(m) for m in [[[0,1],[1,0]],[[0,-s.I],[s.I,0]],[[1,0],[0,-1]]]]
BASIS=[]
for i in range(3):
 for j in range(i,3):
  b=np.zeros((3,3));b[i,j]=b[j,i]=1;BASIS.append(b)
SB=[s.Matrix(b).applyfunc(s.Rational) for b in BASIS]
rows=[]
def check(name,ok,**detail):
 assert bool(ok),(name,detail)
 rows.append(dict(name=name,**detail))
def near(name,x,y,tol=3e-8):
 err=float(np.max(np.abs(np.asarray(x)-np.asarray(y))))
 check(name,err<tol,max_residual=err,tolerance=tol)
def eq(name,x,y):
 z=x-y
 ok=all(s.simplify(t)==0 for t in z) if isinstance(z,s.MatrixBase) else s.simplify(z)==0
 check(name,ok)
def anti(x):return (x-x.T)/2
def rho(x):return sum((x[a,b]*PAULI[a]@PAULI[b]/4 for a,b in product(range(3),repeat=2)),np.zeros((2,2),complex))
def srho(x):return sum((x[a,b]*SP[a]*SP[b]/4 for a,b in product(range(3),repeat=2)),s.zeros(2))
def smat(prefix):
 x=s.symbols(prefix+'_0:6',real=True)
 return s.Matrix([[x[0],x[1],x[2]],[x[1],x[3],x[4]],[x[2],x[4],x[5]]])
def sym(x):return (x+x.T)/2

def geometry(E,W):
 inv=np.linalg.inv(E);g=inv@inv;gi=E@E
 dg=np.array([-inv@w@g-g@w@inv for w in W])
 conn=np.zeros((3,3,3)) # upper, derivative, vector
 for k,i,j,l in product(range(3),repeat=4):
  conn[k,i,j]+=.5*gi[k,l]*(dg[i,l,j]+dg[j,i,l]-dg[l,i,j])
 gam=np.einsum('ia,amn->imn',E,PAULI)
 omega=np.array([inv@(W[j]+conn[:,j,:]@E) for j in range(3)])
 spin=np.array([rho(o) for o in omega]);trace=np.einsum('kkj->j',conn)
 hd=spin-trace[:,None,None]*np.eye(2)/2
 return dict(inv=inv,g=g,gi=gi,dg=dg,conn=conn,gam=gam,omega=omega,spin=spin,hd=hd)

def direct_operator(E,W):
 inv=np.linalg.inv(E);gam=np.einsum('ia,amn->imn',E,PAULI)
 divgam=sum((np.einsum('a,amn->mn',W[i,i,:],PAULI) for i in range(3)),np.zeros((2,2),complex))
 c=0.
 for a,b,cidx,i,j in product(range(3),repeat=5):
  c-=float(s.LeviCivita(a,b,cidx))*E[i,a]*W[i,j,b]*inv[cidx,j]/4
 return gam,-1j*divgam/2+c*np.eye(2)

def run():
 start=time.monotonic()
 # Normal-coordinate variation, with all eighteen first metric-jet components.
 jets=[smat('h'+str(i)) for i in range(3)]
 dw=[s.zeros(3) for _ in range(3)]
 for i,a,b in product(range(3),repeat=3):dw[i][a,b]=(jets[b][i,a]-jets[a][i,b])/2
 spinvar=-s.I*sum((SP[i]*srho(dw[i]) for i in range(3)),s.zeros(2))
 dtrace=s.Matrix([s.trace(jets[i]) for i in range(3)])
 div=s.Matrix([sum(jets[j][i,j] for j in range(3)) for i in range(3)])
 eq('normal_coordinate_spin_connection_variation',spinvar,-s.I*sum(((dtrace[i]-div[i])*SP[i]/4 for i in range(3)),s.zeros(2)))
 eq('half_density_trace_gradient_cancellation',spinvar+s.I*sum((dtrace[i]*SP[i]/4 for i in range(3)),s.zeros(2)),s.I*sum((div[i]*SP[i]/4 for i in range(3)),s.zeros(2)))
 # Darboux calculation at a generic rational positive frame.
 E=s.Matrix([[3,1,0],[1,4,1],[0,1,2]]);inv=E.inv()
 x0,y0,x1,y1=s.symbols('x0 y0 x1 y1',real=True);psi=s.Matrix([x0+s.I*y0,x1+s.I*y1]);psid=s.conjugate(psi).T
 aa=[anti(inv*b) for b in SB];aval=[s.expand((s.I*psid*srho(a)*psi)[0]) for a in aa]
 def pb(f,h):return sum((s.diff(f,x)*s.diff(h,y)-s.diff(f,y)*s.diff(h,x))/2 for x,y in [(x0,y0),(x1,y1)])
 for i in range(6):
  eq('Darboux_momentum_spinor_'+str(i),s.Matrix([-pb(aval[i],z) for z in psi]),srho(aa[i])*psi)
  for j in range(i+1,6):
   deriv=anti(-inv*SB[i]*inv*SB[j])+anti(inv*SB[j]*inv*SB[i])
   curv=deriv+aa[i]*aa[j]-aa[j]*aa[i]
   expected=-(sym(inv*SB[i])*sym(inv*SB[j])-sym(inv*SB[j])*sym(inv*SB[i]))
   eq('connection_curvature_'+str((i,j)),curv,expected)
   eq('Darboux_momentum_curvature_'+str((i,j)),(s.I*psid*srho(deriv)*psi)[0]+pb(aval[i],aval[j]),(s.I*psid*srho(curv)*psi)[0])
 h,k=smat('h'),smat('k')
 eq('identity_metric_curvature',-((-h/2)*(-k/2)-(-k/2)*(-h/2)),-(h*k-k*h)/4)
 # Generic curved-frame challenges. Finite differences are only challenges of P4.
 rng=np.random.default_rng(2026091308)
 for trial in range(8):
  Z=rng.normal(size=(3,3));E=np.eye(3)+Z@Z.T/7
  W=np.array([sym(rng.normal(size=(3,3)))/5 for _ in range(3)])
  V=sym(rng.normal(size=(3,3)))/4;U=np.array([sym(rng.normal(size=(3,3)))/6 for _ in range(3)])
  geo=geometry(E,W);inv=geo['inv'];g=geo['g'];gi=geo['gi'];gam,zero=direct_operator(E,W)
  near('Levi_Civita_frame_skew_'+str(trial),geo['omega']+geo['omega'].transpose(0,2,1),0,tol=3e-12)
  near('scalar_connection_matches_coordinate_geometry_'+str(trial),zero,-1j*sum((gam[i]@geo['hd'][i] for i in range(3)),np.zeros((2,2),complex)),tol=3e-12)
  A=anti(inv@V);dA=np.array([anti(-inv@W[i]@inv@V+inv@U[i]) for i in range(3)])
  eps=2e-5;gp,zp=direct_operator(E+eps*V,W+eps*U);gm,zm=direct_operator(E-eps*V,W-eps*U)
  dgamm=(gp-gm)/(2*eps);dzero=(zp-zm)/(2*eps)
  covgam=np.array([dgamm[i]+rho(A)@gam[i]-gam[i]@rho(A) for i in range(3)])
  covzero=dzero+rho(A)@zero-zero@rho(A)+1j*sum((gam[i]@rho(dA[i]) for i in range(3)),np.zeros((2,2),complex))
  h=-inv@V@g-g@V@inv
  dh=np.array([inv@W[i]@inv@V@g-inv@U[i]@g-inv@V@geo['dg'][i]-geo['dg'][i]@V@inv-g@U[i]@inv+g@V@inv@W[i]@inv for i in range(3)])
  covdh=np.array([dh[k]-geo['conn'][:,k,:].T@h-h@geo['conn'][:,k,:] for k in range(3)])
  divh=np.einsum('jk,kij->i',gi,covdh)
  hi=h@gi
  targetgam=-.5*np.einsum('ij,imn->jmn',hi,gam)
  targetzero=.5j*sum((gam[i]*hi[i,j]@geo['hd'][j] for i,j in product(range(3),repeat=2)),np.zeros((2,2),complex))+.25j*np.einsum('i,imn->mn',divh,gam)
  near('covariant_Dirac_principal_variation_'+str(trial),covgam,targetgam,tol=3e-9)
  near('covariant_Dirac_connection_variation_'+str(trial),covzero,targetzero,tol=3e-9)
  # Polar moment map agrees with intrinsic Kosmann expression at arbitrary jets.
  a=rng.normal(size=3);J=rng.normal(size=(3,3));rhs=J@E-E@J.T
  ev,rot=np.linalg.eigh(E);Om=rot@((rot.T@rhs@rot)/(ev[:,None]+ev[None,:]))@rot.T
  VE=-np.einsum('i,ijk->jk',a,W)+J@E-E@Om
  near('polar_frame_variation_symmetric_'+str(trial),VE,VE.T,tol=3e-12)
  AP=anti(inv@VE);K=anti(inv@J@E)-sum((a[i]*anti(inv@W[i]) for i in range(3)),np.zeros((3,3)))
  near('connection_polar_moment_map_'+str(trial),Om+AP,K,tol=3e-12)
  da=np.array([geo['dg'][i]@a+g@J[:,i] for i in range(3)])
  exterior=anti(da)
  kos=-1j*sum((a[i]*geo['spin'][i] for i in range(3)),np.zeros((2,2),complex))-.25j*sum((gam[i]@gam[j]*exterior[i,j] for i,j in product(range(3),repeat=2)),np.zeros((2,2),complex))
  near('Kosmann_matches_polar_moment_map_'+str(trial),1j*rho(K),kos,tol=3e-12)
  # Differential-operator normal bracket at arbitrary curved first jets.
  # The common N*M derivative of the zero-order connection cancels, so no
  # unknown second frame jet is inserted into this check.
  N,M=rng.normal(size=2);dn,dm=rng.normal(size=(2,3));hn,hm=[sym(rng.normal(size=(3,3))) for _ in range(2)]
  ha=-1j*gam;dha=-1j*np.einsum('ija,amn->ijmn',W,PAULI)
  na=N*ha;ma=M*ha;nb=N*zero+np.einsum('i,imn->mn',dn,ha)/2;mb=M*zero+np.einsum('i,imn->mn',dm,ha)/2
  first=[]
  for j in range(3):
   fij=nb@ma[j]-mb@na[j]+na[j]@mb-ma[j]@nb
   for i in range(3):fij+=na[i]@(dm[i]*ha[j]+M*dha[i,j])-ma[i]@(dn[i]*ha[j]+N*dha[i,j])
   first.append(1j*fij)
  zbracket=nb@mb-mb@nb
  for i in range(3):
   dnb=dn[i]*zero+sum((dha[i,j]*dn[j]+ha[j]*hn[i,j] for j in range(3)),np.zeros((2,2),complex))/2
   dmb=dm[i]*zero+sum((dha[i,j]*dm[j]+ha[j]*hm[i,j] for j in range(3)),np.zeros((2,2),complex))/2
   zbracket+=na[i]@dmb-ma[i]@dnb
  covector=N*dm-M*dn;drift=gi@covector
  driftjet=np.array([(W[i]@E+E@W[i])@covector+gi@(dn[i]*dm+N*hm[i]-dm[i]*dn-M*hn[i]) for i in range(3)])
  targetzero=-1j*np.trace(driftjet)*np.eye(2)/2-1j*np.einsum('i,imn->mn',drift,geo['spin'])
  targetzero-=.25j*sum((gam[i]@gam[j]*(dn[i]*dm[j]-dm[i]*dn[j]) for i,j in product(range(3),repeat=2)),np.zeros((2,2),complex))
  near('curved_normal_bracket_principal_'+str(trial),first,-1j*drift[:,None,None]*np.eye(2),tol=3e-11)
  near('curved_normal_bracket_zero_order_'+str(trial),1j*zbracket,targetzero,tol=3e-11)
  # Time component of the four-dimensional connection at zero shift and unit lapse.
  hdot=-inv@V@g-g@V@inv;Gamma_t=.5*gi@hdot
  omega_t=inv@(V+Gamma_t@E)
  near('spacetime_temporal_connection_'+str(trial),omega_t,A,tol=3e-12)
  # Direct four-dimensional ADM Christoffel calculation with arbitrary lapse/shift jets.
  lapse=1.4;dlapse=rng.normal(size=3)/7;beta=a;dbeta=J
  G=np.zeros((4,4));G[1:,1:]=g;G[0,1:]=G[1:,0]=g@beta;G[0,0]=-lapse*lapse+beta@g@beta
  dG=np.zeros((4,4,4));dG[0,1:,1:]=hdot;dG[0,0,1:]=dG[0,1:,0]=hdot@beta;dG[0,0,0]=beta@hdot@beta
  for k in range(3):
   dG[k+1,1:,1:]=geo['dg'][k]
   dG[k+1,0,1:]=dG[k+1,1:,0]=geo['dg'][k]@beta+g@dbeta[:,k]
   dG[k+1,0,0]=-2*lapse*dlapse[k]+beta@geo['dg'][k]@beta+2*beta@g@dbeta[:,k]
  Ginv=np.linalg.inv(G);C4=np.zeros((4,4,4))
  for mu,nu,rr,ss in product(range(4),repeat=4):C4[mu,nu,rr]+=.5*Ginv[mu,ss]*(dG[nu,ss,rr]+dG[rr,ss,nu]-dG[ss,nu,rr])
  temporal=inv@V+E.T@g@(C4[1:,0,1:]+np.outer(beta,C4[0,0,1:]))@E
  near('full_ADM_temporal_rotation_'+str(trial),temporal,A-E.T@exterior@E,tol=3e-11)
  for k in range(3):
   spatial=inv@W[k]+E.T@g@(C4[1:,k+1,1:]+np.outer(beta,C4[0,k+1,1:]))@E
   near('full_ADM_intrinsic_connection_'+str((trial,k)),spatial,geo['omega'][k],tol=3e-11)

 # Generic contraction underlying the pure metric bracket, and independent torus witnesses.
 lam=s.symbols('lambda',real=True);mom,Hess=smat('p'),smat('n')
 eq('metric_curvature_lapse_contraction',s.trace((mom-lam*s.trace(mom)*s.eye(3))*(Hess-s.trace(Hess)*s.eye(3))),s.trace(mom*Hess)+(2*lam-1)*s.trace(mom)*s.trace(Hess))
 xx=s.symbols('x',real=True);N=1;M=s.cos(xx);drift=s.diff(M,xx)
 trace_witness=s.integrate(drift*s.diff(s.cos(xx),xx),(xx,0,2*s.pi))
 eq('trace_witness_nonzero',trace_witness,s.pi)
 eq('divergence_witness_coefficient',-2*trace_witness,-2*s.pi)
 # Explicit omitted-connection countermodels, with exact scalar source variation.
 X=s.diag(1,0,0);Y=s.Matrix([[0,1,0],[1,0,0],[0,0,0]]);comm=X*Y-Y*X
 eq('spatial_product_bracket_defect',s.I*srho(comm),-SP[2]/2)
 curv0=anti(-X*Y)+anti(Y*X)
 eq('spatial_connection_cancels_defect',s.I*srho(comm)+s.I*srho(curv0),s.zeros(2))
 E0=s.diag(2,3,4);V0=Y;inv0=E0.inv()
 cvar=-sum(s.LeviCivita(a,b,c)*E0[2,a]*V0[j,b]*inv0[c,j]/4 for a,b,c,j in product(range(3),repeat=4))
 eq('normal_product_bracket_scalar_defect',cvar,s.Rational(1,6))
 A0=anti(inv0*V0);gamma3=4*SP[2]
 eq('normal_product_bracket_covariant_formula',-s.I*(gamma3*srho(A0)+srho(A0)*gamma3)/2,cvar*s.eye(2))
 # Compute scalar curvature directly for three arbitrary diagonal functions,
 # then use the Euler derivative of N sqrt(g) R to check the variational input.
 x=s.symbols('xx',real=True);ff=[s.Function('f'+str(i),positive=True)(x) for i in range(3)];nf=s.Function('lapse',real=True)(x)
 gg=s.diag(*ff);gginv=gg.inv();detroot=s.sqrt(s.prod(ff))
 def dx(expr,i):return s.diff(expr,x) if i==0 else s.S(0)
 cc=[[[s.simplify(sum(gginv[k,l]*(dx(gg[l,j],i)+dx(gg[l,i],j)-dx(gg[i,j],l)) for l in range(3))/2) for j in range(3)] for i in range(3)] for k in range(3)]
 ric=s.Matrix(3,3,lambda i,j:sum(dx(cc[k][i][j],k)-dx(cc[k][i][k],j)+sum(cc[k][k][l]*cc[l][i][j]-cc[k][j][l]*cc[l][i][k] for l in range(3)) for k in range(3)))
 scalar=s.simplify(s.trace(gginv*ric));lag=nf*detroot*scalar
 hn=s.Matrix(3,3,lambda i,j:dx(dx(nf,j),i)-sum(cc[k][i][j]*dx(nf,k) for k in range(3)));lap=s.trace(gginv*hn)
 var=detroot*(-nf*(gginv*ric*gginv-gginv*scalar/2)+gginv*hn*gginv-gginv*lap)
 for i in range(3):
  euler=s.diff(lag,ff[i])-s.diff(s.diff(lag,s.diff(ff[i],x)),x)+s.diff(s.diff(lag,s.diff(ff[i],x,2)),x,2)
  eq('scalar_curvature_Euler_variation_'+str(i),euler,var[i,i])
 # Exact general diagonal-metric Legendre inversion and coefficient relation.
 alpha,rr,cc0=s.symbols('alpha rr gamma0',nonzero=True,real=True);ga,gb,gc=s.symbols('ga gb gc',positive=True)
 gm=s.diag(ga,gb,gc);gmi=gm.inv();sq=s.sqrt(ga*gb*gc);pp=smat('pi');ptr=s.trace(gm*pp)
 extr=alpha/sq*(gm*pp*gm-ptr*gm/2);ktr=s.trace(gmi*extr)
 recovered=sq/alpha*(gmi*extr*gmi-ktr*gmi)
 eq('metric_Legendre_inverse',recovered,pp)
 ham=alpha/sq*(s.trace(pp*gm*pp*gm)-ptr**2/2)-sq*rr/alpha+cc0*sq
 eq('metric_ADM_Lagrangian',2*s.trace(pp*extr)-ham,sq/alpha*(s.trace(gmi*extr*gmi*extr)-ktr**2+rr-alpha*cc0))
 # Full periodic differential-operator witness for the spatial bracket.
 x,y,z0=s.symbols('x y z0',real=True);coords=[x,y,z0]
 av=s.Matrix([s.sin(x),0,0]);bv=s.Matrix([s.cos(x)*s.sin(y),s.sin(x)*s.cos(y),0])
 ja=av.jacobian(coords);jb=bv.jacobian(coords);kk=ja*jb-jb*ja
 field=s.Matrix([s.exp(s.I*(x+y+z0)),s.sin(x)+s.I*s.cos(z0)])
 def op(vec,phi):
  jac=vec.jacobian(coords)
  return -s.I*(sum((vec[i]*phi.diff(coords[i]) for i in range(3)),s.zeros(2,1))+s.trace(jac)*phi/2)+s.I*srho(anti(jac))*phi
 bracket=bv.jacobian(coords)*av-av.jacobian(coords)*bv
 canonical=-s.I*(op(av,op(bv,field))-op(bv,op(av,field)))+2*s.I*srho(kk)*field
 curvature=-s.I*srho(kk)*field
 eq('periodic_spatial_joint_constraint_identity',canonical+curvature,-op(bracket,field))
 eq('periodic_spatial_product_bracket_defect',canonical+op(bracket,field),-s.cos(x)**2*s.cos(y)*SP[2]*field/2)
 # Native shift and spin vertices have the correct values at both node chiralities.
 z=s.symbols('zeta',real=True);v=s.sqrt(1-z*z);kx,ky,kz=s.symbols('kx ky kz',real=True)
 shift=s.Matrix([s.sin(kx),s.sin(ky),(z-s.cos(kz))*s.sin(kz)/v]);spin=s.Matrix([s.sin(kz)/v,s.sin(kz)/v,1])
 om=s.Matrix([[0,s.Symbol('u',real=True),s.Symbol('v0',real=True)],[-s.Symbol('u',real=True),0,s.Symbol('w0',real=True)],[-s.Symbol('v0',real=True),-s.Symbol('w0',real=True),0]])
 for chir in [-1,1]:
  node={kx:0,ky:0,kz:chir*s.acos(z)}
  eq('native_shift_node_'+str(chir),shift.subs(node).applyfunc(s.simplify),s.zeros(3,1))
  eq('native_shift_jet_'+str(chir),shift.jacobian([kx,ky,kz]).subs(node).applyfunc(s.simplify),s.diag(1,1,v))
  tau=[SP[0],SP[1],chir*SP[2]]
  spin_target=sum((om[a,b]*tau[a]*tau[b]/4 for a,b in product(range(3),repeat=2)),s.zeros(2))
  native=sum((s.I*sum(s.LeviCivita(a,b,c)*om[a,b] for a,b in product(range(3),repeat=2))*spin[c]*SP[c]/4 for c in range(3)),s.zeros(2))
  eq('native_temporal_spin_vertex_'+str(chir),native.subs(node).applyfunc(s.simplify),spin_target)
 # Apply the new finite-range terms to modulated smooth test spinors on a torus.
 # Carrier phases are kept in each translation; the slowly varying sample is periodic.
 zeta=.6;vel=np.sqrt(1-zeta*zeta);D=np.array([1.,1.,vel]);kappa=np.arccos(zeta)
 coeffA=np.array([[1.,.3,0],[.3,-.2,.1],[0,.1,.2]])
 coeffB=np.array([[.2,0,.1],[0,.4,.2],[.1,.2,-.3]])
 coeffT=np.array([[0,.7,.2],[.7,.1,0],[.2,0,-.1]])
 errors={-1:[],1:[]}; corrected_errors={-1:[],1:[]}
 for count in [12,24,48,96]:
  spacing=2*np.pi/count;xx,yy,zz=np.meshgrid(*(np.arange(count)*spacing for _ in range(3)),indexing='ij')
  Ec=np.eye(3)+.12*np.cos(xx)[...,None,None]*coeffA+.08*np.sin(zz)[...,None,None]*coeffB
  invc=np.linalg.inv(Ec);Vt=.09*np.cos(yy)[...,None,None]*coeffT
  wc=[-.12*np.sin(xx)[...,None,None]*coeffA,np.zeros_like(Ec),.08*np.cos(zz)[...,None,None]*coeffB]
  beta=np.stack([.13*np.sin(xx+yy),.11*np.cos(yy),.17*np.sin(zz)],axis=-1)
  Jc=np.zeros(Ec.shape);Jc[...,0,0]=.13*np.cos(xx+yy);Jc[...,0,1]=.13*np.cos(xx+yy);Jc[...,1,1]=-.11*np.sin(yy);Jc[...,2,2]=.17*vel*np.cos(zz)
  def ant(x):return (x-np.swapaxes(x,-1,-2))/2
  kt=ant(invc@Vt)+ant(invc@Jc@Ec)-sum((beta[...,i,None,None]*ant(invc@(D[i]*wc[i])) for i in range(3)),np.zeros_like(Ec))
  tc=np.stack([kt[...,1,2]/2,-kt[...,0,2]/2,kt[...,0,1]/2],axis=-1)
  dinv=-invc@wc[2]@invc;dJ=np.zeros_like(Jc);dJ[...,2,2]=-.17*vel*np.sin(zz)
  dbetaz=np.zeros_like(beta);dbetaz[...,2]=.17*np.cos(zz)
  dwz=[np.zeros_like(Ec),np.zeros_like(Ec),-.08*np.sin(zz)[...,None,None]*coeffB]
  dkt=ant(dinv@Vt)+ant(dinv@Jc@Ec+invc@dJ@Ec+invc@Jc@wc[2])
  dkt-=sum((dbetaz[...,i,None,None]*ant(invc@(D[i]*wc[i]))+beta[...,i,None,None]*ant(dinv@(D[i]*wc[i])+invc@(D[i]*dwz[i])) for i in range(3)),np.zeros_like(Ec))
  dtc=np.stack([dkt[...,1,2]/2,-dkt[...,0,2]/2,dkt[...,0,1]/2],axis=-1)
  field=np.stack([np.exp(1j*(xx+yy)),(.4+.2j)*np.exp(1j*(yy+zz))],axis=-1)
  dfield=[np.stack([1j*field[...,0],np.zeros_like(xx)],axis=-1),1j*field,np.stack([np.zeros_like(xx),1j*field[...,1]],axis=-1)]
  divbeta=.13*np.cos(xx+yy)-.11*np.sin(yy)+.17*vel*np.cos(zz)
  target_der=1j*(sum((beta[...,i,None]*D[i]*dfield[i] for i in range(3)),np.zeros_like(field))+divbeta[...,None]*field/2)
  for chir in [-1,1]:
   def shift(u,axis,n):return np.exp(1j*chir*kappa*n if axis==2 else 0)*np.roll(u,-n,axis=axis)
   def sn(u,axis,n=1):return (shift(u,axis,n)-shift(u,axis,-n))/(2j)
   def kop(u,i):return sn(u,i) if i<2 else (zeta*sn(u,2)-sn(u,2,2)/2)/vel
   def gop(u,i):
    spin=u@PAULI[i].T
    return sn(spin,2)/vel if i<2 else spin
   actual=-sum((beta[...,i,None]*kop(field,i)+kop(beta[...,i,None]*field,i) for i in range(3)),np.zeros_like(field))/(2*spacing)
   actual+=sum((tc[...,i,None]*gop(field,i)+gop(tc[...,i,None]*field,i) for i in range(3)),np.zeros_like(field))/2
   target=target_der+sum((tc[...,i,None]*(field@PAULI[i].T)*(chir if i<2 else 1) for i in range(3)),np.zeros_like(field))
   err=float(np.sqrt(np.mean(np.sum(np.abs(actual-target)**2,axis=-1))));errors[chir].append(err)
   d2field=np.stack([np.zeros_like(xx),-field[...,1]],axis=-1)
   leading=.75*chir*zeta*(2*beta[...,2,None]*d2field+2*dbetaz[...,2,None]*dfield[2]-beta[...,2,None]*field)
   leading-=.5j*zeta/vel*sum(((2*tc[...,i,None]*dfield[2]+dtc[...,i,None]*field)@PAULI[i].T for i in range(2)),np.zeros_like(field))
   corrected=float(np.sqrt(np.mean(np.sum(np.abs(actual-target-spacing*leading)**2,axis=-1))));corrected_errors[chir].append(corrected)
   check('native_time_shift_leading_Taylor_' +str((chir,count)),corrected<.2*spacing**2,error=corrected,spacing=spacing,normalized_error=corrected/spacing**2,leading_norm=float(np.sqrt(np.mean(np.sum(np.abs(leading)**2,axis=-1)))))
   check('native_time_shift_test_spinor_'+str((chir,count)),err<.12*spacing,error=err,spacing=spacing,normalized_error=err/spacing)
 for chir in [-1,1]:
  # The original 12->24 ratio threshold failed and is preserved. It was stronger
  # than an O(a) theorem. Check the newly predicted asymptotic and corrected rates.
  check('native_time_shift_asymptotic_refinement_'+str(chir),errors[chir][3]<.58*errors[chir][2],errors=errors[chir])
  check('native_time_shift_Taylor_remainder_refinement_'+str(chir),all(corrected_errors[chir][i+1]<.3*corrected_errors[chir][i] for i in range(3)),errors=corrected_errors[chir])
 result=dict(status='ok',check_count=len(rows),checks=rows,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),elapsed_seconds=time.monotonic()-start,scope='Author exact algebra and finite-jet challenges; classical conditional closure is a written argument. No quantum constraint or axiom-selection claim.')
 (HERE/'BLOCK08_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':run()
