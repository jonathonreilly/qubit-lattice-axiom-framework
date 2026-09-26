#!/usr/bin/env python3
"""Source/evidence seal for the completed bounded quantum-lift review."""
from pathlib import Path
import datetime, hashlib, json
HERE = Path(__file__).resolve().parent
RAW = HERE.parent

def identity(p):
    b = p.read_bytes()
    return {'path': str(p), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

def main():
    assert not (HERE / 'FINAL_SEAL.json').exists()
    pre = json.loads((HERE / 'PRE_COMPARISON_SEAL.json').read_text())
    for row in pre['artifacts']:
        assert identity(Path(row['path'])) == row
    assert identity(RAW / 'GEOMETRIC_QUANTUM_LIFT_BOUNDARY.md') == pre['sources']['source_read_completely']
    for row in pre['sources']['procedures_reused_unchanged']:
        assert identity(Path(row['path'])) == row
    result = json.loads((RAW / 'geometric_quantum_lift_checks/RESULTS.json').read_text())
    sources = [identity(RAW / 'GEOMETRIC_QUANTUM_LIFT_BOUNDARY.md')]
    for name, digest in result['sources_sha256'].items():
        row = identity(RAW / name)
        assert row['sha256'] == digest
        sources.append(row)
    evidence = [identity(RAW / name) for name in [
        'geometric_quantum_lift_checks/RESULTS.json', 'GEOMETRIC_QUANTUM_LIFT_RUN.log',
        'GEOMETRIC_QUANTUM_LIFT_RUN.stderr']]
    manifest = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                'sources': sources, 'author_evidence': evidence,
                'procedures_reused_unchanged': pre['sources']['procedures_reused_unchanged'],
                'external_mathematical_imports': [],
                'literature_boundary': 'The two note citations and external receipt were not inspected; contextual literature claims were not verified or used.',
                'unresolved_findings': [], 'failed_attempts': []}
    (HERE / 'FINAL_SOURCES.json').write_text(json.dumps(manifest, indent=2) + '\n')
    artifacts = [identity(p) for p in sorted(HERE.rglob('*')) if p.is_file() and p.name != 'FINAL_SEAL.json']
    seal = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'scope': 'Completed bounded independent reconstruction followed by source comparison. No formal audit status.',
            'precomparison_seal': identity(HERE / 'PRE_COMPARISON_SEAL.json'),
            'report': identity(HERE / 'REPORT.md'),
            'source_manifest': identity(HERE / 'FINAL_SOURCES.json'),
            'artifacts': artifacts, 'unresolved_findings': [], 'failed_attempts': []}
    (HERE / 'FINAL_SEAL.json').write_text(json.dumps(seal, indent=2) + '\n')
    print(json.dumps({'report': identity(HERE / 'REPORT.md'),
                      'seal': identity(HERE / 'FINAL_SEAL.json'),
                      'artifact_count': len(artifacts), 'source_count': len(sources),
                      'author_evidence_count': len(evidence)}, indent=2))

if __name__ == '__main__':
    main()
