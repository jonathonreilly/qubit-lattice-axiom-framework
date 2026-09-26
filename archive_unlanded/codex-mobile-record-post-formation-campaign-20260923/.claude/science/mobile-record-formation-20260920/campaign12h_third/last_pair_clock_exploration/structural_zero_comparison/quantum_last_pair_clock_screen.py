#!/usr/bin/env python3
"""Translation-reduced two-vacancy Poisson equation; exploratory finite screen.

H is periodic hard-core hopping with amplitude kappa, loss beta on adjacent
vacancies, and occupation dephasing sqrt(d) n_x at every site. No fit is a
large-volume theorem. Exact and direct finite controls accompany the reduction.
"""
from pathlib import Path
from datetime import datetime, timezone
from itertools import combinations
import argparse
import hashlib
import json
import time
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sla
import sympy as s

HERE = Path(__file__).resolve().parent


class Model:
    def __init__(self, K):
        assert K >= 4 and K % 2 == 0
        self.K = K
        self.pairs = list(combinations(range(K), 2))
        self.index = {a: i for i, a in enumerate(self.pairs)}
        self.reps = sorted({self.canonical((0, r), b) for r in range(1, K//2+1) for b in self.pairs})
        self.ix = {row: i for i, row in enumerate(self.reps)}
        self.hops = {a: self.neighbors(a) for a in self.pairs}
        self.hazard = {a: int((a[1]-a[0]) in (1, K-1)) for a in self.pairs}
        n = len(self.reps)
        rr = []; cc = []; vv = []
        self.dephasing = np.zeros(n)
        self.loss = np.zeros(n)
        self.rhs = np.zeros(n, dtype=complex)
        for row, (r, u, v) in enumerate(self.reps):
            a = (0, r); b = (u, v)
            self.dephasing[row] = 2-len(set(a) & set(b))
            self.loss[row] = (self.hazard[a]+self.hazard[b])/2
            self.rhs[row] = float(a == b)
            for x in self.hops[a]:
                rr.append(row); cc.append(self.ix[self.canonical(x, b)]); vv.append(-1j)
            for x in self.hops[b]:
                rr.append(row); cc.append(self.ix[self.canonical(a, x)]); vv.append(1j)
        self.commutator = sp.coo_matrix((vv, (rr, cc)), shape=(n, n), dtype=complex).tocsc()
        self.commutator.sum_duplicates()

    def canonical(self, a, b):
        rows = []
        for origin in a:
            aa = sorted((x-origin) % self.K for x in a)
            bb = sorted((x-origin) % self.K for x in b)
            rows.append((aa[1], bb[0], bb[1]))
        return min(rows)

    def neighbors(self, a):
        rows = []
        for i in (0, 1):
            for step in (-1, 1):
                x = (a[i]+step) % self.K
                if x != a[1-i]:
                    rows.append(tuple(sorted((x, a[1-i]))))
        assert len(rows) == len(set(rows))
        return rows

    def reconstruct(self, vector):
        return np.array([[vector[self.ix[self.canonical(a, b)]] for b in self.pairs] for a in self.pairs])

    def solve(self, d, beta=1., kappa=1., direct=False):
        A = kappa*self.commutator+sp.diags(d*self.dephasing+beta*self.loss, format='csc')
        started = time.monotonic()
        x = sla.spsolve(A, self.rhs)
        residual = float(np.linalg.norm(A@x-self.rhs, ord=np.inf))
        assert np.isfinite(x).all() and residual < 1e-7
        diagonal = np.array([x[self.ix[self.canonical(a, a)]] for a in self.pairs])
        assert max(abs(diagonal.imag)) < 1e-7 and min(diagonal.real) > 0
        out = {'K': self.K, 'd': d, 'beta': beta, 'kappa': kappa,
               'Hilbert_dimension': len(self.pairs), 'Poisson_unknowns': len(self.reps),
               'uniform_incoherent_mean': float(np.mean(diagonal.real)),
               'adjacent_localized_mean': float(x[self.ix[self.canonical((0, 1), (0, 1))]].real),
               'opposite_localized_mean': float(x[self.ix[self.canonical((0, self.K//2), (0, self.K//2))]].real),
               'linear_residual_inf': residual, 'solve_seconds': time.monotonic()-started}
        if direct:
            F = self.reconstruct(x)
            D = len(self.pairs)
            H = np.zeros((D, D), dtype=complex)
            for a in self.pairs:
                for b in self.hops[a]: H[self.index[b], self.index[a]] = kappa
            G = np.diag([beta*self.hazard[a] for a in self.pairs])
            dual = 1j*(H@F-F@H)-(G@F+F@G)/2
            for site in range(self.K):
                n = np.diag([int(site in a) for a in self.pairs])
                dual += d*(n@F@n-(n@F+F@n)/2)
            assert np.linalg.norm(dual+np.eye(D), ord=np.inf) < 2e-7
            assert np.max(abs(F-F.conjugate().T)) < 1e-7
            eig = np.linalg.eigvalsh(F)
            assert eig[0] > 0
            out.update(direct_full_Poisson_residual_inf=float(np.linalg.norm(dual+np.eye(D), ord=np.inf)),
                       mean_operator_minimum_eigenvalue=float(eig[0]),
                       worst_coherent_initial_mean=float(eig[-1]))
        return out


def exact_four_cycle():
    m = Model(4)
    d, beta, kappa = s.symbols('d beta kappa', positive=True)
    A = s.zeros(len(m.reps))
    coo = m.commutator.tocoo()
    for i, j, v in zip(coo.row, coo.col, coo.data):
        assert v.real == 0 and v.imag == int(v.imag)
        A[int(i), int(j)] += s.I*int(v.imag)*kappa
    for i in range(len(m.reps)):
        A[i, i] += d*int(m.dephasing[i])+beta*s.Rational(str(m.loss[i]))
    rhs = s.Matrix([int(x.real) for x in m.rhs])
    x = A.inv()*rhs
    assert all(s.factor(z) == 0 for z in A*x-rhs)
    mean = s.factor(sum(x[m.ix[m.canonical(a, a)]] for a in m.pairs)/len(m.pairs))
    opposite = s.factor(x[m.ix[m.canonical((0, 2), (0, 2))]])
    adjacent = s.factor(x[m.ix[m.canonical((0, 1), (0, 1))]])
    # Previously derived C4 dark vector is the alternating opposite-pair word.
    # Reconstruct the exact F expectation without assuming the new mean formula.
    F = s.Matrix([[x[m.ix[m.canonical(a, b)]] for b in m.pairs] for a in m.pairs])
    dark = s.zeros(6, 1); dark[m.index[(0, 2)]] = 1; dark[m.index[(1, 3)]] = -1
    dark_mean = s.factor((dark.T*F*dark)[0]/2)
    previous = 1/d+3/(2*beta)+1/(beta+d)+1/(2*(beta+2*d))+(2*d+beta)/(16*kappa**2)
    assert s.factor(dark_mean-previous) == 0
    return {'K': 4, 'unknowns': len(m.reps), 'uniform_incoherent_mean': str(mean),
            'opposite_localized_mean': str(opposite), 'adjacent_localized_mean': str(adjacent),
            'dark_initial_mean': str(dark_mean),
            'independent_prior_C4_dark_formula_agrees': True,
            'weak_dephasing_uniform_coefficient': str(s.limit(d*mean, d, 0)),
            'strong_dephasing_uniform_coefficient': str(s.limit(mean/d, d, s.oo))}


def dark_space_checks():
    rows = []
    for K in (4, 6, 8, 10, 12):
        m = Model(K); D = len(m.pairs)
        H = s.zeros(D); shift = s.zeros(D)
        for a in m.pairs:
            for b in m.hops[a]: H[m.index[b], m.index[a]] = 1
            b = tuple(sorted((x+1) % K for x in a)); shift[m.index[b], m.index[a]] = 1
        Ppi = s.zeros(D); power = s.eye(D)
        for j in range(K):
            Ppi += (-1)**j*power/K; power = shift*power
        G = s.diag(*[m.hazard[a] for a in m.pairs])
        PD = Ppi*(s.eye(D)-G)
        assert Ppi*Ppi == Ppi and PD*PD == PD and PD.T == PD
        assert H*Ppi == s.zeros(D) and G*PD == s.zeros(D)
        dimension = K//2-2+int(K % 4 == 0)
        assert s.trace(PD) == dimension
        for site in range(K):
            n = s.diag(*[int(site in a) for a in m.pairs])
            assert PD*n*PD == s.Rational(2, K)*PD
        rows.append({'K': K, 'dark_dimension': dimension,
                     'H_annihilates_entire_momentum_pi_space': True,
                     'compressed_each_hole_number': f'2/{K} times P_dark',
                     'predicted_fixed_K_weak_d_mean_coefficient_for_uniform_input': str(s.Rational(dimension, (K-1)*(K-2))),
                     'predicted_fixed_K_strong_d_mean_coefficient_for_uniform_input': str(s.Rational((K-2)*(K-3), 48)),
                     'boundary': 'Exact finite dark projection checks; asymptotic Poisson limits still require the accompanying analytic argument.'})
    return rows


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--maximum-K', type=int, default=24)
    args = parser.parse_args()
    started = time.monotonic()
    output = {'created_utc': datetime.now(timezone.utc).isoformat(),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'exact_C4': exact_four_cycle(), 'dark_projection_controls': dark_space_checks(), 'screen': []}
    for K in (4, 6, 8, 12, 16, 24, 32):
        if K > args.maximum_K: continue
        model = Model(K)
        for d in (0.001, 0.01, 0.1, 0.3, 1., 3., 10., 100.):
            row = model.solve(d, direct=(K <= 8))
            output['screen'].append(row)
            print(json.dumps(row), flush=True)
    output['runtime_seconds'] = time.monotonic()-started
    output['scope'] = 'Finite exploratory scan at beta=kappa=1. No inferred optimum, thermodynamic scaling, or independently checked new theorem.'
    (HERE/'QUANTUM_LAST_PAIR_CLOCK_SCREEN_RESULTS.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({'finished': True, 'exact_C4': output['exact_C4'], 'runtime_seconds': output['runtime_seconds']}), flush=True)
