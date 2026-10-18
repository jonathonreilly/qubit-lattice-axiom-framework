"""Exact aligned-band commutants, separating planes and scalar square symmetry."""
from pathlib import Path
import sympy as s,json,itertools
P=Path(__file__).resolve().parent
states=[b for b in range(16) if b.bit_count()%2==0];lookup={b:i for i,b in enumerate(states)}
def flip(a,b,L,is_y=False):
 M=s.zeros(8)
 for j,q in enumerate(states):
  phase=(-(-1)**(((q>>a)&1)+((q>>b)&1)))**L if is_y else 1
  M[lookup[q^(1<<a)^(1<<b)],j]=phase
 return M
def centralizer(gens):
 M=s.Matrix.vstack(*[s.kronecker_product(s.eye(8),g)-s.kronecker_product(g.T,s.eye(8)) for g in gens])
 # Sympy reshape is row-major, so transpose the column-vectorized result.
 return [v.reshape(8,8).T for v in M.nullspace()]
rows=[]
for L in [3,4]:
 planes=[flip(0,1,L),flip(2,3,L),flip(0,2,L,True),flip(1,3,L,True)]
 S=s.zeros(8)
 for j,q in enumerate(states):
  dest=sum(((q>>i)&1)<<[1,3,0,2][i] for i in range(4));S[lookup[dest],j]=(-1 if q in [0,15] else 1)**L
 C=centralizer(planes);CS=centralizer(planes+[S]);comm=lambda basis:all(a*b==b*a for a,b in itertools.combinations(basis,2))
 assert len(C)==8 and comm(C)==(L%2==0)
 assert len(CS)==4 and comm(CS)
 T=flip(0,2,L)+flip(1,3,L)+flip(0,1,L,True)+flip(2,3,L,True)
 assert all(T*g==g*T for g in planes+[S])
 rows.append(dict(L=L,plane_commutant_dimension=len(C),plane_commutant_commutative=comm(C),square_plane_commutant_dimension=len(CS),square_plane_commutant_commutative=True,T_spectrum={str(e):m for e,m in T.eigenvals().items()}))
(P/'neutral_strong_symmetry.json').write_text(json.dumps(dict(rows=rows,scope='Aligned8state positive-rung band. Representation multiplicities survive isolated equivariant continuation; square-invariant plane-neutral readouts have no intraband inelastic response. No claim band stays isolated at equal coupling.'),indent=2)+'\n');print(rows)
