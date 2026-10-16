"""Root source/text closure after complete changed-wrapper and program inspection."""
from pathlib import Path
from datetime import datetime, timezone
import ast, hashlib, json

N = Path(__file__).resolve().parents[1]
D = N / 'readiness_resources_publication_draft'
Q = N / 'readiness_resources_root_publication_review'
P = D / 'proposal'
W = N.parent / 'correlation_worktree'
PACKET = '.claude/science/physics-loops/toe-readiness-resources-20261015'
NOTE = 'docs/READINESS_RESOURCE_ALTERNATIVES_BOUNDED_THEOREM_NOTE_2026-10-15.md'
PRIMARY = 'scripts/readiness_resource_alternatives_2026_10_15.py'

def pin(p):
    b = p.read_bytes()
    return {'path': str(p), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

def js(p):
    return json.loads(p.read_bytes())

def check(p, row):
    got = pin(p)
    assert all(got[k] == row[k] for k in ('bytes', 'sha256')), str(p)

assert pin(D/'FINAL_FREEZE.json')['sha256'] == '2ef4152f629f9985ee5872fcad1fa45811561b8e82b6bb0076a7366600995ce9'
freeze = js(D/'FINAL_FREEZE.json')
for row in freeze['files']:
    check(D/row['path'], row)
assert {p.relative_to(D).as_posix() for p in D.rglob('*') if p.is_file()} == {r['path'] for r in freeze['files']} | {'FINAL_FREEZE.json'}
note = (P/NOTE).read_bytes()
assert note.split(b'\n\n<!-- BEGIN EXACT ', 1)[0] == (D/'wrapper.md').read_bytes().rstrip()+b'\n'
bodies = js(P/PACKET/'BODY_MAP.json')['bodies']
source_rows = js(P/PACKET/'SOURCE_MANIFEST.json')['sources']
for row in bodies:
    raw = note[row['start_byte_inclusive']:row['end_byte_exclusive']]
    assert len(raw) == row['bytes'] and hashlib.sha256(raw).hexdigest() == row['sha256']
    assert note.count(raw) == 1
    matches = [r for r in source_rows if r['recovery'].get('body_name') == row['name']]
    assert len(matches) == 1 and Path(matches[0]['original_path']).read_bytes() == raw
for row in source_rows:
    check(Path(row['original_path']), row)
    if row['recovery']['kind'] == 'blob':
        check(P/row['recovery']['path'], row)
parents = js(P/PACKET/'DEPENDENCIES.json')['dependencies']
for row in parents:
    check(W/row['path'], row)
    body = row['accepted_body_interval']
    raw = (W/row['path']).read_bytes()[body['start_byte_inclusive']:body['end_byte_exclusive']]
    assert len(raw) == body['bytes'] and hashlib.sha256(raw).hexdigest() == body['sha256']
    assert (W/row['path']).read_bytes().count(raw) == 1
manifest = js(P/PACKET/'INPUT_MANIFEST.json')
for row in manifest['inputs']:
    check(P/row['path'], row)
constants = {}
for node in ast.parse((P/PRIMARY).read_text()).body:
    if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
        try:
            constants[node.targets[0].id] = ast.literal_eval(node.value)
        except (ValueError, TypeError):
            pass
expected = {r['path'] for r in manifest['inputs']} | {PACKET+'/INPUT_MANIFEST.json', PACKET+'/ACTUAL_BINDING.json'} | {r['path'] for r in parents}
assert set(constants['AUDIT_INPUT_PATHS']) == expected and len(constants['AUDIT_INPUT_PATHS']) == len(expected)
generated = (D/'primary_template.py').read_text().replace('"__MANIFEST_SHA256__"', repr(pin(P/PACKET/'INPUT_MANIFEST.json')['sha256']))
generated = generated.replace('__AUDIT_INPUT_PATHS__', repr(tuple(sorted(expected))))
generated = generated.replace('__EXPECTED_BODIES__', repr({r['name']:r['sha256'] for r in bodies})).rstrip()+'\n'
assert generated == (P/PRIMARY).read_text()
receipts = []
for label, code in [('build',1),('build_corrected',0),('verify',0),('seal',0)]:
    r = D/'metadata_runs'/label
    e, launch = js(r/'EXECUTION.json'), js(r/'LAUNCH.json')
    assert e['returncode'] == code and e['timed_out'] is False
    for field in ['launch','stdout','stderr']:
        check(Path(e[field]['path']), e[field])
    for f, field in [('child_source.py','source'),('recorder_source.py','recorder')]:
        check(r/f, launch[field])
    receipts.append({'label':label,'actual_exit_code':code,'receipt':pin(r/'EXECUTION.json')})
assert b"KeyError: 'files'" in (D/'metadata_runs/build/stderr').read_bytes()
assert not (P/PACKET/'ACTUAL_BINDING.json').exists()
Q.mkdir(exist_ok=False)
record = {
    'kind':'root_source_publication_review', 'reviewed_utc':datetime.now(timezone.utc).isoformat(),
    'root_read_complete':True, 'source_draft_freeze':pin(D/'FINAL_FREEZE.json'),
    'note':pin(P/NOTE), 'primary':pin(P/PRIMARY), 'wrapper':pin(D/'wrapper.md'),
    'current_reading':'Complete wrapper; entire primary logic with literal tuple structurally checked; complete build/verify/seal/record programs; all packet Markdown and outer handoff/review map/coverage/delivery. Unchanged exact five mathematical bodies and accepted parents reused from prior complete readings.',
    'sealed_members_verified':len(freeze['files']), 'five_body_pins':bodies, 'source_rows_verified':len(source_rows),
    'parents':parents, 'metadata_receipts':receipts,
    'existing_source_acceptances':{
        'fixed_duration':pin(N/'polynomial_joint_readiness_root_review/ACCEPTANCE.md'),
        'fast':pin(N/'fast_joint_readiness_root_review/ACCEPTANCE.md')},
    'decision':'Publication interpretation accepted at existing conditional source scope; actual checkout binding/integration still pending.',
    'required_current_status_clarification':'Distinguish already pinned canonical joint note from the resource note actual checkout binding in current status certificate; preserve historical source draft.',
    'integration_requirement':'Bind actual captured receipt schemas/source/streams/exit with semantic checks; inspect complete changed integration logic before execution.',
    'scope':'Source integrity and publication reading only; no new independent mathematical replication or retained verdict.',
    'scientific_programs_run':0, 'primary_runs':0, 'historical_programs_replayed':0,
    'editable_prompt_files_changed':[], 'actual_binding':None,
    'verification_limits':['Full current-main/cumulative-stack landing pipeline open','Independent retained audit open','Native controls, memory, isolation, energy/detector and full-program realization remain open']}
(Q/'ROOT_REVIEW.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'root_review':pin(Q/'ROOT_REVIEW.json'),'members':len(freeze['files']),'scope':record['scope']}))
