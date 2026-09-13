"""Small exact native challenges to the Block3 analytical localization proof.

This does not prove the arbitrary-volume locality or semigroup estimates.
It constructs a genuine native fuel-changing seed, its full and truncated
conjugation jets, the energy-defect identity, and battery Fourier factors.
All calculations are by the campaign author; independent review is pending.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parent
checks = {}


def equal(a, b):
    delta = a-b
    if isinstance(delta, s.MatrixBase):
        return all(s.expand(x) == 0 for x in delta)
    return s.simplify(delta) == 0


def check(name, condition):
    checks[name] = bool(condition)
    if not condition:
        raise AssertionError(name)


def comm(a, b):
    return a*b-b*a


edges = ((0, 1), (1, 2), (2, 3), (3, 4))
dim = 16
eye = s.eye(dim)
Z = [s.diag(*[(-1)**((word >> e) & 1) for word in range(dim)])
     for e in range(4)]
vertex_parity = []
for v in range(5):
    op = eye
    for e, endpoints in enumerate(edges):
        if v in endpoints:
            op = op*Z[e]
    vertex_parity.append(op)
number = [(eye-b)/2 for b in vertex_parity]
N = sum(number, s.zeros(dim))
T = []
for e, (u, v) in enumerate(edges):
    mask = []
    for root, other in ((u, v), (v, u)):
        for f, endpoints in enumerate(edges):
            if f != e and root in endpoints:
                neighbor = endpoints[1] if endpoints[0] == root else endpoints[0]
                if neighbor < other:
                    mask.append(f)
    A = s.zeros(dim)
    for word in range(dim):
        sign = (-1)**sum((word >> f) & 1 for f in mask)
        A[word ^ (1 << e), word] = sign
    t = s.I*A*(vertex_parity[u]-vertex_parity[v])/2
    check(f'native_Hermitian_{e}', equal(t, t.H))
    check(f'native_number_{e}', equal(comm(t, N), s.zeros(dim)))
    check(f'native_cubic_{e}', equal(t**3, t))
    T.append(t)

weights = (s.S.One, s.Rational(2, 3), s.Rational(3, 5), s.Rational(4, 7))
h = [w*t for w, t in zip(weights, T)]
Hin = sum(h, s.zeros(dim))
Hout = Hin-h[0]
Hin_R = h[0]+h[1]
Hout_R = h[1]
Q = [(eye+z*Z[0])/2 for z in (1, -1)]
directed = T[0]*number[0]*(eye-number[1])
active = number[0]*(eye-number[1])
check('directed_effect', equal(directed.H*directed, active))
check('directed_Q_order_sign', equal(Q[0]*directed, directed*Q[1]))
check('wrong_Q_order_detected', not equal(Q[0]*directed, directed*Q[0]))
for z, q in enumerate(Q):
    check(f'target_full_H_preserves_new_Record_{z}', equal(comm(Hout, q), s.zeros(dim)))
    check(f'target_local_H_preserves_new_Record_{z}', equal(comm(Hout_R, q), s.zeros(dim)))
check('full_complete_effect', equal(sum((q.H*q for q in Q), s.zeros(dim)), eye))
check('feedback_effect_not_identity', not equal(active, eye))

# One eligible fuel is retained explicitly: fuel0 is the output block,
# fuel1 is the input block. A common 3*Delta scalar is removed from BOTH
# sectors. The remaining +Delta in the input block must not disappear.
gap = s.S.One
A = s.diag(Hout, Hin+gap*eye)
A_R = s.diag(Hout_R, Hin_R+gap*eye)
cut = A-A_R
N_big = s.diag(N, N)
fuel_live = s.diag(s.zeros(dim), eye)
fuel_spent = s.eye(2*dim)-fuel_live


def ambient_seed(local):
    op = s.zeros(2*dim)
    op[:dim, dim:] = local
    return op


def jets(ham, seed, order):
    values = [seed]
    for n in range(order):
        values.append(-s.I*comm(ham, values[-1])/(n+1))
    return values


first_nonzero = {}
matrix_witnesses = {}
for law in ('complete', 'feedback'):
    seeds = [ambient_seed(q if law == 'complete' else q*directed) for q in Q]
    effect = sum((b.H*b for b in seeds), s.zeros(2*dim))
    expected = fuel_live if law == 'complete' else s.diag(s.zeros(dim), active)
    check(law+'_summed_effect', equal(effect, expected))
    for z, b in enumerate(seeds):
        tag = f'{law}_{z}'
        check(tag+'_spends_fuel', equal(fuel_spent*b*fuel_live, b))
        check(tag+'_no_overwrite', equal(b*fuel_spent, s.zeros(2*dim)))
        check(tag+'_N_conserved', equal(comm(b, N_big), s.zeros(2*dim)))
        check(tag+'_cut_initially_commutes', equal(comm(cut, b), s.zeros(2*dim)))
        full = jets(A, b, 5)
        local = jets(A_R, b, 5)
        nonzero = [n for n in range(6) if not equal(full[n], local[n])]
        if equal(b, s.zeros(2*dim)):
            # This bridge isolates vertex0. A directed hop empties it, so
            # its negative-Z output is impossible, before or after dressing.
            check(tag+'_expected_null_bridge', law == 'feedback' and z == 1)
            check(tag+'_null_bridge_all_jets', all(equal(op, s.zeros(2*dim)) for op in full+local))
            first_nonzero[tag] = None
            matrix_witnesses[tag] = {'status': 'identically_zero_bridge_branch'}
        else:
            check(tag+'_genuine_truncation_change', bool(nonzero))
            first_nonzero[tag] = min(nonzero)
            delta = full[min(nonzero)]-local[min(nonzero)]
            i, j = next((i, j) for i in range(2*dim) for j in range(2*dim) if delta[i, j] != 0)
            matrix_witnesses[tag] = {'order': min(nonzero), 'row': i, 'column': j,
                                     'coefficient': str(delta[i, j])}
        for n in range(5):
            # E=-i*d/dtau, so its coefficient is -i(n+1)Y_(n+1).
            direct_energy_comm = comm(A, local[n])-s.I*(n+1)*local[n+1]
            check(tag+f'_energy_boundary_coefficient_{n}',
                  equal(direct_energy_comm, comm(cut, local[n])))
            check(tag+f'_new_Record_jet_{n}',
                  equal(s.diag(Q[z], eye)*local[n], local[n]))
            check(tag+f'_N_jet_{n}', equal(comm(local[n], N_big), s.zeros(2*dim)))

# An old Record at the last edge is guarded by spent last fuel: remove h3.
A_old = s.diag(Hout-h[3], Hin-h[3]+gap*eye)
old_Record = s.diag(Z[3], Z[3])
check('old_Record_full_guard', equal(comm(A_old, old_Record), s.zeros(2*dim)))
check('old_Record_local_guard', equal(comm(A_R, old_Record), s.zeros(2*dim)))
check('old_Record_feedback_seed_guard',
      equal(comm(ambient_seed(Q[0]*directed), old_Record), s.zeros(2*dim)))

# Source-head block counting on a path, independent of all native matrices.
head_degree = (1, 2, 1)
head_effect = s.zeros(3)
for v, w in ((0, 1), (1, 0), (1, 2), (2, 1)):
    move = s.zeros(3)
    move[w, v] = 1
    head_effect += move.H*move
check('head_eligibility_sum', equal(head_effect, s.diag(*head_degree)))
check('head_bound_uses_degree_not_edge_count', max(head_degree) == 2)

# A real energy ladder checks the Fourier sign against energy conservation.
E = s.diag(0, 1, 2)
up = s.zeros(3)
up[1, 0] = up[2, 1] = 1
down = up.H
system_E = s.diag(0, 1)
lower = s.Matrix([[0, 1], [0, 0]])
Htot = s.kronecker_product(system_E, s.eye(3))+s.kronecker_product(s.eye(2), E)
correct_lift = s.kronecker_product(lower, up)
wrong_lift = s.kronecker_product(lower, down)
check('actual_ladder_energy_lift_sign', equal(comm(Htot, correct_lift), s.zeros(6)))
check('reversed_battery_shift_detected', not equal(comm(Htot, wrong_lift), s.zeros(6)))

# Fourier formula from a direct antiderivative; w scales z=w*tau.
u, z = s.symbols('u z', real=True)
antiderivative = s.exp(s.I*z*u)*(s.I*z*s.sin(s.pi*u)-s.pi*s.cos(s.pi*u))/(s.pi**2-z**2)
check('sine_Fourier_antiderivative',
      equal(s.diff(antiderivative, u), s.exp(s.I*z*u)*s.sin(s.pi*u)))
integral = antiderivative.subs(u, 1)-antiderivative.subs(u, 0)
check('sine_Fourier_numerator', equal(integral, s.pi*(1+s.exp(s.I*z))/(s.pi**2-z**2)))
check('sine_normalization', equal(s.integrate(2*s.sin(s.pi*u)**2, (u, 0, 1)), 1))
phi = integral/s.sqrt(s.pi)
check('removable_positive_pole', equal(s.limit(phi, z, s.pi), s.I/(2*s.sqrt(s.pi))))
check('removable_negative_pole', equal(s.limit(phi, z, -s.pi), -s.I/(2*s.sqrt(s.pi))))
x = s.symbols('x', nonnegative=True)
tail_denominator_margin = s.expand((3+x)**2-s.Rational(9, 16)*(4+x)**2)
check('tail_denominator_positive_coefficients',
      all(coefficient >= 0 for coefficient in s.Poly(tail_denominator_margin, x).all_coeffs()))
check('two_sided_tail_constant', equal(2*s.Rational(64, 9)/3, s.Rational(128, 27)))
v, time = s.symbols('v time', positive=True)
bracket = (s.exp(v*time)-1)/v-time
check('locality_Duhamel_integral', equal(s.diff(bracket, time), s.exp(v*time)-1))
check('zero_interaction_limit', equal(s.limit(bracket, v, 0), 0))
for radius in range(1, 7):
    count = sum(abs(a)+abs(b)+abs(c) == radius
                for a in range(-radius, radius+1)
                for b in range(-radius, radius+1)
                for c in range(-radius, radius+1))
    check(f'cubic_l1_sphere_{radius}', count == 4*radius*radius+2)

payload = {
    'status': 'all_small_exact_checks_passed',
    'author_check_only': True,
    'proof': 'BLOCK03_DERIVATION.md',
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'check_count': len(checks),
    'checks': checks,
    'first_changed_Taylor_order': first_nonzero,
    'native_matrix_witnesses': matrix_witnesses,
    'scope': 'Finite exact operator and scalar counterchecks; general estimates are analytical.'
}
(ROOT/'BLOCK03_CHECKS.json').write_text(json.dumps(payload, indent=2)+'\n')
print(json.dumps({key: value for key, value in payload.items() if key != 'checks'}, indent=2))
