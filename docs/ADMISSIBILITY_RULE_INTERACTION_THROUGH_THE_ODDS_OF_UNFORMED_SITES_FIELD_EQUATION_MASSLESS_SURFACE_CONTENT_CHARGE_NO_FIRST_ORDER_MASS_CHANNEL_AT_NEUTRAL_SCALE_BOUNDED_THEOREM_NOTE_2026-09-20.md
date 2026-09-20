---
claim_id: admissibility_rule_interaction_through_the_odds_of_unformed_sites_field_equation_massless_surface_content_charge_no_first_order_mass_channel_at_neutral_scale_bounded_theorem_note_2026-09-20
claim_type: bounded_theorem
claim_scope: "CONDITIONAL on a supplied reading that is not in the axioms memo and is not adopted: an unformed site carries its probability distribution over the possibilities, and that distribution is a condition for its neighbours. For the six-axis rule with the declared isotropic pair weight omega = (p, q, r), T = p + q + 4r, K_1 = omega/T, l1 = (p-q)/T, l2 = (p+q-2r)/T: (T1, exact summation: an unformed site is one unknown content, summed) on a path window two records across a gap of n bonds weigh, against chance, 1 + 3 l1^n + 2 l2^n (equal contents), 1 - 3 l1^n + 2 l2^n (opposite), 1 - l2^n (orthogonal), with average over contents exactly 1; on every window every arrangement of k records weighs z^k Z once contents are summed, so no weight attaches to where the records are, while the contents of records across unformed sites are correlated by the static law; (T2, the self-consistent odds pi_x(s) proportional to the product over neighbours y of sum_b omega(s,b) pi_y(b), a record entering as a point mass) the odds factorize exactly as (T/6)^6 prod_y (1 + 6 (K_1 delta_y)(s)); the derivative of the map at the uniform field is K_1 - 1/6 per neighbour; on a torus the linearized map has the spectrum l_i (6 - E(k)), spectral radius 6 max(|l1|, |l2|) on even sides; 6 l1 = 1 exactly on the surface 5p = 7q + 4r, on which the declared triple (3,1,2) lies, and 6 l2 = 1 exactly on 5p + 5q = 16r; for 6 l1 < 1 the linear response of the vector channel to a source is the screened lattice Green function with m^2 = (1 - 6 l1)/l1 (5/3 at (5,2,4), 3/2 at (7,3,5)); (T3) one neighbour's factor contracts the ratio metric, R(omega x, omega y) <= R/((1-kappa) + kappa R) with kappa the least min/max ratio of two rows of omega, so on finite windows with 6 (1 - kappa) < 1 the odds exist, are unique for every arrangement of records, the iteration approaches them geometrically, and the change of the odds at graph distance n from a changed record is at most log(1/kappa) (6(1-kappa))^(n-1)/(1 - 6(1-kappa)) in log ratio; (T4) the map is covariant under the rotation of all contents, the six-outcome odds have no rotation-invariant component, and the content-averaged weight of a site against the void is 1 + 3 l1^2 sum_{y<y'} m_y.m_y' + higher orders in the neighbours' leans, with no first-order term; (T5, 'no record' counted as a seventh possibility with the weights of the law with vacancies, g = c/c_0) the uniform field of density rho is a fixed point for z = rho/(6(1-rho)(1+rho(g-1))^6) and the derivative of the map has the scalar eigenvalue rho(1-rho)(g-1)/(1+rho(g-1)) and the vector eigenvalue rho g l1/(1+rho(g-1)) per neighbour: at the neutral scale g = 1 the mass channel has no first-order strength; (T6) a record enters the field as a boundary value: in the linearized vector channel the field of a body S of agreeing records is u = 1 on S and u_x = l1 (sum of the six neighbours) off S, which for 6 l1 <= 1 is the probability that a walk killed at rate 1 - 6 l1 per step reaches S; it is monotone and subadditive in S, its charge on a record whose six neighbours are records is exactly 1 - 6 l1 (zero on the massless surface) and nowhere smaller, and the capacity per record falls as the body grows (0.872, 0.520, 0.399 at (5,2,4) and 0.713, 0.277, 0.140 at l1 = 19/119 for cubes of 1, 8, 27 records on the 5^3 torus): the source strength of a body is its capacity, not its number of records. EXECUTED, NOT CLAIMED: the full nonlinear odds around a held record against the screened Green function, the field on the massless surface, and the density excess with and without glue. NOT claimed: anything about the nonlinear field on or beyond the massless surfaces, the infinite lattice, a force law, any identification with a gravitational field, any adoption."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_interaction_through_the_odds_of_unformed_sites_field_equation_massless_surface_2026_09_20.py
---

# Records interacting through the odds of unformed sites: contents interact across empty sites and masses do not; the field equation of the odds, its massless surface 5p = 7q + 4r, a proved screened regime, and no first-order mass channel at the neutral scale

**Date:** 2026-09-20
**Type:** bounded_theorem
**Status:** bounded-support (exact on finite windows and tori under a supplied reading; the nonlinear fields executed, not claimed; nothing adopted or registered; unaudited)

This note works out a supplied reading, in which an unformed site carries its probability distribution and that distribution is a condition for its neighbours; the reading is not in the axioms memo and is not adopted.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 41 (PR #8547) found that records separated by empty sites do not interact. The owner asked (2026-09-20): "why couldnt records interact via the neighborhood probabilities?" They can. Block 41's statement is a theorem about a law in which an empty site carries nothing: every bond that touches it weighs `1`. The axioms' sentence "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." speaks of every site and does not say that a condition must be a record. If an unformed site carries its odds, and its odds are a condition for the next site, influence passes through empty sites. This note works that reading out in its two forms.

1. **Summed form (an unformed site is one unknown content).** Two records across a gap of `n` bonds on a line weigh `1 + 3λ₁ⁿ + 2λ₂ⁿ` against chance when their contents are equal, `1 − 3λ₁ⁿ + 2λ₂ⁿ` when opposite, `1 − λ₂ⁿ` when orthogonal: `3.43, 2.19, 1.59, 1.15, 1.02` for equal contents at `(12,1,2)` and `n = 1, 2, 3, 5, 8`. Averaged over contents the weight is exactly `1` at every `n`, and on any window every arrangement of `k` records weighs the same, `z^k Z`, once contents are summed: contents interact across empty sites, masses do not, at any distance.
2. **Self-consistent form (each site's odds are set by its neighbours' odds).** To first order the departure of a site's odds from the uniform ones is `K₁` applied to the sum of its six neighbours' departures. The part that leans towards a content obeys `v_x = λ₁ Σ_{y∼x} v_y + source`, that is `(−Δ + m²) v = source/λ₁` with `m² = (1 − 6λ₁)/λ₁`: a screened field of range `m⁻¹` lattice steps (`0.77` at `(5,2,4)`). The mass term vanishes exactly on the surface `5p = 7q + 4r`, where the linearized equation has no mass term and its response falls off as one-over-distance; the campaign's first declared triple `(3,1,2)` lies on that surface. Beyond it (`(12,1,2)`: `6λ₁ = 22/7`) the uniform field is unstable.
3. **A proved regime.** For weak preference, `6(1 − κ) < 1` with `κ` read off the pair weight (`κ = 400/441` at `(21,20,20)`), on every finite window the odds exist and are unique whatever the arrangement of records, and the influence of a record decays geometrically with distance. The criterion is silent at `(5,2,4)`, where the linear analysis still gives a screened field.
4. **What crosses is content, not mass.** The map is covariant under the rotation of all contents, so what a record feeds into the odds at first order is its content vector, which changes sign with the content and averages to zero. The six-outcome odds have no component that is blind to content. A weight that is blind to content sees the leans only at second order: `1 + 3λ₁² Σ_{y<y'} m_y·m_{y'}`.
5. **Counting "no record" as a possibility gives mass a channel, and the neutral scale switches it off.** With seven outcomes the density has its own first-order channel of strength `ρ(1−ρ)(g−1)/(1+ρ(g−1))` per neighbour, `g = c/c₀` the glue of block 40. At the neutral scale `g = 1` it is exactly zero. With glue it is a screened field whose mass term vanishes on its own surface (`g = 2` at density `1/2`).

6. **A record enters as a boundary value, not as an additive charge.** A record fixes the odds at its site. A body of agreeing records therefore acts on the field like a conductor held at a potential: its source strength is its capacity, which is carried by its surface (a record surrounded by records carries the charge `1 − 6λ₁`, zero on the massless surface) and grows like the body's size, not like its number of records. Executed near the surface: cubes of `1, 8, 27, 64` records give far fields in the ratio `1 : 2.2 : 3.2 : 4.0`.

So the owner's mechanism gives the record layer a field across empty space with the lattice Laplacian as its operator. Three things separate it from a field of the kind the gravity lane asks for: its first-order charge is the content, not the mass; it has a mass term except on tuned surfaces (and mass enters at first order only through the glue, not at all at the neutral scale); and its sources do not add, because records enter as conditions.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "owner, 2026-09-20: 'why couldnt records interact via the neighborhood probabilities?'; then 'well keep going until we have something solid or need to probe a different direction'"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the reading worked out in its summed and self-consistent forms: exact gap weights, the field equation of the odds with its massless surfaces, a proved screened regime, content as the first-order charge, the mass channel's first-order strength (zero at the neutral scale), and records as boundary values whose strength is a capacity. Next: the nonlinear field on the massless surface (the cubic term is marginal there), the second-order mass channel as an interaction between two records, and the sphere menu's odds beyond its surface; loaded on ai/probes"
conditional_surface_status: "T1-T6 exact at the stated scope (finite windows, tori, the linearization at the uniform field, the contraction regime); the nonlinear fields (sides 15 to 27, floating point) are in the controls and not claimed"
hypothetical_axiom_status: "the reading that an unformed site's odds are a condition for its neighbours, in either form; for T5 the law with vacancies of block 39 and the glue of block 40; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full) is used through "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.", "A site with no record cannot be read." and "No possibility is privileged.". Block 01 (on `main`, proposed and unaudited) supplies the rule as a product of pair weights whose pair weight is symmetric and isotropic with orbit values `(p, q, r)`, and lists the readings of a partially recorded neighbourhood; the summed form below is its reading (iii) and block 24's integrated exterior. Blocks 39, 40, 41 (open PRs #8530, #8546, #8547) supply the law with vacancies, the neutral scale `c₀ = 6/T` and the glue `g = c/c₀`, and the records-only statement this note qualifies.

- **One-neighbour probability.** `K₁ = ω/T`, symmetric and stochastic, with eigenvalues `1`, `λ₁` on the vector functions `e_i(s)` (three), `λ₂` on the quadrupole functions (two). `P_vec(a,b) = e(a)·e(b)/2`; `P_quad` equals `1/3, 1/3, −1/6` on equal, opposite, orthogonal pairs.
- **Summed form.** The weight of records on the set `η` with contents `s_η` is `z^{|η|} Σ Π_{bonds} ω`, the sum over the contents of all unformed sites of the window `Λ`.
- **Self-consistent form.** A field `π = (π_x)` of positive distributions on the unformed sites; a record is the point mass at its content; `Φ(π)_x(s) ∝ Π_{y∼x} Σ_b ω(s,b) π_y(b)`. The extension of the rule to a distribution as a condition is the one linear in the condition. Departure `δ_x = π_x − 1/6`; lean `m_x = Σ_s π_x(s) e(s)`.
- **Ratio metric.** `R(x, y) = max_s (x_s/y_s) / min_s (x_s/y_s) ≥ 1`; `κ(ω) = min_{s≠t} [min_b ω(s,b)/ω(t,b)] / [max_b ω(s,b)/ω(t,b)]`; for `p ≥ r ≥ q` this is `q²/p²`.
- **Seven outcomes.** Contents and "no record"; a content weighs `z`, two contents on a bond weigh `cω`, any bond with "no record" at an end weighs `1`; the same product map.
- `E(k) = 6 − 2Σcos k_i`; `Δ` the lattice Laplacian.

The logarithm of `R` is the projective metric of Hilbert, and the sharp contraction constant of a positive matrix in it is that of Birkhoff and Hopf; a weaker constant is proved here at scope. A unique fixed point of a contraction is the principle of Banach. The screened field equation is that of Helmholtz and its kernel is of the type of Yukawa; with no mass term it is the equation of Laplace and Poisson. Self-consistent one-site odds are the approximation of Weiss, and their cavity variant that of Bethe. Massless modes of a broken continuous symmetry are those of Goldstone. None is used as authority.

## Prior art and what is new

Block 01 listed the marginal reading; block 24 (PR #8158) computed bridges of unformed sites (`φ²`, `φ^{k+2}`); block 40 found the loop factor `1 + 3λ₁ⁿ + 2λ₂ⁿ`, which returns here as the weight of two equal records across a gap; block 41 proved the records-only statement. Blocks 03, 21, 27 proved uniqueness regions for laws by a different criterion. What is new: the two forms of the reading set side by side; the exact statement that under summation contents interact and masses do not; the field equation of the self-consistent odds, its two massless surfaces and the observation that `(3,1,2)` lies on one; a contraction proof of existence, uniqueness and geometric decay at weak preference; the second-order form of the content-blind weight; and the first-order strength of the mass channel with its zero at the neutral scale. Self-consistent odds and their linear stability are classical; they are re-derived here at scope by exact differentiation.

## Exact target and obligation graph

Target: decide whether, and as what, records interact when an unformed site's odds count as a condition. Obligations: (O1) the summed form; (O2) the self-consistent form's field equation; (O3) a regime in which that form is proved well posed; (O4) what a record feeds in; (O5) a channel for mass; (O6) whether sources add. T1–T6 discharge O1–O6 at the stated scope; the controls execute the nonlinear fields.

## Theorem T1 — summed form: contents interact across unformed sites, masses do not

(i) On a path window with records at its two ends and `n` bonds between them, the weight of the contents `(a, b)` is `(ωⁿ)(a,b) = Tⁿ K₁ⁿ(a,b)`; against the weight `Tⁿ/6` of independent uniform ends it is `6K₁ⁿ(a,b) = 1 + 6λ₁ⁿ P_vec(a,b) + 6λ₂ⁿ P_quad(a,b)`, which gives the three values stated. Their average over `b` is `1` because the rows of `P_vec` and `P_quad` sum to zero. (ii) On any window `Σ_{s_η} Σ_{rest} Π ω = Z_Λ` for every `η`, so the arrangement `η` weighs `z^{|η|} Z_Λ`: no weight attaches to where the records are, two masses have no interaction at any distance, and the formation clause consistent with this law is a constant rate with the static law's conditional odds. (iii) The contents of the records are distributed as the marginal of the static law on `η`; across unformed sites they are correlated (on the plaquette at `(3,1,2)` the joint law of two opposite corners is not uniform), so the independence of contents in block 41's T2 does not hold under this reading. ∎

## Theorem T2 — self-consistent form: the field equation of the odds

(a) `Σ_b ω(s,b) π_y(b) = (T/6)(1 + 6 (K₁δ_y)(s))`, hence `Φ(π)_x(s) ∝ Π_{y∼x} (1 + 6 (K₁δ_y)(s))`. (b) Differentiating at the uniform field, `∂Φ_x(s)/∂π_y(b) = K₁(s,b) − 1/6`; on departures of zero sum the linearized map is `δ_x = Σ_{y∼x} K₁ δ_y`. (c) `K₁` acts as `λ₁` on the vector part and `λ₂` on the quadrupole part, and the sum over the six neighbours multiplies a wave of wavevector `k` by `6 − E(k)`; the linearized map on a torus has the eigenvalues `λ_i (6 − E(k))`, and on a torus of even side its spectral radius is `6 max(|λ₁|, |λ₂|)`. (d) `6λ₁ = 1 ⟺ 5p = 7q + 4r` and `6λ₂ = 1 ⟺ 5p + 5q = 16r`; `λ₁ ≥ λ₂ ⟺ r ≥ q`. The triple `(3,1,2)` satisfies `5p = 7q + 4r`; at `(5,2,4)` and `(7,3,5)`, `6λ₁ = 18/23` and `4/5`; at `(12,1,2)`, `6λ₁ = 22/7 > 1`. (e) With a source `σ` in the vector channel the linear response solves `(1 − λ₁(6 − E(k))) v̂ = σ̂`; since `1 − λ₁(6 − E) = λ₁(m² + E)` with `m² = (1 − 6λ₁)/λ₁`, the response is `σ/λ₁` convolved with the Green function of `−Δ + m²`: screened with range `1/m` for `6λ₁ < 1` (`m² = 5/3` at `(5,2,4)`, `3/2` at `(7,3,5)`), and with no mass term on the surface of (d), where the constant field lies in the kernel of the linearized equation. ∎

On the `4³` torus at `(5,2,4)` the exact solution of the linear equation with a point source equals the mode sum at all 64 sites.

## Theorem T3 — a regime in which the odds are proved to exist, to be unique, and to forget records geometrically

**One factor.** Let `x, y` be positive vectors, `g = x/y`, `ν_s(b) ∝ ω(s,b) y_b`. Then `(ωx)_s/(ωy)_s = E_{ν_s}[g]`, and for two rows `ν_s ≥ κ ν_t` pointwise, so `E_{ν_s}[g − g_min] ≥ κ E_{ν_t}[g − g_min]` and `E_{ν_t}[g]/E_{ν_s}[g] ≤ g_max/((1−κ) g_min + κ g_max)`: `R(ωx, ωy) ≤ R/((1−κ) + κR)` with `R = R(x,y)`. Since `t ↦ t − log((1−κ) + κeᵗ)` vanishes at `0` and has slope at most `1 − κ`, `log R(ωx, ωy) ≤ (1−κ) log R(x, y)`.

**The map.** The ratio metric of a product of factors is at most the product of their ratio metrics, so `log R(Φ(π)_x, Φ(π')_x) ≤ (1−κ) Σ_{y∼x, unformed} log R(π_y, π'_y) ≤ 6(1−κ) sup_y log R(π_y, π'_y)`; records contribute nothing, being the same in both fields.

**Consequences, on a finite window with `θ = 6(1−κ) < 1`.** `Φ` is a contraction of the positive fields in the metric `sup_x log R`, which is complete; it has exactly one fixed point for every arrangement of records, and its iterates approach that point geometrically from any positive start. If one record at `y₀` changes its content, a neighbour's factor changes by at most `log(1/κ)` and `S_n = sup_{dist(x, y₀) ≥ n} log R` obeys `S_n ≤ θ S_{n−1}` for `n ≥ 2` and `S_1 ≤ log(1/κ)/(1−θ)`: the change at distance `n` is at most `log(1/κ) θ^{n−1}/(1−θ)`. ∎

At `(21,20,20)`, `κ = 400/441` and `θ = 82/147`. At `(3,1,2)`, `(5,2,4)`, `(12,1,2)` the criterion is silent (`θ = 16/3, 126/25`, and larger). The one-factor bound is nearly attained: the runner's adversarial pairs reach `999/1000` of it.

## Theorem T4 — what a record feeds in: its content at first order, nothing blind to content before second order

(a) `Φ` commutes with the 24 rotations acting on all contents, records included. In the regime of T3 the unique field around one record of content `a` is therefore carried to the field around `Ra` by `R`, so its lean at every site lies along `e(a)` and reverses with `a`; summed over the six contents of the record the first-order source is zero. The six-outcome odds decompose into a constant, fixed by normalization, a vector and a quadrupole: there is no component blind to content for a mass to source. (b) For neighbours with purely vector departures of leans `m_y`, the normalizer of the odds at `x`, against its value in the void, is `(1/6) Σ_s Π_y (1 + 3λ₁ m_y·e(s)) = 1 + 3λ₁² Σ_{y<y'} m_y·m_{y'} + (terms of order three and higher)`, with no first-order term because `Σ_s e(s) = 0`. ∎

Any clause that weighs a record of unread content at a site through this normalizer (block 39's formation rate `zZ_x` is one) therefore responds to the square of the lean field: for one record's field that is the square of the screened Green function, of half the range, and on the massless surface the square of a one-over-distance field. This is a statement about the identity in (b), not a force law.

## Theorem T5 — "no record" as a seventh possibility: the mass channel and its zero at the neutral scale

The factor a neighbour of density `ρ` and uniform contents gives to a content is `1 − ρ + ρ c T/6 = 1 + ρ(g − 1)` and to "no record" is `1`; the uniform field is a fixed point exactly when `ρ/(6(1−ρ)) = z (1 + ρ(g−1))⁶`. A change `dρ` of one neighbour's density changes the logarithm of every content's factor by `(g−1) dρ/(1 + ρ(g−1))` and leaves the factor of "no record" unchanged, so the density at `x` changes by `ρ(1−ρ)(g−1)/(1+ρ(g−1)) · dρ`: the scalar eigenvalue `λ_s`. A vector departure of the contents changes the factor of the content `a` by the relative amount `3 g λ₁ (m·e(a)) ρ/(1+ρ(g−1))` and leaves the density unchanged: the vector eigenvalue `λ_v = ρ g λ₁/(1 + ρ(g−1))`. Both are confirmed by exact differentiation of the seven-outcome map at four points. ∎

Consequences. At the neutral scale `λ_s = 0`: a record, as a unit of mass, has no first-order effect on the odds that a neighbouring site is occupied, in agreement with block 40 (no binding without a cycle; self-consistent odds see no cycles). With glue, the density obeys the same field equation with `m_s² = (1 − 6λ_s)/λ_s`, a positive source at every record whatever its content, and no mass term on `6ρ(1−ρ)(g−1) = 1 + ρ(g−1)` (at `ρ = 1/2`, `g = 2`, where `λ_s = 1/6`). The vector channel is diluted by the density: at `g = 1` its mass term vanishes on `6ρλ₁ = 1`.

## Theorem T6 — records are boundary values: the source strength of a body is its capacity

Work in the linearized vector channel along the common content of a body `S` of agreeing records, with `0 < 6λ₁ ≤ 1`. A record is a point mass, of lean `1`; an unformed site obeys the linear field equation. The field is `u = 1` on `S`, `u_x = λ₁ Σ_{y∼x} u_y` off `S`. (a) Let a walk step to each of the six neighbours with probability `λ₁` and stop with probability `1 − 6λ₁`; `h_S(x)`, the probability that the walk from `x` reaches `S`, satisfies the same equations, and on a finite window with `6λ₁ < 1` the solution is unique, so `u = h_S`. Hence `u_S ≤ u_{S'}` for `S ⊂ S'`, and `u_{A∪B} ≤ u_A + u_B`, since reaching `A ∪ B` means reaching `A` or reaching `B`. (b) The charge of the field is `μ_S = (1 − λ₁ Adj) u`, supported on `S`, and `u = Σ_{s∈S} μ_S(s) G(·, s)` with `G` the kernel of `1 − λ₁ Adj`. On a record whose six neighbours are records `μ_S = 1 − 6λ₁`; on any record `μ_S = 1 − λ₁ Σ_{y∼s} u_y ≥ 1 − 6λ₁`. On the massless surface the records inside a body carry no charge at all. (c) The capacity `cap(S) = Σ_s μ_S(s)` is what the far field is proportional to where the field has no mass term, and it is not additive: on the `5³` torus, cubes of `1, 8, 27` records have capacities per record `0.872, 0.520, 0.399` at `(5,2,4)` and `0.713, 0.277, 0.140` at `λ₁ = 19/119` (that is `(29/10, 1, 2)`), and two single records two steps apart have a capacity below the sum of their capacities. ∎

A density that enters a field equation linearly, as the gravity lane's source does, gives fields that add over the units of mass. A record that enters as a condition does not: whatever the reading of the odds, a body of records is to the field what a conductor at a fixed potential is, and its strength grows with its size rather than with its content of records. For bodies far apart compared with the range the capacities do add, since the walk from one seldom reaches the other; bodies within a range of each other, and the records of one compact body, shield one another.

## Executed: the nonlinear odds around one held record (not proved)

Control `specs/supervisor_control_block42_odds_field.py` (floating point; tori of side 15 to 27; iteration of the full map with one record held at the origin).

| case | linear prediction | executed |
|---|---|---|
| six outcomes, `(5,2,4)` and `(2.5,1,2)` (`6λ₁ = 0.783`, range `0.77`) | lean ratio to `r = 1`: `0.1789, 0.0353, 0.0076, 0.0017` at `r = 2..5` | `0.1790, 0.0353, 0.0076, 0.0017` |
| six outcomes, `(2.9,1,2)` (`6λ₁ = 0.958`, range `1.95`) | `0.3173, 0.1218, 0.0531, 0.0251` | `0.3137, 0.1200, 0.0522, 0.0247` |
| six outcomes, `(3,1,2)`, massless surface | `r·v(r)` constant for a pure one-over-distance field | side 27: `0.299, 0.288, 0.281, 0.286, 0.298` at `r = 1..5`, then rising as the periodic images are met; the plateau lengthens with the side (15, 21, 27) |
| seven outcomes, `(5,2,4)`, `ρ = 0.3`, `g = 1` | no first-order density excess | excess `1.5·10⁻⁴, 3.5·10⁻⁷, 7·10⁻¹⁰` at `r = 1, 2, 3` |
| seven outcomes, `g = 1.5` (`6λ_s = 0.548`) | ratio to `r = 1`: `0.1035, 0.0112, 0.0012` | `0.1029, 0.0111, 0.0012` |
| seven outcomes, `g = 2` (`6λ_s = 0.969`) | `0.339, 0.141, 0.067` | `0.377, 0.170, 0.086` |
| six outcomes, bodies of agreeing records, side 25, `(2.95,1,2)` (range `2.79`): far lean as a multiple of one record's, at 5, 7, 9 steps beyond the face | additive sources would give `8, 27, 64` | cube of 8: `2.15, 2.25, 2.35`; of 27: `2.93, 3.24, 3.58`; of 64: `3.43, 4.00, 4.76`; 8 records spaced 4 apart: `2.01, 2.45, 3.21` |
| the same at `(2.5,1,2)` (range `0.77`) | — | cube of 8: `2.24, 2.47, 2.59`; of 27: `2.96, 3.54, 3.95`; of 64: `3.28, 4.15, 4.86`; spaced: `1.18, 1.34, 1.55` |

The nonlinear field follows the linear prediction away from the surfaces and departs from it by ten to thirty per cent next to the scalar surface, where the held record is a large disturbance. On the vector surface the cubic term of the map is marginal and a slow correction to one-over-distance is expected; the three sides do not separate it from the finite size. Nothing here is claimed.

## No-Go Discipline Gate

The note's negative sentences are: under summation masses do not interact (T1); the six-outcome odds carry no content-blind first-order source (T4); at the neutral scale the mass channel has no first-order strength (T5); the sources of the field do not add (T6). The gate is applied to them.

### N1 — Routes by which the sentences could fail
1. *Another extension of the rule to a distribution as a condition* — the declared extension is linear in the condition (a mixture of records weighs the mixture of their factors). An extension that reads the sharpness of a neighbour's odds would give the six-outcome odds a content-blind input. None is suggested by the axioms' text; none is excluded.
2. *A clause that gives the normalizer a role* — T4(b) shows where mass would enter at second order; whether any clause does so is not settled here.
3. *Cycles* — the self-consistent form does not see cycles; the summed form does. Block 40's loop factors are the summed form's content on cycles of records; for masses the summed form has no interaction at all, cycles included, because unformed sites are summed rather than weighed `1`.
4. *Direction-dependent rules* — outside the declared isotropic class the covariance of T4(a) holds only for rotations of sites and contents together (block 41, refuter W4).
5. *Records as sources rather than conditions* — T6 rests on a record fixing the odds at its site. A reading in which a record adds a fixed term to its neighbours' equations without being a site of the field would have additive sources; it is not the reading worked out here, in which a record is a condition.
6. *The amplitude layer* — untouched by this note.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied reading, the law with vacancies and the glue, declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the sentence the reading rests on; the two others | yes (premise of the reading) |
| block 01 (`main`) | the rule as a product of isotropic pair weights; reading (iii) | yes (premise, proposed) |
| blocks 39, 40 (open PRs #8530, #8546) | the law with vacancies, the neutral scale, the glue | yes for T5 (restated) |
| block 41 (open PR #8547) | the records-only statement qualified here | placement |
| block 24 (open PR #8158), blocks 03, 21, 27 | bridges of unformed sites; uniqueness regions by another criterion | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "contents interact across unformed sites and masses do not; the odds obey a screened field equation with massless surfaces; the first-order charge is the content; at the neutral scale the mass channel has no first-order strength" | executed: gap weights for the three relations at `n = 1..6`; the 36 entries of the derivative; the 24 rotations | executed: all 16 arrangements on the plaquette; the field equation at all 64 sites of the `4³` torus | executed: eigenvalues of `K₁`; waves under the neighbour sum; the mode sum | executed: contraction on 1600 random and 20 adversarial exact pairs, product bound on 200 cases; the seven-outcome derivative at four points; exact fields, charges and capacities of cubes of 1, 8, 27 records on the `5³` torus | T1 and T4(a) on every finite window; T2 on every torus; T3 on every finite window of degree at most six; nothing about the nonlinear field on or beyond the massless surfaces |

### N6 — Partial-closure paths and primitive scan
The registered primitives do not say what a condition is at an unformed neighbour. Whether an unformed site's odds are a condition is the owner's reading to adopt or not; this note adopts nothing.

### N7 — Steelman
Hostile reviewer: "The self-consistent odds are a textbook approximation, and its massless surface is the approximation's artefact; the summed law has its onset elsewhere." Reply: the note keeps the two apart. The summed form is exact and its statements (T1) involve no approximation. The self-consistent form is treated as an object in its own right, the literal reading of 'each site's odds are determined by its neighbours' conditions', and T2–T5 are exact statements about that object; no claim is made that either form approximates the other, and block 28's located onset of the summed law on `(p,1,2)`, near `3.65`, is recorded next to the self-consistent surface at `3`.

### N8 — Cross-cycle echo
Block 40's loop factor is T1's gap weight; block 41's symmetry lemma is T4(a); block 40's "no binding without a cycle" is T5's zero at `g = 1`; block 22's Green function at the origin normalizes the response of T2(e); the uniqueness blocks 03, 21, 27 used a total-variation criterion where T3 uses the ratio metric.

## Falsifiers

- A path window and contents for which the summed weight across a gap differs from the three formulas, or an arrangement whose content-summed weight differs from `z^k Z`.
- A pair of positive vectors violating `R(ωx, ωy) ≤ R/((1−κ) + κR)`.
- A window with `6(1−κ) < 1` and two distinct positive fixed points of `Φ` for the same records.
- A rotation that does not commute with `Φ` for the declared pair weight.
- A point `(ρ, g)` at which the exact derivative of the seven-outcome map has a scalar eigenvalue other than `ρ(1−ρ)(g−1)/(1+ρ(g−1))`.
- Two bodies of agreeing records whose joint linear field exceeds the sum of their separate fields somewhere, or a record surrounded by records with a charge other than `1 − 6λ₁`.

## Boundaries and non-claims

No force law and no gravitational reading is claimed. The field of the self-consistent odds is proved to exist and to be unique only for `6(1−κ) < 1`; elsewhere the statements are about the linearization at the uniform field. Nothing is claimed about the nonlinear field on the massless surfaces, where the cubic term is marginal, nor beyond them, where the uniform field is unstable; for the six-axis menu, whose symmetry is discrete, every channel is expected to have a mass term beyond the surface, and for the sphere menu the transverse channel is expected to have none; neither is proved here. The summed form's law of contents is the static law's marginal, which the campaign treats as the equilibrium comparator. The two forms are different objects. The reading, the law with vacancies and the neutral scale remain proposals.

## Imports
- `minimal_axioms`: the sentences quoted under Premises. Block 01 (on `main`): the rule and its readings; proposed, unaudited. Blocks 39, 40, 41 (PRs #8530, #8546, #8547, open): restated or qualified. Blocks 03, 21, 22, 24, 27, 28 as evidence addresses.
- Named standard imports at definition level: the spectral decomposition of a symmetric matrix commuting with a group; completeness of the ratio metric on positive distributions (Hilbert's projective metric); the fixed-point principle for contractions (Banach); exact differentiation by first-order truncated arithmetic.
- Reference only: Birkhoff and Hopf for the sharp contraction constant `tanh(Δ/4)`, which would enlarge T3's region to `p/q < 7/5` and is not used; Weiss and Bethe for self-consistent odds; Helmholtz, Yukawa, Laplace, Poisson for the field equations; Goldstone for the massless transverse modes.

## Review record
Supervisor-run block (owner 2026-09-20: "why couldnt records interact via the neighborhood probabilities?", then "well keep going until we have something solid or need to probe a different direction"). Lens: block 41's T2 is a statement about a law in which an empty site has no state; the owner's sentence gives it one, and the axioms' text allows it. Tested before writing: exact gap weights and their content average; the nonlinear odds around a record against the screened Green function (four digits at range `0.77`). Primary: T1, T2. Added after a scratch look at bodies of records during the first gate run (which was stopped for it): T6, records as boundary values, with exact capacities on the `5³` torus and the executed far fields of cubes. Added while writing the runner: the elementary contraction bound in multiplicative (rational) form, so that T3 is checked exactly; the seven-outcome map, after noticing that the six-outcome odds have no content-blind component at all. Refuting pass (`specs/supervisor_control_block42_refuter.py`, machinery disjoint from the runner's: enumeration, symbolic differentiation, hill-climbing): W1 gap weights by enumeration of the unformed contents; W2 all 64 arrangements of the `2 × 3` window and the correlation of contents across unformed sites; W3 the derivative of the six-outcome map for symbolic `(p, q, r)`; W4 the seven-outcome fixed point and both eigenvalues as identities in symbolic `(ρ, g, p, q, r)`, the scalar one vanishing identically at `g = 1`; W5 the mode sum against the linear equation at all sites of the `6³` and `3³` tori, three strengths; W6 hill-climbing against the one-factor bound (pairs of ratio at least 2; best `999999/10⁶` of the bound, never above) and two exact trajectories of the full map; W7 the second-order coefficient by symbolic expansion; W8 the integer triples up to 40 on the two massless surfaces, which meet on `q = r`, `5p = 11q`. All pass. The theorem text was re-read against the runner before the gates (block 41's lesson) and five sentences were tightened. Mutation census: 14 mutations, each failing in its own family only; two contraction mutations were first missed by random pairs and are now caught by adversarial pairs and single-neighbour cases. Author checks only; no independent review has taken place.

## Verification

```bash
python3 scripts/admissibility_rule_interaction_through_the_odds_of_unformed_sites_field_equation_massless_surface_2026_09_20.py
python3 scripts/admissibility_rule_interaction_through_the_odds_of_unformed_sites_field_equation_massless_surface_2026_09_20.py --list-mutations
python3 scripts/admissibility_rule_interaction_through_the_odds_of_unformed_sites_field_equation_massless_surface_2026_09_20.py --mutation scalar_channel_glue_at_neutral_scale
python3 .claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block42_refuter.py
```
