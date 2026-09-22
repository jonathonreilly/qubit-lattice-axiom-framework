"""Seal only this bounded comparison; preserve the already frozen PRE packet."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
HERE=Path(__file__).resolve().parent
BASE=HERE.parent
OUT=HERE/'FINAL_SEAL.json'
assert not OUT.exists(), 'Never replace an existing final seal.'
def row(path):
    p=Path(path); b=p.read_bytes()
    return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def verify(r):
    a=row(r['path']);assert a['bytes']==r['bytes'] and a['sha256']==r['sha256'],(r,a)
pre_path=HERE/'PRE_COMPARISON_SEAL.json'
author_path=BASE/'HOMOGENEOUS_CHARGED_RECORDS_AUTHOR_SEAL.json'
assert row(pre_path)['sha256']=='1678d9365ac5c3460d70a13d16b8b3fbeedd0f09b658a023c5ee515e4e213b48'
assert row(author_path)['sha256']=='ec6d68f95a67c810e442fe52d8e453183f4d9723e55e52df36a0d8010727b9b0'
pre=json.loads(pre_path.read_text());author=json.loads(author_path.read_text())
bindings={}
def add(r,role):
    verify(r)
    if r['path'] not in bindings:bindings[r['path']]={**r,'roles':[role]}
    else:
        assert bindings[r['path']]['sha256']==r['sha256']
        if role not in bindings[r['path']]['roles']:bindings[r['path']]['roles'].append(role)
for r in pre['sources']:add(r,'unchanged_PRE_dependency')
for r in pre['artifacts']:add(r,'unchanged_PRE_artifact')
for r in author['artifacts']:add(r,'authorized_author_artifact')
def context_add(obj):
    if isinstance(obj,dict):
        if {'path','bytes','sha256'}<=obj.keys():add(obj,'author_context_binding')
        else:
            for v in obj.values():context_add(v)
    elif isinstance(obj,list):
        for v in obj:context_add(v)
context_add(json.loads((BASE/'HOMOGENEOUS_CHARGED_RECORDS_SOURCE_CONTEXT.json').read_text()))
new=['COMPARISON.md','comparison_check.py','COMPARISON_RESULTS.json','COMPARISON_CHECK.stdout',
     'COMPARISON_CHECK.stderr','COMPARISON_CHECK_RECEIPT.json','seal_comparison.py']
for name in new:add(row(HERE/name),'new_bounded_comparison_evidence')
receipt=json.loads((HERE/'COMPARISON_CHECK_RECEIPT.json').read_text())
assert receipt['exit_code']==0
for k in ['runner','stdout','stderr']:verify(receipt[k])
assert (HERE/'COMPARISON_RESULTS.json').read_bytes()==(HERE/'COMPARISON_CHECK.stdout').read_bytes()
assert (HERE/'COMPARISON_CHECK.stderr').read_bytes()==b''
result=json.loads((HERE/'COMPARISON_RESULTS.json').read_text())
assert result['finding']=='No material discrepancy found in the bounded comparison.'
packet={'created_utc':datetime.now(timezone.utc).isoformat(),
    'status':'Bounded post-seal scientific comparison complete; no required source correction found. No publication or audit status.',
    'pre_seal':row(pre_path),'author_seal':row(author_path),
    'bindings':[bindings[k] for k in sorted(bindings)],
    'counts':{'listed_unique_bindings':len(bindings),'top_level_seal_identities':2,
              'all_including_top_level':len(bindings)+2,'new_comparison_files':len(new)},
    'independent_new_execution':'comparison_check.py, first execution successful; two complete guarded-square sectors, symbolic normalization, selected-edge halo count.',
    'read_coverage':'Complete bound current note, scientific scripts and results; complete relevant receipts, streams, working specification/context and preserved failed-source delta.',
    'limits':['No full author suite replay; exact author outputs were authenticated, with only two selected physical sectors rebuilt independently.',
              'No new proof imported from unrelated PR 8626 receipt; that contextual receipt was hash-authenticated only.',
              'Uniform-volume theorem is conditional on the stated dressed initial code, fourth moments, fixed local support/time and decreasing birth schedule.',
              'Charged-band/phase, finite-rate formation, checkpoint, registry and unrelated frontier sources remain unopened.'],
    'preservation':'All 28 original PRE bindings and PRE seal verified unchanged; preserved author indexing failure retained at its exact source identity.',
    'mutable_exclusion':'CHECKPOINT.md remains an unsealed recovery aid.'}
OUT.write_text(json.dumps(packet,indent=2)+'\n')
for r in packet['bindings']:verify(r)
verify(packet['pre_seal']);verify(packet['author_seal'])
print(json.dumps({'final_seal':row(OUT),'comparison':row(HERE/'COMPARISON.md'),
                  'result':row(HERE/'COMPARISON_RESULTS.json'),'counts':packet['counts'],
                  'all_bindings_reverified':True},indent=2))
