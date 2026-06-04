# Flavor — the (1,2)-vs-(1,1) generation-measure tie is NOT broken in favor of the observed value by any native positivity / normalization / modular principle: RP/T-positivity are AGNOSTIC; on-site unit-trace + KMS(β=0) + locality + Plancherel all FORCE the dimension measure (1,2) → Q=1

**Date:** 2026-06-02
**Claim type:** no_go / narrow native-principle demarcation (one angle of the charged-lepton Koide value).
**Status authority:** independent audit lane only. This note adds no axiom and no import, and sets no audit outcome. It is a /tmp deliverable from a single-angle attack; not landed.
**Runner:** `flavor_koide_measure_tiebreak_native_principles.py` (SCORECARD PASS=38 FAIL=0, venv-verified).

## Framing correction (2026-06-02 — supersedes any exclusion language below)

`Q=1` and `Q=2/3` are **not competitors**; they are different operator classes that
**coexist** on the family `Q = 1/3 + (2/3)·r`, `r ∈ [0,1]`. Per retained
`koide_anticommuting_operator_derivation_theorem_note_2026-05-10`: the **non-chiral**
(circulant / tracial-default) mass operator sits at `r=1` → `Q=1`; the **chiral**
operator (mass anticommutes with `Γ_χ`) sits at `r=1/2` → `Q=2/3`. The charged leptons
are the **chiral (Dirac) sector**.

Therefore `r=1/2` is fixed by a **sector label (chirality)**, not by a measure /
positivity / modular extremum. This note's finding — that the derived **tracial**
reference induces `(1,2)` → `Q=1` — characterizes the **non-chiral complement sector**;
it is the *expected* result and is **NOT evidence against `Q=2/3`**. The task is
sector-*identification* (source the chirality), not breaking the measure tie "in favor
of" `Q=2/3`. The note's value is the precise statement that `Q=2/3`'s selector is **not**
recoverable from any tested measure/positivity principle — so it must come from the
chirality source, and the charged-lepton sector is correctly the *non-tracial* one.

## Question (the angle)

The charged-lepton Koide value reduces (retained
`koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10`,
`charged_lepton_koide_cone_algebraic_equivalence_narrow_theorem_note_2026-05-10`)
to one weighting of the two `C₃` isotypes / minimal central idempotents of
`ℝ[Z₃] = ℝ ⊕ ℂ` (`e₀` = singlet, rank 1; `e₁` = doublet, rank 2):

- **(i) dimension / trace / Plancherel** weight `(1,2)` → `r=|b|²/a²=1` → **Q=1**;
- **(ii) block / idempotent-count** weight `(1,1)` → `r=1/2` → **Q=2/3** (observed).

Representation theory ranks neither a priori (retained no-gos
`koide_frobenius_isotype_split_uniqueness` and `action_normalization` both
decline to rank them).

**Is there an A1+A2-NATIVE principle — reflection positivity, KMS/modular
condition, locality/cluster, emergent-time T-positivity, or the on-site qubit
unit-trace normalization (`Tr=1`) — that SELECTS one of these two measures?**

## Verdict — NO (with a sharp asymmetry, and it does NOT favor the observed value)

**The tie is not broken in favor of the observed `Q=2/3` by any tested native
principle.** More precisely, the tested principles split cleanly into two camps,
and *neither camp lands on the observed value*:

1. **Reflection positivity / emergent-time T-positivity are AGNOSTIC.** The OS /
   transfer-matrix positivity Gram is positive for **both** candidate measure
   points (`r=1/2` and the `r=1` endpoint), and is PSD identically whether the
   doublet is realized as **one complex mode** (det_C → (1,1)) or **two real
   modes** (det_R → (1,2)) — the count lives in the field content/statistics,
   invisible to the covariance. RP/T-positivity selects only the **Hermitian
   readout class** (`H=iD`, the signed/Brannen reading), which holds for *every*
   `r`; it does not rank the measure. (Reproduces and re-verifies
   `FLAVOR_MEASURE_POSITIVITY_AGNOSTIC_NOTE_2026-05-31`.)

2. **On-site qubit unit-trace + KMS(β=0) + locality/cluster + Plancherel all
   FORCE the dimension measure (1,2) → Q=1.** This is the decisive, computed
   result of this angle:
   - The framework's **derived** reference state is the unique tracial state
     `ρ = ⊗ₓ I/2` (retained `pre_record_reference_state_tracial_derivation`,
     `powers_uhf_tracial_uniqueness`, `tomita_tensor_trace`). Restricted to the
     generation carrier it is `ρ_gen = I₃/3`, and its Born weight on the two
     central blocks is **`Tr(ρ e₀) : Tr(ρ e₁) = 1/3 : 2/3 = (1,2)`** — the
     dimension weighting → `r=1` → **Q=1** (runner BLOCK 2, exact).
   - The trace is the **β=0 (infinite-temperature) KMS state**; its
     Tomita–Takesaki modular operator is **`Δ=1`** (verified: the Tomita
     `S(x)=x*` is HS-anti-unitary, so `Δ=S^#S=1`, `S²=I`; runner BLOCK 3). A
     trivial modular flow reweights nothing → uniform per direction → again
     `(1,2)` → Q=1.
   - **Locality/cluster** gives the reference as a *product* state; the induced
     generation-block weight is `(1,2)` for **every** region size `|Λ|` (runner
     BLOCK 5). The product/trace structure is generation-block-agnostic — it
     fixes inter-site independence, not the within-doublet ratio, and what it
     *does* induce is again `(1,2)`.

So the native principles I was asked to test do **not** support the observed
value. The ones that have any selection power at all (`unit-trace`, `KMS`,
`locality`, `Plancherel`) all point at **`(1,2)` → Q=1**, the framework default;
the ones that are blind (`RP`, `T-positivity`) point at neither.

**The observed `(1,1)` → r=1/2 → Q=2/3 requires a NON-tracial / finite-β
weight** that none of these principles supply: realizing `(1,1)` as a Gibbs
factor needs `w₀/w₁ = exp(−β·gap) = 1/2`, i.e. `β·gap = ln 2 ≠ 0` — a finite
temperature / a dynamics (runner BLOCK 3 exhibits an explicit witness density
`diag(1/5,2/5,2/5)` with `gap = ln 2` that lands `r=1/2`, and verifies it is
**not** the tracial `I/3`). (Reproduces
`KOIDE_CARRIER_SCORING_NEEDS_NONTRIVIAL_MODULAR_NOTE_2026-06-02` and
`FLAVOR_FIND_J_ROUND5`.)

## Anti-overreach discipline (the explicit honesty check)

The project memory records two failure modes to avoid: (a) privileging the
trace/dimension measure as "the consistent one" (a prior overreach toward Q=1),
and (b) privileging block-count toward Q=2/3 just because 2/3 is observed. This
note avoids **both**:

- **Not (b):** no tested native principle forces `(1,1)`. The `(1,1)` state is
  exhibited as fully admissible (PD, `C₃`-invariant, unit-trace — runner BLOCK 6)
  but **non-tracial**; admissibility is not forcing. The observed value remains
  an *unforced* selection from the standpoint of these principles.
- **Not (a):** the claim is **not** that `(1,2)`/Q=1 is "the consistent" or
  "the only" measure. `(1,1)` survives every native *constraint* (positivity,
  `C₃`-invariance, unit trace) — it is a different admissible state, not a
  forbidden one (runner BLOCK 6). The precise, defensible statement is the
  weaker and correct one: **among the tested native principles, the only one
  with a distinguished *selection* (the derived tracial reference) selects
  `(1,2)`; the others are blind.** This is a statement about which state the
  framework's *derived reference* is, not a ranking of the abstract measures.
  The retained no-gos `koide_frobenius_isotype_split_uniqueness` and
  `action_normalization` (both decline to rank `(1,1)` vs `(1,2)`) are **not**
  contradicted — this note does not rank the measures either; it locates which
  one the *native reference state* induces, and shows it is the one giving Q=1.

So the honest verdict is a **sector-localization** (NOT a negative for the observed
value): the native positivity/normalization/modular structure places the framework's
*derived tracial reference* on `(1,2)` → `Q=1` — i.e. the **non-chiral / democratic
complement sector**. This is **not** evidence against `Q=2/3`: by retained
`koide_anticommuting_operator_derivation_theorem_note_2026-05-10`, `Q=2/3` is the
value of the **chiral** operator class (mass anticommutes with `Γ_χ`), a *different,
coexisting* sector on the same family `Q = 1/3 + (2/3)·r`. The charged leptons are
that chiral sector, so they are *expected* to sit on a **non-tracial (chiral)** state
rather than on the tracial reference. The tested measure/positivity principles neither
forbid nor supply that state because its selector is **chirality**, not a measure
extremum — which is exactly what this note establishes (see Framing correction at top).

## Derive-vs-posit ledger

| principle | acts how on the (1,2)/(1,1) tie | derive or posit |
|---|---|---|
| Reflection positivity (OS) | AGNOSTIC — PSD for both counts, every physical r | selects readout class only (derived); measure: no selection |
| Emergent-time T-positivity | AGNOSTIC — same as RP (positive transfer ⟹ Hermitian H) | same |
| On-site qubit unit-trace `Tr=1` | FORCES `(1,2)` → Q=1 (derived reference `ρ=⊗I/2` ⟹ `ρ_gen=I/3` ⟹ blocks 1:2) | derived (retained tracial-reference chain) → Q=1 |
| KMS / Tomita–Takesaki modular | trace is β=0, `Δ=1` ⟹ no reweighting ⟹ `(1,2)` → Q=1 | derived → Q=1 |
| Locality / cluster | product/trace structure ⟹ `(1,2)` for all `|Λ|` | derived → Q=1 |
| (1,1) → Q=2/3 | requires non-tracial finite-β Gibbs weight (`β·gap=ln2`) | **POSIT / imported dynamics — not supplied by any tested native principle** |

## Import flags

- **IMPORT FLAG: requires user approval — a finite-β (non-tracial) reference
  state / temperature on the generation carrier.** This is the single ingredient
  the observed `(1,1)` → r=1/2 needs and that no tested native principle
  supplies. The framework's derived reference is the β=0 trace; selecting
  `(1,1)` requires departing from it. Adopting any finite-β / non-tracial weight,
  or a dynamics that lands one, is an import beyond A1+A2+retained.
- The reflection-positivity anchors (`axiom_first_reflection_positivity`,
  `osterwalder_schrader_from_framework`, `free_field_os_wightman_reconstruction`)
  are **`unaudited`** on the live ledger and are therefore **not load-bearing**
  here; the RP-agnosticism conclusion is carried by the explicit covariance
  computation (runner BLOCK 4), independent of those rows' tier.

## What is established vs not

- **Established (verified):** the exact line `Q=1/3+(2/3)r`; the two measure
  points; that the derived tracial reference induces `(1,2)`/Q=1 on the
  generation blocks via four independent native handles (unit-trace Born weight,
  `Δ=1` modular triviality, locality/`|Λ|`-independence, Plancherel); that RP/
  T-positivity are blind to the count; that `(1,1)` is admissible-but-non-tracial
  and needs a finite-β input.
- **Not established / not claimed:** that `(1,2)`/Q=1 is "the" measure or that
  `(1,1)`/Q=2/3 is excluded; a derivation of `Q=2/3`; any new axiom or import.

## Relation to the existing chain

This is the **native-principle** half of the angle named across the prior notes
(`FLAVOR_LANE_PANEL_REDUCES_TO_DOUBLET_MODE_COUNT`,
`FLAVOR_MEASURE_POSITIVITY_AGNOSTIC`, `FLAVOR_FIND_J_ROUND5`,
`KOIDE_CARRIER_SCORING_NEEDS_NONTRIVIAL_MODULAR`,
`KOIDE_READOUT_LANE_DEMARCATION`). It consolidates them into one statement for
the specific principle-set (RP, KMS/modular, locality, T-positivity, unit-trace)
and adds the explicit **unit-trace Born-weight computation** showing the derived
on-site qubit normalization induces `(1,2)` on the generation blocks. It does not
weaken any retained no-go and does not load-bear on
`closure_c_staggered_dirac_gate` / `koide_phase_aps_eta_parity_route`.

## The next path (open, not closing)

The result sharpens the open object exactly as the prior notes did: `r=1/2`
lives on a **non-tracial finite-β / 2-sector-coarse-grained** weight, and the
live question is whether the **emergent-time dynamics** (not the β=0 reference,
not RP, not locality, all of which give Q=1) *delivers* that finite-β structure
non-circularly — e.g. via a records/einselection 2-sector partition or a
chiral-mass-generation argument, both already flagged as `C³=I`-unobstructed.
The `N`-scaling cross-check survives: `(1,1)` gives `r=1/(N-1)`, tying `r=1/2` to
the derived `n_gen=3` — a structural constraint on any future finite-β
derivation.

## No-Go Discipline Gate (N1–N8)

**Status:** PASS for the narrow native-principle demarcation only. The claim being
gated is NOT "Q=2/3 is excluded" and NOT "Q=1 is the framework's flavor answer."
It is the single demarcation that, among the tested A1+A2-native principles, the
only one carrying a distinguished *selection* (the derived tracial reference)
induces the dimension weight `(1,2)` → Q=1 on the generation blocks, while the
positivity principles are blind to the doublet mode count. The observed
`(1,1)` → r=1/2 → Q=2/3 is the **chiral** operator class (retained
`koide_anticommuting_operator_derivation_theorem_note_2026-05-10`), which
**coexists** with Q=1 on `Q = 1/3 + (2/3)·r` and is selected by a sector label
(chirality), not by any measure tested here.

### N1 — Alternative route enumeration

Each native principle that could try to **break the `(1,2)`-vs-`(1,1)` measure
tie in favor of the observed value** was evaluated by direct covariance / Born-
weight computation in the runner. None lands on `(1,1)` / Q=2/3; the camp that
has any selection power lands on `(1,2)` / Q=1, and the positivity camp lands on
neither.

| route | principle | what it would attempt | computed action on the tie | runner | marker |
|---|---|---|---|---|---|
| (P1) | Reflection positivity (OS) | Rank `(1,2)` vs `(1,1)` by demanding a PSD reflection Gram only for one count | **AGNOSTIC** — Gram is PSD for `det_C`→(1,1) AND `det_R`→(1,2), and for every `r∈[0,1]`; the count lives in field content/statistics, invisible to the covariance. Selects only the Hermitian readout class (`H=iD`). | BLOCK 4 | ATTEMPTED → no selection |
| (P2) | Emergent-time T-positivity | Use positive transfer/`H≥0` to force one count | **AGNOSTIC** — collapses to (P1): positive transfer ⟹ Hermitian `H`, holds for every `r`; does not see the within-doublet ratio. | BLOCK 4 | ATTEMPTED → no selection |
| (P3) | On-site qubit unit-trace `Tr=1` | Read the within-doublet ratio off the derived on-site normalization | **FORCES `(1,2)`/Q=1** — derived reference `ρ=⊗ₓ I/2` ⟹ `ρ_gen=I₃/3` ⟹ Born blocks `Tr(ρe₀):Tr(ρe₁)=1/3:2/3` ⟹ r=1. | BLOCK 2 | ATTEMPTED → selects (1,2) |
| (P4) | KMS / Tomita–Takesaki modular | Reweight the blocks by a non-trivial modular flow | **FORCES `(1,2)`/Q=1** — the trace is the β=0 KMS state; `S(x)=x*` HS-anti-unitary ⟹ `Δ=S^#S=1`, `S²=I` ⟹ trivial flow ⟹ no reweighting ⟹ uniform/direction. | BLOCK 3 | ATTEMPTED → selects (1,2) |
| (P5) | Locality / cluster | Source the ratio from inter-site cluster structure | **FORCES `(1,2)`/Q=1** — product/trace structure fixes inter-site independence, not the within-doublet ratio, and the weight it *does* induce is `(1,2)` for every region size `\|Λ\|`. | BLOCK 5 | ATTEMPTED → selects (1,2) |
| (P6) | Plancherel / dimension weight | Take the canonical isotype dimension weight directly | identical endpoint to (P3): `(1,2)` → Q=1; it is the dimension/trace measure already named in (i). Not an independent breaker — the *same* weight the derived reference induces. | BLOCK 1–2 | ATTEMPTED → selects (1,2) |
| (P7) | finite-β / non-tracial Gibbs factor | Realize `(1,1)` as `w₀/w₁=exp(−β·gap)=1/2` | reaches `(1,1)` → r=1/2 → Q=2/3, BUT needs `β·gap=ln2≠0` — a temperature/dynamics, **not supplied by any tested native principle**; left as the open finite-β handle (N6), not a closure here. | BLOCK 3 (witness `diag(1/5,2/5,2/5)`) | OUT OF SCOPE (open) |

No tested native principle in (P1)–(P6) breaks the tie *in favor of* the observed
value; the breaker the observed value would need is (P7), which is an import the
note does not make.

### N2 — Wall-independence audit

The principle set collapses to **two mutually independent facts**, not a stack of
correlated walls:

1. **Positivity blindness** (P1=P2): the OS / transfer Gram is PSD for both
   counts and every `r`. This is a property of the covariance, established by
   direct computation (BLOCK 4), with no dependence on which reference state the
   framework derives.
2. **Derived-reference-is-the-trace** (P3=P4=P5=P6 all reduce to it): the unique
   tracial reference `ρ=⊗I/2` restricts to `I₃/3`, whose Born/modular/cluster/
   dimension reads all give `(1,2)`. This is a property of the *state*, carried by
   the retained tracial-reference chain, independent of the positivity covariance.

Closing fact (1) (e.g. a future statistics-selection that fixes `det_C` vs
`det_R`) would NOT close fact (2), and vice versa; and **neither fact yields
`(1,1)`**. The four handles inside fact (2) are not four independent walls —
they are four reads of the single tracial reference (Born weight, `Δ=1` modular,
`|Λ|`-independent cluster, Plancherel dimension), which is why they agree. The
genuinely independent lever that *does* land `(1,1)` lives outside both facts: a
finite-β / non-tracial weight (P7), i.e. the chirality / dynamics sector, audited
separately.

### N3 — Hidden-wall scan

The words "native", "derived", "positivity", and "modular" are not used as
concealed retained inputs for the demarcation:

- The `(1,2)` selection is sourced **explicitly** to the retained tracial chain
  (`pre_record_reference_state_tracial_derivation`,
  `powers_uhf_tracial_uniqueness`, `tomita_tensor_trace`) and to the on-site
  qubit `Tr=1` normalization — named load-bearing rows, all `retained` on
  `origin/main` (see Tiers table).
- The RP / OS rows (`axiom_first_reflection_positivity`,
  `osterwalder_schrader_from_framework`,
  `free_field_os_wightman_reconstruction`) are **`unaudited` on the live ledger
  and explicitly NOT load-bearing**: the agnosticism conclusion is carried by the
  direct covariance computation (BLOCK 4), so the demarcation does not borrow tier
  from an unaudited positivity claim. (Stated also under "Import flags".)
- The finite-β witness `diag(1/5,2/5,2/5)` is an **exhibited, non-adopted**
  state, not a hidden admission — it is shown precisely to *fail* to be the
  tracial `I/3` while landing r=1/2, demonstrating the import (P7) is real and
  external, not smuggled in.

No PDG value, no fitted selector, and no chiral operator is introduced by this
note; the chirality that *does* select `(1,1)` is cited (retained
`koide_anticommuting_operator_derivation_theorem`), not constructed here.

### N4 — Residual matching

The witnesses this note touches are matched to the residual they actually attack;
non-matching witnesses are flagged as context, not used as load-bearing support
for the demarcation.

| cited witness | residual it governs | residual here | match? |
|---|---|---|---|
| `pre_record_reference_state_tracial_derivation_note_2026-05-20` (`retained`) | the framework's derived reference state IS the trace `ρ=⊗I/2` | exactly the state whose generation-block Born weight is computed as `(1,2)` (BLOCK 2) | yes |
| `powers_uhf_tracial_uniqueness_…` (`retained`) | uniqueness of the tracial state on the qubit lattice | guarantees `(1,2)` is the *unique* tracial read, not one of many | yes |
| `tomita_tensor_trace_…` (`retained`) | tensor-factor traciality | underwrites the `Δ=1` modular step (BLOCK 3) | yes |
| `koide_circulant_q_two_thirds_algebraic_narrow_theorem_…` (`retained`) | the exact line `Q=1/3+(2/3)r` | the algebra both measure points sit on | yes |
| `charged_lepton_koide_cone_algebraic_equivalence_…` (`retained`) | biconditional `Q=2/3 ⟺ r=1/2` | fixes which `r` the observed value names | yes |
| `koide_frobenius_isotype_split_uniqueness_note_2026-04-21` (`retained_no_go`) | **declines** to rank `(1,1)` vs `(1,2)` a priori | cited ONLY for the known absence of an a-priori ranking; this note does not rank the abstract measures, so it does not contradict the decline | partial (compatible) |
| `action_normalization_note` (`retained_no_go`) | **declines** to rank `(1,1)` vs `(1,2)` a priori | same as above — compatible, not contradicted | partial (compatible) |
| `koide_anticommuting_operator_derivation_theorem_note_2026-05-10` (`retained`) | non-chiral→r=1→Q=1; chiral→r=1/2→Q=2/3 | the coexistence frame: places the charged leptons in the chiral (non-tracial) sector, so the tracial `(1,2)` read is the *complement* sector, not a refutation | yes (frame) |
| `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16` (`retained_bounded`) | chirality decoupling on the generation factor | listed because this note introduces NO chiral operator; not a support witness for `(1,2)` | no (context) |

The two retained no-gos are the crux of N4: they *decline to rank* the measures,
and this note **respects that decline** — it does not rank the abstract measures
either. It locates which measure the *derived native reference state* induces
(`(1,2)`), which is a strictly different and weaker statement than "`(1,2)` is the
correct measure."

### N5 — Rhetoric audit

Every superlative is scoped to the coexistence frame (see "Framing correction"),
not to an exclusion of the observed value:

- "**The tie is not broken in favor of the observed value**" means: **no native
  MEASURE / positivity / modular principle tested here breaks it** — the actual
  selector of `(1,1)` / Q=2/3 is **chirality** (a sector label), supplied by
  retained `koide_anticommuting_operator_derivation_theorem`, not by a measure
  extremum. It does NOT mean `(1,1)` is forbidden, and it is NOT evidence against
  Q=2/3.
- "**Native principles select `(1,2)` / Q=1**" means: the tested *derived
  reference* (trace), its `Δ=1` modular flow, its product/cluster structure, and
  the Plancherel dimension weight all read `(1,2)`. This is a statement about
  which state the framework's derived reference IS — i.e. the **non-chiral /
  democratic complement sector** — not a claim that `(1,2)` is "the" flavor
  measure or that the charged leptons live on it.
- "**FORCES (1,2)**" is local to the *tracial* reference: given `ρ=⊗I/2`, the
  block weight is `(1,2)` necessarily. It does not assert the *physical* mass-
  generation reference must be `ρ=⊗I/2`; the chiral charged-lepton sector is
  *expected* to sit on a non-tracial state (N7).

The honest reading is a **sector-localization**: the native positivity/normalization/
modular structure places the *derived tracial reference* on `(1,2)` → Q=1, i.e. the
non-chiral complement; the charged leptons are the **coexisting chiral sector**,
selected by chirality, off this reference.

### N6 — Partial-closure path scan

Two non-axiom partial-closure paths to the observed `(1,1)` remain open, and the
note advances toward them rather than closing them:

1. **The chirality source.** Per retained
   `koide_anticommuting_operator_derivation_theorem`, the chiral operator class
   (mass anticommutes with `Γ_χ`) sits at r=1/2 → Q=2/3 by construction. The
   open object is *sourcing* that chiral grading on the generation factor (the
   shared gate with generation-identification, flagged `C³=I`-unobstructed). This
   note neither builds nor forbids that operator; it shows the *measure* angle
   cannot substitute for it.
2. **A native finite-β reference.** The observed `(1,1)` is the Gibbs weight
   `w₀/w₁=exp(−β·gap)=1/2`, `β·gap=ln2`. Whether the emergent-time dynamics (NOT
   the β=0 reference, NOT RP, NOT locality) *delivers* that finite-β structure
   non-circularly — e.g. via a records / einselection 2-sector partition — is the
   live handle. The `N`-scaling constraint `(1,1)⇒r=1/(N-1)` ties r=1/2 to the
   derived `n_gen=3`, a structural check any future finite-β derivation must pass.

Neither path is called a new axiom here; both are routes for future audited
positive work.

### N7 — Steelman

The strongest objection: the *physical* reference for charged-lepton mass
generation need not be the pre-record β=0 trace at all. Mass generation could be
governed by a finite-β equilibrium or by the chiral Dirac operator's own
spectral state, either of which is a legitimately *non-tracial* reference. On the
coexistence frame this is not a defeat of the note but its **point**: the charged
leptons ARE the chiral / non-tracial sector, so they are *expected* to sit off the
tracial reference, and the demarcation's job is precisely to show the *measure*
principles cannot fix r=1/2 — the chirality / finite-β selector must. This
steelman blocks any (unmade) broader claim that "the framework's flavor answer is
Q=1"; it does not break the scoped demarcation, because the demarcation only says
the tested measure principles induce `(1,2)` on the *tracial reference*, which is
true regardless of which sector the physical leptons occupy.

### N8 — Cross-cycle echo

The recurring failure mode in this repo's flavor lane is to test one
representative state, find Q=1, and overclaim "the framework predicts Q=1" (the
memory-recorded mid-campaign overreach). This note avoids that echo on **both**
sides: it does not claim `(1,2)` / Q=1 is "the" measure (it is the tracial-
reference read of the non-chiral complement), and it does not privilege block-
count toward Q=2/3 just because 2/3 is observed (BLOCK 6 shows `(1,1)` is
admissible-but-non-tracial, fully allowed by every native *constraint*). The
`(1,1)`-vs-`(1,2)` wall is the same wall named across the prior flavor notes
(`FLAVOR_MEASURE_POSITIVITY_AGNOSTIC`, `KOIDE_CARRIER_SCORING_NEEDS_NONTRIVIAL_MODULAR`,
`FLAVOR_FIND_J_ROUND5`); none was retired by a native measure principle, and this
note keeps it narrow (a specific principle-set, on the tracial reference) and
relabels it not as an axiom gap but as a **chirality / finite-β sector selector**
already cited as retained.

## Tiers verified on `origin/main` (`.rows[claim_id].effective_status`)

| claim_id | effective_status | role here |
|---|---|---|
| `pre_record_reference_state_tracial_derivation_note_2026-05-20` | `retained` | derived reference state = trace `ρ=⊗I/2` (the unit-trace selection) |
| `powers_uhf_tracial_uniqueness_on_qubit_lattice_narrow_theorem_note_2026-05-20` | `retained` | uniqueness of the tracial state on the qubit lattice |
| `tomita_tensor_trace_on_finite_dim_matrix_narrow_theorem_note_2026-05-20` | `retained` | tensor traciality (used in BLOCK 3 modular argument) |
| `koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10` | `retained` | `Q=1/3+(2/3)r` algebra |
| `charged_lepton_koide_cone_algebraic_equivalence_narrow_theorem_note_2026-05-10` | `retained` | `Q=2/3 ⟺ r=1/2` biconditional |
| `koide_frobenius_isotype_split_uniqueness_note_2026-04-21` | `retained_no_go` | declines to rank `(1,1)` vs `(1,2)` |
| `action_normalization_note` | `retained_no_go` | declines to rank `(1,1)` vs `(1,2)` |
| `koide_q23_block_weight_frontier_bounded_note_2026-05-29` | `retained_bounded` | block-weight algebra anchor |
| `luders_rule_from_composition_consistency_note_2026-05-20` | `retained_bounded` | records-flow anchor for the finite-β next path |
| `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16` | `retained_bounded` | chirality decoupling (this note introduces no chiral operator) |
| `inner_automorphism_invariance_tracial_identification_narrow_theorem_note_2026-05-20` | `audited_conditional` | trace = inner-automorphism-invariant state (context, not load-bearing) |
| `flavor_ba_ratio_bound_hs_equipartition_note_2026-05-30` | `audited_conditional` | HS-equipartition characterization (context) |
| `axiom_first_reflection_positivity_theorem_note_2026-04-29` | `unaudited` | RP anchor — **not load-bearing** (RP conclusion carried by direct computation) |
| `osterwalder_schrader_from_framework_narrow_theorem_note_2026-05-27` | `unaudited` | OS anchor — **not load-bearing** |
| `free_field_os_wightman_reconstruction_conditional_theorem_note_2026-05-30` | `unaudited` | statistics-selection gap (G3) — context for det_C/det_R blindness |
