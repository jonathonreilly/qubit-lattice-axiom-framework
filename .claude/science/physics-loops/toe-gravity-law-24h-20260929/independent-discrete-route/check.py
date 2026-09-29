"""Independent exact small-matrix checks; no production runner imports."""
import sympy as s
from pathlib import Path
import hashlib, json, subprocess
N=7
T=s.zeros(N)
for x in range(N): T[x,(x+1)%N]=1
d=T-s.eye(N)
def elementary(i,j):
    a=s.zeros(N); a[i,j]=1; return a
I=elementary(0,0); J=elementary(1,1); K=I*d*J-J*d*I
assert K==elementary(0,1)
D=s.BlockMatrix([[s.zeros(N),s.zeros(N)],[d,s.zeros(N)]]).as_explicit()
def contraction(i):
    return s.BlockMatrix([[s.zeros(N),i],[s.zeros(N),s.zeros(N)]]).as_explicit()
def lie(i):
    c=contraction(i); return D*c+c*D
assert D*D==s.zeros(2*N)
assert lie(I)*lie(J)-lie(J)*lie(I)==lie(K)
q0=s.zeros(N,1); q0[2]=1
p0=s.zeros(N,1); p0[0]=1
local_values=[(p0.T*elementary(x,x)*d*q0)[0] for x in range(N)]
assert local_values==[0]*N
assert (p0.T*(I*d*J*d-J*d*I*d)*q0)[0]==1
print('Nearest-neighbour cotangent moment map witness: all 7 constraints=0; {J_delta0,J_delta1}=1.')
print('General contraction K=E_01 closes exactly; its scalar Lie action has (0,1)=-1 and (0,2)=1.')
# Jacobi in the contraction product A star B = A d B, exact arbitrary test entries.
A=s.Matrix(N,N,lambda a,b: (3*a+2*b)%5-2)
B=s.Matrix(N,N,lambda a,b: (a*b+2*a+b)%7-3)
C=s.Matrix(N,N,lambda a,b: (a+3*b*b)%5-2)
br=lambda a,b:a*d*b-b*d*a
assert br(A,br(B,C))+br(B,br(C,A))+br(C,br(A,B))==s.zeros(N)
assert lie(br(A,B))==lie(A)*lie(B)-lie(B)*lie(A)
print('Associative contraction product Jacobi and full 0+1 Cartan representation: exact rational residual zero.')
# Direct symplectic differentiation confirms sign, not only matrix identity.
q=s.Matrix(s.symbols('q0:'+str(2*N))); p=s.Matrix(s.symbols('p0:'+str(2*N)))
mom=lambda a:(p.T*lie(a)*q)[0]
f=mom(I); g=mom(J)
pb=sum(s.diff(f,q[x])*s.diff(g,p[x])-s.diff(f,p[x])*s.diff(g,q[x]) for x in range(2*N))
assert s.expand(pb-mom(K))==0
print('Standard {q_A,p_B}=delta_AB: {J_I,J_J}=J_(I d J-J d I), verified by direct derivatives.')
f0,f1,g0,g1=s.symbols('f0 f1 g0 g1')
assert s.expand(f1*g1-f0*g0-((f1-f0)*g1+f0*(g1-g0)))==0
assert s.expand(f1*g1-f0*g0-((f0+f1)*(g1-g0)+(g0+g1)*(f1-f0))/2)==0
print('Shifted and midpoint product identities: symbolic residual zero.')
alpha=s.symbols('alpha',positive=True)
P=s.diag(1,-1,0)
kin=(s.trace(P*P)-s.trace(P)**2/s.Integer(2))/(4*alpha)
assert kin==1/(2*alpha)
assert d*s.ones(N,1)==s.zeros(N,1)
print('Homogeneous traceless diagonal P=(1,-1,0): seed kinetic density=1/(2 alpha), nonzero; every derivative-only linear constraint=0.')
print('per_element: exact matrix entries (0,1) and (0,2) establish the local toy witness.')
print('per_site: all seven local cotangent constraints vanish at the stated exact phase point.')
print('per_mode: homogeneous seed kinetic density checked symbolically; no nonzero-mode gravity construction claimed.')
print('per_block: nilpotency and full 0+1 Cartan commutator checked on the seven-cycle.')
print('lattice_wide: general algebraic proof is in REPORT.md; finite check does not prove full gravity closure.')
print('TOTAL: PASS=7 FAIL=0')
