"""Seal final correspondence while preserving every earlier sealed member."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def check(path, row):
    assert path.is_file(), str(path)
    assert path.stat().st_size == row['bytes'], str(path)
    assert sha(path) == row['sha256'], str(path)


def main():
    destination = HERE / 'PUBLICATION_COMPARISON_SEAL.json'
    assert not destination.exists(), 'Never replace an earlier seal.'
    preserved = {
        'PRE_SEAL.json': ('75bdc5d36dad74adf96285cefb0896539466f4e14c179cecc30f9afe5dbbf4ca', 25),
        'POST_SEAL.json': ('5c8cf25f153a2e8d2ece143e22afa95242c93e1ebfe137efa005809c2617b6a0', 20)
    }
    for name, (expected, count) in preserved.items():
        assert sha(HERE / name) == expected
        prior = load(HERE / name)
        assert prior['member_count'] == len(prior['members']) == count
        for row in prior['members']:
            check(HERE / row['path'], row)

    pins = load(HERE / 'PUBLICATION_SOURCE_PINS.json')
    assert len(pins['origins']) == 14
    for row in pins['origins']:
        check(HERE / row['frozen'], row)
        check(Path(row['origin']), row)

    evidence = load(HERE / 'PUBLICATION_BINDING_ATTEMPT_01_STDOUT.json')
    execution = load(HERE / 'PUBLICATION_BINDING_ATTEMPT_01_EXECUTION.json')
    assert execution['exit_code'] == 0
    assert sha(HERE / 'publication_bind_and_check.py') == execution['source_sha256'] == evidence['checker_sha256']
    assert sha(HERE / 'PUBLICATION_BINDING_ATTEMPT_01_STDOUT.json') == execution['stdout_sha256']
    assert sha(HERE / 'PUBLICATION_BINDING_ATTEMPT_01_STDERR.txt') == execution['stderr_sha256']
    assert (HERE / 'PUBLICATION_BINDING_ATTEMPT_01_STDERR.txt').stat().st_size == 0
    assert sha(HERE / 'PUBLICATION_SOURCE_PINS.json') == evidence['source_pins_sha256']
    assert evidence['total_current_origins_verified'] == 14
    assert evidence['nine_publication_bindings_verified'] == 9
    assert evidence['external_metadata_bindings_verified'] == 4
    assert evidence['separate_tooling_bindings_verified'] == 1
    assert evidence['full_payload_leaf_counts'] == {'str': 464, 'int': 232, 'bool': 8, 'float': 410}
    assert len(evidence['excluded_elapsed_fields_only']) == 2
    assert evidence['scientific_differences'] == evidence['binding_failures'] == []
    assert evidence['input_fingerprint_sha256'] == 'f82ab9b31c1b7e8dc17b5009f3d58f50bb4c01d4266a4643a208a89a52b51f35'
    assert evidence['full_cache_equals_reconstructed_header_stdout_stderr']
    assert evidence['execution_embedded_stdout_equals_result_plus_pass_marker']
    assert evidence['public_text_exact_scoped_transformations_verified']
    assert evidence['author_and_primary_programs_imported_or_executed'] == []
    assert evidence['cache_helper_imported_or_called'] is False
    assert evidence['new_independent_scientific_reconstruction'] is False
    assert evidence['other_active_science_opened'] == []

    names = [
        'PRE.md', 'PRE_SEAL.json', 'SOURCE_PINS.json',
        'POST.md', 'POST_SEAL.json', 'POST_SOURCE_PINS.json',
        'PUBLICATION_COMPARISON.md', 'PUBLICATION_SOURCE_PINS.json',
        'publication_bind_and_check.py', 'seal_publication_comparison.py',
        'PUBLICATION_BINDING_ATTEMPT_01_EXECUTION.json',
        'PUBLICATION_BINDING_ATTEMPT_01_STDOUT.json',
        'PUBLICATION_BINDING_ATTEMPT_01_STDERR.txt'
    ] + [row['frozen'] for row in pins['origins']]
    assert len(set(names)) == len(names) == 27
    members = [{'path': name, 'sha256': sha(HERE / name), 'bytes': (HERE / name).stat().st_size}
               for name in sorted(names)]
    seal = {
        'sealed_utc': datetime.now(timezone.utc).isoformat(),
        'signed_by': 'Codex scoped independent checker /root/rotor_upper_tail_check',
        'scope': 'Final publication correspondence for finite-window microscopic energy laws. Same scoped checker, no new independent scientific reconstruction, primary rerun or retained audit.',
        'report': 'PUBLICATION_COMPARISON.md',
        'publication_note_sha256': '55b3d3cad252bab95b96af4ab9165404545de141651fa32e8d642bd80940c693',
        'publication_wrapper_sha256': '566e019596b8f24e110bd2dc56e0fcdceb89a5dd57bf02d5dff37395f34ed084',
        'publication_result_sha256': evidence['result_sha256'],
        'publication_cache_sha256': evidence['cache_sha256'],
        'recomputed_input_fingerprint_sha256': evidence['input_fingerprint_sha256'],
        'preserved_seals': {name: {'sha256': pair[0], 'members_verified': pair[1]} for name, pair in preserved.items()},
        'source_origin_counts': {'publication_manifest_members': 9, 'external_process_metadata': 4,
                                 'separately_released_cache_tooling': 1, 'total': 14},
        'exact_parent_git_origins': 3,
        'complete_scientific_payload_leaf_counts': evidence['full_payload_leaf_counts'],
        'excluded_timing_fields': evidence['excluded_elapsed_fields_only'],
        'fresh_scientific_differences': [],
        'repairs_verified': ['Only distance-two A pairs in the full magnetic sum.',
                             'Fixed bounded continuous energy responses.',
                             'PRE Section 5 physical counterexample explicitly attributed; general stopped-instrument extension not promoted.'],
        'additional_repairs_identified': [],
        'failures_preserved': [
            'Root filename-lookup failure for CONTROL_ATTEMPT01_STDOUT.json versus CONTROL_ATTEMPT_01_STDOUT.json; no scientific failure or rerun.',
            'Initial combined metadata display truncated; all fields subsequently read in complete batches and full stdout/cache bound byte-for-byte.',
            'Earlier PRE lookup failure and all previous evidence remain unchanged.'
        ],
        'own_check': {'source': 'publication_bind_and_check.py',
                      'execution': 'PUBLICATION_BINDING_ATTEMPT_01_EXECUTION.json',
                      'output': 'PUBLICATION_BINDING_ATTEMPT_01_STDOUT.json', 'exit_code': 0,
                      'kind': 'Genuinely read-only source/AST/Git/payload/fingerprint/cache/text comparison.'},
        'author_or_primary_programs_imported_or_executed': [],
        'cache_tooling_functions_called': [],
        'other_active_scientific_packets_opened': [],
        'limitations': [
            'Scientific independence belongs to the sealed PRE; exact-source fresh execution is reuse.',
            'Fixed graph, fixed parameters, positive-probability finite windows, bounded spectral responses and ordered limits.',
            'No moment, support-edge, isolated-timestamp, arbitrary simultaneous-schedule or physical energy-calibration upgrade.',
            'No publication/repository/audit mutation; linked evidence-package copies beyond the stated manifest were not separately inventoried.'
        ],
        'member_count': len(members), 'members': members,
        'next_step': 'Stop after delivery; preserve every prior generation and the current publication sources.'
    }
    with destination.open('x') as stream:
        json.dump(seal, stream, indent=2)
        stream.write('\n')
    for member in members:
        (HERE / member['path']).chmod(0o444)
    destination.chmod(0o444)
    for member in load(destination)['members']:
        check(HERE / member['path'], member)
    for name in preserved:
        for member in load(HERE / name)['members']:
            check(HERE / member['path'], member)
    print(json.dumps({
        'status': 'Sealed final correspondence; 27 members, 25 PRE and 20 POST members verified',
        'PUBLICATION_COMPARISON_sha256': sha(HERE / 'PUBLICATION_COMPARISON.md'),
        'PUBLICATION_COMPARISON_SEAL_sha256': sha(destination),
        'PUBLICATION_SOURCE_PINS_sha256': sha(HERE / 'PUBLICATION_SOURCE_PINS.json'),
        'read_only_checker_sha256': sha(HERE / 'publication_bind_and_check.py'),
        'read_only_output_sha256': sha(HERE / 'PUBLICATION_BINDING_ATTEMPT_01_STDOUT.json'),
        'member_count': 27, 'current_source_origins_verified': 14,
        'recomputed_input_fingerprint_sha256': evidence['input_fingerprint_sha256'],
        'no_additional_repair_identified': True,
        'author_or_primary_programs_executed': []
    }, indent=2))


if __name__ == '__main__':
    main()
