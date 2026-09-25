"""One-time POST46 sealer; writes only new POST seal and chmods its new members.

Does not execute a verifier or any scientific/historical/author program. The
unchanged PRE and released author generations are checked, never rewritten.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

D = Path(__file__).resolve().parent
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def identity(p):
    s = p.stat()
    return dict(path=str(p), sha256=sha(p), bytes=s.st_size,
                mtime_ns=s.st_mtime_ns, mode=s.st_mode, inode=s.st_ino)
def read(name):
    return json.loads((D / name).read_text())

assert not (D / 'POST_SEAL.json').exists()
pins = read('POST_SOURCE_PINS.json')
pre = read('PRE_SEAL.json')
assert sha(D / 'PRE_SEAL.json') == pins['pre_seal_sha256']
old = {'PRE_SEAL.json'} | {r['path'] for r in pre['members']}
assert len(old) == 32
for r in pre['members']:
    assert sha(D / r['path']) == r['sha256']
baseline = read('POST_PRESERVATION_BASELINE.json')
for r in baseline['files']:
    assert identity(Path(r['path'])) == r
for r in pins['sources']:
    assert sha(Path(r['origin'])) == sha(D / r['snapshot']) == r['sha256']
for r in pins['reused_pre_origins']:
    assert sha(Path(r['origin'])) == sha(D / r['snapshot']) == r['sha256']
receipt = read('post_verification_attempt01/EXECUTION.json')
result = read('post_verification_attempt01/stdout.json')
assert receipt['exit_code'] == 0 and receipt['all_byte_stat_unchanged'] is True
assert receipt['before'] == receipt['after'] and receipt['observed_files'] == 77
for r in receipt['after']:
    assert identity(Path(r['path'])) == r
assert sha(D / 'verify_post_readonly.py') == sha(D / 'post_verification_attempt01/source.py') == receipt['source_sha256']
assert sha(D / 'post_verification_attempt01/stdout.json') == receipt['stdout_sha256']
assert sha(D / 'post_verification_attempt01/stderr.txt') == receipt['stderr_sha256']
assert (D / 'post_verification_attempt01/stderr.txt').read_bytes() == b''
assert (D / 'POST_CAPTURE.stderr.txt').read_bytes() == b''
assert (D / 'POST_VERIFICATION_RECORDER.stderr.txt').read_bytes() == b''
assert result['primitive_rows_checked'] == result['exact_pre_star_correspondences'] == 8480
assert result['covariance_entries_checked'] == 180 and len(result['groups']) == 5
report = (D / 'POST.md').read_text()
assert 'one required prose repair' in report
assert 'For the separately supplied zero-field basis vector, the expectation of that off-diagonal Hamiltonian current vanishes; it need not vanish for arbitrary field input.' in report
members = []
for p in sorted(D.rglob('*')):
    if p.is_file():
        rel = str(p.relative_to(D))
        assert not p.is_symlink() and '__pycache__' not in p.parts
        if rel in old:
            continue
        members.append(dict(path=rel, sha256=sha(p), bytes=p.stat().st_size))
seal = dict(sealed_utc=datetime.now(timezone.utc).isoformat(),
    phase='Released-source POST46 after unchanged blind PRE46',
    report='POST.md', report_sha256=sha(D / 'POST.md'),
    members=members, source_pins_sha256=sha(D / 'POST_SOURCE_PINS.json'),
    preserved_pre_seal_sha256=sha(D / 'PRE_SEAL.json'),
    reviewed_author_seal_sha256=pins['author_seal_sha256'],
    reviewed_author_note_sha256='b8bec7cc03e7af401aae097445ae24faecd45dcffd8e0273300f16d17d455c1d',
    sources=pins['sources'], reused_origins=pins['reused_pre_origins'],
    findings=dict(equation_or_control_repair_required=False,
        required_prose_repair='Author section 2: remove only/exclusivity of zero-field basis vector for vanishing Hamiltonian-current expectation; nonzero electric basis states and all normal diagonal mixtures also give zero.',
        repair_applied=False, author_generation_preserved=True,
        pre_extensions_separately_attributed=True),
    verification=dict(code='verify_post_readonly.py', receipt='post_verification_attempt01/EXECUTION.json',
        exit_code=0, elapsed_seconds=receipt['elapsed_seconds'], empty_stderr=True,
        observed_files_byte_stat_unchanged=77, raw_rows_exactly_checked=8480,
        raw_rows_all_manually_read=False, all_compact_groups_and_diff_read=True,
        author_or_historical_program_execution=False, failed_post_executions=[]),
    scope='Finite common-law current/domain and initial charge moments; no microscopic derivative transfer, measured spectrum, calibration, public edit or applied audit status.')
with (D / 'POST_SEAL.json').open('x') as f:
    json.dump(seal, f, indent=2, sort_keys=True); f.write('\n')
for r in members:
    (D / r['path']).chmod(0o444)
(D / 'POST_SEAL.json').chmod(0o444)
for r in members:
    assert sha(D / r['path']) == r['sha256']
for r in baseline['files']:
    assert identity(Path(r['path'])) == r
print(json.dumps(dict(report_sha256=seal['report_sha256'],
    seal_sha256=sha(D / 'POST_SEAL.json'), members=len(members),
    prior_pre_members_preserved=31, author_members_preserved=15,
    required_prose_repair=True), indent=2))
