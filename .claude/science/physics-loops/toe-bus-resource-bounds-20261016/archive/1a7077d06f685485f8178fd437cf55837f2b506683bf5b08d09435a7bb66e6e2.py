"""Metadata-only sealing; no scientific program execution."""
from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

OUT = Path(__file__).resolve().parent
N = OUT.parent
W = N.parent / 'correlation_worktree'

def identity(path):
    path = Path(path)
    raw = path.read_bytes()
    return {'path': str(path), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}

def checked(path, sha, coverage, role):
    item = identity(path)
    assert item['sha256'] == sha, (str(path), item['sha256'], sha)
    item.update(read_coverage=coverage, role=role, identity_refreshed=True)
    return item

def write(name, obj):
    (OUT / name).write_text(json.dumps(obj, indent=2) + '\n')

sources = [
 checked(N/'quantitative_bias_selection_root_proposal/PROPOSED_LEMMAS.md',
  '7fb842e6bcdfab8498c7a336d5fcf6c3701b76b6a588da0e75a10bda14cc4baf',
  'Complete, first scientific source read in this task.', 'Exposed proposal under review, not an accepted premise.'),
 checked(N/'quantitative_bias_selection_root_proposal/FREEZE.json',
  '7cf5878a88b72e4bcd3bce017fe7e411a671dd5126d9455e0258ec2888f5c812',
  'Complete; every listed identity checked.', 'Proposal freeze.'),
 checked(N/'quantitative_bias_selection_root_proposal/PRIOR_RESULT_RECONCILIATION.md',
  '4978e57f67c30b7c455123d190cdc71bf4f210be19126e304f56158b465f0567',
  'Complete, read before reconstruction.', 'Existing interpolation result and novelty boundary.'),
 checked(N/'positive_chain_strong_point_candidate/DERIVATION.md',
  '54cdf957111f03d6efadd2d6df91a871ea943859dea8639c47343022bfab0d12',
  'Complete argument previously read and reviewed by this same worker; unchanged identity reused.',
  'Qualified positive-chain premise, including strong C and leading coefficient.'),
 checked(N/'positive_chain_exposed_check/REVIEW.md',
  'ac486c1c75de92cd5da05ceeed178ad2fddf2d7a3ddde214f7889df92b084239',
  'Own completed full proof review reused at unchanged identity.', 'Prior exposed check; not fresh independence.'),
 checked(N/'positive_chain_root_review/QUALIFIED_ACCEPTANCE.json',
  '382531923d20c156d6d05b6a440b26ac11af64e934950738e14fbd452c9a24e4',
  'Complete current read.', 'Qualified source acceptance, explicitly not retained audit.'),
 checked(N/'positive_chain_root_review/FINAL_QUALIFICATIONS.md',
  'bf868c7fa27b24cae2586a1cb1dfb1c56a55778b1817879ef6e3445f23537a5f',
  'Complete current read.', 'Controlling access, scope, preparation, efficiency and parent conditions.'),
 checked(W/'docs/ACCURACY_SCALED_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md',
  'c0332b37e159ecf6aaa70143f65793ee424c3df3a77e8840df91043ddf47bde2',
  'Current complete reads of sections 2-3, lines 59-120, and exposed assessment 3, lines 445-486; prior lines 1-205. Remainder not newly claimed read.',
  'Existing quantitative upper-half polynomial interpolation and finite strict selection.'),
]
reconciliation_freeze = identity(N/'quantitative_bias_selection_root_proposal/RECONCILIATION_FREEZE.json')
reconciliation_freeze.update(read_coverage='Complete current read; all listed identities checked.', role='Root reconciliation freeze.')
sources.append(reconciliation_freeze)

freeze_members = []
for name in ['FREEZE.json', 'RECONCILIATION_FREEZE.json']:
    obj = json.loads((N/'quantitative_bias_selection_root_proposal'/name).read_text())
    for rec in obj['files']:
        actual = identity(rec['path'])
        assert actual == rec, (actual, rec)
        freeze_members.append(actual)

acceptance = json.loads((N/'positive_chain_root_review/QUALIFIED_ACCEPTANCE.json').read_text())
acceptance_members = []
for key in ['candidate', 'candidate_freeze', 'review', 'review_freeze', 'qualifications']:
    rec = acceptance[key]
    actual = identity(rec['path'])
    assert actual == rec, (key, actual, rec)
    acceptance_members.append({'key': key, **actual})

governance = [
 checked(N/'bootstrap/planning/AGENTS.md',
  '3d409e93abb3b58796a9c10ca6d21ba93b7edc73b8fb24e7364da97c805580a9',
  'Complete prior coherent-task read reused; current identity refreshed.', 'Captured task instructions.'),
 checked(N/'bootstrap/sources/docs/ai_methodology/SCIENCE_WORKFLOW.md',
  '05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce',
  'Complete prior coherent-task read reused; current identity refreshed.', 'Science workflow.'),
 checked(N/'bootstrap/sources/docs/ai_methodology/skills/workhorse/SKILL.md',
  '9801055aea637b0e6f765f1558113a9998fe6b4d5a213b0d03d096fe96cb4cdb',
  'Complete prior coherent-task read reused; current identity refreshed.', 'Authorized bounded worker scope.'),
 checked(Path('/Users/jonreilly/.codex/skills/physics-claim-reviewer/SKILL.md'),
  '9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455',
  'Complete prior coherent-task read reused; current identity refreshed.', 'Already applied exposed scientific review scope.'),
]

receipt = json.loads((OUT/'check_run/EXECUTION.json').read_text())
launch = json.loads((OUT/'check_run/LAUNCH.json').read_text())
assert receipt['exit_code'] == 0 and not receipt['timed_out']
for key in ['source_at_launch', 'launcher_at_launch', 'stdout', 'stderr']:
    assert identity(receipt[key]['path']) == receipt[key], key
for key in launch:
    assert receipt[key] == launch[key], key
assert (OUT/'check_quantitative.py').read_bytes() == (OUT/'check_run/executed_source.py').read_bytes()
assert (OUT/'run_check.py').read_bytes() == (OUT/'check_run/launcher_at_launch.py').read_bytes()
assert identity(OUT/'INITIAL_FINDINGS.md')['sha256'] == '3f3dc6486346290863e2386d2173b8a9b9fd13d0026ae963c38c3681ef11eeb3'

utc = datetime.now(timezone.utc).isoformat()
write('SOURCE_MANIFEST.json', {
 'utc': utc, 'task': 'Quantitative weak positive bias spectral and input-precision check',
 'sources': sources, 'governance_reused': governance,
 'exposure': 'Exposed same-model extension. Reviewer authored earlier bus and static transfer material and the previous positive-chain check. No fresh independent parent validation claimed.',
 'new_analytical_content': ['Complex Gram factorization with all zero/repeated cases retained', 'Individual spectral and port factor bounds', 'Uniform explicit matrix-input determinant sensitivity and finite entry-bit request'],
 'reused_result': 'Canonical upper-half interpolation and finite strict selection; no novelty claimed.',
 'excluded': ['Unaccepted padding extension', 'Full bus Q/P spectral gap', 'Efficient source/chain construction', 'Oracle-time bound', 'Native preparation', 'Retained audit status'],
 'old_author_checkers_run': False, 'scientific_executions': 1,
 'external_research_sources': [], 'editable_prompt_files_changed': [],
 'writes_confined_to': str(OUT)
})
write('VERIFICATION.json', {
 'utc': utc, 'kind': 'Metadata identity verification; no scientific computation or rerun.',
 'root_freeze_members_verified': freeze_members,
 'qualified_chain_acceptance_references_verified': acceptance_members,
 'science_receipt_verified': identity(OUT/'check_run/EXECUTION.json'),
 'source_at_launch_and_launcher_match_working_sources': True,
 'all_scientific_streams_preserved_and_read_complete': True,
 'scientific_failures': [],
 'source_location_corrections': ['Initial canonical hash path contained THEM instead of THEOREM and failed; corrected exact path matched expected identity.', 'Broad heading search truncated; not counted as coverage. Required sections reread completely.'],
 'git_operations': 0, 'canonical_writes': 0, 'scientific_reruns': 0
})
(OUT/'CHECKPOINT.md').write_text('''# Final checkpoint

The scoped quantitative result follows, conditional on the unchanged positive-chain supplier and its physical access qualifications. REVIEW.md contains the complete proof, including all zero/repeated cases, complex adjoints, dimensions and explicit matrix-input precision.

The existing canonical upper-half interpolation grid is reused with one consistent constant set. At a selected weak bias the nonzero-gap, signed-gap-separation and off-diagonal-port lower bounds are fixed constants times Lambda^(D/2), D=d(d-1)[d(d-1)+1]. The determinant evaluation requests explicitly bounded absolute entry precision; this is not a runtime bound on arbitrary computable oracles.

One new exact noncommuting complex test completed successfully. It checks all seven grid nodes, joint input perturbations, actual projector-derived transitions, zero/repeated/missing-transition cases, and omitted-adjoint and wrong-exponent mutants. Source, launcher, argv/cwd, limits, full streams and receipt are preserved. Old author checkers were not run. Initial analytical findings were frozen before test construction.

No unresolved mathematical equation remains within this narrow claim. Full bus Q/P separation, efficient chain/source construction, native preparation and complete runtime calibration remain outside its scope. No padding extension is imported. No fresh independent parent validation or retained audit status is claimed. Root owns acceptance and publication. No editable prompt file changed.

Recover from REVIEW.md, SOURCE_MANIFEST.json and check_run/EXECUTION.json. REVIEW_FREEZE.json binds every deliverable member. Preserve these files; any future extension requires a new directory or explicit revision history.
''')

members = [identity(p) for p in sorted(OUT.rglob('*')) if p.is_file() and p.name != 'REVIEW_FREEZE.json']
write('REVIEW_FREEZE.json', {
 'utc': datetime.now(timezone.utc).isoformat(),
 'status': 'Frozen exposed same-model source review and extension; root acceptance pending.',
 'scope_verdict': 'Narrow factorization, spectral factor bounds, and explicit matrix-input precision established conditionally; no broader supplier claim.',
 'members': members,
 'scientific_executions': 1, 'retained_audit': False,
 'fresh_independent_parent_validation': False,
 'editable_prompt_files_changed': []
})
print(json.dumps({'review': identity(OUT/'REVIEW.md'), 'freeze': identity(OUT/'REVIEW_FREEZE.json'), 'members': len(members), 'verified_science_exit': receipt['exit_code'], 'utc': utc}, indent=2))
