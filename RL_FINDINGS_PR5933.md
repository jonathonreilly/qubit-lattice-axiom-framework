# PR #5933 Combined Adversarial Science Review — Iteration 1

Scope: stacked delta `c73a11d1ea7ddd564c48aa2a5a459a43d94262ef..c28a1e42f7441f98ceced0c41f348ebf15ef3dd2` only (five files listed in `RL_FILES_PR5933.txt`).

Review mode: sole combined pass. Repository source files and audit verdict data are read-only. Findings are recorded incrementally here.

Applicable lenses under review: CodeRunnerReviewer; PhysicsClaimBoundaryReviewer; ProofObligationReviewer; ImportsSupportReviewer; NatureRetentionReviewer; NoGoDisciplineReviewer; LabelingConventionReviewer; RepoGovernanceReviewer; AuditCompatibilityReviewer. MethodologySkillReviewer is not applicable because no methodology file is in the stacked delta.

## Findings

### 1. `OVERCLAIM` — the runner does not establish that the arbitrary-dissection floor 56 is attained or immune to compatibility tightening

Lenses: CodeRunnerReviewer; PhysicsClaimBoundaryReviewer; ProofObligationReviewer; NatureRetentionReviewer.

The note correctly derives the lower bound 56 from the minimum *single-cell* normalized ratio, but then says that pairwise disjointness cannot tighten it because “the bound is attained by a cell family” ([note lines 84–88](docs/PHYSICAL_SCALE_FREE_ADJACENCY_DISSECTION_BRACKET_CYCLE724_NOTE_2026-08-03.md#L84-L88)). The runner only identifies the ratio-minimizing `(cost, volume) = (7, 3)` cell class ([runner lines 177–186](scripts/physical_scale_free_adjacency_dissection_bracket_cycle724_2026_08_03.py#L177-L186)); it neither constructs nor searches for a volume-complete, pairwise interior-disjoint family made from those cells. A local argmin proves `cost >= 56`, not existence of a dissection saturating 56, and compatibility constraints could still raise the optimal global floor. The lower bound survives unchanged, but the attainability/“does not tighten” sentences require either an exact dissection certificate or removal.

### 2. `SEMANTIC_BRIDGE` — the physical tick-extended assembly domain is attributed to the Lattice axiom although that realization bridge remains open

Lenses: PhysicsClaimBoundaryReviewer; ImportsSupportReviewer; NatureRetentionReviewer; ProofObligationReviewer; RepoGovernanceReviewer; AuditCompatibilityReviewer.

The note says the preceding physical escape is removed and that the Lattice axiom’s six nearest-neighbor directions “define the admissible set here” ([note lines 18–30](docs/PHYSICAL_SCALE_FREE_ADJACENCY_DISSECTION_BRACKET_CYCLE724_NOTE_2026-08-03.md#L18-L30), [lines 186–190](docs/PHYSICAL_SCALE_FREE_ADJACENCY_DISSECTION_BRACKET_CYCLE724_NOTE_2026-08-03.md#L186-L190)). The runner instead starts from a supplied four-coordinate domain `Z^3 × {tick}` and a supplied simplex cost definition ([runner lines 3–20](scripts/physical_scale_free_adjacency_dissection_bracket_cycle724_2026_08_03.py#L3-L20), [lines 63–74](scripts/physical_scale_free_adjacency_dissection_bracket_cycle724_2026_08_03.py#L63-L74)). The Lattice axiom supplies spatial `Z^3` nearest-neighbor adjacency only. The approved kinetic-isotropy primitive may supply equal tick/edge graining without bounding the result, but it supplies no physical cell-selection or rule-to-tick correspondence; `docs/repo/ACTIVE_REVIEW_QUEUE.md` explicitly keeps the physical tick–Admissibility realization bridge open. Therefore the runner supports a conditional combinatorial theorem on the declared tick-extended simplex/dissection model, not the claimed inference that the framework axioms select that assembly domain or remove the physical frame-label escape. The note must name the tick-extended simplex/dissection model as a supplied condition, cite the kinetic-isotropy primitive for the graining it actually grants, and keep the physical realization bridge open.

### 3. `AUDIT_COMPATIBILITY` — the dependency section creates two non-load-bearing edges to unaudited rows and omits the actual tick-graining premise edge

Lenses: ImportsSupportReviewer; RepoGovernanceReviewer; AuditCompatibilityReviewer.

The note’s markdown dependency links seed edges to the direction-set/covariance and proper-cubic-ceiling rows ([note lines 186–190](docs/PHYSICAL_SCALE_FREE_ADJACENCY_DISSECTION_BRACKET_CYCLE724_NOTE_2026-08-03.md#L186-L190)); both are currently `unaudited` in their individual ledger shards. Neither is load-bearing in the delta: the runner constructs and verifies the monotone-path stencil directly ([runner lines 433–460](scripts/physical_scale_free_adjacency_dissection_bracket_cycle724_2026_08_03.py#L433-L460)), and the proper-cubic covariance ceiling is never used in a formula or gate. Conversely, the supplied tick graining that underlies the four-coordinate cell is not linked to the registered kinetic-isotropy primitive. As submitted, the manifest records three edges but represents provenance as theorem premises and misses the actual approved premise. Move the two historical/covariance references to non-edge context, add the relevant registered-primitive link, and regenerate `docs/audit/data/citation_graph_manifest.json`. This is `FIX`, not an audit verdict.

### 4. `AUDIT_COMPATIBILITY` — absent stacked ancestors are provenance-only and are disclosed rather than load-bearing

Lenses: RepoGovernanceReviewer; AuditCompatibilityReviewer.

Cycles 721, 722, and 723 named at [note lines 192–199](docs/PHYSICAL_SCALE_FREE_ADJACENCY_DISSECTION_BRACKET_CYCLE724_NOTE_2026-08-03.md#L192-L199) are absent from both the merge base and current `origin/main`. They are backticked rather than markdown-linked, the note explicitly says they carry no dependency edge, and the runner reads no ancestor artifact; all enumerations and witnesses are rebuilt locally. The delta therefore does **not** load-bear on the unlanded ancestor campaign. Status for this check: `DISCLOSED` (provenance-only), not `BLOCKED`.

### 5. `BUG` — the LP cross-check treats every unsuccessful solver termination as a proof of disjointness

Lenses: CodeRunnerReviewer; ProofObligationReviewer.

`disjoint_lp` returns `True` whenever `linprog` is not successful ([runner lines 270–294](scripts/physical_scale_free_adjacency_dissection_bracket_cycle724_2026_08_03.py#L270-L294)). Status `infeasible` is the expected certificate when the closed simplices do not meet, but numerical failure, iteration limit, or another abnormal termination would take the same branch and could agree spuriously with `disjoint_batch`, allowing the “0 disagreements” PASS at [lines 297–305](scripts/physical_scale_free_adjacency_dissection_bracket_cycle724_2026_08_03.py#L297-L305). Distinguish the proven-infeasible status from unexpected solver failure and make the latter increment FAIL/abort. The present results are not numerically contradicted: the independent review recomputation saw only optimal or proven-infeasible HiGHS statuses across all 100,128 cost≤4 pairs, but the committed gate is not fail-closed.

### 6. `NIT` — the stated “exact integer arithmetic” implementation uses rounded floating determinants

Lenses: CodeRunnerReviewer; RepoGovernanceReviewer.

The note and runner say all combinatorics is exact integer arithmetic ([note lines 10–14](docs/PHYSICAL_SCALE_FREE_ADJACENCY_DISSECTION_BRACKET_CYCLE724_NOTE_2026-08-03.md#L10-L14), [runner lines 22–27](scripts/physical_scale_free_adjacency_dissection_bracket_cycle724_2026_08_03.py#L22-L27)), but `det4` and the refined sweep call `numpy.linalg.det` in `float64` and round to integers ([runner lines 68–69](scripts/physical_scale_free_adjacency_dissection_bracket_cycle724_2026_08_03.py#L68-L69), [lines 189–208](scripts/physical_scale_free_adjacency_dissection_bracket_cycle724_2026_08_03.py#L189-L208)). On the actual native and refined domains, an independent 24-term integer determinant expansion found zero discrepancies, so this is provenance wording/implementation hygiene rather than a changed result. Use an integer determinant or narrow the exactness statement. Likewise, “removes it without enumerating anything” at [note line 26](docs/PHYSICAL_SCALE_FREE_ADJACENCY_DISSECTION_BRACKET_CYCLE724_NOTE_2026-08-03.md#L26) contradicts the explicit 125-site enumeration at lines 38–41; the clean statement is that the scale-free proof is analytic with a finite local cross-check. Finally, the exact cost identity behind [note lines 104–112](docs/PHYSICAL_SCALE_FREE_ADJACENCY_DISSECTION_BRACKET_CYCLE724_NOTE_2026-08-03.md#L104-L112) is `C = 120 - 2n3 - n4 + n6 + 2n7`; omitting the nonnegative excess still gives the stated lower bound, but “writing the cost as 120 minus” should be written as an inequality (or define signed saving).

### 7. `NO_GO_OVERCLAIM` — N1–N8 supports the simplex no-go but not the broader claim that the physical construction escape is removed

Lenses: PhysicsClaimBoundaryReviewer; NoGoDisciplineReviewer; NatureRetentionReviewer; ProofObligationReviewer.

The negative statement at [note lines 18–30](docs/PHYSICAL_SCALE_FREE_ADJACENCY_DISSECTION_BRACKET_CYCLE724_NOTE_2026-08-03.md#L18-L30) is broader than the proved definition at [lines 34–49](docs/PHYSICAL_SCALE_FREE_ADJACENCY_DISSECTION_BRACKET_CYCLE724_NOTE_2026-08-03.md#L34-L49). N1–N8 result:

- **N1 alternative routes:** (1) a third distinct spatial site is excluded by the bipartite/parity structure of the `Z^3` nearest-neighbor graph; (2) the runner’s translated local-neighborhood exhaustion independently excludes a three-site clique; (3) spatial refinement/rational scaled-lattice vertices do not change that graph argument; (4) arbitrary values on a single tick coordinate still add at most one affine direction to the at-most-one spatial direction; (5) repeated spatial sites do not increase the affine span; but (6) a nonsimplicial cell complex whose *actual 1-skeleton edges* are nearest-neighbor does not require every vertex pair to be adjacent and remains untested. Routes 1–5 close the declared pairwise-adjacency simplex target; route 6 defeats the broader physical-construction rhetoric.
- **N2 wall independence:** tick graining is an approved primitive, not a wall. Physical tick–Admissibility realization and the choice that physical assembly cells are complete-graph simplices/pairwise-adjacency vertex sets are separate unstated conditions; the note gives no collapse argument between them.
- **N3 hidden-wall scan:** “the Lattice axiom names/defines the admissible set” and “this cycle removes that escape” hide those two conditions rather than citing/declaring them.
- **N4 residual matching:** the absent cycle-723 corner census has the same narrow simplex-cost residual and is superseded by local recomputation. Cycles 721/722 concern frame-label readings, while the proper-cubic and direction-set notes concern covariance; none proves the physical assembly identification, so they cannot close this residual.
- **N5 rhetoric/resolution:** the runner tests pairwise sites, 3-/4-simplex rank, native corner cells, unimodular corner dissections, and one spatial refinement. It does not test general nonsimplicial cells, a lattice-wide complex, or physical rule-to-cell realization. The broad “escape removed” sentence exceeds the tested resolutions.
- **N6 partial-closure scan:** the registered kinetic-isotropy primitive closes only equal graining. Existing repo notes explicitly preserve the physical tick–Admissibility realization as supplied/open; the honest path is a bounded conditional combinatorial theorem, not a new axiom and not an axiom-level physical no-go.
- **N7 steelman:** a full-dimensional lattice cell can have a nearest-neighbor 1-skeleton while non-edge vertex pairs are farther apart; the cubic/hypercubic cell is the elementary counter-framing. Because the framework does not select simplicial cells, the affine ceiling on *pairwise-adjacent vertex sets* does not rule out that construction route.
- **N8 cross-cycle echo:** `CUBIC_COXETER_REGGE_LINEARIZED_ACTION_SELECTION_EH_CLASS_NARROW_THEOREM_NOTE_2026-06-10.md` already repaired the analogous adjacency-only inference by stating it as a hypothesis, and the live review queue preserves the tick–Admissibility bridge as open. The same narrowing mechanism applies here.

No-Go Discipline output: **FAIL** for the physical “escape removed” claim (N2, N3, N5, N7, N8); **PASS** only after partial narrowing to the exact theorem “a pairwise spatial-nearest-neighbor vertex set in `Z^3 ×` one tick coordinate has affine rank at most two.”

### 8. `REPO_GOVERNANCE` — the changed science surface uses a noncanonical axiom spelling and conflates the Lattice and Admissibility namespaces

Lenses: LabelingConventionReviewer; RepoGovernanceReviewer.

The changed note and runner repeatedly write the axiom name as all-caps `LATTICE` ([note lines 18–20](docs/PHYSICAL_SCALE_FREE_ADJACENCY_DISSECTION_BRACKET_CYCLE724_NOTE_2026-08-03.md#L18-L20), [line 190](docs/PHYSICAL_SCALE_FREE_ADJACENCY_DISSECTION_BRACKET_CYCLE724_NOTE_2026-08-03.md#L190), [runner lines 3–6](scripts/physical_scale_free_adjacency_dissection_bracket_cycle724_2026_08_03.py#L3-L6)); the controlled name is `Lattice`. More importantly, line 190 says its spatial directions “define the admissible set,” while `Admissibility` is the separate framework axiom governing the local probability distribution/support over possibilities, not a synonym for the lattice direction set or a cell-complex selector. This needs a native-language wording fix together with Finding 2. The explicit scientific title plus “Cycle 724” suffix is acceptable, no new bare letter-number primary science name is introduced, and the bounded theorem is algebraic/combinatorial rather than a labeling stipulation; LabelingConventionReviewer therefore otherwise outputs **PASS**.

## Proof-obligation graph and independent verification

1. **Affine ceiling:** Lattice nearest-neighbor adjacency plus the declared pairwise-adjacency definition implies at most two distinct spatial sites (equivalently, the `Z^3` nearest-neighbor graph is bipartite and triangle-free). Crossing those sites with one tick coordinate gives affine rank at most two. This closes the 3-/4-simplex no-go on the declared mathematical domain; it does not supply the physical assembly bridge.
2. **Native census:** exhaustive five-subsets of the 16 supplied corners, nonzero determinant, and the declared pair cost give 3008 cells, floor 3, 64 minimizers, and the stated unimodular profile. An independent exact 24-term determinant implementation reproduced every count and found zero disagreements with the runner’s rounded determinants.
3. **Arbitrary corner lower bound:** `min(24e/v) = 56` and volume additivity close the lower bound. They do not close global attainability; that is Finding 1.
4. **Unimodular lower bound:** unit determinant forces 24 cells. With `n3 <= 8` and `n3+n4 <= 16`, `C = 120 - 2n3 - n4 + n6 + 2n7 >= 96`. A wholly separate barycentric-LP graph over all 100,128 pairs of the 448 cost≤4 cells plus binary MILP optimization returned exact clique optima 8 and 16 with zero MIP gap.
5. **Upper witness:** the 24 monotone paths have unit determinant, pairwise-disjoint interiors, volume sum 24, profile `{4:12, 5:12}`, and cost 108. A separate LP check confirmed all 276 pair decisions.
6. **Spatial refinement:** the supplied `3^3 × 2` point domain gives `min(24e/v)=10`; multiplying by the spatial coordinate-volume factor 8 gives 80. This is closed only as the explicitly spatial-only, fixed-two-tick refinement stated by the runner.

There is no circular reduction or target-equivalent missing lemma inside the narrow combinatorial theorem. ProofObligationReviewer outputs **CONDITIONAL** because the physical realization premise must be explicit and the asserted saturation of 56 must be removed or proved.

## Import / support inventory

- `Z^3` nearest-neighbor adjacency: framework Lattice axiom; not an import or bounded-status source.
- equal tick/edge graining, where used: registered kinetic-isotropy primitive; not an import or bounded-status source, but its dependency edge is missing.
- tick-extended simplex/corner/dissection model and fixed-two-tick spatial refinement: supplied structural domain/boundary condition; acceptable for a bounded theorem only when named as supplied rather than attributed to the axioms.
- determinant normalization 24 and refinement factor 8: derived geometric normalizations.
- `TOL = 1e-9`: explicit, insensitive numerical nuisance for the LP comparator; the integer separator carries the exact predicate.
- measured/fitted/literature/PDG/cosmological/observational values: none.

ImportsSupportReviewer outputs **DISCLOSED** for numerical inputs, with the structural-domain attribution requiring the demotion/narrowing in Findings 2 and 7. The valid result is a bounded combinatorial theorem, not a retained physical assembly selection.

## Checks and governance record

- `python3 -m py_compile` passed.
- The changed runner completed in 218.97 s with 23 PASS / 0 FAIL; the committed cold transcript contains 23 PASS / 0 FAIL and its embedded receipt equals the committed JSON receipt.
- Independent checks: exact native/refined determinants and rational ratios; full cost≤4 barycentric-LP graph; exact MILP clique certificates; independent monotone-path LP/volume/cost check; manual sign/factor derivation of the 96 lower bound.
- Hard-coded targets were individually traced to the note. The native/refined counts, floors, ratios, cost profile, clique maxima, and 108 witness all received a non-self-confirming check. The full-graph edge/degree totals are descriptive and were reproduced by the changed runner but are not load-bearing on 96–108.
- `scripts/vocab_lint.py --report-only` reported zero mechanical violations; the manual native-language defect is Finding 8. No ambiguous bare letter-number primary science name appears. LabelingConventionReviewer: **PASS**.
- `git diff --check` and the repository-portable-link scan passed.
- A disposable-clone validation pipeline seeded `physical_scale_free_adjacency_dissection_bracket_cycle724_note_2026-08-03` as `bounded_theorem`, `unaudited`, with the three current edges identified in Finding 3. Full pipeline and strict lint completed with no errors (only repository-pre-existing warnings/notices); `check_changed_audit_evidence.py --base origin/main` reported the changed row evidence-ready. The tracked citation-graph manifest regenerated without drift. No audit verdict/effective-status artifact is in the five-file delta.
- The current review worktree was not modified outside this findings file; no source fix, verdict write, commit, push, or audit-worker run occurred.

## Disposition summary

Eight findings: one `BUG`, one `OVERCLAIM`, one `NO_GO_OVERCLAIM`, one `SEMANTIC_BRIDGE`, two `AUDIT_COMPATIBILITY` (one blocking-fix topology defect and one nonblocking ancestor disclosure), one `REPO_GOVERNANCE`, and one `NIT`. Fixed in this review: 0, because the task is review-only. The exact affine/census/lower-bound/bracket core is a salvageable bounded theorem and does not require new science: narrow the physical prose, remove the unsupported saturation statement, correct the dependency edges/manifest, and make the LP comparator fail closed. The branch does not meet the repo’s Nature-grade retention bar as submitted; after those fixes it is suitable to proceed as a bounded candidate for the independent audit worker.

## Review Results (Iteration 1)
### Code / Runner: RISK
### Physics Claim Boundary: BOUNDED
### Proof Obligations: CONDITIONAL
### Imports / Support: DISCLOSED
### Nature Retention: BOUNDED
### No-Go Discipline: FAIL
### Labeling Convention: PASS
### Repo Governance: FIX
### Audit Compatibility: FIX
### Methodology Skill: SKIPPED
### DISPOSITION: FIX_THEN_PROCEED
