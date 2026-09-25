---
claim_id: ring_model_projector_monte_carlo_at_the_pure_ring_point_energies_below_variational_and_no_growth_of_plaquette_order_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Setting, all supplied and none adopted: spin-1/2 link fields on the cubic lattice with the exact vertex Gauss law (cubic ice) and the covariant plaquette clause -g (U + U^dag) at V = 0 (open PRs 9066, 9072), which is stoquastic in the ice basis; a continuous-time projector Monte Carlo guided by the Jastrow state exp(0.2 N_flip) of open PR 9146, with single-plaquette-flip hops, weights exp(-int (E_L - E_ref)), and reconfiguration to a fixed population every dtau = 0.05 (0.1 on the fine torus). Finite diagnostics. (i) Control on the fine Z_4^3 torus (9600 ice states, 937 flip classes, largest 864): exact ground energy -9.0267 against the projector's -9.0412 +- 0.0149; exact mixed flippable number 10.500 against 10.496 +- 0.031; exact pure 10.124, variational 10.907, extrapolated 10.085. (ii) On the coarse 4^3, 6^3, 8^3 tori the projector energy per plaquette is -0.2926(3), -0.2883(3), -0.2871(2) against the variational -0.2766, -0.2806, -0.2797 (gains 5.81%, 2.76%, 2.65%), with the two halves of the kept projection 2.8, 0.7, 1.9 standard errors apart. (iii) Flippable density variational / mixed / extrapolated: 0.295 / 0.314 / 0.333, 0.300 / 0.307 / 0.314, 0.302 / 0.305 / 0.309; connected flippable-plaquette structure factor per plaquette at (pi,pi,pi): 0.274 / 0.284(8) / 0.294, 0.295 / 0.300(10) / 0.305, 0.285 / 0.288(14) / 0.291, with the halves of the projection 1.4, 2.4, 0.6 standard errors apart; mixed values at (0,0,0), (pi,0,0), (pi,pi,0) on 8^3: 0, 0.080, 0.211. The projection times are 16 in units of 1/g on the coarse tori. No phase of the pure-ring point, no thermodynamic limit and no physical identification is claimed; the mixed and extrapolated estimators of diagonal observables carry the usual guiding-function bias."
upstream_dependencies:
  - minimal_axioms
runner: scripts/ring_model_projector_monte_carlo_at_the_pure_ring_point_2026_09_24.py
---

# Projector Monte Carlo of the ring model at the pure-ring point: energies below the variational ones, and no growth of plaquette order to the 8³ torus

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** finite diagnostics of a supplied model; unaudited.

## Result

Open PR 9146 asked what the ring model does at the pure-ring point `V = 0`
and could answer only within a weighted-ice variational family. This note
uses a method that leaves that family: in the ice basis every off-diagonal
element of the Hamiltonian is `−g`, so a positive-weight projector Monte Carlo
converges to the ground state with no sign problem.
- **The method is controlled.** On the fine `Z_4³` torus, where exact
  diagonalization is available, the projector energy and the mixed
  flippable number agree with the exact values within errors, and the
  extrapolated flippable number lands within 0.04 of the exact pure one.
- **The energy drops below the variational one by a few percent.** On the
  4³, 6³ and 8³ tori the projector energy per plaquette is −0.2926, −0.2883,
  −0.2871 against the Jastrow values −0.2766, −0.2806, −0.2797. The 6³ and 8³
  values agree to 0.4%.
- **No growth of plaquette order.** The connected flippable-plaquette
  structure factor per plaquette at `(π, π, π)` is 0.28–0.30 on all three
  sizes, mixed and extrapolated, and stable between the halves of the
  projection. A Bragg peak would grow with the number of plaquettes; these
  do not grow from 192 to 1536 plaquettes. The other high-symmetry
  wavevectors are lower still.

So, as far as a projection of 16 units of `1/g` on tori up to 8³ can see, the
pure-ring ground state is a re-weighted ice ensemble with short-range
plaquette correlations, not a plaquette crystal at any of the four
high-symmetry wavevectors probed. A phase determination would still need
larger sizes, the gap or the photon dispersion, and a check for order at other
wavevectors.

## Setting and decision points

- **D-gauss, D-roles, D-ring (open PRs 9066, 9072).** Link qubits at link
  sites of the doubled lattice; the exact vertex Gauss law, three in and
  three out; the covariant plaquette clause `−g (U + U†)` flipping a
  flippable plaquette; `V = 0`.
- **The guiding function (supplied).** `ψ_G(c) = exp(α N_flip(c))`,
  `α = 0.2`, the variational optimum of open PR 9146.
- **The projector (a method, not a decision point).** Continuous-time
  Green's function Monte Carlo on the similarity-transformed matrix
  `ψ_G(c') H_{c'c}/ψ_G(c)`: from `c`, hops to `c_p` at rate
  `g exp(α ΔN_p)` for each flippable `p`, local energy
  `E_L(c) = −Σ_p g exp(α ΔN_p)`, weights `exp(−∫(E_L − E_ref) dτ)`, and
  stochastic reconfiguration to a fixed population every `Δτ`. Mixed
  estimators `⟨ψ_G|O|ψ₀⟩/⟨ψ_G|ψ₀⟩`; the energy's mixed estimator is exact
  in the limit; for diagonal observables the extrapolated value
  `2⟨O⟩_mixed − ⟨O⟩_var` corrects the first-order bias.

None is adopted.

## Theorem 1 — control on the fine torus

The fine `Z_4³` torus has 9600 ice states in 937 flip classes, the largest
of 864 (open PR 9072). Walkers start in the largest class.
- Exact ground energy −9.0267; projector −9.0412 ± 0.0149.
- Exact mixed flippable number `⟨ψ_G|N|ψ₀⟩/⟨ψ_G|ψ₀⟩ = 10.500`; projector
  10.496 ± 0.031.
- Exact pure `⟨ψ₀|N|ψ₀⟩ = 10.124`; variational 10.907; extrapolated
  `2 × 10.496 − 10.907 = 10.085`.

So the walk, the weights, the reconfiguration and the estimators reproduce
exact diagonalization. ∎

## Theorem 2 — energies on the coarse tori

With populations 100, 80, 60 and projection time 16 in units of `1/g`,
discarding the first third:

| torus | variational | projector | gain | halves apart |
|---|---|---|---|---|
| 4³ | −0.2766 | −0.2926 ± 0.0003 | 5.81% | 2.8 σ |
| 6³ | −0.2806 | −0.2883 ± 0.0003 | 2.76% | 0.7 σ |
| 8³ | −0.2797 | −0.2871 ± 0.0002 | 2.65% | 1.9 σ |

The projector energy is a variational-principle lower step from the Jastrow
energy in every case, and the 6³ and 8³ values agree to 0.4%. The 4³ torus
has the largest finite-size shift and the least settled halves. ∎

## Diagnostic — flippable density and plaquette structure factors

Variational / mixed / extrapolated, by size:

| torus | flippable density | `S(π,π,π)/N_p` | halves |
|---|---|---|---|
| 4³ | 0.295 / 0.314 / 0.333 | 0.274 / 0.284 ± 0.008 / 0.294 | 0.274, 0.293 |
| 6³ | 0.300 / 0.307 / 0.314 | 0.295 / 0.300 ± 0.010 / 0.305 | 0.280, 0.320 |
| 8³ | 0.302 / 0.305 / 0.309 | 0.285 / 0.288 ± 0.014 / 0.291 | 0.296, 0.280 |

On 8³ the mixed structure factor at `(0,0,0), (π,0,0), (π,π,0)` is 0, 0.080,
0.211. A separate longer run (30 and 24 units of `1/g` on 6³ and 8³) gave the
same window, 0.27–0.34 across imaginary-time quarters, with no drift.

## What this means for the lanes

- **Photon lane.** The variational picture of open PR 9146 survives the
  projection: the pure-ring ground state lowers its energy by a few percent
  relative to the best weighted-ice state, raises the flippable density
  slightly, and shows no plaquette order at the high-symmetry wavevectors up
  to 8³. Within these sizes nothing distinguishes it from the class of the
  Rokhsar–Kivelson point; the finite-size gap and the photon dispersion,
  which would, are not computed here.
- **Prior art for orientation.** The diamond-lattice quantum dimer model is
  ordered at pure kinetic coupling (Sikora, Pollmann, Shannon, Penc and Fulde
  2011); pyrochlore quantum spin ice is a U(1) liquid at pure ring exchange
  (Shannon, Sikora, Pollmann, Penc and Fulde 2012). The cubic-lattice
  spin-1/2 ice model at `V = 0` has, to this note's knowledge, no prior
  determination; these diagnostics lean the same way as the pyrochlore case.

## What stays open

- The phase: larger tori, the finite-size gap (from the imaginary-time decay
  of the projected energy), the photon dispersion, and order at wavevectors
  other than the four probed.
- The extent of the Coulomb phase in `V/g`.

## Prior art

Rokhsar and Kivelson 1988; Trivedi and Ceperley 1990 (Green's function Monte
Carlo for lattice models); Sorella 1998 (stochastic reconfiguration);
Hermele, Fisher and Balents 2004; Sikora, Pollmann, Shannon, Penc and Fulde
2011; Shannon, Sikora, Pollmann, Penc and Fulde 2012; Wiese 2013. All cited
as prior art, not as premises.

## Checks

The runner has 3 checks and all pass in about 75 seconds, single-threaded.

| Check | Result |
|---|---|
| Fine-torus control | 9600 / 937 / 864; energy −9.0412(149) vs −9.0267; mixed `N` 10.496(31) vs 10.500; extrapolated 10.085 vs pure 10.124. |
| Energies | The table above; every projector energy at or below the variational one within 2 σ; halves within 3 σ. |
| Observables | The table above; errors below 0.01 (density) and 0.05 (structure factors); halves within 3 σ. |

## Independent check

None yet. The runner was rerun from a clean shell; seeded Monte Carlo
reproduces the cached numbers. While building this block the loop sampler of
open PR 9146 was found to count only counter-clockwise flippable plaquettes
at `α > 0`; that block has been corrected, and its variational numbers now
agree with this runner's independently written sampler (both against the
exact all-states average on the fine torus).

## What this does not do

- It adopts no clause, Gauss law or guiding function.
- It claims no phase of the pure-ring point and no thermodynamic limit.
- Its diagonal observables carry the guiding-function bias of mixed and
  extrapolated estimators; only the energy is bias-free in the limit.
