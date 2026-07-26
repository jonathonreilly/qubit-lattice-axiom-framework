# Cycle 703 patch BKSF tableau covariance — review note

**Date:** 2026-07-25

**Type:** meta

**Authority:** none

**Audit:** unset

**Status:** open-patch and periodic tableau/coset/recurrent-layer construction
positive; geometric preparation remains separate

## Scoped target

The companion scales the phase-oriented edge-qubit state isometry from two
cells to the open three-center L, held 2 x 2, and held 3 x 3 cell geometries.
It also attempts periodic `L=3` with three fixed +1 Wilson rows.  The cell
order is a supplied nearest-neighbor Hamiltonian path.  Each cell carries six
matter modes, one reference mode, the 12 octahedral matter edges, and six
reference spokes per cell.

There are zero extra intercell reference edges.  An adjacent stream uses the
ordinary matter edge and the existing endpoint spokes.  If the stream is a
chord of the supplied cell path, the physical Pauli word also carries the
matter-parity product of every intervening cell.  This is the zero-extra-
reference-edge path grammar.

The graph is not identical to the older Cycle-269 overlap substrate.  That
substrate uses the six-mode matter-only Cycle-235 graph plus supplied carrier,
port, and role-register M2s.  The present graph adds a seventh fermionic
reference and six spokes in every cell, although it adds no reference bond
between cells.  The geometry of the coarse-cell centers overlaps; the physical
edge-qubit graph does not.

The companion constructs independent fundamental-cycle bases, `N-1`
independent local-D rows, phase-oriented logical matter `X/Z`, and a complete
canonical symplectic tableau.  For periodic `L=3`, the cycle basis is split by
universal-cover winding into a contractible kernel plus three axis Wilson
generators, all fixed to +1.

Every matter stream, onsite octahedral coin edge, onsite `B`, and within-cell
`B_i B_j` contact is conjugated through the tableau and compared as an exact
logical Pauli identity with an independently derived Jordan-Wigner/CAR target.
Code preservation and inverse-tableau reconstruction are checked per summand.
No dense physical state or matrix is constructed.

## Transformed-E comparison

Translations and all 24 proper-cubic frames rebuild the target graph and its
independent tableau.  The physical edge permutation is supplemented by the
same local incidence-order CZ/Z gauge needed by the BKSF `A` generators.  The
comparison is not operator covariance alone:

1. every signed source stabilizer must land in the target +1 stabilizer group;
2. every logical `Z` must land on the permuted target occupation operator;
3. every phase-oriented logical `X` must land on the independently computed
   second-quantized Fock-permutation image, including its crossing `Z` factors;
4. the full transformed `W/V` tableau must stay canonical and round-trip in
   target tableau coordinates.

These conditions determine equality of the transformed state isometries up to
one irrelevant common phase.  They test transformed-E rather than inferring it
from update-word covariance.

## Exact patch census

The phase-aware rank, deletion, inverse, and operator checks close with zero
failures:

| geometry | edge M2 | loops / Wilson / D | logical qubits | tableau rows | stream / coin / contact factors |
| --- | ---: | ---: | ---: | ---: | ---: |
| open three-center L | 56 | 36 / 0 / 2 | 18 | 112 | 2 / 36 / 45 |
| held 2 x 2 | 76 | 49 / 0 / 3 | 24 | 152 | 4 / 48 / 60 |
| held 3 x 3 | 174 | 112 / 0 / 8 | 54 | 348 | 12 / 108 / 135 |
| periodic `L=3` | 567 | 376 / 3 / 26 | 162 | 1,134 | 81 / 324 / 405 |

The tableau SHA-256 values in the same order are
`d86785acefc2f85f057c984d856bcbc797308502b9a65285536ec53876af91e3`,
`269a9f9895e1131461410371a2987c63a534f897ced130724886611d0281a454`,
`c276cc24c8418ee4cc5c14f7feacb24a92a7e74d6a66b0fd4fb5478761f91035`,
and
`b23e26cb9104c226f2ca98d537713092a89049d60c546206550f9da8d03d3ac5`.
Deleting any loop or retained `D` drops the stabilizer rank by one; deleting
any periodic Wilson does likewise.  Adding the globally redundant last `D`
does not increase rank and the product of all `D` rows is the phase-free
identity.  Logical `X/Z` add exactly twice the matter-logical count modulo
the stabilizers.  All stream terms, all 12 onsite coin edges per cell, all
six occupations per cell, and all 15 onsite contacts per cell preserve the
code, decode to the independent CAR target, and round-trip through the
tableau inverse.

Before fixing Wilson character, periodic loop plus `D` rank is `402`, so the
code exponent is `165 = 162 + 3`.  This is typed explicitly as
`H_matter tensor C^8_Wilson`; every tested update is
`G_matter tensor I_Wilson`, while cubic transformations only permute the
three Wilson quotient bits.  The displayed 1,134-row tableau fixes the `+++`
slice, but the operator conclusion does not require selecting a Wilson
vector in the direct sum.

## Signed stabilizer-coset localization

For every stream term under all 24 proper-cubic frames and all translations
(four per open patch, all 27 on periodic `L=3`), the runner compares the
transformed source with an independently rebuilt target path-grammar word.
Raw transformed and target-grammar Paulis are exactly equal, including phase:
the raw-target inequality count is zero.  The runner then applies a
deterministic strictly weight-decreasing multiplication by the declared
loop/`D`/Wilson basis.  The resulting representative is usually a different
full Pauli but is signed-coset equal and has the identical independently
decoded logical word.  This is a code-space equality, not an assertion that
the two full-Pauli actions agree away from the stabilized subspace.

| geometry | maximum raw weight | maximum descended weight | maximum cell diameter | maximum basis rows used |
| --- | ---: | ---: | ---: | ---: |
| open L | 13 | 13 | 2 | 1 |
| held 2 x 2 | 25 | 25 | 2 | 2 |
| held 3 x 3 | 40 | 40 | 4 | 3 |
| periodic `L=3` | 147 | 137 | 3 (torus metric) | 9 |

This descent is a constructive representative and upper bound, not a global
minimum-weight decoder.  In particular, it does **not** localize every word
to weight 17: the growing-weight caveat survives this stabilizer-basis
stress test.  Conversely, weight growth is not promoted to a no-go.  For
every frame/translation at least one reduction is nontrivial; deleting one
participating independent stabilizer row makes the signed reconstruction
certificate fail, while the complete reduction has zero reconstruction,
code-preservation, or decoded-action failures.  Separately, deleting the
intervening cell-parity factor from each actual path chord changes its logical
CAR action: `0,1,4,55` active chord deletions on L, 2 x 2, 3 x 3, and periodic
`L=3` respectively.

The support roles must not be conflated.  The following rows use the base
geometry after the same strict stabilizer descent; each entry is
`maximum weight / maximum cell diameter`:

| geometry | individual `G_physical` Pauli summand | complete factor union | logical loader `Z` | logical loader `X` | full `W/V` tableau row |
| --- | ---: | ---: | ---: | ---: | ---: |
| open L | 13 / 2 | 17 / 2 | 6 / 1 | 15 / 2 | 15 / 2 |
| held 2 x 2 | 23 / 2 | 28 / 2 | 6 / 1 | 16 / 2 | 38 / 2 |
| held 3 x 3 | 39 / 4 | 43 / 4 | 6 / 1 | 17 / 2 | 72 / 4 |
| periodic `L=3` | 135 / 3 | 139 / 3 | 6 / 1 | 19 / 2 | 74 / 3 |

Thus the existing weight-17 local grammar closes the open-L fixture only.
On these supplied path-chord targets, even the individual physical update
summands grow; this is not merely growth of a logical loader or a tableau
destabilizer.  The finite scheduled recurrence below is exact, but the
uniform constant-support recurrent-update success contract remains open.

## Executed recurrent layer

The note does not stop at an operand dictionary.  On the open L and held
2 x 2 code spaces it fixes an ordered product of formal nonzero Pauli
rotations comprising every onsite coin edge, every directed seam, and every
onsite contact.  A deterministic edge-M2 conflict coloring gives:

| geometry | coin / seam / contact factors | colors | collisions |
| --- | ---: | ---: | ---: |
| open L | 36 / 2 / 45 = 83 | 25 | 0 |
| held 2 x 2 | 48 / 4 / 60 = 112 | 27 | 0 |

Each two-term hop factor is decoded as a complete factor, preserves every
stabilizer, and induces the target logical rotation before the next factor is
appended.  This supplies an exact factor-by-factor common-E induction for the
whole scheduled `G_physical`; no dense full-volume matrix is inferred or
formed.  Four translated rebuilds have zero coset, color, or collision
failures.  Removing the complete first directed-seam factor changes both the
physical and logical schedule digests on each geometry, so the composition
deletion is active.

The common E used here is not a locally prepared tensor product of bounded
per-cell blocks.  It is the global Clifford isometry selected by symplectic
completion of the connected loop/`D`/(on the displayed slice, Wilson)
stabilizer code.  No bounded-depth/range circuit prepares it in this note.

As a no-refit bridge only, the runner consumes the byte-pinned Cycle-629
contact-dimer receipt with inherited `beta=-0.3` and `g=0.37`.  Exact
factor induction gives `E^dagger U_physical E = U_matter`; therefore each
retained Ritz vector maps to `E v` with the same eigenvalue and residual norm.
The three non-null Cycle-629 rows are copied with exactly zero restricted
spectrum and Ritz-residual differences.  This is inherited spectral
preservation, not a rerun, parameter selection, new empirical prediction, or
claim that a spectral line is an energy.

## Preparation boundary

The deterministic completion is global Gaussian elimination.  Its tableau
rank proves a finite Clifford extension and the runner checks its inverse; it
does not prove bounded-depth or bounded-range preparation.  The path-parity
dressing is empty on Hamiltonian-path edges but grows on chord edges.  Fixed
Wilson character also does not supply Wilson genesis.  Gate routing,
measurement-assisted preparation, and fixed-character resource preparation
remain separate tasks.

No axiom conclusion follows.

## No-Go Discipline

**Gate result: FAIL for any broad compiler or preparation no-go.  Ship only
executed positive rows and explicit open tasks.**

- **N1 — Alternative routes.** Distinct routes include the present supplied
  cell-path parity grammar, a direct parallel-reference-edge graph, a
  geometry-aware local Clifford synthesis, stabilizer measurement with
  feed-forward, a pre-prepared fixed-Wilson resource, and a carrier/role graph
  matching Cycle 269 exactly.  None is ruled out as a family.
- **N2 — Condition independence.** Exact finite tableau existence, local
  update support, transformed-E covariance, geometric gate depth/range,
  periodic Wilson selection, Wilson genesis, and Cycle-269 graph identity are
  independent obligations.  The note does not inflate them into one wall.
- **N3 — Hidden-condition scan.** The supplied Hamiltonian cell path, local
  port order, fixed loop/Wilson character, seventh reference mode, six spokes,
  open versus periodic boundary, and parity-even update scope are explicit.
- **N4 — Residual matching.** Rank/inverse checks certify the tableau;
  stabilizer membership certifies leakage and character; Pauli conjugation
  certifies common-E; support counts certify only held-patch support.  None is
  relabeled as a gate-synthesis or genesis residual.
- **N5 — Resolution audit.** The runner separates cell, stream edge, supplied
  path, held two-dimensional patch, periodic `L=3` volume, and growing-family
  claims.  Held sizes do not establish asymptotic bounded depth or range.
- **N6 — Partial-closure and primitive scan.** Geometry-aware Clifford
  synthesis, local stabilizer measurements, alternate cycle bases, admitted
  fixed-character resources, and a direct Cycle-269 graph tableau remain
  constructive routes.  No new primitive or premise edit is requested.
- **N7 — Steelman.** A hostile reviewer can plausibly eliminate the growing
  chord dressing by changing the logical gauge, adding local ancillas, or
  synthesizing a different tableau; they can also adopt the already supplied
  Cycle-269 carrier/role resources.  The current calculation cannot foreclose
  those mechanisms.
- **N8 — Cross-cycle echo.** Earlier uniform-reference and finite-tableau
  failures were retired by local-D constraints and an explicit phase-oriented
  tableau.  Their former negative language cannot be echoed against larger
  patches.  Conversely, a held-patch success cannot be echoed as a scalable
  preparation theorem.

## Reproduction

```bash
PYTHONPATH=scripts python3 \
  scripts/frontier_cycle703_bksf_patch_tableau_covariance_2026_07_25.py
```

The intended terminal is
`PATCH_AND_PERIODIC_BKSF_TABLEAU_COVARIANCE_POSITIVE_GEOMETRIC_PREPARATION_OPEN`.
