# Fixes, checks, re-review, and final reporting

Required before applying fixes, running post-fix checks, confirming corrected source, or issuing a final report. The named target and its flags remain controlling; every review eventually uses the Final Report requirements.

## Fix Policy

If `--no-fix` was passed, do not edit.

Otherwise apply the narrowest honest fix:

1. Fix verified code bugs, broken reproduction commands, stale runner names,
   false PASS checks, and code/prose mismatches.
2. Demote overclaimed status when the artifact supports only support/bounded
   language.
3. If a claimed proof or reduction terminates at a target-equivalent or
   stronger missing lemma, demote the headline to `open_gate`, exact support,
   or the strongest independently proved narrow lemma. Do not describe the
   reduction as near closure unless it contains a genuinely new mechanism for
   the terminal obligation.
4. Mark imported values explicitly; distinguish derived, conditional, fitted,
   measured, literature, boundary-condition, and insensitive nuisance inputs.
5. Add or repair paired runner/note references only when the artifact exists.
6. Make audit-system hygiene fixes only when they do not change the science:
   status-line tier labels, machine-local path removal, stale runner transcript
   refreshes, generated audit queue/ledger seeding, and discoverability wiring.
7. Rename ambiguous science shorthand to explicit repo vocabulary without
   changing the claim boundary. Examples: write `one-qubit operator algebra`
   (or equivalently `M_2(ℂ) ≅ Cl(3,0)`, `physical Cl(3) local algebra` as
   the real-algebra reading — all co-equal labels for the same retained
   algebra-isomorphism class), `Z^3 lattice`,
   `Koide Frobenius-equipartition condition`, or `Lie type A_1` instead of
   bare `A1` / `A2`.
8. Update `docs/repo/ACTIVE_REVIEW_QUEUE.md` for live unresolved findings.
9. Route detailed resolved packets to
   `docs/work_history/repo/review_feedback/` only when a long packet is needed.
10. When a PR is non-landable but salvageable, preserve only the durable
   note/runner content, make the claim boundary canonical, and land that source
   salvage through the current requested landing path. If the rejected branch
   contains substantial non-source packet material, use a clean temporary
   worktree for integration, but do not create or open a follow-up PR.

For any finding it covers, apply the cure stated in
`docs/ai_methodology/REVIEW_LOOP_PR_CONFORMANCE_SPEC.md`, so the same defect
is cured the same way in every slot instead of being renegotiated per PR.
Reviewer prompts and findings may cite its sections by number as shorthand
for the requirement — "conformance spec section 5, target-equivalent terminal
lemma" — but the authority is the skill, script, or vocabulary file that
section cites, and a finding must be justifiable from that authority. Where
the spec and its cited authority disagree, the cited authority wins and the
spec carries a defect: fix the PR to the authority and report the drift.

Skip:

- nits;
- suspected findings without evidence;
- ambiguous science gaps that need new derivation;
- attempts to paper over missing theorem steps with confident prose;
- repo-wide axiom additions, new theory terminology, or new foundational
  premises that lack explicit user approval;
- broad refactors unrelated to the finding.

## Smoketest

After fixes, run the smallest relevant checks:

- `python3 -m py_compile <changed .py files>` for changed Python files;
- changed paired runners directly when they are expected to be short;
- for changed math-bearing runners, independently verify formulas/constants
  before trusting PASS output: compare note equations to code line by line,
  check signs/factors/normalizations, run a second implementation or symbolic
  simplification when practical, and add finite edge-case or invariant checks
  when they would have caught the suspected class of error;
- inspect resource cost before executing practical changed runners within the
  actual owner-authorized time, memory and attempt limits. Preserve every
  timeout, failure and partial output. A timeout is operational evidence, not
  scientific falsification; retry or extend a limit only when authorized and
  justified by a concrete recovery need. Do not automatically rerun unchanged
  successful science or override a once-only run instruction;
- any reproduction commands named in changed notes when practical;
- publication/control-plane consistency checks by reading changed tables and
  nearby authority surfaces.
- full pipeline, strict lint, and changed-evidence validation at the combined
  [combined candidate stage](COMBINED_VALIDATION.md) when claim notes or governance/publication surfaces
  changed; this bullet does not require an additional per-unit full run.

If a runner is long, stochastic, or requires unavailable data, do not fake the
check. Report it as not run with the reason.

## Re-Review Tracking

Do not routinely repeat clean reviews of unchanged files. Reopen a prior
conclusion when a fix changes its relevant assumptions or interactions.

After each fix pass:

1. Identify files modified by the fix pass.
2. If committing is allowed, create one iteration commit:
   `fix: address physics review findings (iteration N)`.
3. Set `files_to_review` to the files modified by the fix pass.
4. Inspect needed interacting files, including unchanged context, through
   imports, runner/note pairs, canonical harness rows, publication tables, and
   explicit cross-links. Record the affected prior conclusion and reason for
   reopening it. A newly necessary edit expands the recorded changed-file set
   and receives review; it is not covered by an earlier PASS.
5. Loop until clean, no files changed, or max iterations reached.

## Final Report

Report:

- iterations run;
- files reviewed;
- total findings, fixed findings, skipped findings;
- import/support inventory summary;
- final claim-strength disposition;
- audit-compatibility status and proposed claim IDs needing independent audit;
- commits created;
- unit membership and constituent disposition map, train departure reason,
  combined-gate result or identical base/tree receipt reused, landed main SHA,
  and units returned to fallback;
- distinct source reviewed, reviewer/runner time, full pipeline count,
  integration retries, and scientific findings per unit;
- checks run and checks skipped;
- remaining issues with disposition;
- recommendation: `PASS`, `PASS WITH BOUNDED CLAIMS`, or `NEEDS MANUAL SCIENCE`.

Do not claim Nature readiness. Say whether the branch meets this repo's
Nature-grade retention bar or exactly what remains open.
