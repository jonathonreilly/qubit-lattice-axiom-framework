from pathlib import Path
import json,time,itertools
import sympy as s
import mpmath as m
start=time.monotonic();rows=[]
def ck(n,b):
 assert b,n
 rows.append(n)
t=s.symbols('t',real=True);e=-2*s.sqrt(2)*s.cos((t-s.pi)/4)
ck('ring minimum',e.subs(t,s.pi)==-2*s.sqrt(2))
curv=s.diff(e,t,2).subs(t,s.pi);ck('ring curvature',curv==s.sqrt(2)/8)
ck('formal oscillator ground coefficient',s.simplify(s.sqrt(curv)-2**(-s.Rational(5,4)))==0)
ck('formal oscillator gap coefficient',s.simplify(2*s.sqrt(curv)-2**(-s.Rational(1,4)))==0)
K=s.Matrix([[4,4],[4,8]]);L=s.Matrix([[1,0],[-1,1]]);ck('contravariant coordinate metric',L*K*L.T==s.diag(4,4));ck('normal frequency distinct from Schur',s.sqrt(K[0,0])==2 and K.det()/K[1,1]==2)
# Independent70digit direct Hermitian eigensolver, no nested radical formula.
m.mp.dps=70
cert=json.load(open(Path(__file__).parent/'original-8104/.claude/science/physics-loops/flat-holonomy-spectral-floor-20260913/BLOCK15_EXACT_TWIST_CERTIFICATE.json'))
def rational(text):
 a,b=(text.split('/')+['1'])[:2];return m.mpf(a)/m.mpf(b)
def energy(twist):
 total=m.mpf(0)
 for nx,ny,nz in itertools.product(range(3),repeat=3):
  kx,ky,kz=2*m.pi*nx/3,(2*m.pi*ny+twist)/3,2*m.pi*nz/3
  a=-m.mpf(4)/5*m.cos(kx);b=m.mpf(3)/5*m.sin(kx);c=m.mpf(13)/5-m.mpf(3)/5*m.cos(kx)-m.cos(ky)-m.cos(kz);d=-m.mpf(4)/5*m.sin(kx);y=m.sin(ky);u=m.mpf(4)/25;v=m.mpf(3)/25
  H=m.matrix([[c+d,a+b-1j*y,v,u],[a+b+1j*y,-c-d,u,-v],[v,u,c-d,a-b-1j*y],[u,-v,a-b+1j*y,-c+d]])
  vals=m.eighe(H,eigvals_only=True);total+=vals[0]+vals[1]
 return total
z=energy(0);p=energy(m.pi)
ck('direct identity eigenvalue sum inside exact rational certificate',rational(cert['identity_interval'][0])<=z<=rational(cert['identity_interval'][1]))
ck('direct twisted eigenvalue sum inside exact rational certificate',rational(cert['twisted_interval'][0])<=p<=rational(cert['twisted_interval'][1]))
ck('strict witness independent diagonalization',-m.mpf('1.4425')<p-z<-m.mpf('1.4424'))
print(json.dumps(dict(status='PASS',checks=len(rows),controls=rows,difference=m.nstr(p-z,65),elapsed_seconds=time.monotonic()-start,scope='Independent70digit direct4x4 eigenvalues versus original integer certificate; symbolic ring/metric controls. No primary invocation.'),indent=2))
