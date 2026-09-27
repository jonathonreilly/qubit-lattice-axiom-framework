---
claim_id: one_light_cone_under_interactions_on_the_continuous_time_surface_the_walkers_and_a_scalars_speeds_separate_at_second_order_hypercubic_ticks_are_a_sufficient_protection_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "Supplied comparator, none adopted: the campaign's walker (Bloch s(k).sigma; eight nodes, four Dirac flavours) and a lattice scalar (Omega^2 = mu^2 + sum 4 sin^2(q_j/2)), both of speed 1, coupled by g phi_x eps_x psi_x^dag psi_x in Hamiltonian (continuous) time on Z^3, with a scalar mass counterterm keeping the renormalised mass positive. Pairing nodes k and k+(pi,pi,pi) makes this the Lorentz-invariant Yukawa coupling of Dirac fermions. (T1) At second order the two speeds separate by a number that survives the continuum limit: v_psi - v_phi = +0.0263 g^2 when the scalar's physical mass is sent to zero after p -> 0 (walker -0.011675 g^2, scalar -0.0379 g^2), and +0.0284 g^2 at zero scalar mass (walker -0.009564 g^2); 2.4e-3 at g^2/4 pi = 1/137. Numerical evidence (grid quadratures, refined by two independent checks), not a certified bound. (T2) Sufficiency only: under the hyperoctahedral group of Z^4 (the approved kinetic_isotropy_primitive's surface) a scalar quadratic kinetic form is c(nu^2 + |q|^2), and a gauge vector's gauge-invariant form is unique (Maxwell's F^2), while the space-cubic surface leaves a free speed in both; the spin-2 member is treated in the companion note of the same date. Other protections (supersymmetry, strongly coupled fixed points, compositeness) are not excluded; the gravity member's own loop is not computed."
upstream_dependencies:
  - minimal_axioms
  - kinetic_isotropy_primitive
runner: scripts/one_light_cone_under_interactions_continuous_time_surface_speeds_separate_at_second_order_2026_09_27.py
---

# One light cone under interactions on the continuous-time surface: the walker's and a scalar's speeds separate at second order; hypercubic ticks are a sufficient protection

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** grid quadratures refined by two independent checks, and exact
symmetry counts; unaudited.

## In one paragraph

Start two fields at exactly the same speed of light on the lattice, with time
kept separate from the three space directions, and let them interact. Each
one's speed is corrected by its interaction with the other, and the
corrections differ. The gap is about a quarter of a percent at
electromagnetic strength, and it does not shrink when the lattice is made
finer. Experiment says different particles share one speed limit to at least
fifteen decimal places.

Something must therefore bring the speeds together. It could be a retuning at
each order, or a symmetry. One symmetry that does it is the one the framework
approved in June: a tick grained like an edge, time as a fourth lattice
direction. On that surface a scalar's kinetic term, and a gauge field's, can
only come with one speed. Other protections are not ruled out here.

## Why this question

The gravity lane's landed blocks 134–136 found one light cone for the walker
and the member if and only if `α = K/4`. That is a statement at first order
in the fields, a tree-level identity. The Standard Model and gravity need one
light cone for every species, and experiment bounds the differences at the
`1e-15` level or better (external, reference only). The question here is
whether identities of this kind survive interactions on the surface the
campaign uses.

**Prior art in the repository.** The June lane framed this as the "Collins
gate":
- `EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md` is
  a conditional packet with a supplied, IR-attractive one-loop flow. It
  records that the continuous-time one-loop coefficient was not computed.
- `EMERGENT_LORENTZ_SPATIAL_BZ_POWER_MIXING_BOUNDARY_THEOREM_NOTE_2026-06-18.md`
  gives the spatial-only channel and leaves the coefficient open.
- `EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md`
  proves the protection on the hypercubic (B4) tick surface. That surface is
  now supplied by the approved `kinetic_isotropy_primitive`.

This note supplies the missing coefficient for the campaign's own walker
(T1). It extends the symmetry count to gauge vectors (T2). The spin-2 member
is in the companion note of the same date. The literature is reference only:
Collins, Perez, Sudarsky, Urrutia and Vucetich 2004; anisotropic lattice QCD
tuning.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`). `Z^3` with proper cubic
  rotations; the memo supplies no time metric, dynamics or fields. Every
  field and interaction below is a supplied comparator. None is adopted.
- **Walker.** `H_psi = sum_x sum_j [psi_x^dag (sigma_j/2i) psi_{x+e_j} + h.c.]`,
  Bloch `s(k).sigma`, eight nodes of speed 1.
- **Scalar.** `Omega^2 = mu^2 + sum_j 4 sin^2(q_j/2)`, speed 1.
- **Coupling.** `g sum_x phi_x eps_x psi_x^dag psi_x`, `eps_x = (-1)^{x1+x2+x3}`.
  It pairs each node with its partner at `k + (pi,pi,pi)`, so the low-energy
  theory is four Dirac flavours with the Lorentz-invariant Yukawa coupling.
- **Counterterm and order of limits.**
  - The fermion loop lowers the scalar's mass squared by `g^2 chi(0,0)`,
    with `chi(0,0) = 0.910688`.
  - Keeping the vacuum `phi = 0` stable as the scalar gets light therefore
    needs a mass counterterm: `mu^2` is the bare mass, and the renormalised
    mass is kept positive. That is the familiar scalar-mass tuning, flagged
    and not solved here.
  - At second order the speed coefficients are unaffected by the
    counterterm; the differences are `O(g^4)`.
  - Limits are taken in the order `p -> 0`, then infinite volume, then the
    scalar's physical mass to zero. The other order is reported too.
- **Speeds.**
  - Walker: `v_psi = dE/dp` at `p -> 0` on the on-shell second-order energy
    of a particle added to the filled sea.
  - Scalar: `v_phi^2 = (1 - g^2 B)/(1 - g^2 A)`, where `A`, `B` are the
    `nu^2`, `q^2` coefficients of its Euclidean self-energy. The
    Lorentz-invariant nonanalytic part cancels in `A - B`.

## T1 — the speeds separate at second order

*The walker.* Second-order perturbation theory above the filled sea, with the
one blocked vacuum process subtracted:

`delta E(p) = g^2 < (1/2 Omega_q) [ O_1/(e_p - e_{p-q} - Omega_q) + O_2/(e_p + e_{p+q} + Omega_q) ] >_q`

with `e = |s|`, `O_1 = (1 - s^(p).s^(p-q))/2` and `O_2 = (1 + s^(p).s^(p+q))/2`.

The Euclidean Feynman-diagram form, computed independently, reproduces this
term by term. The values of `delta E/p`:
- `-0.0096707`, `-0.0110696`, `-0.0115076` and `-0.0116301` at
  `mu = 1, 1/2, 1/4, 1/8`, reproduced to all digits by the independent check.
- The limit `mu -> 0` taken after `p -> 0` is `-0.011675(1) g^2`. The
  independent check scanned `mu` down to `1/512`. This runner's two-point fit
  gives `-0.01165`: pure `mu^2` scaling sets in only below `mu = 1/16`.
- At `mu = 0` exactly the value is `-0.009564 g^2`. The difference equals the
  same integral for one continuum Dirac fermion with a cutoff on spatial
  momentum only. So the Hamiltonian-time artefact is already present in the
  continuum Yukawa theory once its cutoff treats time differently from
  space.

*The scalar.* The sea's Euclidean vacuum polarisation is

`chi(nu, q) = < ((1 + s^(k).s^(k+q))/2) 2E/(nu^2 + E^2) >_k`,  `E = |s(k)| + |s(k+q)|`,

and the scalar's kernel is `nu^2 + Omega^2 - g^2 chi`. The sign is checked by
the static limit, the sea's energy curvature under a staggered mass.

`A - B = lim [chi(r,0) - chi(0,r)]/r^2 = -0.07589`:
- `-0.07479`, `-0.07556`, `-0.07579`, `-0.07586` and `-0.07588` at
  `r = 0.2, 0.1, 0.05, 0.025, 0.0125` (independent check);
- the sol referee's analytic small-momentum evaluation gives `-0.0758907`;
- this runner's `192^3` grid gives `-0.0755`, under-resolved at `r = 0.05`.

Hence `delta v_phi = -0.0379 g^2`.

*Result.*
- `v_psi - v_phi = +0.0263 g^2`, scalar physical mass sent to zero after
  `p -> 0`.
- `+0.0284 g^2` at zero scalar mass.
- With `g^2/4 pi = 1/137`, about `2.4e-3`.
- Nonzero in both orders of limits. This is numerical evidence without a
  certified error bound.

## T2 — hypercubic ticks are a sufficient protection

*Statement (exact counts).*

| field kernel | space-cubic surface (with time reversal) | hypercubic `Z^4` surface |
|---|---|---|
| scalar quadratic form in `(nu, q)` | `a nu^2 + b |q|^2`: two free coefficients | `c (nu^2 + |q|^2)` |
| gauge vector (`A -> A + k lambda`) | 7 invariant, 2 gauge-invariant: a free speed | 3 invariant, 1 gauge-invariant, proportional to Maxwell's `F^2` |
| spin-2 member (`h -> h + k xi^T + xi k^T`) | 26 invariant, 2 gauge-invariant: `β = −α`, free wave speed | 9 invariant, 1 gauge-invariant, Fierz–Pauli (companion note) |

So on the approved surface the kinetic terms of these fields share one cone
by symmetry. Loop corrections that respect the symmetry and the gauge
invariance can change only the overall normalisation.

*Limits of T2.*
- **Spinors** are not re-classified here. The June B4 note treats the
  canonical staggered kinetic form.
- **A vector without gauge invariance** admits a second hypercubic invariant,
  `sum_mu (∂_mu A_mu)^2`, at dimension 4.
- **Additional hypotheses.** B4 by itself does not give reflection
  positivity, a transfer matrix, a symmetric vacuum or particle poles. Those
  are further hypotheses (the June reflection-positivity notes construct them
  for the free staggered fermion).

## What this does and does not say

What it says:
- On the continuous-time surface the campaign uses, the cubic symmetry of
  space alone does not protect one light cone. The comparator's two fields
  separate at second order by `+0.026–0.028 g^2`. That is the coefficient the
  June Collins-gate notes left open, computed for the campaign's walker.
- On the approved `kinetic_isotropy_primitive` surface, scalar, gauge-vector
  and spin-2 kinetic terms are forced onto one cone (T2 and the companion
  note).
- For the gravity campaign: on its current surface the member's wave speed is
  a free parameter of its gauge-invariant action (companion note, T1).
  Nothing in that surface's symmetry fixes `α = K/4`. Whether loops shift it
  requires the member's own loop, which is not computed here.

What it does not say:
- It does not say the hypercubic surface is necessary. Other protections are
  not excluded: supersymmetry (not in the axioms), a strongly coupled or
  scale-dependent IR fixed point, compositeness, or a small shared set of
  counterterms.
  - The June packet's IR attraction with a constant `γ = O(α)` would reduce
    a Planck-scale gap by only `10^{-19γ}`: about `0.8` for `γ = 0.005` and
    `0.01` for `γ = 0.1`.
  - A strongly coupled flow averaging about `0.65` in its base-10 exponent
    over 19 decades would suffice. It is not excluded here.
- It does not compute the member's loop.
- It does not show that the formation reading's level time can be put on the
  hypercubic surface.

## Independent checks

- **Claude Fable 5.1 subagent.** Same vendor family; not a referee. It
  computed Euclidean Feynman diagrams with residue frequency integrals and
  adaptive Brillouin-zone quadrature, without reading the runner. Verdict:
  confirmed with corrections, all applied here.
  - The refined limits: walker `-0.011675(1)`, scalar `A - B = -0.07589(1)`,
    gap `+0.0263`.
  - The order-of-limits split (`-0.009564` at `mu = 0`) and its continuum
    spatial-cutoff origin.
  - The four-flavour count.
  - `chi(0,0) = 0.910688` (the runner's grid gives `0.910626`).
  - The leading nonanalytic term tested and found Lorentz-invariant.
- **Codex `gpt-5.6-sol` referee** (another vendor family). Verdict on the
  first version: fails as a framework-level necessity claim; the narrow
  one-loop result stands with numerical and hypothesis corrections.
  - Its analytic evaluation gives the gap `+0.0262701 g^2`.
  - Applied: sufficiency, not necessity (the title and framing changed);
    the gravity statement now rests on the companion note's tree-level
    count, not on this loop; the vacuum-stability counterterm and the order
    of limits; T2 restricted to scalar kernels, then extended to gauge
    vectors by an exact count; the IR-attraction statement softened.
  - Its "compositeness or shared counterterms" routes are listed above.

## Reproduction

```bash
python3 scripts/one_light_cone_under_interactions_continuous_time_surface_speeds_separate_at_second_order_2026_09_27.py
```

Expected: `TOTAL: PASS=9 FAIL=0` (about 15 s). The runner's grid values
(`-0.01165`, `-0.0755`) are coarser than the refined values quoted above.
