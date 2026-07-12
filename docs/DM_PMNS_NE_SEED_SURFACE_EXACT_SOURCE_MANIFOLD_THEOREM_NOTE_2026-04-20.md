# DM PMNS Fixed `N_e` Seed-Surface Exact Source-Manifold Theorem

**Claim type:** bounded_theorem
**Date:** 2026-04-20  
**Lane:** PMNS / `I5` remaining angle-pin task  
**Status:** support - structural or confirmatory support note
full positive `I5` closure  
**Does not close:** a framework-native point-selection law on the exact PMNS
source manifold  
**Dedicated verifier:**  
`scripts/frontier_dm_pmns_ne_seed_surface_exact_source_manifold_theorem_2026_04_20.py`

## Scope and tier

This note is a **bounded structural-regularity claim about the preimage of an
empirical target** on a supplied seed parameterization. It does **not** derive
the empirical target triple from the baseline physical `Cl(3)` local algebra
on the `Z^3` spatial substrate alone.

What is claimed (and what the verifier certifies):

1. on the cited supplied fixed `N_e` seed surface `S_Ne`
   (see Inputs below), the cited algebraic angle map `F_Ne` admits at least
   three distinct preimages of the empirical target triple
   `T = (0.307, 0.0218, 0.545)` to numerical precision, established by a
   deterministic compact-chart lattice cover (independent of the polished
   starts listed below) plus local polishing;
2. at every checked preimage point, the finite-difference Jacobian of
   `F_Ne` is rank `3` and that rank is stable across two independent
   step-size scales;
3. the five cited current conditional nonlocal seed-surface candidate
   points (`aligned seed`, `low-action stationary`, `high-action stationary`,
   `constructive eta=1 closure`, `constructive witness`) all miss `T` by
   macroscopic `chi^2 > 0.03`;
4. three selector observables (relative action, transport output on the
   favored column, source cubic) vary by amounts well above their noise floor
   along the checked preimage representatives, so none of them is constant
   on the local preimage manifold.

The empirical target `T` is the NuFit 5.3 / PDG normal-ordering best-fit
central triple
`(sin^2 theta_12, sin^2 theta_13, sin^2 theta_23) = (0.307, 0.0218, 0.545)`,
also used as the comparator triple in
[`DM_PMNS_UPPER_OCTANT_SOURCE_CUBIC_SELECTOR_THEOREM_NOTE_2026-04-20.md`](./DM_PMNS_UPPER_OCTANT_SOURCE_CUBIC_SELECTOR_THEOREM_NOTE_2026-04-20.md)
and
[`DM_NEUTRINO_SOURCE_SURFACE_PERTURBATIVE_UNIQUENESS_THEOREM_NOTE_2026-04-17.md`](./DM_NEUTRINO_SOURCE_SURFACE_PERTURBATIVE_UNIQUENESS_THEOREM_NOTE_2026-04-17.md).
It is an **observational comparator**, not a derived framework output. Every
chi-squared in this note is `(F_Ne(p) - T)^T (F_Ne(p) - T)` and is read as
"how close in the angle-triple space is the source point `p` to the empirical
comparator", not as a sub-axiomatic derivation of `T`.

Tier on the audit ledger: this is a **bounded existence-plus-regularity
sub-derivation conditional on an empirical comparator**. It is the correct
shape to reduce the `I5` task to a sharper structural question (a missing
2-real point-selection law on the certified preimage manifold), but it does
not, by itself, supply that law.

## Inputs (cited authorities)

This note builds on, and re-uses without re-deriving, the following supplied
framework objects. The verifier imports each of them directly from the cited
runner, so the algebraic identities they assert are also re-checked at the
preimage representatives in the runner.

- **The canonical `Y_e`/`H_e` Hermitian block** (`canonical_h(x,y,delta)`)
  — defined and re-used from the PMNS projector-interface note  
  [`DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md`](./DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md).
- **The one-sided active-projector packet readout** (`active_packet_from_h`)
  — `|U_PMNS|^2 = |U_act(H_e)|^2^T` on the charged-lepton-side branch — from  
  [`DM_LEPTOGENESIS_PMNS_ACTIVE_PROJECTOR_REDUCTION_NOTE_2026-04-16.md`](./DM_LEPTOGENESIS_PMNS_ACTIVE_PROJECTOR_REDUCTION_NOTE_2026-04-16.md).
- **The supplied `N_e` seed pair** `(Xbar_Ne, Ybar_Ne) = (169/300, 23/75)`
  used as the conditional seed surface center, from
  [`DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_CONDITIONAL_CALCULATOR_NOTE_2026-07-12.md`](./DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_CONDITIONAL_CALCULATOR_NOTE_2026-07-12.md)
  and used downstream in
  [`DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_STATIONARITY_THEOREM_NOTE_2026-04-16.md`](./DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_STATIONARITY_THEOREM_NOTE_2026-04-16.md)
  and
  [`DM_LEPTOGENESIS_PMNS_REDUCTION_EXHAUSTION_THEOREM_NOTE_2026-04-16.md`](./DM_LEPTOGENESIS_PMNS_REDUCTION_EXHAUSTION_THEOREM_NOTE_2026-04-16.md).
- **The compact chart `(u_1,u_2,v_1,v_2,delta) -> (x,y,delta)` surjective
  onto `S_Ne`** (`compact_chart_to_source`) — defined in  
  [`DM_LEPTOGENESIS_PMNS_REDUCED_SURFACE_SELECTOR_SUPPORT_NOTE_2026-04-16.md`](./DM_LEPTOGENESIS_PMNS_REDUCED_SURFACE_SELECTOR_SUPPORT_NOTE_2026-04-16.md).
  The runner re-checks that polished and grid-lifted preimage representatives
  in fact lie on `S_Ne` (mean-constraint check).
- **The relative-action observable**
  `S_rel(H_e || H_seed) = Tr(H_seed^{-1} H_e) - log det(H_seed^{-1} H_e) - 3`
  — from the bounded relative-action conditional calculator cited above.
- **Selector-family points used in the miss table**:
  - `aligned seed` is the trivial fixed-seed point with `x = (Xbar_Ne,...)` and
    `y = (Ybar_Ne,...)`, supplied by the relative-action conditional calculator.
  - `low-action stationary` and `high-action stationary` come from  
    [`DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_STATIONARITY_THEOREM_NOTE_2026-04-16.md`](./DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_STATIONARITY_THEOREM_NOTE_2026-04-16.md)
    (the runner re-uses `favored_column_and_extremal_params`,
    `closure_point_on_ray`, `constrained_stationary_point`, and
    `HIGH_SOURCE_REF`, `HIGH_SOURCE_REF_Y`).
  - `constructive eta=1 closure` and `constructive witness` come from  
    [`DM_LEPTOGENESIS_PMNS_CONSTRUCTIVE_CONTINUITY_CLOSURE_THEOREM_NOTE_2026-04-17.md`](./DM_LEPTOGENESIS_PMNS_CONSTRUCTIVE_CONTINUITY_CLOSURE_THEOREM_NOTE_2026-04-17.md)
    via `path_point` and `eta_columns_from_active` (the latter under the alias
    `constructive_eta_columns`).

No additional axioms or imports are introduced. The structural claim items
(1)-(4) above are independent of the polished hard-coded starts (existence is
re-established by a deterministic compact-chart lattice cover) and independent
of the finite-difference step size (rank is re-checked across two
step-size scales).

## Summary

The current `I5` gap is now sharper than “derive three PMNS angles somehow.”

On the supplied fixed `N_e` seed surface

```text
S_Ne
  = { (x,y,delta) :
      x_i > 0, y_i > 0,
      (x_1+x_2+x_3)/3 = Xbar_Ne,
      (y_1+y_2+y_3)/3 = Ybar_Ne } ,
```

with

```text
Xbar_Ne = 0.5633333333333334,
Ybar_Ne = 0.30666666666666664,
```

the empirical PMNS angle comparator

```text
(sin^2 theta_12, sin^2 theta_13, sin^2 theta_23)
  = (0.307, 0.0218, 0.545)
```

is already realized exactly.

But it is **not** realized as an isolated selected point on the current exact
stack. On the verified exact points, the PMNS-angle Jacobian on `S_Ne` has
rank `3`, so the exact preimage is a local `2`-real regular source manifold.
Current exact nonlocal seed-surface selector families miss that manifold by
macroscopic `chi^2`.

So `I5` is reduced to one much sharper remaining object:

> a new `2`-real point-selection law on the comparator preimage manifold inside
> the supplied fixed `N_e` seed surface.

## 1. Setup

On the charged-lepton-side minimal PMNS branch, the canonical active block is

```text
Y_e = diag(x_1,x_2,x_3) + diag(y_1,y_2,y_3 e^{i delta}) C,
H_e = Y_e Y_e^dagger.
```

On the one-sided `N_e` branch, the PMNS packet is already the active packet

```text
|U_PMNS|^2 = |U_act(H_e)|^2^T.
```

So on `S_Ne` the PMNS angle map is the explicit exact map

```text
F_Ne(x,y,delta)
  = (sin^2 theta_12(H_e), sin^2 theta_13(H_e), sin^2 theta_23(H_e))
  in R^3.
```

The current theorem asks:

1. does `F_Ne` already hit the physical target triple exactly?
2. if yes, does the present supplied candidate stack on `S_Ne` already choose that
   point?

## 2. Theorem statement

**Theorem (preimage existence, regularity, and selector-stack miss on the
supplied fixed `N_e` seed surface).** Fix the cited conditional objects from the
Inputs section: the canonical Hermitian block `H_e(x,y,delta)`, the
charged-lepton-side active packet readout `F_Ne`, the seed pair
`(Xbar_Ne, Ybar_Ne) = (169/300, 23/75)`, and the compact chart
`(u_1,u_2,v_1,v_2,delta) -> S_Ne`. Take the empirical comparator triple
`T := (0.307, 0.0218, 0.545)` (NuFit 5.3 / PDG normal-ordering best-fit
central values). Then:

1. the empirical comparator `T` lies in the image of `F_Ne` on `S_Ne`;
2. the verifier exhibits, by two independent constructions
   (a deterministic compact-chart lattice sweep with local polishing, and a
   short list of polished hard-coded starts), multiple distinct source points
   `p in S_Ne` with

   ```text
   F_Ne(p) = T
   ```

   to numerical precision;
3. at each checked preimage point, the finite-difference Jacobian `dF_Ne`
   has rank `3`, and this rank is stable across two independent step-size
   scales;
4. therefore, on the verified regular patch, the preimage

   ```text
   F_Ne^(-1)(T) cap S_Ne
   ```

   is locally a `2`-real source manifold inside the `5`-real seed surface;
5. the five cited current conditional nonlocal seed-surface candidate points

   - aligned seed
     ([relative-action conditional calculator note](./DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_CONDITIONAL_CALCULATOR_NOTE_2026-07-12.md)),
   - low-action stationary branch
     ([relative-action stationarity theorem note](./DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_STATIONARITY_THEOREM_NOTE_2026-04-16.md)),
   - high-action stationary branch
     ([reduced-surface selector support note](./DM_LEPTOGENESIS_PMNS_REDUCED_SURFACE_SELECTOR_SUPPORT_NOTE_2026-04-16.md)),
   - constructive `eta = 1` closure point
     ([constructive continuity closure theorem note](./DM_LEPTOGENESIS_PMNS_CONSTRUCTIVE_CONTINUITY_CLOSURE_THEOREM_NOTE_2026-04-17.md)),
   - constructive witness
     ([same constructive continuity note](./DM_LEPTOGENESIS_PMNS_CONSTRUCTIVE_CONTINUITY_CLOSURE_THEOREM_NOTE_2026-04-17.md)),

   all miss the empirical comparator by `chi^2 > 0.03`;
6. three selector observables (the seed-relative relative action, the
   favored-column transport output, and the source cubic
   `Im(H_12 H_23 H_31)`) all vary by amounts well above the numerical noise
   floor across the checked preimage representatives, so none of them is
   constant on the local preimage manifold.

Hence the current conditional nonlocal candidate stack does **not** pick the
empirical comparator on the charged-lepton-side branch. What remains, on this
branch, is a genuinely new `2`-real point-selection law on the certified
preimage manifold.

The theorem is conditional on the empirical comparator `T`. Replacing `T` by
a different empirical comparator inside the regular patch would carry the
preimage structure through unchanged (the same `F_Ne` and the same chart) and
would yield the same structural statement at the new `T`. The theorem does
not derive `T` from the baseline framework alone.

## 3. Exact source representatives

The verifier certifies several exact source points. Three representative ones
are:

| rep | `x` | `y` | `delta` | `S_rel(H_e || H_seed)` | `eta / eta_obs` | source cubic |
|---|---|---|---:|---:|---:|---:|
| A | `(0.060928, 0.750228, 0.878844)` | `(0.498479, 0.245209, 0.176312)` | `-1.533871` | `4.302174` | `(0.777873, 0.700284, 0.827267)` | `-8.65e-4` |
| B | `(0.172810, 0.702009, 0.815181)` | `(0.453865, 0.263544, 0.202591)` | `0.789612` | `1.938594` | `(0.775999, 0.699960, 0.827260)` | `+1.70e-3` |
| C | `(0.284724, 0.657377, 0.747899)` | `(0.396580, 0.281713, 0.241707)` | `-0.635221` | `0.905124` | `(0.769934, 0.698837, 0.827234)` | `-2.24e-3` |

All three reproduce

```text
(sin^2 theta_12, sin^2 theta_13, sin^2 theta_23)
  = (0.307, 0.0218, 0.545)
```

to the verifier tolerance.

The important point is not the specific coordinates. It is that these points
are **distinct**, yet all lie on the same empirical-comparator preimage fiber.

## 4. Regular-manifold consequence

The seed surface `S_Ne` is `5`-real dimensional. The verifier computes the
finite-difference Jacobian of

```text
F_Ne : S_Ne -> R^3
```

at the checked comparator-matching points and finds

```text
rank dF_Ne = 3.
```

So on that regular patch, the implicit-function heuristic is the correct one:
the empirical PMNS comparator does not have an isolated source. Its preimage is a local
`2`-real manifold.

This is the sharp new reduction:

- existence of comparator-matching PMNS points is no longer the live issue;
- branch isolation is no longer the live issue on this patch;
- the live issue is selecting one point on that exact source manifold.

## 5. Current selector-family miss

The verifier checks the current conditional nonlocal candidate points already
on branch:

| selector-family point | PMNS triple | `chi^2` to target |
|---|---|---:|
| aligned seed | `(0.200000, 0.166667, 0.600000)` | `0.035460` |
| low-action stationary | `(0.921382, 0.546423, 0.003479)` | `0.945939` |
| high-action stationary | `(0.950756, 0.094768, 0.962175)` | `0.593782` |
| constructive `eta=1` closure | `(0.701614, 0.911995, 0.865291)` | `1.050754` |
| constructive witness | `(0.737048, 0.951639, 0.878470)` | `1.160744` |

So the supplied seed-surface candidate families checked here do **not** land on the
empirical-comparator preimage manifold. This is the nonlocal analogue of the later Schur-line
no-go:

- local selector families miss the PMNS target on the active DM source sheet;
- current nonlocal seed-surface selector families miss the PMNS target on the
  charged-lepton-side fixed-seed sheet.

## 6. Why this is stronger than “still open”

Before this theorem, “`I5` is still open” still left two qualitatively
different possibilities:

1. maybe the empirical PMNS comparator has no preimage on the supplied
   charged-lepton-side seed surface;
2. maybe it is present, but the supplied candidate stack still does not choose
   it.

This theorem closes the first possibility positively and the second
negatively.

So the sharpened honest state is:

- the empirical PMNS angle comparator has numerical preimages on the supplied `N_e`
  seed surface;
- the current conditional nonlocal candidate stack does not pick it;
- the remaining `I5` target is a new `2`-real point-selection law on that
  exact manifold.

## 7. Consequence for `I5`

`I5` is not closed by this note.

But it is reduced substantially.

The old phrasing

```text
derive the PMNS angle triple
```

can now be sharpened on the charged-lepton-side branch to

```text
derive a point-selection law on the exact 2-real PMNS source manifold
inside the supplied fixed N_e seed surface.
```

Equivalently:

- the seed pair is supplied exactly,
- the supplied parameterization contains empirical-comparator preimages,
- the remaining science is no longer existence or branch hunting,
- it is the missing point-selection law on the exact source manifold.

That is the correct `I5` reduction to cite after this theorem.

## 8. Audit hygiene

What is not claimed here, and what is:

- **Not claimed**: a first-principles derivation of the empirical PMNS
  triple `T` from `Cl(3)` on `Z^3`. The triple is used here as an
  observational comparator only.
- **Not claimed**: that the polished hard-coded starts in the verifier are
  themselves framework-derived special points. They are convenience anchors;
  the existence of preimages of `T` in `S_Ne` is independently re-established
  by the deterministic compact-chart lattice cover.
- **Not claimed**: that the rank-`3` claim is exact or analytic. It is a
  stable finite-difference rank confirmed across two independent step-size
  scales at the polished preimage representatives.
- **Claimed**: items (1)-(6) of the theorem statement, each individually
  certified by the verifier and each individually conditional only on the
  cited framework authorities plus the empirical comparator `T`.

This shape is the structural existence-plus-regularity claim that is
appropriate as a `bounded` source-theorem support note. It reduces the live
`I5` task on the charged-lepton-side branch to the missing point-selection
law on the certified preimage manifold without making, or relying on, any
claim to have derived `T`.

## 9. Reproduction

```bash
PYTHONPATH=scripts python3 scripts/frontier_dm_pmns_ne_seed_surface_exact_source_manifold_theorem_2026_04_20.py
```

Expected (the runner certifies the cited-authority round-trip identities, the
chart-lattice independent existence sweep, the rank-stability check, the seed
surface mean-constraint check, the selector-family miss table, and the
note-text consistency block):

```text
PASS=27 FAIL=0
```

Runtime: about 30 s on a laptop. The dominant cost is the 405-point
compact-chart lattice sweep with bounded least-squares polishing at each
start.
