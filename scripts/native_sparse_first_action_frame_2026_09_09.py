#!/usr/bin/env python3
"""Portable small exact supporting controls; no native arrays or runtime imports."""
from pathlib import Path

AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = [
    'docs/NATIVE_CERTIFIED_LOCAL_GREEN_SCALARS_NOTE_2026-09-09.md',
    'docs/NATIVE_FINITE_EXCITATION_WARD_NOTE_2026-09-09.md',
    'docs/NATIVE_GAPFREE_GENERATOR_PROPAGATION_NOTE_2026-09-09.md',
    'docs/NATIVE_SPARSE_FIRST_ACTION_FRAME_NOTE_2026-09-09.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/README.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-ARTIFACT_PLAN-5a8a2b441ec1dded.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-ASSUMPTIONS_AND_IMPORTS-04947ad72d106df1.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-CHANGE-9882317dd4815aec.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-CLAIM_STATUS_CERTIFICATE-4a3d4f79e164376b.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-CLAIM_STATUS_CERTIFICATE-d91542b92d1821e4.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-COEFFICIENT_PROOF-f79d784bd37b2517.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-DELIVERY_DELTA-d6a894e023ab00c5.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-DELIVERY_FREEZE-49f85f2f2ce6e6cc.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-DELTA-fc67dbfada0640c8.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-DERIVATION-a1006d177b1932e1.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-DERIVATION-cbf75f163032220a.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-DERIVATION-dddfe10d36a12c86.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-FAILURE-206cf484ef15dc83.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-FAILURE_HISTORY-3147455df0646174.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-FREEZE-1f20355da2379ec3.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-FREEZE-2593696b5b90780d.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-FREEZE-578e426608c6598e.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-FREEZE-94c8be13820787c1.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-FREEZE-b599932f76ef0195.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-FREEZE-f0f7bbffadc196e8.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-FREEZE-f3173bd2aabad98a.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-GOAL-525566f7a8b7cb8d.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-HANDOFF-5c7aff5f88361fea.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-HANDOFF-9ef67db77ea9ef6f.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-INPUTS-3a4ca41d8ba01c1d.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-INPUTS-a95b7db693b31df3.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-LITERATURE_BRIDGES-ae1d413e72d87337.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-MUTANTS-881a2dff3832d67a.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-NATIVE_SPARSE_FIRST_ACTION_FRAME_NOTE_2026-09-09-e7353d75fc9b51ee.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-NO_GO_LEDGER-47d6880ce44b1ce7.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-OPPORTUNITY_QUEUE-ccb74c0b7866140d.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-OUTPUT-265f6c06af9bd88c.txt',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-PINS-dc862d976f0d0c23.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-PROTOCOL-4f091956468a5960.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-PROTOCOL-b026b9d068e72bdc.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-PR_BACKLOG-09530898efa27c80.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-PR_BACKLOG-b978f18b90eeb9e7.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-RESULT-107593bda5ddbbf5.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-RESULT-5f5f245505478315.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-RESULT-9de9eff9bc698696.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-RESULT-d8ad03585ad60332.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-REVIEW-451b0613f6d69871.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-REVIEW-532082e43228e01d.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-REVIEW-5dc162cade318838.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-REVIEW-674a23e4d73876b4.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-REVIEW-8d6e5e63b6a9ab14.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-REVIEW_HISTORY-2bbf33a3a9724ebb.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-REVIEW_HISTORY-3f4cb79c836849bf.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-ROOT_DELIVERY-309073da3de77db5.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-ROUTE_PORTFOLIO-026cc4e1e794b8fa.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-SOURCE_FREEZE-003a6d6160d8635f.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-SOURCE_FREEZE-519816765e8e61c9.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-SOURCE_FREEZE-a1812fa3f1e28a8f.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-SOURCE_FREEZE-f88a96c21856b2ad.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-SOURCE_RECOVERY-cb0c9915277cc302.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-SPARSE_ACTION_PROOF-239633707463d370.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-STATE-3b9688acc891237e.yaml',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-STATE-99e5b99424eabcfc.yaml',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-STDERR-6780922888323dc5.txt',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-STDERR-6b23c7140d3e3358.txt',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-TRACE_GATE-f67515f6cce5b41d.md',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-adapter-b549b41150971101.py',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-binder-8918d9060f54e320.py',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-binder-cc7704fa830e10f9.py',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-check-2228efb35f40482c.py',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-check-b44f8b1ce1703ee5.py',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-core-b3fac077d8897fbd.py',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-core-ee0af6f1d4cee8c2.py',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-interval-29ce5f30b8919e2a.py',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-interval-4105fa9c873bb99c.py',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-native-fixed192-compression-pilot-run-c43__RESULT-63849cf2d5f9d645.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-native-fixed192-compression-pilot-run-c43__WORKER_COMPLETE-65cff83a94779046.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-native-fixed192-compression-root-review__ROOT_ACCEPTANCE-d893a468c0343f05.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-native-minimal-first-action-append-root-review__ROOT_ACCEPTANCE-a06e30e2b75e47c2.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-native-minimal-first-action-append-run-5dff__RESULT-45946753cd9ce2ec.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-native-minimal-first-action-append-run-5dff__WORKER_COMPLETE-a74a4e77d01fdede.json',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-native_sparse_first_action_frame_2026_09_09-472f4e4316dd5e2a.py',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-old_reader-15230d57416b27c8.py',
    'docs/work_history/repo/review_feedback/pr8073-evidence/kept/pr8073-worker-1dae40c4d350ad84.py',
    'outputs/native_sparse_first_action_frame_2026_09_09_inputs/CURRENT_INPUTS.json',
    'outputs/native_sparse_first_action_frame_2026_09_09_inputs/PATH_MAP.json',
]
from fractions import Fraction as F
import argparse,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
PACKET_PREFIX='.claude/science/physics-loops/native-sparse-first-action-frame-20260909'
PATH_MAP=json.loads((ROOT/'outputs/native_sparse_first_action_frame_2026_09_09_inputs/PATH_MAP.json').read_text())
def original_path(name):
 return ROOT/PATH_MAP.get(name,name)
def packet(name):
 return original_path(PACKET_PREFIX+'/'+name)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--json',action='store_true');ap.parse_args();n=0
 def ck(x,why):
  nonlocal n
  if not x:raise ValueError(why)
  n+=1
 manifest=json.loads((ROOT/'outputs/native_sparse_first_action_frame_2026_09_09_inputs/CURRENT_INPUTS.json').read_text())
 for p,h in manifest.items():ck(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'source pin '+p)
 def dot(a,b):return sum((x*y for x,y in zip(a,b)),F())
 def gamma(v):return [-v[1],v[0],-v[3],v[2]]
 e=[F(1),F(0),F(0),F(0)];seed=[F(0),F(1),F(1),F(0)]
 # j=<e,Gamma seed>=-1, hence residual=seed+Gamma(e)*j.
 j=dot(e,gamma(seed));res=[seed[k]+gamma(e)[k]*j for k in range(4)]
 ck(res==[0,0,1,0],'paired J sign');ck(dot(e,res)==dot(gamma(e),res)==0,'paired projection')
 for v in (e,seed,res):ck(gamma(gamma(v))==[-x for x in v],'Gamma square')
 # Independent seven-site matrices and three-source self Gram.
 signs=[0,1,-1,1,-1,1,-1]
 reps=(((1,2),(3,4)),((1,2),(3,5)),((1,3),(5,6)),((1,3),(2,4)),((1,3),(2,5)))
 for aa,cc in reps:
  vectors=[[F(signs[j] if j in ids else 0) for j in range(7)] for ids in (aa,cc,range(1,7))]
  gram=[[dot(u,v)/4 for v in vectors] for u in vectors]
  ck(gram==[[F(1,2),0,F(1,2)],[0,F(1,2),F(1,2)],[F(1,2),F(1,2),F(3,2)]],'self Gram')
  ck(2*sum(gram[i][i] for i in range(3))==5,'DATA added trace')
  for u,target in zip(vectors,(2,2,6)):
   t=sum(u[j]*signs[j] for j in range(1,7));ck(t==target,'T orientation');ck(-F(12,5)*t/24==(-F(1,5) if target==2 else-F(3,5)),'bare center J sign')
 # On a formal orthonormal model Kx0=qD-8qA, K Gamma x0=Gamma qD.
 # This demonstrates noncommuting impurity correction without native data.
 b0=[1,-8,0];b1=[0,0,1];ck(dot(b0,b0)==65 and dot(b1,b1)==1 and dot(b0,b1)==0,'rank-two action')
 ck(399*2==798 and 402*2==804 and 4*4+8==24,'domain counts')
 ck(24*25//2==300 and 2*5*(64*16*24+64*24**2)==614400,'sparse counts')
 ck(5*(3*66*2*3+9+6)==6015 and 5*(3*(66*2+1)+3)==2010,'append census')
 result={'status':'PASS_SMALL_EXACT_SUPPORT','checks':n,'native_arrays_replayed':False,'native_leakage_computed':False,'propagation_computed':False,'alpha_computed':False,'scope':'conditional analytical closure; finite supporting controls only'}
 (ROOT/'outputs/native_sparse_first_action_frame_2026_09_09.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print(json.dumps(result,sort_keys=True));print(f'TOTAL: PASS={n} FAIL=0')
 print('per_element: exact small paired-projection, Gram and signed-source predicates executed; no native arrays replayed')
 print('per_site: seven-site synthetic source identities executed; full physical source assembly not executed')
 print('per_mode: formal rank-two action and Gamma identities checked; native propagation remains uncomputed')
 print('per_block: five declared source patterns and sparse census checked; original domain remains distinct from DATA')
 print('lattice_wide: analytical closure only; no uniform physical leakage or thermodynamic computation performed')
if __name__=='__main__':main()
