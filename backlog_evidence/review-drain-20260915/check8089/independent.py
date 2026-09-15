import sympy as s,json,time
from itertools import combinations
start=time.monotonic();checks=[]
def ck(n,a,b):
 d=a-b
 assert all(s.simplify(x)==0 for x in d) if isinstance(d,s.MatrixBase) else s.simplify(d)==0,n
 checks.append(n)
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1);I4=s.eye(4)
# Logical matter × syndrome, independent of native edge graph assembler.
M=(3*Z+4*X)/5;E=(3*I+M)/8;ep=(I+M)/2;em=(I-M)/2
root=ep/s.sqrt(2)+em/2;other=ep/s.sqrt(2)+s.sqrt(3)*em/2
A=(root+other)/s.sqrt(2);B=(root-other)/s.sqrt(2)
S=s.kronecker_product(I,X);R=s.kronecker_product(I,Z);P=(I4+S)/2
U=s.kronecker_product(A,I)+s.kronecker_product(B,I)*R*S
ck('general_full_carrier_unitary',U.H*U,I4)
for z in (-1,1):
 Q=(I4+z*R)/2;J=s.sqrt(2)*Q*P;F=s.kronecker_product(root if z==1 else other,I)
 ck('general_effect_branch_'+str(z),Q*U*P,J*F*P)
wrong=s.kronecker_product(A,I)-s.kronecker_product(B,I)*R*S
assert wrong*P!=U*P;checks.append('pulse_sign_mutant_rejected')
# Full qubit channel norm attaining balanced-state witness and selective current.
k=s.Rational(3,5);eta=s.Rational(4,5);c=3/s.sqrt(10);q=1/s.sqrt(10)
rho=(I+Z/3+X/4)/2;channel=s.zeros(2)
for z in (-1,1):
 F=(c*I+z*q*Z)/s.sqrt(2);out=F*rho*F;prob=s.trace(out)
 ck('selective_X_'+str(z),s.trace(out*X)/prob,eta*s.trace(rho*X)/(1+z*k*s.trace(rho*Z)))
 channel+=out
ck('dephasing_channel',channel,(1+eta)*rho/2+(1-eta)*Z*rho*Z/2)
ck('contrast_disturbance_saturation',k*k,2*(1-eta)-(1-eta)**2)
# Slater update independently via normalized two-orbital wedge minors.
V=s.Matrix([[1,1],[1,s.I],[1,-1],[1,-s.I]])/2;ck('orthonormal_complex_orbitals',V.H*V,s.eye(2));C=V*V.H
R1=s.diag(s.Rational(2,3),1,1,1);W=R1*V;gram=W.H*W;norm=s.det(gram)
ck('wedge_norm_by_minors',sum(abs(W.extract(pair,[0,1]).det())**2 for pair in combinations(range(4),2)),norm)
d=s.Rational(4,9)-1;e=s.eye(4)[:,0];formula=R1*(C-d*C*e*e.H*C/(1+d*C[0,0]))*R1
ck('normalized_occupied_space',formula,W*gram.inv()*W.H);ck('idempotent_update',formula*formula,formula);ck('fixed_particle_number',s.trace(formula),2)
print(json.dumps({'status':'pass','checks':checks,'total_pass':len(checks),'seconds':time.monotonic()-start,'scope':'Independent exact syndrome dilation, parity channel and exterior-algebra Slater controls; no primary import or execution.'},indent=2))
