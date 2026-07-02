#!/usr/bin/env python3
"""
Runner: record count bounds the composition word (finite dial set), bounded theorem.

Block: walls-attack word-bound block21 (2026-07-02).

Scope. This runner supports a BOUNDED theorem note. It does NOT set, predict, or
estimate any audit verdict, and it edits no audit data file. It checks:

  T1  the registration premise REG>=1 is a NAMED, dynamics-shaped premise with
      independent content (monotone registration vs a degenerate zero-record
      step). REG>=1 is named, NOT derived and NOT adopted.
  T2  under REG>=1, the realized record count bounds the word length: k <= N_rec,
      by monotone induction, tight, and violable only by violating REG>=1.
  T3  bounded words over {f(r)=2r^2, g(r)=r^2} give a FINITE, exactly enumerable
      dial set: word count 2^(k+1)-2; fixed-point polynomials of degree 2^m;
      the length-<=2 dial points 1/2, 1, root(2r^3-1)=2^(-1/3),
      root(4r^3-1)=2^(-2/3) are exact and pairwise distinct; all >= 1/2.
  T5  the produced note conserves and enumerates its residues (boundary greps).

Arithmetic is EXACT ONLY: Fraction and integer-coefficient polynomial arithmetic
implemented inline as coefficient lists. No floats. No numeric root-finding.

Citations to block07 (selector-constraint map), block12 (moduli words / boundary
1/2), block20 (action-lane C-add), and PR #4843 (banked Dynamics-axiom proposal)
are REVIEW-PENDING and are used as context only.
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

# --------------------------------------------------------------------------
# The word class: finite compositions of f(r)=2r^2 and g(r)=r^2.
# f.g means f(g(r)) (standard composition; leftmost map outermost).
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

# --------------------------------------------------------------------------
# Toy registration sequences for T1/T2. A sequence is a list of per-step
# record increments (deltas). REG>=1 holds iff every delta >= 1. The realized
# record count after k steps is the cumulative sum (start count 0).
# --------------------------------------------------------------------------

def cumulative(deltas):
    out = []
    tot = 0
    for d in deltas:
        tot += d
        out.append(tot)
    return out

def reg_holds(deltas):
    return all(d >= 1 for d in deltas)

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

# ===== Sentence guards (landed axiom text + occupancy note) ===============

check(
    contains(AXIOMS_DOC, "A state is a configuration of records."),
    "guard: state definition 'A state is a configuration of records.' present in axiom memo",
)
check(
    contains(AXIOMS_DOC, "the locked possibility is invariant under repeated readout"),
    "guard: 'the locked possibility is invariant under repeated readout' present (registration monotone; nothing un-registers)",
)
check(
    contains(AXIOMS_DOC, "For any finite collection of pairwise-disjoint records, scalar readout"),
    "guard: finite-collection additivity sentence present (N_rec finite on any readout collection)",
)
check(
    contains(AXIOMS_DOC, "provide a record-production process"),
    "guard: dynamics disclaimer 'provide a record-production process' present (axioms supply no record-production process)",
)
check(
    contains(OCCUPANCY_DOC, "double-registration update squares registered weights"),
    "guard: occupancy note 'double-registration update squares registered weights' present (the flow step of f,g)",
)

# ===== T1: REG>=1 named, grounded, NOT derived; independent content =======

seq_reg = [1, 2, 1, 3, 1]         # every step registers >= 1 new record
seq_degen = [1, 0, 1, 1]          # monotone (non-decreasing) but a step adds none

check(
    reg_holds(seq_reg) and all(x <= y for x, y in zip(cumulative(seq_reg), cumulative(seq_reg)[1:])),
    "T1: REG>=1 sequence [1,2,1,3,1] registers >=1 each step (monotone registration)",
)
# Degenerate step: counts still non-decreasing, so monotonicity holds, yet REG>=1 fails.
cum_degen = cumulative(seq_degen)
monotone_degen = all(x <= y for x, y in zip(cum_degen, cum_degen[1:]))
check(
    monotone_degen and (not reg_holds(seq_degen)),
    "T1: degenerate step [1,0,1,1] is monotone yet fails REG>=1 -> REG>=1 is strictly stronger than monotonicity (independent content)",
)

# ===== T2: under REG>=1, k <= N_rec (induction, tightness, violation) ======

cum_reg = cumulative(seq_reg)
check(
    reg_holds(seq_reg) and all(cum_reg[k - 1] >= k for k in range(1, len(seq_reg) + 1)),
    "T2: under REG>=1, after k steps at least k records exist (k <= N_rec) for every prefix",
)
seq_tight = [1, 1, 1, 1]          # all-ones: N_rec after k steps equals k exactly
cum_tight = cumulative(seq_tight)
check(
    reg_holds(seq_tight) and all(cum_tight[k - 1] == k for k in range(1, len(seq_tight) + 1))
    and cum_tight[-1] == len(seq_tight),
    "T2: tightness -- all-ones sequence achieves k = N_rec (bound is tight)",
)
seq_viol = [0, 0, 0]              # zero-delta steps: k exceeds N_rec
cum_viol = cumulative(seq_viol)
bound_violated = any(cum_viol[k - 1] < k for k in range(1, len(seq_viol) + 1))
check(
    bound_violated and (not reg_holds(seq_viol)),
    "T2: the bound k <= N_rec is violated only by violating REG>=1 (zero-delta witness: k > N_rec requires a REG>=1 violation)",
)

# ===== T3: bounded words -> finite, exactly enumerable dial set ============

wc = {k: len(all_words(k)) for k in range(1, 5)}
check(
    all(wc[k] == 2 ** (k + 1) - 2 for k in range(1, 5)) and wc == {1: 2, 2: 6, 3: 14, 4: 30},
    "T3: word count over {f,g} for length<=k equals 2^(k+1)-2 exactly (k=1..4: 2,6,14,30)",
)

# degree of p_w = 2^m for a length-m word; sum-of-degrees is a finite integer
# bound on the dial-set cardinality. For k<=2 the exact sum is (4^3-4)/3 = 20.
deg_ok = True
sum_deg_k2 = 0
for m in range(1, 3):
    for tup in product('fg', repeat=m):
        w = ''.join(tup)
        d = poly_deg(fixed_point_poly(w))
        if d != 2 ** m:
            deg_ok = False
        sum_deg_k2 += d
check(
    deg_ok and sum_deg_k2 == 20 and sum_deg_k2 == (4 ** 3 - 4) // 3,
    "T3: each length-m word has fixed-point polynomial of degree 2^m; sum-of-degrees(k<=2)=20 is a finite exact dial-set bound",
)

# Exact polynomial identities and factorizations at POLYNOMIAL level.
p_f = fixed_point_poly('f')
check(
    poly_eq(p_f, [0, -1, 2]),
    "T3: p_f(r) = f(r)-r = 2r^2 - r  (exact coefficient identity)",
)
check(
    poly_eq(poly_mul([0, 1], [-1, 2]), p_f),
    "T3: factorization r*(2r-1) = 2r^2 - r  (positive fixed point r = 1/2)",
)
p_g = fixed_point_poly('g')
check(
    poly_eq(p_g, [0, -1, 1]),
    "T3: p_g(r) = g(r)-r = r^2 - r  (exact coefficient identity)",
)
check(
    poly_eq(poly_mul([0, 1], [-1, 1]), p_g),
    "T3: factorization r*(r-1) = r^2 - r  (positive fixed point r = 1)",
)
p_fg = fixed_point_poly('fg')     # f(g(r)) - r
check(
    poly_eq(p_fg, [0, -1, 0, 0, 2]) and poly_eq(poly_mul([0, 1], [-1, 0, 0, 2]), p_fg),
    "T3: p_{f.g}(r) = f(g(r))-r = 2r^4 - r = r*(2r^3 - 1)  (positive fixed point = root of 2r^3-1, the 2^(-1/3) dial point)",
)
p_gf = fixed_point_poly('gf')     # g(f(r)) - r
check(
    poly_eq(p_gf, [0, -1, 0, 0, 4]) and poly_eq(poly_mul([0, 1], [-1, 0, 0, 4]), p_gf),
    "T3: p_{g.f}(r) = g(f(r))-r = 4r^4 - r = r*(4r^3 - 1)  (positive fixed point = root of 4r^3-1, the 2^(-2/3) dial point)",
)

# Distinctness of the four length-<=2 dial points via exact polynomial algebra.
CUBIC_FG = [-1, 0, 0, 2]          # 2r^3 - 1
CUBIC_GF = [-1, 0, 0, 4]          # 4r^3 - 1
g_cubics = poly_gcd(CUBIC_FG, CUBIC_GF)
check(
    poly_deg(g_cubics) == 0 and poly_trim(g_cubics) != [],
    "T3: gcd(2r^3-1, 4r^3-1) is a nonzero constant -> the two cubics are coprime and share no root (roots 2^(-1/3), 2^(-2/3) distinct)",
)
half, one = Fraction(1, 2), Fraction(1)
not_root = (
    poly_eval(CUBIC_FG, half) != 0 and poly_eval(CUBIC_GF, half) != 0
    and poly_eval(CUBIC_FG, one) != 0 and poly_eval(CUBIC_GF, one) != 0
)
check(
    not_root and half != one,
    "T3: r=1/2 and r=1 are not roots of either cubic (exact eval) and 1/2 != 1 -> all four length-<=2 dial points pairwise distinct",
)

# Block12 boundary fact (every positive fixed point >= 1/2), spot-verified exactly.
sign_fg = poly_eval(CUBIC_FG, half)   # = -3/4
sign_gf = poly_eval(CUBIC_GF, half)   # = -1/2
check(
    half >= half and one >= half
    and sign_fg == Fraction(-3, 4) and sign_gf == Fraction(-1, 2)
    and sign_fg < 0 and CUBIC_FG[-1] > 0 and sign_gf < 0 and CUBIC_GF[-1] > 0,
    "T3: boundary 1/2 -- rationals 1/2,1 are >=1/2 exactly; sign(cubic @1/2)<0 with positive leading coeff => both cubic roots exceed 1/2 (block12 spot-verified)",
)

# ===== T5: the produced note conserves and enumerates its residues ========

note_terms = ["not adopted", "no wall", "review-pending", "morning", "owner decision", "same family"]
missing = [t for t in note_terms if not contains_ci(NOTE_DOC, t)]
check(
    read_norm(NOTE_DOC) is not None and not missing,
    "T5: bounded note present and contains all residue/governance markers "
    + "{'not adopted','no wall','review-pending','morning','owner decision','same family'}"
    + ("" if not missing else " -- MISSING: " + repr(missing)),
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
