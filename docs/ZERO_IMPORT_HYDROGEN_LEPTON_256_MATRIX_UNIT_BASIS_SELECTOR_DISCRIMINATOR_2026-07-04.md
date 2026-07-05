# Zero-Import Hydrogen: Lepton `1/256` Matrix-Unit Basis-Selector Discriminator

**Date:** 2026-07-04
**Type:** partial-narrowing discriminator note
**Claim type:** meta / source-measure support
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_matrix_unit_basis_selector_discriminator.py`

## Scope

This note follows the A2 readout/source split:

- `ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md`
  separated projection/Born trace readout from algebra-basis coefficient
  density.
- `ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md`
  separated L1 algebra-coordinate density from L2 / Hilbert-Schmidt /
  Fisher-unit normalization.

The remaining A2 question is now more precise:

```text
A2 basis/covariance discriminator:
  fixed-basis matrix-unit coefficient density can give 1/256;
  full inner-automorphism covariance sends the same rank-one projection
  to the tracial/projection class 1/16.
```

Therefore the `1/256` route needs not only an L1 norm-domain theorem. It also
needs a **basis/source-frame selector**: a retained reason why the
charged-lepton scalar source is read in the tensor-product matrix-unit frame,
or an invariant determinant/volume theorem that bypasses fixed coordinates.

## Finite Algebra Setup

For the four OS0 slots, the candidate algebra is

```text
A = M_2(C)^tensor4 ~= M_16(C).
```

Write `n = 16`. Then:

```text
Hilbert-space dimension d_H = n = 16
complex algebra dimension dim_C(A) = n^2 = 256
```

In a chosen matrix-unit basis `{E_ij}`, a fixed-basis coefficient-density
functional can assign a uniform coordinate weight

```text
1 / n^2 = 1/256.
```

But the phrase "chosen matrix-unit basis" is load-bearing. A matrix-unit
coordinate is not invariant under arbitrary inner automorphism

```text
A -> U A U^dag.
```

## Exact Covariance Test

Let `E_00` be a rank-one projection in the chosen basis. In that basis:

```text
normalized trace:           Tr(E_00) / n = 1/16
fixed-basis coefficient avg: sum_ij (E_00)_ij / n^2 = 1/256
fixed-basis L1 mass:         sum_ij |(E_00)_ij| = 1
Hilbert-Schmidt norm:        sqrt(Tr(E_00^dag E_00)) = 1
```

Now conjugate by a unitary whose first column is the flat vector
`(1, ..., 1) / sqrt(n)`. The projection

```text
P_flat = U E_00 U^dag
```

has every matrix entry equal to `1/n = 1/16`. Therefore, in the original fixed
matrix-unit basis:

```text
normalized trace:           Tr(P_flat) / n = 1/16
fixed-basis coefficient avg: sum_ij (P_flat)_ij / n^2 = 1/16
fixed-basis L1 mass:         sum_ij |(P_flat)_ij| = 16
Hilbert-Schmidt norm:        sqrt(Tr(P_flat^dag P_flat)) = 1
```

The projection is the same inner-automorphism orbit. The invariant quantities
remain invariant. The fixed-basis L1/coefficient data change:

```text
1/256  ->  1/16
1      ->  16
```

Thus `1/256` is not a full-algebra covariance fact of `M_16(C)`. It is a
fixed-coordinate density fact.

## One-Slot Version

The same issue already appears in one `M_2(C)` slot. In a chosen basis,
`E_00` has fixed-basis coordinate average `1/4`. Under the Hadamard conjugate,
the flat projection has entries `1/2`, so the same fixed-basis average becomes
`1/2`. The full four-slot statement is just the product version:

```text
(1/4)^4 = 1/256
(1/2)^4 = 1/16
```

This confirms that the A2 wall is not only "L1 versus L2." It is also
"which coordinate frame is physically load-bearing?"

## Repo Authority Alignment

| source | relevant boundary |
|---|---|
| `MINIMAL_AXIOMS_2026-06-29.md` | Qubit supplies one-site `M_2(C)` and says no possibility is privileged. It also excludes source/action, physical-observable identification, basis selection, weighting, normalization, probability, and measurement bridges from axiom content. |
| `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md` | The unique tracial-state theorem is the full inner-automorphism invariant state on the one-qubit algebra; it is the projection/tracial direction, not a fixed matrix-unit L1 coefficient rule. |
| `PRE_RECORD_REFERENCE_STATE_MAXIMAL_SYMMETRY_OPEN_GATE_NOTE_2026-06-05.md` | "No preferred basis", max entropy, and traciality collapse to one maximal-symmetry premise; record-absence does not force that premise. This supports treating a preferred matrix-unit source frame as an explicit theorem target, not background. |
| `AXIOM_FIRST_LATTICE_NOETHER_ABSTRACT_BILINEAR_CONTINUITY_NARROW_THEOREM_NOTE_2026-06-06.md` | Supplies finite matrix-unit continuity and support-envelope identities. It does not choose a uniform coefficient measure over all matrix units. |
| `STAGGERED_DIRAC_LOCAL_DENSITY_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-17.md` | Supplies `rho_x = chibar_x chi_x -> a_x^dag a_x` as local number projection on the CAR surface. It does not identify the charged-lepton scalar source with a uniform off-diagonal matrix-unit density over `M_16(C)`. |
| `SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md` | Supplies RN/Fisher source-unit algebra under the sharp-record source premise. Its uniform source unit is the L2 class, not the fixed-basis L1 density class. |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md` | Names L1 algebra-coordinate density as the target class. This note adds that the coordinate frame itself is another explicit selector target. |

## Primitive Boundary

The primitive registry was checked. Approved nodes can be used, but they do not
choose the matrix-unit source frame:

| node | what it supplies | what it does not supply here |
|---|---|---|
| `minimal_axioms` | `Z^3`, one-site `M_2(C)`, admissibility, record additivity | a preferred matrix-unit basis for the charged-lepton scalar source, source/action bridge, normalization rule |
| `kinetic_isotropy_primitive` | OS0 kinetic-form isotropy and the fourth regulator slot | a charged-lepton source frame, basis selector, readout bridge, probability rule |
| `scale_reference_primitive` | one dimensionful ruler | dimensionless `S_l` or matrix-unit density |
| `realized_state_primitive` | pointwise realized-state evaluation | measure, weighting, source frame, normalization rule, or value |

## Open PR Alignment

Open PRs were checked on 2026-07-04 before writing this discriminator:

| PR | effect on this basis-selector discriminator |
|---|---|
| `#4922`, `#4924` Born/composite Gleason and graded-constraint interface | These support projection/frame-function normalization. At `M_16(C)`, that is the tracial/projection `1/16` class unless paired with a source-coordinate theorem. |
| `#4923` record scope semantics / arrow substrate | Supplies record-scope and arrow context, but no source/action measure, basis selector, or formation rule. |
| `#4927` record-comparability block02 | Supplies no clock, rate, formation rule, state selector, probability, or weight; no A2 basis selector. |
| `#4928` Tier-A block03 AC value face | Helps Koide bookkeeping by reclassifying the AC value face, but does not choose the charged-lepton `M_16(C)` matrix-unit source frame. |
| `#4929` Tier-A block04 species-bridge partial-retirement | Possible K3 import-retirement context if accepted, but no source-measure or matrix-unit basis closure for `S_l`. |
| `#4903` D4 kinetic pattern dichotomy | Potential A1 tensor-lift context, but its selector bit is separate from the A2 matrix-unit coordinate frame. |

## Lane Consequence

A2 now has one additional explicit sub-gate:

| sub-gate | closure target |
|---|---|
| A2.1 measure-domain selector | prove `S_l` is a source/coefficient measure, not a projection-event probability |
| A2.2 norm-domain selector | prove L1 density, not L2 / Hilbert-Schmidt / Fisher unit |
| A2.3 basis/source-frame selector | prove the tensor-product matrix-unit frame is physically the charged-lepton scalar source frame, or replace it with an invariant determinant/volume theorem |
| A2.4 coefficient uniformity | prove uniformity over the selected `16^2 = 256` algebra coordinates |
| A2.5 charged-lepton source bridge | identify that selected density with `S_l` |
| A2.6 precision interface | connect exact `256` to the A3 `256.082435...` correction or derive the noninteger divisor directly |

This is progress because it prevents a hidden basis import. The positive route
is still live: the tensor product `M_2(C)^tensor4` may become physical once a
charged-lepton source-frame theorem attaches those four slots to the scalar
source. Until then, the `1/256` coefficient is fixed-coordinate arithmetic, not
a retained charged-lepton suppression theorem.

The positive restricted follow-up
`ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md`
isolates what is already exact after such a frame is supplied: uniform L1
coordinate density over the 256 tensor labels is invariant under tensor-frame
relabelings and coordinate bijections. That support does not remove this
note's full `U(16)` covariance firewall or its physical source-frame selector.

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "matrix-unit density cannot
close A2" is **not** shipped. The narrowed claim is:

```text
The fixed-basis matrix-unit density gives 1/256, but it is not invariant under
full inner automorphism of M_16(C). A retained 1/256 route must therefore
supply a physical basis/source-frame selector or an invariant determinant/
volume theorem.
```

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| full inner-automorphism covariance | Treat the readout as invariant under all `A -> U A U^dag`. | ATTEMPTED. The invariant projection/tracial class gives `1/16`; fixed-basis coefficient density is not invariant. |
| fixed matrix-unit coordinate frame | Use the tensor-product matrix-unit basis and assign uniform coordinate density. | ATTEMPTED. Gives `1/256`, but the physical charged-lepton source-frame theorem is still missing. |
| Qubit/Lattice tensor-slot route | Use the axiom-supplied `M_2(C)` one-site presentation and OS0 slots to restrict the coordinate frame. | OPEN. The axioms supply algebraic presentation and OS0 geometry, but not the charged-lepton source/action bridge or observable identification. |
| abstract bilinear Noether route | Use matrix-unit continuity and support-envelope identities to ground matrix-unit coordinates. | ATTEMPTED. It grounds `E_pq` algebra and currents, not a uniform L1 density over all `E_ij` as `S_l`. |
| local CAR density route | Use `rho_x = chibar_x chi_x -> a_x^dag a_x` as a basis readout. | ATTEMPTED. It gives local number projections and U(1) generator identity, not the off-diagonal `M_16(C)` source-coordinate density. |
| determinant/log-volume route | Replace fixed coordinates by an invariant determinant or volume-density theorem. | OPEN. This could bypass the basis selector, but no charged-lepton theorem is supplied here. |
| restricted permutation/frame covariance | Restrict symmetry to matrix-unit relabelings preserving the tensor frame. | OPEN. This can preserve uniform coordinate density, but the physical restriction itself needs a retained source-frame theorem. |
| realized-state route | Let realized state select the basis/source frame. | RULED OUT AS ZERO-IMPORT CLOSURE. The realized-state primitive supplies pointwise evaluation only, no selector, measure, normalization rule, or value. |

### N2 - Wall-independence audit

The collapsed wall set is:

| wall | content |
|---|---|
| W1 | A1 carrier: the charged-lepton scalar source carries the four OS0 algebra slots |
| W2 | norm-domain selector: L1 density rather than L2/Fisher/HS unit |
| W3 | basis/source-frame selector: the tensor-product matrix-unit frame is physical for the source |
| W4 | coefficient uniformity over the selected 256 coordinates |
| W5 | charged-lepton sector/source identity for `S_l` |
| W6 | A3 precision correction from exact `256` to the comparator divisor |

Pairwise audit:

| pair | closes automatically? | conclusion |
|---|---|---|
| W1 <-> W2 | no in either direction | independent |
| W1 <-> W3 | no in either direction | independent |
| W1 <-> W4 | no in either direction | independent |
| W1 <-> W5 | no in either direction | independent |
| W1 <-> W6 | no in either direction | independent |
| W2 <-> W3 | no in either direction | independent |
| W2 <-> W4 | no in either direction | independent |
| W2 <-> W5 | no in either direction | independent |
| W2 <-> W6 | no in either direction | independent |
| W3 <-> W4 | no in either direction | independent |
| W3 <-> W5 | no in either direction | independent |
| W3 <-> W6 | no in either direction | independent |
| W4 <-> W5 | no in either direction | independent |
| W4 <-> W6 | no in either direction | independent |
| W5 <-> W6 | no in either direction | independent |

Selecting a basis does not select L1 norm or prove uniformity. Selecting L1
norm does not select the basis. Exact `256` still does not explain the
`256.082435...` precision residual.

### N3 - Hidden-wall scan

| phrase class | classification |
|---|---|
| `chosen basis` / `fixed basis` | explicit W3 selector wall, not background. |
| `canonical` | avoided as a proof word unless tied to cited tracial/CAR surfaces. |
| `source frame` | explicit theorem target. |
| `primitive` / `registered` | registry checked; primitives are used only within declared content. |
| `uniform` | explicit W4 wall, not assumed. |
| `natural` | not used as a load-bearing proof word. |

No hidden basis or source-frame selector is left buried as context.

### N4 - Residual matching

| cited surface | residual it attacks | match? |
|---|---|---|
| `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md` | full inner-automorphism invariant tracial state | yes for projection/tracial contrast |
| `PRE_RECORD_REFERENCE_STATE_MAXIMAL_SYMMETRY_OPEN_GATE_NOTE_2026-06-05.md` | no-preferred-basis/traciality classification | yes for basis-selector caution |
| `AXIOM_FIRST_LATTICE_NOETHER_ABSTRACT_BILINEAR_CONTINUITY_NARROW_THEOREM_NOTE_2026-06-06.md` | finite matrix-unit continuity/support envelope | partial: matrix-unit algebra, not source density |
| `STAGGERED_DIRAC_LOCAL_DENSITY_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-17.md` | local CAR number projection | partial: diagonal local density, not uniform `M_16(C)` source density |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md` | L1 versus L2 source-norm split | yes |
| `SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md` | RN/Fisher source unit | yes as L2 contrast |

No tracial or Noether witness is counted as a charged-lepton L1 basis theorem.

### N5 - Rhetoric audit

The note avoids saying "`1/256` is not derivable." The tested resolutions are:

| resolution | tested? | outcome |
|---|---|---|
| fixed matrix-unit basis in `M_16(C)` | yes | `E_00` coefficient average gives `1/256`. |
| unitary conjugate flat projection | yes | same orbit gives fixed-basis average `1/16`. |
| normalized trace / projection readout | yes | invariant value `1/16` before and after conjugation. |
| Hilbert-Schmidt norm | yes | invariant value `1` before and after conjugation. |
| restricted tensor-frame covariance | not closed | left open as a positive route. |
| determinant/log-volume invariant route | not closed | left open as a positive route. |
| physical charged-lepton source-frame theorem | not closed | named W3/A2.3. |

### N6 - Partial-closure path scan

Legitimate closure paths remain:

| path | what it could close |
|---|---|
| retained theorem identifying the lepton scalar source with the tensor-product matrix-unit frame | W3 and part of W5 |
| retained theorem restricting covariance from full inner automorphism to the physical source-frame symmetry group | W3 |
| determinant/log-volume theorem whose coefficient equals the L1 density without fixed coordinates | W2 through W5 |
| Schur carrier theorem deriving the charged-lepton source family and `/64` equivalent | parallel Route B and W5 |
| convention-retirement audit showing the existing lepton-scale notation already has matrix-unit source-density semantics | W2/W3/W5 without a new axiom |

These are not new axioms if derived or retired through audited convention work.
The artifact is a discriminator, not a no-go.

### N7 - Steelman

A hostile reviewer can argue that full `U(16)` covariance is the wrong standard
for a source/action coefficient. The tensor product `M_2(C)^tensor4` is not an
abstract matrix algebra floating without structure; it comes from four OS0
slots over the qubit-lattice presentation. A source coefficient can be a
coordinate in that physical tensor frame, just as lattice derivatives and CAR
number densities are coordinates in a supplied finite carrier. On that reading,
the Hadamard/flat conjugation test over-symmetrizes the problem and attacks a
symmetry the physical source never had. The rebuttal is narrow: this is a
plausible route, but the repo still needs the charged-lepton source-frame
theorem that says this tensor frame is physical for `S_l`.

### N8 - Cross-cycle echo

This mirrors the pre-record reference split: algebraic maximal symmetry gives
a tracial object, while a less symmetric record/source frame needs an explicit
premise or theorem. It also mirrors the Koide form/weight split: finite
structure alone does not choose the measure. Some similar walls later moved by
showing that an already-present carrier supplied the required frame. This note
preserves that path and names the exact target.

**Gate result:** broad no-go fails; narrowed matrix-unit basis-selector
discriminator passes.

## Explicit Non-Claims

- No derivation of `S_l = 1/256`.
- No derivation that the charged-lepton scalar source uses the fixed
  tensor-product matrix-unit frame.
- No derivation of uniform L1 density over the 256 algebra coordinates.
- No derivation of the charged-lepton tensor lift.
- No derivation of a determinant, Schur, or volume-density theorem.
- No derivation of the `256.08` precision correction.
- No derivation of `m_e`, `alpha(0)`, or hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_matrix_unit_basis_selector_discriminator.py
```

The verifier checks the exact covariance arithmetic, source-authority
boundaries, primitive-registry boundaries, open-PR alignment, no-go discipline,
and explicit non-claims.
