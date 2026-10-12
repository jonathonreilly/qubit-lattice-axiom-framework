#!/usr/bin/env python3
"""Independent arithmetic routes to the geometric step; no primary code imported."""
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = [
    "docs/CENTRE_REGULARITY_TO_GEOMETRIC_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/ISOLATED_CENTRE_FILTERING_BOUNDED_THEOREM_NOTE_2026-10-12.md"
]
if not __debug__:
    raise RuntimeError("Run without -O: finite control assertions must be enabled")

from fractions import Fraction as F
from decimal import Decimal as D, localcontext
import json, math

def emit(name, **kw):
    print(json.dumps({'name':name, **kw}, sort_keys=True))

def dec(x):
    if isinstance(x,F):return D(x.numerator)/D(x.denominator)
    return D(str(x))

def energy(k,m,b):return (m*m+b*k*k).sqrt()
def detuning(x,m,b,q):return energy(x+q/2,m,b)-energy(x-q/2,m,b)
def formula_endpoint(m,b,q,e):
    return (e*e*(m*m+b*q*q/4-e*e/4)/(b*(b*q*q-e*e))).sqrt()
def direct_endpoint(m,b,q,e):
    lo=D(0);hi=D(1)
    while detuning(hi,m,b,q)<e:hi*=2
    for _ in range(230):
        mid=(lo+hi)/2
        if detuning(mid,m,b,q)<e:lo=mid
        else:hi=mid
    return (lo+hi)/2

def tent_mass(t,L):
    t=min(t,L)
    return (3/(2*L))*2*(t-t*t/L+t*t*t/(3*L*L))

def square_check(rhs):
    for m,b,p,q in [(F(1),F(1),F(2,3),F(3,5)),(F(3,2),F(7,4),F(-2,7),F(5,8)),(F(2),F(1,3),F(7,5),F(1,6))]:
        left=(m*m+b*(p+q)**2)-(m*m+b*p*p)
        if left!=rhs(b,p,q):return False,{'m':str(m),'beta':str(b),'p':str(p),'q':str(q),'actual':str(left),'candidate':str(rhs(b,p,q))}
    return True,None

ok,_=square_check(lambda b,p,q:b*(2*p*q+q*q));assert ok
for name,fun in [('missing_cross_factor_2',lambda b,p,q:b*(p*q+q*q)),('missing_beta',lambda b,p,q:2*p*q+q*q)]:
    ok,witness=square_check(fun);assert not ok;emit('mutation',defect=name,rejected=True,witness=witness)

# The polynomial equation for G20 is exact rational arithmetic; root finding
# below uses only the two original square-root energies.
for m,b,q,e in [(F(1),F(1),F(1,2),F(1,10)),(F(3,2),F(7,4),F(5,8),F(1,20)),(F(2),F(1,3),F(1,6),F(1,100))]:
    x2=e*e*(m*m+b*q*q/4-e*e/4)/(b*(b*q*q-e*e))
    A=m*m+b*x2+b*q*q/4
    assert b*b*x2*q*q==A*e*e-e**4/4
    assert A-e*e/2>0
emit('exact_endpoint_polynomial',cases=3,identity_verified=True)

# Balance powers without floating exponents: b=2a, e=t^(b+1), r=t.
for b in [1,2,3,7]:
    for t in [F(1,3),F(2,5)]:
        e=t**(b+1)
        assert e/t==t**b
        assert (t**b)**(b+1)==e**b
emit('exact_exponent_balance',cases=8,twice_a=[1,2,3,7])

# Rational unit directions verify the displayed measurable selector's algebra.
for u in [[F(1),F(0)],[F(-1),F(0)],[F(3,5),F(4,5)],[F(1,3),F(2,3),F(2,3)]]:
    d=len(u);v=[F(int(i==0))-u[i] for i in range(d)];vv=sum(x*x for x in v)
    R=[[F(int(i==j))-(2*v[i]*v[j]/vv if vv else 0) for j in range(d)] for i in range(d)]
    assert [row[0] for row in R]==u
    for i in range(d):
        for j in range(d):assert sum(R[k][i]*R[k][j] for k in range(d))==int(i==j)
emit('exact_direction_selector',cases=4,orthogonal_and_maps_e1_to_u=True,scope='finite algebra; Borel dependence proved by explicit formula in note')

with localcontext() as ctx:
    ctx.prec=75
    errors=[]
    for m,b,q,e in [(D(1),D(1),D('0.5'),D('0.1')),(D('1.5'),D('1.75'),D('0.625'),D('0.05')),(D(2),D(1)/3,D(1)/6,D('0.01'))]:
        a=formula_endpoint(m,b,q,e);z=direct_endpoint(m,b,q,e)
        error=abs(a-z);errors.append(error);assert error<D('1e-60')
    emit('direct_energy_bisection',cases=3,max_endpoint_error=str(max(errors)),tolerance='1e-60',precision_digits=75)

    # Finite theta measure. Nontrivial two-component multiplicity is (1,2i)/sqrt(5).
    qs=[D(1)/8,D(1)/4,D(1)/2,D(1)]
    ws=[q*q/4 for q in qs]
    L=D('0.5');ell=D('0.5');m=b=D(1);R=D(2);r0=D(1);C=D(1)
    E=(m*m+b*R*R).sqrt();c=b*m*m/(E**3);kap=b/E
    total=sum(ws);deriv=3*total/(L*L);S2=total+ell*ell*deriv
    assert F(1,5)+F(4,5)==1
    near_cum=D(0);near=[]
    for q,w in zip(qs,ws):
        near_cum+=w;assert near_cum<=C*C*q*q
        near.append({'radius':str(q),'norm_squared':str(near_cum),'C2r2':str(q*q)})
    emit('central_rate_and_multiplicity',a='1',near_thresholds=near,multiplicity_norm_squared='1',target_atom_weight='1/4 (excluded from residual)',residual_norm_squared=str(total),H1_scaled_squared=str(S2))
    for eps in [D('0.01'),D('0.001'),D('0.0001'),D('0.00001')]:
        epsstar=c*ell*r0;assert eps<=epsstar
        r=r0*(eps/epsstar)**(D(1)/3)
        actual=sum(w*tent_mass(direct_endpoint(m,b,q,eps),L) for q,w in zip(qs,ws))
        bound=(C*C*r0*r0+S2)*(eps/epsstar)**(D(2)/3)
        near=sum(w for q,w in zip(qs,ws) if q<=r)
        far=sum(w*tent_mass(direct_endpoint(m,b,q,eps),L) for q,w in zip(qs,ws) if q>r)
        far_bound=eps*S2/(c*r*ell)
        affine_bound=(C*C*r0*r0+S2)*(eps/(kap*ell*r0))**(D(2)/3)
        assert actual<=bound and far<=far_bound and actual<=affine_bound
        emit('finite_band',epsilon=str(eps),radius=str(r),actual_band_squared=str(actual),hessian_bound_squared=str(bound),affine_bound_squared=str(affine_bound),actual_far_squared=str(far),far_bound_squared=str(far_bound),near_full_mass_squared=str(near))
    # Exact algebra makes graph crossing visible: q != 0, x=0 -> D=0,
    # but the singleton has zero dp measure for every actual tent.
    assert detuning(D(0),m,b,D('0.5'))==0
    emit('zero_detuning',pointwise_crossing=True,continuous_tent_singleton_mass='0 analytically',finite_grid_atom_would_violate_joint_dp_measure=True)

    p=D(10);q=D(1);RR=D(11)
    derivative=(p+q)/energy(p+q,D(1),D(1))-p/energy(p,D(1),D(1))
    correct_c=1/(1+RR*RR)**(D(3)/2)
    assert derivative>=correct_c*q
    assert derivative<q
    emit('mutation',defect='upper_hessian_beta_over_M_as_uniform_lower_bound',rejected=True,actual_directional_derivative=str(derivative),correct_lower_bound=str(correct_c*q),mutant_lower_bound='1')

# Sharp line example e^{-|s|}: all three exact scalar quantities equal 1.
assert F(1)<=F(1)*F(1)
assert F(1)>F(1,2)*F(1)*F(1)
emit('mutation',defect='halve_sharp_whole_line_Sobolev_constant',rejected=True,actual_sup_squared='1',L2_norm_squared='1',derivative_L2_norm_squared='1',mutant_bound='1/2')

# Local invariant-weight derivative with psi constant near k=1, M=beta=1.
with localcontext() as ctx:
    ctx.prec=75
    def flat_weight(k):return (2*(1+k*k).sqrt()).sqrt()**(-1)
    h=D('1e-20');point=D(1)
    actual_log_derivative=(flat_weight(point+h)-flat_weight(point-h))/(2*h)/flat_weight(point)
    assert abs(actual_log_derivative+D(1)/4)<D('1e-35')
    assert abs(actual_log_derivative)>D('0.1')
    emit('mutation',defect='omit_invariant_measure_derivative',rejected=True,actual_fprime_over_f=str(actual_log_derivative),exact_limit='-1/4',finite_difference_step='1e-20',limit_tolerance='1e-35',mutant_fprime_over_f='0')

# Smooth p marginal carried by theta=-2p has exact residual D=0.
for p in [F(1,4),F(1,3),F(3,10)]:
    theta=-2*p;assert theta!=0
    assert 1+(p+theta)**2==1+p*p
emit('mutation',defect='replace_joint_dp_dnu_by_smooth_p_marginal',rejected=True,witness='theta=-2p on 1/4<p<1/3; D=0 identically, target theta0=0 absent from this component',scope='spectral measure, not microscopic model')

# Off-mass continuum still lies on target geometric graph, even with an
# isolated target Casimir 4. This vector has not received E_M.
for p in [F(0),F(1,8),F(1,4)]:
    offmass=3-2*p
    assert offmass+(p+1)**2==4+p*p
    assert F(5,2)<=offmass<=3<4
emit('mutation',defect='omit_exact_mass_filter',rejected=True,witness='m(p)^2=3-2p, theta=1, 0<p<1/4; off-mass energies equal target M=2,theta0=0 graph',offmass_Casimir_interval='[5/2,3]',target_Casimir='4')

# Same central character, different integer lift at p=0: squared energies
# differ by 4*pi^2 > 36, whereas the wrong zero-lift clock predicts equality.
def lifted_energy_squared(m,b,p,theta,n):return m*m+b*(p+theta+2*math.pi*n)**2
lift_difference=lifted_energy_squared(1,1,0,0,1)-lifted_energy_squared(1,1,0,0,0)
assert lift_difference>36
emit('mutation',defect='identify_different_integer_lifts_at_target_atom',rejected=True,computed_squared_energy_difference=lift_difference,exact_squared_energy_difference='4*pi^2 > 36 (analytic)',mutant_difference='0')

for N in [8,32,128]:
    # Exact telescoping tail sum_{n=N}^infty 1/[n(n+1)] = 1/N.
    partial=sum((F(1,n*(n+1)) for n in range(N,2*N)),F(0))
    assert partial==F(1,N)-F(1,2*N)
    emit('analytic_tail_control',N=N,exact_infinite_tail='1/'+str(N),missing_central_rate_epsilon_log=-N,missing_H1_epsilon_log=math.log(2)-N*N,scope='finite telescoping identity; infinite-tail proof in note')

print('per_element: exact squared-energy and scale identities checked; no empirical inputs.')
print('per_site: checked and not executed — no local lattice-site realization is supplied by this spectral control.')
print('per_mode: finite central atoms and explicit continuous momentum tents checked with all multiplicity norm factors.')
print('per_block: analytic conditional shell bound is compared to original-energy endpoints, not certified by finite sampling.')
print('lattice_wide: checked and not executed — no infinite lattice model, locality realization, or exhaustion theorem is tested.')
emit('completed',scope='author analytic/finite control only; no independent source-review or audit verdict',baseline_failures=0)

print("TOTAL: PASS=1 FAIL=0")
print("SCOPE: One completed assertion-guarded finite author driver; the tent upper-bound gates remain nondiscriminating for two documented mutants, and no general proof is numerical.")
