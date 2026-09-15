#!/usr/bin/env python3
"""Exact falsifiers for local reference encoding and constructive graph maps.
The scientific source is embedded; general claims rest on the paired proofs.
"""
from dataclasses import dataclass
from itertools import combinations, product
from collections import deque
import copy
import math
import json
import traceback
import numpy as np
from scipy.linalg import expm
AUDIT_TIMEOUT_SEC = 90

@dataclass(frozen=True)
class P:
    p: int = 0
    x: int = 0
    z: int = 0

    def __matmul__(self, b):
        return P((self.p + b.p + 2 * (self.z & b.x).bit_count()) % 4, self.x ^ b.x, self.z ^ b.z)

    def anti(self, b):
        return ((self.x & b.z).bit_count() + (self.z & b.x).bit_count()) % 2

    def dag(self):
        return P((-self.p + 2 * (self.x & self.z).bit_count()) % 4, self.x, self.z)

    def support(self):
        return self.x | self.z

    def weight(self):
        return self.support().bit_count()

    def vec(self, n):
        return self.x | (self.z << n)

    def act(self, n):
        return (n ^ self.x, 1j ** self.p * (-1) ** (self.z & n).bit_count())

def mul(rows):
    ans = P()
    for row in rows:
        ans = ans @ row
    return ans

def reduce_rows(rows, n):
    piv = {}
    for row in rows:
        while row.x or row.z:
            k = row.vec(n).bit_length() - 1
            if k not in piv:
                piv[k] = row
                break
            row = row @ piv[k]
        else:
            assert row.p == 0, ('inconsistent stabilizer phase', row)
    return piv

def remainder(row, piv, n):
    while row.x or row.z:
        k = row.vec(n).bit_length() - 1
        if k not in piv:
            return row
        row = row @ piv[k]
    return row

class Graph:

    def __init__(self, cells, q=6, refs=True, refbonds=False):
        self.cells = tuple(cells)
        self.q = q
        self.refs = refs
        self.v = tuple(((c, a) for c in self.cells for a in range(q + int(refs))))
        self.vid = {v: i for i, v in enumerate(self.v)}
        self.edges = []
        self.eid = {}
        self.streams = []

        def edge(v, w, kind):
            i, j = (self.vid[v], self.vid[w])
            key = frozenset((i, j))
            assert key not in self.eid
            self.eid[key] = len(self.edges)
            self.edges.append((i, j, kind))
        for c in self.cells:
            for a, b in combinations(range(q), 2):
                if q == 6 and a ^ 1 == b:
                    continue
                edge((c, a), (c, b), 'inside')
            if refs:
                for a in range(q):
                    edge((c, a), (c, q), 'spoke')
        cs = set(self.cells)
        for c in self.cells:
            for axis in range(3):
                d = list(c)
                d[axis] += 1
                d = tuple(d)
                if d not in cs:
                    continue
                a, b = (2 * axis + 1, 2 * axis) if q == 6 else (0, 0)
                edge((c, a), (d, b), 'stream')
                self.streams.append((c, a, d, b))
                if refbonds:
                    edge((c, q), (d, q), 'refbond')
        self.inc = [[] for _ in self.v]
        for e, (u, v, _) in enumerate(self.edges):
            self.inc[u].append(e)
            self.inc[v].append(e)

    def B(self, v):
        return P(z=sum((1 << e for e in self.inc[v])))

    def A(self, u, v):
        e = self.eid[frozenset((u, v))]
        z = 0
        for w in (u, v):
            for f in self.inc[w]:
                if f == e:
                    break
                z ^= 1 << f
        return P(0 if u < v else 2, 1 << e, z)

    def path(self, u, v):
        prev = {u: None}
        queue = deque([u])
        while v not in prev:
            w = queue.popleft()
            for e in self.inc[w]:
                a, b, _ = self.edges[e]
                z = b if a == w else a
                if z not in prev:
                    prev[z] = w
                    queue.append(z)
        ans = [v]
        while ans[-1] != u:
            ans.append(prev[ans[-1]])
        return ans[::-1]

    def pathA(self, u, v):
        p = self.path(u, v)
        return P((len(p) - 2) % 4) @ mul((self.A(a, b) for a, b in zip(p, p[1:])))

    def cycles(self):
        prev = {0: None}
        tree = set()
        queue = deque([0])
        while queue:
            u = queue.popleft()
            for e in self.inc[u]:
                a, b, _ = self.edges[e]
                v = b if a == u else a
                if v not in prev:
                    prev[v] = u
                    tree.add(e)
                    queue.append(v)
        assert len(prev) == len(self.v)

        def treepath(u, v):
            pu = []
            w = u
            while w is not None:
                pu.append(w)
                w = prev[w]
            pv = []
            w = v
            while w not in pu:
                pv.append(w)
                w = prev[w]
            return pu[:pu.index(w) + 1] + pv[::-1]
        out = []
        for e, (u, v, _) in enumerate(self.edges):
            if e in tree:
                continue
            vs = treepath(u, v)
            out.append(P(len(vs) % 4) @ mul((self.A(a, b) for a, b in zip(vs, vs[1:] + vs[:1]))))
        return out

    def loaders(self):
        assert self.refs
        xs = []
        zs = []
        ds = []
        for c in self.cells:
            vs = [self.vid[c, a] for a in range(self.q + 1)]
            ds.append(mul((self.B(v) for v in vs)))
            for a in range(self.q):
                zs.append(self.B(vs[a]))
                xs.append(P(3) @ mul((self.B(vs[b]) for b in range(a, self.q))) @ self.A(vs[a], vs[-1]))
        return (xs, zs, ds)

def lift(p, xs, zs):
    return P(p.p) @ mul((xs[i] for i in range(len(xs)) if p.x >> i & 1)) @ mul((zs[i] for i in range(len(zs)) if p.z >> i & 1))

def logical_hop(i, j):
    i, j = sorted((i, j))
    end = 1 << i | 1 << j
    bet = ((1 << j) - 1) ^ ((1 << (i + 1)) - 1)
    return (P(0, end, bet), P(2, end, bet | end))

def stream(g, c, a, d, b, between=True):
    ci, di = (g.cells.index(c), g.cells.index(d))
    if ci > di:
        c, d, a, b, ci, di = (d, c, b, a, di, ci)
    u, v = (g.vid[c, a], g.vid[d, b])
    ru, rv = (g.vid[c, g.q], g.vid[d, g.q])
    core = g.A(ru, u) @ g.A(v, rv)
    bet = mul((g.B(g.vid[g.cells[k], s]) for k in range(ci + 1, di) for s in range(g.q))) if between else P()
    spectator = mul((g.B(g.vid[d, s]) for s in range(g.q) if s != b))
    return (bet @ spectator @ g.B(u) @ g.B(v) @ core, P(2) @ bet @ spectator @ core)

def decode(row, xs, zs, piv, n):
    x = sum((row.anti(z) << i for i, z in enumerate(zs)))
    z = sum((row.anti(a) << i for i, a in enumerate(xs)))
    target = P(0, x, z)
    rem = remainder(row @ lift(target, xs, zs).dag(), piv, n)
    assert rem.x == rem.z == 0
    return P(rem.p, x, z)

def directed_local_stream(g, c, a, d, b):
    u, v = (g.vid[c, a], g.vid[d, b])
    ru, rv = (g.vid[c, g.q], g.vid[d, g.q])
    reference_path = P(2) @ g.A(ru, u) @ g.A(u, v) @ g.A(v, rv)
    core = g.A(u, v) @ reference_path
    spectator = mul((g.B(g.vid[d, k]) for k in range(g.q) if k != b))
    return (P(2) @ spectator @ core, spectator @ g.B(u) @ g.B(v) @ core)

def polynomial_square_is_identity(terms):
    out={}
    for a in terms:
        for b in terms:
            c=a@b;key=(c.x,c.z)
            out[key]=out.get(key,0)+(1j**c.p)/4
    out={key:value for key,value in out.items() if value!=0}
    return out=={(0,0):1}

def annihilate(n, i, create=False):
    if bool(n >> i & 1) == create:
        return None
    return (n ^ 1 << i, (-1) ** (n & (1 << i) - 1).bit_count())

def car_word(n, ops):
    amplitude = 1
    for i, create in reversed(ops):
        r = annihilate(n, i, create)
        if r is None:
            return (n, 0)
        n, a = r
        amplitude *= a
    return (n, amplitude)

def directed(n, i, j):
    return car_word(n, [(j, True), (i, False)])

def dense(p, n):
    out = np.zeros((1 << n, 1 << n), complex)
    for k in range(1 << n):
        j, a = p.act(k)
        out[j, k] = a
    return out

def car_matrix(n, i):
    a = np.zeros((1 << n, 1 << n), complex)
    for k in range(1 << n):
        z = annihilate(k, i)
        if z is not None:
            j, c = z
            a[j, k] = c
    return a

def algebra_checks():
    n = 4
    c = [car_matrix(n, i) for i in range(n)]
    eye = np.eye(1 << n)
    for i in range(n):
        for j in range(n):
            assert np.array_equal(c[i] @ c[j] + c[j] @ c[i], np.zeros_like(eye))
            assert np.array_equal(c[i] @ c[j].conj().T + c[j].conj().T @ c[i], eye * (i == j))
    T = c[0].conj().T @ c[3] + c[3].conj().T @ c[0]
    assert np.array_equal(T, sum((dense(p, n) for p in logical_hop(0, 3))) / 2)
    X = dense(P(x=2), n)
    Z = dense(P(z=1), n)
    assert np.array_equal(T @ X + X @ T, np.zeros_like(T))
    assert np.linalg.norm(T, 2) == 1
    for theta in (0.13, math.pi / 4, math.pi / 2, math.pi):
        U = expm(-1j * theta * T)
        assert abs(np.linalg.norm(U @ X - X @ U, 2) - 2 * abs(math.sin(theta))) < 1e-12
        Y = U.conj().T @ X @ U
        assert abs(np.linalg.norm(Y @ Z - Z @ Y, 2) - 2 * abs(math.sin(2 * theta))) < 1e-12
    rng = np.random.default_rng(705)
    for _ in range(12):
        O = rng.normal(size=T.shape) + 1j * rng.normal(size=T.shape)
        A = (O + X @ O @ X) / 2
        assert np.linalg.norm(A - T, 2) >= 1 - 1e-12
    for q in (1, 2, 6):
        total = q + 1
        for a in range(q):
            for bits in range(1 << q):
                state = bits | bits.bit_count() % 2 << q
                y = state
                amplitude = -1
                for k in (q, a):
                    amplitude *= (-1) ** (y & (1 << k) - 1).bit_count()
                    y ^= 1 << k
                amplitude *= (-1) ** (y & ((1 << q) - 1 ^ (1 << a) - 1)).bit_count()
                expected = bits ^ 1 << a
                expected |= expected.bit_count() % 2 << q
                assert y == expected and amplitude == 1, (q, a, bits, y, amplitude)
    return {'CAR_modes': n, 'local_reference_columns': 2 + 8 + 384, 'unitary_witness_angles': 4}

def graph_checks():
    fixtures = [('L', [(0, 0, 0), (1, 0, 0), (1, 1, 0)], False), ('square', [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)], False), ('square_reference', [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)], True), ('cube3', list(product(range(3), repeat=3)), False), ('cube4', list(product(range(4), repeat=3)), False)]
    rows = []
    for name, cells, refbonds in fixtures:
        g = Graph(cells, refbonds=refbonds)
        n = len(g.edges)
        loops = g.cycles()
        xs, zs, ds = g.loaders()
        m = len(xs)
        assert len(reduce_rows(loops, n)) == n - len(g.v) + 1
        piv = reduce_rows(loops + ds, n)
        assert len(piv) == n - m
        assert len(reduce_rows(loops + [g.B(v) for v in range(len(g.v))], n)) == n
        for i in range(m):
            assert xs[i] @ xs[i] == P() and xs[i] == xs[i].dag()
            for j in range(m):
                assert xs[i].anti(xs[j]) == 0 and xs[i].anti(zs[j]) == (i == j)
            assert all((xs[i].anti(s) == zs[i].anti(s) == 0 for s in loops + ds))
        selected = xs[5::6]
        seen = 0
        for ci, x in enumerate(selected):
            c = g.cells[ci]
            r = g.vid[c, 6]
            spokes = [g.eid[frozenset((g.vid[c, a], r))] for a in range(6)]
            want = P(1, 1 << spokes[5], sum((1 << e for e in spokes)))
            outgoing = [e for e in g.inc[g.vid[c, 5]] if g.edges[e][2] == 'stream']
            assert len(outgoing) <= 1
            want = want @ P(z=sum((1 << e for e in outgoing)))
            assert x == want, (name, c, x, want)
            assert not x.support() & seen
            seen |= x.support()
        bad = 0
        max_between = 0
        for c, a, d, b in g.streams:
            for ucell, ua, vcell, vb in ((c,a,d,b),(d,b,c,a)):
                words=directed_local_stream(g,ucell,ua,vcell,vb)
                terms=(g.B(g.vid[ucell,ua]),g.B(g.vid[vcell,vb]))+words
                assert all(p==p.dag() for p in terms)
                assert polynomial_square_is_identity(terms)
                assert all(not p.anti(stab) for p in terms for stab in loops+ds)
            ci, di = sorted((g.cells.index(c), g.cells.index(d)))
            between = di - ci - 1
            max_between = max(max_between, between)
            ij = (6 * g.cells.index(c) + a, 6 * g.cells.index(d) + b)
            for source, target in zip(stream(g, c, a, d, b), logical_hop(*ij)):
                assert remainder(source @ lift(target, xs, zs).dag(), piv, n) == P()
                assert all((source.anti(xs[6 * k + 5]) == 1 for k in range(ci + 1, di)))
                assert source.weight() >= between
            bet = mul((P(z=sum((1 << 6 * k + s for s in range(6)))) for k in range(ci + 1, di)))
            for source, target in zip(stream(g, c, a, d, b, False), logical_hop(*ij)):
                assert remainder(source @ lift(bet @ target, xs, zs).dag(), piv, n) == P()
            bad += bool(between)
        rows.append({'fixture': name, 'cells': len(cells), 'edges': n, 'code_logicals': m, 'max_intermediate_cells': max_between, 'chords_changed_by_deletion': bad, 'disjoint_loader_max_weight': max((x.weight() for x in selected))})
    return rows

def exchange_checks(spectator=False):
    cells = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)) + (((-1, 0, 0),) if spectator else ())
    g = Graph(cells)
    xs, zs, ds = g.loaders()
    piv = reduce_rows(g.cycles() + ds, len(g.edges))
    exchange = [((0, 1), (1, 0)), ((2, 0), (3, 1)), ((1, 0), (1, 3)), ((1, 3), (2, 2)), ((3, 1), (3, 2)), ((3, 2), (0, 3)), ((2, 2), (2, 0)), ((0, 3), (0, 1))]
    single = [((0, 1), (1, 0)), ((1, 0), (1, 3)), ((1, 3), (2, 2)), ((2, 2), (2, 0)), ((2, 0), (3, 1)), ((3, 1), (3, 2)), ((3, 2), (0, 3)), ((0, 3), (0, 1))]
    phase = {}
    rng = np.random.default_rng(907)
    for edge in exchange:
        phase[edge] = np.exp(1j * rng.uniform(-math.pi, math.pi))
    results = {}
    for label, moves, occupied in [('exchange', exchange, [(0, 1), (2, 0)]), ('one_particle', single, [(0, 1)] + ([(4, 5)] if spectator else []))]:
        initial = sum((1 << 6 * c + a for c, a in occupied))
        expected = initial
        local = initial
        af = al = 1 + 0j
        phases = {initial: np.exp(1j * rng.normal())}
        closed_rephase = 1 + 0j
        for (ci, a), (di, b) in moves:
            i, j = (6 * ci + a, 6 * di + b)
            nxt, amp = directed(expected, i, j)
            assert amp != 0
            targetterms = logical_hop(i, j)
            if ci == di:
                u, v = (g.vid[cells[ci], a], g.vid[cells[di], b])
                physical = (P(1) @ g.A(u, v) @ g.B(u), P(3) @ g.A(u, v) @ g.B(v))
            else:
                physical = directed_local_stream(g, cells[ci], a, cells[di], b)
            localterms = tuple((decode(p, xs, zs, piv, len(g.edges)) for p in physical))
            if ci == di:
                assert set(localterms) == set(targetterms)
            for p, t in zip(physical, localterms):
                assert remainder(p @ lift(t, xs, zs).dag(), piv, len(g.edges)) == P()
            actions = [p.act(local) for p in localterms]
            assert actions[0][0] == actions[1][0]
            newlocal = actions[0][0]
            coefficient = sum((x[1] for x in actions)) / 2
            assert newlocal == nxt and abs(coefficient) == 1
            if nxt not in phases:
                phases[nxt] = np.exp(1j * rng.normal())
            closed_rephase *= phases[nxt].conjugate() * phases[expected]
            factor = phase[(ci, a), (di, b)]
            af *= amp * factor
            al *= coefficient * factor
            local = expected = nxt
        assert expected == initial and local == initial and (abs(closed_rephase - 1) < 1e-12)
        assert abs((af/al).imag)<1e-12
        results[label] = {'fermion_amplitude': [af.real, af.imag], 'local_amplitude': [al.real, al.imag], 'ratio': float((af / al).real), 'moves': len(moves), 'particle_number': len(occupied)}
    assert abs(results['exchange']['ratio'] + 1) < 1e-12
    assert abs(results['one_particle']['ratio'] - 1) < 1e-12
    assert sorted(exchange) == sorted(single)
    return results

def fixed_even_dense_isometry(g):
    n = len(g.edges)
    M = len(g.v)
    loops = g.cycles()
    vac = np.zeros(1 << n, complex)
    vac[0] = 1
    for row in loops:
        vac = (vac + dense(row, n) @ vac) / 2
    vac /= np.linalg.norm(vac)
    basis = [b for b in range(1 << M) if b.bit_count() % 2 == 0]
    columns = []
    for b in basis:
        v = vac.copy()
        fock = 0
        amplitude = 1 + 0j
        for j in range(1, M):
            if not b >> j & 1:
                continue
            v = dense(g.pathA(0, j), n) @ v
            amplitude *= -1j * (-1) ** (fock & (1 << j) - 1).bit_count()
            fock ^= 1 << j
            fock ^= 1
        assert fock == b
        columns.append(v / amplitude)
    E = np.column_stack(columns)
    assert np.max(abs(E.conj().T @ E - np.eye(len(basis)))) < 1e-12
    cs = [car_matrix(M, j) for j in range(M)]
    error = 0.0
    for u in range(M):
        B = np.eye(1 << M) - 2 * cs[u].conj().T @ cs[u]
        assert np.max(abs(dense(g.B(u), n) @ E - E @ B[np.ix_(basis, basis)])) < 1e-12
    for u, v, _ in g.edges:
        T = cs[u].conj().T @ cs[v] + cs[v].conj().T @ cs[u]
        mapped = 1j * dense(g.A(u, v), n) @ (dense(g.B(u), n) - dense(g.B(v), n)) / 2
        err = float(np.max(abs(mapped @ E - E @ T[np.ix_(basis, basis)])))
        assert err < 1e-12
        error = max(error, err)
    return (E, basis, error)

def bksf_dense_checks():
    cells = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0))
    g = Graph(cells, q=1, refs=False)
    E, basis, error = fixed_even_dense_isometry(g)
    for j in range(4):
        assert all((b ^ 1 << j not in basis for b in basis))
    ref = Graph(cells + ((-1, 0, 0),), q=1, refs=False)
    F, even, err = fixed_even_dense_isometry(ref)
    labels = [b | b.bit_count() % 2 << 4 for b in range(16)]
    V = F[:, [even.index(b) for b in labels]]
    assert np.max(abs(V.conj().T @ V - np.eye(16))) < 1e-12
    parity = np.diag([(-1) ** b.bit_count() for b in range(16)])
    assert np.max(abs(dense(ref.B(4), len(ref.edges)) @ V - V @ parity)) < 1e-12
    cs = [car_matrix(4, j) for j in range(4)]
    for u, v, _ in ref.edges:
        if max(u, v) == 4:
            continue
        T = cs[u].conj().T @ cs[v] + cs[v].conj().T @ cs[u]
        mapped = 1j * dense(ref.A(u, v), len(ref.edges)) @ (dense(ref.B(u), len(ref.edges)) - dense(ref.B(v), len(ref.edges))) / 2
        assert np.max(abs(mapped @ V - V @ T)) < 1e-12
    resources = []
    for L in (2, 3, 4):
        g6 = Graph(list(product(range(L), repeat=3)), refs=False)
        n = len(g6.edges)
        M = len(g6.v)
        assert n == 12 * L ** 3 + 3 * (L - 1) * L ** 2 and M == 6 * L ** 3
        assert max(map(len, g6.inc)) == 5
        assert len(reduce_rows(g6.cycles(), n)) == n - M + 1
        resources.append({'L': L, 'edge_qubits': n, 'even_logical_qubits': M - 1, 'maximum_degree': 5})
    return {'matter_modes': 4, 'physical_qubits': 4, 'even_code_dimension': 8, 'max_hopping_residual': error, 'one_reference_physical_qubits': len(ref.edges), 'all_parity_code_dimension': V.shape[1], 'reference_equals_global_matter_parity': True, 'resource_examples': resources}

def geometry_checks():
    rng = np.random.default_rng(773)
    rows = []
    for d in (1, 2, 3):
        for L in (2, 3, 4, 7):
            cells = list(product(range(L), repeat=d))
            N = len(cells)
            edges = []
            idx = {c: i for i, c in enumerate(cells)}
            for c in cells:
                for a in range(d):
                    v = list(c)
                    v[a] += 1
                    v = tuple(v)
                    if v in idx:
                        edges.append((idx[c], idx[v]))
            bound = math.ceil((N - 1) / (d * (L - 1)))
            min_observed = N
            for _ in range(12):
                p = rng.permutation(N)
                gap = max((abs(int(p[u]) - int(p[v])) for u, v in edges))
                assert gap >= bound
                min_observed = min(min_observed, gap)
            rows.append({'d': d, 'L': L, 'universal_edge_gap_lower_bound': bound, 'minimum_random_gap': min_observed})
    for L in (2, 3, 8, 16):
        cells = [(x, 0) for x in range(L)] + [(x, 1) for x in range(L - 1, -1, -1)]
        assert cells[0] == (0, 0) and cells[-1] == (0, 1)
        assert len(cells[1:-1]) == 2 * L - 2
        assert max((min((abs(c[0] - e[0]) + abs(c[1] - e[1]) for e in (cells[0], cells[-1]))) for c in cells[1:-1])) == L - 1
    m = 3
    n = m + 2
    loaders = [P(x=1 << k + 1) for k in range(m)]
    target = logical_hop(0, n - 1)[0]
    assert all((target.anti(x) for x in loaders))
    low = []
    for support_size in range(m):
        for supp in combinations(range(n), support_size):
            for kinds in product((1, 2, 3), repeat=support_size):
                x = z = 0
                for k, kind in zip(supp, kinds):
                    if kind & 1:
                        x |= 1 << k
                    if kind & 2:
                        z |= 1 << k
                row = P(0, x, z)
                syndrome = sum((row.anti(a) << i for i, a in enumerate(loaders)))
                assert syndrome != (1 << m) - 1
                if support_size <= 1:
                    low.append(row)
    for a in low:
        for b in low:
            assert not all(((a @ b).anti(x) for x in loaders))
    active = mul((P(z=1 << k + 1) for k in range(m)))
    assert all((active.anti(x) for x in loaders))
    return rows

def controlled_conj(row, control, S):
    assert not S.support() >> control & 1
    a = row.anti(S)
    b = row.x >> control & 1
    out = row @ (S if b else P()) @ (P(z=1 << control) if a else P())
    return P((out.p + 2 * a * b) % 4, out.x, out.z)

def cz_conj(row, e, f):
    a = row.x >> e & 1
    b = row.x >> f & 1
    return P((row.p + 2 * a * b) % 4, row.x, row.z ^ (a << f) ^ (b << e))

def permutation(row, mapping):
    x = z = 0
    for i, j in enumerate(mapping):
        if row.x >> i & 1:
            x |= 1 << j
        if row.z >> i & 1:
            z |= 1 << j
    return P(row.p, x, z)

def append_edge(g, u, v, kind='refbond'):
    assert frozenset((u, v)) not in g.eid
    e = len(g.edges)
    g.eid[frozenset((u, v))] = e
    g.edges.append((u, v, kind))
    g.inc[u].append(e)
    g.inc[v].append(e)
    return e

def conjugate_word(row, word):
    for control, S in word:
        row = controlled_conj(row, control, S)
    return row

def edge_add(g, u, v, path):
    assert path[0] == u and path[-1] == v and (len(set(path)) == len(path))
    L = P((len(path) - 2) % 4) @ mul((g.A(a, b) for a, b in zip(path, path[1:])))
    assert L == L.dag() and L @ L == P()
    S = P(0 if u < v else 2) @ g.B(u) @ g.B(v) @ L
    assert S == S.dag() and S @ S == P()
    oldAs = [g.A(a, b) for a, b, _ in g.edges]
    oldBs = [g.B(a) for a in range(len(g.v))]
    assert all((not S.anti(A) for A in oldAs))
    assert [i for i, B in enumerate(oldBs) if S.anti(B)] == sorted((u, v))
    e = append_edge(g, u, v)
    for a, A in enumerate(oldAs):
        x, y, _ = g.edges[a]
        assert controlled_conj(A, e, S) == g.A(x, y)
    for a, B in enumerate(oldBs):
        assert controlled_conj(B, e, S) == g.B(a)
    newcycle = g.A(u, v) @ L
    assert controlled_conj(P(x=1 << e), e, S) == newcycle
    assert controlled_conj(g.A(u, v), e, S) == P(x=1 << e) @ L
    return (e, S)

def dense_checks():
    CZ=np.diag([1,1,1,-1])
    for x in range(4):
        for z in range(4):
            row=P(0,x,z)
            assert np.array_equal(CZ@dense(row,2)@CZ,dense(cz_conj(row,0,1),2))
    g = Graph([(0, 0, 0), (1, 0, 0), (2, 0, 0)], q=1, refs=False)
    e, S = edge_add(g, 0, 2, [0, 1, 2])
    assert e == 2
    Id = np.eye(1 << e)
    Sm = dense(S, e)
    zero = np.zeros_like(Id)
    U = np.block([[Id, zero], [zero, Sm]])
    assert np.array_equal(U.conj().T @ U, np.eye(1 << e + 1))
    for x in range(1 << e + 1):
        for z in range(1 << e + 1):
            row = P(0, x, z)
            assert np.array_equal(U @ dense(row, e + 1) @ U, dense(controlled_conj(row, e, S), e + 1))
    factors = []
    Y_count = (S.x & S.z).bit_count()
    sign = (S.p - Y_count) % 4
    assert sign in (0, 2)
    if sign:
        factors.append(dense(P(z=1 << e), e + 1))
    for k in range(e):
        xb = S.x >> k & 1
        zb = S.z >> k & 1
        if not xb and (not zb):
            continue
        Q = dense(P(int(xb and zb), xb << k, zb << k), e)
        factors.append(np.block([[Id, zero], [zero, Q]]))
    V = np.eye(1 << e + 1, dtype=complex)
    for f in factors:
        V = f @ V
    assert np.array_equal(V, U)
    return {'old_edge_qubits': 2, 'new_edge_qubits': 3, 'all_Pauli_conjugations': 64, 'controlled_Pauli_weight': S.weight()}

def build_map(cells):
    old = Graph(cells)
    g = copy.deepcopy(old)
    target = Graph(sorted(cells), refbonds=True)
    old_edges = len(g.edges)
    word = []
    maxS = 0
    bycolor = {}
    streams = sorted(g.streams, key=lambda st: ((st[1] // 2,) + tuple((x % 3 for x in st[0])), st[0]))
    for c, a, d, b in streams:
        color = (a // 2,) + tuple((x % 3 for x in c))
        u, v = (g.vid[c, 6], g.vid[d, 6])
        path = [u, g.vid[c, a], g.vid[d, b], v]
        prev = sum((g.edges[e][2] == 'refbond' for w in (u, v) for e in g.inc[w]))
        e, S = edge_add(g, u, v, path)
        assert S.weight() == 13 - a - b + prev, (S.weight(), a, b, prev)
        assert S.weight() <= 22
        maxS = max(maxS, S.weight())
        word.append((e, S))
        bycolor.setdefault(color, []).append(S.support() | 1 << e)
    for color, supports in bycolor.items():
        seen = 0
        for support in supports:
            assert not support & seen, (color, 'parallel overlap')
            seen |= support
    vertex_map = [target.vid[v] for v in g.v]
    mapping = [target.eid[frozenset((vertex_map[u], vertex_map[v]))] for u, v, _ in g.edges]
    orientation_mask = sum((1 << mapping[e] for e, (u, v, _) in enumerate(g.edges) if (u < v) != (vertex_map[u] < vertex_map[v])))
    gauges = []
    maxinv = 0
    for vertex in range(len(g.v)):
        sequence = [mapping[e] for e in g.inc[vertex]]
        inv = [(sequence[i], sequence[j]) for i in range(len(sequence)) for j in range(i + 1, len(sequence)) if sequence[i] > sequence[j]]
        if g.v[vertex][1] != 6:
            assert not inv
        assert len(inv) <= 15
        maxinv = max(maxinv, len(inv))
        gauges.extend(inv)

    def gauge(row):
        row = permutation(row, mapping)
        for e, f in gauges:
            row = cz_conj(row, e, f)
        return P((row.p + 2 * (row.x & orientation_mask).bit_count()) % 4, row.x, row.z)

    def image(row):
        return gauge(conjugate_word(row, word))
    for u, v, _ in g.edges:
        assert gauge(g.A(u, v)) == target.A(vertex_map[u], vertex_map[v])
    for u in range(len(g.v)):
        assert gauge(g.B(u)) == target.B(vertex_map[u])
    oldX, oldZ, oldD = old.loaders()
    targetX, targetZ, targetD = target.loaders()
    for i, c in enumerate(old.cells):
        j = target.cells.index(c)
        for a in range(6):
            assert image(oldX[6 * i + a]) == targetX[6 * j + a]
            assert image(oldZ[6 * i + a]) == targetZ[6 * j + a]
        assert image(oldD[i]) == targetD[j]
    targetPiv = reduce_rows(target.cycles() + targetD, len(target.edges))
    inputRows = old.cycles() + oldD + [P(x=1 << e) for e in range(old_edges, len(g.edges))]
    outRows = [image(r) for r in inputRows]
    assert len(reduce_rows(outRows, len(target.edges))) == len(targetPiv)
    for r in outRows:
        assert remainder(r, targetPiv, len(target.edges)) == P()
    for u in range(len(old.v)):
        assert image(old.B(u)) == target.B(vertex_map[u])
    active = 0
    for j, (e, S) in enumerate(word):
        cut = word[:j] + word[j + 1:]
        row = gauge(conjugate_word(P(x=1 << e), cut))
        active += remainder(row, targetPiv, len(target.edges)) != P()
    assert active == len(word)
    return {'cells': len(cells), 'old_qubits': old_edges, 'new_qubits': len(target.edges), 'returned_plus_inputs': len(word), 'logical_qubits': len(oldX), 'maximum_controlled_Pauli_weight': maxS, 'colors_used': len(bycolor), 'incidence_CZ_gates': len(gauges), 'orientation_Z_gates': orientation_mask.bit_count(), 'max_incidence_inversions_at_vertex': maxinv, 'deleted_edge_maps_detected': active}


def check_CAR_commutator_and_joint_syndrome_bounds():
    print(json.dumps({'algebra':algebra_checks(),'grid_and_perturbation':geometry_checks()},sort_keys=True))

def check_actual_code_and_exchange_holonomy():
    print(json.dumps({'graph_codes':graph_checks(),'four_cell_exchange':exchange_checks(),'fixed_two_particle_exchange':exchange_checks(True)},sort_keys=True))

def check_fixed_parity_and_marked_reference_escapes():
    print(json.dumps(bksf_dense_checks(),sort_keys=True))

def check_signed_local_Clifford_graph_isometries():
    rows=[build_map([(0,0,0),(1,0,0),(1,1,0),(0,1,0)])]
    rows.extend(build_map(list(product(range(L),repeat=3))) for L in (2,3,4))
    print(json.dumps({'dense_all_Paulis':dense_checks(),'graph_maps':rows},sort_keys=True))

def main():
    checks=[check_CAR_commutator_and_joint_syndrome_bounds,check_actual_code_and_exchange_holonomy,check_fixed_parity_and_marked_reference_escapes,check_signed_local_Clifford_graph_isometries]
    failed=0
    for check in checks:
        try:
            check()
            print('PASS: '+check.__name__,flush=True)
        except Exception:
            failed+=1
            traceback.print_exc()
    print('per_element: exact CAR, Pauli, controlled-Clifford and norm identities test the supplied operator conventions')
    print('per_site: all local reference columns and disjoint mode-five loaders expose the specified encoding hypothesis')
    print('per_mode: every logical X/Z and stream word is compared through signed loop/D stabilizer groups on held graphs')
    print('per_block: closed six-port exchange paths and matched one-particle or stationary-spectator histories test actual statistics')
    print('lattice_wide: grid and edge-addition proofs carry the stated family bounds; finite checks establish no native phase or axiom wall')
    print('TOTAL: PASS='+str(len(checks)-failed)+' FAIL='+str(failed))
    return int(failed>0)
if __name__=='__main__':raise SystemExit(main())
