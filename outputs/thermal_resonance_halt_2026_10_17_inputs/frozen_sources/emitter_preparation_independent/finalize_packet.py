"""Freeze this author packet; bookkeeping only, never execute scientific code."""
from pathlib import Path
from datetime import datetime, timezone
import ast
import hashlib
import json
import os
import re
import subprocess

D = Path(__file__).resolve().parent
W = Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree')
def digest(path):
    raw = path.read_bytes()
    return {'path': str(path.relative_to(D)), 'bytes': len(raw),
            'sha256': hashlib.sha256(raw).hexdigest()}
def save(name, data):
    with (D/name).open('x') as f:
        f.write(json.dumps(data, indent=2) + '\n')
        f.flush()
        os.fsync(f.fileno())

assert not (D/'FREEZE.json').exists()
manifest = json.loads((D/'SOURCE_MAP.json').read_text())
source_checks = []
for row in manifest['sources']:
    local = D/row['snapshot']
    pinned = hashlib.sha256(local.read_bytes()).hexdigest()
    assert pinned == row['sha256']
    current = hashlib.sha256((W/row['repository_path']).read_bytes()).hexdigest()
    source_checks.append({'snapshot': row['snapshot'],
                          'expected_sha256': row['sha256'],
                          'frozen_copy_matches': True,
                          'current_worktree_matches': current == pinned,
                          'current_worktree_sha256': current})
family = (D/'inputs/family.md').read_bytes()
begin = b'<!-- BEGIN UNCHANGED FAMILY AUTHOR BODY -->\n'
end = b'<!-- END UNCHANGED FAMILY AUTHOR BODY -->'
body = family.split(begin, 1)[1].split(end, 1)[0]
# The canonical note surrounds the unchanged source body with wrapper newlines.
body_matches = []
expected = manifest['inherited_family_body_sha256']
for head in range(3):
    for tail in range(3):
        candidate = body[head:len(body)-tail if tail else len(body)]
        if hashlib.sha256(candidate).hexdigest() == expected:
            body_matches.append({'leading_wrapper_bytes': head,
                                 'trailing_wrapper_bytes': tail,
                                 'bytes': len(candidate)})
assert len(body_matches) == 1, body_matches

pre = json.loads((D/'attempt_01/PRELAUNCH.json').read_text())
receipt = json.loads((D/'attempt_01/RECEIPT.json').read_text())
report = json.loads((D/'attempt_01/stdout.json').read_text())
bound_checks = []
for row in pre['bindings']:
    p = Path(row['path'])
    st = p.stat()
    sha = hashlib.sha256(p.read_bytes()).hexdigest()
    generation = {'device': st.st_dev, 'inode': st.st_ino,
                  'mtime_ns': st.st_mtime_ns, 'ctime_ns': st.st_ctime_ns}
    assert sha == row['sha256']
    assert generation == row['generation']
    bound_checks.append({'path': row['path'], 'sha256_matches': True,
                         'generation_matches': True})
for key in ['prelaunch', 'stdout', 'stderr']:
    row = receipt[key]
    assert hashlib.sha256(Path(row['path']).read_bytes()).hexdigest() == row['sha256']
assert receipt['exit_code'] == 0 and not receipt['timed_out']
assert receipt['all_bound_bytes_and_generations_unchanged']
assert len(report['checks']) == 122
assert len(list(D.glob('attempt_*'))) == 1
assert (D/'check_preparation.py').read_bytes() == (D/'attempt_01/check_preparation.py').read_bytes()

patterns = [
    r'emitter.{0,80}(gibbs|thermal|prepar|release)|gibbs.{0,80}(emitter|handoff)|length.independent.{0,80}(release|seed)',
    r'ready.range|Gamma|release|removal|counterterm'
]
notes = ['inputs/family.md', 'inputs/product_seed.md', 'inputs/two_body.md',
         'inputs/local_gibbs.md', 'inputs/controlled_stop.md', 'inputs/local_bias.md']
searches = []
for pattern, paths in [(patterns[0], notes), (patterns[1], ['inputs/local_bias.md'])]:
    argv = ['rg', '-n', '-i', pattern] + paths
    result = subprocess.run(argv, cwd=D, capture_output=True, text=True)
    assert result.returncode in (0, 1)
    searches.append({'argv': argv, 'exit_code': result.returncode,
                     'stdout': result.stdout, 'stderr': result.stderr})
save('PRIOR_SEARCH.json', {'captured_utc': datetime.now(timezone.utc).isoformat(),
                          'scope': 'Narrow local text search over frozen sources; not a scientific run or exhaustive literature review',
                          'searches': searches})

python_files = sorted(D.glob('*.py')) + [D/'attempt_01/check_preparation.py']
for p in python_files:
    ast.parse(p.read_text(), filename=str(p))
note = (D/'CANDIDATE.md').read_text()
links = re.findall(r'\]\(([^)]+)\)', note)
for link in links:
    assert (D/link).exists(), link
assert '\\chi_{\\rm p}t_{\\rm h}+c_{\\rm seed}\\tau+(u+2\\kappa)\\tau/2\n +c_{\\rm phys}t.' in note

save('STATIC_AND_EVIDENCE_CHECK.json', {
    'checked_utc': datetime.now(timezone.utc).isoformat(),
    'kind': 'Bookkeeping and source freshness; no scientific replay',
    'source_checks': source_checks,
    'all_current_worktree_sources_match': all(r['current_worktree_matches'] for r in source_checks),
    'family_body_sha256': expected, 'body_wrapper_offsets': body_matches,
    'prelaunch_binding_count': len(bound_checks),
    'bound_checks': bound_checks,
    'actual_scientific_attempts': 1, 'scientific_failures': 0,
    'scientific_status': report['status'],
    'named_scientific_check_records': len(report['checks']),
    'receipt_exit_code': receipt['exit_code'],
    'wall_seconds': receipt['wall_seconds'],
    'limits': receipt['caps'],
    'python_ast_parse_paths': [str(p.relative_to(D)) for p in python_files],
    'candidate_lines': len(note.splitlines()),
    'candidate_local_links_resolve': links,
    'changed_editable_prompt_files': [],
    'limitations': 'No independent theorem validation, thermalization, controller realization, scientific runner replay or large-device simulation in this finalization.'})
files = [digest(p) for p in sorted(D.rglob('*')) if p.is_file()
         and p.name not in {'FILE_MANIFEST.json', 'FREEZE.json'}]
save('FILE_MANIFEST.json', {'created_utc': datetime.now(timezone.utc).isoformat(),
                           'status': 'Author conditional candidate; separate review required',
                           'members': files})
save('FREEZE.json', {
    'frozen_utc': datetime.now(timezone.utc).isoformat(),
    'status': 'Frozen conditional author candidate, not root qualified or independently checked',
    'source_commit': manifest['source_commit'],
    'candidate': digest(D/'CANDIDATE.md'),
    'source_map': digest(D/'SOURCE_MAP.json'),
    'file_manifest': digest(D/'FILE_MANIFEST.json'),
    'scientific_output': digest(D/'attempt_01/stdout.json'),
    'scientific_receipt': digest(D/'attempt_01/RECEIPT.json'),
    'static_receipt': digest(D/'STATIC_AND_EVIDENCE_CHECK.json'),
    'member_count_excluding_manifest_and_freeze': len(files),
    'root_competing_mechanism_exposure': 'Not viewed before freeze',
    'new_claim': 'Positive full-space preparation controls, thermal marginal to complete finite emitter output, exact seed release bound kappa*tau/sqrt(2)',
    'remaining_decision': 'Separate analytical check before downstream acceptance',
    'write_boundary': str(D)})
print(json.dumps({'freeze': digest(D/'FREEZE.json'),
                  'candidate': digest(D/'CANDIDATE.md'),
                  'manifest': digest(D/'FILE_MANIFEST.json'),
                  'members': len(files),
                  'prelaunch_bindings': len(bound_checks),
                  'all_sources_current': all(r['current_worktree_matches'] for r in source_checks)}, indent=2))
