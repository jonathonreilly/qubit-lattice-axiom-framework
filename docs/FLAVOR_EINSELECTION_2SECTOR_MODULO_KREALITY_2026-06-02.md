# Flavor — einselection reduces the *partition* half of the gate to K-reality (sound), but does NOT deliver r=1/2: H is already block-diagonal, and the genuine Born/thermalizing measure gives r=1, not r=1/2. Residual = two physical inputs (K-reality + the block-counting measure).

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Claim boundary:** a genuine reduction (partition→K-reality) + an honest self-correction of the prior "thermalizing→r=1/2" claim. Not closure.
**Runner:** `scripts/flavor_einselection_2sector_modulo_kreality_2026_06_02.py` (SCORECARD 5/5).
**Source:** workflow `wf_bfb916fc` — 5 routes + 3-lens verification + synthesis (18 agents).

## The question
Does a C₃-invariant + K-real (time-reversal-real) monitored interaction **einselect** the 2 isotype
sectors as the pointer/decoherence partition — so the thermalizing flow coarse-grains by them and r=1/2
is derived? (The last equivalent framing of the gate.)

## Verdict: the *partition* half reduces to K-reality (sound); the *value* r=1/2 is not delivered

### SOUND — einselection→2-sector partition (modulo K-reality)
A C₃-invariant + **K-real** monitored Hermitian observable lies in `span_ℝ{I, C+C²}`; `eig(C+C²)={2,−1,−1}`
— singlet isolated, **doublet degenerate**. So it resolves only the **2 real-irreducible blocks**
(singlet P₀ rank 1, doublet P₁ rank 2). Resolving ω from ω² (the 3-mode/spectral partition → r=0)
*strictly requires* the **K-odd** observable `i(C−C²)` (verified conj=−itself, T-violating). So Zurek
einselection by a K-real coupling **kills the r=0 partition** and einselects the 2-sector partition —
**non-circular, modulo K-reality.** This sharpens the partition half of the gate to **one physical
predicate**: *is the generation-monitoring coupling time-reversal-real?* (Route 4 sharpens it further to
transpose-symmetry `b=c̄`.)

### GAP A — K-reality is posited, not derived
The emergent-time mechanism is **conjugation-even**: `b→b̄` is a spectrum-preserving transpose similarity
(retained_bounded `koide_emergent_time_eta_conjugation_parity`), so it is **blind to arg(b)** and cannot
select the real axis (δ=0). K-reality is *automatic on the whole cone* (it holds at r=1 too) → it carries
**no selective information** distinguishing r=1/2 from r=1. So K-reality = the same **δ=0 / det_C /
Brannen-readout / chirality pin** relabeled in time-reversal language.

### GAP B — the value r=1/2 is not delivered (this *qualifies* the prior thermalization claim)
Even granting K-reality and the 2-block partition:
- **H is already block-diagonal in {P₀,P₁} for *every* r** (verified `‖P₀ H P₁‖~10⁻¹⁶`, by C₃-invariance).
  So the pointer map `P₀(·)P₀+P₁(·)P₁` is a **literal no-op** — einselection places **zero** constraint on
  the inter-block *power* ratio r.
- The genuine **Born/tracial max-entropy** state `ρ=I/3` weights the blocks by **dimension** (`Tr P₀:Tr P₁
  = 1:2`) → **r=1 → Q=1**. r=1/2 needs **equal power per block** (`3a²=6|b|²`, the HS/block-*counting*
  measure) — a *separate* input. So the prior result's "thermalizing flow → r=1/2" used the **2-sector
  (block-counting) entropy, not the Born entropy**; the genuine second-law/Born equilibrium is **r=1**, and
  r=1/2 is the **equal-power-per-block (det_C)** equilibrium. *(Honest correction to
  `FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW`: r=1/2 is the max of the 2-sector entropy and is stable
  under a block-counting-weighted flow, but it is **not** the Born/second-law attractor — that is r=1. The
  endpoint-exclusion and "r=1/2 = 2-sector equipartition stationary point" parts stand; the "second law
  makes it stable" part overclaimed and is corrected here.)*

## Net — the residual is two named physical inputs (both standing gates, both = Koide's free fit)
The charged-lepton value r=1/2 reduces to **two** physical inputs, neither currently derived from
framework baseline+emergent-spacetime:
1. **K-reality** (time-reversal-reality of the generation coupling / δ=0 / transpose-symmetry `b=c̄`) →
   selects the **2-block partition** over the 3-mode one (r=1/2-vs-r=0). *Posited* (emergent-time is
   conjugation-even).
2. **Equal-power-per-block (det_C / block-counting) vs dimension (Born/det_R)** → selects **r=1/2 over
   r=1** *within* the 2-block structure. The standing det_C gate; the Born/second-law measure gives r=1.

Both are physical, in-principle-derivable, and match the literature (Koide leaves the per-sector ratio a
free fit). The campaign has now mapped the gate in *all* its equivalent framings — measure (det_C/det_R),
state (trace/center), partition (einselection), dynamics (thermalizing flow) — and they consistently
collapse to these two inputs.

## The next paths this opens (not closing)
- **For input 1 (K-reality):** find an emergent **T-odd** structure (the emergent-time arrow is even;
  CP-violation / the chirality grading is the candidate T-odd ingredient) that *does* select δ=0 — or
  show δ=0 follows from the charged-lepton (real-mass) reality datum.
- **For input 2 (block-counting vs Born):** the genuine question — does anything make the *equal-power*
  (block-counting) measure physical over the Born/dimension one? This is the as-yet-unreduced det_C core; the
  honest current status is that the Born measure gives r=1 and r=1/2 is the block-counting alternative.

## Provenance (verified 2026-06-02)
- eig(C+C²)={2,−1,−1}, i(C−C²) K-odd, H block-diagonal for all r, Born→(1/3,2/3)→r=1 vs equal-power→r=1/2, b→b̄ spectrum-preserving: verified directly (runner 5/5).
- Anchors: `koide_emergent_time_eta_conjugation_parity` (retained_bounded), `strong_cp_rp_half_cannot_forbid_cp_odd_imaginary` (retained_no_go), `koide_c3_generator_rephasing_obstruction` (retained), `frobenius_isotype_split_uniqueness` (retained_no_go). Matches Koide arXiv:1301.4143 (free per-sector fit).
- Honestly corrects the "second-law → r=1/2" overclaim of the prior note; the stationary-point + endpoint-exclusion content stands.
- Does not load-bear on `closure_c_staggered_dirac_gate` / `koide_phase_aps_eta_parity_route`.
