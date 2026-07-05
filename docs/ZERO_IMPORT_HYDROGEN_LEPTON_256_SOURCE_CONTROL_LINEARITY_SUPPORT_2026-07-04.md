# Zero-Import Hydrogen: Lepton `1/256` Source-Control Linearity Support

**Date:** 2026-07-04
**Type:** partial positive support note
**Claim type:** conditional source-action support
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_source_control_linearity_support.py`

## Scope

The previous source-strength note isolated the norm-domain selector:

```text
finite additive source strength + total strength 1 + tensor-frame transitivity
  -> mu({c}) = 1/256.
```

This note attacks the first source/action piece beneath that selector:

```text
Does the source-coupled local-action convention supply algebraic additivity of
disjoint source controls?
```

The conditional answer is yes. If the source-coupled local-action convention is
adopted and the charged-lepton scalar source is supplied as a slot-resolved
full-cell source family

```text
J(j) = sum_{c in C} j_c O_c,
C = {0,1,2,3}^4,
|C| = 256,
```

then source controls add linearly:

```text
J(j_A + j_B) = J(j_A) + J(j_B)
```

for disjointly supported source-control functions `j_A` and `j_B`.

This proves only the algebraic source-control linearity part. It does not
derive the source-coupled convention, the slot-resolved source family,
nonnegativity, total normalization `mu(C) = 1`, tensor-frame relabeling
symmetry, or the charged-lepton identification with `S_l`.

## Conditional Theorem

Assume the source-coupled local-action convention:

```text
local source derivatives of S define the local operator insertions coupled to
sources.
```

Assume also a lepton-specific full-cell scalar source coupled to the fixed D17
charged-lepton block:

```text
S_src[j] = h * B_lep * J(j),
J(j) = sum_{c in C} j_c O_c.
```

For two source-control functions `j_A` and `j_B` with disjoint supports,
linearity of `J` gives

```text
J(j_A + j_B)
  = sum_c (j_A,c + j_B,c) O_c
  = sum_c j_A,c O_c + sum_c j_B,c O_c
  = J(j_A) + J(j_B).
```

Therefore the source contribution to the local action is additive:

```text
S_src[j_A + j_B] = S_src[j_A] + S_src[j_B].
```

For indicator controls `1_A` and `1_B` of disjoint subsets `A,B subset C`,

```text
J(1_{A union B}) = J(1_A) + J(1_B).
```

Thus the source-coupled local-action convention, once supplied together with
the slot-resolved source family, supports finite source-control additivity
under disjoint source-control coarse graining.

## What This Does And Does Not Select

This note supplies a conditional bridge from source-coupled action linearity to
the additive part of the source-strength selector. It does not supply the
measure semantics needed to turn that linearity into the lepton coefficient.

| property | status after this note |
|---|---|
| source-control linearity | conditionally supported from `J(j) = sum_c j_c O_c` |
| disjoint coarse-graining additivity | conditionally supported for source controls |
| nonnegative source-strength semantics | still open |
| total strength `mu(C) = 1` | still open |
| local relabeling symmetry of source strengths | still open unless supplied by the tensor-frame source theorem |
| singleton coefficient `1/256` | follows only after source-strength semantics, normalization, and transitivity are also supplied |
| charged-lepton identity `S_l` | still open |

The key distinction is:

```text
linearity of source controls is vector-space structure;
source strength is a nonnegative normalized measure on those controls.
```

The former is supported here under the source-coupled local-action convention.
The latter remains the live A2 source-semantics gate.

## Record-Additivity Firewall

The Record axiom contains finite scalar readout additivity:

```text
for pairwise-disjoint records, scalar readout I is additive.
```

That is not the same statement as additive source strength over lepton
matrix-unit controls. Record additivity is about readable values of disjoint
records. It does not supply:

- a source/action bridge;
- a source-control family `J(j)`;
- nonnegative source-strength semantics;
- total normalization `mu(C) = 1`;
- tensor-frame relabeling symmetry;
- a charged-lepton `S_l` identity.

This note therefore does not transfer Record additivity to A2. The supported
route is narrower: if source-coupled local action is supplied, its linear
source map gives source-control additivity directly.

## Relation To The Existing A2 Stack

| surface | relation |
|---|---|
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md` | supplies the derivative attachment `dS_lep/dj_c = h * B_lep * O_c` after the source-coupled convention and lepton full-cell source are supplied |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md` | supplies the tensor-product matrix-unit frame after the slot-resolved source family is supplied |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_ADDITIVITY_SELECTOR_SUPPORT_2026-07-04.md` | shows that nonnegative finite-additive source strength plus total strength and transitivity gives `mu({c}) = 1/256` |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_TRANSFER_DISCRIMINATOR_2026-07-04.md` | blocks direct transfer of the top/RN/Fisher source-unit precedent, which gives `1/16` |
| `SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md` | supplies source-unit/Fisher normalization contrast, not L1 source-strength semantics |

This note reduces the source-strength residual by one step: additivity of the
source controls is no longer mysterious once the source-coupled convention and
slot-resolved source family are supplied. What remains is the physical decision
that the relevant coefficient is a nonnegative normalized source strength.

## Primitive Boundary

The primitive registry was checked. Approved primitives can be used only to
their declared content:

| node | declared help | boundary here |
|---|---|---|
| `minimal_axioms` | `Z^3`, one-site `M_2(C)`, admissibility, record formation, record readout additivity | no source/action bridge, source-control family, weighting, normalization, probability rule, or `S_l` |
| `kinetic_isotropy_primitive` | OS0 kinetic-form isotropy and the fourth regulator slot | no source-control theorem, selector, normalization, readout bridge, or value |
| `scale_reference_primitive` | one dimensionful ruler | no dimensionless source coefficient |
| `realized_state_primitive` | pointwise realized-state evaluation | no state-selection rule, measure, weighting, normalization, preferred state, or mass value |

## Open PR Alignment

Open PRs were checked on 2026-07-04 before writing this note and refreshed
after `#4940` and `#4941` appeared. The current open-review surface does not
close the source-control linearity lane on current main:

| PR | effect on this source-control linearity support |
|---|---|
| `#4922`, `#4924` Born/composite Gleason and graded-constraint interface | projection/frame-function context; no source-control linearity or source-strength selector |
| `#4928`, `#4929`, `#4930`, `#4931`, `#4932` AC/Koide hygiene stack | K1/K2/K3 bookkeeping; no lepton source-control theorem |
| `#4933`, `#4934`, `#4935`, `#4936`, `#4937` theta stack | theta-only current-surface no-go/route-triage work; no charged-lepton source-action convention |
| `#4938` K/CPT orbit-constancy supplied-context bridge | K/CPT boundary repair under supplied finite readout context; no lepton source-control linearity theorem |
| `#4939` AC(i) dynamical-index occupancy no-go | blocks retiring AC(i)'s measure-side occupancy binary from current index/determinant/trace-transfer surfaces; no lepton source-control linearity, source-strength normalization, or `S_l` theorem |
| `#4940` rule achirality from minimality | theta gauge-side/admissibility achirality and law-achiral/state-free context; no charged-lepton source-control linearity, source-strength normalization, or hydrogen input |
| `#4941` AC(i) determinant-order/chiral L-R no-go | blocks a determinant-order and chiral L-R coupling shortcut for AC(i); no lepton source-control linearity, source-strength normalization, or `S_l` theorem |
| `#4903` D4 kinetic pattern dichotomy | possible future A1 context; no A2 source-control theorem |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "source-coupled local
action derives the lepton source-strength measure" is **not** shipped. The
narrowed claim is:

```text
If the source-coupled local-action convention and the slot-resolved lepton
full-cell source family are supplied, then disjoint source controls add
linearly in the local action. This does not supply nonnegative normalized
source-strength semantics or identify the coefficient with S_l.
```

Verdict tag: broad A2/S_l closure fails; narrowed source-control linearity support passes.

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| source-coupled local-action linearity | Use `J(j) = sum_c j_c O_c` and compute `J(j_A+j_B)` for disjoint controls. | SUPPORTED CONDITIONALLY. It gives algebraic source-control additivity after the convention and source family are supplied. |
| source-derivative attachment | Use `dS_lep/dj_c = h * B_lep * O_c`. | PARTIAL. It gives one insertion per source direction, but not positivity or normalization. |
| Record readout additivity | Transfer finite scalar additivity of disjoint records to source controls. | ATTEMPTED. It is a readout statement about records, not a source/action measure over lepton matrix-unit controls. |
| source-strength additivity selector | Use nonnegative additive source strength plus total strength. | PARTIAL. Prior support gives `1/256` after those semantics are supplied; this note supports only the linear control-additivity subpiece. |
| RN/Fisher primitive source unit | Normalize source amplitudes by Fisher norm. | ATTEMPTED. Uniform 256-channel coefficient is `1/16`, not an L1 source-strength coefficient. |
| squared amplitude/probability route | Square the source-unit amplitudes to recover `1/256`. | ATTEMPTED. It changes the object from linear action coefficient to squared-amplitude/probability weight. |
| determinant/log-volume route | Bypass source-control linearity with invariant volume data. | OPEN. It could bypass this route, but no charged-lepton theorem is supplied here. |
| primitive/realized-state shortcut | Appeal to approved primitives or pointwise realized-state evaluation. | RULED OUT AS ZERO-IMPORT CLOSURE. The registry supplies no source/action, weighting, normalization, or value. |

### N2 - Wall-Independence Audit

The collapsed wall set after this support note is:

| wall | content |
|---|---|
| W1 | source-coupled local-action convention is adopted or derived |
| W2 | charged-lepton scalar source is a full-cell slot-resolved source family |
| W3 | source-control linearity applies to the lepton source map |
| W4 | controls carry nonnegative normalized source-strength semantics |
| W5 | tensor-frame local relabeling symmetry is physical for those source strengths |
| W6 | selected source-strength weight is identified with charged-lepton `S_l` |
| W7 | precision correction from exact `256` to the comparator divisor is derived |

| pair | closes automatically? | conclusion |
|---|---|---|
| W1 with W2-W7 | no | convention alone does not supply source family, normalization, symmetry, identity, or precision |
| W2 with W3-W7 | partial only | W1 plus W2 supports W3, but W2 alone does not |
| W3 with W4-W7 | no | linearity does not supply positivity, total strength, symmetry, `S_l`, or precision |
| W4 with W5-W7 | no | source-strength semantics does not prove physical relabeling symmetry, `S_l`, or precision |
| W5 with W6-W7 | no | uniformity does not identify the coefficient or fix the correction |
| W6 with W7 | no | charged-lepton identity does not derive the precision correction |

This note conditionally supports W3 after W1 and W2 are supplied. It leaves W1,
W2, W4, W5, W6, and W7 live.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `source-coupled local action` | explicit W1 convention gate |
| `slot-resolved` / `full-cell` | explicit W2 source-family hypothesis |
| `linear` / `additive` | theorem content for W3, not measure normalization |
| `source strength` | explicit W4 residual, not assumed |
| `Record additivity` | cited as a firewall; not transferred to source controls |
| `primitive` / `approved` | registry-limited content only |

No source convention, source family, positivity, normalization, symmetry,
sector identity, or mass value is hidden as background.

### N4 - Residual Matching

| cited surface | residual it attacks | match? |
|---|---|---|
| source-coupled local-action candidate | local source derivatives of `S` define insertions | yes as convention surface |
| source-coupled attachment support | derivative attachment for lepton full-cell source | yes |
| source-slot frame selector support | frame selected by slot-resolved source family | yes |
| source-strength additivity selector support | normalized additive source strength gives `1/256` | yes as downstream residual |
| minimal axioms / Record | readout additivity over disjoint records | no as source-control measure; firewall only |
| RN-cocycle theorem | Fisher/RN source-unit normalization | yes as L2 contrast |
| #4939 | AC(i) index/determinant/trace-transfer no-go | Koide guard only, not source-control support |

Only the source-control linearity residual is counted as supported here.

### N5 - Rhetoric Audit

The note avoids saying "source-strength semantics are derived," "`S_l` is
derived," or "hydrogen is retained." Tested resolutions are:

| resolution | tested? | outcome |
|---|---|---|
| source-control functions on 256 labels | yes | `J(j_A+j_B)=J(j_A)+J(j_B)` |
| disjoint subset indicators | yes | `J(1_{A union B})=J(1_A)+J(1_B)` |
| action source term | yes | `S_src[j_A+j_B]=S_src[j_A]+S_src[j_B]` for the source term |
| Record readout additivity | yes | not a source/action measure |
| nonnegative source-strength measure | not closed | W4 |
| total normalization `mu(C)=1` | not closed | W4 |
| charged-lepton identity with `S_l` | not closed | W6 |

### N6 - Partial-Closure Path Scan

Legitimate closure paths remain:

| path | what it could close |
|---|---|
| audit acceptance or derivation of the source-coupled local-action convention | W1 |
| retained theorem deriving the lepton full-cell slot-resolved source family | W2 |
| retained theorem that source-control coefficients are nonnegative normalized source strengths | W4 |
| convention-retirement audit showing the existing source-coupled semantics already include normalized source strength | W1-W4 without a new axiom |
| determinant/log-volume theorem matching `1/256` invariantly | possible bypass of W2-W5 |

These are not new axioms if derived, convention-retired, or audited as already
native semantics. This artifact is a conditional support note, not a no-go.

### N7 - Steelman

A hostile reviewer can argue that this note nearly retires the additivity
problem: the local action is literally linear in source controls, and the
source-strength note already proves that finite additivity plus normalization
gives `1/256`. If a source coefficient is an action-strength knob, positivity
and total strength one may be bookkeeping rather than physics. The rebuttal is
narrow: coefficient linearity is vector-space structure and allows arbitrary
sign and scale; the lepton coefficient needs a nonnegative normalized
source-strength measure and a sector identity with `S_l`, neither of which
follows from linearity alone.

### N8 - Cross-Cycle Echo

The observable-principle source-coupled local-action candidate already records
this pattern: moving from a global scalar-generator selection to local
source-coupled action can reduce a premise, but the source-coupling convention
itself remains an open gate until audited or derived. The top RN-cocycle source
work similarly shows that a clean source semantic can close a specific
normalization only after the semantic identification is accepted. The same
mechanism can apply here, but only after the lepton source-control semantics
are explicitly supplied or retired by audit.

**Gate result:** broad A2/S_l closure fails; narrowed source-control
linearity support passes.

## Explicit Non-Claims

- No derivation of `S_l = 1/256`.
- No derivation of the source-coupled local-action convention.
- No derivation that the charged-lepton scalar source is a full-cell
  slot-resolved source family.
- No derivation that source-control coefficients are nonnegative normalized
  source strengths.
- No derivation of total normalization `mu(C) = 1`.
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
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_source_control_linearity_support.py
```

The verifier checks finite source-control linearity, the record-additivity
firewall, the source-strength residual, primitive-registry boundaries, open PR
context, no-go discipline markers, and the explicit non-claim boundary.
