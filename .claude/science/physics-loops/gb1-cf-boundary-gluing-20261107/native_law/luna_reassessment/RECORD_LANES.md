# RECORD / ADMISSIBILITY / State-Law Reassessment

## Revision and authority

- Scientific sources are pinned to **main f5af11cd0102cfd0b51aef0911f600130bf5beb1**. The worktree HEAD matched that commit; docs/ was clean when read.
- The owner-approved wording change is not present in that revision. The operative Admissibility clause still says “nearest-neighbor admissibility rule” at [MINIMAL_AXIOMS_2026-06-29.md:57](/Users/jonreilly/.codex/worktrees/gb1-cf-pair-check/Physics/docs/MINIMAL_AXIOMS_2026-06-29.md:57) and “nearest-neighbor conditions” at [line 61](/Users/jonreilly/.codex/worktrees/gb1-cf-pair-check/Physics/docs/MINIMAL_AXIOMS_2026-06-29.md:61), blob SHA bc23300becfe4e4db57153c0e94cfcdf2338da71. The Lattice clause defines the cubic Z^3 nearest-neighbor adjacency at line 37 of that file. These two Admissibility phrases therefore restrict the current axiom to the six immediate sites. I treat the approved replacement with “neighborhood” only as a future scope broadening; its radius and shape remain unspecified. The registry description repeats the old premise at [axiom_premise_nodes.json:25](/Users/jonreilly/.codex/worktrees/gb1-cf-pair-check/Physics/docs/audit/data/axiom_premise_nodes.json:25), blob SHA b93959cca4f7e26c673cdccbe601e50c3cb93daa. No new tick, probability rule, gate, state, formation rule, or physical primitive is inferred.
- Commit SHA for all main-source findings: f5af11cd0102cfd0b51aef0911f600130bf5beb1. File blob SHAs are listed per finding.
- Read the pinned workflow, exercise procedure and freshness check, minimal axioms, primitive registry procedure and data, scale-reference note, derivation-obligation registry, and review-loop boundary. No scientific status or audit field was changed.

## Four selected source findings

### 1. Six-slot rule census: genuinely shell-limited count, not an invalidated conclusion

**Disposition:** confirmed narrow model dependence; candidate for lead verification if the count is being used to reason about the broadened law space.

**Source:** [EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md](/Users/jonreilly/.codex/worktrees/gb1-cf-pair-check/Physics/docs/EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md:59), blob SHA 61e037667159fa8a719691d55db34065fb63f54d; axiom premise [MINIMAL_AXIOMS_2026-06-29.md](/Users/jonreilly/.codex/worktrees/gb1-cf-pair-check/Physics/docs/MINIMAL_AXIOMS_2026-06-29.md:57), blob SHA bc23300becfe4e4db57153c0e94cfcdf2338da71.

**Literal restriction and inference:** the census defines profiles with “six neighbor slots” each in {open, 0, 1} (lines 61-79), giving 3^6 profiles and 3^24 - 1 varying support tables. Its append construction likewise uses the recorded neighboring values (lines 101-133). Those enumerated numbers genuinely depend on the immediate six-site shell. The note explicitly calls the count a lower-bound witness, says it is not exhaustive for M_2(C), and explains that the continuous-domain distribution table space is larger (lines 82-97).

**Effect of broadening:** the lower-bound construction and its strict-neighbor examples remain valid if that narrower rule class remains available. Only a framework-wide use of 3^24 - 1 as the complete rule count would be invalidated. The note itself does not make that use. Its composition non-entailment comparison (lines 53-57) concerns identical record graphs on different carrier algebras and does not depend on the physical rule being exhaustive.

**Concrete route to test:** on a finite Z^3 patch, define a declared radius-two condition N_2(x) and enumerate covariant support/distribution rules on the full available condition. Compare the six-slot count with the radius-two class and test whether the old support-only append properties still follow. This would be a new bounded model check, not evidence that the physical law uses that radius.

**Still unproved:** which rule is physical; a probability measure on the full continuous possibility domain; formation site, rate, realized draw, and quantum composition.

### 2. Formation-order census: finite graph theorem remains conditional

**Disposition:** exact model result; credible reopening candidate for larger-neighborhood or mediated interaction graphs.

**Source:** [ADMISSIBILITY_FORMATION_ORDER_MENU_ORDER_MIXTURE_MONOTONE_BOX_AND_CUBE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-13.md](/Users/jonreilly/.codex/worktrees/gb1-cf-pair-check/Physics/docs/ADMISSIBILITY_FORMATION_ORDER_MENU_ORDER_MIXTURE_MONOTONE_BOX_AND_CUBE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-13.md:91), blob SHA 71377c525db731ad8a97cec87db50146723bb169; axiom source as above.

**Literal restriction and inference:** the declared law is a positive pair-product rule on finite graph edges; the “records-only reading” says the condition is the values of recorded neighbors and that unrecorded neighbors do not enter (lines 112-134). Lemma L proves the order-law identity for that graph/product class using a common one-neighbor normalizer (lines 237-265). The 28 rectangle laws and 542 cube laws are exact for the specified windows, rules and orders (lines 278-310). Here M=6 is the six-element Bloch-axis menu, not six neighboring sites.

**Effect of broadening:** none of the finite identities or counts becomes false. Lemma L is stated for a finite graph and can be reused on a wider interaction graph if its pairwise factorization, positivity, constant prior and row-sum hypotheses still hold. The exact counts do not transfer to that graph; arbitrary neighborhood-dependent or higher-order kernels are outside this proof. The note says it selects no physical rule/order and makes no infinite-lattice claim (lines 525-550).

**Concrete route to test:** use the same finite order enumeration on a radius-two interaction graph, first preserving pairwise factors, then add one explicit shared-mediator or three-site factor. Compare orders with equal nearest-neighbor K(σ) but different widened predecessor conditions. A differing law would show the old key is insufficient for that widened model; it would not contradict Lemma L on the old graph.

**Still unproved:** a physical formation order or order law, the infinite-volume law, and any application of these counts to the selected framework law.

### 3. Cross-edge marginal theorem: valid under a wider complete condition

**Disposition:** false-positive exclusion. The theorem does not require a six-site-shell interpretation.

**Source:** [G3_CROSS_EDGE_INDEPENDENCE_IS_A_FORMATION_GATE_ATOM_MARGINAL_IDENTITY_FROM_QUALIFICATION_BOUNDED_THEOREM_NOTE_2026-07-12.md](/Users/jonreilly/.codex/worktrees/gb1-cf-pair-check/Physics/docs/G3_CROSS_EDGE_INDEPENDENCE_IS_A_FORMATION_GATE_ATOM_MARGINAL_IDENTITY_FROM_QUALIFICATION_BOUNDED_THEOREM_NOTE_2026-07-12.md:111), blob SHA ee4803e7eed98ed481e83e350a6cb28391f75f82.

**Literal restriction and inference:** the condition is the complete supplied formation-law condition, including the nearest-neighbor/record environment “if the law uses it,” plus every other supplied domain variable (lines 113-165). Under law-equivalence (LE) and a formation law (LAW), the Qualification gives equal single-registration marginals (lines 197-215). The proof establishes no equation between joint weights and products; the note exhibits product and perfectly correlated couplings with the same marginals (lines 217-228).

**Effect of broadening:** the conditional theorem survives if the complete conditions, now including whatever broader neighborhood data are supplied, match after lattice transport. Broadening can make LE harder to satisfy across two epochs; it does not itself create independence or close the cross-edge factorization gap.

**Concrete route to test:** place two fresh sites with overlapping widened neighborhoods around a recorded mediator. Define LE using the full transported neighborhood conditions, then test whether any independently justified screening premise forces m(j,k|c,c)=F_j(c)F_k(c). Without that premise, same marginals still admit correlated couplings.

**Still unproved:** the physical formation law, law-equivalence for actual histories, and cross-edge independence.

### 4. Projective-history law: a finite joint law exists, but it does not supply GB1-CF’s local carrier

**Disposition:** strongest history-law source reviewed within the four-note cap; it is more than a single-step factorization restriction, but it does not close the native local-law or gauge/gluing bridge.

**Source:** [RECORD_PROJECTIVE_HISTORY_LOCAL_APPEND_DOWNSTREAM_LAW_CANDIDATE_BOUNDED_THEOREM_NOTE_2026-08-21.md](/Users/jonreilly/.codex/worktrees/gb1-cf-pair-check/Physics/docs/RECORD_PROJECTIVE_HISTORY_LOCAL_APPEND_DOWNSTREAM_LAW_CANDIDATE_BOUNDED_THEOREM_NOTE_2026-08-21.md:108), blob SHA ca475ec5b950d52f76ff3191371684ee24352af4.

**Literal restriction and inference:** the note provisionally selects a finite rank-one projective sector law: typed Records, trace/Lüders history weights, and a joint trace cylinder for commuting two-wing events (lines 112-125). It proves positive, normalized, prefix-consistent finite cylinders conditional on that kernel (lines 223-258), supplies a global two-wing measure with nonfactorizing singlet correlations (lines 299-344), reconstructs the supplied packet entry-by-entry and demonstrates finite Record-fibre sufficiency on eight declared prefixes (lines 260-297). Thus a conditional global history law already exists in this finite sector.

The note also marks the limits directly: the event map, trace functional, and composite-cylinder rule are supplied inputs, not derived from the four axioms (lines 145-185). Its packet sufficiency is limited to those prefixes and is not complete future-fibre lumpability (lines 291-297). Most directly, the local Admissibility carrier is absent; the full nearest-neighbor Record condition must be shown to determine the selected marginal (lines 127-136, 346-378). The global coupling is separately supplied, not generated by either site’s local kernel (lines 370-378).

**GB1-CF comparison:** the worktree-local [INDEPENDENT_PROPAGATION.md](/Users/jonreilly/.codex/worktrees/gb1-cf-pair-check/Physics/.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/native_law/INDEPENDENT_PROPAGATION.md:111), SHA-256 f9f49331c5b49006cc69bbd9ac0732dfbd578b8c4e3eff7bc06e2943de97d6eb, gives a conditional record relay: a selected nearest-neighbor measure repeated along a supplied self-avoiding path (lines 111-149). It explicitly leaves an autonomous homogeneous joint law and plaquette evolution open. The companion [CHECKER.md](/Users/jonreilly/.codex/worktrees/gb1-cf-pair-check/Physics/.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/CHECKER.md:27), SHA-256 bf7e6f3150d29ffd8d872a8d896dda97405e6e49b07097305aae7aeadb66df1d, describes the GB1-CF result as finite conditional gauge mathematics and expressly does not derive an Admissibility distribution or Record law (lines 27-31). The projective-history note therefore supplies a candidate global finite probability/history layer, but not the local carrier needed to tie it to GB1-CF, and not any SU(2) boundary/gluing result.

**Effect of broadening:** replacing the strict shell by a broader neighborhood could make it possible for more preparation data to enter the local condition; the note’s own missing statement must then be tested with the complete widened condition. Broadening alone does not provide the carrier, event calibration, or a law deriving the global coupling from local conditions.

**Concrete route to test:** for a declared finite N_R(x) large enough to contain the encoded preparation packet, reconstruct the reduced preparation from the local Record map and test whether the one-site marginal is a function of that complete neighborhood for every supported history prefix. A counterexample would be two supplied preparations with identical N_R(x) Record data and unequal local marginals. If the carrier succeeds, separately prove prefix consistency and the joint event law; do not identify that probability result with the finite gauge gluing theorem.

**Still unproved:** physical calibration of the event map, a physical local carrier, formation site/rate/cadence, causal layer and resource renewal, the actual history member, and any bridge from this sector law to the GB1-CF gauge state.

## Synthesis

The genuinely six-shell-sensitive conclusions are the profile counts and the narrow nearest-neighbor model families. Their source notes already scope them as lower bounds or finite conditional theorems; broadening does not prove them false. The graph-product formation identity can be reused on a wider graph under its stated hypotheses. The Qualification-based marginal theorem remains valid under equal complete conditions. A finite global projective history law is available in a provisionally selected conditional sector, but its local carrier and physical identifications remain open.

For GB1-CF, the closest existing law is not “only single-step”: it supplies finite joint history cylinders and a global coupling under supplied premises. It does not supply the next native local-law bridge or replace the gauge boundary/gluing proof. A widened-neighborhood carrier theorem is the credible reopening candidate; it must still show that complete local conditions determine the selected marginal and must be checked separately from the gauge theorem.

## Search scope and provenance limits

- Bounded filename/frontmatter searches covered nearest-neighbor, shell-only, same-neighborhood, formation-order, record-condition, marginal, no-go, and history/joint-law terms under docs/. Four main proof notes are the findings above; no ledger dump was treated as verification.
- One finite ice formation-order note was initially screened then displaced by the more relevant projective-history source after the GB1-CF priority arrived; no conclusion here relies on that note. The filename search also surfaced LIVE_M2_RECORD_SUFFICIENT_JOINT_LAW_STATE_ONTOLOGY_FORK_BOUNDED_THEOREM_NOTE_2026-08-14.md (blob 78190b6c02671430dd85021ae80de53d37cd249e); only its frontmatter/outline were screened, not its proof, and no conclusion depends on it. Gauge/circuit lane candidates were not analyzed.
- The worktree-local GB1-CF receipts are comparison context, not main-source authority. Their hashes identify the files read at this pass.
- No numerical job or runner was executed, and no external literature search, audit/status edit, source fix, commit, or push was performed. lab_ops.py preflight was run as requested (including its origin-reachability check). Its output reported “model floor: no target named, no floor checked”; the runtime does not expose an actual vendor/model-family/effort receipt, so I cannot substantiate a “Luna/max-effort” label.
- Full discovery logs, selected complete source extracts, and pinned instruction/premise snapshots are on disk in /tmp/luna_record_locality_20261108/. Main source documents remain available at the pinned commit. Proof text was read; runners/caches were not re-executed or independently checked.
