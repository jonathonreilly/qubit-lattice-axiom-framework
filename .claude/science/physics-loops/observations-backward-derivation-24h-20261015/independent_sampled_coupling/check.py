import numpy as np,math,json,subprocess,time,sys,hashlib,itertools
from scipy.integrate import solve_ivp,quad
from pathlib import Path
p=Path(__file__).resolve().parent.parent;o=Path(__file__).resolve().parent
rows=[]
def ck(n,c):
 assert c,n
 rows.append(n)
def inverse(s,p,F):
 fm2,fm1,f0,f2,f3,f4=F
 return (f4-(1+s)*f3+(s+p)*f2)/p-((1+s)*f0-(s+p)*fm1+p*fm2)
dt=.29;tau=1.3;b=lambda q:math.exp(q);a=lambda q:2*math.exp(q);u=lambda q:math.sin(q)
for damping in [0.,4.,5.]:
 def basis(t):
  if damping==0:return np.array([1.,math.cos(2*t),math.sin(2*t)])
  if damping==4:return np.array([1.,math.exp(-2*t),t*math.exp(-2*t)])
  return np.array([1.,math.exp(-t),math.exp(-4*t)])
 if damping==0:s0,p0=2*math.cos(2*dt),1.
 elif damping==4:s0,p0=2*math.exp(-2*dt),math.exp(-4*dt)
 else:s0,p0=math.exp(-dt)+math.exp(-4*dt),math.exp(-5*dt)
 cal=np.array([basis(j*dt)@np.array([.4,.7,-1.2]) for j in range(8)]);d=np.diff(cal);H=d[0]*d[2]-d[1]**2
 ss=(d[0]*d[3]-d[1]*d[2])/H;pp=(d[1]*d[3]-d[2]**2)/H
 ck('analytic recurrence '+str(damping),max(abs(ss-s0),abs(pp-p0))<1e-10)
 def evolve(Y,t0,t1,q,times=None):return solve_ivp(lambda t,z:[z[1],-damping*z[1]-4*z[0]-b(q)/tau],[t0,t1],Y,t_eval=times,rtol=2e-12,atol=2e-14)
 for x,y in [(-.3,.8),(.4,-.2)]:
  before=evolve([1.1,-.8],-2*dt,0,x,[-2*dt,-dt,0]);pulse=evolve(before.y[:,-1],0,dt,y);after=evolve(pulse.y[:,-1],dt,4*dt,x,[2*dt,3*dt,4*dt]);ref=evolve(before.y[:,-1],0,dt,x)
  F=u(x)+a(x)*np.r_[before.y[0],after.y[0]];recovered=inverse(ss,pp,F);direct=a(x)*(pulse.y[0,-1]-ref.y[0,-1]);ck('nonpolynomial six-sample '+str((damping,x,y)),abs(recovered-direct)<1e-9)
  if damping==0:J=(1-math.cos(2*dt))/4
  elif damping==4:J=(1-(1+2*dt)*math.exp(-2*dt))/4
  else:J=((1-math.exp(-dt))-(1-math.exp(-4*dt))/4)/3
  ck('passive pulse sign/law '+str((damping,x,y)),J>0 and abs(recovered+a(x)*(b(y)-b(x))*J/tau)<1e-9)
# Half-period undamped samples have rank one even with nonzero pulse response.
cal=np.array([1+.7*(-1)**j for j in range(5)]);d=np.diff(cal);X=np.array([[d[1],-d[0]],[d[2],-d[1]]]);ck('half-period rank loss with positive J',np.linalg.matrix_rank(X)==1 and (1-math.cos(math.pi))/4>0)
# Test corrected sensitivity bound on all six-sample sign corners.
s0,p0=-1.3,.4;eps=.002
for F in itertools.product([-1.,1.],repeat=6):
 for ds,dp in [(eps,eps),(-eps,eps),(eps,-eps),(-eps,-eps)]:
  pmin=min(p0,p0+dp);S=max(abs(s0),abs(s0+ds));bound=eps*(2/pmin+4+(2+2*S)/pmin**2)
  ck('coefficient corner '+str((F,ds,dp)),abs(inverse(s0+ds,p0+dp,F)-inverse(s0,p0,F))<=bound+1e-13)
cmd=[sys.executable,'-B',str(p/'check_sampled_coupling_inverse_v2.py')];start=time.monotonic();r=subprocess.run(cmd,capture_output=True,text=True,timeout=120)
(o/'reproduction.stdout').write_text(r.stdout);(o/'reproduction.stderr').write_text(r.stderr);(o/'reproduction_receipt.json').write_text(json.dumps({'command':cmd,'timeout_seconds':120,'elapsed_seconds':time.monotonic()-start,'returncode':r.returncode},indent=2))
ck('runner succeeds',r.returncode==0);actual=json.loads(r.stdout);ck('full published output reproduced',actual==json.loads((p/'SAMPLED_COUPLING_CONTROLS_v2.json').read_text()))
h=json.loads((o/'frozen_sources.json').read_text());ck('frozen sources unchanged',all(hashlib.sha256((p/n).read_bytes()).hexdigest()==v for n,v in h.items()))
(o/'results.json').write_text(json.dumps({'passed':len(rows),'checks':rows,'author_total':actual['total']},indent=2));print(len(rows),'assertions passed')
