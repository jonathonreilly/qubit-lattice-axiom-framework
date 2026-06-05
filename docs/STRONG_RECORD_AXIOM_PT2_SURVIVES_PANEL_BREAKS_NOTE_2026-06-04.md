---
claim_id: strong_record_axiom_pt2_survives_panel_breaks_note_2026-06-04
claim_type_author_hint: meta
---

# Pressure-Test 2 of the Strong Record Axiom ("which REAL CLASSICAL alternative, counted"): It Survives Break 1 Outright, Defuses Break 3's Mechanism, but Breaks 2 & 3 Collapse to One Shared Physical-Selection Residual

**Date:** 2026-06-04
**Claim type:** meta. This is an adversarial pressure-test of a CANDIDATE axiom
against three named breaks; it sets no audit status, promotes no row, weakens no
retained no-go, edits no axiom, and adopts no import. `r = 1/2` remains the
Tier-A admitted input `AC_φλ`; it is compared **structurally** only (no PDG value
consumed).
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit.
**Primary runner:**
[`scripts/strong_record_axiom_pt2_survives_panel_breaks.py`](../scripts/strong_record_axiom_pt2_survives_panel_breaks.py)
(SCORECARD PASS=37 FAIL=0).
**Cached log:**
[`logs/runner-cache/strong_record_axiom_pt2_survives_panel_breaks.txt`](../logs/runner-cache/strong_record_axiom_pt2_survives_panel_breaks.txt)

## The candidate axiom being tested

> "A record registers WHICH REAL CLASSICAL ALTERNATIVE is realized. The real
> classical alternatives of the local algebra are its real superselection
> sectors (real Wedderburn blocks); each sector is one alternative; record
> readout COUNTS alternatives — additive over disjoint alternatives, and
> DIMENSION-BLIND (one unit per real sector)."

On the recordable commutant `⟨I, C, C²⟩` of the Brannen-circulant `C3` shift,
this selects the type/block-count weight `(1,1)` over the 2 real-Wedderburn
blocks of `ℝ[Z₃] = ℝ ⊕ ℂ` → isotype weight `(w_singlet, w_doublet) = (1,1)` →
Brannen modulus `r = |b|²/a² = 1/2` → Koide `Q = (1+2r)/3 = 2/3`.

The prior closure (`RECORD_MINIMUM_INFORMATION_INTERLOCK_R_HALF_DERIVATION_NOTE_2026-06-04`,
the irreversibility + minimum-information interlock) reached
FORCED-MODULO-TWO-POSITS and was then broken by a 12-angle adversarial panel on
three independent grounds. This axiom was designed to dodge all three. The
runner judges, hostilely, whether the axiom's **content** resolves each break or
merely **relabels** the same choice.

## Verdict table

| break | what it attacks | verdict | why |
|---|---|---|---|
| **1** real-vs-complex Wedderburn fork | is "classical = real" a smuggled choice, vs the 3-idempotent complex reading (→ r=1)? | **SURVIVES** | CPT/conjugation **fuses** the 3 complex idempotents into 2 real blocks; the 3-way split is reachable **only** by a T-ODD coupling |
| **2** count vs dimension/multiplicity | does "which alternative" exclude the central `Mult = E₀+2E₁` (→ (1,2) → r=1)? | **STILL-BITES** | the count-vs-Mult **operator** fork IS resolved (count is the unique dimension-blind which-readout), but `masses ← count` is **asserted**, not derived |
| **3** minimal vs redundant (Darwinism) | does the redundancy/Born "min-info-is-backwards" objection still bite? | **STILL-BITES** | its **original mechanism is DEFUSED** (count is redundancy-invariant; objectivity = redundancy is itself a count; Born is a separable state-weight), but the **Born readout survives** as the same residual as Break 2 |

## Break 1 — SURVIVES (the one clean win)

"REAL CLASSICAL" is genuine content, not a smuggled tie-break. The decisive
computation: model the real structure as complex conjugation `J(X) = X̄` (= time
reversal = CPT on the recordable algebra; its fixed-point real subalgebra is
`ℝ[Z₃]`). Then:

- `J` **fixes** the trivial idempotent `P_triv = E₀` (the `χ=1` character is real)
  and **swaps** the `ω` and `ω̄` idempotents (`J(P_ω) = P_ω̄`). The
  conjugation-symmetric fusion `P_ω + P_ω̄ = E₁` is exactly the rank-2 real
  doublet block. So `(1,1,1)` collapses to the 2 real blocks — **computed**, not
  posited (runner 1A–1B).
- **Every** real/CPT-even (Hermitian) observable in the commutant assigns the
  **same** value to the `ω` and `ω̄` sectors (max separation `4.4e-16` over 5
  witnesses): a real record **cannot** distinguish them (runner 1C.1).
- The cleanest structural fact (runner 1D′): the Hermitian commutant of `C` is
  the 3-dim real space `span_ℝ{I, C+C², i(C−C²)}`. Its CPT-even part
  `span_ℝ{I, C+C²}` has eigenvalues `{2, −1, −1}` — **doublet degenerate**. The
  one extra generator `i(C−C²)` is conjugation-**anti**-fixed (`conj = −itself`,
  T-ODD) and is the **unique** direction that splits the doublet. So a T-EVEN
  record sees exactly **2** levels; resolving a **3rd** classical alternative
  requires a **CPT-violating** coupling.

Therefore the complex 3-way reading is not "another equally-classical choice" —
it is the **non-classical** (T-odd / phase / quantum) resolution. "classical =
real = T-even" is forced by the meaning of *classical fact*, exactly as the
axiom's word "REAL CLASSICAL" intends. The break is genuinely resolved.

## Break 2 — STILL-BITES (operator fork resolved; physical identification asserted)

The multiplicity `Mult = E₀ + 2E₁` is a genuine central, Hermitian, frozen
observable (commutes with `C`, fixed by the doublet's internal unitary): it
passes **every** filter that killed the microstate reading. The fork is real.

What the axiom **does** resolve (runner 2B–2D): a *which-alternative* readout is
a **function on the set of sectors** — its value depends only on the label, not
the fiber dimension. The COUNT functional is the **unique dimension-invariant**
central readout: its weight stays `(1,1)` as the doublet dimension is varied over
`{2,3,5,17}`, while `Mult` tracks the (physically irrelevant) internal dimension
`(1,d)`. The classical quotient (minimal central idempotents) has cardinality
**2**, carrying no dimension data; a record reads THIS, so count is forced **as
the which-readout**. So `Mult` answers a different question ("how many
microstates") than the record ("which alternative").

What the axiom does **not** do (runner 2E): derive, from independent physics,
that **mass-generation** reads the classical which-record (count → r=1/2) rather
than the equally-frozen Born/thermal pushforward of `I/3`, `Tr(E_k · I/3) =
(1/3, 2/3)` → r=1. Both are central and frozen. The axiom **asserts**
`masses ← count`; the Born alternative survives. So Break 2 bites at the
**physical-identification** layer, not the operator layer.

## Break 3 — STILL-BITES via the shared residual (but its original mechanism is defused)

Two layers, judged separately:

- **Mechanism DEFUSED** (runner 3A–3D): the redundancy/Born argument that killed
  *minimum-information* ("min-info is backwards; Darwinism makes records
  maximally redundant; the redundant/Born measure (1/3,2/3) gives r=1") does
  **not** transfer to the count axiom. Redundancy multiplies **copies** of
  "alternative k occurred" — it scales the **token** count (`2N` for `N ∈
  {1,3,10,1000}`) while the **distinct-alternative count stays 2**. Quantum
  Darwinism's own objectivity figure of merit (the redundancy `R_δ`) is itself an
  integer **count** of fragments, **not** the Born probability. And the Born
  weight is a **state** functional (`I/3 → (1/3,2/3)`; a singlet-aligned pure
  state → `(1,0)`), provably separable from the count (two-way independence:
  Born constant while redundancy varies, redundancy constant while Born varies).
  So the axiom is Darwinism-**compatible**, and the "backwards-direction"
  objection is removed.
- **Residual BITES**: the Born readout `(1/3,2/3)` is nonetheless still a central,
  frozen, Darwinism-compatible observable giving r=1 (runner 3E). The axiom does
  not derive that masses read the count rather than this Born weight. This is the
  **same** `masses ← count` vs `masses ← Born` posit as Break 2.

So Break 3's specific attack is genuinely dissolved, but the Born **alternative**
survives — the per-break verdict is STILL-BITES, via the shared residual rather
than via its original argument.

## Net

The axiom converts the prior closure's **two** posits (irreversibility +
minimum-information) **plus** the "minimum-information-is-backwards" objection
into a **single** physical-identification posit, with no backwards-direction
problem:

> **mass-generation reads the classical which-record (count → r=1/2) rather than
> the equally-frozen Born/thermal weight (→ r=1).**

This is real narrowing — Break 1 is removed entirely, the count READOUT is now
the forced dimension-blind which-readout (Breaks 1+2 operator layer), and the
backwards-direction objection is gone — but it is **NOT** a bare-axiom closure.
The Born/thermal readout remains a coherent competing frozen observable, and the
axiom **asserts** rather than derives that masses use the classical-record
readout. The surviving residual is physical and in-principle-derivable, and
matches the literature (Koide leaves the per-sector ratio a free fit).

## No-Go Discipline Gate

- **N1 alternative routes:** three breaks tested independently; for each, the
  resolving computation AND a parallel "does the same choice reappear" check are
  run. Break 1: CPT fusion + T-odd-necessity (resolved). Breaks 2/3: operator
  fork resolved, physical identification not (residual). A future route — a
  derivation that mass-generation is a classical-record (objectivity) process —
  is named, not assumed.
- **N2 wall independence:** the three breaks are independent attacks; the runner
  shows Breaks 2 and 3 are **not** independent after the analysis — they collapse
  to one shared `masses ← count` vs `masses ← Born` residual.
- **N3 hidden-wall scan:** "classical = real," "CPT/time-reversal," "count," and
  "objectivity = redundancy" are tested as content (computed), not admitted as
  hidden theorems. `U = I`, CAR, Hermitian records, and any new axiom are NOT
  introduced.
- **N4 residual matching:** the residual matches the standing block-vs-dimension
  weight frontier (`koide_q23_block_weight_frontier_bounded_note_2026-05-29`,
  retained_bounded) and the records-objectivity conditional
  (`KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31`): the equal-block
  (count) measure gives r=1/2, the Born/dimension measure gives r=1.
- **N5 rhetoric audit:** "SURVIVES" is scoped to Break 1 only; "STILL-BITES" for
  Breaks 2/3 is scoped to the physical-identification layer, with the operator
  fork explicitly marked resolved and Break 3's mechanism explicitly marked
  defused. No "closes," "last route," or "forced" language is applied to the net
  result.
- **N6 partial-closure scan:** a derivation that the framework's mass-generation
  channel is an objectivity/redundancy (classical-record) process rather than a
  Born/thermal-equilibrium one would retire the shared residual without adding an
  axiom.
- **N7 steelman:** the strongest pro-axiom argument is that a *record* of which
  outcome is, by definition, the classical (dimension-blind, count) reading, so
  if masses are recorded facts they track the count. The runner grants this
  reading is coherent and forced **as a readout**; it leaves the
  masses-are-recorded-facts identification as the missing physical input.
- **N8 cross-cycle echo:** the same `(1,1)`-vs-`(1,2)` residual is tracked by the
  block-weight frontier, the einselection-modulo-K-reality note
  (`FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02`), and the records
  objectivity conditional. This note records that the strong axiom narrows the
  residual (removes Break 1 and the backwards-direction objection) without
  closing it.

## Non-circularity

Every check is a substantive computed assertion (PASS=37, FAIL=0); no hard-coded
`True` carries a verdict. The CPT fusion (`J(P_ω)=P_ω̄`, `P_ω+P_ω̄=E₁`), the
T-even/T-odd commutant decomposition (`eig {2,−1,−1}` vs split), the
dimension-invariance of count vs `Mult`, the state-dependence of the Born weight,
and the redundancy-invariance of count are all forward computations on explicit
`3×3` operators. `Q = 2/3` and `r = 1/2` appear only as structural targets; no
PDG value is consumed. The axiom is **tested**, not assumed; the residual is the
output of the computation.

## Verified tiers (origin/main audit ledger context)

| claim_id | effective status |
|---|---|
| [`koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md) | retained |
| [`koide_frobenius_isotype_split_uniqueness_note_2026-04-21`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md) | retained_no_go |
| [`koide_q23_block_weight_frontier_bounded_note_2026-05-29`](KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md) | retained_bounded |
| [`pre_record_reference_state_tracial_derivation_note_2026-05-20`](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md) | retained |
| [`cpt_exact_real_anti_hermitian_d_narrow_theorem_note_2026-05-10`](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md) | retained_bounded |

## Next paths this opens

- The single surviving residual is now sharp and shared by Breaks 2 and 3:
  **does mass-generation read the classical which-record (count) or the
  Born/thermal weight?** The smallest closing step is a derivation that the
  framework's actual mass-generation channel is an **objectivity / redundancy**
  (classical-record) process — for which Break 3 already shows the figure of
  merit is a count — rather than a Born/thermal-equilibrium process (for which
  the einselection note shows the second-law attractor is r=1).
- Break 1's clean result — that "classical = real = T-even" is forced and the
  3-way complex split needs a CPT-violating coupling — is reusable wherever the
  real-vs-complex Wedderburn fork appears (it is the same `det_C`-vs-`det_R` /
  signed-vs-singular-readout / δ=0 object on a different axis).

This is a sharpening of the records-route residual, not a closure; the strong
axiom removes one of three breaks outright and the backwards-direction objection,
leaving one named physical-selection posit.
