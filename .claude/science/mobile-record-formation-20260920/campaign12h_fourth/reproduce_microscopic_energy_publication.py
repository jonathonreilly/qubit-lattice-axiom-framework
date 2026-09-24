"""Replay six selected scientific controls in an expendable adjacent-layout copy.
Historical instruction-authentication wrappers are not part of this replay.
"""
from pathlib import Path
import datetime,hashlib,json,os,shutil,subprocess,sys,tempfile,time
HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
out=Path(tempfile.mkdtemp(prefix='microscopic-energy-portable-'))
packets=('microscopic_birth_energy_author','microscopic_birth_energy_extension_author',
         'microscopic_electric_robustness_author','microscopic_birth_energy_independent',
         'microscopic_electric_robustness_independent')
for name in packets:shutil.copytree(HERE/name,out/name)
runs=(
 ('microscopic_birth_energy_author/exact_star_energy.py','EXACT_STAR_ENERGY_RESULTS.json'),
 ('microscopic_birth_energy_extension_author/star_finite_time_energy.py','STAR_FINITE_TIME_ENERGY_RESULTS.json'),
 ('microscopic_electric_robustness_author/exact_electric_star_energy.py','EXACT_ELECTRIC_STAR_ENERGY_RESULTS.json'),
 ('microscopic_electric_robustness_independent/star_local_matrix_control.py','EXACT_STAR_MATRIX_RESULTS.json'),
 ('microscopic_electric_robustness_independent/star_finite_time_control.py','FINITE_TIME_RESULTS.json'),
 ('microscopic_electric_robustness_independent/compare_frozen_sources.py','COMPARISON_RESULTS.json'))
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'portable_copy':str(out),'scope':'Six scientific replays, no historical procedure wrappers or new independence claim','runs':[]}
for number,(script,resultname) in enumerate(runs,1):
    original=HERE/script;copied=out/script
    stdout=out/f'run{number}.stdout';stderr=out/f'run{number}.stderr'
    start=time.monotonic()
    with stdout.open('wb') as o,stderr.open('wb') as e:
        proc=subprocess.run([sys.executable,str(copied)],cwd=out,
            env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'},stdout=o,stderr=e)
    result=copied.parent/resultname;expected=original.parent/resultname
    same=proc.returncode==0 and result.exists() and result.read_bytes()==expected.read_bytes()
    row={'script':script,'script_sha256':sha(original),'exit_code':proc.returncode,
      'wall_seconds':time.monotonic()-start,'result':str(result.relative_to(out)),
      'result_byte_identical':same,'expected_sha256':sha(expected),
      'actual_sha256':sha(result) if result.exists() else None,
      'stdout':str(stdout),'stderr':str(stderr),'stdout_sha256':sha(stdout),'stderr_sha256':sha(stderr)}
    receipt['runs'].append(row)
    (out/'PORTABLE_RUN_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    if not same:raise AssertionError(row)
receipt['completed_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
(out/'PORTABLE_RUN_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'portable_copy':str(out),'receipt':str(out/'PORTABLE_RUN_RECEIPT.json'),
 'scientific_replays':len(runs),'all_result_bytes_identical':True},indent=2))
