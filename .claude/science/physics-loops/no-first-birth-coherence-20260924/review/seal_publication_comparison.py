#!/usr/bin/env python3
"""Verify this comparison's immutable dependencies, then seal only new files."""
import datetime
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(path, row):
    assert path.is_file() and not path.is_symlink(), str(path)
    assert sha(path) == row['sha256'], str(path)
    if 'bytes' in row:
        assert path.stat().st_size == row['bytes'], str(path)


def write_new(name, value):
    with (ROOT/name).open('x') as stream:
        stream.write(json.dumps(value, indent=2)+'\n')


def main():
    pins = json.loads((ROOT/'PUBLICATION_COMPARISON_SOURCE_PINS.json').read_text())
    protected = set()
    dependency_counts = []
    for dependency in pins['preserved_packet_dependencies']:
        seal_path = ROOT/dependency['seal']
        verify(seal_path, dependency)
        assert seal_path.stat().st_mode & 0o222 == 0
        old = json.loads(seal_path.read_text())
        assert len(old['members']) == dependency['unchanged_members'] == 23
        protected.add(dependency['seal'])
        for member in old['members']:
            path = ROOT/member['path']
            verify(path, member)
            assert path.stat().st_mode & 0o222 == 0
            protected.add(member['path'])
        dependency_counts.append(dependency)

    for row in pins['publication_sources'] + [pins['procedural_cache_API_source']] + pins['actual_declared_inputs']:
        verify(Path(row['source']), row)
        verify(ROOT/row['snapshot'], row)
    for row in pins['previously_reviewed_source_evidence'] + pins['new_comparison_evidence']:
        verify(ROOT/row['path'], row)
    execution = json.loads((ROOT/'PUBLICATION_CHECK_EXECUTION.json').read_text())
    assert execution['returncode'] == 0
    for name, row in execution['files'].items():
        verify(ROOT/name, row)
    assert (ROOT/'PUBLICATION_CHECK.stdout.txt').read_bytes() == (ROOT/'PUBLICATION_EVIDENCE_CHECK.json').read_bytes()
    assert (ROOT/'PUBLICATION_CHECK.stderr.txt').stat().st_size == 0

    verification = {
        'verified_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'scope': 'Final byte-identity and prior-packet preservation verification; no scientific computation',
        'verification_script_sha256': sha(Path(__file__)),
        'preserved_packets': dependency_counts,
        'dispatched_publication_and_external_sources_unchanged': 6,
        'procedural_cache_API_source_unchanged': True,
        'actual_declared_inputs_unchanged': 5,
        'comparison_execution_and_output_hashes_verified': True,
        'publication_comparison_report_sha256': sha(ROOT/'PUBLICATION_COMPARISON.md'),
        'primary_runner_repeated': False,
        'audit_verdict_applied': False,
    }
    write_new('PUBLICATION_COMPARISON_FINAL_VERIFICATION.json', verification)

    members = [r['snapshot'] for r in pins['publication_sources']]
    members += [pins['procedural_cache_API_source']['snapshot']]
    members += [r['path'] for r in pins['new_comparison_evidence']]
    members += ['PUBLICATION_COMPARISON_SOURCE_PINS.json',
                'seal_publication_comparison.py',
                'PUBLICATION_COMPARISON_FINAL_VERIFICATION.json']
    assert len(members) == len(set(members)) == 19
    assert not set(members) & protected
    rows = []
    for name in sorted(members):
        path = ROOT/name
        assert path.is_file() and not path.is_symlink()
        rows.append({'path': name, 'sha256': sha(path), 'bytes': path.stat().st_size})
        path.chmod(0o444)
    seal = {
        'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'scope': 'Frozen no-first-birth publication correspondence only; no audit verdict or independent primary numerical reproduction',
        'dependencies': dependency_counts,
        'members': rows,
        'immutable_policy': 'All member files and this seal are read-only; preserve rather than update this packet.',
    }
    write_new('PUBLICATION_COMPARISON_SEAL.json', seal)
    (ROOT/'PUBLICATION_COMPARISON_SEAL.json').chmod(0o444)
    for row in rows:
        verify(ROOT/row['path'], row)
        assert (ROOT/row['path']).stat().st_mode & 0o222 == 0
    print(json.dumps({
        'report': str(ROOT/'PUBLICATION_COMPARISON.md'),
        'report_sha256': sha(ROOT/'PUBLICATION_COMPARISON.md'),
        'seal': str(ROOT/'PUBLICATION_COMPARISON_SEAL.json'),
        'seal_sha256': sha(ROOT/'PUBLICATION_COMPARISON_SEAL.json'),
        'members': len(rows),
        'preserved_PRE_members': 23,
        'preserved_POST_members': 23,
    }, indent=2))


if __name__ == '__main__':
    main()
