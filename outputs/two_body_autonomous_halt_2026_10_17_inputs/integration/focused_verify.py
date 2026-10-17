from pathlib import Path
import datetime
import hashlib
import json
import py_compile
import re
import shutil
import subprocess
import sys

N = Path(__file__).resolve().parents[1]
W = N.parent / 'correlation_worktree'
D = N / 'two_body_integration'
F = W / 'outputs/two_body_autonomous_halt_2026_10_17_inputs'
Q = W / '.claude/science/physics-loops/toe-two-body-autonomous-halt-20261017'
sys.path[:0] = [str(W / 'scripts'), str(W / 'docs/audit/scripts')]
import runner_cache
import build_citation_graph
import forensic_evidence_readiness
import no_go_discipline_gate

def digest(path):
    b = path.read_bytes()
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

def write_json(path, obj):
    path.write_text(json.dumps(obj, indent=2) + '\n')

def outside_code(text):
    lines = []
    fence = None
    for line in text.splitlines():
        found = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line)
        if fence:
            if found and found[1][0] == fence[0] and len(found[1]) >= len(fence) and not found[2].strip():
                fence = None
            continue
        if found:
            fence = found[1]
            continue
        lines.append(line)
    assert fence is None, 'unclosed fenced source transcript'
    return re.sub(r'(`+).*?\1', '', '\n'.join(lines))

primary = 'scripts/two_body_autonomous_halt_2026_10_17.py'
note = 'docs/TWO_BODY_AUTONOMOUS_HALT_BOUNDED_THEOREM_NOTE_2026-10-17.md'
helper = 'scripts/two_body_autonomous_halt_check_2026_10_17.py'
claim = 'two_body_autonomous_halt_bounded_theorem_note_2026-10-17'

# Archive actual graph evidence and this checker before verifying the manifest.
for name in ['graph_check.py', 'GRAPH_VERIFICATION.json', 'graph_build.stdout',
             'graph_build.stderr', 'graph_manifest.stdout', 'graph_manifest.stderr',
             'focused_verify.py']:
    shutil.copyfile(D / name, F / 'integration' / name)
manifest_path = F / 'ARTIFACT_MANIFEST.json'
manifest = json.loads(manifest_path.read_text())
for p in sorted((F / 'integration').iterdir()):
    if p.is_file():
        manifest['files'][str(p.relative_to(F))] = digest(p)
write_json(manifest_path, manifest)
for rel, pin in manifest['files'].items():
    p = F / rel
    assert p.is_file() and not p.is_symlink(), rel
    assert digest(p) == pin, rel
actual = {str(p.relative_to(F)) for p in F.rglob('*') if p.is_file()}
assert actual == set(manifest['files']) | {'ARTIFACT_MANIFEST.json'}, actual ^ set(manifest['files'])

source = json.loads((Q / 'SOURCE_MANIFEST.json').read_text())
nb = (W / note).read_bytes()
assert digest(W / note) == {k: source['note'][k] for k in ('bytes', 'sha256')}
assert len(source['unchanged_bodies']) == 4
for body in source['unchanged_bodies']:
    raw = (W / body['source']).read_bytes()
    assert nb[body['body_byte_start_inclusive']:body['body_byte_end_exclusive']] == raw
    assert len(raw) == body['bytes'] and hashlib.sha256(raw).hexdigest() == body['sha256']
result = json.loads((W / 'outputs/two_body_autonomous_halt_2026_10_17.json').read_text())
assert len(result['input_sha256']) == 45
for rel, h in result['input_sha256'].items():
    assert digest(W / rel)['sha256'] == h, rel
declared = runner_cache.declared_input_paths(W / primary)
assert set(declared) == set(result['input_sha256']), (declared, result['input_sha256'])
helpers = build_citation_graph.resolve_helper_runner_paths(primary)
assert helpers == [helper], helpers
row = {'claim_id': claim, 'note_path': note, 'runner_path': primary,
       'helper_runner_paths': helpers, 'claim_type': 'bounded_theorem'}
issue = forensic_evidence_readiness.cached_row_readiness_issue(row, {claim: row}, W)
assert issue is None, issue
cache = runner_cache.cache_status(primary)
assert cache == 'fresh', cache
for rel in [primary, helper]:
    py_compile.compile(str(W / rel), cfile=str(D / (Path(rel).name + '.pyc')), doraise=True)

mut = json.loads((F / 'mutations/RESULTS.json').read_text())
assert len(mut['cases']) == 7
for case in mut['cases']:
    assert case['exit_code'] == 1 and case['scientific_assertion_rejected'], case['name']
    case_dir = F / 'mutations' / case['name']
    for stream in ['stdout', 'stderr']:
        assert digest(case_dir / stream) == case[stream], (case['name'], stream)
    assert digest(case_dir / 'mutated.py') == case['source']
    stderr = (case_dir / 'stderr').read_text()
    assert case['expected_scientific_assertion'] in stderr and 'AssertionError' in stderr

graph = json.loads((D / 'GRAPH_VERIFICATION.json').read_text())
assert graph['added'] == [claim] and not graph['removed'] and not graph['rewired']
assert graph['new_node']['note_hash'] == hashlib.sha256(nb).hexdigest()
assert graph['manifest_sha256'] == digest(W / 'docs/audit/data/citation_graph_manifest.json')['sha256']
no_go = no_go_discipline_gate.source_requires_no_go_discipline(note, nb.decode(), 'bounded_theorem')
assert not no_go, no_go
diff = subprocess.run(['git', 'diff', '--check'], cwd=W, capture_output=True, text=True)
assert diff.returncode == 0, diff.stdout + diff.stderr

# Check every new live Markdown link, allowing only this not-yet-written record.
links = []
for p in [W / note, *sorted(Q.glob('*.md'))]:
    for target in re.findall(r'\[[^\]\n]+\]\(([^)\s]+)\)', outside_code(p.read_text())):
        if target.startswith(('http:', 'https:', '#')):
            continue
        raw_dest = p.parent / target.split('#')[0]
        assert not raw_dest.is_symlink(), (p, target)
        dest = raw_dest.resolve()
        assert dest.is_file() or dest == Q / 'PUBLISH_CHECKS.json', (p, target)
        links.append({'source': str(p.relative_to(W)), 'target': str(dest.relative_to(W))})
record = {
    'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'scope': 'Focused deterministic publication checks and actual finite execution only. No independent retained audit, large-clock evolution, shared combined-main landing gate or new scientific conclusion is asserted by this checker.',
    'artifact_hashes_verified': len(manifest['files']),
    'artifact_manifest': digest(manifest_path),
    'unchanged_mathematical_bodies': len(source['unchanged_bodies']),
    'source_manifest': digest(Q / 'SOURCE_MANIFEST.json'),
    'canonical_result_input_hashes': result['input_sha256'],
    'declared_input_count': len(declared),
    'helper_discovery': helpers,
    'deterministic_readiness_issue': issue,
    'cache_status': cache,
    'canonical_execution': json.loads((Q / 'CANONICAL_EXECUTION.json').read_text()),
    'mutation_cases_and_archived_streams': len(mut['cases']),
    'no_go_gate_trigger': no_go,
    'compiled_sources': [primary, helper],
    'relative_regular_file_links': links,
    'graph': graph,
    'tracked_diff_whitespace_exit_code': diff.returncode,
    'publication': 'pending; regular PR URL and exact head recorded separately after creation',
    'shared_landing_gates': 'not run; combined-current-main pipeline, strict lint, changed-evidence checks and independent retained audit remain separate',
}
write_json(Q / 'PUBLISH_CHECKS.json', record)
# Resolve the self-reference only after the completed actual record exists.
assert (Q / 'PUBLISH_CHECKS.json').is_file() and not (Q / 'PUBLISH_CHECKS.json').is_symlink()
for link in links:
    assert (W / link['target']).is_file()
write_json(D / 'FOCUSED_VERIFICATION.json', record)
print(json.dumps({k: record[k] for k in ['utc', 'artifact_hashes_verified',
    'unchanged_mathematical_bodies', 'declared_input_count', 'helper_discovery',
    'deterministic_readiness_issue', 'cache_status', 'mutation_cases_and_archived_streams',
    'no_go_gate_trigger', 'tracked_diff_whitespace_exit_code']}, indent=2))
