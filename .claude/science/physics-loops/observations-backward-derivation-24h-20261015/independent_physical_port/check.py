AUDIT_TIMEOUT_SEC=120
import sympy as s,numpy as np,itertools,json,subprocess,time,sys,hashlib
from pathlib import Path
p=Path(__file__).resolve().parent.parent;o=Path(__file__).resolve().parent
rows=[]
def ck(n,c):
 assert c,n
 rows.append(n)
q,I,j=s.symbols('q I j',real=True);phi=-s.exp(q);k=s.diff(phi,q);W0=q*q;W=W0+phi*I+s.sin(q)*I**2/2+s.exp(2*q)*I**3/3
flux=s.diff(W,I);hc=flux-phi;corr=s.integrate(s.diff(hc.subs(I,j),q)/k,(j,0,I))
ck('negative nonpolynomial flux chart',s.simplify((s.diff(W,q)-s.diff(W0,q))/k-I-corr)==0)
b=s.sin(q);lam=s.Rational(7,3);a=lam*s.diff(b,q);ck('reciprocity decreasing chart',s.simplify(a/k-lam*s.diff(b,q)/k)==0)
q1,q2=s.symbols('q1 q2',real=True);ck('work difference',s.simplify((W-W0).subs(q,q2)-(W-W0).subs(q,q1)-s.integrate(flux.subs(q,q2)-flux.subs(q,q1),(I,0,I)))==0)
# Exact edge counterexample by elementary symbolic integration.
t=s.symbols('t',real=True);g=-s.sin(2*s.pi*t)/(2*s.pi);r=s.Rational(1,4)
asym=s.integrate(g*t/r,(t,0,r))+s.integrate(g,(t,r,1));ck('asymmetric endpoint',s.simplify(asym-1/(4*s.pi**2)+1/(2*s.pi**3))==0)
sym=s.integrate(g*t/r,(t,0,r))+s.integrate(g,(t,r,1-r))+s.integrate(g*(1-t)/r,(t,1-r,1));ck('symmetric endpoint',s.simplify(sym)==0)
# Deterministic complex perturbation corners, no imported author helper.
vals=np.array([2+.7j,.8-.4j,.3+.2j,1.2-.3j,1.1,.6,-.2],complex);eps=np.array([.02,.03,.04,.05,.01,.02,.03]);V,cur,Z,v,m,acc,X=vals
MI,MV,MZ=abs(cur),abs(V),abs(Z);N=V*cur-Z*cur**2;eV,eI,eZ,ev,em,ea,eX=eps
eN=MI*eV+MV*eI+eV*eI+MI**2*eZ+MZ*(2*MI*eI+eI**2)+eZ*(2*MI*eI+eI**2)
bound=eN/(abs(v)-ev)+abs(N)*ev/(abs(v)*(abs(v)-ev))+abs(m)*ea+abs(acc)*em+em*ea+eX
def force(x):V,I,Z,v,m,a,X=x;return (V*I-Z*I*I)/v-m*a-X
for signs in itertools.product([-1,1],repeat=7):
 perturb=eps*np.array(signs)*np.array([1j,1,-1j,1j,1,1,1]);ck('complex corner '+str(signs),abs(force(vals+perturb)-force(vals))<=bound+1e-14)
# Exact sharp linear transfer for two centered pulse-error vectors.
ss,pp=-.4,.7;weights=np.array([-pp,ss+pp,-(1+ss),(ss+pp)/pp,-(1+ss)/pp,1/pp]);eta=.003
ck('centered readout bound sharp',abs(weights@(eta*np.sign(weights))-weights@(-eta*np.sign(weights))-2*eta*sum(abs(weights)))<1e-15)
cmd=[sys.executable,'-B',str(p/'check_physical_port_bridge_v1.py')];start=time.monotonic();out=subprocess.run(cmd,capture_output=True,text=True,timeout=120)
(o/'reproduction.stdout').write_text(out.stdout);(o/'reproduction.stderr').write_text(out.stderr);(o/'reproduction_receipt.json').write_text(json.dumps({'command':cmd,'timeout_seconds':120,'elapsed_seconds':time.monotonic()-start,'returncode':out.returncode},indent=2))
ck('runner succeeds',out.returncode==0);actual=json.loads(out.stdout);ck('full output reproduced',actual==json.loads((p/'PHYSICAL_PORT_CONTROLS_v1.json').read_text()))
h=json.loads((o/'frozen_sources.json').read_text());ck('sources unchanged',all(hashlib.sha256((p/n).read_bytes()).hexdigest()==v for n,v in h.items()))
(o/'results.json').write_text(json.dumps({'passed':len(rows),'checks':rows,'author_summary':actual['summary']},indent=2));print(len(rows),'assertions passed')
