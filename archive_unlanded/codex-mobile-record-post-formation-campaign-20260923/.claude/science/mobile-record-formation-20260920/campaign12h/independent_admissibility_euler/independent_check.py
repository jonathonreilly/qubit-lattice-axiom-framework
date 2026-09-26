#!/usr/bin/env python3
"""Pre-source native-formation Euler checks, independent of primary code.

The birth-star generator is evaluated on all 924 neighbor-count orbits and
all seven center states. Counts are an exact permutation lumping of its six
frozen neighbors, not a different formation rule. Exchange proofs are imported
only from the named sealed independent reports. Numerical ODE checks support,
but do not replace, the analytic nonautonomous estimates.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial, prod
import json
import platform
import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.linalg import expm
import sympy as sp

HERE = Path(__file__).resolve().parent
V = ((0,0,0),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
checks = []


def check(name, condition, details=None):
    if not condition:
        raise AssertionError((name, details))
    checks.append(dict(name=name, passed=True, details=details))


def compositions(total, parts):
    if parts == 1:
        yield (total,)
    else:
        for first in range(total+1):
            for rest in compositions(total-first, parts-1):
                yield (first,) + rest


COUNTS = list(compositions(6, 7))
check('six_distinct_neighbor_orbit_count', len(COUNTS) == 924,
      dict(orbits=len(COUNTS), center_times_orbits=7*len(COUNTS), unlumped_states=7**7))


def star_control(weights, numerators, denominator, beta, reference=None, differentiate=False):
    """Direct sum of the complete center-birth generator in every orbit."""
    p = [F(w, sum(weights)) for w in weights]
    refweights = weights if reference is None else reference
    ref = [F(w, sum(refweights)) for w in refweights]
    means = [F(0)]*6
    adjoint_mean = F(0)
    gradient = [F(0)]*6
    max_uniform_adjoint = F(0)
    neighbor_mass_sum = F(0)
    pair_vector_derivative = F(0)
    for counts in COUNTS:
        multiplicity = factorial(6) // prod(factorial(k) for k in counts)
        neighbor_mass = F(multiplicity * prod(w**k for w,k in zip(weights,counts)), sum(weights)**6)
        neighbor_mass_sum += neighbor_mass
        rates = [beta * F(prod(row[b]**counts[b] for b in range(7)), denominator**6)
                 for row in numerators]
        assert min(rates) > 0
        # The exact seven-center-state generator has row 0 -> a at rates[a-1],
        # row 0 diagonal -sum rates, and all occupied rows zero.
        for a, rate in enumerate(rates):
            means[a] += neighbor_mass * p[0] * rate
        for c in range(7):
            incoming_ratio = -sum(rates) if c == 0 else rates[c-1]*ref[0]/ref[c]
            mass = neighbor_mass*p[c]
            adjoint_mean += mass*incoming_ratio
            uniform_adjoint = -sum(rates) if c == 0 else rates[c-1]
            max_uniform_adjoint = max(max_uniform_adjoint, uniform_adjoint)
            if differentiate:
                for b in range(1,7):
                    score = F(counts[b]+int(c==b),1)/p[b] - F(counts[0]+int(c==0),1)/p[0]
                    gradient[b-1] += mass*incoming_ratio*score
        # The distinguished neighbor's conditional f_1 mean in an orbit is
        # sum counts_b f_1(b)/6. Both endpoints of a neighboring pair may form.
        neighbor_f = F(sum(counts[b]*V[b][0] for b in range(7)),6)
        source_f = sum(rates[a-1]*V[a][0] for a in range(1,7))
        pair_vector_derivative += 2*p[0]*neighbor_mass*source_f*neighbor_f
    ell = [sum(F(row[b],denominator)*p[b] for b in range(7)) for row in numerators]
    expected = [beta*p[0]*z**6 for z in ell]
    expected_adjoint = sum(beta*ell[a-1]**6*(ref[0]/ref[a]*p[a]-p[0]) for a in range(1,7))
    budget = beta*max(F(x,denominator) for row in numerators for x in row)**6
    assert neighbor_mass_sum == 1 and means == expected and adjoint_mean == expected_adjoint
    assert max_uniform_adjoint <= budget
    if differentiate:
        assert reference is None
        expected_gradient = [means[b]/p[b+1]+sum(means)/p[0] for b in range(6)]
        assert adjoint_mean == 0 and gradient == expected_gradient
    mean_vector = sum(p[b]*V[b][0] for b in range(7))
    source_vector = sum(means[a-1]*V[a][0] for a in range(1,7))
    covariance_derivative = pair_vector_derivative-2*mean_vector*source_vector
    return dict(reaction=[str(x) for x in means], adjoint_mean=str(adjoint_mean),
                adjoint_derivative=[str(x) for x in gradient] if differentiate else None,
                max_uniform_adjoint=str(max_uniform_adjoint), entropy_budget_per_site=str(budget),
                adjacent_vector_pair_moment_derivative=str(pair_vector_derivative),
                adjacent_vector_connected_covariance_derivative=str(covariance_derivative))


# A positive nonsymmetric matrix with nonconstant occupied row sums. This
# challenges any accidental normalization of the supplied birth rates.
den = 5
wn = [[den]+[3+(2*a+3*b+a*b)%8 for b in range(1,7)] for a in range(1,7)]
pweights = [8,1,2,3,4,5,6]
general = star_control(pweights, wn, den, F(2,5), differentiate=True)
check('general_W_star_reaction_and_source_adjoint_Taylor', True, general)
off_reference = star_control([2,3,4,5,6,7,8], wn, den, F(2,5), reference=pweights)
check('general_W_off_reference_source_expectation', off_reference['adjoint_mean'] != '0', off_reference)
uniform = star_control(pweights, [[1]*7 for _ in range(6)], 1, F(2,5), differentiate=True)
check('uniform_weight_product_control',
      uniform['reaction'] == [str(F(2,5)*F(8,29))]*6
      and uniform['adjacent_vector_connected_covariance_derivative'] == '0', uniform)

# The local covariance calculation is for a cubic torus with distinct
# neighbors. Exchange contributes zero at a homogeneous product by the
# previously proved stationarity; the two birth terms are computed here.
j0 = F(1,2)
jweights = [[F(1)+j0*sum(V[a][i]*V[b][i] for i in range(3)) for b in range(7)] for a in range(1,7)]
jn = [[int(2*w) for w in row] for row in jweights]
balanced = star_control([6,1,1,1,1,1,1], jn, 2, F(1,3), differentiate=True)
check('j_family_product_law_is_not_preserved',
      balanced['adjacent_vector_connected_covariance_derivative'] == '1/18', balanced)

# Full six-field algebra, assembled in species coordinates before transforming.
p = sp.Matrix(sp.symbols('p1:7', real=True))
rho = sum(p)
beta, j, r = sp.symbols('beta j rho', real=True)
k = sp.symbols('kx ky kz', real=True)
f = [sp.Matrix([V[a][i] for a in range(1,7)]) for i in range(3)]
g = [(p.T*x)[0] for x in f]
reaction = sp.Matrix([beta*(1-rho)*(1+j*sum(V[a+1][i]*g[i] for i in range(3)))**6 for a in range(6)])
T = sp.Matrix([[1]*6,
               [1,-1,0,0,0,0], [0,0,1,-1,0,0], [0,0,0,0,1,-1],
               [sp.Rational(2,3)]*2+[-sp.Rational(1,3)]*4,
               [-sp.Rational(1,3)]*2+[sp.Rational(2,3)]*2+[-sp.Rational(1,3)]*2])
balanced_sub = {pa:r/6 for pa in p}
mu = 12*beta*j*(1-r)
lam = 6*beta
source_linear = (T*reaction.jacobian(p).subs(balanced_sub)*T.inv()).applyfunc(sp.simplify)
expected_source = sp.diag(-lam, mu, mu, mu, 0, 0)
check('all_six_reaction_eigenfields', source_linear == expected_source,
      dict(density='-6 beta', three_vectors='12 beta j (1-rho)', two_quadrupoles='0'))
current_linear = sp.zeros(6)
for i in range(3):
    feature = sp.Matrix([2-3*x*x for x in f[i]])
    S = (p.T*feature)[0]
    J = sp.Matrix([p[a]*(S*f[i][a]+(feature[a]-2*S)*g[i]) for a in range(6)])
    current_linear += k[i]*T*J.jacobian(p).subs(balanced_sub)*T.inv()
expected_current = sp.zeros(6)
for i in range(3):
    expected_current[0,i+1] = 2*r*(1-r)*k[i]
    expected_current[i+1,0] = sp.Rational(2,3)*r*k[i]
check('all_six_axis_balanced_transport_fields',
      all(sp.simplify(x)==0 for x in current_linear-expected_current))

g1,g2,g3,r1,r2 = sp.symbols('g1 g2 g3 r1 r2', real=True)
gs = [g1,g2,g3]; rs = [r1,r2,-r1-r2]
qs = [r/3+x for x in rs]
field_sub = {p[2*i]:(qs[i]+gs[i])/2 for i in range(3)}
field_sub.update({p[2*i+1]:(qs[i]-gs[i])/2 for i in range(3)})
actual_nonlinear = (T*reaction).subs(field_sub, simultaneous=True).applyfunc(sp.simplify)
even = [1+15*(j*x)**2+15*(j*x)**4+(j*x)**6 for x in gs]
odd = [6*j*x+20*(j*x)**3+6*(j*x)**5 for x in gs]
total = 2*beta*(1-r)*sum(even)
expected_nonlinear = sp.Matrix([total]+[2*beta*(1-r)*x for x in odd]
    +[2*beta*(1-r)*(even[i]-sum(even)/3) for i in range(2)])
check('complete_nonlinear_density_vector_quadrupole_reactions',
      all(sp.expand(x)==0 for x in actual_nonlinear-expected_nonlinear))
check('reaction_does_not_depend_on_quadrupole_state',
      all(sp.diff(x,z)==0 for x in actual_nonlinear for z in (r1,r2)))

M = expected_source-sp.I*expected_current
H = sp.diag(1/(r*(1-r)),3/r,3/r,3/r,0,0)
H[4:6,4:6] = (3/r)*sp.Matrix([[2,1],[1,2]])
energy_derivative = H.diff(r)*lam*(1-r)+M.conjugate().T*H+H*M
expected_energy = sp.zeros(6)
expected_energy[0,0] = -lam/r*H[0,0]
for i in range(1,4): expected_energy[i,i] = (2*mu-lam*(1-r)/r)*H[i,i]
expected_energy[4:6,4:6] = -lam*(1-r)/r*H[4:6,4:6]
check('exact_time_dependent_entropy_energy_identity',
      all(sp.simplify(x)==0 for x in energy_derivative-expected_energy))
z, kmag = sp.symbols('z kmag',real=True)
long = sp.Matrix([[-lam,-sp.I*2*r*(1-r)*kmag],[-sp.I*2*r*kmag/3,mu]])
poly = (z*sp.eye(2)-long).det()
check('frozen_longitudinal_polynomial_only',
      sp.expand(poly-((z+lam)*(z-mu)+sp.Rational(4,3)*r*r*(1-r)*kmag**2))==0)

# Direct nonautonomous matrix propagation, retaining all six fields.
rho0, b0, jnum, tend = 0.1, 1/3, 0.9, 2.0
wave = np.array([2*np.pi,4*np.pi,0.0])
def profile(t): return 1-(1-rho0)*np.exp(-6*b0*t)
def drift(t):
    rt=profile(t);vt=1-rt
    matrix=np.diag([-6*b0]+[12*b0*jnum*vt]*3+[0,0]).astype(complex)
    matrix[0,1:4] = -1j*2*rt*vt*wave
    matrix[1:4,0] = -1j*2*rt*wave/3
    return matrix
def metric(t):
    rt=profile(t)
    matrix=np.diag([1/(rt*(1-rt))]+[3/rt]*3+[0,0])
    matrix[4:6,4:6]=(3/rt)*np.array([[2,1],[1,2]])
    return matrix
def matrix_power_positive(matrix, power):
    val,vec=np.linalg.eigh(matrix)
    return (vec*val**power)@vec.T
times=np.linspace(0,tend,101)
solution=solve_ivp(lambda t,u:(drift(t)@u.reshape(6,6)).reshape(-1),
    (0,tend),np.eye(6,dtype=complex).reshape(-1),t_eval=times,rtol=2e-11,atol=2e-13)
check('nonautonomous_matrix_solver_succeeded',solution.success,
      dict(message=solution.message, derivative_evaluations=solution.nfev))
H0invhalf=matrix_power_positive(metric(0),-0.5)
largest_ratio=0.0;transverse_error=0.0;quad_error=0.0
for t,flat in zip(solution.t,solution.y.T):
    U=flat.reshape(6,6);rt=profile(t)
    weighted=matrix_power_positive(metric(t),0.5)@U@H0invhalf
    squared_gain=np.linalg.svd(weighted,compute_uv=False)[0]**2
    lower=max(rho0,1/(4*jnum))
    exponent=0 if rt<=lower else 4*jnum*(rt-lower)-np.log(rt/lower)
    largest_ratio=max(largest_ratio,squared_gain/np.exp(exponent))
    expected_gain=np.exp(2*jnum*(rt-rho0))
    transverse_error=max(transverse_error,abs(U[3,3]-expected_gain))
    quad_error=max(quad_error,float(np.max(np.abs(U[:,4:6]-np.eye(6)[:,4:6]))))
check('finite_time_entropy_energy_bound',largest_ratio<=1+2e-9,
      dict(max_gain_squared_over_bound=float(largest_ratio),times=len(times), tolerance=2e-9))
check('exact_transverse_gain_and_quadrupole_constancy',transverse_error<2e-9 and quad_error<2e-9,
      dict(max_transverse_error=float(transverse_error),max_quadrupole_error=quad_error,
           actual_transverse_gain=float(np.exp(2*jnum*(profile(tend)-rho0))),
           all_time_transverse_bound=float(np.exp(2*jnum*(1-rho0)))))
U=solution.y[:,-1].reshape(6,6)
frozen=expm(tend*drift(0))
difference=float(np.linalg.norm(U-frozen))
check('frozen_exponential_is_not_the_nonautonomous_propagator',difference>0.1,
      dict(frobenius_difference=difference,
           frozen_transverse_gain=float(np.exp(12*b0*jnum*(1-rho0)*tend))))

result=dict(scope='Pre-source independent exact local-generator and symbolic controls, plus stated numerical ODE controls.',
    environment=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,sympy=sp.__version__),
    count=len(checks),checks=checks,
    limitations=['The star is the exact local birth component, with all 7^7 states represented by count orbits; it is not a complete 7^(N^3) torus enumeration.',
                 'No stochastic simulation or primary author code was used.',
                 'Numerical propagators support analytic estimates and do not prove them.'])
text=json.dumps(result,indent=2)+'\n'
(HERE/'RESULTS.json').write_text(text)
print(text,end='')
