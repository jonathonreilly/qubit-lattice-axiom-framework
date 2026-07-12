# Dark-Energy EOS Spectral-Bridge Obstruction and Conditional Corollary

**Date:** 2026-07-12
**Claim type:** `no_go` (author proposal for independent review; the auditor
owns `claim_type` and `audit_status`, and the pipeline derives
`effective_status`)
**Status:** `proposed_retained` no-go for the exact declared surface;
independent audit is required before any effective status, while the positive
spectral-sourcing claim remains open
**Runner:** `scripts/frontier_dark_energy_eos.py`

```yaml
actual_current_surface_status: proposed_retained
target_claim_type: no_go
claim_type_reason: "same-reduct countermodels prove non-entailment on T_F plus an explicitly granted intrinsic spectrum"
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: true
proposal_allowed_reason: "review-loop disposition pass; no open import remains for the narrow no-go"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Result

The requested positive bridge does **not** follow from `T_F` plus the explicitly
granted intrinsic spectrum below.  The exact result on that declared surface
is the following narrow no-go.

> **Spectral-bridge non-entailment theorem.**  Let `T_F` be the current
> framework foundation: Lattice, Qubit, Admissibility, Record, and the three
> approved primitives.  Even after adjoining a fixed intrinsic graph spectral
> datum with reference radius `R_graph`,
>
> `lambda_n(S^3_R_graph) = n(n+2)/R_graph^2`,
>
> the common foundation-plus-spectrum reduct has expansions with distinct
> cosmological-action coefficients, source splits, and physical radius
> histories.  Therefore it does not entail a map from `R_graph` to either the
> physical slice radius `a_phys(t)` or the de Sitter curvature radius `L`, and
> it does not entail
>
> `Lambda = lambda_1(S^3_R_graph)`, `d a_phys/dt = 0`, or `w = -1`.

This is a countermodel theorem, not an argument from missing documentation.
It proves that the load-bearing identification cannot be obtained from the
declared premises without additional action/source, graph-to-geometry, and
physical-history content.  Cauchy data alone can provide the throat
compatibility statement below, not a persistent vacuum source.

The strongest positive statement that survives is strictly conditional:

> **Conditional EOS corollary.**  If a positive, time-independent physical
> vacuum density is separately supplied, then stress-energy conservation in
> an expanding FRW solution gives `p = -rho` and hence `w = -1`.

That implication is exact but does not establish that a graph eigenvalue is
the physical vacuum source.

## Auditor blocker closed by this result

The prior audit identified this load-bearing step:

> Dark energy is identified with the fixed `S^3` graph-Laplacian spectral gap,
> `Lambda = lambda_1(S^3) = 3/R^2`, with `R` fixed thereafter.

The obstruction above closes the disposition of that step on the declared
`T_F` plus intrinsic-spectrum surface: it is an independent premise, not a
derived identity.  The note no longer asks a numerical runner to certify the
physical bridge and no longer
routes around the blocker by calling an upstream assertion retained.

Historical decoration handling named
`dark_energy_eos_retained_corollary_theorem_note` as this row's parent.  That
identifier is preserved here only for the existing audit-prep helper's
source-pin check; it is not a load-bearing dependency of the no-go theorem.

## First-principles premise reset

The minimal allowed premise set is:

1. [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md): Lattice,
   Qubit, Admissibility, and Record;
2. the [approved primitive registry](audit/data/axiom_premise_nodes.json) and
   its three primitive source notes:
   [scale reference](SCALE_REFERENCE_PRIMITIVE_NOTE.md),
   [kinetic isotropy](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md), and
   [realized state](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md);
3. for the stronger geometric stress test only, the displayed closed-FRW
   Einstein equations and the exact continuum round-`S^3` spectrum.

Forbidden proof inputs are observed `H_0`, observed `Lambda`, fitted `R`, DESI
posteriors or forecasts, an assumed graph-to-action map, and an assumed
fixed-radius selector.  No such input appears in the theorem or runner.

The foundation memo explicitly says that Admissibility does not choose a
Hamiltonian or transfer operator and does not provide a time metric or
physical persistence dynamics.  Its open-gate list also leaves source/action
and physical-observable identification outside the axioms.  The approved
primitive registry adds a units reference, kinetic-form isotropy, and a
realized-state slot; none supplies a cosmological action or spectral-source
map.

## Proof of the non-entailment theorem

Fix any model of `T_F` and adjoin the same intrinsic round-`S^3` graph datum
with reference radius `R_graph = R_0` and gap
`lambda_1 = 3/R_graph^2`.  This fixes an intrinsic graph label and spectrum; it
does not define a physical slice radius `a_phys(t)` or curvature radius `L`.
The language and axioms fixed so far do not
define a gravitational action coefficient, a vacuum source, a graph-to-metric
identification, or a radius history.

For `beta = 0, 1, 2`, extend the same reduct by assigning an independent
cosmological coefficient

`Lambda_beta = beta lambda_1`.

All three expansions agree on every supplied foundation and intrinsic graph
datum, but only `beta = 1` satisfies `Lambda = lambda_1`.  The same reduct can
also be extended by distinct physical histories `a_phys(t)` because no map
`R_graph -> a_phys(t)` and no physical time law is supplied.  The theorem does
not deny that the reference graph label `R_graph` is fixed; it denies that its
fixedness supplies a fixed physical cosmological radius.  Two models of all
premises disagreeing on the proposed physical conclusion prove
non-entailment.  This
also shows why matching dimensions and the common coefficient `3` cannot
replace a physical identification theorem.  □

## Stronger closed-FRW obstruction

The same missing data remain visible even after standard closed-FRW Einstein
gravity is granted.  In units `c = 1`, let `a(t)` be the physical radius of a
round spatial slice, `H = (da/dt)/a`, and `rho` the non-vacuum energy density.
The first Friedmann equation and the scalar gap are

`H^2 + 1/a^2 = (8 pi G/3) rho + Lambda/3`,

`lambda_1(S^3_a) = 3/a^2`.

Eliminating `1/a^2` gives the exact residual identity

`Lambda = lambda_1(S^3_a) + 3 H^2 - 8 pi G rho`.

Thus the intrinsic spectrum alone omits extrinsic-curvature data (`H`) and
source data (`rho`).  In pure vacuum, equality
`Lambda = lambda_1(S^3_a)` holds precisely on a time-symmetric slice with
`H = 0`; it is not a general identity on the evolving spacetime.

For global closed de Sitter, writing `L = sqrt(3/Lambda)`, the exact solution
is

`a(t) = L cosh((t-t_0)/L)`,

so

`lambda_1(t) = 3/a(t)^2 = Lambda sech^2((t-t_0)/L)`.

The equality holds at the minimum-radius throat `t = t_0` and fails away from
it.  At the throat, the ADM Hamiltonian constraint with `K_ij = 0` and
`^(3)R = 6/L^2` reconstructs

`Lambda = 3/L^2 = lambda_1(S^3_L)`.

This is exact support for a **time-symmetric-throat compatibility statement**.
It is not spectral sourcing because `Lambda` was already present in the
Einstein constraint.

## The two possible meanings of `R`

The older derivation alternated between a graph or spatial-slice radius and a
de Sitter curvature-radius parameter.  Both readings leave a precise wall.

### `R` as fixed physical spatial radius

The product metric

`ds^2 = -dt^2 + R^2 dOmega_3^2`

has `G_00 = 3/R^2` and `G_ij = -(1/R^2) g_ij`.  The vacuum equations
`G_mu_nu + Lambda g_mu_nu = 0` would require simultaneously

`Lambda = 3/R^2` from the time component,

`Lambda = 1/R^2` from the spatial components.

No finite positive `R` satisfies both.  A fixed positive-radius global round
`S^3` is therefore not a pure-`Lambda` de Sitter vacuum.  The global de Sitter
solution instead has the evolving radius displayed above.

### `R` as the de Sitter curvature parameter `L`

If `R` is retyped as the constant spacetime curvature radius
`L = sqrt(3/Lambda)`, then the auxiliary mathematical equality

`Lambda = 3/L^2 = lambda_1(S^3_L)`

is true.  But it is a reconstruction or relabeling after `Lambda` and `L` are
already related by the de Sitter solution.  A further theorem must still
identify the framework graph radius with `L`, couple its eigenvalue to the
four-dimensional action with the exact normalization, and exclude or absorb
independent vacuum sources.  None is supplied by the current premises.

## Action/source split

The displayed Einstein metric equation and its geometric spectra do not select
how a constant vacuum term is split between the action parameter and stress
tensor.  Starting from

`G_mu_nu + Lambda g_mu_nu = 8 pi G T_mu_nu`,

the simultaneous redefinition

`Lambda' = Lambda + delta`,

`T'_mu_nu = T_mu_nu + (delta/(8 pi G)) g_mu_nu`

leaves the same metric equation and therefore all geometric spectra
unchanged.  A graph spectrum cannot by itself distinguish this split.  A
physical sourcing claim needs an action/source convention or theorem in
addition to geometric compatibility.

## Exact conditional EOS boundary

For a separately supplied constant positive vacuum density,

`d rho_vac/dt + 3 H (rho_vac + p_vac) = 0`

reduces, when `H rho_vac` is nonzero, to

`p_vac = -rho_vac`, hence `w = p_vac/rho_vac = -1`.

This conclusion is independent of the numerical value of the constant.  It
does not require an `S^3` spectrum at all.  Conversely, if an intrinsic
physical-slice gap `rho_gap proportional to lambda_1 proportional to a^-2` is
interpreted as a separately conserved, noninteracting effective fluid, its
scaling exponent would give `w = -1/3`, not `-1`.  Without separate
conservation, that EOS inference is not made.

## Lattice-correction finding

The previous exact coefficient

`lambda_1^latt/lambda_1^cont = 1 - (1/4)(a_lat/R)^2 + ...`

is retracted.  The flat cubic expansion is

`lambda_a(k) = k^2 - (a_lat^2/12) sum_i k_i^4 + O(a_lat^4)`,

so `k^2 = 3/R^2` does not determine the coefficient without a stencil and
mode orientation.  More decisively, a rotationally symmetric geodesic-shell
stencil on the unit `S^3` has shell average `M_h f = cos(h) f` on every
`l = 1` coordinate eigenfunction.  The consistently normalized operator

`L_h = (6/h^2)(I - M_h)`

therefore has

`lambda_1,h = 6(1-cos h)/h^2`

`           = 3[1 - h^2/12 + h^4/360 + ...]`.

Its relative coefficient is `-1/12`, proving that `-1/4` is not universal.
The old unweighted nearest-neighbor toy graph worsened under refinement and
had no derived graph-to-continuum normalization, so its extrapolation is also
withdrawn.

For fixed lattice data and fixed `R`, any time-independent correction changes
only a normalization and leaves the conditional `w = -1` conclusion exactly
unchanged.  If the discretization ratio evolves, no `delta w` bound follows
without a derived evolution law.  The former `10^-120` EOS precision claim is
therefore withdrawn.

## What the declared surface supports

- an exact no-go against deriving the physical spectral-gap/`Lambda` bridge,
  a graph-radius-to-fixed-physical-radius history, or dark-energy EOS from
  `T_F` plus the explicitly granted intrinsic `S^3` spectral data;
- the exact closed-FRW residual
  `Lambda = lambda_1 + 3H^2 - 8 pi G rho`;
- exact throat compatibility `Lambda = lambda_1(S^3_L)` after pure-vacuum,
  time-symmetric Einstein data are supplied;
- the exact conditional implication constant positive vacuum density
  `=> w = -1`;
- non-universality of the former lattice coefficient.

It does **not** support a framework prediction of `w`, `w_0`, or `w_a`; a
framework-level DESI forecast; dark-energy non-clustering; absence of early
dark energy or phantom crossing; identification of a fixed graph radius with a
fixed physical cosmological radius; a numerical `Lambda`;
or a statement that topology protects a scalar Laplacian eigenvalue against
metric deformation.

## Remaining constructive bridge

Non-exhaustive constructive route families include:

1. **Variational action route:** derive a unique covariant term whose physical
   zero-derivative contribution is
   `-2 lambda_1(G) sqrt(-g)`, including exact graph-to-metric normalization,
   conservation, and a proof that independent vacuum terms are absent or
   absorbed.
2. **Cauchy-data compatibility route:** identify the graph `S^3` with a
   physical pure-vacuum time-symmetric slice, prove `K_ij = 0` and `rho = 0`,
   and derive the map from graph radius to de Sitter curvature radius.  This gives throat
   reconstruction; an additional frozen-modulus/action theorem is still
   needed for a constant four-dimensional vacuum source.

These examples are not claimed exhaustive, and the Cauchy-data route is not
sufficient for sourcing by itself.  Until enough additional content is
derived to supply the map, action/source meaning, and physical persistence,
the load-bearing spectral identification remains isolated rather than hidden
in standard cosmological algebra.

## Verification

```bash
python3 scripts/frontier_dark_energy_eos.py
```

Expected result:

```text
runner_check_breakdown = {A: 12, B: 0, C: 0, D: 0, total_pass: 12}
TOTAL: PASS=12 FAIL=0
```

Independent audit is required before any effective status is assigned.  This
source note does not alter audit authority surfaces.
