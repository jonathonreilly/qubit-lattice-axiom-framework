# Cycle 727: finite-box signed reference-to-companion pullback relation

Claim type: `bounded_theorem`

Primary runner: [finite-box runner](../scripts/frontier_cycle727_cross_code_equivalence_2026_07_28.py)

Supporting implementation:

- [pullback primitives](../scripts/frontier_cycle727_cross_code_pullback_core_2026_07_28.py)
- [pullback analysis and supply predicates](../scripts/frontier_cycle727_cross_code_pullback_analysis_2026_07_28.py)
- [finite Pauli/tableau substrate](../scripts/frontier_cycle727_finite_pauli_tableau_2026_07_28.py)
- [finite reference and companion fixtures](../scripts/frontier_cycle727_finite_fixtures_2026_07_28.py)
- [finite companion factorization](../scripts/frontier_cycle727_finite_factorization_2026_07_28.py)
- [partial census and seam spot check](../scripts/frontier_cycle727_cross_code_independent_check_2026_07_28.py)
- [hash-bound receipt](../outputs/cross_code_equivalence_cycle727_receipt_2026_07_28.json)

## Self-contained finite contract

The load-bearing finite fixture, signed-Pauli, tableau, and factorization
definitions are included in the Cycle-727 helper modules above. No Cycle-720
theorem, runner, or audit status is imported as authority. The implementation
was mechanically extracted from the finite definitions historically developed
with
`docs/RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md`,
then compared field by field against those earlier definitions on all four
boxes during review. That path records provenance only and is not a dependency
of this theorem.

## Finite proposition

For each shape

```text
(2,2,2), (3,2,2), (3,3,2), (5,3,2)
```

there is a shape-specific fitted algebraic orientation/factorization for which
the `CellEdgeGauge`, `EulerMarkerGauge`, and fixed-parity
`CompanionFixture` presentations have identical signed pullbacks for every row
of one frozen even-CAR dictionary in each separately supplied sector
`s=+1` and `s=-1`.

The dictionary contains five ordered families:

```text
free       6N
seam       E
reverse    E
contact   15N
coin      15N
total   36N + 2E
```

The primary runner checks each family separately for binary rank, signed
phase and coordinate agreement, zero decoded subsystem-gauge leakage, explicit
center/parity supply predicates, and locality. It also content-addresses the
per-generator certificates.

| shape | cells `N` | edges `E` | dictionary rows | Euler exponent | one fixed companion-sector exponent |
|---|---:|---:|---:|---:|---:|
| `2x2x2` | 8 | 12 | 312 | 48 | 47 |
| `3x2x2` | 12 | 20 | 472 | 72 | 71 |
| `3x3x2` | 18 | 33 | 714 | 108 | 107 |
| `5x3x2` | 30 | 59 | 1,198 | 180 | 179 |

The onsite families have cell diameter zero. The companion seam and reverse
rows have cell diameter at most one; the fitted reference seam and reverse
rows have cell diameter at most three. These are finite-box algebraic support
censuses, not a bounded preparation circuit.

## Explicit supply predicates

The result supplies, rather than derives, constraint signs, local-center
signs, and the fixed total-parity label. The runner nevertheless verifies that:

- the reference and Euler constraint rows have their expected independent
  stabilizer ranks;
- total matter parity is outside both stabilizer spans;
- `CellEdgeGauge` omits exactly one root Gauss row while
  `EulerMarkerGauge` includes all Gauss rows and an odd marker count;
- the companion center splits as local-center rank plus one total-parity
  coordinate;
- the physical and target designated parity coordinates are exactly
  `P_total`;
- every reported supply mask lies inside its declared coordinate range; and
- the per-family supply counts are sector-independent and match frozen
  content hashes.

A mutation control changes one supply count and requires the frozen supply
predicate to fail.

## Exact single-sector dimension lemma

On every tested box,

```text
dim(H_Euler) = 2^(6N)
dim(H_companion,s) = 2^(6N-1)
```

Therefore the full Euler register cannot map isometrically into either one
single fixed-parity companion sector: that codomain has half the dimension.
The direct sum of the two sectors has the same dimension as the Euler
register. Constructing a coherent direct-sum channel, choosing its relative
sector phase, and specifying off-diagonal sector action remain open. No
route-independent or representation-independent nonexistence statement is
made.

## Scope of the partial checker

The submitted secondary checker is deliberately labeled partial. Without
importing the Cycle-727 primary, pullback core/analysis, or factorization
modules, it AST-extracts the frozen tables, recounts stabilizer/operator ranks
and dictionary digests on all four boxes, and reconstructs the complete seam
family on `2x2x2`. It uses the submitted finite fixture/tableau substrate as
its comparison target and does not independently reconstruct the fitted
orientations, all five pullback families, supply predicates, or locality. It
therefore is not presented as an independent proof of the finite proposition.

## Supplied, derived, and open

Supplied:

- the four finite shapes, cell ordering, edge orientation, dictionary order,
  constraint sectors, local-center signs, and external parity label.

Derived within those supplies:

- the shape-specific fitted signed pullback relation for all five families and
  both fixed sectors;
- separate rank, phase, leakage, supply, and locality certificates;
- the exact single-fixed-sector dimension lemma.

Open:

- a size-independent or all-box encoder;
- bounded physical preparation of the fitted reference orientation;
- a coherent both-sector channel and odd-sector intertwiner;
- a literal physical input compiler and collision-free controller epoch;
- any marker/coframe structural map;
- autonomous sector preparation, global tiled channel consistency, periodic
  topology, repair, renewal, and fault tolerance.

The failed no-go minimum for broader negative readings is resolved by this
narrow claim boundary: the package retains only the stated dimension lemma and
does not promote any general obstruction.
