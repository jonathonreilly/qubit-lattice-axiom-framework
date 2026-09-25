---
claim_id: ring_model_winding_sector_splittings_resolved_on_the_small_tori_and_a_multi_exponential_relaxation_at_the_pure_ring_point_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Setting, all supplied and none adopted: spin-1/2 link fields on the cubic lattice with the exact vertex Gauss law (cubic ice) and the covariant plaquette clause -g (U + U^dag) at V = 0 (open PRs 9066, 9072); the guided continuous-time projector Monte Carlo of open PR 9148. Finite diagnostics. (i) Winding sectors: the flux W_a through a slab is the same for every slab of an ice state (spread 0 over all samples) and is conserved by plaquette flips; the canonical zero-winding ice state sigma(v,x) = (-1)^{v_y}, sigma(v,y) = sigma(v,z) = (-1)^{v_x} with q directed x-lines reversed is ice with W = (2q, 0, 0); after winding-preserving loop equilibration, the projector gives on the 4^3 torus E_0(0) = -56.229 +- 0.079, E_0(1) = -55.417 +- 0.052, dE(1) = 0.811 +- 0.095, dE(1) L = 3.25 +- 0.38, dE(2)/dE(1) = 2.75, and on the 6^3 torus E_0(0) = -187.211 +- 0.084, E_0(1) = -186.863 +- 0.103, dE(1) = 0.348 +- 0.133, dE(1) L = 2.09 +- 0.80; the unconstrained uniform-ice flux second moments <Phi_x^2> are 1.393 and 2.033. (ii) Walkers started in the zero-winding uniform ice ensemble relax to E_0 per plaquette -0.2928(1), -0.2892(1), -0.2874(0) on 4^3, 6^3, 8^3 (open PR 9148: -0.2926, -0.2883, -0.2871); the relaxation is not a single exponential: effective rates 2.04, 2.42, 1.88 on tau in [0.3, 0.7] and 1.92, 0.47, 0.58 on [1.0, 2.5]. No gap, no phase and no thermodynamic limit is claimed; the one-quantum splitting is resolved on 4^3 (8.5 standard errors), marginal on 6^3 (2.6), and its 1/L scaling is consistent between the two sizes within errors."
upstream_dependencies:
  - minimal_axioms
runner: scripts/ring_model_winding_sector_splittings_and_imaginary_time_gap_at_the_pure_ring_point_2026_09_24.py
---

# Winding-sector splittings resolved on the small tori, and a multi-exponential relaxation, at the pure-ring point

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** finite diagnostics of a supplied model; unaudited.

## Result

Open PR 9148 left two Coulomb-phase diagnostics open for the ring model at
`V = 0`: the energy cost of a flux quantum threading the torus, which falls
as `1/L` in a Coulomb phase, and the finite-size gap. This note computes the
first on the 4³ and 6³ tori and reports what the second turns out to be at
this precision.
- **Fixed-flux sectors are exact and constructible.** The flux through a
  slab is slab-independent for every ice state and conserved by plaquette
  flips. A canonical zero-winding ice state, with directed lines reversed for
  each flux quantum, gives every sector a starting point, equilibrated by
  winding-preserving loop updates.
- **The one-quantum splitting is resolved on 4³ and marginal on 6³.**
  `dE(1) = 0.811 ± 0.095` on 4³ and `0.348 ± 0.133` on 6³, so
  `dE(1)·L = 3.25 ± 0.38` and `2.09 ± 0.80`: consistent with a `1/L` law
  between the two sizes within errors, and with `dE(2)/dE(1) = 2.75` against
  the quadratic value 4 on 4³.
- **The relaxation from uniform ice is multi-exponential.** The effective
  rate is about 2 on every size at early imaginary time and about 0.5 on 6³
  and 8³ at later times; no single gap can be read off, and the note claims
  none. The late-time energies reproduce open PR 9148's projector energies to
  within 0.001 per plaquette, a third independent run of the same numbers.

So the flux-quantum diagnostic points the same way as the structure factors
of open PRs 9146 and 9148, toward a Coulomb-like pure-ring point, but with
two sizes and one marginal point it does not decide. The gap needs a
different estimator.

## Setting and decision points

- **D-gauss, D-roles, D-ring (open PRs 9066, 9072).** Link qubits at link
  sites of the doubled lattice; the exact vertex Gauss law, three in and
  three out; the covariant plaquette clause `−g (U + U†)`; `V = 0`.
- **The projector (method).** The guided continuous-time Green's function
  Monte Carlo of open PR 9148, guiding function `exp(0.2 N_flip)`.
- **Sector construction (method).** The ice state
  `σ(v,x) = (−1)^{v_y}, σ(v,y) = σ(v,z) = (−1)^{v_x}` has zero winding; each
  reversal of a directed `x`-line (a row of odd `y`) adds two to `W_x` and
  keeps the ice rule. Winding-preserving loop updates (a loop is rejected if
  it changes any `W_a`) equilibrate each sector.

None is adopted.

## Theorem 1 — winding sectors and the flux-quantum splitting

- **Slab independence.** Over every uniform-ice sample on the 4³, 6³ and 8³
  tori the flux through a slab is the same for all slabs of the same
  orientation (spread 0), so `W = (W_x, W_y, W_z)` is a property of the
  state; plaquette flips change no slab sum. The canonical states are ice
  and have `W = (2q, 0, 0)` for `q` reversed lines.
- **4³** (population 120, projection 24/g, first third discarded):
  `E_0(0) = −56.229 ± 0.079`, `E_0(1) = −55.417 ± 0.052`,
  `dE(1) = 0.811 ± 0.095`, `dE(1)·L = 3.25 ± 0.38`, `dE(2)/dE(1) = 2.75`.
- **6³** (population 150, projection 40/g): `E_0(0) = −187.211 ± 0.084`,
  `E_0(1) = −186.863 ± 0.103`, `dE(1) = 0.348 ± 0.133`,
  `dE(1)·L = 2.09 ± 0.80`.
- The unconstrained uniform-ice flux second moments `⟨Φ_x²⟩` are 1.393 (4³)
  and 2.033 (6³).

In a Coulomb phase the flux quantum costs `∝ Φ²/L`; the two products
`dE(1)·L` agree within errors and the quadratic ratio is 2.75 against 4. This
is consistent with, and does not establish, the Coulomb form. ∎

## Diagnostic — the relaxation from uniform ice

Walkers start in the zero-winding uniform ice ensemble (the RK ground
state) and are projected with the guiding function; the mixed energy
`E(τ)` relaxes to the ground energy.

| torus | start | `E_0` per plaquette | open PR 9148 | rate on `[0.3, 0.7]` | rate on `[1.0, 2.5]` |
|---|---|---|---|---|---|
| 4³ | −0.2825 | −0.2928 ± 0.0001 | −0.2926 | 2.04 | 1.92 (13 points) |
| 6³ | −0.2771 | −0.2892 ± 0.0001 | −0.2883 | 2.42 | 0.47 |
| 8³ | −0.2769 | −0.2874 ± 0.0000 | −0.2871 | 1.88 | 0.58 |

The early rate, about 2 in units of `g`, is the same on every size: a local
relaxation. The late rate on 6³ and 8³ is about 0.5, and on 4³ the signal is
gone before the late window. No single exponential describes the curve, so
no gap is extracted; the lowest excitation energy in the symmetric sector
needs a dedicated estimator (a correlation function, or a projection onto
excited states). The 6³ energy sits 0.0009 below open PR 9148's, three of
that block's standard errors, the expected size of its population-control
bias at 80 walkers.

## What this means for the lanes

- **Photon lane.** Three finite diagnostics now lean the same way at the
  pure-ring point: no plaquette order to 8³ (open PRs 9146, 9148), a
  flux-quantum cost compatible with `1/L` between 4³ and 6³, and a quadratic
  ratio near 4. None decides; the missing piece is the photon itself, its
  dispersion or the gap, which the relaxation estimator here cannot give.
- **What the framework supplied.** The Gauss law, the ring and the point
  `V = 0` are decision points; the sector construction and the projector
  are methods.

## What stays open

- The gap and the photon dispersion (a correlation-function or
  excited-state estimator).
- Flux-quantum splittings on 8³ and beyond, at a precision that resolves
  `1/L` against alternatives.
- The phase, and the extent of the Coulomb phase in `V/g`.

## Prior art

Rokhsar and Kivelson 1988; Trivedi and Ceperley 1990; Hermele, Fisher and
Balents 2004 (Coulomb phase, flux sectors); Sikora, Pollmann, Shannon, Penc
and Fulde 2011; Shannon, Sikora, Pollmann, Penc and Fulde 2012. All cited as
prior art, not as premises.

## Checks

The runner has 2 checks and all pass in about 4 minutes, single-threaded.

| Check | Result |
|---|---|
| Winding sectors | Spread 0; canonical states ice with the intended flux; the table above; 4³ resolved at 8.5 σ, 6³ at 2.6 σ. |
| Relaxation | The table above; energies within 0.001 of open PR 9148; early and late rates. |

## Independent check

None yet. The runner was rerun from a clean shell; seeded Monte Carlo
reproduces the cached numbers. A first version of this block reported a
fitted "gap" from a noise-dependent window; that number moved by a factor of
two between runs and was withdrawn in favour of the fixed-window rates above.

## What this does not do

- It adopts no clause, Gauss law or method.
- It claims no gap, no phase and no thermodynamic limit.
- The flux-quantum splitting is resolved on one torus and marginal on a
  second; the 8³ torus carries only the relaxation runs.
