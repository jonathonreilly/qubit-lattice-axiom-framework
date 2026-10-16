AUDIT_TIMEOUT_SEC = 120
import sys,json,time,subprocess,hashlib,itertools,math
from pathlib import Path
import numpy as np
import sympy as s
from scipy.integrate import quad
root=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent
sys.path.insert(0,str(root/'scripts'))
import sampled_coupling_math as h
rows=[]
def ck(n,c):
 assert c,n
 rows.append(n)
def raises(n,f):
 try:f()
 except (ValueError,np.linalg.LinAlgError):ck(n,True)
 else:ck(n,False)
# Independently selected nonpolynomial surfaces; anchor row deliberately has negative a.
grid=np.array([-.6,0.,.4,1.]);a=lambda x:2*x*np.exp(x*x);b=lambda x:np.exp(x*x)
for lam in [2.,-3.]:
 aa=lambda x:lam*a(x)
 D=np.array([[-.17*aa(x)*(b(y)-b(x)) for y in grid] for x in grid]);E,e0,A,B=h.response_surface(D)
 ck('normalized A '+str(lam),np.max(abs(A-np.array([aa(x)/aa(grid[0]) for x in grid])))<1e-12)
 ck('normalized B '+str(lam),np.max(abs(B-(b(grid)-b(grid[0]))/(b(grid[-1])-b(grid[0]))))<1e-12)
 ck('full centered factorization '+str(lam),np.max(abs(E-e0*np.outer(A,B)))<1e-12)
 kap=aa(grid[0])/(lam*(b(grid[-1])-b(grid[0])))
 ck('positive multiplier sign '+str(lam),(e0*kap<0)==(lam>0))
 # Zero of a is handled by A=0, not a division there.
 ck('zero feedback coordinate '+str(lam),A[1]==0)
# Analytic solution bases provide an independent calibration data generator.
for mode in ['critical','overdamped','oscillatory']:
 t=np.arange(7)*.23
 if mode=='critical':F=.7+(.3+.8*t)*np.exp(-2*t);truth=[2*np.exp(-.46),np.exp(-.92)]
 elif mode=='overdamped':F=.7+.3*np.exp(-t)+.8*np.exp(-4*t);truth=[np.exp(-.23)+np.exp(-.92),np.exp(-1.15)]
 else:F=.7+.3*np.cos(2*t)+.8*np.sin(2*t);truth=[2*np.cos(.46),1]
 est,X,y=h.infer_coefficients(F);ck('independent recurrence '+mode,np.max(abs(est-truth))<1e-10)
 eps=1e-9
 for signs in itertools.product([-1,1],repeat=5):
  est2,X2,_=h.infer_coefficients(F[:5]+eps*np.array(signs));bound=h.calibration_error_bound(X2,est2,eps)
  ck('calibration bound '+str((mode,signs)),np.linalg.norm(est2-est,np.inf)<=bound+1e-12)
# Independent symbolic derivative of six-point expression.
ss,pp=s.symbols('ss pp',positive=True);F=s.symbols('f0:6');fm2,fm1,f0,f2,f3,f4=F
D=(f4-(1+ss)*f3+(ss+pp)*f2)/pp-(1+ss)*f0+(ss+pp)*fm1-pp*fm2
for actual,expected in zip(h.coefficient_gradient(ss,pp,F),[s.diff(D,ss),s.diff(D,pp)]):ck('gradient',s.simplify(actual-expected)==0)
for nh,eh in [(1.7,-.4),(-2.,.3)]:
 for dn,de in itertools.product([-.03,.03],[-.02,.02]):ck('ratio '+str((nh,eh,dn,de)),abs(nh/eh-(nh-dn)/(eh-de))<=h.ratio_error_bound(nh,eh,.03,.02)+1e-14)
for x,y in [(-.4,.7),(.7,-.4)]:
 A=lambda t:math.exp(t);B=lambda t:2*math.exp(t);kh=2.03;Ah=lambda t:A(t)+.01;lo,hi=sorted([x,y])
 observed=B(y)+.02-B(x)+.02-kh*quad(Ah,x,y)[0]
 bound=h.shape_error_bound(.02,.02,kh,.01*(hi-lo),.03,quad(lambda t:abs(Ah(t)),lo,hi)[0]);ck('oriented signal unsigned error '+str((x,y)),abs(observed)<=bound+1e-14)
for value in [0.,-1.]:raises('p guard '+str(value),lambda value=value:h.extrapolation_weights(1.,value))
raises('anchor zero',lambda:h.response_surface(np.zeros((3,3))))
raises('ratio margin equality',lambda:h.ratio_error_bound(1.,-.2,.1,.2))
raises('negative ratio uncertainty',lambda:h.ratio_error_bound(1.,2.,-.1,0.))
raises('negative shape integral',lambda:h.shape_error_bound(0,0,1,-1,0,1))
raises('negative coefficient uncertainty',lambda:h.coefficient_error_bound(1,-.1,1,1))
raises('zero coefficient p margin',lambda:h.coefficient_error_bound(1,.1,0,1))
raises('singular calibration',lambda:h.infer_coefficients(np.ones(5)))
raises('uncertified calibration region',lambda:h.calibration_error_bound(np.eye(2),np.ones(2),.25))
# Sharp independent six-point noise signs.
W=h.extrapolation_weights(-.7,.3);noise=1e-6*np.sign(W);ck('six-point sharp read error',abs(W@noise-1e-6*sum(abs(W)))<1e-18)
cmd=[sys.executable,'-B','scripts/sampled_coupling_inverse.py'];start=time.monotonic();r=subprocess.run(cmd,cwd=root,capture_output=True,text=True,timeout=120)
(o/'reproduction.stdout').write_text(r.stdout);(o/'reproduction.stderr').write_text(r.stderr);(o/'reproduction_receipt.json').write_text(json.dumps({'command':cmd,'cwd':str(root),'timeout_seconds':120,'elapsed_seconds':time.monotonic()-start,'returncode':r.returncode},indent=2))
ck('primary succeeds',r.returncode==0);actual=json.loads(r.stdout);cache=(root/'logs/runner-cache/sampled_coupling_inverse.txt').read_text().split('----- stdout -----\n')[1];expected=json.JSONDecoder().raw_decode(cache)[0];ck('full fresh cache exactly reproduced',actual==expected)
frozen=json.loads((o/'frozen_sources.json').read_text());ck('frozen sources unchanged',all(hashlib.sha256((root/n).read_bytes()).hexdigest()==v for n,v in frozen.items()))
(o/'results.json').write_text(json.dumps({'passed':len(rows),'checks':rows,'primary_total':actual['total']},indent=2));print(len(rows),'independent assertions passed')
