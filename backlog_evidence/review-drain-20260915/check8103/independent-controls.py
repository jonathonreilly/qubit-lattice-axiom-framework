import sympy as s,json,time
start=time.monotonic();rows=[]
def ck(n,b):
 assert b,n
 rows.append(n)
# Weighted four-cycle solve by exact constrained minimization, not pseudoinverse.
D=s.Matrix([[1,0,0,-1],[-1,1,0,0],[0,-1,1,0],[0,0,-1,1]])
rho=s.Matrix([1,-1,0,0]);E=s.Matrix([1,0,0,0]);C=s.ones(4,1);W=s.diag(1,2,3,4);n=s.symbols('n');q=((E+C*n).T*W*(E+C*n))[0];n0=s.solve(s.diff(q,n),n)[0];EL=E+C*n0;ET=E-EL
ck('exact weighted minimizer satisfies Gauss',D*EL==rho)
ck('weighted transverse orthogonality',(C.T*W*EL)[0]==0)
ck('affine field remains fractional',EL==s.Matrix([s.Rational(9,10),-s.Rational(1,10),-s.Rational(1,10),-s.Rational(1,10)]))
ck('weighted Pythagoras',(E.T*W*E)[0]==(EL.T*W*EL)[0]+(ET.T*W*ET)[0])
# Formal continuum shift symbol, including nonprimitive step2.
g,k=s.symbols('g k',real=True)
ck('primitive magnetic limit',s.limit((1-s.cos(g*k))/g**2,g,0)==k**2/2)
ck('nonprimitive doubled magnetic limit',s.limit((1-s.cos(2*g*k))/g**2,g,0)==2*k**2)
# Boundary form from literal zero extension.
v=s.Matrix(s.symbols('v0:3'));H=s.Matrix([[1,-s.Rational(1,2),0],[-s.Rational(1,2),1,-s.Rational(1,2)],[0,-s.Rational(1,2),1]])
ck('Dirichlet quadratic form retains both endpoints',s.expand((v.T*H*v)[0]-(v[0]**2+(v[1]-v[0])**2+(v[2]-v[1])**2+v[2]**2)/2)==0)
x,E0=s.symbols('x E0');u=s.Function('u')(x);phi=s.exp(-x*x)*u
ck('ground-state transformed ODE',s.simplify(s.exp(x*x)*(-s.diff(phi,x,2)/2+2*x*x*phi-E0*phi)-(-s.diff(u,x,2)/2+2*x*s.diff(u,x)+(1-E0)*u))==0)
ck('normalized oscillator Gaussian',s.integrate(s.sqrt(2/s.pi)*s.exp(-2*x*x),(x,-s.oo,s.oo))==1)
ck('oscillator gap and zero point',s.sqrt(1*4)==2 and s.sqrt(4)/2==1)
# The exact cycle-affine domain sizes differ from a product cutoff.
from itertools import combinations
eta=[0,1,0,1]
for S in [1,2]:
 count=0
 for occ in combinations(range(4),2):
  r=[int(j in occ)-eta[j] for j in range(4)];e=[r[0],sum(r[:2]),sum(r[:3]),0];count+=max(0,2*S-max(e)+min(e)+1)
 ck('charge domain smaller than product '+str(S),count<6*(2*S+1))
print(json.dumps(dict(status='PASS',checks=len(rows),controls=rows,elapsed_seconds=time.monotonic()-start,scope='Independent exact constrained minimization, shift symbols, zero-extension form and oscillator transform; no primary invocation.'),indent=2))
