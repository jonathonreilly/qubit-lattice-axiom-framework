#!/usr/bin/env python3
"""Literal author finite controls for the memory/current publication candidate.

Five frozen helpers execute in separate namespaces. This replay supplies exact
finite algebra and explicitly floating controls, not a new independent proof
of the continuum spectral, wave-operator, or growing-time theorem.
"""
import hashlib
import json

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = [
    "docs/EXCLUDED_WALK_MEMORY_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-11.md",
    "docs/EXCLUDED_WALK_PROJECTED_FREE_BAND_CANONICAL_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-11.md",
    "docs/EXCLUDED_WALK_LOW_ENERGY_ENERGY_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-11.md",
]

MEMORY_CONTROLS_SOURCE = r'''"""Selective independent-form controls; finite examples do not prove continuum decay."""
import json
import platform
import numpy as np
import scipy
from scipy.linalg import expm
from scipy.integrate import quad
import sympy as sp

checks = 0


def check(name, condition, detail=None):
    global checks
    assert bool(condition), name
    checks += 1
    print(json.dumps({'check': name, 'detail': detail}))


def zero(x):
    if isinstance(x, sp.MatrixBase):
        return all(sp.simplify(y) == 0 for y in x)
    return sp.simplify(x) == 0


I = sp.I
f, h, z = sp.symbols('f h z', real=True, nonzero=True)
D = sp.Matrix([[0, -I*f], [I*f, 0]])
g = sp.Matrix([I*h, 0])
A = D.row_join(g).col_join(g.conjugate().T.row_join(sp.zeros(1)))
e = sp.Matrix([0, 0, 1])
check('direct_block_selfadjoint', zero(A-A.conjugate().T))
direct_resolvent = ((z*sp.eye(3)-A).inv())[2, 2]
self_energy = h**2*z/(z**2-f**2)
scalar_resolvent = 1/(z-self_energy)
check('Schur_sign_and_denominator', zero(direct_resolvent-scalar_resolvent))
check('balanced_helicity_weights', zero((g.conjugate().T*D*g)[0]))

# An independently expanded three-by-three exponential gives a nondecaying
# finite bath, instead of assigning a survival amplitude by the memory formula.
A1 = A.subs({f: sp.Rational(3, 5), h: sp.Rational(4, 5)})
t, s = sp.symbols('t s', real=True)
check('finite_fixture_cubic', zero(A1**3-A1))
U1 = sp.eye(3)-I*sp.sin(t)*A1+(sp.cos(t)-1)*A1**2
check('finite_fixture_exponential_ODE', zero(I*sp.diff(U1, t)-A1*U1))
a1 = (e.T*U1*e)[0]
K1 = (g.conjugate().T*(sp.cos(f*t)*sp.eye(2)-I*sp.sin(f*t)*D/f)*g)[0]
K1 = sp.simplify(K1.subs({f: sp.Rational(3, 5), h: sp.Rational(4, 5)}))
conv = sp.integrate(K1.subs(t, t-s)*a1.subs(t, s), (s, 0, t))
check('Volterra_sign_actual_matrix', zero(sp.diff(a1, t)+conv))
check('finite_bath_exact_recurrence', zero(a1.subs(t, 2*sp.pi)-1))
zero_projection = sp.eye(3)-A1**2
atom = (e.T*zero_projection*e)[0]
check('finite_bath_nonzero_dressing_atom', atom > 0, str(atom))
check('finite_bath_not_exponential_decay', zero(sp.diff(a1, t).subs(t, 0)) and
      sp.diff(a1, t, 2).subs(t, 0) < 0, str(a1))

# Two distinct bath frequencies: direct powers and matrix inversion are compared
# with the convolution recurrence and scalar expression, with no imported code.
freqs = [sp.Rational(2, 3), sp.Rational(5, 7)]
couplings = [sp.Rational(1, 4), sp.Rational(2, 5)]
D2 = sp.diag(*[sp.Matrix([[0, -I*x], [I*x, 0]]) for x in freqs])
g2 = sp.Matrix([I*couplings[0], 0, I*couplings[1], 0])
A2 = D2.row_join(g2).col_join(g2.conjugate().T.row_join(sp.zeros(1)))
e2 = sp.Matrix([0, 0, 0, 0, 1])
za = sp.Rational(2, 5)+I*sp.Rational(3, 7)
m2_direct = ((za*sp.eye(5)-A2).inv())[4, 4]
m2_scalar = 1/(za-sum(y*y*za/(za*za-x*x) for x, y in zip(freqs, couplings)))
check('two_frequency_resolvent', zero(m2_direct-m2_scalar))
ad = [sp.simplify((e2.T*((-I*A2)**n)*e2)[0]) for n in range(14)]
kd = [sp.simplify((g2.conjugate().T*((-I*D2)**n)*g2)[0]) for n in range(12)]
check('convolution_derivative_moments', all(zero(ad[n+1]+
      sum(kd[j]*ad[n-1-j] for j in range(n))) for n in range(1, 12)))
check('dressing_even_moments', all(zero(ad[n]) for n in range(1, 14, 2)))

# At nonzero times a fresh quadrature of the eliminated-field formula is
# compared with the full matrix exponential; this is a floating finite control.
An = np.array(A2, dtype=complex)
Dn = np.array(D2, dtype=complex)
gn = np.array(g2, dtype=complex).ravel()
en = np.array(e2, dtype=complex).ravel()
errors = []
for time in [0.3, 2.1, 7.0]:
    psi = expm(-1j*time*An)@en
    def alpha(x):
        return (expm(-1j*x*An)@en)[-1].real
    un = np.empty(4, dtype=complex)
    for j in range(4):
        fun = lambda x: (-1j*expm(-1j*(time-x)*Dn)@gn)[j]*alpha(x)
        un[j] = quad(lambda x: fun(x).real, 0, time, epsabs=2e-11)[0]+1j*quad(
            lambda x: fun(x).imag, 0, time, epsabs=2e-11)[0]
    p_memory = 0.0
    for omega, coupling in zip(map(float, freqs), map(float, couplings)):
        C = quad(lambda x: np.cos(omega*(time-x))*alpha(x), 0, time, epsabs=2e-11)[0]
        S = quad(lambda x: np.sin(omega*(time-x))*alpha(x), 0, time, epsabs=2e-11)[0]
        p_memory += coupling**2*(C*C+S*S)
    errors.append(max(np.linalg.norm(un-psi[:-1]),
                      abs(p_memory-np.vdot(psi[:-1], psi[:-1]).real),
                      abs(p_memory-(1-abs(psi[-1])**2))))
check('field_and_transfer_integrals_floating', max(errors) < 2e-10, errors)

# Exact constants in the cone proof are derived from the Jacobian integral.
H = sp.Rational(23, 24)
check('cone_derivative_constant_four', sp.Rational(13, 6)/H+
      sp.Rational(2, 3)/H**3 < 4)
check('cone_value_constant_one', sp.Rational(5, 6)/H < 1)
check('cone_direction_constant_half', sp.Rational(1, 3)/H < sp.Rational(1, 2))
b, chi, I0, rad = sp.symbols('b chi I0 rad', positive=True)
r0 = sp.sqrt(chi)/8
G_lower = b*b*chi/(64*I0*rad**2)
density_integrand = sp.Rational(1, 2)*G_lower*rad**2/(2*b)/(2*sp.pi)**3
cone_density = sp.simplify(2*sp.pi*sp.integrate(density_integrand, (rad, r0/2, r0)))
target_density = b*chi**sp.Rational(3, 2)/(16384*sp.pi**2*I0)
check('normalized_single_helicity_density_constant', zero(cone_density-target_density), str(cone_density))

# Direct q-gradient and coordinate determinant check the cone geometry through
# a second implementation. Samples do not replace the uniform Taylor proof.
worst = {'value_ratio': 0.0, 'derivative_ratio': 0.0, 'jacobian_error': 0.0}
for kappa in [np.array([1., 1., 1.]), np.array([1., 0., 0.]), np.array([2., -3., 6.])]:
    bn = np.linalg.norm(kappa)
    axis = kappa/bn
    helper = np.eye(3)[np.argmin(abs(axis))]
    p = np.cross(axis, helper); p /= np.linalg.norm(p)
    q = np.cross(axis, p)
    for cn in [1/256, 1/4, 3/4]:
        rn0 = np.sqrt(cn)/8
        for rn in [rn0/2, rn0]:
            for tn in [-1+cn/4, 0, 1-cn/4]:
                for phi in [0.17, 2.03]:
                    lateral = np.cos(phi)*p+np.sin(phi)*q
                    omega = tn*axis+np.sqrt(1-tn*tn)*lateral
                    domega = axis-tn/np.sqrt(1-tn*tn)*lateral
                    dphi = np.sqrt(1-tn*tn)*(-np.sin(phi)*p+np.cos(phi)*q)
                    point = rn*omega
                    sn, cs = np.sin(point), np.cos(point)
                    eps = np.linalg.norm(sn)
                    nn, dn = sn/eps, kappa*cs
                    fn = np.dot(dn, nn)
                    gradf = kappa*np.cos(2*point)/eps-fn*sn*cs/eps**2
                    ft = np.dot(gradf, rn*domega)
                    worst['value_ratio'] = max(worst['value_ratio'], abs(fn/bn-tn)/rn**2)
                    worst['derivative_ratio'] = max(worst['derivative_ratio'],
                        abs(ft/bn-1)*np.sqrt(1-tn*tn)/rn**2)
                    determinant = abs(np.linalg.det(np.column_stack([omega, rn*domega, rn*dphi])))
                    worst['jacobian_error'] = max(worst['jacobian_error'], abs(determinant/rn**2-1))
                    assert 7*bn/8 <= ft <= 9*bn/8, 'cone_monotone_coordinate'
                    assert np.linalg.norm(np.cross(dn, nn)) >= bn*np.sqrt(cn)/4, 'cone_nonzero_coupling'
check('cone_direct_gradient_and_jacobian_floating', worst['value_ratio'] <= 1 and
      worst['derivative_ratio'] <= 4 and worst['jacobian_error'] < 1e-12, worst)

# The interval/Poisson inequality is checked directly against an unrelated
# finite positive spectral measure, including atoms. Such atoms are precisely
# what the continuum lower-bound argument must exclude in the theorem.
energies = np.array([-1.3, -0.2, 0.7, 1.8])
weights = np.array([0.1, 0.35, 0.4, 0.15])
ratios = []
for center, eta in [(-0.1, 0.3), (0.9, 1.2), (1.7, 0.15)]:
    mass = weights[abs(energies-center) <= eta].sum()
    mv = (weights/(center+1j*eta-energies)).sum()
    rhs = 2*eta*(-mv.imag)
    ratios.append(float(mass/rhs))
check('Poisson_interval_bound_independent_measure', max(ratios) <= 1, ratios)
print(json.dumps({'checks': checks, 'python': platform.python_version(),
                  'sympy': sp.__version__, 'numpy': np.__version__, 'scipy': scipy.__version__,
                  'scope': 'exact finite algebra, floating finite controls and sampled geometry; continuum conclusions use the proof'}))
'''

MEAN_CONTROLS_SOURCE = r'''"""Independent continuous-measure controls for the finite-horizon inequalities."""
import json
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.special import sici

T, b, C, x = sp.symbols('T b C x', positive=True)
split_integral = 2*C*(sp.integrate(1, (x, 0, 1/T))+
                        sp.integrate(1/(T*x), (x, 1/T, 2*b)))
displayed = 2*C*(1+sp.log(2*b*T))/T
assert sp.simplify(sp.expand_log(split_integral-displayed, force=True)) == 0, 'mean_kernel_constant'
print(json.dumps({'check': 'mean_kernel_constant', 'domain': '2*b*T>=1'}))

# Unrelated continuous probability measure: uniform on [-1,1]. Its exact
# Fourier transform is sinc, so these are independent of any matrix fixture.
records = []
for delta in [0.01, 0.1, 0.4]:
    z = 1+1j*delta
    m = 0.5*np.log((z+1)/(z-1))
    e = min(1.0, 4*delta*(-m.imag))
    assert delta <= e+1e-14, 'edge_mass_bound'
    for time in [10., 100., 1000.]:
        integral = sici(2*time)[0]+(np.cos(2*time)-1)/(2*time)
        survival_mean = integral/time
        bound = (e+np.sqrt((1+np.log(2*time))/time))**2
        assert survival_mean <= bound, 'finite_mean_bound'
        records.append({'delta': delta, 'T': time, 'survival_mean': survival_mean,
                        'upper_bound': min(1., bound)})
print(json.dumps({'check': 'edge_mass_and_finite_mean_bound', 'records': records}))
time = 7.3
exact = sici(2*time)[0]+(np.cos(2*time)-1)/(2*time)
numeric = quad(lambda y: np.sinc(y/np.pi)**2, 0, time, epsabs=1e-12)[0]
assert abs(exact-numeric) < 1e-11, 'direct_sinc_integral'
print(json.dumps({'check': 'direct_sinc_integral', 'error': abs(exact-numeric), 'checks': 3,
                  'scope': 'continuous toy measure and exact elementary integral; not a numerical continuum walk proof'}))
'''

WEIGHTED_CONTROLS_SOURCE = r'''"""Exact and independent-form controls for the weighted scattering implication."""
import json
import platform
import numpy as np
import sympy as sp
import scipy
from scipy.integrate import quad

count = 0


def check(name, condition, detail=None):
    global count
    assert bool(condition), name
    count += 1
    print(json.dumps({'check':name,'detail':detail}))


def zero(value):
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(x) == 0 for x in value)
    return sp.simplify(value) == 0


I = sp.I
g = sp.Matrix([sp.Rational(3,13)+I*sp.Rational(4,13), -I*sp.Rational(12,13)])
eta = sp.simplify((g.conjugate().T*g)[0])
V = sp.zeros(2).row_join(g).col_join(g.conjugate().T.row_join(sp.zeros(1)))
check('rank_two_selfadjoint', zero(V-V.conjugate().T))
check('rank_two_actual_rank', V.rank() == 2)
check('rank_two_minimal_polynomial', zero(V**3-eta*V))
singulars = V.singular_values()
trace_norm = sp.simplify(sum(singulars))
claimed_trace_norm = 2*sp.sqrt(eta)
check('trace_norm_factor_two', zero(trace_norm-claimed_trace_norm),
      {'eta':str(eta),'singular_values':list(map(str,singulars))})

# The continuous conjugacy example below has Omega=U P0 on its ac part.
# These exact matrices only test the adjoint/source-channel convention.
U = sp.Matrix([[0,1],[1,0]])
P0 = sp.diag(1,0)
Omega = U*P0
zeta = sp.Matrix([0,1])
check('partial_isometry_initial_final', zero(Omega.conjugate().T*Omega-P0) and
      zero(Omega*Omega.conjugate().T-U*P0*U.conjugate().T))
outgoing = Omega.conjugate().T*zeta
check('reverse_wave_operator_norm_one', zero((outgoing.conjugate().T*outgoing)[0]-1))
check('forward_wave_operator_wrong_source_zero', zero(Omega*zeta))

# Independent continuous model: multiplication by x on L2([-1,1],dx/2)
# conjugated by the exact swap of the constant function and scalar channel.
x = sp.symbols('x', real=True)
t = sp.symbols('t', real=True, positive=True)
a = sp.integrate(sp.cos(t*x), (x,-1,1))/2
check('normalized_continuous_amplitude', zero(a-sp.sin(t)/t))
norm_u = sp.integrate(1+a*a-2*a*sp.cos(t*x), (x,-1,1))/2
check('continuous_full_state_norm', zero(norm_u+a*a-1))
comparison_norm_squared = sp.integrate(a*a, (x,-1,1))/2+a*a
check('strong_comparison_error_exact', zero(comparison_norm_squared-2*a*a))
direct_weight = sp.integrate(x*x*(1+a*a-2*a*sp.cos(t*x)), (x,-1,1))/2
memory_weight = sp.Rational(1,3)+a*a/3+2*a*sp.diff(a,t,2)
check('continuous_weighted_formula', zero(direct_weight-memory_weight))
limit_weight = sp.limit(memory_weight,t,sp.oo)
check('continuous_positive_weighted_limit', limit_weight == sp.Rational(1,3), str(limit_weight))

# The perturbation of the conjugacy model, in (f0,sqrt(3)*x,zeta0),
# is independently represented as an actual finite-rank matrix.
h = sp.Matrix([0,1/sp.sqrt(3),0])
w = sp.Matrix([-1,0,1])
Vtoy = h*w.T+w*h.T
check('continuous_toy_rank_two', Vtoy.rank() == 2 and
      zero(sum(Vtoy.singular_values())-2*sp.sqrt(sp.Rational(2,3))))

# Fresh numerical integrals compare the direct field expression with the
# symbolic weighted formula; no walk grid or finite-time scattering fit.
fn = sp.lambdify(t,memory_weight,'numpy')
errors=[]
for time in [0.13,1.7,8.2,31.0]:
    av=np.sinc(time/np.pi)
    result=quad(lambda q:q*q*abs(np.exp(-1j*time*q)-av)**2/2,-1,1,epsabs=1e-12)[0]
    errors.append(abs(result-float(fn(time))))
check('weighted_integral_floating',max(errors)<2e-10,errors)

# The actual current block, unlike its multiplication block alone, includes
# scalar cross terms. They drop out only on a zero-scalar comparison vector.
m=sp.diag(sp.Rational(-1,3),sp.Rational(2,5))
r=sp.Matrix([sp.Rational(1,7),I*sp.Rational(2,9)])
J=m.row_join(r).col_join(r.conjugate().T.row_join(sp.ones(1)))
v=sp.Matrix([sp.Rational(3,5),I*sp.Rational(4,5),0])
field=sp.Matrix(v[:2])
check('current_on_outgoing_field',zero((v.conjugate().T*J*v)[0]-(field.conjugate().T*m*field)[0]))
perturbed=sp.sqrt(sp.Rational(3,4))*v+sp.Matrix([0,0,sp.Rational(1,2)])
without_cross=sp.diag(sp.Rational(-1,3),sp.Rational(2,5),1)
check('finite_scalar_cross_term_cannot_be_dropped',
      not zero((perturbed.conjugate().T*(J-without_cross)*perturbed)[0]))

# Strict positivity of a weight gives no numerical coercivity constant by
# itself. This exact sequence is a scope control, not the actual u_plus.
n=sp.symbols('n',positive=True)
concentrated_norm=sp.integrate(n,(x,-1/n,1/n))/2
concentrated_weight=sp.integrate(n*x*x,(x,-1/n,1/n))/2
check('positive_weight_no_inferred_uniform_constant',zero(concentrated_norm-1) and
      zero(concentrated_weight-1/(3*n*n)))
print(json.dumps({'checks':count,'python':platform.python_version(),'sympy':sp.__version__,
                  'numpy':np.__version__,'scipy':scipy.__version__,
                  'scope':'exact rank/conjugacy/current identities and floating toy quadrature; not a numerical proof of Kato or continuum-walk scattering'}))
'''

SCALE_CONTROLS_SOURCE = r'''"""Exact finite scale budgets; no continuum/time-asymptotic inference."""
from fractions import Fraction as F
import json

# Direct finite Q16 upper expression, preserving A rather than replacing it by 1.
# These rational samples have lambda^(1/2) and T exactly rational.
rows=[]
for q in (F(1,8),F(1,4),F(3,8)):
    for power in (1,2,4):
        x=F(1,2**power); lam=x**8; root= x**4
        delta=lam**3; sigma=lam**2; T=x**(-int(8*q))
        for A in (root/12,root,2*root):
            assert A<=1 and root/12<=A<=2*root
            # b<2, b^2=3, I0^-1/2<4, C_lambda<=4/lambda, r_delta<=delta.
            exact_relaxed=(delta/sigma*(A*(4+6*T)+(4+3*T))/A
                +(4+F(21,2)*T*T)*lam*4
                +8*sigma/(lam*A)+(A+1)*T*delta/A)
            four_term=(108*delta*T/(sigma*root)+58*T*T*lam
                +96*sigma/(lam*root)+13*T*delta/root)
            leading=x**(4-int(8*q))
            assert exact_relaxed<=four_term<=275*leading
        rows.append({'gamma':str(q),'lambda':str(lam),'relative_bound':str(four_term),'leading_power':str(leading)})
print(json.dumps({'finite_exact_budget_rows':rows}))

# Symbolic exponents from the original general bound, using gamma=1/2-p.
# For 0<p<1/2 all resulting exponents are positive. This is an exact affine
# calculation, not extrapolation from the finite samples above.
import sympy as s
p=s.symbols('p', positive=True)
gamma=F(1,2)-p
exponents=[3-gamma-2-F(1,2), 1-2*gamma, F(1,2), 3-gamma-F(1,2)]
assert [s.simplify(v) for v in exponents]==[p,2*p,F(1,2),p+2]
parameter=s.symbols('parameter', positive=True)
sub={p:1/(2*(1+parameter))}
assert all(s.simplify(v.subs(sub) if hasattr(v,'subs') else v).is_positive for v in exponents)
assert s.simplify(1-gamma-p)==F(1,2)
assert s.simplify(1-p).subs(sub).is_positive
assert F(2,3)*F(1,8)==F(1,12)
assert sum([108,58,96,13])==275
# Using delta=lambda^2 with the same sigma makes its leading error exponent
# negative. The current scale choice is material, not a cosmetic convention.
wrong_delta=2-gamma-2-F(1,2)
assert s.simplify(wrong_delta.subs(sub)).is_negative
print('Exact affine exponents, packet errors and leading coefficient verified; delta=lambda^2 fails these scales.')

# Global physical weights change, but still preserve a uniform fiber bound.
lam=F(1,64); weights=[F(1,5),F(3,10),F(1,2)]
survival=[1-lam**3/F(d) for d in (7,8,9)]
normalization=sum(w*n for w,n in zip(weights,survival))
physical=[w*n/normalization for w,n in zip(weights,survival)]
assert sum(physical)==1 and physical!=weights and min(physical)>0
errors=[F(-1,3),F(2,5),F(5,7)]
assert abs(sum(w*e for w,e in zip(physical,errors)))<=max(map(abs,errors))
print('Exact single global normalization preserves the uniform error; original weights are not substituted.')
'''

OUTGOING_CONTROLS_SOURCE = r'''#!/usr/bin/env python3
"""Exact author controls for the regulated outgoing formula and constants.

The continuum proof is in the note. The finite bath intentionally violates
the absolutely continuous scattering premise and has no unit outgoing datum.
"""
from fractions import Fraction as F
import sympy as s


def check(name, condition):
    assert bool(condition), name
    print('EXACT', name)


def zero(expr):
    return s.simplify(expr) == 0


z = s.symbols('z')
h = s.symbols('h', positive=True)
D = s.diag(-1, 1)
g = s.Matrix([s.Rational(1, 2), s.Rational(1, 2)])
A = D.row_join(g).col_join(g.T.row_join(s.zeros(1, 1)))
zeta = s.Matrix([0, 0, 1])
eta_g = (g.T*g)[0]
Sigma = (g.T*(z*s.eye(2)-D).inv()*g)[0]
M = 1/(z-Sigma)
check('finite Schur resolvent', zero(M-((z*s.eye(3)-A).inv())[2, 2]))
check('finite even bath', zero(Sigma-z/(2*(z*z-1))))
check('finite energy second moment', zero((zeta.T*A*A*zeta)[0]-eta_g))
check('finite scalar spectral decomposition',
      zero(M-2/(3*z)-z/(3*(z*z-s.Rational(3, 2)))))

# Integrate the explicit scalar spectral decomposition, with the causal sign.
omega = s.sqrt(s.Rational(3, 2))
u_abel = []
for j, energy in enumerate((-1, 1)):
    integrated = -s.I*g[j]*(s.Rational(2, 3)/(h-s.I*energy)
        +s.Rational(1, 6)/(h-s.I*(energy-omega))
        +s.Rational(1, 6)/(h-s.I*(energy+omega)))
    candidate = g[j]*M.subs(z, energy+s.I*h)
    check('Abel causal sign channel '+str(j), zero(integrated-candidate))
    u_abel.append(candidate)
norm2 = s.factor(sum(s.conjugate(v)*v for v in u_abel))
check('finite bath has zero Abel outgoing norm', s.limit(norm2, h, 0) == 0)
check('finite dressing retains a point atom',
      s.limit(z*M, z, 0) == s.Rational(2, 3))
check('positive regulator finite norm', norm2.subs(h, 1) > 0)
check('positive regulator contraction fixture', norm2.subs(h, 1) < 1)
print('FINITE_BATH_NORM', norm2)

# A nontrivial two-dimensional transverse helicity decomposition.
J = s.Matrix([[0, -s.I], [s.I, 0]])
coupling = s.I*s.Matrix([s.Rational(3, 5), s.Rational(4, 5)])
Pplus, Pminus = (s.eye(2)+J)/2, (s.eye(2)-J)/2
check('helicity cross term absent',
      zero((coupling.conjugate().T*Pplus*Pminus*coupling)[0]))
weight_plus = s.simplify((coupling.conjugate().T*Pplus*coupling)[0])
weight_minus = s.simplify((coupling.conjugate().T*Pminus*coupling)[0])
claimed_each_helicity_weight = s.Rational(1, 2)
check('helicity half measure', weight_plus == weight_minus == claimed_each_helicity_weight)
check('even measure resolvent conjugacy',
      zero(M.subs(z, -1+s.I*h)+s.conjugate(M.subs(z, 1+s.I*h))))

# These algebraic margins are distinct from the analytic symmetry proof R8.
symmetry_complement = F(1)-F(1, 3)
energy_moment_ceiling = F(2, 3)
check('permutation complement factor', symmetry_complement == energy_moment_ceiling)
interior_cutoff = F(7, 8)
m0 = 1-energy_moment_ceiling/interior_cutoff**2
check('interior mass exact', m0 == F(19, 147))
check('interior mass strictly positive', 0 < m0 < 1)

# Retain pi^2 and I0 symbolically until the last rational relaxation.
pi2, I0, b, chi = s.symbols('pi2 I0 b chi', positive=True)
C_squared = s.Integer(32768)**2*pi2*I0**2/(b*b*chi**3)
cone_coefficient = s.simplify(C_squared*b*b/(4*I0))
claimed_cone_coefficient = 2**37*pi2*I0
check('cone coefficient exact powers',
      zero(cone_coefficient.subs(chi, s.Rational(1, 8))-claimed_cone_coefficient))
K0 = 90*2**34
check('cone rational relaxation',
      claimed_cone_coefficient.subs({pi2:10, I0:s.Rational(9, 8)}) == K0)
rstar = m0/(2*K0)
c0 = m0**3/(8*K0*K0)
check('valid positive cone radius', 0 < rstar < F(1, 2))
check('interior mass after cone removal', m0-K0*rstar == m0/2)
check('weighted mass constant', rstar*rstar*m0/2 == c0)
check('published rational constant',
      c0 == F(6859, 60752858276421362793738298982400))
check('readable conservative decimal', c0 > F(1128, 1000)*F(1, 10**28))
check('canonical current denominator bound', 12*10*F(9, 8) == 135)
print('RATIONAL_BOUNDS', {'K0':K0, 'm0':str(m0), 'rstar':str(rstar),
                           'c0':str(c0), 'current_gap':str(c0/135)})
print('Complete author controls; no continuum theorem is proved by this finite bath.')
'''

AUTHOR_BLOCKS = [
    ('effective_memory/memory_controls.py', '10980b8195c33ac813f59632cc028a1dbd8a04e066930786dabea338ed162c4a', MEMORY_CONTROLS_SOURCE),
    ('effective_memory/mean_controls.py', '8376f00539c79b580b6c142b5b71b8d0d4ec39cd98f47e9577170e915d5b097c', MEAN_CONTROLS_SOURCE),
    ('weighted_memory/weighted_controls.py', '70807cce821d3e2eca3fc96cefd52fa1cfe83c4496801b9c9f2f7b9dd5108c24', WEIGHTED_CONTROLS_SOURCE),
    ('joint_scale_current/scale_controls.py', '1a71fb0d680630d0581fe4f982520d4bc3bc51a2649c2359815c3445c2b4d233', SCALE_CONTROLS_SOURCE),
    ('outgoing_resolvent/outgoing_controls.py', '5959a175ffd66638f25b23315d1923c344d51c790ada16a85166671058049c75', OUTGOING_CONTROLS_SOURCE),
]


def main():
    for name, expected_sha256, source in AUTHOR_BLOCKS:
        actual = hashlib.sha256(source.encode("utf-8")).hexdigest()
        assert actual == expected_sha256, (name, actual, expected_sha256)
        print(json.dumps({"author_block": name, "sha256": actual, "phase": "begin"}), flush=True)
        namespace = {"__name__": "__main__", "__file__": "<frozen-author:" + name + ">"}
        exec(compile(source, namespace["__file__"], "exec"), namespace, namespace)
        print(json.dumps({"author_block": name, "phase": "complete"}), flush=True)
    print(json.dumps({"status": "PASS", "isolated_author_blocks": len(AUTHOR_BLOCKS),
                      "scope": "literal author finite controls; no independent continuum proof"}), flush=True)


if __name__ == "__main__":
    main()
