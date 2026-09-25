"""One-time root replay of sealed, read-only publication correspondence."""
from pathlib import Path
import datetime, hashlib, json, subprocess, sys, time

E = Path(__file__).resolve().parent
P = E/'native-birth-cluster-transport-independent/publication_comparison_42_43'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
seal_path = P/'PUBLICATION_COMPARISON_SEAL.json'
assert sha(seal_path) == 'f9557764e92daca33e8492f77864e2d4021072d2ab90531569b592f540b7736a'
seal = json.loads(seal_path.read_text())
paths = {seal_path}
for row in seal['members']:
    p = P/row['path']
    assert sha(p) == row['sha256'] and p.stat().st_size == row['bytes']
    paths.add(p)
pins = json.loads((P/'SOURCE_PINS.json').read_text())
own = json.loads((P/'OWN_43_PRESERVATION_BEFORE.json').read_text())['files']
mechanics = json.loads((P/'MECHANICAL_SOURCE_PINS.json').read_text())
for row in [*pins['sources'], *own, *mechanics['sources']]:
    p = Path(row.get('origin', row.get('path')))
    assert sha(p) == row['sha256']
    paths.add(p)

def identity(p):
    s = p.stat()
    return dict(sha256=sha(p), bytes=s.st_size, mode=s.st_mode,
                dev=s.st_dev, ino=s.st_ino, mtime_ns=s.st_mtime_ns,
                ctime_ns=s.st_ctime_ns, nlink=s.st_nlink)

before = {str(p): identity(p) for p in sorted(paths)}
script = P/'compare_read_only.py'
assert sha(script) == 'ed893670e8788efff968bb0f412513cc5d9caae04ad385577f9b6dca4779982c'
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
t = time.monotonic()
run = subprocess.run([sys.executable, '-B', str(script)], cwd=P,
                     capture_output=True, check=False)
elapsed = time.monotonic()-t
for suffix, data in [('stdout.json', run.stdout), ('stderr.txt', run.stderr)]:
    with (E/('BIRTH_CHARGE_TRANSPORT_FINAL_ROOT_READONLY.'+suffix)).open('xb') as f:
        f.write(data)
assert run.returncode == 0 and not run.stderr, run.stderr.decode()
assert run.stdout == (P/'comparison.stdout.txt').read_bytes()
after = {str(p): identity(p) for p in sorted(paths)}
assert before == after
j = json.loads(run.stdout)
assert j['source_origins_checked'] == 104 and j['own43_files_unchanged'] == 80
assert [r['exact_nontiming_scalar_leaves'] for r in j['complete_fresh_scientific_payload_comparisons']] == [186008, 17758]
result = dict(
    started_utc=start, elapsed_seconds=elapsed, exit_code=run.returncode,
    verifier_sha256=sha(Path(__file__)), checker_sha256=sha(script),
    report_sha256=sha(P/'PUBLICATION_COMPARISON.md'), seal_sha256=sha(seal_path),
    sealed_members=len(seal['members']), source_origins=104, prior_own43_files=80,
    observed_files=len(paths), complete_byte_and_stat_preservation=True,
    exact_original_comparator_stdout=True,
    stdout_sha256=hashlib.sha256(run.stdout).hexdigest(),
    nontiming_leaves=[186008,17758], required_repairs=[],
    root_reading=dict(report='Complete scientific report, all new code and process/failure records read before replay.',
        output='Complete compact output read. A prior clipped middle was retrieved by exact top-level filename on 2026-09-25 before this receipt; no complete-read credit from the clipped command.',
        lexical_tokens='All lexical declared input records read separately before recovery.',
        historical_science='Separate author42/43 and PRE/POST full readings and fresh read-only replays recorded in their existing receipts.'),
    limits=['Final correspondence is released-source comparison, not a further blind reconstruction.',
        'Orientation-averaged static law includes both signs (coherent edge or unresolved resolved first mark).',
        'Whole-grouping transport coefficients concern the same-number-sector complement, not later-birth population.',
        'Motion result requires supplied immediately pre-mark zero-field input; no persistent particle, calibrated observable or empirical confirmation.'],
    identities=before)
with (E/'BIRTH_CHARGE_TRANSPORT_FINAL_ROOT_VERIFICATION.json').open('x') as f:
    json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in result.items() if k!='identities'},indent=2))
