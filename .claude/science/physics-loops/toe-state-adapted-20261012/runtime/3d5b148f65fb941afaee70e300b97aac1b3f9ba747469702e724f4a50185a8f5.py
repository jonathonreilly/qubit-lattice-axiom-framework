from pathlib import Path
import hashlib, json
from datetime import datetime, timezone

S = Path(__file__).resolve().parent
R = S / 'state_adapted_refinement_review'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
anchors = {
    'STATE_ADAPTED_REFINEMENT_PROBE.md': '459868fcd7f80fa3063c9e7f7a6d62df393eb80f2edc72b221ecda533ba2a971',
    'STATE_ADAPTED_REFINEMENT_REVIEW.md': '2cd925efe30feaea7807ecbc2b21dcdd7c8768d4261d839edb559ca281263700',
    'state_adapted_refinement_review/FINAL_REVIEW_MANIFEST.json': 'a936cf032bcb328929e2ed32fb59e3420f813a9e7b2b447873e7c144263ddc2a',
    'state_adapted_refinement_review/FINAL_REVIEW_RECEIPT.json': '8f9c1d292d8212c5b7236a0105f8c11c255f43e219085a5267cbd018c3e31046',
    'state_adapted_refinement_review/FINAL_SOURCE_REFRESH.json': '2580d4adfc9d78717e0d1596a531e4871f26c4eddaf9215b5681e032d24ab21f',
}
for p, h in anchors.items():
    assert sha(S / p) == h, p
manifest = json.loads((R / 'FINAL_REVIEW_MANIFEST.json').read_text())
for p, h in manifest['files'].items():
    assert sha(S / p) == h, p
refresh = json.loads((R / 'FINAL_SOURCE_REFRESH.json').read_text())
for row in refresh['checks']:
    assert row['expected_sha256'] == row['actual_sha256'] == sha(Path(row['path'])), row
    assert row['match'] is True
assert len(manifest['files']) == 284 and len(refresh['checks']) == 440
core = S / 'state_adapted_refinement/frozen/STATE_ADAPTED_REFINEMENT_PROBE.md'
assert sha(core) == '49cb5895c5d4b6b88256d5a7bdca471a0fd4c59d1a6c585b733007235a7a7f68'
assert (S / 'STATE_ADAPTED_REFINEMENT_PROBE.md').read_bytes().startswith(core.read_bytes())
evidence = [
    'State_adapted_refinement_root_analytic_read.json',
    'state_adapted_author_root_verification_v2/RESULT.json',
    'state_adapted_independent_root_verification/RESULT.json',
    'state_adapted_control_repair/ROOT_COMPARISON.json',
    'state_adapted_refinement_review/REPAIR_ARITHMETIC_DISCRIMINATION.md',
    'state_adapted_refinement_review/INTEGRITY_PROTOCOL.md',
    'state_adapted_refinement_review/REPAIR_EVIDENCE_VERIFICATION.json',
]
coverage = {
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'status': 'complete_source_bound_root_review',
    'anchors': anchors,
    'review_manifest_files': 284,
    'refreshed_source_identities': 440,
    'prior_root_evidence': {p: sha(S / p) for p in evidence},
    'manual_coverage': [
        'Complete 517-line analytic core and exact final appendix, author protocol, helpers, variants and all 260 original author predicates.',
        'Complete fresh review, independent derivation, scientific and integrity helpers, protocols, all case metadata and gates, extrema and all 36 quadrature values.',
        'Final repair arithmetic discrimination: changing proposed quartic coefficient to 16 lambda leaves (1-lambda)s^4; wrong coefficients are detected.',
        'Central polar-frame, same-sequence section equivalence, fourth-power support pole and even-energy rank-two variance calculations hand reconstructed.',
    ],
    'mechanical_coverage': [
        'All 384 complex independent moment residuals and 24 gates recomputed from complete stored raw records; the earlier truncated print is not counted as full manual data coverage.',
        'Complete original and repair receipts, source maps and streams checked; only symbolic row 3 and derived summary differ in the arithmetic repair.',
        'Three copied integrity fixtures checked: valid, pre-launch hash tamper rejection, and preserved child-exit-7 outer-exit-0 survivor.',
        'Final manifest, all 440 refreshed source identities and immutable analytic core prefix rechecked by this program.',
    ],
    'limits': [
        'Separate context of same selected model family, formula-exposed; not blinded or model-diverse.',
        'Root coauthored the route and arithmetic repair; root checks are not independent authorship.',
        'Many-body checks are finite diagnostics and Fourier quadrature is not interval certified; infinite-dimensional claims rely on the analytic proofs.',
        'Same-sequence Cauchy equivalence does not identify distinct recursively refined initial seeds.',
        'Exact chosen-state preservation does not provide finite-scale locality or actual-energy compatibility; counterexamples are retained.',
        'Mixed-flow convergence uses exact pinned parent hypotheses and domains; no Haar H2 rate or new continuum generator-domain result.',
        'No Lean theorem is claimed for this unit; retained status and a combined independent audit remain separate.',
    ],
    'pending': [],
    'science_rerun': False,
    'editable_prompt_files_changed': [],
}
(S / 'State_adapted_refinement_root_review_coverage.json').write_text(json.dumps(coverage, indent=2) + '\n')
(S / 'STATE_ADAPTED_REFINEMENT_MILESTONE_GATE.md').write_text('''# State-adapted refinement milestone gate

Status: OPEN for a regular dependent review PR as a bounded conditional theorem
for the explicitly chosen one-dimensional free gapped chain. This is not an
independent retained audit verdict. Exact source and complete review coverage
are bound in `State_adapted_refinement_root_review_coverage.json`.

The construction preserves the chosen finite-scale quasi-free states exactly.
Its embeddings give the same intrinsic norm-Cauchy section algebra and the
same geometric local continuum quotient for the same microscopic sequences.
Pinned parent hypotheses give the actual compact-parameter mixed-flow limits.
The note also proves infinite support of the adapted local image and an even
observable witnessing failure of exact actual-energy compatibility. Those
fixed-construction failures are not universal failures of refinement schemes.
The distinct energy-adapted follow-up is not imported into this theorem.

Root read the complete argument and necessary premises, all author sources and
raw rows, the full fresh independent reconstruction and its helper sources.
Every independent complex moment and gate was checked against complete stored
data. The reviewer froze a neutral plan before target exposure and evidence
before opening author helpers. It is a separate context of the same model
family. Root is a coauthor, and neither blinded nor diverse-family review is
claimed. The infinite-dimensional theorem remains an analytic proof.

Publication must preserve the original 85/86 baseline and both original
mutants. The root arithmetic repair has a separately frozen source, baseline
86/86, and corrected mutants 70/86 and 85/86; it changes only the exact
half-angle reduction and its derived summary. The two-row author supplement
remains explicitly post-observation. No failed row or survivor is discarded.
Independent finite many-body and quadrature checks retain their scope limits.
The copied integrity test rejects a hash tamper before launch, but deliberately
retains the exit-7 child whose outer recorder returns zero: outer exit alone is
not a correctness certificate.

The publication must name the concrete-chain, four local-flow and dyadic
parents, preserve complete immutable source and subprocess evidence, and
claim no finite-scale locality, exact energy compatibility, uniform locality
constant or Haar H2 error rate. No new axiom, prompt, retained status, or audit
verdict is authorized by this gate. Combined audit remains a later obligation.
''')
print(json.dumps({'status': coverage['status'], 'review_manifest_files': 284, 'source_identity_checks': 440, 'coverage_sha256': sha(S / 'State_adapted_refinement_root_review_coverage.json'), 'gate_sha256': sha(S / 'STATE_ADAPTED_REFINEMENT_MILESTONE_GATE.md')}))
