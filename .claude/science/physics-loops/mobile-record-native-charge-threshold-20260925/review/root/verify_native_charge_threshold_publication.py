"""One-time root receipt for the fully read publication40 correspondence."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,sys,time
E=Path(__file__).resolve().parent;D=E/'native-charge-identification-independent/publication_comparison'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
seal=D/'PUBLICATION_COMPARISON_SEAL.json'
assert sha(seal)=='03acaccb377f4f7296b33ac797031014f90aa652acdd12ed7178ed3819b7d3dd'
assert sha(D/'PUBLICATION_COMPARISON.md')=='191539d0684a81ad60f1867dec2cd236a61486a549da817f116156468deaa67e'
paths={seal}
for row in json.loads(seal.read_text())['members']:
 p=D/row['path'];assert sha(p)==row['sha256'] and p.stat().st_size==row['bytes'];paths.add(p)
for row in json.loads((D/'SOURCE_PINS.json').read_text())['members']:
 p=Path(row['origin']);assert p.read_bytes()==(D/row['snapshot']).read_bytes();paths.add(p)
def state():return {str(p):(sha(p),p.stat().st_size,p.stat().st_mtime_ns,p.stat().st_ctime_ns) for p in paths}
before=state();started=datetime.now(timezone.utc).isoformat();tick=time.perf_counter()
r=subprocess.run([sys.executable,'-B',str(D/'verify_correspondence.py'),'--seal'],capture_output=True)
elapsed=time.perf_counter()-tick
assert state()==before and r.returncode==0 and not r.stderr
old=json.loads((D/'verification_attempt02/stdout.json').read_text());fresh=json.loads(r.stdout)
ignore={'verified_utc','own_seal'}
assert {k:v for k,v in old.items() if k not in ignore}=={k:v for k,v in fresh.items() if k not in ignore}
assert old['own_seal'] is None and fresh['own_seal']==dict(sha256=sha(seal),members=172)
for name,body in [('NATIVE_CHARGE_THRESHOLD_FINAL_ROOT_READONLY.stdout.json',r.stdout),('NATIVE_CHARGE_THRESHOLD_FINAL_ROOT_READONLY.stderr.txt',r.stderr)]:
 with (E/name).open('xb') as f:f.write(body)
receipt=dict(at=started,report_sha256=sha(D/'PUBLICATION_COMPARISON.md'),seal_sha256=sha(seal),
 full_report_all_new_verifier_recorder_sealer_source_and_complete_output_read=True,
 failed_attempt_source_difference_and_full_stderr_read=True,
 scoped_prior_proof_PRE_POST_and_primary_reviews_reused=True,
 elapsed_seconds=elapsed,exit_code=0,stderr_bytes=0,sealed_members=172,
 original_correspondence_inputs=155,observed_files_byte_stat_unchanged=len(paths),
 output_exact_except_timestamp_and_new_seal_count=True,required_repairs=[],
 scope='Released-source correspondence, not an additional independent derivation or audit.',
 limits=['Global edge does not classify fixed-total-momentum fibers.','No finite-g energy-window probability, typical birth energy, selected charge packet or measured force.','Historical attempt04 writer and execution receipt remain missing.'],
 read_note='diff exit 1 means the expected preserved local checker correction, not a failed verification.')
with (E/'NATIVE_CHARGE_THRESHOLD_FINAL_ROOT_VERIFICATION.json').open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps(receipt,indent=2))
