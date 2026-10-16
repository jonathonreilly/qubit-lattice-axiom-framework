"""Preserve v1 evidence; verify the narrow midpoint correction and final sources."""
AUDIT_TIMEOUT_SEC=120
from pathlib import Path
import json,hashlib,gzip,os,subprocess,time,difflib
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent
manifest=ROOT/'.claude/science/physics-loops/ringdown-action-inverse-20261016/CANONICAL_FROZEN_v2.json'
f=json.loads(manifest.read_text());assert all(hashlib.sha256((ROOT/n).read_bytes()).hexdigest()==h for n,h in f.items())
(OUT/'frozen_sources_v2.json').write_text(json.dumps(f,indent=2))
correction=ROOT/'outputs/ringdown_action_inverse/MIDPOINT_CONTROL_CORRECTION.json';c=json.loads(correction.read_text());hist=[]
for r in c['historical_files']:
    b=(ROOT/r['archive']).read_bytes();raw=gzip.decompress(b)
    hist.append({'archive':r['archive'],'archive_hash_matches':hashlib.sha256(b).hexdigest()==r['archive_sha256'],'decompressed_hash_matches':hashlib.sha256(raw).hexdigest()==r['original_sha256']})
assert all(r['archive_hash_matches'] and r['decompressed_hash_matches'] for r in hist)
(OUT/'history_storage_check.json').write_text(json.dumps(hist,indent=2))
old=(OUT/'scratch/scripts/ringdown_action_math.py').read_text();new=(ROOT/'scripts/ringdown_action_math.py').read_text()
(OUT/'midpoint_v1_v2.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='frozen_v1',tofile='frozen_v2')))
scratch=OUT/'scratch_v2'
for n in ['docs/RINGDOWN_ACTION_RECONSTRUCTION_NOTE_2026-10-16.md','scripts/ringdown_action_inverse.py','scripts/ringdown_action_math.py']:
    dest=scratch/n;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes((ROOT/n).read_bytes())
# Retain original integration checker; only source binding and total-count expectation change.
text=(OUT/'integration_check.py').read_text().replace("'frozen_sources.json'","'frozen_sources_v2.json'").replace("==194","==195")
(OUT/'integration_check_v2.py').write_text(text)
receipts=[];env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1'
for label,script,cwd in [('integration_v2',OUT/'integration_check_v2.py',OUT),('sharp_midpoint_v2',OUT/'sharp_midpoint_check.py',OUT),('primary_v2',scratch/'scripts/ringdown_action_inverse.py',scratch)]:
    cmd=['python3','-B',str(script)];start=time.time();r=subprocess.run(cmd,cwd=cwd,env=env,capture_output=True,text=True,timeout=120)
    (OUT/(label+'_stdout.txt')).write_text(r.stdout);(OUT/(label+'_stderr.txt')).write_text(r.stderr)
    receipts.append({'command':cmd,'timeout_seconds':120,'PYTHONDONTWRITEBYTECODE':'1','returncode':r.returncode,'elapsed_seconds':time.time()-start})
(OUT/'execution_receipts_v2.json').write_text(json.dumps(receipts,indent=2))
actual=(scratch/'outputs/ringdown_action_inverse/controls.json').read_bytes();expected=(ROOT/'outputs/ringdown_action_inverse/controls.json').read_bytes()
cache=(ROOT/'logs/runner-cache/ringdown_action_inverse.txt').read_text().split('----- stdout -----\n',1)[1].split('\n----- stderr -----',1)[0]
summary={'controls_byte_identical':actual==expected,'cache_stdout_equal_ignoring_separator_newlines':cache.rstrip('\n')==(OUT/'primary_v2_stdout.txt').read_text().rstrip('\n'),'all_returncodes_zero':all(r['returncode']==0 for r in receipts),'primary_summary':json.loads(actual)['summary'],'integration_summary':json.loads((OUT/'integration_v2_stdout.txt').read_text())['summary'],'sharp_midpoint_summary':json.loads((OUT/'sharp_midpoint_v2_stdout.txt').read_text())['summary'],'note_and_primary_unchanged':all(hashlib.sha256((OUT/'scratch'/n).read_bytes()).hexdigest()==f[n] for n in ['docs/RINGDOWN_ACTION_RECONSTRUCTION_NOTE_2026-10-16.md','scripts/ringdown_action_inverse.py'])}
(OUT/'comparison_v2.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
