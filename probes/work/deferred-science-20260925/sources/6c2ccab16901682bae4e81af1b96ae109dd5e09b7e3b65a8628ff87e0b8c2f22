#!/usr/bin/env python3
"""Own exact finite controls for the blind formation/response reconstruction.

Standard-library Gaussian rational arithmetic; no historical program import.
No time evolution is truncated or simulated. The checks concern core operator
identities, physical paths, geometry, and the exact number-changing loss.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product, combinations
from collections import deque
from pathlib import Path
import hashlib
import json
import time

TIC = time.perf_counter()


@dataclass(frozen=True)
class G:
    r: F = F(0)
    i: F = F(0)

    def __add__(self, other):
        if not isinstance(other, G):
            other = G(F(other))
        return G(self.r + other.r, self.i + other.i)

    def __neg__(self):
        return G(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if not isinstance(other, G):
            other = G(F(other))
        return G(self.r*other.r-self.i*other.i,
                 self.r*other.i+self.i*other.r)

    def conjugate(self):
        return G(self.r, -self.i)


ZERO, ONE = G(), G(F(1))


def add(*vectors):
    out = {}
    for vector in vectors:
        for word, weight in vector.items():
            out[word] = out.get(word, ZERO) + weight
    return {word: weight for word, weight in out.items() if weight != ZERO}


def scale(vector, weight):
    return {word: value*weight for word, value in vector.items()
            if value*weight != ZERO}


def inner(left, right):
    value = ZERO
    for word, weight in left.items():
        value = value + weight.conjugate()*right.get(word, ZERO)
    return value


def compose(left, right):
    return lambda vector: left(right(vector))


def lattice(length):
    vertices = tuple(product(range(length), repeat=3))
    index = {v: i for i, v in enumerate(vertices)}
    A = tuple(i for i, v in enumerate(vertices) if sum(v) % 2 == 0)
    aset = set(A)
    B = tuple(i for i in range(len(vertices)) if i not in aset)
    def moved(v, axis):
        z = list(v); z[axis] = (z[axis]+1) % length
        return tuple(z)
    edges = []
    for x, v in enumerate(vertices):
        for axis in range(3):
            y = index[moved(v, axis)]
            edges.append((x, y) if x in aset else (y, x))
    assert len(set(edges)) == 3*length**3
    edge_index = {frozenset(e): k for k, e in enumerate(edges)}
    neighbours = {v: [] for v in range(len(vertices))}
    for k, (a, b) in enumerate(edges):
        neighbours[a].append((b, k, 1))
        neighbours[b].append((a, k, -1))
    plaquettes = []
    for x, v in enumerate(vertices):
        for mu, nu in combinations(range(3), 2):
            corners = (x, index[moved(v, mu)],
                       index[moved(moved(v, mu), nu)], index[moved(v, nu)])
            circulation = [0]*len(edges)
            for u, w in zip(corners, corners[1:]+corners[:1]):
                k = edge_index[frozenset((u, w))]
                circulation[k] = 1 if edges[k] == (u, w) else -1
            assert sum(t*t for t in circulation) == 4
            plaquettes.append((corners, tuple(circulation)))
    assert len({tuple(sorted(c)) for c, w in plaquettes}) == 3*length**3
    return vertices, A, B, tuple(edges), neighbours, tuple(plaquettes)


def gauss(word, A, edges):
    q, electric = word
    div = [0]*len(q)
    for (a, b), e in zip(edges, electric):
        div[a] += e; div[b] -= e
    assert div == [v-int(i in A) for i, v in enumerate(q)]


def flow(q, A, edges, neighbours):
    parent = {0: None}; order = [0]; queue = deque([0])
    while queue:
        u = queue.popleft()
        for v, k, sign_u in neighbours[u]:
            if v not in parent:
                parent[v] = (u, k, -sign_u)
                order.append(v); queue.append(v)
    assert len(order) == len(q)
    sub = [v-int(i in A) for i, v in enumerate(q)]
    electric = [0]*len(edges)
    for v in reversed(order[1:]):
        u, k, sign_v = parent[v]
        electric[k] = sign_v*sub[v]
        sub[u] += sub[v]
    assert sub[0] == 0
    word = (tuple(q), tuple(electric)); gauss(word, A, edges)
    return word


def shift(vector, circulation, direction=1):
    out = {}
    for (q, electric), weight in vector.items():
        dest = (q, tuple(e+direction*c for e, c in zip(electric, circulation)))
        out[dest] = out.get(dest, ZERO)+weight
    return out


def diagonal(vector, values):
    return scale_each(vector, lambda word: G(F(values(word))))


def scale_each(vector, values):
    return {word: weight*values(word) for word, weight in vector.items()
            if weight*values(word) != ZERO}


def D(word, edges):
    q, electric = word
    return sum(e*(e-q[a]) for (a, b), e in zip(edges, electric)
               if q[a] and not q[b])


def quadrature(circulation, which):
    def action(vector):
        plus = shift(vector, circulation)
        minus = shift(vector, circulation, -1)
        if which == 'X':
            return scale(add(plus, minus), G(F(1, 2)))
        return add(scale(plus, G(F(0), F(-1, 2))),
                   scale(minus, G(F(0), F(1, 2))))
    return action


def double_commutator(left, energy, right, vector):
    return add(left(energy(right(vector))),
               scale(left(right(energy(vector))), G(F(-1))),
               scale(energy(right(left(vector))), G(F(-1))),
               right(energy(left(vector))))


def primitive(vector, paths):
    out = {}
    for word, coefficient in vector.items():
        for dest in paths(word):
            out[dest] = out.get(dest, ZERO)+coefficient
    return {word: weight for word, weight in out.items() if weight != ZERO}


def outward(word, a, neighbours):
    q, electric = word
    if not q[a]:
        return []
    outputs = []
    for b, k, sign in neighbours[a]:
        assert sign == 1
        if q[b]:
            continue
        r, f = list(q), list(electric)
        r[a], r[b] = 0, q[a]; f[k] -= q[a]
        outputs.append((tuple(r), tuple(f)))
    return outputs


def inward(word, a, neighbours):
    q, electric = word
    if q[a]:
        return []
    outputs = []
    for b, k, sign in neighbours[a]:
        if not q[b]:
            continue
        r, f = list(q), list(electric)
        r[a], r[b] = q[b], 0; f[k] += q[b]
        outputs.append((tuple(r), tuple(f)))
    return outputs


def creation(word, a, b, k, sigma, adjoint=False):
    q, electric = word
    if not adjoint:
        if q[a] or q[b]:
            return []
        r, f = list(q), list(electric)
        r[a], r[b] = sigma, -sigma; f[k] += sigma
    else:
        if q[a] != sigma or q[b] != -sigma:
            return []
        r, f = list(q), list(electric)
        r[a], r[b] = 0, 0; f[k] -= sigma
    return [(tuple(r), tuple(f))]


def main():
    geometry = []
    for length in (4, 6, 8):
        vs, aa, bb, ee, nn, pp = lattice(length)
        B_inc = {b: 0 for b in bb}; edge_inc = [0]*len(ee)
        for corners, circulation in pp:
            for b in corners:
                if b in B_inc:
                    B_inc[b] += 1
            for k, c in enumerate(circulation):
                edge_inc[k] += abs(c)
        assert set(B_inc.values()) == {12}
        assert set(edge_inc) == {4}
        geometry.append({'L': length, 'vertices': len(vs), 'plaquettes': len(pp),
                         'B_sites': len(bb), 'plaquettes_per_B': 12,
                         'plaquettes_per_edge': 4,
                         'response_per_vacancy_at_K1': 48})

    vs, A, B, edges, neighbours, plaquettes = lattice(4)
    index = {v: i for i, v in enumerate(vs)}
    def matter(vacancies, minus_A=()):
        q = [0]*len(vs)
        for a in A:
            q[a] = -1 if a in minus_A else 1
        occupied = [b for b in B if b not in vacancies]
        target_B = len(A)-sum(q)
        assert (len(occupied)+target_B) % 2 == 0
        positive = (len(occupied)+target_B)//2
        assert 0 <= positive <= len(occupied)
        for i, b in enumerate(occupied):
            q[b] = 1 if i < positive else -1
        return tuple(q)
    far_vacancies = (index[(1, 0, 0)], index[(3, 2, 2)])
    close_vacancies = (index[(1, 0, 0)], index[(0, 1, 0)])
    patterns = [
        ('initial', matter(B)),
        ('full_occupancy', matter(())),
        ('isolated_two_vacancies', matter(far_vacancies)),
        ('nearby_two_vacancies', matter(close_vacancies)),
        ('eight_vacancies_one_minus_A', matter(B[:8], (A[0],))),
        ('sixteen_vacancies_two_minus_A', matter(B[:16], A[:2])),
    ]
    words = [(name, flow(q, A, edges, neighbours)) for name, q in patterns]
    # Add a noncontractible integer circulation, preserving Gauss.
    winding = [0]*len(edges)
    for x in range(4):
        u, v = index[(x, 0, 0)], index[((x+1) % 4, 0, 0)]
        for k, e in enumerate(edges):
            if frozenset(e) == frozenset((u, v)):
                winding[k] = 3 if e == (u, v) else -3
    q, electric = words[0][1]
    wind_word = (q, tuple(e+c for e, c in zip(electric, winding)))
    gauss(wind_word, A, edges); words.append(('initial_with_winding_three', wind_word))

    operator_rows, coherence_rows, primitive_rows, balance_rows = [], [], [], []
    selected = (0, 13, 74)
    Eop = lambda vector: diagonal(vector, lambda word: D(word, edges))
    total = lambda word: 48*sum(word[0][b] == 0 for b in B)
    Rop = lambda vector: diagonal(vector, total)
    for name, word in words:
        q, electric = word
        gauss(word, A, edges)
        vacuum_count = sum(q[b] == 0 for b in B)
        total_from_faces = sum(2*sum((not q[b])*c*c for (a, b), c in zip(edges, circ))
                               for corners, circ in plaquettes)
        assert total_from_faces == total(word)
        balance_rows.append({'state': name, 'N': sum(t != 0 for t in q),
                             'vacant_B': vacuum_count,
                             'summed_response': total_from_faces,
                             'capacity_relation_exact': total_from_faces == 48*(len(vs)-sum(t != 0 for t in q))})
        for number in selected:
            corners, circ = plaquettes[number]
            X, Y = quadrature(circ, 'X'), quadrature(circ, 'Y')
            atom = {word: ONE}
            Ap = sum((not q[b])*c*c for (a, b), c in zip(edges, circ))
            assert Ap == 2*sum(q[b] == 0 for b in corners if b in B)
            xx = double_commutator(X, Eop, X, atom)
            yy = double_commutator(Y, Eop, Y, atom)
            xy = double_commutator(X, Eop, Y, atom)
            assert xx == scale(Y(Y(atom)), G(F(2*Ap)))
            assert yy == scale(X(X(atom)), G(F(2*Ap)))
            assert xy == scale(X(Y(atom)), G(F(-2*Ap)))
            assert add(xx, yy) == scale(atom, G(F(2*Ap)))
            operator_rows.append({'state': name, 'plaquette': number, 'D': D(word, edges),
                                  'A_p': Ap, 'XX_YY_XY_and_sum_exact': True,
                                  'output_words_XX': len(xx)})
            for phase_name, phase in [('plus', ONE), ('minus', G(F(-1))), ('imaginary', G(F(0), F(1)))]:
                superposition = add(atom, scale(shift(atom, circ, 2), phase))
                norm = inner(superposition, superposition).r
                a = inner(superposition, double_commutator(X, Eop, X, superposition)).r/norm
                c = inner(superposition, double_commutator(Y, Eop, Y, superposition)).r/norm
                off = inner(superposition, double_commutator(X, Eop, Y, superposition)).r/norm
                assert a >= 0 and c >= 0 and a*c-off*off >= 0
                assert a+c == 2*Ap
                coherence_rows.append({'state': name, 'plaquette': number, 'phase': phase_name,
                                       'XX': str(a), 'YY': str(c), 'XY': str(off),
                                       'matrix_determinant': str(a*c-off*off), 'sum': str(a+c)})

        # Nontrivial primitive path tests on a selected local star.
        a = next(v for v in plaquettes[0][0] if v in A)
        b, k, sign = neighbours[a][0]
        circ = plaquettes[0][1]
        W = lambda vector: shift(vector, circ)
        Fa = lambda vector: primitive(vector, lambda w: outward(w, a, neighbours))
        Fstar = lambda vector: primitive(vector, lambda w: inward(w, a, neighbours))
        atom = {word: ONE}
        assert W(Fa(atom)) == Fa(W(atom))
        mids = Fa(atom)
        assert W(Fstar(mids)) == Fstar(W(mids))
        jumps, adjoints = [], []
        for sigma in (-1, 1):
            j = lambda vector, s=sigma: primitive(vector, lambda w: creation(w, a, b, k, s))
            js = lambda vector, s=sigma: primitive(vector, lambda w: creation(w, a, b, k, s, True))
            jumps.append(compose(j, Fa)); adjoints.append(compose(Fstar, js))
        instruments = [('resolved_minus', jumps[0], adjoints[0]),
                       ('resolved_plus', jumps[1], adjoints[1]),
                       ('coherent_edge', lambda v: add(jumps[0](v), jumps[1](v)),
                        lambda v: add(adjoints[0](v), adjoints[1](v)))]
        for label, jump, adjoint in instruments:
            outputs = jump(atom)
            for destination in outputs:
                gauss(destination, A, edges)
                assert sum(t != 0 for t in destination[0]) == sum(t != 0 for t in q)+2
                assert total(destination) == total(word)-96
            assert W(outputs) == jump(W(atom))
            loss = adjoint(jump(atom))
            dissipative = add(adjoint(Rop(jump(atom))),
                              scale(adjoint(jump(Rop(atom))), G(F(-1, 2))),
                              scale(Rop(loss), G(F(-1, 2))))
            assert dissipative == scale(loss, G(F(-96)))
            primitive_rows.append({'state': name, 'instrument': label,
                                   'jump_output_words': len(outputs),
                                   'jump_norm_squared': str(inner(outputs, outputs).r),
                                   'Wilson_commutator_exact': True,
                                   'Gauss_and_number_change_exact': True,
                                   'response_loss_balance_exact': True})
    assert all(row['jump_output_words'] == 0 for row in primitive_rows
               if row['state'] == 'isolated_two_vacancies')
    result = {'scope': 'Own exact finite primitive identities; no evolution simulation, author code or photon identification.',
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'geometry_rows': geometry, 'operator_rows': operator_rows,
              'coherence_rows': coherence_rows, 'primitive_rows': primitive_rows,
              'global_balance_rows': balance_rows,
              'all_assertions_passed': True, 'elapsed_seconds': time.perf_counter()-TIC}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
