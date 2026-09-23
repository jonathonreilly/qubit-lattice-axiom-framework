# Independent scientific review — PR8158

**Recommendation: NEEDS MANUAL SCIENCE.** Do not accept the source as stated. Preserve the sound finite factorization, pendant and path lemmas and valid cube/forest witnesses; narrow the unsupported graph converse and model/transfer claims, repair the lattice fixture and dependencies. This is a scoped scientific review, not an audit verdict or landing review.

Frozen head `dd78e677ba6cda496d6de20cfc215ef8bd09374f`; base `df5316ee81d59d573b3837afb80d371d12d890d6`; methodology `631d6b36cd1e9b860763ebcad36e40a2bbe7439c`. All 36 manifest hashes and sizes match. One read-only review iteration; no original program execution, repository mutation, Git, network, or agents.

## Material findings

### B-01 [P1] The universal graph criterion is not proved by Q1–Q3

**Class:** PROOF_OBLIGATION

**Sources:** `docs/ADMISSIBILITY_RULE_UNRECORDED_SITES_FREE_WINDOW_VERSUS_INTEGRATED_EXTERIOR_READINGS_DIFFER_IFF_AN_UNRECORDED_COMPONENT_TOUCHES_TWO_RECORDED_SITES_BOUNDED_THEOREM_NOTE_2026-09-15.md`:12, 68–69, 117–119, 139–166, 183; `scripts/admissibility_rule_unrecorded_sites_free_window_versus_integrated_exterior_readings_2026_09_15.py`:299–314, 318–319, 366–379

Q1 proves that equality is equivalent to constancy of the product of the component factors. Q2 proves a sufficient condition. Q3 proves nonconstancy for a single-site bridge and an isolated path, but for a general two-attachment component it only rewrites constancy as simultaneous vanishing of two eigenvalues. It never proves those eigenvalues cannot both vanish for a nonconstant rule. Components with three or more attachments and the product of overlapping boundary factors also need an argument. N1(2) does not supply it: distinct components can have identical or overlapping recorded boundaries, so their factors need not vary independently. Positive nonconstant functions can multiply to a constant; factorization alone excludes no cancellation. The sphere proof treats only a single-site bridge. The unrestricted headline and boundary also omit the explicitly allowed constant-rule exception.

**Evidence:** Independent spectral checks confirm powers 1–5 at six triples, including degeneracies. A legal path bridge at p=q=r=2 has F=24 for every endpoint pair and TV=0 despite touching two recorded sites, refuting the unqualified iff. This does not refute the separately qualified nonconstant-rule criterion: its validity remains unresolved here. The primary runner E1 checks one overlapping-boundary geometry and one nonconstant triple; G1 checks lengths of printed strings, not the general claim. Random original controls cover six tiny bridging components and cannot prove a universal assertion.

**Narrow fix:** State Q1, Q2, the path/single-site results, and the confirmed finite witnesses. Replace the universal iff throughout title, scope, trace, N5, boundary and runner fence with the exact criterion that the product of F_C is constant; retain the graph converse as an open obligation unless a proof over the stated domain is supplied. Include the constant-rule exception. Components touching zero recorded sites, when allowed, also contribute constants.

**Independent control:** checks.py / checks.json: spectral_checks, constant_rule_bridge, legal_path_witness; analytical obligation reconstruction.

### B-02 [P1] The plaquette-plus-site witness is not a cubic nearest-neighbour graph

**Class:** BUG

**Sources:** `docs/ADMISSIBILITY_RULE_UNRECORDED_SITES_FREE_WINDOW_VERSUS_INTEGRATED_EXTERIOR_READINGS_DIFFER_IFF_AN_UNRECORDED_COMPONENT_TOUCHES_TWO_RECORDED_SITES_BOUNDED_THEOREM_NOTE_2026-09-15.md`:81, 125–127; `scripts/admissibility_rule_unrecorded_sites_free_window_versus_integrated_exterior_readings_2026_09_15.py`:232–246, 285–296; `.claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block24_unrecorded_sites.py`:63–68; `.claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block24_refuter.py`:24–32

The edge c0–c1 of the plaquette plus x–c0 and x–c1 creates a triangle. Every edge of Z^3 changes coordinate-sum parity, so Z^3 is bipartite and no such site x exists. Thus all three Q4(a) rational values and the D4 test use a graph outside the declared domain. Both original controls repeat the same wrong graph, despite different arithmetic. This is a domain defect, not a rounding discrepancy.

**Evidence:** An independent contraction reproduces all three reported rational TVs for the abstract triangle-bearing graph. Independently generated lattice neighbours of (0,0,0) and (1,0,0) have empty intersection. A valid replacement is W={(0,0,0),(1,1,0)}, E={(1,0,0)}: at (3,1,2), the six endpoint factors are 26,22,24,24,24,24 and TV=1/72. The cube witness is valid and independently reproduces 9778807/1312253264.

**Narrow fix:** Replace Q4(a) and its runner/control fixture with explicit integer coordinates and induced nearest-neighbour edges, or label the old values as abstract-graph examples outside the lattice claim. Add a geometry invariant that detects odd cycles and checks all induced edges; regenerate affected evidence. Preserve the valid cube and pendant witnesses.

**Independent control:** checks.py / checks.json: abstract_triangle_fixture_tv, adjacent_common_neighbours, legal_path_witness, cube_edges_from_coordinates, cube_tv.

### B-03 [P2] Two finite Gibbs constructions do not establish the claimed axiom-satisfying model pair

**Class:** SEMANTIC_BRIDGE

**Sources:** `docs/ADMISSIBILITY_RULE_UNRECORDED_SITES_FREE_WINDOW_VERSUS_INTEGRATED_EXTERIOR_READINGS_DIFFER_IFF_AN_UNRECORDED_COMPONENT_TOUCHES_TWO_RECORDED_SITES_BOUNDED_THEOREM_NOTE_2026-09-15.md`:44–47, 77–83, 131–135; `docs/TOE_DERIVATION_CAMPAIGN_AXIOM_SUFFICIENCY_BY_UNDERDETERMINATION_WITNESSES_NOTE_2026-09-13.md`:35–50

Q5(a) claims models satisfying every quoted axiom sentence, including Records form and the nearest-neighbour distribution clause, but Q1–Q4 only define finite static probability measures on supplied menus. They supply no formation process or explicit interpretation showing how the distribution clause is satisfied after unrecorded variables are integrated out. In R2, conditionals based only on available records can depend on distant records through an unrecorded bridge. The campaign source expressly distinguishes finite conditional examples from completed models and requires these premise checks. The narrowed possibility-covariance parent likewise supplies a sphere and group action, not an all-axiom model. The present finite algebra remains valid without this model claim.

**Evidence:** For the legal length-two path at (3,1,2), the conditional distribution of one recorded endpoint given the other is (13/72,11/72,1/6,1/6,1/6,1/6), reordered with the distant record value. There is no recorded nearest neighbour. This is not a proof that a latent-state reading cannot satisfy the axioms; it demonstrates why an explicit interpretation/extension is necessary and cannot be inferred from Q1–Q4.

**Narrow fix:** Describe two supplied finite static-law readings and a conditional mathematical distinction. Remove the claim of established axiom-model underdetermination, or supply and verify actual models at precisely the claimed premise scope, with formation and latent/record conditioning meanings explicit.

**Independent control:** checks.json: R2_record_only_conditional_on_distant_record; full reads of minimal axioms, campaign method contract and covariance parent.

### B-04 [P2] The blanket transfer of prior window results is not supported by the supplied evidence

**Class:** MISSING_ARTIFACT

**Sources:** `docs/ADMISSIBILITY_RULE_UNRECORDED_SITES_FREE_WINDOW_VERSUS_INTEGRATED_EXTERIOR_READINGS_DIFFER_IFF_AN_UNRECORDED_COMPONENT_TOUCHES_TWO_RECORDED_SITES_BOUNDED_THEOREM_NOTE_2026-09-15.md`:48–50, 131–133, 161, 175

Q1 gives an exact convex-mixture identity. It transfers expectation bounds or other properties shown to be preserved under that mixture, not every statement uniformly true for fixed exterior records. Conditional independence, for example, is not preserved. The note applies the identity to all window results in blocks 17 and 23, and labels torus results from blocks 19–23 reading-independent, without stating the individual propositions or supplying their actual sources in this packet. It also does not establish that each cited torus object has no unrecorded subset. Their truth cannot be inferred from the labels alone.

**Evidence:** Independent positive two-bit product laws with probabilities (9,3,3,1)/16 and (1,3,3,9)/16 both have determinant zero (independence); their equal mixture (5,3,3,5)/16 has determinant 1/16. This refutes the general inference that any boundary-uniform property transfers, not any particular absent block theorem. Those specific theorem dispositions are held.

**Narrow fix:** Retain the mixture identity. State transfer only for a named property with a proof of mixture preservation and bind/read the exact source theorem. Until those sources are supplied, mark the block-wide claims unverified. State the torus assertion conditionally on all its sites being recorded/no E.

**Independent control:** checks.json: mixture_nonclosure_control; packet manifest and complete changed-note citation inspection.

### B-05 [P2] The submitted graph omits all declared premise dependencies

**Class:** AUDIT_COMPATIBILITY

**Sources:** `docs/ADMISSIBILITY_RULE_UNRECORDED_SITES_FREE_WINDOW_VERSUS_INTEGRATED_EXTERIOR_READINGS_DIFFER_IFF_AN_UNRECORDED_COMPONENT_TOUCHES_TWO_RECORDED_SITES_BOUNDED_THEOREM_NOTE_2026-09-15.md`:5–8, 77, 155–161, 185–189; `docs/audit/data/citation_graph_manifest.json`:757–760

The note names minimal_axioms and two scientific parents in YAML and prose but has no Markdown links. The submitted graph node has out_degree=0 and deps_hash=e3b0c44298fc (empty dependency set). Thus the graph does not carry the load-bearing static-law and covariance premises the claim declares. This is an observed source/graph mismatch, not merely an unrun pipeline concern.

**Evidence:** Independent source scan finds zero Markdown links in the changed note. Direct inspection of the submitted JSON confirms the empty dependency node. Frozen review-loop AUDIT_COMPATIBILITY explicitly requires linked authorities and nonempty matching dependencies.

**Narrow fix:** Add repository-relative Markdown links for the actual load-bearing authorities, scoped to their real roles, and regenerate/inspect the graph acknowledgment. Keep framing-only references distinct. Do not write audit verdicts.

**Independent control:** checks.json: changed_note_markdown_links, submitted_graph_node; manifest hash verification.

## Confirmed sound results

- Q1 factorization and the R2 mixture over the actual exterior marginal follow directly from finite sum/integral factorization and conditioning.
- Q2 constancy for a one-attachment component follows from value covariance and a transitive, measure-preserving group action; cycles inside a pendant component do not invalidate it. Zero-attachment components also cancel.
- Q3(a,b) six-axis eigenvalues, projector dimensions, matrix-square entry differences and the constant iff p=q=r criterion are correct. Pure bridging paths give the stated matrix powers when they have only the specified endpoint attachments.
- For exactly two attachments, simultaneous value covariance gives three pair-orbit entries and hence the displayed isotypic form; vanishing of both nonconstant sectors characterizes constancy but does not itself prove their nonvanishing.
- The sphere one-site integral is correct for area measure. At antipodal endpoints its displayed quotient needs the continuous value 4*pi. Its series establishes strict increase for beta>0, including the endpoint by continuity.
- All three submitted plaquette numbers are correct for their abstract graph, though that graph is inadmissible on Z^3. The coordinate-generated cube value is exactly 9778807/1312253264 and the pendant forest TV is exactly zero.
- A valid lattice path witness gives TV=1/72 at (3,1,2), so a scoped finite distinction between the supplied readings survives the fixture correction.
- The explicit non-selection of a physical rule, coupling or reading, and exclusion of infinite exteriors/formation claims from the mathematical results, are appropriate boundaries except where Q5 overreaches them.

## Independent evidence

The self-written `checks.py` ran successfully, with results in `checks.json` and preserved stdout/stderr. It imports no submitted code. No failed executable controls or corrections were discarded. It uses coordinates to derive lattice edges and symmetry-reduced exact contractions, with numerical quadrature only as a supporting sphere check. Analytical derivations establish the general Q1/Q2 and specified Q3 identities; finite tests are not presented as universal proof. The original cache runner hash matches the frozen source, but its invocation and input-fingerprint construction were not authenticated.

## Lens dispositions

- **code_runner:** FAIL: fixture/domain mismatch; broad claim not tested
- **physics_claim_boundary:** OPEN for Q5 model/transfer claims; conditional finite math survives
- **proof_obligations:** FAIL for headline completeness; Q1/Q2 and specified Q3 lemmas closed at declared mathematical scope
- **imports_support:** DISCLOSED for static readings, positive weights, menus and covariance; unsupported model promotion in Q5
- **nature_retention:** OPEN; no Nature readiness or retention granted
- **no_go_discipline:** FAIL: N1/N5/N7 closure defects
- **labeling_convention:** PASS: substantive algebra, not mere naming
- **repo_governance:** FIX: missing dependency links
- **audit_compatibility:** FIX: observed zero-dependency graph; full gate not run
- **methodology_skill:** NOT APPLICABLE: frozen methodology is a review input, not a changed subject

## Imports

- **foundation:** minimal_axioms is registered authority; approved primitives read but do not select a static reading or law
- **conditional_scaffolding:** finite induced cubic graph, six-axis or sphere menu, positive p/q/r or beta>0, value-only covariance, invariant summation/area measure, R1/R2/R3 definitions
- **mathematical_imports:** finite product laws, conditioning, covariance/orbit linear algebra, polar integration; checked/rederived locally
- **fixtures:** rational triples and finite geometries are test inputs, not physical parameters
- **observational_inputs:** none

## No-go discipline

- **N1:** FAIL for claimed closure: single bridges/paths and pendant components are resolved; general component nonvanishing and overlapping-boundary factor cancellation are not. The listed tests do not establish exhaustive route closure.
- **N2:** No independent wall count is claimed; approved primitives are not walls. No wall-independence finding.
- **N3:** Positive weights, finite sets, static product readings, value-only covariance, transitivity, supplied menus/measure are explicit. The graph converse and model-realization/mixture extensions require extra arguments, not silently supplied physics.
- **N4:** Static parent and covariance parent support the limited roles read; the campaign is a research contract, not proof of model completeness. Absent blocks cannot establish Q5(b).
- **N5:** FAIL: executed path algebra and finite fixtures are promoted to all finite graphs and both families. Runner G1 only tests printed-line structure.
- **N6:** Narrow Q1/Q2/Q3 and valid witnesses survive with no axiom or primitive addition. No claim that a new axiom is required is justified or made by this review.
- **N7:** Concrete open mechanism: prove simultaneous nonvanishing for all allowed two-terminal components, extend to larger boundaries and rule out product cancellation; the current spectral restatement and random small samples do not discharge it.
- **N8:** Available formation/static parent has a genuine product-level single-site variation argument; that argument is not reproduced for the different F_C factors. Wider historical search was excluded and is not claimed.

## Reading coverage

The following files were read completely (all theorem statements, proofs, code and outputs, not only search hits):

- `.claude/science/physics-loops/admissibility-induced-law-20260906/ASSUMPTIONS_AND_IMPORTS.md`
- `.claude/science/physics-loops/admissibility-induced-law-20260906/RESULTS_block24.md`
- `.claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block24_refuter.out.txt`
- `.claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block24_refuter.py`
- `.claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block24_unrecorded_sites.out.txt`
- `.claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block24_unrecorded_sites.py`
- `docs/ADMISSIBILITY_RULE_UNRECORDED_SITES_FREE_WINDOW_VERSUS_INTEGRATED_EXTERIOR_READINGS_DIFFER_IFF_AN_UNRECORDED_COMPONENT_TOUCHES_TWO_RECORDED_SITES_BOUNDED_THEOREM_NOTE_2026-09-15.md`
- `logs/runner-cache/admissibility_rule_unrecorded_sites_free_window_versus_integrated_exterior_readings_2026_09_15.txt`
- `scripts/admissibility_rule_unrecorded_sites_free_window_versus_integrated_exterior_readings_2026_09_15.py`
- `docs/MINIMAL_AXIOMS_2026-06-29.md`
- `docs/ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md`
- `docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`
- `docs/POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md`
- `docs/TOE_DERIVATION_CAMPAIGN_AXIOM_SUFFICIENCY_BY_UNDERDETERMINATION_WITNESSES_NOTE_2026-09-13.md`
- `docs/ai_methodology/skills/review-loop/SKILL.md`
- `docs/ai_methodology/skills/review-loop/references/SCIENCE_LENSES.md`
- `docs/ai_methodology/skills/review-loop/references/REVIEW_SETUP.md`
- `docs/ai_methodology/skills/review-loop/references/REVIEW_UNITS.md`
- `docs/ai_methodology/skills/review-loop/references/FIXES_AND_REPORTING.md`
- `docs/ai_methodology/skills/review-loop/references/AUDIT_COMPATIBILITY.md`
- `docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md`
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`
- `docs/audit/data/axiom_premise_nodes.json`
- `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`
- `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`
- `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`
- `docs/ai_methodology/skills/no-go-discipline/SKILL.md`

Partial reads: changed-node metadata in `docs/audit/data/citation_graph_manifest.json`; applicable classification sections/searches in `docs/repo/controlled_vocabulary.yaml`. All manifest bytes were checked for identity, which does not itself establish semantic coverage.

## Coverage gaps and held conclusions

- Frozen methodology references docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md, absent from the packet. Its detailed procedure could not be applied; no complete procedural PASS is issued. The target/proof graph was independently reconstructed from the available lens and source.
- Q5(b) sources for blocks 17 and 19–23 (and contextual 15–16) are absent; the note gives opaque block/PR references rather than exact source paths. Exact filenames cannot be recovered from the cited text without guessing. Their individual claims and mixture preservation are unverified.
- Full original-path disposition, base diff, live repository/current-main preservation, landing mechanics and historical commentary were expressly excluded. The 13 excluded_original_paths in manifest.json were not inspected.
- No submitted primary/control program, primary mutation suite, pipeline or repository tool was run. Original outputs were read as submitted evidence only. Small independent checks do not establish reproducibility of their invocation or authenticate the cache input-fingerprint algorithm, which is absent.
- Unrelated graph nodes and full vocabulary were not scientifically reviewed. All graph bytes were hash-verified; the changed node was inspected. Vocabulary review covered applicable claim/status/no-go/proof classifications. Operational/landing-only methodology references were not applied.
- The nonconstant-rule universal converse is not disproved by this review; it lacks a supplied proof covering general components and factor products. No exhaustive graph/parameter search or external literature search was performed.

All original paths excluded by `manifest.json` remain excluded. No full source-disposition, pipeline, audit or landing PASS is claimed. Findings remain open; no repairs were authorized in this experiment.

## Final scientific recommendation

Preserve the conditional algebra and valid finite witnesses. Repair the graph fixture and dependency links, narrow the universal criterion to proved statements unless its missing converse is supplied, and hold Q5’s model/earlier-block claims until their precise premises are demonstrated. The nonconstant universal graph criterion is unresolved here, not declared false. Freeze this report without further edits.
