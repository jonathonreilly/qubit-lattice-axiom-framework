import sympy as s,itertools,json,subprocess,time,sys,hashlib
from pathlib import Path
p=Path(__file__).resolve().parent.parent;o=Path(__file__).resolve().parent
rows=[]
def ck(n,c):
 assert c,n
 rows.append(n)
xs=[s.Rational(1,3),s.Rational(5,3)];ys=[s.Rational(2,3),s.Rational(7,3)]
def matrix(vals):return s.Matrix([[-(vals[i]-vals[j+2])/(xs[i]-ys[j]) for j in range(2)] for i in range(2)])
for modes in [[],[(4,2)],[(4,2),(4,3)],[(4,2),(7,3)],[(4,2),(7,3),(9,0)],[(4,2),(7,3),(9,1)]]:
 vals=[s.Rational(8,3)-sum(s.Rational(a)/(pole-x) for pole,a in modes) for x in xs+ys];L=matrix(vals);det=L.det();distinct=len(set(pole for pole,a in modes if a>0))
 ck('distinct pole equality '+str(modes),det==0 if distinct<2 else det>0)
 for v in [-3,0,s.Rational(2,5)]:ck('affine readout '+str((modes,v)),matrix([5+v*x for x in vals]).det()==v*v*det)
 M=[sum(s.Rational(a)/pole**(n+1) for pole,a in modes) for n in [1,2,3]]
 pair=sum(s.Rational(a*b)*(s.Rational(1,pole)-s.Rational(1,other))**2/(pole**2*other**2) for j,(pole,a) in enumerate(modes) for other,b in modes[j+1:])
 ck('moment pair sum '+str(modes),s.factor(M[0]*M[2]-M[1]**2-pair)==0)
vals=[s.Rational(8,3)-2/(4-x)-3/(7-x) for x in xs+ys];truth=matrix(vals);eps=[s.Rational(j,10000) for j in [1,2,3,4]];e=s.Matrix([[(eps[i]+eps[j+2])/abs(xs[i]-ys[j]) for j in range(2)] for i in range(2)])
for signs in itertools.product([-1,1],repeat=4):
 H=matrix([v+d*ep for v,d,ep in zip(vals,signs,eps)]);E=abs(H[0,0])*e[1,1]+abs(H[1,1])*e[0,0]+e[0,0]*e[1,1]+abs(H[0,1])*e[1,0]+abs(H[1,0])*e[0,1]+e[0,1]*e[1,0]
 ck('exact error corner '+str(signs),abs(H.det()-truth.det())<=E)
cmd=[sys.executable,'-B',str(p/'probe_multimode_response_v1.py')];start=time.monotonic();r=subprocess.run(cmd,capture_output=True,text=True,timeout=120)
(o/'reproduction.stdout').write_text(r.stdout);(o/'reproduction.stderr').write_text(r.stderr);(o/'reproduction_receipt.json').write_text(json.dumps({'command':cmd,'timeout_seconds':120,'elapsed_seconds':time.monotonic()-start,'returncode':r.returncode},indent=2))
ck('runner succeeds',r.returncode==0);ck('published output exact',json.loads(r.stdout)==json.loads((p/'MULTIMODE_RESPONSE_CONTROLS_v1.json').read_text()))
h=json.loads((o/'frozen_sources.json').read_text());ck('sources unchanged',all(hashlib.sha256((p/n).read_bytes()).hexdigest()==v for n,v in h.items()))
(o/'results.json').write_text(json.dumps({'passed':len(rows),'checks':rows},indent=2));print(len(rows),'assertions passed')
