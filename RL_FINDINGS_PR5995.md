# PR #5995 — Sole Combined Adversarial Science Review (Iteration 1)

Scope: stacked delta only, `3a01b7c0f7cc180cf043c3d38416cdce0c4b9a5c..867aff0edc16f64b5e8d5cc1022cbf9ce92b92de` (129 files). The supplied `RL_DIFF_PR5995.txt` matches this Git delta byte-for-byte.

Review mode: review-only. No repository source, audit verdict, commit, branch, or remote changes are authorized or made. Findings are recorded incrementally in this untracked review artifact.

Applicable lenses: CodeRunnerReviewer; PhysicsClaimBoundaryReviewer; ProofObligationReviewer; ImportsSupportReviewer; NatureRetentionReviewer; NoGoDisciplineReviewer; LabelingConventionReviewer; RepoGovernanceReviewer; AuditCompatibilityReviewer. MethodologySkillReviewer is not applicable because the exact 129-file delta changes no methodology skill or methodology source.

## Incremental review log

- Scope verification complete: the delta contains 17 new bounded-theorem notes, 34 runner logs, 44 output receipts, and 34 Python runners. Six Cycle 928 commits vendor a multi-cycle corpus and add the route-1 sweep claim. Ancestor/main dependency checks and science verification are in progress.

## Findings (incremental)

### F1 — BUG — CodeRunnerReviewer — the primary route-sweep PASS is forced by hard-coded negative gates

The runner does not test whether any real candidate satisfies the claimed license. For every non-planted candidate it sets both `R4_identification_is_derivable_not_alpha_1_nor_2pi_packaging = False` and `R5_scope_is_isolated_by_the_surface = False`, then defines `LICENSED` as the conjunction of all `R*` gates. Consequently every real candidate is rejected by construction and `D_NO_ROUTE_1_SURVIVOR` must pass regardless of the corpus ([`scripts/frontier_cycle928_route1_sweep_2026_07_28.py`](scripts/frontier_cycle928_route1_sweep_2026_07_28.py), lines 795–837 and 928–947). The positive-control survivor does not repair this: it bypasses the real gate path by passing a pre-filled all-true `planted` dictionary.

The same section hard-codes the exact-target and typing answers in `EXACTLY_TWO_THIRDS` and `ANGLE_TYPED`; the defined `exact()` parser is unused ([same runner](scripts/frontier_cycle928_route1_sweep_2026_07_28.py), lines 776–815). Its purported exhaustive angle-context check is also vacuous: the classifier emits only `CITATION...`, `EXCLUSION...`, `CODE SIGNATURE...`, or `OTHER`, while the assertion merely checks that no row equals the never-emitted string `DERIVED ANGLE OBJECT` ([same runner](scripts/frontier_cycle928_route1_sweep_2026_07_28.py), lines 687–713). Thus the runner cannot support the note's “zero survivors,” “exactly one genuinely angle-valued object,” or decisive type-gap theorem at [`docs/ROUTE1_SWEPT_EMPTY_TYPE_GAP_CYCLE928_BOUNDED_THEOREM_NOTE_2026-07-28.md`](docs/ROUTE1_SWEPT_EMPTY_TYPE_GAP_CYCLE928_BOUNDED_THEOREM_NOTE_2026-07-28.md), lines 9–31, 90–116, and 203–217. This is a blocking false-PASS defect, not a request for new science; the claim must be narrowed to a catalog/search report unless the gates are made evidence-driven and re-run.

The purported independent check does not catch this. Its `CK18` reimplements a different gate that accepts six supplied `True` arguments and then concludes that the *primary* sweep could have found a survivor, without exercising the primary's hard-coded-false path ([`scripts/frontier_cycle928_route1_sweep_independent_check_2026_07_28.py`](scripts/frontier_cycle928_route1_sweep_independent_check_2026_07_28.py), lines 483–495). Several attacks are unconditional `check(True, ...)`, and whether a held refutation “overturns” is an author-supplied Boolean rather than a tested consequence (lines 284–304, 336–355, 437–471, and 518–549). The checker even finds the enumeration incomplete but declares the added candidates non-overturning by prose adjudication. It is not an independent verification of the load-bearing gates.

### F2 — AUDIT_COMPATIBILITY — AuditCompatibilityReviewer — load-bearing ancestor note is absent from `origin/main`, and the dependency graph cannot see the imports

Cycle 928 explicitly load-bears on the Cycle 924 note and calls it part of its “full current price” ([Cycle 928 note](docs/ROUTE1_SWEPT_EMPTY_TYPE_GAP_CYCLE928_BOUNDED_THEOREM_NOTE_2026-07-28.md), lines 9–31, 118–134, and 178–193). The primary runner includes `docs/OCCURRENCE_ROUTE_PRICED_ALPHA_FREEDOM_UNIFIED_CYCLE924_BOUNDED_THEOREM_NOTE_2026-07-28.md` in mandatory `SOURCE_NOTES` and reads it unconditionally ([primary runner](scripts/frontier_cycle928_route1_sweep_2026_07_28.py), lines 86–92 and 150–154). That note exists in the stacked base but is absent from `origin/main`; applying this delta without the rejected/unlanded ancestor therefore raises `FileNotFoundError` before the runner can audit-ready execute.

Moreover, the Cycle 928 note links only its runners and receipts. Its load-bearing July no-gos, fixed-locus theorem, Cycle 924 package, vendored theorem packages, and scale-reference primitive are plain prose in the `Imports` section rather than markdown authority links (lines 176–193). A seeded audit row would therefore have missing/incorrect `deps` and could not enforce retained-grade dependency closure. This is `BLOCKED`, not merely provenance disclosure.

### F3 — SEMANTIC_BRIDGE — PhysicsClaimBoundaryReviewer / LabelingConventionReviewer — a permutation-space dimension pair is renamed as a physical Record weight pair

The reusable algebraic core is only that the permutation representation of a chosen free three-point `C3` orbit decomposes over `Q`/`R` as an invariant line plus a two-dimensional complement. The runner creates an unconstrained three-dimensional coefficient space by assignment (`coefficient_space_dim = n`) and asserts that Record additivity makes `I(x)=a_0x_0+a_1x_1+a_2x_2`; it never derives arbitrary scalar coefficients, `C3`-equivariance of the readout functional, or an identification of representation dimensions with readout/formation weights from the Record axiom ([`scripts/frontier_cycle883_record_weight_pair_2026_07_28.py`](scripts/frontier_cycle883_record_weight_pair_2026_07_28.py), lines 1013–1065). Record gives finite scalar additivity on disjoint record collections and content-only readout; it does not make the resulting scalar functional invariant under a chosen spatial subgroup or turn isotype dimensions into physical weights.

The label is also changed to keep the target numeral across scalar fields: over `C` the runner acknowledges the dimension decomposition is `(1,1,1)`, then replaces “dimension” by the *count* of nontrivial characters to recover `(1,2)` ([same runner](scripts/frontier_cycle883_record_weight_pair_2026_07_28.py), lines 1125–1155). That is a convention-dependent repackaging, not field-independent derivation of one physical pair. The note nevertheless says “the record carries the ordered weight pair (1,2) ... with NO free parameter” and that the datum “EXISTS in the axioms” ([`docs/RECORD_WEIGHT_PAIR_DERIVED_CYCLE883_BOUNDED_THEOREM_NOTE_2026-07-28.md`](docs/RECORD_WEIGHT_PAIR_DERIVED_CYCLE883_BOUNDED_THEOREM_NOTE_2026-07-28.md), lines 33–54 and 148–156), then consumes the renamed `2` as a multiplicative anchor at lines 70–90. Split the exact representation-theory lemma from the unproved Record-weight/readout identification; the latter remains an explicit bridge/open gate. As written this fails the labeling-convention gate (`SPLIT-REQUIRED`) and cannot be retained/Nature-grade.

### F4 — EQUIVALENT_STRENGTH_GAP — ProofObligationReviewer — excluding one proposed functional does not derive the other or close the readout obligation

The actual obligation graph is:

`Record(content-only scalar readout)` → **missing lemma A:** a physical record collection carries the freely chosen coefficient module used in Cycle 883 → **missing lemma B:** the readout is the particular `C3`-equivariant functional whose isotype dimensions may be normalized as `(n-1)/n^2` → `F_dim` → `2/9` → **missing h-unit/type bridge** → the target angle.

Cycle 901 proves at most a useful negative boundary about one candidate: `F_res`, when promoted to an unconditional function of records, depends on a separately named ambient subgroup/scope and can be multi-valued or undefined on the selected examples ([`docs/SPACE_IDENTIFICATION_DECIDED_FDIM_CYCLE901_BOUNDED_THEOREM_NOTE_2026-07-28.md`](docs/SPACE_IDENTIFICATION_DECIDED_FDIM_CYCLE901_BOUNDED_THEOREM_NOTE_2026-07-28.md), lines 43–79). It does not follow that the Record axiom positively chooses `F_dim`, much less its normalization, from the infinitely many total content-only scalar functions. The primary nevertheless turns a two-entry, author-declared candidate table into `DECIDED-F_DIM` and says the “positive half therefore rests entirely” on that family ([`scripts/frontier_cycle901_space_identification_2026_07_28.py`](scripts/frontier_cycle901_space_identification_2026_07_28.py), lines 1856–1890). Its own surviving steelman says the scope selector remains outside the axioms (lines 1602–1634), while the checker discloses that it tests structural anchor constants—not the content dependence of the physical readout value `I(x)` ([`scripts/frontier_cycle901_space_identification_independent_check_2026_07_28.py`](scripts/frontier_cycle901_space_identification_independent_check_2026_07_28.py), lines 587–594).

That missing positive-selection lemma is target-equivalent to the disputed binding rather than an incremental consequence of Record. The branch also explicitly classifies `LEMMA-882` as equivalent to the original readout obligation ([`docs/READOUT_IDENTITY_CLOSED_LIBRARY_WALL_CYCLE882_BOUNDED_THEOREM_NOTE_2026-07-28.md`](docs/READOUT_IDENTITY_CLOSED_LIBRARY_WALL_CYCLE882_BOUNDED_THEOREM_NOTE_2026-07-28.md), lines 74–85), then attempts to route around it through the invalid Cycle 883 bridge. Preserve the multi-scope counterexample as exact support; change `DECIDED-F_DIM` and “from the axioms” to an open/conditional two-candidate adjudication until a non-circular positive selection theorem is supplied.

### F5 — NO_GO_OVERCLAIM — NoGoDisciplineReviewer / NatureRetentionReviewer — the negative closeout fails N1–N8 and overstates finite searches as a terminal wall

The combined negative target is the claim that all derivation routes are closed and the remaining angle-scale license necessarily requires a new primitive. It fails the mandatory no-go audit:

- **N1 (route breadth): FAIL.** Cycle 928 consolidates only four top-level routes (angle-native theorem, Record normalization, occurrence/event rate, primitive), below the required five genuinely distinct route families, while ten in-window cycles and two quarantined packages are explicitly unswept/typing-only ([Cycle 928 note](docs/ROUTE1_SWEPT_EMPTY_TYPE_GAP_CYCLE928_BOUNDED_THEOREM_NOTE_2026-07-28.md), lines 65–79 and 118–134).
- **N2/N3 (independent and hidden walls): FAIL.** Type, referent, scope, forcedness, packaging, and primitive-exclusion gates are not shown pairwise independent. In the primary, scope and identification are hard-coded false (F1), so the apparent walls are coupled by construction. “Framework does not provide” and exclusion-clause rhetoric are used as hidden non-derivability premises.
- **N4 (witness/residual match): FAIL.** The checker finds that the charged-lepton referent in Cycles 886/888 is merely an imported circular-selector quotation, not a native derived referent ([`scripts/frontier_cycle928_route1_sweep_independent_check_2026_07_28.py`](scripts/frontier_cycle928_route1_sweep_independent_check_2026_07_28.py), lines 432–451). Moving that witness between bins by editorial adjudication does not establish the same obstruction.
- **N5 (rhetoric resolutions): FAIL.** “Last live route,” “wall,” “closes the loop,” and “wrong number forever” at Cycle 928 lines 9–31 and 203–217 exceed the explicitly finite corpus. Similar unqualified terminal language appears in Cycle 890 (“scope is not derivable,” lines 195–202), Cycle 903 (“terminal supplied,” lines 43–63), and Cycle 904 (“selection question dies its final death,” lines 170–178).
- **N6 (reframe/convention test): FAIL.** A scale-reference primitive's explicit refusal to supply mixing angles/phases proves only that *that primitive* is not the license. It does not rule out a theorem, a convention/definition, another already-granted primitive, or a corrected semantic identification. Thus “measured to need a NEW primitive” is not derived (Cycle 928 lines 128–134).
- **N7 (steelman): FAIL.** The strongest survivor is the possibility of an unenumerated or misclassified native angle-bearing construction; the checker itself finds incomplete enumeration and missing keyword coverage. It is not constructed and tested as a genuine rival.
- **N8 (cross-cycle echo): FAIL.** Prior cycles repeatedly change the operative wall—from grammar, to closed libraries, to scope, to multiplicity-freeness, to type—without a cross-cycle table showing which hypotheses/witnesses persist and which earlier claims are retired. Cycle 882's own equivalent-strength lemma remains open.

Cycle 872's “compact N-gate” is a route summary, not a visible N1–N8 audit ([`docs/SIGMA_LINEAR_ADMISSIBILITY_CLASSIFICATION_CYCLE872_BOUNDED_THEOREM_NOTE_2026-07-28.md`](docs/SIGMA_LINEAR_ADMISSIBILITY_CLASSIFICATION_CYCLE872_BOUNDED_THEOREM_NOTE_2026-07-28.md), lines 99–111); Cycle 882 likewise supplies only “N-gate essentials” (lines 109–117). The bounded enumerations can be retained as partial attempts with named untested routes, but the cross-package no-go/terminal conclusion must be rejected. This is science-needed under the active review-queue precedent; wording alone cannot cure absent N1–N8 evidence.

### F6 — IMPORTED_VALUE — ImportsSupportReviewer — Cycle 899's fitted enclosure is an unpinned hard-coded comparator

Both Cycle 899 runners hard-code the Cycle 897 fitted enclosure as exact rational literals (`0.222222047073817229` to `0.222222047073817230`) ([`scripts/frontier_cycle899_family_binding_2026_07_28.py`](scripts/frontier_cycle899_family_binding_2026_07_28.py), lines 139–141; [`scripts/frontier_cycle899_family_binding_independent_check_2026_07_28.py`](scripts/frontier_cycle899_family_binding_independent_check_2026_07_28.py), lines 113–115). Neither Cycle 897 source nor its receipt is in either runner's `AUDIT_INPUT_PATHS`; the primary's input closure is only the ten files at lines 65–78, yet its docstring says “all pinned, none imported” and “All cited artifacts” are pinned (lines 6 and 55–58). The independent checker copies the same literals, so it is not an independent provenance check.

The note calls Q3 “empirically clean,” reports nearest distances and a denominator lower bound, and then omits Cycle 897 entirely from the `Imports` list ([`docs/FAMILY_BINDING_FDIM_CYCLE899_BOUNDED_THEOREM_NOTE_2026-07-28.md`](docs/FAMILY_BINDING_FDIM_CYCLE899_BOUNDED_THEOREM_NOTE_2026-07-28.md), lines 94–114 and 141–163). The exact transform-space search is valid *conditional on that enclosure*, but the fitted/measured comparator must be named, linked, digest-pinned, and classified as an import; absent that, Q3 is support-only and cannot contribute retained/Nature-grade evidence.

### F7 — MISSING_ARTIFACT — AuditCompatibilityReviewer / ImportsSupportReviewer — Cycle 916 is reproducible only from local unreachable Git objects

Cycle 916 says convention B was “fully re-executed from history,” “B runs only from history,” and emits a “never-landed-dependency row” ([`docs/THETA_DICTIONARY_DECAY_HOLDS_CYCLE916_BOUNDED_THEOREM_NOTE_2026-07-28.md`](docs/THETA_DICTIONARY_DECAY_HOLDS_CYCLE916_BOUNDED_THEOREM_NOTE_2026-07-28.md), lines 43–58). The primary's `HISTORY` table consumes nine raw blobs, and `recover_history()` unconditionally executes `git cat-file blob <sha>` before checking their digests ([`scripts/frontier_cycle916_theta_reconciliation_2026_07_28.py`](scripts/frontier_cycle916_theta_reconciliation_2026_07_28.py), lines 110–151 and 291–318). All nine blobs are absent from `git rev-list --objects origin/main`; the two named source commits `edf69d3c70eb06ecbe5744c974bfefc6b1bbf1b0` and `8f75f76ca28b50748f2398f5339babf93c3fde19` are also not ancestors of `origin/main`. The checker independently repeats raw `git cat-file` access (lines 146–153), so it shares the same unavailable object store rather than establishing clone-level independence.

This is load-bearing, not provenance-only: a fresh normal clone cannot materialize convention B and fails before reaching the claimed comparison/re-execution. Vendor the exact source/cache artifacts or add a reachable, immutable fetch authority and test from a fresh clone. Until then the Cycle 916 measurement is support-only and audit compatibility is `BLOCKED`.

### F8 — AUDIT_COMPATIBILITY — AuditCompatibilityReviewer — twenty runners hard-fail on the current `origin/main` axiom bytes

The branch's `MINIMAL_AXIOMS_2026-06-29.md` SHA-256 is `fc4d60cce8154...`; current `origin/main` is `53175250f045...`. Twenty of the 34 changed runners pin the former bytes (representative sites: [`scripts/frontier_cycle883_record_weight_pair_2026_07_28.py`](scripts/frontier_cycle883_record_weight_pair_2026_07_28.py), line 112; [`scripts/frontier_cycle899_family_binding_2026_07_28.py`](scripts/frontier_cycle899_family_binding_2026_07_28.py), line 98; [`scripts/frontier_cycle916_theta_reconciliation_2026_07_28.py`](scripts/frontier_cycle916_theta_reconciliation_2026_07_28.py), line 81; [`scripts/frontier_cycle921_loop_cost_2026_07_28.py`](scripts/frontier_cycle921_loop_cost_2026_07_28.py), line 114). Their hard-fail preflights therefore reject the current main premise surface before any science check runs.

This is not merely a checksum refresh: current main strengthens/clarifies Admissibility as a probability-distribution rule, so the dependency/axiom impact guard requires an explicit impact review of claims that classify “axiom-available” constructions, admissible families, or derive non-supply from byte searches. Rebase/update the pins and show whether each result is unchanged; otherwise the package is not ready for the independent audit worker on current main.

### F9 — BUG — CodeRunnerReviewer — the committed Cycle 928 PASS cannot be reproduced at this PR's own HEAD

A clean detached worktree at `867aff0e` compiles all 34 changed Python files, but a fresh execution of the primary exits 1 with `TOTAL: PASS=46 FAIL=2; VERDICT: FAIL`. Its two mandatory restriction gates invoke old no-go runners ([`scripts/frontier_cycle928_route1_sweep_2026_07_28.py`](scripts/frontier_cycle928_route1_sweep_2026_07_28.py), lines 277–297); both invoked runners crash because they still require the removed monolithic `docs/audit/data/audit_ledger.json`. The primary ignores each subprocess return code/stderr and records only a missing expected stdout string, yielding `FAIL B1_ANGLE_NATIVE_NO_GO_REPRODUCED` and `FAIL B2_STRETCH_NO_GO_REPRODUCED_924_AUDIT_ROW_1_CONFIRMED`. This review did not read the prohibited ledger; the failure is the current tree's missing path and stale runner dependency.

The committed cache nevertheless reports those same gates as PASS and the primary as `PASS=48 FAIL=0`, so the checked-in receipt/log are stale relative to their executable closure. Running the changed independent checker immediately afterward also exits 1 (`PASS=20 FAIL=1; VERDICT: PRIMARY_REFUTED`) because it reads the freshly failed primary receipt. The package therefore fails its own restriction-gate order and is not runnable/auditable even before the hard-coded-census defect in F1 is considered. Replace the legacy ledger reads with per-claim shard access, require child `returncode == 0`, and regenerate both receipts from a clean clone/worktree.

### F10 — NO_GO_OVERCLAIM — CodeRunnerReviewer / ProofObligationReviewer — Cycle 882's “exact wall” confuses monoids, semigroups, and truncated exponent samples

The load-bearing theorem says every multiplicatively closed anchor library contains `1`, hence no such library can isolate the target ([`scripts/frontier_cycle882_readout_identity_2026_07_28.py`](scripts/frontier_cycle882_readout_identity_2026_07_28.py), lines 1105–1114 and 1157–1166; [`docs/READOUT_IDENTITY_CLOSED_LIBRARY_WALL_CYCLE882_BOUNDED_THEOREM_NOTE_2026-07-28.md`](docs/READOUT_IDENTITY_CLOSED_LIBRARY_WALL_CYCLE882_BOUNDED_THEOREM_NOTE_2026-07-28.md), lines 65–72). That assertion is false without a finite-monoid hypothesis. A multiplicatively closed subset/semigroup need not contain the identity; for example `{(2/9)^n : n >= 1}` is closed under multiplication and omits `1`. Conversely, the runner's sampled sets always contain `1` only because every exponent range includes the all-zero exponent (lines 1120–1129), while a bounded exponent window is itself not closed under multiplication once products leave the window.

The independent checker repeats the same mistake: its purported “semigroup” uses `range(0, w+1)`, including exponent zero/empty product by construction, and again uses a bounded non-closed window ([`scripts/frontier_cycle882_readout_independent_check_2026_07_28.py`](scripts/frontier_cycle882_readout_independent_check_2026_07_28.py), lines 631–685). It therefore cannot refute identity-free semigroups. The primary also inconsistently unions `{0}` into sampled survivors (line 1131) but omits it from the singleton tightness control (lines 1148–1154), so the selection predicate is not applied uniformly. The valid salvage is limited to finite nonzero multiplicative subsemigroups of `Q*` (or explicitly unit-containing libraries/monoids) and to the enumerated generator windows as a search result. The advertised theorem over “any closed algebraic structure,” its exact-wall consequence, and downstream terminal use fail.

### F11 — SUPPORT_ONLY_DEMOTION — NatureRetentionReviewer / PhysicsClaimBoundaryReviewer — Cycle 921 is a finite numerical classifier, not a derived mechanism law

The exact graph identity `shortest pointer-through cycle length = anchor distance in G\{pointer} + 2` is sound and reusable. The physical three-regime “pair-cycle law,” however, is installed as a field-branched prediction by construction: at `lambda=0.05` the code ignores distance-2 dependence edges, while at `0.075` and `0.1` it includes them through a literal branch table ([`scripts/frontier_cycle921_loop_cost_2026_07_28.py`](scripts/frontier_cycle921_loop_cost_2026_07_28.py), lines 623–640 and 1708–1715). No dynamical derivation predicts that crossover or the content/independence thresholds; the rule is scored against the same finite measurement surface used to identify it. The verdict then names a “surviving mechanism” by hit count even though it misses the loop-free degree-2 chain and assigns that miss to an unexplained second channel (lines 1877–1908).

The note accurately discloses `42/42, 42/42, 41/42`, the exception, frozen fields/gates, and numerical tolerances ([`docs/LOOP_COST_PAIR_CYCLE_LAW_CYCLE921_BOUNDED_THEOREM_NOTE_2026-07-28.md`](docs/LOOP_COST_PAIR_CYCLE_LAW_CYCLE921_BOUNDED_THEOREM_NOTE_2026-07-28.md), lines 62–118 and 128–152), but still says the loop cost is “EXPLAINED” and routes the mechanism as a theorem (lines 9–21 and 173–182). Preserve it as bounded measured support/a model-selection result, with the exact graph identity split out. It is not Nature-retained mechanism science and cannot carry a fundamental closure claim.

### F12 — REPO_GOVERNANCE — LabelingConventionReviewer / RepoGovernanceReviewer — new science surfaces use bare workstream codes and branch-local campaign vocabulary

The delta introduces code-like labels as primary scientific names rather than descriptive names with parenthetical aliases: `SL0` in the Cycle 886 filename/title, `SL1b` as the target in Cycle 899 lines 9–16 and 118–125, `M2`/`M4` as headline route names in Cycle 898 lines 9–18 and 42–64, `C901-T2a` and `C901-T7` as theorem names in Cycle 901 lines 54–79 and 110–117, and bare `G1` for the Cycle 921 exception at lines 128–136. `C3`/`C4` as standard cyclic groups are allowed; these workstream/route identifiers are not. The controlled vocabulary requires the scientific object to be the primary name and permits legacy shorthand only after it as an alias (`docs/repo/CONTROLLED_VOCABULARY.md`, lines 73–110).

Repo-facing notes and receipts also repeatedly use branch-only process language such as “owner-directed window 2/2b,” campaign block IDs, and `toe-time-blockG*` as durable framing. Translate those into native scientific scope/provenance fields before merge. This is a mechanical naming/governance fix; it does not demand new science, but the labeling result is `SPLIT-REQUIRED` because the same labels currently conflate exact lemmas, bounded searches, and target-route closures.

### F13 — AUDIT_COMPATIBILITY — AuditCompatibilityReviewer / RepoGovernanceReviewer — the claimed audit rows are embedded prose, not dispatchable audit work

Cycle 928 says nine audit rows are “emitted” ([Cycle 928 note](docs/ROUTE1_SWEPT_EMPTY_TYPE_GAP_CYCLE928_BOUNDED_THEOREM_NOTE_2026-07-28.md), lines 45–51 and 185–201), but the implementation only places nine free-text dictionaries inside the runner receipt ([`scripts/frontier_cycle928_route1_sweep_2026_07_28.py`](scripts/frontier_cycle928_route1_sweep_2026_07_28.py), lines 1058–1145). The delta changes no `docs/audit/data/` shard, supported dispatcher sidecar, active review queue, or dispatch queue. Consequently those requests are not machine-visible to the audit worker. A bounded readiness run of `check_changed_audit_evidence.py --base origin/main` reports `checked=0`, confirming that none of the 17 new non-meta claim notes is represented as changed audit evidence on this branch.

All 17 notes have only three or four markdown links: their own primary/checker and receipts. Their `Imports` sections name load-bearing source notes/primitives only in prose. The independent auditor receives only the source note and its directly cited authorities (`docs/audit/README.md`, lines 509–521), so it would not receive the declared proof/import closure. Seeded rows would immediately face `missing_dependency_edge`. Add real dependency links, seed/validate the claim shards through the normal pipeline, and use supported dispatcher metadata for the requested follow-up rows without applying verdicts. Until that mechanical preparation passes, Audit Compatibility is `BLOCKED`.

### F14 — SALVAGE_CANDIDATE — all science lenses — narrow exact results can be preserved without the rejected closeout

The branch is not a total science loss. The following units are separable from the failed bridges/no-go rhetoric and are candidates for bounded support after pin/link repairs and clean-run receipts:

- Cycle 872's exact algebra on the declared grammar, including the trace-free/conformal projection and its landed trace-zero consequence (`scripts/frontier_cycle872_sigma_linear_admissibility_2026_07_28.py`, lines 138–150 and 297–343).
- Cycles 876/895's exact grading normal form `w(t)=(1,1+t,1-t)`, residual `A+tB`, and sector trace `A` (`scripts/frontier_cycle876_unit_grading_provenance_2026_07_28.py`, lines 481–511 and 831–915; `scripts/frontier_cycle895_t_retirement_2026_07_28.py`, lines 1553–1610).
- Cycle 883's purely representation-theoretic `Q[C3]` permutation-module split `1+2`, with all Record/physical-weight language removed.
- Cycle 899's algebraic identities: the five declared expressions collapse to `(n-1)/n^2`, and the geometric fixed-locus sum is `(n^2-1)/(12n)`, conditional on the explicitly chosen modules; the Cycle 897 fitted comparison remains imported support.
- Cycle 900's correctly signed origin equation for `(Delta-mu^2)G=-delta`, `G(0)-G(e1)=(1-mu^2G(0))/6`, and the consequent massless-slice statement under `G(0)>0` (`scripts/frontier_cycle900_harmonic_repair_2026_07_28.py`, lines 1210–1228).
- Cycle 904's explicit witness `diag(Qp)/totalsum(J)=(n-1)/n^3`, giving `2/27` at `n=3`, as reachability-only evidence; and Cycle 921's exact graph-distance/cycle-length identity plus its finite measurement table as support.

Do not salvage Cycle 882's unrestricted identity obstruction, Cycle 901's positive `F_dim` selection, or Cycle 928's “type-gap/new primitive” closure. The appropriate overall disposition is therefore `FAIL`, not `SALVAGE_REJECT`.

### F15 — MISSING_ARTIFACT — CodeRunnerReviewer / AuditCompatibilityReviewer — the vendored multi-cycle corpus omits load-bearing inputs for numerous changed runners

A static expansion of top-level `AUDIT_INPUT_PATHS`/`PINS` found that eleven changed runners contain 25 direct references to twelve unique paths missing from this worktree; ten of those unique paths are also absent from `origin/main`. These are executable inputs, not optional citations. For example:

- Cycle 872 declares two source runners that are absent both here and on main, then unconditionally reads every `AUDIT_INPUT_PATHS` entry (`scripts/frontier_cycle872_sigma_linear_admissibility_2026_07_28.py`, lines 38–45 and 1579–1585).
- Cycle 895 unconditionally reads its inputs at lines 829–835, but the Cycle 873 primary/receipt and Cycle 880 primary/receipt named at lines 83–98 are absent here and on main.
- Both Cycle 900 runners require the absent Cycle 884 primary/cache (the primary additionally requires the absent Cycle 884 checker); their input reads are unconditional (`scripts/frontier_cycle900_harmonic_repair_2026_07_28.py`, lines 92–99 and 295–309, 567–570).
- Cycle 921's primary hard-pins thirteen Cycle 914/915/917/919 files that are absent here and on main, and `verify_pins()` exits on the first missing path (`scripts/frontier_cycle921_loop_cost_2026_07_28.py`, lines 100–158 and 219–232). Its own load-bearing primary receipt was also omitted: the source note's link at `docs/LOOP_COST_PAIR_CYCLE_LAW_CYCLE921_BOUNDED_THEOREM_NOTE_2026-07-28.md:28-31` is broken, and the changed checker requires that same nonexistent receipt at `scripts/frontier_cycle921_loop_cost_independent_check_2026_07_28.py:69-89`.

Cycle 916 adds the separate unreachable-object problem in F7. These omissions explain why committed caches can exist while the shipped runner closure cannot be reconstructed. Vendor or otherwise provide every load-bearing input on a reachable reviewed surface, repair the broken receipt link, and regenerate from a clean clone. Until then multiple individual claim rows—not only Cycle 928—are ineligible for independent audit execution.

## Load-bearing formula, sign, and normalization verification record

Every changed math-bearing primary was compared against its note, with its paired checker inspected for genuine independence. The per-cycle result is:

| Cycle | Formula/sign/normalization result |
|---|---|
| 872 | Exact conformal projection `/3` and landed `(-2w,w,w)` trace agree; conclusion is bounded to the enumerated grammar. |
| 876 | `w(t)=(1,1+t,1-t)`, `A+tB`, and `trace=A` agree; the unit choice remains a disclosed supplied grading. |
| 882 | `I_alpha(1,1,1)=3 alpha`, hence `alpha=2/27` for `2/9`, agrees; T7 multiplicative-wall logic fails (F10). |
| 883 | `Q/R` permutation representation gives dimensions `1+2`; normalization/physical Record identification fails (F3). |
| 886 | Exact subgroup, Burnside, nullspace, and rational-isotype census is internally normalized; derivation-refusal rhetoric remains a bounded/no-go issue (F5). |
| 888 | Independent group/algebra census identities agree; selector/no-go conclusion is bounded and does not repair Cycle 883's bridge. |
| 890 | Multiplicity census arithmetic agrees on its enumerated scopes; byte-search absence is not a proof that multiplicity-freeness is non-derivable. |
| 895 | Affine residual and sign convention agree exactly; safe as bounded algebra (F14). |
| 898 | Exhibited additivity and involution rows reproduce their note; “route dies” is only within declared readings/families and fails terminal no-go discipline. |
| 899 | `F_dim`, `F_res`, `F_ded`, and fixed-locus normalizations agree; Record binding and fitted-comparator provenance fail (F3/F6). |
| 900 | Screened Green-function sign and factor `1/6` agree; massless equivalence needs the stated positive `G(0)` domain and is safely bounded. |
| 901 | `F_dim(3)=F_res(3)=2/9`, `F_dim(4)=3/16`, `F_res(4)=5/16` agree; the selection inference is the missing lemma (F4). |
| 903 | Sigma's unit/dimensionless decomposition and exact theta-incidence code match the note; primitive exclusion does not prove “terminal supplied.” |
| 904 | `diag(Qp)/totalsum(J)=(n-1)/n^3` and `2/27` at `n=3` agree; reachability does not establish a unique physical selector. |
| 916 | Theta A/B/C subtraction signs match their written definitions; numerical reproduction is not clone-reproducible because its history inputs are missing (F7). |
| 921 | Graph distance/cycle-length normalization and finite ceilings match; the field switch is hard-coded and remains measured support (F11). |
| 928 | The narrow `2 pi k/n = 2/3 => pi=n/(3k)` obstruction is correct for nonzero `k`; the real-candidate gates and fresh execution fail (F1/F9). |

## Verification and classification summary

- **Bugs / false PASS:** F1, F9, and the executable part of F10.
- **Overclaims / no-go / proof gaps / semantic bridges:** F3, F4, F5, F10.
- **Imported-value and missing-artifact problems:** F6, F7, F15.
- **Support-only demotions:** F11, plus the bounded portions listed in F14.
- **Repo governance / labeling:** F12.
- **Audit compatibility:** F2, F7, F8, F13, F15.
- **Salvage:** F14; no `SALVAGE_REJECT` finding is warranted.
- **Nits:** none reported; every retained finding is material to claim scope, reproducibility, provenance, naming, or audit readiness.

Bounded checks: all 34 changed Python files pass `py_compile` with bytecode redirected outside the worktree. A clean detached-HEAD Cycle 928 run fails `46/2`, and its checker then fails `20/1`; those fresh artifacts were confined to and removed with a temporary worktree. `check_changed_audit_evidence.py --base origin/main` exits 0 but checks zero rows, which is itself the missing-seeding/readiness evidence in F13. No monolithic ledger file was read. No repo source, audit verdict, commit, branch, or remote was changed.

## Review Results (Iteration 1)
### Code / Runner: FAIL
### Physics Claim Boundary: REJECT
### Proof Obligations: EQUIVALENT-GAP
### Imports / Support: FAIL
### Nature Retention: REJECT
### No-Go Discipline: FAIL
### Labeling Convention: SPLIT-REQUIRED
### Repo Governance: FIX
### Audit Compatibility: BLOCKED
### Methodology Skill: SKIPPED
### DISPOSITION: FAIL
