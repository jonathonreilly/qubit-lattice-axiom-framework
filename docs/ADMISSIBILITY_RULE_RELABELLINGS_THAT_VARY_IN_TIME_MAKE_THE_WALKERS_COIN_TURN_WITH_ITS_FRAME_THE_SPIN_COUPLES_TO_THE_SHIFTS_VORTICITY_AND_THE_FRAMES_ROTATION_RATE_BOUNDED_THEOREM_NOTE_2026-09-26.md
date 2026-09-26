---
claim_id: admissibility_rule_relabellings_that_vary_in_time_make_the_walkers_coin_turn_with_its_frame_the_spin_couples_to_the_shifts_vorticity_and_the_frames_rotation_rate_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "WITHIN block 62's framed coupling at long wavelength on smooth zero-corner states, on half-densities, with the frame built from the member's lengths (the symmetric e = g^(1/2) = 1 + eta, now varying in time) plus block 158's (1/8) eps.C, the shift entering as (1/2){N^j, -i d_j} (zero background shift), and spatial relabellings that vary in time (xi(t, x), rate chi = d_t xi), which move the walker as a half-density and turn its coin to keep the frame symmetric: (T1) at first order the moved walker differs from the walker of the new fields by exactly (1/4) sigma.curl chi, the coin's turning rate, so consistency needs the coupling (1/4) sigma.curl N, which is the spin part of block 138's symmetric momentum coupled to the shift; (T2) at order strain x relabelling the coupling (1/4) sigma_c eps_cab (e (d_t + L_N) E)_ab, the coin's coupling to the rotation rate of the lengths' frame relative to the shift's flow, restores consistency on all basis pairs of jets; (T3) among local couplings linear in the shift's gradient, in the shift times the strain's gradient or in the frame's rate, up to first order in the strain, scalar or coin vector (636 coefficients), the solutions are this coupling plus a multiple of the scalar expansion rate, which time reversal excludes. Exact over the Gaussian rationals. Relabellings in time with clock profiles that vary in space (the lapse), a background shift and second order in the strain are not examined. The supervisor's own derivation; unrefereed; nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_relabellings_that_vary_in_time_make_the_walkers_coin_turn_with_its_frame_2026_09_26.py
---

# Relabellings that vary in time make the walker's coin turn with its frame: the spin couples to the shift's vorticity and the frame's rotation rate

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** bounded-support (exact at leading order in the spacing, for smooth states of the zero-corner species, with a zero background shift, through first order in the strain; the supervisor's own derivation, not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 62, 65, 136 and 138 as landed on main (the walker's framed coupling, what turning the coin does, the shift and the symmetric momentum); it reports what relabellings that vary in time require of the walker's coupling to the shift and to the frame's rate, through first order in the strain, at leading order in the spacing; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 158 settled the walker's coupling for relabellings that are fixed in time. Relabellings may also change with time. Then the coin, which turns to keep the frame the lengths' own, turns at a changing rate, and the walker feels that rate. This note asks what coupling absorbs it.

- **T1: first order, the spin feels the shift's vorticity.** A relabelling that varies in time leaves the walker off by exactly `¼σ·curl ξ̇`, the coin's turning rate. The member's shift moves by `ξ̇`, so the walker needs the coupling `¼σ·curl N`. That is the spin part of the symmetric momentum that block 138 found the member couples to the shift. So the landed choice of momentum is what these relabellings demand.
- **T2: next order, the spin feels the frame's rotation rate.** At order strain times relabelling, the needed coupling is `¼ σ_c ε_cab (e(∂_t + L_N)E)_ab`: the coin's coupling to how fast the lengths' frame rotates relative to the flow of the shift. At first order this reduces to T1's term.
- **T3: nothing else, up to one term that time reversal forbids.** Take every local coupling linear in the shift's gradient, the shift times the strain's gradient, or the frame's rate, up to first order in the strain, scalar or coin vector. Consistency fixes all of them except a multiple of the local expansion rate, a scalar that is odd under time reversal.

In plain terms: when the relabelling itself moves, the coin has to keep turning to keep up with its frame. The walker then needs a term that lets its spin feel how the frame and the shift rotate. That term is unique, and it is built from the member's own fields. It has the form of the rotation part of the comparator's connection along time; the comparator's operator is not recomputed here. With block 158, the walker's coupling to the member's lengths and shift is now the comparator's, through this order, for every spatial relabelling.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-26.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom."
  - The walker's coupling, the member's relabellings and the comparator are supplied clauses. Nothing is adopted.
- **The walker** (blocks 62 and 158).
  - The coupling is `H = H_f[E] + (1/8)ε·C + ½{N^j, −i∂_j} + V`, with `H_f[E] = ½{E^j_aσ_a, −i∂_j}` on half-densities.
  - The frame is the lengths' own, `e = 1 + η` (symmetric, now varying in time), with `E = e⁻¹`.
  - The shift `N` enters as the derivative along `N` on half-densities. `V` is the coupling to be found.
- **The symmetric momentum** (block 138, landed): "`P^B = P″ + ½∇̄ × (S̃/2)`". Coupled to the shift as `N·P^B`, its spin part is `¼σ·curl N` after summation by parts.
- **Relabellings that vary in time.**
  - The relabelling is `ξ(t, x)`, with rate `χ = ∂_tξ`. It moves the walker as a half-density and turns its coin by the rotation `Θ` that keeps the frame symmetric (block 158).
  - The moved walker is `H′ = (UΦ)H(UΦ)⁻¹ + i∂_t(UΦ)(UΦ)⁻¹`.
  - The fields move to the symmetric `e′`, to `ė′`, and to `N′ = N + uχ`.
  - Conventions: fields are moved forward, `e′ = e − uL_ξ e`, and the shift enters with a plus sign. Then `ġ + L_N g` is unchanged at first order. The landed member writes the shift with the opposite sign, which renames `N`.
- **The unknown couplings.** `V = Σ_c σ_c(A⁰ ∂N + A¹ (e − 1)∂N + A² ∂(e − 1) N + K⁰ ė + K¹ (e − 1)ė)`, where `c = 0` is the scalar part and `c = 1, 2, 3` the coin vector: 636 coefficients.
- **Time reversal.** The walk's `Θ = σ₂K` commutes with `H` (block 54). `σ`, `N` and `ė` are odd under it.
- **The comparator**, named at definition level: the rotation part of the connection of a two-component spinor along the time direction of the shifted slicing, in the time gauge (Weyl; Fock and Ivanenko).
- **Standard imports, named at definition level.**
  - The product rule of the coin's matrices.
  - Derivatives along vector fields on half-densities.
  - Polarization of bilinear identities.
  - Exact linear algebra over the rationals.

## Theorem T1 — first order: the spin feels the shift's vorticity

*Statement.* At first order in the relabelling and zeroth order in the strain:
- the principal parts of the moved walker and of the walker of the new fields agree, with the shift absorbing the moving relabelling;
- the remaining difference is exactly `¼σ·curl χ`.

So `V` must contain `¼σ·curl N`, which is the spin part of block 138's `N·P^B`.

*Proof.* `i∂_t(UΦ)(UΦ)⁻¹ = u·½{χ^j, −i∂_j} + u·½θ̇·σ`. The first term is `½{N′ − N, −i∂}`. At zeroth order in the strain `θ = ½curl ξ`, so the second term is `¼σ·curl χ` (runner B1, on all 60 basis relabellings). ∎

## Theorem T2 — next order: the spin feels the frame's rotation rate

*Statement.* Let `M_ij = ∂_jN^i`. The coupling

`V = ¼ σ_c ε_cab (e(∂_t + L_N)E)_ab = ¼σ·curl N + ¼σ_c ε_cab[−(ηM)_ab + (Mη)_ab + (η̇η)_ab] + (second order in the strain)`

makes the walker of the new fields equal the moved walker at orders `u` and `u·η`, for all relabellings and strains. It is the coin's coupling to the antisymmetric part of `e(∂_t + L_N)E`, the rotation rate of the lengths' frame relative to the flow of the shift.

*Proof.* The difference at a point is bilinear in the jets of `(η, η̇)` and `(ξ, χ)`. So it vanishes iff it vanishes on every pair of basis jets. That gives 29040 exact equations, and the coupling satisfies all of them (runner C1). ∎

## Theorem T3 — nothing else, up to one term that time reversal forbids

*Statement.* Over the 636 coefficients of `V`, the equations have rank 635. Their solutions are T2's coupling plus a multiple of the scalar expansion rate

`div N + N·∇ tr(e − 1) + tr ė − tr((e − 1)ė)`,

that is, `∂_t log √g + div N` through this order. The expansion rate is odd under time reversal while the walk is even, so with time reversal the coupling is unique.

*Proof.* Rank and kernel computed exactly (runner D1). ∎

## What this settles and what it does not

- **Programme T** (panel of 2026-09-26 afternoon) asked what the member's relabellings demand of the walker's coupling.
  - Block 158 answered this for relabellings fixed in time.
  - This note answers it for relabellings that vary in time: the coin must couple to the shift's vorticity and to the frame's rotation rate, uniquely, in the form the comparator's connection has.
  - Spatial relabellings, including those that vary in time, are required under both readings of relabellings in time. So these results do not depend on that reading.
- **The landed symmetric momentum.** Block 136 coupled the shift to `P^B`, and block 138 found its spin part. T1 shows that this spin part is exactly what relabellings that vary in time require.
- **Not settled.**
  - Relabellings in time with clock profiles that vary in space (the lapse), which only reading E requires.
  - A background shift.
  - Second order in the strain.
  - The lattice placement and the other seven species.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "panel 2026-09-26 afternoon, programme T, in time: what do the member's relabellings that vary in time require of the walker's coupling to the shift and the frame's rate?"
source_of_blocker_text: decision-record addenda 46-47 (programme T; the time part left open by block 158)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the lapse sector (clock profiles varying in space, reading E); a background shift; the lattice placement; an other-family referee"
conditional_surface_status: "leading order in the spacing; zero background shift; through first order in the strain; smooth zero-corner states"
hypothetical_axiom_status: "the walker's coupling, the member's relabellings and the comparator are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 62: the framed coupling.
  - Block 65: turning the coin gives a twist.
  - Blocks 136 and 138: the shift couples to the symmetric momentum `P^B`, whose spin part is half the curl of the spin.
- **Pushed blocks** (the supervisor's; unrefereed):
  - 158: relabellings fixed in time need `(1/8)ε·C`;
  - 161: links carrying the lengths' connection supply it.
- **In the literature.**
  - The symmetric momentum as canonical plus half the curl of the spin (Belinfante; Rosenfeld).
  - The coupling of a spinor's spin to the rotation of its frame, the spin connection along time (Weyl; Fock and Ivanenko).
  - Reference only.
- **New here.**
  - T1: the landed spin term is forced by relabellings that vary in time.
  - T2: the coupling at order strain times relabelling.
  - T3: its uniqueness up to the time-odd expansion rate.
- **Provenance.** The supervisor's own derivation, using block 158's machinery extended to time. No other model family has refereed it. Refill z also asks the probes for the time sector.

## Exact target and obligation graph

Target: programme T in time, shift sector. The obligations are:
- (O1) the premise, block 138's momentum (A3);
- (O2) first order (B1);
- (O3) the coupling at order strain times relabelling (C1);
- (O4) uniqueness (D1).

The strongest missing step is the lapse sector.

## No-Go Discipline Gate

The note's negative sentences:
- without `¼σ·curl N` the walker misses relabellings that vary in time at first order;
- no other coupling of the class, apart from the time-odd expansion rate, restores them at the next order.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *The moving term is absorbed by the shift alone.* Only its orbital part is; the coin's turning rate remains (B1). ATTEMPTED.
2. *Another coupling does the job.* The rank is 635 of 636, with the kernel identified (D1). ATTEMPTED.
3. *The frame's rate does not enter.* It does, through `(η̇η)` (C1). ATTEMPTED.

Scope left open:
- couplings with more derivatives;
- the lapse;
- a background shift;
- second order in the strain.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- "Background" appears only in "background shift", a declared restriction.
- "Canonical" appears only in the Prior art's description of the symmetric momentum.
- The sign convention of the shift is declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| blocks 62, 65, 136, 138 (landed) | the coupling, the turn, the shift, `P^B` | yes (138 quoted, A3) |
| block 158 (pushed, unrefereed) | the coupling for relabellings fixed in time | yes (its terms are part of `H`) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the spin couples to the shift's vorticity and the frame's rotation rate, uniquely up to the time-odd expansion rate" | executed: the moved walker at a point with time | executed: 60 basis relabellings at first order | executed: 7200 basis pairs at order u s | executed: the 29040-equation system, rank, kernel | not executed: the lapse; background shift; second order; lattice |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Relabellings that vary in time are just a change of observer."
  - *Reply:* They are among the member's relabellings (its shift moves by `ξ̇`), under either reading.
  - The walker must follow them. T1 shows what that costs at first order: exactly the spin term of the landed symmetric momentum.

### N8 — Cross-cycle echo
- Block 138: the symmetric momentum's spin part.
- Block 158: the fixed-in-time relabellings' term.
- This note: the relabellings that vary in time force the spin part and the frame's rotation-rate coupling.

## Falsifiers

- A basis pair of jets on which T2's coupling fails.
- A second coupling of the class, even under time reversal, that restores consistency.
- A first-order residual other than `¼σ·curl χ`.

## Boundaries and non-claims

- Leading order in the spacing.
- Smooth zero-corner states.
- A zero background shift.
- Through first order in the strain.
- Spatial relabellings only.
- Not refereed.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 54, 62, 65, 136 and 138 (landed), restated and quoted.
- Named standard imports, at definition level:
  - the product rule of the coin's matrices;
  - derivatives along vector fields on half-densities;
  - polarization;
  - exact linear algebra;
  - the spinor's connection along time (Weyl; Fock and Ivanenko) and the symmetric momentum (Belinfante; Rosenfeld), as comparators.

## Review record

- **Who and when.** Supervisor-run block (Claude Opus 5.5), 2026-09-26 evening, during the owner's 12-hour campaign. It extends block 158 to relabellings that vary in time.
- **Before writing.** The own prior-art check covered memory, open PRs, main and the probes. It found blocks 136 and 138 (the symmetric momentum), 158 and refill z's open task on the time sector (no attempt delivered yet).
- **Independence.** The consistency system and the candidate's coefficients are built separately. The candidate is written in closed form from the frame's rotation rate, and the system's kernel is computed exactly.
- **Mutation census.** At least one mutation per science family, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_relabellings_that_vary_in_time_make_the_walkers_coin_turn_with_its_frame_2026_09_26.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
