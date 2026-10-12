#!/usr/bin/env python3
"""Exact finite author controls; none proves the infinite-volume theorem."""
from __future__ import annotations
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = [
    "docs/GAPPED_BOOST_INVARIANCE_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/MICROSCOPIC_CURRENT_IMPLEMENTATION_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    ".claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/EVIDENCE_MAP.json"
]
if not __debug__:
    raise RuntimeError("Run without -O: finite control assertions must be enabled")

import argparse
import hashlib
import json
from pathlib import Path
import platform
import sympy as sp

I = sp.I


def comm(a, b):
    return a * b - b * a


def delta(g, a):
    return I * comm(g, a)


def l1(a):
    return sp.simplify(sum(abs(x) for x in a))


def basis(d, i, j):
    a = sp.zeros(d)
    a[i, j] = 1
    return a


def embed(a, at, sites=(-1, 0, 1)):
    return sp.kronecker_product(*[a if x == at else sp.eye(a.rows) for x in sites])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mutation', choices=['none', 'current_sign', 'current_half',
                        'global_scalar', 'degenerate_rank_one', 'one_sided'], default='none')
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('finite_controls_results.json'))
    args = parser.parse_args()
    rows = []

    def record(name, ok, **values):
        rows.append({'name': name, 'ok': bool(ok), **{k: str(v) for k, v in values.items()}})

    def same(name, a, b):
        residual = l1(a-b) if isinstance(a, sp.MatrixBase) else sp.simplify(a-b)
        record(name, residual == 0, residual=residual)

    x = sp.Matrix([[0, 1], [1, 0]])
    y = sp.Matrix([[0, -I], [I, 0]])
    z = sp.diag(1, -1)
    n = sp.diag(0, 1)
    fixtures = [('qubit_simple', n, x, y, z),
                ('qutrit_degenerate', sp.diag(0, 0, 1),
                 sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
                 sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
                 sp.diag(1, -1, 0))]
    for label, number, q, yy, zz in fixtures:
        d = number.rows
        # Actual finite density h_x=n_x+Q_x-Q_(x+1), with both centers
        # meeting site zero. Onsite sums mean every derivative of a site-zero
        # observable remains on site zero, so these cutoffs are exact there.
        hs = {a: embed(number, a)+embed(q, a)-embed(q, a+1) for a in [-1, 0]}
        hc = hs[-1]+hs[0]
        bc = -hs[-1]
        pc = I*comm(hc, bc)
        pair = sp.zeros(d**3)
        for a in hs:
            for b in hs:
                pair += I*sp.Rational(1, 2)*(b-a)*comm(hs[a], hs[b])
        if args.mutation == 'current_sign':
            pair = -pair
        if args.mutation == 'current_half':
            pair = 2*pair
        same(label+'_oriented_pair_current', pc, pair)
        onsite_current = I*comm(number, q)
        onsite_conservation = I*comm(number, onsite_current)
        for a in range(d):
            for b in range(d):
                aa = embed(basis(d, a, b), 0)
                same(f'{label}_energy_{a}{b}', delta(hc, aa), delta(embed(number, 0), aa))
                same(f'{label}_boost_{a}{b}', delta(bc, aa), delta(embed(q, 0), aa))
                same(f'{label}_current_{a}{b}', delta(pair, aa), delta(embed(onsite_current, 0), aa))
                nested = delta(hc, delta(pc, aa))-delta(pc, delta(hc, aa))
                same(f'{label}_conservation_{a}{b}', nested, delta(embed(onsite_conservation, 0), aa))
        omega = sp.zeros(d**3, 1)
        omega[0] = 1
        probe = embed(yy, 0)
        boost_expectation = (omega.H*delta(bc, probe)*omega)[0]
        same(label+'_boost_expectation', boost_expectation, -2)
        physical_h = sum((embed(number, a) for a in [-1, 0, 1]), sp.zeros(d**3))
        diag = list(physical_h.diagonal())
        record(label+'_positive_onsite_spectrum', min(diag) == 0 and min(v for v in diag if v>0) == 1,
               zero_multiplicity=sum(v==0 for v in diag), positive_gap=min(v for v in diag if v>0))
        if label == 'qubit_simple':
            same('qubit_current_density', onsite_current, y)
            same('qubit_conservation_density', onsite_conservation, -x)
            actual = delta(hc, delta(pc, probe))-delta(pc, delta(hc, probe))
            same('qubit_conservation_failure_expectation', (omega.H*actual*omega)[0], 2)
            record('qubit_kernel_simple_in_finite_onsite_control', diag.count(0) == 1)
        else:
            same('qutrit_current_is_zero', pc, sp.zeros(d**3))
            same('qutrit_conservation_is_zero', onsite_conservation, sp.zeros(d))
            record('qutrit_kernel_degenerate_in_finite_onsite_control', diag.count(0) == 8,
                   zero_multiplicity=diag.count(0))

    # Exact finite energy filtering: every nonzero energy difference below
    # is outside the Fourier support, while g(0)=1. This evaluates the actual
    # finite spectral formula entry by entry, not an approximate time integral.
    def filter_matrix(a, energies):
        return sp.Matrix(a.rows, a.cols, lambda i,j: a[i,j] if energies[i] == energies[j] else 0)

    energies = [0, 2, 5]
    a = sp.Matrix([[7, 1, 2], [3, 11, 4], [5, 6, 13]])
    filtered_actual = filter_matrix(a, energies)
    # Separately derived in the note's G49: only its three diagonal entries
    # have zero energy transfer; every off-diagonal transfer has magnitude >=2.
    filtered_claim = sp.diag(7, 11, 13)
    if args.mutation == 'global_scalar':
        filtered_claim = 7*sp.eye(3)
    same('filtered_operator_matches_actual_spectral_formula', filtered_claim, filtered_actual)
    om = sp.Matrix([1, 0, 0])
    same('simple_filter_column', filtered_actual*om, 7*om)
    same('simple_filter_adjoint_column', filtered_actual.H*om, 7*om)
    record('simple_filter_is_not_global_scalar', l1(filtered_actual-7*sp.eye(3)) != 0,
           scalar_defect=l1(filtered_actual-7*sp.eye(3)))
    for i in range(3):
        for j in range(3):
            same(f'filtered_commutator_expectation_{i}{j}', (om.H*comm(basis(3,i,j),filtered_actual)*om)[0], 0)

    number, q, yy, zz = fixtures[1][1:]
    dg = filter_matrix(yy, [0, 0, 1])
    zero_projection = sp.diag(1, 1, 0)
    projection_claim = zero_projection
    if args.mutation == 'degenerate_rank_one':
        projection_claim = sp.diag(1, 0, 0)
    same('degenerate_actual_zero_projection_column', dg*om, projection_claim*yy*om)
    record('degenerate_filter_column_not_scalar', l1(dg*om) != 0,
           vacuum_expectation=(om.H*yy*om)[0], column_l1=l1(dg*om))
    same('degenerate_filtered_boost_expectation', (om.H*delta(q,dg)*om)[0], -2)

    annihilator = basis(2,0,1)
    om2 = sp.Matrix([1,0])
    same('one_sided_scalar_column', annihilator*om2, sp.zeros(2,1))
    record('one_sided_adjoint_column_nonzero', l1(annihilator.H*om2) != 0)
    actual_commutator = (om2.H*comm(x,annihilator)*om2)[0]
    claimed_commutator = -1 if args.mutation != 'one_sided' else 0
    same('one_sided_commutator_does_not_vanish', actual_commutator, claimed_commutator)

    # Explicit finite support-chain enumeration for the LR recursion. Bond
    # labels j represent {j,j+1}. Norms are one, cardinality s=2, per-site J=2.
    # A chain only meets its immediately preceding bond, unlike a nested
    # support-union history. Both are different estimates in the proof.
    counts = {-1: 1, 0: 1}
    for order in range(1, 8):
        total = sum(counts.values())
        bound = 2*4**(order-1)
        record(f'lr_chain_weight_bound_{order}', total <= bound, actual=total, bound=bound)
        max_distance = max(max(abs(j),abs(j+1)) for j in counts)
        record(f'lr_chain_distance_{order}', max_distance <= order,
               actual_max_distance=max_distance, bound=order)
        record(f'lr_chain_distance_sharp_control_{order}', max_distance > order-1,
               rejected_missing_step_bound=order-1)
        nxt = {}
        for j, count in counts.items():
            for k in [j-1,j,j+1]:
                nxt[k] = nxt.get(k,0)+count
        counts = nxt

    result = {'role':'author finite controls, not independent review or infinite-volume proof',
              'mutation':args.mutation, 'python':platform.python_version(), 'sympy':sp.__version__,
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'rows':rows, 'passed':sum(r['ok'] for r in rows), 'failed':sum(not r['ok'] for r in rows)}
    # Publication suppresses output-directory creation and result writing only; the complete result remains computed.
    for row in rows:
        print(json.dumps(row,sort_keys=True))
    print(f"TOTAL: PASS={result['passed']} FAIL={result['failed']}")
    print('per_element: exact current, filter and vacuum-column finite fixtures are checked; the infinite argument is in the note.')
    print('per_site: finite matrix-unit and support recursion fixtures are checked; intended-model conservation remains supplied.')
    print('per_mode: finite gap/filter fixtures are checked; they do not construct an actual infinite GNS spectrum.')
    print('per_block: simple and degenerate vacuum fixtures retain both passing and failing scalar-column controls.')
    print('lattice_wide: checked and not executed — rapid almost-local graph bounds and state identities rely on the conditional analytic proof.')
    print('SCOPE: Original finite controls only; documented mutation survivors and insensitive rows remain. Counts do not prove the analytic theorem or a physical model.')
    return 1 if result['failed'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
