# PR #5995 Salvage Confirmation Findings — Iteration 3

Confirmation scope: fix commit
`5a5fd4035f42abb02a834ab343cde1402b8b5b6e` and the eight files in
`RL_FIXDIFF2_PR5995.txt`. Pre-existing untracked `RL_*PR5995*` reviewer
artifacts were excluded. No package source was edited during this round.

The review-loop skill was refreshed against `origin/main` at
`12e25af462`; that copy is newer than the installed copy and governs this
confirmation. The applicable lenses were CodeRunnerReviewer,
PhysicsClaimReviewer, ProofObligationReviewer, ImportSupportReviewer,
NatureRetentionReviewer, RepoGovernanceReviewer, and
AuditCompatibilityReviewer. No-Go Discipline and Labeling Convention remain
not applicable/pass respectively for this exact bounded-support package.

## S1 — FIXED

The checker now constructs a canonical expected primary payload from all seven
independent routes and compares the primary payload wholesale after removing
only its self-digest. The new independent six-vertex census visits all 32768
labelled graphs and obtains 24838 graphs with a cycle through the pointer,
matching the primary's independently implemented census.

Cold execution in an isolated archive reproduced:

- primary: `TOTAL: PASS=31 FAIL=0`, exit 0;
- independent checker: `TOTAL: PASS=27 FAIL=0`, exit 0;
- primary receipt SHA-256:
  `096fa90a149556a011cce8da12a59e4e2a39ddf1678e3058421977a6c9ae9fba`;
- checker receipt SHA-256:
  `ffb70ad1686bda4415942a427b4b6bc68c4e9a83bd6a89da42b441a823e8a7e3`.

Both regenerated receipts were byte-identical to the committed receipts. I
also reran the two tamper scenarios externally, rather than relying on the
checker's in-memory regression banners:

- changing unit 1's first ledger trace to `999/1` without rehashing made the
  checker exit 1; both digest and full-payload gates failed;
- making the same semantic change and recomputing the documented self-digest
  made the digest gate pass but the wholesale payload comparison fail, and the
  checker exited 1.

This closes the exact rehashed-semantic-tamper exploit from S1.

## S2 — NOT_FIXED

The packet-visibility part is fixed. A cold citation-graph build seeds
`exact_algebra_salvage_bounded_support_note_2026-08-08` with:

- primary runner
  `scripts/salvaged_exact_algebra_2026_08_08.py`;
- helper runner
  `scripts/salvaged_exact_algebra_independent_check_2026_08_08.py`;
- `claim_type_seed_hint: bounded_theorem` and `deps: []`.

The disclosed epoch deferral is not acceptable under the governing hard gate.
`docs/audit/scripts/build_citation_graph.py` is an exact-hash member of
`DEPENDENCY_POLICY_SOURCES`. The branch file hashes to
`abe1e3aab2ed4a5aa3624d7f4e4ed10b102828266a946c9dfc31d00ead349f5b`,
while `docs/audit/data/dependency_policy_epoch.json` still records
`e09dbee45c074c5f62f0133fa1261bee95b8671adae9147584febb3b658a541e`.
The normal pipeline therefore stops at stage 7 with
`ScienceFingerprintError: dependency-policy epoch manifest does not exactly
match its governed sources`.

I independently confirmed the worker's blast-radius concern: refreshing only
that controlled source hash in a disposable clone caused 891 hard-reset
invalidations (`legacy_dependency_policy_epoch_changed` or
`science_changed:dependency_policy_epoch`). That makes a broad epoch refresh
the wrong narrow fix, but it does not make a deliberately inconsistent
manifest landable. The current review-loop guard permits a narrowed blast
radius only through a separately reviewed machine-readable equivalence/impact
record; none is present. A dedicated policy repair can separate claim-scoped
packet-helper registration from the governed dependency-extraction source, or
otherwise add the reviewed impact mechanism, before this edit lands.

The cited precedent `f4979c872e` does not waive the gate: it was committed on
2026-08-01, while `dependency_policy_epoch.json` was introduced on 2026-08-02.
It therefore predates the policy being invoked. Similar current-main drift is
a regression to repair, not authority to repeat it.

## S3 — FIXED

A cold rebuild produced 4640 nodes and 15422 edges. Running
`write_citation_graph_manifest.py` afterward reproduced the committed manifest
byte-for-byte; both copies hash to
`a6b61b8e3d57937ac23b6b1bb41b174d1d17e5a85f3a98d56ed13ff34303cbcf`.
The manifest contains the exact-algebra claim node with out-degree zero. The
note now correctly distinguishes its ordinary pipeline-seeded `unaudited` row
from extra dispatch/re-audit requests and authored verdicts.

## S4 — NOT_FIXED

All five requested note corrections are present:

1. the scientific title is no longer a branch-process title;
2. runner file inputs are described accurately;
3. the Cycle 872/876/895/900 cross-reference maps to units 1, 2, and 5;
4. branch-local/current-state wording is replaced by historical provenance and
   correct ordinary-row wording;
5. the failed wrapper has both a named recovery branch and immutable commit
   `867aff0edc16f64b5e8d5cc1022cbf9ce92b92de`.

However, the same fix commit adds `REVIEW_LOOP` / `PRIMARY_REVIEW_LOOP` to both
durable runners and both receipts. That payload names the untracked reviewer
artifact `RL_SALVAGE_FINDINGS_PR5995.md` and asserts that S1-S4 were
"addressed" before this confirmation. See
`scripts/salvaged_exact_algebra_2026_08_08.py:63-76`,
`scripts/salvaged_exact_algebra_independent_check_2026_08_08.py:641-654`, and
the corresponding committed receipt fields. The primary payload now treats
that branch-local review record as canonical data.

This is the same governance class S4 was meant to remove: non-source review
state and an unlanded branch-local truth reference have been moved onto the
durable executable/evidence surface. Review provenance already has an honest
historical home in the note's Review record; it must not be duplicated as a
self-certifying runner payload. S4 therefore remains open despite the five
requested prose edits being individually correct.

## Confirmation checks

- Python compilation of both runners: PASS.
- Cold primary and checker runs: PASS, 31/31 and 27/27.
- External unrehashed and rehashed semantic tamper tests: PASS (checker exits
  1 in both; rehashed digest passes while payload equality fails).
- Changed-evidence readiness for the seeded row: PASS; primary and helper are
  both listed and `forensic_evidence_ready: true`.
- Citation graph seed/helper inspection: PASS.
- Citation-manifest deterministic regeneration: PASS.
- Vocabulary lint on the eight confirmation files: PASS, zero violations and
  zero rewrites.
- Repository-portable link scan: PASS.
- `git diff --check`: PASS.
- Full audit pipeline: BLOCKED at stage 7 by S2's dependency-policy epoch
  mismatch. Strict lint was not claimed because the prior hard gate stopped
  the pipeline.

## Final classification

- Code / Runner: PASS
- Physics Claim Boundary: BOUNDED
- Proof Obligations: CLOSED (unchanged exact seven-unit boundary)
- Imports / Support: CLEAN; zero-input exact algebra on stipulated definitions
- Nature Retention: BOUNDED; no retained/Nature-grade claim
- No-Go Discipline: NOT APPLICABLE
- Labeling Convention: PASS
- Repo Governance: FIX
- Audit Compatibility: BLOCKED
- S1: FIXED
- S2: NOT_FIXED
- S3: FIXED
- S4: NOT_FIXED

CONFIRMATION: FAIL — S2 leaves the governed dependency-policy epoch mismatched, and S4 adds unlanded review-loop metadata to durable runners and receipts
