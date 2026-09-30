#!/usr/bin/env python3
"""Finite exact controls for the supplied native dilute-thermodynamics theorem.

Author integration openly reuses earlier literal word and boundary-row controls.
New exact sphere, centering and number-transfer fixtures complement analytic proofs.
No finite control computes T0, a thermodynamic ground state, or a phase observable.
No external scientific data are read at runtime; declared source inputs bind the
mathematical/provenance context through runner_cache. This runner writes stdout only.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, factorial, isqrt
import json

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = [
    'docs/NATIVE_DILUTE_THERMODYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-30.md',
    'docs/NATIVE_DILUTE_PHYSICAL_BOUNDARY_PROOF_2026-09-30.md',
    'docs/NATIVE_DILUTE_CELL_INTERACTION_PROOF_2026-09-30.md',
    'docs/NATIVE_DILUTE_LOWER_AND_LIMITS_PROOF_2026-09-30.md',
    'docs/NATIVE_QUBIT_PAIR_DENSITY_ONSET_BOUNDED_THEOREM_NOTE_2026-09-30.md',
    'docs/NATIVE_FOUR_PARTICLE_THRESHOLD_BOUNDED_THEOREM_NOTE_2026-09-30.md',
    'docs/NATIVE_FOUR_PARTICLE_PERIODIC_BAND_PROOF_2026-09-30.md',
    'docs/NATIVE_FOUR_PARTICLE_THRESHOLD_LIMIT_PROOF_2026-09-30.md',
]

# Scratch mutations alter these actual implementation choices, never expected values.
GRADIENT_WEIGHT = 1
RETAIN_INDIVIDUAL_PLANE_ROWS = True
KEEP_INCIDENT_PINS = True
PLANE_GRADIENT_MULTIPLICITY = 1
SAFE_BOUNDARY_SUBTRACTION = 1
BAD_PARTICLE_F_CHARGE = 2
CENTER_BEFORE_HOLES = True
HUSIMI_MIXED_COEFFICIENT = 4
RESERVE_NUMBER_BUFFER = True
SEAM_WIDTH = 2
PAIR_QUARTIC_DIVISOR = 2

axes = [tuple(int(i == j) for i in range(3)) for j in range(3)]
plus = lambda a, b: tuple(x+y for x, y in zip(a, b))
times = lambda c, a: tuple(c*x for x in a)
minus = lambda a, b: plus(a, times(-1, b))
unit = [times(s, e) for e in axes for s in (-1, 1)]
planes = list(combinations(range(3), 2))
directions = [times(2, e) for e in axes]+[plus(axes[i], times(s, axes[j]))
    for i, j in planes for s in (1, -1)]
graph = set(directions)|{times(-1, d) for d in directions}
canonical = lambda S: tuple(sorted(S))
edge = lambda a, b: canonical((a, b))
phi = lambda m: (m-1)*(m-2)//2

axial = [((times(-1, e), e), 1) for e in axes]
channels = [[(axial[0][0], 1), (axial[1][0], -1)],
            [(axial[0][0], 1), (axial[1][0], 1), (axial[2][0], -2)]]
for i, j in planes:
    channels.append([((times(s, axes[i]), times(t, axes[j])), s*t)
                     for s, t in product((-1, 1), repeat=2)])
weights = [F(1, 2), F(1, 6), F(1, 4), F(1, 4), F(1, 4)]


def action(S):
    """Literal hard-core H column as its separate rational mu and tau parts."""
    S = frozenset(S)
    out = defaultdict(lambda: [F(0), F(0)])
    tri = sum(comb(sum(plus(x, d) in S for d in graph), 2) for x in S)
    out[canonical(S)][0] += len(S)+tri
    centers = {minus(x, u) for x in S for u in unit}
    for c in centers:
        for a, ch in enumerate(channels):
            for pair, cs in ch:
                annih = frozenset(plus(c, u) for u in pair)
                if not annih <= S:
                    continue
                remain = S-annih
                targets = [(c, F(-2 if a < 2 else -1), F(6))]
                targets += [(plus(c, u), F(0), F(-1)) for u in unit]
                for target, mu, tau in targets:
                    for pp, ct in ch:
                        create = frozenset(plus(target, u) for u in pp)
                        if create & remain:
                            continue
                        key = canonical(remain | create)
                        coeff = weights[a]*cs*ct
                        out[key][0] += coeff*mu
                        out[key][1] += GRADIENT_WEIGHT*coeff*tau
    return {s: tuple(c) for s, c in out.items() if any(c)}


def incoming_E_squared(S):
    """Actual coefficient of normalized C_E1^2, with both ordered pairings."""
    def w(x, y):
        d = minus(y, x)
        return (1 if d in (times(2, axes[0]), times(-2, axes[0]))
                else -1 if d in (times(2, axes[1]), times(-2, axes[1])) else 0)
    a, b, c, d = S
    return sum(w(*e)*w(*f) for e, f in
               [((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c))])


def literal_word_control():
    # Expected diagonal/source are the separately derived local-word equations:
    # only the middle axial-y edge is occupied; its number/E/gradient terms give
    # 4mu-4mu/3+4tau, while contraction of the actual Hermitian column gives tau/3.
    S = canonical([(0, 0, 0), (3, -1, 1), (3, 1, 1), (6, 0, 0)])
    row = action(S)
    assert row[S] == (F(8, 3), F(4)), ('literal diagonal', row[S])
    source = tuple(sum(c[j]*incoming_E_squared(T) for T, c in row.items())
                   for j in range(2))
    assert source == (F(0), F(1, 3)), ('literal source', source)
    for T, c in row.items():
        assert action(T).get(S, (F(0), F(0))) == c, ('Hermitian word', T)
    controls = []
    for mu, tau in [(F(1), F(1)), (F(2), F(1)), (F(1, 3), F(3, 2))]:
        h = row[S][0]*mu+row[S][1]*tau
        f = source[0]*mu+source[1]*tau
        generator = -f/(2*h)
        improvement = -generator*f-generator*generator*h
        assert improvement == tau*tau/(96*mu+144*tau)
        controls.append({'mu': str(mu), 'tau': str(tau),
                         'strict_u4_improvement': str(improvement)})
    # The four-site vector at pulse order u^2 is C^2/2, whereas the physical
    # threshold incoming vector is C^2/sqrt(2). Square their actual ratio.
    raw_vector_scale_squared = F(1, 4)
    incoming_scale_squared = F(1, 2)
    computed_quartic_ratio = F(1, PAIR_QUARTIC_DIVISOR)
    assert computed_quartic_ratio == raw_vector_scale_squared/incoming_scale_squared
    return {'sparse_column_entries': len(row), 'hermitian_reverse_columns': len(row),
            'diagonal_mu_tau': [str(x) for x in row[S]],
            'source_mu_tau': [str(x) for x in source], 'couplings': controls,
            'pulse_to_threshold_energy_ratio': str(computed_quartic_ratio)}


def anchor(pair):
    x, y = pair
    d = minus(y, x)
    if d in directions:
        return directions.index(d), x
    return directions.index(times(-1, d)), y


def rank_mod(rows, n=9, p=101):
    """A full minor mod101 proves rational full rank; explicit nulls bound above."""
    a = [[x % p for x in row] for row in rows]
    r = 0
    for j in range(n):
        i = next((i for i in range(r, len(a)) if a[i][j]), None)
        if i is None:
            continue
        a[i], a[r] = a[r], a[i]
        z = pow(a[r][j], -1, p)
        a[r] = [(x*z) % p for x in a[r]]
        for k in range(r+1, len(a)):
            z = a[k][j]
            if z:
                a[k] = [(x-z*y) % p for x, y in zip(a[k], a[r])]
        r += 1
    return r


def boundary_control():
    results = []
    for L in (5, 6):
        sites = set(product(range(L), repeat=3))
        edges = {edge(x, plus(x, d)) for x in sites for d in directions
                 if plus(x, d) in sites}
        constants = []
        row_count = family_count = 0
        incidence = {e: F(0) for e in edges}
        for x in sites:
            pp = [edge(plus(x, u), minus(x, u)) for u in axes]
            rows = []
            if all(all(y in sites for y in p) for p in pp):
                rows.append((dict.fromkeys(pp, 1), F(2, 3)))
                family_count += 1
            for i, j in planes:
                words = [(edge(plus(x, times(s, axes[i])), plus(x, times(t, axes[j]))), s*t)
                         for s, t in product((-1, 1), repeat=2)]
                full = all(all(y in sites for y in p) for p, c in words)
                family_count += 6*full
                for (p, c), (q, d) in combinations(words, 2):
                    if (full or RETAIN_INDIVIDUAL_PLANE_ROWS) and all(
                            y in sites for z in (p, q) for y in z):
                        rows.append(({p: c, q: -d}, F(1, 4)))
            for row, weight in rows:
                row_count += 1
                z = [0]*9
                for p, c in row.items():
                    z[anchor(p)[0]] += c
                constants.append(z)
                size = weight*sum(c*c for c in row.values())
                for p in row:
                    incidence[p] += size
        # Independent count: four plane differences share an endpoint; two do not.
        expected_rows = (L-2)**3+3*(4*(L-2)*(L-1)*L+2*(L-2)**2*L)
        assert row_count == expected_rows, ('individual rows', L, row_count, expected_rows)
        distinct = {tuple(r) for r in constants}
        soft = [[1, -1, 0, 0, 0, 0, 0, 0, 0], [1, 1, -2, 0, 0, 0, 0, 0, 0]]
        for j in (3, 5, 7):
            v = [0]*9
            v[j], v[j+1] = -1, 1
            soft.append(v)
        assert rank_mod(distinct) == 4
        assert all(sum(a*b for a, b in zip(r, v)) == 0 for r in distinct for v in soft)
        hist = defaultdict(int)
        for y in sites:
            pins = {anchor(p)[0] for p in edges if y in p} if KEEP_INCIDENT_PINS else set()
            rk = rank_mod(list(distinct)+[tuple(int(i == d) for i in range(9)) for d in pins])
            assert rk == 9, ('physical incident pin', L, y, rk)
            hist[rk] += 1
        grad15, grad9 = defaultdict(int), defaultdict(int)
        for x in sites:
            words = [(times(-1, u), u) for u in axes]+[
                (times(s, axes[i]), times(t, axes[j])) for i, j in planes
                for s, t in product((-1, 1), repeat=2)]
            for u, v in words:
                p = edge(plus(x, u), plus(x, v))
                for step in axes:
                    q = edge(plus(plus(x, u), step), plus(plus(x, v), step))
                    if p in edges and q in edges:
                        grad15[canonical((p, q))] += 1
            for d in directions:
                p = edge(x, plus(x, d))
                for step in axes:
                    q = edge(plus(x, step), plus(plus(x, d), step))
                    if p in edges and q in edges:
                        grad9[canonical((p, q))] += 1
        assert grad15.keys() == grad9.keys()
        for pq in grad9:
            assert grad9[pq] == 1
            expected = 1 if anchor(pq[0])[0] < 3 else PLANE_GRADIENT_MULTIPLICITY
            assert grad15[pq] == expected, ('gradient multiplicity', pq)
            for p in pq:
                incidence[p] += 2
        assert max(incidence.values()) <= 15
        boundary = sum(any(plus(x, d) not in sites for d in graph) for x in sites)
        assert boundary == L**3-(L-4)**3
        assert F(boundary, L**3) <= F(12, L)
        counts = [sum(plus(x, d) in sites for x in sites) for d in directions]
        assert counts == [(L-2)*L*L]*3+[(L-1)**2*L]*6
        results.append({'L': L, 'individual_S_rows': row_count,
                        'complete_family_subset_rows': family_count,
                        'pins_tested': sum(hist.values()), 'pin_rank': 9,
                        'bare_gradient_rows_with_multiplicity': sum(grad15.values()),
                        'unique_gradient_rows': len(grad9), 'max_incidence': str(max(incidence.values())),
                        'boundary_vertices': boundary, 'anchor_counts': counts})
    return results


def safe_diagonal_control():
    cases = 0
    for q in range(19):
        for m in range(19-q):
            computed = phi(m)-SAFE_BOUNDARY_SUBTRACTION*int(q > 0 and m == 0)
            expected = min(phi(m+j) for j in range(q+1))
            assert computed == expected >= 0, ('safe boundary diagonal', m, q)
            for j in range(q+1):
                assert computed <= phi(m+j)
                cases += 1
    return {'allowed_internal_external_counts': cases,
            'maximum_occupation_polynomial_degree': 19}


def bad_particle_control():
    points = [(0, 0, 0), (2, 0, 0), (-10, 0, 0), (-12, 0, 0),
              (0, 2, 0), (1, 1, 0), (0, 0, 2), (23, 0, 0),
              (25, 0, 0), (42, 1, 0), (43, 2, 0), (60, 0, 0), (63, 0, 0)]
    b = 10
    near = [[max(abs(x-y) for x, y in zip(p, q)) <= b for q in points] for p in points]
    nb = [[minus(q, p) in graph for q in points] for p in points]
    strict_factor_cases = 0
    for mask in range(1 << len(points)):
        occupied = [i for i in range(len(points)) if mask >> i & 1]
        degrees = {i: sum(nb[i][j] for j in occupied) for i in occupied}
        D = sum(phi(degrees[i]) for i in occupied)
        F_b = sum(sum(near[i][j] for j in occupied) >= 3 for i in occupied)
        good = set()
        for i, j in combinations(occupied, 2):
            if nb[i][j] and not any(near[i][k] or near[j][k] for k in occupied if k not in (i, j)):
                good.update((i, j))
        bad = len(occupied)-len(good)
        assert bad <= D+BAD_PARTICLE_F_CHARGE*F_b, ('actual bad-particle count', mask)
        strict_factor_cases += bad > D+F_b
    assert strict_factor_cases > 0
    assert 896*125*125 == 14000000
    assert 251+2*14000000 <= 28000322
    return {'physical_occupation_masks': 1 << len(points), 'radius': b,
            'cases_requiring_factor_two': strict_factor_cases}


def centered_source_control():
    # One literal output occupation; forbidden removed edges have zero amplitude.
    L = 5
    sites = set(product(range(L), repeat=3))
    xi = {(1, 1, 1), (3, 1, 1)}
    checks = 0
    nonzero_removed_means = 0
    for d in directions:
        anchors = sorted(x for x in sites if plus(x, d) in sites)
        hole = {x for x in anchors if {x, plus(x, d)} & xi}
        if not hole:
            continue
        kernel = {x: F(1+(x[0]+2*x[1]+3*x[2]) % 7, 11)
                  if max(abs(x[j]-2) for j in range(3)) <= 1 else F(0) for x in anchors}
        source_anchors = anchors if CENTER_BEFORE_HOLES else [x for x in anchors if x not in hole]
        mean = sum(kernel[x] for x in source_anchors)/len(source_anchors)
        centered = {x: kernel[x]-mean for x in anchors}
        assert sum(centered.values()) == 0, ('full-anchor Neumann centering', d)
        # These are exactly possible independent physical coefficients psi(xi union e).
        # All intersecting edges are forced zero by the true annihilator.
        amplitude = {x: F(0) if x in hole else F((3*x[0]-x[1]+2*x[2]) % 11-5, 13)
                     for x in anchors}
        lhs = sum(kernel[x]*amplitude[x] for x in anchors)
        rhs = sum(centered[x]*amplitude[x] for x in anchors)+mean*sum(amplitude.values())
        assert lhs == rhs
        nonzero_removed_means += mean != 0
        checks += 1
    assert checks == 9 and nonzero_removed_means == 9
    return {'actual_forward_anchor_rectangles': checks,
            'source_pairing': 'exact Fraction identity, holes imposed on physical removal amplitudes only',
            'whole_zone_or_limit_estimate_computed': False}


# Exact Gaussian rationals keep complex off-diagonal sphere controls literal.
def ga(z):
    return z if isinstance(z, tuple) else (F(z), F(0))
def gadd(a, b):
    a, b = ga(a), ga(b)
    return a[0]+b[0], a[1]+b[1]
def gmul(a, b):
    a, b = ga(a), ga(b)
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]
def gconj(a):
    a = ga(a)
    return a[0], -a[1]
def gsum(it):
    s = ga(0)
    for x in it:
        s = gadd(s, x)
    return s

def occ_factor(a):
    result = 1
    for x in a:
        result *= factorial(x)
    return result

def annihilate(state, indices):
    out = {}
    for a, c in state.items():
        b = list(a)
        factor = 1
        for i in indices:
            factor *= b[i]
            b[i] -= 1
            if factor == 0:
                break
        if factor:
            key = tuple(b)
            out[key] = gadd(out.get(key, ga(0)), gmul(factor, c))
    return out

def inner(a, b):
    return gsum(gmul(occ_factor(k), gmul(gconj(c), b.get(k, ga(0)))) for k, c in a.items())


def sphere_control():
    d = 5
    rows = []
    for n in (2, 3, 5):
        state = {
            (n, 0, 0, 0, 0): (F(1), F(1)),
            (0, n, 0, 0, 0): (F(-2), F(1)),
            (n-1, 0, 1, 0, 0): (F(1, 2), F(-1)),
            (0, n-1, 0, 1, 0): (F(-1), F(1, 3)),
            (0, 0, n-1, 0, 1): (F(2), F(0)),
        }
        norm = inner(state, state)
        assert norm[1] == 0 and norm[0] > 0
        Z = norm[0]
        one = [annihilate(state, (i,)) for i in range(d)]
        two = {(i, j): annihilate(state, (i, j)) for i, j in product(range(d), repeat=2)}
        g1 = {(i, k): gmul(F(1, n)/Z, inner(one[k], one[i]))
              for i, k in product(range(d), repeat=2)}
        prefactor = F(comb(n+d-1, d-1)*factorial(n)*factorial(d-1), factorial(n+d+1))/Z
        cases = nonreal = 0
        for i, j, k, l in product(range(d), repeat=4):
            direct = ga(0)
            for alpha, ca in state.items():
                for beta, cb in state.items():
                    p, q = list(beta), list(alpha)
                    p[i] += 1; p[j] += 1
                    q[k] += 1; q[l] += 1
                    if p == q:
                        direct = gadd(direct, gmul(prefactor*occ_factor(p), gmul(ca, gconj(cb))))
            gamma2 = gmul(F(1, n*(n-1))/Z, inner(two[k, l], two[i, j]))
            mixed = gsum([gmul(int(j == l), g1[i, k]), gmul(int(j == k), g1[i, l]),
                          gmul(int(i == l), g1[j, k]), gmul(int(i == k), g1[j, l])])
            rhs = gsum([gmul(n*(n-1), gamma2),
                        gmul(F(HUSIMI_MIXED_COEFFICIENT*n, 4), mixed),
                        ga(int(i == k and j == l)+int(i == l and j == k))])
            rhs = gmul(F(1, (n+d)*(n+d+1)), rhs)
            assert direct == rhs, ('complex sphere identity', n, i, j, k, l, direct, rhs)
            cases += 1
            nonreal += direct[1] != 0
        assert nonreal > 0
        p = F(n*(n-1), (n+5)*(n+6))
        assert n*(n-1)*(1-p) <= 27*n
        rows.append({'n': n, 'ordered_matrix_entries': cases,
                     'nonreal_entries': nonreal, 'unnormalized_state_norm_squared': str(Z)})
    return rows


def ceil_fraction(x):
    return -((-x.numerator)//x.denominator)


def canonical_transfer_control():
    ell = 5
    m = ell**3
    probabilities = {0: F(1, 4), 2: F(1, 3), 6: F(5, 12)}
    rho = sum(k*p for k, p in probabilities.items())/m
    assert sum(probabilities.values()) == 1 and 0 < rho < 1
    q = min(rho, 1-rho)
    rows = []
    for L in (500, 503):
        V = L**3
        B = (L//ell)**3
        R = V-m*B
        for sign in (-1, 1):
            nominal = (rho*V).numerator//(rho*V).denominator+sign*2*isqrt(V)
            N = nominal if nominal % 2 else nominal+1
            d = N-rho*V
            D = 2*m*m
            r = ceil_fraction((abs(d)+D+2)/(q*m))+1 if RESERVE_NUMBER_BUFFER else 0
            assert 0 <= r < B
            Bp = B-r
            counts = {k: (Bp*probabilities.get(k, F(0))).numerator//(Bp*probabilities.get(k, F(0))).denominator
                      for k in range(m)}
            counts[m] = Bp-sum(counts.values())
            assert counts[m] >= 0 and sum(counts.values()) == Bp
            error = sum(abs(counts[k]-Bp*probabilities.get(k, F(0))) for k in range(m+1))
            Nreg = sum(k*count for k, count in counts.items())
            assert error <= 2*m and abs(Nreg-Bp*rho*m) <= D
            U = R+r*m
            needed = N-Nreg
            assert 0 <= needed <= U, ('reserved exact integer capacity', L, sign, needed, U)
            assert q*U > abs(d)+D+1
            assert N % 2 == 1
            rows.append({'L': L, 'N': N, 'rounding_sign': sign, 'regular_cubes': Bp,
                         'reserved_sites': U, 'exact_reserved_particles': needed,
                         'full_sector_probability_initially_zero': True})
    # Direct support enumeration prices BOTH original and artificial periodic terms.
    seam_results = []
    for ell in (5, 6, 8):
        sites = set(product(range(ell), repeat=3))
        support = {(0, 0, 0)}|set(unit)|graph
        changed = sum(any(plus(x, d) not in sites for d in support) for x in sites)
        predicted = ell**3-(ell-2*SEAM_WIDTH)**3
        assert predicted == changed, ('actual radius-two centers', ell, predicted, changed)
        assert 2*changed <= 24*ell**2
        seam_results.append({'ell': ell, 'changed_centers': changed,
                             'two_operator_terms_per_center': 2})
    return {'integer_fixtures': rows, 'seams': seam_results}


def main():
    results = {
        'scope': 'Finite exact author controls; infinite-volume and dilute conclusions are analytic proofs.',
        'provenance': 'Literal word and boundary action paths openly reuse earlier source-bound controls; no new independent-review claim.',
        'literal_word_and_pair_factor': literal_word_control(),
        'physical_boundary_rows_pins_and_gradients': boundary_control(),
        'safe_diagonal': safe_diagonal_control(),
        'all_N_bad_particle_count': bad_particle_control(),
        'centered_physical_removal_pairing': centered_source_control(),
        'finite_complex_sphere_identity': sphere_control(),
        'exact_number_transfer_and_seams': canonical_transfer_control(),
    }
    print(json.dumps(results, indent=2, sort_keys=True))
    print('TOTAL: PASS=7 FAIL=0')


if __name__ == '__main__':
    main()
