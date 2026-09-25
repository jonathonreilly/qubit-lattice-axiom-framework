---
claim_id: ring_model_two_regulators_a_region_bounded_by_records_matches_the_torus_at_size_eight_and_the_walker_population_is_the_larger_regulator_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "Setting, all supplied and none adopted: spin-1/2 link fields with the exact vertex Gauss law (cubic ice) and the covariant plaquette clause -g (U + U^dag) at V = 0, g = 1 (landed); the guided continuous-time projector Monte Carlo with forward-walking estimators of open PRs 9148 and 9161. Exact: a record on a link removes every ring term containing it (P_q U_p P_q = P_q U_p^dag P_q = 0), and on a region bounded by records the Gauss law fixes every plane-section flux to a sum of recorded values, so the region has no winding sectors; checked as a four-qubit identity and on every state of a 3646-state exact flip component of a 3^3 interior. Control: the projector with records reproduces that component's ground state (energy, flippable density, three connected correlations) within 2.9 ten-bin standard errors. Finite diagnostics, 240 walkers, projection 24, forward lag 2: at size 8 the core (depth >= 2) of a region bounded by records agrees with the 8^3 torus within 1.6 standard errors in flippable density (0.3077 and 0.3075 against 0.3093), nearest-neighbour correlations (g_L(1) 0.061, 0.062 against 0.064; g_T(1) -0.2012, -0.2010 against -0.2039) and the two-block variance (0.623, 0.610 against 0.644), for a uniform-ice frame and the ordered canonical frame alike; the transverse correlation at distance two differs by 2.2-2.4 standard errors at both sizes and frames; at size 6 the core flippable density differs by 4.8. The walker population moves the same quantities more: on the 8^3 torus from 60 to 480 walkers the energy per plaquette goes from -0.28736 to -0.28853 (1/n_w extrapolation -0.28853 +- 0.00009) and g_T(1) from -0.1982 to -0.2122 (extrapolation -0.2119 +- 0.0017, equal to the 6^3 value -0.2111 +- 0.0023); the local-energy spread is about 0.17 sqrt(N_p), the effective sample size per block 0.99, 0.96, 0.90, 0.61, 0.60 on 4^3, 6^3, 8^3, 12^3, 16^3, and the distinct ancestors at forward lag 2 are 3-6 % of the walkers on 8^3; independent runs of the pure S_T(k_min) scatter by about twice their ten-bin errors on 8^3 (seven runs, 0.43-0.58, standard deviation 0.059), and averaged over independent runs S_T(k_min) is 0.710 +- 0.010, 0.572 +- 0.018, 0.491 +- 0.022 on 4^3, 6^3, 8^3 (three, four and seven runs of mixed walker numbers), falling monotonically. No phase, no photon law and no thermodynamic limit is claimed; the fixed-momentum growth of S_T reported for 12^3 and 16^3 at 100-120 walkers is not established."
upstream_dependencies:
  - minimal_axioms
  - dynamics_clause_an_exact_gauss_law_freezes_the_link_field_under_every_two_site_generator_the_field_moves_by_rings_and_hops_inside_one_neighbourhood_bounded_theorem_note_2026-09-24
  - dynamics_clause_the_covariant_plaquette_clause_annihilates_uniform_ice_exactly_at_the_rokhsar_kivelson_point_and_unrecorded_plaquettes_can_polarize_the_ice_bounded_theorem_note_2026-09-24
runner: scripts/ring_model_two_regulators_a_region_bounded_by_records_against_the_torus_and_the_walker_population_2026_09_25.py
---

# Two regulators at the pure-ring point: a region bounded by records matches the torus at size eight, and the walker population is the larger regulator

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** exact identities with finite numerical diagnostics under supplied decision points; unaudited.

## Result

The Lattice axiom's sites are all of `Z³`, and a finite computation needs a
regulator. Open PRs 9148–9171 used the torus, a quotient of the lattice
with quantized momenta, winding sectors and no records. The question put to
this block was whether the torus steers the answer. It compares two
regulators of the same bulk question at the pure-ring point.
- **A region bounded by records is an exact alternative (Theorem 1).** A
  record on a link removes every ring term containing it, and the Gauss law
  fixes every plane-section flux of the region to a sum of recorded values:
  the region has no winding sectors, and its sector is set by what is
  recorded around it. This is the framework's own finite object, a recorded
  region with an unrecorded interior, and the projector with records
  reproduces an exact 3646-state ground state.
- **At size 8 the region's interior matches the torus.** Two layers in from
  the records, the flippable density, the nearest-neighbour correlations and
  the two-block field variance agree with the 8³ torus within 1.6 standard
  errors, for records sampled from uniform ice and for the ordered canonical
  records alike, and the two sets of records agree with each other. The
  transverse correlation at distance two differs by 2.2–2.4 standard errors
  at both sizes and for both frames. At size 6 the interior is too close to
  its records (the flippable density differs by 4.8 standard errors).
- **The walker population moves the answer more than the boundary does.** On
  the 8³ torus, going from 60 to 480 walkers moves the energy per plaquette
  by 0.0012 and the nearest-neighbour transverse correlation by 0.014, five
  times the torus–region difference. Extrapolating in the inverse walker
  number returns the 6³ value of that correlation exactly
  (`−0.2119 ± 0.0017` against `−0.2111 ± 0.0023`): its apparent size
  dependence at fixed walker number was the population bias. The walker
  weights spread as the square root of the system size, so the bias grows
  with the torus.
- **The quoted errors of the pure estimator are too small.** At forward lag
  2 only 3–6 % of the walkers' ancestors survive on 8³, and seven
  independent runs of the smallest-momentum structure factor on 8³ scatter
  by about twice their ten-bin errors. Averaged over independent runs, the
  smallest-momentum structure factor falls monotonically, `0.710 ± 0.010`,
  `0.572 ± 0.018`, `0.491 ± 0.022` on 4³, 6³, 8³: the level step between 6³
  and 8³ reported in open PR 9161 is within the run-to-run scatter.

Supplied model, finite diagnostics: no phase, no photon law and no
thermodynamic limit is claimed. The answer to the question is that at the
sizes reached the torus does not steer the result, the walker population
does, and the numbers of open PRs 9161 and 9171 beyond 8³ need a controlled
population before they say anything about `Z³`.

## Setting and decision points

- **The lattice and its regulators.** The Lattice axiom's sites are all of
  `Z³`: "Physical sites are the points of the cubic lattice `Z^3`, with
  nearest-neighbor adjacency, standard translations, and proper cubic
  rotations about each site. No site is privileged." Every finite
  computation needs a regulator. The torus `Z³/LZ³` is a quotient: it keeps
  every site equivalent and the translations and rotations exact, and it
  adds quantized momenta `2πm/L`, winding sectors (loops around the torus
  that do not contract), the identification of `x` with `x + L`, and no
  records. A region of `Z³` whose outside carries records is a subset: the
  framework's own finite object, a recorded region with an unrecorded
  interior. Both are methods here; neither is adopted as the structure of
  the lattice.
- **D-gauss, D-roles, D-ring (landed).** Link qubits at link sites of the
  doubled lattice with the exact vertex Gauss law
  (`DYNAMICS_CLAUSE_AN_EXACT_GAUSS_LAW_FREEZES_THE_LINK_FIELD_UNDER_EVERY_TWO_SITE_GENERATOR_THE_FIELD_MOVES_BY_RINGS_AND_HOPS_INSIDE_ONE_NEIGHBOURHOOD_BOUNDED_THEOREM_NOTE_2026-09-24.md`)
  and the covariant plaquette clause `−g (U + U†)` at `V = 0`, `g = 1`
  (`DYNAMICS_CLAUSE_THE_COVARIANT_PLAQUETTE_CLAUSE_ANNIHILATES_UNIFORM_ICE_EXACTLY_AT_THE_ROKHSAR_KIVELSON_POINT_AND_UNRECORDED_PLAQUETTES_CAN_POLARIZE_THE_ICE_BOUNDED_THEOREM_NOTE_2026-09-24.md`).
- **The record-bounded box (method).** The unrecorded interior
  `{1, …, m}³` of an `(m+2)³` lattice cell whose other links carry records
  (a frame two layers thick, wrapped periodically only so that it is itself
  ice). The records are either a uniform-ice sample of the whole cell in its
  zero-winding sector ("uniform frame") or the canonical zero-winding ice
  state of open PR 9153 ("canonical frame"). Walkers start from the frame's
  own configuration and relax under the projector.
- **The projector and its estimators (method).** The guided continuous-time
  Green's function Monte Carlo of open PR 9148 (guide `exp(0.2 N_flip)`,
  counting only unrecorded plaquettes), with the lineage estimator of open
  PR 9161 at forward lag 2; errors are ten contiguous-bin standard errors.

None is adopted.

## Theorem 1 — records remove the ring terms they touch and fix the fluxes of the region they bound

1. **Records remove ring terms.** Let `P_q` project a link onto its
   recorded value `q`. The ring operator `U_p` of a plaquette `p`
   containing that link flips it, so `P_q U_p P_q = P_q U_p† P_q = 0`. On a
   region bounded by records the clause is therefore the clause of the
   plaquettes all of whose links are unrecorded; plaquettes that touch a
   record are frozen.
2. **Records fix every flux.** Take the slab `S` of interior vertices with
   coordinate `≤ c` along an axis. The Gauss law summed over `S` makes the
   flux through the section of unrecorded links from layer `c` to `c + 1`
   equal to minus the signed sum of the other links leaving `S`, all of
   which touch the frame and carry records. So every plane-section flux of
   the region is fixed by its records: the region has no winding sectors,
   and its sector is set by what is recorded around it.

Both statements are exact. The runner checks the first as a matrix
identity on four qubits (zero to machine precision for both records and
all four link positions) and the second on every one of the 3646 states of
an exact flip component of a `3³` interior (six sections each), and again
on every box of the diagnostic. ∎

On a torus the corresponding fluxes are winding numbers that no record
fixes; open PRs 9153–9171 chose the zero-winding sector. A region bounded
by records makes that choice for itself.

## Control — the projector with records against exact diagonalization

On the `3³` interior of a `5³` cell with a uniform frame, the flip
component of the frame's configuration has 3646 states and ground energy
`−8.30262`. The projector with records (200 walkers, projection 40)
reproduces the energy, the flippable density and three connected
correlations of the exact ground state within the contiguous-bin errors
(deviations −0.6, −2.1, +2.7, +0.2 and −2.9 ten-bin standard errors in the
certifying run; two development runs, one with a second frame, agreed
within 1.9). A first development pass binned
interleaved blocks and reported the correlations six standard errors off;
the bins were nearly copies of each other, and contiguous bins removed the
discrepancy.

## Diagnostic 1 — the boundary regulator

240 walkers, projection 24 in blocks of 0.05, the first 8 discarded,
forward lag 2, ten contiguous bins. The region's core is the unrecorded
links with both ends at depth `≥ 2` from the records; its correlations are
connected (the records induce a mean field near the boundary). `g_L(r)` and
`g_T(r)` are the equal-time correlations of a link field component at
separation `r` along and across its own axis; `χ(ℓ)` is the variance of the
field summed over an `ℓ³` block, per link. Deviations from the torus of the
same size in standard errors are in brackets.

| regulator | `n_f` | `g_L(1)` | `g_T(1)` | `g_T(2)` | `χ(2)` | `χ(3)` |
|---|---|---|---|---|---|---|
| torus 6³ | 0.3114 ± 0.0008 | +0.0595 ± 0.0017 | −0.2111 ± 0.0023 | −0.0028 | 0.631 | 0.477 |
| region 6, uniform records | 0.3055 (−4.8) | +0.0557 (−0.8) | −0.2034 (+1.8) | −0.0116 (−2.2) | 0.613 (−1.6) | 0.450 |
| torus 8³ | 0.3093 ± 0.0007 | +0.0636 ± 0.0020 | −0.2039 ± 0.0021 | −0.0050 | 0.644 | 0.508 |
| region 8, uniform records | 0.3077 (−1.2) | +0.0610 (−0.6) | −0.2012 (+0.4) | −0.0138 (−2.2) | 0.623 (−1.1) | 0.471 |
| region 8, canonical records | 0.3075 (−1.2) | +0.0616 (−0.4) | −0.2010 (+0.4) | −0.0121 (−2.4) | 0.610 (−1.5) | 0.457 |

Block-variance errors are 0.004–0.006 on the tori and 0.014–0.031 in the
regions. Every region's plane-section fluxes equal the values its records
fix, and the two frames — one a uniform-ice sample, one the ordered
canonical state — give the same interior within errors: the interior
forgets which records surround it. The largest block, `χ(3)`, grows from 6
to 8 in both regulators (0.477 → 0.508 on the tori, 0.450 → 0.471 in the
regions), so that growth is not a property of the torus.

## Diagnostic 2 — the population regulator

The guide's local energy has a spread proportional to the square root of
the number of plaquettes; over a block of 0.05 it spreads the walker
weights by the amount below, and the effective sample size per block
follows. Guided samples, 12–100 per size.

| torus | `std(E_L)/√N_p` | log-weight spread per block | effective sample size per block |
|---|---|---|---|
| 4³ | 0.165 | 0.11 | 0.99 |
| 6³ | 0.164 | 0.21 | 0.96 |
| 8³ | 0.169 | 0.33 | 0.90 (measured 0.91–0.92) |
| 12³ | 0.196 | 0.71 | 0.61 |
| 16³ | 0.130 | 0.72 | 0.60 |

On the 8³ torus at fixed projection (24), the walker number moves the
energy and the short-range correlation monotonically within errors, and the
smallest-momentum structure factor within its scatter:

| walkers | `e_0` per plaquette | `S_T(π/4)` | `S_T(π/2)` | `g_T(1)` | ancestors at lag 2 |
|---|---|---|---|---|---|
| 60 | −0.28736 ± 0.00022 | 0.535 ± 0.039 | 0.743 ± 0.033 | −0.1982 | 6 % |
| 120 | −0.28830 ± 0.00025 | 0.427 ± 0.030 | 0.774 ± 0.048 | −0.2052 | 3 % |
| 240 | −0.28813 ± 0.00007 | 0.464 ± 0.035 | 0.784 ± 0.027 | −0.2039 | 4 % |
| 480 | −0.28853 ± 0.00010 | 0.433 ± 0.023 | 0.728 ± 0.024 | −0.2122 | 3 % |
| linear in `1/n_w`, `n_w → ∞` | −0.28853 ± 0.00009 | 0.417 ± 0.023 | 0.751 ± 0.022 | −0.2119 ± 0.0017 | — |

- **The energy and the short-range correlation carry a population bias.**
  Its slope in `1/n_w` is `+0.071` per plaquette for the energy, so 120
  walkers leave the 8³ energy `0.0006` too high. The extrapolated
  `g_T(1) = −0.2119 ± 0.0017` equals the 6³ value `−0.2111 ± 0.0023`, while
  the 240-walker 8³ value `−0.2039` differs from it by 2.5 standard errors:
  at fixed walker number the apparent change from 6³ to 8³ is the bias.
- **The energy drift with size is of the same kind.** At 100–120 walkers the
  energy per plaquette rose from `−0.2880` (8³) to `−0.2874` (10³),
  `−0.2867` (12³) and `−0.2858` (16³) in open PRs 9161 and 9171; a
  converged energy density would not drift, and the weight spread at 12³
  and 16³ is twice that of 8³. The bias there was not measured.
- **The pure structure factor's errors are too small.** Only 3–6 % of the
  walkers' ancestors survive the forward lag, so the ten-bin errors
  understate the variation between runs. Seven independent runs of
  `S_T(π/4)` on 8³ (open PR 9161, its 240-walker auxiliary run, the first
  pass, and the four scan runs) give values from 0.427 to 0.575 with a
  standard deviation of 0.059 against quoted errors of 0.023–0.039; on 6³
  four runs scatter by about 1.5 times their quoted errors. `S_T(π/2)` on 8³ is
  steadier (seven runs, standard deviation 0.035) and shows no walker-number
  trend.
- **Run averages.** Averaging the independent runs of `S_T(k_min)` (open PRs
  9161, 9163, 9169, their auxiliary runs and this scan; walker numbers mixed)
  gives `0.710 ± 0.010` on 4³ (three runs), `0.572 ± 0.018` on 6³ (four) and
  `0.491 ± 0.022` on 8³ (seven), errors of the mean. The fall is monotonic;
  the level step between 6³ and 8³ that open PR 9161 reported from single
  runs is within the scatter. The 8³ scan's extrapolation in the walker
  number, `0.417 ± 0.023`, lies below the run average, so the population
  bias and the scatter act together here.

## Diagnostic 3 — how far the records reach

In the uniform-records region of size 8, by depth from the records:

| depth | flippable density | rms of the estimated link means |
|---|---|---|
| 1 | 0.3030 | 0.404 |
| 2 | 0.3077 | 0.170 |
| 3 | 0.3068 | 0.156 |
| 4 | 0.3255 (six plaquettes) | 0.128 |
| torus 8³ | 0.3093 | 0 by symmetry |

The flippable density is within 1–2 standard errors of the torus from depth
2 on. The records induce a field of rms 0.40 on the first layer; deeper,
the rms of the estimated means (0.13–0.17) is of the order of the
statistical noise of a single link's mean at this precision, which was not
separately measured. ∎

## What this means for the lanes

- **For the question asked.** The torus is a quotient of `Z³`, not a piece
  of it, and it adds structure the axiom does not have. At the sizes
  reached here that structure does not steer the local and block
  quantities: a region bounded by records, the framework's own finite
  object, gives the same interior from size 8, whichever records surround
  it. What does steer the larger tori is the walker population, a regulator
  of the method rather than of the lattice.
- **For open PRs 9161, 9171 and 9172.** Their ten-bin errors on the pure
  structure factor are too small by a factor of about two. The fall of
  `S_T(k_min)` from 4³ to 8³ survives, since every one of seven 8³ runs lies
  0.12–0.27 below the 4³ value, and run averages make it monotonic; the
  level step between 6³ and 8³ and the four-size fits of open PR 9171 are
  within the run-to-run scatter. The
  fixed-momentum growth reported for 12³ and 16³ at 100–120 walkers is not
  established: the population bias grows with the torus and was not
  measured there. Correction notes citing this block are added to those
  three PRs.
- **What stands.** The exact identities of those blocks (the Feynman
  numerator, the transverse-weight sum rule, the RK anchor) and Theorem 1
  here are statements about the model, not about the method.
- **What the framework supplied.** The Gauss law and the ring are decision
  points; the torus, the region bounded by records, the frames and the
  projector are methods; the records theorem uses only the Record axiom's
  "a record locks exactly one admissible local possibility".

## What stays open

- A controlled population: walker numbers growing with the system, a better
  guide (a smaller local-energy spread), or a pure estimator that does not
  rely on lineages (reptation), with errors from independent runs.
- With the population controlled, the fixed-momentum structure factor on
  both regulators at 12 and beyond, which is where the photon question
  lives.
- The distance-two transverse correlation's 2.3-standard-error difference
  between the regulators, and the induced field's decay with depth at a
  precision that separates it from noise.
- Independent checks of every number here.

## Prior art

Rokhsar and Kivelson 1988; Trivedi and Ceperley 1990 (Green's function
Monte Carlo and forward walking); Umrigar, Nightingale and Runge 1993
(population-control bias); Calandra Buonaura and Sorella 1998
(fixed-population Green's function Monte Carlo); Baroni and Moroni 1999
(reptation quantum Monte Carlo). All cited as prior art, not as premises.

## Checks

The runner has 5 checks and all pass in about 25 minutes, single-threaded.

| Check | Result |
|---|---|
| Records theorem | `P_q U P_q = P_q U† P_q = 0` to machine zero; every state of a 3646-state exact component has every section flux equal to the value its records fix. |
| Control | Projector with records against exact diagonalization: deviations −0.6, −2.1, +2.7, +0.2, −2.9 ten-bin standard errors (two development seeds were within 1.9). |
| Population regulator | Spread by size; the 8³ scan; measured effective sample size within 0.1 of the prediction; fits reported. |
| Boundary regulator | Tori 6³, 8³ against regions of size 6 and 8 (two frames at 8); every region's fluxes fixed by its records; `g_T(1)` errors below 0.01. |
| Depth profile | Reported. |

## Independent check

None yet. The runner was run once through the cache tool; seeded Monte
Carlo reproduces the numbers. The seven-run scatter of `S_T(π/4)` on 8³
uses runs from open PR 9161 and its auxiliary runs together with the four
scan runs here.

## What this does not do

- It adopts no clause, Gauss law, regulator or method, and does not claim
  the lattice is finite, periodic or bounded.
- It claims no phase, no photon law and no thermodynamic limit; it does not
  measure the population bias beyond 8³.
