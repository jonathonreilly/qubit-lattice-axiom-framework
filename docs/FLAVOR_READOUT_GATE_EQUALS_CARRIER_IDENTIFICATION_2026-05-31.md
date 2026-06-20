# Flavor — readout/carrier/basepoint gate-collapse map, with J_cs silent on r

**Date:** 2026-05-31
**Claim type:** open_gate
**Claim boundary:** open gate-collapse/support map plus one verified finite-algebra negative. Not a retained derivation of the physical flavor observable; not a forced intensive-readout theorem; not an import.
**Primary runner:** [`scripts/flavor_readout_gate_equals_carrier_identification_2026_05_31.py`](../scripts/flavor_readout_gate_equals_carrier_identification_2026_05_31.py) (SCORECARD 11/11).
**Cached output:** [`logs/runner-cache/flavor_readout_gate_equals_carrier_identification_2026_05_31.txt`](../logs/runner-cache/flavor_readout_gate_equals_carrier_identification_2026_05_31.txt).
**Source:** workflow `wf_400cd07a-108` — 6 attack routes + 3-lens adversarial verification + synthesis (10 agents).

## Source boundary (2026-06-12)

**Boundary:** finite `C3` algebra support plus identification-boundary map.
Effective status is audit-derived; this source records only the claim boundary.

The runner verifies the displayed finite algebra and the negative that `J_cs`
does not select `r`, but the claim that the readout gate, carrier
identification, and zero-section pick are the same gate is a named
identification over existing choices, not an independent derivation from the
restricted packet.

This note may be cited to collapse duplicate bookkeeping gates and to preserve
the finite algebraic negative. It may not be cited as a retained derivation of
the physical flavor observable, a forced intensive readout, or a proof that the
carrier identification has been derived from baseline axioms.

## Source repair for re-audit (2026-06-18)

The prior top-level label `bounded_theorem` overstated the row's load-bearing
move. This packet is an `open_gate`: it maps three names for the same
remaining premise and records an exact negative route (`J_cs` does not select
`r`). It does not derive the remaining premise.

The repaired audit surface is:

- **Exact finite algebra:** the `C3` fixed locus on `R^3` is a line; the
  isolated-fixed-point `2/9` density lives on the transverse doublet; `J_cs`
  commutes with the full circulant mass family and is silent on the
  singlet/doublet ratio `r`; `L_3(1,2)=2/9` and `L_3(1,1)=1/9`.
- **Open gate:** selecting the intrinsic intensive `R^3` density at the
  `z=0` zero-section instead of the extensive lattice embedding is still the
  single physical carrier/basepoint premise.
- **No retained-grade promotion:** this row does not force the physical
  charged-lepton flavor observable from baseline axioms and should not be used
  as a theorem closing `lepton_brannen_bae_delta_two_ninths`.

## Question
Does framework baseline+retained **force** the intensive local Lefschetz density `2/9` as THE physical
charged-lepton flavor observable — over the *extensive* global equivariant index, which vanishes on
the retained `Γ₅=(−1)^{x+y+z}`-paired native staggered Dirac (η=0, χ=0, Lefschetz-sum=0)? Or does it
relocate to the generation-space identification, or stand as an independent third premise?

This is the "readout gate" left by `FLAVOR_GENERATION_SPACE_BRIDGE_REDUCES_TO_OPEN_GATE_2026-05-31`.

## Verdict: the readout gate is not an independent second gate

Five of six attack routes (1, 2, 4, 5, 6) converge on the same algebraic fact, and adversarial
verification of the sole dissenter (Route 3) confirms it delivers **no identification-independent
forcing** of `2/9`. The honest result is a **gate-collapse map**, not a closure:

> The **readout gate** (intensive-vs-extensive), the **generation-carrier identification**
> (`open_gate` `lepton_brannen_bae_delta_two_ninths`), and the **zero-section/basepoint pick** of
> `retained_no_go` `koide_q_delta_residual_cohomology_obstruction` are the **same single gate**.

This localizes the one remaining premise precisely and removes the illusion that the campaign faced
several independent obstacles.

### Why the gates coincide (verified)
- On the **full generation rep R³**, `eig(C) = {1, ω, ω²}` and `det(I−C) = 0` (runner A1) — so the C₃
  fixed locus is the **[111] *line***, not an isolated point. The isolated-fixed-point Atiyah-Bott
  density `2/9` lives **strictly on the transverse doublet** (`det(1−dg|doublet) = (1−ω)(1−ω²) = 3`,
  runner A2). Therefore "`2/9` is the genuine *total* equivariant invariant (nothing to sum)" is **not**
  a property of R³ — it requires *asserting* the observable is the intrinsic-R³ / doublet-normal-bundle
  density with a single fixed locus. **That assertion is the carrier identification.**
- Symmetrically, the "summand of a *vanishing* total" worry is **downstream and conditional**: by the
  retained_bounded `koide_z3_equivariant_anticommuting_no_go`, `Γ₅` (spacetime/site-parity factor) and
  `Γ_χ=(2/3)J−I` (generation factor) live on **different tensor factors**, so the `Γ₅`-vanishing does
  **not** automatically apply to the generation index. It applies only if R³ is *embedded* into the
  lattice diagonal — and that embedding is, again, the carrier choice. Embedding (→ extensive,
  vanishing) and not-embedding (→ intensive, 2/9-as-total) are **both** the identification.
- **Axiom 2 locality is genuinely silent.** Locality on the spatial factor `⊗_x M₂(ℂ)` admits **both**
  intensive per-site densities **and** extensive quasi-local sums (total charge/energy are
  A2-compatible extensive observables). So "A2 forces an intensive density" is *unforced* (Routes 1,
  4, 5; runner D1). The selection is made entirely by **which carrier space** the observable is
  asserted to live on — i.e. by the identification, not by a type-rule.

### New verified negative — J_cs is silent on r (Route 3's load-bearing content)
The tempting route was: the Schur-forced complex structure `J_cs=(C−C²)/√3` forces the *complex*
(`det_C`, `r=1/2`, `Q=2/3`) readout over the *real* (`det_R`, `r=1`, `Q=1`) one. It does not:
- `J_cs` has eigs `{0,+i,−i}`, `J_cs·singlet = 0`, and `J_cs² = −P₋` on the doublet (runner B1) — a
  genuine complex structure on the **transverse doublet only**.
- `[J_cs, H] = 0` for the **entire** mass-operator family `H=aI+bC+b̄C²` (runner B2, max commutator
  `6×10⁻¹⁶` over 500 random samples). So `J_cs` is **provably silent on `r=|b|²/a²`** — the *sole*
  Q-setting parameter (`Q=1/3+(2/3)r`, runner B3). `J_cs` annihilates the singlet, which is exactly
  the central label that sets `r`.

So `J_cs` makes a complex structure **definable** on the doublet but selects **neither** `det_C` nor
`det_R` as the Q-readout. The within-doublet `(1,2)`-weight forcing (`L₃(1,2)=2/9` holomorphic vs
`L₃(1,1)=1/9` real, runner C1) is genuine C₃ representation theory, but it is **(i) circular as a
Q-selector** (it presupposes the Dolbeault/holomorphic complex to derive the holomorphic density) and
**(ii) orthogonal to the operative gate** (`J_cs` vanishes on the singlet/doublet ratio that controls
`r`). A confirmed negative is not forcing toward `2/9`-as-observable.

## Derivation chain (each step labeled)
1. `[forced, A1]` `eig(C)={1,ω,ω²}`, `det(I−C)=0` ⇒ [111] is a fixed **line**, not isolated.
2. `[forced, A1]` `J_cs` eigs `{0,+i,−i}`, `J_cs·singlet=0`, `J_cs²=−P₋` — complex structure on the doublet.
3. `[forced, A1]` `[J_cs,H]=0` for all `H` in the family ⇒ `J_cs` silent on `r`, hence on `Q`.
4. `[forced, rep theory]` transverse `det(1−dg)=3`; `L₃(1,2)=2/9`, `L₃(1,1)=1/9`.
5. `[forced, retained anticommuting_no_go]` `Γ₅` (spacetime) and `Γ_χ` (generation) on different factors ⇒ the `Γ₅`-vanishing does not automatically reach the generation index.
6. `[forced, A2]` locality admits **both** intensive densities and extensive quasi-local sums ⇒ A2 selects neither.
7. `[choice = the gate]` assert the observable is the intensive C₃-equivariant density on the **intrinsic R³** (single fixed locus ⇒ intensive = total), at the **`z=0` zero-section** (`r=1/2`), **not** the `Γ₅`-graded extensive lattice index. This single assertion is simultaneously the carrier identification *and* the zero-section pick the retained no-go proves exactness cannot force.

## The single remaining premise
**The physical charged-lepton flavor observable is the intensive C₃-equivariant Atiyah-Bott density on
the intrinsic generation rep R³ (single [111] fixed locus ⇒ intensive density = total invariant), read
at the `z=0` zero-section (`r=1/2`) via the transverse-doublet `det_C`/(1,2)-weight — and is *not* the
`Γ₅=(−1)^{x+y+z}`-graded extensive index of the embedding Z³ lattice (whose total vanishes).** This is
*one* premise that is simultaneously (i) the carrier identification and (ii) the basepoint pick — they
are the same gate, not two.

## What this advances
- **Collapses three apparent gates into one**, removing the false impression of multiple independent
  obstacles; the remaining premise is now stated as a single carrier-plus-basepoint assertion.
- **New verified negative:** `J_cs` (Schur-forced) is silent on `r`, so it cannot select `det_C` over
  `det_R` — closing off a route that looked promising and clarifying that the operative parameter is
  the singlet/doublet ratio, which `J_cs` annihilates.

## Dissent recorded
Route 3 returned `stands_third_premise` (conf 0.78) on the within-doublet `(1,2)`-weight; the
identification-relabel lens did not refute its *negative* content, but the circularity lens refuted its
use as a **Q-selector** (it smuggles the Dolbeault complex). The synthesis therefore folds Route 3 into
the collapse: its durable contribution is the verified negative, not a third forcing.

## Stale-citation guard (verified vs origin/main ledger, 2026-05-31)
- `lepton_brannen_bae_delta_two_ninths` — **open_gate** (the single gate; this note shows the readout question is the same gate).
- `koide_q_delta_residual_cohomology_obstruction` — **retained_no_go** (the zero-section/basepoint the gate coincides with).
- `koide_z3_equivariant_anticommuting_no_go` — **retained_bounded** (factor-separation of `Γ₅` vs `Γ_χ`).
- `axiom_first_z_n_equivariant_spectral_asymmetry_narrow`, `koide_aps_block_by_block_forcing` — **retained_bounded**.
- Does **NOT** load-bear on `closure_c_staggered_dirac_gate` or `koide_phase_aps_eta_parity_route` (both **unaudited**).
