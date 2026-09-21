---
claim_id: admissibility_rule_the_attraction_is_tied_to_growth_a_body_in_balance_draws_no_wind_pull_proportional_to_net_uptake_growth_rate_fixed_by_the_force_coefficient_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied inertial clause of block 44 (PR #8550) and a supplied emission clause (a body in balance gives back the records it captures, through its faces, with the cosine law about the outward normal); nothing adopted. (T1) By the local conservation of number (block 45, PR #8553) the flux of the mean current out of any region of a stationary state is minus the net uptake inside it, captures minus emissions: a body in balance sends no flux through any surface around it, so its wind has no inverse-square part. (T2) For independent records, cosine-law emission gives contents the weight |s|_1 and places a record of content s on the neighbour e_k with the step frequency |s_k|/|s|_1, so emitted records are directed walks from the body; with the emission rate rho f(s) |s|_1/sqrt 3 per content (for a uniform gas: the cosine law at the capture rate) the surplus cancels the capture deficit of block 48 (PR #8558) at every site: the gas around a body in balance is uniform and no site feels a force at any distance or in any direction. A body that emits uniformly at its capture rate sends no net number through any shell and leaves the force coefficient |r|_1 (|r|_1 - 3/2) in units of rho/(4 pi sqrt 3 r^2): repulsive near the axes, attractive near the body diagonals, with angular mean 1 + 4/pi - 9/4. (T3, closure of blocks 45 and 47) the wind of a body is made by its net uptake and a body takes up momentum with its gross capture, cosine-law emission carrying no momentum on average: the push on body 2 is K_0 (Q_1 - E_1) Q_2/r^2 and the push on body 1 is K_0 (Q_2 - E_2) Q_1/r^2; action and reaction between two bodies differ and the gas carries the difference; two bodies in balance do not attract at this order. (T4) For transparent bodies q_1 = (8 pi/3)(1 - rho) G: the relative growth rate of a body is 8 pi (1 - rho)/3 times the coefficient of the pull it exerts, whatever fraction of its captures it keeps; a mass steady over T ticks pulls with a coefficient below 3/(8 pi (1 - rho) T). EXECUTED, NOT CLAIMED (sphere menu, side 96, density 0.3, gamma = 1, two solid balls of radius 3 at separation 16, 8000 ticks, two seeds per configuration; pushes towards the other body over the reference K_0 Q_1 Q_2/r^2 with gross captures): both bodies capture 0.92 +- 0.05; body 1 in balance (captures 7.24 per tick, emits 7.24) and body 2 capturing (7.84): push on the body in balance 0.75 +- 0.06, push on the capturing body 0.10 +- 0.07; both in balance 0.05 +- 0.07; in a uniform wind a pinned body of about 15 sites in balance takes up 0.85, 0.83, 0.80 (+- 0.03) of u per captured record at gamma = 0, 1, 4 against 0.97 and 0.89 for the same body capturing only, and one site in balance 0.97 +- 0.03 against 1.00 +- 0.02: the shortfall is the body's own emissions captured again. NOT claimed: forces beyond the leading order of the closure, a hydrodynamic limit, any gravitational statement, any adoption."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_the_attraction_is_tied_to_growth_a_body_in_balance_draws_no_wind_pull_proportional_to_net_uptake_2026_09_21.py
---

# The attraction is tied to growth: a body in balance draws no wind, the pull is proportional to the net uptake, and the growth rate is fixed by the force coefficient

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (an exact flux identity; an exact cancellation for independent records; closure statements for the forces; forces of bodies in balance executed, not claimed; nothing adopted or registered; unaudited)

This note works within the supplied inertial clause of block 44 and a supplied emission clause; it reports what wind and what force a body draws when it gives back what it captures; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

In blocks 45 to 48 (PRs #8553, #8554, #8556, #8558) bodies attract because they capture records, and a body that captures grows. Block 48 listed, as an open route, a body that gives back what it captures. This note works that route.

1. **No net uptake, no wind.** Records are conserved, so the flux of the mean current out of any region is minus the net uptake inside it. A body whose emissions equal its captures sends no flux through any surface around it: its wind has no inverse-square part (T1, exact).
2. **Without collisions the shadow is filled exactly.** If the body gives records back through its faces with the cosine law, emitted records are the same directed walks as the ones it removed, and at the capture rate the surplus cancels the deficit at every site: the gas around the body is uniform, and no site feels a force at any distance or in any direction. A body that emits uniformly instead leaves a residue that carries no net number, pushes near the axes and pulls near the body diagonals, and averages to about one per cent of the unbalanced pull (T2, exact for independent records).
3. **Pull and push separate.** In the closure of blocks 45 and 47 the wind of a body is made by its net uptake, while a body takes up the wind's momentum with its gross capture, the cosine-law emission carrying none on average. So a body in balance is still pushed along another body's wind, but pulls nothing: between two bodies action and reaction differ, and the gas carries the difference. Two bodies in balance do not attract at this order (T3). Executed (two solid balls of radius 3 at separation 16, pushes over the reference `K₀Q₁Q₂/r²`): both capture `0.92 ± 0.05`; one in balance, one capturing: the body in balance is pushed with `0.75 ± 0.06` and pulls the other with `0.10 ± 0.07`; both in balance `0.05 ± 0.07`.
4. **The price in one formula.** For transparent bodies `q₁ = (8π/3)(1 − ρ)G`: the relative growth rate of a body is `8π(1 − ρ)/3` times the coefficient of the pull it exerts, and the ratio is the same for a body that keeps any fraction of what it captures. A mass that is steady over `T` ticks pulls with a coefficient below `3/(8π(1 − ρ)T)` (T4).

So, within these clauses: **a body attracts in proportion to the rate at which it is growing, and a body that has stopped growing has stopped attracting.** The inverse-square attraction of blocks 45 to 47 cannot be had with steady masses.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 48 (PR #8558), N1 route 3: 'a body that does not keep what it captures ... a balance of capture and emission is not worked'; decision record (PR #8555): growth shares the rate q_1 with the attraction"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the capture mechanism's attraction is inseparable from growth, with the ratio 8 pi (1 - rho)/3; this closes the route 'balance' for the inertial-capture carrier; next: whether any clause gives the record count a long-range pull without moving records into the body (the owner's fork), and the off-axis force at small scattering rates"
conditional_surface_status: "T1 exact (the lattice divergence theorem applied to block 45's conserved current); T2 exact for independent records; T3, T4 statements in the closure of blocks 45 and 47; the forces of bodies in balance (floating point; side 96; two seeds per configuration) are in the controls and not claimed"
hypothetical_axiom_status: "the inertial clause of block 44 (its scattering re-draws contents), the capture of records by bodies, and the emission clause of this note; hypotheses only"
admitted_observation_status: "comparator only: the age of the universe in units of the smallest time defined by the constants of nature is used once, to illustrate T4's inequality; no theorem depends on it and no value of the tick is asserted"
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full) is used through "A site never carries more than one record; records are permanent." Block 01 (on `main`, proposed and unaudited) supplies the menus. Blocks 44, 45, 47 and 48 (open PRs #8550, #8553, #8556, #8558) supply the clause, the conserved current and the wind `g = √3Q/(4πr²(1 − ρ))`, the rates `q₁ = (√3/2)ρ`, `K₀ = √3/(4πρ(1 − ρ))`, `G = K₀q₁²`, the capture law and the multinomial deficit `h(x, s)`. They are restated; the runner re-derives what it uses.

- **Emission clause (supplied here).** A body in balance keeps the records it captures in a store. Every tick each stored record tries once to leave: a site of the body and one of the six directions are drawn at random; if the neighbouring site in that direction is a free site of the gas, it receives a record whose content follows the cosine law about the outward normal `n` (density proportional to `max(0, s·n)`), and the body's momentum changes by minus that content. This is the time reverse of capture through that face.
- **Net uptake.** Captures minus emissions, per tick. *Gross capture:* captures per tick. *Kept fraction* `β`: net uptake over gross capture.
- **Permanence.** A record given back is the record that was captured, or another of the body's: records are neither made nor destroyed, and a site holds at most one.

That perfectly elastic corpuscles produce no attraction in the shadow picture of Le Sage is the classical objection of Maxwell; the hydrodynamic attraction of pulsating or absorbing bodies was studied by Bjerknes. Steady attraction at the price of steady creation of matter has appeared in cosmology (Hoyle). The age of the universe in units of the time of Planck is about `8·10⁶⁰`. None is used as authority.

## Prior art and what is new

The classical objection is qualitative and concerns a continuum of corpuscles. What is new here is its exact form in the campaign's clause: the flux identity that removes the inverse-square wind of any body without net uptake; the site-by-site cancellation of the multinomial shadow by cosine-law emission, and the direction-dependent residue of uniform emission; the separation of pull (net uptake) from push (gross capture); and the ratio `8π(1 − ρ)/3` between growth rate and force coefficient.

## Exact target and obligation graph

Target: does the attraction of blocks 45 to 47 survive when bodies give back what they capture. Obligations: (O1) the wind of a body in balance; (O2) the force without collisions; (O3) the forces in the closure; (O4) the relation between growth and pull. T1–T4 discharge them at their stated levels; the control executes O3.

## Theorem T1 — no net uptake, no flux

Block 45's T1: the rate of change of the mean occupancy of a site is minus the lattice divergence of the mean current, plus what is emitted onto the site, minus what is captured from it. In a stationary state, summing over the sites of a region and cancelling the bonds inside it, the flux of the mean current out of the region is minus the net uptake of the bodies inside. For a body in balance the net uptake is zero, so the flux through every closed surface around it, and around it alone, is zero. In block 45's closure, where the wind of a body of net uptake `Q − E` is `√3(Q − E)/(4πr²(1 − ρ))`, the wind of a body in balance has no inverse-square part. ∎

## Theorem T2 — independent records: the shadow is filled

Consider one site in balance at the origin, with its six faces free, and write the statements for a content in the first octant; the others follow by reflection.

*(a) Emitted records are directed walks.* Through the face with outward normal `e_k` the cosine law gives the content `s` the weight `max(0, s·e_k)`. Summed over the six faces a content has the weight `|s|₁`, and it is placed on the neighbour `e_k` with probability `|s_k|/|s|₁ = w_k`: the first step of the directed walk of block 48's T3. From there on the record streams. So records of content `s` emitted at the rate `ε(s)` pass the site `x` at the rate `ε(s)h(x, s)`.

*(b) The cancellation.* The capture deficit of block 48 is the density `ρf(s)h(x, s)`, which passes `x` at the rate `ρf(s)(|s|₁/√3)h(x, s)`. With `ε(s) = ρf(s)|s|₁/√3`, which is the rate at which the content `s` is captured, the two cancel at every site. For a uniform gas this emission is the cosine law at the capture rate. The gas around the body is then uniform, and a capturing site anywhere takes up no net momentum.

*(c) Uniform emission.* If the body emits contents uniformly at its capture rate, `(ρ/√3)(3/2)`, the net rate at which the content `s` leaves is `(ρ/(4π√3))(3/2 − |s|₁)` per solid angle, which integrates to zero because `⟨|s|₁⟩ = 3/2`: no net number passes any shell. The force on a transparent site follows as in block 48's T3(e), with the weight `|s|₁ − 3/2` in the place of `|s|₁`: towards the body with the coefficient `|r̂|₁(|r̂|₁ − 3/2)` in units of `ρ/(4π√3 r²)`. It is `−5353/14450 ≈ −0.37` towards `(84, 12, 5)`, `11/98` towards `(2, 3, 6)`, `5/18` towards `(1, 2, 2)`, `95/242 ≈ 0.39` towards `(6, 6, 7)`; negative (a push) where `|r̂|₁ < 3/2`, positive (a pull) beyond. Its angular mean is `1 + 4/π − 9/4 ≈ 0.023`, about one per cent of the unbalanced coefficient. ∎

## Theorem T3 — the closure: pull follows net uptake, push follows gross capture

By T1 and block 45's T3 the wind of body 1 at body 2 is `u₁ = K₀(Q₁ − E₁)/r²` in units of content per record. By block 48's T2 body 2 takes up the momentum `Q₂u₁` per tick through its gross capture `Q₂`: in the closure every record that steps onto the body is a sample of the gas. (Records of the body's own emission that return to it bring back what they took; the closure neglects them, and the second control shows their share.) What it emits with the cosine law has mean content `(2/3)n` per face, and a body has as many faces with outward normal `n` as with `−n`; when its faces emit at equal rates the emitted momentum vanishes on average. Hence the push on body 2 is `K₀(Q₁ − E₁)Q₂/r²` towards body 1, and the push on body 1 is `K₀(Q₂ − E₂)Q₁/r²` towards body 2. With kept fractions `β_i = (Q_i − E_i)/Q_i` the pushes are `β₁` and `β₂` times `K₀Q₁Q₂/r²`. They are equal only when the kept fractions are; the difference is momentum carried off by the gas. Two bodies in balance do not attract at this order. ∎

The order is the first in the capture rates. At the next order a body that takes up momentum from a wind slows the gas around it, and a second body inside that disturbance is pushed along it. That effect is of higher order in the capture rates and is not computed here; the executed pull of a body in balance bounds it at the executed parameters.

## Theorem T4 — growth rate and force coefficient

For transparent bodies (block 47) `G = K₀q₁²` with `q₁ = (√3/2)ρ`, so `q₁/G = 1/(K₀q₁) = 8π(1 − ρ)/3`. A body of `N` records all of which capture grows at the relative rate `q₁` and pulls with the coefficient `G`. If it keeps only the fraction `β` of what it captures it grows at `βq₁` and, by T3, pulls with `βG`: the ratio is unchanged. Hence a body whose mass changes by less than a factor `e` in `T` ticks pulls with a coefficient below `3/(8π(1 − ρ)T)`. ∎

Comparator (not a claim): were the tick the smallest time defined by the constants of nature, a mass steady over the age of the universe, about `8·10⁶⁰` ticks, would pull with a coefficient below about `1.5·10⁻⁶²` in lattice units.

## Executed: bodies in balance against bodies that capture (not proved)

Control `specs/supervisor_control_block49_balanced.py` (sphere menu, side 96 with a reservoir at the walls, density `0.3`, `γ = 1`; two solid balls of radius 3, 123 sites each, at separation 16 along an axis; 1500 ticks of warm-up and 8000 ticks; two seeds per configuration; errors from ten blocks of a run). Pushes are towards the other body; the reference is `K₀Q₁Q₂/r²` with the gross captures.

| configuration | captures, emissions per tick | push on body 1 | push on body 2 | reference |
|---|---|---|---|---|
| both capture | `7.80, 0` and `7.79, 0` | `0.126 ± 0.012`, `0.161 ± 0.018` | `0.138 ± 0.012`, `0.151 ± 0.016` | `0.156` |
| body 1 in balance, body 2 captures | `7.24, 7.24` and `7.84, 0` | `0.095 ± 0.015`, `0.123 ± 0.011` | `0.022 ± 0.012`, `0.007 ± 0.018` | `0.146` |
| both in balance | `7.30, 7.30` and `7.28, 7.28` | `0.041 ± 0.014`, `0.006 ± 0.024` | `−0.022 ± 0.012`, `0.002 ± 0.020` | `0.136` |

Pooled over runs and, where the two bodies play the same part, over bodies: both capture `0.92 ± 0.05` of the reference; the body in balance is pushed with `0.75 ± 0.06` and pulls the capturing body with `0.10 ± 0.07`; two bodies in balance `0.05 ± 0.07`. The net uptake of a body in balance is below `0.003` per tick. Its gross capture is 7 per cent below that of a body that only captures. The push on the body in balance is below the push between capturing bodies by `0.17 ± 0.08` of the reference.

A second control (`specs/supervisor_control_block49_wind.py`; a pinned body in a uniform wind `u = 0.0994`, periodic box, `ρ = 0.3`) measures the momentum taken up minus the momentum emitted, per captured record, over `u`:

| body | `γ` | seeds | in balance | capturing only |
|---|---|---|---|---|
| about 15 sites in a ball of radius 4 | `0` | 400 | `0.85 ± 0.03` | `0.97 ± 0.03` (block 48) |
| the same | `1` | 400 | `0.83 ± 0.03` | `0.89 ± 0.03` (block 48) |
| the same | `4` | 400 | `0.80 ± 0.03` | |
| one site | `0` | 6000 | `0.97 ± 0.03` | `1.00 ± 0.02` |

One site in balance takes up the full `q₁u`. A body of several sites in balance takes up less per capture, with or without scattering: some of the records it captures are its own emissions, and those bring back what they took, not the wind's content. The reduction of the push in the two-body control is of that size.

## No-Go Discipline Gate

The note's negative sentences: a body in balance draws no inverse-square wind; for independent records a body in balance with cosine-law emission exerts no force; in the closure two bodies in balance do not attract; the pull cannot be had without growth at the rate `8π(1 − ρ)G/3`.

### N1 — Routes by which the sentences could fail
1. *Records that are not conserved* — if bodies could destroy records, net uptake would not mean growth. The axioms make records permanent; a clause in which captured records vanish contradicts the sentence used.
2. *Emission that is not the time reverse of capture* — T2(c) is one such clause; its residue has no net number, changes sign with direction and averages to one per cent of the unbalanced pull. That residue is the measure of what an emission law can leave without collisions. In the collisional closure the mean content is proportional to the number current, so by T1 no emission law gives a body without net uptake an inverse-square pull.
3. *A carrier other than records* — the flux identity is about the conserved number of records. A field that is not a conserved current of the record layer is outside this note (blocks 41 to 43 treated the record layer's equilibrium fields: no long-range channel for the record count).
4. *Higher orders* — a force of higher order in the capture rates may survive the balance of one body (the remark after T3); it is not computed, and the executed pull of a body in balance, `0.10 ± 0.07` of the reference, bounds it at the executed parameters.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
T3 and T4 rest on the closure of blocks 45 and 47 (local equilibrium; transparent bodies); T2 on independence. Declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | permanence | yes (premise; N1 route 1) |
| block 01 (`main`) | the menus | yes (premise, proposed) |
| block 45 (open PR #8553) | local conservation of number; the wind's coefficient | yes (restated) |
| blocks 47, 48 (open PRs #8556, #8558) | `q₁`, `G`; the capture law and the multinomial deficit | yes (restated) |
| block 44 (open PR #8550) | the clause; executed: emitters repel | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "no net uptake, no flux; cosine-law emission fills the shadow; uniform emission leaves `|r̂|₁(|r̂|₁ − 3/2)`; pushes `β₁`, `β₂` times `K₀Q₁Q₂/r²`; `q₁ = (8π/3)(1 − ρ)G`" | executed: the cosine law through six faces for five rational contents; the mean emitted content `(2/3)n` | executed: surplus against deficit at the 63 sites of a `4×4×4` block for three contents; the flux identity for three regions | not applicable | executed: the residual coefficients; pushes for four pairs of kept fractions; `q₁/G` at three densities | T1 the lattice divergence theorem applied to block 45's conserved current; T2 exact for independent records; T3, T4 closure statements; forces executed only |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply neither an update law, nor a capture clause, nor an emission clause. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "You chose the emission that kills the force." Reply: T1 does not depend on the emission law: whatever a body emits, without net uptake it sends no flux through any surface, and the inverse-square wind of blocks 45 to 47 is that flux. The emission law matters only for what is left, and T2(c) computes what is left for the other natural choice. Second objection: "Growth may be acceptable if it is slow." Reply: T4 gives the exchange rate: the pull per record is `3/(8π(1 − ρ))` times the relative growth rate. Whether any growth is acceptable is the owner's question; the note supplies the number.

### N8 — Cross-cycle echo
Block 41: the record count has no long-range channel in the record layer's equilibrium. Block 43: what the record layer builds arrives by diffusion. Blocks 44 to 47: a carrier with a speed gives the record count an inverse-square pull. Block 48: the pulled body is carried, not accelerated. This block: the pull is the body's growth seen from a distance. The same conservation law that protects the long range of the wind forbids it to bodies that do not grow.

## Falsifiers

- A stationary configuration with a body of zero net uptake and a non-zero flux of the mean current through a surface around it alone.
- For independent records: a site at which the surplus of cosine-law emission at the capture rate differs from the capture deficit; a direction in which the residue of uniform emission is not `|r̂|₁(|r̂|₁ − 3/2)` at large distance.
- For the executed part: a body in balance that pulls a capturing body with a force comparable to `K₀Q₁Q₂/r²` at large separation; a body in balance that is not pushed along a capturing body's wind.

## Boundaries and non-claims

One density, one scattering rate, one separation along a lattice axis, solid bodies of one size, two seeds per configuration; the pull of a body in balance is bounded, not shown to vanish (`0.10 ± 0.07` of the reference). T3 is the first order in the capture rates; the next order is named, not computed. T2 is the limit of independent records. T4 is for transparent bodies in the collisional closure. The comparator asserts no value of the tick. The clause re-draws contents in encounters (block 44's caveat). No gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the sentence quoted under Premises. Block 01 (on `main`): the menus; proposed, unaudited. Blocks 44, 45, 47, 48 (PRs #8550, #8553, #8556, #8558, open): restated or placed.
- Named standard imports at definition level: the lattice divergence theorem (Gauss); the cosine law of emission from a surface (Lambert, Knudsen) and its mean `2/3`; moments of the uniform sphere.
- Reference only: Maxwell's objection to the shadow picture of Le Sage; Bjerknes; Hoyle; the time of Planck as a comparator.

## Review record
Supervisor-run block of the 12-hour campaign. Lens: block 48 left one route open for the capture picture, a body that gives back what it captures; the conservation of records decides it before any force is computed, because the inverse-square wind is a flux. The theorems and the prediction (a body in balance is pushed but does not pull; two bodies in balance do not attract) were written before the control finished; the control agrees, with a push on the body in balance somewhat below the closure's value. That shortfall was first recorded as unexplained and the gates were started; a uniform-wind control run meanwhile showed it without scattering as well, which refuted the supervisor's first guess (the emitted records diluting the wind through collisions); a one-site control then showed no shortfall, which identifies it as the body capturing its own emissions again. The gates were stopped and the note corrected before it was opened. Refuting pass (`specs/supervisor_control_block49_refuter.py`, machinery disjoint from the runner's): W1 the mean `2/3` of cosine-law emission, `⟨|s|₁⟩ = 3/2` and the mean `1 + 4/π − 9/4` of the residue by symbolic integration; W2 the stationary transport equation with a capturing and emitting site solved site by site in exact arithmetic (uniform density with emission, the capture deficit without); W3 emitted records by enumerating every step sequence; W4 the residue of uniform emission by quadrature at `n = 60, 240, 960`; W5 the ratio `q₁/G` and the comparator arithmetic. All pass. Mutation census: 8 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_attraction_is_tied_to_growth_a_body_in_balance_draws_no_wind_pull_proportional_to_net_uptake_2026_09_21.py
```

Expected: `TOTAL: PASS=14 FAIL=0`.
