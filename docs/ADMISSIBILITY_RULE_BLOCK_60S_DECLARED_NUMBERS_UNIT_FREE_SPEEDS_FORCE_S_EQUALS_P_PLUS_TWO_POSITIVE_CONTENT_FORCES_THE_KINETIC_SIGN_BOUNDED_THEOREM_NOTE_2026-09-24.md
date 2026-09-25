---
claim_id: admissibility_rule_block_60s_declared_numbers_unit_free_speeds_force_s_equals_p_plus_two_positive_content_forces_the_kinetic_sign_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Conditional scaling algebra for the supplied field and kinetic ansatz, not a units-based selection
  theorem. Global time reparameterization scales all site and bond rates; a separate uniform active change w->Cw
  at fixed bond rates gives ell->Cell. With K/alpha held fixed the stated homogeneous mode frequency is invariant
  iff s=p+2; if K/alpha scales as C^kappa the condition instead is s=p+2+kappa. Positive rest-content stationarity
  in the explicitly supplied homogeneous action forces a negative kinetic coefficient on a nonstatic branch. Exact
  smooth conformal curvature densities in dimensions2,3,4 have power d-2; selecting that nonzero curvature sector,
  excluding a volume term, and extending background powers are extra model assumptions. No axiom selection of exponents,
  units of K, common light cone or general lattice evolution.
upstream_dependencies:
- admissibility_rule_a_ledger_linear_in_the_rates_every_clock_a_multiplier_the_ledger_a_wall_term_and_the_curvature_member_doubles_the_bending_bounded_theorem_note_2026-09-21
- admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21
- admissibility_rule_bond_rates_and_lengths_a_body_at_rest_sources_no_length_and_the_bending_of_rays_carries_one_more_free_number_bounded_theorem_note_2026-09-21
- admissibility_rule_bond_strains_and_plaquette_curls_a_field_energy_per_local_tick_that_does_not_see_the_coins_axes_is_the_curvature_member_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_block_60s_declared_numbers_unit_free_speeds_force_s_equals_p_plus_two_positive_content_forces_the_kinetic_sign_2026_09_24.py
---

# Supplied scaling comparisons, the homogeneous kinetic sign and conformal curvature powers

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 59, 60, 62 and 64 as landed; harvest block from a Grok-refereed probes attempt; nothing adopted or registered; unaudited)

This note works within blocks 59, 60, 62 and 64 as landed on main (lengths and rates, the member linear in the rates and its kinetic term, the frame's modes, and blindness to the coin's axes); it reports which of block 60's declared numbers are fixed by stated demands and which stay supplied; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

A uniform active parameter change at fixed bond hopping rates changes the supplied field frequency by C^(2+p-s), provided K/alpha is held fixed. Requiring that particular invariance gives s=p+2. It is not a consequence of changing units: if K/alpha instead scales as C^kappa, the condition is s=p+2+kappa. The original proposal to rescale K while holding it fixed in the speed comparison cannot be used as one argument.

Separately, the explicit homogeneous rest-content action has no positive-m stationary rate solution with a nonnegative kinetic coefficient. Its nonstatic negative-coefficient solutions and their time domain are stated below. The smooth conformal-curvature density has power d-2; selecting its nonzero three-dimensional curvature sector gives p=1. A permitted volume term, different ansatz or different scaling demand prevents treating p=1 and s=3 as generally forced.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-24.
  - "No site is privileged." This sentence supplies no global length-rescaling symmetry or coefficient transformation law.
  - "Admissibility is not a dynamics axiom." The member, its powers and the kinetic term are supplied clauses.
  - "A choice not fixed by the supplied structure remains a named conditional or open dependency." That is where `K` and `α/K` stay.
- **Lengths and rates** (block 59 as landed). A bond's length is `ℓ_b = √(w_xw_y)/c_b`, a pure number. Content has hop energy, on the bonds, and rest energy, at the sites.
- **The member and the kinetic term** (block 60 as landed): `F = Σ_xw_xKℓ_x^p(aΔλ + bq)` with `ℓ = e^λ`, and `Σc_kℓ^sλ̇²/w`. Block 60 T5(b): stationarity in `w` of `c_kℓ^sλ̇²/w − mw` is `mw² + c_kℓ^sλ̇² = 0`.
- **Modes.** Separately extend the flat-background quadratic mode by the ansatz (alpha ellbar^s/wbar) omega^2=K wbar ellbar^p P^2. This is not derived for varying backgrounds from block62. In block62's tensor normalization the transverse trace-free equation has4alpha instead of alpha; absorbing that fixed numerical factor into the mode coefficient does not alter any scaling exponent. Take nonzero K/alpha, ellbar,wbar>0 and P!=0; a positive speed squared additionally needs K/alpha>0.
- **Blindness** (block 64 as landed). Within its six-coefficient continuum ansatz, infinitesimal local coin-rotation invariance fixes the density to a volume term plus the curvature combination. With `c₄ = −2K` that is block 60's member.
- **Comparators, named only:** the scalar curvature built from the Christoffel symbols of a conformally flat metric; the volume power `3` and `c_k = −6K` of the comparator's slicing (Arnowitt–Deser–Misner); the Friedmann-type expansion `t^{2/3}`.

## Theorem T1 — no single weight for the ledger

*Statement.*
- (a) Replacing every site rate w and every bond rate c_b by L times itself and `d/dt` by `L d/dt` multiplies `F` and the kinetic term by `L`, for every `p` and `s`.
- (b) Choose the uniform active transformation w->Cw at fixed positive c_b, C>0. It gives ell_b->C ell_b. The converse is not unique on a bipartite lattice: w_x->C exp(t epsilon_x) w_x gives the same bond lengths. Uniform scaling is a chosen branch. It then multiplies:
  - `F` by `C^{1+p}`;
  - the kinetic term by `C^{s−1}`;
  - the hop energy by `1`;
  - the rest energy by `C`.
- (c) A common weight with the hop energy would need `p = −1`, and one with the rest energy `p = 0`. Neither is block 60's `p = 1`. Thus at fixed coefficients there is no common homogeneous factor when both hop and rest terms are present. Rescaling K alone cannot also correct their unequal weights. No dimension assignment or pure-unit interpretation of K follows; a full change-of-units convention would have to specify every coefficient and observable.

*Proof.*
- (a) `F` is linear in the rates and the lengths have weight zero. The kinetic term gets `L²/L`.
- (b) `ℓ_b = √(w_xw_y)/c_b`. `Δλ` and `q` are unchanged, `ℓ^p → C^pℓ^p` and `w → Cw`.
- (c) Solve.

∎

*Checked (B1).* On a ring of four with symbolic `λ_x`, `w_x` and `c_b`, symbolically in `p` and `s`.

## Theorem T2 — frequency invariance under the chosen active scaling

*Statement.* The supplied mode ansatz gives omega^2=(K/alpha) wbar^2 ellbar^(p-s) P^2. At fixed K/alpha and fixed bond rates, uniform w->Cw and ell->Cell multiply this frequency squared by C^(2+p-s). Thus invariance for every C>0 holds iff s=p+2. This compares frequencies at the same lattice wave vector; it is not an exact common-cone theorem. If K/alpha transforms as C^kappa, the exponent instead is2+p-s+kappa.

*Proof.* Substitute the stipulated scalings. The equality of a power of every positive C to1 forces its exponent to vanish. In particular, p=1 gives s=3 only in the fixed-ratio comparison. The same model with p=1,s=2 and kappa=-1 is an explicit alternative invariant scaling.

*Checked (C1).* The fixed-ratio power and condition. The coefficient-transformation counterexample follows from the displayed exponent, not a unit-conversion axiom.

## Theorem T3 — positive content forces the kinetic sign

*Statement.*
- (a) For the supplied homogeneous action c_k ell^s lambdadot^2/w-mw, with m>0,w>0,ell>0 and lambdadot!=0, stationarity in w at fixed ell and lambdadot gives `c_k = −mw²/(ℓ^sλ̇²)`, which is negative when `m > 0`. With w fixed by the time choice, m constant and s!=0, the length equation is2 lambda-double-dot+s lambda-dot squared=0. The branch ell=(1+t/t0)^(2/s) solves it on1+t/t0>0, t0!=0, but satisfies the rate constraint only if c_k=-m w^2 s^2 t0^2/4. A static branch with m>0 cannot satisfy this constraint. At s=0 the length equation instead permits ell=ell0 exp(vt), with c_k v^2=-m w^2.
- (b) With the isotropic stretch's `c_k = 12α + 36β` (block 124 T2, an open PR), this needs `β < −α/3` for `α > 0`. It is met at `β = −α`, where `c_k = −24α`, and at the comparator's `(K/4, −K/4)`, where `c_k = −6K`.

*Proof.* (a) Block 60 T5(b), solved for `c_k`; then differentiate. (b) Linear in `β`. ∎

*Checked (D1).* The solve, the uniform motion and the three values.

## Theorem T4 — the curvature member's power is d − 2

*Statement.* For `g = ℓ²δ` with `ℓ = e^λ` in `d` dimensions, `√g R = ℓ^{d−2}(−2(d − 1)Δλ − (d − 2)(d − 1)|∇λ|²)`, exactly in `d = 2, 3, 4`. So the curvature member has `p = d − 2`, which is `p = 1` in three dimensions.

This is a smooth continuum identity, not an exact discrete curvature law. Block64 restricts a six-coefficient continuum ansatz at its stated truncation orders and allows a volume term as well as the curvature combination. Selecting a nonzero curvature member and excluding the volume term gives p=1; only with the additional fixed-ratio scaling demand does T2 then give s=3.

*Proof.* Direct computation of the connection coefficients and the scalar curvature of a conformally flat metric. ∎

*Checked (E1).* The scalar curvature in `d = 2, 3, 4`, symbolically, with `λ` a general function.

## What stays supplied

The field and kinetic ansatz, coefficient transformation laws, active scaling demand, curvature-sector selection, and any physical speed identification remain supplied. K and alpha/K are coefficients, not derived unit conventions. The isotropic coefficient12alpha+36beta follows by direct substitution h=2lambda delta; it does not require importing an open PR's broader symmetry claims. With alpha>0 its negativity is exactly beta<-alpha/3. No registered primitive is used to select these values.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 60 as landed: linearity in the rates, p, K, s and the sign of c_k declared, not forced"
source_of_blocker_text: block 60 as landed
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "a clause sharing one light cone between walker and field (fixes alpha/K); block 64's blindness beyond its ansatz"
conditional_surface_status: "T1-T4 exact; p = 1 conditional on block 64's ansatz; s = 3 conditional on the fixed-coefficient active-scaling demand; the kinetic ratio conditional on open block 124"
hypothetical_axiom_status: "the member, its kinetic term and the demands are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 59: lengths as pure numbers.
  - Block 60: the member, T3's `β = 1/p`, T5's kinetic term and its closed-lattice sum rule. Its comparator values were `s = 3` and `c_k = −6K`.
  - Block 62: the modes.
  - Block 64: blindness gives the curvature member within its ansatz.
- **Opened, not landed.** Block 124 (PR #9178): the kinetic family and `c_k = 12α + 36β`.
- **The probes attempt.** `what-fixes-the-powers-and-the-kinetic-sign` a1 (Claude Opus 5.5, issue #8830) found T1–T4 as a table of principles. A Grok referee confirmed it (#8909).
  - The attempt said that no principle forces `p`. Block 64, as landed, does so within its ansatz, and this note places that.
- **In the literature.**
  - The scalar curvature of a conformally flat metric.
  - The comparator's volume power and its expansion `t^{2/3}`.

  All reference only.
- **New here:**
  - an independent exact runner;
  - the ledger of what stays supplied, with block 64 and block 124 placed;
  - the third-column reading: `K` and `α/K` are not from records alone.

## Exact target and obligation graph

Target: which of block 60's declared numbers are fixed by stated demands. The obligations are:
- (O1) weights (T1);
- (O2) the speed demand (T2);
- (O3) the sign (T3);
- (O4) the curvature's power (T4).

T1–T4 discharge them. Open: a clause for one light cone.

## No-Go Discipline Gate

The note's negative sentences:
- no single weight covers the ledger under a rescaling of the lengths;
- nothing in the stated demands fixes `K` or `α/K`.

### N1 — Routes by which the sentence could fail or mislead
1. *Another rescaling.* Holding different rates changes the weights. The one here holds the crossing rates, which fixes the walker's hop frequencies.
2. *The speed demand.* `s = p + 2` is conditional on asking for unit-free speed ratios. Without that demand `s` stays free.
3. *Block 64's ansatz.* `p = 1` is conditional on it. Outside the six-coefficient continuum ansatz, `p` is not fixed here.
4. *One light cone.* A clause sharing a light cone between walker and field would fix `α = K/4`. No such clause is landed.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied member, kinetic term and demands.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no site privileged; no dynamics in the axioms; named conditionals | yes |
| blocks 59, 60, 62, 64 (landed) | lengths; member, kinetic term and sum rule; modes; blindness | yes (restated) |
| block 124 (open, #9178) | `c_k = 12α + 36β`; the kinetic ratio | no (placement) |
| probes (#8830; Grok-refereed #8909) | T1–T4 first derived | yes (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "no common weight; `s = p + 2` for fixed-coefficient active-scaling invariance; `c_k < 0` for positive content; `p = d − 2`" | executed: the member on a ring under both scalings | executed: bond lengths; hop and rest weights | executed: the mode power and `s = p + 2` | executed: the sign, the motion, the curvature in `d = 2, 3, 4` | exact as stated; `p = 1` and `s = 3` conditional as listed |

### N6 — Partial-closure paths and primitive scan
`kinetic_isotropy_primitive` grants `c_t = c_s` of a kinetic form of the repository. Whether it would fix `α/K` is not decided here, and it is not used. `scale_reference_primitive` grants a scale reference as a units conversion only; it does not select or identify K in this model and is not used. Nothing is proposed for registration.

### N7 — Strongest countercontrol
An allowed coefficient scaling K/alpha->C^kappa K/alpha changes the exponent condition. A bipartite alternating site-rate factor changes no bond length. These demonstrate why the uniform fixed-coefficient comparison is an added hypothesis.

### N8 — Earlier statements
The broad units-based derivation is withdrawn. The exact scaling algebra, conditional rest-content constraint and continuum curvature identity remain; no exponent or physical coefficient is derived from the axioms.

## Falsifiers

- A rescaling under which the member and the rest energy share one weight at `p = 1`.
- A mode equation whose frequency ratio is invariant under the specified fixed-coefficient scaling with `s ≠ p + 2`.
- A closed lattice with positive content at rest and `c_k > 0` that is stationary in the rates.

## Boundaries and non-claims

- The member, the kinetic term and the demands are supplied.
- `p = 1` rests on block 64's ansatz, and `s = 3` on the speed demand.
- `K` and `α/K` are not derived.
- No gravitational claim is made.

## Imports

- [Supplied source, block 59](ADMISSIBILITY_RULE_BOND_RATES_AND_LENGTHS_A_BODY_AT_REST_SOURCES_NO_LENGTH_AND_THE_BENDING_OF_RAYS_CARRIES_ONE_MORE_FREE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 60](ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 62](ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 64](ADMISSIBILITY_RULE_BOND_STRAINS_AND_PLAQUETTE_CURLS_A_FIELD_ENERGY_PER_LOCAL_TICK_THAT_DOES_NOT_SEE_THE_COINS_AXES_IS_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.

- `minimal_axioms`. Blocks 59, 60, 62 and 64, restated. Block 124, placed.
- The probes attempt, refereed by another model family.
- Named standard imports, at definition level:
  - the Christoffel symbols and the Ricci scalar of a metric;
  - symbolic differentiation and solving.

## Review record

- **Who and when.** Supervisor-run block, the seventy-seventh since the source-link direction opened; 2026-09-24.
- **Provenance.**
  - The probes attempt by Claude Opus 5.5 derived the results (#8830). A Grok referee confirmed them (#8909).
  - The supervisor re-checked them with its own runner.
  - The supervisor added block 64's placement, which the attempt had missed.
- **Before writing.**
  - Main was re-fetched, and blocks 59, 60, 62 and 64 were read as landed.
  - The own-prior-art check found block 60 T5(b) already giving the sign's equation. T3(a) restates it, and it is not claimed as new.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_block_60s_declared_numbers_unit_free_speeds_force_s_equals_p_plus_two_positive_content_forces_the_kinetic_sign_2026_09_24.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
