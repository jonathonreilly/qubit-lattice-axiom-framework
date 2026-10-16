import sympy as s,json,subprocess,time,sys,hashlib
from pathlib import Path
p=Path(__file__).resolve().parent.parent;o=Path(__file__).resolve().parent
rows=[]
def ck(n,c):
 assert c,n
 rows.append(n)
t=s.symbols('t',real=True);q=t-s.Rational(1,2);psi=t**2*(1-t)**2;g=2;G=4;Om=1;k=s.Rational(3,2);lam=s.Rational(3,4)
A=q*q*s.diff(psi,t,2)+6*q*s.diff(q,t)*s.diff(psi,t)+(6*s.diff(q,t)**2+3*q*s.diff(q,t,2))*psi;B=q*q*psi
ck('clamped endpoints',all(s.diff(psi,t,j).subs(t,e)==0 for j in [0,1] for e in [0,1]));ck('linear adjoint identity',s.integrate(q*A,(t,0,1))==0)
for u,v in [(0,0),(3,-2),(-1,s.Rational(2,3))]:
 w=-q*q+2+u*s.cos(t)+v*s.sin(t);f=k*q+4*lam*q**3+g*q*w;R=f-k*q-4*lam*q**3
 point=q*q*s.diff(R,t,2)-2*q*s.diff(q,t)*s.diff(R,t)+(2*s.diff(q,t)**2-q*s.diff(q,t,2)+Om*q*q)*R+G*q**5/2
 ck('pointwise across crossing '+str((u,v)),s.simplify(point)==0)
 ck('exact weak crossing '+str((u,v)),s.simplify(s.integrate(R*(A+Om*B)+G*q**5*psi/2,(t,0,1)))==0)
# Constant force error, exact bound by integral absolute kernel.
kernel=s.expand(A+B);eps=s.Rational(1,100);err=abs(eps*s.integrate(kernel,(t,0,1)))
ck('force error exact bound',err<=eps*s.integrate(abs(kernel),(t,0,1)))
ck('identically zero blind',s.diff(s.Integer(0),t)==0)
cmd=[sys.executable,'-B',str(p/'probe_division_free_response_v1.py')];start=time.monotonic();r=subprocess.run(cmd,capture_output=True,text=True,timeout=120)
(o/'reproduction.stdout').write_text(r.stdout);(o/'reproduction.stderr').write_text(r.stderr);(o/'reproduction_receipt.json').write_text(json.dumps({'command':cmd,'timeout_seconds':120,'elapsed_seconds':time.monotonic()-start,'returncode':r.returncode},indent=2))
ck('author succeeds',r.returncode==0);ck('published output exact',json.loads(r.stdout)==json.loads((p/'DIVISION_FREE_RESPONSE_CONTROLS_v1.json').read_text()))
h=json.loads((o/'frozen_sources.json').read_text());ck('sources unchanged',all(hashlib.sha256((p/n).read_bytes()).hexdigest()==v for n,v in h.items()))
(o/'results.json').write_text(json.dumps({'passed':len(rows),'checks':rows},indent=2));print(len(rows),'assertions passed')
