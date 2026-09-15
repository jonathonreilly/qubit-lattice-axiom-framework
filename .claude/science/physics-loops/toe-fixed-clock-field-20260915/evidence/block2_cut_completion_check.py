"""Finite cut-flip and bridge-completion challenges.

The analytic cut derivative is checked against sign subtraction and numerical
differentiation; no quotient by a mixed pair factor is used. Separate graph
checks exercise bridge removal and preservation of the source graph.
"""
import itertools
import json
from pathlib import Path

import mpmath as mp
import numpy as np

from block2_forest_interpolation_check import cochains, tree_paths


def bridge_cuts(edges, vertices, root):
    result = []
    for skip, (left, right) in enumerate(edges):
        reached, stack = {root}, [root]
        while stack:
            node = stack.pop()
            for e, (i, j) in enumerate(edges):
                if e == skip:
                    continue
                other = j if i == node else i if j == node else None
                if other is not None and other not in reached:
                    reached.add(other)
                    stack.append(other)
        if len(reached) != vertices:
            assert (left in reached) != (right in reached)
            result.append((skip, set(range(vertices))-reached))
    return result


def combinatorics():
    rng = np.random.default_rng(516935)
    total, completions, max_steps, max_edges, max_sources = 0, 0, 0, 0, 0
    for n in range(2, 9):
        for _ in range(120):
            spatial = []
            for i in range(1, n):
                parent = int(rng.integers(i))
                spatial += [(i, parent)]*int(rng.integers(1, 3))
            source_vertices = rng.integers(n, size=4)
            edges = spatial+[(int(i), n) for i in source_vertices]
            steps, source_count = 0, 4
            while cuts := bridge_cuts(edges, n+1, n):
                skip, A = cuts[0]
                before = {e for e, _ in cuts}
                crossing = [(i, j) for i in sorted(A) for j in range(n+1) if j not in A]
                # Every possible derivative edge must remove this bridge and
                # cannot create a new one. The source endpoint is vertex n.
                for e in crossing:
                    after = {k for k, _ in bridge_cuts(edges+[e], n+1, n)}
                    assert skip not in after and after <= before
                    completions += 1
                e = crossing[int(rng.integers(len(crossing)))]
                edges.append(e)
                source_count += e[1] == n
                steps += 1
                assert steps <= n
            assert len(edges) <= 3*n+2 and 4 <= source_count <= n+4
            max_steps, max_edges = max(max_steps, steps), max(max_edges, len(edges))
            max_sources = max(max_sources, source_count)
            total += 1
    return dict(initial_graphs=total, individual_possible_edge_additions=completions,
                maximum_observed_steps=max_steps, maximum_observed_edges=max_edges,
                maximum_observed_source_legs=int(max_sources))


def numerical_cut_identities():
    mp.mp.dps = 45
    incidence, P, Q = cochains()
    D, B = incidence[1:3]
    c0, xe, xm = 1/32, 18., 2*np.pi*np.pi
    labels = [0, 6, 0, 18]
    kernels = [P-c0*D@D.T, Q-c0*B.T@B]
    J = np.zeros((4, 4))
    for i in range(4):
        for j in range(4):
            if (i < 2) == (j < 2):
                J[i, j] = (xe if i < 2 else xm)*kernels[0 if i < 2 else 1][labels[i], labels[j]]
    assert np.linalg.eigvalsh(J)[0] > 0
    pairs = list(itertools.combinations(range(4), 2))
    tree = [(0, 1), (0, 2), (0, 3)]
    paths = tree_paths(tree)
    t = np.array([.6, .8, .35])
    S = np.eye(4)
    for (i, j), path in zip(pairs, paths):
        S[i, j] = S[j, i] = min(t[path])
    theta = {(i, j):mp.mpf(float(6*np.pi*P[labels[j], labels[i]]))
             for i, j in pairs if (i < 2) != (j < 2)}
    # A previously applied cut with negative parameter must preserve the
    # Gram stability and the endpoints of the next cut operation.
    prior_A, prior_t = {0, 2}, -.4
    r = np.ones((4, 4))
    ri = np.ones(4)
    for i in range(4):
        ri[i] = prior_t if i in prior_A else 1.
        for j in range(4):
            r[i, j] = prior_t if (i in prior_A) != (j in prior_A) else 1.
    zeta = mp.mpc('.6', '.15')
    L = [mp.mpf('.11'), mp.mpf('-.07'), mp.mpc(0,'.09'), mp.mpc(0,'-.04')]
    signs = list(itertools.product([-1, 1], repeat=4))
    # All three tree edges are odd; four initial source legs at vertex 0.
    prefactor = lambda sigma: sigma[0]*sigma[1]*sigma[2]*sigma[3]
    A = {1}  # Leaf bridge in the selected augmented graph.
    mixed_remaining = [(1, 2), (1, 3)]  # Two mixed tree factors were removed.
    self_diagonal = mp.mpf(float(np.trace(J)/2))

    def evaluate(sigma, cut_value, derivative=False, zero_factor=False):
        same_exponent, same_derivative = mp.mpf(0), mp.mpf(0)
        for i, j in [(0, 1), (2, 3)]:
            crossing = (i in A) != (j in A)
            base = mp.mpf(float(S[i, j]*r[i, j]*J[i, j]))*sigma[i]*sigma[j]
            same_exponent -= base*(cut_value if crossing else 1)
            if crossing:
                same_derivative -= base
        source_exponent, source_derivative = mp.mpc(0), mp.mpc(0)
        for i in range(4):
            term = zeta*sigma[i]*L[i]*mp.mpf(float(ri[i]))
            source_exponent += term*(cut_value if i in A else 1)
            if i in A:
                source_derivative += term
        factors, derivatives = [], []
        for i, j in mixed_remaining:
            s = mp.mpf('.5') if zero_factor and (i, j) == (1, 2) else mp.mpf(float(S[i, j]))
            angle = mp.pi if zero_factor and (i, j) == (1, 2) else theta[i, j]
            base = 1j*s*mp.sin(angle)*sigma[i]*sigma[j]*mp.mpf(float(r[i, j]))
            crossing = (i in A) != (j in A)
            factors.append(1+s*(mp.cos(angle)-1)+base*(cut_value if crossing else 1))
            derivatives.append(base if crossing else 0)
        exponential = mp.exp(-self_diagonal+same_exponent+source_exponent)
        product = mp.fprod(factors)
        if not derivative:
            return exponential*product
        # Product rule, including at zeros; no logarithmic derivative.
        mixed_derivative = sum(derivatives[k]*mp.fprod(f for l, f in enumerate(factors) if l != k)
                               for k in range(len(factors)))
        return exponential*((same_derivative+source_derivative)*product+mixed_derivative)

    sign_change_errors, derivative_errors = [], []
    maximum_stability_ratio = 0.
    for sigma in signs:
        flipped = tuple(-s if i in A else s for i, s in enumerate(sigma))
        assert prefactor(flipped) == -prefactor(sigma)
        sign_change_errors.append(abs(evaluate(sigma,-1)-evaluate(flipped,1)))
        for cut_value in [mp.mpf('-.9'), mp.mpf(0), mp.mpf('.37'), mp.mpf('1')]:
            for zero_factor in [False, True]:
                direct_derivative = mp.diff(lambda v:evaluate(sigma,v,zero_factor=zero_factor),cut_value)
                derivative_errors.append(abs(direct_derivative-evaluate(sigma,cut_value,True,zero_factor)))
            Rnew = np.ones((4, 4))
            for i, j in pairs:
                if (i in A) != (j in A):
                    Rnew[i, j] = Rnew[j, i] = float(cut_value)
            assert np.linalg.eigvalsh(S*r*Rnew*J)[0] > -1e-12
            source_bound = sum(abs(zeta*l) for l in L)
            ratio = abs(evaluate(sigma,cut_value))*mp.exp(-source_bound)
            maximum_stability_ratio = max(maximum_stability_ratio,float(ratio))
            assert ratio <= 1+mp.mpf('1e-12')
    left = sum(prefactor(s)*evaluate(s,1) for s in signs)/16
    endpoint = sum(prefactor(s)*(evaluate(s,1)-evaluate(s,-1))/2 for s in signs)/16
    right = mp.quad(lambda v:sum(prefactor(s)*evaluate(s,v,True) for s in signs)/32,[-1,0,1])
    assert max(sign_change_errors) < mp.mpf('1e-35')
    assert max(derivative_errors) < mp.mpf('1e-35')
    assert abs(left-endpoint) < mp.mpf('1e-35') and abs(left-right) < mp.mpf('1e-35')
    return dict(sign_flip_endpoint_error=str(max(sign_change_errors)),
                analytic_derivative_max_error=str(max(derivative_errors)),
                average_identity_endpoint_error=str(abs(left-endpoint)),
                integrated_cut_identity_error=str(abs(left-right)),
                left_real=str(mp.re(left)), left_imag=str(mp.im(left)),
                maximum_tested_stability_ratio=maximum_stability_ratio,
                zero_mixed_factor_derivative_included=True,
                prior_negative_cut_parameter=prior_t,
                scope='45-digit identities at floating cochain entries, not 45-digit certification of those entries.')


def main():
    result = dict(status='finite_cut_completion_checks_passed',
                  combinatorics=combinatorics(), cut_identity=numerical_cut_identities(),
                  scope='Finite author checks; no all-order summation, interval arithmetic, '
                        'infinite-volume physical state or independent review.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
