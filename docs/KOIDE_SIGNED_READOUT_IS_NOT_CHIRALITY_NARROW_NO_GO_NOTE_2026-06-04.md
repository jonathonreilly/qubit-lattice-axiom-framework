# Koide: the Brannen/det_R Signed-Eigenvalue Q=2/3 Readout Is Not the Chiral Grading - Narrow No-Go

**Date:** 2026-06-04
**Claim type:** no_go (narrow route-demarcation, negative result)
**Status authority:** independent audit lane only. This source note adds no axiom
and no import; it sets no audit outcome. `Q = 2/3` appears only as the empirical
comparator, never as a proof input.
**Primary runner:** `scripts/koide_signed_readout_is_not_chirality.py`
(SCORECARD PASS=33, FAIL=0).

---

## Question (the assigned angle)

Source the chirality for charged-lepton flavor by asking: **is the chiral grading
(anticommutation of the mass operator with `Γ_χ = (2/3)J − I`) ENCODED IN / DERIVABLE
FROM the requirement that the native mass operator be a SIGNED Hermitian operator
(real signed eigenvalues, signed `√m`) rather than a positive singular-value (Yukawa)
operator?** Concretely, three sub-questions:

1. Does `{H, Γ_χ} = 0` FORCE a sign pattern on the three generation eigenvalues that
   is EXACTLY the Brannen signed *eigenvalue* readout giving `Q = 2/3`?
2. Is the native operator `H = iD` (Hermitian lift of the real anti-Hermitian
   staggered Dirac `D`) automatically on the chiral/signed side — does it natively
   anticommute with a `Z₃` grading, or natively carry the signed spectrum the Brannen
   readout needs?
3. Is "signed `√m`" a Lattice+Quantum-baseline consequence of using a Hermitian
   `iD` operator rather than a positive Yukawa matrix, or an unforced READOUT CHOICE?

This was floated as a possibly-easier route to chirality than the `C₃`-orbit-splitting
framing.

## Verdict

**NO — the Brannen/det_R signed-eigenvalue readout that gives `Q = 2/3` is not
the `Γ_χ` chiral grading. Confidence: HIGH (rests on retained dependencies plus
exact algebra).**

The signed-eigenvalue Brannen/`det_R` readout that yields `Q = 2/3` is the readout of
the operator that **COMMUTES** with `Γ_χ` (the circulant `H = aI + bC + b̄C²`).
Genuine chirality — an operator that **ANTICOMMUTES** with `Γ_χ` — is a different
mechanism: its spectrum is the sign-symmetric `{−λ, 0, +λ}` (sum zero), its EIGENVALUE
readout is `Q = ∞` (not `2/3`), and it reaches `2/3` only through its
EIGENVECTOR readout. The Brannen signed-`Q` circulant class and the
`Γ_χ`-anticommuting class intersect only at `H = 0`. So "the signed eigenvalue
readout = the chirality" is false: the readout that needs the sign lives on the
**non-chiral (commuting)** operator, and the chiral (anticommuting) operator's own
eigenvalue readout does not even produce `2/3`.

For sub-question (3): Hermiticity (`H = iD`) makes a signed real spectrum available
(the real eigenvalues carry signs) and excludes no real readout — but it does **not
by itself FORCE** the map `√m_k := λ_k` over
`√m_k := |λ_k|`. That selection is an extra identification (the `det_R`/Brannen posit),
matching the still-`unaudited` `koide_readout_lane_demarcation` "native readout is
signed" claim being an internal identification, not a retained theorem. So this angle
**does not derive** the chirality; it dissolves the proposed equivalence.

This is a **route-demarcation no-go**, not a closure of the chirality search. It
removes one conflation (sign ≡ chirality) and hands the chirality question back, intact,
to the genuine carriers (anticommutation realized on a factor distinct from `Γ_χ`'s, or
the dynamics that selects `r = 1/2`).

---

## The decisive structure (all verified in the runner)

Let `R` be the cyclic shift (`R³ = I`), `J` the all-ones matrix,
`Γ_χ = (2/3)J − I` (spectrum `{+1, −1, −1}`).

**Fact 0 — `Γ_χ` is itself a circulant.** `Γ_χ = (−1/3)I + (2/3)R + (2/3)R²`, so
`[Γ_χ, R] = 0` (retained
[`koide_z3_equivariant_anticommuting_no_go`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md),
§2.2).

**Route A — the signed-readout, COMMUTING circulant operator (gives `Q = 2/3` via eigenVALUES).**
The route's operator is the `C₃` circulant `H = aI + bC + b̄C² (= iD)`. Because it is a
circulant and `Γ_χ` is a circulant, `[H, Γ_χ] = 0` and `{H, Γ_χ} ≠ 0`
(runner Part 1). Its real spectrum `λ_k = a + 2|b|cos(θ + 2πk/3)` is genuinely signable
(e.g. at `r = |b|²/a² = 1/2, θ = 0.9`: `{−0.399, 1.520, 1.879}`). The signed eigenvalue
readout `w_k = λ_k` gives `Q = (1 + 2r)/3`, θ-independent, `= 2/3` at `r = 1/2`
(retained
[`koide_circulant_q_two_thirds_algebraic`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md);
runner Part 2).

**Route B — the chiral, ANTICOMMUTING operator (gives `Q = 2/3` only via eigenVECTORS).**
A Hermitian `H` with `{H, Γ_χ} = 0` has the form `H = (1/3)(1⊗h + h⊗1)`, `Σh = 0`
(retained
[`koide_anticommuting_operator_derivation_theorem`](KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md),
§3.1). It is **not** a
circulant (`[H, R] ≠ 0`), its spectrum is `{−λ, 0, +λ}` with `Σλ = 0`, so its
EIGENVALUE readout is `Q = (Σλ²)/(Σλ)² = (nonzero)/0 = ∞` (runner Part 3). The
retained theorem reads `Q = 2/3` from the nonzero-eigenvalue EIGENVECTORS, not from the
eigenvalues (this is the
[`koide_anticommuting_eigenvector_vs_eigenvalue_readout_reconciliation`](KOIDE_ANTICOMMUTING_EIGENVECTOR_VS_EIGENVALUE_READOUT_RECONCILIATION_NOTE_2026-06-01.md)
distinction, here re-derived exactly).

**The discriminator (runner Part 4).** The operator whose SIGNED-EIGENVALUE readout is
`2/3` (Route A) is the one that COMMUTES with `Γ_χ`. The operator that ANTICOMMUTES
with `Γ_χ` (Route B) has eigenvalue readout `∞`, not `2/3`. And no nonzero Hermitian
circulant anticommutes with `Γ_χ` (`comm(R) ∩ anticomm(Γ_χ) = {0}`, retained
[`koide_z3_equivariant_anticommuting_no_go`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md),
re-verified). Therefore the "signed-spectrum
(Brannen-`Q` circulant)" class and the "chiral (anticommuting)" class are **disjoint except at 0**.
The proposed equivalence "signed eigenvalue readout ⟺ chirality" is FALSE.

**Steelman killed (runner Part 5).** Could the SIGN PATTERN of the commuting circulant
encode `Γ_χ`-grade information even without anticommutation (e.g. is "number of negative
eigenvalues" a chirality index)? No: the eigenvectors of the circulant are the fixed
`Z₃` character vectors, with `Γ_χ`-grade `(+1)` on the singlet (`k = 0`) and `(−1)` on
the doublet (`k = 1, 2`). Which `λ_k` is negative roams across grades as θ varies — the
`+1`-graded singlet eigenvalue is the negative one at `θ = π`, a `−1`-graded doublet
eigenvalue is the negative one at `θ = 0.9`. The sign of an eigenvalue is **not locked**
to its `Γ_χ` grade. Moreover the signed readout `Q = 2/3` is θ-INDEPENDENT, so it does
not even resolve which eigenvalue is negative — it cannot be carrying grade-resolved
sign data.

**4D analogy points the other way (runner Part 7).** In 4D, `γ₅` ANTICOMMUTES with the
*massless* Dirac operator; massive eigenvectors have zero chirality expectation. The
finite analog of that chiral structure is precisely Route B (spectrum `{−λ, 0, +λ}`) —
the case whose eigenvalue Koide is `∞`. The native MASSIVE circulant whose signed
spectrum gives `2/3` is the `γ₅`-COMMUTING (non-chiral on this factor) operator. So the
"signedness" that yields `2/3` is the **non-chiral** structure; genuine chirality yields
the massless `{−λ, 0, +λ}` pattern, not `2/3`.

## Answers to the three sub-questions

1. **No.** `{H, Γ_χ} = 0` forces the sign-*symmetric* `{−λ, 0, +λ}` spectrum, whose
   *eigenvalue* Koide is `∞`, not the Brannen `2/3`. Anticommutation does not produce
   the Brannen eigenvalue sign pattern; it produces the massless-Dirac pattern.
2. **Commutes, and has a signed real spectrum — but the two are independent.** `H = iD` is the circulant; it
   COMMUTES with `Γ_χ` (does NOT anticommute), so it is not chiral on the generation
   factor. It does natively carry a signed (real) spectrum because it is Hermitian. The
   signedness comes from Hermiticity, **not** from any `Γ_χ` anticommutation; the
   no-go `comm(R) ∩ anticomm(Γ_χ) = {0}` proves a circulant cannot be both signed-in-the-
   chiral-sense and anticommuting.
3. **Available as a real spectrum, but not forced — a readout posit, flagged.** Hermiticity
   (`iD`) gives a REAL spectrum (each eigenvalue has a definite sign) and fixes the
   masses `m_k = λ_k²` identically for both readouts; it does NOT fix the map
   `spectrum → √m`. Both `√m_k = λ_k` (signed) and `√m_k = |λ_k|` (≥0) are real-valued
   readouts of the same real spectrum, yet give different `Q` (`2/3` vs `<2/3` at
   `θ = 0.9`). Selecting the signed one (`det_R`/Brannen) is an **extra identification**,
   not a theorem-forced consequence of Hermiticity. **Import flag:** asserting "the
   native readout is the signed one" is the `unaudited`
   `koide_readout_lane_demarcation` internal identification — natural from
   self-adjointness, but not retained. It is not a *foreign* import (no PDG value, no
   literature comparator), but it is not derived either.

## Relation to prior work (no churn; this is the missing explicit discriminator)

The signed/singular dichotomy
([`koide_signed_eigenvalue_vs_singular_value_readout`](KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md),
currently `unaudited`) and the eigenvector/eigenvalue reconciliation
([`koide_anticommuting_eigenvector_vs_eigenvalue_readout_reconciliation`](KOIDE_ANTICOMMUTING_EIGENVECTOR_VS_EIGENVALUE_READOUT_RECONCILIATION_NOTE_2026-06-01.md),
`unaudited`)
each established pieces of this. The `reality_favors_signed` note
(`unaudited`) showed reality places the native operator on the signed side as a *shared
mechanism, not a shared object*. **What was not stated explicitly anywhere:** the direct
equivalence-test "signed eigenvalue readout ⟺ chirality (anticommutation)" and its
clean refutation via the disjointness `comm(R) ∩ anticomm(Γ_χ) = {0}` combined with the
eigenvalue-readout-`∞` fact. This note isolates exactly that: the signed readout giving
`2/3` is a property of the `Γ_χ`-**commuting** operator, so signedness cannot be the
source of `Γ_χ`-chirality. It closes the proposed shortcut and leaves the genuine
chirality carriers untouched.

## Stale-retained corrections surfaced (verify-memory discipline)

Dependency posture observed during review-loop parser validation (not an audit verdict for
this note):

- **[`cpt_exact_real_anti_hermitian_d_narrow_theorem_note_2026-05-10`](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md) is now `unaudited`**
  (not `retained_bounded` as the 2026-06-02 companion notes' tables state — its audit was
  re-archived under a new note hash). The isolated narrow "real anti-Hermitian `D` /
  `H = iD`" row is therefore pending re-audit. Its **parent**
  [`cpt_exact_note`](CPT_EXACT_NOTE.md) (which
  bundles the `H = iD` Hermitian-lift bridge) is retained-grade, so the
  "native operator = `iD`" premise is not unsupported — but the narrow, isolated form that
  the signed-side companion notes cite is currently not on retained ground. This is
  consistent with the sub-question (3) finding that the *signed-readout selection* on top
  of `iD` is a separate, not-yet-retained identification.
- **[`koide_signed_eigenvalue_vs_singular_value_readout_narrow_theorem_note_2026-05-29`](KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md) is
  `unaudited`** (a source repair for a θ=π/12 boundary-wording defect landed; the
  terminal status shown in the `records_reality_shrinks` table is point-in-time stale).
- **Confirmed retained-grade / load-bearing here:**
  [`koide_anticommuting_operator_derivation_theorem_note_2026-05-10`](KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md),
  [`koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md),
  [`koide_circulant_character_bridge_narrow_theorem_note_2026-05-09`](KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md), and
  [`koide_z3_equivariant_anticommuting_no_go_note_2026-05-16`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md). The verdict of this note
  rests only on these four retained-grade rows plus exact algebra.

---

## No-Go Discipline Gate (N1–N8)

**N1 — Alternative-route enumeration.** Routes separated and tested: (a) signed
eigenvalue readout of the commuting circulant; (b) singular-value readout of the same;
(c) eigenvalue readout of the anticommuting operator; (d) eigenvector readout of the
anticommuting operator; (e) "sign pattern as a `Γ_χ`-index" steelman; (f) "Hermiticity
forces the signed `√m` map" derive-vs-posit. (a)–(f) are the six checked lanes
(runner Parts 2–7). The genuine chirality carriers (anticommutation on a factor distinct
from `Γ_χ`'s, per
[`koide_z3_equivariant_anticommuting_no_go`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
§4 escape hatches; and the
`r = 1/2` dynamics) are named as the live paths this does NOT touch.

**N2 — Wall-independence.** The result collapses to one statement: the signed-readout-
`2/3` property belongs to the `Γ_χ`-COMMUTING operator, while chirality is
anticommutation, and the two classes meet only at `0`. The signed/singular distinction
(value axis) and the commute/anticommute distinction (grading axis) are independent
axes; this note shows they do not coincide, it does not merge them.

**N3 — Hidden-wall scan.** No PDG mass, no PMNS, no `r = 1/2` selector, and no Lane-6
closure is consumed. `Q = 2/3` is comparator-only. "Native operator = `iD`" is used only
as the premise under test and is explicitly flagged as currently `unaudited`.

**N4 — Residual matching.** The value residual (which `√m` enters `Q`) and the grading
residual (does any operator anticommute with `Γ_χ` on the generation factor) are matched
to distinct retained authorities; this note does not claim to close either — it shows the
signed-readout cannot serve as the grading residual's solution.

**N5 — Rhetoric audit.** "Sign is not chirality" means: the signed-eigenvalue readout
that gives `2/3` is the readout of the `Γ_χ`-commuting circulant, and anticommutation
gives `2/3` only via eigenvectors (eigenvalue `∞`). It does NOT mean chirality is
impossible, nor that the framework cannot supply an anticommuting operator on a separate
factor, nor that `r = 1/2` is unreachable. No "only/last/closes/exhausted" framing is
used; the genuine chirality search remains open and the named escape hatches remain live.

**N6 — Partial-closure path scan.** Still open and untouched: (i) a multi-factor
realization where the chiral grading lives on a factor distinct from `Γ_χ`'s
([`koide_z3_equivariant_anticommuting_no_go`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
§4 route II); (ii) auditing
[`koide_readout_lane_demarcation`](KOIDE_READOUT_LANE_DEMARCATION_NOTE_2026-05-30.md)
toward retained (would put the signed-readout selection
on retained ground, separately from chirality); (iii) the dynamics lane selecting
`r = 1/2`. A later theorem could realize chirality via any of these without contradicting
this note.

**N7 — Steelman.** A reviewer could argue the *number of sign flips* (count of negative
eigenvalues) of the commuting circulant is a topological index correlated with chirality.
Refuted in Part 5: at `r = 1/2` the negative eigenvalue roams across `Γ_χ` grades as θ
varies (singlet-negative at `θ = π`, doublet-member-negative at `θ = 0.9`), and the
signed `Q = 2/3` is θ-independent so it does not resolve the sign location at all. The
sign count is not a `Γ_χ`-grade invariant.

**N8 — Cross-cycle echo.** Prior cycles repeatedly split "signed vs singular" (value) from
"commute vs anticommute" (grading) and split mechanism from object
(`reality_favors_signed`). This note follows that discipline: it identifies that the
signed readout and the chiral grading are on different axes and cannot be identified,
rather than declaring the chirality question closed.

## What this note does NOT claim

- Does **not** claim chirality is unreachable or that the search is closed. It removes one
  proposed shortcut (sign ≡ chirality).
- Does **not** derive `r = 1/2`, `Q = 2/3`, or the individual lepton masses.
- Does **not** retire any retained theorem; it consumes four retained rows and exact
  algebra.
- Does **not** assert the framework forces the signed readout (sub-question 3 explicitly
  finds it is an `unaudited` internal identification, not forced by Hermiticity).
- Does **not** import any PDG value, literature comparator, fitted selector, unit
  convention, or same-surface family argument.

## Forbidden-imports check

- No PDG observed values consumed (`2/3` is comparator-only).
- No literature numerical comparators consumed.
- No fitted selectors consumed (`r = 1/2`, θ are abstract symbols; sample angles
  illustrative).
- No admitted unit conventions load-bearing.
- No same-surface family arguments.
- The one identification under examination ("native readout is signed") is flagged as the
  `unaudited` `koide_readout_lane_demarcation` internal claim — examined, NOT adopted.

## Validation

`scripts/koide_signed_readout_is_not_chirality.py` (SCORECARD PASS=33, FAIL=0) verifies, with
exact sympy plus numpy cross-checks:

- Part 0: `R³ = I`; `Γ_χ² = I`; `Γ_χ` spectrum `{+1,−1,−1}`; `Γ_χ` is the circulant
  `(−1/3, 2/3, 2/3)`; `[Γ_χ, R] = 0`.
- Part 1: `H_circ` Hermitian; `[H_circ, Γ_χ] = 0`; `{H_circ, Γ_χ} ≠ 0`; signed spectrum
  goes negative at `r = 1/2, θ = 0.9`.
- Part 2: `Q(signed) = (1+2r)/3` θ-independent, `= 2/3` at `r = 1/2`; `Q(singular)`
  θ-dependent and `< 2/3` off the sign-homogeneous window.
- Part 3: `H_anti` Hermitian, `{H_anti, Γ_χ} = 0`, `[H_anti, Γ_χ] ≠ 0`, `[H_anti, R] ≠ 0`;
  spectrum `{−λ, 0, +λ}` (sum 0); eigenvalue readout `Q = ∞`; eigenvector readout
  `Q(v) = 2/3`.
- Part 4: the `Q(signed) = 2/3` operator COMMUTES; the anticommuting operator's eigenvalue
  readout is `∞`; no nonzero Hermitian circulant anticommutes with `Γ_χ` (disjointness).
- Part 5: sign of an eigenvalue not locked to its `Γ_χ` grade (roams with θ); signed
  `Q = 2/3` θ-independent (no grade-resolved sign data).
- Part 6: masses identical for signed and singular readouts; `Q(signed) = 2/3` vs
  `Q(singular) < 2/3` — the `√m`-sign is an extra, value-changing choice not forced by
  Hermiticity.
- Part 7: the anticommuting (chiral, massless-analog) case is the `Q = ∞` eigenvalue case;
  the native `Q = 2/3` operator is `Γ_χ`-commuting (non-chiral on this factor).

## Cross-references

- [`koide_anticommuting_operator_derivation_theorem_note_2026-05-10`](KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md) (retained-grade):
  `{H, Γ_χ} = 0` ⟹ nonzero-eigenvalue eigenVECTORS give `Q(v) = 2/3`; such `H` has
  spectrum `{−λ, 0, +λ}`.
- [`koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md) (retained-grade):
  circulant eigenVALUE readout `Q = (1+2r)/3`, `= 2/3` at `r = 1/2`.
- [`koide_z3_equivariant_anticommuting_no_go_note_2026-05-16`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md) (retained-bounded):
  `comm(R) ∩ anticomm(Γ_χ) = {0}` — circulant and anticommuting classes are disjoint;
  §4 names the multi-factor escape hatches for genuine chirality.
- [`koide_anticommuting_eigenvector_vs_eigenvalue_readout_reconciliation_note_2026-06-01`](KOIDE_ANTICOMMUTING_EIGENVECTOR_VS_EIGENVALUE_READOUT_RECONCILIATION_NOTE_2026-06-01.md)
  (`unaudited`): eigenvalue readout of anticommuting `H` is `∞`, not `2/3` — the
  category distinction this note turns into the sign≠chirality discriminator.
- [`koide_signed_eigenvalue_vs_singular_value_readout_narrow_theorem_note_2026-05-29`](KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md)
  (`unaudited`): the signed/singular `Q` dichotomy on the circulant.
- [`koide_readout_lane_demarcation_note_2026-05-30`](KOIDE_READOUT_LANE_DEMARCATION_NOTE_2026-05-30.md) (`unaudited`): the "native readout is
  signed" internal identification flagged here as not-forced-by-Hermiticity.
- [`cpt_exact_real_anti_hermitian_d_narrow_theorem_note_2026-05-10`](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md) (`unaudited` on live
  ledger; parent [`cpt_exact_note`](CPT_EXACT_NOTE.md) is retained-grade): the `H = iD` premise under test — narrow
  row pending re-audit, parent carries the lift bridge at retained tier.
