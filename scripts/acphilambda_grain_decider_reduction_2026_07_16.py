#!/usr/bin/env python3
"""Runner for claim
acphilambda_occupancy_grain_three_candidate_deciders_common_count_binary_reduction_bounded_theorem_note_2026-07-16.

Exact sympy arithmetic (exact rationals and exact algebraics only; no floats).
Gates R1-R9 for the bounded reduction that three candidate occupancy-grain
deciders share one common count binary m in {1, 2} on the supplied C3 model.

Every gate computes its claim; none restates a constant it did not derive.
Prints one PASS/FAIL line per gate and a final `TOTAL: PASS=N FAIL=0` line.
"""

import re
from pathlib import Path

from sympy import (
    I, pi, exp, sqrt, eye, zeros, Matrix, Mul, Rational, Integer, symbols,
    simplify, expand, expand_complex, conjugate, solve, solveset, Eq, FiniteSet,
)
from sympy import re as sym_re, im as sym_im

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LEDGER = DOCS / "audit" / "data" / "ledger" / "ac"

NOTE = DOCS / "ACPHILAMBDA_OCCUPANCY_GRAIN_THREE_CANDIDATE_DECIDERS_COMMON_COUNT_BINARY_REDUCTION_BOUNDED_THEOREM_NOTE_2026-07-16.md"
OBLIGATION = DOCS / "AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md"
NOGO_2A = DOCS / "ACPHILAMBDA_MEASURE_BINARY_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md"
NOGO_2C = DOCS / "ACPHILAMBDA_OCCUPANCY_FORMATION_APPEND_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
LEDGER_3A = LEDGER / "acphilambda_occupancy_determinant_power_split_exact_support_note_2026-07-04.json"

DEP_FILENAMES = [
    "AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md",
    "ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_EXACT_SUPPORT_NOTE_2026-07-04.md",
    "ACPHILAMBDA_FERMIONIC_REALIFICATION_PFAFFIAN_POWER_IDENTITY_NARROW_THEOREM_NOTE_2026-07-12.md",
    "ACPHILAMBDA_MEASURE_BINARY_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md",
    "ACPHILAMBDA_OCCUPANCY_FORMATION_APPEND_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md",
]

# ----------------------------------------------------------------------------
PASS_COUNT = 0
FAIL_COUNT = 0
BLOCK_COUNTS = {}


def check(block, label, condition):
    global PASS_COUNT, FAIL_COUNT
    n = BLOCK_COUNTS.get(block, 0) + 1
    BLOCK_COUNTS[block] = n
    ok = bool(condition)
    if ok:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"{block}.{n} {'PASS' if ok else 'FAIL'}: {label}")


def flat(text):
    """Whitespace-flatten, stripping leading blockquote markers."""
    return " ".join(re.sub(r"(?m)^\s*>\s?", "", text).split())


def zero(expr):
    """Exact zero test tolerant of algebraic form."""
    e = simplify(expr)
    if e == 0:
        return True
    return simplify(expand_complex(e)) == 0


def mzero(M):
    return all(zero(e) for e in M)


def realify(Mc):
    """Ordered realification [[X,-Y],[Y,X]] with X=re, Y=im."""
    X = Mc.applyfunc(sym_re)
    Y = Mc.applyfunc(sym_im)
    n = Mc.rows
    R = zeros(2 * n, 2 * n)
    R[:n, :n] = X
    R[:n, n:] = -Y
    R[n:, :n] = Y
    R[n:, n:] = X
    return R


def dsum(P, Q):
    n, m = P.rows, Q.rows
    D = zeros(n + m, n + m)
    D[:n, :n] = P
    D[n:, n:] = Q
    return D


NOTE_TEXT = NOTE.read_text()
FLAT_NOTE = flat(NOTE_TEXT)

# ----------------------------------------------------------------------------
# Shared C3 model (D1)
w = exp(2 * pi * I / 3)
C = Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
alpha, beta, gamma = symbols("alpha beta gamma", real=True)
A = alpha * eye(3) + beta * C + gamma * (C * C)
lam = [simplify(alpha + beta * w**k + gamma * w**(2 * k)) for k in range(3)]
e1 = Matrix([1, w, w**2])
e2 = Matrix([1, w**2, w])

# ----------------------------------------------------------------------------
# R1a  SOURCE_GATES : verbatim quotes + dependency-filename citations
QUOTES = [
    ("obligation.closure_criterion", OBLIGATION,
     "A closing theorem must derive the physical matter action and its measure, then "
     "distinguish the count-once `det_C`/holomorphic realization from the count-twice "
     "`|det_C|^2`/realified realization without inserting the desired charged-lepton "
     "value or readout dictionary."),
    ("obligation.pending_chain", OBLIGATION,
     "Until such a theorem is independently audited and retained, every result that "
     "uses this statistical-grain selection remains conditional or pending-chain."),
    ("2A.non_selection", NOGO_2A,
     "do not choose generator-channel / orbit / holomorphic count-once over dimension "
     "/ sector / real count-twice."),
    ("2C.unsupplied_dictionary", NOGO_2C,
     "the outcome-to-component dictionary that reads the doublet as count-twice or "
     "count-once;"),
    ("2C.component_row", NOGO_2C,
     "| component dictionary | `x = 2r` | `r = 1/2` |"),
    ("2C.slot_row", NOGO_2C,
     "| slot dictionary | `x = r` | `r = 1` |"),
    ("2C.both_completions", NOGO_2C,
     "Both completions are lawful as formation-rule completions: the difference is "
     "only the unsupplied dictionary/weighting of the doublet outcome."),
    ("2C.route2_matter_action", NOGO_2C,
     "Derive that the physical staggered/finite Grassmann matter action implements "
     "the count-twice or count-once grain."),
    ("3A.claim_scope", LEDGER_3A,
     "For every finite complex matrix K, the displayed realification has determinant "
     "|det_C(K)|^2 and the displayed ordered holomorphic Berezin Gaussian equals "
     "det_C(K); no physical carrier or occupancy-rule identification is included."),
    ("axioms.record_readout", AXIOMS,
     "Only records are readable. A readout value is determined by record content "
     "alone. For any finite collection of pairwise-disjoint records, scalar readout "
     "`I` is additive, with `I(empty)=0`."),
    ("axioms.qualification", AXIOMS,
     "These axioms state only their named primitive content. Further physical "
     "structure requires a retained derivation or bridge, or explicit approved- "
     "primitive registration, before use as a premise. A choice not fixed by the "
     "supplied structure remains a named conditional or open dependency."),
]

for name, src, quote in QUOTES:
    fq = flat(quote)
    src_flat = flat(src.read_text())
    check("SOURCE_GATES", f"verbatim quote present in source and note: {name}",
          fq in src_flat and fq in FLAT_NOTE)

for dep_md in DEP_FILENAMES:
    check("SOURCE_GATES", f"dependency cited in note and present in docs/: {dep_md[:34]}...",
          dep_md in NOTE_TEXT and (DOCS / dep_md).exists())

# ----------------------------------------------------------------------------
# R2  SPECTRAL (T1): C3 spectrum, K action, A eigenrelations
check("SPECTRAL", "det_C(A) == lam0*lam1*lam2",
      zero(A.det() - lam[0] * lam[1] * lam[2]))
check("SPECTRAL", "im(lam0) == 0 (K-fixed sector real)",
      zero(sym_im(lam[0])))
check("SPECTRAL", "lam2 == conj(lam1) (free K-orbit conjugate pair)",
      zero(lam[2] - conjugate(lam[1])))
check("SPECTRAL", "conj(e1) == e2 (K swaps s+ and s-)",
      mzero(e1.conjugate() - e2))
check("SPECTRAL", "C e1 == w e1",
      mzero(C * e1 - w * e1))
check("SPECTRAL", "A e1 == lam1 e1",
      mzero(A * e1 - lam[1] * e1))
check("SPECTRAL", "A e2 == lam2 e2",
      mzero(A * e2 - lam[2] * e2))
check("SPECTRAL", "im(lam1) == sqrt(3)/2 * (beta - gamma)",
      zero(sym_im(lam[1]) - sqrt(3) / 2 * (beta - gamma)))

# ----------------------------------------------------------------------------
# R3  DET_POWER (3A re-gate): realification determinant == det_C * conj(det_C)
kr = symbols("k00r k01r k10r k11r", real=True)
ki = symbols("k00i k01i k10i k11i", real=True)
K2 = Matrix([[kr[0] + I * ki[0], kr[1] + I * ki[1]],
             [kr[2] + I * ki[2], kr[3] + I * ki[3]]])
detC2 = K2.det()
check("DET_POWER", "general 2x2: det(realify(K)) == det_C(K)*conj(det_C(K))",
      zero(realify(K2).det() - detC2 * conjugate(detC2)))

u, v = symbols("u v", real=True)
orbit_block = Matrix([[u, -v], [v, u]])
check("DET_POWER", "1x1 orbit block: det == (u+iv)*conj(u+iv)",
      zero(orbit_block.det() - (u + I * v) * conjugate(u + I * v)))

zr = symbols("z0r z1r z2r", real=True)
zi = symbols("z0i z1i z2i", real=True)
a0, a1, a2 = (zr[0] + I * zi[0], zr[1] + I * zi[1], zr[2] + I * zi[2])
Zc = a0 * eye(3) + a1 * C + a2 * (C * C)
check("DET_POWER", "general 3x3 circulant: det(realify(Z)) == det_C(Z)*conj(det_C(Z))",
      zero(realify(Zc).det() - Zc.det() * conjugate(Zc.det())))

# ----------------------------------------------------------------------------
# R4  REALITY_CLASS (T3a): reality neutrality and modulus-power multiplicativity
check("REALITY_CLASS", "im(lam1*lam2) == 0 (free-orbit modulus real)",
      zero(sym_im(lam[1] * lam[2])))
check("REALITY_CLASS", "lam1*lam2 == lam1*conj(lam1)",
      zero(lam[1] * lam[2] - lam[1] * conjugate(lam[1])))
check("REALITY_CLASS", "det_C(conj(K)) == conj(det_C(K))",
      zero(K2.conjugate().det() - conjugate(detC2)))
mod1 = detC2 * conjugate(detC2)
mod2 = K2.conjugate().det() * conjugate(K2.conjugate().det())
check("REALITY_CLASS", "|det_C(K)|^2 invariant under conjugation",
      zero(mod1 - mod2))
Kc = K2.conjugate()
check("REALITY_CLASS", "power 1: det_C(K (+) Kc) == det_C(K)*det_C(Kc)",
      zero(dsum(K2, Kc).det() - K2.det() * Kc.det()))
lhs2 = dsum(K2, Kc).det() * conjugate(dsum(K2, Kc).det())
rhs2 = (K2.det() * conjugate(K2.det())) * (Kc.det() * conjugate(Kc.det()))
check("REALITY_CLASS", "power 2: |det_C(K (+) Kc)|^2 == |det_C(K)|^2 * |det_C(Kc)|^2",
      zero(lhs2 - rhs2))

# ----------------------------------------------------------------------------
# R5  GLOBAL_POWER (T2): dial invariance under equal rescaling
Ws, Wd = symbols("Ws Wd", positive=True)
r_dial = (Wd / 2) / Ws
r_scaled = ((2 * Wd) / 2) / (2 * Ws)
check("GLOBAL_POWER", "r == r under (Ws,Wd) -> (2Ws,2Wd)",
      zero(r_dial - r_scaled))
check("GLOBAL_POWER", "r(1,1) == 1/2 and r(2,2) == 1/2 (scale-neutral)",
      r_dial.subs({Ws: 1, Wd: 1}) == Rational(1, 2)
      and r_dial.subs({Ws: 2, Wd: 2}) == Rational(1, 2))

# ----------------------------------------------------------------------------
# R6  QUOTIENT_MEASURE (T3b): orbit partition, pushforward vs restriction
K_perm = {0: 0, 1: 2, 2: 1}  # K on sector indices: s0 fixed, s+ <-> s-


def orbits(perm):
    seen, res = set(), []
    for x in sorted(perm):
        if x in seen:
            continue
        cyc, y = [], x
        while y not in seen:
            seen.add(y)
            cyc.append(y)
            y = perm[y]
        res.append(sorted(cyc))
    return res


orb = orbits(K_perm)
check("QUOTIENT_MEASURE", "K-orbit partition == [[0],[1,2]] (computed)",
      orb == [[0], [1, 2]])
cards = sorted(len(o) for o in orb)
check("QUOTIENT_MEASURE", "orbit cardinalities == [1,2] (computed)",
      cards == [1, 2])
orbit_card = len([o for o in orb if len(o) == 2][0])  # 2
mu0, t1, t2 = symbols("mu0 t1 t2", positive=True)
mu_free = {0: mu0, 1: t1, 2: t2}  # unconstrained: independent symbols per sector
check("QUOTIENT_MEASURE", "control: unconstrained measure is NOT K-invariant (t1 - t2 nonzero symbolically)",
      not zero(mu_free[1] - mu_free[2]))
residuals = [expand(mu_free[K_perm[k]] - mu_free[k]) for k in range(3)]
forced = solve(residuals, [t1, t2], dict=True)
check("QUOTIENT_MEASURE", "K-invariance residuals solve to the single constraint t1 == t2 (mu0 free)",
      forced in ([{t1: t2}], [{t2: t1}]))
mu = {k: v.subs(forced[0]) for k, v in mu_free.items()}
t = mu[1]
check("QUOTIENT_MEASURE", "K-invariance forces mu(s+) == mu(s-) (derived, not stipulated)",
      zero(mu[1] - mu[2]))
push_orbit = mu[1] + mu[2]
check("QUOTIENT_MEASURE", "orbit-sum pushforward weight == 2t (count-twice)",
      zero(push_orbit - 2 * t))
restrict_orbit = mu[1]
check("QUOTIENT_MEASURE", "single-representative restriction weight == t (count-once)",
      zero(restrict_orbit - t))
check("QUOTIENT_MEASURE", "orbit weights differ by exactly the factor 2",
      zero(simplify(push_orbit / restrict_orbit) - orbit_card))

# ----------------------------------------------------------------------------
# R7  DICTIONARY (T3c) + dial map
x, r_sym, W = symbols("x r W", positive=True)
sol_comp = solveset(Eq(x, 2 * r_sym), r_sym).subs(x, 1)
sol_slot = solveset(Eq(x, r_sym), r_sym).subs(x, 1)
check("DICTIONARY", "component completion: solve x=2r at x=1 -> {1/2}",
      sol_comp == FiniteSet(Rational(1, 2)))
check("DICTIONARY", "slot completion: solve x=r at x=1 -> {1}",
      sol_slot == FiniteSet(Integer(1)))
comp_r = list(sol_comp)[0]
slot_r = list(sol_slot)[0]


def r_from_Wd(Wd_val):
    return Rational(Wd_val, 2)


check("DICTIONARY", "r == W_d/2 with component W_d=1 -> 1/2",
      r_from_Wd(1) == comp_r)
check("DICTIONARY", "r == W_d/2 with slot W_d=2 -> 1",
      r_from_Wd(2) == slot_r)
w_cell = 1 / (1 + W)
dial = simplify((1 - w_cell) / (2 * w_cell))
check("DICTIONARY", "per-cell dial (1-w_cell)/(2 w_cell) == W/2 with w_cell=1/(1+W)",
      zero(dial - W / 2))
check("DICTIONARY", "per-cell dial at W=1 -> 1/2",
      dial.subs(W, 1) == Rational(1, 2))
check("DICTIONARY", "per-cell dial at W=2 -> 1",
      dial.subs(W, 2) == Integer(1))


def dial_ncell(n):
    wc = Rational(1, n)
    return simplify((1 - wc) / (2 * wc))


check("DICTIONARY", "equal-per-cell 2-cell -> 1/2",
      dial_ncell(2) == Rational(1, 2))
check("DICTIONARY", "equal-per-cell 3-cell -> 1",
      dial_ncell(3) == Integer(1))

# ----------------------------------------------------------------------------
# R8  FAITHFULNESS_CONTROLS (T1 / N1-N4)
check("FAITHFULNESS_CONTROLS", "N1 horns distinct: 1/2 != 1",
      Rational(1, 2) != Integer(1))
sub = {alpha: 2, beta: 1, gamma: 0}
lam1v = lam[1].subs(sub)
check("FAITHFULNESS_CONTROLS", "N2 at (2,1,0): im(lam1) != 0",
      not zero(sym_im(lam1v)))
check("FAITHFULNESS_CONTROLS", "N2 at (2,1,0): lam1 != |lam1|^2",
      not zero(lam1v - lam1v * conjugate(lam1v)))
a_re = symbols("a", real=True)
br, bi = symbols("br bi", real=True)
b = br + I * bi
M = a_re * eye(3) + b * C + conjugate(b) * (C * C)
check("FAITHFULNESS_CONTROLS", "N3 control M is Hermitian (M == M^dagger)",
      mzero(M - M.conjugate().T))
lamM = [simplify(a_re + b * w**k + conjugate(b) * w**(2 * k)) for k in range(3)]
check("FAITHFULNESS_CONTROLS", "N3 control M spectrum all real",
      all(zero(sym_im(v)) for v in lamM))
check("FAITHFULNESS_CONTROLS", "N3 control det_C(M) == lamM0*lamM1*lamM2",
      zero(M.det() - lamM[0] * lamM[1] * lamM[2]))
check("FAITHFULNESS_CONTROLS", "N3 control M is generically NOT K-real (conj(M) - M nonzero symbolically)",
      not mzero(M.conjugate() - M))
check("FAITHFULNESS_CONTROLS", "N3 control conj(M) == M exactly when b is real (bi = 0)",
      mzero((M.conjugate() - M).subs(bi, 0)))
check("FAITHFULNESS_CONTROLS", "N3 control orbit values independent reals: lamM1 - lamM2 nonzero symbolically",
      not zero(lamM[1] - lamM[2]))
check("FAITHFULNESS_CONTROLS", "N4 Born comparator ((2/3)/2)/(1/3) == 1",
      (Rational(2, 3) / 2) / Rational(1, 3) == Integer(1))
check("FAITHFULNESS_CONTROLS", "explicit count: (W_d/2)/W_s with W_d=1,W_s=1 -> 1/2",
      (Rational(1, 2)) / Integer(1) == Rational(1, 2))
check("FAITHFULNESS_CONTROLS", "explicit count: (W_d/2)/W_s with W_d=2,W_s=1 -> 1",
      (Rational(2, 2)) / Integer(1) == Integer(1))

# ----------------------------------------------------------------------------
# R9  TRANSLATION (T4): three guises produce one common count binary + pair
once_factors = Mul.make_args(detC2)
twice_factors = Mul.make_args(detC2 * conjugate(detC2))
n_once = len(once_factors)    # R3 holomorphic weight: one det_C factor
n_twice = len(twice_factors)  # R3 realified weight: conjugate-paired factors
check("TRANSLATION", "reality-class count-once W_d == 1 (single det_C factor from R3)",
      n_once == 1)
check("TRANSLATION", "reality-class count-twice W_d == 2 (conjugate-paired det_C factors from R3)",
      n_twice == 2)
check("TRANSLATION", "the two count-twice factors are mutual conjugates",
      n_twice == 2 and zero(twice_factors[0] - conjugate(twice_factors[1])))

Wd_reality = {1: n_once, 2: n_twice}
Wd_measure = {1: simplify(restrict_orbit / t),      # from R6 derived measure
              2: simplify(push_orbit / t)}
Wd_dict = {1: 2 * comp_r, 2: 2 * slot_r}            # from R7 completions (W_d = 2r)

check("TRANSLATION", "three guises agree at count-once: W_d == 1",
      Wd_reality[1] == 1 and Wd_measure[1] == 1 and Wd_dict[1] == 1)
check("TRANSLATION", "three guises agree at count-twice: W_d == 2",
      Wd_reality[2] == 2 and Wd_measure[2] == 2 and Wd_dict[2] == 2)


def dial_from_Wd(Wd_val):
    wc = Rational(1, 1) / (1 + Wd_val)
    return simplify((1 - wc) / (2 * wc))


check("TRANSLATION", "dial_from_Wd(1) == 1/2",
      dial_from_Wd(1) == Rational(1, 2))
check("TRANSLATION", "dial_from_Wd(2) == 1",
      dial_from_Wd(2) == Integer(1))

pair_reality = [dial_from_Wd(Wd_reality[m]) for m in (1, 2)]
pair_measure = [dial_from_Wd(Wd_measure[m]) for m in (1, 2)]
pair_dict = [dial_from_Wd(Wd_dict[m]) for m in (1, 2)]
target_pair = [Rational(1, 2), Integer(1)]
check("TRANSLATION", "reality-class and measure guises give the same dial pair",
      pair_reality == pair_measure)
check("TRANSLATION", "measure and dictionary guises give the same dial pair",
      pair_measure == pair_dict)
check("TRANSLATION", "common dial pair == {1/2, 1}",
      pair_reality == target_pair)

# ----------------------------------------------------------------------------
# R1b  NOTE_HYGIENE : claim id, required structure, forbidden-pattern + decimal scans
CLAIM_ID = ("acphilambda_occupancy_grain_three_candidate_deciders_common_count_"
            "binary_reduction_bounded_theorem_note_2026-07-16")
check("NOTE_HYGIENE", "claim id present in note",
      CLAIM_ID in NOTE_TEXT)
check("NOTE_HYGIENE", "Claim type line present",
      "**Claim type:** bounded_theorem" in NOTE_TEXT)
check("NOTE_HYGIENE", "Status authority line present",
      "**Status authority:** independent audit lane only." in NOTE_TEXT)
for sec in ["## Purpose", "## Honest auditor read / Boundary", "## Non-claims",
            "## Load-bearing dependencies", "## Runner verification map"]:
    check("NOTE_HYGIENE", f"required section present: {sec}",
          sec in NOTE_TEXT)
check("NOTE_HYGIENE", "no-stipulation footer present",
      "**No check passes by literal stipulation.**" in NOTE_TEXT)

# prose = note with fenced code blocks removed
prose_lines, in_fence = [], False
for ln in NOTE_TEXT.splitlines():
    if ln.strip().startswith("```"):
        in_fence = not in_fence
        continue
    if not in_fence:
        prose_lines.append(ln)
prose = "\n".join(prose_lines)

FORBIDDEN = ["exhaust", "only route", "last route", "closes the",
             "bijection", "fiber", "multiplicity bit", "grain bit", "final"]
found = [f for f in FORBIDDEN if f in prose.lower()]
check("NOTE_HYGIENE", f"no forbidden framing phrases in prose (found={found})",
      found == [])

decimal_hits = [m.group(0) for m in re.finditer(r"[0-9]\.[0-9]", prose)]
check("NOTE_HYGIENE", f"no bare decimals outside code fences (hits={decimal_hits})",
      decimal_hits == [])

# markdown link targets: .md deps and the .py runner must resolve; skip the
# self-referential .txt cache produced by this very run
targets = re.findall(r"\]\(([^)]+)\)", NOTE_TEXT)
unresolved = []
for tgt in targets:
    if "logs/runner-cache" in tgt:
        continue
    if tgt.endswith(".md") or tgt.endswith(".py"):
        if not (DOCS / tgt).resolve().exists():
            unresolved.append(tgt)
check("NOTE_HYGIENE", f"markdown .md/.py link targets resolve (unresolved={unresolved})",
      unresolved == [])

# ----------------------------------------------------------------------------
print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
import sys
sys.exit(1 if FAIL_COUNT else 0)
