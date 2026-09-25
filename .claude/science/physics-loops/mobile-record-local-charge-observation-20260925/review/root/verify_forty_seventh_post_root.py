"""One-shot external receipt writer for the inspected sealed POST47 checker."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, sys, time

E = Path(__file__).resolve().parent
D = E / 'native-charge-finite-time-independent'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
def identity(p):
    s = p.stat()
    return (sha(p), s.st_size, s.st_mode, s.st_ino, s.st_dev,
            s.st_mtime_ns, s.st_ctime_ns, s.st_nlink)

assert sha(D/'POST_SEAL.json') == '2ce94c18e4e8ff9d0a0e14b0e2925e65b41aa7f02f4016530d07fb20325af7a6'
assert sha(D/'POST.md') == '6258dff3852b842a9c736d7194378aca3b1fae6837f1938cc347ea8a75fd36b9'
observed = {p for p in D.rglob('*') if p.is_file()}
counts = {}
for name in ('PRE_SEAL.json', 'POST_SEAL.json'):
    rows = json.loads((D/name).read_text())['members']
    counts[name] = len(rows)
    for r in rows:
        p = D/r['path']
        assert sha(p) == r['sha256'] and p.stat().st_size == r['bytes']
for r in json.loads((D/'POST_SOURCE_PINS.json').read_text())['sources']:
    p = Path(r['origin']); assert sha(p) == r['sha256']
    observed.add(p)
before = {str(p): identity(p) for p in observed}
program = D/'post_compare_read_only.py'
assert sha(program) == 'e3856ecc18409389c7c411af8c4641f43f346259aafa6b226012d6193946952e'
start = datetime.now(timezone.utc).isoformat(); t = time.monotonic()
run = subprocess.run([sys.executable, '-B', str(program)], cwd=D, capture_output=True)
elapsed = time.monotonic()-t
for p, record in before.items(): assert identity(Path(p)) == record
for suffix, raw in [('stdout.json',run.stdout),('stderr.txt',run.stderr)]:
    with (E/('FORTY_SEVENTH_POST_ROOT_READONLY.'+suffix)).open('xb') as f: f.write(raw)
assert run.returncode == 0 and not run.stderr, run.stderr.decode()
data = json.loads(run.stdout)
assert data == json.loads((D/'post_comparison.stdout.txt').read_text())
report = dict(started_utc=start, elapsed_seconds=elapsed, exit_code=run.returncode,
    program_sha256=sha(program), seal_member_counts=counts,
    observed_files=len(before), byte_and_stat_preservation=True,
    complete_scientific_output_equal=True,
    stdout_sha256=hashlib.sha256(run.stdout).hexdigest(),
    complete_POST_argument_and_new_checker_and_writers_read=True,
    all_six_compact_geometry_and_bound_groups_read=True,
    stored_large_support_lists_mechanically_reconstructed_not_all_manually_read=True,
    required_mathematical_repairs=[],
    scope='Root reviewed the complete released proof and fresh read-only correspondence. No independent propagation or new PRE attribution.',
    qualifications=['Degree-at-most-six constants and bounded functions of matter charges.',
      'Root quotient Cov(a,b)/Var(b) differs from PRE Pearson normalization.',
      'PRE colored-series refinement remains separately attributed and locally timed.',
      'Auxiliary A2/B4 tree permits two births; historical A3/B3 fixture does not.',
      'No measured charge/time/length/readout identification or empirical agreement.'])
with (E/'FORTY_SEVENTH_POST_ROOT_REVIEW.json').open('x') as f:
    json.dump(report,f,indent=2); f.write('\n')
print(json.dumps(report,indent=2))
