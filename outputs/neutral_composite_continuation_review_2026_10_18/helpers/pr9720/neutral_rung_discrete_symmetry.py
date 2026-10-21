"""Exact native discrete quarter rotation of collective low-rung axes."""
from pathlib import Path
P=Path(__file__).resolve().parent
import sympy as s,json
from neutral_rung_model import h,Ds,xs,zs
hh=s.Matrix(h.astype(int));dd=[s.Matrix(d.astype(int)) for d in Ds];S=s.zeros(8)
for b in range(8):
 bits=[(b>>(2-j))&1 for j in range(3)];bits+=[sum(bits)%2];new=[0]*4
 for x in range(2):
  for y in range(2):new[2*y+(1-x)]=bits[2*x+y]
 row=sum(new[j]<<(2-j) for j in range(3));S[row,b]=-1 if sum(bits) in (0,4) else 1
Px=s.Matrix((xs[0]@xs[1]).astype(int));T=Px*S
Py=s.Matrix((-xs[0]@xs[2]@zs[0]@zs[2]).astype(int))
assert Px*Py==-Py*Px and Py*Py==s.eye(8)
assert Py*hh==hh*Py
for d in dd:
 assert Py*d*Py in [d,-d]
assert hh*T==T*hh and T.T*T==s.eye(8)
Daction=s.Matrix([[(d*T*e*T.T).trace()/8 for e in dd] for d in dd]);assert Daction.T*Daction==s.eye(4)
cols=[]
for e,m,vs in sorted(hh.eigenvects(),key=lambda v:float(v[0])):cols+=s.GramSchmidt(vs,orthonormal=False)
B=s.Matrix.hstack(*cols);Bi=B.inv();tl=(Bi*T*B)[:2,:2]
t1=s.simplify(s.sqrt(2)*(Bi*dd[0]*dd[1]*B)[:2,:2]);t2=s.simplify(s.sqrt(2)*(Bi*dd[0]*dd[2]*B)[:2,:2]);t3=s.simplify(-s.I*t1*t2)
# Non-normalized exact coordinates: inverse, not transpose, implements adjoint action.
assert s.simplify(tl*t1*tl.inv()+t2)==s.zeros(2)
assert s.simplify(tl*t2*tl.inv()-t1)==s.zeros(2)
assert s.simplify(tl*t3*tl.inv()-t3)==s.zeros(2)
assert s.simplify(tl**4)==-s.eye(2)
assert s.simplify(Px*hh-hh*Px)==s.zeros(8)
result=dict(projective_Px_Py='anticommute exactly, square to identity, preserve full rung h and global interrung bonds',D_signed_permutation=str(Daction),low_T=str(tl),low_adjoint_action=['tau1 -> -tau2','tau2 -> tau1','tau3 -> tau3'],charge_selection='Delta Q0 multiple8, equivalently four collective flips; exact global discrete symmetry',scope='Finite positive-parity tube; no continuous microscopic symmetry or bulk criticality assertion')
(P/'neutral_rung_discrete_symmetry.json').write_text(json.dumps(result,indent=2)+'\n')
print(result)
