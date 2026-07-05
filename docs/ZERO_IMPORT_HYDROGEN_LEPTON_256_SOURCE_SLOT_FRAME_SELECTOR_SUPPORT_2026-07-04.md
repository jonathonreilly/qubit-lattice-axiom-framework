# Zero-Import Hydrogen: Lepton `1/256` Source-Slot Frame Selector Support

**Date:** 2026-07-04
**Type:** partial positive support note
**Claim type:** conditional source-frame support
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_source_slot_frame_selector_support.py`

## Scope

This note follows three Lane 6 support/discriminator surfaces:

- `ZERO_IMPORT_HYDROGEN_LEPTON_256_MATRIX_UNIT_BASIS_SELECTOR_DISCRIMINATOR_2026-07-04.md`
  shows that fixed matrix-unit coordinate density is not invariant under full
  inner automorphism of `M_16(C)`.
- `ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md`
  shows that uniform `1/256` density is stable under relabelings of a supplied
  tensor-product matrix-unit source frame.
- `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md`
  shows that, once a lepton-specific full-cell source-coupled action is
  supplied, action derivatives attach the `256` source directions as scalar
  multipliers on the fixed D17 block.

The next subgate is A2.3:

```text
When does the tensor-product matrix-unit coordinate frame count as a physical
source frame rather than an arbitrary chosen basis of M_16(C)?
```

This note proves the conditional finite answer:

```text
If the charged-lepton scalar source family is supplied as independent
full-cell source knobs j_c coupled to tensor-product matrix units O_c, then
the source map itself selects the tensor-product matrix-unit frame relative to
that source family. Full U(16) conjugations are not symmetries of that fixed
source family unless they preserve the matrix-unit source set up to relabeling.
```

This does not derive the source family, the source-coupled convention, L1
semantics, coefficient uniformity, or `S_l`. It only says that, after the
source family is supplied in slot-resolved form, the matrix-unit frame is not
a hidden extra basis import for that source map.

## Conditional Theorem

Let

```text
A_cell = M_2(C)^tensor4 ~= M_16(C)
C = {0,1,2,3}^4
|C| = 256
O_c = E_{c_x} tensor E_{c_y} tensor E_{c_z} tensor E_{c_tau}.
```

Assume the charged-lepton scalar source family is a linear source map

```text
J : R^C -> A_cell
J(j) = sum_{c in C} j_c O_c.
```

In the source-coupled action notation of the previous support note,

```text
S_lep[J] = h * B_lep * J(j),
dS_lep/dj_c = h * B_lep * O_c.
```

Then the source-coordinate basis `{delta_c}` in `R^C` is part of the supplied
source family: changing `j_c` performs a specific external source intervention
coupled to `O_c`. A transformation preserves this source family as the same
kind of source family only if it carries source directions to source
directions:

```text
O_c -> O_{pi(c)}
```

for a bijection `pi` of `C`, with the tensor-frame subgroup

```text
S_4^4 semidirect S_4
```

as the slot-local relabeling group. Under those relabelings, the source family
is the same family with renamed controls.

By contrast, a generic inner automorphism

```text
O -> U O U^dag
```

does not preserve the matrix-unit source set. For example, the flat-unitary
conjugate of a rank-one matrix unit has every entry nonzero in the original
frame and is not any single tensor-product matrix unit. It is a linear
combination of many `O_c`. Therefore full `U(16)` covariance changes the
source-control family; it is not a relabeling symmetry of the fixed
slot-resolved source map.

Thus, conditional on the supplied source map `J(j) = sum_c j_c O_c`, the
tensor-product matrix-unit frame is physically selected relative to that
source family. The remaining question is whether the charged-lepton scalar
source is indeed supplied by such a slot-resolved full-cell source map.

## What This Moves

| Before | After |
|---|---|
| A2.3 only said a basis/source-frame selector was missing. | It now has a conditional closure shape: a slot-resolved source map selects its own tensor matrix-unit frame. |
| The full `U(16)` firewall could be misread as ruling out the tensor-frame route. | It only rules out treating fixed-coordinate density as full-algebra invariant. It does not rule out a physical source-family frame. |
| Restricted tensor-frame support assumed a supplied physical frame. | This note explains how that frame follows once the source controls themselves are supplied as independent matrix-unit knobs. |

The narrowed A2.3 target is now:

```text
charged-lepton scalar source
  -> slot-resolved full-cell source controls j_c
  -> tensor-product matrix-unit source frame
```

This note supports the second arrow only after the first arrow is supplied.

## Why The Assumptions Are Load-Bearing

The theorem depends on a supplied source family, not just on an abstract
algebra isomorphism `M_2(C)^tensor4 ~= M_16(C)`.

| supplied item | consequence |
|---|---|
| slot-resolved source controls `j_c` | matrix-unit frame is source-coordinate data |
| source-coupled local-action convention | `dS/dj_c` is a physical insertion direction |
| full-cell tensor product shape | coordinate set has `4^4 = 256` source directions |
| L1/simplex source-density semantics | needed later to assign `1/256` to each source direction |
| charged-lepton source bridge | needed later to identify the selected density with `S_l` |

Without slot-resolved source controls, the full `U(16)` covariance firewall
still applies. Without L1/simplex semantics, a uniform source unit gives
`1/16`, not `1/256`. Without the charged-lepton source bridge, the selected
source density is not yet the charged-lepton suppression.

## Authority Boundary

| source | supplies | does not supply |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_MATRIX_UNIT_BASIS_SELECTOR_DISCRIMINATOR_2026-07-04.md` | full `U(16)` covariance firewall for fixed-coordinate density | proof that the charged-lepton source has a physical tensor frame |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md` | invariance of uniform density under relabelings of a supplied tensor frame | selection of that frame |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md` | action-derivative attachment after a supplied source-coupled full-cell source | derivation of the source family |
| `AXIOM_FIRST_LATTICE_NOETHER_ABSTRACT_BILINEAR_CONTINUITY_NARROW_THEOREM_NOTE_2026-06-06.md` | exact finite matrix-unit algebra and support-envelope identities | uniform source-density measure or charged-lepton source selector |
| `STAGGERED_DIRAC_LOCAL_DENSITY_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-17.md` | local CAR number projection and U(1) density bridge | off-diagonal full-cell matrix-unit source density |
| `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md` | full inner-automorphism invariant tracial state | source-coordinate frame or L1 coefficient density |
| approved primitives | minimal one-site algebra, OS0 kinetic-form isotropy, units/state discipline | source/action, selector, weighting, normalization, readout bridge, mass value |

The primitive registry was checked. Approved primitives are not used beyond
their declared content.

## Open PR Alignment

Open PRs were checked on 2026-07-04 before writing this note. The current
open-review surface does not close this source-slot frame selector on current
main:

| PR | effect on this note |
|---|---|
| `#4922`, `#4924` Born/composite Gleason and graded-constraint interface | projection/frame-function context; no slot-resolved source family for `S_l` |
| `#4928`, `#4929`, `#4930`, `#4931`, `#4932` AC/Koide hygiene stack | helps K1/K2/K3 bookkeeping; no lepton source-slot frame theorem |
| `#4933`, `#4934`, `#4935`, `#4936`, `#4937` theta stack | theta-only; `#4937` blocks the G1 defect-closure gate on the current surface; no charged-lepton source-frame selector |
| `#4938` K/CPT supplied-context bridge | K/CPT orbit-constancy and determinant-character boundary repair for theta-chain/readout hygiene; no lepton source-slot frame or `S_l` theorem |
| `#4903` D4 kinetic pattern dichotomy | possible future A1 context; no A2 source-control theorem |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "the tensor-product frame
is now derived for the charged-lepton source" is **not** shipped. The narrowed
claim is:

```text
If the charged-lepton scalar source family is supplied as independent
slot-resolved matrix-unit source controls, then that source family selects the
tensor-product matrix-unit frame relative to its own source map.
```

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| slot-resolved source map | Treat `j_c` as the physical source controls coupled to `O_c`. | SUPPORTED CONDITIONALLY. It selects the tensor matrix-unit frame relative to the source family. |
| full `U(16)` covariance | Demand invariance under arbitrary inner automorphism of `M_16(C)`. | ATTEMPTED. It changes fixed-coordinate density from `1/256` to `1/16`; not a symmetry of the fixed source family. |
| tensor-frame relabeling | Preserve the source family by renaming tensor-slot coordinates. | SUPPORTED. This is the restricted relabeling group already verified. |
| abstract matrix-unit Noether route | Use finite matrix-unit algebra and support envelopes. | ATTEMPTED. It supports the algebra of source directions, not the charged-lepton source selector. |
| local CAR density route | Use `rho_x = chibar_x chi_x` as a physical local density. | ATTEMPTED. It supplies local diagonal number projection, not full `M_16(C)` source-slot density. |
| determinant/log-volume route | Bypass source coordinates with an invariant volume theorem. | OPEN. It could replace A2.3, but no theorem is supplied here. |
| realized-state route | Let the realized state choose the source frame. | RULED OUT AS ZERO-IMPORT CLOSURE. The primitive supplies pointwise evaluation only, no selector. |
| primitive/axiom shortcut | Appeal to minimal axioms or approved primitives. | RULED OUT AS CLOSURE. They do not supply source/action, weighting, normalization, readout, or mass value. |

### N2 - Wall-Independence Audit

The collapsed wall set after this support note is:

| wall | content |
|---|---|
| W1 | source-coupled local-action convention is adopted or derived |
| W2 | charged-lepton scalar source is a full-cell slot-resolved source family |
| W3 | L1/simplex source-density semantics are selected |
| W4 | coefficient uniformity is applied inside the selected frame |
| W5 | selected density is identified with charged-lepton `S_l` |
| W6 | precision correction from exact `256` to the comparator divisor is derived |

| pair | closes automatically? | conclusion |
|---|---|---|
| W1 with W2-W6 | no | source convention alone does not choose source family, density, identity, or precision |
| W2 with W3-W6 | no | source-family frame does not choose L1 semantics, `S_l`, or precision |
| W3 with W4-W6 | partial only | L1 plus selected frame supports uniformity, but not `S_l` or precision |
| W4 with W5-W6 | no | uniformity does not identify the coefficient or fix the correction |
| W5 with W6 | no | charged-lepton identity does not derive the precision correction |

The prior A2.3 frame wall is narrowed: it is conditionally handled by W2, but
W2 itself remains a live source-family theorem target.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `supplied source family` | explicit W2 hypothesis |
| `source controls` / `source knobs` | explicit source-frame selector hypothesis |
| `preserves the source family` | finite source-map condition, not full algebra covariance |
| `physical frame` | conditional on W2, not retained closure |
| `L1` / `simplex` | W3, not supplied here |
| `primitive` / `approved` | registry-limited content only |

No source-family selector, norm-domain selector, or mass input is hidden as
background.

### N4 - Residual Matching

| cited surface | residual it attacks | match? |
|---|---|---|
| matrix-unit basis-selector discriminator | full `U(16)` firewall and need for frame selector | yes |
| restricted tensor-frame support | relabeling invariance after frame is supplied | yes |
| source-coupled attachment support | derivative attachment after source family is supplied | yes |
| abstract bilinear continuity theorem | matrix-unit algebra and support envelope | partial: algebra only, not source selector |
| local density bridge | local diagonal CAR density | partial: diagonal density, not full-cell source frame |
| pre-record tracial theorem | full inner-automorphism invariant contrast | yes as boundary |

Only the conditional source-map frame residual is counted as supported here.

### N5 - Rhetoric Audit

The note avoids saying "`S_l` is derived," "A2 is closed," or "hydrogen is
retained." Tested resolutions are:

| resolution | tested? | outcome |
|---|---|---|
| source-coordinate map `J(j)=sum_c j_c O_c` | yes | selects `{O_c}` relative to source controls. |
| tensor-frame relabelings | yes | preserve the source family by renaming controls. |
| full `U(16)` inner automorphism | yes by prior discriminator and verifier | generic rotations do not preserve fixed source knobs. |
| abstract `M_16(C)` without a source map | not claimed closed | still under full covariance firewall. |
| L1/source-density semantics | not closed | W3. |
| charged-lepton `S_l` bridge | not closed | W5. |

### N6 - Partial-Closure Path Scan

Legitimate closure paths remain:

| path | what it could close |
|---|---|
| retained theorem that the charged-lepton scalar source is slot-resolved over the full OS0 cell | W2 and A2.3 |
| retained theorem that source/action coefficients use L1 density semantics | W3 |
| retained theorem deriving local coordinate relabeling symmetry for that source | W4 support |
| determinant/log-volume theorem invariantly producing `1/256` | possible bypass of W2-W4 |
| charged-lepton source bridge identifying the selected density with `S_l` | W5 |

These are not called new axioms if derived or retired through audited
convention/source work.

### N7 - Steelman

A hostile reviewer can argue that this should be enough to retire A2.3: a
source is, by definition, a set of external controls, and the controls `j_c`
already label the matrix-unit source directions. Asking for full `U(16)`
covariance after the controls are fixed changes the experiment. The strongest
reply is scope: that argument is valid only once the charged-lepton scalar
source family is actually supplied in slot-resolved form; this note does not
derive that source family.

### N8 - Cross-Cycle Echo

This mirrors the repository's recurring distinction between algebraic
availability and physical readout. Matrix units can be exact finite algebra
without selecting a source measure; a source family can select a frame without
selecting L1 normalization; and a uniform coefficient can exist without being
`S_l`. The support theorem keeps those steps separate.

**Gate result:** broad A2/S_l closure fails; narrowed source-slot frame
selector support passes.

## Explicit Non-Claims

- No derivation of `S_l = 1/256`.
- No derivation of the source-coupled local-action convention.
- No derivation that the charged-lepton scalar source is a full-cell
  slot-resolved source family.
- No derivation of L1/simplex source-density semantics.
- No derivation of coefficient uniformity as a physical source theorem.
- No derivation of the charged-lepton source bridge.
- No derivation of the `256.08` precision correction.
- No derivation of `m_e`, Koide readout, `alpha(0)`, or hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_source_slot_frame_selector_support.py
```

The verifier checks finite source-map frame arithmetic, the full `U(16)`
contrast, authority boundaries, primitive-registry boundaries, no-go discipline
markers, and explicit non-claims.
