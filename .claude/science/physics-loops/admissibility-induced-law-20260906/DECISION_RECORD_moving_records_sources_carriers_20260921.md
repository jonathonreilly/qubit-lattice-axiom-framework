# Moving records, sources and carriers — state of knowledge for the owner (blocks 39–46; 2026-09-21)

**What this is.** One page on what the campaign established under the owner's reading that records move, written at the end of the 12-hour campaign of 2026-09-20/21. Nothing here is adopted; every block is an open hand-off PR against `main`; PR numbers are evidence addresses, not status. Author checks only; no independent review has taken place on any of it.

## What is established (exact unless marked executed)

| # | Statement | Evidence address |
|---|---|---|
| 1 | With records that move by pair weights, the static law on the occupied set is the equilibrium; the overall scale `c` of the weights is a constant the rule cannot see; reflection positivity holds iff `c ≥ c₀ = 6/(p+q+4r)`. | block 39, #8530 |
| 2 | At `c = c₀` the pair weight is the rule's likelihood ratio, an empty site is a record of unknown content bond by bond, and records do not bind on any window without a cycle. | block 40, #8546 |
| 3 | A source is a record: the only local additive invariant density is the occupancy. In the records-only law nothing acts across empty sites; through a medium the field of a held record is short-ranged; the content channel's charge is the content vector and the mass carries none; the transit Laplacian is sourced by production. | block 41, #8547 |
| 4 | If an unformed site's odds count as a condition, influence crosses empty sites: contents interact, masses do not (summed form); the self-consistent odds obey a screened lattice field equation, massless exactly on `5p = 7q + 4r` ((3,1,2) lies on it); with "no record" as a possibility the mass channel has strength `∝ c/c₀ − 1`, zero at `c₀`; records enter as boundary values, so a body's strength is its capacity. | block 42, #8548 |
| 5 | Both of those fields are set up by a random walk: a distance `R` costs of the order of `R²` ticks, mass term or not (`a ≥ R²/(2cT)` with the lattice unit left free). | block 43, #8549 |
| 6 | If a record travels along its content (the six contents are the six lattice directions) it has inertia: number and momentum conserved event by event; structureless equilibrium; pressure exactly `ρ/3`; waves at `c² = (1−ρ)/3` (executed within 4 %; sphere menu `(1−ρ)/9`, within 1 %); no force on a body that neither captures nor emits records. | block 44, #8550 |
| 7 | The wind law: local conservation with explicit fluxes; a body capturing `Q` per tick draws an inverse-square inflow whose coefficient follows from the exact current (executed: 0.974–1.003 of the prediction, no free parameter, density flat); two capturing bodies attract with `F = K Q₁Q₂/r²`, symmetric in the two bodies (executed), `K` equal to the free-streaming value at low density and `0.57` of it at density `0.75`; the second-order (inviscid) value with its sign change at `ρ = 3/5` does not apply to the executed viscous flows — a supervisor expectation refuted by a batch designed to confirm it. | block 45, #8553 |
| 7a | The wind has a potential: a circulation-free current whose divergence is fixed by the capture rates is unique up to constants and is the lattice gradient of `Φ = −G * (Q − mean Q)` (exact rank); the wind built up from rest is circulation-free; the gas has radiation's equation of state at every density (pressure = density × speed / 3) and a conserved tensor that is symmetric only in the dilute limit. | block 46, #8554 |
| 8 | Executed after block 45 (campaign controls, not in a note): for dilute bodies the capture rate **is** the record count — `Q/N = 0.236, 0.241, 0.234, 0.221` for `N = 3, 9, 15, 45` sites in a ball of radius 6 (kinetic single-site value `0.251`), falling to `0.188, 0.135` at `N = 87, 180` as the ball becomes opaque. Pairs of such bodies at separation 16 (nine runs): `F/(N₁N₂) = (1.44 ± 0.10)·10⁻⁴` for the most dilute pairs (`N ≈ 15–29`), `1.03·10⁻⁴` for a light body against a heavier one and `0.98·10⁻⁴` at `N ≈ 35–48`, against the parameter-free value `K₀ q₁²/r² = 1.45·10⁻⁴` (`K₀` the free-streaming coefficient of block 45, `q₁ = 0.236` the executed capture rate of one site); `K → 0.675 ± 0.04` against `K₀ = 0.67`. **For bodies transparent to the gas the force is the product of the record counts over the square of the distance, with the coefficient predicted**; it falls below that as bodies become opaque. | scratch controls; queued on `ai/probes` |
| 9 | Executed: without the scattering that re-draws contents there is no sound — six axes: two thirds of a density modulation never moves; sphere menu: it dephases without oscillating. Waves need momentum exchange. | scratch control |

## What the gravity lane on `main` has, and the correspondence
The weak-field packet is a **supplied** quadratic action with `|ψ|²` as source; its own cited note says the field equation "is supplied to the loop … it does not derive the operator from the framework axioms". The record-pair source note lists three missing pieces: a Record-local source, a local conservation/attachment law with cadence and zero mode, an absolute unit. The axioms memo lists update laws and record-production dynamics as open gates: the framework has no committed dynamics in either layer.

In the inertial clause each of the packet's three statements has a counterpart with a reason behind it (a structural correspondence, not a gravitational claim):

| weak-field packet (supplied) | inertial record gas (within a supplied clause) |
|---|---|
| field operator `H = −Δ_lat`, `φ = G₀ P₀ ρ` | records are permanent, so the stationary inflow is divergence-free away from bodies: its potential solves the lattice Poisson equation with the capture rates as sources (exact flux theorem; irrotational flow assumed) |
| source readout: the unique local positive additive density | the capture rate, positive and additive; equal to `0.24 ×` the record count for bodies transparent to the gas (executed; block 41's forced source), to the surface for opaque ones |
| test response `F = m ∇φ`, bilinear in the two sources | a capturing body takes up the momentum of the records it captures: `F = K Q₁Q₂/r²`, bilinear and symmetric (executed) |
| zero mode projected out (`P₀`) | the uniform part of the density, which only grows or shrinks as a whole |

## The forks that are the owner's
1. **Glue or the neutral scale.** `c = c₀` switches off every first-order, content-blind channel through the odds; universal attraction through overlapping neighbourhoods needs `c > c₀` (then it is screened off tuned surfaces).
2. **Is an unformed site's probability distribution a condition for its neighbours?** (block 42.)
3. **Do records have inertia?** (block 44.) It costs no new object, but
4. **may an encounter re-draw a record's content?** Waves and momentum exchange need it (row 9); the Record axiom says a record "locks exactly one admissible local possibility".
5. **Does matter capture records, and is it transparent to them?** The executed attraction needs capture; its charge is the record count only for transparent bodies. Captured records make bodies grow; a moving body is dragged by the same coupling that attracts it (the classical objections to shadow and sink pictures; not answered here).
6. The inertial clause does not use the rule's weights `(p, q, r)` at all yet; a clause joining inertia with the rule is open.

## The cost of the capture picture, in one inequality (supervisor's estimate; not a result)
A capturing site takes up a record of the gas about every `1/(0.87ρ)` ticks (executed: `0.24` per tick at `ρ = 0.29`). That one rate is both the rate at which a body grows and the rate at which its motion is dragged towards the local wind. The attraction scales as `ρ N₁N₂/r²`, so the time to fall a distance `r` towards a body of `N₁` records is about `5 √(ρr³/N₁)` growth-and-drag times: attraction wins only when the gas inside the orbit weighs much less than the central body (roughly `(4π/3)ρr³ ≪ N₁/6`). The executed runs are on the wrong side of this (`ρr³ ≈ 1200` against `N ≈ 45–500`): right for measuring the force, wrong for orbits. The classical objections to shadow and sink pictures appear here as one condition on how dilute the gas must be.

## How the inertial gas meets the owner's picture
The owner asked whether the probability fields at sites could pull records onto them, with the overlap of two neighbourhoods as the attraction. In the inertial gas the local distribution of contents near a capturing body is tilted towards the body — that tilt *is* the wind — and it falls as the inverse square of the distance because records are never destroyed. A second body standing in that tilted field is pulled along it.

## Supervisor's recommendation (not a decision)
Decide fork 4 first: it gates both the odds reading and inertia. If encounters may re-draw contents, the inertial gas is the one record-layer candidate with a carrier that has a speed, a source that adds and a Laplacian protected by permanence; its open questions are quantitative (drag against attraction; growth by capture; a clause that includes the rule's weights) and are loaded on `ai/probes`. If not, the record layer supplies the source (the record count) and nothing else, and the carrier has to come from a dynamics clause for the amplitude layer, which the axioms do not yet contain.
