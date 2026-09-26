"""Narrow F1 acknowledgment; exact replacement and affected loop controls only."""
from pathlib import Path
from datetime import datetime,timezone
from contextlib import redirect_stdout
import hashlib,io,json
HERE=Path(__file__).resolve().parent;REVIEW=HERE.parent;ROOT=REVIEW.parent
sha=lambda b:hashlib.sha256(b).hexdigest()
def rec(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
old=ROOT/'cycle_flow_f1_fix/bounded_cycle_flow_check_before_f1.py'
new=ROOT/'bounded_cycle_flow_check.py';note=ROOT/'BOUNDED_CYCLE_FLOW_AND_EULER_DYNAMICS.md'
author=ROOT/'cycle_flow_f1_fix/TARGETED_RESULTS.json'
oldraw=old.read_bytes();newraw=new.read_bytes()
assert sha(oldraw)=='4f7b078d8e0afc908e5315efb5c785f892295380e7753030f0edc73a2feeffbc'
assert sha(newraw)=='0f408c7ccd9d5dafdf2df0d639b7f99f73461992485fa5e2510af381e2f6da2d'
assert rec(note)['sha256']=='c100b9f20e091b944a78499c0112aae4803fdfb6b54f4e28330714a58b580b56'
oldblock='''    identities = sorted(initial.values())
    check("four_state_cycle_preserves_gauss_capacity_and_record_contents",
          states[-1] == states[0]
          and all(len(s) == 8 and sorted(s.values()) == identities for s in states)
          and all(not charge(field(s, a)) for s in states for a in ("E", "B")),
          distinct_states=len({tuple(sorted(s.items())) for s in states[:-1]}),
          record_count=8, cycle_length=4)
'''
newblock='''    identities = sorted(initial.values())
    distinct_states = len({tuple(sorted(s.items())) for s in states[:-1]})
    check("four_state_cycle_preserves_gauss_capacity_and_record_contents",
          states[-1] == states[0]
          and distinct_states == 4
          and all(len(s) == 8 and sorted(s.values()) == identities for s in states)
          and all(not charge(field(s, a)) for s in states for a in ("E", "B")),
          distinct_states=distinct_states,
          record_count=8, cycle_length=4)
'''
assert oldraw.count(oldblock.encode())==1 and newraw.count(newblock.encode())==1
assert oldraw.replace(oldblock.encode(),newblock.encode())==newraw
recovered=newraw.replace(newblock.encode(),oldblock.encode())
assert recovered==oldraw
# Bind and authenticate the immutable original review; no old evidence is rewritten.
previous=REVIEW/'FINAL_SEAL.json';report=REVIEW/'REPORT.md'
assert rec(previous)['sha256']=='ff379fd75c5a5b5c774d58b270ad6a58ab22ffcb4b5811a5cf5b5451a8c726e7'
assert rec(report)['sha256']=='7cf25f0053ba4fe60dfc39024df0c4e0caaa75e40bbf42f5adc1ea76181b64af'
previous_seal=json.loads(previous.read_text())
for r in previous_seal['artifacts']:assert rec(Path(r['path']))==r
receipts=[]
for name,mutate in [('baseline',False),('identity_mutation',True)]:
 ns={'__name__':'reviewed_author_module','__file__':str(new)}
 exec(compile(newraw,str(new),'exec'),ns)
 if mutate:ns['reverse']=lambda records,center,species:records.copy()
 out=io.StringIO();failure=None
 with redirect_stdout(out):
  try:ns['immutable_gauss_cycle']()
  except AssertionError as exc:failure=str(exc)
 (HERE/(name.upper()+'.stdout')).write_text(out.getvalue())
 receipts.append({'case':name,'assertion_failure':failure,'rows':ns['ROWS']})
assert receipts[0]['assertion_failure'] is None and len(receipts[0]['rows'])==3
assert all(r['pass'] for r in receipts[0]['rows']) and receipts[0]['rows'][0]['distinct_states']==4
assert receipts[1]['assertion_failure']=='four_state_cycle_preserves_gauss_capacity_and_record_contents'
assert len(receipts[1]['rows'])==1 and receipts[1]['rows'][0]['pass'] is False
assert receipts[1]['rows'][0]['distinct_states']==1
author_result=json.loads(author.read_text())
assert author_result['source_sha256']==sha(newraw) and author_result['receipts']==receipts
(HERE/'TARGETED_RESULTS.json').write_text(json.dumps({'corrected_source_sha256':sha(newraw),'receipts':receipts},indent=2)+'\n')
ack={'created_utc':datetime.now(timezone.utc).isoformat(),'finding':'F1','status':'closed',
 'scope':'Exact source replacement, unchanged note identity, affected baseline and identity mutation only. No broader mathematical rerun or audit verdict.',
 'sources':[rec(p) for p in [old,new,note,author,report,previous]],
 'exact_only_change':{'old_block':oldblock,'new_block':newblock,'inverse_recovers_original_bytes':True,'recovered_sha256':sha(recovered)},
 'original_review_artifacts_authenticated_unchanged':len(previous_seal['artifacts']),
 'baseline':'All three affected loop controls pass; four distinct states.',
 'identity_mutation':'Rejected by the corrected first assertion with one distinct state.',
 'author_targeted_receipts_match_independent_execution':True,
 'remaining_findings_from_original_review':[],
 'formal_audit_status_applied':False}
(HERE/'F1_ACK.json').write_text(json.dumps(ack,indent=2)+'\n')
print(json.dumps({k:v for k,v in ack.items() if k not in ('exact_only_change','sources')},indent=2))
