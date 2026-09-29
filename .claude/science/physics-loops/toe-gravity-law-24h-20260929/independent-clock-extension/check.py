"""Exact sparse multi-clock checks; finite classical comparator, no science imports."""
import sympy as s
from itertools import combinations
n=6;m=n-1
T=s.symbols('T0:'+str(m)); q=s.symbols('q0:'+str(n)); p=s.symbols('p0:'+str(n)); Pi=s.symbols('Pi0:'+str(m))
def E(i,j):
    a=s.MutableSparseMatrix(n,n,{});a[i,j]=1;return a
A=[E(i,i+1) for i in range(m)]
F=sum((T[i]*A[i] for i in range(m)),s.zeros(n))
br=lambda a,b:a*b-b*a
B=[]
for a in A:
    cur=a;total=s.zeros(n)
    for degree in range(n):
        total+=cur/s.factorial(degree+1)
        cur=br(F,cur)
    assert cur==s.zeros(n)
    B.append(total.applyfunc(s.expand))
# Convention: {p^T A q,p^T B q}=p^T[A,B]q.
for i,j in combinations(range(m),2):
    curvature=-B[j].diff(T[i])+B[i].diff(T[j])+br(B[i],B[j])
    assert curvature.applyfunc(s.expand)==s.zeros(n)
print('A: six-site chain, five independent clocks: all 10 exact polynomial extended-constraint brackets vanish.')
# Explicit direct symplectic differentiation in the three-site/two-clock subcase.
qa,qb,qc,pa,pb,pc,ta,tb,pita,pitb=s.symbols('qa qb qc pa pb pc ta tb pita pitb')
H0=pa*qb;H1=pb*qc;H2=pa*qc
C0=pita+H0-tb*H2/2;C1=pitb+H1+ta*H2/2
coords=[qa,qb,qc,ta,tb];moms=[pa,pb,pc,pita,pitb]
def pbfull(f,g):
    return s.expand(sum(s.diff(f,a)*s.diff(g,b)-s.diff(f,b)*s.diff(g,a) for a,b in zip(coords,moms)))
assert pbfull(C0,C1)==0
assert pbfull(pita+H0,pitb+H1)==H2
print('B: direct canonical derivatives confirm C0=Pi0+H0-T1 H2/2, C1=Pi1+H1+T0 H2/2 close exactly; frozen-clock bracket is H2.')
# Direct Poisson Jacobi, nontrivial canonical coordinate vs two constraints.
assert s.expand(pbfull(qa,pbfull(C0,C1))+pbfull(C0,pbfull(C1,qa))+pbfull(C1,pbfull(qa,C0)))==0
print('C: direct mixed coordinate/constraint Jacobi identity verified; canonical bracket is unchanged.')
# Coincident-clock sum remains exactly original global Hamiltonian.
t=s.symbols('t');equal={a:t for a in T}
Bsum=sum((a.subs(equal) for a in B),s.zeros(n)).applyfunc(s.expand)
assert Bsum==sum(A,s.zeros(n))
print('D: at T0=...=T4=t, sum of dressed local generators equals the original nearest-neighbour total Hamiltonian exactly.')
# Endpoint coefficient at every graph distance, despite local initial densities.
for distance in range(1,n):
    assert s.expand(B[0].subs(equal)[0,distance]-(-t)**(distance-1)/s.factorial(distance))==0
assert B[0].subs(equal)[0,n-1]==t**4/120
print('E: dressed endpoint generator has coefficients 1,-t/2,t^2/6,-t^3/24,t^4/120 at distances 1,...,5.')
# A positive harmonic nearest-neighbour example also fails frozen local clocks.
x0,x1,v0,v1,kap=s.symbols('x0 x1 v0 v1 kap',real=True)
f=v0*v0/2+kap*(x1-x0)**2/4
g=v1*v1/2+kap*(x1-x0)**2/4
ph=s.expand(sum(s.diff(f,a)*s.diff(g,b)-s.diff(f,b)*s.diff(g,a) for a,b in [(x0,v0),(x1,v1)]))
assert s.expand(ph+kap*(v0+v1)*(x0-x1)/2)==0
assert ph.subs({x0:1,x1:0,v0:0,v1:1,kap:1})==-s.Rational(1,2)
print('F: positive two-site harmonic energy split: frozen-clock curvature=-kappa(p0+p1)(q0-q1)/2; exact witness -1/2.')
# Constraint quotient need not impose the original local energies.
point={qa:0,qb:1,qc:0,pa:1,pb:0,pc:0,ta:0,tb:0,pita:-1,pitb:0}
assert C0.subs(point)==0 and C1.subs(point)==0 and H0.subs(point)==1
print('G: exact extended constraint-surface point has H0=1, Pi0=-1, all C=0: original H_a=0 is not imposed.')
print('per_element: sparse distance-five coefficient and explicit two-clock signs are exact rational polynomials.')
print('per_site: five clock generators on a six-site nearest-neighbour open chain are tested together.')
print('per_mode: no gravitational Fourier-mode or native qubit identification is claimed by this clock extension.')
print('per_block: all ten polynomial curvature matrices and one direct canonical Jacobi triple vanish exactly.')
print('lattice_wide: arbitrary finite-system closure follows from one canonical map; the chain proves no uniform exact support bound for this construction.')
print('TOTAL: PASS=7 FAIL=0')
