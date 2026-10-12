"""Fixture-only tamper checks; never executes the author's science runners."""
from pathlib import Path
import hashlib,json,subprocess,sys
root=Path(__file__).resolve().parent
recorder=root.parent/'dyadic_route_readiness/dyadic_even_refinement/record_process.py'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(recorder)=='3d2461a2df3229f96dd7172fd3afafa1a2001b5535d8b02218bd74992ba3027e'
seal=json.loads((root/'INDEPENDENT_EVIDENCE_SEAL.json').read_text())
rows=[]
def emit(name,ok,**data):
    r=dict(name=name,ok=bool(ok),**data);rows.append(r);print(json.dumps(r),flush=True)
emit('preexposure_independent_seal_unchanged',all(sha(root/x['path'])==x['sha256'] and (root/x['path']).stat().st_size==x['bytes'] for x in seal['files']),files=len(seal['files']))

for case in ['wrong_anchor','changed_before_run','changed_during_run']:
    d=root/'integrity_cases'/case;d.mkdir(parents=True,exist_ok=False)
    fixture=d/'fixture.txt';fixture.write_text('fixed fixture\n')
    manifest=d/'manifest.json';manifest.write_text(json.dumps({'files':{str(fixture):sha(fixture)}})+'\n')
    expected=sha(manifest)
    marker=d/'child_ran.txt'
    child='from pathlib import Path; Path('+repr(str(marker))+').write_text("executed\\n")'
    if case=='wrong_anchor':expected='0'*64
    if case=='changed_before_run':fixture.write_text('changed before execution\n')
    if case=='changed_during_run':child+='; Path('+repr(str(fixture))+').write_text("changed during execution\\n")'
    cmd=[sys.executable,str(recorder),'--record',str(d/'record'),'--timeout','2','--manifest',str(manifest),'--manifest-sha',expected,'--',sys.executable,'-c',child]
    p=subprocess.run(cmd,cwd=root,capture_output=True,timeout=5)
    (d/'recorder.stdout').write_bytes(p.stdout);(d/'recorder.stderr').write_bytes(p.stderr)
    r=json.loads((d/'record.receipt.json').read_text())
    if case!='changed_during_run':
        emit(case+'_rejects_before_child',p.returncode==2 and r['returncode']==2 and not marker.exists(),returncode=p.returncode,error=r.get('error'),child_executed=marker.exists())
    else:
        full_acceptance=(r['returncode']==0 and not r['timeout'] and r.get('source_unchanged') and r.get('source_before')==r.get('source_after'))
        emit('postrun_source_tamper_full_adoption_rejects',not full_acceptance and marker.exists(),returncode=p.returncode,source_unchanged=r.get('source_unchanged'),full_acceptance=bool(full_acceptance))
        emit('weak_returncode_only_check_survives',p.returncode==0,returncode=p.returncode,meaning='Successful process exit does not establish unchanged inputs; the actual author adoption code also checks source hashes.')

# A changed raw stream must no longer satisfy its sealed digest.
source=root/'runs/numeric_01/INNER.stdout';tamper=root/'integrity_cases/tampered_stream.stdout'
tamper.write_bytes(source.read_bytes()+b'\n')
emit('stream_digest_tamper_detected',sha(tamper)!=sha(source),original_sha256=sha(source),tampered_sha256=sha(tamper))
emit('all_integrity_predicates',all(r['ok'] for r in rows),count=len(rows))
sys.exit(0 if all(r['ok'] for r in rows) else 1)
