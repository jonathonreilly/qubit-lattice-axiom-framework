# Post-freeze PR densify — pass-1 full-read brief (2026-09-05 corpus)

You are a full-read triage seat for the SECOND densify wave: the 96
non-draft PRs opened after the 2026-08-31 freeze (mostly 2026-08-28 to
09-04 physics-loop blocks). Apply the frozen pass-1 rubric VERBATIM from:
/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad/pr_triage/RUBRIC.md (read it COMPLETELY first).

Context updates since that rubric was written (apply as KEEP-reason
extensions of its clause 1):
- the TOE alphabet-exclusion lane (toe-axiom-closure blocks 174+) and the
  pin-order/extended-alphabet work are LIVE (current campaign);
- the source-eta-ownership block series (blocks 02-42), the u1-Maxwell
  chain, the spin-half-cubic-ice chain, toe-light-maxwell, and
  toe-connection-dynamics block 229 are ACTIVE lanes of the last week -
  their chain TERMINALS and any uncarried decisive artifact are KEEP;
- "superseded by a later PR in the same series" applies ONLY when the
  later PR is in this corpus or already merged AND restates the result;
  a stacked ancestry PR whose theorem is NOT restated by its terminal is
  KEEP (the wave-1 precedent: closing would orphan unrestated theorems).

For each assigned PR read IN FULL: bodies/<N>.json then diffs/<N>.diff
(diff may be truncated at 180KB; note if so). Then append ONE line to your
verdicts file:
{"pr":N,"verdict":"KEEP|CLOSE|UNSURE","science":"1-3 sentence factual
record of what the PR claims/computes (for the ledger entry)","carrier":
"what carries the result if closed (terminal PR / landed block / memo /
'none - uncarried')","stack":"base branch if stacked","flags":{"forcing":
bool,"promotion_candidate":bool}}
Rules: science line is factual quotation/report, no authority vocabulary
of your own; bias CLOSE per the rubric but NEVER close-verdict an
uncarried theorem; UNSURE only when body+diff genuinely cannot tell.
Finish with {"read_done":"<seat>","count":N}. Write incrementally.
