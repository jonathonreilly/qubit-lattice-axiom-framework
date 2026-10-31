"""Declared after independent run: exact author reproduction, not independent evidence."""
from pathlib import Path
import os,sys,re,json,subprocess,time,hashlib,resource,tempfile,datetime
HERE=Path(__file__).resolve().parent
start=time.monotonic();gates=[]
def gate(stage):
 t=subprocess.check_output(['/usr/bin/memory_pressure','-Q'],text=True)
 free=int(re.search(r'System-wide memory free percentage:\s*(\d+)%',t).group(1))
 load=os.getloadavg();rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 gates.append(dict(stage=stage,free_percent=free,load=load,own_rss_bytes=rss))
 assert free>=50 and max(load)<20 and rss<2_000_000_000
 assert os.getpriority(os.PRIO_PROCESS,0)>=10
 for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']:assert os.environ[k]=='1'
gate('before')
original=HERE/'uniform_one_loop_01.py'
source=original.read_bytes();assert hashlib.sha256(source).hexdigest()=='6cb6ffaddb6b47d526784098bf9eb96bdd3bb1757c7b5b0dad65a3d8fb5091f7'
work=Path(tempfile.mkdtemp(prefix='review_uniform_one_loop_author_',dir='/tmp'))
copy=work/'uniform_one_loop_01.py';copy.write_bytes(source)
with (HERE/'review_uniform_one_loop_author.stdout.txt').open('wb') as out,(HERE/'review_uniform_one_loop_author.stderr.txt').open('wb') as err:
 proc=subprocess.run([sys.executable,str(copy)],stdout=out,stderr=err,env=os.environ.copy())
child_rss=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
assert child_rss<2_000_000_000
gate('after')
assert time.monotonic()-start<60
actual=json.loads((work/'uniform_one_loop_01_results.json').read_text())
expected=json.loads((HERE/'uniform_one_loop_01_results.json').read_text())
(HERE/'review_uniform_one_loop_author_results.json').write_text(json.dumps(actual,indent=2,sort_keys=True)+'\n')
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'declaration':'First reproduction after complete independent38/38 run and full author-code read; exact all-field comparison, no changed thresholds.',
        'source_sha256':hashlib.sha256(source).hexdigest(),'temporary_copy':str(copy),'exit_code':proc.returncode,'results_match_exactly':actual==expected,
        'passed':actual['passed'],'total':actual['total'],'resource_gates':gates,'child_peak_rss_bytes':child_rss,'elapsed_seconds':time.monotonic()-start,
        'original_source_unchanged':original.read_bytes()==source}
(HERE/'review_uniform_one_loop_author_replay.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
assert proc.returncode==0 and actual==expected and original.read_bytes()==source
