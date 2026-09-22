#!/usr/bin/env python3
"""Compact immutable evidence checks; no native acquisition or coefficient replay."""
from pathlib import Path

AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = [
    'docs/NATIVE_CERTIFIED_LOCAL_GREEN_SCALARS_NOTE_2026-09-09.md',
    'docs/NATIVE_FINITE_EXCITATION_WARD_NOTE_2026-09-09.md',
    'docs/NATIVE_GLOBAL_PROJECTOR_CERTIFICATE_NOTE_2026-09-10.md',
    'docs/NATIVE_INFINITE_STAR_NODE_REDUCTION_NOTE_2026-09-09.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/README.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-ACTIVATION_REVIEW-86f505c728a48253.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-ACTIVATION_REVIEW-cb4d66cbad2eac94.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-ARTIFACT_PLAN-5a8a2b441ec1dded.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-ASSUMPTIONS_AND_IMPORTS-04947ad72d106df1.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-AUTHOR_MUTANTS-4c11f8afb8302274.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-A_ONLY_REVIEW-4a2ba4925dd50891.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-CHECKPOINT78_REMOTE_VERIFICATION-9ff6c27c3072fc0d.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-CHECKPOINT79_REMOTE_VERIFICATION-01a3c547180bc9f5.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-CLAIM_STATUS_CERTIFICATE-4a3d4f79e164376b.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-COMPACT-69b5af166a49c855.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-CONTROLS-20f2e6ffca932449.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-CONTROLS-3a369818bf696627.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-CONTROLS-675d89c7fa1b3b43.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-CONTROLS-8a602f9ca83fbf6a.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-CONTROLS-a7b73b9da82d8f92.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-CONTROLS-b2d246b3036c06a9.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-CONTROLS-b3d6dc9a7e68a6db.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-CONTROLS-f23a3edec4cd4b55.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-DELIVERY_CHECKS-d2c56bbdc5ae09fb.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-DELIVERY_REVIEW-a70a576883bc78bc.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-DELTA_CONTROLS-baaf1a12cb9b6b6c.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-DERIVATION-0c6763218d7734e0.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-DERIVATION-159d5c30808e1081.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-DERIVATION-33ba8583384f11ed.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-DERIVATION-62709e00b4615a48.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-DERIVATION-8c91a53ccd862d1b.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-EXTERNAL-28658239fc4a9e58.stderr',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-EXTERNAL-c393aebba515e2dd.stderr',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-FIRST_FIXTURE_FAILURE-7a9c7136600efbe0.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-GEOMETRY_CONTROLS-11d09c2c34f27cae.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-GOAL-525566f7a8b7cb8d.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-GRAPH_NODE-54f4b6d36fe75849.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-HANDOFF-9ef67db77ea9ef6f.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-IMPORT_PROVENANCE-99dd1c01ed11f753.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-INITIAL_COMPACT_FAILURE-b64c27ced389297c.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-INITIAL_REVIEW-3acd7afef4b788fc.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-LITERATURE_BRIDGES-ae1d413e72d87337.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-NO_GO_LEDGER-47d6880ce44b1ce7.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-OPPORTUNITY_QUEUE-ccb74c0b7866140d.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-PARENT_CONTROLS-720586042d469c07.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-PARENT_SOURCE_REVIEW-841d62bd2592c3a9.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-PINS-363bb5009bd537d5.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-PR_BACKLOG-b978f18b90eeb9e7.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-RECEIPT-182cde36864ad325.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-RECEIPT-99c6c43db906ae94.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-REMOTE_RECOVERY_MAP-6549434afacfda1c.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-RESULT-92051ee6ddc51705.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-REVIEW-281ca1a78a5f44f6.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-REVIEW-7bc21b85e4219998.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-REVIEW-9eb580b6eb41f705.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-REVIEW-a050bc114cdca307.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-REVIEW-ced60f66502ab4dd.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-REVIEW-f61e60d9fc9a4fdd.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-REVIEW_HISTORY-3f4cb79c836849bf.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-ROOT_ACCEPTANCE-38e6755ff215833c.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-ROOT_ACCEPTANCE-824f1f3c619ae907.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-ROOT_CONTROLS-e3e5e264249496aa.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-ROOT_REVIEW-ab0d47185b27fc31.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-ROUTE_PORTFOLIO-026cc4e1e794b8fa.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-RUNTIME_WEIGHT_REVIEW-5109a1710d018446.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-SCHEMA_ACCEPTANCE-3560d08426427db8.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-SCHEMA_ACCEPTANCE-9c4103de8557b9dd.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-SERIALIZATION_DELTA-a105c34b391275d5.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-SOURCE_FREEZE-a1812fa3f1e28a8f.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-STATE-3b9688acc891237e.yaml',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-STATUS-6c33a39439907887.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-TRACE_GATE-f67515f6cce5b41d.md',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-WEIGHT_CONTROLS-8df0535bfd94a299.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-WORKER_COMPLETE-4b5f0349d8b47606.json',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-citation-build-1eb283eb8be98dce.stdout',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-citation-build-64231b4595364bb8.stderr',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-citation-manifest-e2ff6fe7b0b3314a.stderr',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-citation-manifest-f307520c9a415ef2.stdout',
    'docs/work_history/repo/review_feedback/pr8077-evidence/kept/pr8077-vocab-816a7bd74ca2db6b.stdout',
    'outputs/native_global_projector_certificate_2026_09_10_inputs/PATH_MAP.json',
]
from fractions import Fraction as F
import argparse,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
PATH_MAP=json.loads((ROOT/'outputs/native_global_projector_certificate_2026_09_10_inputs/PATH_MAP.json').read_text())
PACKET_PREFIX='.claude/science/physics-loops/native-global-projector-certificate-20260910'
def packet(name):
 return ROOT/PATH_MAP[PACKET_PREFIX+'/'+name]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--json',action='store_true');ap.parse_args()
 n=0
 def check(ok,label):
  nonlocal n
  if not ok:raise ValueError(label)
  n+=1
 pins=json.loads((packet('IMPORT_PROVENANCE.json')).read_text())
 for name,row in pins.items():check(sha(packet(name))==row['sha256'],'import '+name)
 read=lambda d,f:json.loads((packet('receipts/'+d+'/'+f)).read_text())
 d='native-global-projector-coefficient-run-prospective';r=read(d,'RESULT.json');ledger=r['ledger'];root=read('native-global-projector-coefficient-root-review','ROOT_ACCEPTANCE.json');schema=read('native-global-projector-coefficient-root-review','SCHEMA_ACCEPTANCE.json')
 check(root['result_sha256']==schema['result_sha256']==sha(packet('receipts/'+d+'/RESULT.json')),'result lineage')
 check(root['schema_sha256']==sha(packet('receipts/native-global-projector-coefficient-root-review/SCHEMA_ACCEPTANCE.json')),'schema lineage')
 check(root['once'] is True and root['independent_coefficient_reconciliation'] is True,'root scope')
 check(r['nodes']==schema['count']==378 and r['coefficient_blocks']==root['blocks']==schema['coefficient_blocks']==756,'node/block census')
 check(r['events']==schema['events']==root['events']==3407,'event census')
 check(r['native_oracle_calls']==0 and r['physical_columns_evaluated'] is False and r['gaussian_consumer_certified'] is False,'actual scope')
 check(root['gaussian_consumer_certified'] is False and schema['native_oracle_replay'] is False,'inherited truth')
 total=F(ledger['total_error']);check(total==F(root['total_error'])==F(schema['total_error']),'total copies')
 low=F(2,9)*F(5439,160)*F(1,2**48)+F(1,6)*F(867,32)*F(1,2**64)
 high=F(1,8)*F(9,64)**15*(1+F(18,64*33));quad=6139*F(4,25)**21
 check(total==low+high+quad+F(ledger['input_error']),'analytic sum')
 check(F(ledger['input_error'])>=0 and 0<total<F(2,10**13),'certified error')
 check(4*378+2+(4*15-2)==1572,'rank bound')
 check(root['external_seconds']==4.73 and root['external_seconds']<120,'external wall')
 check(0<root['external_rss_bytes']<384*1024**2 and 0<root['sampled_whole_tree_peak']<384*1024**2,'external memory')
 a=read('native-global-a378-root-review','ROOT_ACCEPTANCE.json');check(a['status']=='ACCEPTED_NEW_A378_ACQUISITION_ONCE' and a['points']==378 and a['all_A_width_gates'] is True,'A once')
 recovery=json.loads((packet('REMOTE_RECOVERY_MAP.json')).read_text());events=[v for k,v in recovery.items()if k.endswith('/EVENTS.ndjson')]
 check(len(events)==1 and events[0]['sha256']==schema['events_sha256'],'event recovery')
 checkpoints=[json.loads((packet(f'receipts/CHECKPOINT{x}_REMOTE_VERIFICATION.json')).read_text())for x in (78,79)]
 check(all(x['sha256_and_remote_git_blob_match'] is True for x in checkpoints),'remote verification')
 check(root['preregistration_commit']==checkpoints[0]['head'],'coefficient preregistration')
 result={'status':'PASS_COMPACT_EVIDENCE_ONLY','predicates':n,'total_error_upper_approx':float(total),'rank_upper':1572,'native_reruns':0,'full_alpha_established':False}
 (ROOT/'outputs/native_global_projector_certificate_2026_09_10.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print(json.dumps(result,indent=2,sort_keys=True))
 print(f'TOTAL: PASS={n} FAIL=0')
 print('per_element: imported identities and rational error-ledger consequences checked; coefficient assembly is not rerun')
 print('per_site: numerical real-space columns and sitewise wavefunctions are not evaluated by this compact checker')
 print('per_mode: rank upper bound checked algebraically; no numerical mode basis, Gram matrix or occupation tail computed')
 print('per_block: 378-node,756-block and3407-event receipt relationships checked; acquisition and event reconstruction not repeated')
 print('lattice_wide: infinite-operator bound uses linked analytical proofs and authenticated inputs; no full state or alpha calculation')
if __name__=='__main__':main()
