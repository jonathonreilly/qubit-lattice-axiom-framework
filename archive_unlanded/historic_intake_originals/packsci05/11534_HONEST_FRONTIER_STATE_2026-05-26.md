# Honest Frontier State — δ_Brannen = η_APS = 2/9

**Date:** 2026-05-26 (post-panel + hostile-review consolidation)
**Lane:** `dynamics-lane-native-axioms-only-20260526`
**Type:** frontier state synthesis (positive + hostile-review combined)
**Status:** **the converged "no-go" is wrong AND the panel reversal overstates closure** — the actual frontier is a single open bridge lemma with most upstream pieces audit-pending.

## The full picture (honest)

### What's exactly true

1. **η(1,2; 3) = 2/9** by pure cyclotomic algebra — exact, verified to machine precision (`runners/aps_eta_two_ninths_native_verifier.py` PASS=25/0). Independent route confirmed by spectral, index, and math panel agents.
2. **`(ω-1)(ω²-1) = Φ_3(1) = 3`** — standard cyclotomic identity, no admission.
3. **Lindemann-Weierstrass does NOT apply** to η — η is in ℚ (rational, defined mod ℤ), not Q·π. L-W only blocks Q-algebraic → 2π.
4. **`NEW_PARITY_IS_CIRCULANT_PHASE_NARROW_THEOREM_NOTE_2026-05-23` is retained_bounded / audited_clean** on `origin/main`. δ IS the axis-exchange parity order parameter; transposition acts δ → -δ; fixed loci δ ∈ {0, π}. δ has a canonical basepoint at δ=0.
5. **Three independent expert lenses** (spectral, index, math) converged on the APS-η = 2/9 result.
6. **At d ≠ 3 the route gives different values** (1/8 at d=2; 5/16 at d=4; etc. per KOIDE_TWO_29_ROUTES_DISTINCT). The d=3 agreement is a non-trivial uniqueness, not algebraic coincidence.

### What's claimed but conditional / open

The bridge `δ_Brannen = η_APS` requires:

| Step | Status | Open content |
|---|---|---|
| 1. Brannen circulant ← Dirac projection on hw=1 BZ-corner orbit | **conditional** | `STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17` is `audited_conditional`/bounded, NOT `retained`. The bridge inherits this tier. |
| 2. `arg(b) = δ` Plancherel identity inside parameterization | **unaudited** | `KOIDE_A1_BRANNEN_PLANCHEREL_IDENTITY_SUPPORT_NOTE_2026-04-25` is `unaudited` (positive_theorem). The algebra is exact within the cosine ansatz; the identification with the transverse Dirac spectral phase is the open Lemma L_phase. |
| 3. APS η = 2/9 cyclotomic | **retained-clean cyclotomic** + **unaudited applied form** | Cyclotomic identity is standard math; the application to `D_st` at the [111] fixed locus depends on the staggered-Dirac substep work. |
| 4. δ ↔ η unit reconciliation | **OPEN — still smuggles a convention** | Per hostile review Attack 1: η ∈ ℝ/ℤ; δ ∈ ℝ/(2π). The "period-1-rad" convention (or equivalently the bridge derivation agent's "C₃ orbit period = 2π/3" rescaling) is consistent but not yet derived from A1+A2. |
| 5. Descent normalization `N(m_*) = 1` | **OPEN — equation F of composition note** | The single irreducible residual the composition note already named. |

### What the hostile review broke

The panel reversal report had three over-claims:

- **Wall 1 (L-W) is irrelevant to APS-η route** — TRUE, but doesn't mean the bridge is closed. The original radian-bridge no-go (`KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24`, `retained_no_go`) was about *unit identification*, not solely about L-W. η being rational mod ℤ dodges L-W but does **not** automatically dodge the unit-bridge.
- **NEW_PARITY supplies the basepoint** — TRUE, but the basepoint is δ=0, not the period. The basepoint fixes one degree of freedom; the period/scale remains open.
- **"Most upstream pieces already retained"** — MISLEADING. Only 1 of 7 upstream pieces in the composition note is retained (the dimensionless 2/3 identity). 5 are unaudited, 1 is audited_conditional, 1 is retained_no_go. The bridge AT BEST achieves audited_conditional.

### What the Fisher-Rao independent-route check broke

The hostile-review math check found the Fisher-Rao proposal **does not corroborate independently**:

- V(N) = (N-1)/N² is the diagonal of the *inverse* Fisher metric (variance), NOT the diagonal of the metric itself (which is 2N).
- Arc-length along the C₃ orbit at Brannen amplitude gives 0.4724, not 2/9.
- The only regime where Fisher arc-length equals δ is the trivial ε→0 reparameterization (you put δ in by hand).

The Fisher-Rao route as proposed is a category error (variance ≠ arc-length). It is NOT a second independent route. **The APS-η cyclotomic route remains the single closed-form route.**

## The actual frontier (precise)

> **Bridge Lemma (open):** On the C₃[111] transverse 2-plane to the body-diagonal axis on Cl(3)/Z³, the C₃-Fourier mode phase `arg(b)` of the staggered-Dirac restriction to the hw=1 BZ-corner orbit equals the APS equivariant η-defect of `D_st` at the same fixed locus, computed in the natural C₃-orbit period (2π/3).

**This is one theorem, derivable in principle from:**

1. `D_st` retained construction
2. BZ-corner hw=1 orbit (`audited_conditional` substep-3)
3. Brannen-Plancherel `arg(b) = δ` (unaudited)
4. APS equivariant fixed-point formula (standard)
5. Cyclotomic identity `(ω-1)(ω²-1) = 3` (standard math)

**Cleanest attack** (per bridge-derivation agent + composition note §6):

Apply the APS index theorem on the body-diagonal Z₃ fixed locus. Identify `arg(b)` with the Berry holonomy of the staggered-Dirac restricted to the hw=1 orbit, integrand-by-integrand with the Callan-Harvey descent current. The integer-shift correction vanishes at the [111] fixed locus because transverse weights (1,2) are coprime to 3 (no-zero-mode condition). This is a single descent-normalization theorem, not a chain of new theorems.

## What "frontier science" looks like here

This is exactly the open-frontier configuration:

- The diagnostic ("the lane has converged on a no-go") is wrong.
- The reframe ("the APS-η route closes it") is overstated.
- The honest state is: **one bridge lemma is the open piece**, with a concrete attack route, falsifiable at d≠3, and most upstream pieces audit-pending (resolvable by normal audit work).

The right posture is NOT "no-go we cannot close this" and NOT "closed via APS we're done". The right posture is: **the open frontier is precisely the descent-normalization lemma + the unit reconciliation convention question**, and the substrate to attack it is in place.

## Concrete next steps (in order of tractability)

1. **Lift `STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT` from audited_conditional to retained.** This is normal audit-promotion work; once done, the bridge's Step 1 is retained-clean.

2. **Audit-promote `KOIDE_A1_BRANNEN_PLANCHEREL_IDENTITY_SUPPORT_NOTE_2026-04-25`** from unaudited to at least audited_conditional. The algebra is exact within the cosine ansatz; the audit just needs to verify the parameterization is consistent.

3. **Derive the unit-reconciliation convention as forced.** The bridge-derivation agent's argument that the C₃ orbit period (2π/3) is the natural angle scale needs to be elevated from "compatible" to "forced by retained C₃ structure". This is the genuinely open conceptual piece.

4. **Attempt the descent-normalization lemma directly.** APS index theorem at the body-diagonal Z₃ fixed locus, with transverse weights (1,2) coprime to 3. This is the bridge lemma proper.

5. **Independent verification at d=2, 4, 5, 6:** verify the cubic `d³-d-24` uniqueness at d=3 numerically AND show the framework's d=3 selection (color rank = generation count) is itself derivable from A1+A2 + retained gauge structure.

## What the lane delivers right now

The lane's research branch now has:

- 14 commits of substantive native research
- The wrong "no-go" overridden, with explicit diagnosis of where it went wrong
- The APS-η = 2/9 route independently verified (runner PASS=25/0)
- The honest open frontier precisely stated
- Hostile-review-validated assessment of what's truly open

This is genuine forward progress on the actual frontier. The δ=2/9 derivation is not closed, but the open piece is now **a single theorem with a concrete attack route**, not a "bounded no-go with structural gap".

## Memory institutionalized

- `feedback_panel_exercise_on_blocked.md`: convene the 10-physicist panel + 4 meta-exercises whenever claiming convergence on a "no-go"
- This document: the panel reversal needs hostile review to avoid over-claiming

## Cited retained sources (load-bearing)

- A1, A2 (`MINIMAL_AXIOMS_2026-05-03.md`)
- `KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10` (retained positive_theorem — the one fully retained piece)
- `NEW_PARITY_IS_CIRCULANT_PHASE_NARROW_THEOREM_NOTE_2026-05-23` (retained_bounded)
- `KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24` (retained_no_go — still live; APS route narrows but doesn't yet discharge)
- Cyclotomic algebra; Lindemann-Weierstrass; APS index theorem (standard math)

## Cited audit-pending sources (need audit work to land cleanly)

- `koide_phase_aps_eta_parity_route_narrow_theorem_note_2026-05-23` (unaudited bounded_theorem)
- `koide_aps_block_by_block_forcing_note_2026-04-21` (unaudited positive_theorem)
- `koide_two_29_routes_distinct_narrow_theorem_note_2026-05-23` (unaudited bounded_theorem)
- `koide_oplocality_brannen_plancherel_callan_harvey_honest_residual_composition_note_2026-05-25` (unaudited open_gate)
- `koide_a1_brannen_plancherel_identity_support_note_2026-04-25` (unaudited positive_theorem)
- `koide_brannen_callan_harvey_candidate_note_2026-04-22` (unaudited)
- `koide_berry_phase_theorem_note_2026-04-19` (unaudited positive_theorem)
- `staggered_dirac_substep3_bz_corner_hamming_orbit_narrow_theorem_note_2026-05-17` (audited_conditional/bounded_theorem)
