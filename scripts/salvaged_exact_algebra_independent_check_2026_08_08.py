#!/usr/bin/env python3
"""Salvage independent check for the seven exact algebraic units of
`scripts/salvaged_exact_algebra_2026_08_08.py` (PR #5995 salvage pass).

Every unit is recomputed HERE by a different exact route than the
primary used; no gate takes an author-supplied boolean and no route
reuses the primary's computation:

  1. trace-free/conformal split  -> Reynolds group-averaging route:
     the conformal projector is rebuilt as (I + C + C^2)/3 for the
     3-cycle C, not stipulated as J/3
  2. affine grading normal form  -> two-point interpolation route:
     A' = r(0), B' = r(1) - r(0), verified against the definitional
     A, B and at two fresh probe points the primary never used
  3. C_3 permutation module      -> character-theory route with exact
     arithmetic in Z[w]/(w^2 + w + 1)
  4. five-form collapse          -> polynomial-identity route (cross-
     multiplied integer polynomials, no numeric sweep); family
     coincidence -> integer root extraction from the difference
     numerators; fixed-locus sum -> cycle-Laplacian pseudoinverse
     route Tr((L + J/N)^{-1}) - 1
  5. screened origin step        -> exact bivariate polynomial
     elimination in (m, G0)
  6. projector-ratio witness     -> circulant/trace route
     (equal diagonal + trace = n - 1)
  7. pointer-cycle identity      -> edge-removal BFS route on all 1024
     graphs on 5 vertices, 200 seeded 8-vertex graphs, AND the full
     32768-graph 6-vertex census recomputed independently

It then verifies the committed primary receipt fail-closed and
full-surface: the file must exist, its embedded digest must
recompute, and the ENTIRE payload (every unit field, every check row,
the counts, the verdict, and the pinned declared-design constants)
must equal a canonical expected record assembled from this checker's
seven independent routes.  Two tamper regressions are executed on
every run: a byte tamper without rehash must break the digest, and
the same semantic tamper WITH a recomputed self-digest must still be
rejected by the full-payload comparison.  Any miss prints FAIL and
exits 1.
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
PRIMARY_RECEIPT = os.path.join(
    REPO, "outputs", "salvaged_exact_algebra_receipt_2026_08_08.json")
RECEIPT_PATH = os.path.join(
    REPO, "outputs",
    "salvaged_exact_algebra_independent_check_receipt_2026_08_08.json")
DATE = "2026-08-08"
EXPECTED_CHECK_COUNT = 27

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok))
    print(f"{'PASS' if ok else 'FAIL'} {name}")
    return ok


def q(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def mat_id(n):
    return [[Fraction(1) if i == j else Fraction(0) for j in range(n)]
            for i in range(n)]


def mat_mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def mat_add(a, b):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def mat_sub(a, b):
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def mat_eq(a, b):
    return all(x == y for ra, rb in zip(a, b) for x, y in zip(ra, rb))


def mat_scale(c, a):
    return [[c * x for x in row] for row in a]


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
# unit 1 via the Reynolds group average
# ---------------------------------------------------------------------------
def check_split_by_reynolds() -> dict:
    c_mat = [[Fraction(0), Fraction(0), Fraction(1)],
             [Fraction(1), Fraction(0), Fraction(0)],
             [Fraction(0), Fraction(1), Fraction(0)]]
    c2 = mat_mul(c_mat, c_mat)
    reynolds = mat_scale(Fraction(1, 3),
                         mat_add(mat_add(mat_id(3), c_mat), c2))
    ones_third = mat_scale(Fraction(1, 3),
                           [[Fraction(1)] * 3 for _ in range(3)])
    check("reynolds.group_average_equals_the_conformal_projector",
          mat_eq(reynolds, ones_third)
          and mat_eq(mat_mul(reynolds, reynolds), reynolds))

    comp = mat_sub(mat_id(3), reynolds)
    ledger_ok = True
    ledger_rows = []
    for w in range(-6, 7):
        v = [[Fraction(-2 * w)], [Fraction(w)], [Fraction(w)]]
        avg = mat_mul(reynolds, v)
        if any(row[0] != 0 for row in avg):
            ledger_ok = False
        if mat_mul(comp, v) != v:
            ledger_ok = False
        # Reynolds route: P(v) = (trace/3)*(1,1,1), so trace = 3*(Pv)[0]
        trace = 3 * avg[0][0]
        ledger_rows.append({"w": w, "trace": q(trace),
                            "conformal_channel_zero":
                                all(row[0] == 0 for row in avg)})
    check("reynolds.recoil_ledger_is_annihilated_by_the_group_average",
          ledger_ok)

    values = [Fraction(-2), Fraction(0), Fraction(1), Fraction(1, 2),
              Fraction(-3, 7)]
    graded_ok = True
    for v in itertools.product(values, repeat=3):
        col = [[x] for x in v]
        tf = mat_mul(comp, col)
        cf = mat_mul(reynolds, col)
        for s in (Fraction(-1), Fraction(2), Fraction(1, 2)):
            g = mat_add(tf, mat_scale(s, cf))
            fixes = mat_eq(g, col)
            trace_zero = (v[0] + v[1] + v[2] == 0)
            if fixes != trace_zero:
                graded_ok = False
    check("reynolds.graded_operator_fixes_exactly_the_averaged_out_vectors",
          graded_ok)
    return {"probe_count": len(values) ** 3,
            "ledger_rows_recomputed": ledger_rows}


# ---------------------------------------------------------------------------
# unit 2 via two-point interpolation
# ---------------------------------------------------------------------------
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)


def check_grading_by_interpolation() -> dict:
    dirs = [tuple(Fraction(x) for x in v) for v in DIRECTIONS]

    def residual(d, tau, t):
        w = (Fraction(1), 1 + t, 1 - t)
        total = (Fraction(0), Fraction(0), Fraction(0))
        for s in range(3):
            total = vec_add(total, vec_scale(w[s], dirs[tau[s]]))
        return vec_sub(total, vec_scale(w[0], dirs[d]))

    fresh = (Fraction(5, 7), Fraction(-13, 9))   # never used by the primary
    coeff_ok = True
    fresh_ok = True
    trace_ok = True
    count = 0
    for d in range(6):
        for tau in itertools.product(range(6), repeat=3):
            a_interp = residual(d, tau, Fraction(0))
            b_interp = vec_sub(residual(d, tau, Fraction(1)), a_interp)
            a_def = vec_sub(vec_add(vec_add(dirs[tau[0]], dirs[tau[1]]),
                                    dirs[tau[2]]), dirs[d])
            b_def = vec_sub(dirs[tau[1]], dirs[tau[2]])
            if a_interp != a_def or b_interp != b_def:
                coeff_ok = False
            for t in fresh:
                if residual(d, tau, t) != vec_add(a_interp,
                                                  vec_scale(t, b_interp)):
                    fresh_ok = False
            trace = tuple(
                (dirs[tau[0]][axis] - dirs[d][axis])
                + dirs[tau[1]][axis] + dirs[tau[2]][axis]
                for axis in range(3))
            if trace != a_interp:
                trace_ok = False
            count += 1
    check("interp.interpolated_A_B_match_the_definitional_A_B",
          coeff_ok and count == 1296)
    check("interp.affine_law_holds_at_two_fresh_probe_points", fresh_ok)
    check("interp.ledger_trace_recomputed_componentwise_equals_A", trace_ok)
    return {"configurations": count, "fresh_probes": [str(t) for t in fresh]}


# ---------------------------------------------------------------------------
# unit 3 via character theory in Z[w]/(w^2 + w + 1)
# ---------------------------------------------------------------------------
def cyc_mul(a, b):
    # (a0 + a1*w)(b0 + b1*w) with w^2 = -1 - w
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0] - a[1] * b[1])


def cyc_pow(a, k):
    out = (Fraction(1), Fraction(0))
    for _ in range(k):
        out = cyc_mul(out, a)
    return out


def check_module_by_characters() -> dict:
    omega = (Fraction(0), Fraction(1))
    # permutation character of C_3 on 3 points: fixed-point counts
    perm_char = [Fraction(3), Fraction(0), Fraction(0)]
    # w is a primitive cube root: w^3 = 1 and 1 + w + w^2 = 0
    w3 = cyc_pow(omega, 3)
    unit_sum = tuple(sum(x) for x in zip(cyc_pow(omega, 0),
                                         cyc_pow(omega, 1),
                                         cyc_pow(omega, 2)))
    check("character.omega_is_a_primitive_cube_root_of_unity",
          w3 == (Fraction(1), Fraction(0))
          and unit_sum == (Fraction(0), Fraction(0)))

    # multiplicity of character chi_j (chi_j(c^k) = w^{jk}):
    # m_j = (1/3) sum_k perm_char(k) * conj(w^{jk}), conj(w) = w^2
    mults = []
    for j in range(3):
        total = (Fraction(0), Fraction(0))
        for k in range(3):
            conj = cyc_pow(cyc_pow(omega, 2), j * k)
            term = (perm_char[k] * conj[0], perm_char[k] * conj[1])
            total = (total[0] + term[0], total[1] + term[1])
        mults.append((total[0] / 3, total[1] / 3))
    check("character.multiplicities_over_C_are_1_1_1",
          all(m == (Fraction(1), Fraction(0)) for m in mults))

    # fusion over Q: the minimal polynomial of w over Q is x^2 + x + 1,
    # irreducible by the rational root theorem, so the two nontrivial
    # Galois-conjugate characters fuse into ONE 2-dimensional
    # Q-irreducible; the Q/R dimension pair is (1, 2)
    phi3_irreducible = all(r * r + r + 1 != 0
                           for r in (Fraction(1), Fraction(-1)))
    pair = (1, 1 + 1) if phi3_irreducible else None
    check("character.conjugate_characters_fuse_to_the_pair_1_2_over_Q",
          phi3_irreducible and pair == (1, 2))
    # char poly of the complement by the root route: (x - w)(x - w^2)
    # has constant w*w^2 = 1 and linear -(w + w^2) = 1 in Z[w]
    const = cyc_mul(omega, cyc_pow(omega, 2))
    linear = (-(omega[0] + cyc_pow(omega, 2)[0]),
              -(omega[1] + cyc_pow(omega, 2)[1]))
    char_poly = ("x^2 + x + 1"
                 if const == (Fraction(1), Fraction(0))
                 and linear == (Fraction(1), Fraction(0)) else "MISMATCH")
    disc = Fraction(1) * 1 - 4 * 1        # b^2 - 4c for x^2 + bx + c
    return {"multiplicities_over_C": [1, 1, 1],
            "dimension_pair_over_Q": [1, 2],
            "complement_char_poly": char_poly,
            "discriminant": q(disc)}


# ---------------------------------------------------------------------------
# unit 4 via polynomial identities, root extraction, and the cycle
# Laplacian pseudoinverse
# ---------------------------------------------------------------------------
def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def poly_eval(a, x):
    total = Fraction(0)
    for c in reversed(a):
        total = total * x + c
    return total


def check_forms_by_polynomials() -> dict:
    # the five forms at (w0, w1) = (1, n-1) as integer rational functions
    # (numerator, denominator) in n; target is ((n-1), n^2)
    n_minus_1 = [-1, 1]
    n_sq = [0, 0, 1]
    five = {
        "w1/(w0+w1)^2": (n_minus_1, n_sq),          # (n-1)/n^2
        "w0*w1/n^2": (n_minus_1, n_sq),
        "w1/n^2": (n_minus_1, n_sq),
        "(n-1)/n^2": (n_minus_1, n_sq),
        "w1/(w0*n^2)": (n_minus_1, n_sq),
    }
    # rebuild each form symbolically from its (w0, w1) shape on the locus:
    # w0 -> [1], w1 -> [-1, 1], w0 + w1 -> [0, 1], n -> [0, 1]
    built = {
        "w1/(w0+w1)^2": (n_minus_1, poly_mul([0, 1], [0, 1])),
        "w0*w1/n^2": (poly_mul([1], n_minus_1), n_sq),
        "w1/n^2": (n_minus_1, n_sq),
        "(n-1)/n^2": (n_minus_1, n_sq),
        "w1/(w0*n^2)": (n_minus_1, poly_mul([1], n_sq)),
    }
    cross_ok = True
    for name in five:
        num_b, den_b = built[name]
        # cross-multiplied identity with the target (n-1)/n^2
        left = poly_trim(poly_mul(num_b, n_sq))
        right = poly_trim(poly_mul(n_minus_1, den_b))
        if left != right:
            cross_ok = False
    check("polyid.five_forms_equal_(n-1)/n^2_as_rational_functions",
          cross_ok)

    fams = {
        "(N-1)/N^2": ([-1, 1], [0, 0, 1]),
        "(N^2-1)/(12N)": ([-1, 0, 1], [0, 12]),
        "(N-1)(N-2)/(3N)": (poly_mul([-1, 1], [-2, 1]), [0, 3]),
    }
    root_ok = True
    for (na, da), (nb, db) in itertools.combinations(fams.values(), 2):
        diff = poly_trim([x - y for x, y in
                          zip(poly_mul(na, db) + [0] * 8,
                              poly_mul(nb, da) + [0] * 8)])
        roots = [n for n in range(2, 201)
                 if poly_eval(diff, Fraction(n)) == 0]
        if roots != [3]:
            root_ok = False
    check("polyid.pairwise_family_difference_has_root_set_{3}_on_2_to_200",
          root_ok)

    # fixed-locus sum via the cycle-graph Laplacian pseudoinverse:
    # L = 2I - S - S^{N-1}; eigenvalues (1-z)(1-z^{-1}) over z^N = 1;
    # Tr((L + J/N)^{-1}) - 1 = sum over nontrivial z of the reciprocals
    def family_value(name, n):
        num, den = fams[name]
        return poly_eval(num, Fraction(n)) / poly_eval(den, Fraction(n))

    locus_rows = []
    locus_rows_primary_schema = []
    locus_ok = True
    for n in range(2, 13):
        shift = [[Fraction(1) if (i + 1) % n == j else Fraction(0)
                  for j in range(n)] for i in range(n)]
        shift_back = [[shift[j][i] for j in range(n)] for i in range(n)]
        lap = mat_sub(mat_sub(mat_scale(Fraction(2), mat_id(n)), shift),
                      shift_back)
        j_over_n = [[Fraction(1, n)] * n for _ in range(n)]
        inv = mat_inv(mat_add(lap, j_over_n))
        total = sum(inv[i][i] for i in range(n)) - 1
        expected = Fraction(n * n - 1, 12)
        locus_rows.append({"N": n, "sum": q(total),
                           "matches": total == expected})
        locus_rows_primary_schema.append({
            "N": n, "sum": q(total),
            "matches_(N^2-1)/12": total == expected,
            "normalised": q(total / n),
            "normalised_matches_family":
                total / n == family_value("(N^2-1)/(12N)", n)})
        if total != expected:
            locus_ok = False
    check("laplacian.pseudoinverse_trace_gives_(N^2-1)/12_for_N_2_to_12",
          locus_ok)

    n = 5
    shift = [[Fraction(1) if (i + 1) % n == j else Fraction(0)
              for j in range(n)] for i in range(n)]
    shift_back = [[shift[j][i] for j in range(n)] for i in range(n)]
    lap = mat_sub(mat_sub(mat_scale(Fraction(2), mat_id(n)), shift),
                  shift_back)
    j_over_n = [[Fraction(1, n)] * n for _ in range(n)]
    pseudo = mat_sub(mat_inv(mat_add(lap, j_over_n)), j_over_n)
    check("laplacian.pseudoinverse_witness_L_Lplus_is_I_minus_J_over_N",
          mat_eq(mat_mul(lap, pseudo), mat_sub(mat_id(n), j_over_n)))
    return {"fixed_locus_rows": locus_rows,
            "fixed_locus_rows_primary_schema": locus_rows_primary_schema,
            "family_values_at_N_3":
                {name: q(family_value(name, 3)) for name in fams},
            "family_values_at_N_4":
                {name: q(family_value(name, 4)) for name in fams}}


# ---------------------------------------------------------------------------
# unit 5 via bivariate polynomial elimination
# ---------------------------------------------------------------------------
def bp_add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Fraction(0)) + v
    return {k: v for k, v in out.items() if v != 0}


def bp_scale(c, a):
    return {k: c * v for k, v in a.items() if c * v != 0}


def bp_mul(a, b):
    out = {}
    for (i1, j1), v1 in a.items():
        for (i2, j2), v2 in b.items():
            k = (i1 + i2, j1 + j2)
            out[k] = out.get(k, Fraction(0)) + v1 * v2
    return {k: v for k, v in out.items() if v != 0}


def check_origin_by_elimination() -> dict:
    # variables: m -> (1,0), g0 -> (0,1); constants -> (0,0)
    one = {(0, 0): Fraction(1)}
    m = {(1, 0): Fraction(1)}
    g0 = {(0, 1): Fraction(1)}
    # G1 eliminated from 6*G1 - (6+m)*G0 = -1:
    # G1 = ((6+m)*G0 - 1)/6
    six_plus_m = bp_add(bp_scale(Fraction(6), one), m)
    g1 = bp_scale(Fraction(1, 6),
                  bp_add(bp_mul(six_plus_m, g0), bp_scale(Fraction(-1), one)))
    step = bp_add(g0, bp_scale(Fraction(-1), g1))
    claimed = bp_scale(Fraction(1, 6),
                       bp_add(one, bp_scale(Fraction(-1), bp_mul(m, g0))))
    check("bivar.step_equals_(1_minus_m_G0)/6_as_a_polynomial_identity",
          step == claimed)
    # 6*step - 1 = -m*G0 identically, so step = 1/6 iff m*G0 = 0
    left = bp_add(bp_scale(Fraction(6), step), bp_scale(Fraction(-1), one))
    check("bivar.six_step_minus_one_is_minus_m_G0_identically",
          left == bp_scale(Fraction(-1), bp_mul(m, g0)))
    # the positive-G0 slice, on a grid disjoint from the primary's
    slice_ok = True
    for mv in (Fraction(0), Fraction(2, 9), Fraction(3), Fraction(11, 8)):
        for g0v in (Fraction(1, 5), Fraction(3, 8), Fraction(9, 4)):
            g1v = ((6 + mv) * g0v - 1) / 6
            if ((g0v - g1v == Fraction(1, 6)) != (mv == 0)):
                slice_ok = False
    check("bivar.on_G0_positive_step_one_sixth_iff_m_zero", slice_ok)
    return {"identity": "G0 - G1 = (1 - m*G0)/6"}


# ---------------------------------------------------------------------------
# unit 6 via the circulant/trace route
# ---------------------------------------------------------------------------
def check_witness_by_trace() -> dict:
    ok = True
    value_at_3 = None
    rival_at_3 = None
    for n in range(2, 51):
        ones = [[Fraction(1)] * n for _ in range(n)]
        comp = mat_sub(mat_id(n), mat_scale(Fraction(1, n), ones))
        diag_entries = {comp[i][i] for i in range(n)}
        trace = sum(comp[i][i] for i in range(n))
        row_sums = [sum(row) for row in ones]
        totalsum = sum(row_sums)
        if not (len(diag_entries) == 1
                and trace == n - 1
                and next(iter(diag_entries)) == trace / n
                and totalsum == n * n):
            ok = False
        if n == 3:
            value_at_3 = (trace / n) / totalsum
            rival_at_3 = (trace / n) / n
    check("circulant.equal_diagonal_and_trace_route_gives_(n-1)/n_over_n^2",
          ok)
    check("circulant.ratio_at_n_3_is_2/27",
          value_at_3 == Fraction(2, 27))
    return {"n_range": [2, 50],
            "value_at_3": q(value_at_3),
            "rival_value_at_3": q(rival_at_3)}


# ---------------------------------------------------------------------------
# unit 7 via the edge-removal BFS route
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


def cycle_by_edge_removal(adj, n, s):
    """min over neighbours a of s of 1 + dist(a, s) in G minus the edge
    (s, a): a route through the deleted edge's endpoint back to s."""
    best = None
    for a in range(n):
        if not adj[s][a]:
            continue
        adj[s][a] = adj[a][s] = 0
        dist = bfs_dist(adj, n, a)
        adj[s][a] = adj[a][s] = 1
        if s in dist and (best is None or dist[s] + 1 < best):
            best = dist[s] + 1
    return best


def cycle_by_neighbour_pairs(adj, n, s):
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


def check_pointer_by_edge_removal() -> dict:
    n, s = 5, 0
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    agree = True
    total = 0
    cyclic = 0
    for mask in range(1 << len(pairs)):
        adj = [[0] * n for _ in range(n)]
        for k, (i, j) in enumerate(pairs):
            if mask >> k & 1:
                adj[i][j] = adj[j][i] = 1
        a = cycle_by_edge_removal(adj, n, s)
        b = cycle_by_neighbour_pairs(adj, n, s)
        if a != b:
            agree = False
        total += 1
        if a is not None:
            cyclic += 1
    check("edge_removal.matches_the_neighbour_pair_formula_on_all_1024",
          agree and total == 1 << 10 and 0 < cyclic < total)

    # seeded deterministic 8-vertex graphs (linear congruential, no
    # library randomness): both polynomial routes must agree
    n8, s8 = 8, 0
    pairs8 = [(i, j) for i in range(n8) for j in range(i + 1, n8)]
    state = 20260808
    agree8 = True
    cyclic8 = 0
    for _ in range(200):
        adj = [[0] * n8 for _ in range(n8)]
        for (i, j) in pairs8:
            state = (1103515245 * state + 12345) % (1 << 31)
            if state % 100 < 35:                    # edge density 0.35
                adj[i][j] = adj[j][i] = 1
        a = cycle_by_edge_removal(adj, n8, s8)
        b = cycle_by_neighbour_pairs(adj, n8, s8)
        if a != b:
            agree8 = False
        if a is not None:
            cyclic8 += 1
    check("edge_removal.matches_on_200_seeded_8_vertex_graphs",
          agree8 and cyclic8 > 0)

    # full 6-vertex census by this checker's OWN polynomial routes, so
    # the primary's census numbers are recomputed independently rather
    # than merely read back from its receipt
    n6, s6 = 6, 0
    pairs6 = [(i, j) for i in range(n6) for j in range(i + 1, n6)]
    agree6 = True
    total6 = 0
    cyclic6 = 0
    for mask in range(1 << len(pairs6)):
        adj = [[0] * n6 for _ in range(n6)]
        for k, (i, j) in enumerate(pairs6):
            if mask >> k & 1:
                adj[i][j] = adj[j][i] = 1
        a = cycle_by_edge_removal(adj, n6, s6)
        b = cycle_by_neighbour_pairs(adj, n6, s6)
        if a != b:
            agree6 = False
        total6 += 1
        if a is not None:
            cyclic6 += 1
    check("edge_removal.six_vertex_census_recomputed_independently",
          agree6 and total6 == 1 << 15 and 0 < cyclic6 < total6)
    return {"five_vertex_graphs": total,
            "five_vertex_with_cycle_through_pointer": cyclic,
            "eight_vertex_seeded": 200,
            "eight_vertex_with_cycle_through_pointer": cyclic8,
            "six_vertex_graphs": total6,
            "six_vertex_with_cycle_through_pointer": cyclic6}


# ---------------------------------------------------------------------------
# primary receipt verification (fail-closed, full surface)
# ---------------------------------------------------------------------------
# The primary's declared structure, pinned here so the canonical expected
# record covers EVERY field of the primary receipt payload.  Values that are
# mathematics are recomputed by this checker's own routes above; values that
# are the primary's declared design (probe-grid sizes, prose fields) are
# pinned as constants that must not drift without both files changing.
PRIMARY_SCRIPT = "scripts/salvaged_exact_algebra_2026_08_08.py"
PRIMARY_ROLE = ("salvage primary: seven narrow exact algebraic results "
                "on in-file stipulated definitions; bounded support "
                "only; no derivation, closure, or selection claims")
PRIMARY_CHECK_NAMES = (
    "split.decomposition_identity_on_all_probes",
    "split.trace_free_channel_has_zero_trace",
    "split.conformal_channel_is_constant_vector",
    "split.projectors_idempotent_complementary",
    "split.uniqueness_of_the_constant_part",
    "split.recoil_ledger_minus2w_w_w_is_trace_free",
    "split.graded_operator_fixes_exactly_the_trace_free_vectors",
    "grading.residual_equals_A_plus_tB_on_all_configurations",
    "grading.raw_ledger_sector_trace_is_identically_A",
    "grading.B_depends_only_on_the_second_and_third_sector",
    "grading.configuration_census_is_complete",
    "module.fixed_subspace_is_the_line_of_1_1_1",
    "module.complement_is_C_invariant_of_dimension_2",
    "module.complement_char_poly_is_x2_plus_x_plus_1",
    "module.complement_irreducible_over_Q_and_over_R",
    "module.full_char_poly_factors_as_x3_minus_1",
    "module.dimension_pattern_1_2_over_Q_R_and_1_1_1_over_C",
    "forms.five_forms_collapse_to_(n-1)/n^2_on_the_locus",
    "forms.families_coincide_pairwise_exactly_at_N_3",
    "forms.families_separate_at_N_4",
    "forms.fixed_locus_sum_equals_(N^2-1)/12_for_N_2_to_12",
    "forms.evaluation_census_is_complete",
    "origin.step_equals_(1_minus_m_G0)_over_6_on_the_grid",
    "origin.step_is_one_sixth_iff_m_times_G0_is_zero",
    "origin.on_G0_positive_the_massless_slice_is_m_equals_0",
    "witness.diag_Qp_over_totalsum_J_is_(n-1)/n^3_for_n_2_to_50",
    "witness.value_at_n_3_is_2/27",
    "witness.rival_expression_diag_Qp_over_n_is_(n-1)/n^2",
    "cycle.identity_holds_on_all_32768_graphs_on_6_vertices",
    "cycle.census_counts_are_real",
    "gate.check_count_matches_the_declared_census",
)


def build_expected_primary_payload(units: dict) -> dict:
    """The canonical expected primary receipt payload, assembled from this
    checker's independent recomputations plus the primary's pinned
    declared design.  Every load-bearing field of the primary payload is
    covered; comparison is wholesale."""
    reynolds = units["split_by_reynolds"]
    characters = units["module_by_characters"]
    forms = units["forms_by_polynomials"]
    witness = units["witness_by_trace"]
    pointer = units["pointer_by_edge_removal"]
    expected_units = {
        "trace_free_conformal_split": {
            "probe_count": 7 ** 3,           # primary's declared probe grid
            "ledger_rows": reynolds["ledger_rows_recomputed"],
        },
        "affine_grading_normal_form": {
            "configurations": units["grading_by_interpolation"]
            ["configurations"],
            "probe_points_per_configuration": 6,   # primary's declared grid
            "residual_identities_checked":
                units["grading_by_interpolation"]["configurations"] * 6,
        },
        "cyclic_permutation_module": {
            "dimension_pair_over_Q_and_R":
                characters["dimension_pair_over_Q"],
            "dimension_pattern_over_C":
                characters["multiplicities_over_C"],
            "complement_char_poly": characters["complement_char_poly"],
            "discriminant": characters["discriminant"],
        },
        "five_forms_and_families": {
            "five_form_evaluations": 49 * 5,   # primary's declared sweep
            "family_values_at_N_3": forms["family_values_at_N_3"],
            "family_values_at_N_4": forms["family_values_at_N_4"],
            "fixed_locus_rows": forms["fixed_locus_rows_primary_schema"],
        },
        "screened_origin_step": {
            "grid_rows": 5 * 5,               # primary's declared grid
        },
        "projector_ratio_witness": {
            "n_range": [2, 50],               # primary's declared range
            "value_at_3": witness["value_at_3"],
            "rival_value_at_3": witness["rival_value_at_3"],
        },
        "pointer_cycle_identity": {
            "graphs_checked": pointer["six_vertex_graphs"],
            "graphs_with_a_cycle_through_the_pointer":
                pointer["six_vertex_with_cycle_through_pointer"],
            "graphs_without":
                pointer["six_vertex_graphs"]
                - pointer["six_vertex_with_cycle_through_pointer"],
        },
    }
    return {
        "date": DATE,
        "script": PRIMARY_SCRIPT,
        "role": PRIMARY_ROLE,
        "inputs": [],
        "units": expected_units,
        "checks": [{"name": name, "ok": True}
                   for name in PRIMARY_CHECK_NAMES],
        "pass": len(PRIMARY_CHECK_NAMES),
        "fail": 0,
        "expected_check_count": len(PRIMARY_CHECK_NAMES),
        "verdict": "PASS",
    }


def receipt_digest_ok(receipt: dict) -> bool:
    stored = receipt.get("payload_sha256")
    stripped = {k: v for k, v in receipt.items() if k != "payload_sha256"}
    blob = json.dumps(stripped, sort_keys=True, indent=1).encode()
    return stored == hashlib.sha256(blob).hexdigest()


def receipt_content_ok(receipt: dict, expected_payload: dict) -> bool:
    stripped = {k: v for k, v in receipt.items() if k != "payload_sha256"}
    return stripped == expected_payload


def rehash(receipt: dict) -> dict:
    """Recompute a receipt's self-digest by the documented serialization
    (used to build the semantic-tamper regression, never to repair)."""
    out = {k: v for k, v in receipt.items() if k != "payload_sha256"}
    blob = json.dumps(out, sort_keys=True, indent=1).encode()
    out["payload_sha256"] = hashlib.sha256(blob).hexdigest()
    return out


def check_primary_receipt(units: dict) -> dict:
    exists = os.path.isfile(PRIMARY_RECEIPT)
    check("receipt.primary_receipt_file_exists", exists)
    if not exists:
        check("receipt.primary_digest_recomputes", False)
        check("receipt.full_payload_matches_the_canonical_expected_record",
              False)
        check("tamper.unrehashed_tamper_breaks_the_digest", False)
        check("tamper.rehashed_semantic_tamper_is_rejected", False)
        return {"error": "missing primary receipt"}
    with open(PRIMARY_RECEIPT, encoding="utf-8") as fh:
        receipt = json.load(fh)
    expected_payload = build_expected_primary_payload(units)
    check("receipt.primary_digest_recomputes", receipt_digest_ok(receipt))
    check("receipt.full_payload_matches_the_canonical_expected_record",
          receipt_content_ok(receipt, expected_payload))

    # regression 1: a byte tamper WITHOUT rehashing must break the digest
    tampered_plain = json.loads(json.dumps(receipt))
    tampered_plain["units"]["trace_free_conformal_split"]["ledger_rows"][0][
        "trace"] = "999/1"
    check("tamper.unrehashed_tamper_breaks_the_digest",
          not receipt_digest_ok(tampered_plain))

    # regression 2: the SAME semantic tamper with a recomputed self-digest
    # passes the digest gate but MUST be rejected by the full-payload gate
    tampered_rehashed = rehash(tampered_plain)
    check("tamper.rehashed_semantic_tamper_is_rejected",
          receipt_digest_ok(tampered_rehashed)
          and not receipt_content_ok(tampered_rehashed, expected_payload))
    return {"primary_pass": receipt.get("pass"),
            "primary_fail": receipt.get("fail"),
            "primary_digest": receipt.get("payload_sha256"),
            "comparison": "full payload minus self-digest, wholesale"}


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main() -> int:
    units = {
        "split_by_reynolds": check_split_by_reynolds(),
        "grading_by_interpolation": check_grading_by_interpolation(),
        "module_by_characters": check_module_by_characters(),
        "forms_by_polynomials": check_forms_by_polynomials(),
        "origin_by_elimination": check_origin_by_elimination(),
        "witness_by_trace": check_witness_by_trace(),
        "pointer_by_edge_removal": check_pointer_by_edge_removal(),
    }
    units["primary_receipt"] = check_primary_receipt(units)
    check("gate.check_count_matches_the_declared_census",
          len(CHECKS) + 1 == EXPECTED_CHECK_COUNT)
    passes = sum(1 for _n, ok in CHECKS if ok)
    fails = len(CHECKS) - passes
    verdict = "PASS" if fails == 0 else "FAIL"
    payload = {
        "date": DATE,
        "script":
            "scripts/salvaged_exact_algebra_independent_check_2026_08_08.py",
        "role": ("salvage independent check: every unit recomputed by a "
                 "different exact route; primary receipt verified "
                 "fail-closed"),
        "inputs": ["outputs/salvaged_exact_algebra_receipt_2026_08_08.json"],
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
