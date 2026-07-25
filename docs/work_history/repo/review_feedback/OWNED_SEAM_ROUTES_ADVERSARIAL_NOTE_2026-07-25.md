# Owned-seam routes adversarial note

**Type:** meta

**Date:** 2026-07-25

**Reviewed commits:** `315788cd7e`, `483b24693e` (including square decoded
repair `efbc469453` and self-downgrade `582a430b68`)

**Authority:** none

**Audit:** unset

**Status:** finite primitive constructions positive; full physical compositions open

## Comparative verdict

Both repairs contain substantial positive work. The hardened direct-ROM route
now supplies coefficient- and stage-associated observation controls, bounded
coarse support geometry, hash-inventoried finite ROMs, and full L5/L6 torus-
translation audits. The sparse route executes an exact 224-CZ correction as a
378-factor nearest-neighbor word, returns dirty transit M2 exactly, and now
constructs a square unitary decoded direct-sum completion with a same-encoding
residual below `8.5e-16`.

Neither runner executes a full local-M2 all-eleven update on the common
encoding. The sparse owner now says this explicitly: the repaired object is a
decoded compiler candidate, not a physical-site compiler. This is an
equivalent-gap disposition, not a no-go.

| Obligation | Direct ROM `315788cd7e` | Sparse route `483b24693e` |
| --- | --- | --- |
| Old source-XOR decoder self-award removed | closed | not used |
| Physical transition descriptors / routed transition | closed as coefficient-tagged finite ROM | closed as target-inversion-derived 378-factor word |
| Transition order | closed per owner; common product not assembled | closed: correction must precede seams |
| Work return | membership argument per descriptor | closed for both dirty center M2 |
| Coarse locality and translations | diameter 3, owner radius 1; all L5/L6 translations | nearest-neighbor finite fixture |
| Gate-derived carrier preparation | closed in finite ROM | closed as label-block seven-rail matrices |
| Square algebraic completion on common `E` | not assembled | closed on a 125,749-row decoded direct sum |
| Fixed tensor-product M2 ambient | open | open; 125,749-row object is a global-label direct sum |
| All eleven signed local-M2 seams applied on common `E` | open | open; aggregate logical monomials are lifted |
| Shared q-chart preservation after complete word | open | open |
| Operand-level physical-word covariance | open | open |
| Common-code intertwiner/leakage residual | open | closed for decoded direct sum; open for local-M2 word |
| Recurrent/autonomous lattice law | open | open |

## Direct-ROM route

### Observation-only rekey attack passes

The new descriptor conflict check keys rows by `(owner, source_observation,
source_pair, target_pair)`, while the claimed projector control uses physical
observations. Removing the two hidden ray-pair fields does not expose a conflict
on the enumerated domain:

- 46,306 hidden-key directed rows remain 46,306 distinct physical directed
  `(owner, source_observation, target_observation)` rows;
- none has more than one Pauli transition;
- the 23,153 unordered observation pairs contain exactly the expected two
  reverse orientations.

Thus `source_pair` is redundant on this finite enumeration; it is not hiding a
projector conflict. The hardened runner now performs its own observation-only
control rekey after adding the action, stage, and coefficient record and again
reports 46,306 rows with zero conflicts.

### Coefficient, stage, and action association is closed

`local_carrier` now records every Givens factor as `(logical column, canonical
row, other row, cosine, sine)`. The primitive synthesis associates each of the
46,306 transitions with a unique left-carrier Givens, right-carrier Givens, or
occupation-FSWAP action, including its factor ordinal and complex coefficient.
There are zero association conflicts and zero descriptors without a
coefficient/action record. The owner word explicitly supplies left unprepare,
right unprepare, occupation FSWAP/collision phase, inverse right, and inverse
left order.

### Finite locality and translation controls are closed

The hardened support decoder maps edge, vertex, role, and chart M2 factors back
to coarse cells. At both L5 and L6, the maximum periodic coarse L1 diameter is
3 and the maximum radius from an owner endpoint is 1. This closes the earlier
support-count-only finding for the declared finite fixtures.

The translated-fixture control also checks every torus anchor: 125 translations
and 1,375 owner fixtures at L5; 216 translations and 2,376 owner fixtures at
L6. Chart ambiguity, invalid qutrit words, duplicate-chart failures, and carrier
coefficient mismatches are all zero.

### The finite ROM is supplied; recurrent autonomy remains open

The deterministic ROM inventory now includes observation controls, transition
Paulis, action class, Givens coefficient, stage, and 11 diagonal collision-
phase rows. It is sorted and hash-inventoried separately at L5 and L6. This is
an explicit finite ROM supply and the previous ROM-absence finding is closed.

The two finite-volume ROM hashes differ, and the runner explicitly sets
`translation_invariant_recurrent_law_derived` and
`recurrent_volume_update_claimed` to false. Exhausting translations within L5
and L6 does not yet give one volume-independent translated generator or a
collision/composition theorem for overlapping recurrent fixtures.

The direct all-eleven result also remains `11 * max(local residual)` in
`composed_update_controls`; no common physical product is applied. The exact
remaining direct obligation is therefore the common-`E` product/residual and
the recurrent/autonomous-law bridge, not the finite primitive synthesis.

## Sparse routed-transition route

### The routed correction is genuinely executed

The route contains 33 same-cell, 114 neighbor-cell, and 77 distance-two CZ
terms. Every distance-two term is realized as `SWAP-CZ-SWAP`. The runner checks
all 616 local dirty-transit truth-table cases and all 10,516 combinations of the
2,629 `n <= 2` columns with two arbitrary center-transit bits. Data, phase, and
both transit bits return exactly. Sequential reuse of the two center M2 across
all 77 macros is therefore closed for the transition word.

The order is also substantive. `candidate_stream @ transition` equals the
target exactly, whereas moving the correction after the signed seam product
leaves 100 mismatched columns with raw residual 2.

### The square decoded residual is genuine

The `efbc469453` repair closes the previous rectangular-projector and runtime
target-matrix-injection findings. It constructs the candidate from the ordered
11 seam matrices and does not pass `target_stream` as the executed operand.
However, the 224-CZ transition was synthesized offline from the supplied target
exterior inversion set. Commit `483b24693e` now discloses this explicitly; the
candidate is target-independent, while the transition is not an autonomous
target-free derivation. The decoded completion has shape
`125,749 x 125,749`, 1,273,137 nonzeros, maximum `U^dag U-I` entry
`7.11e-15`, same-`E_refresh` intertwiner maximum `8.46e-16`, and leakage
`5.97e-16` at both L5 and held L6. The reverse-order residual remains 2.

These are real algebraic properties of the supplied square matrix. The
`582a430b68` self-downgrade correctly calls it a decoded direct-sum closure and
sets both `fixed_tensor_product_M2_compiler_claimed` and
`free_coin_composed_on_same_E` to false.

### The decoded square is not a fixed local-M2 ambient

The 125,749 rows are not a tensor-product register basis. They are the direct
sum over every complete `n <= 2` logical Fock label:

```text
1 vacuum label x 1 rail
+ 72 one-particle labels x 7 rails
+ 2,556 two-particle labels x 49 rails
= 125,749 rows.
```

The resulting dimension is odd, hence not `2^N` for any collection of M2
registers. More importantly, `lift_logical_operand` iterates over the complete
global `FOCK_BASIS`, reads the unique target from the full logical matrix
column, and maps `offsets[source] + packet` directly to
`offsets[target] + packet`. This is a global-label-conditioned monomial
completion; it is not a factorization into bounded gates on fixed local
registers.

The square word contains one aggregate lift of the whole transition, 11
aggregate lifts of whole logical seam matrices, and one aggregate lift of the
logical contact. The independently verified 378 local SWAP/CZ factors are not
applied to the square ambient, and the seam lifts are not decomposed into their
declared local CZ/SWAP factors there. The contact is likewise lifted from the
complete logical contact matrix rather than composed from the bound onsite
gates.

Chart words are enumerated to count lawful landed rows, but neither chart nor
work M2s occur as tensor operands of the decoded matrix. The qutrit XOR checks
are called only after the decoded completion has already been built. Thus the
current exact residual is not yet a local-M2 executed seam/contact word.

The free coin is absent from the decoded completion, and the
`same_encoding_certificate` target-update parameter is unused. The mass/coin
check in `main` separately calls the logical Route-C update; it does not act on
the decoded square. This separation is now accurately recorded in the sparse
runner's terminal, open list, and claim ceiling.

### Covariance is geometric plus logical, not physical-word covariance

The 24-frame test rotates the tuple of routed endpoint/midpoint labels and
checks its distance-class census. The 576-product test checks functorial tuple
transformation. Separately, Route C checks covariance of the logical
`target_update`, including the separately supplied coin. Translation rows only
check translated cell/edge cardinalities. No test rebuilds or compares the
decoded square, still less a fixed-register local-M2 word, under frames or
translations. The repaired runner now records
`physical_operand_matrices_rebuilt_under_frames = false` and
`translation_test_level = geometry-and-logical-update-only`.

The macro deletion residuals do not add such evidence: the 224 values are
created as the literal tuple `2.0 for _term in ROUTED_TERMS`.

## Exact missing executed objects

For the direct route, use the supplied coefficient-tagged finite ROMs to apply
all eleven owners on one common encoding and compute the direct intertwiner and
leakage. Before a recurrent/autonomous claim, additionally supply one volume-
independent translated generator and prove collision-safe composition for
overlapping translated two-star fixtures.

For the sparse route, embed the finite encoding into declared fixed local M2
registers, including an explicit treatment of all off-code register states.
Replace the complete-label monomial lifts with the 378 routed SWAP/CZ factors,
11 locally decomposed seam words, onsite contact gates, and chart/work erase-
return operands. Compare that independently constructed local word with the
separately constructed target by computing

```text
||U_physical E_refresh - E_refresh G_target||
```

and common-code leakage at L5 and held L6, followed by operand-level frame and
translation covariance. The free coin and mass should remain out of the claim,
as the downgraded runner now states, unless they are actually composed on this
same encoding.

## Reproduction

```bash
PYTHONPATH=scripts:<route-b-scripts>:<route-c-scripts> \
  python3 scripts/frontier_owned_seam_routes_adversary_2026_07_25.py
```

The companion terminates with
`OWNED_SEAM_TRANSITIONS_POSITIVE_FULL_PHYSICAL_COMPOSITIONS_OPEN` when all
adversarial controls behave as reconstructed.
