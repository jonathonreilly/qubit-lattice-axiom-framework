"""Verify the selected formation-capacity publication unit in this checkout."""

from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / 'PUBLICATION_UNIT_FORMATION_CAPACITY.json'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

data = json.loads(MANIFEST.read_text())
assert data['base_commit'] == 'a78c6b8c002051a1ae4d47d94eeac94e562cff3d'
assert data['claim_status'] == 'provisional review proposal; no audit verdict'
assert data['independent_capacity_final_narrative'] == 'absent after checker usage interruption'
declared = set()
for row in data['artifacts']:
    relative = Path(row['path'])
    assert not relative.is_absolute() and '..' not in relative.parts
    assert str(relative) not in declared
    declared.add(str(relative))
    p = HERE / relative
    assert p.is_file() and not p.is_symlink(), p
    assert p.stat().st_size == row['bytes'], p
    assert digest(p) == row['sha256'], p

folders = ('formation_capacity_author','formation_capacity_independent',
           'formation_capacity_review','terminal_path_author')
expected = set()
for folder in folders:
    expected.update(str(p.relative_to(HERE)) for p in (HERE/folder).rglob('*') if p.is_file())
expected.add('FORMATION_CAPACITY_PUBLICATION_README.md')
expected.add('verify_formation_capacity_publication.py')
assert declared == expected, {'missing': sorted(expected-declared),
                              'unexpected': sorted(declared-expected)}

assert data['artifacts_count'] == len(declared)
print(json.dumps({'verified_artifacts':len(declared),
                  'base_commit':data['base_commit'],
                  'checker_final_narrative':data['independent_capacity_final_narrative'],
                  'claim_status':data['claim_status']},indent=2))
