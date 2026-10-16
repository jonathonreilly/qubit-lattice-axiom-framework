"""Capture and verify review sources only; never import or execute science."""
from pathlib import Path
from datetime import datetime, timezone
import ast
import hashlib
import json
import subprocess
import time

O = Path.cwd().resolve()
N = O.parent
S = N / 'local_sine_preparation_root_proposal'
W = N.parent / 'correlation_worktree'
MAIN = '41f192b2dcee96d9967e0e01ad50c5f1229ab252'
EXPECTED_FREEZE = '928ca72cfe15b8c716ab18b609725a451b80a8d2bf117f331aafa2c89eb07108'
EXPECTED_PROPOSAL = 'db759157520cfb3b56777d6540461b6453b0bbfe352034a3ba5514a58edea826'


def pin(path):
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def now():
    return datetime.now(timezone.utc).isoformat()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + '\n')


def capture(source, relative, role):
    target = O / relative
    assert not target.exists(), target
    target.parent.mkdir(parents=True, exist_ok=True)
    before = pin(source)
    target.write_bytes(source.read_bytes())
    assert pin(source) == before
    copied = pin(target)
    assert (before['bytes'], before['sha256']) == (copied['bytes'], copied['sha256'])
    return {'source': before, 'capture': copied, 'role': role}


assert O.name == 'local_sine_preparation_exposed_check'
assert pin(S / 'FINAL_FREEZE.json')['sha256'] == EXPECTED_FREEZE
assert pin(S / 'PROPOSED_LEMMAS.md')['sha256'] == EXPECTED_PROPOSAL
freeze = json.loads((S / 'FINAL_FREEZE.json').read_text())
assert len(freeze['members']) == 14
rows = []
for row in freeze['members']:
    relative = Path(row['path'])
    assert not relative.is_absolute() and '..' not in relative.parts
    source = S / relative
    actual = pin(source)
    assert actual['bytes'] == row['bytes'] and actual['sha256'] == row['sha256']
    rows.append(capture(source, Path('sources/preparation') / relative,
                        'Frozen author preparation source or historical evidence; not a new run'))
rows.append(capture(S / 'FINAL_FREEZE.json', 'sources/preparation/FINAL_FREEZE.json',
                    'Exact root proposal freeze; does not confer acceptance'))

runtime = N / 'local_conserving_control_candidate'
assert pin(runtime / 'DERIVATION.md')['sha256'] == 'c7f0e58c79b7e05f7fe79374a8bbe52a290c0371392a0b0ddcdb98d3dbb49e60'
assert pin(runtime / 'FREEZE.json')['sha256'] == '3128a438f020588eb8e8e945b1cbe9f4e6d64f5524831e19e530ff28a1e08c9b'
for name in ['DERIVATION.md', 'FREEZE.json']:
    rows.append(capture(runtime / name, Path('sources/conditional_runtime') / name,
                        'Conditional runtime interface only; remaining upstream members not recaptured or validated'))

receipt_path = S / 'actual_exact_run/EXECUTION.json'
receipt = json.loads(receipt_path.read_text())
assert receipt['exit_code'] == 0
assert len(receipt['argv']) == 2
assert receipt['argv'][1] == receipt['child_source_at_launch']['path']
assert receipt['child_source_at_launch']['path'] != receipt['source_capture']['path']
assert receipt['start_utc'] < receipt['end_utc']
assert receipt['elapsed_seconds'] > 0
for key, saved_name in [('child_source_at_launch', 'selected_exact_check.py'),
                        ('source_capture', 'actual_exact_run/executed_source.py'),
                        ('recorder', 'actual_exact_run/recorder_source.py'),
                        ('stdout', 'actual_exact_run/stdout'),
                        ('stderr', 'actual_exact_run/stderr')]:
    record = receipt[key]
    original = pin(Path(record['path']))
    saved = pin(S / saved_name)
    assert original == record
    assert saved['bytes'] == record['bytes'] and saved['sha256'] == record['sha256']
assert receipt['child_source_at_launch']['sha256'] == receipt['source_capture']['sha256']
ast.parse((S / 'selected_exact_check.py').read_text())
parsed_stdout = json.loads((S / 'actual_exact_run/stdout').read_text())
assert parsed_stdout['q'] == 1 and parsed_stdout['L'] == 3
assert parsed_stdout['physical_dimension'] == 32
assert (S / 'actual_exact_run/stderr').read_bytes() == b''
original_execution = N / 'runs/local_sine_preparation_exact_01/EXECUTION.json'
assert original_execution.read_bytes() == receipt_path.read_bytes()

rules = ['AGENTS.md', 'docs/ai_methodology/SCIENCE_WORKFLOW.md',
         'docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md',
         'docs/ai_methodology/skills/physics-claim-reviewer/SKILL.md',
         'docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md']
rule_receipts = []
for index, name in enumerate(rules):
    argv = ['git', 'show', MAIN + ':' + name]
    started = now()
    started_monotonic = time.monotonic()
    result = subprocess.run(argv, cwd=W, capture_output=True, check=False)
    duration = time.monotonic() - started_monotonic
    target = O / 'sources/current_rules' / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(result.stdout)
    stderr = O / 'sources/current_rules' / (str(index) + '.stderr')
    stderr.write_bytes(result.stderr)
    record = {'argv': argv, 'cwd': str(W), 'start_utc': started,
              'end_utc': now(), 'elapsed_seconds': duration,
              'exit_code': result.returncode, 'stdout': pin(target), 'stderr': pin(stderr),
              'scope': 'Read-only exact-commit instruction retrieval; no ref refresh or Git mutation'}
    rule_receipts.append(record)
    assert result.returncode == 0 and not result.stderr

write_json(O / 'SOURCE_CAPTURE.json', {
    'utc': now(), 'preparation_freeze': pin(S / 'FINAL_FREEZE.json'),
    'preparation_members_verified': 14, 'source_captures': rows,
    'historical_author_execution': pin(original_execution),
    'historical_receipt_linkage_verified': True,
    'new_scientific_executions': 0,
    'runtime_status': 'Conditional interface; separate root review remains outside this review',
    'current_rule_revision': MAIN,
    'freshness_basis': 'Root supplied actual 2026-10-16T14:41:58 fetch; this check performs no fetch',
    'rule_retrievals': rule_receipts,
    'editable_prompt_files_changed': []})
print(json.dumps({'scope': 'Metadata verification only', 'source_members_verified': 14,
                  'exact_source_captures': len(rows), 'read_only_rule_retrievals': len(rule_receipts),
                  'author_receipt_and_original_captures_match': True,
                  'author_source_parsed_not_executed': True, 'new_scientific_executions': 0}, indent=2))
