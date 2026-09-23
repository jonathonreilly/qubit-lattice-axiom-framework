# PR8177 original independent review

**FIX BEFORE SOURCE CONFIRMATION.** Frozen head `9e98fd751435c1b65898f8e3058250a2e56d9703`; original base `9a3ffc8d913c6f09d822ef19975073d93df0f8ee`; current main `1bb8b7befb857852acaed93bcf2bb1e47925b013`. Same reviewer session `/root/review_8177`. This is source review, not an audit or landing PASS.

## 8177-01 — PROOF_OBLIGATION

note T1.3, scope, N1.3, single-seed remark

The written induction establishes H iff the tight-sibling statement, and H implies the unrooted unit budget. It omits the converse and treats finite-window and all-Z3 realizations interchangeably. The single-seed saturated-support remark further calls the residual a local marks statement without proving that reduction.

**Correction:** Preserve extension/seed proofs and exhaustive induction. State H as a sufficient condition for the unit budget, or explicitly define a finite window class closed under level truncation and prove the converse by truncating at the queried level (kinds unchanged), applying the universal budget there, and using extension for amplified sites. Do not silently extend truncation to a full forward automaton with finite marks; it may generate sites above the cap. Saturation is only below the cap; keep the claimed local characterization conjectural. This is an open equivalent-strength residual, not near closure.

## 8177-02 — OVERCLAIM

note T3.2; runner rhs lines 513-520; historical restricted_count/refuter

The three-variable recursion is not the exact one-processed-child count. At a D entry the entering edge already comes from a successor whose arrow points to the current node. If that successor is processed, the sole processed-child allowance is consumed, but U2 permits another. Independent enumeration gives 8 remaining assignments against 4 legal ones with unit weights. The kind-typed code has the same omission.

**Correction:** Salvage the unchanged polynomial as a relaxed lifted-tree upper bound, prove every admissible restricted lattice tree injects into that relaxed family, explain the ignored incoming-child occupancy and collisions. All eight rational certificates remain valid. Do not call the helper an independent derivation of the exact restricted family.

## 8177-03 — BUG

note T2/scope/introduction; runner family_c C1/C2; cache

Scope and C1 message say all three predecessors of both tight roots have value -1, while Z_B is explicitly [-1,-1,0]. C1 only checks min=-1 and pair minimum<=-1, not the stated exact profile. Primary E1 produces 120 equal minima, zero differences, contrary to note phrase differ in a few. N5 says70 tiny realizations while B uses140.

**Correction:** Correct all summaries and precise C1 assertions to Z_A[-1,-1,-1], Z_B[-1,-1,0]; keep Z_B second tight site predecessor values[-1,-1,-1]. Scope finite absence observations and counts exactly; regenerate evidence on corrected frozen source.

## 8177-04 — OVERCLAIM

note T4 and optimal-tree summaries; shape.py solve_restricted; shape2.py

The125-case MILP R1 restricts only processed parents, not every node. shape2 imports nonexistent shape; its R12 parser produces R1 and 2, omitting R2. Float solver optimum reports are not exact proof certificates. Global optimal trees never branch twice is unsupported, and no exchange argument can prove admissibility excludes cost-increasing exchanges unnecessarily.

**Correction:** Preserve all historical logs and scripts with explicit limitations. The primary60-case exact all-parent restriction is supported. Mark125-case history as weaker parent restriction and float solver evidence; W3 -62/-61 stays an observed solver result until exact witness and lower-bound certification. State only that a cost-preserving exchange between minimal trees is challenged by that observation. Defer formal negative certification with branch preserved; invent no N1 routes.

## 8177-05 — MISSING_ARTIFACT

overlap.py import; structural.py and historical searches

overlap.py imports absent supervisor_control_block33_ssdp; shape2 also has unresolved helper spelling. Historical structural duplication search is time-limited and uses floating MILP, filtered6..110 ones and imported tight.py top-level workload; no complete tested-realization counter is saved. The approximately10000 all-site rooted checks inherit unlanded8176 history and cannot be inferred from these outputs.

**Correction:** Retain complete historical recovery including missing-input diagnostics; repair only active consumers if promoted. Describe structural search by its actual objectives, moves, size filters and observed maxima, not exhaustive absence or exact all-realization proof. Keep unverified counts attributed as historical reports, or omit live numeric totals.

## 8177-06 — AUDIT_COMPATIBILITY

Premises/Imports/frontmatter; citation_graph_manifest

Load-bearing dependencies are code-formatted rather than graph links; added node has out_degree0. Historical siblings are called open authority, and p>= thresholds/proved budget references omit current8174 supplied hypotheses.

**Correction:** Link current-main axioms, product-law parent and canonical8174 theorem where used; state p>=q>0,r>0, independent conditional updates, level order, initial all-a plane and any admissible-family premise. Restate8176 objects/data self-contained without accepting its unlanded theorem. Preserve current8175 lower-bound/conditional scope. Rebuild topology from current main; never copy stale manifest. Use canonical proposed status and native names, primary/cache links.

## 8177-07 — REPO_GOVERNANCE

shared campaign paths, author status/checker packets

Stale branch shared campaign files conflict with current main and carry author conformance PASS as history. Direct replacement loses already-reviewed science.

**Correction:** Preserve all50 path/mode/blob snapshots and binary delta; canonicalize only reviewed note/runner and needed evidence. Archive full original controls, proofs, failures, goals and logs with historical labels, preserving deferred negative material and branch handle. Append scoped corrections rather than replace current campaign files.

## Supported mathematics and independent controls

Extension and seed constructions are valid for the declared finite family: the new nodes occupy strictly higher levels than the attached tree, forks join distinct arborescences, and costs change by +1/-1, -1/-3, or -2 as written. The induction closes every stated non-tight case; the residual remains open. All eight rational certificates pass independent exact arithmetic and explicit slot enumeration.492 independently enumerated edge-subset minima agree with the primary for c1/c2 and both restrictions. Primary B reproduces788 sites,357 predecessor pairs,121 amplified instances,15 single-seed and78 double-seed cases. E reproduces120 equal minima and zero differences. The seed mutation fails B2 as intended.

No full original baseline, expensive climbs, new MILP run or auditor was launched. Two macOS resource-limit setup failures occurred before science and are retained. Certificate v3 used CPU120/wall180 and structurally bounded small data; the finite control used CPU90/wall110 and a sampled512MiB RSS watchdog, finishing0.682s at57568KiB sampled peak. Raw source/stdout/stderr/limits are under `check8177/`.

## Scope, recovery and next step

All50 original paths have complete base/head/main snapshots, modes, blobs, SHA256 and byte counts plus original binary delta under `drain8177-original/`. The paired JSON gives every path a disposition and binds actual inputs. Installed review-loop entry/reference bytes match frozen current main. Full original proofs and research/failed routes must remain recoverable; no invented negative-route packet PASS. Keep the branch for deferred content. Preserve all current-main shared campaign changes and regenerate only intended topology/evidence.

Current-main8174 supplies a conditional global upper2 theorem with explicit model/update/initial-plane assumptions.8175 lower-bound findings do not upgrade global sharpness;8176 remains unlanded research. No primitive supplies these model choices. Fresh corrected-source evidence and same-session affected/cold/final confirmation remain required. No source edits, staging, commits, pipeline runs or audit status changes occurred.
