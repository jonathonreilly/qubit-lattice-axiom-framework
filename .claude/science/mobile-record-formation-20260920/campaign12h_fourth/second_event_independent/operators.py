"""Independently assembled legal-hop and effective-birth operators.

Unit rotor amplitudes; all field shifts retained as integer link vectors.
No author module is imported.  Global T has the stipulated minus sign.
"""
from collections import defaultdict
from itertools import combinations
import numpy as np


def charge_basis(vertices, A, population, total_charge, W):
    minus = (population - total_charge) // 2
    assert population - total_charge == 2 * minus and minus >= 0
    states = []
    for occ in combinations(range(vertices), population):
        if sum(x not in occ for x in A) != W:
            continue
        for neg in combinations(occ, minus):
            q = tuple(-1 if x in neg else 1 if x in occ else 0 for x in range(vertices))
            states.append(q)
    return states


def hops(q, edges):
    for i, (x, y) in enumerate(edges):
        for source, dest, direction in ((x, y, 1), (y, x, -1)):
            if q[source] == 0 or q[dest] != 0:
                continue
            charge = q[source]
            out = list(q)
            out[source], out[dest] = 0, charge
            shift = [0] * len(edges)
            shift[i] = -direction * charge
            yield tuple(out), tuple(shift), -1


def add_shift(a, b):
    return tuple(x + y for x, y in zip(a, b))


def birth_paths(q, edges, channel, charge=None):
    """B=-P j Pi_1 T P, on a supplied P word; coherent if charge=None."""
    x, y = edges[channel]
    for mid, shift, t_amp in hops(q, edges):
        if mid[x] or mid[y]:
            continue
        for c in (-1, 1) if charge is None else (charge,):
            out = list(mid)
            out[x], out[y] = c, -c
            delta = list(shift)
            delta[channel] += c
            yield tuple(out), tuple(delta), -t_amp


def hopping_matrix(source, target, edges, phases):
    ix = {q: i for i, q in enumerate(target)}
    mat = np.zeros((len(target), len(source)), complex)
    for j, q in enumerate(source):
        for out, shift, amplitude in hops(q, edges):
            if out in ix:
                mat[ix[out], j] += amplitude * np.exp(1j * np.dot(phases, shift))
    return mat


def birth_matrix(source, target, edges, phases, channel, charge=None):
    ix = {q: i for i, q in enumerate(target)}
    mat = np.zeros((len(target), len(source)), complex)
    for j, q in enumerate(source):
        for out, shift, amplitude in birth_paths(q, edges, channel, charge):
            assert out in ix
            mat[ix[out], j] += amplitude * np.exp(1j * np.dot(phases, shift))
    return mat


def ring_operators(L, theta):
    n = 2 * L
    edges = [(x, (x + 1) % n) for x in range(n)]
    A = set(range(0, n, 2))
    basis = [charge_basis(n, A, L + 2, L, w) for w in (0, 1, 2)]
    full = charge_basis(n, A, L + 4, L, 0) if L >= 4 else []
    phases = np.zeros(n)
    phases[-1] = theta
    hop = hopping_matrix(basis[0], basis[1], edges, phases)
    Z = hopping_matrix(basis[1], basis[2], edges, phases) @ hop
    M = hop.conj().T @ hop
    H2 = -M
    H4 = M @ M - .5 * Z.conj().T @ Z
    resolved = [birth_matrix(basis[0], full, edges, phases, e, c)
                for e in range(n) for c in (-1, 1)] if full else []
    coherent = [resolved[2 * e] + resolved[2 * e + 1] for e in range(n)] if full else []
    zero = np.zeros_like(H2)
    Gamma = sum((b.conj().T @ b for b in resolved), start=zero)
    Gamma_coh = sum((b.conj().T @ b for b in coherent), start=zero)
    assert np.max(abs(Gamma - Gamma_coh)) < 1e-12
    return basis[0], H2, H4, Gamma, resolved, coherent


def form_word(L, c):
    q = [1 if x % 2 == 0 else 0 for x in range(2 * L)]
    q[-1], q[0], q[1] = 1, c, -c
    return tuple(q)


def first_outputs(L, basis):
    a = np.zeros(len(basis))
    a[basis.index(form_word(L, 1))] = 1
    b = a.copy()
    b[basis.index(form_word(L, -1))] = 1
    b /= np.sqrt(2)
    return a, b


def group_eigenvalues(values, tolerance=1e-8):
    groups = []
    for j, value in enumerate(values):
        if not groups or abs(value - values[groups[-1][0]]) > tolerance:
            groups.append([j])
        else:
            groups[-1].append(j)
    return groups
