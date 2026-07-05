# Zero-Import Hydrogen: Lepton `1/256` Source Positive-Cone Discriminator Support

**Date:** 2026-07-04
**Type:** partial discriminator / positive support note
**Claim type:** conditional source-strength domain support
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_source_positive_cone_discriminator.py`

## Scope

The projective-simplex section note assumes that charged-lepton source
strength is a nonzero nonnegative projective source ray:

```text
[j] in (R_{\ge 0}^C \ {0}) / R_{>0},
sigma([j])_c = j_c / sum_d j_d.
```

This note attacks the first unresolved word in that assumption:

```text
nonnegative.
```

The point is not that raw source probes must be nonnegative. Signed or complex
infinitesimal source coefficients are useful response probes for
`dS/dj_c`. The claim is narrower: if the object being read by the
charged-lepton scale is a source-strength measure, then it must live in an
ordered positive cone. Signed or complex probe amplitudes do not themselves
define normalized source strengths.

## Conditional Theorem

Let

```text
C = {0,1,2,3}^4,
|C| = 256.
```

Assume a source-strength assignment on disjoint source-control blocks:

```text
mu : P(C) -> R
mu(empty) = 0
mu(A union B) = mu(A) + mu(B)  for A cap B = empty
mu(A) <= mu(B)  for A subset B
```

Then every singleton strength is nonnegative:

```text
0 = mu(empty) <= mu({c}).
```

Thus finite additivity plus monotonicity places source strengths in
`R_{\ge 0}`. If `mu(C) > 0`, the normalized singleton weights

```text
w_c = mu({c}) / mu(C)
```

define a nonnegative simplex point. If, in addition, the tensor-frame source
relabeling group acts transitively on `C`, all singleton weights are equal and

```text
w_c = 1/256.
```

This is not a derivation of charged-lepton `S_l`. It is a domain
discriminator: positivity follows from monotone source-strength semantics, not
from raw source-control linearity alone.

## Signed And Complex Probe Firewalls

Raw source probes can be signed:

```text
J(j) = sum_c j_c O_c.
```

For example, let one coordinate have `j_c = -1` and all other coordinates have
`j_d = 1`. The raw sum is positive, so the algebraic L1 ratio exists, but the
distinguished coordinate has negative normalized weight. That cannot be a
source-strength measure.

A zero-sum signed vector is worse:

```text
sum_c j_c = 0.
```

The projective-simplex section is undefined. Complex phases have the same
problem in another form: a complex source amplitude has no order relation
`mu(A) <= mu(B)` and cannot by itself be a real source-strength measure.

There are possible salvage routes, but each changes the object:

| salvage route | what changes | boundary |
|---|---|---|
| absolute values `|j_c|` | replaces linear signed controls by a nonlinear magnitude map | does not follow from source-control linearity |
| squared amplitudes `|j_c|^2` | changes the object to a probability/squared-amplitude weight | not the linear action coefficient multiplying `O_c` |
| positive/negative channel split | replaces `C` by `C x {+,-}` | doubles the channel set unless a sign tag is supplied |
| real monotone strength measure `mu` | keeps finite additivity and order | exactly the source-strength semantics still to be derived or ratified |

Thus signed or complex probes remain available for response theory, but the
normalized source-strength readout must use a positive ordered object.

## What This Moves

Before this note, the positive-cone assumption appeared as a separate open
sub-wall under the projective-simplex section. This note collapses it into a
more precise semantic target:

```text
source strength is a real monotone finitely additive measure over disjoint
source-control blocks.
```

Under that semantic target, singleton nonnegativity is automatic. The live
residue is no longer "invent positivity"; it is:

```text
derive or ratify that charged-lepton source strength, not raw probe amplitude,
is the monotone additive object read by the normalized source-probe interface.
```

| sub-wall | status after this note |
|---|---|
| W1 source-coupled local-action convention | still supplied/conditional |
| W2 charged-lepton full-cell source family `J(j)` | still supplied/conditional |
| W3 raw source-control linearity | conditionally supported by the source-control linearity note |
| W4a source-strength positive cone | conditionally supported after monotone finite-additive source-strength semantics are supplied |
| W4b total-strength projective section | conditionally supported by the projective-simplex section note after positive source strength is supplied |
| W4c `S_l` reads normalized source weight | still open |
| W5 tensor-frame uniform ray | conditionally supported after physical source-frame invariance is supplied |
| W6 A3 precision | still open |

## Authority Boundary

| source | supplies | boundary here |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md` | L1 section for a nonzero nonnegative projective source ray | assumes the positive ordered source-strength domain |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_NORMALIZATION_GAUGE_FIREWALL_2026-07-04.md` | raw source controls rescale against `h`; positivity and total section remain semantic gates | no monotone source-strength theorem |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_ADDITIVITY_SELECTOR_SUPPORT_2026-07-04.md` | finite additive nonnegative source strength plus total strength and transitivity gives `mu({c}) = 1/256` | assumes the physical source-strength semantics |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_CONTROL_LINEARITY_SUPPORT_2026-07-04.md` | raw source controls add linearly under the source-coupled convention | linearity alone allows signed probes and does not impose an order |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_COMPRESSION_SUPPORT_2026-07-04.md` | compressed interface target includes the projective source-strength clause | does not ratify that interface |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COORDINATE_UNFIXED_CHOICE_LABEL_FREE_SUPPORT_2026-07-04.md` | conditional `#4952` support against law-level coordinate tags | no positivity or source-strength readout theorem |
| approved primitives | scale reference, OS0 kinetic-form isotropy, and realized-state evaluation discipline | no source/action convention, weighting rule, normalization rule, probability rule, source-strength order, source-probe interface, mass value, or `S_l` |

The primitive registry was checked. Approved primitives are not walls, but
they also do not supply the source-strength positive cone or the
charged-lepton `S_l` readout identity.

## Open PR Alignment

Open PRs were checked on 2026-07-04 before writing this note and refreshed
after `#4956` appeared and `#4952` closed without merge.

| PR | current effect on this positive-cone lane |
|---|---|
| `#4956` AC first-order determinant retirement-readiness no-go | `UNSTABLE`; AC first-order determinant pruning, no lepton source-strength theorem |
| `#4955` gravity eikonal small-k remainder repair | `CLEAN`; gravity runner/audit repair, no lepton source-strength theorem |
| `#4954` stale sibling-interface runner repair | `CLEAN`; runner-interface hygiene and one escalated `g_bare` science regression, no lepton source-strength theorem |
| `#4953` K-real physicalization current-surface no-go | `CLEAN`; AC/theta shared K-real physicalization pruning, no lepton source-strength theorem |
| `#4952` Qualification unfixed-choice clarification | closed without merge; adjacent law-level unfixed-choice support for coordinate-tag arguments only if equivalent retained authority exists, no positivity or source-strength readout theorem |
| `#4951` theta mass determinant-bridge retirement-readiness no-go | `CLEAN`; theta mass-side pruning, no lepton source-strength theorem |
| `#4950` additive-even premise relocation onto K/CPT bridge | `CLEAN`; theta-chain premise-edge repair, no lepton source-strength theorem |
| `#4949`, `#4948`, `#4947`, `#4946`, `#4945`, `#4944`, `#4943` current clean physics/runner surface | AC/theta/R-eta/runner hygiene, no charged-lepton source-positive-cone theorem |
| `#4902`, `#4905`, `#4906` Koide occupancy/slot/phase stack | Koide/electron readout context, no source-strength positive-cone closure |

Thus no open PR currently closes the monotone source-strength semantic target.

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "positivity is derived for
the charged-lepton source" is **not** shipped. The narrowed claim is:

```text
If charged-lepton source strength is a real monotone finitely additive
source-strength measure over disjoint source-control blocks, then singleton
source strengths are nonnegative. Signed or complex source probes can still be
used as response probes, but they are not normalized source-strength weights.
```

Verdict tag: broad source-positive closure fails; narrowed positive-cone
domain discriminator support passes.

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| monotone finite-additive source strength | Treat source strength as a real ordered measure on disjoint source-control blocks. | SUPPORTED CONDITIONALLY. Monotonicity forces singleton nonnegativity. |
| raw signed action coefficients | Use signed `j_c` directly in the L1 section. | ATTEMPTED. Negative singleton weights or zero denominator can occur. |
| complex source amplitudes | Use complex probe amplitudes as source strengths. | ATTEMPTED. No real order or monotonicity is available. |
| absolute-value route | Normalize `|j_c|`. | OPEN BUT DIFFERENT OBJECT. It is nonlinear and must be licensed separately. |
| squared-amplitude route | Normalize `|j_c|^2`. | OPEN BUT DIFFERENT OBJECT. It is a probability/squared-amplitude weight, not the linear action coefficient. |
| positive/negative channel split | Split each signed coordinate into positive and negative channels. | OPEN BUT IMPORT-BEARING. It introduces a supplied sign tag or a 512-channel carrier. |
| label-free/unfixed-choice route | Use `#4952` to block nonuniform coordinate tags. | PARTIAL. It helps label-freeness, not positivity. |
| primitive/realized-state shortcut | Appeal to approved primitives or realized-state evaluation. | RULED OUT AS ZERO-IMPORT CLOSURE. The registry supplies no source/action, weighting, normalization, source-strength order, readout bridge, or value. |

### N2 - Wall-Independence Audit

The old positivity wall is collapsed into a sharper source-strength semantics
wall:

| wall | content |
|---|---|
| P1 | charged-lepton source strength is a real monotone finite-additive object |
| P2 | source strength is physically projectivized and read through the L1 section |
| P3 | tensor-frame invariance forces the uniform source ray |
| P4 | charged-lepton `S_l` reads the normalized singleton source-strength weight |
| P5 | A3 places or replaces the exact `256` precision correction |

| pair | closes automatically? | conclusion |
|---|---|
| P1 -> positivity | yes | singleton nonnegativity follows from monotonicity |
| P1 with P2-P5 | no | positivity does not choose projective section, uniformity, `S_l`, or precision |
| P2 with P3-P5 | no | L1 section does not force the uniform ray or identify `S_l` |
| P3 with P4-P5 | no | uniformity does not identify the charged-lepton scale symbol or precision |
| P4 with P5 | no | exact `S_l` identity does not derive A3 |

The note therefore reduces one sub-wall, but it does not close the compressed
source-probe interface.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `source strength` | explicit P1 semantic target, not background |
| `monotone` / `ordered` | explicit P1 hypothesis |
| `signed probes` | response-probe allowance, explicitly separated from source-strength readout |
| `complex` | explicit firewall, not silently ruled out for all response theory |
| `projective` / `L1 section` | explicit P2 residual |
| `S_l reads` | explicit P4 residual |
| `primitive` / `approved` / `registry` | registry-limited content only |

No positivity, projectivization, uniformity, `S_l` identity, A3 correction, or
mass value is hidden as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| source-strength normalization gauge firewall | raw control/coupling scale split and open positivity/section semantics | motivation for separating probes from strengths | yes |
| projective-simplex section support | L1 section after positive source ray is supplied | downstream P2 | yes |
| source-strength additivity selector support | nonnegative finite-additive source strength gives `1/256` after total strength and transitivity | P1/P3 downstream | yes |
| source-control linearity support | algebraic additivity of raw probes | contrast with ordered source strength | yes, but not positivity |
| source-probe interface compression support | compressed C1 projective source-strength clause | P1/P2 interface subclause | yes |
| `#4952` unfixed-choice clarification | coordinate-tag law dependence | positivity | no; cited only as adjacent PR support |
| `#4955` gravity repair | gravity eikonal runner/audit repair | source-positive cone | no; cited only as open PR context |

Only matching source-strength residuals are counted as support.

### N5 - Rhetoric Audit

| phrase | tested resolution | result |
|---|---|---|
| "signed probes are not source strengths" | coefficient-vector/source-strength-measure resolution | tested by negative normalized singleton and zero denominator examples |
| "complex probes are not source strengths" | ordered-real-measure resolution | tested by absence of monotone order |
| "positivity follows from monotone source strength" | finite-set singleton resolution | tested by `empty subset {c}` |
| "positive/negative split changes the carrier" | channel-count resolution | tested as `256 -> 512` unless a sign tag is supplied |
| "primitives do not supply the positive cone" | approved primitive-registry resolution | checked; no claim about future owner-approved primitive updates |

No broad no-go against signed response probes is shipped.

### N6 - Partial-Closure Path Scan

Potential closure paths found:

| path | status | what it would close |
|---|---|---|
| derive monotone source-strength semantics from the source-coupled local-action convention | open theorem route | P1 |
| ratify "source strength" as the ordered positive object read by the compressed source-probe interface | open convention-retirement route | P1/P2 |
| prove `S_l = sigma([j])_c` for the charged-lepton scalar source | open semantic bridge | P4 |
| derive determinant/log-volume scalar directly | open bypass route | could bypass P1-P4 |
| use squared amplitudes with a separate bridge to linear action coefficients | open alternate-object route | would need a new bridge, not silent transfer |

No new axiom is declared required. The import-retirement route is to make the
source-strength semantics explicit and then audit it.

### N7 - Steelman

A skeptical reviewer could argue that this note proves very little because
"source strength" already means nonnegative by ordinary language; the real
question is whether the charged-lepton scalar slot is a source-strength
readout at all. That objection is fair. The note therefore does not claim C1
or `S_l` closure. Its value is to prevent a future route from mixing signed
response probes with normalized source weights and then silently reading a
negative or complex coefficient as a strength.

### N8 - Cross-Cycle Echo

Similar repo walls have closed only after the relevant semantic object was
named and bounded. The RN/Fisher source-unit theorem closed a source-unit
normalization only for its declared amplitude object, and it lands at `1/16`
on 256 channels. The projective-simplex section note supplies an L1 section
only after a positive projective source ray is supplied. The `#4938` supplied
context pattern also shows that context can be moved out of axiom content only
when the supplied object is explicitly named. The same mechanism could apply
here if the charged-lepton source-positive cone is ratified as part of the
source-probe interface.

Gate result: `PASS` for the narrowed positive-cone discriminator support and
`FAIL` for the broad source-positive closure claim.

## Non-Claims

- No derivation of `S_l = 1/256`.
- No derivation of the source-coupled local-action convention.
- No derivation that the charged-lepton scalar source is a full-cell
  slot-resolved source family.
- No derivation that raw source probes are nonnegative source strengths.
- No derivation that charged-lepton source strength is physically the
  projective ray `[j]`.
- No derivation that tensor-frame symmetry forces the uniform source ray.
- No derivation that `S_l` reads `sigma([j])_c`.
- No derivation of the `256.08` precision correction.
- No derivation of `m_e`, Koide readout, `alpha(0)`, or hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_source_positive_cone_discriminator.py
```

The verifier checks finite monotone additivity, signed and complex probe
counterexamples, positive/negative channel splitting, authority boundaries,
current open PR alignment, no-go discipline markers, and the non-claim guard.
