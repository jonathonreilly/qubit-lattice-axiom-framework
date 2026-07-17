#!/usr/bin/env python3
"""Berezin count-binary measure-collapse checks on the C_3[111] coupling triple.

Paired note:
docs/KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-17.md

Blocks:
  B1 finite Grassmann/Berezin engine exactness: anticommutation and
     nilpotency, product-formula exp == power-series exp, quadratic integral
     = det M at n = 1, 2, 3 with computed sign under the pinned measure
     ordering, reversed-ordering sign (-1)^n, disjoint-copy factorization,
     coupling-triple determinant and K-copy identities
  B2 sector-selective realization on entrywise-real triples inheriting the
     spectral-pairing note's K-orbit pairing license: count-once integral
     = det3 = lam0*|lam1|^2, count-twice via the K-conjugate partner copy
     = |det3|^2 = lam0^2*|lam1|^4, direct 12-generator witness, r-neutral
     doubling with non-constant ratio det3
  B3 declared-reading generator-count bookkeeping (horn m uses 6m
     generators; a declared translation, never an equivalence)
  B4 linear measure collapse: diagonal rescale scalar, general linear
     redefinition scalar det(B)det(A), no-constant-kappa witness clash,
     uniform-rescale horn split rho versus |rho|^2
  B5 controls: Hermitian real-intersection, off-locus negative (1,i,0),
     pairing-without-reality witness (i,1+i,i), neither-horn-forced witness
     (3,1,1), section-tie endpoint arithmetic (both conditional laws)
  B6 verbatim quote gates: sources carry the consumed sentences and the
     note quotes them in blockquotes
  B7 ledger shard filename gates (timeless: existence only, no status pins)
  B8 note hygiene: section presence, forbidden-phrase absence, no bare
     decimal literals, markdown dependency links, backticked context handles

All algebra is exact sympy. No floats. Exit 1 on any failure.
"""

import re
from pathlib import Path

import sympy as sp
from sympy import I, Matrix, Rational, conjugate, eye, factorial, sqrt

ROOT = Path(__file__).resolve().parents[1]

NOTE = (
    "docs/KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_"
    "BOUNDED_THEOREM_NOTE_2026-07-17.md"
)
RUNNER = (
    "scripts/kcpt_coupling_triple_berezin_count_binary_measure_collapse_"
    "2026_07_17.py"
)
CACHE = (
    "logs/runner-cache/kcpt_coupling_triple_berezin_count_binary_measure_"
    "collapse_2026_07_17.txt"
)

BLOCK05 = (
    "docs/KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_"
    "SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md"
)
SECTIE = (
    "docs/KOIDE_FIRST_ORDER_SECTION_TIE_VS_OUTCOME_LABEL_RESIDUAL_"
    "LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-07-11.md"
)
STAG = (
    "docs/KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_"
    "THEOREM_NOTE_2026-06-11.md"
)
OBLIG = "docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md"
AXIOMS = "docs/MINIMAL_AXIOMS_2026-06-29.md"

PASS = 0
FAIL = 0
FAILURES = []


def check(block, name, condition, detail=""):
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
        FAILURES.append(f"{block}:{name}")
    suffix = f" [{detail}]" if detail else ""
    print(f"{block} {status} {name}{suffix}")


def is_zero(expr):
    e = sp.expand(sp.expand_complex(sp.expand(expr)))
    return sp.simplify(e) == 0


def mat_zero(M):
    return all(is_zero(M[i, j]) for i in range(M.rows) for j in range(M.cols))


def flattened(rel):
    return " ".join((ROOT / rel).read_text(encoding="utf-8").split())


def quote_groups(rel):
    groups, cur = [], []
    for line in (ROOT / rel).read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s.startswith(">"):
            cur.append(s.lstrip(">").strip())
        else:
            if cur:
                groups.append(" ".join(" ".join(cur).split()))
                cur = []
    if cur:
        groups.append(" ".join(" ".join(cur).split()))
    return groups


def in_groups(groups, needle):
    return any(needle in g for g in groups)


# ---------------------------------------------------------------------------
# Finite Grassmann engine (own exact implementation, sparse dict).
# element: dict frozenset(generator indices) -> sympy coefficient
# canonical monomial = generators in ascending index order
# ---------------------------------------------------------------------------


def gadd(A, B):
    out = dict(A)
    for k, v in B.items():
        out[k] = out.get(k, 0) + v
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def gmul(A, B):
    out = {}
    for sa, ca in A.items():
        for sb, cb in B.items():
            if sa & sb:
                continue
            la = sorted(sa)
            inv = 0
            for x in sb:
                inv += sum(1 for y in la if y > x)
            key = sa | sb
            out[key] = out.get(key, 0) + (-1) ** inv * ca * cb
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def gen(i, coeff=1):
    return {frozenset((i,)): sp.sympify(coeff)}


def gexp_product(terms):
    """exp(sum t_k) for even nilpotent single-monomial terms t_k:
    even elements commute and each t_k^2 = 0, so exp = prod (1 + t_k)."""
    res = {frozenset(): sp.Integer(1)}
    for t in terms:
        res = gadd(res, gmul(res, t))
    return res


def gexp_series(A, kmax):
    res = {frozenset(): sp.Integer(1)}
    term = {frozenset(): sp.Integer(1)}
    for k in range(1, kmax + 1):
        term = gmul(term, A)
        if not term:
            break
        res = gadd(res, {kk: v / factorial(k) for kk, v in term.items()})
    return res


def integrate_one(F, i):
    """Berezin d g_i: keep terms containing i; sign moves g_i to the right."""
    out = {}
    for s, c in F.items():
        if i not in s:
            continue
        sign = (-1) ** sum(1 for y in s if y > i)
        key = s - {i}
        out[key] = out.get(key, 0) + sign * c
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def berezin(F, order):
    """Measure written left-to-right as order; rightmost differential acts first."""
    for i in reversed(order):
        F = integrate_one(F, i)
    return F.get(frozenset(), sp.Integer(0))


def minus_action_terms(M, th, tb):
    """-S with S = sum_(i,j) thetabar_i M[i,j] theta_j; th/tb index lists."""
    n = len(th)
    terms = []
    for i in range(n):
        for j in range(n):
            if M[i, j] == 0:
                continue
            gi, gj = tb[i], th[j]
            key = frozenset((gi, gj))
            coeff = -M[i, j] if gi < gj else M[i, j]
            terms.append({key: sp.sympify(coeff)})
    return terms


def holo_integral(M, th, tb):
    """Pinned convention: measure order [th_1, tb_1, ..., th_n, tb_n]
    (d theta_1 d thetabar_1 ... d theta_n d thetabar_n, rightmost first)."""
    terms = minus_action_terms(M, th, tb)
    F = gexp_product(terms)
    order = []
    for k in range(len(th)):
        order.extend([th[k], tb[k]])
    return berezin(F, order)


def holo_integral_reversed(M, th, tb):
    terms = minus_action_terms(M, th, tb)
    F = gexp_product(terms)
    order = []
    for k in range(len(th)):
        order.extend([th[k], tb[k]])
    return berezin(F, list(reversed(order)))


# ---------------------------------------------------------------- B1: engine
e1e2 = gmul(gen(1), gen(2))
e2e1 = gmul(gen(2), gen(1))
anti = gadd(e1e2, e2e1)
sq = gmul(gen(1), gen(1))
check("B1.1", "anticommutation e1e2 + e2e1 = 0 and nilpotency e1^2 = 0",
      anti == {} and sq == {})

m11, m12, m21, m22 = sp.symbols("m11 m12 m21 m22")
M2 = Matrix([[m11, m12], [m21, m22]])
th2, tb2 = [0, 2], [1, 3]
terms2 = minus_action_terms(M2, th2, tb2)
A2 = {}
for t in terms2:
    A2 = gadd(A2, t)
prod_exp = gexp_product(terms2)
series_exp = gexp_series(A2, 4)
diff_keys = set(prod_exp) | set(series_exp)
check("B1.2", "product-formula exp == power-series exp (n=2 symbolic)",
      all(is_zero(prod_exp.get(k, 0) - series_exp.get(k, 0)) for k in diff_keys))

m = sp.Symbol("m")
val1 = holo_integral(Matrix([[m]]), [0], [1])
check("B1.3", "n=1 integral = det M = m (pinned ordering, computed sign +1)",
      is_zero(val1 - m))

val2 = holo_integral(M2, th2, tb2)
check("B1.4", "n=2 generic integral = det M (pinned ordering)",
      is_zero(val2 - M2.det()))

n11, n12, n13, n21, n22, n23, n31, n32, n33 = sp.symbols(
    "n11 n12 n13 n21 n22 n23 n31 n32 n33")
M3 = Matrix([[n11, n12, n13], [n21, n22, n23], [n31, n32, n33]])
th3, tb3 = [0, 2, 4], [1, 3, 5]
val3 = holo_integral(M3, th3, tb3)
check("B1.5", "n=3 generic integral = det M (pinned ordering)",
      is_zero(val3 - M3.det()))

r1 = holo_integral_reversed(Matrix([[m]]), [0], [1])
r2 = holo_integral_reversed(M2, th2, tb2)
r3 = holo_integral_reversed(M3, th3, tb3)
check("B1.6", "reversed measure ordering = (-1)^n det M at n=1,2,3",
      is_zero(r1 + m) and is_zero(r2 - M2.det()) and is_zero(r3 + M3.det()))

p11, p12, p21, p22 = sp.symbols("p11 p12 p21 p22")
N2 = Matrix([[p11, p12], [p21, p22]])
terms_joint = (minus_action_terms(M2, [0, 2], [1, 3])
               + minus_action_terms(N2, [4, 6], [5, 7]))
F_joint = gexp_product(terms_joint)
val_joint = berezin(F_joint, [0, 1, 2, 3, 4, 5, 6, 7])
check("B1.7", "disjoint-copy factorization: joint integral = det M * det N",
      is_zero(val_joint - M2.det() * N2.det()))

a, b, c = sp.symbols("a b c")
ar, br, cr = sp.symbols("ar br cr", real=True)
w = Rational(-1, 2) + sqrt(3) / 2 * I
C = Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])


def W_of(x, y, z):
    return x * eye(3) + y * C + z * C ** 2


def lam(k, x, y, z):
    return x + y * w ** k + z * w ** (2 * k)


def det3(x, y, z):
    return x ** 3 + y ** 3 + z ** 3 - 3 * x * y * z


check("B1.8", "det W = a^3+b^3+c^3-3abc = lam0*lam1*lam2 (generic symbolic)",
      is_zero(W_of(a, b, c).det() - det3(a, b, c))
      and is_zero(det3(a, b, c)
                  - lam(0, a, b, c) * lam(1, a, b, c) * lam(2, a, b, c)))

check("B1.9", "K-copy identity det3(conj entries) = conj(det3) (generic)",
      is_zero(det3(conjugate(a), conjugate(b), conjugate(c))
              - conjugate(det3(a, b, c))))

# ------------------------------- B2: sector-selective realization (05 T3)
l0r = lam(0, ar, br, cr)
l1r = lam(1, ar, br, cr)
l2r = lam(2, ar, br, cr)

check("B2.1", "entrywise-real: lam2 = conj(lam1) and lam0 real (license re-derived)",
      is_zero(l2r - conjugate(l1r)) and is_zero(l0r - conjugate(l0r)))

ok_assoc = True
for k in range(3):
    chi = w ** k
    P = (eye(3) + conjugate(chi) * C + conjugate(chi) ** 2 * C ** 2) / 3
    ok_assoc = ok_assoc and mat_zero(W_of(a, b, c) * P - lam(k, a, b, c) * P)
check("B2.2", "channel association W P_(w^k) = lam_k P_(w^k), k=0,1,2 (generic)",
      ok_assoc)

Wr = W_of(ar, br, cr)
count_once = holo_integral(Wr, th3, tb3)
check("B2.3", "count-once integral = det3 = lam0*|lam1|^2 on real triples",
      is_zero(count_once - det3(ar, br, cr))
      and is_zero(det3(ar, br, cr) - l0r * l1r * conjugate(l1r)))

partner_real = W_of(conjugate(ar), conjugate(br), conjugate(cr))
count_twice_sym = count_once * holo_integral(partner_real, th3, tb3)
check("B2.4", "count-twice = |det3|^2 = lam0^2*|lam1|^4 via K-partner copy; "
      "partner coincides with original on the real locus",
      is_zero(count_twice_sym - det3(ar, br, cr) ** 2)
      and is_zero(det3(ar, br, cr) ** 2
                  - l0r ** 2 * (l1r * conjugate(l1r)) ** 2)
      and mat_zero(partner_real - Wr))

order12 = list(range(12))
aw, bw, cw = sp.Integer(2), 1 + I, -I
Wnum = W_of(aw, bw, cw)
Wnum_conj = W_of(conjugate(aw), conjugate(bw), conjugate(cw))
terms12 = (minus_action_terms(Wnum, [0, 2, 4], [1, 3, 5])
           + minus_action_terms(Wnum_conj, [6, 8, 10], [7, 9, 11]))
F12 = gexp_product(terms12)
val12 = berezin(F12, order12)
expected12 = det3(aw, bw, cw) * conjugate(det3(aw, bw, cw))
check("B2.5", "direct 12-generator joint integral = |det3|^2 at witness (2,1+i,-i)",
      is_zero(val12 - expected12)
      and is_zero(expected12 - sp.Abs(det3(aw, bw, cw)) ** 2))

terms12_sym = (minus_action_terms(Wr, [0, 2, 4], [1, 3, 5])
               + minus_action_terms(partner_real, [6, 8, 10], [7, 9, 11]))
val12_sym = berezin(gexp_product(terms12_sym), order12)
check("B2.6", "direct symbolic 12-generator joint integral = det3^2 on the "
      "entrywise-real locus",
      is_zero(val12_sym - det3(ar, br, cr) ** 2))

check("B2.7", "r-neutral doubling: exponent pairs (1,1)->(2,2) together; "
      "ratio twice/once = det3, not constant",
      is_zero(l0r ** 2 * (l1r * conjugate(l1r)) ** 2
              - (l0r * l1r * conjugate(l1r)) ** 2)
      and is_zero(count_twice_sym - count_once * det3(ar, br, cr)))

# ----------------------- B3: declared-reading generator-count bookkeeping
check("B3.1", "generator-count bookkeeping: horn m uses 6m generators, read "
      "off the constructed integration orders (m=1: 6; m=2: 12)",
      len(th3 + tb3) == 6 and len(order12) == 12
      and len(order12) == 2 * len(th3 + tb3))

# --------------------------------------------- B4: linear measure collapse
d1, d2, c1, c2 = sp.symbols("d1 d2 c1 c2")
Dm = Matrix([[d1, 0], [0, d2]])
Cm = Matrix([[c1, 0], [0, c2]])
val_rescaled = holo_integral(Dm * M2 * Cm, th2, tb2)
check("B4.1", "diagonal rescale: integral -> (d1 d2 c1 c2) * det M (n=2 symbolic)",
      is_zero(val_rescaled - d1 * d2 * c1 * c2 * M2.det()))

a11, a12, a21, a22 = sp.symbols("a11 a12 a21 a22")
b11, b12, b21, b22 = sp.symbols("b11 b12 b21 b22")
Am = Matrix([[a11, a12], [a21, a22]])
Bm = Matrix([[b11, b12], [b21, b22]])
val_gl = holo_integral(Bm.T * M2 * Am, th2, tb2)
check("B4.2", "general linear redefinition: integral = det(B) det(A) det(M) "
      "(n=2 symbolic scalar action)",
      is_zero(val_gl - Bm.det() * Am.det() * M2.det()))

k1 = det3(1, 0, 0) ** 2 / det3(1, 0, 0)
k2 = det3(2, 0, 0) ** 2 / det3(2, 0, 0)
check("B4.3", "no constant kappa with kappa*det3 = det3^2: witness kappas clash",
      k1 == 1 and k2 == 8 and k1 != k2, detail="kappa witnesses 1 vs 8")

u = sp.Symbol("u")
val_once_scaled = holo_integral((u * eye(3)) * Wr, th3, tb3)
rho = u ** 3
val_twice_scaled = val_once_scaled * holo_integral(
    (conjugate(u) * eye(3)) * partner_real, th3, tb3)
check("B4.4", "uniform rescale: once -> rho*once with rho = u^3, "
      "twice -> |rho|^2*twice (horns split, neither converted)",
      is_zero(val_once_scaled - rho * det3(ar, br, cr))
      and is_zero(val_twice_scaled
                  - rho * conjugate(rho) * det3(ar, br, cr) ** 2))

# ----------------------------------------------------------- B5: controls
l0h = lam(0, ar, br, br)
l1h = lam(1, ar, br, br)
l2h = lam(2, ar, br, br)
check("B5.1", "Hermitian real-intersection control: lam1 = lam2 = a - b, "
      "det3 = lam0 * lam1^2 (all real)",
      is_zero(l1h - l2h) and is_zero(l1h - (ar - br))
      and is_zero(det3(ar, br, br) - l0h * l1h ** 2))

l0n = lam(0, 1, I, 0)
l1n = lam(1, 1, I, 0)
l2n = lam(2, 1, I, 0)
gap = sp.expand_complex(l2n - conjugate(l1n))
d3n = det3(1, I, 0)
grouped = sp.expand_complex(l0n * l1n * conjugate(l1n))
check("B5.2", "off-locus (1,i,0): gap = sqrt(3) - i, det3 = 1 - i, "
      "grouped form differs from det3",
      is_zero(gap - (sqrt(3) - I)) and is_zero(d3n - (1 - I))
      and not is_zero(grouped - d3n))

Wp = W_of(I, 1 + I, I)
val_p = holo_integral(Wp, th3, tb3)
check("B5.3", "pairing-without-reality (i,1+i,i): count-once integral = 1 + 3i, "
      "not real",
      is_zero(val_p - (1 + 3 * I)) and not is_zero(val_p - conjugate(val_p)))

W311 = W_of(3, 1, 1)
v_once = holo_integral(W311, th3, tb3)
terms12_311 = (minus_action_terms(W311, [0, 2, 4], [1, 3, 5])
               + minus_action_terms(W311, [6, 8, 10], [7, 9, 11]))
v_twice = berezin(gexp_product(terms12_311), order12)
check("B5.4", "neither horn forced at (3,1,1): Berezin once = 20, "
      "12-generator twice = 400, both nonzero",
      v_once == 20 and v_twice == 400)

eps = sp.Symbol("eps", positive=True)
a2 = eps / 3
b2_cell = eps / 6
b2_mode = 2 * eps / 6
r_cell = sp.simplify(b2_cell / a2)
r_mode = sp.simplify(b2_mode / a2)
Q_cell = (1 + 2 * r_cell) / 3
Q_mode = (1 + 2 * r_mode) / 3
check("B5.5", "endpoint arithmetic: cell law (r,Q) = (1/2, 2/3); "
      "mode law (r,Q) = (1, 1); both conditional on supplied laws",
      r_cell == Rational(1, 2) and Q_cell == Rational(2, 3)
      and r_mode == 1 and Q_mode == 1)

# ------------------------------------------------- B6: verbatim quote gates
NOTE_GROUPS = quote_groups(NOTE)
BLOCK05_FLAT = flattened(BLOCK05)
SECTIE_FLAT = flattened(SECTIE)
OBLIG_FLAT = flattened(OBLIG)
AXIOMS_FLAT = flattened(AXIOMS)

B6_N = 0


def gate(label, needle, src_flat):
    global B6_N
    n = " ".join(needle.split())
    B6_N += 1
    check(f"B6.{B6_N}", f"source text carries: {label}", n in src_flat)
    B6_N += 1
    check(f"B6.{B6_N}", f"note blockquotes verbatim: {label}",
          in_groups(NOTE_GROUPS, n))


gate(
    "spectral-pairing T3 three-part pairing statement",
    "1. `lam_0 = a + b + c` is real, and its channel `P_1` is K-fixed; "
    "2. `lam_2 = conj(lam_1)`, and the channels `{P_w, P_conj(w)}` form one "
    "two-element K orbit; 3. therefore `det3 = lam_0 * |lam_1|^2` exactly, "
    "with a real singlet factor.",
    src_flat=BLOCK05_FLAT,
)
gate(
    "spectral-pairing license sentence",
    "The modulus-square grouping arises on the doublet factor alone, and it "
    "is licensed by the fixed-point-versus-2-orbit channel structure rather "
    "than imposed.",
    src_flat=BLOCK05_FLAT,
)
gate(
    "spectral-pairing underived graining binary",
    "What remains underived is the slot-count graining: one occupancy slot "
    "per K-orbit versus one slot per channel atom.",
    src_flat=BLOCK05_FLAT,
)
gate(
    "spectral-pairing dial sentence",
    "Neither graining horn is forced here, and `r` remains a dial with "
    "settings `0`, `1/2`, and `1`.",
    src_flat=BLOCK05_FLAT,
)
gate(
    "spectral-pairing probe-status FLAG clause",
    "**FLAG — probe, not derived form:** no Yukawa identification, physical "
    "action, or measure is derived for it, there or here.",
    src_flat=BLOCK05_FLAT,
)
gate(
    "axiom-memo Qualification clause",
    "A choice not fixed by the supplied structure remains a named "
    "conditional or open dependency.",
    src_flat=AXIOMS_FLAT,
)
gate(
    "obligation closure criterion",
    "A closing theorem must derive the physical matter action and its "
    "measure, then distinguish the count-once `det_C`/holomorphic realization "
    "from the count-twice `|det_C|^2`/realified realization without inserting "
    "the desired charged-lepton value or readout dictionary.",
    src_flat=OBLIG_FLAT,
)
gate(
    "section-tie residual independence",
    "The stage-selection residual and the equipartition-granularity residual "
    "are independent. One may specify when K-reality acts without choosing an "
    "energy law, or impose one of the two energy laws without deriving when "
    "the physical action imposes K-reality.",
    src_flat=SECTIE_FLAT,
)

# ------------------------------------- B7: ledger shard filename gates
ROWS = [
    "kcpt_coupling_triple_two_presentation_derivable_class_spectral_pairing_bounded_theorem_note_2026-07-16",
    "koide_first_order_section_tie_vs_outcome_label_residual_localization_bounded_theorem_note_2026-07-11",
    "koide_staggered_first_order_generation_determinant_bounded_theorem_note_2026-06-11",
    "koide_convention_invariant_scalar_selector_doublet_constancy_narrow_theorem_note_2026-07-12",
    "acphilambda_occupancy_determinant_power_split_exact_support_note_2026-07-04",
    "acphilambda_fermionic_realification_pfaffian_power_identity_narrow_theorem_note_2026-07-12",
    "ac_orbit_occupancy_statistical_grain_derivation_obligation",
]
for i, rid in enumerate(ROWS, 1):
    shard = ROOT / "docs" / "audit" / "data" / "ledger" / rid[:2] / f"{rid}.json"
    check(f"B7.{i}", f"ledger shard file exists: {rid}", shard.is_file())

# ------------------------------------------------------ B8: note hygiene
RAW = (ROOT / NOTE).read_text(encoding="utf-8")
B8_N = 0

SECTIONS = [
    "## Purpose",
    "## Supplied objects and consumed readings",
    "### Berezin conventions (pinned)",
    "## Claims",
    "### Berezin realization exactness under the pinned convention (T1, exact)",
    "### Sector-selective realization on entrywise-real triples (T2, bounded)",
    "### The count binary as a generator-count binary (T3, declared reading)",
    "### Linear measure collapse on the finite probe surface (T4, bounded negative)",
    "## Gated controls",
    "## Negative controls",
    "## No-Go Discipline Gate",
    "### N1 —",
    "### N2 —",
    "### N3 —",
    "### N4 —",
    "### N5 —",
    "### N6 —",
    "### N7 —",
    "### N8 —",
    "## Non-claims",
    "## Dependency roles and status boundary",
    "## Dependencies",
    "### Non-citation context handles",
    "## Verification",
    "**No check passes by literal stipulation.**",
    "**Status authority:** independent audit lane only.",
]
for s in SECTIONS:
    B8_N += 1
    check(f"B8.{B8_N}", f"note carries: {s}", s in RAW)

FORBIDDEN = [
    "exhaust",
    "only route",
    "last route",
    "closes the",
    "bijection",
    "fiber",
    "multiplicity bit",
    "grain bit",
    "final",
    "decides m",
    "derives the physical action",
    "forces r",
    "derives r",
    "selects r",
    "retained",
]
RAW_LOW = RAW.lower()
for phrase in FORBIDDEN:
    B8_N += 1
    check(f"B8.{B8_N}", f"forbidden phrase absent: '{phrase}'", phrase not in RAW_LOW)

STATUS_SNAPSHOTS = [
    "unaudited at writing",
    "citation grades at writing",
    "audited_renaming",
    "honest auditor read",
    "registered point",
]
for phrase in STATUS_SNAPSHOTS:
    B8_N += 1
    check(
        f"B8.{B8_N}",
        f"source-authored status/value snapshot absent: '{phrase}'",
        phrase not in RAW_LOW,
    )

B8_N += 1
check(
    f"B8.{B8_N}",
    "no bare decimal literals in the note",
    re.search(r"\d\.\d", RAW) is None,
)

DEPS = [
    "MINIMAL_AXIOMS_2026-06-29.md",
    "KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md",
    "KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md",
    "KOIDE_FIRST_ORDER_SECTION_TIE_VS_OUTCOME_LABEL_RESIDUAL_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-07-11.md",
]
for dep in DEPS:
    B8_N += 1
    check(f"B8.{B8_N}", f"markdown dependency link present: {dep}", f"]({dep})" in RAW)

CONTEXT_HANDLES = [
    "AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md",
    "ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_EXACT_SUPPORT_NOTE_2026-07-04.md",
    "ACPHILAMBDA_FERMIONIC_REALIFICATION_PFAFFIAN_POWER_IDENTITY_NARROW_THEOREM_NOTE_2026-07-12.md",
    "KOIDE_CONVENTION_INVARIANT_SCALAR_SELECTOR_DOUBLET_CONSTANCY_NARROW_THEOREM_NOTE_2026-07-12.md",
]
for handle in CONTEXT_HANDLES:
    B8_N += 1
    check(
        f"B8.{B8_N}",
        f"non-citation context handle is backticked and unlinked: {handle}",
        f"`{handle}`" in RAW and f"]({handle})" not in RAW,
    )

B8_N += 1
check(
    f"B8.{B8_N}",
    "every cited or handled doc path exists",
    all((ROOT / p).is_file() for p in [NOTE, RUNNER, BLOCK05, SECTIE, STAG,
                                       OBLIG, AXIOMS])
    and all((ROOT / "docs" / h).is_file() for h in CONTEXT_HANDLES)
    and all((ROOT / "docs" / d).is_file() for d in DEPS),
)

# ------------------------------------------------------------------ summary
print(f"PATH note={NOTE}")
print(f"PATH runner={RUNNER}")
print(f"PATH cache={CACHE}")
print(
    "FLAGS: R1b supplied corner surface; R2b consumed pairing license with "
    "source-side premise weight (row status pipeline-derived); R3b probe, "
    "not derived form; R4b declared Berezin probe surface, not the physical "
    "action or measure; R5b declared count-binary reading, not an "
    "equivalence; T4 scoped to linear generator redefinitions; B5 endpoint "
    "arithmetic conditional on supplied granularity laws; r remains a dial "
    "(0, 1/2, 1); no graining horn selected"
)
if FAILURES:
    print("FAILED CHECKS: " + ", ".join(FAILURES))
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
