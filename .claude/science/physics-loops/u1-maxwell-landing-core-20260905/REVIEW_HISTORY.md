# Review history — block 01

(conformance pass + quote-fidelity checker findings at close)

## 2026-09-04T21:45+00:00 — blind Opus supplied-input ledger: CHECKED (supervisor)
Deliverable: BLIND_supplied_input_ledger_opus.md (26 ranked rows, 16 narrowings/contradictions). Supervisor spot-verified 8/8 load-bearing quotes against inputs/ (PR #7959 "the link role is designed, not derived"; PR #7915 N3 "not a claim that permanent Records update unitarily"; PR #7963 the -3.849 sigma early-window RK coefficient; PR #7921 "would make a supplier choice look like axiom content"; PR #7959 "toward z = 2, not away from it"; PR #7886 line 237 "does not derive kappa_s>0 or kappa_s=kappa_t" and lines 60-62 "a temporal registration kernel by itself supplies only the electric/temporal quadratic block ... has no magnetic restoring block and is not Maxwell"; PR #7915 lines 62/569 attributing kappa to "the Record-overlap magnetic curvature"). All hold verbatim.
Findings carried into block 01: (F-B1) SCOPE CONTRADICTION #7915 vs #7886 on what the Record-overlap chain supplies (magnetic curvature vs temporal block only) — the landing core must state the magnetic restoring block as a supplied input, not Record-derived, at #7886's own scope. (F-B2) the two deepest supplies are the TIME RULE (conservative first-order flow; no axiom names time; Record permanence in tension with per-tick updates) and M5 (positive diagonal conserved energy; #7917's uniqueness evaporates without it) — block 02 candidates. (F-B3) c^2 = U K flips verdict four times across finite volumes (#7945 -> #7952 -> #7955 -> #7963); #7963's own early window carries a resolved -3.849 sigma RK coefficient where #7945 treats RK as a clean null — the landing core's photon item must carry this estimator boundary. Status of this seat's work: CHECKED, awaiting cross-merge with the Fable primary's ledger (disagreements = findings).

## 2026-09-04T22:17+00:00 — block 01 close: checker verdict, fix pass, conformance gate
Checker (Opus, refuting): FIX FIRST — CH-01 blocker (same-carrier attribution), CH-02..CH-05 material, CH-06..CH-14 minor; 203 attributions checked; passes on self-containment, status block, photon-open, terminal, no derivation voice; D3 confirmed for the primary. Supervisor verified CH-01..CH-05 against the note and inputs before applying. Fix pass commit baf24571d5 (all findings applied; none rejected). Deviation logged: that commit was staged with `git add -A` (owner directive forbids it); the staged set was exactly the three deliverables; explicit-path staging from here on.
Conformance gate (REVIEW_LOOP_PR_CONFORMANCE_SPEC sections 1-12):
1 self-containment — PASS (one markdown link, to the landed axiom memo; no unlanded note linked; eleven verbatim PR copies removed from the pack inputs, replaced by a SHA-256 provenance README).
2 cache/execution — NOT APPLICABLE (no runner; the note declares Runner: none and computes one declared product only).
3 claim-scope honesty — PASS (meta; status fields from their enums; "landing core" declared plain prose, not a tier; no bare letter-number names in title; full-surface consistency: title/headline/status block/closing agree on "open" and "meta").
4 N-gate — NOT TRIGGERED (no own-voice no-go; member negatives quoted at scope only; the "does not claim" section is non-claims, not walls) — verified by grep of the note outside quoted spans.
5 proof obligations — NOT APPLICABLE (no theorem claimed).
6 runner validity — NOT APPLICABLE (no runner).
7 packet completeness — NOT APPLICABLE (meta row; no helper runners).
8 links/graph — PASS pending manifest: the delta adds exactly one graph node (u1_maxwell_light_lane_landing_core_meta_note_2026-09-05), no edges rewired; manifest regenerated on the final tree and staged explicitly at commit.
9 note structure — PASS (15 machine-status fields with mandated values; Imports section; Review record section added at close; no `surface_status` field).
10 propose/ratify — PASS (no audit fields written; manifest is the only generated artifact).
11 sourced facts/counts — PASS (as-of stamp 2026-09-05 added; member/record counts recomputed by the primary from the pack inputs at HEAD).
12 pre-review gates — vocab_lint --fix then --report-only: 0; audit_lint --strict: PASS; git diff --check merge-base..HEAD: clean; py_compile: no Python in delta; check_changed_audit_evidence: meta rows exempt; run_pipeline.sh: exit code recorded below when the background run completes; generated outputs restored before commit; explicit-path staging; cold read of the diff by the supervisor.
Independence class disclosed: single family (Claude), cross-model (Fable primary / Opus checker + Opus blind ledger), supervisor hand-verification.

## 2026-09-04T22:30+00:00 — pipeline gate closed; PR opened
run_pipeline.sh, full run on the final tree (HEAD 7bcb2d6764): PIPELINE EXIT=0. The earlier run's exit 1 was caused by the supervisor pruning the eleven pack input copies while that run was in progress ("cannot read static input .../inputs/PR7884__..."), not by the science; the rerun on the final tree is the gate of record. Generated outputs restored before commit (`git restore --source=HEAD --staged --worktree -- docs/audit/data/ docs/audit/AUDIT_QUEUE.md docs/audit/MISSING_DERIVATION_PROMPTS.md docs/repo/FRONT_DOOR_STATUS.md; git clean -fdq -- docs/audit/`); the pipeline's front-door re-render (row counts 4914 -> 4476 from native retirement of the moved notes; publication section in deferred mode) is a nightly-owned surface and is not this block's science. Manifest check: build_citation_graph + write_citation_graph_manifest re-run on the final tree (4761 nodes, 11860 edges) leaves the committed manifest byte-identical — section 8 of the gate is PASS, no longer "pending manifest". Pack hygiene at close: specs/full_primary.log (the dead codex sol seat's raw 316 KB stream, committed in checkpoint 75b4ad0649) is removed from the branch tip — untrusted worker output with no review value; the salvage narration (specs/SALVAGE_sol_primary_narration.md, marked untrusted draft input) stays; the raw stream remains reachable in branch history at 75b4ad0649.

# Review history — block 02 (the #7917 dynamics class against the axioms)

## 2026-09-05 — value gate V1-V5, answered in writing before any PR (Fable primary)
V1 (obstruction closed). No verdict-identified obstruction is closed: the members are unlanded open PRs with no audit row, so
there is no `verdict_rationale` to quote; the obstruction is the terminal's own boundary, quoted at scope from open PR #7917:
"The classification does not derive that dynamics class from the axioms, and exact finite local tick selection remains open."
and "The four axioms do not currently select that class. In particular, they do not state real linear first-order evolution,
energy conservation, minimal (E,B) payload, or continuous time." This block does not close it; it makes it item-exact
(trace_class upstream_support, consumer = the light lane's terminal): two of the seven items are shown mutually redundant
inside the class (compatibility from covariance under the vector-type payload law; covariance from compatibility plus
conservation with no orientation premise), one has a named axiom lever, and the other four are supplies with exact witnesses.
V2 (new content + the search). New: (i) the exact classification of every covariant nearest-neighbor real linear generator on
the one-component edge/face payload under all sixteen signed-permutation representations (four distinct couplings; only the curl
gauge/chain-compatible); (ii) the exact nullspace theorem that nearest-neighbor + gauge + magnetic-Gauss forces the curl with one
lattice-wide coefficient, hence item 4 from items 1,3,5,6,7; (iii) the parity theorem (edge-face couplings only at odd distance);
(iv) the sampling-identification dissipation (Gauss-Seidel decrease, radius two on the collapsed payload); (v) the item-6 versus
2026-08-13 analysis (three-part decomposition; the revision removed the first part for records, the axioms never had the other
two); (vi) ten exact witnesses; (vii) the two-speed extended conservative class with a vertex payload. Search: origin/main
e249016f759f224d9b429932cd0d1db4d452dc1a; the commands, thirty statement patterns, obligation/ledger greps and title greps, all
hits and their classification are in ROUTE_PORTFOLIO.md under "Block 02 prior-art sweep"; every matched hit is context,
method precedent, or a different object/mechanism; target state OPEN.
V3 (framework sentences needed). Yes: the Lattice axiom's "proper cubic rotations about each site" is what makes the face-site
stabilizer a supplied symmetry (the compilation's sector-preserving subgroup is computed from the parity roles, a supplied
structure the axioms permit but do not name); Lattice's "No site is privileged" sentence is the lever for item 4; Admissibility's
covariance and neighborhood sentences define IP-A/IP-B and the sampler; Record's one-record-per-site sentence is why a field
evolution is not a record sequence; the Qualification's one-answer sentence is the lever for the memoryless clause; the
2026-08-13 revision text decides the M5 kin question. Representation theory of D_4 and skew matrices alone would not produce
the adjudication, the identification premises, or the M5 analysis.
V4 (non-trivial). Yes: the redundancy of items 4 and 5 inside the declared class is a structural fact about the terminal that no
member states; the sixteen-representation classification and the cube-connectivity nullspace are constructions; the witnesses
are explicit laws checked exactly, several of which (unoriented, overdamped, vertex-scalar) are not in any member.
V5 (not a one-step variant). No. Closest landed: DYNAMICS_NONTRIVIALITY_SELECTION_FIREWALL_2026-06-06 (class != selection, for
the Wilson class under record preservation — different class, different mechanism, no per-item adjudication);
ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_2026-08-13 (same witness METHOD on static conditional laws — different object);
DYNAMICS_FORM_FROM_RECORD_PRESERVATION_2026-06-05 (gauge invariance from record preservation of a supplied Hamiltonian under
bridges — different mechanism from the covariance stabilizer). Closest campaign cycle: block 01 (meta; catalogued the class
without adjudicating it). Closest member: #7917 (declares the class and uses gauge as a hypothesis; never states that covariance
forces the curl or that its covariance step is implied by its magnetic-Gauss clause); #7921 (uses gauge for the curl too).
Structural distinction: this block removes a hypothesis from the declared class and names the exact residual with witnesses.
Gate: PASS on V2-V5; V1 answered honestly as upstream support, not closure (the PR is a bounded_theorem, not a promotion).
