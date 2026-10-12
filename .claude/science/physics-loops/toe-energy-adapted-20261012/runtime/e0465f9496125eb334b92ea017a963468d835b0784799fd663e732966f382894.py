from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

S = Path(__file__).resolve().parent
R = S / 'energy_adapted_refinement_review'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
anchors = {
    'ENERGY_ADAPTED_REFINEMENT_PROBE.md': '65d49c82eb14b88e4880983eb8b41ecb5141cb0ff00f4e5e4760bbb12a151b9d',
    'ENERGY_ADAPTED_REFINEMENT_REVIEW.md': '2e6fb1da31b3a12e2ce998123ce3f09d9766f3fb375766f99927b840212dc9f0',
    'energy_adapted_refinement/final_manifest.json': 'a9287eb6b86016905a2e11e3e751beaee91238e5e079ca1938bdbe3425540466',
    'energy_adapted_refinement_review/FINAL_MANIFEST.json': '2658ca8d78d15b0a92b377abf913a8f7bb209b7d57571bfecf8e4bb587896e3f',
    'energy_adapted_refinement_review/INDEPENDENT_EVIDENCE.seal.json': '02471e96867ced1abac3cdc464c7e690e51aa542ff35fc6328084d7bf63ae5d3',
}
for p, h in anchors.items():
    assert sha(S / p) == h, p
manifest = json.loads((R / 'FINAL_MANIFEST.json').read_text())
assert len(manifest['files']) == 333
for row in manifest['files']:
    p = R / row['path']
    assert sha(p) == row['sha256'] and p.stat().st_size == row['bytes'], p
receipt = json.loads((R / 'FINAL_RECEIPT.json').read_text())
assert receipt['report_sha256'] == anchors['ENERGY_ADAPTED_REFINEMENT_REVIEW.md']
assert receipt['final_manifest_sha256'] == sha(R / 'FINAL_MANIFEST.json')
refresh = json.loads((R / 'FINAL_SOURCE_REFRESH.json').read_text())
for row in refresh['files']:
    assert sha(Path(row['path'])) == row['expected'] == row['actual_at_final_refresh'], row
assert len(refresh['files']) == 18
core = S / 'energy_adapted_refinement/frozen/ENERGY_ADAPTED_REFINEMENT_PROBE.md'
assert sha(core) == 'f442f32f6c40102d3378f0dc96145250b78c1c13275683ac2bc1f9125828bd80'
assert (S / 'ENERGY_ADAPTED_REFINEMENT_PROBE.md').read_bytes().startswith(core.read_bytes())
evidence = [
    'Energy_adapted_root_analytic_read.json',
    'verify_energy_adapted_author_root.py',
    'energy_adapted_author_root_verification/RESULT.json',
    'verify_energy_adapted_independent_root.py',
    'verify_energy_adapted_independent_root_v2.py',
    'energy_adapted_independent_root_verification_v2/RESULT.json',
    'energy_adapted_refinement_review/FINAL_RECEIPT.json',
    'energy_adapted_refinement_review/FINAL_SOURCE_REFRESH.json',
]
coverage = {
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'status': 'complete_source_bound_root_review',
    'anchors': anchors, 'review_manifest_files': 333, 'refreshed_source_identities': 18,
    'prior_root_evidence': {p: sha(S / p) for p in evidence},
    'manual_coverage': [
        'Complete 415-line analytic core, all 105 final appendix lines, author protocol and all 252 helper/recorder lines; literal variants and all 30 diagnostics.',
        'Complete 218-line independent reconstruction, 74-line check specification, all 346 scientific/recording helper lines, and all five literal source variants.',
        'Full final independent report and its source-refresh qualifications; complete baseline values and every changed mutant value, with identical rows mechanically compared.',
        'Root reconstructed change of measure, exact state/time intertwining, cell alias sign and eventual domain, real complement extension, same-sequence sections, fixed mixed-flow limits, Fourier support and even witnesses, transported periodic boost domain and inverse support motion.',
    ],
    'mechanical_coverage': [
        'Original 69-file author manifest, eight parent pins, six complete receipts, 714 predicates and 30 diagnostic records bound to complete streams.',
        'Independent 212-file evidence seal, twelve complete receipts, all 90 gates recomputed from raw numeric values, and three tamper-guard controls.',
        'All 333 final reviewer files and 18 refreshed source identities rechecked by this program; historical concurrent packaged-tree dirtiness remains documented.',
    ],
    'limits': [
        'Root coauthor; reviewer is a fresh context of the same selected model and effort, neutral plan before target and evidence seal before author helpers, not diverse-family or blinded.',
        'Of 714 author predicate rows, 699 numeric rows were recomputed by the separate reviewer; 15 symbolic/solver booleans are recorded outcomes, not new proofs.',
        'Finite spin matrices, quadrature, finite differences and ODE diagnostics do not prove the infinite-dimensional theorem or provide interval certificates.',
        'Both original mutants survive the loose geometric check; reverse phase improves that diagnostic. All failed checks and survivors remain.',
        'Original nested-session OUTER timeout alone does not guarantee killing a separately sessioned descendant if INNER stalls. All actual original runs completed without timeout.',
        'E23 inverse support motion and eventual aM<2 clarification are explicitly post-execution, with frozen sources unchanged.',
        'F preserves reality while D anticommutes with conjugation and P exchanges with its complement; they are not all real orthogonal maps.',
        'Exact chosen state/time compatibility does not supply finite-scale locality, space/current/boost intertwining, a Haar H2 rate or a microscopic axiom derivation.',
        'Same-sequence Cauchy equivalence does not identify different recursive seeds; pinned supplied-chain and continuum hypotheses remain conditions.',
        'No full N1-N8 mechanical no-go packet PASS, Lean verification, retained audit verdict or whole-tree landing verification is claimed.',
    ],
    'pending': [], 'science_rerun': False, 'editable_prompt_files_changed': [],
}
cp = S / 'Energy_adapted_refinement_root_review_coverage.json'
assert not cp.exists()
cp.write_text(json.dumps(coverage, indent=2) + '\n')
gp = S / 'ENERGY_ADAPTED_REFINEMENT_MILESTONE_GATE.md'
assert not gp.exists()
gp.write_text('''# Energy-adapted refinement milestone gate

Status: OPEN for a regular dependent review PR as a bounded conditional
construction for the supplied one-dimensional free massive chain. This is
not a retained audit verdict. Exact source and review coverage are bound in
Energy_adapted_refinement_root_review_coverage.json.

The dispersion-coordinate half-density embedding preserves the chosen state
and actual time evolution exactly, with nested spectral ranges. Its strong
cell comparison gives the same intrinsic Cauchy sections and geometric local
quotient for the same microscopic sequence. Pinned parent hypotheses supply
the actual compact-parameter mixed-flow limits. The specified finite-scale
map has proved locality, space/current and boost counterexamples; no universal
failure of every refinement or broader physical model follows.

Root read and reconstructed the complete proof and necessary premises, all
author sources, the complete independent reconstruction, all helper sources
and the final report. Complete original evidence was mechanically reconciled.
The separate same-family reviewer froze a neutral plan before target exposure
and evidence before author helpers. Root is a coauthor. The mathematical
argument, rather than a count of diagnostics, supports the conditional theorem.

Preserve baseline 238/0, mutants 190/48 and 226/12, all 30 diagnostics and every
survivor. Independent baseline 15/0 and five variants retain all 63 survivors
and 12 failures. Three copied tamper guards reject altered inputs; no race-free
security guarantee follows. The author's nested-session outer timer alone
does not guarantee descendant cleanup if its inner recorder stalls; original
runs all completed. Preserve the explicit post-execution E23 support-sign and
eventual coordinate-domain clarification and both historical root verification
attempts, including the first bookkeeping filename failure.

The publication must retain transported periodic boost domains, actual current
normalization, exact source revisions and all six direct mathematical parents.
State-adapted refinement is a branch/cache preservation parent, not an assumed
theorem input. No finite-scale local connecting map, Haar H2 rate, massless or
interacting extension, Lean result or broad novelty is claimed. No physical
axiom, prompt, ledger status or audit verdict changes. Full combined landing
validation and independent retained audit remain separate obligations.
''')
print(json.dumps({'status': coverage['status'], 'files_checked': 333, 'source_refresh_checks': 18, 'coverage_sha256': sha(cp), 'gate_sha256': sha(gp)}))
