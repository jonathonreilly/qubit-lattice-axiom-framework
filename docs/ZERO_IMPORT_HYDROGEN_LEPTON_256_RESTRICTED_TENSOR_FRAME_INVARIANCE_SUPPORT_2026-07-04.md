# Zero-Import Hydrogen: Lepton `1/256` Restricted Tensor-Frame Invariance Support

**Date:** 2026-07-04
**Type:** partial positive support note
**Claim type:** conditional source-measure support
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_restricted_tensor_frame_invariance_support.py`

## Scope

This note follows the A2 basis/covariance discriminator:

- `ZERO_IMPORT_HYDROGEN_LEPTON_256_MATRIX_UNIT_BASIS_SELECTOR_DISCRIMINATOR_2026-07-04.md`
  shows that fixed matrix-unit coordinate density can display `1/256`, but
  it is not invariant under full inner automorphism of `M_16(C)`.
- `ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md`
  shows that the needed normalization class is L1 algebra-coordinate density,
  not L2 / Hilbert-Schmidt / Fisher-unit amplitude.

The positive question left open by those discriminators is narrower:

```text
If a physical charged-lepton tensor-product matrix-unit source frame is
supplied, is the uniform L1 coordinate density stable under the natural
relabelings of that frame?
```

The answer is yes. This does not choose the source frame, does not choose L1
source semantics, and does not identify the density with `S_l`. It only proves
that once those earlier selectors are supplied, the coefficient-uniformity
piece is exact finite-set arithmetic.

## Conditional Theorem

Assume a supplied physical tensor-product matrix-unit source frame

```text
F = { e_a1 tensor e_a2 tensor e_a3 tensor e_a4 : a_i in {0,1,2,3} }
```

for

```text
A = M_2(C)^tensor4 ~= M_16(C).
```

Let the coordinate set be

```text
C = {0,1,2,3}^4,
|C| = 4^4 = 256.
```

Define the uniform L1 coordinate density

```text
mu(c) = 1/256 for every c in C.
```

Then:

| property | result |
|---|---|
| normalization | `sum_c mu(c) = 1` |
| one-slot marginal | `sum_{c: c_i = a} mu(c) = 1/4` for each slot `i` and local coordinate `a` |
| product form | `mu(c) = (1/4)^4 = 1/256` |
| slot permutations | every `pi in S_4` has `pi_* mu = mu` |
| independent local relabelings | every `(sigma_1,...,sigma_4) in S_4^4` has `sigma_* mu = mu` |
| tensor-frame relabeling group | the wreath-product relabeling group `S_4^4 semidirect S_4` preserves `mu` |
| arbitrary coordinate bijection | every bijection `b: C -> C` has `b_* mu = mu` |

The proof is finite: the pushforward of a uniform probability density on a
finite set by a bijection is again the same uniform probability density.

## Exact Group Boundary

The tensor-frame relabeling group has size

```text
|S_4^4 semidirect S_4| = 24^5 = 7,962,624.
```

That is a large discrete relabeling symmetry of the supplied tensor coordinate
frame, but it is not full `U(16)` covariance. A full unitary conjugation can
mix matrix-unit coefficients instead of merely relabeling the 256 coordinate
names. The prior basis-selector discriminator gives the sharp contrast:

```text
E_00 fixed-coordinate average      = 1/256
flat conjugate fixed-coordinate avg = 1/16
normalized trace in both cases      = 1/16
```

Therefore this note supports restricted tensor-frame invariance only. It does
not contradict the full-algebra covariance firewall.

## What This Moves

This result narrows A2 but does not close it.

| sub-gate | standing after this note |
|---|---|
| A2.1 measure-domain selector | still open: source/coefficient measure must be selected over projection/Born probability |
| A2.2 norm-domain selector | still open: L1 density must be selected over L2 / Hilbert-Schmidt / Fisher unit |
| A2.3 basis/source-frame selector | still open: the tensor-product matrix-unit source frame must be physically supplied |
| A2.4 coefficient uniformity | conditionally supported: once A2.2 and A2.3 are supplied, uniformity is invariant under all tensor-frame relabelings and all coordinate bijections |
| A2.5 charged-lepton source bridge | still open: the selected density must be identified with charged-lepton `S_l` |
| A2.6 precision interface | still open: exact `256` must connect to `256.082435...` or be replaced by a direct noninteger divisor theorem |

The lane improvement is that A2.4 is no longer a continuous covariance
problem. The remaining issue is not whether uniform finite density survives
renaming of the supplied coordinates; it does. The remaining issue is whether
the framework supplies that coordinate source frame and L1 source semantics
without import.

## Repo Authority Alignment

| source | relevant boundary |
|---|---|
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_MATRIX_UNIT_BASIS_SELECTOR_DISCRIMINATOR_2026-07-04.md` | Establishes the full `U(16)` covariance firewall and names the basis/source-frame selector as A2.3. |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md` | Establishes that the target class is L1 algebra-coordinate density, not L2 / Hilbert-Schmidt / Fisher unit. |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md` | Separates matrix-unit coefficient density from projection/Born trace. |
| `MINIMAL_AXIOMS_2026-06-29.md` | Supplies one-site `M_2(C)` but does not privilege a possibility, choose a physical source frame, or define a source/action measure. |
| `KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` | Supplies OS0 kinetic-form isotropy and the fourth regulator slot, not a charged-lepton source-frame selector. |
| `REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` | Supplies pointwise realized-state evaluation only; no measure, weighting, normalization, selector, or value. |
| `SCALE_REFERENCE_PRIMITIVE_NOTE.md` | Supplies one dimensionful ruler only; it does not supply dimensionless `S_l`. |

## Primitive Boundary

The primitive registry was checked. Approved primitives can be used only to
their declared content:

| node | declared help | boundary here |
|---|---|---|
| `minimal_axioms` | `Z^3`, one-site `M_2(C)`, admissibility, record additivity | no preferred matrix-unit source frame, source/action bridge, weighting, or normalization |
| `kinetic_isotropy_primitive` | OS0 kinetic-form isotropy and fourth regulator slot | no charged-lepton source frame, readout bridge, probability rule, or value |
| `scale_reference_primitive` | one dimensionful ruler | no dimensionless suppression factor |
| `realized_state_primitive` | pointwise realized-state evaluation | no selector, measure, weighting, normalization rule, or mass value |

## Open PR Alignment

Open PRs were checked on 2026-07-04 before writing this support note:

| PR | effect on this restricted tensor-frame support |
|---|---|
| `#4922`, `#4924` Born/composite Gleason and graded-constraint interface | Helpful projection/frame-function context, but they support the projection/Born side rather than the matrix-unit L1 coordinate-density selector. |
| `#4923` record scope semantics / arrow substrate | Supplies record-scope and arrow-substrate context, but no source/action measure, frame selector, or L1 density semantics. |
| `#4927` record-comparability block02 | Supplies no clock, rate, formation rule, state selector, probability, or weight; no A2 closure. |
| `#4928` Tier-A block03 AC value face | Helps Koide bookkeeping by reclassifying the AC value face, but does not choose the charged-lepton tensor source frame. |
| `#4929` Tier-A block04 species-bridge partial-retirement | If accepted, it improves the Koide species-bridge decomposition; it is not an `S_l` source-frame theorem. |
| `#4930` Tier-A block05 R-eta route pruning | Prunes R-eta angle-native candidate classes and sharpens K2 to a licensed bridge target `Phi = S_sum = 2/3`; it does not close A2 or derive `S_l`. |
| `#4903` D4 kinetic pattern dichotomy | Potential A1 tensor-lift context, but its selector bit is separate from this A2 frame-relabeling support. |

## Lane Consequence

This note makes the next Lane 6 attack sharper:

```text
A2.4 uniformity inside a supplied tensor frame: conditionally exact.
A2.3 physical tensor-frame selector: still missing.
A2.2 L1 source semantics: still missing.
```

So the shortest zero-import hydrogen path remains Lane 6, but the work should
not spend another cycle proving that finite uniform density is stable under
coordinate relabeling. The remaining target is a retained reason why the
charged-lepton scalar source is actually evaluated in this tensor-product
matrix-unit frame with L1 source-density semantics.

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "restricted tensor-frame
uniformity closes A2" is **not** shipped. The narrowed claim is:

```text
Given a supplied physical tensor-product matrix-unit source frame and L1
density semantics, the uniform coefficient 1/256 is invariant under all
tensor-frame relabelings and all coordinate bijections. This does not choose
the frame, choose L1 semantics, identify S_l, or close hydrogen.
```

Verdict tag: broad no-go fails; restricted tensor-frame support passes.

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| slot permutations | Permute the four tensor slots. | SUPPORTED. Uniform `mu(c)=1/256` is unchanged. |
| independent local coordinate relabelings | Relabel the four one-slot matrix-unit coordinates independently in each slot. | SUPPORTED. Uniform `mu(c)=1/256` is unchanged. |
| tensor-frame wreath-product relabelings | Combine slot permutations and local relabelings. | SUPPORTED. The group `S_4^4 semidirect S_4` preserves the uniform density. |
| arbitrary coordinate bijection | Relabel all 256 coordinate names by any bijection. | SUPPORTED as finite density arithmetic, not as a claim of physical symmetry. |
| full `U(16)` covariance | Allow arbitrary unitary conjugation mixing matrix-unit coefficients. | RULED OUT AS CLOSURE by the prior basis-selector discriminator: fixed-coordinate average can move from `1/256` to `1/16`. |
| physical frame selector | Derive why the charged-lepton scalar source uses this tensor frame. | OPEN. This is A2.3. |
| L1 source semantics selector | Derive why the source uses L1 density rather than L2/Fisher/HS unit. | OPEN. This is A2.2. |
| determinant/log-volume route | Bypass fixed coordinates with an invariant volume theorem. | OPEN. This could replace the frame-selector route but is not supplied here. |
| realized-state route | Let realized-state evaluation select the frame or density. | RULED OUT AS ZERO-IMPORT CLOSURE. The primitive supplies evaluation only. |

### N2 - Wall-independence audit

The collapsed wall set is:

| wall | content |
|---|---|
| W1 | A1 carrier: the charged-lepton scalar source carries the four OS0 algebra slots |
| W2 | A2.1 measure-domain selector: source/coefficient measure over projection/Born probability |
| W3 | A2.2 norm-domain selector: L1 density over L2/Fisher/HS unit |
| W4 | A2.3 basis/source-frame selector: tensor-product matrix-unit frame is physical |
| W5 | A2.4 coefficient uniformity inside the selected frame |
| W6 | A2.5 charged-lepton sector/source identity for `S_l` |
| W7 | A2.6/A3 precision correction from exact `256` to the comparator divisor |

Pairwise audit:

| pair | closes automatically? | conclusion |
|---|---|---|
| W1 with W2-W7 | no | carrier does not choose measure, norm, frame, uniformity, sector identity, or precision |
| W2 with W3-W7 | no | measure-domain selection does not choose norm, frame, uniformity, sector identity, or precision |
| W3 with W4-W7 | no | L1 selection does not choose frame, sector identity, or precision; it supports W5 only after W4 is supplied |
| W4 with W5-W7 | partial only | frame selection plus uniform L1 definition supports W5, but not sector identity or precision |
| W5 with W6-W7 | no | uniformity does not identify the density with charged-lepton `S_l` or fix the `256.082435...` residual |
| W6 with W7 | no | sector identity does not derive the precision correction |

This note conditionally attacks W5 only. It leaves W1-W4, W6, and W7 as live
unless separate retained theorems supply them.

### N3 - Hidden-wall scan

| phrase class | classification |
|---|---|
| `supplied frame` | explicit assumption, not a derived result. |
| `uniform` | explicit coefficient-density definition, not a source selector. |
| `relabeling` | finite coordinate-name bijection, not full unitary covariance. |
| `L1 density` | explicit norm-domain target, not supplied by this note. |
| `physical charged-lepton` | named bridge target, not assumed as closed. |
| `primitive` | registry-limited content only. |

No source-frame, source-measure, or charged-lepton identity assumption is left
buried as background.

### N4 - Residual matching

| cited surface | residual it attacks | match to this note |
|---|---|---|
| matrix-unit basis-selector discriminator | full `U(16)` covariance firewall | yes as boundary |
| L1 source-norm discriminator | L1 versus L2/Fisher/HS normalization class | yes as prerequisite boundary |
| readout-measure discriminator | matrix-unit density versus projection/Born trace | yes as prerequisite boundary |
| minimal axioms | one-site `M_2(C)` and no privileged possibility | yes as primitive guard |
| kinetic-isotropy primitive | OS0 fourth regulator slot | partial A1 context, not A2 closure |
| Koide PRs `#4928`-`#4930` | K1/K2/K3 readout and species-bridge bookkeeping | no direct `S_l` closure |

Only the finite uniformity residual is counted as supported here.

### N5 - Rhetoric audit

The note avoids claiming A2 closure or saying "`S_l` is derived." Tested
resolutions are:

| resolution | tested? | outcome |
|---|---|---|
| uniform finite density over 256 labels | yes | exact `1/256`. |
| slot permutation invariance | yes | passes. |
| local coordinate relabeling invariance | yes | passes. |
| arbitrary coordinate-bijection invariance | yes | passes as finite arithmetic. |
| full `U(16)` invariance | yes by prior discriminator | fails for fixed-coordinate density. |
| physical frame selection | not closed | named A2.3. |
| L1 source semantics | not closed | named A2.2. |
| charged-lepton `S_l` identity | not closed | named A2.5. |

### N6 - Partial-closure path scan

Legitimate next closure paths remain:

| path | what it could close |
|---|---|
| retained theorem identifying the charged-lepton scalar source frame with the tensor-product matrix-unit frame | A2.3 |
| retained theorem that source/action coefficients use L1 density semantics | A2.2 |
| retained theorem deriving the four OS0 algebra slots on the scalar coefficient | A1 and the carrier side of A2.3 |
| determinant/log-volume theorem matching `1/256` invariantly | possible bypass of A2.3-A2.4 |
| charged-lepton source bridge identifying the selected density with `S_l` | A2.5 |
| direct noninteger divisor theorem or correction after exact `256` | A2.6/A3 |

This support note does not block any of those routes.

### N7 - Steelman

A strong positive reading is that once the framework writes the candidate as
`M_2(C)^tensor4`, the tensor product already supplies the source coordinate
frame, and a uniform coefficient density over the resulting 256 labels is the
least additional structure. Under that reading, this note shows the uniform
`1/256` coefficient is robust under all finite renamings of the supplied
labels.

The narrow rebuttal is that the minimal axioms explicitly do not privilege a
possibility or supply a source/action bridge, and the prior discriminator
shows full `U(16)` covariance does not preserve the fixed-coordinate value.
The source frame must therefore be retained as physical, not inferred from a
convenient notation.

### N8 - Cross-cycle echo

This artifact does not repeat the earlier false closure where `4^4 = 256`
was treated as enough. It changes the residual from "is uniformity stable?"
to "what retained theorem supplies the physical frame and L1 source
semantics?" That is a narrower and testable Lane 6 target.

## Non-Claims

- No derivation of `S_l = 1/256`.
- No derivation that the charged-lepton scalar source uses this tensor-product
  matrix-unit frame.
- No derivation that the source/action coefficient uses L1 density semantics.
- No derivation of the charged-lepton tensor lift.
- No derivation of the charged-lepton source bridge.
- No derivation of the `256.082435...` precision correction.
- No derivation of `m_e`, Koide readout, `alpha(0)`, or hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_restricted_tensor_frame_invariance_support.py
```

The verifier checks the finite-set invariance arithmetic, the `U(16)`
boundary contrast, the primitive boundaries, the no-go discipline markers, and
the non-claim boundary.
