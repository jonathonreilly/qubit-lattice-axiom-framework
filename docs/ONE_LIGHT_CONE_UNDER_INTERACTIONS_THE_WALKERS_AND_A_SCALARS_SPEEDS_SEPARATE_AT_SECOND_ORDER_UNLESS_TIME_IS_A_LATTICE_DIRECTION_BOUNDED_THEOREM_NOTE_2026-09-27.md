---
claim_id: one_light_cone_under_interactions_the_walkers_and_a_scalars_speeds_separate_at_second_order_unless_time_is_a_lattice_direction_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "Supplied comparator, none adopted: the campaign's walker (Bloch s(k).sigma) and a lattice scalar (Omega^2 = mu^2 + sum 4 sin^2(q_j/2)), both of speed 1, coupled by g phi_x eps_x psi_x^dag psi_x, in Hamiltonian (continuous) time on Z^3. Pairing nodes k and k+(pi,pi,pi) makes this the Lorentz-invariant Yukawa coupling of Dirac fermions. (T1) At second order the walker's speed shifts by delta v_psi, whose continuum limit (scalar mass mu -> 0 in lattice units) is -0.01165 g^2; the scalar's speed shifts by delta v_phi = (1/2) lim [chi(r,0) - chi(0,r)]/r^2 = -0.0377 g^2, where chi is the sea's Euclidean vacuum polarisation. The speeds separate by +0.0261 g^2, a number that does not vanish as the lattice spacing goes to zero (2.4e-3 at g^2/4 pi = 1/137). (T2, restating the B4 note's group theory, re-checked) With only the cubic group of Z^3 and time reversal the invariant quadratic form in (nu, q) has two free coefficients; under the hyperoctahedral group of Z^4 (the surface of the approved kinetic_isotropy_primitive) it is a multiple of nu^2 + |q|^2. The current gravity campaign's continuous-time walker is off that surface, so its tree-level cone identity alpha = K/4 is unprotected there. Grid-converged quadratures and a mu^2 extrapolation; one interaction at second order; the gravity lane's member coupling is not computed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/one_light_cone_under_interactions_walker_and_scalar_speeds_separate_at_second_order_2026_09_27.py
---

# One light cone under interactions: the walker's and a scalar's speeds separate at second order unless time is a lattice direction

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** grid-converged quadratures, an extrapolation in the scalar mass, and
an exact symmetry lemma; unaudited; independent checks recorded below.

## In one paragraph

Start two fields at exactly the same speed of light on the lattice and let
them interact. Each one's speed is corrected by its interaction with the
other, and the corrections differ. On a lattice where time is not one of the
lattice directions, nothing forces the corrections to be equal. The gap is
about a quarter of a percent at electromagnetic strength, and it does not
shrink when the lattice is made finer. Experiment says different particles
share one speed limit to at least fifteen decimal places. So either the
lattice's rule is tuned again at every order for every pair of fields, or a
symmetry does it. The symmetry that does it is treating time as a fourth
lattice direction, in the rule's Euclidean form.

## Why this question

The gravity lane's landed blocks 134–136 found one light cone for the walker
and the member if and only if `α = K/4`. That is a statement at first order
in the fields, a tree-level identity. The Standard Model and gravity need one
light cone for every species, and experiment bounds the differences at the
`1e-15` level or better. The question here is whether a tree-level identity
of this kind survives interactions on the framework's lattice.

**Prior art in the repository.** The June lane framed this as the "Collins
gate":
- `EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md` is
  a conditional packet. In it, a supplied one-loop flow makes the speed
  difference IR-attractive and the cubic group reduces it to one scalar. It
  records that the one-loop coefficient on the continuous-time surface was
  not computed.
- `EMERGENT_LORENTZ_SPATIAL_BZ_POWER_MIXING_BOUNDARY_THEOREM_NOTE_2026-06-18.md`
  proves the spatial-only channel. It likewise leaves the coefficient open.
- `EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md`
  proves the protection on the B4 (hypercubic) tick surface. That surface is
  now supplied by the owner-approved `kinetic_isotropy_primitive`: "the
  emergent evolution tick is grained on the same footing as the spatial
  lattice edge", `c_t = c_s`.

T2 below restates the B4 note's group theory, re-checked independently. The
new content is T1: the one-loop coefficient on the continuous-time surface,
for the campaign's own walker. The consequence drawn in the last section is
new as well. The literature on this effect is reference only: Collins,
Perez, Sudarsky, Urrutia and Vucetich 2004; the separate quark and gluon
anisotropy tuning of anisotropic lattice QCD.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`). `Z^3` with proper cubic
  rotations; the memo supplies no time metric. Every field and interaction
  below is a supplied comparator.
- **Walker.** `H_psi = sum_x sum_j [psi_x^dag (sigma_j/2i) psi_{x+e_j} + h.c.]`,
  Bloch `s(k).sigma`, with eight nodes, each of speed 1.
- **Scalar.** `H_phi = sum (pi_x^2/2) + (1/2) sum_{x,j} (phi_{x+e_j} - phi_x)^2
  + (mu^2/2) sum phi_x^2`, `Omega^2 = mu^2 + sum_j 4 sin^2(q_j/2)`, speed 1.
- **Coupling.** `g sum_x phi_x eps_x psi_x^dag psi_x`, `eps_x = (-1)^{x1+x2+x3}`.
  It shifts momentum by `Q = (pi,pi,pi)`, pairing each right-handed node with
  a left-handed one. The pair is a Dirac fermion, and `eps` acts as its
  `psi-bar psi`. In the continuum this is the Lorentz-invariant Yukawa
  theory: with a Lorentz-invariant regulator both speeds stay exactly 1.
- **Vacuum.** The filled negative band (the walker's sea) and the scalar's
  ground state.
- **Speeds.**
  - Walker: `v_psi = dE/dp` at `p -> 0` on the on-shell second-order energy
    `E(p) = |s(p)| + delta E(p)` of a particle added to the sea.
  - Scalar: `v_phi^2 = (1 - g^2 B)/(1 - g^2 A)`, where `A`, `B` are the
    `nu^2`, `q^2` coefficients of its Euclidean self-energy.

## T1 — the speeds separate at second order

*The walker.* Second-order perturbation theory, above the filled sea, with the
one blocked vacuum process subtracted, gives

`delta E(p) = g^2 < (1/2 Omega_q) [ O_1/(e_p - e_{p-q} - Omega_q) + O_2/(e_p + e_{p+q} + Omega_q) ] >_q`

with:
- `e = |s|`;
- `O_1 = (1 - s^(p).s^(p-q))/2`, the overlap of the upper band at `p` with
  the upper band at `p - q + Q`;
- `O_2 = (1 + s^(p).s^(p+q))/2`, the blocked vacuum process;
- `s^` the unit vector of `s`.

Values:
- `delta E(p)/p` at `mu = 1/2` is `-0.011069 g^2`, the same on `160^3` and
  `224^3` to `2e-5`.
- In the scalar mass, `-0.00967`, `-0.01107`, `-0.01150` and `-0.01163` at
  `mu = 1, 1/2, 1/4, 1/8`.
- A fit `a + b mu^2` through `mu = 1/2, 1/4` predicts `-0.011613` at
  `mu = 1/8`; measured `-0.011630`.
- The continuum limit is `delta v_psi = -0.01165 g^2`.

`delta E(p)` vanishes linearly as `p -> 0`, so no mass is generated. The
coupling is odd under `phi -> -phi` with the chiral shift.

*The scalar.* The sea's Euclidean vacuum polarisation for the staggered
bilinear is

`chi(nu, q) = < ((1 + s^(k).s^(k+q))/2) 2E/(nu^2 + E^2) >_k`,  `E = |s(k)| + |s(k+q)|`,

and the scalar's kernel is `nu^2 + Omega^2 - g^2 chi`. The sign is checked by
the static limit: `chi(0,0) = <1/|s|> = 0.910626` equals minus the curvature
of the sea's energy under a uniform staggered mass.

The massless sea makes `chi` nonanalytic at small `(nu, q)`. In the
continuum that part depends only on `nu^2 + q^2`, so it cancels in

`A - B = lim [chi(r,0) - chi(0,r)]/r^2 = -0.0755`

(`192^3`: `-0.07538` at `r = 0.05`, `-0.07548` at `r = 0.1`). Hence
`delta v_phi = (A - B)/2 = -0.0377 g^2`. It does not depend on `mu`.

*Result.* `v_psi - v_phi = +0.0261 g^2`. With `g^2/4 pi = 1/137` that is
`2.4e-3`.

## T2 — the symmetry that forces one cone (restating the B4 note)

*Statement.*
- A quadratic form in `(nu, q_1, q_2, q_3)` invariant under the cubic group
  of `Z^3` and time reversal has two free coefficients, `a nu^2 + b |q|^2`.
- A quadratic form invariant under the hyperoctahedral group of `Z^4`, which
  treats time as a fourth lattice direction, is `c (nu^2 + |q|^2)`.

*Proof.* The runner solves the invariance conditions exactly for all ten
coefficients (sympy). ∎

*Consequence.* Take a lattice theory whose Euclidean form is invariant under
the `Z^4` group. The dimension-4 kinetic term of every field is then
proportional to `nu^2 + |q|^2`. After the Euclidean-to-real-time
reconstruction (reflection positivity; the transfer matrix), every field
shares one cone at low energy, with no tuning. Violations of Lorentz
invariance start with dimension-6 terms and are suppressed by
`(energy x spacing)^2`.

This is why lattice QCD on isotropic lattices needs no speed-of-light
tuning. In Hamiltonian or anisotropic formulations, the time-to-space ratio
must be tuned separately for each field.

## What this does and does not say

What it says:
- On the continuous-time surface, one light cone does not survive
  interactions. The walker and a field it couples to separate at second order
  by `+0.026 g^2`, and the separation survives the continuum limit. This is
  the coefficient the June Collins-gate notes left open, computed for the
  campaign's walker.
- The June packet's IR attraction does not rescue it. That packet supplies
  the flow `d(Δv)/dl = -γ Δv` with `γ = O(α)`. Over the 19 decades from a
  Planck-scale lattice to 1 GeV this shrinks the gap by `10^{-19γ}`: about
  `0.8` for `γ = 0.005` (QED-like), and about `0.01` even for `γ = 0.1`. The
  bounds need `1e-12` relative to the one-loop gap.
- **The current gravity campaign runs on the continuous-time surface.** Its
  walker is `H = sum sin k_j sigma_j` in continuous time, with clocks and
  lapse in level time. That is off the surface of the approved
  `kinetic_isotropy_primitive`. So the campaign's tree-level cone identity
  (`α = K/4`) is unprotected where it currently lives. There are two ways to
  put it under protection:
  - **move the walker onto the B4 tick surface** that the approved primitive
    already names (one tick is one edge in form; a hypercubic Euclidean
    regulator; the reflection-positivity notes' two-step transfer matrix);
  - **accept a retuning** of the rule's constants for every pair of fields at
    every order. At electromagnetic strength the retuning must cancel the
    one-loop gap (`2.4e-3`) down to the external bounds, of order `1e-15`
    (reference only): about twelve decimal places.

What it does not say:
- It does not compute the member's (gravity's) own loop. Its coupling scales
  with energy, so the corrections differ in form. The mechanism (nothing ties
  the time and space coefficients) is the same.
- It does not show that the formation reading's level time can be put on the
  B4 surface. Records forming in level order treat time differently from
  space by construction. T2 says that this difference is exactly what makes
  one light cone a tuning.
- It does not rule out an unknown protecting mechanism. Supersymmetry is the
  known alternative, and it is not in the axioms.

## Independent checks

To be recorded after the independent checks return (see the PR body).

## Reproduction

```bash
python3 scripts/one_light_cone_under_interactions_walker_and_scalar_speeds_separate_at_second_order_2026_09_27.py
```

Expected: `TOTAL: PASS=8 FAIL=0` (about 10 s).
