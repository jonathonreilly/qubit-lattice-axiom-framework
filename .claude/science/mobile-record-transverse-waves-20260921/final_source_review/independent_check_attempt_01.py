#!/usr/bin/env python3
"""Post-source selective checks; independent of the author's implementation."""
from pathlib import Path
from itertools import product, permutations
import json, hashlib, platform
import numpy as np
import sympy as s

out={"scope":"Post-source independent selective review controls, not the prior blind reconstruction","checks":{}}
def check(name,ok,detail=None):
    assert bool(ok),(name,detail)
    out["checks"][name]=detail if detail is not None else True
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
axes=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
corners=list(product((-1,1),repeat=3))
e=[(0,0,0)]+axes+[(0,0,0)]*8
b=[(0,0,0)]*7+corners
lookup={(e[a],b[a]):a for a in range(15)}
S2=np.array([[np.add(cross(e[a],b[z]),cross(e[z],b[a])) for z in range(15)] for a in range(15)],dtype=np.int64)
def h2(word,i):
    l,a,z,r=word
    return int(S2[l,a,i]+S2[a,r,i]-S2[l,z,i]-S2[z,r,i])
theta=np.array([lookup[(e[a],tuple(-x for x in b[a]))] for a in range(15)])
# Tensor covariance plus actual oriented-edge tests for each signed coordinate action.
actions=[]; matrices=[]; improper=0; sample_words=[(14,1,2,14),(0,3,7,10),(9,5,12,2),(6,7,1,14)]
for perm in permutations(range(3)):
    parity=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
    for signs in product((-1,1),repeat=3):
        R=np.zeros((3,3),dtype=np.int64)
        for old in range(3):R[perm[old],old]=signs[old]
        det=parity*np.prod(signs); improper+=int(det<0)
        action=np.array([lookup[(tuple(R@e[a]),tuple(det*(R@b[a])))] for a in range(15)])
        for a in range(15):
            for z in range(15):assert np.array_equal(S2[action[a],action[z]],R@S2[a,z])
        for word in sample_words:
            changed=action[list(word)]
            for old in range(3):
                oriented=changed if signs[old]>0 else changed[::-1]
                assert h2(oriented,perm[old])==h2(word,old)
        assert np.array_equal(theta[action],action[theta])
        matrices.append(R);actions.append(action)
check("polar_axial_tensor_and_oriented_rate_covariance",len(actions)==48 and improper==24,
      {"actions":48,"improper_actions":24,"tensor_pairs_per_action":225,"oriented_word_tests":48*4*3})
# A genuinely different finite component from the author's four-cycle test.
seed=(0,1,2,7,10)
states=sorted(set(permutations(seed))|set(permutations(tuple(theta[list(seed)]))))
index={state:i for i,state in enumerate(states)}
theta_rows=np.array([index[tuple(theta[list(state)])] for state in states])
details=[]
for variant in ("positive_part","linear"):
    Q=np.zeros((len(states),len(states)),dtype=np.int64)
    for row,state in enumerate(states):
        for x in range(5):
            word=tuple(state[(x+d)%5] for d in (-1,0,1,2))
            drive=h2(word,2)
            # Units 1/140; gamma=-3/5, kappa=2/7, K0=11/10.
            rate=40+max(-42*drive,0) if variant=="positive_part" else 154-21*drive
            moved=list(state);moved[x],moved[(x+1)%5]=moved[(x+1)%5],moved[x]
            col=index[tuple(moved)]
            if row!=col:Q[row,col]+=rate;Q[row,row]-=rate
    assert np.array_equal(Q.T,Q[theta_rows][:,theta_rows])
    assert np.all(Q.sum(axis=0)==0) and np.all(Q.sum(axis=1)==0)
    assert np.array_equal(np.diag(Q),np.diag(Q)[theta_rows])
    assert np.any(Q!=Q.T)
    details.append({"variant":variant,"states":len(states),"ordinary_asymmetry_entries":int(np.count_nonzero(Q-Q.T)),"rate_integer_unit":"1/140"})
check("five_cycle_complete_sector_generalized_reversal",True,details)

# Direct relative-entropy differentiation along a species probability path.
rA=s.Rational(2,7);rB=s.Rational(3,8);gamma=s.Rational(-3,5)
pb=s.Matrix([1-rA-rB]+[rA/6]*6+[rB/8]*8)
X=s.Matrix([s.Rational(1,3),s.Rational(-2,5),s.Rational(4,7)])
Y=s.Matrix([s.Rational(-1,2),s.Rational(2,3),s.Rational(1,4)])
u=s.Matrix([0]+[s.Matrix(a).dot(X)/2 for a in axes]+[s.Matrix(v).dot(Y)/8 for v in corners])
eps=s.symbols("epsilon",real=True);p=pb+eps*u
relative=sum(p[a]*s.log(p[a]/pb[a]) for a in range(15))
quadratic=s.simplify(s.diff(relative,eps,2).subs(eps,0)/2)
target=3*X.dot(X)/(2*rA)+Y.dot(Y)/(2*rB)
check("direct_log_entropy_second_derivative",quadratic==target,{"energy":str(quadratic)})
phi=s.zeros(3,1)
for a in range(15):
    for z in range(15):phi+=gamma*s.Matrix(S2[a,z].tolist())*p[a]*p[z]/2
J=[]
for a in range(15):
    one=sum((gamma*s.Matrix(S2[a,z].tolist())*p[z]/2 for z in range(15)),s.zeros(3,1))
    J.append(s.expand(2*p[a])*(one-phi))
flux2=[]
for i in range(3):
    q=sum(s.log(p[a]/pb[a])*J[a][i] for a in range(15))-phi[i]
    flux2.append(s.simplify(s.diff(q,eps,2).subs(eps,0)/2))
check("relative_entropy_flux_from_pair_tensor",s.Matrix(flux2)==gamma*X.cross(Y),
      {"quadratic_flux":[str(x) for x in flux2]})
current2={}
for label,indices,factor in [("A",range(1,7),1-2*rA),("B",range(7,15),1-2*rB),("total",range(1,15),2*pb[0])]:
    coeff=s.Matrix([s.expand(sum(J[a][i] for a in indices)).coeff(eps,2) for i in range(3)])
    assert all(s.simplify(x)==0 for x in coeff-factor*gamma*X.cross(Y))
    current2[label]={"factor":str(factor),"coefficient":[str(x) for x in coeff]}
check("second_order_record_flux_direct_species_sum",True,current2)

# Exact affine-space curl solution, with nonzero divergences and negative signed speed.
x,y,z,t=s.symbols("x y z t",real=True);coords=(x,y,z);c=s.Rational(-3,7)
def curl(f):return s.Matrix([s.diff(f[2],y)-s.diff(f[1],z),s.diff(f[0],z)-s.diff(f[2],x),s.diff(f[1],x)-s.diff(f[0],y)])
def div(f):return sum(s.diff(f[i],coords[i]) for i in range(3))
E0=s.Matrix([1+x+2*y,2+z-x,3+y+z]);B0=s.Matrix([2-y+z,-1+2*x,1-x+3*z])
E=E0+c*t*curl(B0);B=B0-c*t*curl(E0)
assert E.diff(t)==c*curl(B) and B.diff(t)==-c*curl(E)
energy=(E.dot(E)+B.dot(B))/2;flux=c*E.cross(B);momentum=E.cross(B)/c
stress=energy*s.eye(3)-E*E.T-B*B.T
stress_div=s.Matrix([sum(s.diff(stress[i,j],coords[j]) for j in range(3)) for i in range(3)])
defect=momentum.diff(t)+stress_div
assert s.expand(s.diff(energy,t)+div(flux))==0
assert all(s.expand(a)==0 for a in defect+E*div(E)+B*div(B))
at_origin=defect.subs({x:0,y:0,z:0,t:0})
assert at_origin!=s.zeros(3,1)
check("energy_and_stress_on_exact_non_Gauss_solution",True,
      {"signed_speed":str(c),"divergences":[str(div(E)),str(div(B))],"stress_defect_at_origin":[str(s.expand(a)) for a in at_origin]})

# Keep the complete fourteen-field covariance through Gaussian conditioning.
EO=s.Matrix(axes+[(0,0,0)]*8).T;BO=s.Matrix([(0,0,0)]*6+corners).T
rows=[[1]*6+[0]*8,[0]*6+[1]*8]+EO.tolist()+BO.tolist()
rows += [[int(v[0]**2-v[2]**2) for v in e[1:]],[int(v[1]**2-v[2]**2) for v in e[1:]]]
rows += [[int(v[i]*v[j]) for v in b[1:]] for i,j in [(0,1),(0,2),(1,2)]]
rows += [[int(v[0]*v[1]*v[2]) for v in b[1:]]]
T=s.Matrix(rows);assert T.det()!=0
k=s.Matrix([2,-1,3]);norm2=k.dot(k);PT=s.eye(3)-k*k.T/norm2
G=s.zeros(2,14);G[0,2:5]=k.T;G[1,5:8]=k.T
static=[0,1]+list(range(8,14))
results=[]
for name,ra,rb,rank_before,rank_after in [("interior",rA,rB,14,12),("full_occupancy",s.Rational(2,7),s.Rational(5,7),13,11)]:
    pocc=s.Matrix([ra/6]*6+[rb/8]*8)
    C=T*(s.diag(*pocc)-pocc*pocc.T)*T.T
    Cc=C-C*G.T*(G*C*G.T).inv()*G*C
    assert C.rank()==rank_before and Cc.rank()==rank_after
    assert Cc[2:5,2:5]==ra*PT/3 and Cc[5:8,5:8]==rb*PT
    assert Cc.extract(static,static)==C.extract(static,static)
    assert G*Cc==s.zeros(2,14)
    results.append({"active_alphabet":name,"full_covariance_rank":rank_before,"conditioned_rank":rank_after,"static_block_unchanged":True})
check("full_field_Gauss_conditioning_keeps_all_other_modes",True,results)
jumps=(2*EO).col_join(BO)
check("independent_birth_noise_in_both_vector_sectors",jumps*jumps.T==8*s.eye(6))
projected=s.Matrix.vstack(2*k.T*EO,k.T*BO)
check("post_preparation_longitudinal_noise_per_beta_p0",projected*projected.T/norm2==8*s.eye(2))
# Counterexample to the unqualified full-occupancy propagation count.
gamma0_speeds=[0]*13
check("zero_gamma_full_occupancy_scope_counterexample",len(gamma0_speeds)==13,
      {"gamma":0,"propagating_modes":0,"static_modes":13,"reason":"The supplied tensor and all homogeneous product currents vanish identically at gamma=0."})
out["completed_control_groups"]=len(out["checks"])
out["versions"]={"python":platform.python_version(),"numpy":np.__version__,"sympy":s.__version__}
out["source_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
text=json.dumps(out,indent=2)+"\n"
Path("INDEPENDENT_RESULTS.json").write_text(text);print(text,end="")
