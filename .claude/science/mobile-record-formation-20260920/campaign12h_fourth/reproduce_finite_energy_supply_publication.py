"""Six selected scientific replays in an expendable portable copy."""
from pathlib import Path
import datetime,hashlib,json,shutil,subprocess,sys,tempfile,time
HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for verifier in ('verify_microscopic_energy_publication.py','verify_finite_energy_supply_publication.py'):
    subprocess.run([sys.executable,str(HERE/verifier)],check=True)
tmp=Path(tempfile.mkdtemp(prefix='finite-energy-supply-portable-'))
copy=tmp/'campaign12h_fourth'
shutil.copytree(HERE,copy,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
jobs=[
 ('coherent_energy_supply_author','coherent_fuel_control.py',[], 'COHERENT_FUEL_RESULTS.json','COHERENT_FUEL_RESULTS.json'),
 ('coherent_energy_supply_independent','coherent_supply_check.py',['--attempt','portable'], 'RESULTS_portable.json','RESULTS_01.json'),
 ('full_instrument_energy_supply_author','finite_battery_control.py',[], 'FINITE_BATTERY_RESULTS.json','FINITE_BATTERY_RESULTS.json'),
 ('full_instrument_energy_supply_author','marked_collision_control.py',[], 'MARKED_COLLISION_RESULTS.json','MARKED_COLLISION_RESULTS.json'),
 ('full_instrument_energy_supply_independent','control.py',['CONTROL_RESULTS_portable.json'], 'CONTROL_RESULTS_portable.json','CONTROL_RESULTS_02.json'),
 ('full_instrument_energy_supply_independent','comparison_control.py',[], 'COMPARISON_CONTROL_RESULTS.json','COMPARISON_CONTROL_RESULTS.json'),
]
rows=[]
for i,(folder,script,args,result,expected) in enumerate(jobs,1):
    wd=copy/folder;start=time.monotonic();out=tmp/f'run_{i}.stdout';err=tmp/f'run_{i}.stderr'
    with out.open('wb') as stdout,err.open('wb') as stderr:
        done=subprocess.run([sys.executable,script,*args],cwd=wd,stdout=stdout,stderr=stderr)
    row={'script':folder+'/'+script,'argv':[sys.executable,script,*args],'exit_code':done.returncode,
         'wall_seconds':time.monotonic()-start,'stdout':str(out),'stderr':str(err),'source_sha256':sha(HERE/folder/script)}
    rows.append(row)
    assert done.returncode==0,row
    actual=json.loads((wd/result).read_text());old=json.loads((HERE/folder/expected).read_text())
    if script=='coherent_supply_check.py':
        keys=('generic','actual_star_rows','checks','summary','status','runner_sha256')
        assert all(actual[k]==old[k] for k in keys)
        row['comparison']='Exact generic/physical/check results; creation time and attempt name intentionally differ.'
    else:
        assert actual==old,(script,'result differs')
        row['comparison']='Complete result JSON exactly matches frozen evidence.'
    row['result_sha256']=sha(wd/result)
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'temporary_copy':str(copy),
         'runs':rows,'all_six_scientific_replays_passed':True,
         'limits':'Coherent POST procedural-authentication wrapper not rerun with omitted instruction snapshots. Its mathematics, code and frozen comparison were reviewed separately. No private PDF was copied or needed.'}
(tmp/'PORTABLE_RUN_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'receipt':str(tmp/'PORTABLE_RUN_RECEIPT.json'),'runs':len(rows),'all_passed':True}))
