#!/usr/bin/env python3
"""Finite author controls for the written leakage proof; not an index proof."""
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = [
    "docs/DETECTOR_INDEX_LEAKAGE_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/COMPACT_PATCH_SCATTERING_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-10-11.md",
    "docs/COMPACT_PATCH_FOCK_ISOMETRY_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/COMPACT_DETECTOR_CONVERGENCE_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/DETECTOR_SCATTERING_PROJECTION_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/APPROXIMATE_PARTIAL_FACTOR_INDEX_BOUNDED_THEOREM_NOTE_2026-10-11.md"
]
if not __debug__:
    raise RuntimeError("Run without -O: exact control assertions must be enabled")

from fractions import Fraction as F
from itertools import product
import json
import math

DEFECT_DENOMINATOR = 4
FIRST_IDENTITY_TERM = 1
SECOND_IDENTITY_TERM = 1
ENERGY_FACTOR = 2
TAIL_COEFFICIENT = 1
RESOLVENT_SIGN = 1

def emit(name, **data):
    print(json.dumps({"control": name, **data}, sort_keys=True))

def mat(rows):
    return [[F(x) for x in row] for row in rows]

def diag(xs):
    return mat([[x if i == j else 0 for j in range(len(xs))] for i, x in enumerate(xs)])

def eye(n):
    return diag([1] * n)

def add(a, b):
    return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]

def scale(c, a):
    return [[c*x for x in ar] for ar in a]

def sub(a, b):
    return add(a, scale(-1,b))

def mul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def vec(a, v):
    return [sum(x*y for x,y in zip(ar,v)) for ar in a]

def vadd(a, b):
    return [x+y for x,y in zip(a,b)]

def vscale(c, a):
    return [c*x for x in a]

def norm2(v):
    return sum(x*x for x in v)

def outer(v, w):
    return [[x*y for y in w] for x in v]

def inv2(a):
    den=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    assert den != 0
    return scale(1/den, [[a[1][1],-a[0][1]],[-a[1][0],a[0][0]]])

def control_projection():
    count=0
    for signs_tail in product((-1,1),repeat=3):
        signs=(1,)+signs_tail
        for selected_tail in product((0,1),repeat=3):
            selected=(1,)+selected_tail
            if any(p and u != 1 for p,u in zip(selected,signs)):
                continue
            for psi in product((-1,0,2),repeat=4):
                defect=sum((u-1)**2*x*x for u,x in zip(signs,psi))
                leakage=sum((1-p)*x*x for p,x in zip(selected,psi))
                assert F(defect,DEFECT_DENOMINATOR) <= leakage, "defect coefficient invalid"
                count+=1
    # Saturation on a line where U=-1.
    assert F(4,DEFECT_DENOMINATOR) <= 1, "sharp line rejects stronger coefficient"
    emit("abstract projection inequality", exact_cases=count, sharp_defect_squared=4,
         sharp_complement_squared=1, scope="real diagonal unitary controls only")

def control_identity():
    omega=[F(1),F(0),F(0)]
    a=mat([[0,0,0],[0,0,1],[0,0,0]])
    b=mat([[0,0,0],[0,0,0],[1,0,0]])
    for signs,necessary in [((1,1,-1),"second"),((1,-1,1),"first")]:
        u=diag(signs); ident=eye(3)
        delta=sub(mul(mul(u,a),u),a)
        left=vec(mul(delta,b),omega)
        term1=vec(mul(sub(u,ident),mul(a,b)),omega)
        term2=vec(mul(mul(u,a),mul(sub(u,ident),b)),omega)
        right=vadd(vscale(FIRST_IDENTITY_TERM,term1),vscale(SECOND_IDENTITY_TERM,term2))
        assert left==right, f"ordered A,B identity requires {necessary} term"
        assert norm2(vec(delta,omega))==0
        assert norm2(left)==4
        projection=diag([1,1 if signs[1]==1 else 0,1 if signs[2]==1 else 0])
        comp=sub(ident,projection)
        lb=norm2(vec(mul(comp,b),omega))
        lab=norm2(vec(mul(comp,mul(a,b)),omega))
        assert lab+lb >= F(norm2(left),8)
        assert max(lb,lab) >= F(norm2(left),16)
    emit("cyclic witness and ordered identity", examples=2,
         operator_defect=2, vacuum_defect=0, revealed_defect=2,
         scope="faithful M3 representation; no local lattice realization claimed")

def control_energy():
    energies=(0,2,5,9); signs=(1,-1,1,-1); q=(0,1,0,1)
    count=0
    for psi in product((-2,0,1),repeat=4):
        h2=sum(e*e*x*x for e,x in zip(energies,psi))
        d2=sum((u-1)**2*x*x for u,x in zip(signs,psi))
        for cutoff in (2,3,5,8,9,12,100):
            w2=sum(qi*x*x for e,qi,x in zip(energies,q,psi) if 2 <= e <= cutoff)
            rhs=max(F(d2,4)-TAIL_COEFFICIENT*F(h2,cutoff**2),F(0))
            assert w2 >= rhs, "cutoff inequality needs high-energy subtraction"
            de2=sum((u-1)**2*x*x for e,u,x in zip(energies,signs,psi) if 2 <= e <= cutoff)
            tail2=sum((u-1)**2*x*x for e,u,x in zip(energies,signs,psi) if e > cutoff)
            assert de2+tail2==d2
            count+=1
    # One on-site interaction h=diag(-J,J); ground GNS generator H=h+J.
    current_j=F(3,2)
    physical_h=diag([0,2*current_j])
    flip=mat([[0,1],[1,0]])
    omega=[F(1),F(0)]
    energy_norm_squared=norm2(vec(mul(physical_h,flip),omega))
    bound=ENERGY_FACTOR*current_j
    assert energy_norm_squared <= bound*bound, "local generator bound needs factor two"
    assert energy_norm_squared==4*current_j*current_j
    # Additional zero-energy vectors invalidate a positive-window inference.
    hz=diag([0,0]); uz=diag([1,-1]); excited=[F(0),F(1)]
    assert norm2(vec(hz,excited))==0
    assert norm2(vec(sub(uz,eye(2)),excited))==4
    emit("energy cutoff and local interaction normalization", exact_cases=count,
         onsite_J=str(current_j), onsite_energy_norm_squared=str(energy_norm_squared),
         extra_ground_space_counterexample=True,
         scope="finite spectral arithmetic; Stone/domain argument is written in note")

def control_detectors():
    e1=[F(0),F(1),F(0),F(0)]
    e2=[F(0),F(0),F(1),F(0)]
    e3=[F(0),F(0),F(0),F(1)]
    v2=vadd(e1,e2)
    q1=outer(e1,e1); q2=outer(v2,v2)
    k=add(scale(F(1,4),q1),scale(F(1,12),q2))
    assert norm2(vec(k,e3))==0
    block=[[k[i][j] for j in (1,2)] for i in (1,2)]
    assert block[0][0]>0
    assert block[0][0]*block[1][1]-block[0][1]*block[1][0]>0
    # Omitting q2 leaves a selected scattering direction in the kernel.
    assert norm2(vec(q1,e2))==0
    # Range in the scattering subspace is not enough without adjoint symmetry.
    nonselfadjoint=outer(e1,e3)
    assert norm2(vec(nonselfadjoint,e3))==1
    emit("positive detector kernels", nonorthogonal_generators=True,
         selected_missing_axis_for_incomplete_family=True,
         nonselfadjoint_range_shortcut_rejected=True,
         scope="finite rank-one sums; no detector convergence proof by numerics")

def control_resolvent():
    a=mat([[2,1],[1,2]]); b=mat([[1,0],[0,3]]); eta=F(1,3)
    ra=inv2(add(a,scale(eta,eye(2))))
    rb=inv2(add(b,scale(eta,eye(2))))
    lhs=scale(eta,sub(ra,rb))
    rhs=scale(RESOLVENT_SIGN*eta,mul(mul(ra,sub(b,a)),rb))
    assert lhs==rhs, "zero-resolvent identity has wrong sign or order"
    values=[]
    for t in (2,10,100):
        lambda_t=F(1,t*t); eta_t=F(1,t**4)
        wrong_joint=eta_t/(lambda_t+eta_t)
        assert wrong_joint==F(1,t*t+1)
        values.append(str(wrong_joint))
    emit("ordered zero-atom resolvents", exact_noncommuting_identity=True,
         joint_sequence_second_coordinate=values,
         time_first_then_eta_limit_second_coordinate=1,
         joint_limit_second_coordinate=0,
         scope="explicit diagonal counterexample and finite noncommuting identity")

def control_tube_resources():
    # Illustrative admissible constants in P21, not fitted microscopic couplings.
    spatial_d=3; q=1; width=10**6; mu=1.; nu=.5; a_tail=1.; e_bd=1.
    cq=435*(25*97**4*385**3)
    j=math.ceil(math.log(3456*cq*a_tail*width**(spatial_d+3))/mu)
    radius=math.ceil(math.log(8*e_bd*j*width**(spatial_d+3))/nu)
    assert 1 <= radius < width/2
    volume=width**(spatial_d-1)
    boundary=volume-(width-2*radius)**(spatial_d-1)
    kappa=min(.5,abs(q)/(16*math.sqrt(2)*j))
    error=4*e_bd*j*volume*math.exp(-nu*radius)
    approx=4*cq*a_tail*volume*math.exp(-mu*j)
    def g(x):
        return (1+x)*math.log1p(x)-x*math.log(x)
    index_rhs=2*j*boundary/volume+8*j*kappa/math.sqrt(2)+3*g(kappa/math.sqrt(2))/(volume*math.log(2))
    assert error <= .5*width**-4*(1+1e-12)
    assert approx <= width**-4/864*(1+1e-12)
    assert index_rhs < abs(q)
    assert kappa-error-approx > 0
    emit("tube resource arithmetic", dimension=spatial_d, width=width, j=j, R=radius,
         normalized_index_rhs=index_rhs, defect_threshold=kappa-error-approx,
         scope="floating arithmetic on explicit inequalities; no matrix of supersite dimension built")

def main():
    control_projection()
    control_identity()
    control_energy()
    control_detectors()
    control_resolvent()
    control_tube_resources()
    print("per_element: exact finite vector inequalities and cyclic-witness identities executed; infinite-dimensional proof remains in the note.")
    print("per_site: exact one-site interaction normalization executed; this does not model the full supplied Poincare/current setting.")
    print("per_mode: checked and not executed — no continuous-momentum particle or all-mode detector completeness assertion is tested here.")
    print("per_block: full-block tube resource arithmetic executed without constructing its exponentially large algebra; its theorem is analytic.")
    print("lattice_wide: checked and not executed — infinite-qubit index and detector limits use matched written sources, not finite controls.")
    emit("completion", outcome="all finite controls satisfied", evidence_role="author controls, not independent review")

if __name__ == "__main__":
    main()

print("TOTAL: PASS=6 FAIL=0")
print("SCOPE: Six original finite control groups; no physical realization, effective preparer or all-channel completeness.")
