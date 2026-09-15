#!/usr/bin/env python3
"""Compact exact checks only; not archived native matrix replay."""
import argparse,json,hashlib
from pathlib import Path

AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = [
    'docs/NATIVE_COMPRESSION_ACTION_BOUNDARY_NOTE_2026-09-09.md',
    'docs/NATIVE_GENERALIZED_ACTION_BOUNDARY_NOTE_2026-09-09.md',
    'docs/work_history/repo/review_feedback/pr8076-evidence/README.md',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-AFFECTED_CANONICAL_REVIEW-a69223d0da5b42d4.md',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-ARCHIVE_MANIFEST-b4e1a3f6a8213320.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-ARTIFACT_PLAN-5a8a2b441ec1dded.md',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-ASSUMPTIONS_AND_IMPORTS-04947ad72d106df1.md',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-CHECKPOINT75_MANIFEST-f840e9fe13175bed.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-CHECKPOINT75_RECOVERY-423f515f978324d3.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-CLAIM_STATUS_CERTIFICATE-4a3d4f79e164376b.md',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-COMPACT_CONTROLS-a781933369788c3e.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-COMPACT_INPUTS-a908e6d1240c1319.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-COMPACT_RESULT-0991bf261e4a918b.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-DELIVERY_FREEZE-49f85f2f2ce6e6cc.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-DELIVERY_REVIEW-a70a576883bc78bc.md',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-EXACT_SUMMARY-3c08ca146e7464ff.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-GENERALIZED_ACTIVATION_REVIEW-2f16a7adb6adc6c6.md',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-GENERALIZED_ORBIT_0-39124561f48962a5.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-GENERALIZED_ORBIT_1-bf2603bfa7167fd1.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-GENERALIZED_ORBIT_2-1068cd2a789503d9.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-GENERALIZED_ORBIT_3-d5f8d854692b3b5b.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-GENERALIZED_ORBIT_4-29b4350727330f3c.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-GENERALIZED_POST-9a512ec93205dd33.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-GENERALIZED_PROOF-f9142216104fbcb0.md',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-GENERALIZED_ROOT-595ef6ddd27cd3a0.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-GENERALIZED_ROOT_FREEZE-97adb712640d0f8d.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-GENERALIZED_RUNTIME_FREEZE-27cf521dcb938fd0.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-GENERALIZED_SAVED_RESULT-b0f27866a88e04c4.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-GENERALIZED_SAVED_SOURCE_REVIEW-79313fcbd4597019.md',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-GENERALIZED_SOURCE_REVIEW-d24c5ba969d0943f.md',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-GOAL-525566f7a8b7cb8d.md',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-GRAPH_BUILD-2c668d4b2b1b9e52.stdout',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-GRAPH_BUILD-e21baa34344cdb20.stderr',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-GRAPH_MANIFEST-6ac2e699fae742ba.stdout',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-GRAPH_MANIFEST-7fc2c579251ec147.stderr',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-GRAPH_NODE-54f4b6d36fe75849.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-HANDOFF-9ef67db77ea9ef6f.md',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-LITERATURE_BRIDGES-ae1d413e72d87337.md',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-NO_GO_LEDGER-47d6880ce44b1ce7.md',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-OPPORTUNITY_QUEUE-ccb74c0b7866140d.md',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-OUTPUT_CURRENT-d38ed0200f51892f.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-PLATFORM_RUNTIME_PINS-470525051fd7660d.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-PR_BACKLOG-b978f18b90eeb9e7.md',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-RECOVERY_STATUS-85b307118d92c396.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-REMOTE_RECOVERY_MAP-6549434afacfda1c.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-REVIEW_HISTORY-3f4cb79c836849bf.md',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-ROOT_CANONICAL_REVIEW-5917e9ee6e408854.md',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-ROOT_CONTROLS-255d574011c65568.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-ROUTE_PORTFOLIO-026cc4e1e794b8fa.md',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-SELECTED_POST-bb25d287d89d386e.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-SELECTED_PROOF-2fa263725d4e7345.md',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-SELECTED_ROOT-dc8ad4e4ebd36c7e.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-SELECTED_ROOT_FREEZE-5cf36710a883d6d9.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-SELECTED_RUNTIME_FREEZE-08ac0f5b0cb3ac09.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-SOURCE_FREEZE-a1812fa3f1e28a8f.json',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-STATE-3b9688acc891237e.yaml',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-STATUS-6c33a39439907887.md',
    'docs/work_history/repo/review_feedback/pr8076-evidence/kept/pr8076-TRACE_GATE-f67515f6cce5b41d.md',
    'outputs/native_generalized_action_boundary_2026_09_09_inputs/PATH_MAP.json',
]
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
PACKET_PREFIX='.claude/science/physics-loops/native-generalized-action-boundary-20260909'
PATH_MAP=json.loads((ROOT/'outputs/native_generalized_action_boundary_2026_09_09_inputs/PATH_MAP.json').read_text())
def original_path(name):
 return ROOT/PATH_MAP.get(name,name)
def packet(name):
 return original_path(PACKET_PREFIX+'/'+name)

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--json',action='store_true');args=ap.parse_args();d=json.loads((packet('EXACT_SUMMARY.json')).read_text());n=0
 def check(x):
  nonlocal n
  if not x:raise ValueError('compact predicate '+str(n))
  n+=1
 root=json.loads((packet('receipts/SELECTED_ROOT.json')).read_text());check(d['selected']==root['orbits'])
 archive=json.loads((packet('ARCHIVE_MANIFEST.json')).read_text())['inputs']
 original=[]
 for i in range(5):
  source=json.loads((packet(f'receipts/GENERALIZED_ORBIT_{i}.json')).read_text())
  check(hashlib.sha256((packet(f'receipts/GENERALIZED_ORBIT_{i}.json')).read_bytes()).hexdigest()==archive[f'/private/tmp/toe-24h-probes-20260908/native-coordinate-free-run-prospective/ORBIT_{i}/RESULT.json'])
  check(source['status']=='COMPLETE_SOURCE_ONLY_ALGEBRA' and len(source['results'])==2 and source['C_width_gate_required']is False)
  for imp,v in zip((399,400),source['results']):original.append({'orbit':i,'impurity':imp,**v})
 check(d['generalized']==original)
 post=json.loads((packet('receipts/GENERALIZED_POST.json')).read_text());saved=json.loads((packet('receipts/GENERALIZED_SAVED_RESULT.json')).read_text())
 digest=lambda x:hashlib.sha256(x.read_bytes()).hexdigest()
 check(post['status']=='ACCEPTED_FIRST_GENERALIZED_24_ACTION_AND_ALL_SAVED_STAGES');check(post['post_result_sha256']==digest(packet('receipts/GENERALIZED_SAVED_RESULT.json')));check(post['original_root_acceptance_sha256']==digest(packet('receipts/GENERALIZED_ROOT.json')));check(post['native_entry_truth_inherited']is True);check(len(saved['rows'])==5)
 compact=json.loads((packet('COMPACT_INPUTS.json')).read_text())
 for name,h in compact.items():check(digest(packet(name))==h)
 recovery=json.loads((packet('REMOTE_RECOVERY_MAP.json')).read_text());platform=json.loads((packet('PLATFORM_RUNTIME_PINS.json')).read_text())['inputs']
 check(not recovery['unmapped']);check(set(archive)==set(recovery['mapped'])|set(platform));check(not(set(recovery['mapped'])&set(platform)))
 for original,entry in recovery['mapped'].items():check(entry['sha256']==archive[original] and len(entry['commit'])==40 and entry['path'].startswith('.claude/science/physics-loops/'))
 selected_post=json.loads((packet('receipts/SELECTED_POST.json')).read_text());generalized_root=json.loads((packet('receipts/GENERALIZED_ROOT.json')).read_text())
 check(selected_post['status']=='ACCEPTED_DIRECT_SELECTED_PRINCIPAL_AND_SAVED_MATRICES');check(selected_post['original_root_acceptance_sha256']==digest(packet('receipts/SELECTED_ROOT.json')));check(selected_post['result_sha256']==root['result_sha256'])
 check(post['result_sha256']==generalized_root['result_sha256']);check(post['worker_freeze']==generalized_root['worker_freeze']);check(post['root_freeze']==generalized_root['root_freeze'])
 check(len(d['selected'])==5);check(len(d['generalized'])==10)
 for i,r in enumerate(d['selected']):
  check(type(r['orbit'])is int and r['orbit']==i);check(0<=F(r['e'])<F(8,10**6));check(r['width_pass']is False);check(r['l1_pass']is True)
 for j,r in enumerate(d['generalized']):
  check((r['orbit'],r['impurity'])==(j//2,(399,400)[j%2]));check(r['status']=='CERTIFIED_GENERALIZED_LEAKAGE_BOUND');check(F(r['delta_squared_lower'])>F(53,100));check(F(r['delta_squared_upper'])>=F(r['delta_squared_lower']));check(r['target_excluded']is True);check(r['leakage_pass']is False);check(F(r['target_squared'])==F(1,10**12))
 # W=(2,0), K=[[0,-3],[3,0]]. H=4,A=0,Z=36; normalized leakage9.
 H,A,Z=F(4),F(0),F(36);N=Z+A*A/H;check(N/H==9);check(N>=0)
 result={'status':'PASS_COMPACT_EXACT_SUPPORT','predicates':n,'native_matrix_replay':False,'generalized_saved_post':d['generalized_saved_post']}
 (ROOT/'outputs/native_generalized_action_boundary_2026_09_09.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print(json.dumps(result,sort_keys=True))
 print(f'TOTAL: PASS={n} FAIL=0')
 print('per_element: saved rational lower-bound fields and a tiny Schur example checked; original matrix arithmetic not rerun')
 print('per_site: no sitewise physical calculation performed in this compact evidence verifier')
 print('per_mode: fixed paired trial-space rank and target fields checked; no full-band computation performed')
 print('per_block: five selected spaces and ten impurity outcomes checked against immutable historical source identities')
 print('lattice_wide: supplied fixed-family boundary only; arbitrary trial spaces and physical impossibility are not asserted')
if __name__=='__main__':main()
