#!/usr/bin/env python3
"""Independent monitored-completion, dark-state and coherent-clock controls."""
from pathlib import Path
from itertools import combinations, product
import json
import sys
import time
import sympy as s

HERE = Path(__file__).resolve().parent


def one_color_operators(n, edges, birth_edges, kappa, beta, d):
    # Bit one denotes a vacancy. This constructs the ENTIRE 2^n Hilbert space.
    dim = 2**n
    H = s.zeros(dim)
    monitors = []
    births = []
    for x in range(n):
        monitors.append(s.diag(*[1-((mask >> x) & 1) for mask in range(dim)]))
    for x, y in edges:
        for mask in range(dim):
            if ((mask >> x) & 1) != ((mask >> y) & 1):
                H[mask ^ (1 << x) ^ (1 << y), mask] += kappa
    for x, y in birth_edges:
        J = s.zeros(dim)
        for mask in range(dim):
            if (mask & (1 << x)) and (mask & (1 << y)):
                J[mask ^ (1 << x) ^ (1 << y), mask] = 1
        births.append((beta, J))
    I = s.eye(dim)
    L = -s.I*(s.kronecker_product(I, H)-s.kronecker_product(H.T, I))
    for rate, J in births+[(d, x) for x in monitors]:
        JJ = J.T*J
        L += rate*(s.kronecker_product(J, J)-(s.kronecker_product(I, JJ)+s.kronecker_product(JJ.T, I))/2)
    tr = I.vec().T
    assert tr*L == s.zeros(1, dim*dim)
    return H, L


def extract(L, dim, hilbert_indices):
    indices = [r+dim*c for c in hilbert_indices for r in hilbert_indices]
    return L.extract(indices, indices)


def mean_operator(K, q):
    inverse = K.inv(method='DM')
    vecT = -inverse.conjugate().T*s.eye(q).vec()
    T = s.Matrix(q, q, lambda r, c: vecT[r+q*c])
    assert T == T.conjugate().T
    assert K.conjugate().T*T.vec() == -s.eye(q).vec()
    minors = [s.factor(T[:j, :j].det(method='domain-ge')) for j in range(1, q+1)]
    assert all(x > 0 for x in minors)
    return T, {'dimension': q, 'leading_principal_minors': list(map(str, minors)),
               'trace': str(s.factor(T.trace())), 'trace_inverse': str(s.factor(T.inv(method='DM').trace()))}


def square_symbolic_lumping():
    k, b, d = s.symbols('k beta d', positive=True)
    p, a, c, r1, r2, y = s.symbols('p a c r1 r2 y', real=True)
    variables = s.Matrix([p, a, c, r1, r2, y])
    masks = [5, 10, 3, 6, 12, 9]  # opposite 02/13, followed by four adjacent pairs.
    H = s.zeros(6)
    for i in range(2):
        for j in range(2, 6):
            H[i, j] = H[j, i] = k
    def density(v):
        pp, aa, cc, rr1, rr2, yy = v
        rho = s.zeros(6)
        rho[0, 0] = rho[1, 1] = pp/2
        rho[0, 1] = rho[1, 0] = cc
        for j in range(4):
            rho[2+j, 2+j] = aa/4
            for l in range(4):
                if j != l:
                    rho[2+j, 2+l] = rr2 if (j-l) % 4 == 2 else rr1
        for i in range(2):
            for j in range(2, 6):
                rho[i, j] = s.I*yy
                rho[j, i] = -s.I*yy
        return rho
    rho = density(variables)
    actual = -s.I*(H*rho-rho*H)
    for i in range(6):
        for j in range(6):
            actual[i, j] -= (b*(int(i >= 2)+int(j >= 2))/2+d*s.Rational((masks[i]^masks[j]).bit_count(), 2))*rho[i, j]
    rhs = s.Matrix([-16*k*y, 16*k*y-b*a, -8*k*y-2*d*c,
                    4*k*y-(b+d)*r1, 4*k*y-(b+2*d)*r2,
                    k*(p/2+c-a/4-2*r1-r2)-(b/2+d)*y])
    assert (actual-density(rhs)).applyfunc(s.expand) == s.zeros(6)
    M = rhs.jacobian(variables)
    initial = s.Matrix([1, 0, -s.Rational(1, 2), 0, 0, 0])
    integrals = -M.inv(method='DM')*initial
    mean = s.factor(integrals[0]+integrals[1])
    target = 1/d+s.Rational(3, 2)/b+1/(b+d)+1/(2*(b+2*d))+(b+2*d)/(16*k*k)
    assert s.factor(mean-target) == 0
    return {'variables': list(map(str, variables)), 'ODE': list(map(str, rhs)),
            'integrated_variables': list(map(lambda x: str(s.factor(x)), integrals)),
            'mean_compact': str(target), 'mean_combined': str(mean)}, target, (k, b, d)


def finite_liouvillian_checks(target, params):
    cycle = [(0, 1), (1, 2), (2, 3), (0, 3)]
    Q = [mask for mask in range(1, 16) if mask.bit_count() % 2 == 0]
    h2 = [mask for mask in range(16) if mask.bit_count() == 2]
    records = []
    for rates in [(s.Integer(1), s.Integer(1), s.Integer(1)),
                  (s.Rational(2, 3), s.Rational(5, 4), s.Rational(7, 5)),
                  (s.Integer(2), s.Rational(3, 2), s.Rational(1, 4))]:
        k, b, d = rates
        H, L = one_color_operators(4, cycle, cycle, k, b, d)
        K = extract(L, 16, h2)
        T, cert = mean_operator(K, len(h2))
        rho = s.zeros(6)
        i, j = h2.index(5), h2.index(10)
        rho[i, i] = rho[j, j] = s.Rational(1, 2)
        rho[i, j] = rho[j, i] = -s.Rational(1, 2)
        mean = s.factor((T*rho).trace())
        assert s.factor(mean-target.subs(dict(zip(params, rates)))) == 0
        rec = {'kappa': str(k), 'beta': str(b), 'd': str(d),
               'dark_initial_mean': str(mean), 'positive_mean_operator_certificate': cert}
        if rates == (1, 1, 1):
            Tfull, fullcert = mean_operator(extract(L, 16, Q), len(Q))
            rec['all_even_nonfull_mean_operator'] = fullcert
            rec['empty_initial_mean'] = str(Tfull[Q.index(15), Q.index(15)])
            sparse = [[i, j, str(L[i, j])] for i in range(256) for j in range(256) if L[i, j] != 0]
            (HERE/'C4_FULL_LIOUVILLIAN.json').write_text(json.dumps({'basis': 'vacancy bit masks 0..15, vectorized column-major',
                    'kappa': '1', 'beta': '1', 'd': '1', 'shape': [256, 256], 'entries': sparse}, indent=2)+'\n')
            rec['full_Liouville_dimension'] = 256
            rec['full_Liouville_nonzeros'] = len(sparse)
        records.append(rec)
    # Removal of monitoring: the opposite-hole antisymmetric vector is dark.
    H0, L0 = one_color_operators(4, cycle, cycle, 1, 1, 0)
    v = s.zeros(16, 1)
    v[5], v[10] = 1, -1
    dark = v*v.T/2
    assert H0*v == s.zeros(16, 1)
    assert L0*dark.vec() == s.zeros(256, 1)
    # Removal of effective hopping, even with monitoring: opposite-hole mixture.
    _, Lstuck = one_color_operators(4, cycle, cycle, 0, 1, 1)
    mixture = s.zeros(16)
    mixture[5, 5] = mixture[10, 10] = s.Rational(1, 2)
    assert Lstuck*mixture.vec() == s.zeros(256, 1)
    # Odd vacancy parity never reaches full occupation.
    _, L = one_color_operators(4, cycle, cycle, 1, 1, 1)
    odd = s.zeros(16)
    for x in range(4):
        odd[1 << x, 1 << x] = s.Rational(1, 4)
    assert L*odd.vec() == s.zeros(256, 1)
    # No perfect matching is needed: star K1,3, births on just one edge.
    star = [(0, 1), (0, 2), (0, 3)]
    _, Lstar = one_color_operators(4, star, [(0, 1)], 1, 1, 1)
    Tstar, starcert = mean_operator(extract(Lstar, 16, Q), len(Q))
    return {'cycle_cases': records, 'unmonitored_square_dark_density_stationary': True,
            'zero_hopping_even_vacancy_trap_stationary': True,
            'odd_one_hole_density_stationary': True,
            'star_single_birth_edge_positive_mean_operator': starcert,
            'star_empty_initial_mean': str(Tstar[Q.index(15), Q.index(15)])}


def torus_dark_and_reachability():
    N = 4
    coords = list(product(range(N), repeat=3))
    index = {x: i for i, x in enumerate(coords)}
    neighbours = []
    for x in coords:
        nn = []
        for axis in range(3):
            for sign in (-1, 1):
                y = list(x)
                y[axis] = (y[axis]+sign) % N
                nn.append(index[tuple(y)])
        assert len(set(nn)) == 6
        neighbours.append(nn)
    edges = {tuple(sorted((i, j))) for i, nn in enumerate(neighbours) for j in nn}
    assert len(edges) == 192
    pairs = list(combinations(range(64), 2))
    pair_index = {pair: i for i, pair in enumerate(pairs)}
    sine = [0, 1, 0, -1]
    def amp(i, j):
        x, y = coords[i], coords[j]
        return sine[(y[0]-x[0]) % 4]*sine[(y[1]-x[1]) % 4]
    f = [amp(i, j) for i, j in pairs]
    assert all(amp(i, j) == amp(j, i) for i, j in pairs)
    norm = sum(x*x for x in f)
    assert norm == 512
    residual = []
    for i, j in pairs:
        hf = sum(amp(k, j) for k in neighbours[i] if k != j)
        hf += sum(amp(i, k) for k in neighbours[j] if k != i)
        residual.append(hf-4*amp(i, j))
    assert set(residual) == {0}
    assert all(amp(i, j) == 0 for i, j in edges)
    # Construct 31 disjoint birth edges leaving 000 and 111 vacant.
    matching = set()
    for x, y in product(range(4), repeat=2):
        for z in (0, 2):
            matching.add(tuple(sorted((index[(x, y, z)], index[(x, y, z+1)]))))
    path = [(0, 0, 0), (0, 0, 1), (0, 1, 1), (0, 1, 0), (1, 1, 0), (1, 1, 1)]
    pedges = [tuple(sorted((index[path[i]], index[path[i+1]]))) for i in range(5)]
    for i, edge in enumerate(pedges):
        assert edge in edges
        if i % 2 == 0:
            assert edge in matching
            matching.remove(edge)
        else:
            assert edge not in matching
            matching.add(edge)
    used = [x for edge in matching for x in edge]
    assert len(matching) == 31 and len(set(used)) == 62
    holes = sorted(set(range(64))-set(used))
    assert [coords[x] for x in holes] == [(0, 0, 0), (1, 1, 1)]
    assert amp(*holes) == 1
    hole_marginals = [s.Rational(sum(f[pair_index[tuple(sorted((i, j)))]]**2 for j in range(64) if j != i), norm) for i in range(64)]
    assert set(hole_marginals) == {s.Rational(1, 32)}
    monitoring_fidelity_derivative = -sum(h*(1-h) for h in hole_marginals)
    assert monitoring_fidelity_derivative == -s.Rational(31, 16)
    return {'side': N, 'sites': 64, 'undirected_edges': len(edges), 'two_hole_states_checked': len(pairs),
            'amplitude_squared_norm': norm, 'hopping_eigenvalue_for_unit_kappa': 4,
            'max_absolute_eigen_residual': max(map(abs, residual)), 'all_contact_amplitudes_zero': True,
            'birth_only_matching_edges': [[coords[i], coords[j]] for i, j in sorted(matching)],
            'remaining_holes': [coords[x] for x in holes], 'dark_overlap_squared_in_zero_waiting_limit': '1/512',
            'unit_monitoring_initial_dark_fidelity_derivative': str(monitoring_fidelity_derivative),
            'reachability_scope': 'One occupied color, uniform real hopping, H0=0, positive pair births on the displayed 31 edges (in particular positive rates on all nearest-neighbour edges); small positive waiting-time intervals, not zero-time events, give a positive-probability history with nonzero dark projection.'}


def three_state_clock():
    k, b = s.symbols('k beta', positive=True)
    H = s.Matrix([[0, k, 0], [k, 0, 0], [0, 0, 0]])
    J = s.zeros(3)
    J[2, 1] = 1
    I = s.eye(3)
    R = J.T*J
    L = -s.I*(s.kronecker_product(I, H)-s.kronecker_product(H.T, I))
    L += b*(s.kronecker_product(J, J)-(s.kronecker_product(I, R)+s.kronecker_product(R.T, I))/2)
    assert I.vec().T*L == s.zeros(1, 9)
    K = extract(L, 3, [0, 1])
    initial = s.Matrix([[1, 0], [0, 0]]).vec()
    integrated = -K.inv(method='DM')*initial
    mean = s.factor((s.eye(2).vec().T*integrated)[0])
    assert s.factor(mean-(2/b+b/(4*k*k))) == 0
    return {'mean': str(mean), 'mean_sum_form': '2/beta + beta/(4*kappa^2)',
            'at_unit_rates': str(mean.subs({k: 1, b: 1})),
            'limits': 'kappa=0 or beta=0: no first birth from A, infinite mean.'}


def main():
    started = time.monotonic()
    lump, target, params = square_symbolic_lumping()
    print('Square symbolic six-variable closure and mean checked.', flush=True)
    finite = finite_liouvillian_checks(target, params)
    print('Full finite Liouvillian, positive mean operators and premise-removal controls checked.', flush=True)
    torus = torus_dark_and_reachability()
    print('N4 two-hole eigenstate and explicit 31-birth preparation route checked.', flush=True)
    clock = three_state_clock()
    result = {'boundary': 'Pre-author-source independent calculation.', 'square_symbolic': lump,
              'finite_Liouvillian': finite, 'torus_dark_state': torus, 'three_state_clock': clock,
              'runtime_seconds': time.monotonic()-started,
              'versions': {'python': sys.version, 'sympy': s.__version__}}
    (HERE/'RESULTS.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
