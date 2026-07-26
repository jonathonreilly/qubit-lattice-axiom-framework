#!/usr/bin/env python3
"""Cycle 705 - the confusability floor of the first availability set.

The landed empty-state bootstrap leaves this residual:

    "The free off-mirror part of `A0`: ... what remains is which side the
     fixed rule's `A0` sits on."
    -- BOOTSTRAP_CONTINUATION_..._2026-07-04, Residual 1

Both sides of that residual were previously symmetric: nothing supplied by
the axioms distinguished a chiral `A0` from an achiral one.  This runner
shows they are not symmetric under a functional the axioms already carry --
the Clifford trace overlap of two contents -- and computes the exact gap.

Everything below is exact rational arithmetic on integer direction vectors.
No sampling, no floating point, no imports from the repository.

Object.  Contents are polar vectors on the content sphere (the landed
coupled-action model).  Directions are carried as primitive integer vectors
`v`; the state overlap of two contents of equal length is

    Tr(P_v P_w) = (1 + v.w/|v|^2) / 2,

which is forced by the Cl(3,0) identification the Qubit clause supplies, not
chosen (C3 re-earns it).  Define the confusability of a set

    conf(A) = max over distinct pairs of Tr(P_v P_w).

Rows:

  C1  the proper octahedral group O: order 24, closed, all det +1
  C2  orbit sizes on the content sphere are exactly {6, 8, 12, 24},
      and size 6 holds exactly for the four-fold-axis (face) directions
  C3  the Clifford overlap identity, exact, with a wrong-formula control
  C4  conf of the three mirror-locus orbits: 1/2, 2/3, 3/4
  C5  the three-rotation identity: sum_a v . R_a v = |v|^2 over the scan
  C6  the floor and its unique saturator: conf >= 1/2 always, equality iff
      the face orbit; every other orbit has conf >= 2/3
  C7  chirality: every chiral orbit has size 24 and conf >= 2/3
  C8  distinguishability: at most 2 mutually distinguishable contents in any
      orbit, and a chiral orbit has none
  C9  negative controls: a non-invariant set beats the floor
"""

from fractions import Fraction
from itertools import permutations, product

FAILURES = []
PASSES = []


def check(name: str, ok: bool, detail: str = "") -> None:
    (PASSES if ok else FAILURES).append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


# ---------------------------------------------------------------------------
# the proper octahedral group
# ---------------------------------------------------------------------------

Vec = tuple  # (int, int, int)
Mat = tuple  # 3x3 rows


def matmul(A: Mat, B: Mat) -> Mat:
    return tuple(
        tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def matvec(A: Mat, v: Vec) -> Vec:
    return tuple(sum(A[i][k] * v[k] for k in range(3)) for i in range(3))


def det3(A: Mat) -> int:
    return (
        A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
        - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
        + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    )


def signed_permutations():
    """All 48 signed permutation matrices; the cubic group in its lattice form."""
    out = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            M = [[0, 0, 0] for _ in range(3)]
            for i in range(3):
                M[i][perm[i]] = signs[i]
            out.append(tuple(tuple(r) for r in M))
    return out


FULL_CUBIC = signed_permutations()
PROPER = [M for M in FULL_CUBIC if det3(M) == 1]
IDENT = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
INVERSION = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))

# the three 90-degree rotations about the coordinate axes, used by C5
# R_x: (x,y,z) -> (x,-z,y)   R_y: (x,y,z) -> (z,y,-x)   R_z: (x,y,z) -> (-y,x,z)
R_X = ((1, 0, 0), (0, 0, -1), (0, 1, 0))
R_Y = ((0, 0, 1), (0, 1, 0), (-1, 0, 0))
R_Z = ((0, -1, 0), (1, 0, 0), (0, 0, 1))
QUARTER_TURNS = (R_X, R_Y, R_Z)


def c1_group():
    order_ok = len(PROPER) == 24
    dets_ok = all(det3(M) == 1 for M in PROPER)
    S = set(PROPER)
    closed = all(matmul(A, B) in S for A in PROPER for B in PROPER)
    inverses = all(any(matmul(A, B) == IDENT for B in PROPER) for A in PROPER)
    quarters_in = all(Q in S for Q in QUARTER_TURNS)
    check(
        "C1 proper octahedral group: order 24, closed, det +1, quarter-turns present",
        order_ok and dets_ok and closed and inverses and quarters_in,
        f"|O|={len(PROPER)}",
    )


# ---------------------------------------------------------------------------
# orbits on the content sphere
# ---------------------------------------------------------------------------


def orbit(v: Vec):
    return frozenset(matvec(M, v) for M in PROPER)


def primitive(v: Vec) -> bool:
    from math import gcd

    g = gcd(gcd(abs(v[0]), abs(v[1])), abs(v[2]))
    return g == 1


def scan_directions(bound: int):
    """Primitive nonzero integer directions in a cube of the given half-width."""
    out = []
    rng = range(-bound, bound + 1)
    for v in product(rng, repeat=3):
        if v == (0, 0, 0) or not primitive(v):
            continue
        out.append(v)
    return out


SCAN = scan_directions(3)
ORBITS = sorted({orbit(v) for v in SCAN}, key=lambda o: (len(o), sorted(o)))


def is_face(v: Vec) -> bool:
    """A four-fold-axis direction: one nonzero component."""
    return sum(1 for c in v if c != 0) == 1


def c2_orbit_sizes():
    sizes = sorted({len(o) for o in ORBITS})
    sizes_ok = set(sizes) <= {6, 8, 12, 24}

    # orbit-stabilizer, re-earned: |orbit| * |stabilizer| = 24
    os_ok = True
    for o in ORBITS:
        v = next(iter(o))
        stab = sum(1 for M in PROPER if matvec(M, v) == v)
        if len(o) * stab != 24:
            os_ok = False
            break

    # size 6 happens exactly on the four-fold axes, and there is one such orbit
    six = [o for o in ORBITS if len(o) == 6]
    six_ok = len(six) == 1 and all(is_face(v) for v in six[0])
    face_orbit_ok = six[0] == orbit((0, 0, 1)) if six else False

    check(
        "C2 orbit sizes are exactly {6,8,12,24}; the unique size-6 orbit is the face orbit",
        sizes_ok and os_ok and six_ok and face_orbit_ok,
        f"sizes seen={sizes}, orbits scanned={len(ORBITS)}",
    )


# ---------------------------------------------------------------------------
# the Clifford overlap identity  (exact Gaussian-rational 2x2 arithmetic)
# ---------------------------------------------------------------------------
# A 2x2 matrix over Gaussian rationals is a 2x2 tuple of (re, im) Fraction pairs.

Z = (Fraction(0), Fraction(0))


def z(re, im=0):
    return (Fraction(re), Fraction(im))


def zmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def zadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mmul(A, B):
    return tuple(
        tuple(
            zadd(zmul(A[i][0], B[0][j]), zmul(A[i][1], B[1][j])) for j in range(2)
        )
        for i in range(2)
    )


def mtrace(A):
    return zadd(A[0][0], A[1][1])


def projector(a):
    """P_a = (I + a.sigma)/2 for a rational Bloch vector a."""
    ax, ay, az = (Fraction(c) for c in a)
    half = Fraction(1, 2)
    return (
        (z(half * (1 + az)), (half * ax, -half * ay)),
        ((half * ax, half * ay), z(half * (1 - az))),
    )


def msub(A, B):
    return tuple(
        tuple((A[i][j][0] - B[i][j][0], A[i][j][1] - B[i][j][1]) for j in range(2))
        for i in range(2)
    )


def is_zero(A):
    return all(A[i][j] == Z for i in range(2) for j in range(2))


def c3_clifford_overlap():
    """Tr(P_a P_b) = (1 + a.b)/2, and P_a is idempotent exactly when a.a = 1."""
    rational_vectors = [
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1)),
        (Fraction(3, 5), Fraction(4, 5), Fraction(0)),
        (Fraction(-3, 5), Fraction(0), Fraction(4, 5)),
        (Fraction(1, 3), Fraction(2, 3), Fraction(2, 3)),
        (Fraction(1, 2), Fraction(1, 2), Fraction(0)),  # not a unit vector
        (Fraction(2, 7), Fraction(3, 7), Fraction(6, 7)),
    ]

    identity_ok = True
    for a in rational_vectors:
        for b in rational_vectors:
            tr = mtrace(mmul(projector(a), projector(b)))
            dot = sum(x * y for x, y in zip(a, b))
            want = (1 + dot) / 2
            if tr != (want, Fraction(0)):
                identity_ok = False

    # idempotency is equivalent to unit length, not assumed
    idem_ok = True
    for a in rational_vectors:
        P = projector(a)
        unit = sum(x * x for x in a) == 1
        if is_zero(msub(mmul(P, P), P)) != unit:
            idem_ok = False

    # control: the naive formula (1 + a.b)/4 must fail on a real case
    a = (Fraction(1), Fraction(0), Fraction(0))
    b = (Fraction(0), Fraction(1), Fraction(0))
    tr = mtrace(mmul(projector(a), projector(b)))[0]
    control_ok = tr == Fraction(1, 2) and tr != Fraction(1, 4)

    check(
        "C3 Clifford overlap Tr(P_a P_b) = (1 + a.b)/2; idempotent iff unit; wrong formula rejected",
        identity_ok and idem_ok and control_ok,
        f"checked {len(rational_vectors)**2} pairs exactly",
    )


# ---------------------------------------------------------------------------
# confusability
# ---------------------------------------------------------------------------


def norm2(v: Vec) -> int:
    return v[0] ** 2 + v[1] ** 2 + v[2] ** 2


def dot(v: Vec, w: Vec) -> int:
    return v[0] * w[0] + v[1] * w[1] + v[2] * w[2]


def overlap(v: Vec, w: Vec) -> Fraction:
    """Tr(P_v P_w), exact.

    Only defined here for representatives of equal length, where the
    normalization is a single rational divide.  The assertion is deliberate:
    an earlier draft of the C9 control mixed lengths and silently reported a
    wrong overlap.
    """
    assert norm2(v) == norm2(w), f"unequal representative lengths: {v}, {w}"
    return (1 + Fraction(dot(v, w), norm2(v))) / 2


def conf(points) -> Fraction:
    pts = sorted(points)
    best = None
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            o = overlap(pts[i], pts[j])
            if best is None or o > best:
                best = o
    return best


FACE = orbit((0, 0, 1))
CORNER = orbit((1, 1, 1))
EDGE = orbit((1, 1, 0))


def c4_named_orbits():
    vals = {"face": conf(FACE), "corner": conf(CORNER), "edge": conf(EDGE)}
    sizes = {"face": len(FACE), "corner": len(CORNER), "edge": len(EDGE)}
    ok = (
        vals["face"] == Fraction(1, 2)
        and vals["corner"] == Fraction(2, 3)
        and vals["edge"] == Fraction(3, 4)
        and sizes == {"face": 6, "corner": 8, "edge": 12}
    )
    check(
        "C4 mirror-locus orbit confusability: face 1/2, corner 2/3, edge 3/4",
        ok,
        f"{ {k: str(v) for k, v in vals.items()} }",
    )


def c5_quarter_turn_identity():
    """sum over the three coordinate quarter-turns of v . R_a v equals |v|^2.

    This is the mechanism behind the whole result: the three terms are the
    squared components, so one of them is at least |v|^2/3 -- and the term is
    unavailable as a *distinct* pair exactly when R_a v = v, which happens only
    on a four-fold axis.  That single exception is the face orbit.
    """
    identity_ok = True
    exception_ok = True
    for v in SCAN:
        terms = [dot(v, matvec(Q, v)) for Q in QUARTER_TURNS]
        if sum(terms) != norm2(v):
            identity_ok = False
        # the terms are exactly the squared components, in axis order
        if terms != [v[0] ** 2, v[1] ** 2, v[2] ** 2]:
            identity_ok = False
        # a quarter-turn fixes v iff v lies on that axis
        fixed = [matvec(Q, v) == v for Q in QUARTER_TURNS]
        if any(fixed) != is_face(v):
            exception_ok = False
    check(
        "C5 quarter-turn identity sum_a v.R_a v = |v|^2, fixed only on four-fold axes",
        identity_ok and exception_ok,
        f"{len(SCAN)} directions, exact",
    )


def c6_floor_and_saturator():
    floor_ok = True
    equality = []
    above_ok = True
    for o in ORBITS:
        c = conf(o)
        if c < Fraction(1, 2):
            floor_ok = False
        if c == Fraction(1, 2):
            equality.append(o)
        elif c < Fraction(2, 3):
            above_ok = False
    unique_ok = len(equality) == 1 and equality[0] == FACE

    # Unions of orbits.  conf is a max over pairs, so it is monotone under
    # adding points; that alone settles the union case against C6's per-orbit
    # result and is not machine-checked here because it is elementary.  What IS
    # checked is the exactly computable part: unions inside a single shell,
    # where cross-orbit overlaps are rational.  Those are the only unions whose
    # cross terms this runner can evaluate without leaving exact arithmetic.
    shells = {}
    for o in ORBITS:
        shells.setdefault(norm2(next(iter(o))), []).append(o)
    multi = {n: os_ for n, os_ in shells.items() if len(os_) > 1}
    union_ok = True
    union_seen = 0
    for n, os_ in multi.items():
        for i in range(len(os_)):
            for j in range(i + 1, len(os_)):
                u = os_[i] | os_[j]
                cu = conf(u)
                union_seen += 1
                if cu < max(conf(os_[i]), conf(os_[j])) or cu < Fraction(2, 3):
                    union_ok = False

    check(
        "C6 conf >= 1/2 for every invariant orbit; equality only for the face orbit; all others >= 2/3",
        floor_ok and unique_ok and above_ok and union_ok and union_seen > 0,
        f"{len(ORBITS)} orbits, unique saturator size "
        f"{len(equality[0]) if equality else 0}, {union_seen} same-shell unions checked",
    )


def c7_chirality_costs():
    """A chiral orbit is one whose inversion image is a disjoint orbit."""
    chiral, achiral = [], []
    for o in ORBITS:
        twin = frozenset(matvec(INVERSION, v) for v in o)
        (chiral if twin != o else achiral).append(o)

    size_ok = all(len(o) == 24 for o in chiral)
    gap_ok = all(conf(o) >= Fraction(2, 3) for o in chiral)
    named_achiral = FACE in achiral and CORNER in achiral and EDGE in achiral
    found_chiral = len(chiral) > 0

    # the strict separation the residual asked about
    separation_ok = all(conf(o) > conf(FACE) for o in chiral)

    check(
        "C7 every chiral orbit has size 24 and conf >= 2/3, strictly above the face orbit's 1/2",
        size_ok and gap_ok and named_achiral and found_chiral and separation_ok,
        f"{len(chiral)} chiral / {len(achiral)} achiral orbits in scan; "
        f"min chiral conf = {min((conf(o) for o in chiral), default='-')}",
    )


def c8_distinguishability():
    """Mutually distinguishable contents are pairwise antipodal, so at most two."""

    def max_distinguishable(o):
        pts = sorted(o)
        best = 1
        for v in pts:
            if tuple(-c for c in v) in o:
                best = 2
        # three pairwise-antipodal vectors would force v = u; confirm none exist
        for i in range(len(pts)):
            for j in range(i + 1, len(pts)):
                for k in range(j + 1, len(pts)):
                    trio = (pts[i], pts[j], pts[k])
                    if all(
                        overlap(x, y) == 0
                        for x in trio
                        for y in trio
                        if x != y
                    ):
                        return 3
        return best

    cap_ok = all(max_distinguishable(o) <= 2 for o in ORBITS)
    face_two = max_distinguishable(FACE) == 2
    # a chiral orbit contains no antipodal pair at all
    chiral = [
        o for o in ORBITS if frozenset(matvec(INVERSION, v) for v in o) != o
    ]
    chiral_none = all(max_distinguishable(o) == 1 for o in chiral)
    # the alphabet is at least six wide while distinguishable capacity is two
    width_ok = all(len(o) >= 6 for o in ORBITS)

    check(
        "C8 at most 2 mutually distinguishable contents per orbit; chiral orbits have none; width >= 6",
        cap_ok and face_two and chiral_none and width_ok,
        f"face={max_distinguishable(FACE)}, chiral orbits={len(chiral)}",
    )


def c9_controls():
    """The floor comes from cubic invariance, not from the sphere.

    Two witnesses beat 1/2, and both are too small to be invariant -- the
    smallest proper-cubic orbit has six elements (C2).  A third witness shows
    the *value* 1/2 is not itself special: a rotated frame attains it while
    being non-invariant.  So the theorem's content is that invariance forces
    the face orbit up to the cubic frame, not that 1/2 is unreachable
    otherwise.
    """
    # an antipodal pair: perfectly distinguishable, conf 0
    pair = [(0, 0, 1), (0, 0, -1)]
    pair_conf = conf(pair)

    # tetrahedral directions: four contents pairwise below the floor
    tet = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
    tet_conf = conf(tet)

    beats = pair_conf < Fraction(1, 2) and tet_conf == Fraction(1, 3)
    # neither can be cubic-invariant: both are smaller than the minimum orbit
    too_small = all(
        len(s) < min(len(o) for o in ORBITS) for s in (pair, tet)
    )
    not_invariant = all(
        orbit(s[0]) != frozenset(s) for s in (pair, tet)
    )
    # the tetrahedron is a non-invariant half of the corner orbit
    tet_in_corner = set(tet) < set(CORNER)

    # a rotated frame ties the floor without being invariant
    rot = [(0, 0, 5), (0, 0, -5), (3, 4, 0), (-3, -4, 0), (4, -3, 0), (-4, 3, 0)]
    rot_conf = conf(rot)
    ties = rot_conf == Fraction(1, 2) and orbit(rot[2]) != frozenset(rot)

    check(
        "C9 control: sub-orbit-size sets beat the floor; a rotated frame ties it; invariance is load-bearing",
        beats and too_small and not_invariant and tet_in_corner and ties,
        f"antipodal={pair_conf}, tetrahedral={tet_conf}, rotated frame={rot_conf}",
    )


def main() -> int:
    print("Cycle 705 - confusability floor of the first availability set")
    print("=" * 74)
    c1_group()
    c2_orbit_sizes()
    c3_clifford_overlap()
    c4_named_orbits()
    c5_quarter_turn_identity()
    c6_floor_and_saturator()
    c7_chirality_costs()
    c8_distinguishability()
    c9_controls()
    print("=" * 74)
    print(f"{len(PASSES)} PASS / {len(FAILURES)} FAIL")
    if FAILURES:
        for f in FAILURES:
            print(f"  FAILED: {f}")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())
