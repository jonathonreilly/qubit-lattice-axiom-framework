# PR #5995 Salvage Review Findings — Iteration 2

Review scope frozen before this file was created: the aggregate delta from the
stacked base `3a01b7c0f7cc180cf043c3d38416cdce0c4b9a5c` to salvage commit
`b472df1c1b4f03c63a60c97ff5653764fd3f084f`, comprising exactly seven added
package files (one note, two runners, two receipts, and two runner caches).
Pre-existing `RL_*PR5995*` reviewer artifacts and this findings file are
excluded from the review set. The worktree was initially dirty only with those
untracked reviewer artifacts.

This is a fresh combined review under the CodeRunnerReviewer,
PhysicsClaimReviewer, ProofObligationReviewer, ImportSupportReviewer,
NatureRetentionReviewer, NoGoDisciplineReviewer, LabelingConventionReviewer,
RepoGovernanceReviewer, and AuditCompatibilityReviewer lenses. Findings and
verification records are appended incrementally; the verdict block is reserved
for the final write.

## Scope and freshness record

- Review base: `origin/physics-loop/toe-time-blockAC1-20260802`, merge base
  `3a01b7c0f7cc180cf043c3d38416cdce0c4b9a5c`.
- The review-loop skill was refreshed against `origin/main` at
  `9b8207504c`; the current repo copy differs from the installed copy and is the
  governing version for this review.
- GitHub's remote PR head remains the untouched rejected package at
  `867aff0edc`; the local salvage commit is deliberately recoverable without
  overwriting that remote head. The scientific review target is the final
  seven-file aggregate delta at local `HEAD`.

## Incremental verification log

- Both changed Python files compile under Python 3 with bytecode redirected
  outside the worktree.
- Fresh execution of the primary reports `TOTAL: PASS=31 FAIL=0` and exit 0.
  Fresh execution of the independent checker immediately afterward reports
  `TOTAL: PASS=25 FAIL=0` and exit 0.
- Both receipt SHA-256 values are unchanged by the cold rerun
  (`13011f85315f5e80d6db620419f0ea9acf374d56129f6082fafeedbe6cc1bc13`
  primary; `b22b2c2706ab31c361f0c96dce75d42a4caed9297fce837c486bf426b5e76914`
  checker), confirming the no-timestamp deterministic-receipt claim. The two
  committed cache hashes also remain unchanged.

## Findings (incremental)

### S1 — BUG — CodeRunnerReviewer — receipt cross-check is not fail-closed for every recomputed unit

The checker correctly rejects an ordinary one-byte receipt tamper: changing
the primary receipt's unit-6 `value_at_3` from `2/27` to `999/1` without
rewriting its digest produces two failed checks and exit 1. It does not,
however, enforce its stronger stated contract that the primary receipt's
load-bearing values for every unit equal the independent recomputation.
`check_primary_receipt()` compares only selected receipt fields
([`scripts/salvaged_exact_algebra_independent_check_2026_08_08.py`](scripts/salvaged_exact_algebra_independent_check_2026_08_08.py),
lines 581–604). In an isolated copy I changed unit 1's first exact ledger trace
from `0/1` to `999/1`, recomputed the receipt's public self-digest by the same
documented serialization, and reran the checker. Every one of its 25 checks
still reported PASS and it exited 0, even though the independently recomputed
Reynolds result says that ledger trace is zero.

This contradicts the checker docstring's statements that the receipt's
load-bearing values “must equal this checker's own recomputation” (lines
29–32), that every unit is independently tied back to the primary (lines
5–27), and the note's “verifies the primary receipt fail-closed” description
([`docs/EXACT_ALGEBRA_SALVAGE_BOUNDED_SUPPORT_NOTE_2026-08-08.md`](docs/EXACT_ALGEBRA_SALVAGE_BOUNDED_SUPPORT_NOTE_2026-08-08.md),
lines 31–33). The same gap leaves unit 5 entirely absent from `cross_ok`, and
checks only census metadata rather than the substantive unit-2 and unit-7
receipt values. The independent mathematics can still be sound, but the
receipt-verification claim is false. Fix by constructing a canonical expected
result record from all seven independent routes and comparing every
load-bearing primary field (or narrowing the prose to an explicit enumerated
subset), then include a rehashed semantic-tamper regression that must exit 1.

## Independent mathematical verification record

The following checks do not rely on either runner's PASS banner. They compare
the note, primary, and checker formula-by-formula and supply a direct
derivation where the executable checks are finite probes.

1. **Trace-free/conformal split — CLOSED.** With `P = J/3` and `Q = I-P`,
   `J^2=3J` gives `P^2=P`, hence `Q^2=Q`, `PQ=QP=0`, and `P+Q=I` exactly.
   `P(v)=(tr(v)/3)1`, so `tr(Qv)=0`; if `v=u+c1` with `tr(u)=0`, tracing gives
   the unique `c=tr(v)/3`. For `(-2w,w,w)`, the trace is identically zero.
   Finally `G_sigma(v)-v=(sigma-1)P(v)`, so for `sigma != 1` its fixed space is
   exactly `ker P`, the trace-free plane. This matches note lines 64–77,
   primary lines 163–227, and the checker's independent Reynolds average
   `(I+C+C^2)/3=J/3` at lines 126–166.

2. **Affine residual — CLOSED.** Direct expansion gives
   `D[tau0]+(1+t)D[tau1]+(1-t)D[tau2]-D[d] = A+tB`, with exactly the note's
   `A` and `B`; summing the three raw-ledger entries gives `A` componentwise.
   The configuration count is `6*6^3=1296`. This matches note lines 84–98,
   primary lines 240–295, and the independent two-point reconstruction
   `A'=r(0)`, `B'=r(1)-r(0)` plus fresh probes at checker lines 179–218.

3. **`C_3` permutation module — CLOSED.** Solving `Cv=v` gives the invariant
   line `Q(1,1,1)`. The sum-zero complement is invariant and the displayed
   basis yields `[[0,-1],[1,-1]]`, characteristic polynomial
   `x^2+x+1`. Its only possible rational roots `+/-1` fail, and discriminant
   `-3` gives no real eigenline, so it is irreducible over both `Q` and `R`.
   Over `C`, `x^3-1` has three distinct roots and the permutation character
   has multiplicities `(1,1,1)`. This matches note lines 105–117 and primary
   lines 309–362. Checker lines 237–273 independently establish the complex
   multiplicities and rational Galois fusion; the real irreducibility is not
   separately checked there, but the direct negative-discriminant derivation
   above closes it.

4. **Five forms, families, and fixed-locus sum — CLOSED at the stated
   scopes.** Substituting `(w0,w1)=(1,n-1)` turns each displayed form into
   `(n-1)/n^2` identically. Pairwise cross-multiplication of the three families
   gives, after excluding the stated integer domain's `N=1`, factors whose
   only integer root `N>=2` is `N=3`; the note narrows its executable
   separation statement to `2..200`, where the values and the `N=4` witness
   are correct. For `z=e^{2 pi i k/N}`,
   `(1-z)(1-z^{-1})=4 sin^2(pi k/N)`; the standard logarithmic-derivative
   identity `sum_{k=1}^{N-1} csc^2(pi k/N)=(N^2-1)/3` gives the claimed sum
   `(N^2-1)/12`, hence its `/N` normalization. The primary quotient-ring trace
   (lines 383–463) and checker Laplacian pseudoinverse trace (lines 302–383)
   are genuinely different exact finite implementations of that identity.

5. **Screened origin step — CLOSED.** Solving
   `6G1-(6+m)G0=-1` gives `G1=((6+m)G0-1)/6` and therefore
   `G0-G1=(1-mG0)/6`; subtracting `1/6` gives `-mG0/6`. Thus the step is
   `1/6` iff `mG0=0`, and for `G0>0` iff `m=0`. This matches note lines
   155–163, primary lines 469–501, and the independent bivariate dictionary
   algebra at checker lines 409–436.

6. **Projector-ratio witness — CLOSED.** For `Qp=I-J/n`, every diagonal is
   `1-1/n=(n-1)/n`, while `totalsum(J)=n^2`; their ratio is
   `(n-1)/n^3`, giving `2/27` at `n=3`. The rival `/n` reader gives
   `(n-1)/n^2`, so the note correctly frames the first expression as
   reachability rather than selection. This matches note lines 171–183,
   primary lines 507–536, and the checker's equal-diagonal plus trace route at
   lines 442–459.

7. **Pointer-cycle identity — CLOSED.** Every simple cycle through `S` enters
   and leaves through distinct neighbours `a,b`; deleting `S` leaves an
   `a`–`b` path, so the cycle length is at least `2+dist_{G-S}(a,b)`. A
   shortest such path is simple and adjoining the two `S` edges attains the
   bound. This also proves the existence iff. The primary's simple-cycle DFS
   versus neighbour-pair BFS exhausts all `2^15=32768` six-vertex graphs
   (lines 542–631); the checker compares an edge-removal cycle computation to
   the formula on all `2^10=1024` five-vertex graphs and 200 deterministic
   eight-vertex samples (lines 465–552). The proof, rather than either finite
   census, establishes the unrestricted finite-simple-graph statement.

ProofObligationReviewer result for the seven stipulated targets is `CLOSED`.
No target-equivalent physical bridge, selector, or derivation claim remains in
those targets.

### S2 — AUDIT_COMPATIBILITY — AuditCompatibilityReviewer — the independent checker is absent from the audit packet

On a current-`origin/main` integration of exactly these seven files, the
citation graph seeds the intended claim
`exact_algebra_salvage_bounded_support_note_2026-08-08` with
`claim_type: bounded_theorem`, `audit_status: unaudited`, `deps: []`, and the
primary runner path. Its `helper_runner_paths` is empty. This is expected from
the current parser: `Runners:` selects the first script as primary, while
helper paths are obtained from transitive imports or the explicit sibling map
([`docs/audit/scripts/build_citation_graph.py`](docs/audit/scripts/build_citation_graph.py),
lines 682–730). The independent checker intentionally does not import the
primary, and this new claim has no entry in that explicit map.

Consequently the restricted independent-audit packet will not include the
second runner whose different routes and receipt checks are presented as part
of the package's evidence. The local changed-evidence gate still reports
`checked=1 failures=0`, so it does not catch this omission. Register
`scripts/salvaged_exact_algebra_independent_check_2026_08_08.py` as an
explicit packet helper for this claim (or use another supported
machine-readable helper mechanism) and rerun the pipeline. Do not make the
checker import the primary merely to obtain discovery; that would weaken the
claimed implementation independence.

### S3 — AUDIT_COMPATIBILITY — RepoGovernanceReviewer / AuditCompatibilityReviewer — citation-manifest acknowledgment is missing and the note misstates row seeding

The aggregate salvage delta contains only the seven package files. Adding the
new claim note changes the current-main citation graph from 4649 to 4650 nodes;
`build_citation_graph.py` plus `write_citation_graph_manifest.py` produces a
real `docs/audit/data/citation_graph_manifest.json` delta adding
`exact_algebra_salvage_bounded_support_note_2026-08-08` with out-degree zero.
The review-loop's proactive stage-18 gate requires that acknowledgment to
co-land, but it is absent from this branch.

The same validation also shows that the note necessarily seeds its own
ordinary unaudited bounded-theorem row. Thus “This note requests no audit
rows” and especially “it does not seed audit rows”
([`docs/EXACT_ALGEBRA_SALVAGE_BOUNDED_SUPPORT_NOTE_2026-08-08.md`](docs/EXACT_ALGEBRA_SALVAGE_BOUNDED_SUPPORT_NOTE_2026-08-08.md),
lines 295–300) are too broad. The honest distinction is that it requests no
extra dispatch/re-audit rows and authors no verdict; its own claim row is
pipeline-seeded and remains `unaudited` for independent review.

Validation details: the current-main integration's changed-evidence gate
passes the one seeded row, and `audit_lint.py --strict` reports no errors. The
full pipeline reaches stale-audit restoration and then stops on current
`origin/main`'s pre-existing dependency-policy epoch-manifest mismatch; none
of these seven files touches that manifest or any governed policy source, so
that unrelated baseline failure is recorded but not attributed to this
package.

### S4 — REPO_GOVERNANCE — RepoGovernanceReviewer — small source-boundary and review-record corrections remain

The scientific boundaries are honest, but four mechanical statements should
be corrected before the note becomes a durable repo-facing source:

- The title and status make the audit row's scientific title a branch process
  description (“salvage of the rejected route-sweep package” and
  “review-loop salvage pass on PR #5995”; note lines 1 and 9–11). The native
  claim title should be simply the seven exact stipulated algebraic results;
  PR/review provenance can remain in the clearly historical Review record.
- “The runners read no repo files” (lines 22–25) is literally false for the
  independent checker, which reads the primary receipt at checker lines
  45–46 and 558–568 and declares it in its own receipt `inputs`. Say that the
  primary has no file inputs and the checker has exactly one non-science input:
  the primary receipt.
- The Review record says the exact algebra from Cycles 872, 876, 895, and 900
  survives as units “1, 2, 4, 5” (note lines 282–288). Unit 4 is Cycle 899;
  the listed source group maps to units 1, 2, and 5. This is a factual
  cross-reference typo.
- “This branch deletes” and “does not seed audit rows” (lines 212–214 and
  298–300) are branch-local/current-state statements that become stale on
  landing. Restate the first as historical salvage provenance and the second
  as “authors no audit verdict or extra dispatch request,” consistent with S3.
- The controlled-vocabulary salvage-note rule asks for a stable recovery path
  for the failed wrapper. “Recoverable on the PR head branch” (lines 212–214)
  names neither the branch nor immutable head `867aff0edc`; at minimum pin
  that recovery handle explicitly (and use the canonical
  `archive_unlanded/<cluster-tag>/` path if the wrapper is archived in-repo).

Apart from those points, the Review record covers every original material
finding: F1–F13 and F15 are represented in the dropped inventory, while F14
is the stated salvage basis. It does not reassert any of the rejected physical
bridges, selector conclusions, terminal/no-go conclusions, fitted comparator,
or measured mechanism law.

## Hygiene and dropped-content sweep

- Exact-name grep of every path and basename deleted by salvage commit
  `b472df1c1b` against the seven final files returns zero references; there are
  no dangling links to the deleted package.
- All six markdown links in the note resolve to the two present scripts, two
  present receipts, and two present caches. There are no absolute local-path
  markdown targets.
- A targeted scan for the prior route-sweep, type-gap/new-primitive,
  Record-weight, positive-selector, fitted/empirical, and measured loop-law
  language finds it only in explicit `Not established`, `dropped`, or
  historical-review sentences. The executable surfaces and receipt roles
  contain only the seven exact stipulated results and bounded-support
  disclaimers.
- `scripts/vocab_lint.py --fix` on all seven files in the isolated
  current-main integration reports zero violations and makes no edits;
  `git diff --check` is clean.

## Final classification summary

- Files reviewed: all seven files in the frozen aggregate salvage delta.
- Findings: four material findings (`BUG` 1, `AUDIT_COMPATIBILITY` 2,
  `REPO_GOVERNANCE` 1); fixed in this review: 0; skipped: 0. This was a
  review/report request, so no package source was edited.
- Code and mathematics: both runners compile and reproduce their committed
  31/31 and 25/25 outputs; all seven stipulated theorem targets are
  independently `CLOSED`. The semantic rehash-tamper test in S1 prevents a
  clean Code/Runner verdict until repaired.
- Import/support inventory: all seven claims are `zero-input structural` on
  in-file stipulated definitions. There are no axiom/primitive dependencies,
  measured/fitted/literature values, normalizations imported from another
  note, or physical identification bridges. The checker's primary receipt is
  an execution-evidence input, not a science import, and must be described as
  such.
- Claim strength: bounded exact support only. This package does not meet or
  claim the repo's retained/Nature-grade bar; it is an honest
  `bounded_theorem` candidate for later independent audit after the four
  narrow repairs.
- No-Go Discipline: not applicable. The `Not established` boundaries and the
  historical account of rejected no-go claims do not assert a new negative
  theorem, named-wall bounded result, or route foreclosure.
- Labeling: pass. `C_3` is the standard cyclic group, and `A`, `B`, `G0`,
  `G1`, and `Qp` are local mathematical variables rather than bare workstream
  names. The process-framed title is instead handled as repo governance in S4.
- Audit readiness: the proposed claim id is
  `exact_algebra_salvage_bounded_support_note_2026-08-08`; it must remain
  `unaudited` for the independent audit worker. Current readiness is `FIX`
  because its checker is not packet-visible and its citation-manifest
  acknowledgment is absent. No audit verdict was authored or applied.
- Review-branch commits created: none. The isolated current-main validation
  commit and generated pipeline files are scratch only and are not part of the
  reviewed branch or proposed landing set.
- Required confirmation round: after S1–S4 are repaired, re-review only the
  changed note/checker plus the helper-registration and citation-manifest
  interaction surfaces; rerun both runners, both tamper variants, the
  current-main pipeline/readiness gate, strict lint, and `git diff --check`.

## Review Results (Iteration 2)
### Code / Runner: FAIL
### Physics Claim Boundary: BOUNDED
### Proof Obligations: CLOSED
### Imports / Support: CLEAN
### Nature Retention: BOUNDED
### No-Go Discipline: NOT APPLICABLE
### Labeling Convention: PASS
### Repo Governance: FIX
### Audit Compatibility: FIX
### Methodology Skill: SKIPPED
### DISPOSITION: FIX_THEN_PROCEED
