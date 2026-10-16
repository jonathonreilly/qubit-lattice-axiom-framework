import sympy as s, math,json,time,subprocess,sys,hashlib
from pathlib import Path
p=Path(__file__).resolve().parent.parent;o=Path(__file__).resolve().parent
rows=[]
def ck(n,c):
 assert c,n
 rows.append(n)
# Direct determinant formulation: four points lie on a projective graph iff
# the columns [1,u,y,u*y] are linearly dependent.
us=[s.Rational(-2),0,1,3]
y=[(2+3*s.I+(1-s.I)*u)/(5+u) for u in us]
ck('projective determinant',s.simplify(s.Matrix([[1,u,v,u*v] for u,v in zip(us,y)]).det())==0)
ck('nonprojective response fails',s.Matrix([[1,u,u*u,u**3] for u in us]).det()!=0)
# Energy-bound equality for anisotropic K, independently chosen saturator.
K=s.Matrix([[3,1],[1,2]]);c=s.Matrix([2,-1]);q=K.inv()*c
energy=(q.T*K*q)[0]/2
ck('sharp mismatch certificate',(c.T*q)[0]**2/4==energy*(c.T*K.inv()*c)[0]/2)
ck('zero mismatch',s.zeros(2,1).dot(c)==0)
# Polynomial antiderivative expansion rather than beta-integral implementation.
for n in [3,7,11,15]:
 for r in [0,1,2,3,4]:
  coefficient=sum((-1)**k*s.binomial(n,k)/s.Integer(k+r+1) for k in range(n+1))/s.factorial(n)/s.factorial(r)
  ck('pulse coefficient '+str((n,r)),coefficient==1/s.factorial(n+r+1))
  m=n+2
  tail=sum((-1)**k*s.binomial(m,k)/s.Integer(k+r+1) for k in range(m+1))/s.factorial(m)/s.factorial(r)
  ck('pulse remainder '+str((n,r)),tail==1/s.factorial(n+r+3))
cmd=[sys.executable,'-B',str(p/'probe_instrument_invariants_v1.py')];start=time.monotonic()
r=subprocess.run(cmd,capture_output=True,text=True,timeout=120)
(o/'reproduction.stdout').write_text(r.stdout);(o/'reproduction.stderr').write_text(r.stderr)
(o/'reproduction_receipt.json').write_text(json.dumps({'command':cmd,'timeout_seconds':120,'elapsed_seconds':time.monotonic()-start,'returncode':r.returncode},indent=2))
ck('runner succeeds',r.returncode==0)
a=json.loads(r.stdout);ck('full published JSON reproduced',a==json.loads((p/'INSTRUMENT_INVARIANTS_CONTROLS_v1.json').read_text()))
frozen=json.loads((o/'frozen_sources.json').read_text());ck('frozen sources unchanged',all(hashlib.sha256((p/k).read_bytes()).hexdigest()==v for k,v in frozen.items()))
(o/'results.json').write_text(json.dumps({'passed':len(rows),'checks':rows,'author_summary':a['summary']},indent=2));print(json.dumps({'passed':len(rows),'author_summary':a['summary']}))
