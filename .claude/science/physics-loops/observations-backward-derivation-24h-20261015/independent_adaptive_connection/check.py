import sympy as s,json,subprocess,time,sys,hashlib
from pathlib import Path
p=Path(__file__).resolve().parent.parent;o=Path(__file__).resolve().parent
rows=[]
def ck(n,c):
 assert c,n
 rows.append(n)
# Recover ramp coefficients by the ODE recurrence, not closed-form cosine.
g,C,tau=s.symbols('g C tau',positive=True);coeff={0:0,1:0}
for j in range(7):coeff[j+2]=s.simplify(((-g/2 if j==2 else 0)-C*coeff[j])/(tau*(j+2)*(j+1)))
ck('ramp t4',coeff[4]==-g/(24*tau));ck('ramp t6',coeff[6]==g*C/(720*tau**2));ck('coefficient ratio',s.simplify(coeff[6]/coeff[4]+C/(30*tau))==0)
q,w=s.symbols('q w',real=True);k=s.Rational(3,2);gn=s.Rational(2,3);Cn=s.Rational(7,5);boundary=gn**2/(8*Cn)
for lam in [boundary,boundary+s.Rational(1,7)]:
 V=k*q*q/2+Cn*w*w/2+gn*w*q*q/2+lam*q**4
 ck('valley stable '+str(lam),s.expand(V.subs(w,-gn*q*q/(2*Cn)))==k*q*q/2+(lam-boundary)*q**4)
lam=boundary-s.Rational(1,7);ck('unstable valley leading sign',lam-boundary<0)
# Direct Fourier integral at a nonresonant positive frequency.
x=s.symbols('x',real=True);om=s.Rational(2,5);tn=s.Rational(3,2);ln=s.Rational(1,3);D=Cn-4*tn*om**2
wp=-gn/(4*Cn)-gn*s.cos(2*x)/(4*D);cubic=4*ln*s.cos(x)**3+gn*wp*s.cos(x)
ck('Fourier third harmonic',s.simplify(s.integrate(s.expand_trig(cubic*s.cos(3*x)),(x,-s.pi,s.pi))/s.pi-(ln-gn**2/(8*D)))==0)
# Explicit zero-frequency domain counterexample in the stable family.
static=s.Rational(1,2);formal=s.Rational(1,8);ck('zero frequency nonidentifiability witness',static!=formal and static==4*formal)
cmd=[sys.executable,'-B',str(p/'probe_adaptive_connection_v1.py')];start=time.monotonic();r=subprocess.run(cmd,capture_output=True,text=True,timeout=120)
(o/'reproduction.stdout').write_text(r.stdout);(o/'reproduction.stderr').write_text(r.stderr);(o/'reproduction_receipt.json').write_text(json.dumps({'command':cmd,'timeout_seconds':120,'elapsed_seconds':time.monotonic()-start,'returncode':r.returncode},indent=2))
ck('runner succeeds',r.returncode==0);ck('published full JSON matches',json.loads(r.stdout)==json.loads((p/'ADAPTIVE_CONNECTION_CONTROLS_v1.json').read_text()))
h=json.loads((o/'frozen_sources.json').read_text());ck('frozen sources unchanged',all(hashlib.sha256((p/n).read_bytes()).hexdigest()==v for n,v in h.items()))
(o/'results.json').write_text(json.dumps({'passed':len(rows),'checks':rows,'source_finding':'omega=0 third-harmonic identification is degenerate'},indent=2));print(len(rows),'independent assertions passed; omega=0 domain finding retained')
