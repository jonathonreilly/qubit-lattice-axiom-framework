from pathlib import Path
import json,subprocess,re,difflib
r=Path(__file__).resolve().parent;w=r/'drain-author-slot';inv=json.loads((r/'drain8158-original-inventory.json').read_text())[0];head=inv['headRefOid']
oldnote=next(x['path'] for x in inv['original_paths'] if x['path'].startswith('docs/ADMISSIBILITY_RULE_'));runner=next(x['path'] for x in inv['original_paths'] if x['path'].startswith('scripts/'))
read=lambda p:subprocess.check_output(['git','-C',str(w),'show',head+':'+p],text=True)
orig=read(oldnote);code=read(runner);newnote='docs/ADMISSIBILITY_RULE_FINITE_UNRECORDED_COMPONENT_FACTORIZATION_AND_ATTACHMENT_FACTORS_BOUNDED_THEOREM_NOTE_2026-09-15.md';cid=Path(newnote).stem.lower()
front='''---
claim_id: '''+cid+'''
claim_type: bounded_theorem
claim_scope: "Finite supplied positive static models: component factorization and conditional averaging, constancy with at most one attachment, exact single-bridge/path/spectral factors, and explicitly scoped finite graph witnesses. No universal graph iff or all-axiom-model certification."
upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: '''+runner+'''
---

# Finite unrecorded components: factorization, attachment factors and exact marginalization witnesses

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (supplied finite probability models; unaudited)

## Result up front

For the explicitly supplied static models below, summing finite unrecorded components multiplies the recorded-site bond weight by one effective factor per component. Components with zero or one recorded attachment contribute constants. A single bridging site or a simple bridging path has the exact nonconstant factor stated below when the six-axis rule is nonconstant. General two-attachment factors have an exact spectral constancy criterion; no proof that this criterion always fails for every nonconstant rule and every component is supplied.

The genuine unit-cube and pendant examples are nearest-neighbour cubic-lattice fixtures. The three square-plus-extra-vertex values are retained as abstract-graph diagnostics: the extra vertex touches adjacent square corners, creating a triangle, so that graph cannot be a nearest-neighbour subgraph of the cubic lattice. The general factorization and conditional-average identities apply to finite graphs and justify that diagnostic separately.

The original universal graph-based iff, its unsupported cancellation argument, and claims of two complete models of all axiom sentences are deferred. No physical reading is selected. A component touching two recorded sites is not by itself a proved sufficient condition for different normalized laws in general.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Finite supplied-law marginalization; universal graph criterion and physical reading selection remain outside this theorem."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independent source review and finite evidence; independent audit remains separate."
conditional_surface_status: "Explicit finite positive models, scoped attachment factors and named graph examples only."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The [axiom memo](MINIMAL_AXIOMS_2026-06-29.md) provides framework context, without selecting either supplied probability convention. The [finite-window static-law source](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md) supplies the product-law reading; the [possibility-covariance source](POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md) supplies the conditional sphere/value-covariance context. These conditional inputs do not establish two models satisfying every framework requirement.

'''
objects=orig[orig.index('Declared objects.'):orig.index('## Prior art and what is new')]
objects=objects.replace('and the uniform measure `dσ`','and the rotation-invariant surface-area measure `dσ` of total mass `4π`')
objects=objects.replace('- **Sites.**','- **Sites.**')
objects += '\nFor the separately labeled abstract-graph diagnostic, replace only the cubic-lattice graph by its explicitly listed finite graph. This extension is a mathematical diagnostic, not a proposed lattice geometry. Using normalized sphere measure instead multiplies the displayed integrals by fixed constants which cancel in normalized laws.\n\n'
proof=orig[orig.index('## Theorem Q1'):orig.index('## Corollary Q5')]
proof=proof.replace('(Executed on the plaquette with one unrecorded site: D4.)','(D4 checks the identity on the explicitly abstract square-plus-vertex graph.)')
proof=proof.replace('whenever every component of `E` touches exactly one recorded site.','whenever every component of `E` touches at most one recorded site. A component with no attachment has no recorded argument and is constant by definition.')
proof=proof.replace('If `C` is a path of `k` internal bonds whose end sites attach to `x` and `y` respectively,','If `C` consists of a path of `k` internal bonds with exactly the two endpoint bonds to `x` and `y` and no other attachments,')
proof=proof.replace('strictly increasing in `v_x·v_y`;','with value `4π` at `v_x + v_y = 0` by continuity and strictly increasing in `v_x·v_y`;')
proof=proof.replace('## Theorem Q4 — the witnesses','## Theorem Q4 — named finite-graph witnesses')
proof=proof.replace('(a) `W` a plaquette, `E` one site adjacent to two adjacent corners:', '(a) On an abstract graph, `W` is a four-cycle and `E` one vertex joined to two adjacent cycle vertices (a triangle is present; this is not a cubic-lattice fixture):')
proof=proof.replace('whose combined factor is the entrywise square of `φ²` and is nonconstant unless `p = q = r` (E1).','whose combined factor is the entrywise square of `φ²` and is nonconstant unless `p = q = r`: the entries of `φ²` are positive and squaring is injective on positive reals, so this follows from (b). E1 checks the sector formulas and a named nonconstant example; it is not an exhaustive numerical test.')
fences=["This note proves finite component factorization, conditional averaging, at-most-one-attachment constancy, scoped bridge and path factors, and named finite graph witnesses for supplied positive static models; it does not prove a universal graph-based equivalence or select a physical reading.","No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.","The mathematical imports and supplied probability conventions are explicit; they do not establish a physical interpretation."]
post='''## Conditional averaging and scope

For every finite exterior, the integrated law is a mixture of the conditional exterior-record laws with the actual exterior marginal weights. A bound on an expectation that holds uniformly for every exterior record therefore holds after averaging. This does not by itself transfer nonlinear properties or certify every result from a historical lane. A full finite torus has no exterior in this construction; no comparison of alternative infinite-volume state selections is asserted.

The two declared finite probability conventions can differ, as the valid cube example shows. The candidate clauses “sum over unrecorded possibilities” and “normalize over recorded sites alone” are descriptive alternatives, not adopted axiom readings. No all-axiom consistency or logical independence theorem follows solely from the finite witnesses.

## No-go applicability

N1: General normalized equality is equivalent to the PRODUCT of component factors being constant on recorded configurations (the base density is strictly positive). At most one attachment per component is sufficient. The converse based only on graph attachments is deferred. Distinct factors can share recorded arguments; their being written as a product does not rule out cancellation.
N2: No repository no-go wall is a premise.
N3: The rule, graph and probability convention are explicit supplied objects; no physical interpretation is hidden in the calculation.
N4: The two linked scientific parents supply conditional model context; the axiom memo is framework context. The commutant statement and sphere integration are mathematical tools stated below.
N5: Finite spectral, symbolic path, sphere-integral and rational graph calculations test the named formulas. The cube and pendant fixtures are lattice examples; the triangle-containing diagnostic is an abstract graph. No finite census proves the deferred universal converse.
N6: Neither the registered primitives nor these finite examples supply a preferred reading.
N7: General marginalization is standard. The useful content is the explicit attachment factors, exact scoped examples and conditional-average identity under the stated assumptions.
N8: The complete original source, numerical controls, historical claims and failed proof of the universal converse remain in the recovery archive.

## Boundaries and non-claims

'''+ '\n\n'.join(fences)+'''

## Imports

The two scientific parents and framework context are linked above. The finite factorization and averaging identities are proved here. The six-axis spectral decomposition is proved directly. The general two-attachment representation uses the stated standard commutant fact for pairwise inequivalent irreducible representations (Schur); this is a mathematical import, not physical authority. The sphere integral uses polar coordinates. No imported result selects a probability convention.

## Recovery and verification

All 22 original path/mode/blob versions, original broad claims, historical control source and output, and prior review assertions are preserved in the [original recovery archive](work_history/review_loop/pr8158/README.md). Historical review and execution assertions are not current evidence. The original branch is retained for the deferred universal and physical claims.

The [runner](../'''+runner+''') and its [canonical capture](../logs/runner-cache/'''+Path(runner).stem+'''.txt) provide 20 checks, including metadata and scope predicates. They do not prove the deferred graph converse. The 13 original mutation routes are preserved in source and archive; they are not rerun or claimed as fresh evidence here.

```bash
python3 '''+runner+'''
```

Expected final line: `TOTAL: PASS=20 FAIL=0`.
'''
s=front+objects+proof+post
assert not (w/newnote).exists();(w/newnote).write_text(s)
t=code.replace(oldnote,newnote).replace(Path(oldnote).stem.lower(),cid)
t=t.replace('"""Exact checks: unrecorded sites — the free-window reading (R1) and the integrated-exterior reading (R2) of the static law differ\nexactly when an unrecorded component touches two recorded sites.','"""Exact finite component factors and scoped marginalization diagnostics.\nNo universal graph-based converse is tested or claimed.')
t=t.replace('the plaquette-plus-site witnesses','the abstract square-plus-site diagnostics').replace('the plaquette with one unrecorded site on two adjacent corners','the abstract square-plus-vertex graph with a triangle (not a cubic-lattice fixture)').replace('on the plaquette with one unrecorded site,','on the abstract square-plus-vertex diagnostic,').replace('exact plaquette and cube witnesses','abstract-graph diagnostics and genuine cube witnesses')
a=t.index('FENCES = (');b=t.index('\nFORBIDDEN =',a);t=t[:a]+'FENCES = '+repr(tuple(fences))+'\n'+t[b:]
t=t.replace('lattice_wide: Q1-Q3 proved for every finite recorded set with a finite unrecorded exterior and every non-constant rule of the two families; the readings\' intent not claimed','lattice_wide: component factorization and at-most-one-attachment sufficiency are proved analytically; general attachment-only converse deferred; finite diagnostics do not prove it')
assert not (w/runner).exists();(w/runner).write_text(t);(w/runner).chmod(0o755);compile(t,runner,'exec')
(r/'drain8158-author-live.json').write_text(json.dumps({'oldnote':oldnote,'note':newnote,'runner':runner,'head':head,'source_only_draft':True,'primary_executions':0},indent=2)+'\n')
(r/'drain8158-author-corrections-v1.patch').write_text(''.join(difflib.unified_diff(orig.splitlines(True),s.splitlines(True),fromfile='original/'+oldnote,tofile='corrected/'+newnote))+''.join(difflib.unified_diff(code.splitlines(True),t.splitlines(True),fromfile='original/'+runner,tofile='corrected/'+runner)))
print('draft authored; arithmetic unchanged; source metadata/resource plan awaits fulloriginalreview')
