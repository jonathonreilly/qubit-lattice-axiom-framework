# Unit receipts: versions 1–3 and scoped scientific coverage

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
executes or regenerates a runner. A preflight without populated summary
corrections needs no cache; schema-3 summary corrections require `--cache`
and the owner-primary cache bindings described below.

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

All keys below are required. Version 1 remains valid for existing units.
Version 2 additionally requires `supporting_proofs`, described below; old
checkers reject version 2 rather than silently skip its scientific coverage.
All five input categories are explicit lists,
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
  imported `docs/audit/scripts/ledger_io.py`. These API script paths must appear
  in `inputs.tooling` even when an edited helper map is already in `source.paths`;
  source ownership alone does not satisfy the checker's tooling category. Use
  the actual checker schema when assembling the record and reuse matching
  verified discovery rather than repeating scans or scientific review to repair
  a category omission. The ledger API is imported only;
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
  timeout, either in its source or as an explicit per-runner source-SHA-bound
  entry in `docs/audit/data/runner_timeout_declarations.json`. There is no
  implicit default in this contract. Source edits invalidate sidecar entries;
  source declarations take precedence. Bind the sidecar as a tooling input
  when present so the preflight rechecks its disk and index bytes. These entries
  avoid metadata edits to widely imported unchanged science helpers; they do
  not change the required cap, scientific scope or execution freshness checks.
  The fallback belongs to review tooling; audit runtime policy is unchanged.
  All literal declared inputs are readable and bound. An absent input
  declaration differs from an invalid empty/dynamic declaration. This validates
  declared closure, not arbitrary Python I/O. Check the actual receipt API's
  `declared_review_timeout_for` (which first uses the cache API's source declaration) for every primary and discovered helper before freezing
  or executing the unit; a fresh existing cache does not establish this required
  metadata. Apply any justified metadata correction before capturing evidence.
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

## Current supporting proofs

`repository_dependencies` records load-bearing paths, not a promise that every
path is an autonomous ledger claim. If a path is also an explicit version-2
supporting proof owned by that same canonical note, the integration gate must
verify its exact owner, source/input hash, immutable unit record and reviewer
reference before treating it as owned proof instead of a separate graph parent.
Retain that proof binding in the landing receipt. Require ordinary graph parents
for all other dependencies; never exempt a directory or suppress a genuinely
missing premise.


A proof fragment can belong to a canonical claim without being an autonomous
claim note. Keep it as current scientific source: do not label it historical or
non-scientific, fabricate a standalone claim/runner, or duplicate its argument
solely to satisfy the record format. Use **schema version 2** and an explicit
`supporting_proofs` list:

```json
{"path":"docs/PROOF_FRAGMENT.md","canonical_note":"docs/NOTE.md",
 "citations":[],
 "rationale":"Current supporting proof, fully reviewed under NOTE's stated hypotheses and conclusion; not an autonomous claim.",
 "review_reference":{"path":"/absolute/review.json","sha256":"REPORT_SHA256"}}
```

The owner must be a full reviewed `notes` entry, including its ordinary runner,
helper, premise and cache checks. Each supporting proof must be discovered
Markdown, hash-bound in `inputs.runtime`, directly linked from that owner, and
declared as an input of its primary or registered helper. Its own actual Markdown
citations must exactly match `citations` and have bound target bytes; unresolved
links fail. Its full argument, imported premises and interactions remain part of
the owner's independent scientific review. The reviewer must explain that
coverage and bind the corresponding report. The helper checks the recorded
relationship, not the truth or completeness of that scientific judgment.

An autonomous `claim_id`, extracted Type or primary runner requires a full
`notes` entry instead. Duplicate classifications, absent/unreviewed owners,
missing links/pins, missing input hashes and changed reports fail. Supporting
proofs never belong in `non_science_notes`; that category retains its historical
or non-scientific boundary. Version 1 cannot carry `supporting_proofs`. Version 2
may use an empty list. Success output retains its envelope `schema_version: 1`
and explicitly reports `record_schema_version` and the checked supporting proof
relationships. Evidence remains immutable across versions.

## Canonical and declared identities

Each note maps its exact source path and `declared_claim_id` (the actual frontmatter
value, or null when absent) to the graph API's canonical `claim_id`. A legitimate
legacy short ID may differ from the canonical ID; neither source renaming nor a
fabricated graph alias is needed. Canonical-ID ambiguity still fails for ordinary
claims. A registered premise parent may share its stable ID with historical
aliases only when the linked, hash-bound path is the premise registry
`current_path`, that path belongs to exactly one registered alias set, and all
discovered colliding paths belong to that same set. Superseded targets and
unregistered collisions fail; the registry bytes remain receipt-bound.

`notes` may be empty for a process-only unit, provided its affected discovered
Markdown has complete explicit non-science dispositions. A nonempty source delta
is still required. The checker independently inventories discovered Markdown changed by the proposal
and unchanged notes affected by a changed primary, packet/transitive helper or
literal declared input. Every such note must appear in `notes`, be a checked
version-2 supporting proof, or have an explicit
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

## Per-invocation discovery reuse

The checker memoizes results of the actual graph and packet import parsers and
literal input parser during one invocation. It returns fresh copies, restores the
original APIs on success or failure, and never persists these results as authority.
Every parsed source (including absent paths), the scripts directory, and scanned
notes retain generation tokens checked before return. A new/removed note changes
the actual discovered inventory and fails. Existing source/index/hash guards remain.
Stdout includes parser hit/miss counts so whole-repository cost can be measured
without rerunning scientific controls. This changes execution cost, not coverage.

### Proof inputs outside graph discovery

When the actual graph API excludes a proof input's location (for example,
Markdown under `outputs/`), preserve and fully review it as a hash-bound runtime
input. Describe its ownership and scope in the canonical argument and reviewer
report, using portable inline paths where the citation resolver cannot accept a
link. Do not invent a graph claim or a non-science exemption. Version 2's
`supporting_proofs` relationship applies only to discovered Markdown; ordinary
runtime proof inputs can use version 1. Both require complete proof, premise and
input review under the owner's claim.

## Scoped summary corrections (schema version 3)

Use this role only for independently reviewed derivative reporting corrections,
including a current boundary annotation on a preserved historical snapshot. It
is **not** a whole-note scientific PASS, a non-science exemption, supporting
proof ownership, or an invented primary. Autonomous calculations, proof steps,
normalizations, selectors and physical implications still require ordinary
canonical records. Neither the checker nor a byte diff can establish semantic
entailment; the independent reviewer must read every complete changed argument
and its necessary context, including negative/withdrawal claims.

Schema 3 requires all schema-2 keys plus an explicit `summary_corrections` list
(empty is permitted). Schema 1/2 reject that key even when empty. Schema 3 rejects
unknown fields in its record structure and new role/report structures; schemas
1/2 retain their existing contract. Each role has unique path ownership. Existing
summary metadata is preserved exactly: complete LF/CRLF delimiter-line
frontmatter (malformed or unclosed blocks fail), explicit type/status/authority/runner
lines, extracted type and primary cannot be added, deleted or changed through
this role. Graph discovery and actual edges/status remain unchanged by the
receipt classification. Untouched claims and unrelated historical primaries are
not newly approved.

Each item has exactly these fields:

```json
{"path":"docs/LIVE_SUMMARY.md",
 "base_sha256":"OLD_WHOLE_FILE_SHA256",
 "current_sha256":"NEW_WHOLE_FILE_SHA256",
 "review_reference":{"path":"/absolute/independent-summary.json",
                     "sha256":"REPORT_SHA256","json_pointer":"/confirmation"},
 "edits":[{
   "old":{"start":100,"end":130,"sha256":"OLD_SLICE_SHA256"},
   "new":{"start":100,"end":155,"sha256":"NEW_SLICE_SHA256"},
   "old_context":{"start":70,"end":200,"sha256":"OLD_SECTION_SHA256"},
   "new_context":{"start":70,"end":225,"sha256":"NEW_SECTION_SHA256"},
   "canonical_notes":[{"path":"docs/CANONICAL.md","claim_id":"canonical",
     "scope":"Exact independently confirmed conditional claim scope.",
     "review_reference":{"path":"/absolute/independent-owner.json",
                         "sha256":"OWNER_REPORT_SHA256","json_pointer":"/confirmation"}}],
   "rationale":"Why this changed assertion is no stronger than those canonical claims."
 }]}
```

The baseline is the exact existing regular-file blob at `source.base`, not a
convenient older snapshot. File mode must remain unchanged. Additions, deletions
and renames have no summary-role shortcut. Ordered nonoverlapping half-open
ranges use **UTF-8 bytes**, never character/line offsets; both boundaries must
be valid even for zero-width insertion/deletion ranges. Every range and enclosing
context is hash-bound. Context must enclose the changed range and be nonempty;
reviewers determine whether it covers the complete argument. Replacement slices
plus unchanged baseline segments must reconstruct the entire candidate exactly.
Omissions, stale anchors, overlap, no-op edits, uncovered prefix/tail edits and
hash drift fail. Whole-file replacements still need complete human scope review.

The immutable summary reference selects an object with exactly `decision`,
`path`, `base_sha256`, `current_sha256`, `edits`, and `scope_rationale`.
`decision` must be `confirmed_derivative`; path, hashes and the complete edits
(including owner references and rationales) must equal the record. The nonempty
scope rationale records the independent entailment judgment. A changed assertion
or rationale requires a new confirmation; repinning an old report cannot supply
it. Evidence hashes are rechecked before return. This is identity validation,
not authentication of the human reviewer or an automated truth judgment.

Each owner must be a unique normal `notes` record checked in this operation;
external receipts and summary-to-summary ownership are unsupported. Its reference
selects exactly `decision`, `path`, `claim_id`, `source_sha256`, `scope`, and
`bindings`. The decision is `confirmed`, not held/pending; all values must match
current owner identity and declared scope. `bindings` is a sorted list of exact
`path`/`sha256` pairs covering that canonical note, primary, all discovered
helpers, all literal inputs of those runners, actual citation targets, and its
primary cache. This binds the review to helper/input changes as well as the note.
Owners retain all normal type, primary, helper, cap, premise and input checks.
Summary corrections additionally require `--cache` and a fresh, bound primary
cache for each owner. Helpers require the usual exact source/input/cap closure;
they do not automatically require a standalone cache or execution. A helper that
is itself a canonical owner has its own ordinary primary requirement.

No canonical owner may depend back on a summary through its declared inputs or
load-bearing dependencies, including other same-operation canonical parents.
A citation is not by itself an entailment proof; held dependencies cannot be
laundered through a `confirmed` label without independent current-scope review.
Original constituent/disposition lineage remains required and unchanged.

Inventory is computed independently over changed Markdown **and** changed
primary/helper/declared-input effects, even when a note itself changed. This
initial version conservatively rejects the summary role if that summary's own
discovered primary, helper, or declared input changed, including a self-input.
Use normal canonical coverage or retain HOLD; do not suppress that inventory.
Other affected canonical consumers still require their normal records and fresh
required caches. A summary correction does not satisfy their obligations.

Success output visibly uses `role: scoped_summary_correction`, exact byte ranges
and canonical bindings; it never places a summary in the ordinary `notes` PASS
scope. `cache_checked` and mechanical success do not confer retained status or
approve unchanged summary content. A current-main adapter must reconstruct and
review against its actual new base, not transplant old ranges.
