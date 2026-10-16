#!/usr/bin/env python3
"""Exact source capture only; no scientific computation."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent
W=BASE.parent/'correlation_worktree'
SPECS=[
 ('candidate',BASE/'mass_scaled_transport_root_candidate/DERIVATION.md','785e56e3f8e667750b1f54da8963274096ac3ddac9fb8c56db3d6460846773e7','DERIVATION.md'),
 ('candidate proposal freeze',BASE/'mass_scaled_transport_root_candidate/PROPOSAL_FREEZE.json',None,'PROPOSAL_FREEZE.json'),
 ('single-port mathematical parent',BASE/'local_clock_single_port_mediator_candidate/DERIVATION.md','d4ed04f737c418cd951d9c736a81785863e09b0031a3ffaecf2c02233f1f3d25','single_port_DERIVATION.md'),
 ('separate single-port source-exposed assessment',BASE/'local_clock_single_port_mediator_decisive_check/REPORT.md','081d9eb9f65993fcaf11caa0c984e194a861ba5993a5bd92890d4e5e67edebf0','single_port_REPORT.md'),
 ('root single-port source acceptance',BASE/'single_port_mediator_root_review/ACCEPTANCE.md','374139d56c7217ab52c59b1f94fcec8808fc29a1753fadc2428bf39de1009ec4','single_port_ROOT_ACCEPTANCE.md'),
 ('root single-port freeze',BASE/'single_port_mediator_root_review/FINAL_FREEZE.json',None,'single_port_ROOT_FINAL_FREEZE.json'),
 ('exact original geometry',BASE/'local_clock_routed_auxiliary_preparation_candidate/sources/geometry_reservoir.md','26220ec995a93bd6af725a6b3463d0b676b9d8a864b4867459bef7dd9560e9b4','geometry_reservoir.md'),
 ('exact original memory geometry',BASE/'local_clock_routed_auxiliary_preparation_candidate/sources/geometry_memory.md','f38d4590d700db0ce12c491c4e2c21a7843207d226b74089b537519acbd5a86a','geometry_memory.md'),
 ('this worker prior geometry coverage, not new independence',BASE/'local_clock_routed_auxiliary_preparation_decisive_check/REPORT.md','fa97db9c1922c56e757de800b1f84095ea6abe229ce412c7c70280a3c520ae59',None),
 ('previously read instructions',W/'AGENTS.md','f9a7b41213cee9ff0b7e9a28f79b555c152de52ef012ff3bcdd09b996d3aa32f',None),
 ('previously read workflow',W/'docs/ai_methodology/SCIENCE_WORKFLOW.md','05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce',None),
 ('previously read reviewer skill',Path('/Users/jonreilly/.codex/skills/physics-claim-reviewer/SKILL.md'),'9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455',None)
]
rows=[]
for role,p,expected,copy in SPECS:
    b=p.read_bytes(); sha=hashlib.sha256(b).hexdigest()
    if expected is not None: assert sha==expected,str(p)
    row={'role':role,'path':str(p),'bytes':len(b),'sha256':sha,'recovery_copy':None}
    if copy:
        target=ROOT/'sources'/copy
        target.parent.mkdir(parents=True,exist_ok=True); target.write_bytes(b)
        row['recovery_copy']=str(target.relative_to(ROOT))
    rows.append(row)
proposal=json.loads((ROOT/'sources/PROPOSAL_FREEZE.json').read_text())
assert proposal['source']['sha256']==rows[0]['sha256'] and proposal['source']['bytes']==rows[0]['bytes']
assert proposal['source_dependency_sha256']==rows[2]['sha256']
(ROOT/'SOURCE_MANIFEST.json').write_text(json.dumps({'scope':'Exact source identities and role-limited reuse; no scientific run.','sources':rows},indent=2)+'\n')
print(json.dumps({'sources':len(rows),'recovery_copies':sum(r['recovery_copy'] is not None for r in rows),'candidate':rows[0],'proposal_freeze':rows[1],'scientific_execution':False},indent=2))
