"""Scoped integration checks for the covariance review and charged author unit.

This validates artifact integrity and changed documentation, not scientific
truth, a full-repository pipeline, formal audit, or whole-PR approval.
"""
from pathlib import Path
import ast, hashlib, json, re, subprocess, tempfile

L = Path('.claude/science/toe-ruleset-20261021/agents/ym4d-proof')
C = L/'checks'
def sha(data): return hashlib.sha256(data).hexdigest()
bindings = json.loads((C/'full_proof_covariance_review_bindings.json').read_text())
paths = {r['path'] for r in bindings['artifacts']}
paths.update(str(p) for p in C.glob('full_proof_covariance_review_*'))
paths.update(str(p) for p in C.glob('full_proof_covariance_jet_*'))
paths.update(str(L/n) for n in ['HANDOFF.md', 'APPROACH_REGISTRY.md', 'SESSION25_RESULTS.md', 'PROOF.md'])
records = []
for row in bindings['artifacts']:
    assert sha(Path(row['path']).read_bytes()) == row['sha256'], row['path']
failed_syntax = {'review_soft_fluctuation_independent_01.py': '066a13078404b99a0835486f3b6ed10eccb103e7a4ba0a2d51e286303a8950f2'}
header_dir = Path(tempfile.mkdtemp(prefix='ym-covariance-jet-docs-'))
markdown = []
links = []
archived_syntax = []
empty_json = []
for name in sorted(paths):
    p = Path(name); data = p.read_bytes()
    records.append({'path': name, 'sha256': sha(data), 'bytes': len(data)})
    if p.suffix == '.py':
        if p.name in failed_syntax:
            assert sha(data) == failed_syntax[p.name]
            archived_syntax.append(name)
        else: ast.parse(data, filename=name)
    if p.suffix == '.json':
        if data: json.loads(data)
        else:
            assert p.name in ['review_soft_fluctuation_independent_01.stdout.json', 'review_soft_fluctuation_additional_01.stdout.json']
            empty_json.append(name)
    if p.suffix != '.md': continue
    s = data.decode(); context = p.parent
    if p.name == 'review_soft_fluctuation_original_source.md': context = L
    if p.name == 'PROOF.md':
        header, legacy = s.split('> **PROVENANCE WARNING', 1)
        assert sha(('> **PROVENANCE WARNING'+legacy).encode()) == '4efdee19aa03123a89053e466525f0ef5e9d8a4b8eb1ea38a1e87125043e728c'
        s = header; target = header_dir/'PROOF_header.md'; target.write_text(s); markdown.append(str(target))
    else: markdown.append(name)
    fenced = False
    for line in s.splitlines():
        if line.startswith('> '): line = line[2:]
        elif line == '>': line = ''
        if line.lstrip().startswith('```'):
            fenced = not fenced; continue
        if fenced or line.startswith('    '): continue
        for value in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)', line):
            target = value.split('#', 1)[0]
            if not target or re.match(r'^[a-zA-Z]+:', target): continue
            target = target.strip('<>')
            assert (context/target).exists(), (name, target)
            links.append({'source': name, 'target': str(context/target)})
vocab_path = header_dir/'vocab.json'
lint = subprocess.run(['python3', 'scripts/vocab_lint.py', '--report-only', '--report-path', str(vocab_path), *markdown], capture_output=True)
assert lint.returncode == 0, lint.stderr.decode()
vocab = json.loads(vocab_path.read_bytes())
whitespace = subprocess.run(['git', 'diff', '--check', 'HEAD', '--', *sorted(paths)], capture_output=True)
assert whitespace.returncode == 0, whitespace.stdout.decode()+whitespace.stderr.decode()
replay = json.loads((C/'full_proof_covariance_review_replay_summary.json').read_bytes())
assert replay['all_ok'] and len(replay['runs']) == 3
result = {'scope': __doc__, 'all_ok': True, 'files': records,
          'bound_artifact_records': len(bindings['artifacts']), 'local_links_checked': len(links),
          'archived_failed_syntax_preserved': archived_syntax, 'archived_empty_json_preserved': empty_json,
          'vocabulary_report': vocab, 'vocabulary_stdout': lint.stdout.decode(),
          'whitespace_exit_code': whitespace.returncode, 'legacy_PROOF_body_unchanged': True,
          'reviewer_programs_reproduced': 3, 'charged_independent_review': 'PENDING',
          'full_existence': 'OPEN', 'physical_continuum_mass_gap': 'OPEN'}
out = C/'full_proof_covariance_jet_integration_validation.json'
assert not out.exists(), str(out)
out.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'all_ok': True, 'files': len(records), 'bound_artifact_records': len(bindings['artifacts']),
                  'local_links_checked': len(links), 'vocabulary_report': vocab}))
