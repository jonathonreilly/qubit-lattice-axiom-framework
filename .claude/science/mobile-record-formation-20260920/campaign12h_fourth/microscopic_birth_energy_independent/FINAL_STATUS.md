# Current recovery checkpoint: comparison complete

The bounded independent reconstruction and the authorized post-PRE comparison
are complete. This file supersedes RECONSTRUCTION_STATUS.md, which remains
unchanged as part of the sealed historical PRE packet.

Read POST_FINAL_COMPARISON.md for the final proof comparison and explicit
reservoir-premise limitations. It reports no mathematical discrepancy in the
two released author notes. PRE_MICROSCOPIC_STAR_RECONSTRUCTION.md preserves
the independent pre-exposure reconstruction. This is not an audit or landing
verdict.

Source bindings:

* PRE_SEAL.json SHA256:
  82e5b45bc8ecf0aad7deb8f2af8c457062c2bcb860dc83d18c4538a1ac3053d9.
* Exact-star author seal SHA256:
  ff9362d4ad06b36c86153d71b23b361843a77a26ceb4400f7b6ed14bea12aff5.
* Finite-time extension author seal SHA256:
  4812c28ae4ec3cfcace52536cecd9156557cd851b1fd2b2958d361cc49fca3b1.

The PRE control completed 222 checks. POST run 02 completed 249 checks,
including source and artifact bindings, all published exact marked outputs,
the independent two-dimensional spectral derivation, 18 full GKLS cases for
both instruments, and seven high-precision author-row comparisons. Full logs,
results and failed runner revisions are retained. The POST's 25 additional
asymptotic samples corroborate the proof; they do not prove it by themselves.

Reproduce using fresh attempt names:

    python3 microscopic_star_complete_matrix_check.py --attempt new_pre_run
    python3 post_compare_and_extend.py --attempt new_post_run
    python3 verify_pre_seal.py PRE_SEAL.json
    python3 verify_pre_seal.py FINAL_COMPARISON_SEAL.json

The two runners deliberately fail if asked to overwrite a prior result.
The original author files were only read. Copies under post_sources/ are
snapshots; the independent POST computation does not execute them.

No open obligation remains within this bounded assignment. Root owns source
integration and any publication decision. Formal retention, a physical
reservoir construction, changed-instrument effects, other graphs, repeated
births and volume limits are outside this assignment. No editable prompt
files, audit status, repository source files or other worker's files were
changed; all writes are inside the assigned reconstruction directory.
