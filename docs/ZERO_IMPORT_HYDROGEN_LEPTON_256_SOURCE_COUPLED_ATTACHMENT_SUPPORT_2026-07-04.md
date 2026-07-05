# Zero-Import Hydrogen: Lepton `1/256` Source-Coupled Attachment Support

**Date:** 2026-07-04
**Type:** partial positive support note
**Claim type:** conditional source-action support
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_source_coupled_attachment_support.py`

## Scope

This note follows the A1 full-cell and D17 separability support:

- `ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md`
  proves that a supplied full OS0-cell linear source has carrier
  `M_2(C)^tensor4` with `256` matrix-unit coordinates.
- `ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md`
  proves that, if that carrier is supplied as a scalar source multiplier on
  the D17 charged-lepton block, the D17 `1/sqrt(2)` normalization separates
  from the `256` source weights.

The remaining A1 attachment question is narrower:

```text
If the source-coupled local-action convention is adopted for a lepton-specific
full OS0-cell scalar source, does the local action attach the 256 source
directions as scalar multipliers on the D17 charged-lepton block?
```

The answer is yes, conditionally. Under that convention, source derivatives of
the action define local insertions, so a full-cell source field multiplying the
D17 block has exactly one action derivative per full-cell coordinate. This
does not prove the source-coupled local-action convention, does not prove that
the charged-lepton scalar source is full-cell, and does not identify the
coefficient with `S_l`.

## Conditional Theorem

Let the D17 charged-lepton block be the fixed scalar singlet

```text
B_lep = (1/sqrt(2)) sum_alpha bar L_L^alpha H_alpha e_R.
```

Let the supplied full OS0-cell carrier be

```text
A_cell = M_2(C)^tensor4
C = {0,1,2,3}^4
|C| = 256
O_c = E_{c_x} tensor E_{c_y} tensor E_{c_z} tensor E_{c_tau}.
```

Under the source-coupled local-action convention, a lepton-specific full-cell
scalar source has local action term

```text
S_lep[J] = h * B_lep * sum_{c in C} j_c O_c.
```

Then each source derivative is

```text
dS_lep/dj_c = h * B_lep * O_c.
```

Thus:

1. the D17 block is a fixed scalar multiplier;
2. the independent source directions are the `256` coordinates `c in C`;
3. the action derivative does not introduce `512` independent product weights;
4. if a later A2 theorem supplies uniform simplex weights
   `w_c = 1/256`, the separated action coefficient is
   `(1/sqrt(2))*(1/256)`.

This is the attachment half of the D17/full-cell separability result, now tied
to the source-coupled local-action convention.

## Why The Assumptions Are Load-Bearing

The theorem needs all of the following:

| supplied item | role |
|---|---|
| source-coupled local-action convention | turns action source derivatives into local operator insertions |
| charged-lepton D17 block | supplies `B_lep` and the `1/sqrt(2)` block normalization |
| lepton-specific full OS0-cell source | supplies the `M_2(C)^tensor4` source carrier rather than a generic regulator source |
| scalar multiplication of the D17 block | keeps the D17 vector fixed instead of adding product-vector components |
| A2 simplex/source-density theorem | needed later for `w_c = 1/256` |
| charged-lepton source bridge | needed later to call the coefficient `S_l` |

If the source-coupled convention is not adopted, this note becomes only a
formal action calculation. If the source is not full-cell, the derivative
directions are `16`, `4`, `1`, or `2` in the weaker shapes already separated by
the full-cell support note. If the source is attached as a product unit vector,
the coefficient class is still `(1/sqrt(2))*(1/16)`.

## What This Moves

| Before | After |
|---|---|
| The scalar-multiplier attachment in A1 was only listed as a hypothesis of the D17/full-cell separability support. | It is now conditionally supported by the source-coupled local-action derivative rule. |
| Source attachment could be confused with A2 source-density readout. | Attachment is action-derivative bookkeeping; A2 still chooses the measure/norm/readout class. |
| The source-coupled local-action note was only a route marker for A1. | It now has a precise lepton-facing consequence: `dS_lep/dj_c = h * B_lep * O_c`. |

The live A1 residual is therefore sharper:

```text
source-coupled local-action convention
  + lepton-specific full OS0-cell scalar source
  -> scalar-multiplier attachment to the D17 block
  -> D17-compatible 256-coordinate carrier.
```

This note supports only the final arrow after the first two inputs are
supplied.

## Authority Boundary

| source | supplies | does not supply |
|---|---|---|
| `OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md` | open-gate convention: local source derivatives of `S` define coupled local operator insertions; derivatives of `W = log Z` generate responses | retained derivation of source coupling or lepton-specific full-cell locality |
| `OBSERVABLE_PRINCIPLE_P1_BRIDGE_LOCALITY_OF_SOURCE_DERIVATIVES_NARROW_NOTE_2026-05-21.md` | warning that source-derivative locality at the scalar-generator level can relabel P1 | lepton full-cell source attachment |
| `LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10.md` | bounded charged-lepton scalar singlet and `1/sqrt(2)` normalization | source/action convention, full-cell carrier, mass value |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md` | conditional `M_2(C)^tensor4` carrier count from supplied full-cell source locality | physical proof of that source locality |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md` | compatibility of supplied scalar multiplier with D17 normalization and `256` weights | derivation of the source-coupled convention |
| `SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md` | RN/Fisher source-unit contrast, where a uniform 256-channel unit amplitude gives `1/16` | L1/simplex density or lepton `S_l` |
| approved primitives | minimal one-site algebra, OS0 kinetic-form isotropy, units/state discipline | source/action, selector, weighting, normalization, readout bridge, mass value |

The primitive registry was checked. Approved primitives are used only to their
declared content and are not treated as source/action authorities.

## Open PR Alignment

Open PRs were checked on 2026-07-04 before writing this support note. The
current open-review surface does not close this source-coupled attachment on
current main:

| PR | effect on this note |
|---|---|
| `#4922`, `#4924` Born/composite Gleason and graded-constraint interface | normalization/frame-function context; no lepton full-cell action-source attachment |
| `#4928`, `#4929` AC value/species-bridge movement | Koide bookkeeping; no `S_l` source action theorem |
| `#4930`, `#4931`, `#4932` R-eta and AC measure shortcut blocks | Koide K1/K2 hygiene; no lepton source-coupled attachment theorem |
| `#4933`, `#4934`, `#4935`, `#4936` theta mass/gauge/G3 stack | theta-only; `#4936` is unstable and blocks deriving the G3 phase-type `F cup F` insertion from current surfaces |
| `#4903` D4 kinetic pattern dichotomy | possible future tensor-lift context; no charged-lepton scalar source convention |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "source-coupled local
action closes A1 and derives `S_l`" is **not** shipped. The narrowed claim is:

```text
If the source-coupled local-action convention and a lepton-specific full-cell
scalar source are supplied, source derivatives attach the 256 full-cell
coordinates as scalar multipliers on the D17 charged-lepton block.
```

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| source-coupled action derivative | Use `S_lep[J] = h B_lep sum_c j_c O_c` and compute `dS_lep/dj_c`. | SUPPORTED CONDITIONALLY. It gives one D17-multiplied insertion per `c in C`. |
| W/log-det response route | Try to get attachment from `W = log Z` responses alone. | ATTEMPTED. It addresses connected responses after the source is named, not the local action attachment itself. |
| strict scalar-generator source-derivative locality | Treat locality of `dW/dj` as the source of attachment. | RULED OUT BY PRIOR for closure: the P1 locality note shows this relabels scalar-generator additivity at the relevant precision. |
| RN/Fisher source unit | Transfer the top source-unit route to 256 channels. | ATTEMPTED. It gives `1/16`, not the L1/simplex `1/256` density class. |
| D17-only route | Use only the charged-lepton scalar singlet. | ATTEMPTED. It supplies `1/sqrt(2)` but no full-cell source directions. |
| full-cell-only route | Use only the OS0 carrier. | ATTEMPTED. It supplies `256` directions but no charged-lepton scalar block. |
| direct product unit vector | Unit-normalize over `2 * 256` components. | ATTEMPTED. It gives `(1/sqrt(2))*(1/16)`, not the separated density class. |
| primitive/axiom shortcut | Appeal to minimal axioms or approved primitives. | RULED OUT AS CLOSURE. They do not supply source/action, weighting, normalization, readout, or mass value. |

### N2 - Wall-independence audit

The collapsed wall set after this support note is:

| wall | content |
|---|---|
| W1 | source-coupled local-action convention is adopted or derived |
| W2 | charged-lepton scalar source is a full OS0-cell source |
| W3 | physical tensor-product matrix-unit source frame is selected |
| W4 | A2 source-density semantics choose linear simplex/L1 density |
| W5 | selected coefficient is identified with charged-lepton `S_l` |
| W6 | precision correction from exact `256` to the comparator divisor is derived |

| pair | closes automatically? | conclusion |
|---|---|---|
| W1 with W2-W6 | no | source convention alone does not choose sector, frame, density, identity, or precision |
| W2 with W3-W6 | no | full-cell locality does not select frame, density, `S_l`, or correction |
| W3 with W4-W6 | no | frame selection does not choose norm/readout, sector identity, or correction |
| W4 with W5-W6 | no | simplex density does not identify the coefficient with `S_l` or fix precision |
| W5 with W6 | no | sector identity does not derive the noninteger correction |

The previous scalar-multiplier attachment wall is not counted separately once
W1 and W2 are supplied; this note supplies that conditional derivative
bookkeeping.

### N3 - Hidden-wall scan

| phrase class | classification |
|---|---|
| `source-coupled` / `local action` | explicit W1 convention gate, not retained closure |
| `lepton-specific` | explicit W2 sector/source hypothesis |
| `full-cell` | explicit W2 source-locality hypothesis |
| `scalar multiplier` | supported only after W1 and W2 |
| `uniform` / `1/256` | A2 hypothesis, not derived here |
| `primitive` / `approved` | registry-limited content only |

No source convention, sector selector, readout rule, or mass input is hidden as
background.

### N4 - Residual matching

| cited surface | residual it attacks | match? |
|---|---|---|
| source-coupled local-action candidate | source derivatives of `S` define local insertions | yes, as open-gate convention |
| D17 source note | charged-lepton scalar block and `1/sqrt(2)` normalization | yes |
| full-cell source-carrier support | `M_2(C)^tensor4` carrier count under supplied full-cell locality | yes |
| D17/full-cell separability support | scalar multiplier preserves D17 normalization and `256` source weights | yes |
| P1 source-derivative locality no-go | scalar-generator locality circularity | boundary only, not a witness for attachment |
| RN-cocycle source-measure theorem | RN/Fisher unit contrast | boundary only, not L1/simplex support |

Only the action-derivative attachment residual is counted as supported here.

### N5 - Rhetoric audit

The note avoids saying "`S_l` is derived," "A1 is closed," or "hydrogen is
retained." Tested resolutions are:

| resolution | tested? | outcome |
|---|---|---|
| D17 block multiplier | yes | derivative keeps fixed `B_lep`. |
| full-cell source directions | yes | `4^4 = 256` directions. |
| source derivative attachment | yes | `dS_lep/dj_c = h * B_lep * O_c`. |
| direct product unit normalization | yes | remains `(1/sqrt(2))*(1/16)`. |
| source-coupled convention as retained theorem | not closed | W1. |
| physical lepton full-cell source theorem | not closed | W2. |
| A2 source-density readout | not closed | W4. |
| mass/hydrogen consequence | not closed | W5-W6 plus alpha gates. |

### N6 - Partial-closure path scan

The legitimate partial-closure path is convention retirement, not a new axiom:
derive or explicitly adopt the source-coupled local-action convention, then
prove the charged-lepton scalar source is the full-cell source to which the
convention applies. If those land through the audit lane, the scalar-multiplier
attachment does not need to remain an independent wall. The approved primitives
do not supply this content silently.

### N7 - Steelman

A hostile reviewer can argue that this essentially closes A1: the framework
already has a local action tradition in the source-coupled note, D17 already
names the charged-lepton scalar block, and full-cell support already proves
the `256` carrier under full-cell locality, so `S_lep[J] = h B_lep sum_c j_c
O_c` is the natural lepton action term. The narrow reply is that "natural" is
not retained authority: the source-coupled convention remains an open gate,
and the lepton-specific full-cell source theorem is still not supplied.

### N8 - Cross-cycle echo

This follows the same repo pattern as the RN-cocycle and observable-principle
work: an algebraic identity can reduce a broad physical wall, but the semantic
source/action identification must stay explicit until audited. This note
therefore records a support theorem, not a retained source convention.

**Gate result:** broad A1/S_l closure fails; narrowed source-coupled
attachment support passes.

## Explicit Non-Claims

- No derivation of `S_l = 1/256`.
- No derivation of the source-coupled local-action convention.
- No derivation that the charged-lepton scalar source has full OS0-cell source
  locality.
- No derivation of physical tensor-product source-frame selection.
- No derivation of A2 source-density readout.
- No derivation of the `256.08` precision correction.
- No derivation of `m_e`, Koide readout, `alpha(0)`, or hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_source_coupled_attachment_support.py
```

The verifier checks the finite source-derivative attachment arithmetic, the
source-authority boundary, the primitive-registry boundary, the open PR
alignment, the no-go discipline section, and the explicit non-claims.
