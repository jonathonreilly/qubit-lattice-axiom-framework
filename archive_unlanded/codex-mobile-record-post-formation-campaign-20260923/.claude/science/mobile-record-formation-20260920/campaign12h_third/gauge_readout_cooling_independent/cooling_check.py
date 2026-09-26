#!/usr/bin/env python3
"""Independently assembled physical component, exact ranks, and countercontrol."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter, deque
import hashlib
import json
import time
import numpy as np
from scipy.linalg import expm
import sympy as s
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent


def exact_rank(A):
    return DomainMatrix.from_Matrix(A.applyfunc(s.expand)).convert_to(s.QQ_I).rank()


def vector(A):
    return s.Matrix([A[i, j] for j in range(A.cols) for i in range(A.rows)])


def unvector(v, n):
    return s.Matrix(n, n, lambda i, j: v[i+n*j])


def jump(n, pairs):
    L = s.zeros(n)
    for a, b in pairs:
        for row in (a, b):
            L[row, a] += s.Rational(1, 2)
            L[row, b] -= s.Rational(1, 2)
    assert L*L == s.zeros(n)
    P = L.H*L; assert P*P == P
    return L


def liouvillian(jumps, rates, energies):
    n = jumps[0].rows; I = s.eye(n)
    P = [L.H*L for L in jumps]
    H = sum((h*A for h, A in zip(energies, P)), s.zeros(n))
    B = sum((g*A for g, A in zip(rates, P)), s.zeros(n))
    G = -s.I*(s.kronecker_product(I, H)-s.kronecker_product(H.T, I))
    for L, A, g in zip(jumps, P, rates):
        G += g*(s.kronecker_product(L.conjugate(), L)-
                (s.kronecker_product(I, A)+s.kronecker_product(A.T, I))/2)
    return G, H, B, P


def physical_component():
    width = 3
    edges = [((x, y), (x+1, y)) for y in (0, 1) for x in range(width)]
    edges += [((x, 0), (x, 1)) for x in range(width+1)]
    index = {e: i for i, e in enumerate(edges)}; z = []
    for x in range(width):
        v = [0]*len(edges)
        for edge, sign in [(((x, 0), (x+1, 0)), 1), (((x+1, 0), (x+1, 1)), 1),
                           (((x, 1), (x+1, 1)), -1), (((x, 0), (x, 1)), -1)]:
            v[index[edge]] = sign
        z.append(v)
    def positive(b, v):
        return all(((b >> i) & 1) == (0 if a > 0 else 1) for i, a in enumerate(v) if a)
    def adjacent(b):
        for v in z:
            mask = sum(1 << i for i, a in enumerate(v) if a)
            if positive(b, v) or positive(b, [-a for a in v]):
                yield b ^ mask
    remaining = set(range(1 << len(edges))); components = []
    while remaining:
        root = min(remaining); remaining.remove(root); todo = deque([root]); component = []
        while todo:
            b = todo.popleft(); component.append(b)
            for new in adjacent(b):
                if new in remaining:
                    remaining.remove(new); todo.append(new)
        components.append(sorted(component))
    C = min(c for c in components if len(c) == max(map(len, components)))
    ix = {a: i for i, a in enumerate(C)}; pairs = []
    for v in z:
        mask = sum(1 << i for i, a in enumerate(v) if a)
        local = [(ix[b], ix[b ^ mask]) for b in C if positive(b, v)]
        assert len({x for pair in local for x in pair}) == 2*len(local)
        for a, b in local:
            assert [((C[b] >> i) & 1)-((C[a] >> i) & 1) for i in range(len(edges))] == v
        pairs.append(local)
    vertices = sorted({x for edge in edges for x in edge})
    incidence = s.zeros(len(vertices), len(edges))
    for e, (x, y) in enumerate(edges):
        incidence[vertices.index(x), e] = 1; incidence[vertices.index(y), e] = -1
    assert all(incidence*s.Matrix(v) == s.zeros(len(vertices), 1) for v in z)
    charges = [incidence*s.Matrix([s.Rational(2*((b >> i) & 1)-1, 2) for i in range(len(edges))]) for b in C]
    assert all(q == charges[0] for q in charges)
    inventory = json.loads((HERE/'GEOMETRY_INVENTORY.json').read_text())
    assert C == inventory['selected_largest_lexicographic_component']
    assert {str(k): v for k, v in Counter(map(len, components)).items()} == inventory['component_size_histogram']
    return C, z, pairs, edges, charges[0]


def polynomial_lowering(f, x, delta):
    current = s.expand(f-f.subs(x, x+delta)); g = s.S.Zero; coefficient = s.Rational(1, 2)
    while current != 0:
        g += coefficient*current
        current = s.expand(current.subs(x, x+delta)-current)
        coefficient *= -s.Rational(1, 2)
    return s.expand(g)


def physical_controls():
    C, z, pairs, edges, charge = physical_component(); n = len(C)
    jumps = [jump(n, a) for a in pairs]
    rates = [s.Integer(1), s.Integer(2), s.Integer(3)]
    energies = [-s.Integer(2), s.Rational(1, 3), s.Integer(4)]
    G, H, B, P = liouvillian(jumps, rates, energies)
    ones = s.ones(n, 1); rho = s.ones(n)/n
    assert exact_rank(s.Matrix.vstack(*jumps)) == n-1
    assert all(L*ones == s.zeros(n, 1) for L in jumps)
    assert G*vector(rho) == s.zeros(n*n, 1)
    rank = exact_rank(G); assert rank == n*n-1
    Q = H+s.I*B/2
    # The integer encoded word separates all five configurations. Its change
    # under each plaquette is constant, so it suffices for polynomial controls.
    x = s.Symbol('x'); rows = []
    for degree in range(n):
        f = x**degree; fvec = s.Matrix([f.subs(x, a) for a in C]); rhs = s.zeros(n, 1)
        for p, (L, v) in enumerate(zip(jumps, z)):
            delta = sum((1 << i)*a for i, a in enumerate(v))
            g = polynomial_lowering(f, x, delta)
            assert g == 0 or s.degree(g, x) < degree
            gvec = s.Matrix([g.subs(x, a) for a in C])
            assert P[p]*fvec == L.H*gvec
            rhs += (energies[p]+s.I*rates[p]/2)*L.H*gvec
        assert Q*fvec == rhs
        rows.append({'degree': degree, 'all_pair_lowering_identities_exact': True})
    span = ones; todo = deque([ones]); ranks = [1]
    operators = [L.H for L in jumps]+[Q]
    while todo and span.cols < n:
        v = todo.popleft()
        for op in operators:
            new = op*v; candidate = span.row_join(new)
            if exact_rank(candidate) > span.cols:
                span = candidate; todo.append(new); ranks.append(span.cols)
                if span.cols == n: break
    assert span.cols == n
    # Expected total number of selected-p jump records, not all supplied probes.
    A = s.Matrix(G.H); rhs = -vector(B)
    for j in range(n*n): A[0, j] = s.Rational(1, n)
    rhs[0] = 0
    R = unvector(A.inv()*rhs, n).applyfunc(s.expand)
    assert all(s.cancel(a) == 0 for a in G.H*vector(R)+vector(B))
    assert all(s.cancel(a) == 0 for a in R.H-R)
    assert all(s.cancel(a) == 0 for a in R*ones)
    rnum = np.array(R, dtype=complex)
    eigenR = np.linalg.eigvalsh(rnum)
    assert eigenR.min() > -1e-10
    assert np.linalg.eigvalsh(rnum-np.eye(n)+np.ones((n, n))/n).min() > -1e-10
    eig = np.linalg.eigvals(np.array(G, dtype=complex))
    nonzero = [a for a in eig if abs(a) > 1e-10]
    assert len(nonzero) == n*n-1 and max(a.real for a in nonzero) < 0
    # Single-p fresh collision and the exact local semigroup, including h P^-.
    L = jumps[0]; Pminus = P[0]
    Cgate = s.kronecker_product(L, s.Matrix([[0, 0], [1, 0]]))
    Cgate += Cgate.H
    assert Cgate**3 == Cgate
    conserved = s.kronecker_product(Pminus, s.eye(2))+s.kronecker_product(s.eye(n), s.diag(0, 1))
    assert Cgate*conserved == conserved*Cgate
    first = pairs[0][0]; dvec = s.zeros(n, 1); dvec[first[0]] = 1; dvec[first[1]] = -1
    initial = s.kronecker_product(dvec, s.Matrix([1, 0]))
    swap = s.eye(2*n)-Cgate*Cgate-s.I*Cgate
    assert swap*swap*initial == -initial
    t = -2*np.log(.6)/float(rates[0]); p = 1-np.exp(-float(rates[0])*t)
    ln = np.array(L, dtype=complex); pn = np.array(Pminus, dtype=complex)
    M0 = np.eye(n)+(np.exp(-float(rates[0])*t/2-1j*float(energies[0])*t)-1)*pn
    M1 = np.sqrt(p)*ln
    channel = np.kron(M0.conj(), M0)+np.kron(M1.conj(), M1)
    local = liouvillian([L], rates[:1], energies[:1])[0]
    local_error = np.linalg.norm(channel-expm(np.array(local, dtype=complex)*t), ord=2)
    assert local_error < 1e-12
    # Overlapping local finite steps must not be advertised as the exact sum.
    dt = .2; ordered = np.eye(n*n, dtype=complex)
    for Lp, gp, hp in zip(jumps, rates, energies):
        localp = liouvillian([Lp], [gp], [hp])[0]
        ordered = expm(dt*np.array(localp, dtype=complex))@ordered
    product_error = np.linalg.norm(ordered-expm(dt*np.array(G, dtype=complex)), ord=2)
    assert product_error > 1e-5
    return {'geometry': 'Open strip of three square plaquettes, ten spin-half links',
            'component': C, 'component_dimension': n, 'canonical_edges': edges,
            'oriented_pairs_by_plaquette': pairs, 'fixed_displacements': z,
            'common_Gauss_charge_vector': [str(a) for a in charge],
            'rates': [str(a) for a in rates], 'Hamiltonian_coefficients': [str(a) for a in energies],
            'common_dark_dimension_exact': 1, 'Liouvillian_rank_exact': rank,
            'polynomial_degree_lowering_controls': rows,
            'adjoint_jump_and_effective_H_cyclic_span_ranks': ranks,
            'numeric_largest_nonzero_Liouvillian_real_part': float(max(a.real for a in nonzero)),
            'expected_total_jump_count': {'uniform_mixture_exact': str(s.factor(s.trace(R)/n)),
                                          'localized_means_exact': [str(s.factor(R[i, i])) for i in range(n)],
                                          'dual_Poisson_and_target_annihilation_exact': True,
                                          'minimum_eigenvalue_numeric': float(eigenR.min()),
                                          'worst_initial_mean_numeric': float(eigenR.max())},
            'fresh_collision': {'cubic_identity_exact': True, 'local_energy_like_conserved_sum': 'P_minus+P_spent',
                                'single_local_semigroup_spectral_norm_error': float(local_error),
                                'reused_probe_two_pi_over_two_pulses_undo_cooling_exactly': True,
                                'overlapping_plaquette_product_error_at_dt_point2': float(product_error)},
            'scope': 'Exact finite controls support, but do not replace, the displacement/polynomial proof. No uniform volume gap is inferred.'}


def countercontrol():
    jumps = [jump(4, [(0, 1), (2, 3)]), jump(4, [(1, 2), (3, 0)])]
    G, H, B, P = liouvillian(jumps, [1, 1], [0, 0])
    uniform = s.ones(4)/4
    u = s.Matrix([1, 0, -1, 0]); v = s.Matrix([0, 1, 0, -1])
    support = (u*u.T+v*v.T)/2; trapped = support/2
    assert support*support == support and exact_rank(support) == 2
    assert exact_rank(s.Matrix.vstack(*jumps)) == 3
    assert G*vector(uniform) == s.zeros(16, 1)
    assert G*vector(trapped) == s.zeros(16, 1)
    assert s.trace(uniform*trapped) == 0 and s.trace(trapped) == 1
    for L, Pp in zip(jumps, P):
        assert (s.eye(4)-support)*L*support == s.zeros(4)
        assert (s.eye(4)-support)*Pp*support == s.zeros(4)
    # Constant displacements on these two oriented matchings force c0=c2.
    c0, c1, c2, c3, z1, z2 = s.symbols('c0 c1 c2 c3 z1 z2')
    equations = [c1-c0-z1, c3-c2-z1, c2-c1-z2, c0-c3-z2]
    solutions = s.linsolve(equations, (c0, c1, c2, c3, z1, z2))
    assert all(s.expand(sol[0]-sol[2]) == 0 and s.expand(sol[1]-sol[3]) == 0 for sol in solutions)
    return {'dimension': 4, 'oriented_pair_families': [[(0, 1), (2, 3)], [(1, 2), (3, 0)]],
            'connected_configuration_graph': True, 'unique_common_dark_vector': 'uniform',
            'stationary_orthogonal_mixed_state': [[str(x) for x in trapped.row(i)] for i in range(4)],
            'stationary_state_rank': 2, 'uniform_target_overlap': 0,
            'constant_displacement_embedding_would_force': ['c0=c2', 'c1=c3'],
            'conclusion': 'Connectivity and one common dark vector do not imply attraction without the physical move structure.'}


if __name__ == '__main__':
    started = time.monotonic()
    result = {'created_utc': datetime.now(timezone.utc).isoformat(),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'physical_controls': physical_controls(), 'countercontrol': countercontrol(),
              'runtime_seconds': time.monotonic()-started}
    text = json.dumps(result, indent=2)+'\n'
    (HERE/'COOLING_RESULTS.json').write_text(text); print(text, end='')
