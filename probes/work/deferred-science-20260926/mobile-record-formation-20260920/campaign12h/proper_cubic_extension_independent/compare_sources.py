from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
def rec(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
pre=json.loads((HERE/'PRE_COMPARISON_SEAL.json').read_text())
for r in [pre['source'],pre['dependency']]+pre['artifacts']:assert rec(Path(r['path']))==r
paths=[ROOT/n for n in ['PROPER_CUBIC_ELEVEN_COUPLINGS_AND_VECTOR_SELECTION.md','proper_cubic_eleven_check.py','PROPER_CUBIC_ELEVEN_RESULTS.json','PROPER_CUBIC_ELEVEN_RUN.log','cubic_entropy_symbol_check.py']]
author=json.loads(paths[2].read_text());own=json.loads((HERE/'INDEPENDENT_RESULTS.json').read_text())
assert author['source_sha256']==rec(paths[1])['sha256']
assert author['frozen_base_source_sha256']==rec(paths[4])['sha256']=='7103bd3d00d204186952c6d4e7b29d1286a619413b0ce0b01f9cfca179477927'
assert json.loads(paths[3].read_text())==author
assert author['proper_cubic_dimension_exact']==author['explicit_family_dimension']==11
assert author['full_vector_source_channels']==[0,1,3,4,5,6,7,8]
assert author['curl_readout_source_channels']==[3,4,7,8]
assert author['extra_six_have_even_reversal_parity'] is True
assert author['closed_vector_generic_example_nonzero_modes']==own['generic_closed_vector_example_rank']==10
assert author['closed_vector_generic_example_zero_modes']==4
result={'created_utc':datetime.now(timezone.utc).isoformat(),'sources':[rec(p) for p in paths]+[pre['dependency']],
 'status':'Complete note, checker and results/log compared; source bindings and findings agree',
 'author_checker_executed_by_review':False,'independent_exact_checks':'Actual species covariance, complete polynomial constraint systems, determinant, rank and current normalization',
 'not_inferred_from_author_floating_controls':['No-cancellation necessity','Raw-Gauss kernel condition','Longitudinal kernel condition for derivative readouts'],
 'actionable_findings':[]}
(HERE/'COMPARISON_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
