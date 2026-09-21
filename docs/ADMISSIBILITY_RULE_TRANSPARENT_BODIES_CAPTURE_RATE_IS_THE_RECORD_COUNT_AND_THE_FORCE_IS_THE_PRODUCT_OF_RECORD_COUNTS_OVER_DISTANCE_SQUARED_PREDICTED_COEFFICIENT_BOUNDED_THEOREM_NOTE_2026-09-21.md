---
claim_id: admissibility_rule_transparent_bodies_capture_rate_is_the_record_count_and_the_force_is_the_product_of_record_counts_over_distance_squared_predicted_coefficient_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied inertial clause of block 44 (PR #8550) and the wind law of block 45 (PR #8553); nothing adopted. (T1) In the uniform product state at density rho the expected rate at which records step onto one given site is q_1 = 6 rho <max(0, s.e)>/sqrt 3 = (sqrt 3/2) rho for the sphere menu (<max(0, s_z)> = 1/4) and q_1 = rho for the six-axis menu: the kinetic capture rate of one capturing site, depletion neglected. (T2) For a body of capturing sites the same expectation is (number of exposed faces) rho/(4 sqrt 3): separate sites add (6 faces each), adjacent sites share faces (10 for a pair, 24 for a 2x2x2 cube, 78, 174, 294, 486 for lattice balls of radius 2 to 5): the capture rate is the record count for bodies whose sites do not touch, and follows the surface for compact ones. (T3) With block 45's free-streaming force K_0 Q_1 Q_2/r^2, K_0 = sqrt3/(4 pi rho (1 - rho)), two bodies of N_1 and N_2 separate capturing sites attract with G N_1 N_2/r^2, G = K_0 q_1^2 = 3 sqrt3 rho/(16 pi (1 - rho)). EXECUTED, NOT CLAIMED (sphere menu, side 96, density 0.3, gamma 1): capture rate per site 0.236, 0.241, 0.234, 0.221, 0.188, 0.135 for 3, 9, 15, 45, 87, 180 sites scattered in a ball of radius 6 (kinetic value 0.251); capture rate per exposed face 0.041, 0.045, 0.045, 0.045 for solid balls of radius 2 to 5 (kinetic value 0.042; block 45's controls); force between two dilute bodies at separation 16: F/(N_1 N_2) = (1.44 +- 0.10) 10^-4 for 15 to 29 sites each (four runs), 1.03 10^-4 for a light body against a heavier one (three runs), 0.98 10^-4 for 35 to 48 sites (two runs), against G/r^2 = 1.65 10^-4 with the kinetic q_1 and 1.46 10^-4 with the executed q_1 = 0.236; K = 0.675 +- 0.042 for the most dilute pairs against K_0 = 0.67. NOT claimed: a force law beyond what was executed, the transparent regime at other densities or scattering rates, growth and drag (which share the rate q_1), any gravitational statement, any adoption."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_transparent_bodies_capture_rate_is_the_record_count_force_is_the_product_of_record_counts_predicted_coefficient_2026_09_21.py
---

# Transparent bodies: the capture rate is the record count, and the force is the product of the record counts over the square of the distance, with the coefficient predicted

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact product-state expectations within a supplied clause; capture rates and forces executed, not claimed; nothing adopted or registered; unaudited)

This note works within the supplied inertial clause of block 44 and the wind law of block 45; it reports when the capture rate of a body is its number of records and what force follows; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 45 (PR #8553) found that two capturing bodies attract with `F = K Q₁Q₂/r²`, where the `Q` are capture rates, and that for dense bodies the capture rate follows the surface, not the number of records. Block 41 (PR #8547) had shown that the only local additive invariant density of the record layer is the record count. This note closes the gap between the two for bodies that are transparent to the gas.

1. **One site.** In the uniform product state a capturing site takes up `q₁ = (√3/2)ρ` records per tick (sphere menu; `ρ` for the six axes), from the six faces through which records can step onto it (T1).
2. **A body.** The same expectation for a body is its number of exposed faces times `ρ/(4√3)`: sites that do not touch add, sites of a compact body share faces (T2). Executed: `0.236, 0.241, 0.234` per site for `3, 9, 15` sites scattered in a ball of radius 6 (kinetic value `0.251`), falling to `0.135` at `180` sites as the ball becomes opaque; per exposed face `0.041`–`0.045` for solid balls of radius 2 to 5 (kinetic `0.042`).
3. **The force.** With block 45's free-streaming coefficient the force between two transparent bodies is `G N₁N₂/r²`, `G = K₀q₁² = 3√3 ρ/(16π(1 − ρ))` (T3). Executed at separation 16: `F/(N₁N₂) = (1.44 ± 0.10)·10⁻⁴` for the most dilute pairs, against `G/r² = 1.46·10⁻⁴` with the executed `q₁` (`1.65·10⁻⁴` with the kinetic one); `K = 0.675 ± 0.042` against `K₀ = 0.67`. As the bodies fill up, `F/(N₁N₂)` falls (`1.03·10⁻⁴`, `0.98·10⁻⁴`).

So in the inertial clause, for bodies transparent to the gas, **the source of the wind law is the record count** — block 41's forced source — **and the force is the product of the record counts over the square of the distance, with a coefficient fixed by the density of the gas.** What this costs is unchanged: encounters must re-draw contents, bodies must capture records, and the same rate `q₁` makes them grow and drags them (Boundaries).

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "owner, 2026-09-20: 'ok lets define what a source is and go from there' (block 41: the source is the record count); block 45: the wind law's charge is the capture rate, which for dense bodies is not the record count; the record-pair source note on main: identify the Record source and supply a source/response law"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "for transparent bodies the wind law's source is the record count and the executed force is N1 N2/r^2 with the predicted coefficient; next: the same at other densities and scattering rates, the opacity at which additivity fails as a function of the body's column density, and growth and drag against the attraction; queued on ai/probes"
conditional_surface_status: "T1, T2 exact expectations in the uniform product state (depletion by the capturing body neglected); T3 combines them with block 45's free-streaming coefficient; capture rates and forces (floating point; side 96; one to four seeds) are in the controls and not claimed"
hypothetical_axiom_status: "the inertial clause of block 44 (its scattering re-draws contents) and the capture of records by bodies; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full) is used through "A site never carries more than one record; records are permanent." Block 01 (on `main`, proposed and unaudited) supplies the menus. Blocks 44 and 45 (open PRs #8550, #8553) supply the clause, the stationarity of the uniform measure, the wind and the free-streaming force; block 41 (open PR #8547) the statement that the record count is the only local additive invariant density. They are restated; the runner re-derives what it uses.

- **Capturing site, body.** A solid site keeps any record that steps onto it. A body is a set of capturing sites; it is *transparent* when a record of the gas rarely meets two of its sites, *opaque* when it rarely gets through.
- **Exposed face.** A face between a site of the body and a site outside it.
- **`q₁`, `K₀`, `G`.** `q₁` the capture rate of one site; `K₀ = √3/(4πρ(1−ρ))` the free-streaming coefficient of block 45's force `K Q₁Q₂/r²`; `G = K₀q₁²`.

The rate at which a gas strikes a surface is the effusion rate of kinetic theory, associated with Knudsen; capture limited by transport is the problem of Smoluchowski; the attenuation of a beam by scattered absorbers is the law of Lambert and Beer; the requirement that matter be transparent to the corpuscles is the oldest objection to the shadow picture of Le Sage. None is used as authority.

## Prior art and what is new

The effusion rate and the transparency requirement are classical. What is new is the closing of a gap inside the campaign: block 41's forced source (the record count) and block 45's executed charge (the capture rate) coincide exactly when bodies are transparent, with `q₁` computed from the clause and the executed force matching `G N₁N₂/r²` with no free parameter.

## Exact target and obligation graph

Target: when is the wind law's charge the record count, and what is the force then. Obligations: (O1) one site; (O2) a body; (O3) the coefficient. T1–T3 discharge them; the controls execute capture rates and forces.

## Theorem T1 — the kinetic capture rate of one site

In the uniform product state each neighbour of the site is occupied with probability `ρ` by a record of uniform content, and a record of content `s` at the neighbour in direction `−e_k` steps onto the site at the rate `max(0, s·e_k)/√3`. Over the uniform sphere `⟨max(0, s_z)⟩ = (1/2)∫₀¹ μ dμ = 1/4`. Summing over the six neighbours, `q₁ = 6ρ(1/4)/√3 = (√3/2)ρ`. For the six-axis menu a neighbour holds a record pointing at the site with probability `ρ/6`, and `q₁ = ρ`. ∎

The uniform state is what the gas is in far from bodies; next to a capturing site it is depleted, which the expectation neglects (executed: `0.236`–`0.241` against `0.251`).

## Theorem T2 — a body captures through its exposed faces

The argument of T1 applies to each face between a site of the body and a site outside it, and to no other face. So the expected capture rate of a body in the product state is its number of exposed faces times `ρ/(4√3)`. A site has six; two separate sites twelve; two adjacent sites ten; a `2×2×2` cube `24`; lattice balls of radius `2, 3, 4, 5` have `33, 123, 257, 515` sites and `78, 174, 294, 486` exposed faces. For sites no two of which touch the capture rate is `q₁` times the number of sites. ∎

## Theorem T3 — the coefficient of the force between transparent bodies

Block 45's free-streaming force between two capturing bodies is `K₀ Q₁Q₂/r²` (its T3 and T5). With `Q_i = q₁N_i` from T2, `F = G N₁N₂/r²` with `G = K₀q₁² = [√3/(4πρ(1−ρ))](3ρ²/4) = 3√3 ρ/(16π(1 − ρ))`; in rational form `(4πG)² = 27ρ²/(16(1−ρ)²)`. ∎

At `ρ = 0.29`, `G = 0.0422`; with the executed `q₁ = 0.236` in the place of the kinetic one, `0.0373`.

## Executed: capture rates and forces of dilute bodies (not proved)

Control `specs/supervisor_control_block47_bodies.py` (sphere menu, side 96, density `0.3`, `γ = 1`; a body is a ball of radius 6 in which each site is solid with probability `f`).

| `f` | solid sites `N` | capture rate `Q` | `Q/N` |
|---|---|---|---|
| `0.005` | 3 | `0.709` | `0.236` |
| `0.01` | 9 | `2.167` | `0.241` |
| `0.02` | 15 | `3.516` | `0.234` |
| `0.05` | 45 | `9.963` | `0.221` |
| `0.1` | 87 | `16.35` | `0.188` |
| `0.2` | 180 | `24.29` | `0.135` |

Pairs at separation 16, 10000 ticks each (mean and standard error over runs):

| pair | runs | `N₁`, `N₂` | `F` | `K = F r²/(Q₁Q₂)` | `F/(N₁N₂)` |
|---|---|---|---|---|---|
| `f = 0.02` both | 4 | 15–29 | `0.057 ± 0.006` | `0.675 ± 0.042` | `(1.44 ± 0.10)·10⁻⁴` |
| `f = 0.02` against `0.05` | 3 | 15–20, 47–50 | `0.083 ± 0.007` | `0.530 ± 0.015` | `(1.03 ± 0.04)·10⁻⁴` |
| `f = 0.05` both | 2 | 35–48 | `0.186 ± 0.023` | `0.555 ± 0.001` | `0.98·10⁻⁴` |
| prediction `G/r²` | | | | `K₀ = 0.67` | `1.65·10⁻⁴` (kinetic `q₁`), `1.46·10⁻⁴` (executed `q₁`) |

Solid balls (block 45's controls, PR #8553): capture rates `3.17, 7.8, 13.2, 21.8` at radius `2, 3, 4, 5`, that is `0.041, 0.045, 0.045, 0.045` per exposed face, against the kinetic `0.042`.

## No-Go Discipline Gate

The note's negative sentence: for compact bodies the capture rate is not the record count (it follows the exposed faces).

### N1 — Routes by which the sentence could fail
1. *Porous matter* — a body whose sites do not touch and whose column density is small is transparent, and then the capture rate is the record count; this is the positive half of the note.
2. *Another capture clause* — a body that captures only with a small probability per encounter is transparent at any filling; not executed.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The product-state expectation neglects the depletion caused by the body; declared, with the executed size of the effect.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | permanence | yes (premise) |
| block 01 (`main`) | the menus | yes (premise, proposed) |
| blocks 44, 45 (open PRs #8550, #8553) | the clause; the uniform stationary measure; the wind and the free-streaming force | yes (restated) |
| block 41 (open PR #8547) | the record count as the only local additive invariant density | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "a site captures `(√3/2)ρ`; a body captures through its exposed faces; transparent bodies attract with `G N₁N₂/r²`" | executed: the half-sphere moment `1/4`; the six-axis neighbour count | executed: exposed faces of sites, pairs, a cube and four balls | not applicable | executed: the coefficient at three densities | T1, T2 exact expectations in the uniform product state; T3 a combination with block 45's free-streaming force; capture rates and forces executed only |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply neither an update law nor a capture clause. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "You have tuned nothing, but you have chosen everything: a gas, a capture rule, a dilute body." Reply: yes; each is a supplied clause and is listed as such, with its cost. What the note establishes is a conditional with no free parameter: under those clauses the source is the record count and the force is `G N₁N₂/r²` with `G` computed from the density, and the executed force agrees. Whether the clauses are the framework's is the owner's question.

### N8 — Cross-cycle echo
Block 42's capacity (sources that do not add when records are boundary values) and block 45's surface-following capture rate are the opaque side of the same fact; the transparent side is where block 41's forced source reappears.

## Falsifiers

- A body of separate capturing sites whose product-state capture rate is not `q₁` times their number, or a compact body whose rate is not its exposed faces times `ρ/(4√3)`.
- For the executed part: dilute pairs whose `F/(N₁N₂)` departs from `G/r²` by more than the errors and the depletion of `q₁` allow; a `Q/N` that does not approach the kinetic value as the body empties.

## Boundaries and non-claims

One density, one scattering rate, one separation for the pairs; one to four seeds. The product-state expectation neglects depletion (six per cent at the executed parameters). The rate `q₁` at which a site captures is also the rate at which a body grows and at which its motion is dragged towards the local wind; attraction outruns both only when the gas inside an orbit weighs much less than the central body (an estimate recorded in the campaign's decision record, not a result). The clause re-draws contents in encounters (block 44's caveat). No gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the sentence quoted under Premises. Block 01 (on `main`): the menus; proposed, unaudited. Blocks 41, 44, 45 (PRs #8547, #8550, #8553, open): restated or placed.
- Named standard imports at definition level: the first moment of a half-sphere; counting faces of a lattice body.
- Reference only: Knudsen for effusion, Smoluchowski for transport-limited capture, Lambert and Beer for attenuation, Le Sage for the transparency requirement.

## Review record
Supervisor-run block of the 12-hour campaign. Lens: block 45 left the wind law's charge as the capture rate and showed it is not the record count for dense bodies; block 41 had forced the record count as the source; the two must meet in the transparent limit if anywhere. The kinetic rate `(√3/2)ρ` was computed first and the dilute capture rates executed against it (`0.236`–`0.241` against `0.251`); the pair forces were then executed against the parameter-free `G/r²`. Refuting pass (`specs/supervisor_control_block47_refuter.py`, machinery disjoint from the runner's): W1 the half-sphere moment by symbolic integration; W2 exposed faces as `6N` minus twice the adjacent pairs; W3 the coefficient symbolically; W4 the six-axis capture rate over all `7⁶` neighbour states. All pass. Mutation census: 7 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
python3 scripts/admissibility_rule_transparent_bodies_capture_rate_is_the_record_count_force_is_the_product_of_record_counts_predicted_coefficient_2026_09_21.py
python3 scripts/admissibility_rule_transparent_bodies_capture_rate_is_the_record_count_force_is_the_product_of_record_counts_predicted_coefficient_2026_09_21.py --list-mutations
python3 .claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block47_refuter.py
```
