# REALRGA author log and current checkpoint

Task: execute `briefs_q/REALRGA/AUTHOR.md`, producing a real-derivative RG
induction specification. Only `REALRGA.md`, this log, and `checks/realrga_*`
may be written. No commits, PR, audit, ledger, axiom or prompt edits.

Source checkout: `cd67e1c9e6bbed8b92fee069de66ef0b25486316`, branch
`claude/q-L1`. Initial status contained only the untracked REALRGA brief.
The explicit author brief and PROCESS_LIGHT govern this bounded task;
the lane-builder skill supplies packaging and claim boundaries. The
physics-loop and exercise entry points were inspected for applicability;
no campaign, exercise fan-out, or backlog process was started.

The initial `git fetch origin ai/execution --quiet` returned exit 0 and
its planning AGENTS was read at `56c5c0ab64f532c5784e895b2f9aa6894fa334e0`.
A later `git fetch origin main --quiet` failed with `Operation not permitted`
opening the worktree FETCH_HEAD. The available origin/main is
`01589af3faf806b736c42dc2f3bd625e9edead9f`; it lacks these lane paths.
Thus this packet uses the user-specified checkout as candidate evidence;
it does not certify that the supplied lane claims are current-main or
audited results. Workflow and lane-builder/freshness files compared equal
to that available main. No working-tree refresh was attempted.

## Current checkpoint

- Target/domain: finite compatible periodic SU(N), N>=2, odd L>=3;
  actual Wilson weight and Decision-4 normalized soft kernels, fixed
  original sources, all complete histories and their genuine readers.
- Closest result: REALONLY section 7 specifies real mixed bounds and the
  conditional graph argument, but no derivative-stable RG contract.
- Construction: real Lie-direction jets, original-source jets, explicit
  multiplicity-aware regulators, derivative-inclusive matched integration,
  a real Mayer expansion, extraction and same-order invariant budgets.
- Success criterion: precise conditional contract and proofs of its
  elementary replacements, with every actual-model estimate marked OPEN;
  complete carry-over and consumer maps; fresh hostile review.
- Open obligations: matched joint jet prices, differentiated normalizers
  and selectors, real locality construction, extracted continuation,
  all-order separated hierarchy, matching and symmetry defect bounds.
- Pitfalls preserved: pointwise positivity is not derivative control;
  fixed-order jets are not an all-order hierarchy; overlapping regulators
  do not reduce to a single regulator on the union; fixed finite-order
  field derivatives do not replace arbitrarily many decoupling derivatives.
- Author contract and proofs complete. Initial frozen note SHA256
  `007cf62c59bb76ec7079ed6e68d8e6a4ee1d02b92d3b0f5e45b673329fd059b2`;
  preserved in `checks/realrga_review_source_v1.md`.
- Fresh review requested under PROCESS_LIGHT, using the physics-claim-reviewer
  skill. It is a separate same-family Codex context, with no model/effort
  override, not cross-family review or audit.
- Reviewer identified a missing explicit inequality in the abstract
  recurrence: the per-step s, eta and e must be nonnegative and bounded by
  their starred envelopes; lambda must be nonnegative. Added those and
  M_q>0. This repairs the conditional proof, not an actual gauge estimate.
- Added explicit carry-over rows for RD3 D14–D16 and JMBRA A19–A23b.
  Complete author fix read at `checks/realrga_author_fixes_v2.diff`.
  Corrected note SHA256
  `bdd97cc9fbbd822938fe6c921936fcb09f2957059ef71b8b46c15a3aee706b6d`.
- A subsequent author/reviewer domain check made the real evaluation
  domain open, with uniform bounds there and declared closed inner sets.
  Uniform supported-series convergence now explicitly gives C^(p,q)
  regularity on compact subsets, without an unsupported extension across
  a closed-set boundary. The reviewer also requested the explicit
  definition J_(j,B)=partial_B Phi_j(0;U_j), under the unperturbed chain.
  Both clarifications are in the cumulative
  [v3 correction](checks/realrga_author_fixes_v3.diff), read in full.
  Current note SHA256
  `e9a08eed121b1e05b792afdc4904f0872e31ea0f9e0f7899ccb7edc09492bbed`.
- Fresh reviewer confirmation is complete: **VERDICT: LAND** for the
  scoped contract note at the current hash, with all identified corrections
  resolved. Actual gauge-model realization remains OPEN. The task is
  complete as a contract specification; no no-go or exhaustion claim.
- Next research decision, outside this completed author task: construct
  RGA14–RGA16 for a bounded mixed core on the actual all-cut reference,
  with differentiated normalizers and all four original-source labels.

Source identities and literature locators are in
[realrga_sources.json](checks/realrga_sources.json); its note hash is the
initial review freeze, with the correction tracked separately above.
All 23 source files matched their initial identities on the author check;
all tracked inputs matched HEAD. The untracked owner brief is hashed too.

## Read coverage and method

The complete author note was read in three segments before review, and the
complete subsequent correction diff was read before affected review. Legacy
sources were read using headings and offsets. Unneeded historical no-go
packets and old runner logs were not treated as live instructions. Large
batched outputs that truncated were not counted as completed verification;
the affected argument passages needed for this note were read in smaller
ranges. This is not a complete independent rereview of all legacy lanes.

Principal source coverage (line positions in the pinned input snapshot):

- REALONLY 1–592: consumer table, real estimates and proposed real LF contract.
- CHARGE 1–557: original charge, real all-cut cap, flux/saddle/sector algebra,
  exact continuation, joint/window/creation obligations.
- RD3 1–591: histories, references, finite germ, hard species, integrated
  comparisons, hole norm, literal factors and remaining induction.
- RD4 25–277, 336–461, 521–669: domain, conditional cells, matched real
  ratios, budgets, full support and induction/consumer factors.
- JMBRA 24–703: replacement, reader elimination, grouping/tree bounds,
  weighted tails, survival/reference comparison, finite germ and all returns.
- JMBRB 84–726: transfer, mass, gaps, geometry, renewal, seams, mixed gas,
  extraction and invariant budgets. Its old comparative absence of JMBRA
  is historical and was not used.
- RENEW 79–266, 304–337, 398–560: linear and rough-orbit scope, finite cap,
  window/group bounds and exact open construction.
- LFPRICE 76–453, 470–711: units, charge, seam, geometry, split, graph
  estimate, cutoff arithmetic, kernel-gap and LF-JMBR interfaces.
- LIB1 43–132, 164–439, 696–781: graph definition, resummation/counting,
  full versus active norm and remaining scope. Its B1 repair note and
  the later affected review's identity/findings were also inspected;
  historical pending-review wording is not mistaken for the later outcome.
- STEP55 CX/NZ-ret and errata, especially 483–543 and 656–698: complex
  decoupling derivatives and restored normalization factors.
- WITNESS 505–594; K4MATCH 149–183 and 305–360; TQ2 284–390;
  N5B 153–214 and 475–526: exact requested consumer interfaces.

Primary literature was inspected online for method attribution. BBS
1907.05474v2 Definition 7.1.2/(7.1.9), Chapter 7's real Taylor/product
discussion and Appendix A.2's alternative circle-product definition;
Brydges–Slade 1403.7244v2 Definition 3.3, Proposition 3.7 and its proof
passage in section 5.1; Dimock's two primary abstracts for scalar d=3 scope.
No paper/PDF was added to the repository, no external theorem substitutes
for the written proofs, and no memory-only [m] claim is load-bearing.

## Numerical and mechanical evidence

The exact rational diagnostic criteria were written before the implementation.
The numerical process was invoked once, with `nice -n 10`, Python -B, and
six BLAS/OpenMP-related thread variables set to 1. It exited 2 at preflight:
`nice: setpriority: Operation not permitted`; observed niceness was 0.
It performed **zero mathematical checks**. Status is NOT RUN, not PASS.
The observed RSS was 22,298,624 bytes, free memory 39%, and loads
2.87255859375 / 3.02490234375 / 3.0205078125. The other resource limits
passed, but this did not waive the niceness requirement. No retry bypassed it.

Full evidence: [criteria](checks/realrga_criteria.md),
[script](checks/realrga_check.py), [result](checks/realrga_result.json),
[stdout](checks/realrga_stdout.json), [stderr](checks/realrga_stderr.txt).
The checker was statically inspected; its unexecuted diagnostics are not
used as proof of the contract. The principal evidence is the written
derivation and fresh mathematical review.

[Document/source validation](checks/realrga_validation.json) checked local
links, table structure and unchanged source hashes. Its first table scanner
misclassified three standalone absolute-value equations as table rows;
that bookkeeping failure is retained in
[the initial receipt](checks/realrga_validation_initial.json). Narrowing the
scanner to actual table rows resolved it without a mathematical change.
`git diff --check` returned zero; the new note was inspected separately
because it is untracked. No existing editable prompt file was changed,
and no platform instruction was modified.

The adjacent `briefs_q/REALRGA/REVIEW.md` was also inspected. Its substantive
review requirements were already covered by the fresh-review dispatch.
Its suggested `REVIEW_REALRGA.md` destination is outside the explicitly
invoked AUTHOR brief's allowed output paths, so the review uses the allowed
`checks/realrga_review.md` instead. No permission question or out-of-scope
write was needed.

The reproducible nonnumerical validator is
[realrga_validate.py](checks/realrga_validate.py), invoked with
`python3 -B checks/realrga_validate.py` from this folder. It checks inputs,
links, tables, output-path scope and the link between the unchanged
criteria/checker and the saved refusal; it does not execute the diagnostic
calculations. This use of deterministic inventory/hashing is distinct
from the blocked numerical run.

## Final independent review and disposition

[Fresh hostile review](checks/realrga_review.md) binds note SHA256
`e9a08eed121b1e05b792afdc4904f0872e31ea0f9e0f7899ccb7edc09492bbed` and
ends `VERDICT: LAND`. Its SHA256 is
`7b4488f600b2b73e7a93290280af87a229f1278623c7a2414e297d1792c3047b`.
The author read the complete report. It confirms the recurrence hypotheses,
open-domain regularity, zero-source jet definitions and source-map additions.
Its own derivations examine ordered Leibniz calculus, normalized quotient
derivatives, joint regulators, both tree estimates, extraction, recurrence
arithmetic, four-source normalization and all-order consumer combinatorics.
Read coverage and remaining verification limits are explicit in the report.

This is same-family review in a fresh context, not cross-family or formal
audit. LAND means readiness of this conditional specification only; it is
not a git landing, an actual-model induction theorem or a retained status.
No mathematical numerical check ran. The author and reviewer agree that
matched local mixed jets, sector regularity, real localization, coherent
extracted continuation and the actual consumer modules remain OPEN.

Final file identities and the permitted-path/source checks are bound in
[the final receipt](checks/realrga_receipt.json). Only the requested note,
this log and `checks/realrga_*` were created. Existing files and editable
prompts are unchanged, no file was staged, and HEAD remains the supplied
revision. No commit, PR, audit or ledger mutation was performed.
