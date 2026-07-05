# Zero-Import Hydrogen: Lepton `1/256` D17 Full-Cell Separability Support

**Date:** 2026-07-04
**Type:** partial positive support note
**Claim type:** conditional source-carrier support
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_d17_full_cell_separability_support.py`

## Scope

This note follows the A1 full-cell source-carrier support:

- `ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md`
  proves that a supplied full OS0-cell linear source has carrier
  `M_2(C)^tensor4` with `256` matrix-unit coordinates.
- `ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md`
  keeps A1 separate from A2: direct unit normalization over
  `D17 x M_2(C)^tensor4` gives `(1/sqrt(2))*(1/16)`, not the target
  `(1/sqrt(2))*(1/256)`.

This note attacks the D17 compatibility part of A1:

```text
If a full-cell source carrier is supplied as a scalar source multiplier on the
stated D17 charged-lepton Yukawa block, does it preserve the D17 `1/sqrt(2)`
block normalization while leaving the `256` source coordinates separate?
```

The answer is yes. This is a conditional finite theorem. It does not prove
that the charged-lepton scalar source has full OS0-cell source locality, does
not promote the D17 source note, and does not identify the source coefficient
with `S_l`.

## Conditional Theorem

The D17 source note works inside the stated charged-lepton Yukawa-shaped block

```text
bar L_L^alpha H_alpha e_R,    alpha in {1,2}.
```

Within that stated block it gives the normalized scalar singlet

```text
H_unit^lep = (1/sqrt(2)) sum_alpha bar L_L^alpha H_alpha e_R
Z_lep^2 = N_c N_iso = 1 * 2 = 2.
```

Let a full OS0-cell source carrier be supplied independently:

```text
A_cell = M_2(C)^tensor4
C = {0,1,2,3}^4
|C| = 256.
```

If the carrier acts as a scalar source multiplier on the D17 block, the
separable lifted source has the form

```text
S_lift[J] =
  (1/sqrt(2)) sum_alpha (bar L_L^alpha H_alpha e_R)
  * sum_{c in C} w_c O_c.
```

The D17 vector is fixed and unit-normalized:

```text
sum_alpha |1/sqrt(2)|^2 = 1.
```

The source-carrier coefficients remain the `256` weights `w_c`. For the
uniform simplex candidate,

```text
w_c = 1/256,
coefficient(alpha,c) = (1/sqrt(2)) * (1/256).
```

So D17 compatibility does not force a unit vector over `512` product
components. It preserves the D17 `1/sqrt(2)` block anchor and leaves the
source-density/readout class to A2.

## What This Moves

| Before | After |
|---|---|
| T3 D17 compatibility was listed as a separate A1 requirement. | Conditionally supported: a full-cell scalar source multiplier preserves D17's `1/sqrt(2)` normalization. |
| The `D17 x M_2(C)^tensor4` product could be read as requiring unit normalization over `512` components. | That is only the direct-product unit-vector shortcut. A separable source multiplier has `256` source weights and a fixed D17 block vector. |
| T2 sector specificity was completely mixed with full-cell locality. | Inside the stated D17 charged-lepton block, the scalar contraction is unique; the remaining sector wall is the physical attachment of the supplied carrier to that block. |

## Load-Bearing Assumptions

The theorem needs all of the following supplied:

1. the D17 charged-lepton Yukawa-shaped block inputs;
2. a full OS0-cell source carrier `M_2(C)^tensor4`;
3. a scalar-multiplier attachment of that carrier to the D17 block;
4. A2 source-density semantics if the `w_c` are to become `1/256` rather than a
   primitive source-unit amplitude;
5. the later charged-lepton source bridge identifying the selected coefficient
   with `S_l`.

Without the scalar-multiplier attachment, several other shapes remain possible:

| shape | result |
|---|---|
| direct unit vector over `2 * 256` components | per-component coefficient `(1/sqrt(2))*(1/16)`, wrong readout class |
| arbitrary product weights `u_{alpha,c}` | `512` free weights, double-counts the D17 block instead of preserving it |
| SU(2)-triplet carrier insertion | outside the stated D17 charged-lepton scalar block unless a triplet absorber is supplied |
| D17 singlet without full-cell carrier | only the `1/sqrt(2)` block anchor; no `256` carrier |
| full-cell carrier without D17 block attachment | regulator/source algebra only; no charged-lepton scalar sector |

## Authority Boundary

| source | supplies | does not supply |
|---|---|---|
| `LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10.md` | bounded source-note theorem for the unique scalar singlet and `1/sqrt(2)` normalization inside the stated charged-lepton block | retained mass claim, full-cell carrier, source-density readout |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md` | conditional `M_2(C)^tensor4` carrier from full OS0-cell source locality | proof that the charged-lepton scalar source has that locality |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md` | conditional coefficient uniformity once linear simplex source semantics and physical frame are supplied | D17 block attachment or source convention |
| `OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md` | source-coupled local-action route marker | retained derivation of source coupling |
| approved primitives | one-site algebra, OS0 geometry, scale/reference/state discipline | source/action, selector, weighting, normalization, readout bridge, mass value |

The D17 source note is used only inside its declared bounded scope. This note
does not treat D17 as a retained electron-mass theorem.

## Remaining Residual

After this support theorem, the A1 residual is smaller:

```text
charged-lepton scalar source
  -> full OS0-cell source locality
  -> scalar-multiplier attachment to the D17 block
  -> D17-compatible M_2(C)^tensor4 carrier.
```

The second and third arrows are not proved here as physical facts. What is
proved is that, if they are supplied, they do not conflict with the D17
normalization and do not force the wrong `512`-unit normalization class.

## Open PR Alignment

Open PRs were checked on 2026-07-04. The current open-review surface does not
close this D17/full-cell separability theorem on current main:

| PR | effect on this note |
|---|---|
| `#4925` presentation-gauge axis-sign theorem | Orientation/gauge-section context; no D17/full-cell scalar source attachment. |
| `#4922`, `#4924` Born/composite Gleason and graded-constraint interface | Readout/normalization context; no D17 scalar-multiplier theorem. |
| `#4932` AC measure binary axiom shortcut block | Koide K1 hygiene; no D17/full-cell carrier attachment. |
| `#4934` theta gauge no-go | Theta hygiene; no direct lepton A1 movement. |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "D17 plus the full-cell
carrier closes A1" is **not** shipped. The narrowed claim is: D17 is compatible
with a supplied full-cell scalar source multiplier, and the D17 block
normalization separates from the `256` source-carrier weights.

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| separable scalar source multiplier | Attach `A_cell` as a scalar source multiplier on the D17 singlet. | SUPPORTED CONDITIONALLY. It preserves `1/sqrt(2)` and leaves `256` source weights. |
| direct unit vector over product components | Unit-normalize all `2 * 256` components. | ATTEMPTED. It gives `(1/sqrt(2))*(1/16)`, not the target density class. |
| arbitrary product weights | Let each `(alpha,c)` have an independent coefficient. | ATTEMPTED. It creates `512` free weights and does not preserve the D17 block anchor. |
| D17-only route | Use the scalar singlet without a full-cell carrier. | ATTEMPTED. It gives `1/sqrt(2)` but no `256` source carrier. |
| full-cell-only route | Use the OS0 carrier without the charged-lepton block. | ATTEMPTED. It gives `256` coordinates but no charged-lepton scalar attachment. |
| SU(2)-triplet route | Insert a triplet carrier into `bar L sigma H`. | RULED OUT INSIDE THE STATED D17 BLOCK unless an additional triplet absorber is supplied. |
| source-coupled local-action route | Use a local-action convention to justify scalar source attachment. | OPEN. It remains an open-gate convention candidate. |

### N2 - Wall-independence audit

| pair | closes automatically? | conclusion |
|---|---|---|
| D17 block uniqueness <-> full-cell source locality | no in either direction | independent |
| full-cell source locality <-> scalar-multiplier attachment | no in either direction | independent |
| scalar-multiplier attachment <-> A2 source-density readout | no in either direction | independent |
| D17 compatibility <-> charged-lepton source bridge `S_l` | no in either direction | independent |

This note supports D17 compatibility only after source locality and attachment
are supplied. It does not collapse A2 or the final `S_l` bridge.

### N3 - Hidden-wall scan

| phrase class | classification |
|---|---|
| `D17` | bounded source-note theorem inside stated charged-lepton block; not a retained mass claim. |
| `scalar multiplier` | explicit attachment wall. |
| `full-cell` | explicit source-locality wall inherited from the full-cell support note. |
| `source` / `local action` | explicit convention wall; candidate only. |
| `normalization` | D17 block normalization if `1/sqrt(2)`; A2 wall otherwise. |
| `primitive` / `approved` | primitive registry checked; no primitive is granted beyond declared content. |

No D17 status, source attachment, or readout premise is left as background.

### N4 - Residual matching

| cited surface | residual it attacks | match? |
|---|---|---|
| `LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10.md` | scalar singlet and `1/sqrt(2)` normalization inside the stated charged-lepton block | yes |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md` | finite full-cell carrier count under supplied source locality | yes |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md` | direct-product unit-normalization firewall and T3 compatibility wall | yes |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md` | downstream simplex coefficient uniformity | no as A1 closure; yes as later A2 compatibility |
| `OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md` | source-coupled local-action convention route | route marker only |

No cited surface is counted as proving physical charged-lepton full-cell source
locality or `S_l`.

### N5 - Rhetoric audit

The note avoids saying "D17 closes A1" or "`S_l` is derived." Tested
resolutions are:

| resolution | tested? | outcome |
|---|---|---|
| D17 weak-isospin block | yes | normalized vector has squared norm `1`. |
| full-cell source carrier | yes | `256` source coordinates. |
| separable D17 times source-density coefficient | yes | coefficient `(1/sqrt(2))*(1/256)`. |
| direct product unit normalization | yes | coefficient `(1/sqrt(2))*(1/16)`, wrong class. |
| physical source locality | not closed | named residual. |
| A2 source-density readout | not closed | downstream wall. |

### N6 - Partial-closure path scan

The primitive registry was checked. Approved primitives do not supply
source/action, selector, weighting, normalization, readout bridge, or mass
value. The partial-closure path remains the source-coupled local-action
candidate plus a lepton-specific full-cell source attachment theorem. This
note therefore does not say a new axiom is required.

### N7 - Steelman

A hostile reviewer can argue that this is enough for A1: D17 uniquely selects
the charged-lepton scalar block, full-cell support supplies `M_2(C)^tensor4`,
and source/action language already treats Yukawa terms as scalar sources, so
the separable product should be accepted as the lepton carrier. That is the
strongest positive reading. The reply is scope: source/action is explicitly
outside current axiom content, the source-coupled local-action note is still an
open gate, and this note proves compatibility of a supplied attachment, not the
physical attachment itself.

### N8 - Cross-cycle echo

This repeats the recurring separation between algebraic compatibility and
physical readout/attachment. D17 compatibility can be a clean finite theorem
while the source/action convention and sector attachment remain future
retirement work, just as earlier source-measure notes separated local algebra
from physical observable identification.

**Gate result:** broad T2/T3 closure fails; narrowed D17 full-cell
separability support passes.

## Explicit Non-Claims

- No derivation of `S_l = 1/256`.
- No derivation of A1 closure from D17.
- No derivation of charged-lepton full OS0-cell source locality.
- No derivation of the source-coupled local-action convention.
- No derivation of A2 source-density readout.
- No derivation of the `256.08` precision correction.
- No derivation of `m_e`, `alpha(0)`, or hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_d17_full_cell_separability_support.py
```

The verifier checks D17/source-carrier separability, direct-product
normalization counterexamples, authority boundaries, open-PR references, and
non-claim guards.
