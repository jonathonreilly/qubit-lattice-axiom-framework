# PR8172 original independent review

Head `c8ae4a4622c1aa924ff6c9b3452021022f20746d`; merge base `6dda46fc1af02827e9c6b64b2f7d05c381a3ce07`; authority main `8bf464953779b8ada8415208e89a656411f9f525`.

**FIX REQUIRED. No original landing PASS or audit verdict.**

## Material findings

### 8172-R1 [P1] Point checks do not establish the claimed half-line uniqueness region
BUG; `docs/ADMISSIBILITY_RULE_MAP_OF_MEMORY_WHERE_EACH_OF_THE_FOUR_LAWS_KEEPS_ITS_PLANE_LOCATED_AGAINST_THE_PROVED_REGIONS_WITH_THE_HEALING_AND_INFLUENCE_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-16.md` lines [25, 108, 134].
Independent exact enumeration confirms 3c(37/10)=406962630/413162167 and 3c(19/5)=871815/862244, but at p=1/10 gives 3c=87/52>1. The claimed criterion holds for p<=3.7 is false. This does not prove nonuniqueness at p=1/10.
Repair: State the two exact point evaluations only; any connected interval or threshold-location assertion needs its actual interval proof. For epsilon from p=285718, include derivatives showing monotonicity, or narrow to the two integer evaluations.

### 8172-R2 [P1] Healing proof and region enumerator omit translated islands
PROOF_OBLIGATION; `docs/ADMISSIBILITY_RULE_MAP_OF_MEMORY_WHERE_EACH_OF_THE_FOUR_LAWS_KEEPS_ITS_PLANE_LOCATED_AGAINST_THE_PROVED_REGIONS_WITH_THE_HEALING_AND_INFLUENCE_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-16.md` lines [116].
The step i_j<=D is false without normalization. I={(100,-100,0)} has D=0, three region sites, while the original coordinate box counts zero. Translated triangle has 76 actual sites and zero counted. C1 also compares max(-a-b) rather than true third coordinate t-a-b, so its maximum check is weaker than claimed. The union-bound theorem is salvageable, not refuted.
Repair: Use B_j=D+1+M_j, sum B_j=4D+3, or translate by an island point on level zero then explicitly apply the original bound. Count U by a complete predecessor enumeration or valid coordinate limits; test translation invariance and t-a-b maxima. Define island nonempty or handle empty set separately. Bound survival by min(1,18(D+1)^3 epsilon) when giving a probability reading; healing is at least 1-bound, not equality.

### 8172-R3 [P1] Sphere influence is conditional on an unproved contraction import
IMPORTED_VALUE; `docs/ADMISSIBILITY_RULE_MAP_OF_MEMORY_WHERE_EACH_OF_THE_FOUR_LAWS_KEEPS_ITS_PLANE_LOCATED_AGAINST_THE_PROVED_REGIONS_WITH_THE_HEALING_AND_INFLUENCE_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-16.md` lines [124, 167, 199].
The source proves only propagation of the supplied recurrence. Block27 contraction is neither reproduced nor linked/input-bound, while prose says it is re-proved. D0 is <=2 delta, not equality for arbitrary two distinct initial directions. Primary D1 checks a scalar recurrence at one rational g; it does not construct or verify the sphere coupling.
Repair: Keep full original proof. Narrow T3 to a nonnegative recurrence lemma with explicit supplied coefficient and D0<=2 delta, or import the independently corrected block27 theorem with exact hypotheses and current source/input pins after its landing. Never treat unlanded 8171 repair as main authority.

### 8172-R4 [P1] Finite simulations are promoted to actual memory thresholds and never statements
OVERCLAIM; `docs/ADMISSIBILITY_RULE_MAP_OF_MEMORY_WHERE_EACH_OF_THE_FOUR_LAWS_KEEPS_ITS_PLANE_LOCATED_AGAINST_THE_PROVED_REGIONS_WITH_THE_HEALING_AND_INFLUENCE_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-16.md` lines [21, 32, 38, 44, 74, 144].
One seeded finite run per setting, no equilibrium/mixing or thermodynamic-limit control, cannot show permanent memory or its absence at all beta. Positive finite kernels permit later loss. The ratio about one third is a descriptive ratio of chosen finite observations, not a physical/theorem threshold ratio. A finite-run bracket is not a certified transition bracket.
Repair: Preserve all exact original simulations and outputs as historical exploratory observations, with sizes, run lengths, seeds, observables, and lack of error/equilibration certification explicit. Replace actual strengths/keeps/never by measured finite-time results and defer asymptotic thresholds. No reruns required to honestly archive observations.

### 8172-R5 [P2] Reported simulation coverage exceeds the saved runs
BUG; `docs/ADMISSIBILITY_RULE_MAP_OF_MEMORY_WHERE_EACH_OF_THE_FOUR_LAWS_KEEPS_ITS_PLANE_LOCATED_AGAINST_THE_PROVED_REGIONS_WITH_THE_HEALING_AND_INFLUENCE_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-16.md` lines [144].
L16 heat-bath scan has 3.5 and 4, not 3.6/3.7. Metropolis has 3.6 and 3.8, not 3.7. Thus all three lattice sizes and both algorithms at 3.6/3.7 is unsupported. Healing refuter uses a rectangular superset of the true forward cone, not the asserted event; the smallest island rectangle has 16 level-one sites while the true cone has 3. Larger bounds exceed one and are vacuous.
Repair: Report each protocol exactly as saved. Label healing rectangular test as a different/superset observable, with no claimed direct frequency test of exact F. Preserve existing outputs and code without retroactively relabeling execution.

### 8172-R6 [P1] Historical proved-region table conflicts with corrected main scope
SEMANTIC_BRIDGE; `docs/ADMISSIBILITY_RULE_MAP_OF_MEMORY_WHERE_EACH_OF_THE_FOUR_LAWS_KEEPS_ITS_PLANE_LOCATED_AGAINST_THE_PROVED_REGIONS_WITH_THE_HEALING_AND_INFLUENCE_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-16.md` lines [4, 26, 82, 137].
Current-main formation stability note explicitly records that static reflection order remains conditional because site-reflection parity leaves a dissemination gap. PR8172 cannot restore unconditional static order at p>=432. Current-main sphere beta>0.76 bound is a sufficient supplied-model corollary with Gaussian-domination import, not an actual transition. Other uninspected old region assertions cannot be certified by addresses or prose alone.
Repair: If retaining comparison table, link and bind corrected current sources with their exact conditional bounds. Otherwise preserve old map historically and defer the theorem comparison. Do not overwrite already-corrected main science.

### 8172-R7 [P1] Runtime evidence closure and resolution certificate are incomplete
AUDIT_COMPATIBILITY; `scripts/admissibility_rule_map_of_memory_four_laws_transitions_located_against_proved_regions_healing_and_influence_bounds_2026_09_16.py` lines [26, 285, 286].
Only three note paths are declared; no simulation source/output or sphere contraction source is bound. No Markdown premise links exist in original note. N5 per_block says executed simulation although primary never executes or reads the specs/results; lattice_wide overstates proofs. Historical PASS cache does not cure missing inputs or validate finite data. No helper execution was performed in this review.
Repair: Bind actual active proof/data inputs and paired runner/parent links; use owned proof/runtime inputs as appropriate. Say simulations were historical, checked but not executed in current primary; infinite lattice is proof-only or conditional. Capture only the final corrected frozen primary under authorized limits; retain old receipt unchanged.

### 8172-R8 [P2] N1-N8 does not certify broad negative or threshold conclusions
NO_GO_OVERCLAIM; `docs/ADMISSIBILITY_RULE_MAP_OF_MEMORY_WHERE_EACH_OF_THE_FOUR_LAWS_KEEPS_ITS_PLANE_LOCATED_AGAINST_THE_PROVED_REGIONS_WITH_THE_HEALING_AND_INFLUENCE_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-16.md` lines [146, 151, 177].
N1 lists four items, not five normalized attempted families; finite size and finite time remain unresolved, N3 hides contraction and sampling assumptions, N4 labels imports as evidence addresses, N5 overstates coverage, and N7 itself concedes true thresholds unproved.
Repair: Withhold negative certification, record actual tested controls and untested routes honestly, and retain only positive conditional finite lemmas plus historical observations. Do not fabricate a fifth route or weaken the schema. Any future negative certificate needs its real route/proof support.

### 8172-R9 [P2] Campaign packaging is not canonical science or independent review
REPO_GOVERNANCE; `docs/ADMISSIBILITY_RULE_MAP_OF_MEMORY_WHERE_EACH_OF_THE_FOUR_LAWS_KEEPS_ITS_PLANE_LOCATED_AGAINST_THE_PROVED_REGIONS_WITH_THE_HEALING_AND_INFLUENCE_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-16.md` lines [13, 74, 82, 203].
Block numbers, open-PR assertions, supervisor PASS and campaign certificates are live-facing. Common .claude campaign files contain inherited earlier history and must not be copied over current source. Generated manifest is the only shared changed path.
Repair: Archive exact campaign source/proofs/specs/logs with path/mode/hash recovery and explicit historical status; keep active scientific proofs accessible. Use descriptive scientific names and genuine Markdown links. Recompute generated manifest only at coordinator integration; no audit verdict changes.

## Independent mathematics
Exact checks confirmed the two advertised sensitivity fractions and the integer epsilon crossing, refuted the asserted half-line criterion and translation-invariant region count, and confirmed the directed-walk multinomial coefficients through eight steps. Complete script/stdout/stderr are in check8172. No original runner or simulation was executed.

A narrow healing repair needs no new axiom: with B_j=D+1+M_j, sum B_j=4D+3, each level has at most C(4D+4,2) possible predecessors, which is below 18(D+1)^2 for D>=0. Alternatively recenter at one island point on level zero and retain the original loose bound. The eroder maximum argument and noise-free coupling are valid for a nonempty finite island.

T3 is a valid comparison-recursion lemma under its supplied contraction hypothesis. For arbitrary initial directions use D0<=2 delta; equality is unnecessary. A recurrence solution cannot establish that sphere kernels admit the claimed coupling.

## Preservation and disposition
All 24 changed paths have original path/mode/blob/SHA-256 and explicit dispositions in the JSON report. Original/base/main byte snapshots and three deltas are retained. The complete 79-file inherited campaign packet is archived and byte-verified, including old unsuccessful proposals; no proof is replaced by a summary. The original primary cache remains historical. Only generated citation manifest overlaps main changes. Final integration must preserve corrected-main theorem boundaries and regenerate this manifest, not copy old bytes.

## Scope and next step
Salvage exact point arithmetic, repaired finite healing, a conditional recurrence lemma, and the full historical finite simulation record. Actual asymptotic thresholds and broad absence/order claims remain deferred. The final author must fix live prose, actual inputs and certificates before final focused capture. Original source is unchanged; root owns release. Same reviewer session required for correction/cold/final confirmation.

## Counts and checks
One original review iteration; 9 material finding groups; zero fixes/commits/audits/pipeline runs. Three whitespace checks passed. Independent finite control exit 0 (0.046 seconds), no explicit wall-time cap; all outputs preserved. Combined candidate gates are coordinator work after final source confirmation.

**Recommendation: NEEDS MANUAL SCIENCE on the original; narrow salvage is available.**
