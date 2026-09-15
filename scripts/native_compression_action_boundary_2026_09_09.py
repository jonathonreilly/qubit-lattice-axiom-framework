"""Compact immutable evidence checks and tiny algebra; never a native replay."""
from pathlib import Path

AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = [
    'docs/NATIVE_COMPRESSION_ACTION_BOUNDARY_NOTE_2026-09-09.md',
    'docs/NATIVE_SPARSE_FIRST_ACTION_FRAME_NOTE_2026-09-09.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/README.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-ACCEPTED_BINDING_DELTA-546060197c0bfbdc.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-ARTIFACT_PLAN-5a8a2b441ec1dded.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-ASSUMPTIONS_AND_IMPORTS-04947ad72d106df1.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-AUTHOR_CONTROL_SOURCE-1f251857ca2c74f5.py',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-CLAIM_STATUS_CERTIFICATE-4a3d4f79e164376b.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-DELIVERY_FREEZE-49f85f2f2ce6e6cc.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-DELTA-2754b1a7e7062a9c.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-DERIVATION-bd634b82f8f13d25.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-FINAL_DELIVERY_DELTA-cde5ae7fc7f7ccc9.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-FINAL_DELTA-40fa0d67991b4400.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-FINAL_DELTA-f801a88f7f8369d7.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-FIRST-e905eeb2bb3a1c26.stdout',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-FIRST-ff679c2ed28fbf70.stderr',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-GOAL-525566f7a8b7cb8d.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-HANDOFF-9ef67db77ea9ef6f.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-INPUT_MANIFEST-0eab090f4c53089d.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-INPUT_MANIFEST-4f9e6a32101df3cc.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-INPUT_MANIFEST-fc018b2065a25394.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-LITERATURE_BRIDGES-ae1d413e72d87337.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-NOTE-cf6d3d941e925ad5.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-NOTE-cfb09dda19bef0d1.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-NO_GO_LEDGER-47d6880ce44b1ce7.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-OPPORTUNITY_QUEUE-ccb74c0b7866140d.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-PAIRED_OUTPUT-4dd4034b0fb485c8.txt',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-POST_ACCEPTANCE-024b049fa5337b92.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-POST_ACCEPTANCE-059d76942c658786.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-POST_ACCEPTANCE-7f8f79616193a50b.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-POST_ACCEPTANCE-88e81e8288bc097a.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-PROTOCOL-19dc9db4c0a20b95.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-PROTOCOL-7df9ed379810cf5a.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-PR_BACKLOG-b978f18b90eeb9e7.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-RECEIPT-1d9ba301260ad086.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-RECEIPT-3c9df52733b31177.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-RECEIPT-b19bff3cb1738f2d.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-RECEIPT-ee002596cac3f7c5.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-RECEIPT-fd7a29472ea0be86.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-RECOVERY_MANIFEST-4d62e773ceaf9a1f.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-REMOTE_PREREGISTRATION-22abe9e8a9f488f2.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-REMOTE_PREREGISTRATION-925ee50aa768a537.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-REMOTE_PREREGISTRATION-a4c902370c20cb4b.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-REMOTE_PREREGISTRATION-c88e145374539569.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-REMOTE_PREREGISTRATION-daf3aba711ab62b5.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-RESULT-063da6a7f916477f.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-RESULT-2479df11a70a9a40.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-RESULT-399670f6ce175344.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-RESULT-4246aa31762b6fe8.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-RESULT-475591080fc221e6.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-RESULT-79506b7c79187a8f.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-RESULT-bd2a107043a3cbf8.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-RESULT-d8bc57a2a03a0341.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-REVIEW-00c60e5cc7e3a6f7.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-REVIEW-17b5dba75b5a1402.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-REVIEW-2efd754f55a1b708.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-REVIEW-5a61ad6db7900a7b.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-REVIEW-94ae5224643d9067.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-REVIEW-a030e98b65d568ea.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-REVIEW-aff8156e62432075.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-REVIEW-ee7dfd87da9990ef.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-REVIEW_HISTORY-3f4cb79c836849bf.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-ROOT-38c614ca02e39e97.stderr',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-ROOT-3adcd73d63699b8a.stderr',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-ROOT-3b3ad1cb9fd578ca.stderr',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-ROOT-6ff886b08d8090a1.stderr',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-ROOT-d9a9d8b1ea91a297.stderr',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-ROOT_ACCEPTANCE-5fffd0e25fa04932.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-ROOT_ACCEPTANCE-732f741030650f50.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-ROOT_ACCEPTANCE-ca5be5043d36e4b0.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-ROOT_ACCEPTANCE-f70aed99be229130.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-ROOT_ACCEPTANCE-f7759041c1894fcf.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-ROOT_ADDENDUM-3efbdf5fe171b82a.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-ROOT_ADDENDUM-7f89fc01603db427.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-ROOT_FREEZE-271b9c1ac45aba7d.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-ROOT_FREEZE-288f0d05711f7e1f.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-ROOT_FREEZE-4505a86ec48b2c08.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-ROOT_FREEZE-6d95549cdea96fa0.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-ROOT_FREEZE-c58c9475ce62adbf.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-ROUTE_PORTFOLIO-026cc4e1e794b8fa.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-SCHEMA_ACCEPTANCE-0fd517c089c34dcc.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-SCHEMA_ACCEPTANCE-3ffad6e863c87a82.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-SCHEMA_ACCEPTANCE-6090e2036b299a10.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-SCHEMA_ACCEPTANCE-7177334f2a39ec7c.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-SCHEMA_ACCEPTANCE-8611d585c56e4e4a.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-SEMANTIC_CONTROLS-e979b89e48cdc4c2.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-SIXTIETH_SHA256-ae71bb341f9e980a.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-SIXTY_FIFTH_SHA256-5610b8b75b3a7766.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-SIXTY_FIRST_SHA256-040b713374079e5f.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-SIXTY_FOURTH_SHA256-ce8f58d3eecbce6c.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-SIXTY_SECOND_SHA256-a1d387fe12ee903f.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-SIXTY_THIRD_SHA256-bdf813e0739794d2.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-SOURCE_FREEZE-22873ae5c8866567.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-SOURCE_FREEZE-8d359175c8327933.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-SOURCE_FREEZE-a1812fa3f1e28a8f.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-STATE-3b9688acc891237e.yaml',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-TRACE_GATE-f67515f6cce5b41d.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-TYPING_DELTA-fe6573a8db6abc7f.md',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-WORKER_COMPLETE-09c978fa3dea4f9b.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-WORKER_COMPLETE-5b425a70451112ad.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-WORKER_COMPLETE-b4439e1543f5f723.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-WORKER_COMPLETE-c10c9e59c1b61515.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-WORKER_COMPLETE-d683ff187bc6fef2.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-WORKER_COMPLETE-d6f0b38ac16cfa32.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-WORKER_COMPLETE-d70594fe3e687de8.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-WORKER_COMPLETE-def155cf89de2c0c.json',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-arithmetic-8f04de0d6d6c3d8c.py',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-check-2f41f1dd5679442a.py',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-check-8c06730424d23a19.py',
    'docs/work_history/repo/review_feedback/pr8074-evidence/kept/pr8074-pre-delivery-source-freeze-f0e597864eab3d33.json',
    'outputs/native_compression_action_boundary_2026_09_09_inputs/CURRENT_INPUTS.json',
    'outputs/native_compression_action_boundary_2026_09_09_inputs/PATH_MAP.json',
]
from fractions import Fraction as F
from math import isqrt
import argparse,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
PACKET_PREFIX='.claude/science/physics-loops/native-compression-action-boundary-20260909'
PATH_MAP=json.loads((ROOT/'outputs/native_compression_action_boundary_2026_09_09_inputs/PATH_MAP.json').read_text())
def original_path(name):
 return ROOT/PATH_MAP.get(name,name)
def packet(name):
 return original_path(PACKET_PREFIX+'/'+name)

COUNT=0
def require(x,message):
 global COUNT
 if not x:raise ValueError(message)
 COUNT+=1
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(folder,name='RESULT.json'):
 return json.loads((packet('verification/evidence/'+folder+'/'+name)).read_text())
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--verify',action='store_true');ap.add_argument('--json',action='store_true');ap.parse_args()
 manifest=json.loads((ROOT/'outputs/native_compression_action_boundary_2026_09_09_inputs/CURRENT_INPUTS.json').read_text())
 for path,h in manifest['files'].items():
  p=(ROOT/path).resolve();require(ROOT in p.parents,'repository-local input');require(sha(p)==h,'source/input hash '+path)
 rec=json.loads((packet('verification/RECOVERY_MANIFEST.json')).read_text())
 require(rec['status']=='COMPACT_SNAPSHOT_WITH_REQUIRED_REMOTE_FORENSIC_RETRIEVAL','recovery scope')
 for row in rec['local_copies']:
  p=original_path(row['local_path']);require(sha(p)==row['sha256'] and p.stat().st_size==row['bytes'],'original bytes')
  require(bool(row['archive_matches']) and all(x['sha256']==row['sha256'] and len(x['commit'])==40 for x in row['archive_matches']),'durable retrieval identity')
 action=load('native-sparse-pivot-action-root-review','ROOT_ACCEPTANCE.json');post=load('native-sparse-pivot-action-root-review','POST_ACCEPTANCE.json');saved=load('native-sparse-action-saved-post-run-593b')
 require(action['status']=='ACCEPTED_COMPLETE_ORIGINAL_FOUR_PAIR_ACTION_ENCLOSURE','action status')
 require(post['result_sha256']==action['result_sha256'] and post['post_result_sha256']==sha(packet('verification/evidence/native-sparse-action-saved-post-run-593b/RESULT.json')),'action post binding')
 require(saved['events_checked']==80 and saved['native_calls']==0 and len(saved['orbits'])==5,'saved action scope')
 require(len(action['orbits'])==5,'five action orbits')
 for i,o in enumerate(action['orbits']):
  require(type(o['orbit']) is int and o['orbit']==i and len(o['impurities'])==2,'action shape')
  for a in o['impurities']:
   require(a['leakage_pass'] is False and a['certified_diagonal_exceeds_optional_target'] is True,'all ten leakage outcomes false')
   require(F(a['delta_squared_lower_from_diagonal'])>F(3,10)>F(1,10**12),'certified trial-space diagonal lower')
   require(F(a['delta_squared_upper'])>=F(a['delta_squared_lower_from_diagonal']),'action enclosure order')
 four=load('native-fixed192-compression-root-review','ROOT_ACCEPTANCE.json');twelve=load('native-compression-continuation-root-review','ROOT_ACCEPTANCE.json');twentyfour=load('native-compression-24-root-review','ROOT_ACCEPTANCE.json')
 for k,r in [(4,four),(12,twelve),(24,twentyfour)]:
  require(len(r['orbits'])==5,'compression orbit census')
  for i,o in enumerate(r['orbits']):require(type(o['orbit']) is int and o['orbit']==i and o['pairs']==k and o['residual_pass'] is False and o['coordinate_pass'] is True,'fixed cap outcomes')
 for o in twentyfour['orbits']:
  require(F(o['raw_residual_upper'])>F(1,1062*10**6),'24 residual target remains unmet')
  require(F(o['coordinate_radius_squared'])<=F(1,40000**2),'24 coordinate target')
 for folder,h,c,n in [('native-compression-twelve-saved-post-run-02ca',40,271320,342930),('native-compression-24-saved-post-run-8522',60,885780,983426)]:
  p=load(folder);require(p['histories']==h and p['coordinates']==c and p['predicates']==n,'saved continuation scope')
 diag=load('native-fresh-pivot-width-run');dr=load('native-fresh-pivot-width-root-review','ROOT_ACCEPTANCE.json')
 require(diag['status']=='COMPLETE_SAVED_SCALAR_DIAGNOSTIC' and dr['result_sha256']==sha(packet('verification/evidence/native-fresh-pivot-width-run/RESULT.json')),'fresh result identity')
 rows=diag['rows'];require(len(rows)==78 and len(diag['forced_blockers'])==53,'fresh coverage')
 require(len({(x['orbit'],x['row']) for x in rows})==78,'unique fresh rows')
 first=[]
 for i in range(5):
  r=[x for x in rows if x['orbit']==i and x['must_fail_width']];require(bool(r),'orbit blocker')
  x=min(r,key=lambda x:x['row']);first.append(x['row']+1)
  require(F(x['exact_image_width_lower_bound'])>F(1,2**39),'exact image obstruction')
 for x in rows:
  require(x['threshold']==2**192//2**39 and x['width']==x['forced_upper']-x['forced_lower'],'saved scalar arithmetic metadata')
  require(x['must_fail_width']==(x['width']>x['threshold']),'saved width flag')
 require(first==[7,8,8,8,9],'one-based fresh witnesses')
 # Tiny independent scalar-width examples; no saved pivot r is recomputed.
 for a,b in [(1,2),(2,3),(3,7)]:
  l,u=F(a*a),F(b*b);w=1/(2*F(a))-1/(2*F(b));require(w==(u-l)/(2*a*b*(a+b)),'rationalized width')
  require(w>=(u-l)/(4*u*b),'width lower bound')
 S=2**16;l=S;u=4*S;lo=S*S//(2*isqrt(u*S));hi=-((-S*S)//(2*isqrt(l*S)))
 require((lo,hi)==(S//4,S//2),'toy directed endpoints')
 print('per_element: compact saved scalar witnesses and ten diagonal lower bounds checked; original numerical arithmetic not re-executed')
 print('per_site: checked and not executed — no sitewise physical assertion in this block')
 print('per_mode: checked and not executed — no full-band mode or propagation computation')
 print('per_block: five fixed compression orbits and ten four-pair action outcomes checked against immutable receipts')
 print('lattice_wide: checked and not executed — supplied-model implementation boundary, no physical no-go')
 result={'status':'PASS_COMPACT_BOUNDARY_EVIDENCE','checks':COUNT,'fresh_first_pairs':first,'native_calls':0,'saved_physics_replays':0,'original_snapshot_required_remote_retrieval':True,'recovery_archive_bundled':True}
 (ROOT/'outputs/native_compression_action_boundary_2026_09_09.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print(json.dumps(result,sort_keys=True))
 print(f'TOTAL: PASS={COUNT} FAIL=0')
if __name__=='__main__':main()
