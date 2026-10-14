# Review and reproducibility history

Author read the complete cold note and runner diff. The fixed contract is
synthetic; the note's formulas supply its independent expected values.
Initial actual execution passed 10 check families. Independent methods include
matrix inverse versus spectral resolvent, gamma moments versus quadrature,
frequency versus momentum Wightman normalization, radial versus mass-space
source kernels, analytic inverse versus synthetic charges, and covariance
versus high-precision differentiation. Earlier campaign independent proofs
motivated the portable packet; those earlier summaries do not replace final
source review.

Ten scratch-source mutations were actually executed: alter spectral weight
normalization; replace the squared mass matrix by the mass-coordinate matrix;
shrink the Hermite bound; halve the noise normalization; remove the finite
mass threshold; discard the tail weight; change the shell denominator sign;
exchange a source mass fraction in the inverse; change ell^4 to ell^3; reverse
the covariance score sign. Every intended family failed. Exact old/new text,
source hashes and exit codes are in evidence/MUTATION_RECEIPT.json. Following
a reviewer hygiene finding, the runner now explicitly rejects source shape
other than 1; all mutations were repeated and an isolated shape 2 contract was
rejected. The production source was not mutated in place.

Actual cache generation uses scripts.runner_cache.execute_and_write_cache
with the declared 120-second timeout. No hand-written or copied PASS cache.
Vocabulary lint on the three science files reported zero findings.
No formal audit was invoked or applied.

Focused reviewer: the existing `neutrino_candidate` independent agent,
dispatched for source review with final exact note/runner/contract hashes.
The campaign requested Astra with max reasoning for hard science. The active
agent tooling does not expose a verifiable live model configuration; no
stronger provider/model attestation is claimed.
The same reviewer confirmed the one source-shape guard correction and read
the full final source. Final disposition: PASS WITH BOUNDED CLAIMS, with
zero unresolved material source findings. The complete report and portable
independent checker are preserved in evidence/independent_review/.
Final science hashes remain those in evidence/SOURCE_FREEZE.json.

## Conformance disposition before PR

Reviewed against current main 516cb69d8487ff04f8a48e065d3dcbe71d7dd237,
`docs/ai_methodology/REVIEW_LOOP_PR_CONFORMANCE_SPEC.md` and the owning
physics-loop CLAIM_STATUS/DELIVERY references. No spec wording is treated as
scientific evidence.

1. Self-containment: PASS. The entire mathematical chain is in the new note;
   the primary runner uses only its shipped fixed contract plus numerical
   libraries. Its declared inputs are this note and contract. Earlier working
   packets provide provenance, not missing premise proofs or runtime inputs.
2. Cache/execution: PASS. The runner declares AUDIT_TIMEOUT_SEC=120 and the
   actual cache is generated with execute_and_write_cache at that timeout.
   Final source and input hashes are bound. No hand-written PASS or metadata.
3. Scope: PASS under the owning claim-status rule. The note, runner and pack
   consistently state conditional-support/bounded_theorem/frontier_discovery.
   No measured datum was fitted; synthetic examples and finite checks remain
   separate from the proofs. The stale promotion-token conflict in the spec
   is reported in HANDOFF.md rather than followed.
4. Negative-claim gate: NOT TRIGGERED. This is a constructive conditional
   theorem and explicit response example, with hypotheses and degenerate
   controls. It asserts no exhausted route, missing framework primitive,
   impossibility of completion, or universal no-go. Physical bridges are
   named future inputs, not an impossibility claim.
5. Proof obligations: PASS. The exact target precedes the proof; the explicit
   obligation graph preserves its action, measure, state, source and probe
   hypotheses. Degenerate cases and strict exterior versus gamma-surface
   scope are stated. No target-equivalent unproved terminal lemma remains;
   actual measurement calibration is a separate stronger physical task.
6. Runner validity: PASS. Ten independent mathematical check families ran;
   ten actual load-bearing mutations failed their intended families. The
   independent reviewer reproduced those failures, reconstructed the proof,
   and ran eight checks without importing author helpers. Raw failed reviewer
   attempts and the correction are preserved. Numerical diagnostics do not
   replace analytic proofs or interval certificates.
7. Packet completeness: PASS for this source unit. One self-contained primary
   runner reproduces every numerical value used by the scientific note. No
   helper runner is a scientific premise or required output. Independent
   review checks are validation artifacts, not an undeclared computational
   dependency. No helper-registry or dependency-policy edit is made.
8. Links/graph: PASS for source preparation. The note's four local links and
   the handoff link resolve in the proposed delta. The serialized graph build
   and manifest writer ran. The inspected manifest adds exactly one node,
   zero edges; all 15805 prior edges and 7023 prior nodes are preserved.
   Only the generated manifest carve-out is staged. The later combined-tree
   stage-18 gate remains a landing obligation.
9. Structure: PASS. Complete claim-status and trace fields, premise/import
   table and dependency graph are in the note. This adds a new argument and
   neither replaces nor narrows existing source. No packet helper is needed.
10. Propose/ratify: PASS. No verdict, applied audit standing, queue, ledger,
    premise registry or publication status is changed. The bounded_theorem
    row is a future independent-audit target, not author ratification.
11. Facts/counts: PASS. Current main and the intended graph delta were read;
    all check counts come from actual final execution/replay records. No
    empirical observation, fitted constant, or unsupported novelty claim is
    smuggled into the theorem. Main/open-PR comparison remains scoped.
12. Focused gates: source/runner/premise review complete; final scoped
    vocabulary, Python compilation and full staged-delta whitespace checks
    are recorded below after execution. This independent branch adds no
    inherited science and deletes no current-main source. The complete cold
    science diff and shape-guard correction were read. Full pipeline, strict
    audit lint and changed-evidence readiness are deliberately UNRUN here:
    section 12 assigns them to one exact integrated current-main landing
    candidate, not an additional per-PR source run. This task authorizes a
    regular review PR, not landing or audit application.

Final metadata extraction correction: the header initially placed Date, Claim
type and Status on one line, so the anchored graph parser read no type hint.
They now occupy separate lines; the actual parser returns bounded_theorem.
The mathematical body, runner and numerical contract are unchanged. The cache
was actually regenerated for the new note input. The original source freeze
is retained in runtime, and the updated freeze records the change explicitly.
The first direct parser import lacked its script directory on sys.path; adding
the actual repository script path resolved that tooling check without edits.

Final focused execution: scoped vocabulary --fix and --report-only each
reported zero findings; both shipped Python sources compile. The final
metadata-only correction was confirmed by the original reviewer; the final
note-input-bound cache actually ran 10/0. The graph was then regenerated
again from final bytes: the intended node has bounded_theorem author hint,
the primary runner is attached, and the manifest topology delta is unchanged.

The first staged whitespace check flagged a context-only blank line inside a
verbatim raw patch artifact. Raw correction diffs remain intact in runtime;
the redundant patch copies are omitted from this delivery. The actual source
corrections, hashes, review and executions remain in the packet. The final
staged delta then passed the whitespace gate.
