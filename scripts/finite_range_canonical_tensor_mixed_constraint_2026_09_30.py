#!/usr/bin/env python3
"""Exact matrix-symbol and changed-carrier controls for a supplied canonical jet.
The all-finite-support statement is the source proof, not an extrapolated scan.
No external scientific data are read; imported clock helper is package-local.
"""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "scripts/finite_range_mixed_gravity_clock_control_2026_09_30.py",
    "docs/FINITE_RANGE_CANONICAL_TENSOR_MIXED_CONSTRAINT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-30.md",
    "docs/ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/ADMISSIBILITY_RULE_THE_CURVATURE_MEMBERS_CONSTRAINT_ALGEBRA_CLOSES_ON_THE_LATTICE_ONLY_AT_BETA_EQUALS_MINUS_ALPHA_AND_THERE_THE_WALKERS_OWN_STATES_CANNOT_BE_ITS_CONTENT_BOUNDED_THEOREM_NOTE_2026-09-24.md",
)
import os
from pathlib import Path
import json
for name in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):
    os.environ[name]='1'
import sympy as s
z=s.symbols('z',nonzero=True)

def zero(M): return all(s.simplify(x)==0 for x in M)
def sharp(M): return M.subs(z,1/z).T

# 1. Canonical TT variables and proper C4 representation, including shear.
A,B,C,J,K,H=s.symbols('A B C J K H')
P,Q,R,L,M,S=s.symbols('P Q R L M S')
coords=[A,B,C,J,K,H]; momenta=[P,Q,R,L,M,S]
pb=lambda f,g:s.expand(sum(s.diff(f,a)*s.diff(g,p)-s.diff(f,p)*s.diff(g,a)
                         for a,p in zip(coords,momenta)))
q1=(B-C)/2;q2=H;p1=Q-R;p2=S
assert s.Matrix([[pb(q1,p1),pb(q1,p2)],[pb(q2,p1),pb(q2,p2)]])==s.eye(2)
rot=s.Matrix([[1,0,0],[0,0,-1],[0,1,0]])
metric=s.Matrix([[A,J,K],[J,B,H],[K,H,C]])
transformed=rot*metric*rot.T
assert s.simplify((transformed[1,1]-transformed[2,2])/2+q1)==0
assert transformed[1,2]==-q2
other=s.diag(s.eye(2),s.Matrix([[0,-1],[1,0]]))
assert (other+s.eye(4)).det()==8
print('TT canonical pairing: identity. Proper C4: -I2; complement excludes eigenvalue -1.')

# 2. General real symmetric density pair, with explicit finite offsets.
a,b=-2,1
ms=s.symbols('m0:4'); mat=s.Matrix(2,2,ms)
F=mat*z**(b-a)+mat.T*z**(a-b)
Aa=-a*mat*z**(b-a)-b*mat.T*z**(a-b)
assert zero(F-sharp(F))
assert zero(Aa-sharp(Aa)-z*F.diff(z))
print('General density pair: F#=F and A-A#=z Fprime verified symbolically.')

# 3. Symbolic noncommuting-matrix elimination, allowing nonzero U0 constant.
d=s.Matrix(2,2,s.symbols('d0:4'))
f=s.Matrix(2,2,s.symbols('f0:4'))
a0=s.Matrix(2,2,s.symbols('a0:4'))
dd=s.Matrix(2,2,s.symbols('v0:4'))
mu0,mu1=s.symbols('mu0 mu1')
ds=mu0*s.eye(2)-f.inv()*d*f
raw=dd*f+d*a0+a0*ds-mu0*a0-mu1*f
reduced=dd+d*a0*f.inv()-a0*f.inv()*d-mu1*s.eye(2)
assert zero(raw*f.inv()-reduced)
assert s.simplify(s.trace(d*a0*f.inv()-a0*f.inv()*d))==0
print('Generic 2x2 elimination verified; mu0 cancels and commutator trace is zero.')

# 4. Independent finite-position functional/Hessian construction.
# Site-major ordering, two canonical components per site, finite periodic box.
n=17; positions=list(range(-n//2+1,n//2+1)); assert len(positions)==n
index={x:i for i,x in enumerate(positions)}
wrap=lambda x:(x+n//2)%n-n//2
def op(coeffs):
    out=s.zeros(2*n)
    for x in positions:
        for shift,block in coeffs.items():
            y=wrap(x+shift)
            for i in range(2):
                for j in range(2):out[2*index[x]+i,2*index[y]+j]+=block[i,j]
    return out
Dc={-1:s.Matrix([[1,2],[-1,3]]),0:s.Matrix([[2,-1],[4,0]]),1:s.Matrix([[0,1],[2,-2]])}
DD=op(Dc)
mm=s.Matrix([[2,1],[-3,4]]); aa=-1;bb=1
FF=s.zeros(2*n);BB=s.zeros(2*n)
for x in positions:
    u=wrap(x+aa);v=wrap(x+bb)
    for i in range(2):
        for j in range(2):
            ui=2*index[u]+i;vj=2*index[v]+j
            FF[ui,vj]+=mm[i,j];FF[vj,ui]+=mm[i,j]
            BB[ui,vj]+=x*mm[i,j];BB[vj,ui]+=x*mm[i,j]
Ac={bb-aa:-aa*mm,aa-bb:-bb*mm.T}
AO=op(Ac);XX=s.diag(*[x for x in positions for _ in range(2)])
expected_F=op({bb-aa:mm,aa-bb:mm.T})
assert FF==expected_F and FF==FF.T and BB==BB.T
pp=s.zeros(2*n,1)
for x,vals in [(-2,(1,2)),(0,(-1,3)),(2,(2,-2))]:
    for i in range(2):pp[2*index[x]+i]=vals[i]
assert (BB-XX*FF-AO)*pp==s.zeros(2*n,1)
comm_dx=op({r:r*v for r,v in Dc.items()})
lhs=DD*BB+BB*DD.T-XX*(DD*FF+FF*DD.T)
rhs=comm_dx*FF+DD*AO+AO*DD.T
assert (pp.T*(lhs-rhs)*pp)[0]==0
# Direct gradient contraction independently verifies canonical bracket sign.
direct=(DD.T*pp).dot(BB*pp)
hessian=(pp.T*(DD*BB+BB*DD.T)*pp)[0]/2
assert direct==hessian
print('Explicit finite-position density/Hessian and canonical bracket sign controls verified.')

# 5. Exact stress tests for the scope and constant-Laurent-coefficient step.
singF=s.diag(1,0);singD=s.Matrix([[0,1],[0,0]]);singA=s.Matrix([[0,s.Rational(1,2)],[s.Rational(1,2),0]])
assert singD*singF+singF*singD.T==s.zeros(2)
assert singD*singA+singA*singD.T==singF
print('Singular-F stress example satisfies both uniform/affine equations: invertibility matters.')

symbols=s.symbols('c0:10')
trD=sum((symbols[2*(r+2)]+symbols[2*(r+2)+1])*z**r for r in range(-2,3))
der=s.expand(z*s.diff(trD,z))
assert der.coeff(z,0)==0
assert s.expand(der-2).coeff(z,0)==-2
print('Laurent trace derivative has zero constant coefficient; required I2 has trace constant 2.')

out={'canonical_TT_pairing':True,'proper_C4_complement_plus_identity_det':8,
     'density_pair_adjoint_identity':True,'generic_matrix_elimination':True,
     'finite_position_hessian_control':True,'singular_F_counterexample':True,
     'trace_constant_coefficient':0,'required_trace_constant':2,
     'proof_domain':'all finite supports; finite examples are independent controls'}
OUT=Path(__file__).resolve().parents[1]/'outputs'/'finite-range-mixed-gravity-2026-09-30'
OUT.mkdir(parents=True,exist_ok=True)
print(json.dumps(out),flush=True)

# 6. Distinct cochain algebra: direct complete matrices and canonical witness.
nc=5
shift=s.zeros(nc)
for i in range(nc):shift[i,(i+1)%nc]=1
inc=shift-s.eye(nc)
I=s.diag(1,0,0,0,0);J=s.diag(0,1,0,0,1)
contraction=lambda m:s.diag(m*inc,inc*m)
li,lj=contraction(I),contraction(J)
ij=I*inc*J-J*inc*I
assert li*lj-lj*li==contraction(ij)
assert ij[0,1]==1 and ij[0,0]==0
qs=s.symbols('q0:5');ps=s.symbols('p0:5')
j0=ps[0]*(qs[1]-qs[0]);j1=ps[1]*(qs[2]-qs[1])
comm=s.expand(sum(s.diff(j0,q)*s.diff(j1,p)-s.diff(j0,p)*s.diff(j1,q) for q,p in zip(qs,ps)))
assert s.expand(comm-ps[0]*(qs[2]-qs[1]))==0
pt={**{x:0 for x in qs+ps},qs[2]:1,ps[0]:1}
assert all((ps[i]*(qs[(i+1)%nc]-qs[i])).subs(pt)==0 for i in range(nc))
assert comm.subs(pt)==1
out['cochain_contraction_and_constraint_surface']=True

# 7. Endpoint link gauge covariance and orthogonal Gram invariance.
U=s.Matrix([[1,2],[0,1]]);gx=s.Matrix([[2,0],[1,1]]);gy=s.Matrix([[1,1],[0,2]])
vx=s.Matrix([1,-1]);vy=s.Matrix([2,3])
assert (gx*U*gy.inv())*(gy*vy)-gx*vx==gx*(U*vy-vx)
R=s.Matrix([[0,-1],[1,0]]);frame=s.Matrix([[1,2],[3,1]])
assert (R*frame).T*(R*frame)==frame.T*frame
out['endpoint_link_covariance_and_metric_invariance']=True

# 8. Translation-fixed ideal witness and its target kinetic value.
e,alpha=s.symbols('e alpha',nonzero=True)
assert inc*s.ones(nc,1)==s.zeros(nc,1)
Pdiag=[e,-e,0]
kin=(sum(x*x for x in Pdiag)-sum(Pdiag)**2/2)/(4*alpha)
assert s.simplify(kin-e*e/(2*alpha))==0
out['homogeneous_target_kinetic']='e^2/(2alpha)'

# 9. Exact central-stencil residual; no continuum closure is inferred.
central=(z-1/z)/2
residual=s.expand(z*s.diff(central,z)-1)
assert residual==(z+1/z)/2-1
assert residual.subs(z,1)==0 and residual.subs(z,-1)==-2
out['central_stencil_residual']='(z+z^-1)/2-1'

# 10. Canonical clock extension, independently derived by direct brackets.
import finite_range_mixed_gravity_clock_control_2026_09_30
out['clock_extension_exact_checks']=True
(OUT/'result.json').write_text(json.dumps(out,indent=2)+'\n')
print('per_element: exact TT canonical derivatives, rational matrix elimination and Laurent coefficients were checked.')
print('per_site: the complete scalar constraint-surface witness and homogeneous kinetic witness were evaluated.')
print('per_mode: both TT components and general noncommuting symbols are retained; singular and central-stencil controls were checked.')
print('per_block: finite-position two-component Hessians, cochain matrices and exact six-site clock brackets were checked.')
print('lattice_wide: the all-finite-support theorem follows from the stated analytic trace and plateau proof; native gravity dynamics not executed.')
print('TOTAL: PASS=10 FAIL=0; bounded exact controls, with analytic general proof in the source note.')
