#!/usr/bin/env python3
"""Independent legal-hop reconstruction of the finite-spin H2 core correction.

Uses physical charge/electric-flux states and no Fourier-fiber or existing
ring matrix builder.  Output is a finite-core coefficient table, not a
fixed-time convergence certificate.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/core_derivation.py',)
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
import hashlib, json, math
from pathlib import Path

BKG = (1, 0, 1, 0, 1, 0)
QSTAR = (1, -1, 1, 0, 1, 1)
ESTAR = (1, 0, 0, 0, 0, 1)
INITIAL = (QSTAR, ESTAR)


def valid(state):
    q, e = state
    return all(e[j] - e[(j - 1) % 6] + BKG[j] == q[j] for j in range(6))


def count_empty_A(state):
    q, _ = state
    return sum(q[j] == 0 for j in (0, 2, 4))


def all_hops(state, spin=None):
    """Return physical moves with T amplitude, edge, source m and shift a."""
    q, e = state
    out = []
    C = None if spin is None else spin * (spin + 1)
    for x, charge in enumerate(q):
        if charge == 0:
            continue
        for step in (-1, 1):
            y = (x + step) % 6
            if q[y] != 0:
                continue
            edge = x if step == 1 else y
            a = -charge * step
            m = e[edge]
            ee = list(e)
            ee[edge] += a
            if spin is not None and (abs(ee[edge]) > spin or any(abs(v) > spin for v in e)):
                continue
            if spin is None:
                amplitude = -1.0
            else:
                radicand = 1.0 - m * (m + a) / C
                if radicand < -1e-14:
                    raise ArithmeticError((spin, m, a, radicand))
                amplitude = -math.sqrt(max(0.0, radicand))
            qq = list(q)
            qq[x], qq[y] = 0, charge
            target = (tuple(qq), tuple(ee))
            assert valid(target), (state, target, edge, a)
            out.append((target, amplitude, edge, m, a))
    return out


def two_hop_paths(state, spin=None):
    """All ordered P->Pi1->P paths with exact first-order H2 coefficient."""
    assert count_empty_A(state) == 0
    paths = []
    for q1, amp1, _e1, m1, a1 in all_hops(state, spin):
        if count_empty_A(q1) != 1:
            continue
        for q2, amp2, _e2, m2, a2 in all_hops(q1, spin):
            if count_empty_A(q2) != 0:
                continue
            # H2=-P T Pi1 T P.  For T_S=-1+v/(2C)+O(C^-2),
            # the coefficient of C^-1 in each negative two-hop amplitude is
            # +(v1+v2)/2.
            d = Fraction(m1 * (m1 + a1) + m2 * (m2 + a2), 2)
            paths.append((q2, -amp1 * amp2, d, (m1, a1, m2, a2)))
    return paths


def rotor_h2(state):
    out = defaultdict(Fraction)
    for q2, _h2, _d, _data in two_hop_paths(state):
        out[q2] -= 1
    return dict(out)


def rotor_d(state):
    out = defaultdict(Fraction)
    for q2, _h2, d, _data in two_hop_paths(state):
        out[q2] += d
    return dict(out)


def walk_nodes(radius):
    nodes = {0: INITIAL}
    seen = {INITIAL}
    def choose(current, previous, positive):
        candidates = [x for x in rotor_h2(current) if x != current and x != previous]
        assert len(candidates) == 1, (current, candidates, previous)
        return candidates[0]
    plus_prev = None
    cur = INITIAL
    for n in range(1, radius + 1):
        candidates = [x for x in rotor_h2(cur) if x != cur and x != plus_prev]
        if plus_prev is None:
            picked = [x for x in candidates if x[0][5] == 0]
            assert len(picked) == 1, candidates
            nxt = picked[0]
        else:
            assert len(candidates) == 1
            nxt = candidates[0]
        assert nxt not in seen
        seen.add(nxt)
        nodes[n] = nxt
        plus_prev, cur = cur, nxt
    minus_prev = None
    cur = INITIAL
    for n in range(-1, -radius - 1, -1):
        candidates = [x for x in rotor_h2(cur) if x != cur and x != minus_prev]
        if minus_prev is None:
            candidates = [x for x in candidates if x not in nodes.values()]
        assert len(candidates) == 1, candidates
        nxt = candidates[0]
        assert nxt not in seen
        seen.add(nxt)
        nodes[n] = nxt
        minus_prev, cur = cur, nxt
    return nodes


def frac(x):
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def finite_spin_h2(state, spin):
    out = defaultdict(float)
    for q1, amp1, *_ in all_hops(state, spin):
        if count_empty_A(q1) != 1:
            continue
        for q2, amp2, *_ in all_hops(q1, spin):
            if count_empty_A(q2) == 0:
                out[q2] -= amp1 * amp2
    return dict(out)


def main():
    qwords = set(permutations((0, -1, 1, 1, 1, 1)))
    pwords = [q for q in qwords if all(q[j] for j in (0, 2, 4))]
    assert len(pwords) == 15 and valid(INITIAL) and count_empty_A(INITIAL) == 0
    assert len(two_hop_paths(INITIAL)) == 4
    assert sum(1 for p in two_hop_paths(INITIAL) if p[0] == INITIAL) == 2

    nodes = walk_nodes(12)
    inv = {s: n for n, s in nodes.items()}
    assert len(set(nodes.values())) == len(nodes)
    h2_rows, d_rows = {}, {}
    for n, state in nodes.items():
        if not -8 <= n <= 8:
            continue
        h2 = rotor_h2(state)
        d = rotor_d(state)
        assert h2.get(state) == -2
        h2n = {inv[t]: v for t, v in h2.items() if t in inv}
        dn = {inv[t]: v for t, v in d.items() if t in inv}
        assert len(h2n) == 3, (n, h2n)
        h2_rows[str(n)] = {str(k): int(v) for k, v in sorted(h2n.items())}
        d_rows[str(n)] = {str(k): frac(v) for k, v in sorted(dn.items())}
        # H2 support is the diagonal and the two path neighbors.
        assert set(h2n) == {n - 1, n, n + 1}
        assert set(dn) == set(h2n)

    # Independently compare the finite-spin matrix coefficient at each fixed
    # core entry with D, while staying away from every spin boundary.
    convergence = []
    core = range(-2, 3)
    for spin in (5, 8, 12, 20, 32):
        C = spin * (spin + 1)
        maximum = 0.0
        compared = 0
        for n in core:
            state = nodes[n]
            exact = finite_spin_h2(state, spin)
            rotor = rotor_h2(state)
            d = rotor_d(state)
            for target in set(rotor) | set(d):
                if target not in inv:
                    continue
                diff = C * (exact.get(target, 0.0) - rotor.get(target, 0))
                maximum = max(maximum, abs(diff - float(d.get(target, 0))))
                compared += 1
        convergence.append({"S": spin, "C": C, "fixed_core_entries": compared,
                            "max_abs_C_times_remainder": maximum,
                            "scaled_by_C": maximum / C})

    result = {
        "claim_status": "independent exact path-coefficient reconstruction on a finite electric-support core; fixed-time convergence not established",
        "source_revision": "b6eb31bedb3134dfacd8f4ab83cb7d96fc6dc953",
        "source_note_sha256": "76d7f2faf3a0b4635499ddff1d8a88868d691d58c035780af737129701e30eeb",
        "model": "six-site alternating ring, q=(1,-1,1,0,1,1), E=(1,0,0,0,0,1), actual resolved first-mark output",
        "basis": "physical integer-link-flux states; all ordered P->Pi1->P legal-hop paths are enumerated",
        "path_coordinate": "n=0 is actual output; positive direction is selected by vacancy moving to site 5; one path edge per H2 off-diagonal",
        "P_charge_words": len(pwords),
        "paths_from_initial": len(two_hop_paths(INITIAL)),
        "initial_H2_terms": {"diagonal": -2, "distinct_neighbors": 2, "neighbor_amplitudes": [-1, -1]},
        "D_matrix_rows_n_minus8_to8": d_rows,
        "H2_infinity_matrix_rows_n_minus8_to8": h2_rows,
        "finite_spin_core_comparison": convergence,
        "interpretation": "The matrix rows include both diagonal returns and each distinct two-hop endpoint. Fixed-core agreement does not bound propagation to flux values growing with S or time.",
    }
    data = json.dumps(result, indent=2) + "\n"
    Path(__file__).with_name("CORE_D_RESULTS.json").write_text(data)
    print(data, end="")

if __name__ == "__main__":
    main()
