---
claim_id: the_walkers_sea_feels_the_shape_of_a_constant_metric_under_the_natural_coupling_a_designed_coupling_removes_it_for_free_matter_interactions_bring_it_back_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "Supplied comparator couplings, not adopted; computed facts plus a conditional naturalness warning. Natural coupling: the walker's hop along axis j carries sigma_a e_a^j (constant inverse vielbein e, g^{-1} = e e^T); a shear is e = expm(eps/2), eps symmetric traceless (volume kept). (T1) With a cutoff on the proper momentum the free sea is shear-blind; with a coordinate-fixed ball its shape coefficient is 2E_0/15. (T2) The walker's sea on Z^3: E_0 = -1.19380, shape coefficients c_E = -0.17793 (axis shears) and c_T = -0.14667 (face shears) per cell, converged; flat is a maximum along shears; a direct 8^3 diagonalisation agrees; frame rotations change nothing. Under a face shear the natural coupling gives the 4 nodes with cos K_1 cos K_2 = -1 the mirrored metric; a taste-universal local coupling (adding range-2 hops) gives all 8 nodes one metric and c_T = -0.10882 (c_E unchanged). (T3) These are the long-wavelength limits of the static kernel: for a cos(q x) modulation along an axis (per mean-square amplitude, vielbein at hop midpoints) the two TT polarisations' coefficients approach c_E and the taste-universal c_T at order q^2, and for axis propagation they sit in their own little-group irreps, apart from lapse, shift and trace. (T4) Euclidean Z^4 free scalar, two site-local couplings: c_3 ~ 0.10, c_6 ~ 0.09-0.12 per site, mass-dependent. (T5) A complex boson with the walker's own dispersion cancels the shape dependence exactly. (T6) For free matter the dependence belongs to the coupling: relabelling the zone by the volume-keeping flow of a divergence-free trigonometric field with the same symmetric Jacobian at the 8 nodes gives an exponentially local coupling with an exactly shear-blind sea and one common sheared metric (J^T J) at all nodes. (T7) With that coupling a nearest-neighbour density interaction's first-order energy is shape-dependent again (0.0019 V axis, 0.0037 V face); on-site interactions stay blind at first order; a zone relabelling that keeps every momentum-conserving vertex momentum-conserving is an integer matrix, so no small shear. (T9) On the continuous-time surface the clock is protected and the shift is not: a constant lapse multiplies H, so any matter's vacuum energy is exactly linear in it; a constant shift couples to a momentum operator, and in a 12-site spin-chain comparator its vacuum curvature is zero for free matter and nonzero with interactions (-0.0122 XXZ, -0.0017 with a next-nearest term, per site, for the hopping current); a search of all local charges of range <= 3 finds a conserved momentum-like one for the free and the integrable chain (its energy current) and none for the non-integrable chain (nearest candidate 0.195). (T8) Conditional on block 101's member and the bridge 'a hop costs hbar c/a': a coefficient c gives the long-wavelength TT modes omega^2 = c wbar/(2 alpha) (GR normalisation m^2 = 32 pi G c/a^4): |m| = 3.3 M_P at the Planck spacing, 1.0e-3 eV at an illustrative a = 1e-19 m (|c| = 0.109); c < 0 means growth. Frequency dependence, higher orders, gauge fields, the trace sector, the shift beyond a 1D comparator, and many-body constructions of a shear-blind coupling are not computed or excluded."
upstream_dependencies:
  - minimal_axioms
  - kinetic_isotropy_primitive
  - if_the_members_leading_action_respects_the_hypercubic_tick_surface_it_is_unique_beta_equals_minus_alpha_and_alpha_equals_k_over_four_follow_bounded_theorem_note_2026-09-27
runner: scripts/lattice_vacuum_feels_the_shape_of_a_constant_metric_2026_09_27.py
---

# The walker's sea feels the shape of a constant metric under the natural coupling; a designed coupling removes it for free matter; interactions bring it back

**Date:** 2026-09-27
**Type:** bounded_theorem (computed facts) with a conditional naturalness
warning
**Status:** numerical identities and converged zone integrals; supplied
comparator couplings; unaudited. Independent checks are recorded below.

## In one paragraph

A regular lattice has a shape. In a continuum, stretching space along one
axis while squeezing it along another, at fixed volume, only relabels
coordinates, and the vacuum cannot notice. On a fixed lattice it can: the
lattice's grain is fixed in coordinates, and the metric decides how that
grain looks in proper lengths.

The campaign's walker sea, coupled to a metric in the natural way, notices.
Its energy changes by about 15 % of its size per unit shear squared, with
different values along the axes and across the faces. The flat shape is a
maximum. The same number is the long-wavelength limit of how the sea responds
to a slowly varying shear, so a gravitational wave coupled to this sea would
carry a mass-type term, or a growth rate, of the vacuum's size.

For free matter this can be engineered away. A coupling that relabels
momentum space, instead of stretching the hops, leaves the free vacuum
exactly blind to shear. Interactions undo that. The relabelling does not
respect how momenta add when particles collide, and a nearest-neighbour
interaction makes the vacuum shape-dependent again at first order. So for
interacting matter no construction is known that forbids the effect. Unless
one is found, the member's mass-type terms must be tuned, like the
cosmological constant, but for more numbers.

## Why this question

- The viability map's decision 2 (the hypercubic tick surface) listed loops
  as not settled. The panel's gravitation lens proposed inducing the member
  from the sea. The map's own assessment was by reasoning only.
- The cleanest place to test is zero wavelength. In general relativity a
  spatially constant, volume-preserving change of the metric is locally
  pure gauge (`ξ_i ∝ h_ij x^j`). So its energy cost, taken as the
  long-wavelength limit of a local kernel, is a mass-type term for the
  member's transverse-traceless (TT) modes. That is the kind of term
  gravitational-wave dispersion bounds.
- This note computes it for the campaign's own matter, checks that it is a
  genuine long-wavelength limit, and tests whether a different coupling or
  interactions change it.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`): `Z^3` with proper cubic
  rotations. The memo supplies no member and no metric coupling.
- **The walker:** `H = sum_x sum_j [psi_x^dag (sigma_j/2i) psi_{x+e_j} + h.c.]`,
  with symbol `sum_j sigma_j sin k_j`. The sea is the filled lower band.
- **Natural coupling** (supplied): the hop along axis `j` carries
  `sigma_a e_a^j` in place of `sigma_j`.
  - `e` is the inverse vielbein on that link, and the inverse metric is
    `g^{-1} = e e^T`.
  - `H` is linear in `e`, so the coupling has no separate contact term.
  - For constant `e`, the sea's energy per cell is `E(e) = −<|e^T s(k)|>`.
- **Shear:** `e = expm(eps/2)` with `eps` symmetric traceless, so
  `g^{-1} = expm(eps)` and the proper volume per cell is unchanged.
- **Shape coefficient:** `E(expm(t eps/2)) = E_0 + c t^2/2 + O(t^3)` for
  `tr eps^2 = 1`.
  - Cubic symmetry allows `c_E` (axis shears) and `c_T` (face shears).
  - The gradient along shears vanishes by cubic symmetry, so the
    coefficient is intrinsic to the fixed-volume family of metrics.
- **The member** (supplied, block 101):
  `L = [α tr(ḣ²) + β(tr ḣ)²]/w̄ + K w̄(u R_1 + R_2) − e u`.
- **Tick surface** (the approved `kinetic_isotropy_primitive`, a Euclidean
  hypercubic regulator; used as a comparator): a free lattice scalar with
  free energy per site `(1/2)<log(g^{μν} C_μν(k) + m^2)>`.

## T1 — comparators: covariant and coordinate-fixed cutoffs

- **Cutoff on the proper momentum** (`|e^T k| < π`). Changing variables to
  `q = e^T k` shows the energy is shear-independent at `det e = 1`. On a
  direct grid: `−1.2330` at shear `0.3`, exact `−1.2337`.
- **Cutoff fixed in coordinate momentum** (the ball `|k| < π`).
  - Averaging `|e^T k̂| = sqrt(k̂ expm(eps) k̂)` over the sphere gives
    `E = E_0 (1 + tr eps^2/15)`, so `c = 2E_0/15` for every shear.
  - The runner gives `−0.16449`; exact `−π²/60`.

The shape dependence comes from the cutoff being fixed in coordinates, not
from cubic anisotropy. A lattice is such a cutoff.

## T2 — the walker's sea on Z^3 (natural coupling)

| | value per cell (lattice units) |
|---|---|
| `E_0` | `−1.19380` |
| `c_E` (axis shears) | `−0.17793` |
| `c_T` (face shears) | `−0.14667` |

- Converged: `64^3` to `128^3` moves them by `3.6e-7`.
- Both are negative, so the flat shape is a maximum along every shear.
- `c_E/c_T = 1.213`: the response is cubic, not isotropic.
- **The natural coupling does not give all 8 species one metric under a
  face shear.**
  - Near node `K`, `sin k_j ≈ η_j q_j` with `η_j = cos K_j`. So the
    dispersion there is `|e^T D_η q|`, and the metric that node sees is
    `D_η g^{-1} D_η`.
  - For an axis shear that is `g^{-1}` at every node. For a face shear, the
    off-diagonal entry flips sign at the 4 nodes with `η_1 η_2 = −1`. The
    runner finds `+0.142` at 4 nodes and `−0.142` at the other 4 (shear
    `0.2`).
  - A **taste-universal** local coupling fixes this. It adds to each
    `σ_a` the range-2 hops `e_{ja} cos k_a sin k_j cos k_j` (`j ≠ a`), which
    near every node equal `η_a e_{ja} q_j`. All 8 nodes then see
    `+0.142`.
  - Its coefficients are `c_E = −0.17793` (unchanged) and
    `c_T = −0.10882`. These are the face-shear numbers used from here on.
- **Real space.** A direct diagonalisation on a periodic `8^3` lattice
  matches the `k`-space formula at every shape tested. Shearing moves the
  spectrum by up to `0.13`, so for this coupling the sheared and unsheared
  matter are not unitarily equivalent.
- **Only the shape matters.**
  - Rotating the frame index (`e -> e R`) changes nothing (`6.7e-16`).
  - With the taste-universal coupling, turning an axis shear by 45° makes it
    a face shear, and its cost moves from `c_E t^2/2` to `c_T t^2/2`.
- The map's earlier reasoning blamed infinitesimal rotations. That was
  imprecise: a rotation does not change a constant flat metric. The effect
  is about shape.

## T3 — it is the long-wavelength limit of the static kernel

Modulate the vielbein as `ε cos(q.x)` with `q` along `x`.
- The TT polarisations are then `h_yy − h_zz` and `h_yz`.
- The second-order energy gives `c(q) = −τ/4 − χ(q)/2`, where:
  - `τ = <sin^2 k_1/|s|>` is the uniform stress;
  - `χ(q)` is the interband susceptibility of the link stress.
  - Both are per mean-square amplitude of the cosine, with the vielbein
    evaluated at each hop's midpoint.
  - `h_yz` uses the taste-universal coupling.

| `q` | `0` | `0.065` | `0.131` | `0.262` |
|---|---|---|---|---|
| `h_yy − h_zz` | `−0.17793` | `−0.17789` | `−0.17777` | `−0.17728` |
| `h_yz` (taste-universal) | `−0.10882` | `−0.10880` | `−0.10877` | `−0.10865` |

- At `q = 0` the decomposition reproduces T2's finite differences exactly.
  The other-vendor referee's independent projector calculation agrees.
- The approach is smooth, at order `q^2`. The sea's point nodes cause no
  jump.
- For `q` along an axis, the little group is `C_4v`. There `h_yy − h_zz` and
  `h_yz` sit in the one-dimensional irreps `B_1` and `B_2`. Lapse and trace
  are `A_1`; shift and `h_xy`, `h_xz` are `E`. So these two TT coefficients
  do not mix with the constraint sector.
- For axis propagation, each TT polarisation has its own coefficient. That
  makes the waves birefringent at long wavelengths.
- Not computed: the frequency dependence at `q = 0`, and propagation off the
  axes.

## T4 — the hypercubic tick surface (Euclidean) does not remove it

A free lattice scalar on Euclidean `Z^4` (per site; `24^4` to `36^4` changes
the values by `6e-8`):

| site-local coupling | `m^2` | `c_3` (diagonal) | `c_6` (off-diagonal) |
|---|---|---|---|
| forward, `C_μν = Re[(e^{ik_μ}−1)(e^{−ik_ν}−1)]` | 0.5 | `0.0982` | `0.0905` |
| | 0.1 | `0.1022` | `0.0945` |
| mixed: forward diagonal, central off-diagonal (`sin k_μ sin k_ν`) | 0.5 | `0.0982` | `0.1114` |
| | 0.1 | `0.1022` | `0.1173` |

- The off-diagonal set includes Euclidean time–space shears.
- The values depend on the mass and the coupling. Fermions contribute with
  the opposite sign.
- This is Euclidean evidence only. Under Wick rotation, and with lapse and
  shift as constraints, the Lorentzian time–space entries need separate
  treatment.
- `4 sin(k_μ/2) sin(k_ν/2)` is not used. It is not periodic, so it is not a
  site-local coupling without half-link structure.

## T5 — matched bosons cancel it

A complex boson with exactly the walker's frequencies `|e^T s(k)|` has
zero-point energy `+<|e^T s|>`. It cancels the sea's shape dependence at
every shape; the runner finds `0` at four shapes. The standard
forward-difference complex scalar does not: the sum's coefficients are
`0.178` and `0.191`.

This is the lattice form of boson–fermion cancellation of vacuum energy
(supersymmetry; reference only). To remove the effect it must hold mode by
mode at the lattice scale.

## T6 — for free matter the dependence belongs to the coupling

Relabel momentum space instead of stretching the hops.
- **Construction.**
  - Take a divergence-free trigonometric field `v` that vanishes at the 8
    nodes, and let `phi` be its time-1 flow. Use the symbol
    `sigma . s(phi(k))`.
  - Axis shear: `v = curl(A e_3)` with `A = (λ/4) sin 2k_1 sin 2k_2`. Its
    Jacobian at every node is `diag(λ, −λ, 0)`.
  - Face shear: `A = (λ/2)(sin^2 k_2 − sin^2 k_1)`, i.e.
    `v = (λ/2)(sin 2k_2, sin 2k_1, 0)`. Its Jacobian at every node is
    `λ(E_12 + E_21)`, the same face shear everywhere.
- **Energy.** The flow keeps volume, so the sea energy is exactly `E_0`.
  The runner gives changes of `−3.0e-9` (axis) and `1.6e-9` (face) at
  `λ = 0.1`, which is grid error. The natural coupling at the same axis
  metric changes it by `−7.1e-3`.
- **Metric.** Near each node, `|s(phi(K+q))|^2 = q^T J_K^T J_K q`. The runner
  compares `J_K^T J_K` directly across the 8 nodes; the spread is `2e-9`.
  - Axis: `diag(e^{2λ}, e^{−2λ}, 1)`.
  - Face: off-diagonal `sinh 2λ = 0.201`.

  The low-energy matter sees one sheared metric.
  - An earlier face construction (`A ∝ cos k_1 cos 3k_2`) mirrored the shear
    at half the nodes, like the natural coupling.
  - The earlier check compared the wrong matrices and hid this. The
    other-vendor referee found it.
- **Locality.** The symbol is analytic, so the hops decay exponentially.
  The largest at range 20 is `5e-17` (axis) and `8e-17` (face).

So for free matter a constant shear can be made an exact relabelling, and the
free vacuum can be made shape-blind. T2's numbers belong to the natural
coupling. Only constant metrics are treated here. A position-dependent
version of this coupling is not built.

## T7 — interactions bring it back

- **Computed.** With the T6 coupling, add `V sum_{x,j} n_x n_{x+e_j}`.
  - Its first-order (exchange) energy depends on the shear: `0.0019 V`
    (axis) and `0.0037 V` (face) per unit shear. The referee's independent
    integration gave `0.00194 V` for the axis shear.
  - The on-site density matrix does not change (`1.7e-16`). So on-site
    interactions stay blind at first order.
- **Why, for zone relabellings.** To carry a translation-invariant two-body
  interaction along, a relabelling must keep every momentum-conserving
  vertex momentum-conserving: `phi(a) + phi(b) = phi(c) + phi(d)` whenever
  `a + b = c + d`.
  - Setting `c = a + b` and `d = 0` gives
    `phi(a) + phi(b) = phi(a+b) + phi(0)`. So `phi − phi(0)` is a continuous
    homomorphism of the torus, i.e. an integer matrix.
  - No small non-integer shear is one. The designed `phi` violates momentum
    addition by `0.125` at `λ = 0.1`.
  - This excludes zone relabellings only. Many-body constructions, and
    exact lattice Ward identities for interacting matter, are not excluded.
- An `h`-dependent interaction could cancel the first-order term. That
  cancellation would have to be redone at every order and for every
  interaction.
- **The campaign's own books meet the same wall.** Exact books hold for
  free walkers and are lost once records scatter or bind (blocks 137 and
  143).

## T9 — the clock is protected; the shift is not

On the continuous-time surface, a spatially constant member has three
parts: lapse (the clock), shift, and shape.
- **Lapse.** A constant lapse `u` multiplies the Hamiltonian, `H -> (1+u) H`.
  So every vacuum energy is exactly linear in `u`, with no curvature. That
  holds for any lattice matter, free or interacting. The linear term is the
  cosmological constant.
  - Runner: curvature below `4e-12` for the free, integrable and
    non-integrable chains below.
- **Shift.** A constant shift couples to a momentum operator `P`. The
  vacuum's curvature in it is zero when the ground state is an eigenstate of
  `P`, for example when `P` is conserved.
  - For free translation-invariant matter, band-diagonal momenta are
    conserved. A filled band carries none, so the free walker sea is exactly
    shift-blind for shifts below the cone speed (no pockets form).
  - With interactions, is there any local conserved momentum-like charge?
- **A comparator for interacting matter:** a spin-1/2 chain of 12 sites at
  zero magnetisation (spinless fermions).
  - Models: hopping; plus `ZZ` (XXZ, integrable); plus a next-nearest `ZIZ`
    term (non-integrable).
  - The runner searches every translation-invariant,
    magnetisation-conserving local charge of range `<= 3`. It splits them by
    spatial parity: momentum-like charges are odd.

| chain | conserved local charges | conserved odd (momentum-like) charge | shift curvature per site (hopping current) |
|---|---|---|---|
| free | 4 | yes | `0` |
| XXZ (integrable) | 2 | yes (its energy current) | `−0.0122` |
| XXZ + next-nearest | 1 (`H`) | **no**: nearest candidate misses by `‖[H,Q]‖²/‖Q‖² = 0.195` | `−0.0017` |

So the pattern of T6 and T7 holds in the shift sector too.
- Free matter has a conserved momentum that a designed coupling could use.
- Integrable matter has one too, its energy current. Coupling the shift to
  the hopping current instead leaves the curvature nonzero.
- Generic interacting matter has none of range `<= 3` in this comparator.
  - This fits the expectation that non-integrable lattice matter keeps only
    energy and its internal charges locally (reference only; not proved
    here).
  - Longer ranges and three dimensions are not searched.

The one conservation law a lattice with continuous time always keeps,
energy, protects exactly the member's clock part.

## T8 — what the coefficient would do to the member (conditional)

This section is conditional on two things: block 101's member, and the
bridge "a hop costs `ħc/a`". The axioms do not set that bridge; the scale
reference primitive supplies units only.

- A long-wavelength TT mode `h_ij = h(t) eps_ij` has action
  `(α/w̄) ḣ^2 − (c/2) h^2`, so `ω^2 = c w̄/(2α)`.
- In general relativity's normalisation (`α/w̄ = 1/(64πG)`), this is
  `m^2 = 32πG c/a^4`.

| spacing `a` | untuned `|m|` (with `|c| = 0.109`, the smaller taste-universal coefficient) |
|---|---|
| Planck length | `3.3 M_P` |
| `1e-19 m` (illustrative) | `1.0e-3 eV` |

- The mass scales as `l_P/a^2`.
- **For `c > 0`.** The LIGO–Virgo–KAGRA dispersion bound `1.27e-23 eV`
  (reference input) constrains the constant term of each polarisation's
  dispersion. It would require `c` to be `~1e-40` of its natural size at
  `1e-19 m`, and `~1e-103` at the Planck spacing.
- **For `c < 0`,** as for this fermion sea, the modes grow at rate `|m|`
  instead: flat space would not persist.

## What this means for the axioms (a conditional naturalness warning)

- **The finding.** Couple a member to lattice matter by local couplings of
  the kinds tested here. The vacuum's shape dependence then gives the
  member's long-wavelength TT modes mass-type terms of the vacuum's size.
- **When it applies.**
  - For free matter a designed coupling removes them (T6).
  - For interacting matter, zone relabellings cannot (T7), and no other
    construction is known.
  - Unless one is found, the terms must be cancelled by tuned local terms,
    redone at every order: at least the two TT-sector numbers, `c_E` and
    `c_T` or `c_3` and `c_6`.
  - The trace and shift sectors may add more. The lapse is protected (T9);
    the shift is not, in the comparator; the trace is not computed.
  - The cosmological constant does not cover any of them.
- **The tick surface** does not remove them (T4). Probe 4's uniqueness
  concerns two-derivative terms. This is the term with none.
- **On the continuous-time surface the clock is safe** (T9). The lapse
  couples to the exactly conserved energy, so it gets no such term. The shift
  and shape parts couple to momentum and stress. Generic interacting lattice
  matter conserves neither locally.
- **Routes the owner could weigh** (none derived here):
  1. Accept the tuning, as the cosmological constant is accepted.
  2. Match zero-point shape energies of bosons and fermions mode by mode at
     the lattice scale (T5).
  3. Find a many-body construction, or exact lattice Ward identities, that
     makes a shear an exact symmetry of interacting lattice matter. Related
     prior art: perfect actions restoring discrete diffeomorphisms (Bahr and
     Dittrich 2009; reference only).
  4. Do not put the member on a fixed shape. Randomly placed discreteness,
     as in causal sets, carries no preferred frame (Bombelli, Henson and
     Sorkin 2006; reference only). This would touch the Lattice axiom's
     regular `Z^3`.
- **What does not help.** Letting the lattice relax, with displacement
  modes of its own, makes it a solid. In the solid effective theory the
  graviton is still massive (Dubovsky 2004; Endlich, Nicolis and Wang 2013;
  reference only).
- **Layman sentence (proposed, not adopted):** "A crystal has a shape, and
  anything living in it can feel that shape. Gravitational waves are changes
  of shape. Free particles can be made not to notice, but particles that
  collide do, so on a crystal gravity waves come out heavy unless something
  is tuned."

## What this does not show

- The couplings are supplied comparators. Other contact terms shift `c` by
  local constants. Choosing them to cancel `c` is the tuning discussed
  above.
- Free matter plus one interaction at first order only. No gauge fields,
  higher orders or Standard Model content. That the dependence returns at
  every order for generic interactions is expected, not computed.
- The frequency dependence at zero wavelength and propagation off the axes
  are not computed.
- The trace sector is not computed. The lapse and shift are treated only at
  zero wavelength, and the shift only in a one-dimensional comparator.
- Whether a member induced from the sea (the gravitation lens's route)
  inherits the same coefficient is expected but not computed.
- **Literature (reference only):**
  - Collins, Perez, Sudarsky, Urrutia and Vucetich (2004), on fine-tuning of
    Lorentz violation;
  - Caracciolo, Curci, Menotti and Pelissetto (1990), on Ward identities of
    the lattice energy-momentum tensor;
  - Rubakov (2004) and Dubovsky (2004), on Lorentz-violating massive
    gravity;
  - Bahr and Dittrich (2009), on discrete diffeomorphisms;
  - Endlich, Nicolis and Wang (2013), on solids;
  - LIGO–Virgo–KAGRA GWTC-3 (2021), on graviton-mass bounds.

## Independent checks

- **Codex `gpt-5.6-sol` referee**, at xhigh. Another vendor family; it read
  only the axioms memo and this note's first version, before T3, T6 and T7
  existed.
  - **Verdict: "fails".** The numbers were reproduced independently: every
    coefficient, `2E_0/15 = −π²/60`, the oscillator equation, the GR
    normalisation and the size estimates.
  - The conclusion did not follow as stated. Its findings:
    - the note promoted one coupling's constant-background result into an
      unavoidable graviton mass;
    - a constant shear is not yet a pole mass without the long-wavelength
      limit and the constraint structure;
    - contact terms are load-bearing;
    - "resists" contradicted the negative sign;
    - one Euclidean coupling was not site-local;
    - the tuning count omitted the trace, lapse and shift sectors;
    - the dimensional bridge and the collider spacing were unsupported.
  - **Applied in this revision:**
    - retitled to what is shown;
    - the long-wavelength limit and the little-group decoupling added (T3);
    - the free-matter escape (T6) and its failure under interactions (T7),
      found independently by the author;
    - "resists" replaced and the sign stated;
    - the non-periodic coupling replaced by a site-local one;
    - the count stated as "at least two TT-sector numbers";
    - the bridge declared and the spacing made illustrative;
    - the prior art added (perfect actions, solids, Ward identities).
- **Codex `gpt-5.6-sol`, second round** (on the renamed revision).
  - Resolved: contact terms, sign, dimensional bridge, site-local Euclidean
    couplings, and the count.
  - Partly resolved: frequency dependence, now disclosed. T3 was confirmed
    independently, including the `B_1`/`B_2` non-mixing.
  - T7 was confirmed within scope.
  - **Not resolved: T6's face construction.** It gave a node-dependent
    metric in common coordinates. The runner had hidden this with a
    node-dependent reflection.
  - **Applied:**
    - the face flow replaced by one with a common symmetric Jacobian;
    - the metric compared as `J^T J`;
    - the same defect found in the natural coupling, and the
      taste-universal coupling added (T2, T3);
    - face numbers updated (T7 `0.0037 V`; T8 `|c| = 0.109`);
    - the finite-`q` normalisation stated.
  - A third round is pending.
- **Claude Fable 5.1 subagent:** pending.

## Reproduction

```bash
python3 scripts/lattice_vacuum_feels_the_shape_of_a_constant_metric_2026_09_27.py
```

Expected: `TOTAL: PASS=13 FAIL=0` (about 2 minutes).
