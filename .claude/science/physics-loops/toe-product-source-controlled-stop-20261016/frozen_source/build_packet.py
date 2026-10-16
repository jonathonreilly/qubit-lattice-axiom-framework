"""Assemble an unapproved source-only proposal; no scientific execution."""
from pathlib import Path
import hashlib,json,difflib,datetime
D=Path(__file__).resolve().parent;N=D.parent
NOTE='proposal/docs/PRODUCT_SOURCE_CONTROLLED_STOP_BOUNDED_THEOREM_NOTE_2026-10-16.md'
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def write(rel,b):
 p=D/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b if isinstance(b,bytes) else b.encode())
def js(rel,x):write(rel,json.dumps(x,indent=2)+'\n')
expected={
'BOUNDED_SLEW_INSTALLATION_ADDENDUM.md':'47a40af19554e87c7d4f1af4ce034487b8d63c0b3bb032a3f15f4ee1eda414e6',
'INSTALLATION_WORK_ADDENDUM.md':'398ddef66cd7965c687882f4a356170863723a096978b89346b7cb5e008c546f',
'EXTERNAL_STOP_AND_WORK_RETURN_ADDENDUM.md':'18cd2458fc84e1132c2b31b3774e64d4c5f6f4d4389e283130d7deccc7007ce0',
'C1_MINIMUM_DURATION_RAMPS_ADDENDUM.md':'212571bcf9ed6837808f6d8347eb0c74ef1fab394b6672658018a27ba561d15b'}
reviews=['installation','installation_work','external_stop','c1_ramps']
review_hashes=['dc3f2e653f5df472c7440d37def34db1545d34334d2d86f4ee01be4fced89b15','81f1914b3ab465f6c230725827d09bbf60f3afd5f9218dba219cf4686dd2411a','57f52ff14bec371aaafcb6afa6c20742d228947d9a0fcd676b85b74b588c9def','5b4e50abaf3150c3089cc40e377f381659f21ffe89426c5ee2842032e90e331b']
roots=['product_source_mediator_installation_work_root_review','product_source_mediator_stop_c1_root_review']
root_hashes=['43ab4e6cdd919c5d214d92bef15f398cd7aaf57d0eeb598bc7448cce55e8a977','218ddfbed74e18f18dc30c8103a6a10acadb7a50daeb0d10dd0ee5f4e207ab9a']
body_sources=[('author_'+k,str(N/'product_source_mediator_candidate'/k),h) for k,h in expected.items()]
body_sources += [('review_'+r,str(N/f'product_source_mediator_{r}_exposed_check/REVIEW.md'),h) for r,h in zip(reviews,review_hashes)]
body_sources += [('controlling_'+r,str(N/r/'QUALIFICATION.md'),h) for r,h in zip(roots,root_hashes)]
raw=(D/'wrapper.md').read_bytes();bodies=[]
for label,path,h in body_sources:
 b=Path(path).read_bytes();assert ident(b)['sha256']==h,path
 raw+=f'\n\n<!-- Complete unchanged body: {label} -->\n\n'.encode();start=len(raw);line=raw.count(b'\n')+1;raw+=b
 bodies.append(dict(label=label,original=path,**ident(b),start_byte=start,end_byte=len(raw),start_line=line,end_line=line+b.count(b'\n')-1,read_coverage='complete changed argument read'))
write(NOTE,raw)
evidence=[]
def capture(path,role):
 p=Path(path);b=p.read_bytes();i=ident(b);rel='evidence/'+i['sha256'];write(rel,b)
 row=dict(original=str(p),capture=rel,role=role,**i);evidence.append(row);return row
hist=[];selected_freezes=[]
for name in reviews:
 p=N/f'product_source_mediator_{name}_exposed_check'
 for rel in ['FREEZE.json','SOURCE_MANIFEST.json','SOURCE_COVERAGE.md','metadata/EXECUTION.json','inspect_sources.py','record_metadata.py','metadata/executed_source.py','metadata/launcher_source.py','metadata/stdout','metadata/stderr']:
  capture(p/rel,f'{name}:{rel}')
 selected_freezes.append(str(p/'FREEZE.json'))
 hist.append(dict(kind='exposed_review_metadata_v1',directory=str(p),receipt=str(p/'metadata/EXECUTION.json')))
capture(N/'product_source_mediator_external_stop_exposed_check/ROOT_CONTEXT_MESSAGE.txt','attributed_tail_context')
for name in roots:
 for rel in ['ACCEPTANCE.json','FREEZE.json']:capture(N/name/rel,f'{name}:{rel}')
 selected_freezes.append(str(N/name/'FREEZE.json'))
for name in ['product_installation_work_root_acceptance','product_stop_c1_root_acceptance']:
 p=N/'runs'/name;e=json.loads((p/'EXECUTION.json').read_bytes())
 for rel in ['EXECUTION.json','executed_source.py','stdout','stderr']:capture(p/rel,f'{name}:{rel}')
 capture(e['child_source_at_launch']['path'],f'{name}:original_child');capture(e['recorder']['path'],f'{name}:recorder')
 hist.append(dict(kind='root_metadata_v1',directory=str(p),receipt=str(p/'EXECUTION.json')))
for rel in ['PUBLICATION.json','ATTACHMENT.json']:capture(N/'publication_integration/product_source'/rel,'parent_'+rel)
parent=N/'publication_integration/product_source/canonical_source/docs/PRODUCT_SOURCE_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-16.md'
b=parent.read_bytes();assert ident(b)==dict(bytes=63977,sha256='4e68ea3c55620eb0ad3c721084780d2af44bc5eaa249cb8c205e516575189d20')
manifest=dict(schema='product_source_controlled_stop_source_only_v1',assembled_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),note=dict(path=NOTE,**ident(raw)),bodies=bodies,evidence=evidence,historical_runs=hist,selected_freezes=selected_freezes,direct_parent=dict(path=str(parent),**ident(b),read_coverage='complete canonical note, lines 1 through end; necessary source/static/rounding/Pauli premises and qualifications read',copied=False),source_decisions=dict(installation_work=str(N/roots[0]/'ACCEPTANCE.json'),stop_c1=str(N/roots[1]/'ACCEPTANCE.json')),integration=dict(wrapper_root_approval=None,selected_base=None,canonical_body_map=None,canonical_execution=None,staged_review=None,publication=None,retained_audit=None),scientific_executions=0,editable_prompt_files_changed=[])
js('INPUT_MANIFEST.json',manifest);js('BODY_MAP.json',bodies)
write('UNCHANGED_BODY_DIFFS.txt',''.join(f'{r["label"]}: byte-identical, {r["bytes"]} bytes, SHA256 {r["sha256"]}; no source diff.\n' for r in bodies))
print(json.dumps(dict(note=manifest['note'],bodies=len(bodies),evidence_aliases=len(evidence),unique_evidence_blobs=len({r['capture'] for r in evidence}),scientific_executions=0)))
