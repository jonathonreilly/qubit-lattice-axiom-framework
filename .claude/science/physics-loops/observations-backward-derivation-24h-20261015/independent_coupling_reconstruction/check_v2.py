import numpy as np, math,json,subprocess,time,sys,hashlib,itertools
from scipy.integrate import solve_ivp,quad
from pathlib import Path
p=Path(__file__).resolve().parent.parent;o=Path(__file__).resolve().parent
rows=[]
def ck(n,c):
 assert c,n
 rows.append(n)
# Fit independent elementary scalar solution bases, not augmented expm.
pre=np.array([-.6,-.3,0.]);post=.47;h=.13;tau=1.3
for damping in [0.,4.,5.]:
 def basis(t):
  if damping==0:return np.array([1.,math.cos(2*t),math.sin(2*t)])
  if damping==4:return np.array([1.,math.exp(-2*t),t*math.exp(-2*t)])
  return np.array([1.,math.exp(-t),math.exp(-4*t)])
 def green(t):
  if damping==0:return math.sin(2*t)/2
  if damping==4:return t*math.exp(-2*t)
  return (math.exp(-t)-math.exp(-4*t))/3
 O=np.array([basis(t) for t in pre]);weights=np.linalg.solve(O.T,basis(post))
 ck('baseline identifiable '+str(damping),np.linalg.cond(O)<1e4)
 for initial in [[.7,-1.2],[-3.,2.1]]:
  x,y=.2,.9;a=1+x*x;b=lambda q:q+q**3/3;u=.6
  def evolve(y0,t0,t1,drive,times=None):
   return solve_ivp(lambda t,Y:[Y[1],-damping*Y[1]-4*Y[0]-drive/tau],[t0,t1],y0,t_eval=times,rtol=2e-12,atol=2e-14)
  before=evolve(initial,pre[0],0,b(x),pre);during=evolve(before.y[:,-1],0,h,b(y));after=evolve(during.y[:,-1],h,post,b(x));reference=evolve(before.y[:,-1],0,post,b(x))
  fpre=u+a*before.y[0];actual=u+a*after.y[0,-1];baseline=weights@fpre
  ck('same-run baseline '+str((damping,initial)),abs(baseline-(u+a*reference.y[0,-1]))<1e-10)
  J=quad(lambda s:green(post-s),0,h,epsabs=1e-13)[0]
  ck('finite pulse '+str((damping,initial)),abs(actual-baseline+a*(b(y)-b(x))*J/tau)<1e-10)
# Nonpolynomial reciprocal example with zero a at q=0.
A=lambda x:x*math.exp(x*x);B=lambda x:(math.exp(x*x)-1)/(math.e-1);kap=2/(math.e-1)
for x,y in [(-.7,.8),(.8,-.7),(0,.9)]:
 ck('nonpolynomial reciprocal shape '+str((x,y)),abs(B(y)-B(x)-kap*quad(A,x,y)[0])<1e-13)
# Bound (14) interpreted with positive segment integrals, including reversal.
for x,y in [(.2,.9),(.9,.2)]:
 ea,ek,eb=.02,.03,.01;kh=kap+ek;Ah=lambda s:A(s)+ea
 exact=B(y)-B(x)-kap*quad(A,x,y)[0]
 measured=B(y)+eb-(B(x)-eb)-kh*quad(Ah,x,y)[0]
 lo,hi=sorted([x,y]);bound=2*eb+abs(kh)*ea*(hi-lo)+ek*(quad(lambda s:abs(Ah(s)),lo,hi)[0]+ea*(hi-lo))
 ck('residual bound reversed-safe '+str((x,y)),abs(measured-exact)<=bound+1e-13)
for nh,eh in [(2.,.5),(-2.,-.5)]:
 for dn,de in itertools.product([-.1,.1],[-.05,.05]):
  rh=nh/eh;true=(nh-dn)/(eh-de);bound=(.1+abs(rh)*.05)/(abs(eh)-.05)
  ck('ratio corners '+str((nh,eh,dn,de)),abs(rh-true)<=bound+1e-13)
cmd=[sys.executable,'-B',str(p/'check_coupling_reconstruction_v2.py')];start=time.monotonic();r=subprocess.run(cmd,capture_output=True,text=True,timeout=120)
(o/'reproduction_v2.stdout').write_text(r.stdout);(o/'reproduction_v2.stderr').write_text(r.stderr);(o/'reproduction_v2_receipt.json').write_text(json.dumps({'command':cmd,'timeout_seconds':120,'elapsed_seconds':time.monotonic()-start,'returncode':r.returncode},indent=2))
ck('author succeeds',r.returncode==0);actual=json.loads(r.stdout);expected=json.loads((p/'COUPLING_CONTROLS_v2.json').read_text());ck('published full output reproduced',actual==expected)
hashes=json.loads((o/'frozen_sources_v2.json').read_text());ck('frozen sources unchanged',all(hashlib.sha256((p/n).read_bytes()).hexdigest()==v for n,v in hashes.items()))
(o/'results_v2.json').write_text(json.dumps({'passed':len(rows),'checks':rows,'author_total':actual['total']},indent=2));print(len(rows),'independent assertions passed')
