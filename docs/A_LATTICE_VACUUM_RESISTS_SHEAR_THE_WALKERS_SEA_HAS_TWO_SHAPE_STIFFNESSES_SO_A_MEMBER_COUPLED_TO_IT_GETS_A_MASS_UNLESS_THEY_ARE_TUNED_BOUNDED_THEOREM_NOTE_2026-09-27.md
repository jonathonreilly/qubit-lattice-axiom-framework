---
claim_id: a_lattice_vacuum_resists_shear_the_walkers_sea_has_two_shape_stiffnesses_so_a_member_coupled_to_it_gets_a_mass_unless_they_are_tuned_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "Supplied comparator coupling, not adopted: the walker's hop along axis j carries sigma_a e_a^j with a constant inverse vielbein e (g^{-1} = e e^T); a shear is e = expm(eps/2), eps symmetric traceless, which keeps the proper volume per cell. (T1) Comparators: with a cutoff on the proper momentum the free sea's energy is independent of shear (change of variables); with a cutoff fixed in coordinate momentum (a ball) it is not, with isotropic stiffness 2E_0/15. (T2) The walker's filled lower band on Z^3 has energy per cell -1.19380 and shape stiffnesses c_E = -0.17793 (axis shears) and c_T = -0.14667 (face shears) in lattice units, converged; a direct 8^3 real-space diagonalisation agrees with the k-space formula, and the sheared spectrum differs from the unsheared one, so no unitary map of the matter relates them. Frame rotations change nothing. (T3) On the hypercubic tick surface (Euclidean Z^4, free lattice scalar, two metric couplings) the stiffnesses are c_3 ~ 0.10 and c_6 ~ 0.07-0.09 per site, time-space shears included; they depend on the mass. (T4) A complex boson with the walker's own dispersion cancels the shape energy at every shape; the forward-difference scalar does not. (T6) For free matter the stiffness belongs to the coupling, not the lattice: relabelling the zone by the volume-keeping flow of a divergence-free trigonometric field that is linear at the 8 nodes gives an exponentially local coupling under which the sea energy is exactly shear-independent and every node sees one sheared metric. (T7) Interactions bring it back: with that coupling, a nearest-neighbour density interaction's first-order energy has stiffness about 0.0019 V (axis) and 0.0049 V (face); on-site interactions stay blind at first order; and no zone relabelling that carries every momentum-conserving vertex along can be a small shear (it would be a continuous homomorphism of the torus, an integer matrix). (T5) With block 101's member, a stiffness c gives the member's spatially constant transverse-traceless modes omega^2 = c wbar/(2 alpha) (in GR's normalisation m^2 = 32 pi G c/a^4); untuned, |m| is 3.8 M_P at the Planck spacing and 1e-3 eV at a = 1e-19 m, 1e20 times the LIGO-Virgo-KAGRA bound (reference input), so c must be tuned to about 1e-40 (1e-104 at the Planck spacing) of its natural size. Free matter at one loop plus first order in one interaction; the member's own counterterms, higher orders, gauge fields, the shift and lapse sector, and finite wavelengths are not computed; other (many-body) constructions of a shear-blind coupling are not excluded."
upstream_dependencies:
  - minimal_axioms
  - kinetic_isotropy_primitive
  - if_the_members_leading_action_respects_the_hypercubic_tick_surface_it_is_unique_beta_equals_minus_alpha_and_alpha_equals_k_over_four_follow_bounded_theorem_note_2026-09-27
runner: scripts/lattice_vacuum_shape_stiffness_gives_the_member_a_mass_unless_tuned_2026_09_27.py
---

# A lattice vacuum resists shear: the walker's sea has two shape stiffnesses, so a member coupled to it gets a mass unless they are tuned

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** numerical identities and converged zone integrals; a supplied
comparator coupling; unaudited. Independent checks are recorded below.

## In one paragraph

A regular lattice has a shape. In a continuum, stretching space along one
axis while squeezing it along another, at fixed volume, is only a relabelling
of coordinates, and the vacuum's energy cannot notice it. On a fixed lattice
it can: the lattice's grain is fixed in coordinates, and the metric decides
how that grain looks in proper lengths. The campaign's walker sea does notice
it. Its energy changes by about 15% of its size per unit shear squared, with
different values for shears along the axes and across the faces. So the
vacuum behaves like a solid, not a fluid. Gravitational waves are shears of
space. A member (the campaign's gravity field) coupled to this vacuum
therefore gets a mass, or an instability, of the vacuum's size. With the
lattice at the Planck spacing, that is about four Planck masses. At the
coarsest spacing colliders allow, it is still `10^20` times the bound from
gravitational waves.

For free matter this can be engineered away. A cleverer coupling relabels
momentum space instead of stretching the hops, and then the free vacuum
cannot feel a shear at all. Interactions undo that. The relabelling does not
respect how momenta add when particles collide, and a nearest-neighbour
interaction makes the vacuum stiff again at first order. For interacting
matter nothing known forbids the stiffness, so it must be tuned away, like the
cosmological constant, for two more numbers.

## Why this question

The viability map's decision 2 (the hypercubic tick surface) listed loops as
not settled. The panel's gravitation lens proposed inducing the member from
the sea. The map's own assessment was by reasoning only: it said lattice
matter is not invariant under infinitesimal rotations, so loops should spoil
the member.

The cleanest place to test that is zero wavelength. A spatially constant,
volume-preserving change of the metric is pure gauge in general relativity.
Its energy cost is the member's mass term for the constant transverse-traceless
(TT) modes, which is what gravitational-wave dispersion bounds. This note
computes it for the campaign's own matter.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`): `Z^3` with proper cubic
  rotations. The memo supplies no member and no metric coupling.
- **The walker:** `H = sum_x sum_j [psi_x^dag (sigma_j/2i) psi_{x+e_j} + h.c.]`,
  with symbol `sum_j sigma_j sin k_j`. Its sea is the filled lower band, with
  energy per cell `-<|s(k)|>`, where `s = (sin k_1, sin k_2, sin k_3)`.
- **Supplied comparator coupling** (not fixed by the axioms or the campaign):
  - The hop along axis `j` carries `sigma_a e_a^j` in place of `sigma_j`.
  - `e` is a constant inverse vielbein, and the inverse metric is
    `g^{-1} = e e^T`.
  - The sea's energy per cell is `E(e) = -<|e^T s(k)|>` over the zone.
  - A spatial coupling of this kind is needed physically. The member must
    couple to the spatial metric for light to bend by the observed amount
    and for gravitational waves to act on matter.
- **Shear:** `e = expm(eps/2)` with `eps` symmetric and traceless, so
  `g^{-1} = expm(eps)`. The proper volume per cell is unchanged.
- **Shape stiffness:** for a unit shear (`tr eps^2 = 1`),
  `E(expm(t eps/2)) = E_0 + c t^2/2 + O(t^3)`.
  - Cubic symmetry allows two values: `c_E` for axis shears (`eps`
    diagonal) and `c_T` for face shears (`eps` off-diagonal).
  - At a stationary point (after the cosmological constant is tuned so flat
    space solves the equations), the second derivative does not depend on
    how the metric is parametrised.
- **The member**, as in block 101 (supplied):
  `L = [α tr(ḣ²) + β(tr ḣ)²]/w̄ + K w̄(u R_1 + R_2) − e u`.
- **Tick surface** (the approved `kinetic_isotropy_primitive`, used as a
  comparator): Euclidean `Z^4`. A free lattice scalar has free energy per
  site `(1/2)<log(g^{μν} C_μν(k) + m^2)>`.

## T1 — comparators: covariant and coordinate-fixed cutoffs

- **Cutoff on the proper momentum** (`|e^T k| < π`). Changing variables to
  `q = e^T k` gives energy `-(1/det e) x` a constant. With `det e = 1`, the
  energy is independent of shear. The runner checks this on a direct grid:
  `-1.2330` against `-1.2336` at shear `0.3`, exact `-1.2337`, within the
  grid's error.
- **Cutoff fixed in coordinate momentum** (the ball `|k| < π`). The ball is
  rotation-invariant but not covariant. Expanding
  `|e^T k̂| = sqrt(k̂ expm(eps) k̂)` to second order and averaging over the
  sphere gives `E = E_0 (1 + tr eps^2 / 15)`. So `c = 2E_0/15`, the same for
  every shear. The runner gives `-0.16449` for both, against `2E_0/15 =
  -0.16449`.

So the stiffness comes from the cutoff being fixed in coordinates, not from
cubic anisotropy. A lattice is such a cutoff.

## T2 — the walker's sea on Z^3

| | value per cell (lattice units) |
|---|---|
| sea energy `E_0` | `-1.19380` |
| axis-shear stiffness `c_E` | `-0.17793` |
| face-shear stiffness `c_T` | `-0.14667` |

- The grid change from `64^3` to `128^3` moves the stiffnesses by `3.6e-7`.
- Both are negative. Along every shear, the flat shape is a maximum of the
  sea's energy: the sea gains energy by shearing.
- `c_E/c_T = 1.213`. The response is cubic, not isotropic.

*Real space.* The vielbein-coupled walker on a periodic `8^3` lattice was
diagonalised directly. Its sea energy per site equals the `k`-space formula
on the same momenta at the flat shape and at two shears (to `1e-12`). A shear
of `0.4` moves the spectrum by up to `0.13`.

So the sheared and unsheared matter are not unitarily equivalent. No
relabelling of the matter, local or not, maps one onto the other. The
continuum's protection (a shear is a coordinate change) has no lattice
counterpart for this coupling.

*Only the shape matters.*
- Rotating the frame index (`e -> e R`) changes the sea energy by
  `6.7e-16`.
- Turning an axis shear by 45° about an axis makes it a face shear. That
  changes its cost from `c_E t^2/2` to `c_T t^2/2`, as expected.

The map's earlier reasoning blamed infinitesimal rotations. That was
imprecise: at zero wavelength a rotation does not change a flat metric at
all. The obstruction is shape.

## T3 — the hypercubic tick surface does not remove it

A free lattice scalar on Euclidean `Z^4` (per site; grid `24^4` to `36^4`
changes the values by `6e-8`):

| metric coupling | `m^2` | `c_3` (diagonal) | `c_6` (off-diagonal) |
|---|---|---|---|
| symmetric difference, `C_μν = p̂_μ p̂_ν`, `p̂ = 2 sin(k/2)` | 0.5 | `0.0982` | `0.0712` |
| | 0.1 | `0.1022` | `0.0729` |
| forward difference, `C_μν = Re[(e^{ik_μ}−1)(e^{−ik_ν}−1)]` | 0.5 | `0.0982` | `0.0905` |
| | 0.1 | `0.1022` | `0.0945` |

- The off-diagonal set includes time–space shears. On the tick surface
  these are tied to space–space shears by the hypercubic symmetry, but
  neither vanishes.
- The values depend on the mass and on the coupling, so they are not
  universal numbers.
- Fermions contribute with the opposite sign.
- `sin k` is not used as a second dispersion. Over the zone `sin k` and
  `sin(k/2)` take the same values with the same weights, so it would repeat
  the first test at a rescaled mass.

## T4 — cancelling needs matched dispersions

- A complex boson whose modes have exactly the walker's frequencies,
  `|e^T s(k)|`, has zero-point energy `+<|e^T s|>`. It cancels the walker
  sea's shape energy at every shape; the runner checks four shapes and finds
  exactly `0`.
- The standard forward-difference complex scalar does not cancel it. The
  sum's stiffnesses are `0.178` and `0.191`.

This is the lattice form of the familiar boson–fermion cancellation of
vacuum energy (supersymmetry; reference only). To remove the shape stiffness
it would have to hold mode by mode at the lattice scale, for the whole
matter content and at every order.

## T5 — what the stiffness does to the member

Take the member's spatially constant TT mode `h_ij = h(t) eps_ij`. The
member's gradient terms vanish for it, so its action is
`(α/w̄) ḣ^2 − (c/2) h^2`, and

`ω^2 = c w̄ / (2α)`.

At the one-light-cone value `α = K/4` this is `2 c w̄ / K`. In general
relativity's normalisation (`α/w̄ = 1/(64πG)`, `w̄ = 1`) it is
`m^2 = 32πG c` per cell volume, i.e. `m^2 = 32π c l_P^2 / a^4`.

| spacing `a` | untuned `|m|` | against the bound `1.27e-23 eV` |
|---|---|---|
| Planck length | `3.8 M_P` | tune `c` to `~1e-104` |
| `1e-19 m` (about the coarsest colliders allow) | `1.2e-3 eV` | `1e20` times too large; tune `c` to `~1e-40` |

These use `|c| = 0.147`, the walker's smaller stiffness. The bound is the
LIGO–Virgo–KAGRA GWTC-3 limit on the graviton mass (reference input).

For the fermion sea `c < 0`, so the constant TT modes grow instead of
oscillating: flat space is unstable at that rate.

## T6 — for free matter the stiffness belongs to the coupling

The natural coupling stretches each hop by the vielbein. Another coupling
relabels momentum space instead.
- Take a divergence-free trigonometric vector field `v` on the zone that
  vanishes at the 8 nodes, and let `phi` be its time-1 flow. Use the symbol
  `sigma . s(phi(k))`.
  - Axis shear: `v = curl(A e_3)`, `A = (λ/4) sin 2k_1 sin 2k_2`. Its
    Jacobian at every node is `diag(λ, −λ, 0)`.
  - Face shear: `A = −(λ/4) cos k_1 cos 3k_2`. Its symmetric Jacobian at node
    `K` is `λ cos K_1 cos K_2` times the face shear, plus a rotation, which
    the coin frame absorbs.
- The flow keeps volume, so the sea energy `−<|s(phi(k))|>` equals `E_0`
  exactly. The runner gives `−3.0e-9` (axis) and `1.6e-9` (face) at
  `λ = 0.1`: grid error. The natural coupling at the same axis metric
  changes it by `−7.1e-3`.
- Near each node, `|s(phi(K+q))| = |P q|` with one common `P` for all 8
  nodes (spread `1e-10`). Axis: `P = diag(e^λ, e^{−λ}, 1)`. Face: `P_12 =
  0.099` at `λ = 0.1`. So at low energy the matter sees one sheared metric,
  as a metric coupling should.
- The symbol is analytic, so the hops decay exponentially with range. The
  largest at range 20 is `5e-17` (axis) and `4e-13` (face).

So for free matter a shear can be made an exact relabelling, and the free
vacuum can be made shape-blind. T2's stiffness is a property of the natural
coupling.

## T7 — interactions bring it back

- **Computed.** With the T6 coupling, add a nearest-neighbour density
  interaction `V sum_{x,j} n_x n_{x+e_j}`.
  - The first-order energy of its exchange part depends on the shear. The
    stiffness per unit shear is `0.0019 V` (axis) and `0.0049 V` (face).
  - The on-site density matrix does not change (to `1.7e-16`). So on-site
    interactions stay blind at first order; nearest-neighbour ones do not.
- **Why, in general.** For a relabelling to carry a translation-invariant
  two-body interaction along, it must keep every momentum-conserving vertex
  momentum-conserving: `phi(a) + phi(b) = phi(c) + phi(d)` whenever
  `a + b = c + d`.
  - Setting `c = a + b` and `d = 0` gives `phi(a) + phi(b) = phi(a+b) +
    phi(0)`. So `phi − phi(0)` is a continuous homomorphism of the torus,
    i.e. an integer matrix.
  - No small non-integer shear is an integer matrix. The designed `phi`
    violates momentum addition by `0.125` at `λ = 0.1` (runner).
  - This rules out only zone relabellings. Many-body constructions are not
    excluded.
- An `h`-dependent interaction strength could cancel the first-order
  stiffness. That cancellation would then have to be redone at every order
  and for every interaction, which is what tuning means.

## What this means for the axioms

- **A fixed regular lattice plus a member field has a fine-tuning problem
  beyond the cosmological constant, once matter interacts.** The vacuum's
  shape stiffness is a cubic invariant. For free matter a designed coupling
  removes it (T6). For interacting matter no known construction does (T7).
  There it is cancelled only by local counterterms in the member's action,
  or by an `h`-dependent coupling, tuned against every species'
  contribution and redone at every order. On `Z^3` with continuous
  time there are two such numbers for the spatial shears. On the tick
  surface there are two, `c_3` and `c_6`, which also cover time–space
  shears. Both counts come on top of the cosmological constant.
- **The tick surface does not help here** (T3). Probe 4's uniqueness of the
  member's leading action concerns terms with two derivatives. This is the
  term with none.
- **Routes the owner could weigh** (none derived here):
  1. Accept the tuning, as the cosmological constant is accepted.
  2. Match zero-point shape energies of bosons and fermions mode by mode at
     the lattice scale (T4). That is a strong constraint on the matter
     content.
  3. Find a many-body construction that makes shear an exact symmetry of
     interacting lattice matter. Zone relabellings cannot (T7).
  4. Do not put the member on a fixed shape. Geometry could come from the
     lattice's own structure in a way that carries no preferred shape.
     Randomly placed discreteness, as in causal sets, is the known example
     with no preferred frame (Bombelli, Henson and Sorkin 2006; reference
     only). This would touch the Lattice axiom's regular `Z^3`.
- **Layman sentence (proposed, not adopted):** "A crystal has a shape, and
  anything living in it can feel that shape. Gravitational waves are changes
  of shape, so on a crystal they come out heavy unless the crystal's
  stiffness is tuned away."

## What this does not show

- **Couplings.** The couplings are supplied comparators. A second-order
  (seagull) term in the member–matter coupling adds a local constant to `c`.
  Choosing it to cancel `c` is the tuning, not an escape from it.
- **Content.** Free matter, plus one interaction at first order. There are
  no gauge fields, no higher orders and no Standard Model content. That the
  stiffness returns at every order for generic interactions is expected, not
  computed.
- **The member's own terms.** Block 101's member has no mass term. A tuned
  counterterm is not modelled.
- **Shift and lapse.** Constant `h_0i` (the lattice's velocity) and `h_00`
  on the continuous-time surface are not computed. Their masses matter for
  which phase of Lorentz-violating massive gravity results (reference only:
  Rubakov 2004; Dubovsky 2004).
- **Finite wavelength.** The `q -> 0` limit is identified with the uniform
  response. The sea has point nodes and no Fermi surface, so no intraband
  term enters. The full `q`-dependence is not computed.
- **Induced member.** Whether a member induced from the sea (the gravitation
  lens's route) inherits the same stiffness is expected but not computed.
  A member induced from matter that is stiff to shear has the stiffness as
  its mass term.
- **Literature.** Reference only: Collins, Perez, Sudarsky, Urrutia and
  Vucetich (2004) on fine-tuning of Lorentz violation; Caracciolo, Menotti
  and Pelissetto (1990) on the lattice energy-momentum tensor; Endlich,
  Nicolis and Wang (2013) on gravity in solids.

## Independent checks

Pending: a Claude Fable 5.1 subagent from its own code, and a codex
`gpt-5.6-sol` referee.

## Reproduction

```bash
python3 scripts/lattice_vacuum_shape_stiffness_gives_the_member_a_mass_unless_tuned_2026_09_27.py
```

Expected: `TOTAL: PASS=11 FAIL=0` (about 1 minute).
