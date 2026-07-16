# Review History

## Local review-loop passes

The user forbade subagents, so the required reviewer roles are run locally:

- Code/runner: exit semantics, cache agreement, independent formula check;
- Physics claim: one-particle/Fock types, units, contour scope, causal boundary;
- Import/support: `m`, `a_tau`, standard complex analysis, external rigidity
  context, and candidate LR composition;
- Nature-retention: hostile check against causal/conformal overclaim;
- No-go discipline: N1-N8 on the abstract-word timing/rate boundary;
- Repo governance: claim types, links, forbidden audit outputs, and vocabulary.

## Iteration 1 findings and fixes

- **Code/runner:** a forced missing-note probe exposed that the consumer tried
  to relativize an out-of-root path before returning its failure code. The
  path display is now total, and the same probe returns `1` without raising.
- **Physics:** an independent symbolic check found that the displayed identity
  for `Re sin^2(x+i y)` omitted the `cosh(2y)` factor. The note and runner now
  use the exact identity and the runner checks it numerically.
- **Governance:** the consumer markdown-linked a free-bilinear LR note even
  though it was explicitly non-load-bearing. It is now a code-formatted future
  candidate, not a declared dependency.
- **Overclaim:** "retained mathematical content" was narrowed to "bounded
  mathematical content" because this repair does not assign retained status.

## Iteration 2 disposition

- Code/runner: **PASS** — all three runners use integer return values and
  `SystemExit`; the forced failure probe returns nonzero.
- Physics claim: **OPEN / BOUNDED** — record timing is a no-go, the kernel result
  is fixed-mass one-particle contour support, and the consumer remains open.
- Assumptions/imports: **PASS** — `m > 0`, `a_tau > 0`, the complex-analysis
  input, and all absent causal bridges are explicit.
- Nature-retention: **OPEN** — no sharp cone, LR velocity, causal order, or
  conformal class is claimed.
- No-go discipline: **PASS** — N1-N8 are recorded in the claim certificate.
- Repo governance: **PASS** — claim typing, dependency scope, vocabulary, and
  forbidden audit-output checks are clean.
- Audit compatibility: **PASS** — the deterministic pipeline and strict lint
  pass in a disposable worktree; no verdict was produced or applied.

Recommendation: **PASS WITH BOUNDED CLAIMS**.

## Independent Sol xhigh review-loop iteration 3

- **Semantic bridge:** the consumer runner listed the independently judged
  free-bilinear LR candidate among required source-packet files, so the
  supposedly non-load-bearing pointer still affected PASS. The candidate is
  now excluded from the required packet, and the runner instead checks that it
  remains code-formatted context rather than a citation-graph dependency.
- **Pack consistency:** `STATE.yaml` now records the actual fresh
  `origin/main` merge base used by PR #5422.
- **Independent math:** symbolic reduction confirms the exact
  `Re sin^2(x+i y)` identity; high-precision contour integration agrees after
  the one-coordinate shift; finite Fock enumeration confirms the vacuum and
  multiparticle spectrum split; and `-log(exp(-2E))/(2a_tau)=E/a_tau`.
