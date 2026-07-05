# Zero-Import Hydrogen: Lepton `1/256` Source-Strength Additivity Selector Support

**Date:** 2026-07-04
**Type:** partial positive support note
**Claim type:** conditional source-action support
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_source_strength_additivity_selector_support.py`

## Scope

This note follows the current A2 source-normalization stack:

- `ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md`
  separates the needed `1/256` L1 density from the `1/16`
  L2/Hilbert-Schmidt/Fisher source-unit class.
- `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_TRANSFER_DISCRIMINATOR_2026-07-04.md`
  shows that direct transfer of the top/RN/Fisher source-unit precedent gives
  `1/sqrt(256) = 1/16`, while a linear action simplex density gives `1/256`.
- `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md`
  proves that, once simplex normalization and local coordinate relabeling
  symmetry are supplied, transitivity forces the unique coefficient `1/256`.
- `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md`
  narrows the frame-selector wall: a slot-resolved source family
  `J(j) = sum_c j_c O_c` selects its own tensor-product matrix-unit source
  frame.

The next selector question is:

```text
If the slot-resolved source controls are nonnegative linear action-strength
coordinates, and source strength is finitely additive under disjoint
source-control coarse graining, does the L1/simplex normalization follow?
```

The answer is yes as a conditional finite theorem. This source-strength
additivity selector support does not prove that the charged-lepton source
has additive source-strength semantics. It only proves that this semantics is
exactly the missing selector that turns the 256 source controls into the
`1/256` L1/simplex class rather than the `1/16` L2/RN/Fisher class.

## Conditional Theorem

Let

```text
C = {0,1,2,3}^4,
|C| = 256,
J(j) = sum_{c in C} j_c O_c.
```

Assume the supplied source controls carry a nonnegative source-strength
functional

```text
mu : P(C) -> R_{\ge 0}
```

with

```text
mu(empty) = 0,
mu(A union B) = mu(A) + mu(B)  for A cap B = empty,
mu(C) = 1.
```

Define singleton source weights

```text
w_c = mu({c}).
```

Finite additivity gives, for any finite coarse graining block `A subset C`,

```text
mu(A) = sum_{c in A} w_c.
```

If the supplied tensor-frame source family is invariant under the local
coordinate relabeling symmetry already isolated in the simplex-uniformity
note, the action on `C` is transitive. Therefore all singleton weights are
equal:

```text
w_c = w_*.
```

The normalized total source strength then gives

```text
1 = mu(C) = sum_{c in C} w_c = 256 w_*,
w_* = 1/256.
```

Thus finite additivity for linear action-strength coordinates is a selector
for the L1/simplex normalization class:

```text
source-strength additivity + total strength 1 + tensor-frame transitivity
  -> mu({c}) = 1/256.
```

This is stronger than merely saying "if simplex then `1/256`": the simplex
law is now tied to a source-action semantics, namely additivity of
source-strength under disjoint source-control coarse graining.

## L2/RN/Fisher Contrast

The primitive RN/Fisher source-unit class normalizes amplitudes by

```text
sum_c u_c^2 = 1.
```

For a uniform 256-channel source unit,

```text
u_c = 1/sqrt(256) = 1/16.
```

That is not a finitely additive linear action-strength measure on source
controls. For a block of `k` equal subcontrols:

| semantics | per-subcontrol coefficient | additive total over the block |
|---|---:|---:|
| L1/source-strength measure | `1/k` | `1` |
| L2/RN/Fisher unit amplitude | `1/sqrt(k)` | `sqrt(k)` |
| squared L2 amplitude | `1/k` | `1` |

The squared L2 amplitudes can be additive probabilities, but then the additive
object is `u_c^2`, not the linear action coefficient multiplying `O_c` in
`J(j) = sum_c j_c O_c`. The lepton `1/256` target needs the coefficient itself
to carry source-strength measure semantics. A source-unit amplitude over the
same 256 labels gives `1/16`.

## What This Moves

| sub-gate | standing after this note |
|---|---|
| A2.1 measure-domain selector | sharpened: the needed object is source-strength over action controls, not projection probability |
| A2.2 norm-domain selector | conditionally supported: finite additivity plus total strength selects L1/simplex, not L2/RN/Fisher amplitude |
| A2.3 basis/source-frame selector | still conditional on the slot-resolved source family supplied in the source-slot frame note |
| A2.4 coefficient uniformity | conditionally handled by transitivity once source-strength additivity and the physical tensor frame are supplied |
| A2.5 charged-lepton source bridge | still open: the selected source-strength weight must be identified with `S_l` |
| A2.6 precision interface | still open: exact `256` must connect to `256.082435...` or be replaced by a direct noninteger divisor theorem |

The narrowed theorem target is now:

```text
charged-lepton scalar source controls are nonnegative additive action-strength
coordinates over the slot-resolved full-cell tensor source family.
```

If that lands together with the already isolated frame and symmetry hypotheses,
the source-strength coefficient is no longer an independent numerical choice.

## Authority Boundary

| source | supplies | does not supply |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md` | `1/256` as L1 algebra-coordinate density; `1/16` as L2/Fisher unit contrast | physical source-strength additivity theorem |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_TRANSFER_DISCRIMINATOR_2026-07-04.md` | top/RN source-unit transfer lands at `1/16`; linear action simplex density lands at `1/256` | proof that the lepton scalar source uses simplex semantics |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md` | transitivity plus simplex normalization forces `1/256` | source-strength additivity or charged-lepton source identity |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md` | slot-resolved source controls select the tensor-product matrix-unit frame relative to `J(j)` | derivation of the slot-resolved source family or L1 semantics |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md` | action derivatives attach source directions once source-coupled local action is supplied | adoption or derivation of the source-coupled convention |
| `SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md` | RN-cocycle source-unit/Fisher normalization and `lambda = 1` source-unit class | L1 source-strength measure for lepton matrix-unit controls |
| approved primitives | minimal one-site algebra, OS0 kinetic-form isotropy, units/state discipline | source/action, selector, weighting, normalization, readout bridge, mass value |

The primitive registry was checked. Approved primitives are used only within
their declared content; no primitive supplies source-strength additivity,
source/action identification, weighting, normalization, or `S_l`.

## Open PR Alignment

Open PRs were checked on 2026-07-04 before writing this note and refreshed
after `#4939`, `#4940`, and `#4941` appeared. The current open-review surface
does not close the additive source-strength selector on current main:

| PR | effect on this source-strength additivity selector |
|---|---|
| `#4922`, `#4924` Born/composite Gleason and graded-constraint interface | projection/frame-function context; helpful for probability normalization, but not a linear source-strength coefficient theorem |
| `#4928`, `#4929`, `#4930`, `#4931`, `#4932` AC/Koide hygiene stack | sharpens K1/K2/K3 bookkeeping; no lepton source-strength additivity theorem |
| `#4933`, `#4934`, `#4935`, `#4936`, `#4937` theta stack | theta-only current-surface no-go/route-triage work; no charged-lepton source-strength law |
| `#4938` K/CPT orbit-constancy supplied-context bridge | K/CPT orbit-constancy and determinant-character boundary repair under supplied finite readout context; no lepton additive source-strength or `S_l` theorem |
| `#4939` AC(i) dynamical-index occupancy no-go | blocks retiring AC(i)'s measure-side occupancy binary from current index/determinant/trace-transfer surfaces; no lepton additive source-strength, source normalization, or `S_l` theorem |
| `#4940` rule achirality from minimality | theta gauge-side/admissibility achirality and law-achiral/state-free context; no lepton additive source-strength, source normalization, or `S_l` theorem |
| `#4941` AC(i) determinant-order/chiral L-R no-go | blocks a determinant-order and chiral L-R coupling shortcut for AC(i); no lepton additive source-strength, source normalization, or `S_l` theorem |
| `#4903` D4 kinetic pattern dichotomy | possible future A1 context; no A2 source-strength normalization selector |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "A2 is closed" is **not**
shipped. The narrowed claim is:

```text
If slot-resolved source controls carry a nonnegative finitely additive
linear action-strength measure of total strength 1, and the supplied tensor
source frame is transitive under local relabelings, then each source control
has strength mu({c}) = 1/256. This does not derive that physical
source-strength semantics or identify the coefficient with S_l.
```

Verdict tag: broad A2/S_l closure fails; narrowed source-strength additivity selector support passes.

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| finite additive source-strength measure | Treat disjoint source-control coarse graining as additive action strength. | SUPPORTED CONDITIONALLY. With total strength `1` and transitivity it gives `mu({c}) = 1/256`. |
| local coordinate relabeling symmetry | Use the prior `S_4^4` transitivity result to force equal singleton weights. | SUPPORTED by the simplex-uniformity note once the physical frame and source semantics are supplied. |
| L2/RN/Fisher primitive source unit | Normalize source amplitudes by `sum_c u_c^2 = 1`. | ATTEMPTED. Uniform 256-channel coefficient is `1/sqrt(256) = 1/16`, not additive linear strength `1/256`. |
| squared L2 amplitudes | Treat `u_c^2` as the additive object. | ATTEMPTED. It gives `1/256` as a probability/squared-amplitude weight, not as the linear action coefficient multiplying `O_c`. |
| projection/Born trace | Use rank-one projection trace on `M_16(C)`. | RULED OUT AS COMPLETE `S_l` ROUTE by the readout discriminator: it gives `1/16`. |
| source-slot frame selector | Let slot-resolved controls select the matrix-unit frame. | PARTIAL. It handles the frame only after the source family is supplied; it does not choose additive strength. |
| determinant/log-volume route | Bypass source-coordinate additivity with an invariant volume theorem. | OPEN. It could replace this route, but no charged-lepton theorem is supplied here. |
| primitive/realized-state shortcut | Appeal to approved primitives or pointwise realized-state evaluation. | RULED OUT AS ZERO-IMPORT CLOSURE. The registry supplies no source/action, measure, weighting, normalization, or value. |

### N2 - Wall-Independence Audit

The collapsed wall set after this support note is:

| wall | content |
|---|---|
| W1 | source-coupled local-action convention is adopted or derived |
| W2 | charged-lepton scalar source is a full-cell slot-resolved source family |
| W3 | source controls carry nonnegative finite-additive action-strength semantics |
| W4 | tensor-frame local relabeling symmetry is physical for those source strengths |
| W5 | selected source-strength weight is identified with charged-lepton `S_l` |
| W6 | precision correction from exact `256` to the comparator divisor is derived |

| pair | closes automatically? | conclusion |
|---|---|---|
| W1 with W2-W6 | no | source convention alone does not supply source family, additivity, symmetry, identity, or precision |
| W2 with W3-W6 | no | source-family frame does not choose additive strength, `S_l`, or precision |
| W3 with W4-W6 | no | finite additivity does not prove physical relabeling symmetry, `S_l`, or precision |
| W4 with W5-W6 | no | uniformity does not identify the coefficient or fix the correction |
| W5 with W6 | no | charged-lepton identity does not derive the precision correction |

This note conditionally supports W3. It does not collapse W1, W2, W4, W5, or
W6.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `source controls` / `slot-resolved` | explicit W2 hypothesis from the source-slot frame note |
| `nonnegative` | explicit W3 hypothesis, not derived |
| `additive` / `coarse graining` | explicit W3 hypothesis, not derived |
| `normalized` / `mu(C) = 1` | explicit total-strength hypothesis, not background |
| `uniform` / `transitive` | explicit W4 condition supplied by the prior finite relabeling support note |
| `primitive` / `approved` | registry-limited content only; primitives are not used as source-strength selectors |

No source-action, additivity, normalization, relabeling, sector-identity, or
mass-value premise is left buried.

### N4 - Residual Matching

| cited surface | residual it attacks | match? |
|---|---|---|
| source-action simplex transfer discriminator | top/RN/Fisher source-unit transfer versus linear action simplex density | yes |
| L1 source-norm discriminator | `1/256` L1 density versus `1/16` L2/Fisher unit | yes |
| simplex-uniformity support | transitivity and simplex coefficient uniqueness | yes |
| source-slot frame selector support | tensor-product matrix-unit source frame after slot-resolved controls are supplied | yes as frame support, not source-strength closure |
| source-coupled attachment support | action derivative attachment after source-coupled convention is supplied | partial: action-source form only |
| RN-cocycle theorem | primitive source-unit/Fisher normalization | yes as contrast |
| approved primitive registry | minimal/primitive boundary | yes as exclusion of shortcut semantics |

Only the finite source-strength additivity selector residual is counted as
supported here.

### N5 - Rhetoric Audit

The note avoids saying "`1/256` is derived" or "A2 is closed." Tested
resolutions are:

| resolution | tested? | outcome |
|---|---|---|
| finite additive measure on 256 source controls | yes | singleton strength `1/256` under transitivity |
| disjoint source-control coarse graining | yes | `mu(A union B) = mu(A) + mu(B)` |
| one-slot marginal of the 256 source controls | yes | `64/256 = 1/4` |
| L2/RN/Fisher uniform source unit | yes | coefficient `1/16` |
| squared L2 amplitude | yes | additive only after changing the object from action coefficient to square/probability |
| physical charged-lepton additive source-strength theorem | not closed | named W3 |
| charged-lepton identity with `S_l` | not closed | named W5 |

### N6 - Partial-Closure Path Scan

Legitimate closure paths remain:

| path | what it could close |
|---|---|
| retained theorem that lepton scalar source controls are additive linear action-strength coordinates | W3 |
| convention-retirement audit showing existing source-coupled local-action semantics already carry finite source-strength additivity | W1-W3 without a new axiom |
| retained theorem deriving the slot-resolved source family and its relabeling symmetry together | W2-W4 |
| determinant/log-volume theorem matching `1/256` invariantly | possible bypass of W2-W4 |
| direct noninteger divisor theorem | A2/A3 combined if it bypasses exact `256` |

These are not new axioms if derived, convention-retired, or audited as already
native semantics. This artifact is a conditional support note, not a no-go.

### N7 - Steelman

A hostile reviewer can argue that additive source-strength semantics should
already be native to a source-coupled local action: source terms enter the
action linearly, external knobs superpose linearly, and disjoint source
controls should add exactly as coefficients in `J(j) = sum_c j_c O_c`.
The Record axiom also contains finite scalar additivity for disjoint records,
so finite additivity is not alien to the framework. On that reading, this note
nearly closes the norm-domain selector once the slot-resolved source frame is
accepted. The rebuttal is narrow: record additivity is readout additivity over
records, not source-strength additivity over lepton matrix-unit controls, and
the source-coupled local-action convention remains an open-gate convention
candidate until derived or audited as native.

### N8 - Cross-Cycle Echo

Prior source/action campaigns show the same pattern: a finite algebraic
normalization can be exact while the physical source semantics remain the
live gate. The `SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md`
retired part of the top source-unit wall only after identifying the RN/Fisher
source-unit semantics; it did not automatically transfer to L1 source-strength
semantics. The current lepton A2 notes likewise isolate arithmetic from
physical source identity. Open PR `#4938` is also a supplied-context bridge:
it repairs K/CPT boundary premises under supplied finite readout context, but
does not make supplied-context semantics free for unrelated lepton source
normalization. The same mechanism can help here only if a source-strength
context is explicitly supplied or retired by audit.

**Gate result:** broad A2/S_l closure fails; narrowed source-strength
additivity selector support passes.

## Explicit Non-Claims

- No derivation of `S_l = 1/256`.
- No derivation that the charged-lepton scalar source uses additive
  source-strength semantics.
- No derivation of the source-coupled local-action convention.
- No derivation that the charged-lepton scalar source is a full-cell
  slot-resolved source family.
- No derivation of tensor-frame relabeling symmetry as a physical source
  theorem.
- No derivation of the charged-lepton source bridge.
- No derivation of the `256.08` precision correction.
- No derivation of `m_e`, Koide readout, `alpha(0)`, or hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_source_strength_additivity_selector_support.py
```

The verifier checks finite additivity arithmetic, the L1/L2 contrast,
source-authority boundaries, primitive-registry boundaries, open PR context,
no-go discipline markers, and the explicit non-claim boundary.
