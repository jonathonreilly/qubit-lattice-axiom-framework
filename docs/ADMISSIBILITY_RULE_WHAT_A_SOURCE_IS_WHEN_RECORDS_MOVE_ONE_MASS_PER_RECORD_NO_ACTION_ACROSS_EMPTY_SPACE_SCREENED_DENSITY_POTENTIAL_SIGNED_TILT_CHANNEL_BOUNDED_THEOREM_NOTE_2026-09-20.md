---
claim_id: admissibility_rule_what_a_source_is_when_records_move_one_mass_per_record_no_action_across_empty_space_screened_density_potential_signed_tilt_channel_bounded_theorem_note_2026-09-20
claim_type: bounded_theorem
claim_scope: "CONDITIONAL on the moving-records reading of block 39 (PR #8530), which is not in the axioms memo and is not adopted. For the six-axis rule with the declared isotropic pair weight omega = (p, q, r) and the law with vacancies (a bond between two records weighs c omega, a bond with an empty end weighs 1, a record weighs z), on finite windows: (T1) a local additive one-site density that vanishes on an empty site and is invariant under the rotations acting on contents is a constant times the occupancy, because the 24 proper rotations of the cube act transitively on the six axes: every record has the same mass and the mass of a cluster is its number of records; (T2) the weight of an arrangement is the product of the weights of its occupied components, at every binding scale, so sets of records separated by empty sites do not interact and their contents are independent given the occupancy; (T3) the mean occupancy around a held record exceeds the density by rho (g(r) - 1), g the occupancy pair correlation; on the periodic 2 x 8 ladder at (12,1,2), the neutral scale and z = 1/12, g - 1 is 161179/10^7, 12151/10^7, 1249/10^7, 502/10^7 at r = 1..4, and on a window without a cycle it is exactly zero at the neutral scale; (T4) in every law invariant under the rotation of all contents together the mean content vector at y given the content a at x is a coefficient times the vector of a, the same coefficient for the six contents (24/433 across the occupied plaquette at (3,1,2)), and it is zero when the content at x is not read: the charge of the content channel is the content vector, odd and of zero mean, and the occupancy carries none; in the declared quadratic model of an ordered medium a held tilt a has the mean field a G(y)/G(0) and two held tilts interact by -kappa a b G(r)/(G(0)^2 - G(r)^2), G the lattice Green function: like tilts attract and opposite tilts repel; (T5) under symmetric transit with one record per site the generator applied to the occupancy of a site is the lattice Laplacian of the occupancy (the exclusion cancels in the mean), so with a production profile j held fixed the mean occupancy is a uniform part growing at the rate mean j plus the stationary field G * (j - mean j)/kappa; at the neutral scale the formation rate z Z_x of block 39 next to records of independent uniform contents equals the rate in the void on average, exactly, and next to k agreeing records it is larger by 6^(k-1) (p^k + q^k + 4 r^k)/(p + q + 4r)^k >= 1 (13/12 and 5/4 at (3,1,2), 46/21 and 2348/343 at (12,1,2), k = 2, 3). EXECUTED, NOT CLAIMED: on the cubic lattice (side 16, one seed) the fitted range of the field of a held record is about one lattice step or less at every point tried away from the clumping onset. NOT claimed: any attraction between masses at long range, any force law, any identification of the production field with a gravitational potential, the infinite lattice, direction-dependent rules (for which the symmetry part of T4 fails: refuter W4), any adoption."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_what_a_source_is_when_records_move_one_mass_per_record_screened_density_signed_tilt_2026_09_20.py
---

# What a source is when records move: one mass per record, no action across empty sites, a field of short range for the density, a signed tilt as the charge of the long-range channel, and a transit Laplacian whose source is production

**Date:** 2026-09-20
**Type:** bounded_theorem
**Status:** bounded-support (exact on finite windows under a supplied reading; the ranges on the cubic lattice executed, not claimed; nothing adopted or registered; unaudited)

This note works under the moving-records reading of block 39 and defines a source by the requirements the gravity lane already states; it finds no universal one-over-distance attraction in the equilibrium of moving records, and it adopts nothing.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The owner asked (2026-09-20): "ok lets define what a source is and go from there." The gravity lane on `main` already says what a source has to be: a density that is local, positive, additive and covariant, entering a field equation whose operator is minus the lattice Laplacian. This note applies those requirements to records that move and follows the consequences.

1. **The definition is forced.** The symmetry that acts on contents carries every content to every other, so a density of that kind cannot tell contents apart: it is a constant times "is there a record here". Every record has the same mass; the mass of a lump is its number of records.
2. **Empty sites carry nothing.** Two sets of records with an empty site between them weigh exactly the product of their separate weights, at any binding scale, and their contents are independent. In the equilibrium of moving records there is no action across empty sites, at any distance.
3. **Through a medium of records the field of a mass is of short range.** Holding a record raises the mean occupancy nearby by the pair correlation. On the ladder that excess is computed exactly and falls about tenfold per step; on windows without a cycle at the neutral scale it is exactly zero; on the cubic lattice the executed range is about one lattice step or less away from the clumping onset.
4. **The long-range channel carries the wrong charge.** The field that does reach far, in a medium whose contents are ordered, is the tilt of the contents. Exactly, by the symmetry of the declared rule, what a record puts into that channel is its content vector: it changes sign with the content and vanishes for a record whose content is not read. The mass puts in nothing. In the quadratic model two held tilts interact at one-over-distance, like tilts attracting and opposite tilts repelling.
5. **There is one Laplacian that the mass does enter: transit itself.** With one record per site and symmetric hops, the mean number of records obeys the lattice heat equation exactly, so a place that produces records at a steady excess rate is surrounded by a stationary halo given by the lattice Green function, the operator of the gravity lane's field equation. Its source is the production of records, not their presence; in equilibrium it is zero. At the neutral scale the formation rate of block 39 next to records of unrelated contents equals the rate in the void on average, and next to two or more records that agree it is larger: matter whose records agree is a net source of records (a single record, or a flat face of a lump, changes nothing: the excess needs an empty site that touches two or more agreeing records).

So: with mass defined the only way the symmetry allows, the equilibrium of moving records holds no one-over-distance attraction between masses. The places where one could still come from are named under Boundaries.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "owner, 2026-09-20: 'ok lets define what a source is and go from there'; the gravity lane's open item on main: 'identify the branchwise Record source and supply an absolute source/response/unit law'"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the source is defined (record count) and its three channels are worked out: nothing across empty sites, a field of short range through a medium, no charge in the tilt channel; the transit Laplacian is sourced by production. Next: the halo around a lump of agreeing records under formation and transit (profile, strength against the lump's record count), and what a second lump does inside it (accretion on the near side; drift where records bind); both are loaded on ai/probes as computations"
conditional_surface_status: "T1, T2, the symmetry part of T4 and the closure of T5 proved for every finite window and every positive six-axis triple of the declared isotropic class; the quadratic model of T4 is a declared stand-in; the executed ranges (one seed, side 16, 3000 sweeps) are in the controls and not claimed"
hypothetical_axiom_status: "the moving-records clause of block 39; where the neutral scale is used, the value c = c_0 of block 40; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full) is used through "No possibility is privileged.", "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." and "A site with no record cannot be read.". Block 01 (on `main`, proposed and unaudited) supplies the rule as a product of pair weights whose pair weight is symmetric and isotropic with orbit values `(p, q, r)`. Block 39 (open PR #8530) supplies the moving-records reading, the law with vacancies, pair-weight transit and the formation rate; block 40 (open PR #8546) the neutral scale and the law on windows without a cycle. The requirements on a source are read from the gravity lane's weak-field bridge note on `main` (`GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11`: "local, diagonal, positive, phase-invariant quadratic density", field operator `−Δ_lat`); that note is a statement of requirements here, not a premise.

- **The law with vacancies.** A site is empty or carries a record; a record weighs `z`; a bond between two records weighs `W = cω`; a bond with an empty end weighs `1`. `n_x ∈ {0, 1}` is the occupancy, `s_x` the content, `e(s)` its unit vector.
- **Internal rotations.** A proper rotation of the cube applied to every content, sites fixed. The declared pair weight is invariant: `ω(Ra, Rb) = ω(a, b)`.
- **Pair correlation.** `g(x, y) = ⟨n_x n_y⟩/(⟨n_x⟩⟨n_y⟩)`.
- **Quadratic model of an ordered medium** (a declared stand-in, as in blocks 26, 29, 34, 35): a real field `θ` on the torus with weight `exp(−(κ/2) Σ_bonds (θ_x − θ_y)²)`, zero mode removed; covariance `G/κ`, `G` the Green function of `−Δ_lat`.
- **Symmetric transit.** Each record hops to each empty neighbour at rate `κ`, whatever surrounds it. Block 39's pair-weight transit coincides with it whenever the moving record touches no other record before or after the move.
- **Formation rate** (block 39, T4): `zZ_x`, `Z_x = Σ_a Π_{y∼x, occupied} W(a, s_y)`. **Neutral scale** (block 40): `c₀ = 6/(p + q + 4r)`, at which every row of `W` sums to `6`.

Laws of this kind are those of Gibbs; the field equation `−Δu = j` is that of Poisson; a force of short range of the form found in T3 is of the type of Yukawa, and the structure-factor fit used in the controls is that of Ornstein and Zernike; the massless tilt modes of an ordered medium with a continuous symmetry are those of Goldstone; an attraction between neutral inclusions carried by fluctuations of such modes is of the type of Casimir and of van der Waals; one record per site with symmetric hops is the symmetric exclusion process, whose closed equation for the mean is classical. None is used as authority.

## Prior art and what is new

Blocks 19, 29 and 35 located a Green-function kernel in the tilt channel of ordered sphere laws and measured its strength; none of them asked what charge a record carries in that channel. Block 39 introduced moving records and the law with vacancies; block 40 showed that at the neutral scale records do not bind without a cycle. The gravity lane on `main` keeps as its open item the identification of the record source. Probe-fleet referees on the light-cone law (`ai/probes`, problem two-source-interaction) found the same sign structure for two pinned records there, and that pinned means do not superpose exactly; T4's sentence on two held tilts is stated accordingly. What is new here: the definition of the source forced by the symmetry (T1); the exact absence of any action across empty sites (T2); the identification of the field of a held record with the pair correlation and its exact short range on the ladder (T3); the symmetry lemma that the content channel's charge is the content vector, of zero mean, with the occupancy carrying none, together with the sign structure of the long-range interaction in the quadratic model (T4); and the observation that the gravity lane's operator acts on the mass density through transit, with production as its source, with the exact production excess at the neutral scale (T5). The closed equation for the mean under exclusion is classical and is re-proved at scope in two lines.

## Exact target and obligation graph

Target: say what a source is for records that move, and find every channel through which one source can act on another in the laws the campaign has. Obligations: (O1) the definition; (O2) empty space; (O3) the density channel; (O4) the content channel; (O5) the transit channel. T1–T5 discharge O1–O5 at the stated scope; the controls execute O3 on the cubic lattice.

## Theorem T1 — one mass per record

Let `m` assign a number `m(s) ≥ 0` to a record of content `s` and `0` to an empty site, and let the mass of a region be the sum over its sites (local, additive, non-negative). If `m` is invariant under the rotations acting on contents, then `m(s) = m(Rs)` for the 24 proper rotations `R` of the cube; these carry any axis to any other, so `m` is constant on the six contents: `m = m₀ n_x`. The mass of a set of records is `m₀` times its number of records, and `m₀` is a unit. The same argument on the sphere menu uses the transitivity of the rotation group on the sphere. ∎

This is the record-layer counterpart of the gravity lane's source readout: there the requirements single out one density of the amplitude, here they single out the occupancy.

## Theorem T2 — no action across empty sites

In the law with vacancies the weight of an arrangement is `z^{|η|}` times the product over bonds with both ends occupied. A bond with an empty end contributes `1`, so if the occupied set splits into components `A₁, …, A_m` with no bond between different components, the weight is `Π_i w(A_i)` with `w(A)` the weight of `A` alone: summed over contents, `Π_i Σ w(A_i)`, and given the occupancy the contents of different components are independent. Nothing in the weight depends on the distance between components or on the scale `c`. Pair-weight transit and formation at rate `zZ_x` read only a site's neighbours, so they too are blind to anything beyond an empty site. ∎

On a line at `(12,1,2)` two clusters of `2` and `3` records weigh `w(A)w(B)` at gaps of `1` to `4` empty sites at both scales tried; when they touch, the weight is multiplied by `1` at the neutral scale (no cycle) and by `7/2 = c/c₀` at scale `1`.

## Theorem T3 — the field of a held record is the pair correlation

`⟨n_y | n_x = 1⟩ − ⟨n_y⟩ = ⟨n_y⟩ (g(x, y) − 1)`, by the definition of `g`. This is the whole effect on the density at `y` of holding one more unit of mass at `x`, and the mean force between two records held at `x` and `y` derives from the potential `−log g(x, y)` in units of the temperature of the law.

On the periodic `2 × 8` ladder at `(12,1,2)`, the neutral scale and `z = 1/12` (density `0.338`), the exact values of `g − 1` along a leg are `161179/10⁷, 12151/10⁷, 1249/10⁷, 502/10⁷` at `r = 1, 2, 3, 4`, each rounded down: positive (an attraction) and falling by about a factor of ten per step until the periodic image is met at `r = 4`. On a window without a cycle at the neutral scale `g ≡ 1` exactly (block 40, T2): there the field of a held record is zero, and all of it on the ladder comes from the loops. At scale `1` on the open line of five sites `Cov(n₀, n₁) = 0.02511…` and positive at every distance. ∎

## Theorem T4 — the charge of the content channel is the content vector; the mass carries none

**Symmetry lemma.** Let a law on arrangements be invariant under the internal rotations (the static law and the law with vacancies of the declared class are, and so is every formation law built from the declared rule along an order that does not read contents; an order that reads contents must read them invariantly for the lemma to apply). Fix sites `x ≠ y` and a content `a`. The vector `F(a) = ⟨n_y e(s_y) | s_x = a⟩` satisfies `F(Ra) = R F(a)`. The rotations about the axis of `a` fix `a`, so they fix `F(a)`, which therefore lies along `e(a)`: `F(a) = f(a) e(a)`. A rotation carrying `a` to `b` gives `f(b) = f(a)`. Hence `F(a) = f · e(a)` with one coefficient `f = f(x, y)` for the six contents (for the sphere menu, for every content): the field a record puts into the content channel is its own content vector times a number. It is odd, `F(−a) = −F(a)`, and summing over the contents with their equal weights, `⟨n_y e(s_y) | n_x = 1⟩ = 0`: a record whose content is not read, that is a unit of mass as such, puts nothing into the content channel. In a state ordered along one axis the same argument with the rotations about that axis shows that the occupancy puts nothing into the components of the content transverse to the order. ∎

Across the occupied plaquette at `(3,1,2)` the coefficient is `24/433`. The lemma uses the isotropy of the declared pair weight; for a rule whose weights depend on the direction of the bond only the rotations acting on sites and contents together are symmetries, and the lemma fails: refuter W4 exhibits a radial content field `(−53/391, 0, 0)` next to a record of unread content.

**The long-range part, in the quadratic model.** For the field `θ` with covariance `G/κ`, holding `θ_x = a` gives the mean field `⟨θ_y⟩ = a G(y − x)/G(0)`, linear in `a`. Holding `θ_x = a` and `θ_y = b` costs `(κ/2) (a, b) M^{-1} (a, b)ᵀ` with `M` the `2 × 2` matrix of `G(0)` and `G(r)`; the part that depends on both is `−κ a b G(r)/(G(0)² − G(r)²)`. Since `G(r) > 0` falls off as one-over-distance on `Z³`, like tilts attract and opposite tilts repel at one-over-distance. The mean field of two held tilts is linear in `(a, b)`, each term being the field of one tilt with the other site held at zero; it is not the sum of the two one-tilt fields, because holding a site also constrains it, and the difference vanishes as `G(r)/G(0) → 0`: in the far field the tilts add as signed quantities. On the `4³` and `6³` tori `G(0) > G(1) > G(2)`, `G(1) > 0`, and the signs are as stated. ∎

Together: the only channel of the record layer with a one-over-distance kernel has a signed charge of zero mean, and the mass of T1 has no charge in it. By the same symmetry a neutral inclusion can couple to the tilt field only through rotation-invariant combinations, which start at second order in the field; the interaction this gives between two inclusions is of second order in the coupling and is not computed here (queued). The quadratic model stands for the ordered sphere medium (blocks 19, 29); for the six-axis menu, whose symmetry is discrete, the campaign has found no kernel of long range at all.

## Theorem T5 — the transit Laplacian is sourced by production

**Closure.** Under symmetric transit with one record per site the rate of change of `n_x` is `κ Σ_{y∼x} [n_y(1 − n_x) − n_x(1 − n_y)] = κ Σ_{y∼x} (n_y − n_x)`: the products cancel, so for every law of the arrangement `d⟨n_x⟩/dt = κ (Δ_lat⟨n⟩)_x`. With formation at an empty site at rate `J_x(η)` the equation is `d⟨n_x⟩/dt = κ (Δ_lat⟨n⟩)_x + j_x`, `j_x = ⟨J_x (1 − n_x)⟩`. ∎

**Stationary field.** On the torus `−Δ_lat G = δ₀ − 1/L³` (all 64 sites of the `4³` torus in the runner). With `j` held fixed in time every non-zero mode of `⟨n⟩` relaxes to the value given by `u = G * (j − j̄)/κ`, while the uniform part grows at the rate `j̄`. The field of a steady excess of production is the lattice Green function, the kernel of the gravity lane's field equation `−Δ_lat φ = ρ`, with the production rate in the place of `ρ`. Without net production, `j = j̄`, it vanishes. ∎

**Which records produce.** At the neutral scale every row of `W` sums to `6`, so next to `k` records of independent uniform contents the mean of `Z_x` is `Σ_a Π_j (Σ_b W(a, b)/6) = 6`: the formation rate equals the rate in the void on average, exactly, for every `k`. Next to `k` agreeing records `Z_x/6 = 6^{k−1}(p^k + q^k + 4r^k)/(p + q + 4r)^k`, which is at least `1` by the inequality between the mean of `k`-th powers and the `k`-th power of the mean, with equality only for `p = q = r`: `13/12` and `5/4` at `(3,1,2)`, `46/21` and `2348/343` at `(12,1,2)`, for `k = 2, 3`. Records that agree are a net source of records; records that do not are not. ∎

For pair-weight transit the closure holds on every arrangement in which the moving record touches no other record before or after its move, hence in the dilute far field of a lump; where records touch, the correction terms are pair correlations of adjacent records (refuter W5 shows that they do not vanish).

## Executed: the range of the field of a held record on the cubic lattice (not proved)

Control `specs/supervisor_control_block41_screening.py` (the block 39 simulator with the occupancy structure factor accumulated; side `16`, `3000` sweeps, seed `7`; fit of `1/S(k)` against `E(k) = 6 − 2Σcos k_i` on the 170 modes with `E < 1.6`, range `ξ` from `1/S = (1/S₀)(1 + ξ²E)`). Independent occupancies at fixed number give `S = ρ(1 − ρ)`, that is `0.21` at density `0.3`.

| rule | scale | density | lowest shell `S` | `ξ` (lattice steps) |
|---|---|---|---|---|
| `(4,1,2)` | neutral | `0.3` | `0.212` | flat: no range resolved |
| `(8,1,2)` | neutral | `0.3` | `0.263` | `0.19` |
| `(10,1,2)` | neutral | `0.3` | `0.310` | `0.35` |
| `(3,1,2)` | `1` | `0.3` | `1.18` | `0.79` |
| `(4,1,2)` | `1` | `0.3` | `1.63` | `1.1` |
| one content, `c = 2.0` | — | `0.5` | `1.04` | `0.97` |
| one content, `c = 2.4` | — | `0.5` | `7.26` | fit fails: `1/S` not linear in `E` |

Away from the clumping onset the range is about one lattice step or less; at the neutral scale and moderate preference the occupancy is indistinguishable from independent. The last row sits next to the one-content clumping onset located in block 39 (`2.43`–`2.7`): there the small-`k` structure factor grows and the fit form no longer applies. One seed, one side; nothing here is claimed.

## No-Go Discipline Gate

The note's negative sentences are T2 (no action across empty sites), the zero-charge part of T4, and the summary sentence that the equilibrium of moving records holds no one-over-distance attraction between masses among the channels examined. The gate is applied to them.

### N1 — Routes by which the sentences could fail
1. *Direction-dependent rules* — a pair weight that depends on the direction of the bond, or block 01's reading (ii) in which an empty neighbour contributes a direction-dependent factor to the record beside it, breaks the internal symmetry; then a record of unread content carries a radial content field (refuter W4) and the zero-charge sentence of T4 fails. T2 survives reading (ii): the factor of an empty neighbour belongs to the one record beside it, so the weight still factorizes over occupied components (refuter W7), though the weight of a component then depends on its shape. Both are outside the declared class and the declared law with vacancies.
2. *The amplitude layer* — T2 is about the record layer's law. The axioms say an empty site cannot be read, not that nothing is there; a field of the amplitude layer across empty sites is the gravity lane's own object and is untouched by this note.
3. *The clumping onset* — near the onset the small-`k` structure factor grows (the last executed row) and the range is not short; T3's short range is a statement away from it.
4. *Out of equilibrium* — T5 shows a Green-function field whenever production is not uniform; T2–T4 are statements about equilibrium laws and about symmetry.
5. *Common tilt* — if all matter carried the same tilt against an ordered medium, the tilt channel would attract universally; the axioms' "No possibility is privileged." gives no such tilt, and the note claims nothing about it.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond block 39's reading and law and block 40's scale, declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the three sentences behind the symmetry and the reading | yes (premise) |
| block 01 (`main`) | the rule as a product of isotropic pair weights | yes (premise, proposed) |
| block 39 (open PR #8530) | the reading, the law with vacancies, pair-weight transit, the rate `zZ_x` | yes (restated) |
| block 40 (open PR #8546) | the neutral scale; the law on windows without a cycle | yes for the neutral-scale sentences (restated) |
| the gravity lane's weak-field bridge note (`main`) | the requirements on a source; the operator `−Δ_lat` | statement of requirements, not a premise |
| blocks 19, 29, 35 (open PRs #8153, #8173, #8180) | the Green-function kernel of the tilt channel | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "mass is the record count; nothing acts across empty sites; the field of a held record is of short range; the content channel's charge is the content vector and the mass carries none; the transit Laplacian is sourced by production" | executed: the 24 rotations and the orbit of an axis; the formation rate next to one, two and three records of every content | executed: two clusters at gaps of 1 to 4 and touching, two scales; independence of contents; closure on all 256 arrangements of the cube graph | executed: the Green function on the `4³` and `6³` tori; two held tilts; the field equation at all 64 sites | executed: the ladder and the open line; the content field on the occupied plaquette | T1, T2, the symmetry part of T4 and the closure of T5 hold on every finite window; T3 exact on the ladder and executed on the cubic lattice; no claim about the infinite lattice |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply neither a record source nor a coupling of the occupancy to a massless field. The production field of T5 is not registered and not proposed as a primitive.

### N7 — Steelman
Hostile reviewer: "You defined mass so that it cannot gravitate and then reported that it does not." Reply: the definition is not chosen; it is the only local additive density the symmetry allows (T1), and it is the one the gravity lane's own requirements pick. The absence of action across empty sites is a property of the law with vacancies, exact at any scale (T2), and the zero charge in the tilt channel is a symmetry statement about the declared rule (T4). The note does not say masses cannot attract: it lists where an attraction could still come from, and T5 exhibits the one Laplacian the mass does enter.

### N8 — Cross-cycle echo
Block 40's tree law returns as the exact vanishing of the field of a held record on windows without a cycle; block 19's and block 35's kernel returns as the tilt channel, now with its charge identified; block 39's formation rate returns as the production profile of T5; block 22's `G(0)` is the self-term of T4's two-tilt energy.

## Falsifiers

- A window and a scale at which two components separated by an empty site have a weight different from the product (against T2).
- A law of the declared class and a pair of sites with `⟨n_y e(s_y) | n_x = 1⟩ ≠ 0`, or with `F(a)` not along `e(a)` (against T4's lemma).
- An arrangement on which symmetric transit with one record per site gives a rate of change of `n_x` different from the Laplacian (against T5's closure).
- A triple at which the mean formation rate at the neutral scale next to independent uniform records differs from the rate in the void.
- For the executed table: a run away from the clumping onset with a fitted range of several lattice steps.

## Boundaries and non-claims

No attraction between masses at long range is claimed or excluded beyond the channels examined. Where one could still come from: (a) the amplitude layer, where the gravity lane's field lives and where the source is a density of the amplitude, with the occupancy of T1 as its record-layer counterpart; (b) the transit field of T5, which needs net production and whose action on a second lump (accretion on the near side, drift where records bind) is not derived here and is not a force law; (c) the density channel at the clumping onset, a tuned place; (d) a common tilt of all matter against an ordered medium, which nothing in the axioms supplies; (e) direction-dependent rules outside the declared class. The quadratic model is a stand-in for the ordered sphere medium, not the law itself. The executed table is one seed on one side. No statement is made about the infinite lattice. Nothing is adopted; the moving-records clause and the neutral scale remain proposals.

## Imports
- `minimal_axioms`: the sentences quoted under Premises. Block 01 (on `main`): the rule; proposed, unaudited. Blocks 39 and 40 (PRs #8530, #8546, open): restated. The gravity lane's weak-field bridge note on `main`: the requirements on a source, as a statement of requirements. Blocks 19, 22, 29, 35 as evidence addresses.
- Named standard imports at definition level: the conditional mean and the quadratic form of a centred Gaussian vector given two of its components; the power-mean inequality (for `k = 2`, that of Cauchy and Schwarz); the one-over-distance decay of the Green function of the lattice Laplacian on `Z³`, used only in words.
- Reference only: Poisson for the field equation; Yukawa, Ornstein and Zernike for the form of a field of short range; Goldstone for the massless tilt modes; Casimir and van der Waals for fluctuation-carried attraction; the symmetric exclusion process for the closed equation of the mean.

## Review record
Supervisor-run block (owner 2026-09-20: "ok lets define what a source is and go from there"). Lens: the gravity lane on `main` already lists what a source must be, so the definition is an application of its requirements to the record layer, and the work is in finding what such a source can act through. Primary: T1–T4 and the ladder. During the refuting pass the supervisor added the symmetry lemma in its general form (first draft: the quadratic model only), found its limit (direction-dependent rules, W4), and added T5 after asking where the lane's operator could act on the occupancy at all. Refuting pass (`specs/supervisor_control_block41_refuter.py`, machinery disjoint from the runner's: site-level enumeration on general graphs): W1 a block with a cycle and a cluster across an empty column at three scales; W2 the periodic `2 × 4` ladder by enumeration of all `7⁸` site states against the transfer matrix, exact equality; W3 the lemma on all 30 ordered pairs of the occupied `2 × 3` window at `(12,1,2)`; W4 the lemma's failure for a direction-dependent rule; W5 closure on the `3 × 3` torus under an arbitrary law, its failure with a preference for occupied neighbourhoods, and agreement for a single record; W6 the production mean at `(5,2,3)`, `k = 4`; W7 under block 01's reading (ii) the weight still factorizes across an empty site. All pass. A re-read of the theorem text against the runner before the gates corrected two sentences (the lemma's scope for orders that read contents; reading (ii) does not break T2). Mutation census: 13 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
python3 scripts/admissibility_rule_what_a_source_is_when_records_move_one_mass_per_record_screened_density_signed_tilt_2026_09_20.py
python3 scripts/admissibility_rule_what_a_source_is_when_records_move_one_mass_per_record_screened_density_signed_tilt_2026_09_20.py --list-mutations
python3 scripts/admissibility_rule_what_a_source_is_when_records_move_one_mass_per_record_screened_density_signed_tilt_2026_09_20.py --mutation content_field_not_odd_injected
python3 .claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block41_refuter.py
```
