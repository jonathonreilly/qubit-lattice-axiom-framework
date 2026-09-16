"""Finite challenges for the proposed hybrid generator, not a scaling proof.

The physical source is evaluated by clock-link enumeration and independent
plaquette image sums, followed by the exact Gaussian smoothing formula.
No potential-extension evaluator is used to establish the shift identities.
"""
import itertools
import json
import math
from pathlib import Path

import numpy as np
from scipy.special import logsumexp


def cube():
    vertices = list(itertools.product(range(2), repeat=3))
    edges = [(x, i) for x in vertices for i in range(3) if x[i] == 0]
    faces = [(x, (i, j)) for x in vertices
             for i in range(3) for j in range(i + 1, 3)
             if x[i] == x[j] == 0]
    ei = {e: n for n, e in enumerate(edges)}
    D = np.zeros((6, 12), dtype=int)
    for p, (x, (i, j)) in enumerate(faces):
        xi, xj = list(x), list(x)
        xi[i] += 1
        xj[j] += 1
        for e, sign in [((x, i), 1), ((tuple(xi), j), 1),
                        ((tuple(xj), i), -1), ((x, j), -1)]:
            D[p, ei[e]] += sign
    # A spanning tree is chosen directly in the vertex graph.
    reached = {vertices[0]}
    tree = set()
    while len(reached) < len(vertices):
        for n, (x, i) in enumerate(edges):
            y = list(x)
            y[i] += 1
            y = tuple(y)
            if (x in reached) != (y in reached):
                reached.update([x, y])
                tree.add(n)
                break
    chord = [n for n in range(12) if n not in tree]
    D0 = D[:, chord]
    assert np.linalg.matrix_rank(D0) == 5
    return D.astype(float), D0.astype(float)


class PhysicalSource:
    def __init__(self, N, beta, tau, cutoff=8):
        self.N, self.beta, self.tau = N, beta, tau
        self.D, D0 = cube()
        self.A = np.eye(6) + tau * self.D @ self.D.T
        self.K = np.linalg.inv(self.A)
        clock = np.array(list(itertools.product(range(N), repeat=5)))
        angles = (2 * np.pi / N) * clock @ D0.T
        angles = (angles + np.pi) % (2 * np.pi) - np.pi
        images = np.arange(-cutoff, cutoff + 1)
        self.X = math.sqrt(beta) * (angles[:, :, None] - 2 * np.pi * images)
        self.logw = -self.X**2 / 2
        self.logden = logsumexp(np.sum(logsumexp(self.logw, axis=2), axis=1))

    def mgf(self, t):
        t = np.asarray(t, dtype=complex)
        source = self.K @ t
        exponent = self.logw + source[None, :, None] * self.X
        # Stable complex image sums, then stable complex clock sums.
        shift = np.max(exponent.real, axis=2)
        one = np.exp(exponent - shift[:, :, None]).sum(axis=2)
        row = shift.sum(axis=1) + np.log(one).sum(axis=1)
        offset = max(row.real)
        value = np.exp(offset - self.logden) * np.exp(row - offset).sum()
        gaussian = np.exp(self.tau * np.dot(self.D.T @ source,
                                          self.D.T @ source) / 2)
        return value * gaussian


def main():
    rows = []
    rng = np.random.default_rng(731905)
    for N, beta in [(2, .25), (3, .5), (4, .8)]:
        law = PhysicalSource(N, beta, 1 / 64)
        wider = PhysicalSource(N, beta, 1 / 64, cutoff=10)
        h = 2 * np.pi * math.sqrt(beta)
        t = rng.normal(size=6) * .19
        assert abs(law.mgf(np.zeros(6)) - 1) < 2e-13
        source_cutoff_error = abs(law.mgf(1j * t) - wider.mgf(1j * t))
        assert source_cutoff_error < 2e-13
        balance_errors, rates, bounds, jump_terms = [], [], [], []
        for p in range(6):
            v = h * np.eye(6)[p]
            Av, q = law.A @ v, float(v @ law.A @ v)
            rate_plus = math.exp(-q / 4) * law.mgf(-Av / 2)
            rate_minus = math.exp(-q / 4) * law.mgf(Av / 2)
            bound = math.exp(-q / 8)
            assert abs(rate_plus.imag) < 1e-13
            assert abs(rate_minus.imag) < 1e-13
            assert 0 < rate_plus.real <= bound + 2e-13
            assert abs(rate_plus - rate_minus) < 2e-13
            assert abs(q - h*h*(1+4*law.tau)) < 2e-13
            # Translation invariance of the actual carrier plus periodic potential.
            lhs = law.mgf(1j*t - Av)
            rhs = np.exp(q/2 - 1j*np.dot(t, v)) * law.mgf(1j*t)
            error = abs(lhs-rhs) / max(1, abs(rhs))
            assert error < 4e-12
            balance_errors.append(float(error))
            u = np.dot(t, v)
            jump = math.exp(-q/4) * (
                np.expm1(1j*u)*law.mgf(1j*t-Av/2)
                + np.expm1(-1j*u)*law.mgf(1j*t+Av/2))
            assert abs(jump) < 3e-13
            jump_terms.append(float(abs(jump)))
            rates.append(float(rate_plus.real))
            bounds.append(bound)
        # Challenge the macroscopic Taylor bound for actual rate expectations.
        taylor_rows = []
        for scale in [1, .5, .25, .125]:
            u = h * scale * t
            rp = np.exp(1j*u)-1-1j*u+u*u/2
            rm = np.exp(-1j*u)-1+1j*u+u*u/2
            actual_bound = float(np.dot(np.abs(rp)+np.abs(rm), rates))
            theorem_bound = h**3/3 * bounds[0] * float(np.sum(abs(scale*t)**3))
            assert actual_bound <= theorem_bound + 2e-13
            taylor_rows.append(dict(scale=scale, integrated_absolute_bound=actual_bound,
                                    cubic_bound=theorem_bound))
        rows.append(dict(N=N, beta=beta, tau=law.tau,
                         clock_configurations=N**5,
                         cutoff_comparison=source_cutoff_error,
                         max_quasiperiod_error=max(balance_errors),
                         max_stationary_jump_source_error=max(jump_terms),
                         rates=rates, rate_bounds=bounds, taylor=taylor_rows))
    result = dict(status='finite_checks_passed', families=rows,
                  scope='Three finite free three-cubes; no infinite-volume or '
                        'mixing claim, interval certificate, or independent review.')
    out = Path(__file__).with_suffix('.json')
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
