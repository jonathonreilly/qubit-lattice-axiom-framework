---
claim_id: ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "Supplied link-qubit ice model with the exact vertex Gauss law and the ring clause -g (U + U^dag) at V = 0, g = 1, on L^3 tori, walkers in the flip component of the canonical zero-winding state. Exact: for the cyclic triple of transverse modes (a-links modulated along axis a + 1 mod 3) the averaged f-sum f = 2 u s(k)^2 holds without any symmetry of the state, and log-convexity of the averaged spectral moments gives omega_min(k) <= 2 s(k) (u/chi)^(1/2) and S_T(k) <= s(k) (u chi)^(1/2), with chi the triple-averaged static susceptibility read from E(h) = E_0 - (3N/4) h^2 chi + O(h^4); on the exact 2^3 component the averaged f-sum holds to 1e-9 and the chain reads 2.5173 <= 2.7754 <= 2.8724 <= 2.9728. Finite estimates from a compiled fixed-population projector (480 walkers, projection 30, two to eight seeds, errors from the larger of seed scatter and bin error): chi = 1.04-1.21 for k = pi/8 ... pi/2 on 6^3-16^3 (4^3: 0.89), rising slightly with k (fitted chi ~ k^(0.08 +- 0.01)), the value at each torus's smallest momentum about 5 % below the same momentum on a larger torus; evaluated bounds omega_min <= 1.03-1.05 s(k) and S_T <= 0.53-0.55 s(k) at the smallest momenta (0.410 and 0.213 at pi/8 on 16^3). At 8^3, 1920 walkers give chi(pi/2) 4 % below 480 walkers (2.3 standard errors). The estimates are inconsistent at their stated errors with a residual constant S_0 = 0.39 in S_T and with a quadratic mode, and lie 3-10 standard errors below the earlier forward-walking structure factors on 12^3 and 16^3. No photon law, phase or limit is claimed; the evaluated bounds are estimates of bounds, not certified enclosures."
upstream_dependencies:
  - minimal_axioms
  - ring_model_pure_ring_point_transverse_fluctuations_at_the_smallest_momentum_are_a_third_of_the_uniform_ice_constant_and_the_feynman_photon_bound_shows_no_resolved_power_on_small_tori_bounded_theorem_note_2026-09-24
  - ring_model_two_regulators_a_region_bounded_by_records_matches_the_torus_at_size_eight_and_the_walker_population_is_the_larger_regulator_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_controlled_population_the_transverse_susceptibility_from_energies_bounds_the_photon_2026_09_25.py
---

# Energy-only bounds on the pure-ring photon from the mode-averaged transverse susceptibility

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** exact inequalities of the supplied model with finite projector estimates; unaudited.

## Result

The landed two-regulator note found the walker population, not the torus,
steering the projector's structure factors on the larger tori, and the
forward-walking ancestry collapsing (0.5 % of the walkers at lag 2 on 16³).
This block controls the population by changing both the code and the
observable.
- **Exact: energies bound the photon (Theorem 1).** For a cyclic triple of
  transverse modes that meets each plaquette orientation once, the averaged
  f-sum rule `f̄ = 2us²` holds with no symmetry assumption. With the
  triple-averaged static susceptibility `χ̄_T(k)`, read from ground-state
  energies in a weak field, log-convexity of the spectral moments bounds
  the lowest transverse excitation and the structure factor:
  `ω_min(k) ≤ 2 s(k) (u/χ̄)^{1/2}` and `S̄_T(k) ≤ s(k) (u χ̄)^{1/2}`. The
  energies need no lineages: the mixed energy estimator is exact for any
  guide.
- **A projector whose events cost the same on every torus.** Only the
  plaquettes within two link steps of a flip change their rates; the
  compiled code updates those alone and runs 70 to 360 times faster than
  before on 8³ to 16³. It reproduces two exact ground states.
- **The susceptibility is nearly flat.** On 6³–16³, `χ̄_T = 1.04–1.21` for
  `k = π/8 … π/2`, rising slightly with `k` (`χ̄ ∝ k^{0.08 ± 0.01}`) and not
  growing at small `k`; each torus's smallest momentum reads about 5 %
  below the same momentum on a larger torus.
- **What the bounds then say.** At the smallest momenta the lowest
  transverse excitation is bounded by `1.03–1.05 s(k)` and the structure
  factor by `0.53–0.55 s(k)`: on 16³ at `π/8`, `ω_min ≤ 0.410` and
  `S̄_T ≤ 0.213`. A residual constant `S_0 = 0.39` would need `χ̄` twice
  (12³) to 3.4 times (16³) the measured value; a quadratic mode would make
  `χ̄(π/6)/χ̄(π/2)` near 9 on 12³, against a measured `0.89 ± 0.02`.
- **The earlier forward-walking values.** On 4³ and 6³ they sit at the
  bound (98 % and 103 % of it); on 12³ and 16³ they lie 3–10 standard
  errors above it.

Supplied model, finite estimates: no photon law, phase or limit is
claimed. Read through the landed Gaussian comparator, the estimates
correspond to `U = 1/χ̄ = 0.913` and `K = 4u = 1.152`, a velocity
`(UK)^{1/2} = 1.025` and `S̄_T/s(k) = 0.562`: the values at which both
bounds are saturated.

## Setting and decision points

- **D-gauss, D-roles, D-ring (landed).** Link qubits at link sites of the
  doubled lattice with the exact vertex Gauss law
  (`DYNAMICS_CLAUSE_AN_EXACT_GAUSS_LAW_FREEZES_THE_LINK_FIELD_UNDER_EVERY_TWO_SITE_GENERATOR_THE_FIELD_MOVES_BY_RINGS_AND_HOPS_INSIDE_ONE_NEIGHBOURHOOD_BOUNDED_THEOREM_NOTE_2026-09-24.md`)
  and the covariant plaquette clause `−g (U + U†)` at `V = 0`, `g = 1`
  (`DYNAMICS_CLAUSE_THE_COVARIANT_PLAQUETTE_CLAUSE_ANNIHILATES_UNIFORM_ICE_EXACTLY_AT_THE_ROKHSAR_KIVELSON_POINT_AND_UNRECORDED_PLAQUETTES_CAN_POLARIZE_THE_ICE_BOUNDED_THEOREM_NOTE_2026-09-24.md`),
  on `L³` tori, walkers started in the flip component of the canonical
  zero-winding state
  (`RING_MODEL_WINDING_SECTOR_SPLITTINGS_RESOLVED_ON_THE_SMALL_TORI_AND_A_MULTI_EXPONENTIAL_RELAXATION_AT_THE_PURE_RING_POINT_BOUNDED_THEOREM_NOTE_2026-09-24.md`).
- **The mode triple and the probe field (method).** The cyclic triple of
  transverse modes `O_a(k) = N^{−1/2} Σ_{a-links} e^{ik x_b} σ` with
  `b = a + 1 mod 3`: `z`-links modulated along `x`, `x`-links along `y`,
  `y`-links along `z`. Each plaquette orientation carries exactly one of
  them. The probe is `H(h) = H − h Σ_a Σ_{a-links} cos(k x_b) σ`, diagonal,
  so `H(h)` keeps the sign structure that makes the projector exact.
- **The projector (method).** A compiled continuous-time Green's function
  Monte Carlo with a fixed population and local updates, guide
  `exp(0.2 N_flip + (h/2) Σ cos(k x_b) σ)`.

None is adopted.

## Theorem 1 — energies bound the mode-averaged photon

Let `a_n = (1/3) Σ_a |⟨n|O_a(k)|0⟩|²` be the triple-averaged spectral weights
of a ground state `|0⟩` of the flip component, `ω_n = E_n − E_0`, and
`m_j = Σ_n a_n ω_n^j`, the sums over excited states.

1. `m_0 = S̄_T(k)`, the triple-averaged transverse structure factor, when
   the modes have no ground-state component.
2. `m_1 = f̄(k) = 2 u s(k)²`, with `u = Σ_p ⟨R_p⟩/N_p` the ring expectation
   per plaquette and `s(k)² = 2 − 2 cos k`. The landed note
   `RING_MODEL_PURE_RING_POINT_TRANSVERSE_FLUCTUATIONS_AT_THE_SMALLEST_MOMENTUM_ARE_A_THIRD_OF_THE_UNIFORM_ICE_CONSTANT_AND_THE_FEYNMAN_PHOTON_BOUND_SHOWS_NO_RESOLVED_POWER_ON_SMALL_TORI_BOUNDED_THEOREM_NOTE_2026-09-24.md`
   states the orientation-averaged identity, with its proof, without any symmetry of the
   state; mode `a` is changed only by the plaquettes of orientation
   `(a, a+1)`, so the cyclic triple averages each orientation once and the
   same identity holds for it. At `V = 0`, `u = −E_0/N_p`.
3. `m_{−1} = χ̄_T(k)/2`, the triple-averaged static susceptibility. The
   three modes carry different momenta, so second-order perturbation
   theory in the probe gives `E(h) = E_0 − (3N/4) h² χ̄_T(k) + O(h⁴)` for
   `2k ≢ 0`, with `N = L³` vertices, and twice that coefficient when
   `2k ≡ 0`.
4. The moments of a positive measure are log-convex, so
   `ω_min ≤ m_0/m_{−1} ≤ (m_1/m_{−1})^{1/2} ≤ m_1/m_0`, where `ω_min` is the
   lowest excitation coupled to any of the three modes. Hence
   `ω_min(k) ≤ 2 s(k) (u/χ̄_T(k))^{1/2}` and, by Cauchy–Schwarz,
   `S̄_T(k) ≤ s(k) (u χ̄_T(k))^{1/2}`.

These are inequalities of the model: evaluated with exact energies they
are rigorous. Evaluated with projector estimates of `E_0` and `E(h)`, they
inherit those estimates' statistical and population errors and are
estimates of bounds, not certified enclosures. On the exact 2³ component
at `k = π` the averaged f-sum holds to the last digit
(`3.008907 = 2us²`), the chain reads `2.5173 ≤ 2.7754 ≤ 2.8724 ≤ 2.9728`,
and the structure-factor bound `1.0475` lies 3.5 % above the exact
`S̄_T = 1.0122`. A finite `χ̄_T` as `k → 0` would bound the lowest
transverse excitation by a linear law in `s(k)` and make `S̄_T` vanish at
least linearly; a structure factor tending to a constant, or a mode whose
energy vanishes as `k²` at fixed weight, would instead make `χ̄_T` grow as
`1/k` or `1/k²`. ∎

## Method — controlling the population

- **A projector whose events cost the same on every torus.** The earlier
  projector recomputed the rate of every plaquette after each flip, so its
  cost per event grew with the torus. After a flip only the plaquettes
  within two link steps can change their flippability or their guide
  ratio: about seventy, whatever the size. The compiled projector updates
  those alone and draws the next flip from block sums of the rates. It
  reproduces the exact 2³ and 3³-region ground states, and its cost per
  walker per unit imaginary time is tabled below against the earlier
  code's.
- **An observable that needs no lineages.** Forward walking needs the
  walkers' ancestry to survive the forward lag; on 16³ only 0.5 % of it
  does, so more walkers alone cannot rescue it. The susceptibility needs
  only ground-state energies with and without a weak field. The mixed
  energy estimator is exact for any positive guide, the guide here carries
  half the field to cut the variance, and the population bias of the plain
  energy largely cancels between the runs that are differenced.
- **The field fit.** `E(h) = E_0 − a h² − b h⁴ + …` with `a = N χ/4`; the
  runs at `h = 0, 0.15, 0.30` eliminate `b`:
  `a = (15 E_0 − 16 E(0.15) + E(0.30))/(12 · 0.15²)`. On the exact 2³ curve
  with the mode triple this fit lands 0.1 % above the exact susceptibility
  at `k = π`, where the response is most nonlinear.
- **Errors.** Each (torus, momentum) point has two to eight independent
  seeds. Its error is the larger of the seed scatter of the mean and the
  pooled ratio of seed scatter to bin error times the mean bin error; in
  this block that ratio is 0.93, so the choice is conservative, not a
  calibrated error model.

## Diagnostic 1 — controls

- **Exact 2³ component, `k = π`, cyclic triple.** Averaged f-sum
  `3.008907 = 2us²`; per-mode susceptibilities `0.72938` (all three);
  structure factor `1.01215`; chain `2.5173 ≤ 2.7754 ≤ 2.8724 ≤ 2.9728`;
  bound `1.0475`. The `h⁴`-eliminating fit of the exact energies at
  `h = 0.15, 0.30` gives `0.73019` (0.1 %). Projector energies at those
  fields lie within 1.9 standard errors of the exact ones.
- **Exact 3³ interior bounded by records (3646 states).** The compiled
  projector's energy `−8.3112 ± 0.0067` against `−8.30262`, and its pure
  flippable density `0.24101 ± 0.00043` against `0.24138`.

## Diagnostic 2 — the walker population

On 8³ at `k = π/2`, eight seeds at 480 walkers give `χ̄ = 1.208 ± 0.015` and
four at 1920 give `1.157 ± 0.016`: 2.3 standard errors apart, a possible
population effect of about 4 % at 480 walkers that the grid below carries.
The plain energy per plaquette shifts from `−0.28842` to `−0.28875`. In this
block independent seeds scatter by 0.93 times the ten-bin errors, so the
error inflation built into the runner (the larger of seed scatter and that
ratio times the bin error) is conservative, not a calibrated error model.
Cost per walker per unit imaginary time: 0.65, 2.28 and 5.98 ms on 8³, 12³
and 16³, against 47, 500 and 2170 ms for the earlier projector.

## Diagnostic 3 — the susceptibility and the bounds

480 walkers, projection 30, probe fields 0.15 and 0.30; `u` from the plain
energy of each torus.

| torus | `k` | `χ̄_T` | runs | bound on `ω_min` | bound / `s(k)` | bound on `S̄_T` |
|---|---|---|---|---|---|---|
| 4³ | π/2 | 0.888 ± 0.020 | 3 | 1.625 | 1.149 | 0.721 |
| 6³ | π/3 | 1.071 ± 0.015 | 3 | 1.039 | 1.039 | 0.556 |
| 8³ | π/4 | 1.064 ± 0.008 | 8 | 0.797 | 1.042 | 0.424 |
| 8³ | π/2 | 1.182 ± 0.013 | 8 | 1.397 | 0.988 | 0.826 |
| 12³ | π/6 | 1.084 ± 0.017 | 3 | 0.533 | 1.030 | 0.289 |
| 12³ | π/3 | 1.130 ± 0.017 | 3 | 1.009 | 1.009 | 0.570 |
| 12³ | π/2 | 1.214 ± 0.018 | 3 | 1.376 | 0.973 | 0.835 |
| 16³ | π/8 | 1.038 ± 0.029 | 2 | 0.410 | 1.051 | 0.213 |
| 16³ | π/4 | 1.114 ± 0.020 | 2 | 0.776 | 1.014 | 0.432 |
| 16³ | π/2 | 1.181 ± 0.021 | 2 | 1.393 | 0.985 | 0.822 |

The bounds carry half the relative error of `χ̄` (0.3–1.4 %).

- **Flat, not growing.** A weighted fit `χ̄ ∝ k^{−p}` over all ten points
  gives `p = −0.080 ± 0.011`; a flat mean `1.095 ± 0.005` leaves
  `χ² = 238` for 9 degrees of freedom, so the small rise with `k` is
  resolved. A residual constant would need `p = 1`, a quadratic mode
  `p = 2`.
- **Fixed momentum across tori.** `χ̄(π/2)`: 0.888, 1.182, 1.214, 1.181 on
  4³, 8³, 12³, 16³; `χ̄(π/4)`: 1.064 (8³), 1.114 (16³); `χ̄(π/3)`: 1.071 (6³),
  1.130 (12³). Beyond 4³ the values at a fixed momentum agree within
  2–3 standard errors, and the smallest momentum of each torus reads about
  5 % low.

## Diagnostic 4 — what the estimates are inconsistent with

| comparison | value | against |
|---|---|---|
| forward walking, 4³ π/2 (run average) | 0.710 ± 0.010 | bound 0.721 (−0.9) |
| forward walking, 6³ π/3 (run average) | 0.572 ± 0.018 | bound 0.556 (+0.8) |
| forward walking, 8³ π/4 (run average) | 0.491 ± 0.022 | bound 0.424 (+3.0) |
| forward walking, 8³ π/2 (run average) | 0.765 ± 0.013 | bound 0.826 (−4.4, below) |
| forward walking, 12³ π/6 (100 walkers) | 0.496 ± 0.057 | bound 0.289 (+3.6) |
| forward walking, 12³ π/3 (100 walkers) | 0.778 ± 0.048 | bound 0.570 (+4.3) |
| forward walking, 16³ π/8 (120 walkers) | 0.591 ± 0.037 | bound 0.213 (+10.2) |
| forward walking, 16³ π/4 (120 walkers) | 0.770 ± 0.047 | bound 0.432 (+7.2) |
| forward walking, 16³ π/2 (120 walkers) | 1.039 ± 0.073 | bound 0.822 (+3.0) |
| residual `S_0 = 0.392` at 12³ π/6 | needs `χ̄ ≥ 2.00` | measured 1.08 |
| residual `S_0 = 0.392` at 16³ π/8 | needs `χ̄ ≥ 3.53` | measured 1.04 |
| `χ̄(π/6)/χ̄(π/2)` on 12³ | 0.89 ± 0.02 | quadratic mode about 9, residual constant about 3 |

Deviations in brackets are in standard errors, combining both errors. The
forward-walking values are six-mode averages and the bound is for the
cyclic triple; they coincide for a cubic-symmetric state and otherwise the
six-mode average is the mean of the cyclic and anticyclic triples. ∎

## What this means for the lanes

- **Photon lane.** With the population controlled through an observable
  that needs no lineages, the estimates from 6³ to 16³ say one consistent
  thing: the transverse susceptibility stays near one down to the smallest
  momentum reached, so the lowest transverse excitation is bounded by a
  linear law with slope near one and the transverse structure factor
  vanishes at least linearly. On the sizes where forward walking is
  reliable the structure factor sits at its bound, the single-mode
  signature. The residual-constant and quadratic readings of the earlier
  notes are inconsistent with these estimates. This is a finite-torus
  statement about a supplied model: no limit and no phase is claimed.
- **Earlier notes.** The forward-walking values on 12³ and 16³ in the
  landed notes on the Feynman bound and the 10³ point were already scoped
  as biased estimator outputs by review; these bounds quantify how far.
- **What the framework supplied.** The Gauss law and the ring are decision
  points; the projector, the probe field and the mode triple are methods.

## What stays open

- An independent check of the bounds, and larger tori (20³, 24³) at the
  smallest momenta, where the 5 % suppression at `k_min` can be followed.
- A population study at 16³ like the 8³ one, and the 4 % walker effect at
  8³ at a precision that separates it from zero.
- The sweep toward the RK point, where the bound must soften (companion
  block), and the region bounded by records with the same probe.

## Evidence limits

- **Domain:** the supplied model on the listed tori, the zero-winding flip
  component of the canonical state, the listed estimator settings.
- **Exact versus estimated:** Theorem 1 and the 2³ numbers are exact; every
  larger-torus number is a projector estimate with bin and seed errors that
  have no proved coverage.
- **Population:** the energy differences were checked at one size and one
  momentum; a population effect of a few per cent is not excluded.
- **Counterroutes:** other sectors, non-Gaussian states and finite-size
  effects beyond these tori remain available.

## Prior art

Feynman 1954; the sum-rule and moment inequalities of linear-response theory
(for example Pitaevskii and Stringari, Bose–Einstein Condensation, 2003);
Trivedi and Ceperley 1990; Calandra Buonaura and Sorella 1998; Hermele,
Fisher and Balents 2004; Shannon, Sikora, Pollmann, Penc and Fulde 2012;
Benton, Sikora and Shannon 2012. All cited as prior art, not as premises.

## Checks

The runner has 5 checks and all pass in about 50 minutes, single-threaded.

| Check | Result |
|---|---|
| Exact 2³ control | Averaged f-sum to 1e-9; the chain; the bound; the fit within 0.1 %; projector energies within 1.9 standard errors. |
| Records control | Energy and pure flippable density of an exact 3646-state region within errors. |
| Walker population | 480 against 1920 walkers on 8³: 2.3 standard errors (threshold 3); seed scatter 0.93 times the bin errors. |
| Susceptibility grid | Ten (torus, momentum) points, errors below 25 %; bounds; the exponent. |
| Comparisons | Reported. |

## Independent check

None yet. The runner was run once through the cache tool; seeded Monte
Carlo reproduces its numbers.

## What this does not do

- It adopts no clause, Gauss law, method or comparison.
- It claims no photon law, velocity, phase or limit; the evaluated bounds
  are estimates, not certified enclosures.
