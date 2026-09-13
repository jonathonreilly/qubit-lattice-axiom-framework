"""Exact canonical interacting nonconvexity certificate, no eigensolver.

Trial vectors were discovered numerically. Verification uses only rational
Hermitian LDL and variational upper bounds with rational square-root brackets.
This certifies the stated three-particle finite sector at lambda=-20 only.
"""
from pathlib import Path
from math import isqrt
import hashlib
import json
import time
import sympy as s

HERE = Path(__file__).resolve().parent
INPUT = HERE / 'BLOCK05_CANONICAL_NONCONVEX_WITNESS.json'


def run():
    start = time.monotonic()
    data = json.loads(INPUT.read_text())
    checks = []

    def check(name, condition):
        assert bool(condition), name
        checks.append(name)

    basis = [word for word in range(64) if word.bit_count() == 3]
    check('fixed_declared_sector', data['basis'] == basis
          and data['sector_particles'] == 3 and data['lambda'] == -20)
    index = {word: n for n, word in enumerate(basis)}
    dim = len(basis)
    onsite = []
    for x in range(3):
        diagonal = []
        for word in basis:
            a, b = (word >> (2*x)) & 1, (word >> (2*x+1)) & 1
            diagonal.append(s.Rational(5, 2)*(a-b)
                            - 20*(a-s.Rational(1, 2))*(b-s.Rational(1, 2)))
        onsite.append(s.diag(*diagonal))

    # Direct occupation-basis CAR signs, independent of the full-space JW
    # matrices in the other finite checker.
    def adag_a(i, j):
        result = s.zeros(dim)
        for col, word in enumerate(basis):
            if not (word >> j) & 1:
                continue
            sign = (-1)**((word & ((1 << j)-1)).bit_count())
            after = word ^ (1 << j)
            if (after >> i) & 1:
                continue
            sign *= (-1)**((after & ((1 << i)-1)).bit_count())
            result[index[after | (1 << i)], col] = sign
        return result

    W = s.Matrix([[-1, s.I], [s.I, 1]]) / 2
    bond = s.zeros(dim)
    for x in range(2):
        for a in range(2):
            for b in range(2):
                t = W[a, b]*adag_a(2*x+a, 2*(x+1)+b)
                bond += t+t.H
    H0 = sum(onsite, s.zeros(dim)) + bond
    check('literal_hermitian_matrix', H0 == H0.H)
    lower = s.Rational(data['lower_ground_shift'])
    matrix = H0-lower*s.eye(dim)
    L = s.eye(dim)
    pivots = []
    for j in range(dim):
        pivot = s.cancel(matrix[j, j]-sum(L[j, k]*s.conjugate(L[j, k])*pivots[k]
                                          for k in range(j)))
        check('strict_positive_rational_pivot_'+str(j), pivot.is_Rational and pivot > 0)
        pivots.append(pivot)
        for i in range(j+1, dim):
            L[i, j] = s.cancel((matrix[i, j]-sum(
                L[i, k]*s.conjugate(L[j, k])*pivots[k] for k in range(j)))/pivot)
    residue = L*s.diag(*pivots)*L.H-matrix
    check('exact_LDL_reconstruction', all(s.cancel(v) == 0 for v in residue))

    trials = []
    for trial in data['trials']:
        sign = trial['sign']
        check('trial_sign_'+str(sign), sign in (-1, 1))
        eps = s.Rational(sign, 1000)
        N = [1+eps, 1-2*eps, 1+eps]
        check('positive_mean_one_lapse_'+str(sign), min(N) > 0 and sum(N) == 3)
        # Scale cancels in a Rayleigh quotient; retain integer Gaussian entries.
        vector = s.Matrix([a+s.I*b for a, b in trial['vector']])
        norm = (vector.H*vector)[0]
        check('nonzero_trial_'+str(sign), norm.is_Rational and norm > 0)
        diagonal = s.cancel((vector.H*sum((N[x]*onsite[x] for x in range(3)),
                                          s.zeros(dim))*vector)[0]/norm)
        coefficient = s.cancel((vector.H*bond*vector)[0]/norm)
        check('real_rational_rayleigh_parts_'+str(sign),
              diagonal.is_Rational and coefficient.is_Rational)
        square = N[0]*N[1]
        scale = 10**20
        root_floor = isqrt(int(s.numer(square))*scale**2//int(s.denom(square)))
        lo, hi = s.Rational(root_floor, scale), s.Rational(root_floor+1, scale)
        check('exact_sqrt_bracket_'+str(sign), 0 <= lo and lo**2 <= square <= hi**2)
        upper = diagonal+coefficient*(hi if coefficient >= 0 else lo)
        trials.append(dict(sign=sign, upper_rational=str(upper),
                           upper_display=float(upper), sqrt_interval=[str(lo), str(hi)]))
    check('both_opposite_trials', sorted(t['sign'] for t in trials) == [-1, 1])
    midpoint_upper = sum(s.Rational(t['upper_rational']) for t in trials)/2
    margin = lower-midpoint_upper
    check('strict_midpoint_convexity_violation', margin > s.Rational(8, 100000))
    out = dict(status='PASS', checks=len(checks), details=checks,
               lower_ground_bound=str(lower), trial_bounds=trials,
               midpoint_violation_margin_rational=str(margin),
               midpoint_violation_margin_display=float(margin),
               positive_LDL_pivots=[str(p) for p in pivots],
               elapsed_seconds=time.monotonic()-start,
               source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               input_sha256=hashlib.sha256(INPUT.read_bytes()).hexdigest(),
               scope='Exact finite three-cell, three-particle-sector nonconvexity at lambda=-20. No grand-canonical or weak-coupling claim.')
    (HERE/'BLOCK05_CANONICAL_CERTIFICATE.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({k: v for k, v in out.items() if k not in ('details', 'positive_LDL_pivots')}, indent=2))


if __name__ == '__main__':
    run()
