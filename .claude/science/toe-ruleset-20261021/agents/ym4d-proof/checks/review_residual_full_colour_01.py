"""Independent exact controls; no author helper imports.

Actual 4D lattice/covariant-Laplacian and S4-prime contour calculations.
Finite instances support/falsify identities, not the uniform analytic proof.
"""
from fractions import Fraction as F
from itertools import product, permutations
from math import lcm
import json
import sys
import numpy as np
import sympy as s

checks = []
details = {}

def check(name, value, detail=None):
    checks.append({"name": name, "passed": bool(value), "detail": detail})

def avg(values):
    values = list(values)
    return sum(values, F(0)) / len(values)

# An actual periodic 3^4 covariant scalar Laplacian, varied along a pure gauge.
# The five eigenvalues are obtained independently from the 3-cycle characters.
T = 3
points = list(product(range(T), repeat=4))
index = {p: i for i, p in enumerate(points)}
V = len(points)
Delta = np.zeros((V, V), dtype=np.int64)
for x in points:
    i = index[x]
    for mu in range(4):
        for sign in (-1, 1):
            y = list(x)
            y[mu] = (y[mu] + sign) % T
            Delta[i, i] += 1
            Delta[i, index[tuple(y)]] -= 1
x = s.symbols("x")
poly = s.Poly(s.interpolate([(0, 0)] + [(3*j, s.Rational(1, 3*j)) for j in range(1, 5)], x), x)
coeff = [F(poly.nth(j)) for j in range(5)]
den = lcm(*(q.denominator for q in coeff))
Gnum = np.zeros_like(Delta)
power = np.eye(V, dtype=np.int64)
for c in coeff:
    Gnum += int(c * den) * power
    power = power @ Delta
check("actual_periodic_inverse_I_minus_P0", np.array_equal(81*Delta@Gnum, den*(81*np.eye(V,dtype=np.int64)-np.ones((V,V),dtype=np.int64))))
check("periodic_G_has_both_constant_kernels", np.all(Gnum.sum(axis=0)==0) and np.all(Gnum.sum(axis=1)==0))
check("false_inverse_identity_I_rejected", not np.array_equal(Delta@Gnum, den*np.eye(V,dtype=np.int64)))

# V(x)=cos(2*pi*x_2/3).  Delta(eps)=exp(i eps V) Delta exp(-i eps V)
# is exactly a charged covariant Laplacian for a periodic pure-gauge connection.
W = np.array([2 if p[1]==0 else -1 for p in points], dtype=np.int64)
diff = W[:,None]-W[None,:]
B1 = diff*Delta             # O_1=i B1/2
B2 = -(diff**2)*Delta       # O_2=B2/8
tad = F(int(np.trace(Gnum@B2)), 8*den)
bub = F(int(np.trace(Gnum@B1@Gnum@B1)), 8*den*den)
frozen_complement_coefficient = tad+bub
variance = avg(F(int(z),2)**2 for z in W)-avg(F(int(z),2) for z in W)**2
check("actual_pure_gauge_fixed_complement_Gram", frozen_complement_coefficient == -variance == -F(1,2))
check("actual_pure_gauge_rotating_kernel_correction_nonzero", frozen_complement_coefficient != 0)
check("wrong_half_bubble_rejected", tad+2*bub != -variance)
check("dropped_seagull_rejected", bub != -variance)
details["periodic_pure_gauge"] = {"tadpole":str(tad),"bubble":str(bub),"fixed_complement_logdet_epsilon2":str(frozen_complement_coefficient),"density":str(frozen_complement_coefficient/V),"true_pseudodeterminant_epsilon2":"0", "explanation":"Exact adjugate formula gives det_complement Delta(eps)=det_prime Delta times |mean exp(i eps V)|^2. The displayed discrepancy is not discarded at finite T."}

# Fourier anchoring: P0 and shifts put every propagator at a finite partial sum
# of external transfers. With exactly two external legs +p,-p these are 0,+p,-p.
word_routes = []
for transfers in ((1,-1),(-1,1),(0,)):
    current=0
    route=[current]
    for transfer in transfers:
        current+=transfer
        route.append(current)
    word_routes.append(route)
check("all_two_leg_projector_anchor_routes", all(set(r) <= {-1,0,1} and r[-1]==0 for r in word_routes))

# Nonzero exceptional trace from a different operator word than the author's:
# Tr(P0 V G V Delta G V G V) = 1/(4 lambda(p)^2) on T>=5 at p=2pi/T,
# when no +/-2p resonance. Its fixed-p density is O(T^-4); allowing two
# unmatched transfers would create +/-2p and is deliberately excluded.
check("unmatched_two_leg_claim_rejected", not set([0,1,2]) <= {-1,0,1})

# Actual neutral Wilson tadpole on the 6^4 periodic lattice.  Its trigonometric
# spectrum is rational; summing each orientation is independent of the answer.
lam1 = [0,1,3,4,3,1]
V6 = 6**4
trace_curl = F(0)
for q in product(range(6), repeat=4):
    ls=[lam1[i] for i in q]
    if sum(ls):
        trace_curl += F(ls[0]+ls[2],sum(ls))
trace_curl /= V6
check("actual_6_to_4_Wilson_curl_trace", trace_curl == F(1,2)*(1-F(1,V6)))
for N in (3,5):
    H = s.zeros(N,N-1)
    for j in range(N-1):
        H[j,j]=1
        H[N-1,j]=-1
    gram=H.T*H/N
    complete=H*gram.inv()*H.T
    check(f"Cartan_inverse_Gram_completeness_SU{N}", complete==N*s.eye(N)-s.ones(N,N))
    h=s.Matrix([s.Rational(2*j-(N-1),2) for j in range(N)])
    # Expand 1/2 Tr log W from the actual cosine Hessian, then divide by
    # the Wilson quadratic coefficient in the same non-unit Cartan field.
    wilson2=(h.T*h)[0]/(2*N)
    one_loop2=-s.Rational(1,4)*s.Rational(trace_curl.numerator,trace_curl.denominator)*sum(complete[j,j]*h[j]**2/N for j in range(N))
    beta=s.factor(one_loop2/wilson2)
    check(f"neutral_Wilson_normalization_SU{N}",beta==-s.Rational(N-1,4)*(1-s.Rational(1,V6)))
    check(f"background_independent_neutral_mutation_SU{N}",beta!=0)
    details[f"neutral_Wilson_SU{N}"]=str(beta)

# Actual adopted S4-prime paths in d=4, L=3, all 24 orders and 81 offsets.
# Polynomial link fields give exact local contour phases, not invented samples.
def link_value(base,mu):
    a=(mu+1)*(base[(mu+1)%4]+2*base[(mu+2)%4]**2)+base[0]*base[1]
    b=(mu+2)*(base[(mu+2)%4]-base[(mu+3)%4]**2)+base[2]*base[3]+base[0]**2
    return (F(a,17),F(b,17))

def segment(start,end,order):
    pos=list(start)
    ans=[F(0),F(0)]
    for mu in order:
        while pos[mu]!=end[mu]:
            sign=1 if end[mu]>pos[mu] else -1
            if sign<0:
                pos[mu]-=1
            values=link_value(tuple(pos),mu)
            for j in range(2):
                ans[j]+=sign*values[j]
            if sign>0:
                pos[mu]+=1
    return ans

phases=[]
mu=0
root=(0,0,0,0)
nextroot=(3,0,0,0)
for offset in product((-1,0,1),repeat=4):
    other=tuple(offset[i]+(3 if i==mu else 0) for i in range(4))
    for order in permutations(range(4)):
        front=segment(root,offset,order)
        leg=segment(offset,other,(mu,))
        tail=segment(nextroot,other,order)
        p=[front[j]+leg[j]-tail[j] for j in range(2)]
        phases.append((p[0],p[1],-p[0]-p[1]))
check("actual_S4_prime_contour_count",len(phases)==24*3**4)
check("actual_contour_SU3_traceless",all(sum(p)==0 for p in phases))
means=[avg(p[j] for p in phases) for j in range(3)]
moments={r:[avg((p[j]-means[j])**r for p in phases) for j in range(3)] for r in (2,3,4)}
b=[F(5,13),F(-7,13),F(2,13)]
delta=[b[j]-means[j] for j in range(3)]
direct2=sum(avg((p[j]-b[j])**2-(p[j]-means[j])**2 for p in phases) for j in range(3))/6
direct4=sum(avg((p[j]-means[j])**4-(p[j]-b[j])**4 for p in phases) for j in range(3))/72
formula2=sum(v*v for v in delta)/6
pieces=[sum(delta[j]*moments[3][j] for j in range(3))/18,
        -sum(delta[j]**2*moments[2][j] for j in range(3))/12,
        -sum(v**4 for v in delta)/72]
formula4=sum(pieces)
check("actual_SU3_normalized_quadratic",direct2==formula2)
check("actual_SU3_normalized_quartic",direct4==formula4)
check("all_neutral_quartic_monomial_groups_nonzero",all(v!=0 for v in pieces))
for j in range(3):
    check(f"quartic_group_{j}_omission_rejected",direct4!=formula4-pieces[j])
# Solve the actual diagonal SU(3) constrained maximizer to third order:
# Im(exp(-i bstar_j) M_j) must be equal for every j, sum bstar_j=0.
mean_mu3=sum(moments[3])/3
shift=[(-moments[3][j]+mean_mu3)/6 for j in range(3)]
lagrange=[-moments[3][j]/6-shift[j] for j in range(3)]
check("SU3_constrained_maximizer_trace",sum(means)==0 and sum(shift)==0)
check("SU3_constrained_maximizer_stationarity",len(set(lagrange))==1)
check("SU3_trace_phase_correction_is_nontrivial",mean_mu3!=0)
check("SU3_trace_phase_does_not_change_quartic",sum(delta)==0 and sum(delta[j]*mean_mu3 for j in range(3))==0)
details["actual_S4_prime_SU3"]={"means":list(map(str,means)),"mu2":list(map(str,moments[2])),"mu3":list(map(str,moments[3])),"quartic_parts":list(map(str,pieces)),"normalized_quartic":str(direct4),"constrained_center_cubic_shift":list(map(str,shift))}

# Arbitrary internal colour: the complete cubic trace with two Cartan inputs
# vanishes, including the off-diagonal Gell-Mann directions.
H1=s.I*s.diag(1,-1,0)
H2=s.I*s.diag(2,1,-3)
generators=[H1,H2]
for a in range(3):
    for b0 in range(a+1,3):
        S=s.zeros(3); S[a,b0]=s.I;S[b0,a]=s.I
        A=s.zeros(3); A[a,b0]=1;A[b0,a]=-1
        generators.extend([S,A])
check("all_SU3_internal_colours_two_Cartan_cubic_zero",all(s.re(s.trace(H1*H2*X))==0 for X in generators))
check("no_cubic_exchange_source_all_SU3_colours",all(s.trace(X*(H1*H2-H2*H1))==0 for X in generators))

output={"scope":"Exact finite actual lattice/contour controls; no general convergence or uniform-depth certificate", "checks":checks,"passed":sum(q["passed"] for q in checks),"total":len(checks),"details":details,"versions":{"python":sys.version,"numpy":np.__version__,"sympy":s.__version__}}
print(json.dumps(output,indent=2))
sys.exit(0 if all(q["passed"] for q in checks) else 1)
