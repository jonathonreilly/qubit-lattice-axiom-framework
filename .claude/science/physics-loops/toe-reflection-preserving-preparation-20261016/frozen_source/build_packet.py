"""Build only the scoped source publication proposal; no science, Git or canonical writes."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
D=Path(sys.argv[1]).resolve();N=D.parent;P=D/'proposal'
plan=json.loads((D/'SOURCE_PLAN.json').read_text());PK=plan['packet'];NOTE=plan['note'];SCRIPT=plan['script']
sha=lambda b:hashlib.sha256(b).hexdigest()
def put(rel,b):
 p=P/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
def js(rel,x):put(rel,(json.dumps(x,indent=2)+'\n').encode())
def ident(b):return {'bytes':len(b),'sha256':sha(b)}
sources={};objects={};freeze_rows=[]
def add(path,alias=None,role='historical_source'):
 b=path.read_bytes();alias=alias or str(path.relative_to(N));h=sha(b)
 r={'source':alias,'original_path':str(path),'role':role,**ident(b),'recovery_path':PK+'/archive/sha256/'+h}
 if alias in sources:assert sources[alias]==r or sources[alias]['sha256']==h
 else:sources[alias]=r
 objects[h]={'path':r['recovery_path'],**ident(b)};put(r['recovery_path'],b)
 return b

assert not P.exists(),'Refuse overwrite of existing proposal'
for folder,pin in plan['roots'].items():
 raw=add(N/folder/'FREEZE.json',role='source_freeze');assert sha(raw)==pin,folder
 frozen=json.loads(raw);key='members' if 'members' in frozen else 'files';rows=frozen[key]
 for row in rows:
  p=Path(row['path']);p=p if p.is_absolute() else N/folder/p;p.relative_to(N)
  raw=add(p);assert ident(raw)=={'bytes':row['bytes'],'sha256':row['sha256']},str(p)
 freeze_rows.append(dict(folder=folder,key=key,members=len(rows),sha256=pin))
for row in plan['extra']:
 raw=add(Path(row['path']),row['alias'],row['role']);assert ident(raw)=={'bytes':row['bytes'],'sha256':row['sha256']}
note=(D/'packet_text/WRAPPER.md').read_bytes();wrapper_len=len(note);maps=[]
for name,alias in plan['bodies']:
 raw=(N/alias).read_bytes();note+=('\n\n<!-- Unchanged complete source: '+name+' -->\n\n').encode();start=len(note);note+=raw
 maps.append(dict(name=name,source=alias,container=NOTE,start_byte_inclusive=start,end_byte_exclusive=len(note),**ident(raw)))
put(NOTE,note)
js(PK+'/BODY_MAP.json',dict(new_wrapper_bytes=[0,wrapper_len],bodies=maps))
js(PK+'/SOURCE_MANIFEST.json',dict(schema='reflection_preparation_source_archive_v1',sources=list(sources.values())))
js(PK+'/ARCHIVE_INDEX.json',dict(objects=list(objects.values())))
js(PK+'/FROZEN_SOURCE_CLOSURE.json',dict(roots=freeze_rows,closure_rule=plan['closure_rule']))
js(PK+'/PARENT_BINDING.json',dict(canonical_binding_complete=False,direct_mathematical_parents=plan['parents'],git_ancestry_is_not_mathematical_dependency=True))
js(PK+'/ACCEPTANCE_BINDING.json',dict(qualified_source_decisions=plan['acceptances'],source_wrapper_review=None))
js(PK+'/PARENT_PUBLICATION_EVIDENCE.json',dict(parent_publication_binding=None,this_source_publication=None,scope='Exact parent bytes only; no live publication observation.'))
state={k:None for k in ['source_wrapper_review','source_publication','canonical_integration','current_base_observation','canonical_review','primary_execution','publication_action','retained_audit']};state.update(scientific_programs_run_this_draft=0,scientific_replays=0)
js(PK+'/PUBLICATION_STATE.json',state)
js(PK+'/ACTUAL_BINDING.json',dict(kind='unbound_source_only_proposal',source_review=None,base_observation=None,canonical_review=None,canonical_parent_binding=None))
for name in ['PR_BODY.md','BINDING_CONTRACT.md']:put(PK+'/'+name,(D/'packet_text'/name).read_bytes())
js(PK+'/EXPOSURE.json',plan['exposure'])
inputs=[dict(path=str(p.relative_to(P)),**ident(p.read_bytes())) for p in sorted(P.rglob('*')) if p.is_file()]
js(PK+'/INPUT_MANIFEST.json',dict(schema='reflection_preparation_publication_inputs_v1',inputs=inputs))
msha=sha((P/PK/'INPUT_MANIFEST.json').read_bytes());template=(D/'primary_template.py').read_text()
generated=template.replace('__MANIFEST_SHA256__',msha).replace('__AUDIT_INPUT_PATHS__',repr([r['path'] for r in inputs]+[PK+'/INPUT_MANIFEST.json'])).replace('__EXPECTED_BODIES__',repr({r['name']:r['sha256'] for r in maps}))
put(SCRIPT,generated.encode())
result=dict(utc=datetime.now(timezone.utc).isoformat(),note=NOTE,note_sha256=sha(note),unchanged_bodies=len(maps),source_aliases=len(sources),unique_archive_objects=len(objects),freeze_member_counts=[r['members'] for r in freeze_rows],input_manifest_sha256=msha,scientific_executions=0,canonical_execution=None)
(D/'BUILD_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
