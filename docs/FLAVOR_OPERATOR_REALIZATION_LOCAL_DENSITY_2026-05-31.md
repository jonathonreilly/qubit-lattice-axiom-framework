# Flavor operator-realization local-density bridge: executable finite KS check

**Date:** 2026-05-31; repaired 2026-06-03
**Claim type:** bounded_theorem
**Claim boundary:** bounded finite-lattice operator certificate for the supplied
Kawamoto-Smit staggered surface at `L=4,6`. It proves the local-density
operator side inside this packet; it does not prove the physical readout bridge
that a single fixed-point summand is the charged-lepton asymmetry observable.
**Runner:** `scripts/flavor_operator_realization_local_density_2026_05_31.py`
(`SCORECARD PASS=10 FAIL=0`).

## Question

Does the supplied finite Kawamoto-Smit staggered operator realize the
Atiyah-Bott local fixed-point density `L_3(1,2)=2/9` through an actual
`C_3` operator action, rather than by importing the `(1,2)` weight by hand?

## Verdict

Yes, on the bounded finite surface checked here. The runner now builds the
nearest-neighbor 3D staggered operator directly on even periodic `L^3`
lattices and verifies the operator side of the bridge:

1. The raw cyclic axis permutation fails to commute with the staggered operator:
   `||P D P^T - D|| = 13.8564` at `L=4` and `25.4558` at `L=6`.
2. An explicit site-local `Z_2` sign gauge repairs the cyclic action:
   for `U_phys = S P`, the runner verifies `U_phys D U_phys^T = D` and
   `U_phys^3 = I` to numerical zero at both `L=4` and `L=6`.
3. The tangent action at a diagonal fixed site splits as one singlet plus the
   faithful transverse `C_3` doublet with weights `(1,2)`.
4. The local Atiyah-Bott density is computed exactly:
   `L_3(1,2)=2/9`, while the degenerate alternative gives `L_3(1,1)=1/9`.
5. The global readouts vanish on the same finite operators: the staggered
   chirality anticommutes with `D`, the signed eta sum is zero, the
   equivariant eta trace is zero within numerical tolerance, and
   `Tr(gamma5 U_phys)=0`.

So the value `2/9` is no longer just an abstract representation-weight
calculation in this packet. It is the local fixed-point density of an explicitly
constructed, gauge-corrected `C_3` symmetry of the supplied finite staggered
operator.

## What changed in this repair

The previous runner hard-coded the hardest operator claims as passing prose
checks. This repair removes those prose-only checks and replaces them with:

- construction of the finite `L^3` Kawamoto-Smit nearest-neighbor matrix;
- construction of the raw cyclic coordinate permutation;
- graph-based solution of the site-local `Z_2` sign gauge satisfying
  `diag(s) (P D P^T) diag(s) = D`;
- verification that the corrected symmetry has order three and commutes with
  the operator;
- exact symbolic verification of the `(1,2)` density and transverse
  determinant; and
- finite spectral verification that global eta/equivariant readouts vanish.

## Remaining boundary

This does not promote the charged-lepton asymmetry to a fully closed
prediction. The still-open bridge is the physical readout step:

> the charged-lepton asymmetry observable is the single fixed-point local
> Lefschetz density `2/9`, not the vanishing global eta/equivariant invariant
> and not the extensive sum over all fixed sites.

This PR also does not claim a thermodynamic-limit theorem, a continuum theorem,
or a new axiom. It is a bounded executable operator certificate for the finite
KS surface used by the flavor asymmetry packet.

## Load-bearing one-hop authorities

- [`STAGGERED_AXIS_SYMMETRY_IS_S3_NARROW_THEOREM_NOTE_2026-05-23.md`](STAGGERED_AXIS_SYMMETRY_IS_S3_NARROW_THEOREM_NOTE_2026-05-23.md)
  supplies the retained-bounded axis-as-gauge context; this runner constructs
  the cyclic `Z_2` gauge explicitly on the finite `L=4,6` operators.
- [`HIERARCHY_APS_ETA_STAGGERED_BULK_VANISHING_SCOPING_NOTE_2026-05-26.md`](HIERARCHY_APS_ETA_STAGGERED_BULK_VANISHING_SCOPING_NOTE_2026-05-26.md)
  supplies retained-bounded context for the staggered global-vanishing surface;
  this runner recomputes the finite global eta/equivariant vanishing checks
  inside the current packet.
- [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md),
  [`THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md`](THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md),
  and [`THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md`](THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md)
  supply the retained finite `C^3` generation-carrier algebra context. The
  physical charged-lepton readout identification remains outside this note.

## Non-load-bearing context

The broader `Z_N` spectral-asymmetry and ABSS/global-bridge packets remain
outside this theorem's load-bearing chain. This note recomputes the local
`L_3(1,2)=2/9` arithmetic directly and keeps the physical single-summand
readout promotion as the named open bridge.
