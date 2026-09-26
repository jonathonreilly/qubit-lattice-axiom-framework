#!/usr/bin/env python3
"""Exact pair-birth algebra and Gaussian finite-mode constraint controls."""
from pathlib import Path
from itertools import product
import hashlib,json
import sympy as s
H=Path(__file__).resolve().parent
checks=[]
def check(name,value,detail=None):
 assert bool(value),(name,detail)
 checks.append(dict(name=name,passed=True,detail=detail));print('PASS:',name,flush=True)
def zero(M):return all(s.expand(x)==0 for x in M)
axes=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
cubes=list(product((-1,1),repeat=3))
e=[s.Matrix(x) for x in axes]+[s.zeros(3,1)]*8
b=[s.zeros(3,1)]*6+[s.Matrix(x) for x in cubes]
bar=[next(c for c in range(14) if e[c]==-e[a] and b[c]==-b[a]) for a in range(14)]
E=s.Matrix.hstack(*e);B=s.Matrix.hstack(*b);P=s.zeros(14)
for a in range(14):P[bar[a],a]=1
check('opposite_is_fixed_point_free_involution',P*P==s.eye(14) and all(P[a,a]==0 for a in range(14)))
check('each_pair_conserves_both_vectors',E*P==-E and B*P==-B)
beta,v=s.symbols('beta v',positive=True);pa=s.Matrix(s.symbols('p1:15',positive=True));q=s.Matrix(s.symbols('q1:15',real=True))
q0=1-sum(q);V=beta*s.Rational(1,2)*sum(v*v*q[a]*q[bar[a]]/(pa[a]*pa[bar[a]])-q0*q0 for a in range(14))
subs=dict(zip(q,pa));vsub={pa[-1]:1-v-sum(pa[:-1])}
check('pair_reaction_adjoint_zero_at_reference',s.simplify(V.subs(subs,simultaneous=True).subs(vsub))==0)
grad=s.Matrix([s.diff(V,x) for x in q]).subs(subs,simultaneous=True).subs(vsub)
Hessian=s.diag(*[1/x for x in pa])+s.ones(14)/v
reaction=beta*v*v*s.ones(14,1)
check('pair_reaction_adjoint_projection_is_entropy_H_times_B',all(s.simplify(x)==0 for x in grad-(Hessian*reaction).subs(vsub)))
Q=s.zeros(14)
for a in range(14):
 increment=s.eye(14)[:,a]+s.eye(14)[:,bar[a]]
 Q+=beta*v*v*s.Rational(1,2)*increment*increment.T
check('full_fourteen_species_pair_birth_covariance',Q==beta*v*v*(s.eye(14)+P))
check('density_birth_noise_has_cluster_factor_two',(s.ones(1,14)*Q*s.ones(14,1))[0]==28*beta*v*v)
check('leading_vector_birth_noise_vanishes',zero(E*Q*E.T) and zero(B*Q*B.T) and zero(E*Q*B.T))
check('pair_covariance_rank_and_nonnegative_spectrum',(s.eye(14)+P).eigenvals()=={2:7,0:7})
# Full two-site generator: only the all-vacant row has nonzero birth rates.
labels=[(s.zeros(3,1),s.zeros(3,1))]+list(zip(e,b));states=list(product(range(15),repeat=2));lookup={x:i for i,x in enumerate(states)}
L=s.zeros(225,225);source=lookup[(0,0)]
for a in range(14):L[source,lookup[(a+1,bar[a]+1)]]=beta/6
L[source,source]=-14*beta/6
check('complete_225_state_birth_generator_rows_conserve_probability',L*s.ones(225,1)==s.zeros(225,1))
for name,component,factor in [('electric',0,s.Rational(-1,3)),('magnetic',1,s.Rational(-4,3))]:
 observable=s.Matrix([labels[x][component][0]*labels[y][component][0] for x,y in states])
 initial_derivative=v*v*(L*observable)[source]
 check(name+'_adjacent_connected_covariance',s.simplify(initial_derivative-factor*beta*v*v)==0,dict(value=str(initial_derivative)))
 for_component=s.Matrix([labels[x][component][0]+labels[y][component][0] for x,y in states])
 check(name+'_total_vector_exact_generator_conservation',L*for_component==s.zeros(225,1))
# Fourier birth noise from the generator increment, with an arbitrary phase.
z=s.symbols('z',complex=True);d2=(1-z)*(1-s.conjugate(z))
Qe=s.zeros(3);Qb=s.zeros(3)
for a in range(14):
 de=e[a]+z*e[bar[a]];db=b[a]+z*b[bar[a]]
 Qe+=beta*v*v*s.Rational(1,6)*de*de.conjugate().T
 Qb+=beta*v*v*s.Rational(1,6)*db*db.conjugate().T
check('one_edge_fourier_vector_brackets',zero(Qe-beta*v*v*d2*s.eye(3)/3) and zero(Qb-4*beta*v*v*d2*s.eye(3)/3))

# Gaussian conditioning formula: covariance is I-G^T(GG^T)^-1G.
k=s.Matrix([1,2,2]);PL=k*k.T/9;PT=s.eye(3)-PL
G=(k.T/3).row_join(s.zeros(1,3)).col_join(s.zeros(1,3).row_join(k.T/3))
conditioned=s.eye(6)-G.T*(G*G.T).inv()*G
check('finite_mode_Gauss_conditioning_removes_only_longitudinal_variance',conditioned==s.diag(PT,PT))
C=s.Matrix([[0,-k[2],k[1]],[k[2],0,-k[0]],[-k[1],k[0],0]])
D=s.zeros(3).row_join(s.I*C).col_join((-s.I*C).row_join(s.zeros(3)))
check('curl_drift_preserves_Gauss_subspace',zero(G*D) and zero(D*conditioned-D))
t,st,v0=s.symbols('t s v0',nonnegative=True)
rho=lambda u:1-v0*s.exp(-14*beta*u)
noise_integral=s.integrate(8*beta*v0*s.exp(-14*beta*t),(t,st,t))
check('single_birth_longitudinal_noise_after_preparation',s.simplify(noise_integral-s.Rational(4,7)*(rho(t)-rho(st)))==0)
report=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),checks=checks,
 scope='Exact pair-birth finite-generator and covariance identities; finite Gaussian conditioning algebra. Does not prove an interacting fluctuation theorem, simultaneous N/constraint limits, or microscopic gauge invariance.')
(H/'PAIRED_FORMATION_GAUSS_RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
print('TOTAL:',len(checks),'exact controls',flush=True)
