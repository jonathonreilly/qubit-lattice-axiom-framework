from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
Q=Path(__file__).resolve().parent;N=Q.parent;A=N/'mass_scaled_transport_root_candidate';V=N/'mass_scaled_transport_decisive_check';W=N.parent/'correlation_worktree'
def read(p):return json.loads(Path(p).read_text())
def pin(p):
 p=Path(p);b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def same(p,r):
 a=pin(p);assert a['bytes']==r['bytes'] and a['sha256']==r['sha256'],str(p)
assert pin(V/'FINAL_FREEZE.json')['sha256']=='7032c75133b61287fa22da90149a6e04654d7810cc584e76b83d90613610920b'
f=read(V/'FINAL_FREEZE.json');actual={str(p.relative_to(V)) for p in V.rglob('*') if p.is_file()}
assert actual=={r['path'] for r in f['files']}|{'FINAL_FREEZE.json'}
for r in f['files']:same(V/r['path'],r)
assert pin(A/'DERIVATION.md')['sha256']=='785e56e3f8e667750b1f54da8963274096ac3ddac9fb8c56db3d6460846773e7'
assert pin(V/'REPORT.md')['sha256']=='cc5670ba9d6da565d75efb7bf70f7fc5d39f677a129cd2d1b744cc529b7b106e'
proposal=read(A/'PROPOSAL_FREEZE.json');same(A/'DERIVATION.md',proposal['source'])
m=read(V/'SOURCE_MANIFEST.json');copies=0
for r in m['sources']:
 same(r['path'],r)
 if r['recovery_copy']:same(V/r['recovery_copy'],r);copies+=1
receipts=[]
for label in ['capture','final']:
 folder=V/'metadata_runs'/label;l=read(folder/'LAUNCH.json');r=read(folder/'EXECUTION.json')
 assert r['returncode']==0 and l['scientific_execution'] is False
 same(folder/'LAUNCH.json',r['launch']);same(folder/'child_source.py',l['source_at_launch']);same(folder/'recorder_source.py',l['recorder_at_launch'])
 same(l['source_at_launch']['path'],l['source_at_launch']);same(l['recorder_at_launch']['path'],l['recorder_at_launch'])
 for o in r['outputs']:same(o['path'],o)
 receipts.append({'launch':pin(folder/'LAUNCH.json'),'receipt':pin(folder/'EXECUTION.json'),'start':l['launched_utc'],'end':r['finished_utc']})
fresh=read(V/'FINAL_SOURCE_RECHECK.json')
for r in fresh['sources']+[fresh['report'],fresh['coverage']]:same(r['path'],r)
seal=read(V/'SEAL_RECEIPT.json');same(V/seal['source_at_launch']['path'],seal['source_at_launch']);same(V/seal['preseal_metadata_execution']['path'],seal['preseal_metadata_execution'])
parent=W/'docs/NEAREST_NEIGHBOR_SHARED_MEDIATOR_PROGRAMMING_BOUNDED_THEOREM_NOTE_2026-10-15.md';assert pin(parent)['sha256']=='68f0ee48bc27f86fabb19f1920cd63f8ea829b716c2fde043fe68001aa6e5649'
raw=(N/'local_clock_single_port_mediator_candidate/DERIVATION.md').read_bytes();assert parent.read_bytes().count(raw)==1
r={'utc':datetime.now(timezone.utc).isoformat(),'candidate':pin(A/'DERIVATION.md'),'proposal_freeze':pin(A/'PROPOSAL_FREEZE.json'),'review':pin(V/'REPORT.md'),'review_freeze':pin(V/'FINAL_FREEZE.json'),'review_members_verified':len(f['files']),'live_sources_verified':len(m['sources']),'recovery_copies_verified':copies,'actual_metadata_receipts':receipts,'canonical_parent':pin(parent),'exact_parent_body_present':True,'acceptance':pin(Q/'ACCEPTANCE.md'),'root_scientific_executions':0,'scope':'Source and actual receipt closure only. Analytic disposition and its qualifications are in ACCEPTANCE.md; no audit.'}
(Q/'SOURCE_CLOSURE.json').write_text(json.dumps(r,indent=2)+'\n')
rows=[{**pin(p),'path':str(p.relative_to(Q))} for p in sorted(Q.rglob('*')) if p.is_file() and p!=Q/'FINAL_FREEZE.json']
(Q/'FINAL_FREEZE.json').write_text(json.dumps({'frozen_utc':datetime.now(timezone.utc).isoformat(),'status':'Conditional source acceptance for regular milestone review; no audit','files':rows},indent=2)+'\n')
print(json.dumps({'acceptance':pin(Q/'ACCEPTANCE.md'),'closure':pin(Q/'SOURCE_CLOSURE.json'),'freeze':pin(Q/'FINAL_FREEZE.json'),'science_executions':0}))
