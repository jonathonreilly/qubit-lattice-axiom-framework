---
claim_id: admissibility_rule_if_the_member_sees_the_sea_its_uniform_shear_modes_acquire_a_gap_under_the_free_particle_rule_and_grow_under_the_frame_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "WITHIN block 135's quadratic member action as landed (L = [alpha tr(hdot^2) + beta (tr hdot)^2]/wbar + K wbar(u R1 + R2) - e u + (1/2) Theta.h), block 147's filled sea as landed and block 150 as landed, with the supplied reading that the member sees the sea, so that the sea's energy per site E_sea(h) enters the member's action: (T1) a uniform traceless strain h = eps S has no curvature term and no trace rate, so L = (alpha/wbar) tr(S^2) epsdot^2 - E2 eps^2 and omega^2 = wbar E2/(alpha tr S^2), which is 4 wbar E2/(K tr S^2) at alpha = K/4; (T2) under the free-particle stretch rule (blocks 184, 187, 190; pushed) E2 > 0 for both shear classes (exact on the side-6 and side-8 tori), so these modes acquire a real gap; (T3) under block 62's frame the sea's second-order energy is -<sum lam^2 s^2/|s| - (sum lam s^2)^2/(2|s|^3)>, negative for every nonzero stretch because (sum lam^2 s^2)(sum s^2) - (sum lam s^2)^2 = sum_(i<j) s_i^2 s_j^2 (lam_i - lam_j)^2, so the modes grow; (T4) under block 183's reach-three completions with q2 = -1/2 they grow too; (T5) a vacuum whose energy depends on the volume only gives no second-order term along det g = 1, hence no gap. The kinetic side of seeing the sea is block 150 T4 (landed): the sea's inertia takes the member off its closing line. The supervisor's own derivation, unrefereed. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_one_light_cone_exactly_on_the_lattice_the_two_step_content_meets_the_members_identity_for_every_state_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
  - admissibility_rule_the_members_zero_mode_tests_the_zero_of_energy_if_the_member_sees_the_half_filled_sea_a_closed_lattice_bounces_or_cannot_move_bounded_theorem_note_2026-09-25
  - admissibility_rule_every_clock_profile_a_relabelling_forces_the_whole_momentum_constraint_and_no_positive_inertia_can_be_added_to_the_member_bounded_theorem_note_2026-09-25
runner: scripts/admissibility_rule_if_the_member_sees_the_sea_its_uniform_shear_modes_acquire_a_gap_2026_09_28.py
---

# If the member sees the sea, its uniform shear modes acquire a gap under the free-particle rule and grow under the frame

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 135, 147 and 150 as landed; blocks 183, 184, 187 and 190 are pushed and placed, and the facts used from them are re-derived; the supervisor's own derivation, unrefereed; nothing adopted or registered; unaudited)

This note works within blocks 135, 147 and 150 as landed on main (the member's quadratic action, the filled sea, and the sea's inertia) and asks what the sea's response to shear does to the member's own modes if the member sees the sea; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 190 (pushed) found that under the free-particle stretch rule the filled sea's energy rises when the lattice is sheared at fixed volume. Under the frame and the reach-three completions it falls. The zero-of-energy row asks whether the member sees the sea. This note follows the sea's shear response into the member's own equations.

- **T1: the sea sets the modes' frequency.** A uniform traceless strain `h = εS` has no curvature term in the member's landed action, and no trace rate. Its only restoring force is the seen sea's second-order energy `E₂ε²`. So `ω² = w̄E₂/(α tr S²)`, which is `2w̄E₂/K` at `α = K/4` for `tr S² = 2`.
- **T2: under the free-particle rule, a gap.** `E₂ > 0` for both shear classes, so the member's uniform shear modes acquire a real gap. On the infinite lattice (block 190 T5, second version) the gap satisfies:
  - `ω²K/w̄ ∈ [1/32, 7/40]` for the diagonal class;
  - `ω²K/w̄ ∈ [1/20, 3/20]` for the off-diagonal class.
- **T3: under the frame, growth.** The sea's second-order energy is negative for every nonzero stretch, by an exact inequality, so the modes grow.
- **T4: under the reach-three completions, growth too.**
- **T5: a vacuum that sees only volume gives no gap.** Its energy has no second-order term along fixed-volume shears.

In plain terms: if the member feels the filled sea, the sea's reaction to shear acts on the member's own shear motions like a spring. Under the free-particle rule the spring holds, so these motions acquire a lowest frequency, a gap, instead of being free. Under the simple rescaling rule it pushes, so they run away. A vacuum that only cares about volume, as in the comparator, would do neither. So seeing the sea costs the member twice: its shear modes are gapped (this note), and its kinetic term leaves the closing line (block 150).

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-28) is used for three things: no possibility or site is privileged; the Lattice axiom's sites, bonds and translations; and the memo's silence on amplitude dynamics. Blocks 135, 147 and 150 are used as landed on main. Blocks 183, 184, 187 and 190 are pushed and placed; the facts used from them are re-derived (runner C1, D1, E1).

- **The member** (block 135), quoted: "`L = [α tr(ḣ²) + β(tr ḣ)²]/w̄ + Kw̄(uR₁ + R₂) − e_uu + ½ΣΘ_ijh_ij`". `R₁ = p² tr h − p·h·p`, and `R₂` is quadratic in `p`.
- **The sea** (block 147), quoted: "Counting each reduced-zone pair once gives the sea energy per site".
- **Seeing the sea** (supplied, the zero-of-energy row). The sea's energy per site, `E_sea(h)`, enters the member's action as content. The sea's stress is isotropic, so a traceless strain has no first-order term, and the second-order term is `E₂ε²`.
- **Block 150** (landed), quoted: "**T4: the sea's inertia is such an addition.**" The sea's adiabatic inertia is positive and moves the member off its closing line.
- **Strains.** `g = exp(εS)` with `S` traceless and `tr S² = 2`: the diagonal class `diag(1, −1, 0)` and the off-diagonal class `e₁e₂ + e₂e₁`.

In the literature, a vacuum energy that depends on the metric only through `√det g` is what a Lorentz-invariant vacuum gives. A term acting as a mass for a metric field's spin-two modes is the Fierz–Pauli mass term. This note uses neither as authority.

## Domain qualifications

- Uniform traceless strain modes only, in the member's quadratic action.
- `E₂` is exact on the side-6 and side-8 tori. On the infinite lattice it is enclosed exactly by block 190 T5 (second version):
  - `E₂ ∈ [1/64, 7/80]` per `ε²` for `S = diag(1, −1, 0)`, a quarter of block 190's `λ`-value;
  - `E₂ ∈ [1/40, 3/40]` for `S = e₁e₂ + e₂e₁`.
- The sea's inertia (block 150's kinetic side) is not added to `α` here. It would lower the gap, without changing its sign.

## Theorem T1 — the sea sets the modes' frequency

*Statement.* For `h = εS` with `S` traceless and uniform, `R₁ = R₂ = 0` and `tr ḣ = 0`. So `L = (α/w̄) tr(S²) ε̇² − E₂ε²`, and `ε̈ = −ω²ε` with `ω² = w̄E₂/(α tr S²)`. At `α = K/4`, `ω² = 4w̄E₂/(K tr S²)`.

*Proof.* The curvature terms are quadratic in the wave vector and vanish for a uniform strain, and `tr S = 0`. The equation of motion is then runner B1's. ∎

## Theorem T2 — under the free-particle rule, a gap

*Statement.* Under the free-particle rule `E₂ > 0` for both shear classes on sides 6 and 8. On side 6 it is `1/27 + (34√3 + 65√6)/3456` for the diagonal class and `25/648 + (9√6 − 8√3)/1728` for the off-diagonal class. So `ω² > 0`: the uniform shear modes have a real gap, `ω² = 2w̄E₂/K` at `α = K/4`. With block 190 T5's enclosures the gap holds on the infinite lattice, with `ω²K/w̄` in `[1/32, 7/40]` (diagonal class) and `[1/20, 3/20]` (off-diagonal class).

*Proof.* Block 190 T3–T4, re-derived through block 187's second-order spectrum (runner C1). The infinite-lattice bounds are block 190 T5's enclosures inserted in T1 (placed, not re-derived here). ∎

## Theorem T3 — under the frame, growth

*Statement.* Under block 62's frame, `F_a = s_a/ℓ_a`, the sea's second-order energy is

`−⟨Σ_a λ_a² s_a²/|s| − (Σ_a λ_a s_a²)²/(2|s|³)⟩`.

Since `(Σ λ_a² s_a²)(Σ s_a²) − (Σ λ_a s_a²)² = Σ_{i<j} s_i² s_j² (λ_i − λ_j)² ≥ 0`, the bracket is at least `½Σ λ_a² s_a²/|s|`. So the energy is negative for every nonzero stretch, and `ω² < 0`: the modes grow. On side 6 with `λ = (1, −1, 0)` the value is negative.

*Proof.* Runner D1: the expansion and the identity symbolically, and the side-6 value exactly. ∎

This is the frame's "gives way" of blocks 155 and 167, now as a sign that holds on every lattice.

## Theorem T4 — under the reach-three completions, growth too

*Statement.* Under block 183's reach-three completions with `q₂ = −½`, `E₂ < 0` on sides 6 and 8. So the modes grow.

*Proof.* Exact label sums (runner E1). ∎

## Theorem T5 — a vacuum that sees only volume gives no gap

*Statement.* `det exp(εS) = exp(ε tr S) = 1` for traceless `S`. So a vacuum energy `ρ√det g` has no second-order term along these strains, and gives no gap.

*Proof.* Runner F1. ∎

## What this settles and what it does not

- **Settled.** If the member sees the sea, its uniform shear modes are:
  - gapped under the free-particle rule;
  - growing under the frame (on every lattice) and under the reach-three completions;
  - free only for a vacuum whose energy depends on volume alone, which the lattice sea is not.
- **For the third column (the zero-of-energy row).** Seeing the sea costs the member in two ways:
  - its kinetic term leaves the closing line (block 150 T4, landed);
  - its uniform shear modes acquire a gap `ω² = 2w̄E₂/K` (this note).
  - The gap is small in the walker's units only if `K ≫ E₂`, with `E₂` between `1/64` and `3/40` per `ε²` on the infinite lattice (block 190 T5).
  - Under the free-particle rule the other two dangers soften: the bounce (186) and giving way (190).
- **Not settled.**
  - Non-uniform shear waves; the gap would set their lowest frequency if the sea's response stays local.
  - The sea's inertia added to `α`.
  - The massive sea's gap: block 190 found `E₂` positive for the massive sea too.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "the zero-of-energy row: consequences of the member seeing the sea (blocks 147, 150, 183, 186, 190)"
source_of_blocker_text: admissibility_rule_the_members_zero_mode_tests_the_zero_of_energy_if_the_member_sees_the_half_filled_sea_a_closed_lattice_bounces_or_cannot_move_bounded_theorem_note_2026-09-25
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "an other-family referee; non-uniform shear waves with the sea's response; the sea's inertia in alpha"
conditional_surface_status: "exact within block 135's quadratic action and the tori examined, under the supplied reading that the member sees the sea"
hypothetical_axiom_status: "seeing the sea and the stretch rules are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.**
  - Block 135 (landed): the member's action and `α = K/4`.
  - Block 147 (landed): the sea.
  - Block 150 (landed): the sea's inertia.
  - Blocks 155 and 167: the frame's "gives way".
  - Block 183 (pushed): the reach-three formula.
  - Blocks 184, 187 and 190 (pushed): the free-particle rule and the sea's shear energy under it.
- **In the literature.**
  - A Lorentz-invariant vacuum energy depends on the metric only through `√det g`.
  - A spin-two mass term of Fierz–Pauli type.
  - The Cauchy–Schwarz inequality.
  - None is used as authority.
- **New here.**
  - The gap formula for the member's uniform shear modes (T1).
  - The frame's sign on every lattice (T3).
  - The member-side reading of blocks 183 and 190 (T2, T4).
- **Provenance.** The supervisor's own (Claude Opus 5.5), unrefereed.

## Exact target and obligation graph

Target: the effect on the member of seeing the sea's shear response. The obligations are:
- (O1) the premises (A3);
- (O2) the mode equation (B1);
- (O3) the free-particle rule's sign (C1);
- (O4) the frame's sign (D1);
- (O5) the reach-three sign (E1);
- (O6) the volume-only vacuum (F1).

## No-Go Discipline Gate

The note's negative sentences:
- if the member sees the sea, its uniform shear modes are not free under any of the three rules examined;
- under the frame they grow on every lattice.

### N1 — Attack routes and the scope they leave
Attack routes, each examined:
1. *A different mode normalisation.* The gap is `w̄E₂/(α tr S²)` for any traceless `S`. ATTEMPTED; closed.
2. *The sea's inertia.* It would enlarge `α` and lower the gap; the sign is unchanged. ATTEMPTED; stated.
3. *Non-uniform modes.* Not examined.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The following are declared: seeing the sea, the member's quadratic action, uniform modes, and the tori.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; sites, bonds, translations; silence on amplitude dynamics | yes |
| block 135 (landed) | the member's action | yes (quoted, A3) |
| block 147 (landed) | the sea | yes (quoted, A3) |
| block 150 (landed) | the sea's inertia | cited (A3) |
| blocks 183, 184, 187, 190 (pushed) | the sea's shear energies | re-derived (C1, D1, E1) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "seen sea: gap under the free-particle rule, growth under the frame and reach three, none for a volume-only vacuum" | executed: the mode equation; the frame's expansion | executed: the inequality | executed: exact `E₂` on sides 6, 8 | executed: `det exp(εS) = 1` | the frame's sign is proved on every lattice; the rule's infinite-lattice sign is enclosed exactly in block 190 T5 (placed) |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "A gap at the lattice scale is harmless if `K` is large."
  - *Reply:* Agreed; T1 gives the scaling, `ω² = 2w̄E₂/K`. The note records the cost; it does not rank it.

### N8 — Cross-cycle echo
- Block 150: seeing the sea moves the member's kinetic term.
- Blocks 155, 167 and 183: the sea gives way under the frame and reach three.
- Block 190: under the free-particle rule it resists.
- This note: the member's uniform shear modes are gapped or growing accordingly.

## Falsifiers

- A traceless uniform strain with a curvature term in the member's quadratic action.
- A lattice on which the frame's second-order sea energy under a nonzero stretch is nonnegative.

## Boundaries and non-claims

- Uniform traceless modes in the member's quadratic action; the tori examined.
- Seeing the sea and the stretch rules are supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 135, 147 and 150 (landed), quoted. Blocks 183, 184, 187 and 190 (pushed), placed and re-derived.
- Named standard imports, at definition level:
  - Euler–Lagrange equations of a quadratic action;
  - the Cauchy–Schwarz inequality;
  - the matrix exponential;
  - exact symbolic arithmetic with radicals.

## Review record

- **Who and when.** Supervisor-run block (Claude Opus 5.5), 2026-09-28, during the owner's third 12-hour campaign.
- **Provenance.** The supervisor's own derivation, unrefereed.
- **Floating control in scratch.** On the infinite lattice, under the free-particle rule, `E₂` is `+0.0504` (diagonal class) and `+0.0491` (off-diagonal) per `ε²` for `g = exp(εS)`. Both are enclosed exactly in block 190 T5 (second version); this note's second version cites the enclosures.
- **Mutation census.** One mutation per science family, each failing only in its own family, and two in family G.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_if_the_member_sees_the_sea_its_uniform_shear_modes_acquire_a_gap_2026_09_28.py
```

Expected: `TOTAL: PASS=13 FAIL=0`.
