# Nine-source exposed reconstruction after the failed transfer

Parent protocol, 2026-10-12, written before this new fit. The two unchanged
six-source transfers and their failures were preserved in commit
94f791c83d before any new weights are computed. They remain failures.
The fixed campaign deadline and all cancellation guards remain in force.

Question: can the same twenty-ramp response family describe all nine fixed
source/velocity maps together? This distinguishes failure of two selected
weight vectors from limited flexibility of the declared family. It is
exposed model development; all nine velocity/error arrays are fitting data.
There is no independent test set in this block.

Use NGC2976, UGC07577, KK98-251, then all six unchanged extension names
NGC3949, NGC3972, UGC06667, UGC08837, DDO064, DDO168. Keep every scored row
and all original baryonic/geometry/nuisance assumptions. Keep knots,
nonnegative weights, sum(w)<=100, and the M and D definitions from
FROZEN_DIRECT_INVERSE_PROTOCOL.md. No knot, row, galaxy, cap, error floor,
source parameter, or statistical likelihood is adjusted.

Run exactly six cases: for each M and D, (1) nine galaxies alone,
(2) nine galaxies plus the original external-acceleration rectangle,
(3) nine galaxies plus external and solar rectangles. For cases 2 and 3,
hold E at 1.4915242022774435e-10 m/s², the previously frozen E.
This is a controlled fixed-E diagnostic, not a global optimization over E
or a rejection at every external field. Case 1 is independent of E.

Use the same checked linear-Poisson columns. Reuse the three existing
operator receipts and construct columns for the additional six from their
already validated cached Newtonian base geometries. Run the existing
Newtonian, prior-response and synthetic-superposition controls on each
new source. Save their receipts and hashes separately; no old file is
overwritten. Source-only column construction is distinct from target fitting.

The original two-stage LP is reused as a reviewed numerical component:
first minimize nonnegative common fractional acceleration tolerance t,
then minimize total weight with t<=t_min+1e-8. Preserve both solver status
and all scaled primal residuals. All six outcomes are retained. A numerical
LP minimum does not certify a continuum family exclusion.

Freeze the six returned weight vectors before direct field checks. Evaluate
each successful vector directly through P[N(|U|)U] on all nine base,
refined and extended-boundary geometries. Require positive finite forces,
maximum <=0.005 refinement change and <=0.003 boundary change. Do not
infer response convergence from the two earlier weight vectors. Readout
uses every scored row, the same descriptive rectangles, and equal-galaxy
RMS log10 velocity. Keep any difference between LP baseline g_N and the
direct finite-grid Newtonian projection; no positive mismatch is zeroed.

Solar/external quantities in the relevant cases are calibration constraints.
For galaxy-only cases any later solar readout is a diagnostic under supplied
E, not a new measurement prediction. No field theory, covariance, matter
dynamics, metric completion or statistical significance follows from the fit.

New artifacts live under runtime gravity/response_inverse/nine_source and
this source directory. Hash source, protocol, inherited components, previous
failed transfer, target/source files and all source/basis receipts. Never
overwrite a scientific receipt; interrupted numerical work may reuse only
matching identities. No new detached AI author or supervisor is involved.

Prior-source check: origin/main freshly fetched, with statement queries for
QUMOND and both orderings of nine-source response/reconstruction on source
notes. The exact existing three-source reconstruction and six-source fixed
transfer are the immediate prior work and are read in full. This is a new
exposed-data reconstruction, not a literature-priority claim or a relabelled
successful test. Full current-main search result is recorded at execution.
