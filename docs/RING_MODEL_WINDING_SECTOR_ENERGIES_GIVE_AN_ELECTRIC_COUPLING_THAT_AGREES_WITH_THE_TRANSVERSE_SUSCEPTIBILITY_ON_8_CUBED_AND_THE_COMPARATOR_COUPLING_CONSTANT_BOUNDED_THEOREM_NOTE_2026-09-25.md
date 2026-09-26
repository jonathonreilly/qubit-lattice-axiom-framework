---
claim_id: ring_model_winding_sector_energies_give_an_electric_coupling_that_agrees_with_the_transverse_susceptibility_on_8_cubed_and_the_comparator_coupling_constant_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "Supplied link-qubit ice model with the exact vertex Gauss law and the ring clause -g (U + U^dag) at V = 0, g = 1, on L^3 tori; conserved section fluxes W = (2q, 0, 0) built by reversing q straight loops. Exact: in the landed Gaussian comparator one coupling U sets the flux-sector energies U W^2 / (2L), the transverse susceptibility 1/U, the static pair tail -U/(pi d) and, with the landed matching rule K = 4u, the velocity (4uU)^(1/2) and the dimensionless coupling alpha_G = U/(pi c_G) = (U/u)^(1/2) / (2 pi). Finite projector estimates (compiled projector of open PR 9236, 1920 walkers, projection 50, four to eight seeds; errors are the larger of seed scatter and bin error, a heuristic): U_W = L [E(1) - E(0)] / 2 is 1.463 +- 0.017, 1.110 +- 0.059, 0.674 +- 0.177 on 4^3, 6^3, 8^3 (fit A q^2 + B q^4: 1.586, 1.067, 0.880 +- 0.077), against 1/chi = 1.152, 0.944, 0.933 +- 0.012 at the smallest momentum of the same tori; the ratio [E(2) - E(0)] / [E(1) - E(0)] is 2.99, 3.70, 5.57 +- 1.49 against the comparator's 4. alpha_G on 8^3 is 0.286 +- 0.002 from 1/chi and 0.278 +- 0.012 from U_W. On the exact 2^3 torus the projected sector energies match exact diagonalization for q = 0, 1. No limit, phase, coupling of a physical field or comparison value is claimed."
upstream_dependencies:
  - minimal_axioms
  - ring_model_winding_sector_splittings_resolved_on_the_small_tori_and_a_multi_exponential_relaxation_at_the_pure_ring_point_bounded_theorem_note_2026-09-24
  - gaussian_lattice_maxwell_comparator_gives_a_linear_size_independent_transverse_structure_factor_and_misses_the_pure_ring_level_step_bounded_theorem_note_2026-09-24
runner: scripts/ring_model_electric_coupling_from_winding_sector_energies_and_the_comparator_coupling_constant_2026_09_25.py
---

# Winding-sector energies give an electric coupling that agrees with the transverse susceptibility's on 8³, and the comparator's dimensionless coupling

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** exact identities of the supplied model and its comparator, with finite projector estimates; unaudited.

## Result

Open PR 9236 read the electric coupling of the pure-ring point from the
transverse response, `U = 1/χ̄ ≈ 0.9`, and open PR 9244 read it from static
charges, `1.48 ± 0.20` through their adjacent-pair core. In the Gaussian
comparator one coupling sets both, and also the energy of a uniform field.
The pure-ring point conserves the section flux, so a uniform field is a
sector of its own. This block measures the sector energies, again from
ground-state energies alone.

- **The uniform-field coupling moves onto the transverse one with size.**
  `U_W = L [E(1) − E(0)] / 2`, the comparator's `U` for one flux quantum, is
  `1.463 ± 0.017`, `1.110 ± 0.059` and `0.674 ± 0.177` on 4³, 6³ and 8³; a
  fit `A q² + B q⁴` through three quanta gives `1.586`, `1.067 ± 0.023` and
  `0.880 ± 0.077`. The transverse route on the same tori gives
  `1/χ̄ = 1.152`, `0.944` and `0.933 ± 0.012`. On 4³ the two differ by more
  than eight standard errors, on 6³ by three to five, and on 8³ they agree
  within one and a half.
- **The sector energy approaches the quadratic law.** The ratio
  `[E(2) − E(0)] / [E(1) − E(0)]`, which is 4 in the comparator, is
  `2.99 ± 0.04`, `3.70 ± 0.20` and `5.57 ± 1.49`: well below the quadratic
  law on 4³, closer on 6³, within errors on 8³.
- **The comparator's dimensionless coupling.** With the ring expectation
  `u` from the same runs, `α_G = U / (π c_G) = (U/u)^{1/2} / (2π)` is
  `0.286 ± 0.002` from the transverse route and `0.278 ± 0.012` from the
  flux sectors on 8³, and `0.288` and `0.306` on 6³. The static-pair
  coupling through the core would give `0.360`.

Supplied model, finite estimates: agreement on 8³ within errors is not an
equivalence, three sizes cannot exclude a further drift, and `α_G` is a
number of the comparator, not a measured coupling of any physical field.
What the data show is that the uniform-field and transverse routes to the
comparator's one coupling differ strongly on the smallest torus and agree
within errors by 8³.

## Setting and decision points

- **D-gauss, D-ring (landed).** Spin-1/2 link fields `σ = ±1` on the cubic
  `L³` torus with the exact vertex Gauss law, and the clause
  `−g Σ_p (U_p + U_p†)` at `V = 0`, `g = 1`.
- **The section fluxes (landed).** The flux `W_x`, the sum of `σ` over the
  x-links crossing a plane `x = const`, is the same for every plane and is
  conserved by every plaquette flip
  (`RING_MODEL_WINDING_SECTOR_SPLITTINGS_RESOLVED_ON_THE_SMALL_TORI_AND_A_MULTI_EXPONENTIAL_RELAXATION_AT_THE_PURE_RING_POINT_BOUNDED_THEOREM_NOTE_2026-09-24.md`).
  The sector with `W = (2q, 0, 0)` is built by reversing `q` straight x-loops
  in the staggered zero-flux state.
- **The Gaussian comparator (landed).** The lattice Maxwell comparator of
  `GAUSSIAN_LATTICE_MAXWELL_COMPARATOR_GIVES_A_LINEAR_SIZE_INDEPENDENT_TRANSVERSE_STRUCTURE_FACTOR_AND_MISSES_THE_PURE_RING_LEVEL_STEP_BOUNDED_THEOREM_NOTE_2026-09-24.md`,
  `H = (U/2) Σ E² + (K/2) Σ (curl A)²`, with `E` normalised like `σ` and the
  matching rule `K = 4u` of that note. It is used as a comparator, not as a
  description of the model.
- **The projector (method).** The compiled projector of open PR 9236, guide
  `exp(0.2 N_flip)`, walkers started from loop-move samples of the sector
  that keep its flux, fixed populations of 1920 walkers and projection
  time 50 per run.

None is adopted.

## Theorem 1 — what the comparator predicts from one coupling

In the Gaussian comparator, with `E` normalised like `σ`:

1. **Flux sectors.** A sector with section flux `W` has its lowest energy
   `U W² / (2L)` above `W = 0`: the uniform field `W / L²` on each of the
   `L³` x-links minimises the electric energy, and the oscillators, which
   carry the zero-point energy, are the same in every sector. So
   `U_W ≡ L [E(1) − E(0)] / 2` equals `U` for the sector `q = 1`, and
   `[E(2) − E(0)] / [E(1) − E(0)] = 4`.
2. **Transverse response.** The triple-averaged static susceptibility of
   open PR 9236 is `χ̄ = 1/U` at every momentum.
3. **Static charges.** A pair of divergence `±2` costs `4U [G(0) − G(d)]`
   (open PR 9244), with the tail `−U / (π d)` since `G(d) → 1 / (4π d)`.
4. **Velocity and coupling.** Each transverse oscillator has frequency
   `(UK)^{1/2} |s(k)|`, so with `K = 4u` the velocity is `c_G = (4uU)^{1/2}`
   and the static tail over the velocity is the dimensionless number
   `α_G = U / (π c_G) = (U/u)^{1/2} / (2π)`.

These are identities of the comparator. The supplied model need not obey
them; the diagnostics measure how far it does, on each route separately. ∎

## Diagnostic 1 — exact control on 2³

On the `2³` torus every ice state is enumerated. The sector `q = 0` has 880
states, of which the seed's flip component holds 864; the sector `q = 1`
has 464 states, all in one component. Loop moves that keep the flux,
started from the seed, sample each sector, and the projector started from
those samples gives `−9.03006 ± 0.00685` and `−7.40135 ± 0.00299` against the
exact sector ground energies `−9.026721` and `−7.399111`. The sector `q = 2`
is the control's caveat: its seed is a frozen one-state component, the
flux-preserving loop moves cannot leave it on this torus, and the sector's
ground `−5.656854` lies in its other 55 states. On the larger tori the loop
samples of each sector are not checked for this; their energies are those
of the part of the sector the samples reach.

## Diagnostic 2 — the sector energies

Energies in units of `g`; `u = −E(0)/N_p`.

| torus | `E(0)` | `E(1) − E(0)` | `E(2) − E(0)` | `E(3) − E(0)` | `U_W`, `q = 1` | `U_W`, fit `A q² + B q⁴` | `[E(2) − E(0)] / [E(1) − E(0)]` |
|---|---|---|---|---|---|---|---|
| 4³ (four seeds) | −56.2820 ± 0.0069 | 0.7315 ± 0.0084 | 2.1900 ± 0.0083 | — | 1.463 ± 0.017 | 1.586 ± 0.023 | 2.99 ± 0.04 |
| 6³ (six seeds) | −187.4349 ± 0.0145 | 0.3699 ± 0.0198 | 1.3671 ± 0.0179 | 2.9497 ± 0.0203 | 1.110 ± 0.059 | 1.067 ± 0.023 | 3.70 ± 0.20 |
| 8³ (eight seeds) | −443.3635 ± 0.0311 | 0.1685 ± 0.0443 | 0.9381 ± 0.0452 | 2.1575 ± 0.0433 | 0.674 ± 0.177 | 0.880 ± 0.077 | 5.57 ± 1.49 |

On 4³ the fit uses two sector differences for two parameters, so it has no
freedom left; the `A q² + B q⁴` form is an ansatz throughout.

## Diagnostic 3 — the two routes on the same tori

The transverse susceptibility is re-measured here at the smallest momentum
of each torus with the probe of open PR 9236 (480 walkers, four seeds).

| torus | `k` | `χ̄` | `1/χ̄` | `U_W`, `q = 1` | `U_W`, fit |
|---|---|---|---|---|---|
| 4³ | π/2 | 0.868 ± 0.025 | 1.152 ± 0.033 | 1.463 (+8.5 σ) | 1.586 (+10.9 σ) |
| 6³ | π/3 | 1.060 ± 0.013 | 0.944 ± 0.012 | 1.110 (+2.7 σ) | 1.067 (+4.7 σ) |
| 8³ | π/4 | 1.072 ± 0.014 | 0.933 ± 0.012 | 0.674 (−1.5 σ) | 0.880 (−0.7 σ) |

The susceptibilities agree with open PR 9236's (0.888, 1.071, 1.064).

## Diagnostic 4 — the comparator's dimensionless coupling

| torus | route | `U` | `c_G = (4uU)^{1/2}` | `α_G` |
|---|---|---|---|---|
| 4³ | `1/χ̄` | 1.152 | 1.162 | 0.3155 ± 0.0045 |
| 4³ | flux sectors | 1.586 | 1.364 | 0.3702 ± 0.0026 |
| 6³ | `1/χ̄` | 0.944 | 1.045 | 0.2875 ± 0.0018 |
| 6³ | flux sectors | 1.067 | 1.111 | 0.3057 ± 0.0033 |
| 8³ | `1/χ̄` | 0.933 | 1.038 | 0.2861 ± 0.0019 |
| 8³ | flux sectors | 0.880 | 1.008 | 0.2779 ± 0.0121 |
| 8³ | static pair through the core (open PR 9244) | 1.48 ± 0.20 | — | 0.360 |

`c_G` is the comparator's velocity with the matching rule `K = 4u`. Open PR
9236 bounded the lowest transverse excitation of the supplied model by
`c_G s(k)` with `U = 1/χ̄` on these tori. If a velocity `c` is read from that
excitation, `U/(π c)` is at least `α_G` for the same `U`.

## What this does not do

- It claims no limit: three sizes cannot exclude a further drift of either
  route, and agreement within errors on 8³ is not an equivalence.
- It does not establish that the flux-preserving loop samples reach every
  part of a sector on the larger tori.
- `α_G` is a dimensionless number of the Gaussian comparator evaluated with
  the supplied model's energies. It is not a coupling of any physical field
  and is compared with no measured value.
- It adopts no clause, Gauss law, comparator, matching rule or method.

## Prior art (not premises)

Hermele, Fisher and Balents 2004 and Benton, Sikora and Shannon 2012 (the
Gaussian description of the Coulomb phase of quantum ice); Pace,
Morampudi, Moessner and Laumann 2021 (the same dimensionless combination
for quantum spin ice); Trivedi and Ceperley 1990, Calandra Buonaura and
Sorella 1998 (fixed-population projectors). All cited as prior art, not as
premises.

## Checks

The runner has four checks: the exact 2³ control; the sector energies on
4³–8³; the two routes on the same tori; `α_G` from each route (reported).
The fresh run takes about 52 minutes.

## Independent check

None yet.

## Evidence limits and No-Go Discipline Gate

- **N1 — Domain:** the supplied link-qubit ice model and clause on the stated tori, sectors and projector settings.
- **N2 — Independence:** self-checked; the 2³ control is internal to this runner.
- **N3 — Imports:** the Gauss law, clause, comparator and matching rule are supplied, not framework admissions.
- **N4 — Dependencies:** the landed parents' scopes govern; open PRs are cited, not relied on.
- **N5 — Resolution:** finite Monte Carlo with heuristic errors; the fit form is an ansatz.
- **N6 — Residuals:** larger tori, sector connectivity and the static-charge tail beyond the core remain open.
- **N7 — Counterroutes:** other sectors, guides, populations and orders of limits remain available.
- **N8 — Boundary:** source note, not an audit verdict.

## Premise authority

The framework boundary is [the current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).
