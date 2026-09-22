"""Compact identity and immutable saved-status checks; no scientific replay."""
from pathlib import Path
import os,sys
if __name__=='__main__' and not (sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site):
 os.execv(sys.executable,[sys.executable,'-I','-B','-S',__file__,*sys.argv[1:]])
from fractions import Fraction as F
from itertools import combinations
import json,hashlib,math
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'outputs/native_finite_moment_ward_2026_09_10_inputs'
def validate_packet(tag, blobs):
 """Pure saved receipt validation. No original numerical evaluator is called."""
 def need(x):
  if not x:raise ValueError('invalid '+tag+' packet')
 def number(x,cap):need(type(x)in(int,float)and math.isfinite(x)and 0<x<cap)
 def integer(x,want):need(type(x)is int and x==want)
 def digest(name):return hashlib.sha256(blobs[name]).hexdigest()
 r,a,w,rr,s,rf=[json.loads(blobs[k])for k in ['RESULT','ROOT_ACCEPTANCE','WORKER_COMPLETE','RECEIPT','SCHEMA_ACCEPTANCE','ROOT_FREEZE']]
 caps={'DEGREE10':20,'ALLQ':10,'OMEGA5':30};cap=caps[tag]
 need(a['once']is True and a['result_sha256']==digest('RESULT')==w['result_sha256']==s['result_sha256'])
 need(a['root_freeze']==digest('ROOT_FREEZE') and a['worker_freeze']==digest('RUNTIME_FREEZE')==w['runtime_sha256']==rr['worker_freeze']==rf['worker_freeze'])
 need(a['schema_sha256']==digest('SCHEMA_ACCEPTANCE'));need(w['binding_sha256']==digest('BINDING'))
 number(r['seconds'],cap-1);number(w['seconds'],cap-1);number(rr['seconds'],cap-.5);number(a['external_seconds'],cap)
 need(r['seconds']<=w['seconds']<=rr['seconds']<=a['external_seconds'])
 need(rr['pass']is True and rr['failure']is None);integer(rr['returncode'],0)
 for x in [w['rss_bytes'],a['external_rss_bytes'],a['sampled_whole_tree_peak'],rr['sampled_whole_tree_peak']]:need(type(x)is int and 0<x<=384*1048576)
 need(a['sampled_whole_tree_peak']==rr['sampled_whole_tree_peak'])
 expected={
 'DEGREE10':('COMPLETE_FIXED_DEGREE10_CERTIFICATE','ACCEPTED_NEW_DEGREE10_WARD_CERTIFICATE_ONCE','COMPLETE_NEW_DEGREE10_ONLY','ACCEPTED_DEGREE10_WARD_SCHEMA'),
 'ALLQ':('COMPLETE_SAVED_ALLQ_SCREEN','ACCEPTED_NEW_NATIVE_ALLQ_SAVED_SCREEN_ROOT_REVIEW_ONCE','COMPLETE_SAVED_ALLQ_SCREEN_ONLY','ACCEPTED_ALLQ_SAVED_SCREEN_SCHEMA'),
 'OMEGA5':('CERTIFIED_TARGET','ACCEPTED_NEW_NATIVE_OMEGA5_ROOT_REVIEW_ONCE','COMPLETE_NEW_OMEGA5_ONLY','ACCEPTED_NEW_OMEGA5_SCHEMA')}
 need(tuple(x['status']for x in [r,a,w,s])==expected[tag])
 if tag=='DEGREE10':
  for key,v in [('choices',2),('events',205),('oracle_calls',0),('new_covariance_calls',0)]:integer(r[key],v)
  integer(s['count'],2);integer(s['events'],205);integer(s['native_oracle_calls'],0)
  need(r['sign_certified']is False and s['sign_certified']is False and a['sign_certified']is False)
  need(type(r['rows'])is list and len(r['rows'])==2)
  need([x['mode']for x in r['rows']]==['residual','variational']);need([x['status']for x in r['rows']]==s['choice_statuses']==a['choice_statuses']==['INDETERMINATE_SIGN']*2)
  for x in r['rows']:integer(x['ordered_words'],90)
 elif tag=='ALLQ':
  for key,v in [('modes',2),('saved_events',205),('native_calls',0),('original_moments_recomputed',0)]:integer(r[key],v)
  integer(s['count'],2);integer(s['source_events'],205);integer(s['excluded_modes'],2)
  need(r['all_fixed_first_polynomials_excluded']is True and s['all_fixed_first_polynomials_excluded']is True and s['alpha_no_go']is False)
  need(type(r['rows'])is list and len(r['rows'])==2);need([x['mode']for x in r['rows']]==['residual','variational'])
  for x in r['rows']:need(x['excluded']is True and x['status']=='CERTIFICATE_FAMILY_EXCLUDED')
 else:
  for key,v in [('nodes',1742),('panels',67),('moments_count',41),('tail_terms',40),('endpoint_oracles_reused',3484),('oracle_calls',0)]:integer(r[key],v)
  integer(s['count'],1742);integer(s['panels'],67);integer(s['oracle_calls'],0)
  need(s['target_certified']is True and s['full1742_node_and_tail_arithmetic_reconciled']is True)
  need(r['new_quantity_integral']is True and r['middle_width_gate']is True and r['weighted_t6_gate']is True)
  need(r['observable']=='omega5=E_X_power_5_over_2' and r['target']=='1/1000000000000000000000000')
 return True

def validation_mutants(tag, packet):
 """Rehash changed results so semantic adversaries are not merely hash failures."""
 def changed(name,key,value,rehash=False):
  b=dict(packet);x=json.loads(b[name]);x[key]=value;b[name]=json.dumps(x).encode()
  if rehash:
   dh=hashlib.sha256(b['RESULT']).hexdigest()
   for dest in ['ROOT_ACCEPTANCE','WORKER_COMPLETE','SCHEMA_ACCEPTANCE']:
    y=json.loads(b[dest]);y['result_sha256']=dh;b[dest]=json.dumps(y).encode()
   y=json.loads(b['ROOT_ACCEPTANCE']);y['schema_sha256']=hashlib.sha256(b['SCHEMA_ACCEPTANCE']).hexdigest();b['ROOT_ACCEPTANCE']=json.dumps(y).encode()
  return b
 cases=[changed('ROOT_ACCEPTANCE','once',False),changed('ROOT_ACCEPTANCE','result_sha256','0'*64),changed('RESULT','status','PHYSICAL_ALPHA_POSITIVE',True),changed('RESULT','oracle_calls'if tag!='ALLQ'else'native_calls',False,True),changed('WORKER_COMPLETE','rss_bytes',True)]
 count=0
 for bad in cases:
  try:validate_packet(tag,bad)
  except (ValueError,KeyError,TypeError):count+=1
  else:raise AssertionError('validation mutant accepted')
 return count

AUDIT_TIMEOUT_SEC=30
AUDIT_INPUT_PATHS=('docs/work_history/repo/review_feedback/pr8079-evidence/kept/pr8079-HIERARCHY-3d2cbcb326f3df28.md', 'docs/work_history/repo/review_feedback/pr8079-evidence/kept/pr8079-DEGREE10-bf797a38935a935a.md', 'docs/work_history/repo/review_feedback/pr8079-8083-scientific-recovery/manifest.json', 'docs/NATIVE_FINITE_MOMENT_WARD_NOTE_2026-09-10.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/ASSUMPTIONS_AND_IMPORTS.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/CLAIM_STATUS_CERTIFICATE.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/HANDOFF.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/IMPORT_PROVENANCE.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/NO_GO_LEDGER.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/RECOVERY.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/RECOVERY_MAP.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/REVIEW_HISTORY.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/STATE.yaml', 'outputs/native_finite_moment_ward_2026_09_10_inputs/TRACE_GATE.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/ALLQ_BINDING.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/ALLQ_PROTOCOL.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/ALLQ_RECEIPT.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/ALLQ_RESULT.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/ALLQ_ROOT_ACCEPTANCE.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/ALLQ_ROOT_FREEZE.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/ALLQ_RUNTIME_FREEZE.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/ALLQ_SCHEMA_ACCEPTANCE.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/ALLQ_WORKER_COMPLETE.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/ALLQ_compute.py', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/ALLQ_worker.py', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/ALL_Q.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/DEGREE10.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/DEGREE10_BINDING.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/DEGREE10_PROTOCOL.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/DEGREE10_RECEIPT.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/DEGREE10_RESULT.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/DEGREE10_ROOT_ACCEPTANCE.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/DEGREE10_ROOT_FREEZE.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/DEGREE10_RUNTIME_FREEZE.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/DEGREE10_SCHEMA_ACCEPTANCE.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/DEGREE10_WORKER_COMPLETE.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/DEGREE10_compute.py', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/DEGREE10_worker.py', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/DEGREE11.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/DEGREE20.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/HIERARCHY.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/OMEGA5.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/OMEGA5_BINDING.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/OMEGA5_PROTOCOL.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/OMEGA5_RECEIPT.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/OMEGA5_RESULT.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/OMEGA5_ROOT_ACCEPTANCE.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/OMEGA5_ROOT_FREEZE.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/OMEGA5_RUNTIME_FREEZE.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/OMEGA5_SCHEMA_ACCEPTANCE.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/OMEGA5_WORKER_COMPLETE.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/OMEGA5_compute.py', 'outputs/native_finite_moment_ward_2026_09_10_inputs/imports/OMEGA5_worker.py', 'outputs/native_finite_moment_ward_2026_09_10_inputs/reviews/AFFECTED_RUNNER_REVIEW.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/reviews/native-allq-saved-screen-cold-review_REVIEW.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/reviews/native-degree10-ward-cold-review_REVIEW.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/reviews/native-degree10-ward-runtime-cold-review_GUARD_DELTA.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/reviews/native-degree10-ward-runtime-cold-review_INITIAL_REVIEW.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/reviews/native-degree11-independent-review_REVIEW.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/reviews/native-degree20-independent-review_REVIEW.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/reviews/native-finite-moment-ward-cold-review_REVIEW.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/reviews/native-omega5-independent-review_AFFECTED_CONFIRMATION.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/reviews/native-omega5-independent-review_REVIEW.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/reviews/native-omega5-math-cold-review_REVIEW.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/reviews/native-omega5-root-independent-review_AFFECTED_PASS.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/reviews/native-omega5-root-independent-review_REVIEW.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/verification/CHECKPOINT83_REMOTE_VERIFICATION.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/verification/DELIVERY_CHECKS.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/verification/DELIVERY_FREEZE.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/verification/FINAL_PARENT_DELIVERY_REVIEW.md', 'outputs/native_finite_moment_ward_2026_09_10_inputs/verification/GRAPH_RECEIPT.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/verification/SOURCE_FREEZE.json', 'outputs/native_finite_moment_ward_2026_09_10_inputs/verification/SUPPORT_OUTPUT.txt', 'outputs/native_finite_moment_ward_2026_09_10_inputs/verification/VOCAB.json')
def main():
 n=0
 def check(ok):
  nonlocal n
  if not ok:raise AssertionError(n)
  n+=1
 for row in json.loads((PACK/'IMPORT_PROVENANCE.json').read_text()):check(hashlib.sha256((ROOT/('outputs/native_finite_moment_ward_2026_09_10_inputs'+row['local'].removeprefix('.claude/science/physics-loops/native-finite-moment-ward-20260910'))).read_bytes()).hexdigest()==row['sha256'])
 labels=list(combinations(range(6),2));degrees=[sum(not(set(a)&set(c))for c in labels)for a in labels];check(degrees==[6]*15);check(sum(degrees)==90)
 # Literal polynomial-division identity at synthetic single-atom points.
 for x in [F(1),F(2),F(3)]:
  for t in [F(1,2),F(1),F(2)]:check(x*x-x*t*t+t**4-t**6/(x+t*t)==x**3/(x+t*t))
 check(F(9,4)-F(17,16)**2-F(15,16)**2==F(31,128))
 # Exact cancellation underlying all-q exclusion, synthetic nonnegative data.
 for E in [F(1),F(2)]:
  X,V,a,j,delta,T=F(3),F(4),F(2),F(2),F(1),F(5)
  C=E*(2*X+E+V)
  nominal=a*a*(1+j/delta)+a*T/delta
  error=C+(X+E)*T/delta
  check(nominal-error<=a*a*(1+j/delta)-C)
 d=json.loads((PACK/'imports/DEGREE10_RESULT.json').read_text());check(d['sign_certified']is False);check([r['status']for r in d['rows']]==['INDETERMINATE_SIGN']*2)
 a=json.loads((PACK/'imports/ALLQ_RESULT.json').read_text());check(a['all_fixed_first_polynomials_excluded']is True);check([r['status']for r in a['rows']]==['CERTIFICATE_FAMILY_EXCLUDED']*2)
 o=json.loads((PACK/'imports/OMEGA5_RESULT.json').read_text());check(o['status']=='CERTIFIED_TARGET');check(o['oracle_calls']==0)
 for tag in ['DEGREE10','ALLQ','OMEGA5']:
  names=['RESULT','ROOT_ACCEPTANCE','WORKER_COMPLETE','RECEIPT','SCHEMA_ACCEPTANCE','ROOT_FREEZE','RUNTIME_FREEZE','BINDING']
  packet={name:(PACK/'imports'/(tag+'_'+name+'.json')).read_bytes()for name in names}
  check(validate_packet(tag,packet));check(validation_mutants(tag,packet)==5)
 result={'status':'PASS_COMPACT_ONLY','checks':n,'native_or_saved_arithmetic_replays':0}
 print(f'TOTAL: PASS={n} FAIL=0')
 print('SUPPORT_ONLY: no native or saved-node arithmetic replay; full integration and audit NOT RUN')
 result['current_claim_disposition']='positive constructions and finite descriptive outcomes only; negative certification deferred'
 (ROOT/'outputs/native_finite_moment_ward_2026_09_10.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print('per_element: exact finite synthetic identities and saved certificate semantics; original numerical arithmetic not replayed')
 print('per_site: supplied local defect families and original Gaussian reference; no new physical lattice or state evaluation')
 print('per_mode: preserved residual and variational modes, with both sign intervals still inconclusive')
 print('per_block: immutable source/result bindings and semantic rejection controls; historical production budgets remain distinct')
 print('lattice_wide: conditional analytical Ward and moment statements use linked proofs; no full alpha sign or model-selection calculation')
if __name__=='__main__':main()
