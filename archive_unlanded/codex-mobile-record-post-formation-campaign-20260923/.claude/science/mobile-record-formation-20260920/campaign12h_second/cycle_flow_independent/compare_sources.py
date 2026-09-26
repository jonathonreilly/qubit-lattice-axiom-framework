from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
import numpy,scipy,sympy
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent

def rec(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
pre=json.loads((HERE/'PRE_COMPARISON_SEAL.json').read_text())
for r in pre['sources']+pre['artifacts']:assert rec(Path(r['path']))==r
runner=ROOT/'bounded_cycle_flow_check.py';result=ROOT/'BOUNDED_CYCLE_FLOW_RESULTS.json';log=ROOT/'BOUNDED_CYCLE_FLOW_RUN.log'
assert rec(runner)['sha256']=='4f7b078d8e0afc908e5315efb5c785f892295380e7753030f0edc73a2feeffbc'
author=json.loads(result.read_text());lines=log.read_text().splitlines()
rows=[json.loads(line) for line in lines if line.startswith('{')]
assert rows==author['checks'] and lines[-1]=='TOTAL: PASS=10 FAIL=0'
assert len(rows)==10 and author['pass'] and all(row['pass'] for row in rows)
assert author['note_sha256']==pre['sources'][0]['sha256'] and author['runner_sha256']==rec(runner)['sha256']
target=json.loads((HERE/'RUNNER_ASSERTION_RESULTS.json').read_text())
baseline=target['receipts'][0]['rows']
assert baseline==rows[6:9]
assert target['receipts'][1]['rows'][0]['distinct_states']==1
res={'created_utc':datetime.now(timezone.utc).isoformat(),'sources':pre['sources']+[rec(p) for p in [runner,result,log]],
 'author_log_matches_complete_result':True,'author_control_rows':len(rows),'full_author_suite_reexecuted':False,
 'selective_author_execution':'Three loop controls baseline plus identity-reversal mutation, compiled in memory after pre-comparison seal',
 'mathematical_findings':[],'executable_findings':[{'id':'F1','severity':'narrow assertion coverage','function':'immutable_gauss_cycle','details':'Four-state construction count is reported, not asserted; identity reversal passes all three controls.'}],
 'runtime':{'python':sys.version,'numpy':numpy.__version__,'scipy':scipy.__version__,'sympy':sympy.__version__}}
(HERE/'SOURCE_COMPARISON.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
