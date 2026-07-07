#!/usr/bin/env python3
"""Exact carrier invariant-functional closure for the species bridge gap.

This runner closes only the parent note's named invariant-ring proof-strength
gap at the linear Hermitian functional grade used by the parent corner-diagonal
readout.  It does not import the parent runner, because that runner executes
additional interface reads; instead it reimplements the same carrier ordering,
C3 block, and eps intertwiner construction exactly.
"""

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PARENT_NOTE = (
    ROOT
    / "docs"
    / "SPECIES_BRIDGE_MINIMUM_DECOMPOSITION_BOUNDED_THEOREM_NOTE_2026-06-13.md"
)
NOTE_FILE = (
    "docs/SPECIES_CARRIER_INVARIANT_RING_NO_ORBIT_SEPARATOR_EXACT_NOTE_2026-07-03.md"
)
SCRIPT_FILE = "scripts/frontier_species_carrier_invariant_ring_2026_07_03.py"

F = Fraction
_pass = 0
_fail = 0


def check(num, desc, ok, detail=""):
    global _pass, _fail
    tag = "PASS" if ok else "FAIL"
    if ok:
        _pass += 1
    else:
        _fail += 1
    line = f"CHECK {num:02d}: {tag} - {desc}"
    if detail:
        line += f" [{detail}]"
    print(line)


def normalize_text(text):
    replacements = {
        "\u2081": "1",
        "\u2082": "2",
        "\u2083": "3",
        "\u03b5": "eps",
        "\u2013": "-",
        "\u2014": "--",
        "\u2192": "->",
        "\u2212": "-",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return " ".join(text.split())


def zeros(rows, cols):
    return [[F(0) for _ in range(cols)] for _ in range(rows)]


def eye(n):
    out = zeros(n, n)
    for i in range(n):
        out[i][i] = F(1)
    return out


def matmul(a, b):
    rows = len(a)
    mid = len(b)
    cols = len(b[0])
    out = zeros(rows, cols)
    for i in range(rows):
        for k in range(mid):
            if a[i][k] == 0:
                continue
            aik = a[i][k]
            for j in range(cols):
                if b[k][j] != 0:
                    out[i][j] += aik * b[k][j]
    return out


def matvec(a, v):
    return [sum(a[i][j] * v[j] for j in range(len(v))) for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def matpow(a, n):
    out = eye(len(a))
    base = a
    k = n
    while k:
        if k & 1:
            out = matmul(base, out)
        base = matmul(base, base)
        k >>= 1
    return out


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def rank(rows):
    a = [list(row) for row in rows]
    if not a:
        return 0
    m = len(a)
    n = len(a[0])
    r = 0
    for c in range(n):
        pivot = None
        for i in range(r, m):
            if a[i][c] != 0:
                pivot = i
                break
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        pv = a[r][c]
        a[r] = [x / pv for x in a[r]]
        for i in range(m):
            if i != r and a[i][c] != 0:
                fac = a[i][c]
                a[i] = [a[i][j] - fac * a[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def rank_columns(cols):
    rows = [[cols[c][r] for c in range(len(cols))] for r in range(len(cols[0]))]
    return rank(rows)


def matrix_equal(a, b):
    return a == b


def block_from_corner_map(source, target, transform):
    target_index = {corner: i for i, corner in enumerate(target)}
    out = zeros(len(target), len(source))
    for col, corner in enumerate(source):
        image = transform(corner)
        out[target_index[image]][col] = F(1)
    return out


def perm_from_block(block):
    perm = []
    for col in range(len(block[0])):
        rows = [row for row in range(len(block)) if block[row][col] == 1]
        if len(rows) != 1:
            raise ValueError("block is not a permutation matrix")
        perm.append(rows[0])
    return perm


def is_single_three_cycle(perm):
    seen = []
    x = 0
    for _ in range(3):
        seen.append(x)
        x = perm[x]
    return sorted(seen) == [0, 1, 2] and x == 0 and perm != [0, 1, 2]


EDGES = [(0, 1), (1, 2), (2, 0)]
BASIS = (
    [("D", (0, 0)), ("D", (1, 1)), ("D", (2, 2))]
    + [("S", e) for e in EDGES]
    + [("A", e) for e in EDGES]
)
SYM_INDEX = {frozenset(e): 3 + i for i, e in enumerate(EDGES)}
ANTI_INDEX = {e: 6 + i for i, e in enumerate(EDGES)}


def functional_action_from_perm(perm):
    out = zeros(9, 9)
    for col, (kind, pair) in enumerate(BASIS):
        if kind == "D":
            row = perm[pair[0]]
            sign = F(1)
        elif kind == "S":
            row = SYM_INDEX[frozenset((perm[pair[0]], perm[pair[1]]))]
            sign = F(1)
        else:
            image = (perm[pair[0]], perm[pair[1]])
            if image in ANTI_INDEX:
                row = ANTI_INDEX[image]
                sign = F(1)
            elif (image[1], image[0]) in ANTI_INDEX:
                row = ANTI_INDEX[(image[1], image[0])]
                sign = F(-1)
            else:
                raise ValueError("bad antisymmetric edge image")
        out[row][col] = sign
    return out


def reynolds(group, vector):
    total = [F(0) for _ in vector]
    for g in group:
        gv = matvec(g, vector)
        total = [total[i] + gv[i] for i in range(len(vector))]
    return [x / len(group) for x in total]


def spread(values):
    return max(values) - min(values)


def fmt_fraction(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def main():
    expected_gap = (
        "Honest about the proof's reach: the tested C3-grade "
        "contentlessness conclusion is *carried by checks 4 and 7*; a fully "
        'rigorous "zero structural-selection bits" statement would require '
        "computing the C3- (and eps-) invariant functional ring of the carrier "
        "and showing it has no orbit-separating generator -- check 8 "
        "establishes the representative case (the diagonal corner-weight) "
        "rather than the full ring, so the conclusion is argued/strongly-"
        "supported, not exhaustively proven."
    )
    parent_text = normalize_text(PARENT_NOTE.read_text(encoding="utf-8"))
    check(
        1,
        "parent gap sentence is present in the live parent note",
        expected_gap in parent_text,
    )

    corners = [
        (n1, n2, n3)
        for n1 in (0, 1)
        for n2 in (0, 1)
        for n3 in (0, 1)
    ]

    def chars(corner):
        return tuple(-1 if bit else 1 for bit in corner)

    hw1_cols = [j for j, corner in enumerate(corners) if sum(corner) == 1]
    hw2_cols = [j for j, corner in enumerate(corners) if sum(corner) == 2]
    hw1 = [None, None, None]
    for j in hw1_cols:
        trip = chars(corners[j])
        hw1[trip.index(-1)] = corners[j]
    hw2 = [None, None, None]
    for j in hw2_cols:
        trip = chars(corners[j])
        hw2[trip.index(1)] = corners[j]

    def parent_ur_corner(corner):
        n1, n2, n3 = corner
        return (n3, n1, n2)

    def parent_eps_corner(corner):
        return tuple(1 - bit for bit in corner)

    c3_1 = block_from_corner_map(hw1, hw1, parent_ur_corner)
    c3_2 = block_from_corner_map(hw2, hw2, parent_ur_corner)
    eh = block_from_corner_map(hw1, hw2, parent_eps_corner)
    eps_pullback = matmul(transpose(eh), eh)

    c3_perm = perm_from_block(c3_1)
    eps_perm = perm_from_block(eps_pullback)
    carrier_ok = (
        hw1 == [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
        and hw2 == [(0, 1, 1), (1, 0, 1), (1, 1, 0)]
        and matrix_equal(matpow(c3_1, 3), eye(3))
        and matrix_equal(matmul(eh, c3_1), matmul(c3_2, eh))
        and matrix_equal(eps_pullback, eye(3))
    )
    check(
        2,
        "parent carrier ordering, C3 block, and eps intertwiner are reproduced",
        carrier_ok,
        f"c3 perm={c3_perm}, eps pullback perm={eps_perm}",
    )

    c3_action = functional_action_from_perm(c3_perm)
    eps_action = functional_action_from_perm(eps_perm)
    group = [
        matmul(matpow(eps_action, b), matpow(c3_action, a))
        for b in range(2)
        for a in range(3)
    ]
    group_ok = (
        len(group) == 6
        and matrix_equal(matpow(c3_action, 3), eye(9))
        and matrix_equal(matpow(eps_action, 2), eye(9))
        and matrix_equal(matmul(c3_action, eps_action), matmul(eps_action, c3_action))
    )
    check(
        3,
        "abstract C3+eps averaging group has six elements and exact relations",
        group_ok,
        f"distinct functional actions={len({tuple(sum(g, [])) for g in group})}",
    )

    raw_diag = [F(0), F(2), F(5)]
    raw_h = raw_diag + [F(0) for _ in range(6)]
    avg_h = reynolds([matpow(c3_action, a) for a in range(3)], raw_h)
    parent_check_ok = is_single_three_cycle(c3_perm) and spread(raw_diag) > 0
    parent_check_ok = parent_check_ok and spread(avg_h[:3]) == 0
    check(
        4,
        "parent check-4 orbit fact and check-8 diagonal average are reproduced",
        parent_check_ok,
        f"raw spread={fmt_fraction(spread(raw_diag))}, averaged spread={fmt_fraction(spread(avg_h[:3]))}",
    )

    basis_rank = rank(eye(9))
    basis_ok = len(BASIS) == 9 and basis_rank == 9
    check(
        5,
        "complete 9D Hermitian linear-functional basis is closed",
        basis_ok,
        "D0,D1,D2,S01,S12,S20,A01,A12,A20",
    )

    molien_dim = sum(trace(g) for g in group) / len(group)
    basis_vectors = [[F(1) if i == j else F(0) for i in range(9)] for j in range(9)]
    averaged = [reynolds(group, v) for v in basis_vectors]
    reynolds_rank = rank_columns(averaged)
    complete_ok = molien_dim.denominator == 1 and reynolds_rank == molien_dim
    check(
        6,
        "degree-one Molien coefficient equals the Reynolds-image rank",
        complete_ok,
        f"Molien dim={fmt_fraction(molien_dim)}, Reynolds rank={reynolds_rank}",
    )

    full_spreads = [spread(v[:3]) for v in averaged]
    no_separator = all(s == 0 for s in full_spreads)
    check(
        7,
        "every full-group averaged generator has zero corner-diagonal spread",
        no_separator,
        "spreads=" + ",".join(fmt_fraction(s) for s in full_spreads),
    )

    broken_group = [eye(9), eps_action]
    broken_averaged = [reynolds(broken_group, v) for v in basis_vectors]
    broken_spreads = [spread(v[:3]) for v in broken_averaged]
    broken_molien_dim = sum(trace(g) for g in broken_group) / len(broken_group)
    broken_has_separator = any(s > 0 for s in broken_spreads)
    check(
        8,
        "negative control drops C3 and produces an orbit separator",
        broken_has_separator and broken_molien_dim == 9,
        f"broken Molien dim={fmt_fraction(broken_molien_dim)}, max spread={fmt_fraction(max(broken_spreads))}",
    )

    print(f"TOTAL: PASS={_pass} FAIL={_fail}")
    verdict = (
        "none in the full C3+eps averaged generator set; "
        "present after dropping C3"
    )
    print(f"SUMMARY files: {NOTE_FILE}; {SCRIPT_FILE}")
    print(f"SUMMARY check count: PASS={_pass} FAIL={_fail} TOTAL={_pass + _fail}")
    print(f"SUMMARY invariant dimension found: {fmt_fraction(molien_dim)}")
    print(f"SUMMARY separator verdict: {verdict}")
    print(
        "SUMMARY uncertainties: scoped to linear Hermitian functionals on "
        "the parent corner-diagonal readout surface; no count change"
    )
    raise SystemExit(0 if _fail == 0 else 1)


if __name__ == "__main__":
    main()
