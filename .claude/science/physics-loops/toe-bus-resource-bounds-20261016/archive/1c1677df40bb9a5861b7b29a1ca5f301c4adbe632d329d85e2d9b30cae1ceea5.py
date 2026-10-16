"""One exact finite discriminator: installed versus code-compressed moments."""
import json
import platform
import signal
import sympy as s
signal.alarm(30)
I=s.eye(2); X=s.Matrix([[0,1],[1,0]]); Y=s.Matrix([[0,-s.I],[s.I,0]]); Z=s.diag(1,-1)
n=s.diag(0,1); sm=s.Matrix([[0,1],[0,0]]); sp=sm.T
N=3; sites=6; dim=2**sites; ID=s.eye(dim)
def embed(op,j):
    return s.kronecker_product(*[op if k==j else I for k in range(sites)])
def pair(op1,j,op2,k): return embed(op1,j)*embed(op2,k)
def exchange(j,k): return pair(sp,j,sm,k)+pair(sm,j,sp,k)
def swap(j,k): return (ID+pair(X,j,X,k)+pair(Y,j,Y,k)+pair(Z,j,Z,k))/2
def eq(A,B,label):
    assert A.shape==B.shape,label
    assert all(s.simplify(v)==0 for v in A-B),label
xi=s.Rational(1,7); vp=s.Rational(2,3); r=s.Rational(3,5)
omega=s.Rational(3,2); u=-s.Rational(2,5); v=s.Rational(4,7); jf=s.Rational(2,3)
H=embed(Y+2*Z,0); B=I+X; Bfull=embed(B,0)
blocks=[]
def block(h,c): blocks.append((h,c))
block(3*ID,s.Integer(3))
for j,d in [(1,s.Rational(4,3)),(2,s.Rational(5,3))]: block(d*embed(n,j),d)
hop=s.Rational(1,4); block(hop*(exchange(1,2)+ID),2*hop)
for j in range(3,6): block(omega*embed(n,j),omega)
for j in range(3,5): block(jf*(ID-swap(j,j+1)),2*jf)
block(xi*vp*(Bfull*embed(X,1)+2*ID),4*xi*vp)
block(xi*r*(exchange(2,3)+ID),2*xi*r)
for j in range(3,6): block(xi**2*(u*embed(n,j)-u*ID),xi**2*abs(u))
for j in range(3,5): block(xi**2*v*pair(n,j,n,j+1),xi**2*abs(v))
A=sum((h for h,c in blocks),s.zeros(dim)); C0=sum(c for h,c in blocks)
Gamma=sum((c*ID-h for h,c in blocks),s.zeros(dim)); K=H+A
eq(K+Gamma,H+C0*ID,'complete compensation identity')
alpha=s.Matrix([1,s.I])/s.sqrt(2); vac=s.Matrix([1,0])
Omega=s.kronecker_product(vac,vac,alpha,alpha,alpha)
J=s.kronecker_product(I,Omega); KJ=K*J
first=J.conjugate().T*KJ; second=KJ.conjugate().T*KJ
R=3+hop+xi*(2*vp+r)+xi**2*N*(-u)
a=omega+xi**2*u; b=xi**2*v
mu=a*N/2+b*(N-1)/4
var=a*a*N/4+b*b*(5*N-7)/16+a*b*(N-1)/2
Hsmall=Y+2*Z; scalar=R+mu
predfirst=Hsmall+scalar*I
predsecond=Hsmall*Hsmall+2*scalar*Hsmall+(scalar**2+var+xi**2*r**2/2)*I+xi**2*vp**2*(B*B)
eq(first,predfirst,'first compression')
eq(second,predsecond,'complete second compression')
AJ=A*J
predA2=(scalar**2+var+xi**2*r**2/2)*I+xi**2*vp**2*(B*B)
eq(AJ.conjugate().T*AJ,predA2,'release residual compression')
Nhat=sum((embed(n,j) for j in range(3,6)),s.zeros(dim))
D=sum((pair(n,j,n,j+1) for j in range(3,5)),s.zeros(dim))
Dcode=Nhat*(Nhat-ID)/N
Kmut=K+xi**2*v*(Dcode-D); KmutJ=Kmut*J
eq(J.conjugate().T*KmutJ,first,'mutant preserves first moment')
mutsecond=KmutJ.conjugate().T*KmutJ
eq(second-mutsecond,(b*b/12)*I,'omitted off-code fluctuation detected')
assert b*b/12>0
Rphi=(I+s.I*X)/s.sqrt(2)
eq(Rphi*vac,alpha,'equatorial phase orientation')
assert Hsmall*B!=B*Hsmall
print(json.dumps({
 'python':platform.python_version(),'sympy':s.__version__,'dimension':dim,'source_length':N,
 'number_positive_bus_blocks':len(blocks),'H_noncommutes_with_B':True,
 'C0':str(C0),'actual_reserve_R':str(R),'source_mean':str(mu),'source_variance':str(var),
 'first_compression':str(first),'second_compression':str(second),
 'complete_compensation_identity':True,'release_residual_identity':True,
 'code_only_mutant_preserves_mean':True,'missing_variance_per_old_vector':str(b*b/12),
 'rotation_phase':'exp(-i*pi/4) per source qubit for positive log (pi/4)(I-X)',
 'scope':'One exact finite compression check, not propagation or a family proof.'},indent=2))
