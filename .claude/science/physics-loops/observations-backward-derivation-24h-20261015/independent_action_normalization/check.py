import sympy as s,json,subprocess,time,hashlib,sys
from pathlib import Path
p=Path(__file__).resolve().parent.parent;o=Path(__file__).resolve().parent
rows=[]
def ck(n,c):
 assert c,n
 rows.append(n)
M=s.Matrix([[3,1],[1,2]]);K=s.Matrix([[5,-2],[-2,4]]);v=s.Matrix([1,-1]);z=1+s.I;force=s.Matrix([2,-1]);c=s.Matrix([1,3])
ck('noncommuting SPD base',M*K!=K*M and M.det()>0 and K.det()>0)
for u in [-s.Rational(1,4),0,2]:
 Ku=K+(1+u)*v*v.T
 for lam in [s.Rational(1,7),1,5]:
  A=z*z*M+Ku;Al=z*z*lam*M+lam*Ku
  ck('direct complex transfer '+str((u,lam)),s.simplify((lam*c.T*Al.inv()*force-c.T*A.inv()*force)[0])==0)
  x=s.symbols('x');ck('generalized spectrum '+str((u,lam)),s.expand((lam*Ku-x*lam*M).det()-lam**2*(Ku-x*M).det())==0)
# Exact time-series from noncommuting matrix ODE, constant force and zero state.
t=s.symbols('t');q=s.zeros(2,1)
for j in range(5):q+=(-M.inv()*K)**j*M.inv()*force*t**(2*j+2)/s.factorial(2*j+2)
W=s.integrate((force.T*s.diff(q,t))[0],(t,0,t));lam=s.Rational(7,3)
qs=q/lam;Ws=s.integrate((force.T*s.diff(qs,t))[0],(t,0,t))
ck('series work scaling',s.simplify(Ws-W/lam)==0)
ck('series output equality',s.simplify((lam*c.T*qs-c.T*q)[0])==0)
# Identical nonzero preparation cannot preserve full recorded output at t=0.
qinit=s.Matrix([1,0]);ck('nonzero preparation exclusion',(lam*c.T*qinit-c.T*qinit)[0]!=0)
cmd=[sys.executable,'-B',str(p/'probe_action_normalization_v1.py')];start=time.monotonic();r=subprocess.run(cmd,capture_output=True,text=True,timeout=120)
(o/'reproduction.stdout').write_text(r.stdout);(o/'reproduction.stderr').write_text(r.stderr);(o/'reproduction_receipt.json').write_text(json.dumps({'command':cmd,'timeout_seconds':120,'elapsed_seconds':time.monotonic()-start,'returncode':r.returncode},indent=2))
ck('runner successful',r.returncode==0);ck('published output exact',json.loads(r.stdout)==json.loads((p/'ACTION_NORMALIZATION_CONTROLS_v1.json').read_text()))
h=json.loads((o/'frozen_sources.json').read_text());ck('source hashes unchanged',all(hashlib.sha256((p/n).read_bytes()).hexdigest()==v for n,v in h.items()))
(o/'results.json').write_text(json.dumps({'passed':len(rows),'checks':rows},indent=2));print(len(rows),'checks passed')
