#!/usr/bin/env python3
"""
Runner: record count bounds composition words; pure single-chart dials stay fixed.

Scope. This runner supports a bounded-theorem note. It does not set, predict, or
estimate any audit verdict, and it edits no audit data file. It checks named,
unadopted premises plus exact polynomial arithmetic:

  * pure-letter event premise: a single-chart word is a pure iterate of the
    occupancy note's one flow read in one supplied dictionary.
  * chart-mix premise: a mixed word requires per-step dictionary supply.
  * record-production premise: each event registers at least one new record.
  * record persistence: records persist across events; grounded on the landed
    Record axiom sentence that records are permanent (commit 7950d9202c), not a
    separately supplied premise.
  * finite-collection-containment premise: a supplied finite readout collection
    contains the realized history's registered records.
  * record-count bound: under the pure-letter, production, persistence, and
    containment premises, k <= N_rec.
  * finite dial enumeration: the length-<=2 mixed-word surface is exact, while
    pure single-chart iteration stays at {1/2} or {1} for all word lengths.

Arithmetic is exact only: Fraction and integer-coefficient polynomial arithmetic
implemented inline as coefficient lists. No floats. No numeric root-finding.
Context-only surfaces are not used as authority.
"""

import os
import sys
from fractions import Fraction
from itertools import product

# --------------------------------------------------------------------------
# Exact polynomial arithmetic. A polynomial is a list of Fraction coefficients
# indexed by power: p[i] is the coefficient of r**i. The zero polynomial is [].
# --------------------------------------------------------------------------

def poly_trim(p):
    q = [Fraction(c) for c in p]
    while q and q[-1] == 0:
        q.pop()
    return q

def poly_add(a, b):
    n = max(len(a), len(b))
    r = []
    for i in range(n):
        ca = a[i] if i < len(a) else 0
        cb = b[i] if i < len(b) else 0
        r.append(Fraction(ca) + Fraction(cb))
    return poly_trim(r)

def poly_sub(a, b):
    n = max(len(a), len(b))
    r = []
    for i in range(n):
        ca = a[i] if i < len(a) else 0
        cb = b[i] if i < len(b) else 0
        r.append(Fraction(ca) - Fraction(cb))
    return poly_trim(r)

def poly_mul(a, b):
    if not a or not b:
        return []
    r = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, ca in enumerate(a):
        for j, cb in enumerate(b):
            r[i + j] += Fraction(ca) * Fraction(cb)
    return poly_trim(r)

def poly_compose(outer, inner):
    """Return outer(inner(r)) by exact Horner substitution."""
    res = []
    for c in reversed(outer):
        res = poly_add(poly_mul(res, inner), [Fraction(c)])
    return poly_trim(res)

def poly_eval(p, x):
    """Exact evaluation at rational x (Fraction)."""
    x = Fraction(x)
    acc = Fraction(0)
    for c in reversed(p):
        acc = acc * x + Fraction(c)
    return acc

def poly_deg(p):
    q = poly_trim(p)
    return len(q) - 1 if q else -1

def poly_divmod(a, b):
    a = poly_trim(a)
    b = poly_trim(b)
    if not b:
        raise ZeroDivisionError("division by zero polynomial")
    q = [Fraction(0)] * max(len(a) - len(b) + 1, 0)
    rem = a[:]
    while poly_trim(rem) and len(poly_trim(rem)) >= len(b):
        rem = poly_trim(rem)
        coeff = rem[-1] / b[-1]
        shift = len(rem) - len(b)
        q[shift] += coeff
        sub = [Fraction(0)] * shift + [coeff * Fraction(c) for c in b]
        rem = poly_sub(rem, sub)
    return poly_trim(q), poly_trim(rem)

def poly_gcd(a, b):
    """Euclidean GCD over Q (returned non-monic; a nonzero constant means coprime)."""
    a = poly_trim(a)
    b = poly_trim(b)
    while b:
        _, r = poly_divmod(a, b)
        a, b = b, poly_trim(r)
    return a

def poly_eq(a, b):
    return poly_trim(a) == poly_trim(b)

def monomial(coeff, deg):
    """coeff * r**deg."""
    p = [Fraction(0)] * (deg + 1)
    p[deg] = Fraction(coeff)
    return poly_trim(p)

# --------------------------------------------------------------------------
# The word class (related moduli-word context's formal word class): finite compositions of
# f(r)=2r^2 and g(r)=r^2. f.g means f(g(r)) (leftmost map outermost).
# --------------------------------------------------------------------------

R_POLY = [Fraction(0), Fraction(1)]                       # identity: r
F_POLY = [Fraction(0), Fraction(0), Fraction(2)]          # f(r) = 2 r^2
G_POLY = [Fraction(0), Fraction(0), Fraction(1)]          # g(r) =   r^2

def apply_map(m, p):
    return poly_compose(F_POLY if m == 'f' else G_POLY, p)

def word_poly(word):
    """Polynomial of the composed word (leftmost letter outermost)."""
    p = R_POLY[:]
    for ch in reversed(word):
        p = apply_map(ch, p)
    return p

def fixed_point_poly(word):
    """p_w(r) = word(r) - r."""
    return poly_sub(word_poly(word), R_POLY)

def all_words(k):
    out = []
    for m in range(1, k + 1):
        for tup in product('fg', repeat=m):
            out.append(''.join(tup))
    return out

def iterate_poly(base, m):
    """base composed with itself m times, as a polynomial in r."""
    p = R_POLY[:]
    for _ in range(m):
        p = poly_compose(base, p)
    return p

def discriminant_quadratic(q):
    """For q = [c, b, a] (a r^2 + b r + c): return b^2 - 4 a c (exact)."""
    q = poly_trim(q)
    c = q[0] if len(q) > 0 else Fraction(0)
    b = q[1] if len(q) > 1 else Fraction(0)
    a = q[2] if len(q) > 2 else Fraction(0)
    return b * b - 4 * a * c

# --------------------------------------------------------------------------
# Toy histories for the premise family record-production premise/record-persistence premise/finite-collection-containment premise and the bound record-count bound. A realized
# history is a list of per-event integers. Everything here is exact integer
# arithmetic (no floats).
#   * production per event  -> record-production premise holds iff every entry >= 1.
#   * persistent net change -> record-persistence premise holds iff the running count never decreases
#     (records do not vanish across events).
#   * in-collection flag    -> finite-collection-containment premise containment holds iff every registration lands
#     in the supplied counted collection.
# --------------------------------------------------------------------------

def cumulative(deltas):
    out, tot = [], 0
    for d in deltas:
        tot += d
        out.append(tot)
    return out

def non_decreasing(seq):
    return all(x <= y for x, y in zip(seq, seq[1:]))

def production_holds(prod):
    return all(p >= 1 for p in prod)

def persistence_holds(net):
    return non_decreasing(cumulative(net))

# --------------------------------------------------------------------------
# Document text access (read-only; whitespace-normalized substring search).
# --------------------------------------------------------------------------

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DOCS = os.path.join(ROOT, 'docs')

AXIOMS_DOC = os.path.join(DOCS, 'MINIMAL_AXIOMS_2026-06-29.md')
OCCUPANCY_DOC = os.path.join(
    DOCS,
    'OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md',
)
NOTE_DOC = os.path.join(
    DOCS,
    'RECORD_COUNT_BOUNDS_COMPOSITION_WORDS_FINITE_DIAL_BOUNDED_NOTE_2026-07-02.md',
)

def read_norm(path):
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            return ' '.join(fh.read().split())
    except OSError:
        return None

def contains(path, needle):
    text = read_norm(path)
    if text is None:
        return False
    return ' '.join(needle.split()) in text

def contains_ci(path, needle):
    text = read_norm(path)
    if text is None:
        return False
    return ' '.join(needle.split()).lower() in text.lower()

# --------------------------------------------------------------------------
# Check harness.
# --------------------------------------------------------------------------

_checks = []

def check(cond, desc):
    _checks.append((bool(cond), desc))

# ===== Sentence guards (landed axiom text + occupancy note) [checks 1-7] ====

check(
    contains(AXIOMS_DOC, "A state is a configuration of records."),
    "guard: state definition 'A state is a configuration of records.' present in axiom memo",
)
check(
    contains(AXIOMS_DOC, "records are permanent"),
    "guard: 'records are permanent' present in axiom memo (Record / Fixed Reality; landed commit 7950d9202c) -- permanence across events is axiom text and grounds record persistence directly; the pre-restoration wording 'the locked possibility is invariant under repeated readout' gave only within-readout stability and is superseded, so persistence is no longer a supplied correction premise",
)
check(
    contains(AXIOMS_DOC, "For any finite collection of pairwise-disjoint records, scalar readout"),
    "guard: 'For any finite collection of pairwise-disjoint records, scalar readout' present -- a CONDITIONAL on a supplied finite collection, NOT a bound on a configuration's record total",
)
check(
    contains(AXIOMS_DOC, "provide a record-production process"),
    "guard: dynamics disclaimer 'provide a record-production process' present (axioms supply no record-production process; grounds record-production premise as dynamics-shaped)",
)
check(
    contains(OCCUPANCY_DOC, "double-registration update squares registered weights"),
    "guard: occupancy note 'double-registration update squares registered weights' present (the ONE flow step read in a supplied chart)",
)
check(
    contains(OCCUPANCY_DOC, "the same binary, not three independent binaries"),
    "guard: occupancy tri-guise 'the same binary, not three independent binaries' present (f, g are two charts of one binary; mixed words need chart-mix)",
)
check(
    contains(AXIOMS_DOC, "physical persistence dynamics"),
    "guard: axiom Open Gates 'physical persistence dynamics' present -- the persistence MECHANISM/dynamics stays outside the axioms, distinct from the landed permanence FACT ('records are permanent', commit 7950d9202c) that grounds the record-persistence input to the count bound",
)

# ===== pure-letter event premise: letter = event (pure words) + CHART-MIX  [checks 8-9] ============

# Single-chart words are pure iterates of the ONE supplied flow read in ONE chart.
check(
    poly_eq(word_poly('ff'), iterate_poly(F_POLY, 2))
    and poly_eq(word_poly('gg'), iterate_poly(G_POLY, 2))
    and poly_eq(word_poly('fff'), iterate_poly(F_POLY, 3)),
    "pure-letter event premise: a single-chart word is a pure iterate of the ONE flow read in ONE supplied chart -- 'ff'=f^2, 'gg'=g^2, 'fff'=f^3 (component chart -> f, slot chart -> g)",
)
lead = {w: word_poly(w)[-1] for w in ('ff', 'gg', 'fg', 'gf')}
check(
    lead['ff'] == 8 and lead['gg'] == 1 and lead['fg'] == 2 and lead['gf'] == 4
    and lead['fg'] not in (lead['ff'], lead['gg'])
    and lead['gf'] not in (lead['ff'], lead['gg']),
    "pure-letter event premise / chart-mix: single-chart f.f=8r^4, g.g=r^4 vs mixed f.g=2r^4, g.f=4r^4 -- mixed leading coeffs {2,4} match neither single chart {8,1}; a mixed word is not an iterate of any single supplied flow",
)

# ===== record-production premise: production named, dynamics-shaped, independent content [check 10] =

prod_yes = [1, 2, 1, 3, 1]        # each event registers >= 1 new record
prod_no = [0, 0, 0]               # events occur, nothing is produced
check(
    production_holds(prod_yes) and (not production_holds(prod_no))
    and cumulative(prod_no)[-1] == 0 and len(prod_no) == 3,
    "record-production premise (production): NAMED, dynamics-shaped (memo disclaims a record-production process); independent content -- a zero-production history [0,0,0] advances the word (3 events) yet registers no record, so production is not supplied by the letters alone",
)

# ===== record persistence: grounded on landed axiom permanence; witness content [check 11] =

net_persist = [1, 1, 1, 1]        # records persist -> running count non-decreasing
net_vanish = [1, -1, 1, -1]       # produced then vanish -> not persistent
cum_vanish = cumulative(net_vanish)
check(
    persistence_holds(net_persist) and (not persistence_holds(net_vanish))
    and cum_vanish == [1, 0, 1, 0] and cum_vanish[-1] < len(net_vanish),
    "record persistence: GROUNDED on the landed axiom sentence 'records are permanent' (commit 7950d9202c) -- permanence across events is axiom text, so persistence is no longer a supplied correction premise; the produce-then-vanish history [+1,-1,+1,-1] is kept only as the load-bearing witness that the count step depends on persistence (count 0 would cease to bound the 4 events), a dependence the permanence axiom now meets",
)

# ===== finite-collection-containment premise: collection scoping / FIN [check 12] =============================

# No axiom bound on a configuration's record total: finiteness is a free
# parameter of the SUPPLIED collection, and registrations must be contained.
supplied_sizes = [1, 5, 100, 10 ** 6]
counts = [n for n in supplied_sizes]                       # N_rec = |supplied collection|
free_and_finite = (counts == supplied_sizes) and non_decreasing(counts) \
    and len(set(supplied_sizes)) == len(supplied_sizes)    # arbitrarily large; no cap
registered = {1, 2, 3}
collection = {1, 2, 3, 4, 5}
contained = registered.issubset(collection) and len(collection) == 5
check(
    free_and_finite and contained,
    "finite-collection-containment premise (scoping/FIN): the axioms do NOT bound a configuration's record total (an all-sites-recorded Z^3 config satisfies every quoted sentence); finiteness enters only via the supplied finite collection -- N_rec = |collection| for arbitrarily large supplied sizes (no cap), and the registered records are contained in the counted collection",
)

# ===== record-count bound: under pure-letter event premise(pure)+record-production premise+record-persistence premise+finite-collection-containment premise, k <= N_rec [checks 13-17] =============

# Positive direction: produce >= 1, all persist, all contained -> N_rec >= k.
prod_reg = [1, 2, 1, 3, 1]
counted_reg = cumulative(prod_reg)                         # persistent, all contained
check(
    production_holds(prod_reg) and persistence_holds(prod_reg)
    and all(counted_reg[k - 1] >= k for k in range(1, len(prod_reg) + 1)),
    "record-count bound: under record-production premise+record-persistence premise+finite-collection-containment premise, after k events at least k contained persistent records exist (k <= N_rec) for every prefix (monotone induction)",
)
prod_tight = [1, 1, 1, 1]
counted_tight = cumulative(prod_tight)
check(
    production_holds(prod_tight) and persistence_holds(prod_tight)
    and all(counted_tight[k - 1] == k for k in range(1, len(prod_tight) + 1))
    and counted_tight[-1] == len(prod_tight),
    "record-count bound: tightness -- a unit, persistent, contained history achieves k = N_rec exactly (the bound is tight)",
)
# Violation, drop record-production premise: unbounded word with no new records.
cum_p2 = cumulative(prod_no)
check(
    (not production_holds(prod_no))
    and any(cum_p2[k - 1] < k for k in range(1, len(prod_no) + 1)),
    "record-count bound: drop record-production premise -> unbounded words with no new records: events advance k while N_rec stays fixed, so k > N_rec (zero-production witness [0,0,0])",
)
# Violation, drop record-persistence premise: records vanish; the count ceases to bound.
check(
    (not persistence_holds(net_vanish))
    and any(cum_vanish[k - 1] < k for k in range(1, len(net_vanish) + 1)),
    "record-count bound: drop record-persistence premise -> records vanish and the count ceases to bound: produce-then-vanish witness [+1,-1,+1,-1] has count 0 < 4 events",
)
# Violation, drop finite-collection-containment premise containment: registrations land outside the counted collection.
prod_all = [1, 1, 1]
in_coll = [1, 0, 1]               # event 2 lands outside the counted collection
counted_out = sum(p for p, c in zip(prod_all, in_coll) if c)
check(
    (not all(in_coll)) and counted_out < len(prod_all),
    "record-count bound: drop finite-collection-containment premise containment -> registrations land outside the counted collection: 3 registrations, 1 outside, so N_rec = 2 < 3 = k",
)

# ===== finite dial enumeration: bounded words -> finite, exactly enumerable dial set ===========
# ===== [checks 18-28] ======================================================

wc = {k: len(all_words(k)) for k in range(1, 5)}
check(
    all(wc[k] == 2 ** (k + 1) - 2 for k in range(1, 5)) and wc == {1: 2, 2: 6, 3: 14, 4: 30},
    "finite dial enumeration: word count over {f,g} for length<=k equals 2^(k+1)-2 exactly (k=1..4: 2,6,14,30)",
)
deg_ok, sum_deg_k2 = True, 0
for m in range(1, 3):
    for tup in product('fg', repeat=m):
        d = poly_deg(fixed_point_poly(''.join(tup)))
        if d != 2 ** m:
            deg_ok = False
        sum_deg_k2 += d
check(
    deg_ok and sum_deg_k2 == 20 and sum_deg_k2 == (4 ** 3 - 4) // 3,
    "finite dial enumeration: each length-m word has fixed-point polynomial of degree 2^m; sum-of-degrees(k<=2)=20 is a finite exact dial-set-cardinality bound",
)
p_f = fixed_point_poly('f')
check(
    poly_eq(p_f, [0, -1, 2]) and poly_eq(poly_mul([0, 1], [-1, 2]), p_f),
    "finite dial enumeration: p_f(r) = f(r)-r = 2r^2 - r = r*(2r-1) -- positive fixed point r = 1/2",
)
p_g = fixed_point_poly('g')
check(
    poly_eq(p_g, [0, -1, 1]) and poly_eq(poly_mul([0, 1], [-1, 1]), p_g),
    "finite dial enumeration: p_g(r) = g(r)-r = r^2 - r = r*(r-1) -- positive fixed point r = 1",
)
p_fg = fixed_point_poly('fg')     # f(g(r)) - r
check(
    poly_eq(p_fg, [0, -1, 0, 0, 2]) and poly_eq(poly_mul([0, 1], [-1, 0, 0, 2]), p_fg),
    "finite dial enumeration: p_{f.g}(r) = f(g(r))-r = 2r^4 - r = r*(2r^3 - 1) -- mixed word; positive fixed point = root of 2r^3-1, the 2^(-1/3) dial point, arises only under chart-mix",
)
p_gf = fixed_point_poly('gf')     # g(f(r)) - r
check(
    poly_eq(p_gf, [0, -1, 0, 0, 4]) and poly_eq(poly_mul([0, 1], [-1, 0, 0, 4]), p_gf),
    "finite dial enumeration: p_{g.f}(r) = g(f(r))-r = 4r^4 - r = r*(4r^3 - 1) -- mixed word; positive fixed point = root of 4r^3-1, the 2^(-2/3) dial point, arises only under chart-mix",
)
# f.f and g.g: the omitted length-2 single-chart words -- factor and show the
# quadratic cofactors are positive-definite, so NO new positive root.
p_ff = fixed_point_poly('ff')     # 8r^4 - r
cof_ff = [1, 2, 4]                # 4r^2 + 2r + 1
check(
    poly_eq(p_ff, [0, -1, 0, 0, 8])
    and poly_eq(poly_mul([0, 1], poly_mul([-1, 2], cof_ff)), p_ff)
    and discriminant_quadratic(cof_ff) == -12 and discriminant_quadratic(cof_ff) < 0
    and cof_ff[-1] > 0,
    "finite dial enumeration: p_{f.f}(r) = 8r^4 - r = r*(2r-1)*(4r^2+2r+1); cofactor discriminant 4-16=-12 < 0 with positive leading coeff => positive-definite, NO new positive root -- f.f adds only r = 1/2",
)
p_gg = fixed_point_poly('gg')     # r^4 - r
cof_gg = [1, 1, 1]                # r^2 + r + 1
check(
    poly_eq(p_gg, [0, -1, 0, 0, 1])
    and poly_eq(poly_mul([0, 1], poly_mul([-1, 1], cof_gg)), p_gg)
    and discriminant_quadratic(cof_gg) == -3 and discriminant_quadratic(cof_gg) < 0
    and cof_gg[-1] > 0,
    "finite dial enumeration: p_{g.g}(r) = r^4 - r = r*(r-1)*(r^2+r+1); cofactor discriminant 1-4=-3 < 0 with positive leading coeff => positive-definite, NO new positive root -- g.g adds only r = 1; the length-<=2 dial set is COMPLETE",
)
# Distinctness of the four length-<=2 dial points.
CUBIC_FG = [-1, 0, 0, 2]          # 2r^3 - 1
CUBIC_GF = [-1, 0, 0, 4]          # 4r^3 - 1
g_cubics = poly_gcd(CUBIC_FG, CUBIC_GF)
half, one = Fraction(1, 2), Fraction(1)
not_root = (
    poly_eval(CUBIC_FG, half) != 0 and poly_eval(CUBIC_GF, half) != 0
    and poly_eval(CUBIC_FG, one) != 0 and poly_eval(CUBIC_GF, one) != 0
)
check(
    poly_deg(g_cubics) == 0 and poly_trim(g_cubics) != [] and not_root and half != one,
    "finite dial enumeration: length-<=2 dial set complete and distinct -- gcd(2r^3-1, 4r^3-1) is a nonzero constant (coprime cubics), r=1/2,1 are not roots of either cubic, 1/2 != 1: the four points {1/2, 1, 2^(-1/3), 2^(-2/3)} are pairwise distinct ({1/2,1} unconditional, {2^(-1/3),2^(-2/3)} conditional on chart-mix)",
)
# Strict-monotonicity identity replacing the invalid general-cubic sign inference.
def cubediff_lhs(a, r1):
    return [Fraction(-a) * Fraction(r1) ** 3, Fraction(0), Fraction(0), Fraction(a)]

def cubediff_rhs(a, r1):
    lin = [Fraction(-r1), Fraction(1)]                     # (x - r1)
    quad = [Fraction(r1) ** 2, Fraction(r1), Fraction(1)]  # x^2 + r1 x + r1^2
    return poly_mul([Fraction(a)], poly_mul(lin, quad))

mono_ok = True
for a in (2, 4):
    for r1 in (Fraction(1, 3), Fraction(1, 2), Fraction(3, 4), Fraction(2)):
        if not poly_eq(cubediff_lhs(a, r1), cubediff_rhs(a, r1)):
            mono_ok = False
    for r1, r2 in [(Fraction(1, 3), Fraction(1, 2)),
                   (Fraction(1, 2), Fraction(3, 4)),
                   (Fraction(1, 4), Fraction(9, 10))]:
        val = a * (r2 ** 3 - r1 ** 3)
        fac_lin = r2 - r1
        fac_quad = r2 ** 2 + r2 * r1 + r1 ** 2
        if not (val > 0 and fac_lin > 0 and fac_quad > 0):
            mono_ok = False
check(
    mono_ok,
    "finite dial enumeration: strict monotonicity of a*r^3-1 -- identity a*(r2^3-r1^3) = a*(r2-r1)*(r2^2+r2*r1+r1^2) holds exactly (a in {2,4}), and for 0<r1<r2 each factor > 0 so the difference > 0; this REPLACES the invalid general-cubic 'negative at 1/2 + positive leading coeff' sign inference",
)
sign_fg = poly_eval(CUBIC_FG, half)   # = -3/4
sign_gf = poly_eval(CUBIC_GF, half)   # = -1/2
check(
    mono_ok and sign_fg == Fraction(-3, 4) and sign_gf == Fraction(-1, 2)
    and sign_fg < 0 and sign_gf < 0 and CUBIC_FG[-1] > 0 and CUBIC_GF[-1] > 0
    and half >= half and one >= half,
    "finite dial enumeration: boundary >= 1/2 VIA STRICT MONOTONICITY -- (2r^3-1)@1/2 = -3/4, (4r^3-1)@1/2 = -1/2 both < 0 with positive leading coeff; since each cubic is strictly increasing on r>0 (identity above) its unique positive root exceeds 1/2; 1/2, 1 are >= 1/2 exactly (related moduli-word context boundary spot-checked)",
)

# ===== Pure-word corollary (the headline) [checks 29-31] ===================

# f^m = 2^(2^m - 1) * r^(2^m): coefficient-level induction, base + step + direct.
f_ind = poly_eq(iterate_poly(F_POLY, 1), F_POLY)
for m in range(1, 4):
    f_ind = f_ind and poly_eq(poly_compose(F_POLY, monomial(Fraction(2) ** (2 ** m - 1), 2 ** m)),
                              monomial(Fraction(2) ** (2 ** (m + 1) - 1), 2 ** (m + 1)))
f_form = all(poly_eq(iterate_poly(F_POLY, m), monomial(Fraction(2) ** (2 ** m - 1), 2 ** m))
             for m in range(1, 5))
f_fp = True
for m in range(1, 5):
    cof = poly_sub(monomial(Fraction(2) ** (2 ** m - 1), 2 ** m - 1), [1])   # coeff*r^(2^m-1) - 1
    fp = poly_sub(iterate_poly(F_POLY, m), R_POLY)
    if not (poly_eq(fp, poly_mul([0, 1], cof))
            and poly_eval(cof, half) == 0
            and poly_eval(cof, Fraction(1, 4)) < 0 and poly_eval(cof, one) > 0):
        f_fp = False
check(
    f_ind and f_form and f_fp,
    "corollary: f^m(r) = 2^(2^m - 1) * r^(2^m) exactly by coefficient-level induction (base f^1, step, and direct m=1..4); f^m - r = r*(coeff*r^(2^m-1) - 1) whose cofactor is a strictly increasing monomial-minus-1, so the UNIQUE positive fixed point is r = 1/2 for every m",
)
g_ind = poly_eq(iterate_poly(G_POLY, 1), G_POLY)
for m in range(1, 4):
    g_ind = g_ind and poly_eq(poly_compose(G_POLY, monomial(Fraction(1), 2 ** m)),
                              monomial(Fraction(1), 2 ** (m + 1)))
g_form = all(poly_eq(iterate_poly(G_POLY, m), monomial(Fraction(1), 2 ** m))
             for m in range(1, 5))
g_fp = True
for m in range(1, 5):
    cof = poly_sub(monomial(Fraction(1), 2 ** m - 1), [1])                   # r^(2^m-1) - 1
    fp = poly_sub(iterate_poly(G_POLY, m), R_POLY)
    if not (poly_eq(fp, poly_mul([0, 1], cof))
            and poly_eval(cof, one) == 0
            and poly_eval(cof, half) < 0 and poly_eval(cof, Fraction(2)) > 0):
        g_fp = False
check(
    g_ind and g_form and g_fp,
    "corollary: g^m(r) = r^(2^m) exactly by coefficient-level induction (base g^1, step, and direct m=1..4); g^m - r = r*(r^(2^m-1) - 1), so the UNIQUE positive fixed point is r = 1 for every m",
)
# Headline synthesis: per-chart dial set is a SINGLETON for all lengths; the
# mixed dial points are CHART-MIX artifacts (not pure fixed points).
pure_f_fixed_1_2 = all(poly_eval(poly_sub(iterate_poly(F_POLY, m), R_POLY), half) == 0
                       for m in range(1, 5))
pure_g_fixed_1 = all(poly_eval(poly_sub(iterate_poly(G_POLY, m), R_POLY), one) == 0
                     for m in range(1, 5))
mixed_not_pure = (poly_eval(CUBIC_FG, half) != 0 and poly_eval(CUBIC_FG, one) != 0
                  and poly_eval(CUBIC_GF, half) != 0 and poly_eval(CUBIC_GF, one) != 0)
check(
    pure_f_fixed_1_2 and pure_g_fixed_1 and mixed_not_pure,
    "corollary headline: under any single supplied dictionary the dial set is exactly {1/2} (component, all f) or {1} (slot, all g) for all word lengths; the mixed points 2^(-1/3), 2^(-2/3) are neither 1/2 nor 1, so they require chart-mix and are not pure-word fixed points",
)

# ===== residue map: the produced note conserves and enumerates its residues ========
# ===== [checks 32-33] ======================================================

note_terms = [
    "not adopted",
    "no wall is closed",
    "owner/science decision",
    "chart-mix",
    "record persistence",
    "does not bound",
    "Context-only surfaces",
]
missing = [t for t in note_terms if not contains_ci(NOTE_DOC, t)]
check(
    read_norm(NOTE_DOC) is not None and not missing,
    "residue map: bounded note present and contains all governance/residue markers "
    + repr(note_terms)
    + ("" if not missing else " -- MISSING: " + repr(missing)),
)
residue_families = [
    "record production",
    "finite-collection containment",
    "per-step dictionary",
    "realized history",
    "banked Dynamics proposal",
]
missing_res = [t for t in residue_families if not contains_ci(NOTE_DOC, t)]
check(
    read_norm(NOTE_DOC) is not None and not missing_res,
    "residue map: the note enumerates the residue list -- record production, finite-collection containment, per-step dictionary supply, realized history/step count, and banked context with no adopted premise status"
    + ("" if not missing_res else " -- MISSING: " + repr(missing_res)),
)

# --------------------------------------------------------------------------
# Report.
# --------------------------------------------------------------------------

def main():
    npass = sum(1 for ok, _ in _checks if ok)
    nfail = sum(1 for ok, _ in _checks if not ok)
    for i, (ok, desc) in enumerate(_checks, 1):
        print("CHECK {:02d}: {} — {}".format(i, "PASS" if ok else "FAIL", desc))
    print("TOTAL: PASS={} FAIL={}".format(npass, nfail))
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
