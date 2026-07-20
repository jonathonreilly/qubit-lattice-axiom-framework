# Time-axis source navigation inventory and finite witness replay

claim id: `time_axis_import_bundle_three_leg_disclosure_bounded_note_2026-07-17`

**Type:** meta

- **Date:** 2026-07-17
- **Claim strength:** support-only navigation plus two finite, independently
  reproducible witness families; no theorem about a necessary or complete
  time-axis import decomposition
- **Premise weight:** zero for the navigation labels; downstream science must
  cite and classify the underlying source rows directly
- **Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
- **Primary runner:** `scripts/time_axis_import_bundle_three_leg_disclosure_2026_07_17.py`
- **Cached run:** `logs/runner-cache/time_axis_import_bundle_three_leg_disclosure_2026_07_17.txt`

## Purpose

This file is a navigation aid for work that uses a fourth lattice coordinate,
an OS/RP transfer construction, or a physical clock interpretation. It records
where the relevant conditions are discussed and keeps two finite witness
replays in one place.

The labels A/B/C/D below are bookkeeping labels only. This note does not prove
that a phrase such as “`Z^4` with OS time” logically requires those components,
that the list is minimal or complete, or that the components are independent.
It is not a sufficient theorem dependency. A downstream claim must cite the
underlying row that supplies each condition it actually uses.

## Source navigation inventory

| Label | Question to classify in the downstream claim | Direct source rows | This note's disposition |
|---|---|---|---|
| A | What relates a realized record history and its monotone index to an operator-layer transfer direction and any periodic compactification? | [`TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md`](TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md) | Navigation only. The source row owns its representation-bridge scope. |
| B | What selects or declares which lattice axis carries the RP/transfer construction? | [`SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md`](SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md) and the `B-AXIS.2` surface in [`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md) | Navigation only. The finite BC-asymmetry calculation below is a witness on one explicit block, not an axis-selection theorem. |
| C-internal | What normalization accompanies the supplied two-step transfer object? | The `B-AXIS.1` split in [`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md) and [`SINGLE_CLOCK_BLOCKED_TIME_UNIT_SPLIT_N2_SUPPORT_NOTE_2026-06-17.md`](SINGLE_CLOCK_BLOCKED_TIME_UNIT_SPLIT_N2_SUPPORT_NOTE_2026-06-17.md) | Navigation only. The source distinguishes the internal `2a_tau` denominator from an absolute physical unit. |
| C-absolute | What supplies an absolute clock unit, time metric, or physical rate? | The same `B-AXIS.1` sources above and the rate boundary in the time-axis note | Navigation only. No absolute unit or rate is computed here. |
| D | What excludes or admits an independent commuting transfer factor as a second physical clock? | The `B-AXIS.3` surface in the axiom-first note, [`SINGLE_CLOCK_INDEPENDENT_COMMUTING_TRANSFER_FACTOR_N5_NO_GO_NOTE_2026-06-17.md`](SINGLE_CLOCK_INDEPENDENT_COMMUTING_TRANSFER_FACTOR_N5_NO_GO_NOTE_2026-06-17.md), and [`SINGLE_CLOCK_PHYSICAL_CLOCK_ADMISSION_INVENTORY_N5_SUPPORT_NOTE_2026-06-17.md`](SINGLE_CLOCK_PHYSICAL_CLOCK_ADMISSION_INVENTORY_N5_SUPPORT_NOTE_2026-06-17.md) | Separate downstream condition; it is not folded into A, B, or C. This note does not adjudicate the cited rows. |

Audit and effective status are pipeline-derived and intentionally not copied
into this source-authored table. Consumers must read the live audit ledger and
the cited rows rather than treating this inventory as status authority.

The Record permanence sentence used by the finite record fixtures comes from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md): when a Record is
present it is permanent. That approved premise does not itself provide the
operator-layer bridges catalogued above.

## Finite witness claims

### W1 — explicit staggered-hop exchange witnesses

On the finite block `(L_tau, L_1, L_2, L_3) = (4, 4, 2, 2)` with mass `0.3`,
the runner constructs the antisymmetrized staggered hop matrix `M_KS` and

```text
W = P_{tau<->1} diag((-1)^{x_tau x_1}).
```

It verifies the following fixture-level statements:

1. `W` is orthogonal and `W M_KS W^T = M_KS` under periodic boundary
   conditions.
2. The plain axis swap without the sign field has operator-norm residual
   `4*sqrt(2)`.
3. Antiperiodic tau with periodic `x_1` has residual `2*sqrt(2)`.
4. Antiperiodic boundary conditions on both exchanged axes restore the exact
   exchange equality on this block.
5. At zero mass, the temporal-antiperiodic sector has kernel dimension `0`
   while the spatial-periodic sector has kernel dimension `32`.

These are exact or tolerance-bounded calculations on the named finite fixture.
They do not establish a lattice-wide necessity claim and do not select a
physical time axis.

### W2 — explicit record-history fixture replay

On seven extensionally defined histories in a `2x2x2` window, the runner uses
only integer, tuple, set, frozenset, and dictionary operations to verify:

1. stacking by the history index and reconstructing the histories is an exact
   round trip;
2. the history index is record-monotone on every fixture;
3. the two generic fixtures have the history index as their unique
   record-monotone stack direction;
4. named static, single-record, uniform-burst, translation-invariant-growth,
   and face-confined fixtures exhibit non-uniqueness under the declared slice
   comparability rule; and
5. an explicitly enumerated `48`-element window-automorphism family relates
   the two generic fixtures as claimed by the runner.

This is a finite replay, not a proof of a universal record-history theorem and
not a bridge from record histories to an operator-layer transfer construction.

### P — lexical provenance checks

The runner also verifies ten selected anchor fragments in the four source files
it reads. Those checks establish only that the navigation targets still expose
the cited clauses. They do not establish necessity, completeness, implication,
or theorem support. The cache fingerprints the note and all four mutable source
texts, so a change to any of them invalidates cached evidence before use.

## Honest boundary

- This note is `meta`; it does not mint a theorem from the A/B/C/D inventory.
- The finite calculations W1 and W2 are useful support artifacts but are not
  elevated here into a physical time-selection or clock theorem.
- A/B/C/D may overlap, may be reorganized, and may be closed by one combined
  construction. The labels carry no premise weight.
- C-internal and C-absolute are deliberately distinct: a source-supported
  internal denominator is not an absolute physical clock calibration.
- D is deliberately visible as its own admission condition rather than being
  hidden inside a three-label summary.
- Literal anchor checks are provenance guards only. A semantic change outside
  an anchor can require human review even when every lexical check remains
  green.

## Non-claims

- No axis, transfer construction, compactification, clock unit, physical rate,
  or single-clock admission rule is derived or selected here.
- No source row is promoted, demoted, retained, rejected, or assigned an audit
  verdict here.
- No necessity, completeness, independence, or minimality claim is made for
  the navigation inventory.
- No downstream claim may use this wrapper in place of the direct source row
  that supplies its actual premise.
- No universal record-history proposition is re-proved by the finite fixtures.

## Source dependencies

| Dependency | Content used here |
|---|---|
| [`TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md`](TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md) | navigation for the record-history/operator representation boundary and the record-fixture design |
| [`SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md`](SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md) | source of the finite exchange/BC-asymmetry fixture design |
| [`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md) | navigation for `B-AXIS.1`, `B-AXIS.2`, and `B-AXIS.3` |
| [`SINGLE_CLOCK_BLOCKED_TIME_UNIT_SPLIT_N2_SUPPORT_NOTE_2026-06-17.md`](SINGLE_CLOCK_BLOCKED_TIME_UNIT_SPLIT_N2_SUPPORT_NOTE_2026-06-17.md) | direct C-internal/C-absolute split |
| [`SINGLE_CLOCK_INDEPENDENT_COMMUTING_TRANSFER_FACTOR_N5_NO_GO_NOTE_2026-06-17.md`](SINGLE_CLOCK_INDEPENDENT_COMMUTING_TRANSFER_FACTOR_N5_NO_GO_NOTE_2026-06-17.md) | direct D countermodel row; navigation only |
| [`SINGLE_CLOCK_PHYSICAL_CLOCK_ADMISSION_INVENTORY_N5_SUPPORT_NOTE_2026-06-17.md`](SINGLE_CLOCK_PHYSICAL_CLOCK_ADMISSION_INVENTORY_N5_SUPPORT_NOTE_2026-06-17.md) | direct D admission-inventory row; navigation only |
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Record permanence premise used by the finite record fixture |

## Runner verification map

| Block | Checks | Content |
|---|---:|---|
| `[L2-W]` | `6` | finite `W` orthogonality, exchange, falsifier, BC-asymmetry, restoration, and kernel-dimension witnesses |
| `[REC]` | `15` | exact-arithmetic record-history fixture replay and automorphism enumeration |
| `[PROVENANCE]` | `10` | selected anchor fragments present in the four files read by the runner; lexical navigation only |
| `[NOTE_HYGIENE]` | `4` | meta/status-authority metadata, required sections, bounded vocabulary, and decimal-placement checks |

## Run

```text
$ python3 scripts/time_axis_import_bundle_three_leg_disclosure_2026_07_17.py
Expected final line: TOTAL: PASS=35 FAIL=0
```

## Cached run result

```text
cache: logs/runner-cache/time_axis_import_bundle_three_leg_disclosure_2026_07_17.txt
TOTAL: PASS=35 FAIL=0
```

The paired cache is valid only while both the runner SHA and its declared-input
fingerprint match the current repository files.
