# Zero-Import Hydrogen: Lepton `1/256` Source-Strength Normalization Gauge Firewall

**Date:** 2026-07-04
**Type:** partial firewall / bounded residual note
**Claim type:** source-action normalization discriminator
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_source_strength_normalization_gauge_firewall.py`

## Scope

The current A2 source/action stack now has two useful conditional positives:

```text
source-coupled local action + slot-resolved full-cell source family
  -> disjoint source controls add linearly,

nonnegative additive source strength + total strength mu(C) = 1
  + tensor-frame transitivity
  -> mu({c}) = 1/256.
```

This note attacks the scale between those two statements. It asks:

```text
Does source-control linearity itself fix the total source-strength section
mu(C) = 1?
```

The answer is no. Source-control linearity supplies vector-space additivity,
not the positive total-strength section. If the local source term is

```text
S_src[j] = h * B_lep * J(j),
J(j) = sum_{c in C} j_c O_c,
C = {0,1,2,3}^4,
|C| = 256,
```

then for any positive `lambda`,

```text
(h, j) -> (h/lambda, lambda j)
```

leaves the product `h * J(j)` invariant. Therefore the split between source
control magnitude and source-coupling amplitude is a normalization gauge
unless a retained theorem, convention, or admitted-and-then-retired import
selects the total source strength.

This does not invalidate the previous source-strength additivity selector. It
sharpens its hypothesis: the theorem proves `1/256` after the source-strength
object has already been placed on the normalized simplex section `mu(C) = 1`.
The remaining physical question is whether the charged-lepton scalar
suppression `S_l` reads that normalized source-strength weight rather than an
unnormalized control amplitude or the product of control amplitude with the
coupling `h`.

## Finite Normalization Split

Let all 256 source controls have the same positive value `a`:

```text
j_c = a  for all c in C.
```

Then

```text
J(j) = a * sum_c O_c,
sum_c j_c = 256a.
```

The normalized source-strength weights are

```text
w_c = j_c / sum_d j_d = a / (256a) = 1/256.
```

But the source term can also be written by moving the total strength into the
front amplitude:

```text
S_src[j] = h * B_lep * a * sum_c O_c
         = H * B_lep * sum_c (1/256) O_c,
H = 256a h.
```

Thus the number `1/256` is the normalized source-weight coordinate, while the
number multiplying the action before the section is fixed is `h*a`. Unless the
framework supplies `H = 1`, or supplies that `S_l` is the normalized weight
`w_c`, the charged-lepton scale is not fixed by source-control linearity.

A concrete rescaling shows the hazard. Starting from normalized uniform
weights, choose `lambda = 16`:

```text
h * (1/256) = (h/16) * (1/16).
```

The same source term can be represented with a `1/16` control coefficient and
a rescaled source-coupling amplitude. That is why the RN/Fisher source-unit
number `1/16` cannot be rejected by algebraic linearity alone; the difference
between `1/16` and `1/256` becomes physical only after the source-strength
section and the `S_l` readout identity are fixed.

## What This Moves

The source/action residual should now be split more finely:

| sub-wall | content | status after this note |
|---|---|---|
| W1 | source-coupled local-action convention | still supplied/conditional |
| W2 | charged-lepton full-cell source family `J(j)` | still supplied/conditional |
| W3 | source-control linearity | conditionally supported by the source-control linearity note |
| W4a | positive source-strength cone | still open |
| W4b | total-strength section `mu(C) = 1` | still open; not fixed by linearity |
| W4c | `S_l` reads normalized source weight rather than amplitude/coupling | still open |
| W5 | tensor-frame relabeling symmetry for the source strengths | conditionally supported once the physical frame and semantics are supplied |
| W6 | precision correction from exact `256` to the comparator divisor | still open |

The immediate next theorem is no longer merely "show additivity." It is:

```text
charged-lepton source strengths live on a positive normalized simplex section,
and the scalar suppression S_l is the singleton normalized source weight.
```

That theorem could be a definition/convention ratified by the framework, a
bridge theorem from source-coupled action, or an import-retirement path. It
cannot be silently inherited from vector-space linearity.

## Authority Boundary

| source | supplies | boundary here |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_CONTROL_LINEARITY_SUPPORT_2026-07-04.md` | `J(j_A + j_B) = J(j_A) + J(j_B)` and source-term additivity after the convention and source family are supplied | no positivity, no total-strength section, no `S_l` identity |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_ADDITIVITY_SELECTOR_SUPPORT_2026-07-04.md` | `mu({c}) = 1/256` after nonnegative finite additivity, `mu(C) = 1`, and transitivity are supplied | no derivation of the total-strength section or the physical source-strength semantics |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md` | `dS_lep/dj_c = h * B_lep * O_c` after the source-coupled convention and lepton full-cell source are supplied | no fixation of the split between `h` and `j_c` |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md` | source controls select the tensor-product matrix-unit frame relative to `J(j)` | no normalization of source controls |
| `SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md` | RN/Fisher source-unit normalization; uniform 256-channel coefficient `1/16` | not an L1 source-strength section |
| approved primitives | minimal one-site algebra, OS0 kinetic-form isotropy, units/state discipline | no source/action bridge, weighting, normalization rule, readout bridge, mass value, or `S_l` |

The primitive registry was checked. Approved primitives are used only within
their declared content; no primitive supplies a dimensionless source-strength
normalization rule, source/action observable identity, or charged-lepton
scale value.

## Record-Additivity Firewall

The Record axiom says finite scalar readout is additive over pairwise-disjoint
records. That does not fix the normalization of source controls. Record
formation now belongs to the minimal axiom surface, but it still does not
supply which admissible possibility forms, at which site, with what weight, or
at what rate. Therefore Record additivity and Record formation do not supply:

- the source/action convention;
- the full-cell lepton source family;
- the positive source-strength cone;
- the total-strength section `mu(C) = 1`;
- the identity that `S_l` reads normalized source weight.

## Open PR Alignment

Open PRs were checked on 2026-07-04 before writing this note and refreshed
again after `#4942`, `#4943`, and `#4944` appeared. Merge-state labels are
moving review metadata, not proof inputs. The current open-review surface does
not close the source-strength normalization gauge:

| PR | merge state at refresh | effect on this firewall |
|---|---:|---|
| `#4938` K/CPT orbit-constancy supplied-context bridge | `DIRTY` | repairs theta-chain/readout premise location under supplied finite readout context; no lepton source-strength normalization or `S_l` theorem |
| `#4939` AC(i) dynamical-index occupancy no-go | `CLEAN` | blocks an AC(i) occupancy shortcut; no lepton source-strength normalization or charged-lepton scalar source theorem |
| `#4940` rule achirality from minimality | `CLEAN` | theta gauge-side/admissibility achirality and law-achiral/state-free context; no lepton source normalization, `m_e`, `alpha(0)`, or hydrogen input |
| `#4941` AC(i) determinant-order/chiral L-R no-go | `CLEAN` | blocks determinant-order/chiral L-R AC(i) shortcuts; no lepton source-strength normalization or `S_l` theorem |
| `#4942` AC(i) mode-set / corner-transfer no-go | `CLEAN` | blocks K-covariant corner-transfer and mode-set shortcuts for AC(i); no lepton source-strength normalization or `S_l` theorem |
| `#4943` stale-green runner-cache repair sweep | `DIRTY` | repairs/regenerates runner caches and reports honest-red science regressions; no charged-lepton source normalization, `m_e`, `alpha(0)`, or hydrogen theorem |
| `#4944` AC(i) matter-action/statistics no-go | `UNSTABLE` | blocks matter-action/statistics shortcuts for AC(i)'s statistical-grain selector; no lepton source-strength normalization, `S_l`, `m_e`, `alpha(0)`, or hydrogen theorem |

These PRs are review context, not proof inputs. If one lands later with a
charged-lepton source-normalization theorem, this firewall should be revisited.

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "source-control linearity
closes A2/source normalization" is **not** shipped. The narrowed claim is:

```text
Source-control linearity and source-coupled action are invariant under
positive rescaling of source controls paired with inverse coupling rescaling;
therefore total source-strength normalization mu(C) = 1 is an extra
section/semantic choice unless supplied by a retained theorem, convention, or
explicit import-retirement route.
```

Verdict tag: broad A2/S_l closure fails; narrowed source-strength normalization gauge firewall passes.

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| source-control linearity | Use `J(j_A+j_B) = J(j_A)+J(j_B)` to derive normalized singleton strength. | ATTEMPTED. It supplies vector additivity but remains invariant under positive rescaling. |
| source-coupling amplitude | Use `S_src[j] = h * B_lep * J(j)` to fix the source scale. | ATTEMPTED. The split `(h, j) -> (h/lambda, lambda j)` leaves the source term invariant. |
| source-strength additivity selector | Use finite additivity plus total strength. | PARTIAL. It gives `1/256` only after `mu(C) = 1` is supplied. |
| Record additivity and formation | Transfer finite record-readout additivity to source controls. | RULED OUT BY PRIOR BOUNDARY. Record additivity is a readout rule over records and supplies no source/action normalization. |
| RN/Fisher source-unit route | Use the retained RN/Fisher source-unit precedent. | ATTEMPTED. Uniform 256-channel source-unit amplitude gives `1/16`, not L1 singleton weight `1/256`. |
| squared-amplitude route | Square the RN/Fisher amplitudes to recover `1/256`. | ATTEMPTED. It changes the object to a squared-amplitude/probability weight, not the linear action coefficient. |
| determinant/log-volume route | Bypass normalized source controls with an invariant volume theorem. | OPEN. It could replace this route, but no charged-lepton theorem is supplied here. |
| primitive/realized-state shortcut | Appeal to approved primitives or pointwise realized-state evaluation. | RULED OUT AS ZERO-IMPORT CLOSURE. The registry supplies no source/action, weighting, normalization rule, readout bridge, or value. |

### N2 - Wall-Independence Audit

The collapsed wall set is:

| wall | content |
|---|---|
| W1 | source-coupled local-action convention is adopted or derived |
| W2 | charged-lepton scalar source is a full-cell slot-resolved source family |
| W3 | source controls add linearly |
| W4a | source controls are restricted to a positive source-strength cone |
| W4b | total source strength is fixed by the section `mu(C) = 1` |
| W4c | charged-lepton `S_l` reads normalized source weight, not source amplitude or coupling |
| W5 | tensor-frame relabeling symmetry is physical for those source strengths |
| W6 | exact `256` is corrected to, or replaced by, the physical comparator divisor |

| pair | closes automatically? | conclusion |
|---|---|---|
| W1 with W2-W6 | no | convention alone does not supply source family, positivity, normalization, `S_l`, symmetry, or precision |
| W2 with W3-W6 | partial only | W1 plus W2 supports W3, but W2 alone does not fix positivity or scale |
| W3 with W4a-W6 | no | linearity allows arbitrary signs and arbitrary scale unless further restricted |
| W4a with W4b-W6 | no | positivity does not choose total strength one or the `S_l` readout identity |
| W4b with W4c-W6 | no | normalization does not by itself say which physical scalar reads the normalized weight |
| W4c with W5-W6 | no | the sector identity does not prove tensor-frame symmetry or precision |
| W5 with W6 | no | uniformity does not derive the precision correction |

No wall is collapsed by this note except the wording of the old W4 into W4a,
W4b, and W4c. That split is the point of the firewall.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `source-coupled local action` | explicit W1 convention gate |
| `slot-resolved` / `full-cell` | explicit W2 source-family hypothesis |
| `positive source vector` | explicit W4a hypothesis, not derived |
| `normalized` / `mu(C) = 1` / `total-strength section` | explicit W4b residual, not background |
| `S_l reads normalized source weight` | explicit W4c residual, not assumed |
| `by convention` / `section` | possible partial-closure path, not silent derivation |
| `primitive` / `approved` / `registry` | registry-limited content only |

No source normalization, positivity, source family, tensor-frame symmetry,
sector identity, or mass value is hidden as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| source-control linearity support | algebraic additivity of disjoint source controls | W3 linearity | yes |
| source-strength additivity selector support | `1/256` after nonnegative additivity, total strength, and transitivity | downstream of W4a/W4b/W5 | yes as conditional contrast |
| source-coupled attachment support | derivative attachment of source directions to D17 block | W1/W2 attachment only | yes, but not normalization |
| source-slot frame selector support | source family selects tensor matrix-unit frame | W2/frame selector | yes, but not normalization |
| RN/Fisher source-measure theorem | source-unit/Fisher normalization gives `1/16` on 256 channels | norm-domain contrast | yes |
| `#4941` AC(i) determinant-order/chiral L-R no-go | AC(i) determinant/readout bridge shortcut | source-normalization gauge | no; cited only as open PR context |

Only matching residuals are used as support. Non-matching open PRs are not
used as proof witnesses.

### N5 - Rhetoric Audit

| phrase | tested resolution | result |
|---|---|---|
| "linearity does not fix normalization" | coefficient-vector and local-action-product resolution | tested: rescaling `j` and inverse-rescaling `h` preserves `h*J(j)` |
| "Record additivity does not fix source normalization" | axiom/readout resolution only | tested against minimal axiom wording; no claim about future source/action bridges |
| "RN/Fisher gives `1/16`" | uniform 256-channel source-unit resolution | tested; squared-amplitude and L1 alternatives separated |
| "primitive shortcut does not close zero-import normalization" | approved primitive registry resolution | tested by registry and primitive notes; no claim about future owner-approved primitive updates |

No lattice-wide universal no-go is shipped. The result is a local
source-normalization gauge firewall for the current A2 route.

### N6 - Partial-Closure Path Scan

Potential closure paths found:

| path | status | what it would close |
|---|---|---|
| Ratify `mu(C) = 1` as a source-strength section for charged-lepton scalar sources | open convention/bridge route | W4b total-strength section |
| Define `S_l` as the normalized singleton source-strength weight for the supplied full-cell source family | open semantic route | W4c `S_l` readout identity |
| Derive a source-action Noether/response normalization from the local action convention | open theorem route | W4a/W4b if it fixes positive total strength |
| Derive a determinant/log-volume scalar directly | open bypass route | could bypass W4 source-strength semantics |
| Use RN/Fisher source-unit then square amplitudes | known alternate object | could close a probability-weight route, not the linear action coefficient without another bridge |

This firewall therefore does not say a new axiom is required. It says the
normalization section or semantic bridge must be supplied explicitly and then
audited.

### N7 - Steelman

A strong objection is that the total-strength section may be pure bookkeeping:
once the charged-lepton source family is named, source "strength" could be
defined only up to normalized weights, with the overall amplitude assigned to
`h` by convention. Under that framing, `mu(C) = 1` would be a harmless
coordinate section, not a physics import; the previous additivity theorem plus
tensor-frame transitivity would then close `1/256` as soon as the repo ratifies
that `S_l` reads the normalized coefficient. This objection is strong enough
that the broad no-go is not shipped. The current retained surface has not yet
ratified that section or the `S_l` identity for the charged-lepton scalar
source, so this note records the exact import-retirement target.

### N8 - Cross-Cycle Echo

Similar walls in the repo have been retired only when the missing object was
named as a convention, bridge, supplied context, or approved primitive and then
checked:

| prior shape | mechanism | relevance |
|---|---|---|
| scale-reference primitive | approved units primitive | dimensionful scale can be a registered primitive; it does not supply dimensionless source normalization |
| kinetic-isotropy primitive | approved structural graining primitive | a structural section can be ratified, but only to its declared content |
| K/CPT supplied-context bridge in `#4938` | moves orbit/readout context out of axiom content into supplied bridge context | similar route could ratify source-normalization context, but has not done so |
| source-coupled local-action candidate | convention/admission candidate | source-action attachment is a candidate convention, not yet total-strength normalization |
| RN/Fisher source-unit theorem | retained source-unit normalization | normalizes a different object and lands at `1/16` for 256 channels |

Gate result: `PASS` for the narrowed firewall and `FAIL` for the broad closure
claim.

## Non-Claims

- No derivation of `S_l = 1/256`.
- No derivation of the source-coupled local-action convention.
- No derivation that the charged-lepton scalar source is a full-cell
  slot-resolved source family.
- No derivation that source controls are positive source strengths.
- No derivation of total normalization `mu(C) = 1`.
- No derivation that `S_l` reads normalized source weight.
- No derivation of tensor-frame relabeling symmetry as a physical source
  symmetry.
- No derivation of the `256.08` precision correction.
- No derivation of `m_e`, Koide readout, `alpha(0)`, or hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_source_strength_normalization_gauge_firewall.py
```

The verifier checks the positive-rescaling invariance, the finite
normalization split, the `1/16` versus `1/256` contrast, the cited authority
boundary, and the non-claim guard.
