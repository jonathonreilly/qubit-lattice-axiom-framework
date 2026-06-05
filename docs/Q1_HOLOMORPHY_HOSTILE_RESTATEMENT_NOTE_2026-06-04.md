# Q1 keystone, angle D (HOSTILE) — "read the doublet holomorphically (det_C) → r=1/2" is a RESTATEMENT of the equal-block measure, not a genuine forcing; and even granting holomorphy, avoiding overreach needs a SECOND input

**Date:** 2026-06-04
**Claim type:** meta
**Claim boundary:** A skeptic's adjudication of one proposed forcing (the "read each real Wedderburn block by its native division algebra → det_C → r=1/2" keystone). It **sets no audit status, assigns no grade, changes no row**, and imports nothing. It re-derives objects already verified on `origin/main` (the diag(3,6,6) HS metric; J_cs measure-neutrality; the det_C↔det_R fork) to test whether the holomorphy framing has independent content. Conclusions are negative/structural.
**Runner:** `scripts/q1_holomorphy_hostile_restatement_2026_06_04.py` (SCORECARD 22/22; numpy linear algebra, deterministic, no RNG).
**Cache:** `logs/runner-cache/q1_holomorphy_hostile_restatement_2026_06_04.txt`.

## The claim under attack
Q1 keystone: the generation Yukawa is *forced* to a holomorphic (`det_C`) reading of the C₃-doublet
coefficient `b`, hence `r = |b|²/a² = 1/2`, hence the charged-lepton `Q = (1+2r)/3 = 2/3`. The proposed
mechanism: "read each real Wedderburn block of `ℝ[Z₃] = ℝ ⊕ ℂ` by its native division algebra" — the
doublet block's endomorphism ring is `ℂ`, so count it *holomorphically* (once). Sister agents test the
forcing, sector-dependence, and chirality. This note attacks the **forcing itself** as a skeptic.

## Setup (all A1-native / standard rep theory; runner GT0–GT3, F1a)
`H = aI + bC + b̄C²` on the generation factor `ℝ³` (C³=I). `ℝ[Z₃] = ℝ(singlet) ⊕ ℂ(doublet)` (two minimal
central idempotents; the doublet's commutant is `ℂ`). A1's coherent-state resolution induces the
Hilbert–Schmidt metric `diag(3,6,6)` on `(a, Re b, Im b)` — **reading-neutral** (it is *simultaneously*
"two real modes" and "one complex mode"). The retained Brannen functional
`Q = (Σλ²)/(Σλ)² = (1+2r)/3` is **phase-independent** (δ=arg b drops out), so the entire question is the
**count `r`**:
- `det_C` (doublet as **one** complex mode): balance `3a² = 6|b|²` → `r = 1/2` → `Q = 2/3` (observed).
- `det_R` (doublet as **two** real modes): balance `3a² = 3|b|²` → `r = 1` → `Q = 1` (maximal hierarchy).

## Per-front verdict

### Front 1 — RESTATEMENT (the central charge): **RESTATEMENT, no independent content**
"Read by native division algebra (`det_C`)" is **arithmetically identical** to "count the `ℂ`-block once"
= the equal-block weight = `AC_φλ` (runner F1a–F1d). The algebra furnishes **two** equally-canonical
per-block invariants: the **block count** `(1,1)` (one minimal idempotent per block → `r=1/2`) and the
**ℝ-dimension** `(1,2)` (`dim_ℝ` of each block → `r=1`). "Native division algebra" picks `(1,1)` **only by
adding a rule** ("count blocks" not "count real dimensions") — and that added rule *is* the `AC_φλ`
choice. Every C₃-/division-algebra-/HS-metric invariant computed is reading-neutral (same `diag(3,6,6)`
for both), so deriving `r=1/2` **presupposes** the block-count choice it claims to produce. This matches
the retained no-go `koide_frobenius_isotype_split_uniqueness` (**retained_no_go**): equal-block-vs-dimension
is the irreducible residual, and **rep theory ranks neither**. The division-algebra language re-encodes
"count the ℂ block once"; it is not a deeper canonical-reading principle.

### Front 2 — RESTRICTION OF SCALARS (the strongest break): **det_C is a CHOICE; det_R is equally canonical (in fact the A1 default) → FATAL to "genuine forcing"**
The complex block, as a complex line, has a holomorphic volume (`det_C`); its **restriction of scalars**
`ℂ→ℝ²` (forget the ℂ-action, keep the ℝ-linear structure) has a real Lebesgue volume (`det_R`). **Both
are standard representation theory** (`Hom_ℂ` vs `Hom_ℝ`); neither is "the" canonical reading without
extra input (runner F2a). Three independent facts make `det_C` an unforced posit, not a forced reading:
- **F2b (decisive).** The only A1-native candidate to license holomorphy — the Schur complex structure
  `J_cs=(C−C²)/√3` — is an automorphism of **both** measures: `exp(θ J_cs)=SO(2)` preserves the real HS
  block (`det g`) **and** has `det=1` (preserves the holomorphic volume). A complex structure is an
  automorphism of *its own* real-plane Lebesgue measure *and* of the holomorphic volume — it **cannot
  distinguish** the two readings. So the *existence* of `J_cs` does **not** select `det_C`. (Reproduces
  retained `flavor_find_J_round1`.)
- **F2c.** C₃ admits **both** invariant bilinears — symmetric `I` (`det_R`) and antisymmetric `A=C−C²`
  (`det_C`); choosing the antisymmetric/symplectic pairing (one complex mode) is an unforced extra posit.
- **F2d.** A1's *native* operator pairing is the **real** HS trace form, which presents the two doublet
  directions `C+C²` and `i(C−C²)` as two independent, equal-norm(=6), HS-orthogonal **real** Hermitian
  directions → `det_R` → `r=1`. The holomorphic pairing is an **added** ingredient.

Therefore `det_C` is the **equal-power choice** = `AC_φλ` renamed in division-algebra language; restriction
of scalars (`det_R`) is the equally-canonical (indeed default) alternative. **The holomorphy is the
convention slot, not a resolution of it.** Consistent with the verified
`flavor_doublet_metric_default_is_detr` (A1 default = `det_R` → `r=1`) and the retained-no-go residual.

### Front 3 — OVERREACH → second input: **TWO inputs, not one (and the 2nd is itself unsupplied)**
If holomorphy were forced and **universal**, every `ℝ[Z₃]` sector → `r=1/2` → `Q=2/3`, which is
**falsified by quarks**: PDG-fit `Q_down = 0.731`, `Q_up = 0.849` (runner F3a). The charged sectors form a
**monotone ladder** between the two readings — leptons `0.667` < down `0.731` < up `0.849` < rank-1
democratic `1.0` (F3b) — so "which end a sector sits at" is an **extra datum**. Avoiding overreach
therefore **requires a sector-discriminator** (the Dirac-vs-Majorana / chirality lane assignment): the
honest input count is **two** — `holomorphy + discriminator` — not one (F3c). The obvious gauge
discriminator (electric charge) **cannot** be it: it is generation-blind (`U(1)` acts as a scalar
`e^{iχ}I` on the triplet, `[U(1),C]=0`) and quarks carry it yet miss `2/3` (F3d). Moreover the candidate
second input is *itself not derived*: the retained `flavor_find_J_round3` shows the charged-lepton Dirac
reality operator's **generation action** is not closed (it factors through `SO(3)`, blind to the `SU(2)`
cover). So Q1 alone does **not** close `r=1/2`; granting holomorphy still leaves a second, independent,
currently-unsupplied import.

### Front 4 — does it beat the panel that killed the prior closure? **No — same walls, new name**
The adversarial panel killed the minimum-information closure on three walls: (i) real-vs-complex is a
convention slot; (ii) the faithfulness-target is a choice; (iii) quantum-Darwinism makes records redundant
not minimal. "Read by native division algebra" would resolve wall (i) **only if** restriction-of-scalars
were invalid — but Front 2 shows it is a standard, valid functor, so wall (i) stays **open** (runner F4a).
"Native division algebra" *is* the real-vs-complex convention slot renamed. Walls (ii)/(iii) are orthogonal
to the holomorphy framing and untouched (F4b). The framing does not beat the panel.

## Two key findings
1. **Genuine-or-restatement → RESTATEMENT.** Restriction-of-scalars (`det_R`) is an equally-canonical
   (indeed the A1-default) reading of the same complex block; the only A1-native complex structure
   preserves both measures. So `det_C` is a *choice* identical to the equal-block (`AC_φλ`) weight, and
   Q1's holomorphy is that convention slot renamed in division-algebra language — **not** a genuine
   forcing. Q1 does **not** close `r=1/2`.
2. **One-input-or-two → TWO.** Universal holomorphy overreaches (falsified by the quark ladder); avoiding
   overreach requires a sector-discriminator (Dirac-vs-Majorana/chirality), which Q1 does not supply and
   electric charge cannot be. So even granting holomorphy, the closure needs a second, independent input —
   and that input is itself not yet derived (its generation action is open).

## Where this leaves the next path
The forcing fails *as a reading-principle*, which sharpens — rather than closes — the open question. The
honest residual is unchanged from the cluster's standing: the single binary `det_C`(equal-block)/`det_R`
(dimension) is the irreducible measure choice (`koide_frobenius_isotype_split_uniqueness`, retained_no_go),
and the live lever for selecting it is a **dynamical / first-order (Berezin) Dirac structure on the
generation `b`** whose generation action is not yet built — exactly the chirality / Dirac-vs-Majorana gate
that Front 3 surfaces as the *second* input. A genuine forcing would have to (a) show restriction-of-scalars
*provably forgets structure* a physical readout must keep (defeating Front 2), **and** (b) supply the
sector-discriminator that makes the reading sector-dependent without overreach (defeating Front 3). Neither
is delivered by the division-algebra framing; both remain open targets.

## Stale-citation guard (verified vs `origin/main` ledger + note text, 2026-06-04)
- `koide_frobenius_isotype_split_uniqueness` — **retained_no_go** (the equal-block-vs-dimension residual; rep theory ranks neither).
- `koide_c3_generator_rephasing_obstruction` — **retained** (continuous `U(1)_b` quantized by C³=I; the obvious continuous J is forbidden).
- `koide_q_delta_residual_cohomology_obstruction` — **retained_no_go** (section family `s_a(t)=(t,at)`; no canonical zero-section → `r=1/2` not preferred).
- `koide_circulant_q_two_thirds` — **retained** (the Brannen functional `Q=(Σλ²)/(Σλ)²=(1+2r)/3` used here; `r=1/2` is its input, not its output).
- `three_generation_observable_theorem` — **retained** (algebra/carrier; species→flavor ID explicitly out-of-scope).
- `koide_z3_equivariant_anticommuting_no_go` — **retained_bounded**.
- `koide_real_rep_block_count_permitted_not_forced` — **unaudited** (block-count permitted, not forced; not load-bearing here, cited for consistency only).
- `inner_automorphism_invariance_tracial_identification` (PRR) — **unaudited** (not invoked; the `det_R` default here rests on the *real HS pairing*, not on PRR/full-U(3)).
- Companions reproduced (verified on `origin/main`): `flavor_doublet_metric_default_is_detr_2026-06-02`, `flavor_find_J_round1_jcs_measure_neutral_2026-06-02`, `flavor_find_J_round2_power_not_count_2026-06-02`, `flavor_find_J_round3_dirac_generation_blind_2026-06-02`, `flavor_both_readings_charge_selects_note_2026-05-30`, `flavor_carrier_not_derived_two_inputs_2026-05-31` (all **audited_conditional**/**meta**).
- Does **not** load-bear on `closure_c_staggered_dirac_gate` or `koide_phase_aps_eta_parity_route` (both unaudited).

## Provenance
- All four fronts + the ground-truth fork + consistency guards verified directly (runner 22/22).
- Hostile self-check: the runner initially mis-coded the Brannen functional (`(Σλ)²/(3Σλ²)` instead of
  `(Σλ²)/(Σλ)²`) and truncated `1/√2`; both were caught by the runner's own FAILs and corrected before this
  verdict — the conclusion rests on the corrected, phase-independent functional.
- This note **sets no audit status and assigns no grade**; grading is the independent audit lane's call.
