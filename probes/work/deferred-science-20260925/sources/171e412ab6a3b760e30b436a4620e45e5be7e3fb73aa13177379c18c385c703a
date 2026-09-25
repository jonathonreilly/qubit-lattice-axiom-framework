"""Seal generation02 correspondence without replacing earlier evidence."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def verify(path, row):
    assert path.stat().st_size == row['bytes'] and sha(path) == row['sha256'], str(path)


def main():
    target = HERE / 'PUBLICATION_REVISION_SEAL.json'
    assert not target.exists(), 'Never replace an earlier seal.'
    check = load(HERE / 'PUBLICATION_REVISION_CHECK_STDOUT.json')
    execution = load(HERE / 'PUBLICATION_REVISION_CHECK_EXECUTION.json')
    pins = load(HERE / 'PUBLICATION_REVISION_SOURCE_PINS.json')
    assert execution['exit_code'] == 0
    assert sha(HERE / 'publication_revision_check.py') == execution['source_sha256'] == check['source_sha256']
    assert sha(HERE / 'PUBLICATION_REVISION_CHECK_STDOUT.json') == execution['stdout_sha256']
    assert sha(HERE / 'PUBLICATION_REVISION_CHECK_STDERR.txt') == execution['stderr_sha256']
    assert (HERE / 'PUBLICATION_REVISION_CHECK_STDERR.txt').stat().st_size == 0
    assert sha(HERE / 'PUBLICATION_REVISION_SOURCE_PINS.json') == check['source_pins_sha256']
    assert len(pins['origins']) == check['current_origins_verified'] == 14
    for row in pins['origins']:
        verify(HERE / row['frozen'], row)
        verify(Path(row['origin']), row)
    for name, row in check['preserved_seals'].items():
        assert sha(HERE / name) == row['sha256']
        prior = load(HERE / name)
        assert prior['member_count'] == len(prior['members']) == row['members']
        for member in prior['members']:
            verify(HERE / member['path'], member)
    assert check['science_canonical_citations_and_final_physical_obligations_byte_unchanged']
    assert check['full_actual_diff_equals_supplied_diff'] and check['full_result_execution_stdout_cache_exact']
    assert check['full_scientific_payload_leaf_counts'] == {'str': 464, 'int': 232, 'bool': 8, 'float': 410}
    assert len(check['only_excluded_payload_fields']) == 2
    assert check['scientific_differences'] == check['check_failures'] == []
    assert check['programs_or_cache_helpers_imported_or_executed'] == check['other_active_packets_opened'] == []
    names = [
        'PRE.md', 'PRE_SEAL.json', 'SOURCE_PINS.json',
        'POST.md', 'POST_SEAL.json', 'POST_SOURCE_PINS.json',
        'PUBLICATION_COMPARISON.md', 'PUBLICATION_COMPARISON_SEAL.json', 'PUBLICATION_SOURCE_PINS.json',
        'PUBLICATION_REVISION.md', 'PUBLICATION_REVISION_SOURCE_PINS.json',
        'publication_revision_check.py', 'seal_publication_revision.py',
        'PUBLICATION_REVISION_CHECK_EXECUTION.json', 'PUBLICATION_REVISION_CHECK_STDOUT.json',
        'PUBLICATION_REVISION_CHECK_STDERR.txt'
    ] + [row['frozen'] for row in pins['origins']]
    assert len(names) == len(set(names)) == 30
    members = [{'path': name, 'sha256': sha(HERE / name), 'bytes': (HERE / name).stat().st_size}
               for name in sorted(names)]
    seal = {
        'sealed_utc': datetime.now(timezone.utc).isoformat(),
        'signed_by': 'Codex scoped independent checker /root/rotor_upper_tail_check',
        'scope': 'Narrow generation02 final publication correspondence: provenance paragraph revision and complete fresh source/payload/cache binding. No scientific rerun, fresh independence claim or retained audit.',
        'report': 'PUBLICATION_REVISION.md',
        'preserved_seals': check['preserved_seals'],
        'generation01_commit': check['generation01_commit'],
        'generation01_recovery_scope': 'Nine pinned publication files verified from exact Git bytes; six artifact copies and four earlier external metadata records verified in history. Not a full 65-file package audit.',
        'generation02_note_sha256': check['new_note_sha256'],
        'generation02_manifest_sha256': check['new_manifest_sha256'],
        'generation02_result_sha256': check['new_result_sha256'],
        'generation02_cache_sha256': check['new_cache_sha256'],
        'recomputed_input_fingerprint_sha256': check['new_input_fingerprint_sha256'],
        'current_origin_count': 14,
        'scientific_payload_leaf_counts': check['full_scientific_payload_leaf_counts'],
        'excluded_payload_timers': check['only_excluded_payload_fields'],
        'science_and_canonical_citations_unchanged': True,
        'additional_repair_identified': False,
        'mechanical_failure_preserved': 'Historical markdown provenance links were rejected by the focused docs-only resolver, as recorded by root. Directory-link repair and named-file existence checked; gate not rerun by this checker.',
        'earlier_frozen_sources_overwritten': False,
        'author_primary_or_cache_programs_executed': [],
        'other_active_scientific_packets_opened': [],
        'own_read_only_check': 'PUBLICATION_REVISION_CHECK_EXECUTION.json',
        'member_count': len(members), 'members': members,
        'next_step': 'Stop after delivery; full package/allowlist and mechanical-gate verification remain root work.'
    }
    with target.open('x') as stream:
        json.dump(seal, stream, indent=2)
        stream.write('\n')
    for member in members:
        (HERE / member['path']).chmod(0o444)
    target.chmod(0o444)
    for member in load(target)['members']:
        verify(HERE / member['path'], member)
    for name in check['preserved_seals']:
        for member in load(HERE / name)['members']:
            verify(HERE / member['path'], member)
    print(json.dumps({
        'status': 'Revision sealed; 30 members and all earlier PRE/POST/final members verified unchanged',
        'PUBLICATION_REVISION_sha256': sha(HERE / 'PUBLICATION_REVISION.md'),
        'PUBLICATION_REVISION_SEAL_sha256': sha(target),
        'PUBLICATION_REVISION_SOURCE_PINS_sha256': sha(HERE / 'PUBLICATION_REVISION_SOURCE_PINS.json'),
        'read_only_checker_sha256': sha(HERE / 'publication_revision_check.py'),
        'read_only_check_output_sha256': sha(HERE / 'PUBLICATION_REVISION_CHECK_STDOUT.json'),
        'member_count': 30, 'current_origins_verified': 14,
        'new_input_fingerprint_sha256': check['new_input_fingerprint_sha256'],
        'additional_repair_identified': False
    }, indent=2))


if __name__ == '__main__':
    main()
