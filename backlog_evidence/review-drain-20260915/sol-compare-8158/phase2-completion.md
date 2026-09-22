# PR 8158 independent comparison review — phase 2 completion

Phase-one report remains frozen and unchanged. Verdict remains **FAIL**. This continuation reads broader source and parent context; it is not a second reviewer or a fresh finding from another seat.

## Additional material findings

4. **A finite static-law pair is promoted to an all-axiom model pair.** The note says “Two models satisfying every axiom sentence used” (note lines 44–47) and Q5(a) repeats it (lines 129–133). Its declared objects and proofs define only normalized finite static laws R1/R2 (lines 79–85, Q1–Q4). They do not construct a record-formation process, permanent/readable records, a global or full-domain extension, or a rule whose conditional probabilities vary with nearest-neighbor conditions for each model. The actual campaign parent explicitly requires formation, Record, readout, global consistency and relevant primitive checks when claiming a model-pair witness (`docs/TOE_DERIVATION_CAMPAIGN_AXIOM_SUFFICIENCY_BY_UNDERDETERMINATION_WITNESSES_NOTE_2026-09-13.md`, lines 34–66). Thus the exact cube TV can demonstrate a difference between two *declared static readings*, but not by itself two complete models of every quoted axiom. Narrow salvage: call them finite static-law constructions under alternative supplied readings; keep the separating clause as a proposed distinction, without the all-axiom witness label.

5. **The citation graph records no parents for the new load-bearing theorem.** The note front matter lists `minimal_axioms`, the possibility-covariance note, and block 01 as `upstream_dependencies` (note lines 5–8), and the proof uses their status as named inputs (lines 75–83, 155–160). Yet the changed `docs/audit/data/citation_graph_manifest.json` adds the new node with `deps_hash: e3b0c44298fc` and `out_degree: 0` (original delta to `dd78e677`), the SHA-256 prefix of an empty dependency list. The changed note cites file paths in inline code instead of linked authority references. This leaves a new theorem’s load-bearing dependency topology invisible in the submitted graph acknowledgment. Narrow salvage: use repository-relative Markdown links to the actual authority notes and regenerate the manifest from corrected topology. No audit verdict should be carried.

## Parent and premise coverage

- Current-main parent blob identities at `9ff59dc9`: block 01 `ec3bb81397ea1b136c4040c69832ad1a1bc9ee76`; possibility-covariance note `eb9f897127d2db9b2f3226abd1e93311188fdcee`; campaign meta note `8a4323aa1529ebc3b755f269d8e033292582bee9`; axiom memo `bc23300becfe4e4db57153c0e94cfcdf2338da71`.
- Block 01 Theorem A, lines 195–259, proves uniqueness of its positive finite static product law **under its named full-conditional reading**, and lines 73–145 explicitly distinguish records-only, absence-as-condition, and marginal readings. It supplies a conditional static construction, not an axiom-selected treatment of unrecorded sites.
- The possibility-covariance note’s sphere section, lines 185–206, treats the sphere as a supplied pure-state restriction and distinguishes unsoldered and diagonal cubic actions; it does not select a physical sphere law or the new exponential coupling.
- The campaign meta note, lines 34–66 and 162–175, calls the unrecorded-site interpretation a research hypothesis and requires complete premise checks for an all-axiom model-pair claim.
- Read the current-main axiom memo, primitive registry/check and registered primitive sources for premise authority. The primitive notes supply no missing reading of unrecorded sites.

## Original source and current-main disposition

Original source identity: PR head `dd78e677ba6cda496d6de20cfc215ef8bd09374f`, delta base `df5316ee81d59d573b3837afb80d371d12d890d6`, inventory `/private/tmp/review-drain-20260915/drain8158-original-inventory.json` (22 paths). `git cat-file -t` confirms the original commit remains reachable locally. Current main is `9ff59dc9caf61444b8bf3bd3d0d13ea53ace1dac`. No reviewed content was landed or discarded by this seat. “Absent” below means not present at that path on current main, but the original blob is recoverable from the frozen PR head; “changed” means main has a separate blob at the same path. The disposition is preservation/recovery, not approval to land as-is.

| # | Original path | Original blob | Current main | Source/claim disposition |
|---:|---|---|---|---|
| 1 | `.claude/science/physics-loops/admissibility-induced-law-20260906/APPROACH_REGISTRY.md` | `2b81f9187ba7` | changed 8f9c496033ee | campaign history/state; retain original in PR commit; reconcile only if claims corrected |
| 2 | `.claude/science/physics-loops/admissibility-induced-law-20260906/ASSUMPTIONS_AND_IMPORTS.md` | `3e36d47c89d9` | changed e99dd0e244c2 | campaign history/state; retain original in PR commit; reconcile only if claims corrected |
| 3 | `.claude/science/physics-loops/admissibility-induced-law-20260906/CHECKER_block24_findings.md` | `2b69853a455c` | absent | opaque historical finding/output; inventory only, not read for blind review |
| 4 | `.claude/science/physics-loops/admissibility-induced-law-20260906/CLAIM_STATUS_CERTIFICATE_block24.md` | `befd5da70064` | absent | block24 claim/provenance; preserve; correct overclaims before any landing |
| 5 | `.claude/science/physics-loops/admissibility-induced-law-20260906/GOAL_block24.md` | `f137b09788ef` | absent | block24 claim/provenance; preserve; correct overclaims before any landing |
| 6 | `.claude/science/physics-loops/admissibility-induced-law-20260906/HANDOFF.md` | `31e4296b5da2` | changed 6dfc9de13838 | campaign history/state; retain original in PR commit; reconcile only if claims corrected |
| 7 | `.claude/science/physics-loops/admissibility-induced-law-20260906/LITERATURE_BRIDGES.md` | `488b0d3e63cc` | changed 9ccaee75bb42 | campaign history/state; retain original in PR commit; reconcile only if claims corrected |
| 8 | `.claude/science/physics-loops/admissibility-induced-law-20260906/NO_GO_LEDGER.md` | `a8966b7bf9bb` | changed 2977b7f9903b | campaign history/state; retain original in PR commit; reconcile only if claims corrected |
| 9 | `.claude/science/physics-loops/admissibility-induced-law-20260906/OPPORTUNITY_QUEUE.md` | `73909cadade2` | changed 74d2f60bae1b | campaign history/state; retain original in PR commit; reconcile only if claims corrected |
| 10 | `.claude/science/physics-loops/admissibility-induced-law-20260906/RESULTS_block24.md` | `c3b0ee109d64` | absent | block24 claim/provenance; preserve; correct overclaims before any landing |
| 11 | `.claude/science/physics-loops/admissibility-induced-law-20260906/REVIEW_HISTORY.md` | `8f89c64f620c` | changed 08d17f0940e3 | opaque historical finding/output; inventory only, not read for blind review |
| 12 | `.claude/science/physics-loops/admissibility-induced-law-20260906/ROUTE_PORTFOLIO.md` | `06a6b19ce05f` | changed 9b1cd3a27f32 | campaign history/state; retain original in PR commit; reconcile only if claims corrected |
| 13 | `.claude/science/physics-loops/admissibility-induced-law-20260906/STATE.yaml` | `41b20051b2da` | changed e16642020759 | campaign history/state; retain original in PR commit; reconcile only if claims corrected |
| 14 | `.claude/science/physics-loops/admissibility-induced-law-20260906/TRACE_GATE.md` | `0ff62c310bd5` | changed 8f432e2cd263 | campaign history/state; retain original in PR commit; reconcile only if claims corrected |
| 15 | `.claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block24_refuter.out.txt` | `7985dab4a907` | absent | opaque historical finding/output; inventory only, not read for blind review |
| 16 | `.claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block24_refuter.py` | `09caf12beb84` | absent | historical control source; read as source, no execution |
| 17 | `.claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block24_unrecorded_sites.out.txt` | `ed78f8df19ff` | absent | opaque historical finding/output; inventory only, not read for blind review |
| 18 | `.claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block24_unrecorded_sites.py` | `08a99142e08e` | absent | historical control source; read as source, no execution |
| 19 | `docs/ADMISSIBILITY_RULE_UNRECORDED_SITES_FREE_WINDOW_VERSUS_INTEGRATED_EXTERIOR_READINGS_DIFFER_IFF_AN_UNRECORDED_COMPONENT_TOUCHES_TWO_RECORDED_SITES_BOUNDED_THEOREM_NOTE_2026-09-15.md` | `6114b13d508c` | absent | canonical theorem note; block as-is; salvage Q1/Q2/narrow Q3/Q4 |
| 20 | `docs/audit/data/citation_graph_manifest.json` | `59aa39de5dd7` | changed bc5927ec7f3c | topology acknowledgment; regenerate after corrected source links |
| 21 | `logs/runner-cache/admissibility_rule_unrecorded_sites_free_window_versus_integrated_exterior_readings_2026_09_15.txt` | `62ecdf827091` | absent | primary cached evidence; preserve original; refresh only after corrected runner |
| 22 | `scripts/admissibility_rule_unrecorded_sites_free_window_versus_integrated_exterior_readings_2026_09_15.py` | `9345102c8c45` | absent | primary runner; block as-is; correct lattice witness/scope |

## Review coverage and limits

- Read complete original canonical note and primary runner; original source of the two supervisor control scripts without executing them; changed block24 goal, results, certificate, assumptions/imports, trace and campaign history diffs; changed citation manifest and primary pinned cache; actual load-bearing parent arguments and campaign method contract on current main. Original opaque reviewer findings, reviewer history and control output files were inventoried by path/blob only, not read.
- The primary runner, control scripts, pipeline, audit and GitHub were not run or mutated. The simple parity, constant-rule and spectral checks in phase one remain the independent controls. No new numeric witness was calculated in phase two.
- Current-main preservation is path/blob identity only; it does not imply the PR source is current, valid, or that later main changes have been semantically merged. The corrected candidate needs its own exact-current-main loss check and final validation by the owner review lane.
