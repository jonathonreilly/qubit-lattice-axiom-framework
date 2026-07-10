# Review History

## 2026-07-10 iteration 1

Parallel specialist review covered code/math, physics claim boundary,
imports/support, Nature retention, no-go discipline, labeling, and repository
governance.

Findings fixed:

- demoted trace reach from direct closure to upstream support because temporal
  mixed-kernel stripping remains open;
- narrowed the exact no-go to suppression of `L_s` across two tested PBC
  sizes; boundary-condition notation is definition hygiene, not a proved
  dependence theorem;
- demoted stochastic rhetoric to a declared bounded diagnostic and disclosed
  missing autocorrelation/ESS/confidence certification;
- added full stochastic protocol/import inventory and dependency links;
- replaced audit-authority language in the acceptance check with a declared
  heuristic window;
- checked real and imaginary beta-zero controls;
- removed a non-load-bearing audited-renaming citation edge;
- canonicalized source status wording and removed branch-workflow prose from
  the durable source note.

Independent math checks:

- a separate SciPy MILP formulation found exact minimum triality-filling
  weights `3` and `5`, matching the meet-in-the-middle runner;
- the code reviewer independently checked local versus full action changes to
  `4.44e-16`, proposal unitarity/determinant to about `1e-15`, character
  identities to about `9e-16`, and the `E[chi*]/d` normalization;
- four-chain replays reproduced the paired MC output; block-size diagnostics
  reported stable nominal errors, but those extra diagnostics are not promoted
  into a calibrated uncertainty claim.

## 2026-07-10 iteration 2

Focused re-review of changed files returned:

- Code / runner: PASS with bounded statistical disclosure;
- Physics claim boundary: OPEN parent, exact narrow NO-GO sub-result, BOUNDED
  MC packet;
- Imports / support: DISCLOSED;
- Nature retention: OPEN overall;
- No-Go Discipline: PASS for the narrow `L_s`-suppression claim;
- Labeling convention: PASS;
- Repository governance: source fixes PASS; delivery bookkeeping updated here;
- Audit compatibility: PASS in validation mode, with new rows typed
  `no_go`/`bounded_theorem`, all three target rows queue-visible, strict lint
  reporting zero errors, and all generated audit/status outputs restored to
  `origin/main` before commit.

Local review-loop disposition: `pass` for shipping the exact no-go and bounded
support artifacts. This is not an audit verdict and does not close the parent
operator identification.
