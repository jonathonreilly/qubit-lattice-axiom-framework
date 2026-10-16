"""Conditional linear weak-source laboratory bridge: synthetic controls only."""
import hashlib,json,math,sys
from pathlib import Path
import numpy as np
import sympy as s
from scipy.integrate import quad
HERE=Path(__file__).resolve().parent
checks=[];details={}
def ck(name,ok,**values):checks.append(dict(name=name,passed=bool(ok),**values))
def exact(name,expr):
 e=s.simplify(expr);ck(name,e==0,residual=str(e))
r,m,L=s.symbols('r m L',positive=True)
K=s.exp(-m*r)/r
exact('Yukawa radial Helmholtz away from source',s.diff(K,r,2)+2*s.diff(K,r)/r-m*m*K)
exact('radial torque derivative',s.diff(K,r)+s.exp(-m*r)*(1+m*r)/r**2)
exact('decreasing positive radial bound',s.diff((1+m*r)*s.exp(-m*r)/r**2,r)+s.exp(-m*r)*(m*m/r+2*m/r**2+2/r**3))
z=s.symbols('z',positive=True)
exact('form factor monotonic numerator',s.diff(z*s.cosh(z)-s.sinh(z),z)-z*s.sinh(z))
rr=s.symbols('rr',positive=True);rho,M,R,G=s.symbols('rho M R G',positive=True)
exact('central uniform core potential',4*s.pi*G*s.integrate(rr*3*M/(4*s.pi*R**3),(rr,0,R))-3*G*M/(2*R))
N,Nc,Y,Yc,rhat,rtrue=s.symbols('N Nc Y Yc rhat rtrue')
ah=(rhat*Nc-N)/(Y-rhat*Yc);aa=(rtrue*Nc-N)/(Y-rtrue*Yc)
exact('complex Mobius difference',(ah-aa)-(rhat-rtrue)*(Nc*Y-N*Yc)/((Y-rhat*Yc)*(Y-rtrue*Yc)))
a=s.symbols('a',nonnegative=True);rrec=(N+a*Y)/(Nc+a*Yc)
exact('calibration ratio inversion',(rrec*Nc-N)-a*(Y-rrec*Yc))
exact('zero-mass strength cancellation',((N+a*N)/(Nc+a*Nc))-N/Nc)

def shc(z):return 1. if z==0 else math.sinh(z)/z
profiles=[('uniform',lambda x:1.),('central',lambda x:1-x*x),('outer',lambda x:x**4),('reserved_mixed',lambda x:.3+x+2*x**3)]
radial=[]
for label,f in profiles:
 norm=quad(lambda y:4*math.pi*y*y*f(y),0,1,epsabs=1e-12)[0]
 for mm in [0,.3,1,3]:
  Q=quad(lambda y:4*math.pi*y*y*f(y)*shc(mm*y)/norm,0,1,epsabs=1e-12)[0]
  ck('positive support bound '+str((label,mm)),1-1e-12<=Q<=shc(mm)+1e-12,Q_over_M=Q,upper=shc(mm))
  for ext in [1.2,2.5]:
   def shell(y):
    angular=quad(lambda u:math.exp(-mm*math.sqrt(ext*ext+y*y-2*ext*y*u))/math.sqrt(ext*ext+y*y-2*ext*y*u),-1,1,epsabs=2e-12,epsrel=2e-12)[0]
    return 2*math.pi*y*y*f(y)*angular/norm
   direct=quad(shell,0,1,epsabs=2e-12,epsrel=2e-12)[0]
   reduced=math.exp(-mm*ext)*Q/ext;err=abs(direct-reduced)
   ck('angular/reduced response '+str((label,mm,ext)),err<3e-10,error=err)
   radial.append(dict(profile=label,mR=mm,r_over_R=ext,Q_over_M=Q,error=err))
  eps=.17
  lower=(1-eps)*Q;upper=Q
  ck('bounded stress trace '+str((label,mm)),lower>=1-eps-1e-12 and upper<=shc(mm)+1e-12)
details['radial_controls']=radial
for mm in [.4,2]:
 core=quad(lambda y:3*y*y*shc(mm*y)/.01**3,0,.01,epsabs=1e-12)[0]
 shell=quad(lambda y:3*y*y*shc(mm*y)/(1-.999**3),.999,1,epsabs=1e-12)[0]
 ck('approach central endpoint '+str(mm),abs(core-1)<5e-5,Q=core)
 ck('approach outer endpoint '+str(mm),abs(shell-shc(mm))<.002,Q=shell,upper=shc(mm))
cores=[dict(radius=x,Q=quad(lambda y:3*y*y*shc(y)/x**3,0,x)[0],central_potential=3/(2*x))for x in [.2,.05,.01]]
ck('exterior bound does not bound interior',cores[-1]['central_potential']>cores[0]['central_potential']*10 and cores[-1]['Q']<cores[0]['Q'],examples=cores)

def rot(x,theta):
 c=np.cos(theta);ss=np.sin(theta)
 return np.stack([c*x[0]-ss*x[1],ss*x[0]+c*x[1],np.zeros_like(c)+x[2]],axis=-1)
def torque(x,y,mm,theta):
 X=rot(np.array(x),theta);dy=X-np.array(y);rad=np.linalg.norm(dy,axis=-1);J=np.stack([-X[...,1],X[...,0],np.zeros_like(rad)],axis=-1)
 return -np.sum(dy*J,axis=-1)*(1+mm*rad)*np.exp(-mm*rad)/rad**3

def energy(x,y,mm,theta):
 rad=np.linalg.norm(rot(np.array(x),theta)-np.array(y),axis=-1)
 return -np.exp(-mm*rad)/rad
pairrows=[]
for x,y in [([.7,.2,0],[1.3,-.4,.8]),([-.3,.8,0],[.6,.1,.5])]:
 d=abs(x[2]-y[2]);lever=math.hypot(x[0],x[1])
 for mm in [0,.4,2]:
  bound=lever*(1+mm*d)*math.exp(-mm*d)/d**2
  for theta in [.13,.8,2.1]:
   h=2e-5;fd=-(energy(x,y,mm,theta+h)-energy(x,y,mm,theta-h))/(2*h);ans=torque(x,y,mm,theta)
   ck('pair energy derivative '+str((x,mm,theta)),abs(fd-ans)<2e-8,error=float(abs(fd-ans)))
  theta=2*math.pi*np.arange(4096)/4096;tau=torque(x,y,mm,theta)
  harmonic=np.mean(tau*np.exp(-1j*theta))
  ck('signed kernel/harmonic bound '+str((x,mm)),np.max(np.abs(tau))<=bound and abs(harmonic)<=bound,max_kernel=float(np.max(abs(tau))),harmonic=float(abs(harmonic)),bound=bound)
  pairrows.append(dict(x=x,y=y,m=mm,bound=bound,harmonic=[harmonic.real,harmonic.imag]))
# Opposite equal detector masses eliminate odd harmonics despite nonzero pair forces.
theta=2*math.pi*np.arange(4096)/4096
for mm in [0,.4,2]:
 t1=torque([.7,.2,0],[1.3,-.4,.8],mm,theta);t2=torque([-.7,-.2,0],[1.3,-.4,.8],mm,theta)
 v=abs(np.mean((t1+t2)*np.exp(-1j*theta)))
 ck('positive masses harmonic cancellation '+str(mm),v<1e-13 and np.max(abs(t1+t2))>1e-3,first_harmonic=float(v),max_torque=float(np.max(abs(t1+t2))))
# Discrete positive mass measures check the signed bilinear norm inequality.
XA=np.array([[.7,.2,0],[-.3,.8,0]]);YB=np.array([[1.3,-.4,.8],[.6,.1,.5],[1.1,.9,.9]])
ma=np.array([.8,1.1]);mb=np.array([.6,.9,1.2]);da=np.array([.04,-.08]);db=np.array([-.03,.05,-.06])
for mm in [0,.4,2]:
 J=np.array([[np.mean(torque(x,y,mm,theta)*np.exp(-1j*theta))for y in YB]for x in XA]);
 delta=(ma+da)@J@(mb+db)-ma@J@mb
 d=.5;lever=max(np.linalg.norm(XA[:,:2],axis=1));bound=lever*(1+mm*d)*math.exp(-mm*d)/d**2*(ma.sum()*abs(db).sum()+mb.sum()*abs(da).sum()+abs(da).sum()*abs(db).sum())
 ck('density total-variation bound '+str(mm),abs(delta)<=bound,actual=float(abs(delta)),bound=float(bound))
details['pair_controls']=pairrows
# Three Fourier channels with one calibration channel; all chosen before execution.
geometries=[([.5,.1,0],[2.3,-.4,1.3]),([.7,.2,0],[1.3,-.4,.8]),([-.3,.8,0],[.6,.1,.5])]
Ns=np.array([np.mean(torque(x,y,0,theta)*np.exp(-1j*theta))for x,y in geometries])
ratios=[]
for mm in [0,.4,2]:
 Ys=np.array([np.mean(torque(x,y,mm,theta)*np.exp(-1j*theta))for x,y in geometries])
 for strength in [0,.2,1.5]:
  records=2.4*1.7*(Ns+strength*Ys);rs=records[1:]/records[0];As=Ys[1:]-rs*Ys[0];bs=rs*Ns[0]-Ns[1:]
  ck('ratio model consistency '+str((mm,strength)),np.max(abs(bs-strength*As))<1e-14,error=float(np.max(abs(bs-strength*As))))
  ck('common gain scale degeneracy '+str((mm,strength)),np.max(abs((2.4/4.1)*(1.7*4.1)*(Ns+strength*Ys)-records))<1e-14)
  if mm==0:
   ck('massless ratio degeneracy '+str(strength),np.max(abs(As))<1e-14 and np.max(abs(bs))<1e-14)
   continue
  aa=bs/As
  ck('strength reconstructed '+str((mm,strength)),np.max(abs(aa-strength))<1e-11,error=float(np.max(abs(aa-strength))))
  for i in range(2):
   e=1e-7;noise_errors=[];enclosures=[]
   for phase in np.arange(16)*2*math.pi/16:
    rh=rs[i]+e*np.exp(1j*phase);Ah=Ys[i+1]-rh*Ys[0];den=abs(Ah)-abs(Ys[0])*e
    assert den>0
    ah=(rh*Ns[0]-Ns[i+1])/Ah
    bound=e*abs(Ns[0]*Ys[i+1]-Ns[i+1]*Ys[0])/(abs(Ah)*den)
    noise_errors.append(abs(ah-strength));enclosures.append(bound)
   ck('complex noisy ratio bound '+str((mm,strength,i)),all(err<=bd+1e-12 for err,bd in zip(noise_errors,enclosures)),max_error=float(max(noise_errors)),max_bound=float(max(enclosures)))
  if strength>0:
   wrong=bs/Ys[1:]
   ck('calibration omission detected '+str((mm,strength)),np.max(abs(wrong-strength))>1e-3,max_bias=float(np.max(abs(wrong-strength))))
  ratios.append(dict(m=mm,a=strength,A_abs=np.abs(As).tolist(),reconstructed=[[float(v.real),float(v.imag)]for v in aa]))
ck('pairwise determinants alone insufficient',np.linalg.det(np.array([[0,1],[0,2]]))==0 and not np.allclose(np.array([1,2]),np.zeros(2)))
details['ratio_controls']=ratios
source_names=['LAB_YUKAWA_BRIDGE_v1.md','LAB_YUKAWA_PLAN_v1.json',Path(__file__).name]
out={'source_sha256':{n:hashlib.sha256((HERE/n).read_bytes()).hexdigest()for n in source_names},'passed':sum(c['passed']for c in checks),'failed':sum(not c['passed']for c in checks),'checks':checks,'details':details,'data_roles':'Exact algebra and synthetic numerical diagnostics; no empirical fit or independent empirical test','numerical_status':'Floating quadrature/finite-difference checks, not interval-certified integration; analytic inequalities are separately derived in note'}
print(json.dumps(out,indent=2));sys.exit(bool(out['failed']))
