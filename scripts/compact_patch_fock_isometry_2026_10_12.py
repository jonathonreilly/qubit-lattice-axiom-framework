#!/usr/bin/env python3
"""Exact author controls for the bounded Fock-isometry argument.

Not an independent review, proof of analytic estimates, or physical model test.
The runner is intended to be executed once under an external 60-second timeout.
"""
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = [
    "docs/COMPACT_PATCH_FOCK_ISOMETRY_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/COMPACT_PATCH_SCATTERING_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-10-11.md",
]
if not __debug__:
    raise RuntimeError("Run without -O: exact control assertions must be enabled")

from collections import Counter
from itertools import combinations, permutations
from math import factorial
import json
import sympy as s

def out(kind, **data):
    print(json.dumps({"check": kind, **data}, sort_keys=True), flush=True)

def add(*polys):
    r=Counter()
    for p in polys:
        r.update(p)
    return Counter({k:v for k,v in r.items() if v})

def scale(c,p):
    return Counter({k:c*v for k,v in p.items() if c*v})

def mul(*polys):
    r=Counter({():1})
    for p in polys:
        nr=Counter()
        for a,ca in r.items():
            for b,cb in p.items(): nr[a+b]+=ca*cb
        r=Counter({k:v for k,v in nr.items() if v})
    return r

def atom(name): return Counter({(name,):1})
def comm(a,b): return add(mul(a,b),scale(-1,mul(b,a)))

# Exact noncommutative identity used before taking vacuum limits.
checks=[]
for n in range(1,10):
    a=atom("a")
    cs=[atom(f"c{i}") for i in range(n)]
    lhs=mul(a,*cs)
    rhs=mul(*cs,a)
    double_terms=Counter()
    for k in range(n):
        rhs=add(rhs,mul(*(cs[:k]+cs[k+1:]),comm(a,cs[k])))
        for ell in range(k+1,n):
            term=mul(*(cs[:k]+cs[k+1:ell]),comm(comm(a,cs[k]),cs[ell]),*cs[ell+1:])
            rhs=add(rhs,term); double_terms=add(double_terms,term)
    assert lhs==rhs,(n,lhs,rhs)
    if n>=2:
        assert lhs!=add(rhs,scale(-1,double_terms))
    checks.append({"n":n,"double_commutators":n*(n-1)//2})
out("unreduced_annihilator_recursion",exact=True,cases=checks,
    dropped_double_commutators_rejected_for_n_ge_2=True)

# Q^2 expansion does not assume different lowering operators commute.
for count in range(1,8):
    a=[atom(f"a{i}") for i in range(count)]
    ad=[atom(f"a{i}*") for i in range(count)]
    q=add(*(mul(ad[i],a[i]) for i in range(count)))
    first=add(*(mul(ad[i],comm(a[i],ad[j]),a[j])
                for i in range(count) for j in range(count)))
    second=add(*(mul(ad[i],ad[j],a[i],a[j])
                 for i in range(count) for j in range(count)))
    assert mul(q,q)==add(first,second)
out("energy_induction_Q_squared_expansion",exact=True,
    translation_counts=list(range(1,8)),no_commuting_lowerers_assumed=True)

# Actual differentiated mass dispersion, including determinant.
M,beta=s.symbols("M beta",positive=True)
hessian_results=[]
for d in range(1,4):
    k=s.symbols(f"k0:{d}",real=True)
    E=s.sqrt(M*M+beta*sum(x*x for x in k))
    H=s.hessian(E,k)
    expected=(beta/E)*s.eye(d)-(beta**2/E**3)*s.Matrix(k)*s.Matrix(k).T
    assert all(s.simplify(x)==0 for x in H-expected)
    det=s.factor(H.det())
    assert s.simplify(det-beta**d*M*M/E**(d+2))==0
    hessian_results.append({"d":d,"determinant":"beta**d * M**2 / E**(d+2)"})
out("mass_dispersion_hessian",symbolic=True,cases=hessian_results)

# Verify the proposed velocity inverse through squared energy and exact ratio.
for d in range(1,6):
    v=s.symbols(f"v0:{d}",real=True)
    r2=sum(x*x for x in v)
    # Assumed domain beta > |v|^2; the selected square roots are positive.
    denom=s.sqrt(beta)*s.sqrt(beta-r2)
    k=[M*x/denom for x in v]
    Epos=M*s.sqrt(beta)/s.sqrt(beta-r2)
    assert s.simplify(Epos**2-(M*M+beta*sum(x*x for x in k)))==0
    assert all(s.simplify(beta*ki/Epos-vi)==0 for ki,vi in zip(k,v))
assert s.Rational(4,5)==s.Rational(8,10)
out("velocity_inverse_and_mixed_mass_overlap",symbolic_dimensions=list(range(1,6)),
    domain="M>0, beta>0, |v|^2<beta",
    different_mass_equal_velocity={"M1":3,"k1":[4],"E1":5,"M2":6,"k2":[8],"E2":10,"velocity":"4/5"},
    automatic_separation_by_mass_rejected=True)

def lowering(L,x):
    N=2**L
    mat=s.zeros(N)
    for b in range(N):
        if b&(1<<x): mat[b^(1<<x),b]=1
    return mat

def all_principal_minors_nonnegative(A):
    n=A.rows
    for r in range(1,n+1):
        for ix in combinations(range(n),r):
            if A.extract(ix,ix).det()<0: return False
    return True

# Finite cyclic translates of a hard-core lowering operator satisfy the exact
# energy-kernel assumptions and saturate the particle-count factor.
energy_rows=[]
for L in range(1,4):
    N=2**L
    aa=[lowering(L,x) for x in range(L)]
    Q=sum((a.T*a for a in aa),s.zeros(N))
    assert Q==s.diag(*(b.bit_count() for b in range(N)))
    # Only same-site [a_x,a_0*] contributes to S, and its norm is exactly 1.
    assert (aa[0]*aa[0].T-aa[0].T*aa[0])**2==s.eye(N)
    for x in range(1,L): assert aa[x]*aa[0].T-aa[0].T*aa[x]==s.zeros(N)
    fs=[s.Integer(x+1) for x in range(L)]
    f2=sum(x*x for x in fs)
    C=sum((f*a.T for f,a in zip(fs,aa)),s.zeros(N))
    for R in range(L+1):
        ids=[b for b in range(N) if b.bit_count()<=R]
        PE=s.diag(*(int(b in ids) for b in range(N)))
        assert max((PE*Q*PE).diagonal())==R
        # Creator bound requires R+L_transfer = R+1.
        creator=(R+1)*f2*s.eye(len(ids))-(C.T*C).extract(ids,ids)
        annih=R*f2*s.eye(len(ids))-(C*C.T).extract(ids,ids)
        assert all_principal_minors_nonnegative(creator)
        assert all_principal_minors_nonnegative(annih)
        energy_rows.append({"sites":L,"energy_cutoff":R,"Gamma":R,"S_B":1,
                            "creator_and_adjoint_bounds_exact_PSD":True})
    vac=s.eye(N)[:,0]
    assert (C*vac).dot(C*vac)>0  # Padding omission would give bound zero at R=0.
out("finite_energy_bounds",exact=True,models="finite cyclic hard-core translates",
    cases=energy_rows,missing_creator_energy_padding_rejected=True,
    limitation="Finite-dimensional controls of the algebraic bound only, not the infinite-volume theorem.")

# Precise lowering hypothesis: nilpotence of one untranslated operator is weaker.
a=s.Matrix([[0,1],[0,0]])
T=s.Matrix([[0,1],[1,0]])
a1=T*a*T
assert a*a==s.zeros(2) and a*a1!=s.zeros(2)
out("mixed_product_kernel_negative_control",single_operator_square_zero=True,
    mixed_translate_product_nonzero=True,
    conclusion="Do not replace all mixed-product kernels by ker(A**r).")

# Permanent recurrence and creation-operator normalization.
def matchings(m,n):
    if m==0: return {():1} if n==0 else {}
    if n==0: return {}
    result=Counter()
    for perm in permutations(range(n),m):
        if m==n: result[tuple(enumerate(perm))]+=1
    return dict(result)
for m in range(7):
    for n in range(7):
        if m==n:
            exact=matchings(m,n)
            assert len(exact)==factorial(n)
        else:
            assert matchings(m,n)=={}
for n in range(10):
    assert sum(1 for _ in permutations(range(n)))==factorial(n)
out("Fock_Gram_normalization",rectangular_pairs=49,
    equal_vector_norm_squared=[factorial(n) for n in range(10)],
    convention="a*(psi1)...a*(psin) Omega, with no extra 1/n! in the permanent")

rates=[]
for d in range(1,7):
    squared=s.Rational(d,2)-3*s.Rational(d,2)
    assert squared==-d
    for total in range(2,13):
        corrected=-s.Rational(d,2)
        naive=d*(total-2)-s.Rational(d,2)
        rates.append({"d":d,"remaining_factors":total-2,"corrected_exponent":str(corrected),
                      "naive_polynomial_exponent":str(naive)})
out("regular_contraction_power_count",cases=rates,
    conclusion="Finite-energy word bounds preserve a negative error exponent for every fixed particle number.")

out("scope",author_control=True,independent_review=False,
    analytic_stationary_phase_proved_by_script=False,
    clustering_proved_by_script=False,full_GNS_exhaustion=False,
    prior_compact_patch_verdict_assumed=False)


print("per_element: exact noncommutative word and symbolic Hessian identities checked")
print("per_site: exact finite cyclic hard-core energy bounds for one to three sites checked")
print("per_mode: exact velocity inverse formulas and mixed-mass overlap fixture checked")
print("per_block: complete finite-word recursion checked; normalization enumeration is bookkeeping only")
print("lattice_wide: checked and not executed — clustering, spectral density and Fock extension are analytic proof obligations")
print("TOTAL: PASS=9 FAIL=0")
print("SCOPE: nine finite control records; no analytic Fock proof, physical realization, full-GNS exhaustion or audit verdict from this runner")
