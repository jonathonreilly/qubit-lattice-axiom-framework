#!/usr/bin/env python3
"""Cycle 706 - census of flip-odd channels by lattice quotient and range.

Residual 2 of the landed bootstrap continuation:

    "Quotient-size thresholds: the `L = 2` parity protection suggests a graded
     family -- which odd channels first fire at which lattice quotients -- a
     possible tool for bounding rule chirality by locality range."
    -- BOOTSTRAP_CONTINUATION_..._2026-07-04, Residual 2

The landed result is for one specific channel at one range: `J2` vanishes
identically on the `L = 2` torus, so "direction-sensitive rule chirality needs
L >= 3".  This runner replaces that single data point with a census.

An "odd channel" is a function of the local configuration transforming by the
determinant character of the full cubic group -- the unique character that
distinguishes a configuration from its improper image.  The number of
independent odd channels is the multiplicity of that character in the
permutation representation on configurations:

    mult(det) = (1/48) sum over g of det(g) * Fix(g),

with `Fix(g)` the number of configurations g leaves alone.  This is a pure
character count: exact integer arithmetic, no sampling.

The census is run over two configuration types:

  occupancy      each window site is empty or occupied
  contented      each window site is empty or carries one of the six face
                 contents, which the group moves as polar vectors

Rows:

  K1  the cubic group acts on (Z/L)^3; order 48; 24 proper, 24 improper
  K2  L = 2 is special: inversion acts trivially on sites, and every odd
      occupancy channel vanishes at every range as a consequence
  K3  L = 4 is not special: inversion acts nontrivially, so the K2 mechanism
      is specific to L = 2 and not an even-L effect
  K4  the occupancy census over (L, r), and where the first channel fires
  K5  the contented census over (L, r) -- contents can carry oddness that
      occupancy cannot
  K6  Burnside cross-check: the trivial-character multiplicity equals the
      orbit count, computed independently
"""

from itertools import permutations, product

FAILURES = []
PASSES = []


def check(name: str, ok: bool, detail: str = "") -> None:
    (PASSES if ok else FAILURES).append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


# ---------------------------------------------------------------------------
# the full cubic group
# ---------------------------------------------------------------------------


def det3(A):
    return (
        A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
        - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
        + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    )


def signed_permutations():
    out = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            M = [[0, 0, 0] for _ in range(3)]
            for i in range(3):
                M[i][perm[i]] = signs[i]
            out.append(tuple(tuple(r) for r in M))
    return out


CUBIC = signed_permutations()
INVERSION = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))


def act_site(M, x, L):
    """The cubic action on (Z/L)^3."""
    return tuple(
        sum(M[i][k] * x[k] for k in range(3)) % L for i in range(3)
    )


def act_content(M, c):
    """Contents are polar vectors: the group moves them by the same matrix."""
    return tuple(sum(M[i][k] * c[k] for k in range(3)) for i in range(3))


FACE_CONTENTS = [
    (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1),
]


# ---------------------------------------------------------------------------
# windows on the torus
# ---------------------------------------------------------------------------


def torus_l1(x, L):
    return sum(min(c % L, (-c) % L) for c in x)


def window(L, r):
    """Sites of (Z/L)^3 within torus taxicab distance r of the origin.

    The torus taxicab metric is invariant under signed permutations, so the
    window is a union of group orbits -- required for the action below to be
    well defined.
    """
    return sorted(x for x in product(range(L), repeat=3) if torus_l1(x, L) <= r)


def site_cycles(M, W, L):
    """Number of cycles of the permutation g induces on the window."""
    idx = {x: i for i, x in enumerate(W)}
    seen = set()
    cycles = 0
    for x in W:
        if x in seen:
            continue
        cycles += 1
        y = x
        while y not in seen:
            seen.add(y)
            y = act_site(M, y, L)
            assert y in idx, "window is not closed under the group action"
    return cycles


def site_cycle_lengths(M, W, L):
    lengths = []
    seen = set()
    for x in W:
        if x in seen:
            continue
        n = 0
        y = x
        while y not in seen:
            seen.add(y)
            y = act_site(M, y, L)
            n += 1
        lengths.append(n)
    return lengths


# ---------------------------------------------------------------------------
# character counts
# ---------------------------------------------------------------------------


def fix_occupancy(M, W, L):
    """Configurations W -> {0,1} fixed by g: one free choice per site cycle."""
    return 2 ** site_cycles(M, W, L)


def fix_contented(M, W, L):
    """Configurations W -> {empty} U {six face contents} fixed by g.

    Around a site cycle of length n the value is determined by one site, and
    consistency requires that value to be fixed by M^n acting on contents.
    Empty is always consistent.
    """
    total = 1
    for n in site_cycle_lengths(M, W, L):
        Mn = M
        for _ in range(n - 1):
            Mn = tuple(
                tuple(sum(M[i][k] * Mn[k][j] for k in range(3)) for j in range(3))
                for i in range(3)
            )
        stable = sum(1 for c in FACE_CONTENTS if act_content(Mn, c) == c)
        total *= (1 + stable)  # empty, or a content fixed by M^n
    return total


def mult_det(W, L, fix):
    """Multiplicity of the determinant character; exact integer."""
    s = sum(det3(M) * fix(M, W, L) for M in CUBIC)
    assert s % 48 == 0, f"character sum {s} not divisible by 48"
    return s // 48


def mult_trivial(W, L, fix):
    s = sum(fix(M, W, L) for M in CUBIC)
    assert s % 48 == 0
    return s // 48


# ---------------------------------------------------------------------------
# rows
# ---------------------------------------------------------------------------


def k1_group():
    order_ok = len(CUBIC) == 48
    proper = [M for M in CUBIC if det3(M) == 1]
    improper = [M for M in CUBIC if det3(M) == -1]
    split_ok = len(proper) == 24 and len(improper) == 24
    # the action is well defined on every quotient used below
    action_ok = True
    for L in (2, 3, 4, 5):
        W = window(L, 1)
        for M in CUBIC:
            if any(act_site(M, x, L) not in set(W) for x in W):
                action_ok = False
    check(
        "K1 full cubic group of order 48 acts on (Z/L)^3, 24 proper / 24 improper",
        order_ok and split_ok and action_ok,
        f"|G|={len(CUBIC)}",
    )


def k2_l2_is_protected():
    """On L=2, inversion is trivial on sites, killing every odd occupancy channel."""
    L = 2
    sites = list(product(range(L), repeat=3))
    inversion_trivial = all(act_site(INVERSION, x, L) == x for x in sites)

    # the mechanism: every improper element acts exactly as its proper partner
    pairing_ok = True
    for M in CUBIC:
        if det3(M) == -1:
            partner = tuple(tuple(-c for c in row) for row in M)  # -M is proper
            if det3(partner) != 1:
                pairing_ok = False
            if any(act_site(M, x, L) != act_site(partner, x, L) for x in sites):
                pairing_ok = False

    # the consequence, computed independently at every available range
    ranges = [1, 2, 3]
    mults = {r: mult_det(window(L, r), L, fix_occupancy) for r in ranges}
    all_zero = all(v == 0 for v in mults.values())

    check(
        "K2 L=2: inversion acts trivially on sites, so every odd occupancy channel "
        "vanishes at every range",
        inversion_trivial and pairing_ok and all_zero,
        f"mult(det) by range {mults}",
    )


def k3_l4_is_not_special():
    """The K2 mechanism is about L=2, not about L being even."""
    L = 4
    sites = list(product(range(L), repeat=3))
    inversion_nontrivial = any(act_site(INVERSION, x, L) != x for x in sites)
    # and at least one improper element acts differently from its proper partner
    differs = False
    for M in CUBIC:
        if det3(M) == -1:
            partner = tuple(tuple(-c for c in row) for row in M)
            if any(act_site(M, x, L) != act_site(partner, x, L) for x in sites):
                differs = True
    check(
        "K3 L=4: inversion acts nontrivially, so the L=2 protection is not an even-L effect",
        inversion_nontrivial and differs,
        "-1 != 1 mod 4",
    )


OCC_TABLE = {}
CON_TABLE = {}


def k4_occupancy_census():
    rows = []
    for L in (2, 3, 4, 5):
        for r in (1, 2, 3):
            W = window(L, r)
            m = mult_det(W, L, fix_occupancy)
            OCC_TABLE[(L, r)] = (len(W), m)
            rows.append(f"L={L} r={r} |W|={len(W)} mult={m}")
    for line in rows:
        print("      " + line)

    l2_zero = all(OCC_TABLE[(2, r)][1] == 0 for r in (1, 2, 3))
    # the first quotient at which an odd occupancy channel exists
    firing = sorted(
        [(L, r) for (L, r), (_, m) in OCC_TABLE.items() if m > 0]
    )
    monotone_ok = True
    for L in (3, 4, 5):
        ms = [OCC_TABLE[(L, r)][1] for r in (1, 2, 3)]
        if any(b < a for a, b in zip(ms, ms[1:])):
            monotone_ok = False
    check(
        "K4 occupancy census computed over L in {2..5}, r in {1..3}; L=2 identically zero",
        l2_zero and monotone_ok,
        f"first firing (L,r) = {firing[0] if firing else 'none'}; "
        f"{len(firing)} of {len(OCC_TABLE)} cells nonzero",
    )


def k5_contented_census():
    rows = []
    for L in (2, 3, 4):
        for r in (1, 2):
            W = window(L, r)
            m = mult_det(W, L, fix_contented)
            CON_TABLE[(L, r)] = (len(W), m)
            rows.append(f"L={L} r={r} |W|={len(W)} mult={m}")
    for line in rows:
        print("      " + line)

    # contents can carry oddness where occupancy cannot: compare like for like
    strictly_richer = any(
        CON_TABLE[k][1] > OCC_TABLE[k][1] for k in CON_TABLE if k in OCC_TABLE
    )
    l2_contented = {r: CON_TABLE[(2, r)][1] for r in (1, 2)}
    check(
        "K5 contented census; contents carry oddness occupancy cannot",
        strictly_richer,
        f"L=2 contented mult by range {l2_contented}",
    )


def k6_burnside_crosscheck():
    """The trivial-character multiplicity must equal the orbit count."""
    ok = True
    detail = []
    for (L, r) in [(2, 1), (3, 1), (2, 2)]:
        W = window(L, r)
        idx = {x: i for i, x in enumerate(W)}
        # direct orbit count on occupancy configurations
        configs = list(product((0, 1), repeat=len(W)))
        seen = set()
        orbits = 0
        cset = set(configs)
        for cfg in configs:
            if cfg in seen:
                continue
            orbits += 1
            for M in CUBIC:
                img = [0] * len(W)
                for x in W:
                    img[idx[act_site(M, x, L)]] = cfg[idx[x]]
                t = tuple(img)
                assert t in cset
                seen.add(t)
        burnside = mult_trivial(W, L, fix_occupancy)
        detail.append(f"(L={L},r={r}) orbits={orbits} burnside={burnside}")
        if orbits != burnside:
            ok = False
    check(
        "K6 Burnside cross-check: trivial-character multiplicity equals the orbit count",
        ok,
        "; ".join(detail),
    )


def k7_nn_occupancy_is_achiral():
    """The mechanism behind the range-1 zero, checked directly.

    A permutation representation contains the determinant character exactly on
    those orbits whose point stabilizer contains no improper element.  So
    `mult(det) = 0` on the nearest-neighbour star is equivalent to: EVERY
    occupancy pattern of a site and its six neighbours has an improper
    symmetry.  That is checked here one configuration at a time, independently
    of the character sum, and a witness is exhibited.
    """
    L = 5  # any L >= 3 gives the same seven-site star
    W = window(L, 1)
    idx = {x: i for i, x in enumerate(W)}
    assert len(W) == 7

    def image(M, cfg):
        img = [0] * len(W)
        for x in W:
            img[idx[act_site(M, x, L)]] = cfg[idx[x]]
        return tuple(img)

    every_pattern_achiral = True
    witnesses = {}
    for cfg in product((0, 1), repeat=len(W)):
        improper_syms = [M for M in CUBIC if det3(M) == -1 and image(M, cfg) == cfg]
        if not improper_syms:
            every_pattern_achiral = False
            break
        witnesses[cfg] = improper_syms[0]

    # the equivalent character statement, computed the other way
    char_zero = mult_det(W, L, fix_occupancy) == 0

    # and the same star DOES carry oddness once contents are attached
    contented_nonzero = mult_det(W, L, fix_contented) > 0

    check(
        "K7 every nearest-neighbour occupancy pattern has an improper symmetry, so NN "
        "occupancy is achiral; contents on the same star are not",
        every_pattern_achiral and char_zero and contented_nonzero,
        f"{len(witnesses)} patterns each with an improper stabilizer element; "
        f"contented mult={mult_det(W, L, fix_contented)}",
    )


def make_fix_inert(k: int):
    """Sites carry empty or one of k INERT labels the group does not move.

    An earlier draft of this row assumed inert labels cannot carry oddness, on
    the reasoning that only position is left to carry it.  That is FALSE, and
    the runner caught it: distinguishability alone breaks improper symmetries.
    Label the three neighbours `+e1, +e2, +e3` with distinct labels and the
    mirror swapping `e1, e2` no longer fixes the configuration.  So the real
    graded parameter is alphabet richness, not whether contents transform.
    """

    def fix(M, W, L):
        total = 1
        for _ in site_cycle_lengths(M, W, L):
            total *= (1 + k)
        return total

    return fix


def k8_l2_oddness_is_content_carried():
    """At L=2 the only carrier left is the content transformation.

    L=2 kills position-carried oddness at every range (K2: inversion is
    trivial on sites).  Inert labels of ANY richness therefore cannot rescue
    it -- the group acts on nothing.  Polar-vector contents can, because the
    group still moves them.  That is a clean separation, and it holds only at
    L=2.
    """
    inert_l2 = {
        (k, r): mult_det(window(2, r), 2, make_fix_inert(k))
        for k in (1, 2, 6, 12)
        for r in (1, 2)
    }
    inert_all_zero = all(v == 0 for v in inert_l2.values())

    polar_l2 = {r: mult_det(window(2, r), 2, fix_contented) for r in (1, 2)}
    polar_nonzero = all(v > 0 for v in polar_l2.values())

    # the separation is specific to L=2: at L=3 inert labels do carry oddness
    inert_l3 = mult_det(window(3, 1), 3, make_fix_inert(6))
    separation_is_l2_only = inert_l3 > 0

    check(
        "K8 at L=2 oddness is exclusively content-carried: inert labels give zero at "
        "every richness and range, polar contents do not",
        inert_all_zero and polar_nonzero and separation_is_l2_only,
        f"inert L=2 all zero over k in {{1,2,6,12}}; polar L=2 {polar_l2}; "
        f"inert L=3 r=1 = {inert_l3}",
    )


def k9_alphabet_threshold_at_nn_range():
    """How rich must the alphabet be before the NN star carries an odd channel?

    Binary occupancy (k=1) is achiral on the star at every L (K7).  This row
    finds the smallest inert alphabet that is not, which is the sharp form of
    the range-1 statement.
    """
    L = 5  # any L >= 3: the star is the same seven sites
    W = window(L, 1)
    table = {k: mult_det(W, L, make_fix_inert(k)) for k in range(1, 7)}
    for k in sorted(table):
        print(f"      k={k} (alphabet {k+1} incl. empty)  mult={table[k]}")

    binary_zero = table[1] == 0
    firing = [k for k in sorted(table) if table[k] > 0]
    threshold = firing[0] if firing else None
    # once it fires it keeps firing
    monotone = all(
        table[a] <= table[b] for a, b in zip(sorted(table), sorted(table)[1:])
    )

    # Independent cross-check of the threshold value by a different method:
    # the det multiplicity equals the number of full-group orbits whose point
    # stabilizer contains no improper element.  Counted here directly on the
    # 3^7 configurations, with no character sum involved.
    idx = {x: i for i, x in enumerate(W)}

    def image(M, cfg):
        img = [0] * len(W)
        for x in W:
            img[idx[act_site(M, x, L)]] = cfg[idx[x]]
        return tuple(img)

    seen = set()
    chiral_orbits = 0
    for cfg in product(range(3), repeat=len(W)):  # empty + 2 labels
        if cfg in seen:
            continue
        orb = {image(M, cfg) for M in CUBIC}
        seen |= orb
        if not any(det3(M) == -1 and image(M, cfg) == cfg for M in CUBIC):
            chiral_orbits += 1
    direct_agrees = chiral_orbits == table[2]

    check(
        "K9 alphabet-richness threshold on the nearest-neighbour star, cross-checked by "
        "direct orbit-stabilizer counting",
        binary_zero and threshold is not None and monotone and direct_agrees,
        f"binary occupancy = 0; first nonzero at k={threshold} "
        f"(alphabet size {threshold+1} including empty), mult={table[2]}; "
        f"direct orbit count = {chiral_orbits}",
    )


def main() -> int:
    print("Cycle 706 - odd-channel census by lattice quotient and range")
    print("=" * 74)
    k1_group()
    k2_l2_is_protected()
    k3_l4_is_not_special()
    k4_occupancy_census()
    k5_contented_census()
    k6_burnside_crosscheck()
    k7_nn_occupancy_is_achiral()
    k8_l2_oddness_is_content_carried()
    k9_alphabet_threshold_at_nn_range()
    print("=" * 74)
    print(f"{len(PASSES)} PASS / {len(FAILURES)} FAIL")
    for f in FAILURES:
        print(f"  FAILED: {f}")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())
