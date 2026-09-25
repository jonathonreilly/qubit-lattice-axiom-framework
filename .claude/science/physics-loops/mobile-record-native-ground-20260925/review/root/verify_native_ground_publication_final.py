"""Root binds the sealed final comparison and replays its read-only checker.

Only new root verification files are written. No scientific program is run.
"""
from pathlib import Path
import datetime, hashlib, json, subprocess, sys, time

E = Path(__file__).resolve().parent
P = E/'ground-formation-incompatibility-independent/publication_comparison'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
seal = P/'PUBLICATION_COMPARISON_SEAL.json'
assert sha(seal) == 'fe73f2ace3948ed56f9b756652364fbb7012d2e8f858b73f7c42f8e896e95087'
s = json.loads(seal.read_text())
assert len(s['members']) == 113
def check_seal():
    for r in s['members']:
        p = P/r['path']
        assert sha(p) == r['sha256'] and p.stat().st_size == r['bytes'], str(p)
check_seal()
inventory = json.loads((P/'SOURCE_INVENTORY.json').read_text())
assert len(inventory['sources']) == 97
for r in inventory['sources']:
    assert (P/r['copy']).read_bytes() == Path(r['origin']).read_bytes()
assert sum(len(x['members']) for x in inventory['prior_seals']) == 254
for x in inventory['prior_seals']:
    assert sha(Path(x['origin'])) == x['sha256']
    for r in x['members']:
        assert sha(Path(r['path'])) == r['sha256']
outputs = [E/x for x in ['NATIVE_GROUND_FINAL_READONLY_RESULT.json',
    'NATIVE_GROUND_FINAL_READONLY.stderr', 'NATIVE_GROUND_FINAL_ROOT_VERIFICATION.json']]
assert not any(x.exists() for x in outputs)
program = P/'check_publication_read_only.py'
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
t = time.monotonic()
r = subprocess.run([sys.executable,str(program)],cwd=P,capture_output=True)
elapsed = time.monotonic()-t
for p,body in zip(outputs,[r.stdout,r.stderr]):
    with p.open('xb') as f: f.write(body)
assert r.returncode == 0 and not r.stderr
assert r.stdout == (P/'comparison_attempt01.stdout.txt').read_bytes()
report = json.loads(r.stdout)
assert report['all_checks_completed']
check_seal()
v = {'verified_utc':start,'elapsed_seconds':elapsed,'exit_code':r.returncode,
    'sealed_report_sha256':sha(P/'PUBLICATION_COMPARISON.md'),
    'seal_sha256':sha(seal),'seal_members':113,'frozen_sources':97,
    'prior_seals':9,'prior_member_entries':254,
    'checker_sha256':sha(program),'checker_is_read_only_after_full_source_review':True,
    'root_stdout_sha256':sha(outputs[0]),'root_stderr_bytes':len(r.stderr),
    'fresh_checker_output_byte_identical_to_sealed_output':True,
    'canonical_note_sha256':s['canonical_note_sha256'],
    'complete_payload_leaf_counts':report['all_payload_leaf_counts'],
    'exact_certificate_rows':sum(x['matrix_dimension'] for x in report['exact_quotient_certificates']),
    'exact_certificate_nonzero_entries':sum(x['serialized_nonzero_entries'] for x in report['exact_quotient_certificates']),
    'disclosed_difference_count':len(report['all_differences']),
    'new_scientific_or_eigensolver_execution':False,
    'audit_verdict_applied':False,'required_mathematical_repairs':[],
    'verification_scope':'Full final report/code/process read; all frozen sources and prior seals rebound; exact stored-certificate and cache arithmetic replay. Earlier blind PRE/released POST scopes remain separate.'}
with outputs[2].open('x') as f: json.dump(v,f,indent=2); f.write('\n')
print(json.dumps(v,indent=2))
