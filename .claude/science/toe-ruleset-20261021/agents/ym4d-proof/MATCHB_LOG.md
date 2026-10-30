# MATCHB author log

Task: execute `briefs_q/MATCHB/AUTHOR.md`, in the supplied YM4D folder.
Started 2026-10-30. This is an author research packet, not an audit or a
Yang–Mills construction. Only MATCHB.md, MATCHB_LOG.md and checks/matchb_*
may be created/edited. Existing inputs are read-only. No commits.

## Source and process record

Read the author brief, PROCESS_LIGHT.md, HANDOFF.md current assignments,
REFMATCH.md and REVIEW_REFMATCH.md, MIXSMALL.md, REALRGA.md, REALRGB.md,
JMBRA.md and LIB1.md. Large sources were read in numbered-range chunks.
The substantive source search used `rg -n -i` for interacting cells,
conditional references, finite-range dependence, marginalization and
reference cumulants across those files and RD3/RD4. This is a bounded
snapshot search, not a global novelty claim.

The supplied `repo` directory is a file snapshot: it has no `.git` or
`docs` directory. `git status` therefore fails with "not a git repository".
Historical commit IDs printed in input notes do not authenticate this
snapshot. Current source bytes will be identified by hashes.

The physics-loop skill and its discovery/status/delivery references were
inspected for applicability. Its full repository workflow cannot run in
this snapshot: the required skill-freshness document and repository
authority surfaces are absent. No freshness, primitive-registry, PR,
campaign or negative-packet certification is claimed. The user's more
specific author brief and PROCESS_LIGHT govern this bounded task; no
extra loop pack, branch, commit, audit or ledger is created. The local
no-go-discipline skill path is also absent. The final note confines its
diagnostics to explicit constructions and general-inference failures.

FR (fixed-domain/selector regularity), KR (finite-coupling remainder), and
TC (original-law charges and tails) remain named inputs. Their coordinator
work is not reproduced or extended to all histories by assumption.

## Research decisions

The construction uses the opened positive ancestry on exactly the
numerator's integration variables. The all-cut denominator can be lifted
to that space with dummy probability Haar variables; unequal hard supports
are never divided. Conditional block laws retain every incident factor.

Three meanings of locality are kept distinct: finite factor readers,
finite-range conditional specification, and independence at separation.
Only the last supplies the product factorization used in REFMATCH.
Absorbing a strong action into a reference does not establish it.

The nonproduct replacement for the connected logarithm uses a gas of
joint-cumulant types. Compatibility is disjointness of atom labels, not
disjointness of their spatial supports. Its quantitative input is an
explicit full-reader cumulant sum; production and regeneration of that
sum for the actual law remain separate obligations.

## Checks and review

`checks/matchb_criteria.md` was created before the diagnostic script.
Execution, source hashes, independent review and any fixes will be recorded
below. Written proofs carry mathematical assertions; a finite check or
review verdict cannot establish the open history-uniform estimates.

### Numerical execution

The first invocation used `nice -n 10`, Python `-B`, six thread variables
equal to one and an exclusive advisory lock. Its observed niceness was
20, load averages were approximately 1.97/1.76/2.01, and peak RSS was
21,757,952 bytes. It stopped before mathematics because `psutil` was
unavailable. The original runner, result, stdout and stderr are preserved
as `checks/matchb_attempt1_*`; the receipt has status NOT RUN and no checks.

The runner was then repaired to measure memory using native macOS
`memory_pressure`, `vm_stat` and `sysctl`, retaining the original 30%
threshold. The available-memory measure is conservative: free minus
speculative plus inactive pages, with no credit for compressed or
purgeable pages. The criteria and mathematical diagnostics were unchanged.
The second invocation again observed niceness 20 and all thread settings
one. Load averages were approximately 2.02/1.94/2.05 and peak RSS was
22,167,552 bytes. System-wide memory-pressure free percentage was 50%,
but the registered available-memory measure was 24.612236%, below 30%.
It stopped before every mathematical diagnostic. No threshold was relaxed.

The current `checks/matchb_result.json` and matching stdout therefore say
**NOT RUN**, with an empty check list. There is no numerical PASS, no
executed omission-mutation result, and no empirical validation of an
actual gauge estimate. The failure is a resource preflight, not a failed
mathematical assertion. The runner can be used later when every registered
resource condition is satisfied. No pools, memory-limit overrides or
additional interpreter packages were used.

### Provenance and fresh review

`checks/matchb_sources.json` identifies the current input bytes.
`checks/matchb_inventory_before.json` hashes all pre-existing files,
excluding only the new MATCHB author outputs. The inventory was captured
after the initial draft and guarded attempts, before any review repair;
all earlier writes in this task were confined to those excluded outputs.
This is metadata validation, not a numerical scientific check or Git
authentication.

A fresh-context subagent was launched for the hostile review expressly
required by PROCESS_LIGHT. It is same-family Codex review, not model-family
diversity or formal audit. It writes only `checks/matchb_review.md` because
the author brief's file restriction excludes `REVIEW_MATCHB.md`. The
reviewer's mathematical assessment is independent of the author's
conversation and is not allowed to rely on unexecuted diagnostics.

The first review is [checks/matchb_review.md](checks/matchb_review.md),
ending **VERDICT: HOLD** for two binding fixes. It independently accepted
the exact label-disjoint cumulant gas, its tree constant, the nonproduct
marginal identity and the regeneration diagnostics at their stated scope.
The candidate reviewed there has SHA256
`9f5fb403665e154c54427b2cfca25e2387357a2ea96b4706bb532a36352b7e54`
and is preserved as `checks/matchb_review_source_v1.md`.

- **B1 repaired:** distinguish `Z_C^full=F_ext Z_C^loc` from the incident
  normalizer `Z_C^loc=int q_C`. The incident-score bounds now apply to
  the local normalizer and conditional density. Full normalizers and full
  ratios retain the exterior factor, its original readers and its jets.
  MB8/MB9 and the regeneration budget use the same explicit convention.
- **B2 repaired:** require every comparison core H and H_G to be nonempty,
  connected and complete. A connected hull's actual size is paid in the
  support weights, comparison bill and full-root input sum.
- The review's additional clarity request is also applied: `sigma>=0`
  is explicit at the pinned comparison and cumulant-gas theorem.

The changes were applied directly, as PROCESS_LIGHT requires. There is
no commit because the brief forbids commits. The exact repair is
`checks/matchb_review_fix.diff`. The repaired source has SHA256
`40fc8888735639281dab191124bcacd866b3f5afaf53329d3ddf6ee481cc04d9`.
The same fresh reviewer was asked to confirm only the affected arguments
and their interactions with MB29, retaining its independent coverage of
the unchanged parts. The first HOLD report is preserved rather than
rewritten. Final disposition will be recorded after that confirmation.

Both diagnostic scripts parse as Python and every local Markdown link in
the draft resolves. This is static metadata/syntax validation only. No
mathematical diagnostic was run after the guard failure, and no numerical
claim is transferred from the draft to the repaired source.

### Final disposition

The affected-fix confirmation is
[checks/matchb_review_final.md](checks/matchb_review_final.md), ending
**VERDICT: LAND** for the stated partial and conditional results, with no
binding fixes remaining. It confirms the exact repaired source hash above,
the local/full normalizer convention through MB29, the paid connected
cores, and the nonnegative support rate. The first HOLD and its archived
source remain unchanged. This is same-family review, not audit ratification
or an actual-model GO.

The delivered result is the exact positive adapted reference on the
numerator variables, the pinned fixed-support calculus and local ratios,
the conditional RM7–RM12 replacement, the proved joint-cumulant gas
replacing RM13's factorization mechanism, and the exact regeneration map.
The actual history-uniform pinned/reference/cumulant budgets and their
same-constant regeneration are **OPEN**. The generic sign counterexamples
do not assert a failure of the actual gauge construction.

Final metadata validation is recorded in
[checks/matchb_validation.json](checks/matchb_validation.json). It checks
input preservation, the exact reviewed source identity, local links,
Python syntax and receipt hashes. All 4,013 pre-existing files remain
unchanged, and all new files are inside the author brief's permitted
paths. No Git checkout exists here and no commit was made. The numerical
status remains NOT RUN; static checks and independent written review are
not numerical verification.

The next scientific action is the actual bounded-core/separator
construction described at the end of MATCHB §8: produce and bound its
joint differentiated cumulant family on the same all-cut comparison,
then reproduce MB29 at the next scale. FR, KR and TC remain named inputs;
none has been extended beyond its proved scope by this lane.
