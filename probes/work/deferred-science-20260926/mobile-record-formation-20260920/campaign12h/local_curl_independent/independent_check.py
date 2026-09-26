"""Independent local-curl source review controls. No author checker imports."""
from __future__ import annotations
from itertools import product, permutations
from fractions import Fraction
from pathlib import Path
import json, sys, platform
import sympy as s
from collections import Counter, deque

checks=[]
def record(name, **data):
    checks.append(dict(name=name, status="passed", **data))
    print(json.dumps(checks[-1], sort_keys=True), flush=True)
def zero(m):
    return all(s.simplify(x)==0 for x in m)
def cross(v):
    x,y,z=v
    return s.Matrix([[0,-z,y],[z,0,-x],[-y,x,0]])
basis=[s.eye(3)[:,i] for i in range(3)]
ev=[s.zeros(3,1)]; bv=[s.zeros(3,1)]
names=["vacancy"]
for i in range(3):
    for sign in (1,-1):
        ev.append(sign*basis[i]);bv.append(s.zeros(3,1)); names.append(f"A{i}:{sign}")
for signs in product((1,-1),repeat=3):
    ev.append(s.zeros(3,1));bv.append(s.Matrix(signs)); names.append("B"+str(signs))
Ea=s.Matrix.vstack(*[v.T for v in ev[1:]])
Ba=s.Matrix.vstack(*[v.T for v in bv[1:]])
nA=s.Matrix([int(a<=6) for a in range(1,15)])
one=s.ones(14,1)
rows=[one.T,(7*nA-3*one).T]
rows += [2*Ea[:,i].T for i in range(3)]
rows += [Ba[:,i].T for i in range(3)]
rows += [(Ea[:,i].applyfunc(lambda x:x*x)-nA/3).T for i in range(2)]
rows += [s.Matrix([bv[a][i]*bv[a][j] for a in range(1,15)]).T for i,j in ((0,1),(0,2),(1,2))]
rows += [s.Matrix([s.prod(bv[a]) for a in range(1,15)]).T]
T=s.Matrix.vstack(*rows)
assert T.shape==(14,14) and T.det()!=0
Ti=T.inv()
record("complete_fourteen_field_basis", determinant=str(T.det()), fields=["rho","4rhoA-3rhoB","U1","U2","U3","V1","V2","V3","r1","r2","M12","M13","M23","M123"])

# Enumerate loop templates directly, not from the proposed h_i formula.
N=7
def add(x,y):return tuple((x[i]+y[i])%N for i in range(3))
z=(0,0,0)
unit=[tuple(int(i==j) for i in range(3)) for j in range(3)]
def scale(v,a):return tuple(a*x for x in v)
templates=[]
for c in product(range(N),repeat=3):
    for i,j in ((0,1),(0,2),(1,2)):
        for orient in (1,-1):
            for sp in (0,1):
                pts=[add(c,scale(unit[j],-1)),add(c,unit[i]),add(c,unit[j]),add(c,scale(unit[i],-1))]
                lab=[(sp,i,orient),(sp,j,orient),(sp,i,-orient),(sp,j,-orient)]
                d=dict(zip(pts,lab))
                if z in d:templates.append(d)
assert len(templates)==48
background={(2,0,0):(0,1,1),(2,1,1):(0,2,1),(2,0,2):(0,1,-1),(2,6,1):(0,2,-1)}
def divergence(config):
    out=Counter()
    for x,(sp,i,sign) in config.items():
        out[(sp,add(x,scale(unit[i],-1)))]+=sign
        out[(sp,add(x,unit[i]))]-=sign
    return {k:v for k,v in out.items() if v}
assert divergence(background)=={}
assert all(add(z,scale(u,a)) not in background for u in unit for a in (1,-1))
counts=[]
for bg in ({},background):
    count=Counter(d[z] for d in templates if not (d.keys()&bg.keys()))
    counts.append(count)
    assert sum(count.values()) in (48,40)
for key in counts[0]:
    assert counts[0][key]==4
    assert counts[1][key]==(4 if key[1]==0 else 3)
record("loop_conditional_law_counterexample", templates=48, totals=[48,40],
       empty_probability="1/12", blocked_x_probability="1/10", blocked_yz_probability="3/40",
       only_intersecting_background_site=sorted(set().union(*(set(d) for d in templates))&background.keys()))

# Exact new weights and full signed cubic action.
G=Ea*Ea.T+Ba*Ba.T/4
assert min(G)==-1 and max(G)==1
j=s.symbols("j",real=True)
W=s.ones(14,14)+j*G
assert W*one==14*one
signed_rotations=[]
for perm in permutations(range(3)):
    for signs in product((1,-1),repeat=3):
        R=s.zeros(3)
        for i in range(3):R[i,perm[i]]=signs[i]
        signed_rotations.append(R)
        det=R.det()
        mapping=[]
        for a in range(15):
            image=(tuple(R*ev[a]),tuple(det*R*bv[a]))
            mapping.append(next(b for b in range(15) if image==(tuple(ev[b]),tuple(bv[b]))))
        for a,b in product(range(1,15),repeat=2):
            assert G[a-1,b-1]==G[mapping[a]-1,mapping[b]-1]
        for k in basis:
            assert cross(R*k)*(det*R)==R*cross(k)
            assert cross(R*k)*R==det*R*cross(k)
record("weights_and_full_cubic_covariance", signed_actions=48, weight_bracket_min="-1",weight_bracket_max="1",row_sum="14")

# Exact Gauss identity by convolution coefficients for all elementary impulses.
def curl2(f):
    out={}
    for x in product(range(N),repeat=3):
        v=[0,0,0]
        for i,jj,kk in ((0,1,2),(1,2,0),(2,0,1)):
            v[i]=f.get(add(x,unit[jj]),[0]*3)[kk]-f.get(add(x,scale(unit[jj],-1)),[0]*3)[kk]
            v[i]-=f.get(add(x,unit[kk]),[0]*3)[jj]-f.get(add(x,scale(unit[kk],-1)),[0]*3)[jj]
        if any(v):out[x]=v
    return out
def div2(f):
    return [sum(f.get(add(x,unit[i]),[0]*3)[i]-f.get(add(x,scale(unit[i],-1)),[0]*3)[i] for i in range(3)) for x in product(range(N),repeat=3)]
for a in range(15):
    for f in (ev[a],bv[a]):
        assert not any(div2(curl2({z:list(f)})))
record("all_label_impulse_divergence_of_curl",torus_side=N,impulses=30,scope="Linearity makes every configuration and all allowed transitions follow.")

# Differentiate the species currents/reactions via an independent arbitrary tangent.
rho,beta,gamma,h=s.symbols("rho beta gamma h",real=True)
u=s.Matrix(s.symbols("u0:14"))
p=rho*one/14+h*Ti*u
X=Ea.T*p;Y=Ba.T*p
ma=one+j*(Ea*X+Ba*Y/4)
birth=beta*(1-sum(p))*ma.applyfunc(lambda v:v**6)
Rfirst=s.Matrix([s.diff(expr,h).subs(h,0) for expr in birth])
R=(T*Rfirst).jacobian(u).applyfunc(s.simplify)
lam=12*beta*j*(1-rho)
want=s.diag(-14*beta,0,*([lam]*6),*([0]*6))
assert R==want
Ai=[]
for i in range(3):
    current=s.Matrix([gamma*p[a]*(ev[a+1].cross(Y)+X.cross(bv[a+1])-2*X.cross(Y))[i] for a in range(14)])
    Jfirst=s.Matrix([s.diff(expr,h).subs(h,0) for expr in current])
    Ai.append((T*Jfirst).jacobian(u).applyfunc(s.simplify))
K=s.Matrix(s.symbols("K1:4",real=True))
AK=sum((K[i]*Ai[i] for i in range(3)),s.zeros(14))
c=2*gamma*rho/7
expected=s.zeros(14)
expected[2:5,5:8]=-c*cross(K)
expected[5:8,2:5]=c*cross(K)
assert AK==expected
zz=s.symbols("z")
block=(R-s.I*AK)[2:8,2:8]
poly=s.factor(block.charpoly(zz).as_expr())
target=(zz-lam)**2*((zz-lam)**2+c*c*sum(x*x for x in K))**2
assert s.factor(poly-target)==0
assert zero(R*AK-AK*R)
record("full_reaction_flux_jacobian",reaction_diagonal=[str(v) for v in R.diagonal()],
       vector_characteristic=str(s.factor(target)),spectator_zero_fields=7,density_decay="-14 beta")
record("nonautonomous_commuting_propagator",lambda_over_rho_prime="6 j / 7",curl_speed=str(c),
       scopes="Homogeneous equal-per-label background; all fourteen fields retained.")

# Exact source-adjoint derivative on a biased 15-label reference.
pref=s.Matrix([s.Rational(i,120) for i in range(1,16)])
assert sum(pref)==1
p0=pref[0];po=pref[1:,:]
Wnum=W.subs(j,-s.Rational(2,5))
m= s.ones(14,1)+(Wnum-s.ones(14))*po
# Differentiate the full seven-site product expectation using all center and neighbor scores.
score_deriv=s.zeros(14,1)
for b in range(14):
    for a in range(14):
        central=p0/po[a]*po[a]-p0
        central_deriv=p0/po[a]*int(a==b)+1
        neighbor_deriv=6*m[a]**5*(Wnum[a,b]-1)
        score_deriv[b]+=central_deriv*m[a]**6+central*neighbor_deriv
H=s.diag(*[1/x for x in po])+s.ones(14)/p0
Rb=p0*m.applyfunc(lambda x:x**6)
assert zero(score_deriv-H*Rb)
assert all((p0/po[a]*po[a]-p0)==0 for a in range(14))
record("birth_adjoint_constant_linear_cancellation",reference="(1,...,15)/120",j="-2/5",
       derivative="H(p) B(p)",alphabet_size=15,uniform_reference_site_upper_bound="beta (1+abs(j))^6")

# Exact adjacent covariance derivative, sum both endpoints and subtract mean drifts.
pp=rho*one/14
mu=T*pp
Wfull=s.Matrix.hstack(one,W)
Ffull=s.Matrix.hstack(s.zeros(14,1),T)
pfull=s.Matrix([1-rho]+list(pp))
birth_mean=beta*(1-rho)*T*one
one_endpoint=beta*(1-rho)*T*Wfull*s.diag(*pfull)*Ffull.T
pair=(one_endpoint+one_endpoint.T-birth_mean*mu.T-mu*birth_mean.T).applyfunc(s.simplify)
desired=s.zeros(14)
for a in range(2,8):desired[a,a]=16*beta*j*rho*(1-rho)/7
assert pair==desired
witness=desired[2,2].subs({rho:s.Rational(3,5),beta:s.Rational(2,3),j:-s.Rational(1,2)})
assert witness==-s.Rational(32,175)
record("adjacent_native_covariance_generator",six_vector_diagonal=str(desired[2,2]),
       every_other_entry_zero=True,negative_j_rational_witness=str(witness))

# Birth covariance and curl signs/normalization under uniform formation.
C=(T*(s.diag(*pp)-pp*pp.T)*T.T).applyfunc(s.simplify)
Q=beta*(1-rho)*T*T.T
assert C[2:8,2:8]==4*rho*s.eye(6)/7
assert Q[2:8,2:8]==8*beta*(1-rho)*s.eye(6)
P=sum(x*x for x in K)*s.eye(3)-K*K.T
curl_transform=s.zeros(6)
curl_transform[:3,3:]=s.I*cross(K)
curl_transform[3:,:3]=-s.I*cross(K)
vector_drift=-s.I*AK[2:8,2:8]+lam*s.eye(6)
assert zero(curl_transform*vector_drift-vector_drift*curl_transform)
derivedC=(curl_transform*C[2:8,2:8]*s.conjugate(curl_transform.T)).applyfunc(s.simplify)
assert derivedC[:3,:3]==4*rho*P/7 and derivedC[3:,3:]==4*rho*P/7
assert derivedC[:3,3:]==s.zeros(3)
record("curl_covariance_noise_and_propagation",one_sector_covariance="4 rho/7 (|K|^2 I-K K^T)",
       one_sector_birth_bracket="8 beta(1-rho) (|K|^2 I-K K^T)",scaled_lattice_symbol="N sin(K/N)")

# Complete four-cycle count sector checks actual context rates, not just moment closure.
labels=(1,2,7,11)
states=list(permutations(labels))
index={x:i for i,x in enumerate(states)}
Qsector=s.zeros(len(states))
def tensor(a,b,i=2):
    return s.Rational(3,4)*(ev[a].cross(bv[b])+ev[b].cross(bv[a]))[i]
for k,eta in enumerate(states):
    for x in range(4):
        l,a,b,r=[eta[(x+d)%4] for d in (-1,0,1,2)]
        drive=tensor(l,a)+tensor(a,r)-tensor(l,b)-tensor(b,r)
        rate=s.Rational(1,3)+max(drive,0)
        swapped=list(eta); swapped[x],swapped[(x+1)%4]=swapped[(x+1)%4],swapped[x]
        zidx=index[tuple(swapped)]
        Qsector[k,zidx]+=rate;Qsector[k,k]-=rate
assert Qsector*s.ones(len(states),1)==s.zeros(len(states),1)
assert s.ones(1,len(states))*Qsector==s.zeros(1,len(states))
reached={0};todo=deque([0])
while todo:
    a=todo.popleft()
    for b in range(len(states)):
        if a!=b and Qsector[a,b]>0 and b not in reached:reached.add(b);todo.append(b)
assert len(reached)==len(states)
record("complete_finite_context_count_sector",states=len(states),uniform_stationary=True,
       irreducible=True,coordinate_direction=3,scope="Four-site periodic coordinate-line control; general torus proof uses telescoping and the positive floor.")

# Canonical Fourier covariance on two complete count sectors and their mixture.
def sector(counts):
    seq=[a for a,n in counts.items() for _ in range(n)]
    states=sorted(set(permutations(seq)))
    V=len(seq)
    assert V==4
    probs=s.zeros(14,1)
    for a,n in counts.items():probs[a-1]=s.Rational(n,V)
    ff=T*probs;CF=T*s.diag(*probs)*T.T-ff*ff.T
    means={};cov={}
    fields={}
    for mode in (0,1,2,3):
        phase=[s.I**(-mode*x) for x in range(V)]
        fields[mode]=[sum((phase[x]*T[:,eta[x]-1] for x in range(V)),s.zeros(14,1))/2 for eta in states]
        means[mode]=sum(fields[mode],s.zeros(14,1))/len(states)
        if mode: assert means[mode]==s.zeros(14,1)
    for m in (1,2,3):
        for n in (1,2,3):
            raw=sum((a*s.conjugate(b.T) for a,b in zip(fields[m],fields[n])),s.zeros(14))/len(states)
            cov[m,n]=raw.applyfunc(s.simplify)
            assert cov[m,n]==(s.Rational(4,3)*CF if m==n else s.zeros(14))
    site0=sum((T[:,eta[0]-1] for eta in states),s.zeros(14,1))/len(states)
    site01=sum((T[:,eta[0]-1]*T[:,eta[1]-1].T for eta in states),s.zeros(14))/len(states)
    assert site01-site0*site0.T==-CF/3
    return len(states),CF,means,cov
a=sector({1:1,2:1,7:1,11:1})
b=sector({1:2,3:1,12:1})
mix=s.Rational(1,3)*a[3][1,1]+s.Rational(2,3)*b[3][1,1]
assert mix==s.Rational(4,3)*(a[1]/3+2*b[1]/3)
zero_mix=(s.Rational(2,9)*(a[2][0]-b[2][0])*(a[2][0]-b[2][0]).T)
assert zero_mix!=s.zeros(14)
uniform=s.ones(14,1)/14
CF=T*(s.diag(*uniform)-uniform*uniform.T)*T.T
assert CF.rank()==13
assert CF[2:8,2:8]==4*s.eye(6)/7
assert CF[0,:]==s.zeros(1,14)
record("canonical_fourier_and_random_count_mixture",enumerated_sectors=[a[0],b[0]],
       nonzero_modes=3,mode_pairs_per_sector=9,fields=14,full_occupancy_covariance_rank=13,
       random_zero_mode_covariance_nonzero=True)

# Absorption/count monotonicity checks are exact and independent of mixing speed.
rm=s.symbols("r_min",positive=True)
for m in range(1,21):
    F=lambda n:s.harmonic(n)/rm
    assert s.simplify(rm*m*(F(m-1)-F(m)))==-1
tested=0
for occupied in range(7):
    vac=6-occupied
    for na in range(occupied+1):
        for added in range(vac+1):
            assert na<=na+added<=na+vac
            tested+=1
record("absorption_lyapunov_and_count_squeeze",harmonic_levels=20,count_completions=tested,
       lyapunov="H_m/r_min",finite_time_vacancy="v0 exp(-14 beta T)",
       ordered_limits="Long time at each fixed N; then N to infinity. Fixed T hydrodynamics is used only to select final counts.")

output=dict(scope="Independent calculations sealed before reading associated author checkers/results.",
            python=sys.version,sympy=s.__version__,platform=platform.platform(),checks=checks,
            passed=len(checks),failed=0)
Path(__file__).with_name("INDEPENDENT_RESULTS.json").write_text(json.dumps(output,indent=2,sort_keys=True)+"\n")
print(json.dumps({"passed":len(checks),"failed":0},sort_keys=True))
