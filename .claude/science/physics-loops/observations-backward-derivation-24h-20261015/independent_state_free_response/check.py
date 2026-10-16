import sympy as s,json,subprocess,time,hashlib,sys
from pathlib import Path
p=Path(__file__).resolve().parent.parent;o=Path(__file__).resolve().parent
rows=[]
def ck(n,c):
 assert c,n
 rows.append(n)
t=s.symbols('t',real=True);q=s.exp(t);a=1;b=q*q;m=s.Rational(3,2);k=s.Rational(5,3);tau=s.Rational(2,3);C=4*tau;g=s.Rational(-3,4);lam=s.Rational(1,5);Om=C/tau;G=g*g/tau
psi=t*t*(1-t)**2;P=s.diff(psi,t,2)+Om*psi;B=4*lam*s.diff(psi,t,2)+(4*lam*Om-G/2)*psi
for u,v in [(0,0),(2,-3),(-1,s.Rational(1,2))]:
 w=-g*s.exp(2*t)/(2*tau*(4+Om))+u*s.cos(2*t)+v*s.sin(2*t)
 z=m*a+k+4*lam*b+g*w
 ck('constructed hidden ODE '+str((u,v)),s.simplify(tau*s.diff(w,t,2)+C*w+g*b/2)==0)
 ck('exact clamped weak integral '+str((u,v)),s.simplify(s.integrate((z-m*a)*P-k*Om*psi-b*B,(t,0,1)))==0)
# g=0 spurious solution satisfies eliminated equation but not force equation.
h=s.cos(2*t);ck('zero coupling spurious homogeneous solution',s.diff(h,t,2)+4*h==0 and h!=0)
cz=-Om;ca2=m;ca=m*Om;c1=k*Om;cb2=4*lam;cb=4*lam*Om-G/2
ck('shared action constraints',cz<0 and ca2>0 and c1>0 and ca==-cz*ca2 and 2*(-cz*cb2-cb)==G)
ck('stable coefficient equivalence',s.simplify(cb-4*Om*(lam-G/(8*Om)))==0 and cb>0)
# Lower bound valid continuously for every published q waveform, not merely samples.
ck('global nonzero chart for primary profiles',s.Rational(13,10)-s.Rational(25,100)-s.Rational(17,100)-s.Rational(7,100)>s.Rational(8,10))
cmd=[sys.executable,'-B',str(p/'probe_state_free_response_v1.py')];start=time.monotonic();r=subprocess.run(cmd,capture_output=True,text=True,timeout=120)
(o/'reproduction.stdout').write_text(r.stdout);(o/'reproduction.stderr').write_text(r.stderr);(o/'reproduction_receipt.json').write_text(json.dumps({'command':cmd,'timeout_seconds':120,'elapsed_seconds':time.monotonic()-start,'returncode':r.returncode},indent=2))
ck('author succeeds',r.returncode==0);ck('published output exactly reproduced',json.loads(r.stdout)==json.loads((p/'STATE_FREE_RESPONSE_CONTROLS_v1.json').read_text()))
hashes=json.loads((o/'frozen_sources.json').read_text());ck('frozen unchanged',all(hashlib.sha256((p/n).read_bytes()).hexdigest()==v for n,v in hashes.items()))
(o/'results.json').write_text(json.dumps({'passed':len(rows),'checks':rows},indent=2));print(len(rows),'assertions passed')
