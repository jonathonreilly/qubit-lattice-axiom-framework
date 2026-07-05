# Zero-Import Hydrogen: Lepton `1/256` Source-Action Simplex Transfer Discriminator

**Date:** 2026-07-04
**Type:** partial-narrowing discriminator note
**Claim type:** meta / source-action support
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_source_action_simplex_transfer_discriminator.py`

## Scope

The previous A2 notes narrowed the lepton `1/256` lane:

- `ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md`
  separated projection/Born trace from algebra-basis coefficient density.
- `ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md`
  showed that `1/256` is the L1 algebra-coordinate density class, while the
  RN/Fisher/Hilbert-Schmidt source-unit class gives `1/16`.
- `ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md`
  showed that uniform density is stable under tensor-frame relabelings once a
  physical tensor frame and L1 semantics are supplied.

This note tests the next tempting shortcut:

```text
Can the top-sector RN/Fisher source-action precedent be transferred directly
to the charged-lepton 256-channel source and thereby derive 1/256?
```

The answer is no as a direct transfer. The top source-action precedent selects
a primitive unit source vector, i.e. the L2/RN/Fisher class. On 256 uniform
channels that class gives coefficient `1/sqrt(256) = 1/16`, not `1/256`.

The positive arithmetic is also exact: a **linear action simplex average**
over 256 supplied tensor-frame coordinates gives coefficient `1/256`. But
that is a different source semantics from the primitive RN/Fisher unit. A
future theorem must show that the charged-lepton scalar suppression is a
linear action coefficient density, not merely a primitive source-coordinate
amplitude.

## Exact Transfer Split

Let `N` be the number of supplied source coordinates.

Two natural uniform source classes are distinct:

| class | coefficient per coordinate | normalization |
|---|---:|---|
| primitive RN/Fisher/L2 source unit | `1/sqrt(N)` | `sum_i u_i^2 = 1` |
| linear action simplex density | `1/N` | `sum_i w_i = 1` |

For the top precedent, `N = 6`:

```text
u_top,i = 1/sqrt(6)
w_top,i = 1/6
```

The retained top source-unit packet uses the first number, not the second. It
selects a unit vector amplitude over the six `Q_L` color-isospin components.

For the lepton tensor coordinate target, `N = 256`:

```text
u_256,i = 1/sqrt(256) = 1/16
w_256,i = 1/256
```

Thus the same RN/Fisher source-unit logic that supports the top coefficient
would land the lepton tensor source at `1/16`. To reach `1/256`, the source
must be read as a simplex density or linear action average over the supplied
coordinates:

```text
O_avg = (1/256) sum_{i=1}^{256} O_i.
```

Viewed as an RN/Fisher source coordinate, `O_avg` has norm

```text
||O_avg||_2 = 1/16.
```

Equivalently, it is the primitive unit vector rescaled by

```text
lambda = 1/sqrt(256) = 1/16.
```

The RN/Fisher source-unit theorem explicitly treats such `lambda != 1`
rescalings as non-primitive source coordinates. Therefore the lepton `1/256`
route needs a retained **simplex-density / linear-action-coefficient**
theorem, not a direct copy of the top primitive-source-unit theorem.

## Hydrogen-Facing Consequence

The D17-prime lepton block front factor is

```text
1/sqrt(2).
```

If the four-slot `M_2(C)^tensor4` source is read as a primitive uniform
RN/Fisher unit over 256 coordinates, the suppression is

```text
(1/sqrt(2)) * (1/16).
```

The hydrogen-facing lepton scale target instead needs

```text
(1/sqrt(2)) * (1/256).
```

So the missing factor is exactly `1/16`, the ratio between simplex density
and primitive unit amplitude on 256 channels.

This is not a numerical accident; it is the same L1/L2 split already found in
the source-norm discriminator, now tied to the top source-action precedent.

## What This Moves

This note sharpens A2.1 and A2.2:

| sub-gate | standing after this note |
|---|---|
| A2.1 measure-domain selector | narrowed: the target is a linear action coefficient density / simplex average, not projection probability and not primitive RN source amplitude |
| A2.2 norm-domain selector | narrowed: the target is L1 simplex density, not L2 / RN / Fisher unit |
| A2.3 basis/source-frame selector | still open: the charged-lepton tensor-product matrix-unit source frame must be physically supplied |
| A2.4 coefficient uniformity | conditionally supported by the restricted tensor-frame note once A2.2 and A2.3 are supplied |
| A2.5 charged-lepton source bridge | still open: the selected simplex density must be identified with `S_l` |
| A2.6 precision interface | still open: exact `256` must connect to `256.082435...` or be replaced by a direct noninteger divisor theorem |

The immediate next theorem target is now more precise:

```text
charged-lepton scalar source coefficient
  = linear action simplex density over the supplied M_2(C)^tensor4
    matrix-unit source frame.
```

That theorem would still need A1 carrier authority and A2.5 sector identity,
but it is the right normalization class for `1/256`.

The positive follow-up
`ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md`
proves the finite symmetry half: once a simplex-normalized linear action
source over the supplied tensor-frame coordinates is invariant under local
coordinate relabelings, transitivity forces the unique coefficient `1/256`.
It does not supply the physical source-action theorem or the tensor-frame
selector.

## Repo Authority Alignment

| source | relevant boundary |
|---|---|
| `YT_QUBIT_DEMOCRATIC_TOP_COEFFICIENT_CANDIDATE_NOTE_2026-05-25.md` | The exact top support lemma is a democratic unit vector over six components, giving amplitude `1/sqrt(6)`. It is not a simplex average `1/6`. |
| `YT_PRIMITIVE_SOURCE_UNIT_FISHER_NORMALIZATION_SUPPORT_NOTE_2026-05-25.md` | Primitive source-unit normalization rejects `lambda != 1` as a rescaled source coordinate; this is the L2/RN/Fisher class. |
| `YT_TIER_A_SOURCE_ACTION_TOP_PREMISE_CLOSURE_NOTE_2026-05-29.md` | On the accepted Tier-A source-measure surface, the top source unit closes as `lambda = 1`, `y_33 = 1/sqrt(6)`. It does not derive a lepton simplex density. |
| `SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md` | Gives the RN-cocycle source-unit algebra and Fisher norm `lambda^2`; it supports the contrast with the lepton L1 density class. |
| `OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md` | Records source-coupled local action as an open-gate convention candidate. It can host a future linear-action theorem, but it is not retained source/action closure by itself. |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md` | Establishes the L1-vs-L2 split at `N=256`. |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md` | Establishes finite relabeling invariance of the uniform L1 density once the physical frame and L1 semantics are supplied. |
| `MINIMAL_AXIOMS_2026-06-29.md` | Supplies one-site `M_2(C)` and records-form content, but no source/action identification, probability, weighting, normalization, physical observable bridge, or source frame. |

## Primitive Boundary

The primitive registry was checked following the current no-go-discipline
freshness rules. Approved primitives chain-satisfy only their declared
content:

| node | declared help | boundary here |
|---|---|---|
| `minimal_axioms` | `Z^3`, one-site `M_2(C)`, admissibility, record additivity, generic record formation | no source/action bridge, weighting, normalization, source frame, probability rule, or physical observable identification |
| `kinetic_isotropy_primitive` | OS0 kinetic-form isotropy and fourth regulator slot | no source-density selector, readout bridge, mass ratio, phase, or empirical match |
| `scale_reference_primitive` | one dimensionful ruler | no dimensionless `S_l` or simplex coefficient |
| `realized_state_primitive` | pointwise realized-state evaluation | no state-selection rule, measure, weighting, normalization, preferred state, or value |

## Open PR Alignment

Open PRs were checked on 2026-07-04 before writing this discriminator:

| PR | effect on this source-action simplex discriminator |
|---|---|
| `#4922`, `#4924` Born/composite Gleason and graded-constraint interface | Projection/frame-function context. Helpful for the `1/16` projection/RN side, not a simplex-density selector. |
| `#4923` record scope semantics / arrow substrate | Supplies record-scope and arrow-substrate context, but no source/action measure, frame selector, or L1 simplex semantics. |
| `#4928` Tier-A block03 AC value face | Koide bookkeeping. It does not select the charged-lepton source density. |
| `#4929` Tier-A block04 species-bridge partial-retirement | Species-bridge import-retirement context only; not an `S_l` source/action theorem. |
| `#4930` Tier-A block05 R-eta route pruning | Prunes R-eta angle-native candidates and sharpens K2 to a licensed bridge target `Phi = S_sum = 2/3`; no lepton `1/256` source semantics. |
| `#4931` Tier-A block06 R-eta occurrence axiom shortcut | Blocks treating the updated `Records form` axiom as an R-eta occurrence/event license. It is Koide/R-eta hygiene, not a source-action simplex theorem for `S_l`. |
| `#4903` D4 kinetic pattern dichotomy | Potential A1 tensor-lift context, but no A2 source/action density selector. |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "source-action cannot
derive `1/256`" is **not** shipped. The narrowed claim is:

```text
The existing top/RN/Fisher primitive source-unit route transfers to a
256-channel uniform coefficient as 1/16, not 1/256. The 1/256 target is a
linear action simplex density and needs a separate charged-lepton source
semantics theorem.
```

Verdict tag: broad no-go fails; narrowed source-action simplex transfer discriminator passes.

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| RN/Fisher primitive source unit | Transfer the top source-unit theorem to 256 uniform channels. | ATTEMPTED. Gives `1/sqrt(256)=1/16`, not `1/256`. |
| top democratic source precedent | Treat the top `1/sqrt(6)` as evidence for a lepton source coefficient. | ATTEMPTED. The top precedent is a unit-vector amplitude, not a simplex density; direct transfer gives the wrong class. |
| linear action simplex average | Read the charged-lepton scalar coefficient as `(1/256) sum_i O_i`. | ATTEMPTED. Gives exact `1/256`, but the physical charged-lepton source-action theorem is still missing. |
| source-coupled local-action convention | Use the open-gate local action convention to host coefficient densities. | OPEN. The convention is a candidate admission shape, not current retained closure. |
| projection/Born route | Use a rank-one projection or frame-function normalization on `M_16(C)`. | RULED OUT AS COMPLETE `S_l` ROUTE by the readout discriminator: it gives `1/16`. |
| determinant/log-volume route | Bypass source-coordinate amplitude with a determinant or volume-density theorem. | OPEN. Right normalization shape, but no charged-lepton theorem is supplied here. |
| restricted tensor-frame uniformity | Use finite relabeling invariance of uniform density. | PARTIAL. It supports uniformity after frame and L1 semantics are supplied; it does not supply those selectors. |
| realized-state route | Let realized-state evaluation choose the density. | RULED OUT AS ZERO-IMPORT CLOSURE. The primitive supplies pointwise evaluation only, no measure or normalization. |

### N2 - Wall-independence audit

The collapsed wall set is:

| wall | content |
|---|---|
| W1 | A1 carrier: the charged-lepton scalar source carries the four OS0 algebra slots |
| W2 | A2.1 measure-domain selector: linear action coefficient density over projection/RN amplitude |
| W3 | A2.2 norm-domain selector: L1 simplex density over L2/Fisher unit |
| W4 | A2.3 basis/source-frame selector: tensor-product matrix-unit source frame is physical |
| W5 | A2.5 charged-lepton sector/source identity for `S_l` |
| W6 | A2.6/A3 precision correction from exact `256` to the comparator divisor |

Pairwise audit:

| pair | closes automatically? | conclusion |
|---|---|---|
| W1 with W2-W6 | no | carrier does not choose measure, norm, frame, sector identity, or precision |
| W2 with W3-W6 | no | linear action semantics does not by itself choose L1 normalization, frame, sector identity, or precision |
| W3 with W4-W6 | no | L1 simplex density does not choose the physical frame, sector identity, or precision |
| W4 with W5-W6 | no | frame selection does not identify the coefficient with `S_l` or fix precision |
| W5 with W6 | no | sector identity does not derive the precision correction |

This note attacks only W2/W3 by classifying the transfer. It leaves W1, W4,
W5, and W6 live.

### N3 - Hidden-wall scan

| phrase class | classification |
|---|---|
| `source-action` | explicit open selector target, not assumed. |
| `simplex` / `linear action average` | explicit candidate semantics, not derived. |
| `primitive source unit` | cited RN/Fisher route; not used as L1 density. |
| `transfer` | tested route, not a proof of physical identity. |
| `top precedent` | bounded source-unit support only, not lepton closure. |
| `primitive` | registry-limited content only. |

No lepton source-action bridge is left as background.

### N4 - Residual matching

| cited surface | residual it attacks | match to this note |
|---|---|---|
| Y_T primitive source-unit Fisher support | primitive unit-source normalization, `lambda = 1` | yes as direct-transfer contrast |
| Y_T Tier-A source-action closure | top `lambda=1`, `y_33=1/sqrt(6)` on Tier-A source-measure surface | yes as top precedent boundary |
| source-measure RN-cocycle theorem | RN/Fisher source-unit algebra and `lambda^2` norm | yes as L2 contrast |
| L1 source-norm discriminator | `1/256` as L1 density and `1/16` as L2 unit | yes |
| restricted tensor-frame support | uniform density relabeling invariance after selectors | partial: supports uniformity, not source semantics |
| open PRs `#4928`-`#4931` | Koide/R-eta bookkeeping and route pruning | no direct `S_l` closure |

Only the source-normalization transfer residual is counted here.

### N5 - Rhetoric audit

The note avoids saying "`1/256` is not derivable." Tested resolutions are:

| resolution | tested? | outcome |
|---|---|---|
| top `N=6` primitive source unit | yes | `1/sqrt(6)`, not `1/6`. |
| lepton `N=256` primitive source unit | yes | `1/16`, not `1/256`. |
| lepton `N=256` simplex density | yes | exact `1/256`. |
| D17 front factor plus primitive unit | yes | `(1/sqrt(2))*(1/16)`. |
| D17 front factor plus simplex density | yes | `(1/sqrt(2))*(1/256)`. |
| physical lepton source-action theorem | not closed | named A2.1/A2.2/A2.5. |

### N6 - Partial-closure path scan

Legitimate closure paths remain:

| path | what it could close |
|---|---|
| retained source-action theorem identifying the lepton scalar coefficient with a linear simplex average | A2.1 and A2.2 |
| source-coupled local-action convention retirement or audit acceptance in the lepton scalar sector | could host A2.1 without a new axiom |
| retained carrier theorem deriving the four OS0 algebra slots on the scalar coefficient | A1 and part of A2.3 |
| determinant/log-volume theorem matching `1/256` invariantly | possible bypass of the coordinate simplex route |
| charged-lepton source bridge identifying the selected density with `S_l` | A2.5 |
| direct noninteger divisor theorem or controlled correction after exact `256` | A2.6/A3 |

No closure path is called a new axiom merely because it is not yet derived.

### N7 - Steelman

A hostile reviewer can argue that a source-coupled local action is already
linear in its source coefficients, so an action coefficient should be an L1
simplex weight by default. The lepton-scale probe writes
`1/(dim_C M_2(C))^4`, not `1/sqrt(dim_C M_2(C)^4)`, and the restricted
tensor-frame theorem shows that the resulting uniform density is stable under
relabeling. This is the strongest positive route.

The narrow rebuttal is that the top source-action precedent currently audited
through the RN/Fisher route selects primitive unit amplitudes, not simplex
averages. The repo therefore needs an explicit charged-lepton theorem that
the scalar suppression is a linear action density over the tensor-frame
coordinates.

### N8 - Cross-cycle echo

This is the same failure mode as the earlier reciprocal-readout wall: treating
an `N`-component structure as if it automatically supplies `1/N`. The exact
calculation shows two live readings, `1/sqrt(N)` and `1/N`, with different
source semantics. The artifact narrows the residual to the source-action
simplex theorem rather than repeating the broad "256 exists, therefore
suppression exists" move.

## Non-Claims

- No derivation of `S_l = 1/256`.
- No derivation that the charged-lepton scalar source uses linear action
  simplex-density semantics.
- No derivation that the charged-lepton scalar source uses the tensor-product
  matrix-unit frame.
- No derivation of the charged-lepton tensor lift.
- No derivation of the charged-lepton source bridge.
- No derivation of the `256.082435...` precision correction.
- No derivation of `m_e`, Koide readout, `alpha(0)`, or hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_source_action_simplex_transfer_discriminator.py
```

The verifier checks the top/lepton transfer arithmetic, the RN/Fisher versus
simplex split, the D17 front-factor consequence, the primitive boundaries, the
open PR context, the no-go discipline markers, and the non-claim boundary.
