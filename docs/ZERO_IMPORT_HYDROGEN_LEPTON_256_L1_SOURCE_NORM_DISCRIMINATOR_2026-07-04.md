# Zero-Import Hydrogen: Lepton `1/256` L1 Source-Norm Discriminator

**Date:** 2026-07-04
**Type:** partial-narrowing discriminator note
**Claim type:** meta / source-measure support
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_l1_source_norm_discriminator.py`

## Scope

This note follows
`ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md`.
That discriminator separated projection/Born trace readout from algebra-basis
coefficient density. This note sharpens the source/action side:

```text
A2 source-norm discriminator:
  L1 algebra-coordinate density over M_2(C)^tensor4 gives 1/256.
  L2 / Hilbert-Schmidt / Fisher-unit source normalization gives 1/16.
```

Therefore the `1/256` route is not merely "a source-measure theorem." It is
specifically an **L1 algebra-coordinate density** theorem, or an equivalent
determinant/volume theorem that has the same normalization class.

## Exact Norm Split

For one `M_2(C)` algebra slot:

```text
dim_C M_2(C) = 4.
```

Uniform algebra-coordinate **density** and uniform algebra-coordinate
**unit amplitude** differ:

| one-slot normalization | per-coordinate value |
|---|---:|
| L1 density over 4 algebra coordinates | `1/4` |
| L2 / Hilbert-Schmidt / Fisher unit over 4 coordinates | `1/sqrt(4) = 1/2` |

Across the four OS0 slots:

```text
N = 4^4 = 256.
```

The two classes become:

| four-slot class | value |
|---|---:|
| L1 algebra-coordinate density | `(1/4)^4 = 1/256` |
| L2 / Hilbert-Schmidt / Fisher unit amplitude | `(1/2)^4 = 1/16` |

Equivalently, in the product algebra

```text
A = M_2(C)^tensor4 ~= M_16(C),
dim_C(A) = 256,
```

a uniform L1 density vector has coefficient `1/256` and L2 norm `1/16`;
a uniform L2 unit vector has coefficient `1/16` and L1 mass `16`. These are
not the same source normalization.

## Transfer Check Against Existing Source-Measure Lanes

| route | transfer result for the lepton `1/256` target |
|---|---|
| RN-cocycle / P-cal source unit | The source-measure note fixes the primitive Fisher source unit. For a uniform `N`-component source, Fisher/L2 unit normalization gives `1/sqrt(N)`, hence `1/16` at `N=256`. It does not by itself select L1 density `1/256`. |
| source-action simplex transfer | `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_TRANSFER_DISCRIMINATOR_2026-07-04.md` checks the top/RN source-unit precedent directly. It gives `1/sqrt(256)=1/16` under primitive source-unit transfer, while a linear action simplex average gives `1/256`. The lepton route therefore needs a source-action density theorem, not just the top source-unit theorem. |
| source-action simplex uniformity | `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md` proves that a simplex-normalized linear action coefficient over the supplied tensor-frame coordinates is uniquely `1/256` if local coordinate relabeling symmetry is physical. It does not supply that physical symmetry or source-action theorem. |
| Hilbert-Schmidt matrix-unit source | A unit vector over the 256 matrix-unit coordinates again gives coefficient `1/16`. This is the same L2 class as the RN/Fisher source unit. |
| L1 algebra-coordinate density | Gives `1/256` exactly. This is the class the hydrogen lane needs, but the physical charged-lepton source-density theorem remains open. |
| matrix-unit basis/source frame | `ZERO_IMPORT_HYDROGEN_LEPTON_256_MATRIX_UNIT_BASIS_SELECTOR_DISCRIMINATOR_2026-07-04.md` shows that fixed-basis coefficient density is not full-inner-automorphism invariant: a unitary conjugate can move the fixed-basis average from `1/256` to `1/16`. The L1 route therefore also needs a basis/source-frame selector. |
| restricted tensor-frame relabeling | `ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md` proves that, once the physical tensor-product matrix-unit frame and L1 semantics are supplied, the uniform `1/256` density is invariant under tensor-frame relabelings and coordinate bijections. It does not supply the frame or L1 selector. |
| D4 fixed-density scale bridge | The hierarchy bridge proves a positive density-to-scale fourth-root map once a physical order parameter has been identified. It is not a per-matrix-unit charged-lepton source measure and does not transfer directly to `S_l`. |
| determinant / Schur source-family route | The DM Wilson Schur theorem gives exact determinant-response reduction once a charged microscopic block and support are supplied. It is a possible future shape, but it does not supply the lepton `M_16(C)` carrier, L1 source density, or sector identity here. |

## Primitive Boundary

The primitive registry was checked. Approved primitives can be used, but their
declared content does not choose L1 source density:

| node | what it supplies | what it does not supply here |
|---|---|---|
| `minimal_axioms` | `Z^3`, one-site `M_2(C)`, admissibility, record additivity | source/action bridge, weighting, normalization, probability, L1 density rule |
| `kinetic_isotropy_primitive` | OS0 kinetic-form isotropy and the fourth regulator slot | source-norm selector, readout bridge, probability rule, empirical match |
| `scale_reference_primitive` | one dimensionful ruler | dimensionless `S_l` |
| `realized_state_primitive` | pointwise realized-state evaluation | measure, weighting, normalization rule, or value |

## Open PR Alignment

Open PRs were checked on 2026-07-04 before writing this discriminator:

| PR | effect on this source-norm discriminator |
|---|---|
| `#4928` Tier-A block03 AC value face | Reclassifies AC(i)'s value face as realized-state registered data while keeping AC_phi_lambda alive. It does not derive or force `r=1/2`; surviving residuals include measure-side/dynamical occupancy realization, R-eta, and species bridge. It helps Koide bookkeeping, not the lepton `1/256` source norm. |
| `#4923` record scope semantics / arrow substrate | Owner-approved record-scope context and arrow substrate. It supplies no source/action measure, no global order among disconnected events, and no formation rule that would select L1 density. |
| `#4927` record-comparability block02 | Supplies no clock, rate, formation rule, state selector, probability, or weight; no A2 closure. |
| `#4922`, `#4924` Born/composite Gleason and graded-constraint interface | Projection/frame-function work supports the projection/Born side, which is the `1/16` class at `M_16(C)` rank-one resolution. |
| `#4903` D4 kinetic pattern dichotomy | Potential tensor-lift context, but not a source-norm selector. |

## Lane Consequence

A2 now has a sharper norm-domain target:

| sub-gate | refined target |
|---|---|
| A2.1 measure-domain selector | select algebra-coordinate source density, not projection-event probability |
| A2.2 norm-domain selector | select L1 density, not L2 / Hilbert-Schmidt / Fisher unit amplitude |
| A2.3 basis/source-frame selector | prove the tensor-product matrix-unit frame is the physical charged-lepton scalar source frame, or replace it with an invariant determinant/volume theorem |
| A2.4 coefficient uniformity | prove uniformity over the selected `4^4 = 256` algebra coordinates |
| A2.5 charged-lepton source bridge | identify that L1 density with the charged-lepton scalar suppression |
| A2.6 precision interface | connect exact `256` to the A3 `256.082435...` correction or derive the noninteger divisor directly |

This is progress because it prevents a false closure by the existing
source-measure P-cal/RN lane. That lane is valuable for primitive source-unit
normalization, but on a uniform 256-channel model it lands in the wrong
normalization class for `S_l`.

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "source-measure routes
cannot close A2" is **not** shipped. The narrowed claim is:

```text
RN/Fisher/Hilbert-Schmidt unit normalization alone gives the L2 class 1/16
on a uniform 256-channel source. The target 1/256 is the L1
algebra-coordinate density class and needs a separate physical theorem.
```

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| L1 algebra-coordinate density | Assign uniform density over the 256 matrix-unit coordinates. | ATTEMPTED. Gives `1/256`, but the physical charged-lepton source-density theorem is still missing. |
| L2 / Hilbert-Schmidt unit source | Normalize a uniform vector over the 256 matrix-unit coordinates. | ATTEMPTED. Gives coefficient `1/16`, not `1/256`. |
| RN-cocycle / P-cal Fisher unit | Transfer primitive Fisher source-unit normalization to a uniform 256-channel source. | ATTEMPTED. Fisher/L2 unit gives `1/sqrt(256)=1/16`; it does not supply L1 density. |
| projection/Born trace | Use rank-one projection trace on `M_16(C)`. | RULED OUT AS COMPLETE A2 ROUTE by the readout-measure discriminator: gives `1/16`. |
| determinant/log-volume route | Seek a determinant or volume-density theorem for the charged-lepton scalar source. | OPEN. This could produce the L1 class but is not supplied here. |
| hierarchy D4 density-scale bridge | Transfer the fixed positive D4 density-to-scale bridge. | ATTEMPTED. It proves a fourth-root scale map after an order parameter is identified, not a matrix-unit L1 source density for `S_l`. |
| Schur source-family route | Use local determinant-response/Schur reduction. | OPEN. Existing Schur support is conditional on supplied charged blocks and does not derive the lepton `M_16(C)` carrier or L1 norm. |
| realized-state route | Let the realized-state primitive provide the density. | RULED OUT AS ZERO-IMPORT ROUTE. The primitive supplies pointwise evaluation only, no measure, weighting, normalization rule, or value. |

### N2 - Wall-independence audit

The collapsed wall set is:

| wall | content |
|---|---|
| W1 | A1 carrier: the charged-lepton scalar source carries the four OS0 algebra slots |
| W2 | norm-domain selector: L1 density rather than L2/Fisher/HS unit |
| W3 | coordinate-basis and uniformity over the 256 algebra channels |
| W4 | charged-lepton sector/source identity for `S_l` |
| W5 | A3 precision correction from exact `256` to the comparator divisor |

Pairwise audit:

| pair | closes automatically? | conclusion |
|---|---|---|
| W1 <-> W2 | no in either direction | independent |
| W1 <-> W3 | no in either direction | independent |
| W1 <-> W4 | no in either direction | independent |
| W1 <-> W5 | no in either direction | independent |
| W2 <-> W3 | no in either direction | independent |
| W2 <-> W4 | no in either direction | independent |
| W2 <-> W5 | no in either direction | independent |
| W3 <-> W4 | no in either direction | independent |
| W3 <-> W5 | no in either direction | independent |
| W4 <-> W5 | no in either direction | independent |

Selecting L1 density does not prove the carrier, uniformity, sector identity,
or precision correction. Proving the carrier does not select a norm.

### N3 - Hidden-wall scan

| phrase class | classification |
|---|---|
| `source unit` / `Fisher unit` | explicit L2 normalization class, not used as L1 density. |
| `density` | explicit target wall, not assumed. |
| `uniform` | explicit coordinate-basis and coefficient wall. |
| `primitive` / `registered` | registry checked; primitives are used only within declared content. |
| `transfer` | tested route, not a proof of physical identity. |

No hidden L1 density rule is left as background.

### N4 - Residual matching

| cited surface | residual it attacks | match? |
|---|---|---|
| `SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md` | primitive source-unit / Fisher norm route | yes as L2 contrast |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md` | projection/Born trace versus matrix-unit coefficient density | yes |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md` | A1 carrier and direct-product unit-normalization wall | yes as carrier/norm contrast |
| `HIERARCHY_D4_DENSITY_SCALE_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md` | fixed positive D4 density-to-scale bridge | partial: density algebra precedent, not lepton source norm |
| `DM_WILSON_DIRECT_DESCENDANT_LOCAL_SCHUR_SOURCE_FAMILY_THEOREM_NOTE_2026-04-18.md` | conditional determinant-response Schur source family | partial: determinant-response shape, not lepton carrier or L1 norm |
| `#4928` | AC value-face realized-state bookkeeping | Koide guard only |

No source-unit witness is counted as an L1 density theorem.

### N5 - Rhetoric audit

The note avoids saying "`1/256` is not derivable." The tested resolutions are:

| resolution | tested? | outcome |
|---|---|---|
| one-slot `M_2(C)` L1 density | yes | `1/4`. |
| one-slot `M_2(C)` L2 unit | yes | `1/2`. |
| four-slot product L1 density | yes | `1/256`. |
| four-slot product L2 unit | yes | `1/16`. |
| RN/Fisher source-unit transfer | yes | L2 class, `1/16`. |
| determinant/Schur/volume future routes | not closed | left open. |
| physical charged-lepton L1 source-density theorem | not closed | named A2.2-A2.4. |

### N6 - Partial-closure path scan

Legitimate closure paths remain:

| path | what it could close |
|---|---|
| retained theorem identifying the lepton scalar source as an L1 algebra-coordinate density | A2.2 and A2.4 |
| determinant/log-volume theorem whose normalized coefficient equals the L1 density | A2.2 through A2.4 |
| Schur carrier theorem deriving a charged-lepton `/64` or equivalent L1 coefficient | parallel Route B and A2 |
| convention-retirement audit showing the existing source coefficient already has L1 density semantics | A2 without a new axiom |
| direct noninteger divisor theorem | A2/A3 combined if it bypasses exact `256` |

These are not new axioms if derived or retired through audited convention work.
The artifact is a discriminator, not a no-go.

### N7 - Steelman

A hostile reviewer can argue that a source/action coefficient is naturally an
L1 density, because it weights action terms rather than normalizing a state
vector. The lepton-scale probe writes `1/(dim_C M_2(C))^4`, not
`1/sqrt(dim_C M_2(C)^4)`, so the notation already chooses algebraic density.
The RN/Fisher comparison may be attacking the wrong source semantics. This is
the strongest positive route. The rebuttal is narrow: the repo still needs to
prove that the charged-lepton scalar source uses that L1 density semantics;
the existing source-unit theorem alone does not supply it.

### N8 - Cross-cycle echo

This mirrors the Koide form/weight split and the hierarchy density-scale
bridge: exact algebraic normalization classes can be clean before the physical
readout identity lands. Some similar walls have later moved by proving that a
quantity already had the needed density semantics. This note preserves that
path and names the exact target.

**Gate result:** broad no-go fails; narrowed L1 source-norm discriminator
passes.

## Explicit Non-Claims

- No derivation of `S_l = 1/256`.
- No derivation that the charged-lepton scalar source uses L1 algebra-density
  semantics.
- No derivation of uniformity over the 256 algebra coordinates.
- No derivation of the charged-lepton tensor lift.
- No derivation of a determinant, Schur, or volume-density theorem.
- No derivation of the `256.08` precision correction.
- No derivation of `m_e`, `alpha(0)`, or hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_l1_source_norm_discriminator.py
```

The verifier checks the L1/L2 source-norm arithmetic, transfer boundaries for
the RN/Fisher and density-scale lanes, primitive-registry boundaries, open-PR
alignment, no-go discipline, and explicit non-claims.
