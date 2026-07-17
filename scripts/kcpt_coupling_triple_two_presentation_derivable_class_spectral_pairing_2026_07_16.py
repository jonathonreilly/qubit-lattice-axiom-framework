#!/usr/bin/env python3
"""Coupling-triple two-presentation derivable class + spectral pairing checks.

Paired note:
docs/KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md

Blocks:
  V1 corner carrier and the two pinned involutions (entrywise K vs adjoint),
     with residual identities pinning each fixed locus exactly
  V2 determinant factorization, character-projector swap structure, and the
     channel-eigenvalue association
  V3 real-triple spectral pairing, exact pairing-gap closed form and
     equal-imaginary-parts locus, sector-selective modulus grouping,
     negative control with exact values, r-neutral positive control
  V4 Hermitian section: Brannen spectrum, delta -> -delta action,
     permutation identity, delta-evenness, fixed set delta = 0 mod pi,
     registered-point non-fixedness
  V5 locus separation witnesses, intersection arithmetic, Wirtinger and
     Laplacian controls, holomorphic-surface harmonicity
  V6 section-tie endpoint arithmetic (both conditional laws, neither derived)
  V7 verbatim quote gates: sources carry the consumed sentences and the note
     quotes them in blockquotes
  V8 ledger shard filename gates (timeless: existence only, no status pins)
  V9 note hygiene: section presence, forbidden-phrase absence, no bare
     decimal literals, markdown dependency links

All algebra is exact sympy. No floats. Exit 1 on any failure.
"""

import re
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

NOTE = (
    "docs/KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_"
    "SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md"
)
RUNNER = (
    "scripts/kcpt_coupling_triple_two_presentation_derivable_class_"
    "spectral_pairing_2026_07_16.py"
)
CACHE = (
    "logs/runner-cache/kcpt_coupling_triple_two_presentation_derivable_"
    "class_spectral_pairing_2026_07_16.txt"
)

KCPT = (
    "docs/KCPT_ORBIT_CONSTANT_REGISTERED_OCCUPANCY_WEIGHTS_DERIVABLE_"
    "PROTOCOL_CLASS_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
SECTIE = (
    "docs/KOIDE_FIRST_ORDER_SECTION_TIE_VS_OUTCOME_LABEL_RESIDUAL_"
    "LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-07-11.md"
)
OBLIG = "docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md"
W1B = (
    "docs/ACPHILAMBDA_OCCUPANCY_GRAIN_RULE_CLASS_UNIVERSALITY_BOUNDED_"
    "THEOREM_NOTE_2026-07-11.md"
)
STAG = (
    "docs/KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_"
    "THEOREM_NOTE_2026-06-11.md"
)
SEL = (
    "docs/KOIDE_CONVENTION_INVARIANT_SCALAR_SELECTOR_DOUBLET_CONSTANCY_"
    "NARROW_THEOREM_NOTE_2026-07-12.md"
)
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
    e = sp.expand(sp.expand_trig(sp.expand_complex(sp.expand(expr))))
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
    n = " ".join(needle.split())
    return any(n in g for g in groups)


# ---------------------------------------------------------------- V1: carrier
I3 = sp.eye(3)
C = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
C2 = C * C


def Wf(x, y, z):
    return x * I3 + y * C + z * C2


ar_, ai_, br_, bi_, cr_, ci_ = sp.symbols("ar ai br bi cr ci", real=True)
a = ar_ + sp.I * ai_
b = br_ + sp.I * bi_
c = cr_ + sp.I * ci_
W = Wf(a, b, c)

check("V1.1", "C is a real 0/1 integer matrix", all(e in (0, 1) for e in C))
check("V1.2", "C^3 = I", C ** 3 == I3)
check("V1.3", "C^T = C^2", C.T == C2)
check(
    "V1.4",
    "entrywise K: conj(W(a,b,c)) = W(conj a, conj b, conj c)",
    mat_zero(W.conjugate() - Wf(sp.conjugate(a), sp.conjugate(b), sp.conjugate(c))),
)
check(
    "V1.5",
    "adjoint: W(a,b,c)^dagger = W(conj a, conj c, conj b)",
    mat_zero(W.H - Wf(sp.conjugate(a), sp.conjugate(c), sp.conjugate(b))),
)
W012 = Wf(0, 1, 2)
check(
    "V1.6",
    "involutions differ generically at witness (a,b,c)=(0,1,2)",
    W012.conjugate() == Wf(0, 1, 2)
    and W012.H == Wf(0, 2, 1)
    and W012.conjugate() != W012.H,
)
Wbc = Wf(a, b, b)
check("V1.7", "involutions agree exactly at b = c", mat_zero(Wbc.conjugate() - Wbc.H))
resK = W.conjugate() - W
check(
    "V1.8",
    "K-residual identity: conj(W) - W = -2i(Im a*I + Im b*C + Im c*C^2)",
    mat_zero(resK + 2 * sp.I * (ai_ * I3 + bi_ * C + ci_ * C2)),
)
check(
    "V1.9",
    "K-residual entries separate: (0,0) = -2i Im a, (0,1) = -2i Im b, "
    "(0,2) = -2i Im c; vanishing pins entrywise-real exactly",
    is_zero(resK[0, 0] + 2 * sp.I * ai_)
    and is_zero(resK[0, 1] + 2 * sp.I * bi_)
    and is_zero(resK[0, 2] + 2 * sp.I * ci_),
)
resH = W.H - W
check(
    "V1.10",
    "adjoint-residual entries: (0,0) = -2i Im a, (0,1) = conj(c) - b, "
    "(0,2) = conj(b) - c; vanishing pins a real and c = conj(b) exactly",
    is_zero(resH[0, 0] + 2 * sp.I * ai_)
    and is_zero(resH[0, 1] - (sp.conjugate(c) - b))
    and is_zero(resH[0, 2] - (sp.conjugate(b) - c)),
)
resD = W.conjugate() - W.H
check(
    "V1.11",
    "involution-difference residual: conj(W) - W^dagger = "
    "(conj(b) - conj(c))*(C - C^2); vanishing pins b = c exactly",
    mat_zero(resD - (sp.conjugate(b) - sp.conjugate(c)) * (C - C2)),
)

# ------------------------------------------- V2: determinant and projectors
w = sp.Rational(-1, 2) + sp.sqrt(3) / 2 * sp.I
wc = sp.conjugate(w)
lams = [sp.expand(a + b * w ** k + c * w ** (2 * k)) for k in range(3)]

check(
    "V2.1",
    "det W = lam0*lam1*lam2",
    is_zero(W.det() - lams[0] * lams[1] * lams[2]),
)
check(
    "V2.2",
    "det W = a^3 + b^3 + c^3 - 3abc",
    is_zero(W.det() - (a ** 3 + b ** 3 + c ** 3 - 3 * a * b * c)),
)

P = {}
for chi in (sp.Integer(1), w, wc):
    P[chi] = sp.expand((I3 + sp.conjugate(chi) * C + sp.conjugate(chi) ** 2 * C2) / 3)

check(
    "V2.3",
    "character projectors resolve the identity",
    mat_zero(P[1] + P[w] + P[wc] - I3),
)
check("V2.4", "K fixes the singlet projector P_1", mat_zero(P[1].conjugate() - P[1]))
check(
    "V2.5",
    "K swaps P_w <-> P_conj(w)",
    mat_zero(P[w].conjugate() - P[wc]) and mat_zero(P[wc].conjugate() - P[w]),
)
check(
    "V2.6",
    "integer-cycle basis {I, C, C^2} is presentation-shared",
    I3.conjugate() == I3 and C.conjugate() == C and C2.conjugate() == C2,
)
orth = all(
    mat_zero(sp.expand(P[x] * P[y]) - (P[x] if x == y else sp.zeros(3, 3)))
    for x in P
    for y in P
)
check("V2.7", "projector idempotence and mutual orthogonality", orth)
chis = [sp.Integer(1), w, wc]
assoc = all(
    mat_zero(sp.expand(W * P[chis[k]] - lams[k] * P[chis[k]])) for k in range(3)
)
check(
    "V2.8",
    "channel-eigenvalue association: W*P_(w^k) = lam_k*P_(w^k) for k = 0, 1, 2",
    assoc,
)

# --------------------------------------- V3: real-triple spectral pairing
x_, y_, z_ = sp.symbols("x y z", real=True)
lamsR = [sp.expand(x_ + y_ * w ** k + z_ * w ** (2 * k)) for k in range(3)]
det3R = x_ ** 3 + y_ ** 3 + z_ ** 3 - 3 * x_ * y_ * z_
mod1sq = sp.expand(sp.re(lamsR[1]) ** 2 + sp.im(lamsR[1]) ** 2)

check("V3.1", "lam0 = a+b+c is real on entrywise-real triples", is_zero(sp.im(lamsR[0])))
check(
    "V3.2",
    "lam2 = conj(lam1) on entrywise-real triples",
    is_zero(lamsR[2] - sp.conjugate(lamsR[1])),
)
check(
    "V3.3",
    "det3 = lam0*|lam1|^2 exactly on entrywise-real triples",
    is_zero(det3R - lamsR[0] * mod1sq),
)
lam1_pt = sp.expand_complex(1 + sp.I * w)
lam2_pt = sp.expand_complex(1 + sp.I * w ** 2)
det_pt = sp.expand_complex(1 + sp.I ** 3)
pair_gap = sp.simplify(sp.expand_complex(lam2_pt - sp.conjugate(lam1_pt)))
check(
    "V3.4",
    "negative control (1,i,0): exact values computed, pairing fails and "
    "det3 is not real",
    is_zero(pair_gap - (sp.sqrt(3) - sp.I))
    and is_zero(det_pt - (1 - sp.I))
    and sp.im(det_pt) != 0,
    detail="lam2-conj(lam1)=sqrt(3)-i, det3=1-i",
)
check(
    "V3.5",
    "|det3|^2 = lam0^2*|lam1|^4 on entrywise-real triples (r-neutral)",
    is_zero(sp.expand(det3R ** 2) - sp.expand(lamsR[0] ** 2 * mod1sq ** 2)),
)
gap_full = sp.expand_complex(lams[2] - sp.conjugate(lams[1]))
gap_w_form = sp.expand_complex(2 * sp.I * (ai_ + bi_ * w ** 2 + ci_ * w))
gap_closed = sp.sqrt(3) * (bi_ - ci_) + sp.I * (2 * ai_ - bi_ - ci_)
check(
    "V3.6",
    "pairing-gap closed form: lam2 - conj(lam1) = 2i(Im a + Im b*w^2 + Im c*w) "
    "= sqrt(3)(Im b - Im c) + i(2 Im a - Im b - Im c)",
    is_zero(gap_full - gap_w_form) and is_zero(gap_full - gap_closed),
)
check(
    "V3.7",
    "gap real/imag parts separate: Re = sqrt(3)(Im b - Im c), "
    "Im = 2 Im a - Im b - Im c; vanishing pins Im a = Im b = Im c exactly",
    is_zero(sp.re(gap_full) - sp.sqrt(3) * (bi_ - ci_))
    and is_zero(sp.im(gap_full) - (2 * ai_ - bi_ - ci_)),
)
eq_locus = {bi_: ai_, ci_: ai_}
check(
    "V3.8",
    "on the equal-imaginary-parts locus the pairing holds and "
    "det3 = lam0*|lam1|^2",
    is_zero(gap_full.subs(eq_locus))
    and is_zero(
        (W.det() - lams[0] * lams[1] * sp.conjugate(lams[1])).subs(eq_locus)
    ),
)
check(
    "V3.9",
    "Im lam0 = Im a + Im b + Im c = 3*Im a on the pairing locus: singlet "
    "reality cuts the pairing locus exactly to the entrywise-real triples",
    is_zero(sp.im(lams[0]) - (ai_ + bi_ + ci_))
    and is_zero(sp.im(lams[0]).subs(eq_locus) - 3 * ai_),
)
wa_, wb_, wc2_ = sp.I, 1 + sp.I, sp.I
wlam = [sp.expand_complex(wa_ + wb_ * w ** k + wc2_ * w ** (2 * k)) for k in range(3)]
wdet = sp.expand_complex(wa_ ** 3 + wb_ ** 3 + wc2_ ** 3 - 3 * wa_ * wb_ * wc2_)
check(
    "V3.10",
    "witness (i,1+i,i): pairing holds off the entrywise-real locus with "
    "non-real grouped det3 = 1+3i",
    is_zero(wlam[2] - sp.conjugate(wlam[1]))
    and is_zero(wdet - (1 + 3 * sp.I))
    and sp.im(wlam[0]) != 0,
    detail="lam0=1+3i, det3=1+3i",
)

# --------------------------------- V4: Hermitian section and delta action
aH, R_, d_ = sp.symbols("aH R delta", real=True)
bH = R_ * sp.exp(sp.I * d_)
cH = R_ * sp.exp(-sp.I * d_)
lamsH = [sp.expand(aH + bH * w ** k + cH * w ** (2 * k)) for k in range(3)]

for k in range(3):
    target = aH + 2 * R_ * sp.cos(d_ + 2 * sp.pi * k / 3)
    check(
        f"V4.{k + 1}",
        f"Brannen spectrum lam_{k} = a + 2R cos(delta + 2*pi*{k}/3)",
        is_zero(lamsH[k] - target),
    )

WH = Wf(aH, bH, cH)
check(
    "V4.4",
    "K on the Hermitian section acts as delta -> -delta",
    mat_zero(WH.conjugate() - WH.subs(d_, -d_)),
)
check("V4.5", "lam0 is delta-even on the section", is_zero(lamsH[0].subs(d_, -d_) - lamsH[0]))
check("V4.6", "lam1(-delta) = lam2(delta)", is_zero(lamsH[1].subs(d_, -d_) - lamsH[2]))
check("V4.7", "lam2(-delta) = lam1(delta)", is_zero(lamsH[2].subs(d_, -d_) - lamsH[1]))
detH = sp.expand(aH ** 3 + bH ** 3 + cH ** 3 - 3 * aH * bH * cH)
check(
    "V4.8",
    "det3 is delta-even on the section (class function on unordered pairs)",
    is_zero(detH.subs(d_, -d_) - detH),
)
perm = all(is_zero(lamsH[k].subs(d_, -d_) - lamsH[(3 - k) % 3]) for k in range(3))
check("V4.9", "permutation identity lam_k(-delta) = lam_{(3-k) mod 3}(delta)", perm)
d0 = sp.Rational(2, 9)
WH_p = WH.subs(d_, d0)
WH_m = WH.subs(d_, -d0)
check(
    "V4.10",
    "registered point delta=2/9: K maps W(2/9) to W(-2/9), a different "
    "matrix; the point is not K-fixed and the unordered pair {2/9, -2/9} "
    "is the K-orbit",
    mat_zero(WH_p.conjugate() - WH_m) and not mat_zero(WH_p - WH_m),
)
check(
    "V4.11",
    "section fixed set is delta = 0 mod pi: W is K-fixed at delta in "
    "{0, pi}, not at the registered point",
    mat_zero(WH.subs(d_, 0).conjugate() - WH.subs(d_, 0))
    and mat_zero(WH.subs(d_, sp.pi).conjugate() - WH.subs(d_, sp.pi))
    and not mat_zero(WH_p.conjugate() - WH_p),
)

# ------------------------- V5: locus separation, Wirtinger, harmonicity
pa, pb, pc = sp.Integer(1), sp.I, -sp.I
check(
    "V5.1",
    "(1,i,-i) is on the Hermitian section but not entrywise-real",
    sp.simplify(pc - sp.conjugate(pb)) == 0
    and sp.im(pa) == 0
    and sp.im(pb) != 0,
)
qa, qb, qc = sp.Integer(1), sp.Integer(2), sp.Integer(3)
check(
    "V5.2",
    "(1,2,3) is entrywise-real but off the Hermitian section",
    all(sp.im(t) == 0 for t in (qa, qb, qc)) and qc != sp.conjugate(qb),
)
bS = br_ + sp.I * bi_
gap = sp.expand_complex(sp.conjugate(bS) - bS)
check(
    "V5.3",
    "intersection (c = conj(b) and entrywise-real) yields real b = c",
    is_zero(gap.subs(bi_, 0)) and sp.simplify(gap.subs(bi_, 1)) != 0,
)
ars, bs, bbs, cs = sp.symbols("ars bs bbs cs")
F = ars ** 3 + bs ** 3 + bbs ** 3 - 3 * ars * bs * bbs
check(
    "V5.4",
    "Wirtinger d^2 det3 / dbs dbbs = -3a on the section coordinates",
    sp.simplify(sp.diff(F, bs, bbs) + 3 * ars) == 0,
)
xr, yr = sp.symbols("xr yr", real=True)
g = F.subs({bs: xr + sp.I * yr, bbs: xr - sp.I * yr})
check(
    "V5.5",
    "realified section Laplacian = -12a",
    is_zero(sp.diff(g, xr, 2) + sp.diff(g, yr, 2) + 12 * ars),
)
h = ars ** 3 + (xr + sp.I * yr) ** 3 + cs ** 3 - 3 * ars * (xr + sp.I * yr) * cs
check(
    "V5.6",
    "holomorphic surface (b,c independent) is harmonic in (Re b, Im b)",
    sp.simplify(sp.diff(h, xr, 2) + sp.diff(h, yr, 2)) == 0,
)

# --------------------------- V6: section-tie endpoint arithmetic (gated)
eps = sp.symbols("epsilon", positive=True)
a2 = eps / 3
r_cell = sp.simplify((eps / 6) / a2)
r_mode = sp.simplify((2 * eps / 6) / a2)


def q_of_r(r):
    return sp.simplify(sp.Rational(1, 3) + sp.Rational(2, 3) * r)


check("V6.1", "per-outcome-cell law gives r = 1/2 (conditional)", r_cell == sp.Rational(1, 2))
check("V6.2", "per-real-mode law gives r = 1 (conditional)", r_mode == 1)
check("V6.3", "Q(1/2) = 2/3", q_of_r(sp.Rational(1, 2)) == sp.Rational(2, 3))
check("V6.4", "Q(1) = 1", q_of_r(sp.Integer(1)) == 1)

# ------------------------------------------------- V7: verbatim quote gates
NOTE_GROUPS = quote_groups(NOTE)
KCPT_FLAT = flattened(KCPT)
KCPT_GROUPS = quote_groups(KCPT)
SECTIE_FLAT = flattened(SECTIE)
OBLIG_FLAT = flattened(OBLIG)
W1B_GROUPS = quote_groups(W1B)
STAG_FLAT = flattened(STAG)
SEL_FLAT = flattened(SEL)
AXIOMS_FLAT = flattened(AXIOMS)

V7_N = 0


def gate(label, needle, src_flat=None, src_groups=None):
    global V7_N
    n = " ".join(needle.split())
    V7_N += 1
    if src_groups is not None:
        check(f"V7.{V7_N}", f"source quote-group carries: {label}", in_groups(src_groups, n))
    else:
        check(f"V7.{V7_N}", f"source text carries: {label}", n in src_flat)
    V7_N += 1
    check(f"V7.{V7_N}", f"note blockquotes verbatim: {label}", in_groups(NOTE_GROUPS, n))


gate(
    "KCPT L-K2 comparison opening",
    "Hold that record data and every other named clause fixed, and compare "
    "the supplied Pauli/corner presentation",
    src_flat=KCPT_FLAT,
)
gate(
    "KCPT L-K2 two-presentation sentence",
    "By L-K1 these are two presentations of the same named real-algebra structure.",
    src_flat=KCPT_FLAT,
)
gate(
    "KCPT L-K2 sign-non-selectability conclusion",
    "The two states have the same normalization and satisfy the same named "
    "clauses, but the sign of `eps` is exchanged. No named supplied condition "
    "selects one sign. By the quoted Qualification clause, a nonzero K-odd "
    "initial datum therefore remains a named conditional or open dependency; "
    "it is not derivable. Under declared reading R2, derivable initial data "
    "is K-real.",
    src_flat=KCPT_FLAT,
)
gate(
    "KCPT declared reading R2 with FLAG",
    "**R2 — K-real derivable initial data.** Derivable initial data is "
    "K-real. **FLAG — two-model mechanism:** the entrywise-conjugate "
    "presentations in L-K2 satisfy the same named clauses and exchange every "
    "K-odd seed. The memo's live Qualification leaves the unfixed choice "
    "conditional/open.",
    src_flat=KCPT_FLAT,
)
gate(
    "KCPT supplied corner carrier",
    "Let the corner-triplet factor be `C^3`, with the supplied real cyclic "
    "permutation `C`, `C^3=I_3`.",
    src_flat=KCPT_FLAT,
)
gate(
    "KCPT entrywise-conjugation convention",
    "In the canonical joint basis, `K` is entrywise conjugation.",
    src_flat=KCPT_FLAT,
)
gate(
    "axiom-memo Qualification clause",
    "A choice not fixed by the supplied structure remains a named "
    "conditional or open dependency.",
    src_flat=AXIOMS_FLAT,
)
gate(
    "section-tie weight-stage definition",
    "1. **weight-stage K-reality:** impose `c = conj(b)` on the coupling "
    "section before classifying the weight's analytic dependence;",
    src_flat=SECTIE_FLAT,
)
gate(
    "section-tie outcome-stage definition",
    "2. **outcome-stage K-reality:** keep `b,c` independent through the "
    "holomorphic calculation and impose K-real grouping only on the "
    "registered data afterward.",
    src_flat=SECTIE_FLAT,
)
gate(
    "section-tie residual independence",
    "The stage-selection residual and the equipartition-granularity residual "
    "are independent. One may specify when K-reality acts without choosing an "
    "energy law, or impose one of the two energy laws without deriving when "
    "the physical action imposes K-reality.",
    src_flat=SECTIE_FLAT,
)
gate(
    "section-tie Osterwalder–Schrader sentence",
    "A future Osterwalder–Schrader theorem could close the first while "
    "leaving the second open.",
    src_flat=SECTIE_FLAT,
)
gate(
    "section-tie preserved N6 route",
    "No new axiom or primitive is required. A framework-native theorem for "
    "the full first-order action could decide the K-reality stage. A separate "
    "derivation of the weighting/equipartition law would still be needed to "
    "select the value.",
    src_flat=SECTIE_FLAT,
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
    "staggered Fact-3 Wirtinger control",
    "on the K-real line `c = b̄` the Wirtinger derivative "
    "`∂² det₃ / ∂b ∂b̄ = −3a` (Laplacian `−12a`)",
    src_flat=STAG_FLAT,
)
gate(
    "selector unordered-PVM counterexample sentence",
    "Thus the unlabeled three-block partition is convention-stable and "
    "resolves all three sectors without privileging either doublet member. "
    "Convention freeness alone does not derive ORBIT-INDEXING or identify "
    "the conjugate sectors as one record content.",
    src_flat=SEL_FLAT,
)

W1B_NEEDLE = " ".join(
    (
        "The charged-lepton 2-sector occupancy surface is the K/CPT-orbit "
        "partition `{singlet sector, doublet orbit}` with occupancy "
        "distribution `(p_s,p_d)`, `p_s+p_d=1`, where the equal-power-per-block "
        "grain reads `r=1/2` at `p_s=p_d`."
    ).split()
)
V7_N += 1
check(
    f"V7.{V7_N}",
    "W1b declaration in W1b note quote-group",
    in_groups(W1B_GROUPS, W1B_NEEDLE),
)
V7_N += 1
check(
    f"V7.{V7_N}",
    "W1b declaration in KCPT note quote-group",
    in_groups(KCPT_GROUPS, W1B_NEEDLE),
)
V7_N += 1
check(
    f"V7.{V7_N}",
    "W1b declaration blockquoted in this note",
    in_groups(NOTE_GROUPS, W1B_NEEDLE),
)

# ------------------------------------- V8: ledger shard filename gates
ROWS = [
    "kcpt_orbit_constant_registered_occupancy_weights_derivable_protocol_class_bounded_theorem_note_2026-07-12",
    "koide_first_order_section_tie_vs_outcome_label_residual_localization_bounded_theorem_note_2026-07-11",
    "koide_staggered_first_order_generation_determinant_bounded_theorem_note_2026-06-11",
    "koide_convention_invariant_scalar_selector_doublet_constancy_narrow_theorem_note_2026-07-12",
    "acphilambda_occupancy_grain_rule_class_universality_bounded_theorem_note_2026-07-11",
    "kcpt_orbit_constancy_and_determinant_character_boundary_supplied_context_bridge_note_2026-07-04",
    "acphilambda_record_outcome_orbit_occupancy_non_supply_no_go_note_2026-07-04",
    "acphilambda_occupancy_determinant_power_split_exact_support_note_2026-07-04",
    "acphilambda_fermionic_realification_pfaffian_power_identity_narrow_theorem_note_2026-07-12",
    "ac_orbit_occupancy_statistical_grain_derivation_obligation",
]
for i, rid in enumerate(ROWS, 1):
    shard = ROOT / "docs" / "audit" / "data" / "ledger" / rid[:2] / f"{rid}.json"
    check(f"V8.{i}", f"ledger shard file exists: {rid}", shard.is_file())

# ------------------------------------------------------ V9: note hygiene
RAW = (ROOT / NOTE).read_text(encoding="utf-8")
V9_N = 0

SECTIONS = [
    "## Purpose",
    "## Supplied objects and consumed readings",
    "### Involution conventions (pinned)",
    "## Claims",
    "### T1 —",
    "### T2 —",
    "### T3 —",
    "### T4 —",
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
    "## Citation grades at writing",
    "## Honest auditor read",
    "## Dependencies",
    "## Verification",
    "**No check passes by literal stipulation.**",
    "**Status authority:** independent audit lane only.",
]
for s in SECTIONS:
    V9_N += 1
    check(f"V9.{V9_N}", f"note carries: {s}", s in RAW)

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
]
RAW_LOW = RAW.lower()
for phrase in FORBIDDEN:
    V9_N += 1
    check(f"V9.{V9_N}", f"forbidden phrase absent: '{phrase}'", phrase not in RAW_LOW)

V9_N += 1
check(
    f"V9.{V9_N}",
    "no bare decimal literals in the note",
    re.search(r"\d\.\d", RAW) is None,
)

DEPS = [
    "MINIMAL_AXIOMS_2026-06-29.md",
    "KCPT_ORBIT_CONSTANT_REGISTERED_OCCUPANCY_WEIGHTS_DERIVABLE_PROTOCOL_CLASS_BOUNDED_THEOREM_NOTE_2026-07-12.md",
    "KOIDE_FIRST_ORDER_SECTION_TIE_VS_OUTCOME_LABEL_RESIDUAL_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md",
    "KOIDE_CONVENTION_INVARIANT_SCALAR_SELECTOR_DOUBLET_CONSTANCY_NARROW_THEOREM_NOTE_2026-07-12.md",
    "ACPHILAMBDA_OCCUPANCY_GRAIN_RULE_CLASS_UNIVERSALITY_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md",
    "ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md",
    "AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md",
    "ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_EXACT_SUPPORT_NOTE_2026-07-04.md",
    "ACPHILAMBDA_FERMIONIC_REALIFICATION_PFAFFIAN_POWER_IDENTITY_NARROW_THEOREM_NOTE_2026-07-12.md",
]
for dep in DEPS:
    V9_N += 1
    check(f"V9.{V9_N}", f"markdown dependency link present: {dep}", f"]({dep})" in RAW)

# ------------------------------------------------------------------ summary
print(f"PATH note={NOTE}")
print(f"PATH runner={RUNNER}")
print(f"PATH cache={CACHE}")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(
    "FLAGS: R1c supplied corner surface; R2c consumed unaudited reading; "
    "R4c declared extension reading (coupling slot); T2 conditional on "
    "R2c+R4c; V6 endpoints conditional on their granularity laws; r remains "
    "a dial (0, 1/2, 1); delta=2/9 registered, not derived"
)
if FAILURES:
    print("FAILED CHECKS: " + ", ".join(FAILURES))
if FAIL:
    raise SystemExit(1)
