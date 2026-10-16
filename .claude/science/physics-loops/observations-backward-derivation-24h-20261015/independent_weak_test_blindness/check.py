import sympy as s,math,json,subprocess,time,sys,hashlib,difflib
from pathlib import Path
p=Path(__file__).resolve().parent.parent;o=Path(__file__).resolve().parent
rows=[]
def ck(n,c):
 assert c,n
 rows.append(n)
t=s.symbols('t');Om=s.symbols('Om',positive=True)
def shifted(n):return s.diff(t**n*(t-1)**n,t,n)/s.factorial(n)
def integrate_poly(poly):return sum(co/(power[0]+1) for power,co in s.Poly(poly,t).terms())
delta=shifted(10);q=1+t
for j in range(5):
 psi=t*t*(1-t)**2*shifted(j);kernel=s.expand(q*q*s.diff(psi,t,2)+6*q*s.diff(psi,t)+(6+Om*q*q)*psi)
 actual=s.factor(integrate_poly(delta*kernel));expected=0 if j<4 else s.Rational(70,21*math.comb(20,10))*Om
 ck('Rodrigues projection '+str(j),actual==expected)
 ck('exact degree '+str(j),s.degree(kernel,t)==j+6)
point=s.expand(q*q*s.diff(delta,t,2)-2*q*s.diff(delta,t)+(2+Om*q*q)*delta)
ck('pointwise leading obstruction',s.Poly(point,t).LC()==Om*math.comb(20,10) and s.degree(point,t)==12)
a=(p/'probe_weak_test_blindness_v1.py').read_text();b=(p/'probe_weak_test_blindness_v2.py').read_text();ck('serialization-only correction',b==a.replace('degree=s.degree(K,t)','degree=int(s.degree(K,t))'))
(o/'v1_v2.diff').write_text(''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True))))
err=(p/'WEAK_TEST_BLINDNESS_EXECUTION_v1.stderr').read_text();ck('preserved original serialization failure','TypeError' in err and 'JSON serializable' in err)
cmd=[sys.executable,'-B',str(p/'probe_weak_test_blindness_v2.py')];start=time.monotonic();r=subprocess.run(cmd,capture_output=True,text=True,timeout=120)
(o/'reproduction.stdout').write_text(r.stdout);(o/'reproduction.stderr').write_text(r.stderr);(o/'reproduction_receipt.json').write_text(json.dumps({'command':cmd,'timeout_seconds':120,'elapsed_seconds':time.monotonic()-start,'returncode':r.returncode},indent=2))
ck('author succeeds',r.returncode==0);ck('published output exact',json.loads(r.stdout)==json.loads((p/'WEAK_TEST_BLINDNESS_CONTROLS_v2.json').read_text()))
h=json.loads((o/'frozen_sources.json').read_text());ck('sources unchanged',all(hashlib.sha256((p/n).read_bytes()).hexdigest()==v for n,v in h.items()))
(o/'results.json').write_text(json.dumps({'passed':len(rows),'checks':rows},indent=2));print(len(rows),'assertions passed')
