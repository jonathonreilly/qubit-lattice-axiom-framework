# Flavor — measure-from-the-cut: the classical-record cut (T2) makes BLOCK-COUNT the record-natural (partition-only) measure, establishing r=1/2 as the CLASSICAL-RECORD setting and r=1 as the WITHIN-BLOCK setting — TWO distinguished settings on the dial, NOT a forcing

**Date:** 2026-06-04
**Claim type:** meta
**Claim boundary:** a *measure-localization* result. It establishes that the charged-lepton
isotype-weight dial has **two record-distinguished settings** (block-count → r=1/2, Born/dimension →
r=1) and that the **block-count setting is the one intrinsic to a partition-only / label-valued
classical record** (T2), while Born is the within-block / projector-rank reading. It does **NOT**
force r=1/2, does **NOT** add an axiom or import, and explicitly leaves the dial open (the same
record bit governs other sectors). It relocates — does not close — the standing det_C/det_R datum.
**Runner:** `scripts/flavor_measure_from_cut_blockcount_setting_2026_06_04.py` (SCORECARD 25/25).
**Cache:** `logs/runner-cache/flavor_measure_from_cut_blockcount_setting_2026_06_04.txt`.

---

## ⚠️ Frame (explicit, governs every claim below)

This note does **not** try to derive or force `r=1/2`. The charged-lepton Koide modulus
`r = |b|²/a²` (`Q = 1/3 + (2/3)r`) lives on a multi-valued **measure dial** whose distinguished
settings are `r ∈ {0, 1/2, 1}` (`Q ∈ {1/3, 2/3, 1}`). A mechanism that yielded `r=1/2` for **all**
sectors would be a **failure** — it is falsified by quarks (`Q≈0.85/0.73`) and neutrinos (`Q≈1/3`).
The result tested and obtained here is the weaker, correct one: **block-count is the record-natural
(partition-only) measure → r=1/2 is the classical-record setting; Born/dimension is the within-block
measure → r=1 is the full-quantum setting.** Two settings, neither forced, dial left open.

---

## The new angle: measure-from-the-cut (within-block information)

The two competing measures on the einselected 2-block partition of the generation algebra
`ℝ[Z₃] = ℝ(singlet) ⊕ ℂ(doublet)` differ in **exactly one thing — within-block information**:

| measure | what it reads | weights | `r` | `Q` |
|---|---|---|---|---|
| **block-count** | the **partition** only (which block) | (1, 1) | **1/2** | **2/3** |
| **Born / dimension** | the **number of states inside** each block (dim) | (1, 2) | **1** | **1** |

The record axiom's "real" stance (**T2**) derives the 2-block partition: the recordable/frozen
structure is the **center** (the Wedderburn block labels — the classical/quantum cut), while
**within-block** (the simple-factor interior `M_n`) is reversible/quantum and **not** classically
recorded. The claim under test: *a record that resolves only the partition (T2) can only block-count;
Born/dimension requires the within-block state-count the classical record provably does not carry.*

---

## What the runner establishes (25/25)

**§1 — the cut (T2).** The two central idempotents `e₀=(I+C+C²)/3` (rank 1, singlet) and `e₁=I−e₀`
(rank 2, doublet) partition the identity; they are the only central atoms of the einselected
C₃-commutant `span{I,C,C²}`. The **center of a simple block `M_n` is the scalars** — so within a block
there is **no further recordable central label**; only the block label is recordable. The recordable
partition is exactly `{singlet, doublet}` (2 cells). The real Wedderburn type that sharpens everything:
the doublet is the **FS-complex block** carrying its own native complex structure
`J_cs=(C−C²)/√3` (real, C₃-equivariant, `J_cs²=−e₁`) — the within-block datum.

**§2 — block-count is the unique partition-only measure → r=1/2.** By the record axiom's additivity
`I(R₁⊔R₂)=I(R₁)+I(R₂)` plus **label-permutation symmetry** (a partition-only record has no within-cell
handle to break the singlet↔doublet label symmetry), the **unique** measure definable from the bare
partition is **counting**: each block = 1 unit → (1,1). A uniqueness sweep confirms only symmetric
weights `w₀=w₁` are partition-only-definable; every asymmetric weight (including Born's (1,2)) needs an
external label-distinguishing (size) input. Block-count = equal **power per block**
(`‖aI‖²=3a² = ‖bC+b̄C²‖²=6|b|²`) → **r=1/2** → **Q=2/3**, and `r=1/2` is the equal-2-block-power
(max 2-cell Shannon `ln 2`) point — the partition-only record's MaxEnt setting.

**§3 — Born/dimension requires within-block info → r=1.** The Born/tracial reference `ρ=I/3` weights
the blocks by **dimension** (`Tr e₀:Tr e₁ = 1:2`) → populations `(1/3, 2/3)`. Equal power **per
within-block state** (`3a²/1 = 6|b|²/2`) → **r=1** → **Q=1**. The (1,2) Born weights are literally the
**ranks** of the central idempotents — within-block state counts, an **operator attribute** beyond the
bare "which block" label.

**§4 — the distinction made operational.** Two algebras with the **same center-as-a-set-of-atoms**
(2 labels) but **different block dimensions** (the real carrier `ℝ⊕ℂ`, dims (1,2); a toy `ℝ⊕ℝ`, dims
(1,1)) produce an **identical label-record** but **different Born weights**. Hence: **block-count is
dimension-invariant; Born is dimension-dependent.** A partition-only record can realize block-count but
**provably not** Born. This is the **forward link**: *partition-only ⇒ dimension-invariant ⇒ not-Born ⇒
(with additivity) block-count.* It is also **not** a relabeling of Born — the two differ whenever a
block has dim > 1 (the doublet, dim 2), guarding against the scalar-relabeling trap that killed the
`r↦1−r` self-dual escape in prior panels. The label-vs-rank bit **is** exactly the standing det_C/det_R
fork (doublet = one complex mode vs two real modes).

**§5 — honesty + the dial stays open.** The dial is genuinely multi-valued (`r∈{0,1/2,1}` →
distinct `Q`). The mechanism is **per-sector** (a record bit), **silent** on quarks/neutrinos (observed
`r_up≈0.775`, `r_ν≈0` ≠ 1/2) — so it does **not** collapse all sectors to `r=1/2`. Both settings sit on
the **retained free cone** `koide_frobenius_isotype_split_uniqueness` (the C₃-invariant Gram is the
2-parameter `B = α·Tr(A_t²) + (α+3β)·Tr(A_s²)`; `β=0` → r=1, equal-block → r=1/2; positivity ranks
**neither**) — confirming **settings, not forcing**.

---

## Honesty — is the partition-only → block-count link AIRTIGHT?

**Almost — with exactly ONE named residual, verified and not hidden (§4.3).** The link is airtight
**given that the classical record is LABEL-valued** — i.e. it carries only "which pointer state /
which block," with no retained operator structure, which is the genuine meaning of *classical record*.
Under that reading, §2 (uniqueness) + §4 (dimension-invariance) close the forward implication.

The residual: a central idempotent `e_k`, when resolved **as a projection operator**, carries its
**rank** `Tr(e_k) = dim(block)`. So a record that resolves the center **"as ranked projectors"** already
sees `(1,2)` = Born; one that resolves it **"as bare labels/atoms"** (which-cell, no rank) sees `(1,1)`
= block-count. **T2 ("the center is recordable") is exactly ambiguous between the label-valued and the
projector-rank-valued reading.** Equivalently — and this is the sharper statement — the **center of
`ℝ[Z₃]` is itself `ℝ⊕ℂ`**, so the doublet's central component is the field `ℂ` (real-dim 2) while the
singlet's is `ℝ` (real-dim 1): a record that resolves the center **as a real algebra** (retaining the
Frobenius–Schur field of each atom) **can** read "1 vs 2" and lands on Born; a record that resolves the
center **as the set of central atoms** (the partition) cannot, and lands on block-count.

So the honest verdict is **TWO-SETTINGS-FROM-CUT with the link AIRTIGHT modulo one residual**, *not*
"block-count forced." The residual is **the same single open bit** the consolidated chain-of-custody
already names (det_C/block-count vs det_R/Born) — **relocated**, with sharper resolution, onto the
record's *label-vs-projector-rank* (atoms-vs-real-algebra) reading of T2's recordable center. It is
**not** closed here. (This is consistent with the prior `koide_records_objectivity_conditional` finding
that block-count is one of two named-but-underived inputs; this note explains *why* block-count is the
record-natural one of the two and pins the residual to a single, sharply-posed reading question.)

**Confirmed:** the mechanism leaves the dial **open** — it is silent on the other sectors, so it does
**not** overreach into an all-sector `r=1/2` collapse.

---

## The next paths this opens (not a closing statement)

The residual is now a **single, sharply-posed, framework-internal reading question**, and it is
**unobstructed** (no wall forbids either reading):
- **Does the classical record carry the central idempotent's RANK, or only its LABEL?** Equivalently:
  does T2's "recordable center" mean the **set of central atoms** (→ block-count → r=1/2) or the
  **central real algebra with its FS field** (→ Born/dimension → r=1)? A persistence/objectivity
  argument that a *classical* record is intrinsically **label-valued** (pointer states are
  distinguishable outcomes, not operators-with-rank) would tip it to block-count — the record-natural
  setting. A counter-argument that the FS field `ℂ` on the doublet atom **is** itself frozen/recordable
  would tip it to Born.
- **Lane-assignment companion:** what sector property puts charged leptons (and not quarks/neutrinos)
  on the label-valued / record-natural reading? The dial is open precisely because this is a per-sector
  bit; identifying the bit per sector is the live forward path.

---

## Provenance & anchors (ledger status verified on origin/main, 2026-06-04)

- Central idempotents, the cut, both measures, `Q(r)`, the dimension-invariance distinction, the
  residual rank-exposure, the free-cone span: verified directly (runner 25/25).
- **Load-bearing retained anchors:**
  `three_generation_observable_no_proper_quotient_narrow_theorem` (**retained** — carrier is full
  `M₃(ℂ)`, irreducible);
  `charged_lepton_koide_cone_algebraic_equivalence_narrow_theorem` /
  `koide_cone_three_form_equivalence_narrow_theorem` (**retained** — the exact `Q=1/3+(2/3)r`
  cone biconditional);
  `koide_frobenius_isotype_split_uniqueness` (**retained_no_go** — singlet:doublet ratio FREE, so
  neither measure is forced);
  `action_normalization` (**retained_no_go** — declines to rank (1,1) vs (1,2)).
- **Context (cited, not load-bearing; current ledger status noted):**
  `pre_record_reference_state_tracial_derivation` (**unaudited** — the tracial/Born reference giving
  the r=1 setting);
  `koide_records_objectivity_conditional`, `koide_records_pointer_grounds_block_channel` (**unaudited**
  — prior record-readout framings this note sharpens);
  `flavor_block_count_native_via_Jcs` / `J_cs` complex structure (the native doublet within-block datum).
- **Consolidated standing this slots into:** `CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02`
  (derived-modulo-`AC_φλ`; the value reduces to K-reality + the det_C/det_R measure bit). This note
  addresses the **measure** half: it makes block-count the **record-natural** reading and names the one
  residual that decides it. Matches the literature (Koide arXiv:1301.4143 leaves the per-sector ratio a
  free fit).
- Does **not** load-bear on `closure_c_staggered_dirac_gate` or `koide_phase_aps_eta_parity_route`.
- No new axiom, no import. `claim_type=meta` (a reading/measure-localization on the existing free
  isotype-ratio datum, per the convention-localization precedent).
