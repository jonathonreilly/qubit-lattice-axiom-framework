"""Seal the bounded released-source POST without changing the blind PRE."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def check_file(path, expected):
    assert path.is_file(), str(path)
    assert sha(path) == expected['sha256'], str(path)
    assert path.stat().st_size == expected['bytes'], str(path)


def main():
    destination = HERE / 'POST_SEAL.json'
    assert not destination.exists(), 'Never replace a sealed POST.'
    assert sha(HERE / 'PRE.md') == '59be01a8d017fb3d1c08887723f91b25af203e318192749185791617f31de743'
    assert sha(HERE / 'PRE_SEAL.json') == '75bdc5d36dad74adf96285cefb0896539466f4e14c179cecc30f9afe5dbbf4ca'
    previous = read(HERE / 'PRE_SEAL.json')
    assert len(previous['members']) == previous['member_count'] == 25
    for member in previous['members']:
        check_file(HERE / member['path'], member)

    pins = read(HERE / 'POST_SOURCE_PINS.json')
    assert len(pins['sources']) == 10
    for source in pins['sources']:
        check_file(HERE / source['frozen'], source)
        check_file(Path(source['origin']), source)
    author_seal = read(HERE / 'post_frozen_author' / 'AUTHOR_SEAL.json')
    assert len(author_seal['files']) == 8
    for name, expected in author_seal['files'].items():
        check_file(HERE / 'post_frozen_author' / name, expected)

    execution = read(HERE / 'POST_BINDING_EXECUTION.json')
    evidence = read(HERE / 'POST_BINDING_STDOUT.json')
    assert execution['exit_code'] == 0
    assert sha(HERE / 'post_bind_and_check.py') == execution['source_sha256'] == evidence['checker_sha256']
    assert sha(HERE / 'POST_BINDING_STDOUT.json') == execution['stdout_sha256']
    assert sha(HERE / 'POST_BINDING_STDERR.txt') == execution['stderr_sha256']
    assert (HERE / 'POST_BINDING_STDERR.txt').stat().st_size == 0
    assert evidence['PRE_members_unchanged'] == 25
    assert evidence['released_source_origins_verified'] == 10
    assert evidence['author_members_verified'] == 8
    assert len(evidence['parent_bindings']) == 3
    assert evidence['row_counts'] == {'spectrum': 10, 'first_event': 15,
                                      'characteristic': 20, 'soft_and_interval': 5}
    assert evidence['author_programs_imported_or_executed'] == []
    assert evidence['other_active_packets_opened'] == []
    assert evidence['independent_numerical_replication'] is False
    assert evidence['failures'] == []

    names = ['PRE.md', 'PRE_SEAL.json', 'SOURCE_PINS.json', 'POST.md',
             'POST_SOURCE_PINS.json', 'post_bind_and_check.py',
             'POST_BINDING_EXECUTION.json', 'POST_BINDING_STDOUT.json',
             'POST_BINDING_STDERR.txt', 'seal_post.py']
    names += [source['frozen'] for source in pins['sources']]
    assert len(set(names)) == len(names) == 20
    members = [{'path': name, 'bytes': (HERE / name).stat().st_size,
                'sha256': sha(HERE / name)} for name in sorted(names)]
    seal = {
        'sealed_utc': datetime.now(timezone.utc).isoformat(),
        'signed_by': 'Codex independent checker /root/rotor_upper_tail_check',
        'scope': 'Released-source POST34: full argument and recorded generic four-state control compared with frozen independent PRE; exact correction and bounded source/output arithmetic, not a primary numerical rerun or audit verdict.',
        'report': 'POST.md',
        'preserved_PRE_sha256': sha(HERE / 'PRE.md'),
        'preserved_PRE_seal_sha256': sha(HERE / 'PRE_SEAL.json'),
        'preserved_PRE_members_verified': 25,
        'released_source_origin_count': 10,
        'exact_scientific_parent_origins_checked_in_binding_record': 3,
        'author_seal_sha256': pins['author_seal_sha256'],
        'author_members_verified': 8,
        'post_disclosure_correction': {
            'path': 'post_frozen_author/FINITE_WINDOW_ENERGY_MAGNETIC_SUM_CORRECTION.md',
            'sha256': 'cd145383f395171e33c34666744c326c92729018117e00e30bfd5a8a250ada51',
            'scope': 'Restore distance(a,c)=2 in the general-graph H4 pair sum; author generation unchanged.'
        },
        'wording_recommendation': 'Use fixed bounded continuous energy-response function; pointwise finite continuous functions need not have convergent means.',
        'own_evidence': 'Stored-output decimal arithmetic and exact source/log hashes only; direct author eigensystems and matrix exponentials are not independently rerun.',
        'author_programs_imported_or_executed': [],
        'other_active_packets_opened': [],
        'provenance_distinctions': [
            'Generic four-state bounded-compensation example belongs to the sealed root packet.',
            'Disconnected physical twelve-dimensional example and stopped-instrument proof are independent PRE additions.'
        ],
        'limitations': [
            'Fixed graph and parameters; positive limiting probability for conditional finite-bin events.',
            'Weak energy-law convergence and fixed bounded continuous responses; no moment or spectral-edge upgrade.',
            'Ordered small-window limit or an existence diagonal, not arbitrary simultaneous schedules or isolated microscopic timestamps.',
            'No physical calibration, energy-source, heat/work, audit, publication or model-selection conclusion.'
        ],
        'member_count': len(members),
        'members': members,
        'next_step': 'Stop after delivering this POST seal; preserve author and PRE generations.'
    }
    with destination.open('x') as stream:
        json.dump(seal, stream, indent=2)
        stream.write('\n')
    for member in members:
        (HERE / member['path']).chmod(0o444)
    destination.chmod(0o444)
    for member in read(destination)['members']:
        check_file(HERE / member['path'], member)
    for member in previous['members']:
        check_file(HERE / member['path'], member)
    print(json.dumps({
        'status': 'POST sealed; all 20 POST and all 25 preserved PRE members verified',
        'POST_sha256': sha(HERE / 'POST.md'),
        'POST_SEAL_sha256': sha(destination),
        'POST_SOURCE_PINS_sha256': sha(HERE / 'POST_SOURCE_PINS.json'),
        'own_binding_code_sha256': sha(HERE / 'post_bind_and_check.py'),
        'own_binding_output_sha256': sha(HERE / 'POST_BINDING_STDOUT.json'),
        'member_count': len(members),
        'released_source_origin_count': 10,
        'author_programs_executed': []
    }, indent=2))


if __name__ == '__main__':
    main()
