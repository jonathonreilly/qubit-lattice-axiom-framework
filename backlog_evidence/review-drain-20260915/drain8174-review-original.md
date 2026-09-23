# PR8174 original independent review

Frozen head `cc7662e14ebf17010a0c60fdb8e7e634b176ce99`; original merge base `6dda46fc1af02827e9c6b64b2f7d05c381a3ce07`; authority/current-main revision `6332b12b59c83c5b08cc7b4ad90898cb6666050d`.

**Disposition: FIX BEFORE SOURCE CONFIRMATION.** The four threshold certificates are salvageable bounded mathematical support. This is not landing PASS or an audit verdict.

## Material findings

### 8174-01 — BUG
Location: note T1(a), front matter, conditional_surface_status; primary family B/G.
The assertion d1 <= max(d2,d3) for every positive weight triple is false. At (1/10,1,1), d1=5000/5001 and d2=d3=410/411. The proposed monotone coupling uses this inequality when eta has one dissenting predecessor but xi has none.
Correction: Restrict this coupling to p>=q>0,r>0 (sufficient for all four threshold rays), or redefine epsilon2=max(d1,d2,d3). For p>=q, d1<=d2 follows from (p-q)[q^2(p+q)+4r^3]>=0. Give the general monotonicity derivatives explicitly; remove the unused der_ok expression that accepts symbolic unknown and is never asserted.

### 8174-02 — BUG
Location: note T5 statement/proof; primary E1.
The full recursion domain at y=0 is 0<=x<4/27, not <=. At x=4/27 the least U fixed point gives v=3/2 and D=9/4+D, so bounded D is impossible. E1 only maximizes the U scalar equation and falsely reports the full-domain conclusion.
Correction: Supply the D denominator argument (D=v^2/(1-3xv^2)) and strict endpoint exclusion. Retain the strict necessary epsilon2<256/531441 and the independently verified 4150/4165 bracket. Do not call these bounds an exact minimal integer threshold or a certificate at every nearby integer.

### 8174-03 — OVERCLAIM
Location: note introduction, T5 reading, N4/N7/N8, review record; campaign additions.
Unlanded PR8172 simulation is repeatedly called the actual strength, located strength, and truth is eleven. Neither a finite simulation nor an unlanded sibling establishes the infinite-volume threshold; the factor 380 to truth and attribution of the whole gap inherit this problem.
Correction: Delete truth/actual-threshold assertions from live science. Preserve comparison only as explicitly historical finite-simulation context with its unproved infinite-volume bridge and no authority. No need to import or run PR8172.

### 8174-04 — NO_GO_OVERCLAIM
Location: note T5 reading and N1/N7; APPROACH_REGISTRY F30.5/F30.6; checker.
Treating amplification as noise leaves cannot make the ordered region empty: epsilon2 tends to zero at large p and recovers a single-noise contour regime. The overlap route has no explicit overlap/cycle witness or exhaustive impossibility proof in the original packet. Current N1 mixes checks of the same construction with alternative routes and does not demonstrate five normalized attempted negative-route families.
Correction: Say the leaf method loses this improvement, not all certificates; preserve tree-of-trees as an unresolved attempted construction with a named overlap obligation, not an impossibility theorem. Retain genuine route history and state attempted/untested/prior status honestly. N1 packet coverage remains a procedural limitation until actual evidence is supplied; do not invent routes or infer theorem false from quota.

### 8174-05 — AUDIT_COMPATIBILITY
Location: note Premises/Imports/front matter and citation_graph_manifest new node.
The two load-bearing dependencies are code-formatted names, not Markdown graph edges. Original manifest adds the claim with out_degree=0 despite upstream_dependencies listing two inputs. Status is legacy bounded-support rather than current author proposal wording.
Correction: Use actual relative Markdown links to the axiom memo and product-rule note, explicit primary/cache links, canonical status/trace enums, current-main native source framing, and regenerate topology acknowledgment on the final candidate. Do not land stale whole manifest or author-generated audit authority.

### 8174-06 — OVERCLAIM
Location: note Result up front, T4, execution counts, primary D3/G and history.
Exact threshold ratios are around 68.5-68.6, not 69 as an exact factor; primary asserts >=68. The primary cache has 4096 explained configurations (932+2321+843), while 4290 belongs to the distinct historical 1500-random-cone control.
Correction: Say approximately 69 or at least 68 and distinguish the primary and historical construction counts. Scope execution text to actual finite/random controls; analytical lattice-wide proof is not an executed lattice-wide check.

### 8174-07 — REPO_GOVERNANCE
Location: all campaign additions, historical controls and existing current-main paths.
The PR appends research/certificate state to six files that have diverged on current main; copying the stale files loses unrelated reviewed science. Historical controls include finite floating-point scans returning success after a fixed iteration cap and simulation outputs; their least-certified/transition claims cannot be used as rigorous negative certificates.
Correction: Preserve every original path and blob as historical recovery, retain full mathematical proofs/attempts, and land only corrected canonical note/runner/evidence plus explicit durable history. Keep current-main existing paths intact or append a scoped correction. The manifest must be rebuilt, not copied.

## Independent checks and limits

Independent stdlib exact Fraction recomputation, all 216 predecessor states at four threshold triples, certificate factorization and 10 percent amplification mutation, endpoint contradiction and threshold bracket. 30 s CPU; 45 s wall; 512 MiB RSS watchdog.
Attempts 1 and 2 failed before science because macOS rejected RLIMIT_AS and RLIMIT_DATA; scripts/stdout/stderr preserved. Attempt 3 used real sampled RSS watchdog with CPU and alarm limits; no science retries of a completed run.
All four certificate bounds passed: 7.6934551567e-8, 7.2441560890e-8, 7.6934551567e-8, 6.4848260436e-8. Raw artifacts and limit receipt are under `check8174/`. No original primary, simulation, combined gate or auditor was executed.

## Proof and import boundary

T2/T3 preserve the full extended-tree and lifted generating-function argument. T1 needs the stated domain correction; T5 needs strict endpoint exclusion. T4 is conditional on the supplied product rule, six-axis menu, positive weights, records-only reading, level order and all-a plane; compactness/Feller and extremal-decomposition mathematics are standard imports, not selected physical dynamics. Registered primitives supply none of those choices. PR8171/8172/8173 are not accepted authorities.

The exact inequalities are successful independently of the original implementation. General T2 construction was reviewed mathematically and in source; historical primary/control outputs are not claimed as fresh executions. Supply the finite ancestor-cone localization and full pole-transport identity in canonical text rather than depending on an unlanded sibling.

## Preservation and next step

All 25 original paths have base/head/main path-mode-blob inventories, full original binary delta and complete source snapshots under `/private/tmp/review-drain-20260915/drain8174-original`. `actual-inputs.json` binds both actual upstream inputs: bytes agree at original head and current main. `main-loss-guard.json` identifies seven conflicting existing paths (six campaign files and topology manifest) that must not be replaced from the stale head.
Full path dispositions and N1-N8 are in the adjacent JSON. Preserve historical attempts and raw outputs as history; do not launder author PASS certificates into current authority. Original primary cache and scan outputs require scoped historical labels, and fresh corrected cache requires authorized final execution.

Same reviewer session must inspect affected corrected proof/source/input interactions, cold diff and final frozen source. Combined mechanical validation and current-main preservation remain coordinator obligations. Source slot remains strictly clean, including ignored files. No source edits, commits, pushes, closures or audit status changes performed.
