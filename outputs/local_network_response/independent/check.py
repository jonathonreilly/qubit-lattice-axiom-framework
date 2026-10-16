import sys,json,math,subprocess,time,hashlib
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parents[3]; out=Path(__file__).resolve().parent
sys.path.insert(0,str(root/'scripts'))
import local_network_response_math as h
rows=[]
def check(n,c):
 assert c,n
 rows.append(n)
K=s.Matrix([[4,-1,0],[-1,5,-1],[0,-1,6]]); e=s.eye(3)[:,0]; w=s.Matrix([0,1,-1]); O=s.Matrix([[1,0,0],[0,s.Rational(3,5),-s.Rational(4,5)],[0,s.Rational(4,5),s.Rational(3,5)]]); P=O*K*O.T
# Independent direct powers, including negative stable interventions and d=0.
for A,v in [(K,w),(P,w),(K,e),(s.Matrix([[4,-1,-1],[-1,5,-1],[-1,-1,6]]),w)]:
 d=next(j for j in range(3) if (v.T*A**j*e)[0]!=0); mu=(v.T*A**d*e)[0]
 check('access '+str((d,mu)),h.first_access_moment(A,e,v)==(d,mu))
 for theta in [s.Rational(-1,10),s.Rational(2,3),0]:
  B=A+theta*v*v.T
  for k in range(2*d+2):
   actual=(-1)**k*(e.T*(A**k-B**k)*e)[0]/s.factorial(2*k+1)
   expected=theta*mu**2/s.factorial(4*d+3) if k==2*d+1 else 0
   check('Taylor coefficient '+str((d,theta,k)),s.simplify(actual-expected)==0)
check('factor25',((w.T*K*e)[0]/(w.T*P*e)[0])**2==25)
check('zero direction invisible',h.first_access_moment(K,e,s.zeros(3,1))==(None,None))
check('zero time remainder',h.remainder_certificate(10,0,0)==0)
check('negative time symmetry',h.remainder_certificate(10,2,-.3)==h.remainder_certificate(10,2,.3))
z=1+s.I; R=(z*z*s.eye(3)+K).inv(); c=s.eye(3)[:,2]
for theta in [0,s.Rational(-1,10),s.Rational(2,3)]:
 direct=(c.T*(R-(z*z*s.eye(3)+K+theta*w*w.T).inv())*e)[0]
 check('complex noncollocated '+str(theta),s.simplify(direct-h.rank_one_difference(R,e,c,w,theta))==0)
for settings in [[0,1,2],[1,1,2],[-s.Rational(1,10),s.Rational(1,3),1]]:
 ds=[s.simplify((c.T*(R-(z*z*s.eye(3)+K+t*w*w.T).inv())*e)[0]) for t in settings]
 check('degenerate/negative polynomial '+str(settings),s.simplify(h.three_setting_residual(settings,ds))==0)
cmd=[sys.executable,'-B','scripts/local_network_response.py','--json']; start=time.monotonic()
p=subprocess.run(cmd,cwd=root,capture_output=True,text=True,timeout=120)
(out/'reproduction.stdout').write_text(p.stdout); (out/'reproduction.stderr').write_text(p.stderr)
(out/'execution.json').write_text(json.dumps({'command':cmd,'cwd':str(root),'timeout_seconds':120,'elapsed_seconds':time.monotonic()-start,'returncode':p.returncode},indent=2))
check('runner successful',p.returncode==0)
actual=json.loads(p.stdout); cache=(root/'logs/runner-cache/local_network_response.txt').read_text().split('----- stdout -----\n')[1]; expected=json.JSONDecoder().raw_decode(cache)[0]
check('fresh cache exact payload',actual==expected)
frozen=json.loads((out/'frozen_sources.json').read_text())
(out/'independent_results.json').write_text(json.dumps({'passed':len(rows),'checks':rows,'runner_summary':actual['summary']},indent=2))
print(json.dumps({'independent_checks':len(rows),'runner':actual['summary']}))
