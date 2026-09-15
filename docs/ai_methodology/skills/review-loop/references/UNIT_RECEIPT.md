# Unit receipt version 1

This handoff format binds an existing independent review to concrete source and
input bytes. It does not create a review, infer PASS, or replace the original
reviewer's affected-change confirmation. Keep reports and execution receipts as
immutable evidence. Changed identities require a new record and the appropriate
review, not rewriting an older report or restamping its output.

## Cheap preflight

Run before expensive execution, after staging the source proposal:

```sh
python3 docs/ai_methodology/skills/review-loop/scripts/review_receipt.py \
  --repo /absolute/unit-worktree --record /absolute/unit-v1.json
```

After authorized bounded execution, stage its canonical cache, obtain the
original reviewer's final binding, and create a new record with the new tree and
cache identities. Check it with `--cache`. This flag checks freshness; it never
executes or regenerates a runner. The first preflight needs no cache.

Exit 0 means recorded mechanical checks passed. It says nothing about the
science verdict, remote PR head freshness, completeness of scientific reading,
or combined integration validation. Exit 1 gives a JSON error. Stdout includes
the input-record and checker SHA-256. Save it under a new evidence filename.
The helper never writes reports, stages files, applies audit status or runs a
pipeline. `git write-tree` may add a Git object; it does not change the index.

Each CLI process targets one repository and imports its actual citation and
cache APIs, never scientific runners. It checks canonical IDs, explicit Type,
primary and packet helper discovery, actual citations and declared inputs. It
rejects missing fields, unknown versions, changed hashes, ambiguous IDs,
incomplete path maps, unstaged tracked changes and stale required caches. It
runs working, staged and base-relative whitespace checks, then rechecks bound
source, input, index and evidence identities before returning.

## Required record

All keys below are required. All five input categories are explicit lists,
including when empty. File entries use repository-relative `path` and a SHA-256
`sha256`. Paths cannot escape the repository or name a final symlink. Evidence
references use existing absolute paths and SHA-256. Git identities are full
object IDs. The following is a shape illustration, not an executable receipt:
replace every placeholder and include complete file/input lists.

```json
{
  "schema_version": 1,
  "unit_id": "PR1234",
  "constituents": [{
    "id": "PR1234",
    "head": "FULL_ORIGINAL_HEAD",
    "delta_base": "FULL_ORIGINAL_DELTA_BASE",
    "dispositions": {
      "path": "/absolute/original-review.json",
      "sha256": "REPORT_SHA256",
      "json_pointer": "/original_dispositions"
    }
  }],
  "source": {
    "base": "FULL_CONFIRMATION_BASE_COMMIT",
    "commit": "FULL_WORKTREE_HEAD_COMMIT",
    "tree": "FULL_STAGED_TREE",
    "paths": [{"path": "docs/NOTE.md", "sha256": "NOTE_SHA256"}],
    "deleted_paths": []
  },
  "inputs": {
    "runtime": [], "helpers": [], "parents": [], "context": [], "tooling": []
  },
  "reviewer": {
    "session": "original-reviewer-session-identity",
    "report": {"path": "/absolute/original-review.json", "sha256": "REPORT_SHA256"},
    "references": []
  },
  "non_science_notes": [],
  "notes": [{
    "path": "docs/NOTE.md",
    "claim_id": "note",
    "declared_claim_id": "legacy-note-id",
    "claim_type": "bounded_theorem",
    "primary_runner": "scripts/check_note.py",
    "helpers": [],
    "citations": [],
    "repository_dependencies": [],
    "dependency_rationale": "Self-contained supplied model; no repository theorem is a premise."
  }]
}
```

- `source.paths` covers exactly the nondeleted staged delta from `source.base`;
  `deleted_paths` covers its deletions. Inputs may include unchanged tracked files.
  Every bound file agrees with both disk and index.
- Each constituent keeps its original delta endpoints after retargeting or
  salvage. The checker compares all original paths, using delta-base bytes for
  deleted originals. It never calls GitHub: the coordinator separately verifies
  current remote heads against the frozen originals before landing/closure.
- The JSON pointer selects an existing list in immutable reviewer evidence.
  Each disposition row requires `original_path`, `original_sha256`, `disposition`,
  `recovery`, `final_path` and `final_sha256`. A null final path is allowed for
  rejected, deferred or superseded material; disposition and recovery remain
  nonempty reviewer-owned judgments. A mapped final path/hash must match a
  source/input binding. Renames use deletion/addition accounting from
  `git diff --no-renames`.
- `runtime` records actual scientific data/modules; `helpers` includes transitive
  and explicit packet helpers; `parents` records load-bearing repository
  authorities; `context` records other inspected authority/context inputs;
  `tooling` records tools. Identical path/hash pairs may occupy multiple categories.
  Reviewers must identify actual runtime inputs that static APIs cannot discover.
  Mechanical validity does not prove semantic completeness of that inventory.
- Tooling includes `docs/audit/scripts/build_citation_graph.py`,
  `docs/audit/scripts/static_pipeline_checkpoint.py` , `scripts/runner_cache.py`, `scripts/audit_packet_script_deps.py` and its
  imported `docs/audit/scripts/ledger_io.py`. The ledger API is imported only;
  no ledger materialization or audit command is called.
  When present, `docs/audit/data/axiom_premise_nodes.json` and
  `docs/audit/data/doc_authority_registry.json` are also bound because the actual
  citation API reads them. The checker itself is identified in stdout.
- `citations` is the exact actual-API target list, including historical/context
  citations. Every target is hash-bound. `repository_dependencies` is the
  reviewer-declared load-bearing subset, using repository paths; each is linked
  and in `inputs.parents`. Empty dependencies are legitimate with an explicit
  rationale. The checker never invents premise links from contextual references.
- The helper list matches actual graph/packet closure. Each runner declares a
  timeout; all literal declared inputs are readable and bound. An absent input
  declaration differs from an invalid empty/dynamic declaration. This validates
  declared closure, not arbitrary Python I/O.
- `reviewer.references` binds execution receipts, independent controls, external
  method evidence and other relied-on files. The report's scientific verdict is
  deliberately neither parsed nor promoted.

A prose summary can link this record and its evidence but cannot replace their
identities. Source changes reopen affected scientific conclusions even when a
regenerated preflight passes.

## Adapting an existing review once

Do not edit an old report to fit this schema. Create a new identity-only handoff
record, referencing the old report by absolute path and SHA-256. If its disposition
rows use different field names, create a separate mapping addendum containing the
required rows and a hash reference to the original evidence. Point the constituent
`dispositions` reference to that addendum; retain the original report under
`reviewer.report`. The original reviewer must confirm the mapping and affected
source identities. An adapter must not fill an absent judgment with PASS or infer
reading coverage from a successful runner.

Each note maps its exact source path and `declared_claim_id` (the actual frontmatter
value, or null when absent) to the graph API's canonical `claim_id`. A legitimate
legacy short ID may differ from the canonical ID; neither source renaming nor a
fabricated graph alias is needed. Canonical-ID ambiguity still fails.

`notes` may be empty for a process-only unit, provided its affected discovered
Markdown has complete explicit non-science dispositions. A nonempty source delta
is still required. The checker independently inventories discovered Markdown changed by the proposal
and unchanged notes affected by a changed primary, packet/transitive helper or
literal declared input. Every such note must appear in `notes`, or have an explicit
entry in `non_science_notes` with `path`, a nonempty reviewer `rationale`, and a
hash-bound absolute `review_reference`. The latter is for reviewed historical or
non-scientific material, not an automatic directory exemption. Its source bytes
must also be bound. Uncovered notes fail; the checker cannot decide whether an
asserted historical disposition is scientifically honest. That remains independent
review work. Example disposition:

```json
{"path":"docs/HISTORY.md","rationale":"Historical author narrative only; no current claim adopted.",
 "review_reference":{"path":"/absolute/review.json","sha256":"REPORT_SHA256"}}
```

The separate packet resolver's actual `transitive_helpers` API receives the
primary basename without `.py`; returned basenames are mapped to `scripts/*.py`.
Its closure must exactly match the graph API’s `resolve_helper_runner_paths`
transitive closure, otherwise preflight fails. Both discovery results are emitted. Graph-only explicit helpers
remain required; one resolver does not silently override the other. Affected-note
coverage uses their union. The transitive API reads source files, not audit ledger
or queue data; those generated surfaces are neither materialized nor used here.
