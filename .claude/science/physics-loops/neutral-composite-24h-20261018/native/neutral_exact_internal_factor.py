"""Exact collective/internal factorization of the supplied eight-state rung."""
from pathlib import Path
import sympy as s,json,itertools
P=Path(__file__).resolve().parent
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1)
k=s.kronecker_product
p=lambda label:k(*[dict(I=I,X=X,Y=Y,Z=Z)[c] for c in label])
h=-p('XIX')-p('IXI')+p('XXI')*p('ZZI')+p('IIX')*p('ZZI')
Ds=[p(t) for t in ['ZII','IZI','IIZ','ZZZ']]
# Protected Z,X and two commuting internal Pauli pairs.
Pz=p('XXI');Px=p('YIY');Az=p('IIY');Ax=p('XIX');Bz=p('IXI');Bx=p('YYY')
project=(s.eye(8)+Pz)*(s.eye(8)+Az)*(s.eye(8)+Bz)/8
w=project[:,0];w=s.simplify(w/s.sqrt((w.conjugate().T*w)[0]))
W=s.Matrix.hstack(*[Px**i*Ax**j*Bx**l*w for i,j,l in itertools.product(range(2),repeat=3)])
assert s.simplify(W.conjugate().T*W)==s.eye(8)
h4=-k(I,Z)-k(X,I)-k(Y,Y)-k(Z,X)
assert s.simplify(W.conjugate().T*h*W)==k(I,h4)
labels=['YZZ','XIY','ZYZ','IXY'];signs=[1,1,-1,-1]
for d,label,sign in zip(Ds,labels,signs):assert s.simplify(W.conjugate().T*d*W)==sign*p(label)
# Unique internal ground projector, no numerical state selector.
ground=s.simplify(h4*(h4-2*s.sqrt(2)*s.eye(4))/16)
assert ground**2==ground and s.trace(ground)==1
Bs=[k(Z,Z),k(I,Y),k(Y,Z),k(X,Y)]
for b in Bs:assert s.simplify(s.trace(ground*b))==0
# All four vertices connect the ground exclusively to zero-energy internal states.
for b in Bs:assert s.simplify(h4*b*ground)==s.zeros(4)
# Every virtual two-rung denominator is 4sqrt2. Derive protected interaction.
As=[Y,X,-Z,-I]
K=s.zeros(4)
for a,b in itertools.product(range(4),repeat=2):
 overlap=s.simplify(s.trace(ground*Bs[a]*Bs[b]))
 K-=overlap**2*k(As[a]*As[b],As[a]*As[b])/(4*s.sqrt(2))
K=s.simplify(K)
coeff={a+b:str(s.simplify(s.trace(k(A,B)*K)/4)) for a,A in zip('IXYZ',[I,X,Y,Z]) for b,B in zip('IXYZ',[I,X,Y,Z]) if s.simplify(s.trace(k(A,B)*K))!=0}
r=dict(exact_unitary=True,internal_hamiltonian='-IZ-XI-YY-ZX',native_vertices=[str(sign)+'*'+label for sign,label in zip(signs,labels)],internal_spectrum=['-2sqrt2','0','0','2sqrt2'],all_internal_ground_vertex_means_zero=True,all_ground_vertex_transitions_at_gap='2sqrt2',second_order_protected_coefficients=coeff,scope='Exact coordinate change in specified positive physical rung parity; no new qubits or interactions. Low-band projection still requires weak coupling; full factorization is exact at any coupling.')
(P/'neutral_exact_internal_factor.json').write_text(json.dumps(r,indent=2)+'\n');print(r)
