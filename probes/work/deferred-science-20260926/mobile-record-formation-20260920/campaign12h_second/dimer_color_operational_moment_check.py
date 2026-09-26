#!/usr/bin/env python3
"""Author symbolic color-covariance and finite-qubit moment-map controls."""
from pathlib import Path
import datetime,hashlib,itertools,json
import sympy as s

HERE=Path(__file__).resolve().parent

def rotations():
 out=[]
 for p in itertools.permutations(range(3)):
  for signs in itertools.product([-1,1],repeat=3):
   R=s.zeros(3)
   for i in range(3):R[i,p[i]]=signs[i]
   if R.det()==1:out.append(R)
 assert len(out)==24
 return out

def symmetry_moments():
 x,y,z=s.symbols('x y z',real=True);n=s.Matrix([x,y,z])
 f=s.Matrix([y*z*(y*y-z*z),z*x*(z*z-x*x),x*y*(x*x-y*y)])
 group=rotations()
 for R in group:
  rn=R*n;transformed=f.subs(dict(zip([x,y,z],rn)),simultaneous=True)
  assert s.simplify(transformed-R*f)==s.zeros(3,1)
 a,b,c,d,e,h=s.symbols('a b c d e h',real=True)
 M=s.Matrix([[a,d,e],[d,b,h],[e,h,c]])
 variables=[a,b,c,d,e,h];results=[]
 for label,name in [(s.Matrix([1,0,0]),'A_axis'),(s.ones(3,1),'B_corner')]:
  stabilizer=[R for R in group if R*label==label]
  equations=[v for R in stabilizer for v in R*M*R.T-M]
  sol=s.linsolve(equations,variables);solution=next(iter(sol))
  fixed=M.subs(dict(zip(variables,solution)))
  opposite=[R for R in group if R*label==-label]
  assert all(s.simplify(R*fixed*R.T-fixed)==s.zeros(3) for R in opposite)
  results.append(dict(color=name,stabilizer_order=len(stabilizer),opposite_rotations=len(opposite),
    exact_invariant_symmetric_matrix=str(fixed),all_opposite_rotations_preserve_it=True))
 return dict(exact_quartic_covariance_rotations=24,stabilizer_solutions=results)

def pair_density():
 x,y,z=s.symbols('x y z',real=True);n=s.Matrix([x,y,z])
 sigmas=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
 singlet=s.Matrix([0,1,-1,0])/s.sqrt(2)
 B=s.Matrix.hstack(singlet,*[s.kronecker_product(a,s.eye(2))*singlet for a in sigmas])
 assert s.simplify(B.conjugate().T*B)==s.eye(4)
 P=(s.eye(2)+sum((v*a for v,a in zip(n,sigmas)),s.zeros(2)))/2
 direct=s.kronecker_product(P,s.eye(2)-P)
 q=s.Matrix([1,x,y,z]);moment=B*q*q.T*B.conjugate().T/2
 remainder=[]
 for entry in direct-moment:
  numerator=s.expand(entry*4)
  # Exact reduction by the single unit-vector polynomial; real/imaginary
  # parts use a rational polynomial coefficient field.
  for part in [s.re(numerator).expand(complex=True),s.im(numerator).expand(complex=True)]:
   residue=s.reduced(part,[x*x+y*y+z*z-1],x,y,z)[1]
   assert s.expand(residue)==0
 eps=s.symbols('epsilon',real=True);M=s.MatrixSymbol('M',3,3)
 # Rational positive-definite moments and unit directions verify the tilted
 # Schur complement explicitly, separately from the all-open-patch proof.
 controls=[]
 for moments in [s.diag(s.Rational(1,2),s.Rational(1,3),s.Rational(1,6)),
                 s.Matrix([[s.Rational(1,3),s.Rational(1,12),0],[s.Rational(1,12),s.Rational(1,3),0],[0,0,s.Rational(1,3)]])]:
  for axis in range(3):
   for tilt in [s.Rational(-3,4),s.Rational(1,3)]:
    mu=tilt*moments*s.eye(3)[:,axis]
    rho=s.Matrix.vstack(s.Matrix.hstack(s.ones(1),mu.T),s.Matrix.hstack(mu,moments))/2
    even=s.diag(s.Rational(1,2),s.Rational(1,2),s.Rational(1,2),s.Rational(1,2))
    rho0=s.diag(1,1,1,1)/2;rho0[1:4,1:4]=moments/2
    _,D=rho.LDLdecomposition(hermitian=False);assert all(v>0 for v in D.diagonal())
    defect=(1+abs(tilt))*rho0-rho
    assert all(v.is_nonnegative for v in defect.eigenvals())
    controls.append(dict(axis=axis,tilt=str(tilt),exact_positive_LDL_pivots=list(map(str,D.diagonal())),
      tilted_operator_domination=True))
 return dict(Bell_basis_orthonormal=True,projector_formula_mod_unit_sphere_exact=True,tilted_moment_controls=controls)

def kernel_controls():
 a,c=s.symbols('a c',real=True);Ms=[];features=[];labels=[]
 for axis in range(3):
  for sign in [-1,1]:
   v=s.eye(3)[:,axis]*sign
   Ms.append((1-a)*s.eye(3)/2+(3*a-1)*v*v.T/2)
   features.append(s.Matrix.vstack(v,s.zeros(3,1)));labels.append(tuple(v))
 for signs in itertools.product([-1,1],repeat=3):
  v=s.Matrix(signs);Ms.append((s.Rational(1,3)-c)*s.eye(3)+c*v*v.T)
  features.append(s.Matrix.vstack(s.zeros(3,1),v));labels.append(tuple(v))
 # A and B are disjoint label families even if their coordinate tuples agree.
 opposite={}
 for i in range(14):
  family=range(6) if i<6 else range(6,14)
  opposite[i]=next(j for j in family if labels[j]==tuple(-x for x in labels[i]))
  assert Ms[i]==Ms[opposite[i]]
 selected=[i for i in range(14) if i<opposite[i]]
 V=s.Matrix.hstack(*[s.eye(14)[:,i]-s.eye(14)[:,opposite[i]] for i in selected])
 T=s.Matrix.hstack(*[s.Matrix([M[0,0],M[1,1],M[2,2],M[0,1],M[0,2],M[1,2]]) for M in Ms])
 F=s.Matrix.hstack(*features)
 assert V.rank()==7 and T*V==s.zeros(6,7) and (F*V).rank()==6
 assert all(s.trace(M)==1 for M in Ms)
 # Fixed interior moment values make the full tangent rank five explicit.
 numeric=T.subs({a:s.Rational(1,2),c:s.Rational(1,12)})
 tangent=s.Matrix.hstack(*[s.eye(14)[:,i]-s.eye(14)[:,13] for i in range(13)])
 assert (numeric*tangent).rank()==5
 return dict(opposite_pairs=[(i,opposite[i]) for i in selected],odd_tangent_rank=7,
   exact_moment_image_of_odd_tangent_zero=True,vector_feature_rank_on_kernel=6,
   finite_interior_moment_tangent_rank=5,equal_prior_even_discrimination_bound='1/7',
   scope='Interior moment values test only the algebraic rank bound; they are not estimates of actual spherical region moments.')

def main():
 out=HERE/'dimer_color_operational_moment_checks';out.mkdir(exist_ok=False)
 groups=[]
 for name,fn in [('cubic_stabilizers',symmetry_moments),('pair_quantum_density',pair_density),('wave_population_kernel',kernel_controls)]:
  value=fn();groups.append(dict(group=name,passed=True,detail=value));print(name,'PASS',flush=True)
 sources={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in [Path(__file__).name,'DIMER_COLOR_OPERATIONAL_MOMENT_MAP.md','DIMER_ROUTED_RECORD_TRANSPORT.md']}
 result=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),sources_sha256=sources,groups=groups,
  scope='Exact symbolic controls conditional on ordinary single-pair quantum-state/Born readout. No alternate ontology or encoding excluded; no stochastic-wave theorem changed.')
 (out/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':main()
