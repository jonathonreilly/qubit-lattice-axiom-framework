---
claim_id: admissibility_rule_free_capturing_bodies_are_carried_by_the_wind_capture_law_anisotropic_collisionless_shadow_dilution_law_of_motion_and_its_window_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "Conditional supplied forward hops and body model. Exact capture is weighted by |s|_1; a fully exposed site and a body balanced across axes capture the mean content of a first-harmonic homogeneous reservoir. An arbitrary plate has an anisotropic response. Independent directed walkers have the exact multinomial deficit and simplex moments; the fixed-ray large-distance shadow has the stated directional coefficient, with vector remainder O(r^-3) and coordinate-plane multiplicity. Product closure gives the expected captured-content mixture; motion, spherical inflow and accelerated-fall estimates require further closure. Constant Q/M=q1 requires the additional growing-active-site idealization N=M, not a fixed rigid footprint. No physical force or hydrodynamic limit is proved."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_free_capturing_bodies_are_carried_by_the_wind_capture_law_anisotropic_collisionless_shadow_dilution_law_of_motion_2026_09_21.py
---

# Free capturing bodies are carried by the wind: the capture law, the anisotropic collisionless shadow, and the dilution law of motion with its window

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact expectations in product states and for independent records, within supplied clauses; a closure law of motion; free-body runs executed, not claimed; nothing adopted or registered; unaudited)

This note works within the supplied inertial clause of block 44 and a supplied body clause; it reports what a capturing body takes up, what force free streaming gives, and how a free capturing body moves; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Conditional supplied forward hops and body model. Exact capture is weighted by |s|_1; a fully exposed site and a body balanced across axes capture the mean content of a first-harmonic homogeneous reservoir. An arbitrary plate has an anisotropic response. Independent directed walkers have the exact multinomial deficit and simplex moments; the fixed-ray large-distance shadow has the stated directional coefficient, with vector remainder O(r^-3) and coordinate-plane multiplicity. Product closure gives the expected captured-content mixture; motion, spherical inflow and accelerated-fall estimates require further closure. Constant Q/M=q1 requires the additional growing-active-site idealization N=M, not a fixed rigid footprint. No physical force or hydrodynamic limit is proved.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "campaign decision record (PR #8555): 'the same rate q_1 makes bodies grow and drags them; attraction outruns both only if the gas inside the orbit weighs much less than the central body' was an estimate; blocks 45 and 47 held the bodies fixed"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the estimate is now a derived window with its coefficient, and block 45's free-streaming reason is corrected; next: the force between transparent bodies off the lattice axes and at small scattering rates (the anisotropy of T3 predicts a dependence on direction), and two free bodies in a dilute gas inside the window; queued on ai/probes"
conditional_surface_status: "T1, T2, T4 exact expectations in a product state (what the body does to the gas around it neglected); T3 exact for independent records, its large-distance coefficient with an explicit remainder; T5 a closure; the free-body runs (floating point; side 32 and 64; 96 to 300 seeds) are in the controls and not claimed"
hypothetical_axiom_status: "the inertial clause of block 44 (its scattering re-draws contents), the capture of records by bodies, and the body clause of this note; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full) is used through "A site never carries more than one record; records are permanent." Block 01 (on `main`, proposed and unaudited) supplies the menus. Blocks 44, 45 and 47 (open PRs #8550, #8553, #8556) supply the clause, the wind `g = √3Q/(4πr²(1 − ρ))`, the kinetic capture rate `q₁ = (√3/2)ρ` and the coefficients `K₀ = √3/(4πρ(1 − ρ))`, `G = K₀q₁²`. They are restated; the runner re-derives what it uses.

- **Streaming (block 44).** A record of content `s` (a unit vector) steps to `x + e_k` at the rate `max(0, s·e_k)/√3`; its mean velocity is `s/√3`. A capturing site keeps a record that steps onto it.
- **Body clause (supplied here).** A free body is a rigid set of capturing sites with a mass `M`, the number of records it holds, and a momentum `P`, the sum of their contents. On a clock of rate one it steps to `x + e_k` with probability `max(0, (P/M)·e_k)/√3`, which is the streaming rule of a record of content `p = P/M`; records on the sites it enters are captured; a captured record adds one to `M` and its content to `P`. Number and momentum of gas and bodies together are conserved. For `M = 1` it is the rule of a record.
- **First-harmonic law.** The content law `(1 + 3u·s)/(4π)`, `|u| ≤ 1/3`, of mean content `u`. A gas in local equilibrium, whose content law is proportional to `exp(b·s)`, has it to first order in `b`.
- **Independent records.** Records that stream without exchange and without scattering: the limit of small density of the clause with `γ = 0`.
- **Step frequencies.** For a content `s`, `w_k = |s_k|/|s|₁`: the probabilities with which the directed walk of the record takes its next step along the three axes.

The rate at which a gas strikes a surface is the effusion rate associated with Knudsen. The beam integrals over the simplex are the integrals of Dirichlet; the remainder estimate is Taylor's. A body that absorbs an ambient flux and is pushed into the shadow of another is the picture of Le Sage, and the classical objections to it (drag on moving bodies, accretion, the transparency of matter) are what T4 and T5 compute in this clause. The attraction of sinks in a fluid was studied by Bjerknes. Motion in which velocity, not acceleration, follows the push is what is called Aristotelian. None is used as authority.

## Prior art and what is new

The classical objections to the shadow picture are qualitative. What is new here is their exact form in the campaign's clause: the capture weight `|s|₁` and the two moment identities that make the simple estimate exact in a first-harmonic wind; the multinomial shadow with its direction-dependent force coefficient `|r̂|₁²` against the collisional `9/4`; the dilution law, which holds for both capture channels; and the window `(4π/3)ρr³ ≪ 8N₁/(3π²(1 − ρ))` with its coefficient, which replaces the estimate in the campaign's decision record (PR #8555). The note also corrects the reason given in block 45's T5.

## Exact target and obligation graph

Target: what a capturing body takes up, where the coefficient `K₀` holds, and how a free capturing body moves. Obligations: (O1) the capture law; (O2) the simple estimate in a wind; (O3) the force without collisions; (O4) the content of a free body; (O5) the law of motion and the condition for an accelerated fall. T1–T5 discharge them at their stated levels; the controls execute O2, O4 and O5.

## Theorem T1 — the capture law

In a product state each neighbour of a capturing site is occupied with probability `ρ` by a record whose content has the law `f`, and a record of content `s` at the neighbour in direction `−e_k` steps onto the site at the rate `max(0, s·e_k)/√3`. Since `Σ_k max(0, s·e_k) = |s_x| + |s_y| + |s_z| = |s|₁` over the six directions, the site takes up records at the rate `(ρ/√3)⟨|s|₁⟩_f` and momentum at the rate `(ρ/√3)⟨|s|₁ s⟩_f`. For a unit vector `|s|₁² = 1 + 2Σ_{i<j}|s_i s_j|` lies between 1 and 3, the upper end by the inequality between the arithmetic and quadratic means. The mean content of the captured records is `⟨|s|₁ s⟩/⟨|s|₁⟩`, which is not `⟨s⟩` in general: for the contents `(1,0,0)` and `(−3/5,−4/5,0)`, equally likely, the gas has mean `(1/5, −2/5, 0)` and the captured records `(1/15, −7/15, 0)`. ∎

A body made of lattice sites does not present the same cross-section to every direction of arrival, because records move along the axes only: a face is entered along its normal, at a rate proportional to the component of the content along that normal.

## Theorem T2 — first-harmonic winds

Over the uniform sphere `z` is uniform on `[−1, 1]` and, given `z`, `x²` averages `(1 − z²)/2`. Hence `⟨|z|⟩ = 1/2`, `⟨|z|³⟩ = 1/4`, `⟨|z| x²⟩ = 1/8`, and `⟨|s|₁⟩ = 3/2`, `⟨|s|₁ s_x²⟩ = 1/4 + 2/8 = 1/2`, while `⟨|s|₁ s_x s_y⟩ = 0` by reflection. In the first-harmonic law the odd term does not change the capture rate, `(ρ/√3)(3/2) = q₁`, and the momentum rate is `(ρ/√3)·3u_j⟨|s|₁ s_i s_j⟩ = q₁u`. Every captured record brings `u` on average. ∎

For a body, a face entered along `+z` takes up `(ρ/√3)[e_z/6 + 3 T u]` with `T = diag(1/16, 1/16, 1/8)`. The constant terms cancel between opposite faces, which are equally many for any body. The response is parallel to `u` for every `u` exactly when the exposed faces are equally many along the three axes (a cube: `8, 8, 8`; a ball of radius 3: `58, 58, 58`); for a `2×2×1` plate (`4, 4, 8`) it is `diag(5/4, 5/4, 3/2)` in units of `ρ√3`.

**Correction to block 45.** T5 of block 45 (PR #8553) derived the free-streaming value `K₀` from the statement that a body presents the same projected area to every direction of arrival, so that "the records it captures are an unbiased sample of the records of the gas". By T1 that is false for a lattice body. The value K0 follows for a homogeneous first-harmonic wind and equal exposed-face counts along the three axes, by the identities above, and that is the wind of a gas in local equilibrium, which block 45's T3 assumes. Block 47's coefficient `G = K₀q₁²` stands on the same footing: it is a conditional isotropic capture-closure value, not a general consequence of collisions.

## Theorem T3 — the collisionless shadow and its force

Consider independent records of density `ρ` and content law `f`, and one capturing site at the origin.

*(a) The deficit.* Write the statements for a content in the first octant; the others follow by reflection. The stationary density of records of content `s` at `x` is `ρf(s)[1 − h(x, s)]`, where `h` is the probability that the directed walk of step frequencies `w` started at the origin passes `x`: `h(x, s) = (n!/(x₁!x₂!x₃!)) w₁^{x₁}w₂^{x₂}w₃^{x₃}` for `x` in the closed octant of `s`, with `n = |x|₁`, and zero outside it. Indeed `h(0) = 1` and `h(x) = Σ_k w_k h(x − e_k)` elsewhere, which is the stationary transport equation `Σ_k a_k[n(x) − n(x − e_k)] = 0` with `a_k = |s_k|/√3`, and the capturing site holds no record. With a uniformly vanishing deficit along every backward escape path, it is the only bounded solution: the difference of two solutions is the average of itself over the walk run backwards, which leaves every bounded region or ends at the origin, where the difference is zero.

*(b) Shells.* `Σ_{|x|₁ = n} h(x, s) = 1`: the shadow carries the whole capture through every shell.

*(c) The force.* A transparent capturing site at `x ≠ 0` takes up momentum from its six neighbours; by the transport equation the part missing because of the shadow is `(ρ/√3)∫ f(s) |s|₁ s h(x, s) dΩ`. Its nonzero components have the corresponding signs of x, so the deficit produces inward components; at finite x the force need not be exactly parallel to x. Summed over the sites of a shell, the momentum missing because of the contents of any set of directions is `(ρ/√3)∫ f |s|₁ s dΩ` over that set, whatever the distance.

*(d) The simplex.* In the step frequencies, `dΩ = |s|₁³ dw₁dw₂` (the radial projection of the simplex onto the sphere, with `|s|₁ = 1/|w|₂`), and `∫ h(x, w) dw = n!/(n + 2)! = 1/((n + 1)(n + 2))` for every site of the shell. So `(n + 1)(n + 2) h(x, ·)` is a probability density on the simplex, with mean `μ = (x + 1)/(n + 3)` and summed variance at most `1/(n + 4)`.

*(e) The coefficient.* For the uniform sphere, each octant whose contents reach `x` contributes `−(ρ/(4π√3)) E[Φ(W)]/((n + 1)(n + 2))` with `Φ(w) = w (w·w)^{−5/2}`, reflected into that octant; there are `m(x)` such octants, 1 off the coordinate planes, 2 on a plane, 4 on an axis, and their components along the axes on which `x` vanishes cancel. On the simplex `w·w ≥ 1/3`, the operator norm of the Hessian of each component of Phi is bounded by `15(w·w)^{−3} + 35(w·w)^{−3} ≤ 1350`, and the mean of `W − μ` vanishes, so each component of `E[Φ(W)] − Φ(μ)` is at most `675/(n + 4)` in absolute value; `μ` differs from `x/n` by at most `2/(n + 3)` in each component. At `μ = r̂/|r̂|₁`, `|Φ| = |r̂|₁⁴` along `r̂`, and `n = r|r̂|₁`. Hence

`F(x) = −(ρ/(4π√3)) m |r̂|₁² r̂/r² + O(r^(-3))`, with a vector remainder along any fixed ray; the error need not be radial.

The coefficient `|r̂|₁²` is `10201/7225 ≈ 1.41` towards `(84, 12, 5)`, `121/49` towards `(2, 3, 6)`, `25/9` towards `(1, 2, 2)`, `361/121 ≈ 2.98` towards `(6, 6, 7)`; it runs from 1 near an axis to 3 on the body diagonal. In the same units the collisional coefficient of block 47 at small density is `(3/2)² = 9/4` in every direction. ∎

The average of `|r̂|₁²` over directions is `1 + 4/π ≈ 2.27`, within about one per cent of `9/4`; the two laws differ in shape, not in mean strength. At finite density the exchange of contents between records displaces them, and T3 is the first order in `ρ`.

## Theorem T4 — the dilution law

Let a body of `N` separate capturing sites and content `p = P/M` sit in a product state whose content law is first-harmonic with mean `u`. Records step onto it at the rate `Nq₁` and bring `u` each on average (T2). The body steps at the rate `|p|₁/√3` and enters `N` sites, each occupied with probability `ρ` by a record of the gas, whose mean content is `u`. Hence the expected momentum gain is `u` times the expected mass gain, `N(q₁ + ρ|p|₁/√3)`, whatever `p`. In the product closure, conditional on a fixed number m of captures, the expected content of a body that started with `M₀` records of mean content `p₀` is `(1 − f)p₀ + f u`, `f = m/(M₀ + m)`. ∎

The closure neglects what the body does to the gas around it: its own shadow, which for a moving body is not symmetric, and, with scattering, the local loss of wind where momentum is taken up. Both reduce the content brought per capture; the executed reduction is 3 to 22 per cent.

## Theorem T5 — the law of motion in the closure, and the window of accelerated fall

Take a transparent body of capture rate `Q` and mass `M`, slow enough that `|p|₁ ≪ 1`. By T4, `dp/dt = (Q/M)(u(x) − p)`, and its velocity is `p/√3`. For the additional idealization in which the number N of active separate capturing sites grows with mass as N=M, Q/M=q1. This is different from the fixed rigid footprint in the supplied body clause; for that footprint Q=Nq1 and Q/M decreases as captures accumulate. Under the N=M idealization, the content relaxes to the wind's at the rate `q₁`, whatever the mass. In the wind of a transparent body of `N₁` records (blocks 45, 47), `u = K₀q₁N₁/r² = 3N₁/(8π(1 − ρ)r²)`.

*Early times.* From rest, velocity is gained at the rate `q₁u/√3 = A/r²`, `A = 3ρN₁/(16π(1 − ρ))`, the same for every body: this is `G N₁/(√3 r²)`, the force of block 47 over the inertia `√3` of a record.

*The window (constant central source, isotropic closure, N=M idealization).* A fall from rest at `r` under `A/r²` lasts `t` with `t² = (π²/8) r³/A`, so `(q₁t)² = (π³/2)ρ(1 − ρ)r³/N₁`, which is the number of gas records inside the radius, `(4π/3)ρr³`, over `8N₁/(3π²(1 − ρ))`. The fall is accelerated throughout only when that ratio is small.

*Outside the window.* `p` follows `u(x)`: `dr/dt = −u/√3 = −C/r²`, `C = √3N₁/(8π(1 − ρ))`, so `r³ = r₀³ − 3Ct`. A content perpendicular to the wind decays as `exp(−q₁t)`: an orbit loses its tangential motion at the capture rate. ∎

## Historical author observations (not fresh evidence): a free body in a uniform wind, and a free body near a fixed one (not proved)

Control `specs/supervisor_control_block48_freebody.py` (sphere menu; floating point). A body is a rigid set of capturing sites, each site of a ball of radius 4 solid with probability `0.06` (15 sites on average), `M₀ = N`, `p₀ = 0`.

*Uniform wind* (periodic box of side 32; content law proportional to `exp(0.3 s_x)`, `u = 0.0994`; 300 seeds). Measured content along the wind over `u` times the captured fraction `f`, and displacement over `(u/√3)Σf`:

| case | ticks | `f` at the end | `p_x/(u f)` | displacement ratio |
|---|---|---|---|---|
| pinned, `ρ = 0.3`, `γ = 0` | 40 | `0.89` | `0.97 ± 0.03` | |
| pinned, `ρ = 0.3`, `γ = 1` | 40 | `0.89` | `0.89 ± 0.03` | |
| free, `ρ = 0.3`, `γ = 1` | 40 | `0.90` | `0.78 ± 0.03` | `0.86 ± 0.05` |
| free, `ρ = 0.1`, `γ = 1` | 120 | `0.90` | `0.87 ± 0.03` | `0.93 ± 0.04` |

The transverse contents are zero within errors. The first row is T2; the others show the reductions that the closure of T4 neglects.

*A free body near a fixed one* (open box of side 64 with a reservoir at its walls; `ρ = 0.3`, `γ = 1`; body 1 fixed, a ball of radius 6 filled to `0.1`, 92 sites on average, capture rate `16.66`; body 2 as above, held for 600 ticks while the wind is established, then released at separation 20; 96 seeds). The closure is evaluated along the measured mean path, `u = √3Q₁/(4πr²ρ(1 − ρ))` at the measured separation:

| ticks after release | separation | captured fraction | content towards body 1 | closure `u f` | ratio | drift (sites) | closure | ratio |
|---|---|---|---|---|---|---|---|---|
| 76 | `19.17` | `0.943` | `0.0266 ± 0.0029` | `0.0281` | `0.95 ± 0.10` | `0.83 ± 0.19` | `1.04` | `0.80 ± 0.18` |
| 151 | `18.11` | `0.971` | `0.0288 ± 0.0023` | `0.0324` | `0.89 ± 0.07` | `1.89 ± 0.23` | `2.35` | `0.80 ± 0.10` |
| 226 | `17.12` | `0.980` | `0.0306 ± 0.0021` | `0.0366` | `0.84 ± 0.06` | `2.88 ± 0.26` | `3.85` | `0.75 ± 0.07` |
| 300 | `16.26` | `0.985` | `0.0321 ± 0.0020` | `0.0407` | `0.79 ± 0.05` | `3.74 ± 0.26` | `5.50` | `0.68 ± 0.05` |

At the end 84 per cent of the seeds have moved towards the fixed body and 8 per cent away. The body is carried at 0.7 to 0.9 of the closure's rate; the reductions are of the size found in the uniform wind. Body 1 is not transparent at this filling (block 47), and the separation is less than three times the sum of the radii; neither is corrected for. At these parameters the gas inside the starting radius, about `10⁴` records, is far outside the window of T5 (`0.27 N₁/(1 − ρ) ≈ 36`): this is the carried regime, and the accelerated fall is not executed.

## No-Go Discipline Gate

The note's negative sentences: captured records are not an unbiased sample of the gas; without collisions the force between transparent sites is not the same in every direction; outside the window a free capturing body is carried, not accelerated.

### N1 — Routes by which the sentences could fail
1. *Another streaming rule* — records that could step along diagonals, or a body whose faces are not lattice faces, would change the capture weight `|s|₁`; the clause of block 44 has neither.
2. *Collisions* — may motivate a local closure but do not establish isotropic inflow; the companion cubic-viscosity note explicitly shows why this inference fails.
3. *A body that does not keep what it captures* — a body that re-emits records with their momentum averaged would not grow; emission was executed in block 44 and gives repulsion between emitters; a balance of capture and emission is not worked.
4. *A dilute gas inside the window* — the constant-source, growing-active-site closure predicts approximately accelerated fall there; not executed in this note.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The product state (T1, T2, T4) neglects what the body does to the gas; independence (T3) neglects exchange and scattering; T5 is a closure of T4 with the wind of blocks 45 and 47. Each is declared, with the executed size of the neglected effect where there is one.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | permanence | yes (premise) |
| block 01 (`main`) | the menus | yes (premise, proposed) |
| block 44 (open PR #8550) | the streaming rule | yes (restated) |
| blocks 45, 47 (open PRs #8553, #8556) | the wind, `q₁`, `K₀`, `G` | yes for T5 (restated); T5 of block 45 corrected |
| decision record (open PR #8555) | the estimate that T5 replaces | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "capture is weighted by `|s|₁`; in a first-harmonic wind every captured record brings `u`; the collisionless force has the coefficient `m|r̂|₁²`; both capture channels bring `u`; the window is `(4π/3)ρr³` against `8N₁/(3π²(1 − ρ))`" | executed: the identity and the range of `|s|₁` for 174 rational unit contents; the sphere moments `3/2` and `1/2`; the face response | executed: the multinomial deficit and its transport equation on a `5×5×5` block for four contents; the simplex integral at all 56 sites with `n ≤ 5`; the octant multiplicities | not applicable | executed: shell sums for `n ≤ 6`; the coefficients `10201/7225, 121/49, 25/9, 361/121` and the remainder bound; the dilution identity; the window algebra | T1, T2, T4 exact expectations in a product state; T3 exact for independent records, with an explicit remainder at large distance; T5 a closure; the runs are controls |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply neither an update law, nor a capture clause, nor a body clause. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "The body clause is yours; another clause would give another law of motion." Reply: the clause is the one in which a body moves as the centre of mass of its records and total momentum is conserved; T4 needs only that captured records join the body with their contents, and then the dilution law is bookkeeping. A clause in which bodies do not keep what they capture is route 3 of N1 and is open. Second objection: "The anisotropy is an artefact of independent records." Reply: it is the exact law of that limit, and it distinguishes the directed-walk limit from a separately assumed isotropic closure; collisions alone do not establish that closure. The executed forces of those blocks were along a lattice axis at scattering rates of 0.1 to 4 per tick (mean free paths of about 3 to 0.1 sites against separations of 12 to 40), inside the collisional regime; off-axis forces at small scattering rates are not executed.

### N8 — Cross-cycle echo
Block 43 found that the record layer's fields arrive by diffusion and a carrier needs a speed; block 44 supplied one; this block finds that a body which takes up the carrier is itself carried. The pattern of the lane: each mechanism that gives the record count a long-range pull does so by moving records, and what moves records moves bodies with them.

## Falsifiers

- A content law and a capturing site whose product-state capture rates are not `(ρ/√3)⟨|s|₁⟩` and `(ρ/√3)⟨|s|₁ s⟩`; a first-harmonic wind in which a site with six free faces takes up other than `q₁u`.
- For independent records: a site at which the stationary deficit is not the multinomial expression; a direction off the coordinate planes in which `F r²` does not approach `(ρ/(4π√3))|r̂|₁²`.
- For the executed part: a free dilute body in a uniform wind whose content exceeds `u f` beyond errors, or falls below it by much more than the executed reductions; a free body near a capturing one whose drift departs from the quasi-static prediction by more than the same reductions.

## Boundaries and non-claims

One wind strength, two densities, one body size for the uniform wind; one configuration for the free body near a fixed one. The product closure neglects the body's effect on the gas (executed: 3 to 22 per cent). T3 is the limit of independent records; its anisotropy at finite density and small scattering rate is not executed, and the executed forces of blocks 45 and 47 were along a lattice axis in the collisional regime. T5 is a closure and treats the wind as established; the accelerated fall inside the window is not executed. A balance of capture and emission is not worked. The clause re-draws contents in encounters (block 44's caveat). No gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the sentence quoted under Premises. Block 01 (on `main`): the menus; proposed, unaudited. Blocks 44, 45, 47 and the decision record (PRs #8550, #8553, #8556, #8555, open): restated, corrected or placed.
- Named standard imports at definition level: moments of the uniform sphere (uniformity of one coordinate, Archimedes); the integral of a monomial over a simplex (Dirichlet), re-derived in the runner by term-by-term polynomial integration; the second-order remainder of Taylor; the time of fall from rest under an inverse-square acceleration.
- Reference only: Knudsen for effusion; Le Sage and the classical objections to the shadow picture; Bjerknes for sinks in a fluid.

## Review record — original author provenance
Supervisor-run block of the 12-hour campaign. Lens: blocks 45 and 47 held the bodies fixed, and the decision record carried only an estimate of what happens when they are let go. Writing the capture rate of a moving body showed first that block 45's reason for the free-streaming value was wrong (a lattice body does not present the same area to every direction), then why its value is nevertheless right in a wind (two moment identities), then that without collisions the force depends on direction. The uniform-wind control was run before the closure was written; its first 24 seeds suggested a reduction to `0.62`, which 300 seeds did not confirm (`0.78 ± 0.03`). Refuting pass (`specs/supervisor_control_block48_refuter.py`, machinery disjoint from the runner's): W1 the sphere moments by symbolic integration; W2 the deficit by enumerating every step sequence of the walk; W3 the change of variables by quadrature; W4 the collisionless coefficient by Monte Carlo over contents and paths at the shell `n = 60`; W5 the window algebra and the average `1 + 4/π` symbolically. All pass; W4 shows the approach to `|r̂|₁²` with a deviation proportional to `1/n` (times `n`: `−16`, `−24`, `+5.6`, `−6.3` towards `(1,2,2)`, `(1,1,1)`, `(28,1,1)`, `(11,16,33)`), so at the separations executed in blocks 45 and 47 the leading term alone is not accurate. Mutation census: 11 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Current review boundaries and dependencies

Conditional supplied forward hops and body model. Exact capture is weighted by |s|_1; a fully exposed site and a body balanced across axes capture the mean content of a first-harmonic homogeneous reservoir. An arbitrary plate has an anisotropic response. Independent directed walkers have the exact multinomial deficit and simplex moments; the fixed-ray large-distance shadow has the stated directional coefficient, with vector remainder O(r^-3) and coordinate-plane multiplicity. Product closure gives the expected captured-content mixture; motion, spherical inflow and accelerated-fall estimates require further closure. Constant Q/M=q1 requires the additional growing-active-site idealization N=M, not a fixed rigid footprint. No physical force or hydrodynamic limit is proved.

Historical simulations and auxiliary refuters remain on original branch head `f23fd989d6ef2290319167208ab7098cd7975f62`; their reported values are preserved but not freshly verified by this canonical runner. Companion links identify supplied mathematical models, not audited physical authority.

- [Companion model and limitations](ADMISSIBILITY_RULE_RECORDS_WITH_INERTIA_CONTENT_AS_DIRECTION_OF_TRAVEL_CONSERVED_MOMENTUM_STRUCTURELESS_EQUILIBRIUM_SOUND_SPEED_FORCES_NEED_CAPTURE_OR_EMISSION_BOUNDED_THEOREM_NOTE_2026-09-20.md)
- [Companion model and limitations](ADMISSIBILITY_RULE_THE_WIND_LAW_FLUX_THEOREMS_INVERSE_SQUARE_WIND_OF_A_CAPTURING_BODY_SECOND_ORDER_MOMENTUM_FLUX_FORCE_PROPORTIONAL_TO_PRODUCT_OF_CAPTURE_RATES_BOUNDED_THEOREM_NOTE_2026-09-20.md)
- [Companion model and limitations](ADMISSIBILITY_RULE_TRANSPARENT_BODIES_CAPTURE_RATE_IS_THE_RECORD_COUNT_AND_THE_FORCE_IS_THE_PRODUCT_OF_RECORD_COUNTS_OVER_DISTANCE_SQUARED_PREDICTED_COEFFICIENT_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion model and limitations](ADMISSIBILITY_RULE_THE_WIND_OF_A_CAPTURING_BODY_IS_NOT_ISOTROPIC_LATTICE_STREAMING_GIVES_A_VISCOUS_TERM_OF_CUBIC_SYMMETRY_DIRECTION_DEPENDENCE_DOES_NOT_DECAY_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Finite-window rule](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md)

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_free_capturing_bodies_are_carried_by_the_wind_capture_law_anisotropic_collisionless_shadow_dilution_law_of_motion_2026_09_21.py
```

Expected: `TOTAL: PASS=20 FAIL=0`.
