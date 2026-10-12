# Final scoped implementation review

Source confirmation: 2026-10-12, same reviewer session as
[REVIEW_V1.md](REVIEW_V1.md). The corrected implementation passes this focused
source check under the supplied QUMOND equation and isolated-source assumptions.
The galaxy force accuracy and empirical conclusions remain conditional on the
unfinished numerical gates. This is not a whole-branch landing approval or an
audit verdict.

## Exact reviewed source

| File | SHA-256 | Disposition |
| --- | --- | --- |
| `direct_qumond_disk.py` | `701bc4d1ba659f9b25cd98855547864300b83c2f002a477e7bc3b2b5ac3f7b00` | Complete original source plus complete final correction diff reviewed; implementation confirmed within stated scope |
| `DIRECT_FIELD_DERIVATION.md` | `ad7e69fefbdf57dd6f0e961ff9e54ed96a2e4cf0000f983dbb0c16cb3e075c46` | Unchanged complete argument confirmed; continuum formula and conditional physics boundary agree with source |
| `FROZEN_FORWARD_CONTRACT.md` | `f6225b00b62a82b050586535a933f82d8320783d7934d35ef0ce9e8f31d49b93` | Unchanged protocol confirmed; numerical acceptance requirements remain binding |

The original and final solver snapshots are preserved here. Original receipts
remain bound to original source `0d02f2a...`; later ell128/256 receipts inspected
below remain bound to `144cf1f...`. They were not relabeled as final-source
executions. The latter change added controls without changing the field
projection. The final masked evaluation does not alter positive-norm,
positive-radial entries. The four frozen input hashes and complete selection
ordering checked in the first pass remain the reviewed input closure.

## Finding dispositions and affected checks

1. **Missing nonzero correction control: fixed and confirmed.** The author
   added radial-only and transverse-only l=2 controls. Their incomplete-gamma
   and E1 expressions agree with this reviewer's independent integration of
   the source-divergence Green function. The final suite reports normalized
   errors `1.37244e-5` and `1.09208e-5`. The standalone independent fixture
   also produces the same original convergence results for final source.
   Removing the correction now fails the suite. Additional mutations
   reversing its sign, halving it, and reversing the polar-basis sign all
   fail for the intended non-gradient discrepancy. The respective radial/
   transverse errors are `(4.8833, 2.0000)`, `(1.2208, 0.5000)`, and
   `(1.3724e-5, 2.0000)`.

2. **Zero-radial eager evaluation: fixed and confirmed.** A valid nonzero
   normal vector with zero radial component now yields finite projected
   force and an unavailable algebraic comparator, without evaluating nu(0).
   The original raises on the identical input. A zero vector everywhere now
   returns exactly zero projected force, consistent with
   `|nu(|U|/a0) U| ~ sqrt(a0 |U|) -> 0`. A negative-radial probe retains
   negative force; the code does not apply an absolute value to make a
   circular-support prediction positive. These are diagnostic field controls,
   not new physical source models.

3. **Numerical accuracy: still pending.** Original refinement failures remain
   in evidence. The completed ell128-to-256 comparisons, with unchanged
   radial grid and doubled angular order, give maximum relative changes:

   | Galaxy | Force change |
   | --- | ---: |
   | NGC2976 | 0.0031493603 |
   | UGC07577 | 0.0073951263 |
   | KK98-251 | 0.0016482538 |

   UGC07577 still exceeds the frozen 0.005 resolution threshold. The author's
   final-source ell512 calculation and doubled-boundary/Hankel4096 calculations
   were pending when source review concluded. This review grants no one-percent
   force budget, residual conclusion, or subset expansion. A passing source
   review cannot substitute for those numerical receipts.

The added source start/end assertion was checked by changing only a copied
review subject during its calculation. It raises the intended source-change
error and creates no output receipt. No active author source was changed.
The final author suite was rerun on the preserved exact source and passed;
the original failed mutation is now rejected. The final probe used about
106 MB maximum RSS and under one second of elapsed calculation, with one
configured numerical thread. Stop markers and the original packaging deadline
were respected.

## Evidence and scope boundary

Reviewer source:
[independent_fixture.py](independent_fixture.py),
[probe_author.py](probe_author.py), and
[affected_fix_probe.py](affected_fix_probe.py).
The independent expectation program imports no author helpers; the separate
probe executes the author only as the subject under test. The independent
derivation, units, distributional sheet treatment, input roles and original
findings are recorded in [REVIEW_V1.md](REVIEW_V1.md).

The corresponding runtime `independent_direct_review/` directory contains
`final_author_probe_v4.json`, `affected_fix_probe_v4.json`, the original
fixtures/receipts and logs, and `final_review_receipt.json` with hashes.
Reproduction uses `probe_author.py --source snapshot_final_direct_qumond_disk.py
--name <fresh-name>.json` after the frozen fixture has been generated. Output
paths are exclusive to preserve failed and successful attempts.

Two focused passes were completed. Two source findings were corrected by the
author and independently confirmed; one numerical acceptance item remains
open. The independently checked theorem is the conditional Poisson projection,
not a derivation of the supplied QUMOND law or fitted constants. No observed
velocities were read or fitted by this reviewer. No formal audit, commit,
push, status promotion, or integration pipeline was run. Further source/input
changes require affected confirmation; future numerical receipts must satisfy
the frozen gates on their own recorded identities.
