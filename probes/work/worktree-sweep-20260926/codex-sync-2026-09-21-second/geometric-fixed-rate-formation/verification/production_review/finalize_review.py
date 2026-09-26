#!/usr/bin/env python3
"""Seal this bounded review; prior seals and external evidence remain read-only."""
from pathlib import Path
import datetime,hashlib,json,sys
import numpy as np
HERE=Path(__file__).resolve().parent;RAW=HERE.parent;ROOT=RAW.parents[3]
def identity(p):
    p=Path(p);h=hashlib.sha256()
    with p.open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):h.update(block)
    return {'path':str(p),'bytes':p.stat().st_size,'sha256':h.hexdigest()}
def pinned(p,digest):
    row=identity(p);assert row['sha256']==digest;return row
def load(p):return json.loads(p.read_text())
selections=load(HERE/'SELECTION_SEAL.json');endpoints=load(HERE/'ENDPOINT_PRECOMPARISON_SEAL.json');aggregation=load(HERE/'AGGREGATION_PRECOMPARISON_SEAL.json')
for seal in [selections,endpoints,aggregation]:
    for row in seal['sources']+seal['artifacts']:assert identity(row['path'])==row
for row in endpoints['selected_archive_identities']:assert identity(row['path'])==row
auth=load(HERE/'PRODUCTION_AUTHENTICATION.json');comparison=load(HERE/'ANALYSIS_COMPARISON.json')
external=[auth[k] for k in ['manifest','summary','binary']]+comparison['analysis_sources']
for row in external:assert identity(row['path'])==row
for name in ['ENDPOINT_RUN_RECEIPT.json','AUTHENTICATION_RUN_RECEIPT.json','ANALYSIS_COMPARISON_RECEIPT.json']:
    assert load(HERE/name)['returncode']==0
assert load(HERE/'RENDER_ATTEMPT_01_RECEIPT.json')['returncode']==1
assert not comparison['findings']
prior=[
    pinned(RAW/'geometric_fixed_rate_independent/REPORT.md','fc272b01eaeb93c3e3d1b2947561376c83df94ba47153a9b4eab0ee27ce7e594'),
    pinned(RAW/'geometric_fixed_rate_independent/FINAL_SEAL.json','b3754b93fa492301d4875760c3de7cc598664530a7cf119cda91b1958f39f7fb'),
    pinned(RAW/'geometric_fixed_rate_independent/correction_ack/CORRECTION_ACK.json','3b2a7475e727ec1e8da404e973ee06ad648e842a0b916be46d1bed50cf1a6cbd'),
    pinned(RAW/'geometric_fixed_rate_independent/correction_ack/ACK_SEAL.json','c818967744a8c4d2ea982c0786637741ed42666ff3f3720ca334896a7041e54a'),
    pinned(RAW/'geometric_fixed_rate_analysis_fix/before_analyze_geometric_fixed_rate_followup.py','531c59d50c910bca28f8ae0255bc3507831ac32dc3dbd2dd011cb433bd9d557d'),
]
procedures=[
    pinned(ROOT/'AGENTS.md','9bea097b409610ed70f55f53349ce206b6df7e62c63205d7775bac9b3d10dde6'),
    pinned(ROOT/'docs/ai_methodology/SCIENCE_WORKFLOW.md','d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4'),
    pinned('/Users/jonreilly/.codex/skills/physics-claim-reviewer/SKILL.md','9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455'),
]
artifacts=[identity(p) for p in sorted(HERE.iterdir()) if p.is_file() and p.name!='FINAL_SEAL.json']
seal={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Selective production endpoint reconstruction, complete file-identity authentication and full-table point/SE aggregation; no generator replay, phase inference or formal audit.',
      'sources':selections['sources'],'production_and_analysis_metadata':external,
      'selected_archive_identities':endpoints['selected_archive_identities'],
      'full_receipt_file_inventory':auth['hash_inventory'],'receipt_identities_bound_by':identity(HERE/'PRODUCTION_AUTHENTICATION.json'),
      'prior_review_dependencies_unchanged':prior,'procedures_reused':procedures,'artifacts':artifacts,
      'staged_seals_preserved':True,'unresolved_findings':[],
      'verification':{'selected_endpoints':24,'selected_modes':384,'recorded_histories':2496,'listed_receipt_files_hashed':14976,'point_estimates':144,'standard_errors':144,'production_bootstrap_rerun':False},
      'preserved_failure':'Independent rendering checker had one extra Markdown separator cell; source and outputs were unchanged.',
      'runtime':{'python':sys.version,'numpy':np.__version__}}
(HERE/'FINAL_SEAL.json').write_text(json.dumps(seal,indent=2)+'\n')
print(json.dumps({'report':identity(HERE/'REPORT.md'),'final_seal':identity(HERE/'FINAL_SEAL.json'),
                  'counts':{k:len(seal[k]) for k in ['sources','production_and_analysis_metadata','selected_archive_identities','prior_review_dependencies_unchanged','procedures_reused','artifacts']}},indent=2))
