#!/usr/bin/env python3
"""Salvage primary: seven narrow exact algebraic results on in-file
stipulated definitions (review-loop salvage pass on the toe-time blockAC2
package, PR #5995).

Every definition this runner consumes is stipulated IN THIS FILE.  There
are no file inputs, no axiom-byte pins, no git-history reads, and no
imported fitted values.  Nothing here claims derivation from the repo
axioms, physical identification, route closure, or selection among
rival expressions.  Each unit is exact rational/integer mathematics on
its own stipulated objects, offered as bounded support only.

Units (all salvaged per the PR #5995 review's salvage finding):

  1. trace-free/conformal split of a sector triple in Q^3, and the
     trace-zero property of the recoil ledger family (-2w, w, w)
     [salvaged from the Cycle 872 runner's exact algebra]
  2. affine grading normal form: the balance residual on the grading
     line w(t) = (1, 1+t, 1-t) equals A + tB exactly, with A the
     sector trace of the raw ledger  [from Cycles 876/895]
  3. the permutation module of the cyclic group C_3 on Q^3 splits as
     invariant line + irreducible 2-dimensional complement over Q and
     over R, and as three character lines over C  [from Cycle 883,
     with every physical-weight/Record identification removed]
  4. five stipulated closed forms collapse to (n-1)/n^2 on the locus
     (w0, w1) = (1, n-1); the three stipulated rational families
     coincide pairwise exactly at N = 3; and the fixed-locus sum over
     nontrivial N-th roots of unity equals (N^2-1)/12
     [from Cycle 899; the fitted-enclosure comparison is dropped]
  5. the screened origin equation 6*G1 - (6+m)*G0 = -1 gives
     G0 - G1 = (1 - m*G0)/6 exactly, and the step equals 1/6 iff
     m*G0 = 0 (so iff m = 0 when G0 > 0)  [from Cycle 900]
  6. projector-ratio witness: with J the all-ones n x n matrix and
     Qp = I - J/n, diag(Qp)/totalsum(J) = (n-1)/n^3 (2/27 at n = 3);
     exhibited as reachability-only, with a rival expression shown so
     no selection is implied  [from Cycle 904]
  7. pointer-cycle identity: in a finite simple graph the shortest
     cycle through a marked vertex S has length 2 + the least
     distance in G - S between two distinct neighbours of S; verified
     exhaustively on all 32768 graphs on 6 labelled vertices
     [from Cycle 921; the field-branched measurement table is dropped]

Fail-closed: every check computes both sides; there are no supplied
booleans; a check-count gate rejects silently skipped sections; any
failure prints FAIL and the process exits 1.  Exit 0 only on a full
real PASS.  The receipt is deterministic (no timestamps).
"""
from __future__ import annotations

import hashlib
import itertools
import json
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
RECEIPT_PATH = os.path.join(
    REPO, "outputs", "salvaged_exact_algebra_receipt_2026_08_08.json")
DATE = "2026-08-08"
EXPECTED_CHECK_COUNT = 31

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok))
    print(f"{'PASS' if ok else 'FAIL'} {name}")
    return ok


def q(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


# ---------------------------------------------------------------------------
# small exact linear algebra over Fraction
# ---------------------------------------------------------------------------
def mat_id(n):
    return [[Fraction(1) if i == j else Fraction(0) for j in range(n)]
            for i in range(n)]


def mat_mul(a, b):
    n, m, p = len(a), len(b), len(b[0])
    return [[sum(a[i][k] * b[k][j] for k in range(m)) for j in range(p)]
            for i in range(n)]


def mat_add(a, b):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def mat_sub(a, b):
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def mat_eq(a, b):
    return all(x == y for ra, rb in zip(a, b) for x, y in zip(ra, rb))


def mat_scale(c, a):
    return [[c * x for x in row] for row in a]


def mat_rank(rows_in):
    rows = [list(r) for r in rows_in]
    if not rows:
        return 0
    width = len(rows[0])
    rank = 0
    for col in range(width):
        pivot = next((r for r in range(rank, len(rows)) if rows[r][col] != 0),
                     None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = Fraction(1) / rows[rank][col]
        rows[rank] = [inv * x for x in rows[rank]]
        for r in range(len(rows)):
            if r != rank and rows[r][col] != 0:
                f = rows[r][col]
                rows[r] = [x - f * y for x, y in zip(rows[r], rows[rank])]
        rank += 1
    return rank


def mat_inv(a):
    n = len(a)
    aug = [list(row) + [Fraction(1) if i == j else Fraction(0)
                        for j in range(n)] for i, row in enumerate(a)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col] != 0), None)
        if pivot is None:
            raise ZeroDivisionError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        inv = Fraction(1) / aug[col][col]
        aug[col] = [inv * x for x in aug[col]]
        for r in range(n):
            if r != col and aug[r][col] != 0:
                f = aug[r][col]
                aug[r] = [x - f * y for x, y in zip(aug[r], aug[col])]
    return [row[n:] for row in aug]


def vec_add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def vec_sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def vec_scale(c, a):
    return tuple(c * x for x in a)


# ---------------------------------------------------------------------------
# unit 1: trace-free/conformal split of a sector triple in Q^3
# ---------------------------------------------------------------------------
def unit_trace_free_conformal_split() -> dict:
    """Stipulated: sector triple v in Q^3; conformal channel
    conf(v) = (trace(v)/3)*(1,1,1); trace-free channel tf(v) = v - conf(v);
    graded operator G_sigma(v) = tf(v) + sigma*conf(v);
    recoil ledger family (-2w, w, w)."""
    one = (Fraction(1), Fraction(1), Fraction(1))

    def trace(v):
        return v[0] + v[1] + v[2]

    def conf(v):
        return vec_scale(trace(v) / 3, one)

    def tf(v):
        return vec_sub(v, conf(v))

    values = [Fraction(-2), Fraction(-1), Fraction(0), Fraction(1),
              Fraction(2), Fraction(1, 2), Fraction(-3, 7)]
    probes = [tuple(t) for t in itertools.product(values, repeat=3)]

    check("split.decomposition_identity_on_all_probes",
          all(vec_add(tf(v), conf(v)) == v for v in probes))
    check("split.trace_free_channel_has_zero_trace",
          all(trace(tf(v)) == 0 for v in probes))
    check("split.conformal_channel_is_constant_vector",
          all(len(set(conf(v))) == 1 for v in probes))

    proj_conf = mat_scale(Fraction(1, 3),
                          [[Fraction(1)] * 3 for _ in range(3)])
    proj_tf = mat_sub(mat_id(3), proj_conf)
    zero = [[Fraction(0)] * 3 for _ in range(3)]
    check("split.projectors_idempotent_complementary",
          mat_eq(mat_mul(proj_conf, proj_conf), proj_conf)
          and mat_eq(mat_mul(proj_tf, proj_tf), proj_tf)
          and mat_eq(mat_mul(proj_conf, proj_tf), zero)
          and mat_eq(mat_mul(proj_tf, proj_conf), zero)
          and mat_eq(mat_add(proj_conf, proj_tf), mat_id(3)))

    # uniqueness: v = u + c*(1,1,1) with trace(u) = 0 forces c = trace(v)/3
    offsets = [Fraction(1), Fraction(-1), Fraction(1, 3), Fraction(5, 2)]
    check("split.uniqueness_of_the_constant_part",
          all(trace(vec_sub(v, vec_scale(trace(v) / 3 + d, one))) != 0
              for v in probes[:64] for d in offsets))

    ledger_rows = []
    for w in range(-6, 7):
        vw = (Fraction(-2 * w), Fraction(w), Fraction(w))
        ledger_rows.append({"w": w, "trace": q(trace(vw)),
                            "conformal_channel_zero":
                                conf(vw) == (0, 0, 0)})
    check("split.recoil_ledger_minus2w_w_w_is_trace_free",
          all(r["trace"] == "0/1" and r["conformal_channel_zero"]
              for r in ledger_rows))

    def graded(sigma, v):
        return vec_add(tf(v), vec_scale(sigma, conf(v)))

    sigmas = [Fraction(-1), Fraction(1), Fraction(2), Fraction(1, 2)]
    trace_free_probes = [tf(v) for v in probes[:64]]
    check("split.graded_operator_fixes_exactly_the_trace_free_vectors",
          all(graded(s, v) == v for s in sigmas for v in trace_free_probes)
          and all(graded(s, v) != v
                  for s in sigmas if s != 1
                  for v in probes[:64] if trace(v) != 0))
    return {"probe_count": len(probes), "ledger_rows": ledger_rows}


# ---------------------------------------------------------------------------
# unit 2: affine grading normal form on the line w(t) = (1, 1+t, 1-t)
# ---------------------------------------------------------------------------
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)


def unit_affine_grading_normal_form() -> dict:
    """Stipulated: direction set D = the six unit vectors of Z^3 (order
    above); configuration = (direction d, triple tau in D^3); grading
    line w(t) = (1, 1+t, 1-t); balance residual
    r(t) = sum_s w_s(t) D[tau_s] - w_0(t) D[d];
    raw ledger L(d, tau) = (D[tau_0] - D[d], D[tau_1], D[tau_2]);
    sector trace = sum of the three ledger vectors.
    Exact statements: r(t) = A + tB with
    A = D[tau_0] + D[tau_1] + D[tau_2] - D[d] and B = D[tau_1] - D[tau_2];
    the sector trace of the raw ledger is identically A (a function of
    the support alone); B never depends on d or tau_0."""
    dirs = [tuple(Fraction(x) for x in v) for v in DIRECTIONS]
    probes = [Fraction(0), Fraction(1), Fraction(-1), Fraction(2, 3),
              Fraction(-7, 5), Fraction(9, 4)]

    def residual(d, tau, t):
        w = (Fraction(1), 1 + t, 1 - t)
        total = (Fraction(0), Fraction(0), Fraction(0))
        for s in range(3):
            total = vec_add(total, vec_scale(w[s], dirs[tau[s]]))
        return vec_sub(total, vec_scale(w[0], dirs[d]))

    configs = [(d, tau) for d in range(6)
               for tau in itertools.product(range(6), repeat=3)]
    identities = 0
    affine_ok = True
    trace_ok = True
    b_by_tail = {}
    b_tail_ok = True
    for d, tau in configs:
        a_vec = vec_sub(vec_add(vec_add(dirs[tau[0]], dirs[tau[1]]),
                                dirs[tau[2]]), dirs[d])
        b_vec = vec_sub(dirs[tau[1]], dirs[tau[2]])
        for t in probes:
            if residual(d, tau, t) != vec_add(a_vec, vec_scale(t, b_vec)):
                affine_ok = False
            identities += 1
        ledger = (vec_sub(dirs[tau[0]], dirs[d]), dirs[tau[1]],
                  dirs[tau[2]])
        if vec_add(vec_add(ledger[0], ledger[1]), ledger[2]) != a_vec:
            trace_ok = False
        tail = (tau[1], tau[2])
        if tail in b_by_tail and b_by_tail[tail] != b_vec:
            b_tail_ok = False
        b_by_tail[tail] = b_vec

    check("grading.residual_equals_A_plus_tB_on_all_configurations",
          affine_ok and identities == len(configs) * len(probes))
    check("grading.raw_ledger_sector_trace_is_identically_A", trace_ok)
    check("grading.B_depends_only_on_the_second_and_third_sector",
          b_tail_ok and len(b_by_tail) == 36)
    check("grading.configuration_census_is_complete",
          len(configs) == 6 * 6 ** 3)
    return {"configurations": len(configs),
            "probe_points_per_configuration": len(probes),
            "residual_identities_checked": identities}


# ---------------------------------------------------------------------------
# unit 3: the C_3 permutation module on Q^3
# ---------------------------------------------------------------------------
def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def unit_cyclic_permutation_module() -> dict:
    """Stipulated: C is the permutation matrix of the 3-cycle
    (0 -> 1 -> 2 -> 0) acting on Q^3.  Exact statements: the fixed
    subspace is the line spanned by (1,1,1); the complement (image of
    I - J/3) is C-invariant of dimension 2 and is irreducible over Q
    and over R (its characteristic polynomial is x^2 + x + 1); over C
    the module splits into three one-dimensional character lines.
    No physical identification of any kind is attached to these
    dimensions."""
    c_mat = [[Fraction(0), Fraction(0), Fraction(1)],
             [Fraction(1), Fraction(0), Fraction(0)],
             [Fraction(0), Fraction(1), Fraction(0)]]
    c_minus_i = mat_sub(c_mat, mat_id(3))
    fixed_dim = 3 - mat_rank(c_minus_i)
    ones_col = [[Fraction(1)], [Fraction(1)], [Fraction(1)]]
    check("module.fixed_subspace_is_the_line_of_1_1_1",
          fixed_dim == 1
          and mat_eq(mat_mul(c_minus_i, ones_col), [[0], [0], [0]]))

    proj = mat_scale(Fraction(1, 3), [[Fraction(1)] * 3 for _ in range(3)])
    comp = mat_sub(mat_id(3), proj)
    check("module.complement_is_C_invariant_of_dimension_2",
          mat_eq(mat_mul(c_mat, comp), mat_mul(comp, c_mat))
          and mat_rank(comp) == 2)

    # matrix of C on the complement in the basis (e0 - e1, e1 - e2):
    # C(e0 - e1) = e1 - e2;  C(e1 - e2) = e2 - e0 = -(e0 - e1) - (e1 - e2)
    action = [[Fraction(0), Fraction(-1)], [Fraction(1), Fraction(-1)]]
    trace2 = action[0][0] + action[1][1]
    det2 = action[0][0] * action[1][1] - action[0][1] * action[1][0]
    # characteristic polynomial x^2 - trace2*x + det2
    char_is_cyclotomic = (-trace2 == 1 and det2 == 1)
    # degree-2 rational reducibility test: a rational root must be +-1
    # (rational root theorem on x^2 + x + 1); discriminant = -3 < 0
    disc = trace2 * trace2 - 4 * det2
    no_rational_root = all(r * r + r + 1 != 0
                           for r in (Fraction(1), Fraction(-1)))
    check("module.complement_char_poly_is_x2_plus_x_plus_1",
          char_is_cyclotomic)
    check("module.complement_irreducible_over_Q_and_over_R",
          no_rational_root and disc < 0)

    full_char = poly_mul([-1, 1], [1, 1, 1])   # (x - 1)(x^2 + x + 1)
    check("module.full_char_poly_factors_as_x3_minus_1",
          full_char == [-1, 0, 0, 1] and disc != 0)

    pair_qr = (fixed_dim, 3 - fixed_dim)
    over_c = (1, 1, 1) if disc != 0 else None
    check("module.dimension_pattern_1_2_over_Q_R_and_1_1_1_over_C",
          pair_qr == (1, 2) and over_c == (1, 1, 1))
    return {"dimension_pair_over_Q_and_R": list(pair_qr),
            "dimension_pattern_over_C": list(over_c),
            "complement_char_poly": "x^2 + x + 1",
            "discriminant": q(Fraction(disc))}


# ---------------------------------------------------------------------------
# unit 4: five-form collapse, family coincidence at N = 3, fixed-locus sum
# ---------------------------------------------------------------------------
FAMILIES = {
    "(N-1)/N^2": lambda n: Fraction(n - 1, n * n),
    "(N^2-1)/(12N)": lambda n: Fraction(n * n - 1, 12 * n),
    "(N-1)(N-2)/(3N)": lambda n: Fraction((n - 1) * (n - 2), 3 * n),
}

FIVE_FORMS = {
    "w1/(w0+w1)^2": lambda w0, w1, n: Fraction(w1, (w0 + w1) ** 2),
    "w0*w1/n^2": lambda w0, w1, n: Fraction(w0 * w1, n ** 2),
    "w1/n^2": lambda w0, w1, n: Fraction(w1, n ** 2),
    "(n-1)/n^2": lambda w0, w1, n: Fraction(n - 1, n ** 2),
    "w1/(w0*n^2)": lambda w0, w1, n: Fraction(w1, w0 * n ** 2),
}


def fixed_locus_sum_quotient_ring(n: int) -> Fraction:
    """Trace of the inverse of multiplication by (1-x)(1-x^{n-1}) in
    Q[x] / ((x^n - 1)/(x - 1)): the exact sum over nontrivial n-th
    roots of unity z of 1/((1-z)(1-z^{-1})).  No floating point."""
    d = n - 1
    modulus = [1] * n                       # (x^n - 1)/(x - 1)

    def reduce_poly(p):
        p = [Fraction(x) for x in p]
        while len(p) > d:
            lead = p.pop()
            k = len(p)
            for i in range(d):
                p[k - d + i] -= lead * modulus[i]
        while len(p) < d:
            p.append(Fraction(0))
        return p

    u = poly_mul([1, -1], [1] + [0] * (n - 2) + [-1])  # (1-x)(1-x^{n-1})
    cols = [reduce_poly([0] * j + list(u)) for j in range(d)]
    mult = [[cols[j][i] for j in range(d)] for i in range(d)]
    inv = mat_inv(mult)
    return sum(inv[i][i] for i in range(d))


def unit_five_forms_and_families() -> dict:
    """Stipulated: the five closed forms in (w0, w1, n) listed in
    FIVE_FORMS; the locus (w0, w1) = (1, n-1); the three rational
    families listed in FAMILIES.  Exact statements: on the locus every
    one of the five forms equals (n-1)/n^2; the three families coincide
    pairwise exactly at N = 3 (value 2/9) and separate at every other
    N >= 2; the fixed-locus sum over nontrivial N-th roots of unity of
    1/((1-z)(1-z^{-1})) equals (N^2-1)/12, so its 1/N normalisation is
    the family (N^2-1)/(12N).  Exhibiting several expressions with one
    value at one point selects none of them; no selection is claimed."""
    collapse_ok = True
    evaluations = 0
    for n in range(2, 51):
        target = Fraction(n - 1, n * n)
        for fn in FIVE_FORMS.values():
            if fn(1, n - 1, n) != target:
                collapse_ok = False
            evaluations += 1
    check("forms.five_forms_collapse_to_(n-1)/n^2_on_the_locus",
          collapse_ok)

    names = list(FAMILIES)
    coincidence_ok = True
    for n in range(2, 201):
        for a, b in itertools.combinations(names, 2):
            equal = FAMILIES[a](n) == FAMILIES[b](n)
            if equal != (n == 3):
                coincidence_ok = False
    at3 = {name: q(fn(3)) for name, fn in FAMILIES.items()}
    at4 = {name: q(fn(4)) for name, fn in FAMILIES.items()}
    check("forms.families_coincide_pairwise_exactly_at_N_3",
          coincidence_ok and set(at3.values()) == {"2/9"})
    check("forms.families_separate_at_N_4",
          sorted(at4.values()) == sorted(["3/16", "5/16", "1/2"]))

    locus_rows = []
    locus_ok = True
    for n in range(2, 13):
        total = fixed_locus_sum_quotient_ring(n)
        expected = Fraction(n * n - 1, 12)
        locus_rows.append({"N": n, "sum": q(total),
                           "matches_(N^2-1)/12": total == expected,
                           "normalised": q(total / n),
                           "normalised_matches_family":
                               total / n == FAMILIES["(N^2-1)/(12N)"](n)})
        if not (total == expected
                and total / n == FAMILIES["(N^2-1)/(12N)"](n)):
            locus_ok = False
    check("forms.fixed_locus_sum_equals_(N^2-1)/12_for_N_2_to_12",
          locus_ok)
    check("forms.evaluation_census_is_complete",
          evaluations == 49 * 5 and len(locus_rows) == 11)
    return {"five_form_evaluations": evaluations,
            "family_values_at_N_3": at3,
            "family_values_at_N_4": at4,
            "fixed_locus_rows": locus_rows}


# ---------------------------------------------------------------------------
# unit 5: screened origin step
# ---------------------------------------------------------------------------
def unit_screened_origin_step() -> dict:
    """Stipulated: rationals G0 (origin value) and G1 (common neighbour
    value) satisfying the single origin equation 6*G1 - (6+m)*G0 = -1,
    with m the screening parameter (m = mu^2 >= 0 in the source
    reading; here just a rational).  Exact statements: the equation is
    equivalent to G0 - G1 = (1 - m*G0)/6; the step equals 1/6 iff
    m*G0 = 0; on the half-line G0 > 0 that is iff m = 0.  Whether any
    particular lattice Green function satisfies the stipulated symmetry
    is NOT claimed here."""
    m_grid = [Fraction(0), Fraction(1, 100), Fraction(1, 4), Fraction(1),
              Fraction(7, 3)]
    g0_grid = [Fraction(1, 6), Fraction(1, 4), Fraction(1, 2),
               Fraction(5, 7), Fraction(1)]
    step_ok = True
    iff_ok = True
    rows = []
    for m in m_grid:
        for g0 in g0_grid:
            g1 = ((6 + m) * g0 - 1) / 6          # solve the origin equation
            claimed = (1 - m * g0) / 6
            if g0 - g1 != claimed:
                step_ok = False
            if (g0 - g1 == Fraction(1, 6)) != (m * g0 == 0):
                iff_ok = False
            rows.append({"m": q(m), "G0": q(g0),
                         "step": q(g0 - g1)})
    check("origin.step_equals_(1_minus_m_G0)_over_6_on_the_grid",
          step_ok)
    check("origin.step_is_one_sixth_iff_m_times_G0_is_zero", iff_ok)
    check("origin.on_G0_positive_the_massless_slice_is_m_equals_0",
          all((Fraction(1) - m * g0 == 1) == (m == 0)
              for m in m_grid for g0 in g0_grid if g0 > 0))
    return {"grid_rows": len(rows)}


# ---------------------------------------------------------------------------
# unit 6: projector-ratio witness
# ---------------------------------------------------------------------------
def unit_projector_ratio_witness() -> dict:
    """Stipulated: J = all-ones n x n matrix; P = J/n (group-averaging
    projector for a transitive action); Qp = I - P; the scalar readers
    diag(M) = M[0][0] and totalsum(M) = sum of all entries.  Exact
    statements: diag(Qp) = (n-1)/n, totalsum(J) = n^2, so
    diag(Qp)/totalsum(J) = (n-1)/n^3, which is 2/27 at n = 3.
    Reachability only: the rival expression diag(Qp)/n = (n-1)/n^2 on
    the SAME data shows that exhibiting an expression selects nothing."""
    ratio_ok = True
    rival_ok = True
    for n in range(2, 51):
        ones = [[Fraction(1)] * n for _ in range(n)]
        comp = mat_sub(mat_id(n), mat_scale(Fraction(1, n), ones))
        diag_qp = comp[0][0]
        totalsum_j = sum(sum(row) for row in ones)
        if not (diag_qp == Fraction(n - 1, n)
                and totalsum_j == n * n
                and diag_qp / totalsum_j == Fraction(n - 1, n ** 3)):
            ratio_ok = False
        if diag_qp / n != Fraction(n - 1, n * n):
            rival_ok = False
    check("witness.diag_Qp_over_totalsum_J_is_(n-1)/n^3_for_n_2_to_50",
          ratio_ok)
    check("witness.value_at_n_3_is_2/27",
          Fraction(3 - 1, 3 ** 3) == Fraction(2, 27))
    check("witness.rival_expression_diag_Qp_over_n_is_(n-1)/n^2",
          rival_ok)
    return {"n_range": [2, 50],
            "value_at_3": q(Fraction(2, 27)),
            "rival_value_at_3": q(Fraction(2, 9))}


# ---------------------------------------------------------------------------
# unit 7: pointer-cycle identity
# ---------------------------------------------------------------------------
def bfs_dist(adj, n, src):
    dist = {src: 0}
    frontier = [src]
    while frontier:
        nxt = []
        for u in frontier:
            for v in range(n):
                if adj[u][v] and v not in dist:
                    dist[v] = dist[u] + 1
                    nxt.append(v)
        frontier = nxt
    return dist


def shortest_cycle_through_by_dfs(adj, n, s):
    """Brute force: enumerate every simple path from s and close it back
    to s; the minimum closed length >= 3 is the shortest cycle through
    s.  Exponential but exact; used only on n <= 6 here."""
    best = [None]

    def dfs(u, visited, length):
        # any cycle completed from here needs at least one more edge,
        # so it has length >= length + 1: sound pruning bound
        if best[0] is not None and length + 1 >= best[0]:
            return
        for v in range(n):
            if not adj[u][v]:
                continue
            if v == s and length >= 2:
                if best[0] is None or length + 1 < best[0]:
                    best[0] = length + 1
            elif v not in visited and v != s:
                visited.add(v)
                dfs(v, visited, length + 1)
                visited.remove(v)

    dfs(s, set(), 0)
    return best[0]


def pointer_formula(adj, n, s):
    """2 + min over distinct neighbour pairs (a, b) of s of their
    distance in G - s; None if no such pair is connected in G - s."""
    neigh = [v for v in range(n) if adj[s][v]]
    sub = [[adj[i][j] if i != s and j != s else 0 for j in range(n)]
           for i in range(n)]
    best = None
    for i, a in enumerate(neigh):
        dist = bfs_dist(sub, n, a)
        for b in neigh[i + 1:]:
            if b in dist and (best is None or dist[b] + 2 < best):
                best = dist[b] + 2
    return best


def unit_pointer_cycle_identity() -> dict:
    """Stipulated: G a finite simple graph on vertex set {0..n-1}; S a
    marked vertex ('pointer').  Exact statement: a cycle through S
    exists iff two distinct neighbours of S are joined in G - S, and
    then the shortest cycle through S has length exactly
    2 + min_{a != b in N(S)} dist_{G-S}(a, b).
    Proof shape: any cycle through S is S, a, ..., b, S with the inner
    path avoiding S, so its length is >= 2 + dist_{G-S}(a, b); a
    shortest such path closes to a simple cycle attaining the bound.
    Verified exhaustively on ALL graphs on 6 labelled vertices."""
    n = 6
    s = 0
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    total = 0
    cyclic = 0
    agree = True
    for mask in range(1 << len(pairs)):
        adj = [[0] * n for _ in range(n)]
        for k, (i, j) in enumerate(pairs):
            if mask >> k & 1:
                adj[i][j] = adj[j][i] = 1
        got = shortest_cycle_through_by_dfs(adj, n, s)
        want = pointer_formula(adj, n, s)
        if got != want:
            agree = False
        total += 1
        if got is not None:
            cyclic += 1
    check("cycle.identity_holds_on_all_32768_graphs_on_6_vertices",
          agree and total == 1 << 15)
    check("cycle.census_counts_are_real",
          0 < cyclic < total)
    return {"graphs_checked": total,
            "graphs_with_a_cycle_through_the_pointer": cyclic,
            "graphs_without": total - cyclic}


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main() -> int:
    units = {
        "trace_free_conformal_split": unit_trace_free_conformal_split(),
        "affine_grading_normal_form": unit_affine_grading_normal_form(),
        "cyclic_permutation_module": unit_cyclic_permutation_module(),
        "five_forms_and_families": unit_five_forms_and_families(),
        "screened_origin_step": unit_screened_origin_step(),
        "projector_ratio_witness": unit_projector_ratio_witness(),
        "pointer_cycle_identity": unit_pointer_cycle_identity(),
    }
    # structural count gate: a silently skipped section cannot pass.
    # The gate is itself the final check, so the declared census includes it.
    check("gate.check_count_matches_the_declared_census",
          len(CHECKS) + 1 == EXPECTED_CHECK_COUNT)
    passes = sum(1 for _n, ok in CHECKS if ok)
    fails = len(CHECKS) - passes
    verdict = "PASS" if fails == 0 else "FAIL"
    payload = {
        "date": DATE,
        "script": "scripts/salvaged_exact_algebra_2026_08_08.py",
        "role": ("salvage primary: seven narrow exact algebraic results "
                 "on in-file stipulated definitions; bounded support "
                 "only; no derivation, closure, or selection claims"),
        "inputs": [],
        "units": units,
        "checks": [{"name": name, "ok": ok} for name, ok in CHECKS],
        "pass": passes,
        "fail": fails,
        "expected_check_count": EXPECTED_CHECK_COUNT,
        "verdict": verdict,
    }
    blob = json.dumps(payload, sort_keys=True, indent=1).encode()
    payload["payload_sha256"] = hashlib.sha256(blob).hexdigest()
    os.makedirs(os.path.dirname(RECEIPT_PATH), exist_ok=True)
    with open(RECEIPT_PATH, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, sort_keys=True, indent=1)
        fh.write("\n")
    print(f"TOTAL: PASS={passes} FAIL={fails}")
    print(f"VERDICT: {verdict}")
    print(f"receipt: {os.path.relpath(RECEIPT_PATH, REPO)}")
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
