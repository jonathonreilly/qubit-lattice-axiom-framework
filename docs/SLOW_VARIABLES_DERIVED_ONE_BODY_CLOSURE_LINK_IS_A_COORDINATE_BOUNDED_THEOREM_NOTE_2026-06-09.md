# The "Added Slow Variables" Premise Discharges in Its Chosen-Enlargement Form: the Closing Set Is Derived, and the Link Is a Coordinate

**Date:** 2026-06-09
**Type:** bounded_theorem
**Scope:** retire-mode: derives a premise the campaign listed as a needed admission.
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_slow_variables_derived_one_body_closure_2026_06_09.py`
**Cache:** `logs/runner-cache/frontier_slow_variables_derived_one_body_closure_2026_06_09.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=8 FAIL=0`, exact, full
64-dim Fock space, no MC.

## The premise being retired

The gauge-dynamics campaign's lever-space map listed **"added slow variables"**
as a promotion route **requiring a new premise**: the
[`INDUCED_COMPOSITE_LINK_TRAJECTORY_COVARIANCE_INCREMENT_LAW_NON_AUTONOMY_BOUNDED_THEOREM_NOTE_2026-06-08`](INDUCED_COMPOSITE_LINK_TRAJECTORY_COVARIANCE_INCREMENT_LAW_NON_AUTONOMY_BOUNDED_THEOREM_NOTE_2026-06-08.md)
exhibited the composite link's non-autonomy (two states, same `U_eff`, different
`U̇_eff`), and closing the dynamics appeared to need a *chosen* enlargement of
the state. **This note derives the enlargement instead — nothing is admitted.**
Precisely: the **chosen-enlargement form** of the premise discharges. The
closing set is the **full one-body density `G`** — strictly larger than the
registered candidate `(U,Q)∼M=G_xy`, which the runner shows does **not** close
on its own (its flow needs the diagonal blocks) — and the link acquires **no
autonomous law** (consistent with the
[`RECORD_DOMINATED_POINTER_SECTOR_TRANSPORT_GENERATOR_VACUOUS_LINK_BOUNDED_THEOREM_NOTE_2026-06-09`](RECORD_DOMINATED_POINTER_SECTOR_TRANSPORT_GENERATOR_VACUOUS_LINK_BOUNDED_THEOREM_NOTE_2026-06-09.md)
result).

## What is proved (exact — runner `PASS=8 FAIL=0`)

**(T1) Operator-level closure, state-independent.** For the named quadratic hopping
generator (`H = Σ h_ij a_i†a_j`), the Heisenberg flow of the one-body bilinears
**closes on itself exactly**: `e^{iHt} a_i†a_j e^{-iHt} = Σ_{kl} W*_{ik}W_{jl} a_k†a_l`
with `W = e^{-iht}` (verified on the full `2⁶`-dim Fock space, dev `10⁻¹¹`; the state-level
corollary `G(t)` law holds on a **non-Gaussian** state to `10⁻¹⁶`). The "slow variables"
are the rest of the one-body density `G` — **forced by the quadratic structure of the
retained hopping, not chosen.**

**(T2) The record channels preserve the closure.** The campaign's named instruments act on
`G` by exact linear one-body rules — re-verified here for I-A on a non-Gaussian state
(`G → (1−λ)G + λ·diag(G)`, dev `10⁻¹⁷`); I-B's exact one-body rules were Fock-anchored in
[`RECORD_INSTRUMENT_COMPOSITE_LINK_POINTER_ERASURE_EXACT_SLAVING_BOUNDED_THEOREM_NOTE_2026-06-09`](RECORD_INSTRUMENT_COMPOSITE_LINK_POINTER_ERASURE_EXACT_SLAVING_BOUNDED_THEOREM_NOTE_2026-06-09.md).
The interleaved (Hamiltonian + record) flow is therefore closed at the `G`
level.

**(T3) The link is a coordinate.** `U_eff = polar(G_xy)` is a nonlinear, lossy coordinate
of the closed object `G`. The Sylvester law `U̇_eff = U·Ω` is evaluated **on the true
`G`-flow generator** (`Ġ = i[hᵀ,G]`, itself derived from T1) and matches the finite
difference of the **actual evolution** — with a wrong-generator **control** showing the
check has discriminating power (the reviewer found and we replaced a generator-circular
draft check). And the registered candidate set `(U,Q)∼M` does **not** close: two `G`'s
with the same cross block but different diagonal blocks evolve `G_xy` differently.
The induced-trajectory note's non-autonomy is coordinate non-autonomy — the closed derived flow read
through a coordinate that discards data the flow carries.

**(T4) Teeth.** A quartic (density–density) term **breaks** the closure — `a_0†a_3(t)`
leaves the bilinear span (projection residual `0.23`). The closure is a derived property
of the *named quadratic hopping generator*, not generic.

## What this retires, and what it does not

- **Discharged (as a source proposal):** the **chosen-enlargement form** of the
  route-(i) premise — no slow-variable *choice* is needed; the closing set is **derived**
  (and is the full `G`, not the registered `(U,Q)`). The campaign's link-generator story upgrades
  from "the link-level generator is vacuous" to "**the closed derived dynamics exists at
  the `G` level; the link is a lossy coordinate of it, with no autonomous law**."
- **Not touched:** the pointer-frame admission `{P_r}` and the stratification theorem
  (the record-level *reduction* of the `G`-flow still carries the frame admission — this
  note moves none of that); the realization gate ("the physical dynamics *is* this
  quadratic `H`" is a separate lane); interacting/non-quadratic matter (T4 is the exact
  boundary). Conditional on the supplied `C³` color carrier as throughout the campaign.
- No new axiom, import, or framing; no PDG value; the audit lane sets all status.

## Cross-references

- The non-autonomy exhibit this explains:
  [`INDUCED_COMPOSITE_LINK_TRAJECTORY_COVARIANCE_INCREMENT_LAW_NON_AUTONOMY_BOUNDED_THEOREM_NOTE_2026-06-08`](INDUCED_COMPOSITE_LINK_TRAJECTORY_COVARIANCE_INCREMENT_LAW_NON_AUTONOMY_BOUNDED_THEOREM_NOTE_2026-06-08.md).
- The exact one-body record rules:
  [`RECORD_INSTRUMENT_COMPOSITE_LINK_POINTER_ERASURE_EXACT_SLAVING_BOUNDED_THEOREM_NOTE_2026-06-09`](RECORD_INSTRUMENT_COMPOSITE_LINK_POINTER_ERASURE_EXACT_SLAVING_BOUNDED_THEOREM_NOTE_2026-06-09.md).
- The vacuous-link-generator comparison:
  [`RECORD_DOMINATED_POINTER_SECTOR_TRANSPORT_GENERATOR_VACUOUS_LINK_BOUNDED_THEOREM_NOTE_2026-06-09`](RECORD_DOMINATED_POINTER_SECTOR_TRANSPORT_GENERATOR_VACUOUS_LINK_BOUNDED_THEOREM_NOTE_2026-06-09.md).
- The composite-link construction:
  [`COLOR_LINK_INDEX_ROUTING_VIA_CROSS_SITE_MATTER_BILINEAR_UNITARIZATION_BOUNDED_THEOREM_NOTE_2026-06-08`](COLOR_LINK_INDEX_ROUTING_VIA_CROSS_SITE_MATTER_BILINEAR_UNITARIZATION_BOUNDED_THEOREM_NOTE_2026-06-08.md).
- Standard math (method only): Heisenberg evolution of quadratic forms; polar decomposition; Sylvester equations.
