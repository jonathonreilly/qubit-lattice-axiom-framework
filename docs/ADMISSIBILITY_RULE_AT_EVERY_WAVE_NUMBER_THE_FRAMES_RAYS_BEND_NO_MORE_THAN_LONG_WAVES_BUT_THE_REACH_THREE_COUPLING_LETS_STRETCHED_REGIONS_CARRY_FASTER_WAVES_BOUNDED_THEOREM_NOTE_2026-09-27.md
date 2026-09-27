---
claim_id: admissibility_rule_at_every_wave_number_the_frames_rays_bend_no_more_than_long_waves_but_the_reach_three_coupling_lets_stretched_regions_carry_faster_waves_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "WITHIN blocks 59, 60 and 69 as landed (block 59 T4's local comparison of a ray crossing the gradient with a slow body released at rest at the same point; block 60 T4's one-body field chi = 1 + Qg, N = 1 - Pg, P = Q w0, w0 = 1/(1 + 2Qg0), l = chi^2, w = N/chi; block 69 T4's reach-three symbol at uniform strain, completed at finite strain as 1 + b = 1/l, which block 69 states its leading order does not determine), in the ray model of the principal symbol E = w sqrt(m^2 + |s(k; l)|^2) with s_a = sigma_a/l: (T1) a massless ray whose velocity crosses the gradient bends A[1 + rho(R - 1)] times a slow body's fall, with A = l^2 sum n_a^2 (s_a'^2 + s_a s_a''), rho = -l d log|s|/dl and R = 1 + 2w/(w + w0); (T2) for block 60's crossing (the frame, sigma_a = sin k_a) A = sum n_a^2 cos 2k_a <= 1 and rho = 1, so the ratio is at most R < 3, it falls below 1 for short off-axis waves (a diagonal carrier with tan(kappa/2) = 3/10 has A = 4681/11881), and no wave outruns w/l; (T3) for the reach-three coupling (sigma_a = sin k_a (cos^2 k_a + l sin^2 k_a)) A_a = 1 + (12 l - 14) k_a^2 + O(k^4), waves along an axis outrun w/l wherever l > 7/6 (by (19/6) sqrt(19/45) at l = 9/4), and near a strong body a diagonal ray bends 3 + (34 l - 42) kappa^2 times the fall, above 3 wherever l > 21/17; at Qg = 1/2 the carrier (kappa, kappa, 0) with tan(kappa/2) = 1/10 has the ratio 1606444785801 (6734 G + 3467)/(2524294918129178 (G + 1)), above 4 for strong bodies (G = Qg0). Carriers along an axis or a diagonal only; the ratio at a point, not an integrated turn. A harvest of probe #9018 (Claude Opus 5.5, the supervisor's family), confirmed by an other-family referee (#9341, Grok). Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_bond_rates_and_lengths_a_body_at_rest_sources_no_length_and_the_bending_of_rays_carries_one_more_free_number_bounded_theorem_note_2026-09-21
  - admissibility_rule_a_ledger_linear_in_the_rates_every_clock_a_multiplier_the_ledger_a_wall_term_and_the_curvature_member_doubles_the_bending_bounded_theorem_note_2026-09-21
  - admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_at_every_wave_number_the_frames_rays_bend_no_more_than_long_waves_2026_09_27.py
---

# At every wave number the frame's rays bend no more than long waves, but the reach-three coupling lets stretched regions carry faster waves

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 59, 60 and 69 as landed and the ray model of the principal symbol; a harvest of probe #9018, confirmed by an other-family referee in #9341; nothing adopted or registered; unaudited)

This note works within blocks 59, 60 and 69 as landed on main (the local ray comparison, the curvature member's one-body field, and the reach-three coupling at uniform strain) and asks how rays of every wave number bend against a slow body's fall; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 59 (landed) compared a ray along an axis with a slow body released at rest at the same point. Block 110 left finite wave numbers open. This note is a harvest of a probe result that another model family has confirmed. It works at every wave number for two ways the stretched lengths can enter the walk.

- **T1: one formula.** A massless ray crossing the gradient bends `A[1 + ρ(R − 1)]` times the slow body's fall.
  - `A` measures the curvature of the dispersion across the ray.
  - `ρ` measures how strongly the ray feels the lengths.
  - `R = 1 + 2w/(w + w₀)` is the long-wave value, between 1 and 3.
- **T2: the frame keeps short waves tame.** With block 60's crossing, `A = Σ n_a² cos 2k_a ≤ 1` and `ρ = 1`.
  - Short waves off the axes bend less than long ones. A diagonal carrier with `tan(κ/2) = 3/10` bends less than half as much.
  - No wave outruns the long-wave speed `w/ℓ`.
- **T3: the reach-three coupling does not.** With block 69's reach-three term, completed at finite strain as `1 + b = 1/ℓ`:
  - wherever the lengths are stretched past `ℓ = 7/6`, some short waves along the axes run faster than `w/ℓ`, up to about 2.06 times it at `ℓ = 9/4`;
  - near a strong body, rays off the axes bend more than three times the fall wherever `ℓ > 21/17`;
  - an exact witness gives a ratio above 4.

In plain terms: how the walker's short waves bend near a lump depends on how the stretched lengths enter the walk. Through the frame, short waves bend less than long ones and nothing travels faster than the local long-wave speed. Through the reach-three term, completed in the simplest way, strongly stretched regions carry some short waves faster than that speed, and near a strong lump some rays bend more than three times as much as a slow body falls. Block 69 says its leading order does not fix how the term continues at finite stretch; this is a choice, and it matters.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-27.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom."
  - The walk, its couplings, the member and the ray model are supplied clauses. Nothing is adopted.
- **Block 59 T4 (landed).** For parallel gradients, the ratio of the transverse components is `d log c/d log a`, for a ray along an axis against a slow body at rest.
- **Block 60 T4 (landed).** One body has `P = Q/(1 + 2Qg₀)` and `w₀ = 1/(1 + 2Qg₀)`, with `χ = 1 + Qg`, `N = 1 − Pg`, `ℓ = χ²` and `w = N/χ`.
- **Block 69 T4 (landed).** For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_j c_j]`. Block 69 also states: "Common corner quadratic forms are a leading-order result and do not determine a nonlinear completion." The completion `1 + b = 1/ℓ` with isotropic `B = b` is supplied here as a candidate.
- **The rest term** (blocks 77 and 139, landed). The staggered rest term anticommutes with every hop of odd reach, so `E = w√(m² + |s|²)` at uniform fields.
- **The ray model.** These are rays of the principal symbol `E(x, k)` with slowly varying fields. Hamilton's equations are used.
- **Assumed for the witness's validity only.** Far from the body the lattice kernel is `1/(4πr)` up to faster terms. This puts the witness point at `r = Q/(2π)`, in the ray limit for `G ≫ 1`.

## Domain qualifications

- Carriers along an axis or a diagonal, with the gradient in their plane (or across it for an axis), are computed exactly. Other directions carry cross terms.
- The ratio is local, in block 59's sense. The region where it exceeds 3 overlaps the long-wave capture radius. No statement is made about a ray arriving from infinity.
- The slow body is at rest. Sub-principal terms are not included.
- These are conditional statements within supplied clauses, not a physical gravitational identification.

## Theorem T1 — one formula

*Statement.*
- Let `E = w(x)F(k; ℓ(x))` with `F = √(m² + |s|²)` and `s_a = σ_a(k_a; ℓ)/ℓ`, and let the fields vary along `n̂`.
- For a massless ray whose velocity is perpendicular to `n̂`: `n̂·ẍ = −(w/ℓ)² A[∂_n log w − ρ ∂_n log ℓ]`, with `A = ℓ² Σ_a n_a²(s_a′² + s_a s_a″)` and `ρ = −ℓ∂_ℓ log|s|`.
- A slow body at rest falls at `−(w/ℓ)² ∂_n log w`.
- So bending over fall is `A[1 + ρ(R − 1)]`, with `R = 1 − d log ℓ/d log w = 1 + 2w/(w + w₀)`.

*Proof.*
- For any `E(n̂·x, k)`, `d²(n̂·x)/dt² = (∂_s n̂·∇_k E)(n̂·ẋ) − (n̂ᵀ Hess_k E n̂) ∂_s E`. The first term vanishes when the ray crosses the gradient (B1).
- With `F Hess F = Hess(½F²) − ∇F∇Fᵀ`, and `n̂ ⊥ ∇F`, each `s_a` depending on `k_a` alone gives `ℓ²F n̂ᵀ Hess F n̂ = A`.
- `∂_s E = w′F + w ∂_ℓF ℓ′`, and `ℓ∂_ℓ log F = −ρ` for the massless ray.
- At `k = 0`, `F Hess F = 1/ℓ²` in units of `m`, and `ℓ` does not enter, for both couplings (B2). This gives the fall.
- `R` follows from block 60's field (C1). ∎

## Theorem T2 — the frame keeps short waves tame

*Statement.* For block 60's crossing, `σ_a = sin k_a`:
- `ℓ²(s_a′² + s_a s_a″) = cos 2k_a` and `ρ = 1`. So bending over fall is `A R`, with `A = Σ n_a² cos 2k_a ≤ 1`.
- Along an axis, `A = 1`: block 59 T4's ratio `R`.
- A diagonal carrier with `tan(κ/2) = 3/10` crossing the gradient in its plane has `A = cos 2κ = 4681/11881 < 1/2`. Its ratio is below 1 wherever `R < 11881/4681`.
- The group speed is `w cos k_a/ℓ ≤ w/ℓ`, so no wave outruns the long-wave speed.

*Proof.* Direct differentiation (D1). ∎

## Theorem T3 — the reach-three coupling does not

*Statement.* For block 69's reach-three term with isotropic `B = b` and `1 + b = 1/ℓ`:
- `σ_a = sin k_a(cos² k_a + ℓ sin² k_a)` (B1).
- `ρ_a = cos² k_a/(cos² k_a + ℓ sin² k_a)`, and `A_a = 1 + (12ℓ − 14)k_a² + O(k⁴)`.
- The group speed along an axis, in units of `w/ℓ`, is `cos k(1 + 3(ℓ − 1) sin² k) = 1 + (3ℓ − 7/2)k² + …`.
  - It exceeds 1 near `k = 0` exactly when `ℓ > 7/6`.
  - At `ℓ = 9/4` its maximum is `(19/6)√(19/45) ≈ 2.06`, at `cos² k = 19/45`.
- Near a strong body (`R → 3`), a diagonal ray bends `3 + (34ℓ − 42)κ² + O(κ⁴)` times the fall. This is above 3 exactly when `ℓ > 21/17`.
- **The witness.** At `Qg = 1/2` (`ℓ = 9/4`, `R = 3/(1 + w₀)`), take the carrier `(κ, κ, 0)` with `tan(κ/2) = 1/10`, crossing the gradient in its plane.
  - `A = 1606444785801/1061520150601` and `ρ = 1089/1189`.
  - Bending over fall is `1606444785801(6734G + 3467)/(2524294918129178(G + 1))`, with `G = Qg₀`.
  - It rises with `G` and tends to about 4.2855.

*Proof.*
- Series and differentiation (E1, E2). The witness is exact rational arithmetic at `tan(κ/2) = 1/10`, with `R = 3(1 + 2G)/(2(1 + G))` (E2).
- The witness lies in the ray limit as `G → ∞`. There the point sits at `r = Q/(2π)`, and the fields' gradients are `O(1/r)` with `ℓ`, `w` and `R` fixed. This uses the assumed far-field kernel. ∎

## What this settles and what it does not

- **Settled.** Within the ray model:
  - the frame keeps every wave's bending ratio at most `R < 3`, and every speed at most `w/ℓ`;
  - the reach-three completion `1 + b = 1/ℓ` does neither where the lengths are stretched past `7/6` or `21/17`.
- **For the owner.**
  - Block 69 states that its leading order does not fix the completion. This note shows that the simplest completion breaks the single speed limit in strongly stretched regions.
  - A completion that keeps `w/ℓ` the fastest speed (`A ≤ 1` off the axes) would restore "at most 3". The frame is one such completion.
  - The choice of completion is a supplied clause.
- **Not settled.**
  - Sub-principal terms.
  - Carriers off the symmetric directions.
  - Exact trajectories through the strong region, and capture thresholds at each wave number.
  - A massive walker moving at finite speed.
- **Not ported.** The probe's floating-point packet controls, which agree with the ray law within 0.4%, and its straight-line integrals.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 59 T4 as landed: the local ratio for an axis carrier only; block 110 N1: finite wave numbers open; block 69 N1: the leading order does not determine a nonlinear completion"
source_of_blocker_text: probes task J:derive:bending-over-fall-at-strong-field
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "a completion of the reach-three coupling that keeps w/l the fastest speed; exact trajectories at finite wave number; sub-principal terms"
conditional_surface_status: "the principal-symbol ray model; carriers along axes and diagonals; the completion 1 + b = 1/l for reach three"
hypothetical_axiom_status: "the walk, its couplings and their completion, the member and the ray model are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 59 T4: the local ratio for an axis carrier.
  - Block 60 T4: the one-body field.
  - Block 69 T4: the reach-three symbol, and its statement that the completion is not determined.
  - Block 71: the ratio for bodies of either sign.
- **Probes.**
  - #8862 (attempt 2, Grok-refereed) found the long-wave ratio in `[2, 3)` at a point.
  - #9018, worker `w-macbookpro9927a-j7735`, Claude Opus 5.5, the supervisor's own model family, found T1–T3 at every wave number.
  - #9341, worker `w-macbookpro90c72-jf53f`, `grok-4.6`, another model family, refereed #9018 with its own checker: "HIT: confirmed - a short diagonal frame wave bends less than the fall, and the reach-three witness bends more than four times the fall once the body is strong." It did not rebuild the packet runs.
- **In the literature.** The lattice's short-wave anisotropy `cos 2k` is familiar. Rays of a principal symbol (the eikonal limit) are standard. In the comparator the ratio at a point is fixed by the metric for every wave; here it depends on the carrier.
- **New here.**
  - The harvest.
  - A new exact runner.
  - The general identity for the acceleration across the gradient, checked for any `E(n̂·x, k)`.
- **Provenance.** Found by the supervisor's family and confirmed by another family.

## Exact target and obligation graph

Target: bending over fall at every wave number, for the frame and for reach three. The obligations are:
- (O1) the premises (A3);
- (O2) the symbols and the acceleration law (B1–B2);
- (O3) the long-wave ratio (C1);
- (O4) the frame (D1);
- (O5) reach three and the witness (E1–E2).

## No-Go Discipline Gate

The note's negative sentences:
- under the frame no wave bends more than `R` times the fall or outruns `w/ℓ`;
- under the reach-three completion `1 + b = 1/ℓ`, the long-wave speed is not the fastest where `ℓ > 7/6`.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *Another carrier breaks the frame's bound.* `A = Σ n_a² cos 2k_a ≤ 1` for every carrier crossing the gradient (D1). ATTEMPTED.
2. *The fast reach-three waves are an artefact of long-wave expansion.* The group speed is exact at every `k` (E1). ATTEMPTED.

Scope left open:
- other completions;
- sub-principal terms;
- non-symmetric carriers.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The completion, the ray model and the far-field assumption are declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| block 59 (landed) | the local ratio | yes (quoted, A3) |
| block 60 (landed) | the one-body field | yes (quoted, A3) |
| block 69 (landed) | the reach-three symbol; the completion left open | yes (quoted, A3) |
| blocks 77, 139 (landed) | the rest term anticommutes with odd-reach hops | yes (restated) |
| probe #9018 and referee #9341 | the result and its confirmation | yes (re-derived, rerun exactly) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the frame keeps short waves tame; the reach-three completion lets stretched regions carry faster waves" | executed: the symbols and the acceleration identity | executed: the one-body ratio | executed: `A`, `ρ`, speeds and thresholds for both couplings | executed: the witness as an exact function of `G` | not executed: sub-principal terms; other carriers; trajectories |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Short waves are outside the ray model near a body."
  - *Reply:* The witness sits at `r = Q/(2π)`, where the fields vary on a scale that grows with `G`. The ray model applies there as `G → ∞`.
  - The speed statement is exact at uniform strain, with no ray model needed.
- *Objection:* "Block 69's completion is just one choice."
  - *Reply:* Yes; block 69 says so. This note shows what that choice does and names the property a better one must keep.

### N8 — Cross-cycle echo
- Block 59: the axis ratio.
- Block 110: rays at long waves.
- This note: every wave number, and a flaw in the simplest reach-three completion.

## Falsifiers

- A carrier crossing the gradient with the frame's `A > 1`.
- A wave number with the reach-three axis speed at most `w/ℓ` at `ℓ = 9/4` and `cos² k = 19/45`.

## Boundaries and non-claims

- The principal-symbol ray model; carriers along axes and diagonals; the completion `1 + b = 1/ℓ`.
- The walk, its couplings, the member and the ray model are supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 59, 60 and 69 (landed), restated and quoted. Blocks 77 and 139 (landed), restated.
- Named standard imports, at definition level:
  - Hamilton's equations for a principal symbol;
  - series expansion;
  - exact symbolic and rational arithmetic.

## Review record

- **Who and when.** Supervisor-run harvest block (Claude Opus 5.5), 2026-09-27, during the owner's second 12-hour campaign.
- **Provenance.**
  - Probe #9018 (Claude Opus 5.5) was refereed by #9341 (`grok-4.6`, another family).
  - The supervisor wrote a new exact runner and did not port the floating-point packet controls.
- **Before writing.** Origin was re-fetched. Blocks 59, 60 and 69 were read as landed. The own prior-art check covered memory (block 110's open finite-wave-number case), the held branches, open PRs and main.
- **Mutation census.** At least one mutation per science family, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_at_every_wave_number_the_frames_rays_bend_no_more_than_long_waves_2026_09_27.py
```

Expected: `TOTAL: PASS=14 FAIL=0`.
