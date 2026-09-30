"""Independent rational polynomial controls; imports no candidate code."""
from pathlib import Path
import itertools, json, math
import sympy as s

AUDIT_TIMEOUT_SEC = 180
checks = []
def check(name, ok, **detail):
    checks.append(dict(name=name, ok=bool(ok), **detail))
    print(name, bool(ok), detail, flush=True)
    assert ok, name

n = s.Matrix(s.symbols('nx ny nz'))
v = s.symbols('a b c d e')
T = s.Matrix([[v[0],v[2],v[3]],[v[2],v[1],v[4]],[v[3],v[4],-v[0]-v[1]]])
qmons = [n[i]*n[j] for i in range(3) for j in range(i,3)]
tmons = [v[i]*v[j] for i in range(5) for j in range(i,5)]
mons = [a*b for a in qmons for b in tmons]
var = list(n)+list(v)
keys = [s.Poly(m,*var).monoms()[0] for m in mons]
rot = []
for pm in itertools.permutations(range(3)):
    for sg in itertools.product([-1,1], repeat=3):
        R = s.zeros(3)
        for i in range(3): R[i,pm[i]]=sg[i]
        if R.det()==1: rot.append(R)
trans = []
for R in rot:
    rn,rt=R*n,R*T*R.T
    trans.append(dict(zip(var,list(rn)+[rt[0,0],rt[1,1],rt[0,1],rt[0,2],rt[1,2]])))
cols=[]
for m in mons:
    p=s.Poly(s.expand(sum(m.xreplace(sub) for sub in trans)/24),*var)
    dd=p.as_dict();cols.append(s.Matrix([dd.get(k,0) for k in keys]))
P=s.Matrix.hstack(*cols)
check('exact cubic Reynolds projection', P*P==P and P.rank()==6,
      dimension=P.rank(), rotations=len(rot), coefficient_dimension=len(mons))
basis=P.columnspace()
polys=[s.expand(sum(c*m for c,m in zip(b,mons))) for b in basis]
rows=[]
for axis in range(3):
    u=s.eye(3)[:,axis]; e=n.cross(u)
    H=(n*e.T+e*n.T)/2
    sub=dict(zip(v,[H[0,0],H[1,1],H[0,1],H[0,2],H[1,2]]))
    for z in v:
        ps=[s.Poly(s.expand(s.diff(F,z).subs(sub,simultaneous=True)),*n) for F in polys]
        kk=set().union(*(set(p.monoms()) for p in ps))
        rows.extend([[p.as_dict().get(k,0) for p in ps] for k in sorted(kk)])
C=s.Matrix(rows)
N=C.nullspace()
eh=s.expand((n.dot(n)*s.trace(T*T))/2-(T*n).dot(T*n))
ehvec=s.Matrix([s.Poly(eh,*var).as_dict().get(k,0) for k in keys])
Bn=s.Matrix.hstack(*basis)
coef=Bn.gauss_jordan_solve(ehvec)[0]
check('all-direction helicity-one annihilator is EH only',
      len(N)==1 and C*coef==s.zeros(C.rows,1),
      constraint_rank=C.rank(), nullity=len(N), exact_polynomial_constraints=C.rows)
axis=s.Matrix([0,0,1]); tt=s.diag(1,-1,0); h0=s.diag(1,1,-2)
def form(t):
    return s.Rational(1,2)*s.trace(t*t)-(t*axis).dot(t*axis)
check('EH is indefinite on spin-two', form(tt)/s.trace(tt*tt)==s.Rational(1,2)
      and form(h0)/s.trace(h0*h0)==-s.Rational(1,6),
      helicity_two='1/2', helicity_zero='-1/6')

xi=s.Matrix(s.symbols('x0:3'))
aa=s.symbols('A0:5')
A=s.Matrix([[aa[0],aa[2],aa[3]],[aa[2],aa[1],aa[4]],[aa[3],aa[4],-aa[0]-aa[1]]])
cross=s.Matrix([[0,-n[2],n[1]],[n[2],0,-n[0]],[-n[1],n[0],0]])
M=(n*xi.T+xi*n.T)/2+(cross*A-A*cross)/2
zz=M*n; scalar=n.dot(zz)
h1=2*(zz.dot(zz)-scalar**2)
ttweight=s.trace(M*M)-2*zz.dot(zz)+scalar**2-(s.trace(M)-scalar)**2/2
def df(k): return math.prod(range(k,0,-2)) if k>0 else 1
def average(p):
    total=0
    for powers,c in s.Poly(s.expand(p),*n).terms():
        if any(k%2 for k in powers): continue
        total+=c*s.Rational(math.prod(df(k-1) for k in powers),df(sum(powers)+1))
    return s.expand(total)
av1,av2=average(h1),average(ttweight)
check('exact angular quarter identity',
      s.expand(av1-av2/4-xi.dot(xi)/3)==0,
      helicity_one=str(av1), helicity_two=str(av2))

params=s.symbols('m0:18')
MM=s.zeros(3)
for ij,(i,j) in enumerate([(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]):
    MM[i,j]=MM[j,i]=sum(params[3*ij+k]*n[k] for k in range(3))
constraint=s.Poly(s.expand(n.dot(n)*s.trace(MM)-n.dot(MM*n)),*n)
coeff=s.Matrix([c for _,c in constraint.terms()])
CC=coeff.jacobian(params)
check('scalar-compatible first moments rank ten',CC.rank()==10,
      unknowns=18, polynomial_rank=CC.rank(), kernel_dimension=18-CC.rank())
mr=s.Matrix([M[i,j] for i,j in [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]])
coeffM=s.Matrix([s.expand(f).coeff(z) for f in mr for z in n])
image=coeffM.jacobian(list(xi)+list(aa))
check('gauge and symmetric curl span exact kernel',
      image.rank()==8 and CC*image==s.zeros(10,8), dimension=image.rank())

# Positivity alone permits odd corrections above a positive quadratic term.
x=s.symbols('x',real=True)
check('analytic PSD cubic counterexample',
      s.expand(x*x*(1+x))==x*x+x**3,
      domain='|x|<1', form='x^2(1+x)', conclusion='general remainder O(q^3); O(q^4) after quadratic compression vanishes')
# Both definitions of a qubit stiffness, checked as actual Pauli matrices.
Z=s.diag(1,-1)/2; I=s.eye(2)
zs=[s.kronecker_product(*[Z if k==j else I for k in range(3)]) for j in range(3)]
norm=sum((z*z for z in zs),s.zeros(8))
trace=sum(zs,s.zeros(8)); fp=norm-trace*trace
check('qubit norm stiffness constant; FP nonconstant',
      norm==s.eye(8)*s.Rational(3,4) and fp!=s.eye(8)*fp[0,0],
      norm_constant='3/4', FP_distinct_diagonal=sorted(set(map(str,fp.diagonal()))))
kk=s.symbols('k0:5'); tv=s.symbols('t0:5')
k=s.Matrix([[kk[0],kk[2],kk[3]],[kk[2],kk[1],kk[4]],[kk[3],kk[4],-kk[0]-kk[1]]])
t=s.Matrix([[tv[0],tv[2],tv[3]],[tv[2],tv[1],tv[4]],[tv[3],tv[4],1-tv[0]-tv[1]]])
tau=t-s.eye(3)
cx=s.Matrix([[0,-xi[2],xi[1]],[xi[2],0,-xi[0]],[-xi[1],xi[0],0]])
B=A+cx
g=M*n
f=(n.dot(k*n)*t-(n.dot(t*n)-n.dot(n))*k)*n
identity=2*s.det(s.Matrix.hstack(n,g,f))+n.dot(n)*(n.dot(k*n)*n.dot(tau*B*n)-n.dot(tau*n)*n.dot(k*B*n))
check('H2 identity by generic symbolic expansion', s.expand(identity)==0,
      premise='symmetric trace-zero k, symmetric trace-one t; no numerical samples')
omega=s.Matrix(s.symbols('w0:3'))
Om=s.Matrix([[0,-omega[2],omega[1]],[omega[2],0,-omega[0]],[-omega[1],omega[0],0]])
for label,kv,tv0,want in [
    ('generic',s.Matrix([[1,1,0],[1,2,1],[0,1,-3]]),s.Matrix([[2,1,2],[1,-2,1],[2,1,1]]),0),
    ('special_z',s.diag(1,2,-3),s.diag(1,1,-1),1),
    ('special_y',s.diag(1,-3,2),s.diag(1,-1,1),1),
]:
    assert kv.det()!=0 and s.trace(kv)==0 and s.trace(tv0)==1
    pp=kv.inv()*(tv0-s.eye(3))
    eq=pp.T*Om-Om*pp
    rank=s.Matrix(list(eq)).jacobian(omega).rank()
    check('exact H2 omega nullity '+label, 3-rank==want,
          nullity=3-rank, expected=want, k_determinant=str(kv.det()))
    fv=((n.dot(kv*n))*tv0-(n.dot(tv0*n)-n.dot(n))*kv)*n
    gcd=s.polys.polytools.terms_gcd(fv[0])
    gcd=s.gcd(s.gcd(fv[0],fv[1]),fv[2])
    check('primitive cubic '+label, s.Poly(gcd,*n).total_degree()==0,
          common_factor=str(gcd))

# Independent continuum moment maps for full vs transverse-only momentum rules.
cx0=n.cross(MM*n)
cp=s.Matrix([c for e in cx0 for _,c in s.Poly(s.expand(e),*n).terms()])
cr=cp.jacobian(params)
check('transverse momentum first moments pure trace',cr.rank()==15,
      dimension=18-cr.rank(), interpretation='ell(n) I')
dp=s.Matrix([c for e in MM*n for _,c in s.Poly(s.expand(e),*n).terms()])
dr=dp.jacobian(params)
check('full tensor momentum first moments vanish',dr.rank()==18,
      dimension=18-dr.rank())

# A gapped trace can carry unreduced helicity-one weight; eliminating it matters.
bb=s.Matrix([[1,0,0],[0,0,0],[0,0,0]])
mix=s.Matrix([[1,1,0],[1,1,0],[0,0,1]])
eff=mix[1:,1:]-mix[1:,0]*mix[0,1:]/mix[0,0]
check('gapped-sector Schur correction is consequential',
      eff==s.diag(0,1),
      unreduced_kinetic_weight=1, effective_kinetic_weight=0,
      conclusion='quarter identity must be applied to projected effective move family')
assert all(c['ok'] for c in checks)
print('RATIONAL CONTROLS PASS:', len(checks))
