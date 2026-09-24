"""Replay seven scientific controls without mutating frozen publication evidence."""
from pathlib import Path
import datetime,hashlib,json,shutil,subprocess,sys,tempfile,time
HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for f in ('verify_finite_energy_supply_publication.py','verify_autonomous_clock_publication.py'):
 subprocess.run([sys.executable,str(HERE/f)],check=True)
tmp=Path(tempfile.mkdtemp(prefix='autonomous-clock-portable-'));copy=tmp/'campaign12h_fourth'
shutil.copytree(HERE,copy,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
jobs=[('autonomous_clock_author','clock_control.py','CLOCK_CONTROL_RESULTS.json'),('autonomous_clock_author','original_star_clock_control.py','ORIGINAL_STAR_CLOCK_RESULTS.json'),('autonomous_clock_independent','exact_clock_control.py','EXACT_CLOCK_RESULTS.json'),('autonomous_clock_independent','finite_clock_dynamics_control.py','FINITE_CLOCK_DYNAMICS_RESULTS.json'),('autonomous_clock_independent','clock_uniformity_control.py','CLOCK_UNIFORMITY_RESULTS.json'),('autonomous_clock_independent','traveling_packet_identity_control.py','TRAVELING_PACKET_IDENTITY_RESULTS.json'),('autonomous_clock_independent','traveling_program_and_star_control.py','TRAVELING_PROGRAM_AND_STAR_RESULTS.json')]
rows=[]
for i,(folder,script,result) in enumerate(jobs,1):
 wd=copy/folder;out=tmp/f'run_{i}.stdout';err=tmp/f'run_{i}.stderr';start=time.monotonic()
 with out.open('wb') as stdout,err.open('wb') as stderr:r=subprocess.run([sys.executable,script],cwd=wd,stdout=stdout,stderr=stderr)
 row={'script':folder+'/'+script,'source_sha256':sha(HERE/folder/script),'exit_code':r.returncode,'wall_seconds':time.monotonic()-start,'stdout':str(out),'stderr':str(err)};rows.append(row)
 assert r.returncode==0,row
 actual=json.loads((wd/result).read_text());expected=json.loads((HERE/folder/result).read_text())
 assert actual==expected,(script,'result differs')
 row['comparison']='Complete result JSON exactly equals frozen evidence.';row['result_sha256']=sha(wd/result)
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'temporary_copy':str(copy),'runs':rows,'all_seven_scientific_replays_passed':True,'limits':'Scientific controls rerun directly. Historical instruction-authentication/sealing wrappers are not rerun with omitted provenance snapshots. No private PDF or display diff needed.'}
(tmp/'PORTABLE_RUN_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'receipt':str(tmp/'PORTABLE_RUN_RECEIPT.json'),'runs':len(rows),'all_passed':True}))
