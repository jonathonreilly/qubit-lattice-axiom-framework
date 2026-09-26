"""Independent quantum/carrier/Born-deformation controls; no author imports."""
from pathlib import Path
from itertools import product,permutations
from collections import Counter
import json,sys,platform
import sympy as s
import numpy as np
import scipy
from scipy.optimize import linprog
from scipy.integrate import solve_ivp
from scipy.linalg import expm,svdvals

out=Path(__file__).resolve().parent
checks=[]
def check(name, ok=True, **details):
    assert bool(ok),(name,details)
    item=dict(name=name,status="passed",**details);checks.append(item)
    print(json.dumps(item,sort_keys=True),flush=True)
def clean(M):return M.applyfunc(s.simplify)
def iszero(M):return all(s.simplify(x)==0 for x in M)
I2=s.eye(2)
pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
def sigma(v):return sum((v[i]*pauli[i] for i in range(3)),s.zeros(2))
unit=[s.eye(3)[:,i] for i in range(3)]
e=[];b=[]
for i in range(3):
    for sign in (1,-1):e.append(sign*unit[i]);b.append(s.zeros(3,1))
for signs in product((1,-1),repeat=3):e.append(s.zeros(3,1));b.append(s.Matrix(signs))
E=s.Matrix.vstack(*[v.T for v in e]);B=s.Matrix.vstack(*[v.T for v in b])
F=E.row_join(B/2);T=F*F.T;one=s.ones(14,1)
S=E+B/s.sqrt(3)
j=s.symbols("j",real=True)
P=(s.ones(14)+j*T)/14
check("rank_seven_original_kernel",F.T*F==2*s.eye(6) and T*T==2*T and T*one==s.zeros(14,1)
      and P.subs(j,s.Rational(3,5)).rank()==7,
      eigenvalues=["1 once","j/7 six times","0 seven times"])
# A rank-four stochastic truncation saturates the Frobenius lower bound.
Q=(s.ones(14)+j*E*E.T)/14
difference=P-Q
frob=s.simplify(sum(v*v for v in difference))
check("rank_TV_constant_and_Frobenius_control",
      Q.subs(j,s.Rational(3,5)).rank()==4 and frob==3*j*j/49
      and s.simplify(s.sqrt(s.Rational(3,49)/28)-s.sqrt(s.Rational(3,7))/14)==0,
      lower_bound="sqrt(3/7) |j| / 14",rank_four_example_worst_TV="3 |j| / 28")

# Direct probabilities for the fixed-natural minimax witness and reduced dual.
u,w=s.symbols("u w",real=True)
alpha=eta=s.Rational(1,14)
unat=0;wnat=j*(2-s.sqrt(3))/56
Rays=[S[a,:].T for a in range(14)]
rho=[(I2+sigma(v))/2 for v in Rays]
effects=[alpha*I2+unat*sigma(e[a]) if a<6 else eta*I2+wnat*sigma(b[a]) for a in range(14)]
Qnat=s.Matrix(14,14,lambda a,bb:s.simplify(s.trace(effects[a]*rho[bb])))
for jj in (s.Rational(1,5),-s.Rational(3,5),s.Rational(1,1)):
    tv=[s.simplify(sum(s.Abs((P[a,bb]-Qnat[a,bb]).subs(j,jj)) for a in range(14))/2) for bb in range(14)]
    assert all(s.simplify(x-abs(jj)*(3-s.sqrt(3))/14)==0 for x in tv)
dual_weight=s.sqrt(3)/(2+s.sqrt(3))
A_loss=j/14-u+4*w
B_loss=s.sqrt(3)*u+3*j/28-2*s.sqrt(3)*w
check("natural_encoding_minimax_exact_primal_and_dual",
      iszero(sum(effects,s.zeros(2))-I2)
      and s.simplify(dual_weight*A_loss+(1-dual_weight)*B_loss-j*(3-s.sqrt(3))/14-dual_weight*u)==0,
      optimum="|j|(3-sqrt(3))/14",a_effect_slope="0",b_effect_slope="j(2-sqrt(3))/56")

# Numerical LP for the fully justified twirled family; all column TV constraints.
Sn=np.array(S,dtype=float); En=np.array(E,dtype=float);Bn=np.array(B,dtype=float);Tn=np.array(T,dtype=float)
lp_results=[]
# Variables alpha,eta,u,w,delta,t_00,...,t_13,13.
for jj in (-0.83,-0.17,0.0,0.29,0.91):
    nv=5+196; objective=np.zeros(nv);objective[4]=1
    aub=[];bub=[]
    for a,bb in product(range(14),repeat=2):
        q=np.zeros(nv)
        q[0 if a<6 else 1]=1
        q[2 if a<6 else 3]=(En[a] if a<6 else Bn[a])@Sn[bb]
        pp=(1+jj*Tn[a,bb])/14
        for sign in (1,-1):
            row=sign*q;row[5+14*a+bb]=-1
            aub.append(row);bub.append(sign*pp)
    for bb in range(14):
        row=np.zeros(nv);row[4]=-1
        for a in range(14):row[5+14*a+bb]=.5
        aub.append(row);bub.append(0)
    for i,ii,r in ((0,2,1),(1,3,np.sqrt(3))):
        for sign in (1,-1):
            row=np.zeros(nv);row[i]=-1;row[ii]=sign*r
            aub.append(row);bub.append(0)
    ae=np.zeros((1,nv));ae[0,0]=6;ae[0,1]=8
    bounds=[(0,None),(0,None),(None,None),(None,None),(0,None)]+[(0,None)]*196
    result=linprog(objective,A_ub=np.array(aub),b_ub=np.array(bub),A_eq=ae,b_eq=[1],bounds=bounds,method="highs")
    target=abs(jj)*(3-np.sqrt(3))/14
    assert result.success and abs(result.fun-target)<1e-9
    lp_results.append(dict(j=jj,optimum=float(result.fun),target=float(target),largest_inequality_violation=float(np.max(np.array(aub)@result.x-np.array(bub)))))
check("natural_minimax_symmetry_reduced_LP",cases=lp_results,scope="Numerical cross-check of the exact twirling/primal/dual proof, not a separate unrestricted encoding optimization.")

# Explicit qutrit basis and all 196 probabilities.
G=[]
for (a,bb,imag) in ((0,1,False),(0,1,True)):
    M=s.zeros(3);M[a,bb]=-s.I if imag else 1;M[bb,a]=s.I if imag else 1;G.append(M)
G.append(s.diag(1,-1,0))
for (a,bb,imag) in ((0,2,False),(0,2,True),(1,2,False)):
    M=s.zeros(3);M[a,bb]=-s.I if imag else 1;M[bb,a]=s.I if imag else 1;G.append(M)
assert s.Matrix(6,6,lambda a,bb:s.trace(G[a]*G[bb]))==2*s.eye(6)
Gt=[sum((F[a,r]*G[r] for r in range(6)),s.zeros(3)) for a in range(14)]
qstates=[s.eye(3)/3+v/(3*s.sqrt(2)) for v in Gt]
qeffects=[s.eye(3)/14+3*s.sqrt(2)*j*v/28 for v in Gt]
assert iszero(sum(qeffects,s.zeros(3))-s.eye(3))
for a,bb in product(range(14),repeat=2):
    assert s.simplify(s.trace(qeffects[a]*qstates[bb])-P[a,bb])==0
min_state=min(float(np.linalg.eigvalsh(np.array(v,dtype=complex)).min()) for v in qstates)
min_effect=min(float(np.linalg.eigvalsh(np.array(v.subs(j,jj),dtype=complex)).min()) for v in qeffects for jj in (s.Rational(1,3),-s.Rational(1,3)))
check("qutrit_exact_construction",min_state>0 and min_effect>=-1e-12,
      exact_probability_pairs=196,certified_range="|j|<=1/3 by Hilbert-Schmidt norm bound",
      numerical_endpoint_min_state=min_state,numerical_endpoint_min_effect=min_effect)

# Four-dimensional orbit-register construction.
states4=[s.diag(rho[a],s.zeros(2)) if a<6 else s.diag(s.zeros(2),rho[a]) for a in range(14)]
effects4=[s.diag((I2+j*sigma(e[a]))/14,I2/14) if a<6
          else s.diag(I2/14,(I2+j*s.sqrt(3)*sigma(b[a])/4)/14) for a in range(14)]
assert iszero(sum(effects4,s.zeros(4))-s.eye(4))
for a,bb in product(range(14),repeat=2):
    assert s.simplify(s.trace(effects4[a]*states4[bb])-P[a,bb])==0
check("four_dimensional_exact_construction",exact_probability_pairs=196,
      effect_bloch_radii=["|j|","3|j|/4"],covariance="I_orbit tensor the proper-cubic spinor")

# Resource countercontrol: coordinated encoding/measurement seed raises rank.
shared=s.zeros(14)
for r in range(6):
    for a,bb in product(range(14),repeat=2):
        shared[a,bb]+=(1+6*j*F[a,r]*F[bb,r])/(14*6)
check("shared_encoding_randomness_scope_countercontrol",iszero(shared-P),
      range="|j|<=1/6",resource="Uniform six-valued shared seed r; input Bloch z=t_br and effect slope 6j t_ar. Excluded by the note's product-resource assumption.")

# Derive the ordinary S4 table from the proper signed cubic actions.
diags=[(1,a,bb) for a,bb in product((1,-1),repeat=2)]
pairings=[frozenset((frozenset(x),frozenset(set(range(4))-set(x)))) for x in ((0,1),(0,2),(0,3))]
def cycle_type(p):
    rem=set(range(4));lens=[]
    while rem:
        x=next(iter(rem));y=x;length=0
        while y in rem:rem.remove(y);length+=1;y=p[y]
        lens.append(length)
    return tuple(sorted(lens))
classes={}
for perm in permutations(range(3)):
    for signs in product((1,-1),repeat=3):
        R=s.zeros(3)
        for i in range(3):R[i,perm[i]]=signs[i]
        if R.det()!=1:continue
        p=[]
        for v in diags:
            w=list(R*s.Matrix(v))
            if w[0]<0:w=[-x for x in w]
            p.append(diags.index(tuple(w)))
        typ=cycle_type(p)
        fixed=sum(p[i]==i for i in range(4))
        sign=(-1)**(4-len(typ))
        fixed_pairings=sum(frozenset(frozenset(p[x] for x in pair) for pair in pairs)==pairs for pairs in pairings)
        row=(1,sign,fixed_pairings-1,int(s.trace(R)),fixed-1)
        classes.setdefault(typ,[]).append(row)
order=[(1,1,1,1),(1,1,2),(2,2),(1,3),(4,)]
sizes=[len(classes[t]) for t in order]
assert sizes==[1,6,3,8,6] and all(len(set(classes[t]))==1 for t in order)
chars=s.Matrix.hstack(*[s.Matrix(classes[t][0]) for t in order])
expected=s.Matrix([[1,1,1,1,1],[1,-1,1,1,-1],[2,0,2,-1,0],[3,-1,-1,0,1],[3,1,-1,0,-1]])
assert chars==expected
assert chars*s.diag(*sizes)*chars.T/24==s.eye(5)
assert sum(chars[i,0]**2 for i in range(5))==24
candidates=[chars[2,:],2*chars[0,:],chars[0,:]+chars[1,:],2*chars[1,:]]
allowed=[idx for idx,W in enumerate(candidates) if -1+W[1]>=0]
assert allowed==[1]
squares=[m for m in product(range(1,4),repeat=3) if sum(x*x for x in m)==3]
check("proper_cubic_character_and_projective_commutant_obstruction",squares==[(1,1,1)],
      character_table=[list(map(int,chars[i,:])) for i in range(5)],class_sizes=sizes,
      allowed_W="two trivial characters",required_commutant_dimension=3,
      required_projective_blocks="three inequivalent one-dimensional blocks with one shared multiplier",
      available_ordinary_character_ratios=2)

# Preservation checks: distinct columns, and a mixed-state scope exception.
assert len({tuple(T[:,a]) for a in range(14)})==14
overlap=s.Matrix(14,14,lambda a,bb:(1+Rays[a].dot(Rays[bb]))/2)
nonorth_pairs=sum(int(bool(overlap[a,bb]>0)) for a in range(14) for bb in range(a+1,14))
proj=[s.diag(1,0),s.diag(0,1)]
mixed=[s.diag(s.Rational(1,4),s.Rational(3,4)),s.diag(s.Rational(3,4),s.Rational(1,4))]
assert all(sum((q*r*q for q in proj),s.zeros(2))==r for r in mixed)
check("pure_parent_permanence_scope",nonorthogonal_natural_pairs=int(nonorth_pairs),
      distinct_original_columns=14,pure_carrier_minimum=14,
      mixed_state_countercontrol="Z measurement preserves two distinct diagonal mixed states on average and has different outcome laws; pure-state factorization cannot be reused.")

# Born-compatible kernel, 2-design and exact sharp fidelity witness.
PB=(s.ones(14)+j*S*S.T)/14
assert S.T*S==s.Rational(14,3)*s.eye(3)
assert PB.subs(j,s.Rational(3,5)).rank()==4
EB=[(I2+j*sigma(Rays[a]))/14 for a in range(14)]
assert iszero(sum(EB,s.zeros(2))-I2)
for a,bb in product(range(14),repeat=2):
    assert s.simplify(s.trace(EB[a]*rho[bb])-PB[a,bb])==0
swap=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
assert clean(sum((s.kronecker_product(r,r) for r in rho),s.zeros(4))/14)==(s.eye(4)+swap)/6
K=[(3*I2+sigma(Rays[a]))/(2*s.sqrt(35)) for a in range(14)]
assert all(iszero(K[a].conjugate().T*K[a]-EB[a].subs(j,s.Rational(3,5))) for a in range(14))
fidelity=s.simplify(sum(s.trace(r*K[a])*s.conjugate(s.trace(r*K[a])) for r in rho for a in range(14))/14)
check("Born_kernel_2design_and_fidelity_witness",fidelity==s.Rational(14,15),
      kernel_rank=4,j="3/5",fidelity=str(fidelity),sharp_formula="(2+sqrt(1-j^2))/3",
      scope="The analytical Kraus trace inequality supplies optimality over instruments and recovery.")
# Two-parent matrix rate and trace checks, normalized beta/N=1 for this identity.
FB=[s.kronecker_product(I2+j*sigma(v),I2+j*sigma(v)) for v in Rays]
sumFB=clean(sum(FB,s.zeros(4)))
target=14*s.eye(4)+s.Rational(14,3)*j*j*sum((s.kronecker_product(q,q) for q in pauli),s.zeros(4))
assert iszero(sumFB-target)
for bb,cc in ((0,1),(0,2),(6,13),(0,6)):
    rr=s.kronecker_product(rho[bb],rho[cc])
    for a in range(14):
        assert s.simplify(s.trace(FB[a]*rr)-(1+j*Rays[a].dot(Rays[bb]))*(1+j*Rays[a].dot(Rays[cc])))==0
check("positive_two_parent_event_rate_matrix",marked_matrix_probability_checks=56,
      total_rate_operator="14 I + (14 j^2/3) sum_i sigma_i tensor sigma_i",
      sufficient_event_step="dt <= N/[14 beta (1+|j|)^k]",
      scope="One observed event instrument only; no repeated classical exponential waiting law.")

# Full fourteen-field Born reaction/current matrix, independently differentiated.
nA=s.Matrix([int(a<6) for a in range(14)])
rows=[one.T,(7*nA-3*one).T]+[2*E[:,i].T for i in range(3)]+[B[:,i].T for i in range(3)]
rows += [(E[:,i].applyfunc(lambda z:z*z)-nA/3).T for i in range(2)]
rows += [s.Matrix([b[a][i]*b[a][k] for a in range(14)]).T for i,k in ((0,1),(0,2),(1,2))]
rows += [s.Matrix([s.prod(v) for v in b]).T]
M=s.Matrix.vstack(*rows);Minv=M.inv()
rho0,beta,gamma,delta=s.symbols("rho beta gamma delta",real=True)
v=s.Matrix(s.symbols("v0:14"))
p=rho0*one/14+delta*Minv*v
XX=E.T*p;YY=B.T*p
birth=beta*(1-sum(p))*(one+j*S*(XX+YY/s.sqrt(3))).applyfunc(lambda z:z**6)
R=(M*s.Matrix([s.diff(z,delta).subs(delta,0) for z in birth])).jacobian(v)
R=clean(R);h=beta*j*(1-rho0)
Rwant=s.zeros(14);Rwant[0,0]=-14*beta
for i in range(3):
    Rwant[2+i,2+i]=12*h;Rwant[5+i,5+i]=16*h
    Rwant[2+i,5+i]=Rwant[5+i,2+i]=8*s.sqrt(3)*h
assert iszero(R-Rwant)
def cross(k):
    return s.Matrix([[0,-k[2],k[1]],[k[2],0,-k[0]],[-k[1],k[0],0]])
kk=s.Matrix(s.symbols("k1:4",real=True))
Js=s.Matrix([gamma*p[a]*(e[a].cross(YY)+XX.cross(b[a])-2*XX.cross(YY)).dot(kk) for a in range(14)])
AK=clean((M*s.Matrix([s.diff(z,delta).subs(delta,0) for z in Js])).jacobian(v))
c=2*gamma*rho0/7
AW=s.zeros(14);AW[2:5,5:8]=-c*cross(kk);AW[5:8,2:5]=c*cross(kk)
assert iszero(AK-AW)
L=R-s.I*AK
z=s.symbols("z")
char=s.factor(L[2:8,2:8].charpoly(z).as_expr())
char_target=z*(z-28*h)*(z*z-28*h*z+c*c*kk.dot(kk))**2
assert s.factor(char-char_target)==0
O=s.Matrix([[s.sqrt(3),2],[-2,s.sqrt(3)]])/s.sqrt(7)
Aorb=s.Matrix([[3,2*s.sqrt(3)],[2*s.sqrt(3),4]])
assert clean(O*Aorb*O.T)==s.diag(7,0)
assert O*s.Matrix([[0,1],[-1,0]])*O.T==s.Matrix([[0,1],[-1,0]])
check("complete_Born_reaction_flux_linearization",density="-14 beta",spectator_zero_fields=7,
      vector_characteristic="z(z-28h)(z^2-28hz+c^2|K|^2)^2",
      constant_PQ_rotation_preserves_curl=True)

# Parity qualification and concrete noncommuting time matrices.
Ref=s.diag(-1,1,1)
old=Rays[0].dot(Rays[6])
after=(Ref*e[0]).dot(Ref.det()*Ref*b[6]/s.sqrt(3))
assert s.simplify(after+old)==0 and old!=0
Kval=s.Matrix([1,2,3])
L1=L[2:8,2:8].subs({kk[0]:1,kk[1]:2,kk[2]:3,gamma:s.Rational(4,5),beta:s.Rational(1,3),j:s.Rational(2,5),rho0:s.Rational(1,4)})
L2=L[2:8,2:8].subs({kk[0]:1,kk[1]:2,kk[2]:3,gamma:s.Rational(4,5),beta:s.Rational(1,3),j:s.Rational(2,5),rho0:s.Rational(3,4)})
assert not iszero(L1*L2-L2*L1)
check("parity_cost_and_time_ordering",reflection_cross_term_before=str(old),reflection_cross_term_after=str(after),
      time_matrices_noncommute=True,norm_statement_scope="Six raw vector components only; density has a separate -14 beta drift.")

# Numerically test proved norm envelopes and asymptotic scattering tail for both signs.
ode=[]
vinit=.63;be=.23;ga=-.8;Kn=np.array([2*np.pi,0,2*np.pi])
Cn=np.array(cross(s.Matrix(Kn)),dtype=complex)
A0=np.block([[np.zeros((3,3)),1j*Cn],[-1j*Cn,np.zeros((3,3))]])
R0=np.kron(np.array([[12,8*np.sqrt(3)],[8*np.sqrt(3),16]]),np.eye(3))
cinf=2*ga/7;Linf=cinf*A0
assert np.max(abs(Linf+Linf.conj().T))<1e-14
times=np.linspace(0,8,161)
for jj in (-.61,.61):
    def fun(t,y):
        vacancy=vinit*np.exp(-14*be*t);rh=1-vacancy
        LL=cinf*rh*A0+be*jj*vacancy*R0
        return (LL@y.reshape(6,6)).reshape(-1)
    sol=solve_ivp(fun,(0,8),np.eye(6,dtype=complex).reshape(-1),method="DOP853",t_eval=times,rtol=1e-11,atol=1e-13)
    assert sol.success
    mats=[sol.y[:,i].reshape(6,6) for i in range(len(times))]
    violations=[]
    for t,phi in zip(times,mats):
        gain=np.exp(2*jj*vinit*(1-np.exp(-14*be*t)))
        lower=min(1,gain);upper=max(1,gain);sv=svdvals(phi)
        violations.append(max(lower-sv[-1],sv[0]-upper))
    assert max(violations)<2e-9
    a=14*be
    bound_phi=np.exp(2*max(jj,0)*vinit)
    constant=vinit*(28*be*abs(jj)+abs(cinf)*np.linalg.norm(Kn))
    z6=expm(-Linf*6)@mats[120]
    z8=expm(-Linf*8)@mats[160]
    tail_bound=bound_phi*constant/a*np.exp(-a*6)
    actual=np.linalg.norm(z8-z6,2)
    assert actual<=tail_bound+2e-10
    ode.append(dict(j=jj,max_norm_envelope_violation=float(max(violations)),
                    scattering_change_6_to_8=float(actual),proved_tail_bound_from_6=float(tail_bound),
                    limiting_map_lower_singular_bound=float(np.exp(2*min(jj,0)*vinit)),
                    observed_Z8_min_singular=float(svdvals(z8)[-1])))
check("time_ordered_vector_norm_and_scattering_numerical_controls",cases=ode,
      scope="Finite-mode matrix ODE only; proof supplies uniform-in-time envelope/tail.")
# The full density mode is an explicit guard against exporting the vector norm bound.
check("density_mode_scope_guard",np.exp(-14*be)<1,
      density_norm_ratio_at_t1=float(np.exp(-14*be)),note="Not subject to the vector norm lower bound.")

# Late-state hypotheses survive kernel change; exact uniform feature covariance.
assert (s.ones(14)+j*S*S.T)*one==14*one
fullp=one/14
Cf=clean(M*(s.diag(*fullp)-fullp*fullp.T)*M.T)
assert Cf.rank()==13 and Cf[2:8,2:8]==4*s.eye(6)/7
check("late_state_kernel_and_covariance_hypotheses",positive_weight_range="1-|j| to 1+|j|",
      occupied_row_sum=14,uniform_vector_covariance="4 I_6/7",full_feature_covariance_rank=13,
      required_order="t to infinity at each finite N, then N to infinity; fixed interior equal-label product initial law.")

result=dict(scope="Independent reconstruction and controls before author-checker/result access.",
            versions=dict(python=sys.version,sympy=s.__version__,numpy=np.__version__,scipy=scipy.__version__,platform=platform.platform()),
            checks=checks,passed=len(checks),failed=0)
(out/"INDEPENDENT_RESULTS.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
print(json.dumps(dict(passed=len(checks),failed=0),sort_keys=True))
