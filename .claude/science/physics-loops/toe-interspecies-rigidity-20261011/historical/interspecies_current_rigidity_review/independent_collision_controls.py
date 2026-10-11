"""Independent exact controls for interspecies rigidity.

Uses symbolic edge multipliers, all-parameter skew-line residuals, and an
actual continuum AB energy-shell parametrization with quadratic charges.
No author helper is imported. These controls do not prove the unrestricted
C1 theorem or establish a physical collision measure/selection rule.
"""
import itertools
import json
import platform
import time

import sympy as sp

started = time.monotonic()
checks = 0


def zero(value):
    entries = list(value) if isinstance(value, sp.MatrixBase) else [value]
    return all(sp.expand(x) == 0 for x in entries)


def check(name, condition, detail=None):
    global checks
    assert bool(condition), name
    checks += 1
    print(json.dumps({"check": name, "detail": detail}, sort_keys=True))


# A nonorthogonal affine image of a tetrahedron. Solve for edge multipliers,
# rather than assigning arbitrary charge vectors at a finite velocity grid.
M = sp.Matrix([[3, -1, -4], [1, 3, 5], [1, -5, -2]])
t = sp.Matrix([2, -1, 3])
e1, e2, e3 = [sp.eye(3)[:, j] for j in range(3)]
x1, x2, y1, y2 = t, t + M * e1, t + M * e2, t + M * e3
check("genuinely_noncoplanar_anchors", M.det() == 82)
l11, l21, l22, l12 = sp.symbols("l11 l21 l22 l12", real=True)
cycle = l11*(x1-y1) - l21*(x2-y1) + l22*(x2-y2) - l12*(x1-y2)
solution = sp.solve(list(cycle), [l11, l21, l22], dict=True)
check("four_edge_cycle_forces_one_multiplier",
      solution == [{l11: l12, l21: l12, l22: l12}], str(solution))

# For every real r,h, including r=0,1 where a cross edge is zero, an A
# residual on the opposite line is allowed by the two B anchors alone.
r, h, alpha, beta, mu = sp.symbols("r h alpha beta mu", real=True)
u, v = x2-x1, y2-y1
x = y1 + r*v
y_star = x1 + h*u
residual = alpha*v
check("anchor_lines_alone_leave_exceptional_residual",
      zero(residual.cross(x-y1)) and zero(residual.cross(x-y2)))
check("equal_velocity_endpoints_are_included",
      zero(x.subs(r, 0)-y1) and zero(x.subs(r, 1)-y2))
displacement = x-y_star
check("skew_transversality_for_every_parameter",
      sp.expand(sp.Matrix.hstack(u, v, displacement).det()) == -82,
      "constant determinant, including every r,h and equal-anchor endpoint")
exceptional_matrix = sp.Matrix.hstack(v, -u, -displacement)
check("cross_edge_kills_both_line_residuals_without_division_by_parameters",
      sp.expand(exceptional_matrix.det()) == 82
      and zero(exceptional_matrix*sp.Matrix([alpha, beta, mu])
               - (alpha*v-beta*u-mu*displacement)))

# Actual continuum AB collisions for E_s(k)=|k|^2/(2m_s), masses 2 and 3.
# The species have different Hessians and full three-dimensional velocity
# images. Relative-momentum rotations conserve both supplied quantities.
m_A, m_B = sp.Integer(2), sp.Integer(3)
K = sp.Matrix(sp.symbols("K1:4", real=True))
p = sp.Matrix(sp.symbols("p1:4", real=True))
a = m_A/(m_A+m_B)*K + p
b = m_B/(m_A+m_B)*K - p
energy = sp.expand(a.dot(a)/(2*m_A) + b.dot(b)/(2*m_B))
check("unequal_mass_AB_shell_parametrization",
      zero(a+b-K) and zero(energy-K.dot(K)/10-sp.Rational(5, 12)*p.dot(p)))
Rx = sp.Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
Rz = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
for label, R in [("x", Rx), ("z", Rz)]:
    c = m_A/(m_A+m_B)*K + R*p
    d = m_B/(m_A+m_B)*K - R*p
    check("actual_AB_collision_rotation_" + label,
          zero(c+d-K) and zero(energy-c.dot(c)/(2*m_A)-d.dot(d)/(2*m_B)))

qa = sp.symbols("qa11 qa22 qa33 qa12 qa13 qa23", real=True)
qb = sp.symbols("qb11 qb22 qb33 qb12 qb13 qb23", real=True)
ba = sp.symbols("ba1:4", real=True)
bb = sp.symbols("bb1:4", real=True)
ca, cb = sp.symbols("ca cb", real=True)


def symmetric(q):
    return sp.Matrix([[q[0], q[3], q[4]], [q[3], q[1], q[5]], [q[4], q[5], q[2]]])


def charge(k, q, linear, constant):
    return (k.dot(symmetric(q)*k))/2 + sp.Matrix(linear).dot(k) + constant


incoming = charge(a, qa, ba, ca) + charge(b, qb, bb, cb)
equations = []
for R in [Rx, Rz]:
    c = m_A/(m_A+m_B)*K + R*p
    d = m_B/(m_A+m_B)*K - R*p
    defect = sp.expand(incoming-charge(c, qa, ba, ca)-charge(d, qb, bb, cb))
    equations.extend(sp.Poly(defect, *K, *p).coeffs())
equations = list(dict.fromkeys(equations))
unknowns = list(qa) + list(qb) + list(ba) + list(bb) + [ca, cb]
L, rhs = sp.linear_eq_to_matrix(equations, unknowns)
lam, bx, by, bz, const_a, const_b = sp.symbols("lam bx by bz const_a const_b", real=True)
family = sp.Matrix([lam/m_A]*3 + [0]*3 + [lam/m_B]*3 + [0]*3
                   + [bx, by, bz]*2 + [const_a, const_b])
family_matrix = family.jacobian([lam, bx, by, bz, const_a, const_b])
check("actual_shell_constraints_have_exact_common_coefficient_family",
      zero(rhs) and L.rank() == 14 and family_matrix.rank() == 6
      and zero(L*family_matrix),
      {"charge_ansatz_unknowns": len(unknowns), "constraint_rank": L.rank(),
       "kernel_dimension": len(unknowns)-L.rank(),
       "family": "lambda E_s + common b dot k + independent species constants"})

# A wrong equal-Hessian assignment differs from the required equal energy
# coefficient when masses differ; an actual continuum collision detects it.
wrong_family = family.subs({qb[j]: qb[j] for j in range(6)})
wrong_family = sp.Matrix([lam/m_A]*3 + [0]*3 + [lam/m_A]*3 + [0]*3
                         + [bx, by, bz]*2 + [const_a, const_b])
check("equal_Hessians_are_not_common_energy_coefficients_for_unequal_masses",
      not zero(L*wrong_family))

# Energy and momentum conservation alone need not conserve E grad E.
incoming_current = e1/(2*m_A**2) - e1/(2*m_B**2)
outgoing_current = e2/(2*m_A**2) - e2/(2*m_B**2)
check("ordinary_energy_conservation_does_not_supply_current_selection",
      incoming_current-outgoing_current == sp.Rational(5, 72)*(e1-e2))

# Exact regular K=0 radial collisions with current J_s=beta_s k.
def radial_collision(CA, CB, beta_A, beta_B):
    EA, EB = sp.sqrt(CA+beta_A), sp.sqrt(CB+beta_B)
    relative_in = (beta_A/EA + beta_B/EB)*e1
    relative_out = (beta_A/EA + beta_B/EB)*e2
    defect = (beta_A-beta_B)*(e1-e2)
    return EA, EB, relative_in, relative_out, defect


EA, EB, vin, vout, defect = radial_collision(5, 10, -1, -1)
check("negative_common_beta_is_regular_and_current_conserving",
      EA == 2 and EB == 3 and vin == -sp.Rational(5, 6)*e1
      and vout == -sp.Rational(5, 6)*e2 and zero(defect))
EA, EB, vin, vout, defect = radial_collision(2, 6, 2, 3)
check("unequal_radial_current_coefficients_fail_on_a_regular_AB_collision",
      EA == 2 and EB == 3 and vin == 2*e1 and vout == 2*e2
      and defect == -e1+e2)

# The source's explicit orbit-ball separation, checked as rational geometry.
rotations = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([-1, 1], repeat=3):
        R = sp.zeros(3)
        for row, col in enumerate(perm):
            R[row, col] = signs[row]
        if R.det() == 1:
            rotations.append(R)
q = sp.Matrix([sp.Rational(1, 5), sp.Rational(2, 5), sp.Rational(3, 5)])
orbit = [R*q for R in rotations]
minimum = min((x-y).dot(x-y) for i, x in enumerate(orbit) for y in orbit[i+1:])
check("cubic_counterexample_support_balls_are_disjoint",
      len(rotations) == 24 and len({tuple(x) for x in orbit}) == 24
      and minimum == sp.Rational(6, 25) and minimum > sp.Rational(4, 100)**2,
      {"minimum_squared_separation": str(minimum), "twice_support_diameter": "4/100"})

print(json.dumps({"checks": checks, "python": platform.python_version(),
                  "sympy": sp.__version__, "elapsed_seconds": time.monotonic()-started,
                  "scope": "Exact independent geometry and actual continuum-collision ansatz controls; no physical measure verification or unrestricted C1 proof."}, sort_keys=True))
