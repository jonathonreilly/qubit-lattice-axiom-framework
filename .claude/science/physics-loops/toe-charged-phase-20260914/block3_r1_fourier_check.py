"""r=1 Wilson sign: exact Clifford algebra, graph certificate, rational tail,
and independent full determinants on the isolated cycle. No phase claim.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
import json,math
import numpy as np
import sympy as sp
word=[-1,-4,3,-2,-3,1,2,3,4,-3]
x=(1,1,0,1);visited=[x];edges=[]
for a in word:
    y=list(x);y[abs(a)-1]+=1 if a>0 else -1;y=tuple(y)
    assert all(v in [0,1] for v in y)
    edges.append((x,y));visited.append(y);x=y
assert visited[-1]==visited[0] and len(set(visited[:-1]))==10
# Exhaust the subcurrent claim without using spin matrices.
closed=[]
for bits in product([0,1],repeat=10):
    div={v:0 for v in visited[:-1]}
    for b,(x,y) in zip(bits,edges):div[x]-=b;div[y]+=b
    if not any(div.values()):closed.append(bits)
assert closed==[(0,)*10,(1,)*10]
# Clifford e_A e_B multiplication by inversion parity, independent of matrices.
def mul(A,B):
    out={}
    for a,ca in A.items():
        for b,cb in B.items():
            inversions=sum((b&((1<<i)-1)).bit_count() for i in range(4) if a&(1<<i))
            mask=a^b;out[mask]=out.get(mask,F(0))+ca*cb*((-1)**inversions)
    return {k:v for k,v in out.items() if v}
poly={0:F(1)}
for a in word:poly=mul(poly,{0:F(1,2),1<<(abs(a)-1):F(-1 if a>0 else 1,2)})
trace=4*poly.get(0,F(0));assert trace==F(1,32)
sx=sp.Matrix([[0,1],[1,0]]);sy=sp.Matrix([[0,-sp.I],[sp.I,0]]);sz=sp.diag(1,-1);I=sp.eye(4)
gam=[sp.kronecker_product(sx,g) for g in [sx,sy,sz]]+[sp.kronecker_product(sy,sp.eye(2))]
def projector(a):return (I-sp.sign(a)*gam[abs(a)-1])/2
def spin_product(w):
    P=I
    for a in w:P=(P*projector(a)).applyfunc(sp.expand)
    return P
P=spin_product(word);Prev=spin_product([-a for a in word[::-1]]);Pbar=spin_product([-a for a in word])
assert sp.trace(P)==sp.Rational(trace.numerator,trace.denominator)
assert sp.trace(Pbar)==sp.trace(P) and sp.trace(Prev)==sp.trace(P)
l=sp.symbols('l');char=P.charpoly(l).as_expr()
assert sp.expand(char-(l**4-l**3/32+l**2/1024))==0
# Derive the isolated-cycle determinant's Laurent form from the two transfer
# products, then compare whole 40x40 determinants at nontrivial phases.
z,u=sp.symbols('z u',nonzero=True)
forward=sp.expand((I-u**10*z*P).det())
reverse=sp.expand((I-u**10/z*Prev).det());cycle=sp.expand(forward*reverse)
paired=sp.expand(cycle*cycle)
assert sp.expand(paired).coeff(z,1).coeff(u,10)==-sp.Rational(1,16)
assert all(sp.expand(paired).coeff(z,1).coeff(u,r)==0 for r in range(10))
checks=[]
for mass in [2.5,5.,10.]:
    for angle in [0.,.317,1.1,math.pi]:
        D=np.eye(40,dtype=complex)
        for i,a in enumerate(word):
            j=(i+1)%10;phase=np.exp(1j*angle) if i==0 else 1
            Pf=np.array(projector(a),complex);Pb=np.array(projector(-a),complex)
            D[4*i:4*i+4,4*j:4*j+4]-=Pf*phase/mass
            D[4*j:4*j+4,4*i:4*i+4]-=Pb*phase.conjugate()/mass
        direct=np.linalg.det(D)
        predicted=complex(cycle.subs({u:1/mass,z:np.exp(1j*angle)}).evalf(30))
        err=abs(direct-predicted);assert err<3e-14
        checks.append({'mass':mass,'angle':angle,'direct_determinant_real':float(direct.real),'transfer_formula_error':err})
# Full 16-site four-dimensional box: exact global polynomial tail, no
# finite-angle approximation of its 32-dimensional Fourier coefficient.
mass=2**100
ratio=F(16*math.comb(128,11)*4**11,mass-39);assert ratio<1
assert all(F(4*(128-r),r+1)<=39 for r in range(11,128))
# Bound is derived from principal minors and the axial norm. Directly check
# the actual full-box norm and gamma5-Hermiticity at independent phase fields.
vs=list(product(range(2),repeat=4));ix={v:i for i,v in enumerate(vs)}
g5=gam[0]*gam[1]*gam[2]*gam[3];G5=np.kron(np.eye(16),np.array(g5,complex))
rng=np.random.default_rng(91410);full=[]
for rep in range(3):
    K=np.zeros((64,64),complex)
    for x in vs:
        for mu in range(4):
            if x[mu]==1:continue
            y=list(x);y[mu]+=1;y=tuple(y);a=slice(4*ix[x],4*ix[x]+4);b=slice(4*ix[y],4*ix[y]+4)
            phase=np.exp(1j*rng.uniform(-math.pi,math.pi))
            K[a,b]=-np.array(projector(mu+1),complex)*phase
            K[b,a]=-np.array(projector(-mu-1),complex)*phase.conjugate()
    norm=float(np.linalg.norm(K,2));assert norm<=4+1e-12
    assert np.linalg.norm(K.conj().T-G5@K@G5)<1e-13
    full.append(norm)
result={'word':word,'cycle_vertices':[list(v) for v in visited],'proper_nonempty_closed_subcurrents':0,'Clifford_trace_exact':str(trace),'explicit_matrix_charpoly':str(char),'adjoint_and_reverse_trace_equal':True,'leading_full_box_Fourier_coefficient':'-1/(16*M^10)','certificate_mass':str(mass),'remainder_to_leading_upper_exact':str(ratio),'remainder_to_leading_upper_float':float(ratio),'negative_real_Fourier_coefficient_certified':True,'isolated_cycle_determinant':str(cycle),'independent_cycle_determinant_checks':checks,'full_box_random_phase_operator_norms':full,'scope':'pointwise-positive standard r=1 Wilson paired determinant is not universally of positive Fourier type; no phase/no-go conclusion'}
print(json.dumps(result,indent=2),flush=True)
Path(__file__).with_name('BLOCK3_R1_FOURIER_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
