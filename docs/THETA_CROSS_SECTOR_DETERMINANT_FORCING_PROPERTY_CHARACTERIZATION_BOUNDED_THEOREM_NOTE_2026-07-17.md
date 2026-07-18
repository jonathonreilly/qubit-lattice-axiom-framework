---
claim_id: theta_cross_sector_determinant_forcing_property_characterization_bounded_theorem_note_2026-07-17
claim_type: bounded_theorem
claim_scope: "Bridge-conditional forcing-level characterization on the supplied determinant-channel readout surface of the theta mass side: a supplied property set GUARANTEES vanishing registered phase content for every functional satisfying it exactly when the set contains K/CPT orbit constancy together with at least one odd-side ingredient (record-additivity with its conjugate-pair trivial-sector normalization, or the independent-block determinant homomorphism). The guarantee direction re-derives the two landed routes; the necessity direction is per role and per route, witnessed exactly (the k = 1 multiplicative character keeps the homomorphism ingredient and registers, so orbit constancy is not removable; the K-even cosine probe keeps orbit constancy and registers, so the odd side is not removable; the odd phase functional sin(phi) witnesses the additive route at its consequence level). Individual functionals may be phase-silent without the properties (an exact silent witness outside both odd-side properties is gated), so no individual-functional biconditional is claimed. Consequence, stated as a reduction and not a closure: under the cross-sector identification named by the open obligation, the forcing half reduces to one transported property — K/CPT orbit constancy on the quark determinant channel — with the odd side sector-local. No physical readout, exhaustion, carrier, or orientation is derived; the gauge-side theta and the invariant theta-bar combination are untouched; the obligation is not closed."
upstream_dependencies:
  - minimal_axioms
  - theta_p2_k_cpt_determinant_character_phase_erasure_bounded_note_2026-06-10
  - registrable_readout_additive_even_phase_free_narrow_theorem_note_2026-06-10
  - strong_cp_determinant_readout_bridge_narrow_theorem_note_2026-06-12
runner: scripts/theta_cross_sector_determinant_forcing_property_characterization_2026_07_17.py
---

# Theta Cross-Sector Determinant Readout: Exact Characterization Of The Forcing Properties

**Date:** 2026-07-17
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** bridge-conditional; every channel property below is a property of
a supplied readout class, assumed, not adopted; no physical identification
is made.
**Audit-status authority:** independent audit lane only. This note sets no
audit verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or
enlarged here.
**Primary runner:**
[`scripts/theta_cross_sector_determinant_forcing_property_characterization_2026_07_17.py`](../scripts/theta_cross_sector_determinant_forcing_property_characterization_2026_07_17.py)
**Runner cache:**
[`logs/runner-cache/theta_cross_sector_determinant_forcing_property_characterization_2026_07_17.txt`](../logs/runner-cache/theta_cross_sector_determinant_forcing_property_characterization_2026_07_17.txt)

## Purpose

The open derivation obligation
[`THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md`](THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md)
asks: "Derive from the retained framework chain whether the charged-lepton
`K`/CPT occupancy carrier is the same physical channel that controls the
quark-sector determinant readout, and whether that identification forces
`arg det(M_q) = 0`."

The cited mass-side source notes (audit status owned by the audit lane) erase the determinant phase by two routes,
each inside a supplied class:
[`THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md`](THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md)
(multiplicative character class: K/CPT invariance forces `k = 0`, with the
hostile guard "K/CPT orbit invariance alone gives evenness, not phase
erasure"),
[`REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md)
(its Consequence A: additivity forces the per-sector phase functional odd,
orbit constancy forces it even, odd-and-even forces zero — summarized in
its own verification line "homomorphism forces odd; even forces zero"), and
[`STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md`](STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md)
(the dedicated mass-determinant-channel bridge). What no landed note states
is the exact division of labor: which of the named channel properties carry
the forcing, which are individually necessary, and therefore what exactly
the cross-sector identification must transport for the obligation's forcing
half to go through. This note proves that characterization and nothing
else. It does not construct a carrier, derive a physical readout, or close
the obligation; the axiom-update route remains closed exactly as in
[`THETA_MASS_DETERMINANT_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md`](THETA_MASS_DETERMINANT_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md).

## The Supplied Surface

Per sector block, the supplied determinant channel carries a nonzero
complex value `z` (the block determinant) and a scalar readout functional
`r(z)`. Writing `z = |z| e^{i·arg z}`, the registered phase content of `r`
is its dependence on `arg z` at fixed `|z|`, captured by a per-sector phase
functional `h(arg z)`. Three channel properties are in play, each stated by the cited source notes as
part of a supplied class and none derived from the axioms:

- **(P-add)** finite additivity of the scalar readout over pairwise-disjoint
  records together with the conjugate-pair trivial-sector normalization
  (the pair at `(φ, −φ)` composes to the trivial sector, whose phase
  content is zero — both parts of the landed Record-registrability shape;
  additivity alone does not give oddness, and the runner flags this
  explicitly) — consequence: `h` is odd.
- **(P-hom)** the independent-block determinant homomorphism
  `det(M_1 ⊕ M_2) = det(M_1) det(M_2)` with the readout respecting block
  composition — its named consequence: `h` is additive in the angle, hence
  odd.
- **(P-orb)** K/CPT orbit constancy: `z ↦ conj(z)` leaves the readout
  unchanged — its named consequence: `h` is even.

## Results

**T1 (forcing-level characterization).** Within the supplied surface, a
property set drawn from {(P-add), (P-hom), (P-orb)} **guarantees**
`h ≡ 0` for every readout satisfying it **iff** the set contains (P-orb)
together with at least one odd-side member. No individual-functional
biconditional is claimed: a functional can be phase-silent while
satisfying neither odd-side property (exact witness: `r(z) = 1 + |z|`,
orbit-constant, silent, and neither additive nor multiplicative under
block composition — gated), so vanishing does not imply the properties;
the characterization is about which supplied property sets carry the
guarantee.

- *Forward (the guarantee).* Angles compose modulo `2π` (the phase
  domain is the circle, with the runner gating a wrapping witness and the
  branch-point convention), and the per-sector phase functional is taken
  at fixed `|z|`, the landed resolution, with block composition handled
  per block. Either odd-side ingredient makes `h` odd — (P-add) via the
  conjugate-pair normalization it carries, (P-hom) via exponent
  additivity; (P-orb) makes `h` even; `h(φ) = −h(−φ) = −h(φ)` forces
  `h ≡ 0`. This is the landed mechanism, re-derived formally in the
  runner.
- *(P-orb) is not removable.* The witness `r(z) = e^{i · arg z}` (the
  `k = 1` character; every nonzero `k` is distinguished at a suitable
  phase) satisfies the homomorphism ingredient with odd phase functional
  `arg z`, is not orbit-constant, and registers the phase (values `1`
  versus `i` at `arg z = 0` and `π/2`, exactly). For the additive route
  the same removal is witnessed at the consequence level: the odd
  functional `h(φ) = sin(φ)` satisfies oddness — all (P-add) contributes
  to the mechanism — and registers. So neither route's guarantee survives
  dropping orbit constancy.
- *The odd side is necessary.* The witness `r(z) = cos(arg z)` is
  orbit-constant (even), satisfies neither odd-side property (it is not
  odd: `cos(−φ) = cos(φ)`; not block-homomorphic:
  `cos(π) = −1 ≠ 0 = cos(π/2)·cos(π/2)`, exactly), and registers the phase
  (`cos 0 = 1 ≠ −1 = cos π`). This is the landed hostile guard, now
  placed as the exact witness that the guarantee does not survive
  dropping the odd side: orbit constancy alone admits a registering
  functional.
- *Each odd-side ingredient suffices alone.* Given (P-orb), either
  (P-add) or (P-hom) individually completes the guarantee (both routes
  are landed; the runner re-derives each oddness consequence separately).
  They are two separate sufficient routes; no independence claim beyond
  that is made.

**T2 (cross-sector reduction — a reduction, not a closure).** Conditional
on an independently supplied quark-side odd-side ingredient — (P-add) as
the Record-registrable shape of the quark channel's scalar readout, or
(P-hom) as the block law its interface states, neither derived here — the
remaining cross-sector content of the obligation's *forcing* half is the
transport of one property: **K/CPT orbit constancy on the quark
determinant channel**. Transport is an assumption named here, not a
consequence of carrier identity (the cited phase-erasure note itself
states that membership of the physical readout in the Record-registrable
class is a standing modeling premise); with it and the quark-side
odd-side ingredient, T1's guarantee yields vanishing registered
`arg det(M_q)` content — "one transported property" in exactly that
conditional sense. What T1 does not and cannot supply is the identification itself: the
quark determinant carrier construction, the physical readout map, and the
physical-exhaustion statement (the no-go note's remaining live route 1)
stay open, exactly per the obligation's closure criterion that "[A]lgebraic similarity, shared notation, and historical decision
text are insufficient."

**T3 (theta-bar honesty guard).** Everything above concerns the mass-side
registered content only. The gauge-side slot and the invariant combination
`theta_bar = theta_gauge + arg det(M_u M_d)` (the no-go note's live route
3) are untouched: no gauge-side statement is made, and T1's conclusion is
about the registered content of a supplied channel, not about the
action-level bare slot (strong-CP premise 1, tracked separately).

## No-Go Discipline Gate

T1's necessity halves are bounded negatives ("without (P-orb) nothing
forces"; "without the odd side nothing forces"), answered:

- **N1 route inventory (per negative).** Against "(P-orb) is not
  removable": (1) multiplicative-characters-only class — the character
  witness lives exactly there; ATTEMPTED; (2) continuity/smoothness — the
  `k = 1` character is smooth; RULED OUT as a rescue; (3) real-valuedness
  — at the consequence level the odd registering functional `sin(φ)` is
  real; ATTEMPTED; (4) `|z| = 1` restriction — the witness lives there;
  (5) higher-arity block laws — two blocks already suffice for the
  oddness consequence; named untested beyond. Against "the odd side is
  not removable": (1) the cosine witness is smooth, real, and lives at
  `|z| = 1`, so those three rescues fail together; ATTEMPTED; (2)
  strengthening evenness to full unitary invariance of the value — the
  cosine depends only on `arg z` and is conjugation-even, so orbit-side
  strengthening inside the stated surface does not remove it; named to
  its stated resolution; (3) adding either odd-side ingredient — that is
  the forward cell, not a rescue of the negative.
- **N2 wall independence:** the two necessity statements concern disjoint
  property sides and are witnessed by different functionals; neither
  implies the other.
- **N3 hidden-wall scan:** all properties are stated as supplied-class
  properties; the phase functional's definition (dependence at fixed
  `|z|`, angles modulo `2π`, branch convention gated) is the same
  resolution the cited notes use, with the wrap and radius walls now
  stated explicitly in the forward bullet.
- **N4 residual matching:** the cited prior negatives are the landed
  hostile guard (reused as the exact odd-side witness) and the axiom-update
  no-go (respected; no axiom reading is used).
- **N5 rhetoric audit:** each necessity is stated as a guarantee-removal
  statement witnessed by an exact registering functional; no
  individual-functional biconditional and no blanket "forces nothing"
  claim survives in the results.
- **N6 partial-closure scan:** closure paths named — transport of (P-orb)
  plus an independently supplied quark-side odd-side ingredient (T2); the
  no-go note's live routes 1 (mass determinant-channel theorem), 2
  (scalar-mass action-surface theorem), and 3 (joint gauge/mass theorem)
  remain the closure surface for the physical half.
- **N7 steelman:** "the characterization is just the cited lemmas
  relabeled." Reply: the cited notes prove two forward erasures inside
  supplied classes; the forcing-level necessity structure — which
  property sets carry the guarantee, witnessed per role and per route —
  is not stated by any of the four cited source notes (the verifiable
  comparison set), and it is what the obligation's forcing half needs
  named.
- **N8 cross-cycle echo:** the mechanism echoes the lane pattern of
  boundary-by-witness (parent Born-lane blocks); the same discipline of
  per-horn exact witnesses is applied here to the theta surface.

## Non-Claims

- Does **not** derive the physical quark determinant readout, its carrier,
  or the physical-exhaustion bridge; does **not** close or weaken the
  obligation, which remains open exactly as stated.
- Does **not** identify the charged-lepton carrier with the quark channel;
  T2 is conditional on that identification and reduces only its forcing
  half.
- Does **not** touch the gauge-side theta, the theta-bar combination, the
  action-level bare slot, or the positive-orientation surface.
- Does **not** read the axioms as supplying any channel property (the
  axiom-update no-go is respected), and does **not** set an audit verdict;
  independent audit remains required.

## Verification

The primary runner checks the conditional odd/even eliminations, the
selected witness points, the determinant identity, and the source needles
— and nothing more (sympy, exact arithmetic, single process): the
odd-and-even elimination to zero; the oddness consequences of (P-add)
(with its conjugate-pair normalization, flagged in the runner's own
output) and (P-hom) separately, as formal eliminations; the
block-determinant homomorphism on symbolic blocks; the `k = 1` character
witness (odd phase functional, multiplicative composition at exact
witnesses, orbit-constancy failure, exact registration); the `sin(φ)`
consequence-level witness; the cosine witness (evenness, both odd-side
failures at exact angles, exact registration); the silent-without-
properties witness `1 + |z|`; the wrapping and branch-convention gates for
the mod-`2π` phase domain; the conjugation action; and needle checks
pinning the obligation's exact-target sentence, the hostile-guard
sentence, the "homomorphism forces odd; even forces zero" line, and this
note's claim identifier and property labels. The cross-sector transport,
the quark-side premises, and the no-go live routes are conditions and
context, not runner-checked content. Mutation checks (one load-bearing
mutation per check family, reverted) are recorded in the review history
and PR body.

Measured runner total after final verification:
`TOTAL: PASS=30 FAIL=0`.
