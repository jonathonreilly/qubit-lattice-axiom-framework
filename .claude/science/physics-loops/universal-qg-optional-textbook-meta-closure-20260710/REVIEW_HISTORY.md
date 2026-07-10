# Review History

## 2026-07-10 — iteration 1

- `CodeRunnerReviewer`: **RISK**. The runner checked that the `Z4` firewall
  sentence existed but an arbitrary source edit could add substantive content
  without necessarily failing that semantic guard.
- `PhysicsClaimReviewer`: **SUPPORT**. Correctly scoped as a meta predicate;
  no physics theorem or continuum grade is supported.
- `ImportSupportReviewer`: **CLEAN**. No measured, fitted, literature,
  observational, normalization, or physics-convention imports.
- `NatureRetentionReviewer`: **OPEN / not applicable to physics retention**.
  The finite predicate is exact support for metadata only.
- `NoGoDisciplineReviewer`: not applicable; rejected packaging routes are not
  scientific no-go claims.
- `LabelingConventionReviewer`: **PASS**. The row is already `meta`; no
  labeling content is presented as a bounded theorem.
- `RepoGovernanceReviewer`: **PASS after fix**. No authority edge or authored
  verdict; the independent audit lane remains sovereign.

Fix: SHA-pin the complete reviewed source note in the runner. Any source edit
now fails closed until source, runner, and cache are reviewed together.

## 2026-07-10 — iteration 2

- `PhysicsClaimReviewer`: **FIX**. Section 3 still used legacy phrases
  describing the external theorem stack and closure parent as already closed,
  which exceeded this row's declared zero-authority scope.

Fix: replace those phrases with status-neutral prohibitions against assigning
or changing the stack's status and against substituting for the substantive
claim row.

## 2026-07-10 — iteration 3

- `CodeRunnerReviewer`: **PASS**. Direct runner reports `PASS A=18 B=1`, and
  an independent implementation confirms the SHA, six labels, zero outbound
  markdown edges, and 12 guarded inbound-reference lines.
- `PhysicsClaimReviewer`: **SUPPORT**. Scope remains exactly the packaging
  invariant; the note explicitly disclaims grades for named physics rows.
- `ImportSupportReviewer`: **CLEAN**.
- `NatureRetentionReviewer`: **OPEN / not applicable to physics retention**.
- `NoGoDisciplineReviewer`: **NOT APPLICABLE**.
- `LabelingConventionReviewer`: **PASS**.
- `RepoGovernanceReviewer`: **PASS**.
- `Audit Compatibility`: **PASS**. Validation pipeline gives `claim_type:
  meta`, leaves the audit field unaudited, derives effective status `meta`,
  records `deps: []`, and attaches the fresh runner path and expected note
  hash, with no target audit-queue entry.
  Strict lint reports no errors; existing repository warnings/notices are
  unrelated.

Final local disposition: **pass**, with exact support limited to the finite
metadata predicate.
