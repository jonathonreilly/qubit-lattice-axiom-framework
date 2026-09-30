# Mechanical graph acknowledgment — 2026-09-30

The actual serialized `run_citation_graph_build.py` completed with exit 0,
followed by the actual deterministic `write_citation_graph_manifest.py`.
The graph is 6,815 nodes and 15,265 edges, compared with 6,814 and 15,264
on this branch's own HEAD and fetched main, both
`30a9461ee19a49b99fa6628fe942f08e504e8903`.

Every one of the 6,814 existing manifest entries was compared and is unchanged.
The sole new node is
`nonlinear_canonical_gravity_analytic_approximation_bounded_theorem_note_2026-09-30`.
Its sole dependency is `minimal_axioms`; its primary is the frozen
`scripts/nonlinear_canonical_gravity_analytic_approximation_2026_09_30.py`,
with no helper runner paths. Its graph note hash equals the reviewed source
hash `3a2615b0fb90d01dde1c62a66e159f88bc1c5bd320afa68b0793200c3243bcef`.
The minimal-axioms citation identifies the framework comparison expressly
bounded in the note; it does not derive the supplied canonical law.

The resulting manifest SHA256 is
`71fce10591f8e82db2d5c100bacc75bafcae78abfe10b8af3219d392e6099ed3`.
Its exact bytes agree with the owning writer's `compute_manifest` result.
The JSON companion records the complete new node, all changed-entry lists,
counts and graph hash. No existing node was removed or changed. The manifest
is the only tracked working-tree delta. No incidental tracked audit output
needed restoration; no index change was made.

The managed build used 526.902171 wall seconds, 493.824853 child user CPU
seconds and 9.100014 child system CPU seconds. Child peak RSS was 187,727,872
bytes; the producer's sampled peak was 156,499,968 bytes. The child resource
totals include the short `ps` probes. The allowed envelope was 1,200 wall
seconds and 500,000,000 sampled producer RSS bytes, with all six numerical
thread settings fixed to one. Deadline and STOP checks ran before launch,
throughout the build, and before the manifest write. No guard fired.

`GRAPH_PREBUILD.json`, `GRAPH_BUILD.log`, `GRAPH_BUILD_METRICS.json`,
`GRAPH_DELTA.json` and `GRAPH_MECHANICAL_PRECHECKS.json` contain the actual
identity, execution and comparison evidence. Fresh main was unchanged;
the read-only open inventory contained PR9397 and draft PR9008. No new
gravity-source or premise interaction was identified in that inventory.

This acknowledges topology only. Source review remains bound to
`REVIEW_IDENTITIES.json`; this mechanical work issues no review or audit
verdict. Combined pipeline, strict audit lint, changed-evidence validation,
final inventory, commit and same-reviewer committed-head confirmation remain
for root. No staging, commit, push, PR operation, audit application or full
pipeline was performed here.
