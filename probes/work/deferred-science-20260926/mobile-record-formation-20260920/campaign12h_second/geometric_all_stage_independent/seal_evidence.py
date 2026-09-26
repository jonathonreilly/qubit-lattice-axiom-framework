#!/usr/bin/env python3
"""Seal the completed bounded review; refuses to overwrite the final seal."""
from pathlib import Path
import datetime, hashlib, json
HERE = Path(__file__).resolve().parent
RAW = HERE.parent

def identity(p):
    b = p.read_bytes()
    return {'path': str(p), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

def read(p):
    return json.loads(p.read_text())

def main():
    assert not (HERE / 'FINAL_SEAL.json').exists()
    pre = read(HERE / 'PRE_COMPARISON_SEAL.json')
    for row in pre['artifacts']:
        assert identity(Path(row['path'])) == row
    before = read(HERE / 'PRE_COMPARISON_SOURCES.json')
    for field in ['sources', 'reused_independent_dependencies', 'procedures_reused_unchanged']:
        for row in before[field]:
            assert identity(Path(row['path'])) == row
    ext = before['external_import_reused_by_identity']
    assert identity(Path(ext['path'])) == ext
    expected_prior_reports = {
        'geometric_partner_independent': 'ea444723e0720ad9d7f17ba9e2b5cd836bab8cd3b799b7bbdb73776e92f58423',
        'geometric_general_graph_independent': '091636c4217f45ce2389569e1d6a7e4888a71ee4d5c9af8764b4c24004c57166',
        'geometric_last_pair_clock_independent': '233f0d3c23ad5f314fcbad698d201e0bde62a5a23b97cae7113eed060efd774f',
        'geometric_polynomial_relaxation_independent': '552484e9eaf353b5832eb579272d2ddd4c0fa5f2dde5a91c49cb172f7df0e369'}
    for folder, digest in expected_prior_reports.items():
        assert identity(RAW / folder / 'REPORT.md')['sha256'] == digest
    author = read(RAW / 'geometric_all_stage_checks/RESULTS.json')
    for name, digest in author['sources_sha256'].items():
        assert identity(RAW / name)['sha256'] == digest
    sources = before['sources'] + [identity(RAW / name) for name in [
        'geometric_all_stage_check.py', 'geometric_corridor_transport_check.py']]
    author_evidence = [identity(p) for p in sorted((RAW / 'geometric_all_stage_checks').iterdir()) if p.is_file()]
    author_evidence += [identity(RAW / name) for name in [
        'GEOMETRIC_ALL_STAGE_RUN.log', 'GEOMETRIC_ALL_STAGE_RUN.stderr',
        'geometric_corridor_transport_checks/RESULTS.json']]
    manifest = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                'sources': sources,
                'author_evidence_authenticated_after_preseal': author_evidence,
                'reused_independent_dependencies': before['reused_independent_dependencies'],
                'external_import_reused_by_identity': ext,
                'procedures_reused_unchanged': before['procedures_reused_unchanged'],
                'read_scope': 'Complete candidate note, author all-stage checker and imported corridor helper; all stored author JSON parsed and checked as described in REPORT.md. No primary suite rerun; no new literature theorem imported.',
                'unresolved_findings': []}
    (HERE / 'FINAL_SOURCES.json').write_text(json.dumps(manifest, indent=2) + '\n')
    artifacts = [identity(p) for p in sorted(HERE.rglob('*')) if p.is_file() and p.name != 'FINAL_SEAL.json']
    seal = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'scope': 'Completed bounded independent reconstruction and post-source comparison; no formal audit status.',
            'precomparison_seal': identity(HERE / 'PRE_COMPARISON_SEAL.json'),
            'report': identity(HERE / 'REPORT.md'),
            'sources_and_evidence_manifest': identity(HERE / 'FINAL_SOURCES.json'),
            'artifacts': artifacts,
            'failed_attempts_preserved': ['failed_attempt_01/FAILURE_RECEIPT.json'],
            'unresolved_findings': []}
    (HERE / 'FINAL_SEAL.json').write_text(json.dumps(seal, indent=2) + '\n')
    print(json.dumps({'report': identity(HERE / 'REPORT.md'),
                      'seal': identity(HERE / 'FINAL_SEAL.json'),
                      'artifact_count': len(artifacts), 'source_count': len(sources),
                      'author_evidence_count': len(author_evidence)}, indent=2))

if __name__ == '__main__':
    main()
