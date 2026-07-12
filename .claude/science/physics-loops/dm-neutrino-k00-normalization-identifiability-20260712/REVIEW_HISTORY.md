# Review History

## Pre-review checkpoint

- Review-loop disposition: pending.
- Positive claim was demoted before review because exact countermodels expose
  two free normalization parameters.
- Required reviewers: code/runner, physics claim, import/support, Nature
  retention, no-go discipline, labeling convention, repo governance, and
  audit compatibility.
- Parallel subagents were not authorized for this task; reviewer lenses will
  be emulated locally and consolidated here.

## V1-V5 value gate

Recorded in `OPPORTUNITY_QUEUE.md`; disposition PASS for the non-churn scoped
no-go artifact.

## Review Results — Iteration 1

Original changed surface: target note, primary runner/cache, and loop pack.
Reviewer lenses were run locally because parallel subagents were not authorized.

- **Code / Runner: RISK.** Three findings: the target `K00` trace identity did
  not independently check the heavy bright matrix element; determinant-ratio
  equality did not explicitly exclude an absolute-value sign branch; approved
  primitive source scopes were inferred rather than checked and linked.
- **Physics Claim Boundary: NO-GO.** The narrow restricted-packet claim is
  supported; no framework-global wording found.
- **Imports / Support: CLEAN for the no-go; DISCLOSED for the positive
  endpoint.** W-map and W-source are explicit and independent.
- **Nature Retention: NO-GO candidate.** Independent audit is required.
- **No-Go Discipline: PASS.** N1-N8 completed with six attempted routes.
- **Labeling Convention: NOT APPLICABLE.** The claim is an algebraic
  identifiability theorem, not a naming convention.
- **Repo Governance: FIX.** Sibling pin sweep found the historical
  Record-invariance companion hard-pinned to withdrawn prose/hash/pass counts.
- **Audit Compatibility: pending pipeline.**

Fixes applied:

1. added the direct heavy bright-entry check beside the trace-dual check;
2. solved equality of squared determinant polynomials to exclude a hidden
   log-absolute sign branch;
3. linked and runtime-checked all approved primitive source scopes; and
4. re-authored the stale Record-invariance companion as historical/diagnostic
   evidence retirement with a synchronized 20-pass meta runner/cache.

## Review Results — Iteration 2

Re-reviewed only the target note/runner changes from iteration 1 and the newly
interacting companion note/runner/cache.

- **Code / Runner: PASS.** Primary `16/16`; companion `20/20`; leptogenesis
  projection sibling `10/10`; both changed caches SHA-fresh.
- **Physics Claim Boundary: NO-GO.** Exact finite-packet obstruction with a
  concrete falsifier; positive `K00 = 2` remains open.
- **Imports / Support: CLEAN / DISCLOSED.** No observation, fit, literature
  number, or normalization is consumed by the negative theorem.
- **Nature Retention: NO-GO.** Meets the repo's retention bar as an author-side
  no-go candidate, subject to independent audit.
- **No-Go Discipline: PASS.** No hidden wall or overbroad resolution found.
- **Labeling Convention: NOT APPLICABLE.**
- **Repo Governance: PASS.** No repo-wide authority or publication surface is
  changed; links are portable; sibling pins are green.
- **Audit Compatibility: PASS.** Validation pipeline ingested the target as
  `no_go`, the companion as `meta`, linked exactly the four approved premise
  nodes, queued the target, and strict lint reported zero errors. All generated
  audit/effective-status/front-door outputs were stripped afterward.

## Independent math check

An implementation separate from the runner used the matrix determinant lemma
with normalized bright vectors `u3` and `u2`:

`det(mI + x uu^T)/m^n = 1 + x/m`.

It independently returned `K00 = c tau_+` and reproduced the three witness
points `(tau_+,c,K00) = (1,1,1), (1,2,2), (1/2,2,1)`.

## Final disposition

- Iterations: 2
- Findings: 4
- Fixed: 4
- Skipped: 0
- Review-loop recommendation: `PASS`
- Independent audit required for claim ID
  `dm_neutrino_k00_bosonic_normalization_theorem_note_2026-04-15`.
