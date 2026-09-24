#!/usr/bin/env python3
"""Independent finite rotor charge/shift words; no author builder or imports."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import hashlib
import json

A = (0, 3, 5, 6)
B = (1, 2, 4, 7)
EDGES = tuple((a, b) for a in A for b in B if (a ^ b) in (1, 2, 4))
OMEGA = (tuple(1 if x in A else 0 for x in range(8)), (0,) * 12)


def clean(v):
    return {k: c for k, c in v.items() if c}


def add(*terms):
    ans = defaultdict(Fraction)
    for scale, v in terms:
        for k, c in v.items():
            ans[k] += scale * c
    return clean(ans)


def hop(v, center=None):
    ans = defaultdict(Fraction)
    for (q, e), c in v.items():
        for k, (a, b) in enumerate(EDGES):
            if center is not None and a != center:
                continue
            if not q[a] or q[b]:
                continue
            qq, ee = list(q), list(e)
            charge = qq[a]
            qq[a], qq[b], ee[k] = 0, charge, ee[k] - charge
            ans[(tuple(qq), tuple(ee))] += c
    return clean(ans)


def birth(v, edge, sign):
    ans = defaultdict(Fraction)
    k = EDGES.index(edge)
    a, b = edge
    for (q, e), c in v.items():
        if q[a] or q[b]:
            continue
        qq, ee = list(q), list(e)
        qq[a], qq[b], ee[k] = sign, -sign, ee[k] + sign
        ans[(tuple(qq), tuple(ee))] += c
    return clean(ans)


def mark(v, edge, name):
    if name == 'coherent':
        return add((1, birth(v, edge, 1)), (1, birth(v, edge, -1)))
    return birth(v, edge, 1 if name == 'plus' else -1)


def adjoint_product_polynomial(v):
    """Translation polynomial of X*X on arbitrary initial physical fields."""
    ans = defaultdict(Fraction)
    for (q1, e1), c1 in v.items():
        for (q2, e2), c2 in v.items():
            if q1 == q2:
                shift = tuple(y - x for x, y in zip(e1, e2))
                ans[shift] += c1 * c2
    return clean(ans)


def check_gauss(v):
    for q, e in v:
        div = [0] * 8
        for field, (a, b) in zip(e, EDGES):
            div[a] += field
            div[b] -= field
        assert div == [q[x] - int(x in A) for x in range(8)]


def main():
    omega = {OMEGA: Fraction(1)}
    F1 = hop(omega)
    F2 = hop(F1)
    rows = []
    zero = (0,) * 12
    all_vectors = {}
    for edge in EDGES:
        for name, b, r in [('plus', 2, 4), ('minus', 2, 2), ('coherent', 4, 6)]:
            bv = mark(F1, edge, name)
            rv = add((-1, hop(bv, center=edge[0])))
            direct = add((Fraction(1, 2), mark(F2, edge, name)), (-1, hop(bv)))
            assert rv == direct
            assert adjoint_product_polynomial(bv) == {zero: b}
            assert adjoint_product_polynomial(rv) == {zero: r}
            check_gauss(bv); check_gauss(rv)
            for edge2 in EDGES:
                assert not birth(rv, edge2, 1) and not birth(rv, edge2, -1)
            wrong = add((1, mark(F2, edge, name)), (-1, hop(bv)))
            assert wrong != rv
            rows.append({'edge': edge, 'mark': name, 'B_adjoint_B': b,
                         'R_adjoint_R': r, 'B_word_count': len(bv),
                         'R_word_count': len(rv), 'R_dark': True,
                         'minimal_source_identity': True,
                         'missing_half_coefficient_rejected': True})
            all_vectors[(edge, name)] = rv

    # The complete rotor W=1,N=6 charge labels: five positive and one negative
    # occupied site, with one A vacancy and one B vacancy. The original loss
    # is exactly 2 on adjacent vacancy pairs and 0 on the other pairs.
    losses = []
    for av in A:
        for bv in B:
            occupied = [x for x in range(8) if x not in (av, bv)]
            for negative in occupied:
                q = tuple(0 if x in (av, bv) else (-1 if x == negative else 1)
                          for x in range(8))
                v = {(q, zero): Fraction(1)}
                resolved = sum(sum(c*c for c in birth(v, edge, sign).values())
                               for edge in EDGES for sign in (1, -1))
                coherent = sum(sum(c*c for c in mark(v, edge, 'coherent').values())
                               for edge in EDGES)
                assert resolved == coherent == (2 if (av, bv) in EDGES else 0)
                losses.append(int(resolved))

    # A coherent birth cannot be replaced by a resolved mixture merely because
    # its source norm agrees. The cross-source density on one edge is nonzero.
    edge = EDGES[0]
    rp, rm = all_vectors[(edge, 'plus')], all_vectors[(edge, 'minus')]
    assert not set(rp).intersection(rm)
    normp = sum(c*c for c in rp.values())
    normm = sum(c*c for c in rm.values())
    cross_hs_squared = 2 * normp * normm
    assert cross_hs_squared == 16
    totals = {}
    for instrument in ('resolved', 'coherent'):
        selected = [row for row in rows if (row['mark'] == 'coherent') == (instrument == 'coherent')]
        totals[instrument] = {'sum_B_adjoint_B': sum(row['B_adjoint_B'] for row in selected),
                              'sum_R_adjoint_R': sum(row['R_adjoint_R'] for row in selected)}
        assert totals[instrument] == {'sum_B_adjoint_B': 48, 'sum_R_adjoint_R': 72}

    result = {'status': 'PASS-exact-primitive-source-identities',
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'edge_order': EDGES, 'mark_checks': rows, 'instrument_totals': totals,
              'full_first_high_charge_label_count': len(losses),
              'bright_charge_labels': losses.count(2), 'dark_charge_labels': losses.count(0),
              'rotor_loss_maximum': max(losses),
              'coherent_vs_resolved_single_edge_source_difference_HS_squared': int(cross_hs_squared),
              'scope': 'Integer rotor charge/shift words and exact Laurent X*X identities for arbitrary input field. Not finite-spin or dynamical replication; no generator diagonalization or author code.'}
    here = Path(__file__).resolve().parent
    (here / 'PRIMITIVE_SOURCE_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
