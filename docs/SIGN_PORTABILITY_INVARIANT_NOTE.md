# Sign Portability Invariant Note

**Date:** 2026-04-06 (status line narrowed 2026-04-28; finite-gate scope repair 2026-06-10)
**Status:** bounded finite cached gate comparison across reported sign-law
families. Not a tier-ratifiable portability theorem, cross-family inheritance
proof, or independent order parameter.

## Artifact Chain

- [`scripts/SIGN_PORTABILITY_INVARIANT_COMPARE.py`](../scripts/SIGN_PORTABILITY_INVARIANT_COMPARE.py)
- [`logs/2026-04-06-sign-portability-invariant.txt`](../logs/2026-04-06-sign-portability-invariant.txt)
- registered runner-cache output: [`logs/runner-cache/SIGN_PORTABILITY_INVARIANT_COMPARE.txt`](../logs/runner-cache/SIGN_PORTABILITY_INVARIANT_COMPARE.txt)
- first-principles derivation within one family (load-bearing dependency for the four gates):
  [`SIGN_PORTABILITY_INVARIANT_FAMILY_SECOND_GROWN_DERIVATION_THEOREM_NOTE_2026-05-09.md`](SIGN_PORTABILITY_INVARIANT_FAMILY_SECOND_GROWN_DERIVATION_THEOREM_NOTE_2026-05-09.md)
- retained family notes: [`GROWN_TRANSFER_BASIN_NOTE.md`](GROWN_TRANSFER_BASIN_NOTE.md), [`ALT_CONNECTIVITY_FAMILY_BASIN_NOTE.md`](ALT_CONNECTIVITY_FAMILY_BASIN_NOTE.md), [`SECOND_GROWN_FAMILY_SIGN_NOTE.md`](SECOND_GROWN_FAMILY_SIGN_NOTE.md), [`THIRD_GROWN_FAMILY_SIGN_NOTE.md`](THIRD_GROWN_FAMILY_SIGN_NOTE.md), [`FOURTH_FAMILY_QUADRANT_NOTE.md`](FOURTH_FAMILY_QUADRANT_NOTE.md)
- holdout confirmation: [`archive_unlanded/fifth-family-stale-runners-2026-04-30/FIFTH_FAMILY_RADIAL_NOTE.md`](../archive_unlanded/fifth-family-stale-runners-2026-04-30/FIFTH_FAMILY_RADIAL_NOTE.md), [`archive_unlanded/fifth-family-stale-runners-2026-04-30/FIFTH_FAMILY_RADIAL_FM_TRANSFER_NOTE.md`](../archive_unlanded/fifth-family-stale-runners-2026-04-30/FIFTH_FAMILY_RADIAL_FM_TRANSFER_NOTE.md), [`FIFTH_FAMILY_RADIAL_BOUNDARY_NOTE.md`](FIFTH_FAMILY_RADIAL_BOUNDARY_NOTE.md)

### Primary runner behavior (2026-05-09)

`scripts/SIGN_PORTABILITY_INVARIANT_COMPARE.py` runs in two blocks.

**Block 1 — derivation within one family.** The runner re-runs the
second grown family at a small two-row subset (`drift=0.0, seed=0` and
`drift=0.2, seed=1`) by importing the family construction and
measurement code directly. It checks the four invariant gates on each
row at the same row-level thresholds used in Block 2. This block is
the numerical-side companion to the algebraic / leading-order proofs
in
[`SIGN_PORTABILITY_INVARIANT_FAMILY_SECOND_GROWN_DERIVATION_THEOREM_NOTE_2026-05-09.md`](SIGN_PORTABILITY_INVARIANT_FAMILY_SECOND_GROWN_DERIVATION_THEOREM_NOTE_2026-05-09.md).

**Block 2 — finite cross-family gate check.** As before, the runner
reads the registered per-row outputs of each one-hop family runner
(the runner-cache files when populated, the dated logs in `logs/` as
fallback) and asserts the four common thresholds that the note
uses as the signed-control fixed-point gate packet:

- G1 zero-source cancellation: `|zero| <= 1e-12` on every row
- G2 neutral same-point cancellation: `|neutral| <= 1e-12` on every row
- G3 plus/minus antisymmetry: `|plus+minus| / max(|plus|,|minus|) <= 5e-3`
  on every row
- G4 unit-slope tolerance: `|exp-1| <= 5e-3` on every row the family
  runner itself accepted (sign orientation OK)

Rows the family runner rejected for sign orientation are surfaced as
explicit basin/seed exclusions in the runner output, per family. The
runner exits 0 only when both blocks pass; otherwise it exits 1. The
claim scope is now narrowed to the finite cached gate certificate: the
runner verifies these gates in the named logs at the displayed thresholds.
It is not a tier-ratifiable portability theorem and does not prove that other
families inherit the gates by a common lower-bound or linear-response theorem.

## Question

What is the smallest finite gate packet that survives in the registered
signed-source family logs?

## Comparison

| family | exact controls | sign orientation | weak-field response | basin shape |
| --- | --- | --- | --- | --- |
| Grown transfer basin | exact zero-source and neutral same-point cancellation | retained on nearby rows | `F~M = 1.000` | narrow and selective |
| Alternative connectivity family | exact zero-source and neutral same-point cancellation | retained on passing rows | `F~M = 0.999994` | bounded but broadest of the retained sign-law families |
| Second grown-family sign | exact zero-source and neutral same-point cancellation | retained on all tested rows | mean exponent `1.000072` | independent basin, still narrow in architecture space |
| Third grown-family sign | exact zero-source and neutral same-point cancellation | retained on passing rows | mean exponent `0.999842` | bounded drift basin |
| Fourth family quadrant | exact zero-source and neutral same-point cancellation | retained on passing rows; mixed at `drift=0.2` | alpha near `1.0` | narrow and seed-selective |

## Out-Of-Band Confirmation

The later fifth-family radial holdout agrees on the same control surface:

| family | exact controls | sign orientation | weak-field response | basin shape |
| --- | --- | --- | --- | --- |
| Fifth family radial | exact zero-source and neutral same-point cancellation | retained on sampled rows; flips at the interior boundary | mean exponent `0.999439` | narrow holdout confirmation |

## Safe Read

In the registered sign-law basin logs, the thing that survives is not the
geometry family itself.

What survives is the signed-control fixed point:

- exact zero-source cancellation
- exact neutral same-point cancellation
- plus/minus antisymmetry
- weak-field response pinned near unit slope

Within this finite cached comparison, the family construction changes basin
width and selectivity.
Some families are broad, some are narrow, and some are seed-selective, but the
signed-control gate packet passes the same thresholds on the retained/passing
rows surfaced by the family logs.

### Load-bearing step (finite cached gate certificate)

The load-bearing claim is finite and cached: the registered comparison runner
reads the listed family logs and checks the four displayed gates at the stated
thresholds. The first-principles derivation within ONE retained sign-law family
(the second grown family), documented in
[`SIGN_PORTABILITY_INVARIANT_FAMILY_SECOND_GROWN_DERIVATION_THEOREM_NOTE_2026-05-09.md`](SIGN_PORTABILITY_INVARIANT_FAMILY_SECOND_GROWN_DERIVATION_THEOREM_NOTE_2026-05-09.md),
is supporting context for that family, not a proof of cross-family inheritance.

That note derives the four gates from the action and the
source-construction map: G1 and G2 as exact algebraic identities at
finite source strength, G3 and G4 as leading-order weak-field identities
with explicit bounded second-order remainders.

This note no longer claims that the other families inherit the four gates by
the same proof steps. A family-uniform lower-bound / linear-response bridge,
especially for G4, remains open. The table above is therefore a finite
comparison certificate over the registered family logs, not an inherited
cross-family theorem.

## Exact Mismatch

- basin width is not invariant
- seed selectivity is not invariant
- complex-action selectivity is not part of this invariant
- the `gamma = 0` branch analog is not the same control surface as the
  zero-source signed branch

## Final Verdict

**bounded finite cached gate comparison positive:** the registered family logs
pass the signed-control gate packet under the comparison runner thresholds,
with basin width as the family-dependent variable. This does not promote the
note to a tier-ratifiable portability theorem or a cross-family inheritance
proof.

## Review boundary

Earlier review feedback flagged the old source as a cross-family comparison
without enough one-hop family wiring or a registered comparison runner/cache.
This repair keeps the bounded comparison value while narrowing the source to
the finite cached gate certificate. It is not a portability theorem or an
independent order parameter.

## What this note does NOT claim

- A tier-ratifiable portability theorem.
- A cross-family inheritance proof.
- An independent order parameter beyond the cross-family comparison.
- That the in-family derivation theorem note is itself fully
  unconditional: it still has its own row-wise lower-bound condition for the
  detector denominator and the plus-source linear response (G4 conditional).
  Block 1 of the runner therefore verifies G1/G2/G3/G4 numerically at
  the working source strength but does not promote the theorem note
  beyond its own conditional status.

## Audit dependency repair links

The one-hop dependencies of this note are wired by markdown links in the
artifact chain above and are regenerated into the audit ledger by the
pipeline. The live audit ledger owns their effective statuses. The
cross-family comparison block of the runner reads the same family
runner-cache outputs that their own runners produce.

| dep claim_id | family runner | runner-cache file |
| --- | --- | --- |
| `sign_portability_invariant_family_second_grown_derivation_theorem_note_2026-05-09` | (this runner, derivation block) | n/a (in-process) |
| `alt_connectivity_family_basin_note` | `scripts/ALT_CONNECTIVITY_FAMILY_BASIN.py` | `logs/runner-cache/ALT_CONNECTIVITY_FAMILY_SIGN_SWEEP.txt` |
| `second_grown_family_sign_note` | `scripts/SECOND_GROWN_FAMILY_SIGN_SWEEP.py` | `logs/runner-cache/SECOND_GROWN_FAMILY_SIGN_SWEEP.txt` |
| `third_grown_family_sign_note` | `scripts/THIRD_GROWN_FAMILY_SIGN_SWEEP.py` | `logs/runner-cache/THIRD_GROWN_FAMILY_SIGN_SWEEP.txt` |
| `fourth_family_quadrant_note` | `scripts/FOURTH_FAMILY_QUADRANT_SWEEP.py` | `logs/runner-cache/FOURTH_FAMILY_QUADRANT_SWEEP.txt` |
| `fifth_family_radial_boundary_note` | `scripts/FIFTH_FAMILY_RADIAL_FAILURE_AUDIT.py` | `logs/runner-cache/FIFTH_FAMILY_RADIAL_SWEEP.txt` |

The "Grown transfer basin" entry in the cross-family table above is
verified via the dated log
`logs/2026-04-06-nonlabel-grown-drift-basin-sweep.txt` (the
runner-cache file `GROWN_TRANSFER_BASIN_SWEEP.txt` exists but is
empty in the current cache); the underlying basin authority is the
`grown_transfer_basin_note` row in the audit ledger, which is
referenced by the artifact chain but the relevant rows are also
recoverable from `alt_connectivity_family_basin_note` and the second
grown family. The cross-family threshold check in Block 2 is therefore
identical regardless of which path is used to populate the basin row.

## What would close this lane (Path A future work)

Promoting from bounded conditional to retained would require:

1. ~~Registering the comparison runner/log.~~ Done: the runner
   `scripts/SIGN_PORTABILITY_INVARIANT_COMPARE.py` is the registered
   runner for this note in the audit ledger, with cached output at
   `logs/runner-cache/SIGN_PORTABILITY_INVARIANT_COMPARE.txt`.
2. ~~Adding the family and holdout notes as one-hop dependencies with
   their current audit statuses.~~ Done: the six dependencies above
   are the audit ledger `deps` list for this row.
3. ~~Making the runner assert common thresholds for zero-source
   cancellation, neutral same-point cancellation, antisymmetry,
   unit-slope tolerance, and basin/seed exclusions.~~ Done: Block 2
   of the runner reads each family's per-row records and asserts the
   four common gates `ZERO_TOL=1e-12`, `NEUTRAL_TOL=1e-12`,
   `ANTISYM_TOL=5e-3`, `EXP_TOL=5e-3`, with rejected rows surfaced
   as explicit basin/seed exclusions per family.
4. Closing the residual G4 lower-bound condition on the in-family
   derivation theorem note (an open item on that note, not on this
   one). Until that lower-bound is supplied, the cross-family
   unit-slope corollary remains conditional on the same nonzero
   linear response assumption.
