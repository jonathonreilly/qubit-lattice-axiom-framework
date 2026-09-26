"""Targeted post-seal check of the author's advertised four-state assertion.

Runs only immutable_gauss_cycle, with all artifacts written here. Primary
source bytes are compiled in memory, never changed or imported via pycache.
"""
from pathlib import Path
from contextlib import redirect_stdout
from datetime import datetime,timezone
import hashlib,io,json
HERE=Path(__file__).resolve().parent;source=HERE.parent/'bounded_cycle_flow_check.py'
raw=source.read_bytes();sha=hashlib.sha256(raw).hexdigest()
assert sha=='4f7b078d8e0afc908e5315efb5c785f892295380e7753030f0edc73a2feeffbc'
receipts=[]
for name,mutate in [('baseline',False),('identity_reversal',True)]:
 ns={'__file__':str(source),'__name__':'reviewed_author_module'}
 exec(compile(raw,str(source),'exec'),ns)
 if mutate:ns['reverse']=lambda records,center,species:records.copy()
 stream=io.StringIO();failure=None
 with redirect_stdout(stream):
  try:ns['immutable_gauss_cycle']()
  except AssertionError as exc:failure=str(exc)
 (HERE/(name.upper()+'.stdout')).write_text(stream.getvalue())
 receipts.append({'case':name,'assertion_failure':failure,'rows':ns['ROWS']})
assert receipts[0]['assertion_failure'] is None and receipts[0]['rows'][0]['distinct_states']==4
assert receipts[1]['assertion_failure'] is None and receipts[1]['rows'][0]['distinct_states']==1
assert all(row['pass'] for result in receipts for row in result['rows'])
result={'created_utc':datetime.now(timezone.utc).isoformat(),'author_source_sha256':sha,'finding':'Advertised four-state check does not assert four distinct configurations; identity reversal passes all three loop checks.',
 'narrow_correction':'Include distinct_states == 4 in the check condition; optionally also assert each prescribed reversal changes its state.',
 'current_mathematical_construction':'Correct, independently checked before author access. This is a verification-coverage defect, not a theorem counterexample.',
 'receipts':receipts}
(HERE/'RUNNER_ASSERTION_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='receipts'},indent=2))
