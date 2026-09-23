"""Freeze only this completed comparison; never mutate PRE or author files."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent / 'cube_unprepared_author'
SPECTRAL = HERE.parent / 'cube_point_spectrum_independent'


def row(path):
    path = Path(path).resolve()
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def authenticate(binding):
    assert row(binding['path']) == binding, binding


pre_row = row(HERE / 'PRE_COMPARISON_SEAL.json')
assert pre_row['sha256'] == '5d7d37fcc06fb75a647a1b5e2fe40b49ed6467c2185f5218da78b2fa2f8ca715'
pre = json.loads(Path(pre_row['path']).read_text())
for binding in pre['science_sources'] + pre['independent_artifacts']:
    authenticate(binding)
author_row = row(AUTHOR / 'AUTHOR_SEAL.json')
assert author_row['sha256'] == 'ed066b95b18992f86718fe960ed6624c163854d142d0f90a742a4c85377159f4'
author = json.loads(Path(author_row['path']).read_text())
for binding in author['artifacts']:
    assert Path(binding['path']).parent == AUTHOR
    authenticate(binding)
spectral_row = row(SPECTRAL / 'FINAL_SEAL.json')
assert spectral_row['sha256'] == 'f2df1efd5a7c7a63fb5200c0becb48278f79e448000afddcc8dc2bc48785111f'
comparison = json.loads((HERE / 'COMPARISON_RESULTS.json').read_text())
for binding in comparison['read_identities']:
    authenticate(binding)
assert comparison['source_sha256'] == row(HERE / 'comparison_check.py')['sha256']
receipt = json.loads((HERE / 'COMPARISON_RECEIPT.json').read_text())
assert receipt['exit_code'] == 0
assert receipt['script_sha256'] == comparison['source_sha256']
assert receipt['stdout_sha256'] == row(HERE / 'COMPARISON.stdout')['sha256']
assert receipt['stderr_sha256'] == row(HERE / 'COMPARISON.stderr')['sha256']
assert (HERE / 'COMPARISON.stderr').read_bytes() == b''
stream = (HERE / 'COMPARISON.stdout').read_text()
decoder = json.JSONDecoder()
objects = []
while stream.strip():
    obj, end = decoder.raw_decode(stream.lstrip())
    objects.append(obj)
    stream = stream.lstrip()[end:]
assert len(objects) == 3
assert objects[:2] == comparison['complete_spin_comparisons']
assert objects[-1] == comparison

source_paths = {binding['path'] for binding in comparison['read_identities']
                if Path(binding['path']).parent != HERE}
artifacts = [row(path) for path in sorted(HERE.iterdir())
             if path.is_file() and path.name != 'FINAL_SEAL.json']
assert len(artifacts) == 31
result = {
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'status': 'Completed selective source comparison; no required mathematical correction. Not a formal audit, retention or no-go verdict.',
    'original_pre_seal': pre_row,
    'authorized_author_seal': author_row,
    'scope': pre['scope'],
    'source_read_coverage': 'Entire frozen cube candidate proof, complete runner, saved result, stdout and receipt; full permitted spectral COMPARISON. Six candidate artifacts and all25 original PRE bindings authenticated. Author second_event helper and spectral author sources deliberately unopened; own frozen rules used instead.',
    'sources': [row(path) for path in sorted(source_paths)],
    'artifacts': artifacts,
    'mathematical_disposition': 'Fixed-electric-window density of the original supplied cube initialization converges to the N4 field density of trace exp(-48 kappa t), uniformly on compact ordinary-time intervals in the specified joint-spin scaling. No full trace-norm subsequence exists at fixed positive time in the fixed embedding. Source-bound deterministic microscopic transfer applies.',
    'required_corrections': [],
    'quantitative_differences': 'Author Gamma6<=36 kappa and R+2 enlargement are valid conservative bounds. Independent PRE gives Gamma6<=16 kappa and R+1; floating full-basis discrepancies are at most1.78e-15.',
    'author_addition_checked_after_pre': 'Uniform-input time-averaged local escape over arbitrary S-dependent initial positive densities. The initial-density convergence hypothesis is unnecessary in the integrated compactness/commutant argument. This stronger stated lemma is credited to the author.',
    'independent_pre_additions_preserved': 'Sharper16 loss and R+1 bounds; finite-spin first-clock Taylor and eight-unit-loss counterexamples; exact/asymptotic count bounds and count subsequence compactness; varying-source refocusing and translated-absorbing-state topology countercontrols.',
    'spectral_dependency': {
        'final_seal': spectral_row,
        'comparison': row(SPECTRAL / 'COMPARISON.md'),
        'disposition': 'Pending comparison dependency closed by permitted authenticated FINAL and complete COMPARISON, which reports no correction. No new spectral proof or recursive spectral audit performed in this consequence packet.',
        'domain': 'Physical six-record charge-four P-space rotor H2 only.'
    },
    'attribution_and_timeline': 'Independent PRE froze before checker candidate access; mathematical progress was sent to root during reconstruction, so reciprocal author blindness is not claimed. Author candidate already credits the prior independent ring commutant/time-smearing insight. Its cube uniform-input extension remains author-attributed; independent sharper controls remain PRE-attributed.',
    'executed_check': 'Post-PRE comparison runner used only frozen independent physical rules to reconstruct every author S1/S2 complete-spin matrix diagnostic and exact first-sector path formula. No author runner imported or executed; no time evolution or new spectral computation performed.',
    'execution_receipt': row(HERE / 'COMPARISON_RECEIPT.json'),
    'execution_stream_validation': 'All3 comparison stdout JSON objects match saved result/rows; stderr empty; exit0.',
    'failures_preserved': 'No mathematical comparison execution failed. One read-only ad hoc relative-path inspection failed, was corrected, and is explicitly preserved in POST_PRE_ADHOC_FAILURE.json without inventing an unavailable timed receipt.',
    'preservation': 'Original PRE seal, all5 sources and20 bound own artifacts unchanged; author and prior independent packets unchanged.',
    'limits': 'No exact limiting six/eight number split, positive lower second-event probability, growing-field distribution, unbounded electric-observable limit, quantitative convergence rate, alternative scaling/model conclusion, formal audit or retained/no-go packet PASS.',
    'excluded_sources_and_actions': 'All compensation/proposal packets, general compensation checker, campaign plans/checkpoint/registry, Git, publication, formal audit, external messaging and onward delegation remained excluded. Writes only in cube_unprepared_independent.'
}
destination = HERE / 'FINAL_SEAL.json'
assert not destination.exists()
destination.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'final_seal': row(destination), 'source_bindings': len(result['sources']),
                  'artifact_bindings': len(artifacts), 'pre_unchanged': True,
                  'mathematical_comparison_exit_code': receipt['exit_code']}, indent=2))
