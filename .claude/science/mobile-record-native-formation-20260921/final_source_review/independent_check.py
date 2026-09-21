#!/usr/bin/env python3
"""New selective exact controls for the assembled publication proof.

No author checker is imported. Earlier full-state jet/proof evidence is reused
by identity, so this checks projection, full complex energy and proof constants.
"""
from pathlib import Path
from itertools import combinations, permutations
from collections import Counter
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent
results=[]
def check(name,condition,detail=None):
    assert condition,(name,detail)
    results.append(dict(name=name,detail=detail))
    print("VERIFIED",name,json.dumps(detail,sort_keys=True),flush=True)

def exchange_matrix(configurations,edges,blocked=False):
    lookup={q:i for i,q in enumerate(configurations)}
    matrix=s.zeros(len(configurations))
    for row,q in enumerate(configurations):
        for x,y in edges:
            if q[x]==q[y] or (blocked and {q[x],q[y]}=={1,2}):continue
            new=list(q);new[x],new[y]=new[y],new[x]
            column=lookup[tuple(new)]
            matrix[row,column]+=1;matrix[row,row]-=1
    return matrix
pair=sorted(set(permutations((1,1,0,0))))
triple=sorted(set(permutations((1,1,2,0))))
projection=s.zeros(len(triple),len(pair))
for row,q in enumerate(triple):
    projection[row,pair.index(tuple(int(a==1) for a in q))]=1
for name,edges in [("four_cycle",[(0,1),(1,2),(2,3),(3,0)]),
                   ("four_site_star",[(0,1),(0,2),(0,3)])]:
    h2=exchange_matrix(pair,edges)
    h3=exchange_matrix(triple,edges)
    bad=exchange_matrix(triple,edges,blocked=True)
    check(name+"_full_stirring_projection",h3*projection==projection*h2,
          dict(pair_states=len(pair),triple_states=len(triple)))
    defect=bad*projection-projection*h2
    check(name+"_blocked_vector_vacancy_swap_is_detected",defect!=s.zeros(*defect.shape),
          dict(nonzero_entries=sum(int(x!=0) for x in defect),maximum=max(abs(int(x)) for x in defect)))
rho,beta,j,alpha=s.symbols("rho beta j alpha",real=True)
kx,ky,kz=s.symbols("kx ky kz",real=True)
v=1-rho;lam=6*beta;mu=12*beta*j*v
metric=s.zeros(6);metric[0,0]=1/(rho*v)
for a in range(1,4):metric[a,a]=3/rho
metric[4:6,4:6]=(3/rho)*s.Matrix([[2,1],[1,2]])
transport=s.zeros(6)
for a,k in enumerate((kx,ky,kz),1):
    transport[0,a]=2*alpha*rho*v*k
    transport[a,0]=2*alpha*rho*k/3
reaction=s.diag(-lam,mu,mu,mu,0,0)
drift=reaction-s.I*transport
actual=(metric.diff(rho)*lam*v+drift.conjugate().T*metric+metric*drift).applyfunc(s.factor)
expected=s.zeros(6);expected[0,0]=(-lam/rho)*metric[0,0]
for a in range(1,4):expected[a,a]=(2*mu-lam*v/rho)*metric[a,a]
expected[4:6,4:6]=(-lam*v/rho)*metric[4:6,4:6]
check("all_six_fields_arbitrary_complex_Fourier_energy",
 (actual-expected).applyfunc(s.simplify)==s.zeros(6),
 dict(coordinates=["density","g1","g2","g3","r1","r2"],r3="-r1-r2"))
check("frozen_acoustic_speed_from_inherited_amplitude",
 s.factor(transport[0,1]*transport[1,0]+transport[0,2]*transport[2,0]+transport[0,3]*transport[3,0]
          -4*alpha**2*rho**2*v*(kx*kx+ky*ky+kz*kz)/3)==0)
# The argument convention is fixed by both inherited proofs.
density=(s.Rational(1,41),s.Rational(81,41))
d_density=s.simplify((s.sqrt(density[0])-s.sqrt(density[1]))**2)
d_sqrt=s.simplify((density[0]**s.Rational(1,4)-density[1]**s.Rational(1,4))**2)
check("Dirichlet_density_argument_is_not_square_root_argument",d_density!=d_sqrt,
 dict(density=[str(x) for x in density],D_f=str(d_density),D_sqrt_f=str(d_sqrt)))
# Explicit extension paths are generic; N=4 also exercises periodic identifications.
for side in (4,5):
    origin=(0,0,0)
    neighbors=[]
    for axis in range(3):
        for sign in (1,-1):
            q=[0,0,0];q[axis]=sign%side;neighbors.append(tuple(q))
    edge_weights=Counter()
    paths=[]
    def add(a,b):return tuple((x+y)%side for x,y in zip(a,b))
    def is_edge(a,b):
        diff=[(x-y)%side for x,y in zip(a,b)]
        return sum(x!=0 for x in diff)==1 and next(x for x in diff if x)!=0 and any(x in (1,side-1) for x in diff)
    for y,z in combinations(neighbors,2):
        opposite=all((a+b)%side==0 for a,b in zip(y,z))
        if opposite:
            axis=next(i for i,a in enumerate(y) if a)
            other=(axis+1)%3
            w=tuple(int(i==other) for i in range(3))
            path=[y,add(y,w),w,add(z,w),z]
        else:path=[y,add(y,z),z]
        assert origin not in path and len(set(path))==len(path)
        assert all(is_edge(a,b) for a,b in zip(path,path[1:]))
        length=len(path)-1
        for a,b in zip(path,path[1:]):edge_weights[tuple(sorted((a,b)))]+=length
        paths.append(path)
    congestion=s.Rational(max(edge_weights.values()),6)
    check("puncture_extension_paths_side_%d"%side,len(paths)==15 and congestion<=10,
          dict(maximum_path_length=max(len(p)-1 for p in paths),exact_Cauchy_bound=str(congestion)))
ones=s.ones(6,1)
projector=s.eye(6)-ones*ones.T/6
pair_energy=s.zeros(6)
for a,b in combinations(range(6),2):
    e=s.zeros(6,1);e[a]=1;e[b]=-1
    pair_energy+=e*e.T/6
check("complex_neighbor_extension_variance_identity",projector.T*projector==pair_energy)
(HERE/'INDEPENDENT_RESULTS.json').write_text(json.dumps(dict(
 source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 checks=results,scope="Exact finite/symbolic selective controls, not a numerical proof of the uniform heat or entropy limit.",
 versions=dict(sympy=s.__version__)),indent=2,sort_keys=True)+'\n')
print("SELECTIVE_EXACT_GROUPS",len(results),flush=True)
