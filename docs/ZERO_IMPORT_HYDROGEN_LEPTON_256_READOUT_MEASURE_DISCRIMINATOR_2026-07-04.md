# Zero-Import Hydrogen: Lepton `1/256` Readout-Measure Discriminator

**Date:** 2026-07-04
**Type:** partial-narrowing discriminator note
**Claim type:** meta / readout-boundary support
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_readout_measure_discriminator.py`

## Scope

This note sharpens A2 from the zero-import hydrogen lepton-scale lane:

```text
A2 | Readout rule: prove that the reciprocal-dimension readout from
     M_2(C)^tensor4 is the charged-lepton scale suppression S_l.
```

The prior reciprocal-readout firewall showed that a count `N=256` is
ambiguous: amplitude normalization gives `1/sqrt(N)=1/16`, while density
or volume reciprocal gives `1/N=1/256`. This note makes the ambiguity more
precise by separating projection/Born trace readout from algebra-basis
coefficient density.

## Finite Algebra

The OS0 four-slot repair points at the finite algebra

```text
A = M_2(C)^tensor4 ~= M_16(C).
```

There are two different dimensions in play:

```text
d_H       = 16                    Hilbert-space dimension of C^16
dim_C(A)  = d_H^2 = 256           complex algebra dimension
```

A rank-one projection in `M_16(C)` and a matrix-unit coordinate of
`M_16(C)` are therefore not the same readout object.

## Discriminator Table

| readout measure | readout object | exact value | D17-attached value | hydrogen-lane status |
|---|---|---:|---:|---|
| projection trace / Born frame | rank-one projection on `C^16` | `1/16` | `(1/sqrt(2))*(1/16)` | wrong for the target `S_l`; matches the unit-amplitude class |
| algebra-basis coefficient density | one matrix-unit coordinate among `16^2` coordinates | `1/256` | `(1/sqrt(2))*(1/256)` | matches the target value, but needs the physical source-measure theorem |
| unit-amplitude normalization over 256 modes | one equal-amplitude mode | `1/16` | `(1/sqrt(2))*(1/16)` | same numerical class as projection trace |
| D17-prime lepton block normalization | lepton scalar singlet block | `1/sqrt(2)` | `1/sqrt(2)` | already present; not the missing suppression |

Thus the next A2 question is not merely "Born or not Born." It is:

```text
prove that the charged-lepton scalar suppression is read in the
algebra-basis / coefficient-source measure, not as a projection event
on the Hilbert space.
```

## Repo Authority Alignment

This discriminator is consistent with existing repo boundaries:

| source | relevant boundary |
|---|---|
| `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md` | normalized trace on a full matrix algebra gives rank-one projection weight `1/n`; for `M_16(C)` that is `1/16`. |
| `FLAVOR_RECORD_READOUT_FORM_NOT_WEIGHT_2026-06-02.md` | Record supports additive/log form only after a readout surface is specified; it does not choose dimension weight, block count, Born weight, or normalization. |
| `scripts/flavor_einselection_2sector_modulo_kreality_2026_06_02.py` | genuine Born/tracial weighting and equal-power-per-block / Hilbert-Schmidt-style block counting are separated as different physical inputs. |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_RECIPROCAL_READOUT_FIREWALL_2026-07-04.md` | `1/sqrt(N)` and `1/N` were already distinct A2 possibilities. |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md` | the direct product with D17 gives the wrong unit-normalized class `(1/sqrt(2))*(1/16)` unless a reciprocal coefficient-density readout is supplied. |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md` | the source/action version of the same wall: L1 algebra-coordinate density gives `1/256`; L2 / Hilbert-Schmidt / Fisher-unit normalization gives `1/16`. |

## Primitive Boundary

The primitive registry was checked. The approved nodes can be used, but their
declared content does not select this measure:

| node | what it supplies | what it does not supply here |
|---|---|---|
| `minimal_axioms` | `Z^3`, one-site `M_2(C)`, admissibility, record additivity | coefficient-source measure, projection-to-source bridge, normalization rule, mass value |
| `kinetic_isotropy_primitive` | OS0 kinetic-form isotropy and the fourth regulator slot | readout bridge, probability rule, selector, mass ratio, empirical match |
| `scale_reference_primitive` | one dimensionful ruler | dimensionless physics or `S_l` |
| `realized_state_primitive` | pointwise realized-state evaluation | state content, measure, weighting, normalization rule, or value |

The discriminator therefore preserves the positive OS0 gain while keeping the
readout selection as an explicit A2 theorem target.

## Open PR Alignment

Open PRs were checked on 2026-07-04 before writing this discriminator:

| PR | effect on this discriminator |
|---|---|
| `#4922` Born form via composite Gleason | If merged, it supports a projection/frame-function route. At `M_16(C)` rank-one resolution, that route naturally gives `1/16`, not the algebra-basis `1/256` source measure by itself. |
| `#4924` graded-constraint interface | Repairs the conditioning-form interface for frame-function strength. It is useful for projection/Born normalization, but does not identify the charged-lepton scalar coefficient with a matrix-unit source density. |
| `#4928` Tier-A block03 AC value face | Reclassifies an AC value face as realized-state registered data, but leaves measure-side/dynamical occupancy, R-eta, and species bridge residuals. It does not select the lepton `1/256` source norm. |
| `#4923` record scope semantics / arrow substrate | Owner-approved record-scope and arrow-substrate context; no source/action measure or L1 density selector. |
| `#4927` record-comparability block02 | Adds comparability/no-go and conditional chain-arrow context. Its own boundary says it supplies no clock, rate, formation rule, state selector, probability, or weight, so it does not close A2. |
| `#4903` D4 kinetic pattern dichotomy | Potential future tensor-lift context; the selector bit remains undecided and it is not a readout-measure selector. |
| `#4902`, `#4905`, `#4906` Koide stack | Keep occupancy, slot, and phase-readout questions open; they support the form/weight caution but do not close the lepton-scale readout. |

## Lane Consequence

A2 now splits into sharper sub-gates:

| sub-gate | closure target |
|---|---|
| A2.1 measure-domain selector | prove `S_l` is a coefficient/source measure, not a projection-event probability |
| A2.2 norm-domain selector | prove the source measure is L1 algebra-coordinate density, not L2 / Hilbert-Schmidt / Fisher unit |
| A2.3 basis/source-frame selector | prove the tensor-product matrix-unit frame is physical for the charged-lepton scalar source, or replace it with an invariant determinant/volume theorem |
| A2.4 coefficient uniformity | prove the relevant source measure is uniform over the selected `16^2 = 256` algebra coordinates |
| A2.5 charged-lepton source bridge | identify that coefficient density with the charged-lepton scalar suppression |
| A2.6 precision interface | connect exact `256` to the separate A3 `256.082435...` correction or derive the noninteger divisor directly |

This is progress because it converts the vague readout wall into a concrete
discriminator: a projection/Born theorem alone is not enough unless it is
paired with a source-measure bridge that changes the readout object.

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "A2 cannot be derived" is
**not** shipped. The narrowed claim is:

```text
projection-trace / Born-frame readout alone gives the M_16(C) rank-one
scale 1/16, while algebra-basis coefficient density gives 1/256 but still
needs a physical charged-lepton source-measure theorem.
```

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| projection/Born trace | Read the `M_16(C)` event as a rank-one projection. | ATTEMPTED. Normalized trace gives `1/16`, not `1/256`. |
| algebra-basis coefficient density | Read one matrix-unit coordinate among `16^2` algebra coordinates. | ATTEMPTED. It gives `1/256`, but the charged-lepton source-measure bridge is still missing. |
| unit-amplitude vector over 256 modes | Normalize one equal-amplitude state over the 256 count. | ATTEMPTED. Gives `1/sqrt(256)=1/16`, the wrong class for `S_l`. |
| D17-prime scalar normalization | Use the lepton scalar singlet unit coefficient. | RULED OUT AS COMPLETE SUPPRESSION ROUTE. It gives `1/sqrt(2)` only. |
| determinant/log-volume route | Treat the charged-lepton scalar block as a determinant or volume-density object. | OPEN. It has the right shape for `1/N`, but no retained theorem is supplied here. |
| Schur `/64` route | Use lattice `g_2^2/64 = 1/256`. | OPEN parallel route; it still needs the charged-lepton Schur carrier and two-scale split. |
| Born composite Gleason route | Use #4922/#4924 frame-function strength. | OPEN/CONDITIONAL. It supports projection trace form, not the algebra-basis source measure by itself. |
| comparability route | Use #4927 record-chain comparability. | RULED OUT AS A2 CLOSURE. The PR boundary supplies no probability or weight. |

### N2 - Wall-independence audit

The collapsed wall set is:

| wall | content |
|---|---|
| W1 | measure-domain selector: projection event versus coefficient/source measure |
| W2 | uniformity over the `16^2 = 256` algebra coordinates |
| W3 | charged-lepton sector/source identity for `S_l` |
| W4 | precision correction from exact `256` to the A3 divisor |

Pairwise audit:

| pair | closes automatically? | conclusion |
|---|---|---|
| W1 <-> W2 | no in either direction | independent |
| W1 <-> W3 | no in either direction | independent |
| W1 <-> W4 | no in either direction | independent |
| W2 <-> W3 | no in either direction | independent |
| W2 <-> W4 | no in either direction | independent |
| W3 <-> W4 | no in either direction | independent |

Selecting coefficient space does not prove uniformity. Uniformity does not
prove the charged-lepton scalar uses that measure. Exact `256` still does not
explain `256.082435...`.

### N3 - Hidden-wall scan

| phrase class | classification |
|---|---|
| `projection trace` / `Born` | explicit readout domain; yields `1/16` at rank-one `M_16(C)` resolution. |
| `coefficient density` / `source measure` | explicit A2 wall, not assumed. |
| `natural` / `readout object` | descriptive only; the theorem target remains explicit. |
| `primitive` / `registered` | registry checked; primitives are used only within their declared content. |
| `uniform` | explicit A2.2 wall, not background. |

No hidden weighting or source-measure rule is left as background.

### N4 - Residual matching

| cited surface | residual it attacks | match? |
|---|---|---|
| `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md` | normalized-trace projection weights on matrix algebras | yes for the projection side only |
| `FLAVOR_RECORD_READOUT_FORM_NOT_WEIGHT_2026-06-02.md` | form/weight separation and block-count residual | yes as a measure-selection precedent |
| `scripts/flavor_einselection_2sector_modulo_kreality_2026_06_02.py` | Born/dimension weighting versus equal-power-per-block weighting | yes as a measure-domain precedent |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_RECIPROCAL_READOUT_FIREWALL_2026-07-04.md` | `1/sqrt(N)` versus `1/N` A2 ambiguity | yes |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md` | direct-product unit-normalization gives `(1/sqrt(2))*(1/16)` | yes as contrast |
| `#4922` / `#4924` | projection/frame-function Born bridge | partial: projection side only |
| `#4927` | comparability boundary with no probability/weight | guard only |

No projection-trace witness is counted as a coefficient-source theorem.

### N5 - Rhetoric audit

The note avoids saying "`1/256` is not derivable." The tested claim is at
specific resolutions:

| resolution | tested? | outcome |
|---|---|---|
| rank-one projection in `M_16(C)` | yes | normalized trace gives `1/16`. |
| algebra matrix-unit coordinate count | yes | uniform coefficient density gives `1/256`. |
| unit-amplitude normalization over 256 modes | yes | gives `1/16`. |
| D17-prime scalar block normalization | yes | gives `1/sqrt(2)`. |
| physical charged-lepton source-measure theorem | not closed | named as A2.1-A2.3. |
| determinant, Schur, or future source-action routes | not closed | left open. |

### N6 - Partial-closure path scan

Legitimate closure paths remain:

| path | what it could close |
|---|---|
| retained source/action theorem for the charged-lepton scalar coefficient | A2.1 and A2.3 |
| retained Hilbert-Schmidt or matrix-unit source-measure theorem | A2.1 and A2.2 |
| determinant/log-volume theorem for the lepton scalar block | A2.1 through A2.3 |
| charged-lepton Schur carrier and `/64` bridge | parallel Route B |
| convention-retirement audit showing the source coefficient already has matrix-unit density semantics | A2 without adding an axiom |

These are not new axioms if they are ordinary theorem work or explicit
import-retirement audits. The artifact is therefore a discriminator, not a
no-go.

### N7 - Steelman

A hostile reviewer can argue that a Yukawa coefficient is a source/action
coefficient, not a detector event probability. On that reading, projection
trace is the wrong comparison class from the start; the source coefficient
should live in operator-coordinate space, where the finite algebra has
`16^2 = 256` matrix-unit coordinates. The lepton-scale probe already names
`1/(dim_C M_2(C))^4`, which looks exactly like an algebra-dimension density,
not a Hilbert rank. This is the strongest positive route. The rebuttal is
that it is still a route: the repo needs the source/action or matrix-unit
measure theorem that makes this semantics physical for the charged-lepton
scalar coefficient.

### N8 - Cross-cycle echo

This echoes the Koide form/weight split: finite structure and additive form
were not enough until the measure choice was named. Some similar walls have
later moved by convention-retirement or by proving that the quantity already
had the relevant source semantics. The present note preserves that opening:
if a source-measure theorem lands, this discriminator tells exactly where it
plugs in.

**Gate result:** broad no-go fails; narrowed readout-measure discriminator
passes.

## Explicit Non-Claims

- No derivation of `S_l = 1/256`.
- No derivation that the charged-lepton scalar coefficient uses the
  algebra-basis source measure.
- No derivation of uniform coefficient density over the 256 matrix units.
- No derivation of the charged-lepton tensor lift.
- No derivation of a determinant, density, or volume readout theorem.
- No derivation of the `256.08` precision correction.
- No derivation of `m_e`, `alpha(0)`, or hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_readout_measure_discriminator.py
```

The verifier checks the projection-versus-coefficient arithmetic, the source
authority boundary, the primitive-registry boundary, the no-go discipline
section, the fresh open-PR alignment, and the explicit non-claims.
