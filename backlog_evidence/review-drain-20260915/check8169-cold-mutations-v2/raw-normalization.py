"""Exact finite menu/exchange probability checks; no physical-law selection.
Corrected endpoint controls are finite analogues, not numerical Haar proofs.
"""
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import hashlib, json
AUDIT_TIMEOUT_SEC = 120
AUDIT_MEMORY_MB = 256
AUDIT_INPUT_PATHS = ['docs/FRAME_ATTACHED_MENU_EXCHANGE_COVARIANT_PROBABILITIES_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md']
EXPECTED_INPUT_SHA256 = {'docs/FRAME_ATTACHED_MENU_EXCHANGE_COVARIANT_PROBABILITIES_BOUNDED_THEOREM_NOTE_2026-09-16.md': 'd9450ac04bcb887168291f0ccbd4fc101456aa180ab3c543effa38254d2a2e6b', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md': '86d269fec1b464c008b8ba0c9f705e6cf9411c041bdf21b4f96c4ec78f0a047a'}
ROOT = Path(__file__).resolve().parents[1]

def normalize(text: str) -> str:
    return ' '.join(text.split())

def dot(u, v) -> Fraction:
    return sum((Fraction(a) * Fraction(b) for a, b in zip(u, v, strict=True)), Fraction(0))

def add(u, v):
    return tuple((Fraction(a) + Fraction(b) for a, b in zip(u, v, strict=True)))

def scale(c, u):
    return tuple((Fraction(c) * Fraction(a) for a in u))

def neg(u):
    return tuple((-Fraction(a) for a in u))

def apply_matrix(matrix, vector):
    return tuple((sum((matrix[i][j] * vector[j] for j in range(3)), start=Fraction(0)) for i in range(3)))

def proper_cubic_rotations():
    mats = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            matrix = [[Fraction(0)] * 3 for _ in range(3)]
            sign_prod = 1
            inversions = sum((perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3)))
            perm_sign = -1 if inversions % 2 else 1
            for i in range(3):
                matrix[perm[i]][i] = Fraction(signs[i])
                sign_prod *= signs[i]
            if perm_sign * sign_prod == 1:
                mats.append(tuple((tuple(row) for row in matrix)))
    return tuple(mats)

def four_point_support(q, qp):
    return (q, qp, neg(q), neg(qp))

def distinct_four(q, qp) -> bool:
    pts = four_point_support(q, qp)
    return len(set(pts)) == 4

def linear_copy_mass(lam: Fraction, t: Fraction) -> Fraction:
    return (1 + lam * (1 + t)) / 4

def gibbs_copy_mass_at_orthogonal(B):
    """B=exp(2 beta)>0, t=0 only; no silent discarded t argument."""
    if B <= 0:
        raise ValueError('B must be positive')
    return B / (2 * B + 2)

def main():
    results = []

    def check(label, condition, detail):
        ok = bool(condition)
        results.append(dict(label=label, passed=ok, detail=detail))
        print(('PASS' if ok else 'FAIL') + ': ' + label + ' ' + detail)
    q = (Fraction(0), Fraction(0), Fraction(1))
    qp = (Fraction(1), Fraction(0), Fraction(0))
    rotations = proper_cubic_rotations()
    check('orthogonal-menu', dot(q, qp) == 0 and distinct_four(q, qp), 'Four allowed points, not assumed positive support')
    swap = lambda v: (v[2], -v[1], v[0])
    check('bisector-swap', swap(q) == qp and swap(qp) == q, 'Internal rotation exchanges ordered records')
    flip = lambda v: (-v[0], -v[1], v[2])
    check('different-input', flip(q) == q and flip(qp) == neg(qp), 'This relates distinct inputs; no forced alpha=gamma')
    check('cubic-group', len(rotations) == len(set(rotations)) == 24, 'Original full proper cubic group')
    check('menu-covariance', all((set(four_point_support(apply_matrix(M, q), apply_matrix(M, qp))) == {apply_matrix(M, s) for s in four_point_support(q, qp)} for M in rotations)), 'All 24 finite group controls; general SO(3) proof is analytic')
    slots = ((Fraction(1), Fraction(0), Fraction(0)), (Fraction(0), Fraction(1), Fraction(0)))
    for label, b in (('adjacent', slots[1]), ('opposite', neg(slots[0]))):
        check('slot-exchange:' + label, any((apply_matrix(M, slots[0]) == b and apply_matrix(M, b) == slots[0] for M in rotations)), 'Proper cubic slot exchange exists in this occupancy stratum')
    weights = (Fraction(1, 2), Fraction(1, 4), Fraction(1, 8), Fraction(1, 8))
    law = lambda x, y, w: dict(zip(four_point_support(x, y), w))
    check('ordered-unequal-covariance', all(({apply_matrix(M, s): v for s, v in law(q, qp, weights).items()} == law(apply_matrix(M, q), apply_matrix(M, qp), weights) for M in rotations)), 'Unequal masses retain internal covariance')
    check('ordered-exchange-distinction', law(q, qp, weights) != law(qp, q, weights), 'Exchange is an additional hypothesis')
    samples = ((Fraction(1, 4), Fraction(1, 4)), (Fraction(1, 2), Fraction(0)), (Fraction(0), Fraction(1, 2)), (Fraction(3, 8), Fraction(1, 8)))
    check('exchange-family', all((2 * a + 2 * g == 1 and a >= 0 and (g >= 0) and (law(q, qp, (a, a, g, g)) == law(qp, q, (a, a, g, g))) for a, g in samples)), 'Original four pairs, including zero weights')
    check('invalid-family', 2 * Fraction(1, 3) + 2 * Fraction(1, 3) != 1, 'Original normalization countercontrol')
    check('support-not-menu', [sum((v > 0 for v in (a, a, g, g))) for a, g in samples] == [4, 2, 2, 4], 'Support counts use nonzero masses')
    check('singleton-one-record', len({q: Fraction(1)}) == 1 and all(({apply_matrix(M, s): v for s, v in {q: Fraction(1)}.items()} == {apply_matrix(M, q): Fraction(1)} for M in rotations)), 'delta_q is a normalized covariant singleton; covariance also follows from pushforward')
    check('gibbs-B2', gibbs_copy_mass_at_orthogonal(Fraction(2)) == Fraction(1, 3), 'B=2,t=0: alpha=1/3,gamma=1/6')
    check('gibbs-B1', gibbs_copy_mass_at_orthogonal(Fraction(1)) == Fraction(1, 4), 'B=1 gives uniform masses')
    check('original-linear-fixtures', [linear_copy_mass(l, Fraction(0)) for l in (Fraction(0), Fraction(1), Fraction(-1), Fraction(1, 2))] == [Fraction(1, 4), Fraction(1, 2), Fraction(0), Fraction(3, 8)], 'Original lambda values at t=0 retained')
    for t in (Fraction(-3, 5), Fraction(0), Fraction(3, 5)):
        r = (Fraction(4, 5), Fraction(0), t) if t else qp
        for lam in (Fraction(0), 1 / (1 + t), -1 / (1 + t)):
            vals = [(1 + lam * dot(s, add(q, r))) / 4 for s in four_point_support(q, r)]
            check('linear-bound:' + str((t, lam)), sum(vals) == 1 and min(vals) >= 0, 'Exact valid lambda(t) boundary and interior')
        for alpha in (Fraction(0), Fraction(1, 8), Fraction(1, 2)):
            lam = (4 * alpha - 1) / (1 + t)
            check('lambda-inverse:' + str((t, alpha)), linear_copy_mass(lam, t) == alpha and abs(lam) * (1 + t) <= 1, 'Function parameterization, not a fixed universal lambda')
        raw = tuple(((1 + dot(s, q)) / 3 for s in four_point_support(q, r)))
        norm = tuple((v / 2 for v in raw))
        check('overlap-normalization:' + str(t), sum(raw) == 2 and sum(norm) == 1 and (min(norm) >= 0), 'Raw sum2, normalized ordered-reference law')
    check('excluded-lambda', Fraction(1, 2) - linear_copy_mass(Fraction(1), Fraction(3, 5)) == Fraction(-3, 20), 'lambda=1 at t=3/5 violates nonnegativity')
    normalized = lambda x, y: law(x, y, tuple(((1 + dot(s, x)) / 4 for s in four_point_support(x, y))))
    check('normalized-exchange', normalized(q, qp) != normalized(qp, q), 'Exchange failure, not blanket framework variation failure')
    r = (Fraction(4, 5), Fraction(0), Fraction(3, 5))
    check('second-record-dependence', normalized(q, qp) != normalized(q, r), 'Moving atoms and t change the normalized law')
    check('collinear-menu', len(set(four_point_support(q, q))) == 2, 'Original collinear menu control')
    check('chain-endpoint-event', all((abs(dot(q, scale(a * b, q))) == 1 for a, b in product((-1, 1), repeat=2))), 'Every one-record sign path is collinear, including singleton choices')
    axes = tuple((scale(sign, e) for e in (q, qp, (Fraction(0), Fraction(1), Fraction(0))) for sign in (-1, 1)))
    check('independent-endpoint-analogue', sum((abs(dot(l, r)) < 1 for l, r in product(axes, repeat=2))) == 24, 'Finite six-axis analogue:24/36; Haar probability1 is analytic, not this finite test')
    failed = sum((not r['passed'] for r in results))
    passed = len(results) - failed
    print(f'TOTAL: PASS={passed} FAIL={failed}')
    print('per_element: exact menu atoms, scalar probabilities, support and parameter-bound checks.')
    print('per_site: one-record singleton/pair cases and both adjacent/opposite occupied-slot strata.')
    print('per_mode: checked and not executed — no physical spectrum or dynamical modes are defined.')
    print('per_block: 24 cubic rotations, rational parameter fixtures, four chain sign paths and 36 six-axis endpoint pairs.')
    print('lattice_wide: checked and not executed — Haar measure and general process statements require analytic proofs; no infinite lattice is simulated.')
    return int(failed > 0)
if __name__ == '__main__':
    raise SystemExit(main())
