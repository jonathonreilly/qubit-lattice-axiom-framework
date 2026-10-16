from pathlib import Path
import hashlib, json
from datetime import datetime, timezone

N = Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023')
D = N / 'bus_joint_energy_publication_draft'
R = N / 'root_bus_joint_energy_publication_review'
P = D / 'proposal'
Q = P / '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016'
W = N.parent / 'correlation_worktree'
def pin(p):
    b = p.read_bytes()
    return {'path': str(p), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}
def same(p, row):
    a = pin(p)
    assert (a['bytes'], a['sha256']) == (row['bytes'], row['sha256']), str(p)
def read(p):
    return json.loads(p.read_text())
def put(p, obj):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(obj, indent=2)+'\n')
freeze = read(D/'FINAL_FREEZE.json')
assert pin(D/'FINAL_FREEZE.json')['sha256'] == 'd0997db66b3b7465a8a02a233a6d0b8c56cb48af6571a3659fa49852cb28700f'
for row in freeze['files']:
    same(D/row['path'], row)
manifest = read(Q/'INPUT_MANIFEST.json')
for row in manifest['inputs']:
    same(P/row['path'], row)
sources = read(Q/'SOURCE_MANIFEST.json')['sources']
for row in sources:
    same(Path(row['original']), row)
    same(P/row['recovery_path'], row)
bodies = read(Q/'BODY_MAP.json')['bodies']
for row in bodies:
    raw = (N/row['source']).read_bytes()
    note = (P/row['container']).read_bytes()
    assert note[row['start_byte_inclusive']:row['end_byte_exclusive']] == raw
    assert note.count(raw) == 1
parent = read(Q/'PARENT_BINDING.json')
assert len(parent['canonical_parents']) == 1
for row in parent['canonical_parents']:
    same(W/row['path'], row)
    for b in row['accepted_body_intervals']:
        raw = (W/b['container']).read_bytes()[b['start_byte_inclusive']:b['end_byte_exclusive']]
        assert len(raw) == b['bytes'] and hashlib.sha256(raw).hexdigest() == b['sha256']
paths = sorted({r['path'] for r in manifest['inputs']} | {str((Q/'INPUT_MANIFEST.json').relative_to(P)), str((Q/'ACTUAL_BINDING.json').relative_to(P)), parent['canonical_parents'][0]['path']})
expected = (D/'primary_template.py').read_text().replace('__MANIFEST_SHA256__', pin(Q/'INPUT_MANIFEST.json')['sha256']).replace('__AUDIT_INPUT_PATHS__', repr(paths))
primary = P/'scripts/bus_joint_energy_moments_2026_10_16.py'
assert primary.read_text() == expected
receipts = []
for label in ['build', 'inspection']:
    root = D/'metadata_runs'/label
    launch, run = read(root/'LAUNCH.json'), read(root/'EXECUTION.json')
    assert all(run[k] == v for k, v in launch.items())
    assert run['exit_code'] == 0 and not run['timed_out'] and run['inputs_unchanged_after_run']
    for k in ['child_source_at_launch','original_source_at_launch','recorder','input_identities_at_launch','stdout','stderr']:
        same(Path(run[k]['path']), run[k])
    for row in read(root/'INPUT_IDENTITIES_AT_LAUNCH.json'):
        same(Path(row['path']), row)
    receipts.append(pin(root/'EXECUTION.json'))
inspection = read(D/'VERIFICATION.json')
assert len(inspection['scoped_mutants']) == 9 and all(x['detected'] for x in inspection['scoped_mutants'])
assert not inspection['primary_main_executed']
coverage = '''# Root publication content review\n\nRead the complete new wrapper, all packet prose, primary template, builder, inspector, recorder and sealer. Verified the generated primary differs only by the exact manifest pin and declared input closure. Read the actual metadata launch/execution records and complete stdout/stderr; verified captured source, recorder and input identities. An initially overlong aggregate was truncated; the relevant receipts and streams were reread completely, with long identity lists checked deterministically.\n\nReused the previously fully read and qualified two mathematical bodies at 86a830e1 and 498017c6, their controlling moment acceptance530e64f0 and bus parent1733b296/cc2e519d. Both body intervals are exact and occur once. No mathematical body changed; no scientific executable or primary main was rerun. Reviewed metadata assertions are provenance controls only.\n\nThe wrapper retains the full-space off-code square, reserve cross terms, bus-vacuum cubic cancellation premises, commuting secular generator, distinct all-time formal moments versus finite-window state approximation, actual runtime/phase recomputation, and energy-weighted preparation/calibration costs. Operational measured energy, native source, halt and reuse remain open. Same-model exposed-check limits and missing historical bus launchers remain.\n\nDraft actual-base and root/canonical-binding fields correctly remain unbound. The proposed integration must bind the actual current base and real captured root-review/source/streams; no boolean alone is sufficient. Add the existing actual source-acceptance execution receipt in canonical recovery without rewriting the historical draft statement. Canonical changed-content review and actual phase verification remain separate.\n'''
assert not (R/'READ_COVERAGE.md').exists()
(R/'READ_COVERAGE.md').write_text(coverage)
result = {
 'kind':'root_source_publication_review', 'utc':datetime.now(timezone.utc).isoformat(),
 'root_read_complete':True, 'source_draft_freeze':pin(D/'FINAL_FREEZE.json'),
 'note':pin(P/'docs/BUS_JOINT_ENERGY_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-16.md'),
 'primary':pin(primary), 'body_pins':bodies, 'parent_binding':parent,
 'read_coverage':pin(R/'READ_COVERAGE.md'), 'source_acceptance':pin(N/'bus_joint_energy_root_review/QUALIFIED_ACCEPTANCE.json'),
 'freshness':pin(N/'refresh_before_positive_bias_publication/BINDING_REFS.json'),
 'verified_freeze_members':len(freeze['files']), 'source_aliases':len(sources), 'metadata_receipts':receipts,
 'decision':'Accept reviewed source-preserving package for root integration as conditional support; canonical review remains separate.',
 'required_integration_qualification':'Bind actual root/canonical/base evidence, and include actual source-acceptance receipt and its captured source/streams as separate canonical recovery; preserve the immutable draft.',
 'scientific_programs_run_this_review':0, 'primary_runs':0, 'historical_programs_replayed':0,
 'limits':['Content review records actual reading; this execution checks identity only.','No retained audit, blind replication, device realization or measured-energy identification.','Canonical changed content and phased integration are not yet accepted.'],
 'editable_prompt_files_changed':[]}
put(R/'REVIEW.json', result)
print(json.dumps({'review':pin(R/'REVIEW.json'),'verified_freeze_members':len(freeze['files']),'metadata_mutants':9,'canonical_binding':None},indent=2))
