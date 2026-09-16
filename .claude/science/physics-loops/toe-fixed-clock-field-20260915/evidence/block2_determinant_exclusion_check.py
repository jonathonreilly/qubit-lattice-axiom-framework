"""Author challenges of Gram determinant exclusion; no independent review.

Exact symbolic derivatives are compared with finite CAR traces and BKAR
quadrature. Shared floating cochains supply a physical finite fixture.
"""
import itertools
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss
from block2_forest_interpolation_check import cochains, partitions


def subsets(items):
    for bits in itertools.product([0, 1], repeat=len(items)):
        yield tuple(i for bit, i in zip(bits, items) if bit)


def creators(n):
    out = []
    for k in range(n):
        c = np.zeros((2**n, 2**n))
        for mask in range(2**n):
            if not mask & (1 << k):
                c[mask | (1 << k), mask] = (-1)**((mask & ((1 << k)-1)).bit_count())
        out.append(c)
    return np.array(out)


def forest_matrix(n, tree, values):
    s = np.eye(n)
    for (i, j), t in zip(tree, values):
        s[i, j] = s[j, i] = t
    for k in range(n):
        for i in range(n):
            for j in range(n):
                s[i, j] = max(s[i, j], min(s[i, k], s[k, j]))
    return s


def determinant_polynomial(footprints):
    n = len(footprints)
    pairs = list(itertools.combinations(range(n), 2))
    variables = sp.symbols('s:'+str(len(pairs)))
    s = sp.eye(n)
    for x, (i, j) in zip(variables, pairs):
        s[i, j] = s[j, i] = x
    result = sp.Integer(1)
    for u in set().union(*footprints):
        members = [i for i, a in enumerate(footprints) if u in a]
        result *= s.extract(members, members).det()
    return pairs, variables, sp.expand(result)


def main():
    rng = np.random.default_rng(513497)
    trace_error = cross_error = commutator_error = 0.
    trace_cases = cross_cases = 0
    for n in [2, 3, 4, 5]:
        basis = creators(n)
        vectors = rng.normal(size=(n, n))
        vectors /= np.linalg.norm(vectors, axis=0)
        # Identity, rank-one, general Gram, and genuine forest degenerations.
        matrices = [np.eye(n), np.ones((n, n)), vectors.T@vectors,
                    forest_matrix(n, [(i, i+1) for i in range(n-1)],
                                  [.7 if i % 2 else 1. for i in range(n-1)])]
        for s in matrices:
            eigen, vec = np.linalg.eigh(s)
            v = np.diag(np.sqrt(np.maximum(eigen, 0)))@vec.T
            c = np.einsum('ki,kab->iab', v, basis)
            words = {}
            for subset in subsets(tuple(range(n))):
                word = np.eye(2**n)
                for i in subset:
                    word = c[i]@word
                words[subset] = word
                actual = np.trace(word.T@word)/2**n
                expected = np.linalg.det(s[np.ix_(subset, subset)])*2.**(-len(subset))
                trace_error = max(trace_error, abs(actual-expected))
                trace_cases += 1
            # Non-principal minors are needed by derivative bounds.
            for left, right in itertools.product(words, repeat=2):
                if len(left) != len(right):
                    continue
                actual = np.trace(words[left].T@words[right])/2**n
                expected = np.linalg.det(s[np.ix_(left, right)])*2.**(-len(left))
                cross_error = max(cross_error, abs(actual-expected))
                cross_cases += 1
            x = rng.normal(size=(2**n, 2**n))
            for a, b in itertools.product(c, repeat=2):
                commutator_error = max(commutator_error,
                    np.max(abs(a.T@b.T@x@b@a-b.T@a.T@x@a@b)))
    assert max(trace_error, cross_error) < 2e-13
    assert commutator_error < 5e-12

    derivative_cases = 0
    derivative_ratio = 0.
    families = [ [{0}, {0}, {0}], [{0}, {1}, {0}],
                 [{0, 1}, {0, 2}, {1, 2}, {0, 1, 2}],
                 [{0, 1}, {1, 2}, {2, 3}, {3, 0}] ]
    for footprints in families:
        pairs, variables, poly = determinant_polynomial(footprints)
        n = len(footprints)
        points = []
        for _ in range(25):
            v = rng.normal(size=(n, n))
            v /= np.linalg.norm(v, axis=0)
            points.append(v.T@v)
            perm = rng.permutation(n)
            tree = list(zip(perm[:-1], perm[1:]))
            points.append(forest_matrix(n, tree, rng.uniform(size=n-1)))
        points += [np.eye(n), np.ones((n, n))]
        args = np.array([[s[i, j] for i, j in pairs] for s in points]).T
        for chosen in subsets(tuple(range(len(pairs)))):
            derivative = sp.diff(poly, *(variables[e] for e in chosen)) if chosen else poly
            value = np.asarray(sp.lambdify(variables, derivative, 'numpy')(*args))
            bound = 2**len(chosen)*math.prod(len(footprints[pairs[e][0]] & footprints[pairs[e][1]]) for e in chosen)
            if bound:
                derivative_ratio = max(derivative_ratio, float(np.max(abs(value))/bound))
                assert np.max(abs(value)) <= bound+2e-12
            else:
                assert derivative == 0
            derivative_cases += len(points)
        # Endpoint equals original full exclusion, checked directly.
        original_hc = int(all(not (a & b) for a, b in itertools.combinations(footprints, 2)))
        assert poly.subs(dict.fromkeys(variables, 0)) == 1
        assert poly.subs(dict.fromkeys(variables, 1)) == original_hc

    # A generic cube point is not a correlation matrix: positivity is scoped.
    cube_control = np.array([[1., 1., 1.], [1., 1., 0.], [1., 0., 1.]])
    cube_determinant = np.linalg.det(cube_control)
    assert cube_determinant < -.99

    incidence, p, _ = cochains()
    c0, d, _, _ = incidence
    triple = [0, 6, 1]
    footprints = []
    for face in triple:
        edges = np.flatnonzero(d[face])
        vertices = np.flatnonzero(np.any(c0[edges] != 0, axis=0))
        footprints.append({('edge', int(i)) for i in edges} |
                          {('vertex', int(i)) for i in vertices})
    pairs, variables, poly = determinant_polynomial(footprints)
    overlap = [len(footprints[i]&footprints[j]) for i, j in pairs]
    assert overlap[0] == overlap[2] == 0 and overlap[1] > 0
    assert sp.expand(poly-(1-variables[1]**2)**overlap[1]) == 0
    derivatives = {}
    for chosen in subsets(tuple(range(3))):
        expr = sp.diff(poly, *(variables[e] for e in chosen)) if chosen else poly
        derivatives[chosen] = sp.lambdify(variables, expr, 'numpy')
    signs = np.array(list(itertools.product([-1., 1.], repeat=3)))
    signpairs = np.array([signs[:, i]*signs[:, j] for i, j in pairs])
    x = 18.
    gram = x*(p-d@d.T/32)[np.ix_(triple, triple)]
    coupling = np.array([gram[i, j] for i, j in pairs])
    self_factor = np.exp(-x*np.sum(d[triple]**2)/64-.5*np.trace(gram))
    h = .011*np.cos(np.arange(len(p))*.71+.2)
    source = -np.sqrt(x)*(p@h)[triple]*(.4+.3j)

    def weight(s, chosen=()):
        gaussian = np.exp(-(s*coupling)@signpairs)*np.exp(signs@source)[None, :]*self_factor
        factor = np.zeros_like(gaussian)
        for h_derivatives in subsets(chosen):
            term = np.broadcast_to(np.asarray(derivatives[h_derivatives](*s.T), dtype=float), (len(s),))[:, None]
            term = np.broadcast_to(term, gaussian.shape).copy()
            for e in chosen:
                if e not in h_derivatives:
                    term *= -coupling[e]*signpairs[e]
            factor += term
        return np.mean(gaussian*factor, axis=1)

    reference = 0j
    for partition in partitions(list(range(3))):
        labels = {i: k for k, block in enumerate(partition) for i in block}
        s = np.array([[float(labels[i] == labels[j]) for i, j in pairs]])
        reference += (-1)**(len(partition)-1)*math.factorial(len(partition)-1)*weight(s)[0]
    quadrature = []
    for order in [12, 20, 28]:
        nodes, weights = leggauss(order)
        nodes, weights = (nodes+1)/2, weights/2
        grid = np.array(list(itertools.product(nodes, repeat=2)))
        qw = np.prod(np.array(list(itertools.product(weights, repeat=2))), axis=1)*grid[:, 0]
        value = 0j
        for tree in itertools.combinations(range(3), 2):
            missing = next(e for e in range(3) if e not in tree)
            for first, second in [tree, tree[::-1]]:
                s = np.zeros((len(grid), 3))
                s[:, first] = grid[:, 0]
                s[:, second] = grid[:, 0]*grid[:, 1]
                s[:, missing] = s[:, second]
                value += qw@weight(s, tree)
        quadrature.append(dict(order=order, absolute_error=float(abs(value-reference))))
    assert quadrature[-1]['absolute_error'] < 1e-18
    c_single = creators(1)[0]
    missing_boost = float(np.trace(c_single.T@c_single)/2)
    bad_trace_identity = float(np.trace(np.eye(8)))
    assert abs(missing_boost-1) > .49 and bad_trace_identity > 7
    result = dict(status='finite_author_checks_passed', independent_review=False,
                  gram_trace_cases=trace_cases, gram_trace_error=float(trace_error),
                  cross_minor_cases=cross_cases, cross_minor_trace_error=float(cross_error),
                  commuting_map_error=float(commutator_error),
                  derivative_point_checks=derivative_cases, maximum_derivative_bound_ratio=derivative_ratio,
                  non_psd_cube_determinant=float(cube_determinant),
                  physical_cochain_triple=triple, shared_resource_counts=overlap,
                  physical_connected_reference=dict(real=float(reference.real), imag=float(reference.imag)),
                  bkar_quadrature=quadrature,
                  normalization_control=dict(single_resource_without_boost=missing_boost,
                                             unnormalized_trace_identity_at_n3=bad_trace_identity),
                  limitations=['finite identities only', 'shared float cochain fixture',
                               'no derivative operator source theorem', 'no physical all-order convergence'])
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
