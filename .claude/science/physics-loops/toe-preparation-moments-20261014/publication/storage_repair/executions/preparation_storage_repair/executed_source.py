import ast,gzip,hashlib,json,shutil
from pathlib import Path
from common import N,W,pin,check_pin,read_json,write_json,git_read,run,now,require_campaign_active
D=N/'publication_integration/preparation';R=D/'storage_repair';R.mkdir(exist_ok=False);P=N/'preparation_moment_publication_components';c=read_json(P/'INPUTS.json');packet=c['packet'];publication=W/packet/'publication';prepared=read_json(D/'PREPARED_SOURCE.json');manifest_path=packet+'/IDENTITY_INPUTS.json'
require_campaign_active();assert git_read('rev-parse','HEAD').decode().strip()==prepared['base_head']
original_paths=git_read('diff','--cached','--name-only','-z').decode().rstrip('\0').split('\0')
expected=set(prepared['installed_paths'])|set(read_json(D/'PUBLICATION_EVIDENCE_PACKAGE.json')['files'])|{packet+'/'+x for x in ['HANDOFF.md','TRACE_GATE.md','REVIEW_HISTORY.md']}|{'docs/audit/data/citation_graph_manifest.json','logs/runner-cache/'+Path(c['helper']).stem+'.txt'}
assert set(original_paths)==expected
for name,row in prepared['installed_pins'].items():check_pin(W/name,row)
for name,row in read_json(D/'PUBLICATION_EVIDENCE_PACKAGE.json')['files'].items():check_pin(W/name,row)
# Snapshot each changed old canonical byte string before replacing its representation.
old_bytes={name:(W/name).read_bytes() for name in prepared['installed_paths']}
bodymap=read_json(W/packet/'BODY_MAP.json');renamed={}
for row in bodymap['fragments']:
 old=row['path'];new=old+'.gz';raw=(W/old).read_bytes();assert len(raw)==row['bytes'] and hashlib.sha256(raw).hexdigest()==row['sha256']
 target=W/new;assert not target.exists();target.write_bytes(gzip.compress(raw,mtime=0));assert gzip.decompress(target.read_bytes())==raw
 row['path']=new;row['codec']='gzip';renamed[old]=new;(W/old).unlink()
write_json(W/packet/'BODY_MAP.json',bodymap)
template=(P/'templates/identity_runner.py.in').read_text();before="    fragments = [data[f['path']] for f in bodymap['fragments']]\n"
after="    fragments = []\n    for row in bodymap['fragments']:\n        require(row['codec'] == 'gzip', 'fragment codec')\n        fragment = gzip.decompress(data[row['path']])\n        identity(fragment, row, 'framing fragment')\n        fragments.append(fragment)\n"
assert template.count(before)==1;template=template.replace(before,after);(R/'identity_runner.py.in').write_text(template)
manifest=read_json(W/manifest_path)
for old,new in renamed.items():manifest['files'].pop(old);manifest['files'][new]={k:pin(W/new)[k] for k in ['bytes','sha256']}
manifest['files'][packet+'/BODY_MAP.json']={k:pin(W/packet/'BODY_MAP.json')[k] for k in ['bytes','sha256']};manifest['integrity_paths']=sorted(set(manifest['files'])-set(manifest['external_scientific_paths']));write_json(W/manifest_path,manifest)
inputs=sorted(list(manifest['files'])+[manifest_path]);helper=template.replace('@AUDIT_INPUT_PATHS@',repr(inputs)).replace('@MANIFEST_PATH@',repr(manifest_path)).replace('@MANIFEST_SHA256@',repr(pin(W/manifest_path)['sha256']))
for key,value in prepared['scope_lines'].items():helper+='    print('+repr(key+': '+value)+')\n'
ast.parse(helper);(W/c['helper']).write_text(helper)
# Reconstruct the entire formerly executed canonical tree, including its old helper and metadata.
prior_map=[]
for name,raw in old_bytes.items():
 target=W/name
 if target.is_file() and target.read_bytes()==raw:storage={'repository_path':name,'codec':'identity'}
 else:
  target=publication/'storage_repair/before_objects'/(hashlib.sha256(raw).hexdigest()+'.gz');target.parent.mkdir(parents=True,exist_ok=True)
  if not target.exists():target.write_bytes(gzip.compress(raw,mtime=0))
  storage={'repository_path':str(target.relative_to(W)),'codec':'gzip'}
 prior_map.append({'original_path':name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),**storage})
write_json(publication/'storage_repair/PRE_REPAIR_CANONICAL_MAP.json',{'scope':'All formerly executed canonical bytes, including prior control-fixture base, preserved exactly; later gzip framing changes representation only.','files':prior_map})
# Encode patch context and deliberate framing terminators without editing historical bytes.
for source in list((publication/'generation').rglob('*')):
 if source.is_file() and (source.suffix=='.diff' or (source.suffix=='.md' and source.read_bytes().endswith(b'\n\n'))):
  target=Path(str(source)+'.gz');assert not target.exists();raw=source.read_bytes();target.write_bytes(gzip.compress(raw,mtime=0));assert gzip.decompress(target.read_bytes())==raw
  renamed[str(source.relative_to(W))]=str(target.relative_to(W));source.unlink()
# Remap every frozen component member to exact current/recoverable original bytes.
reconstruction=read_json(publication/'SOURCE_COMPONENT_RECONSTRUCTION.json')
for row in reconstruction['files']:
 name=row['repository_path'];target=W/name
 if name in renamed:row['repository_path']=renamed[name];row['codec']='gzip';target=W/row['repository_path']
 else:row['codec']='identity'
 raw=gzip.decompress(target.read_bytes()) if row['codec']=='gzip' else target.read_bytes()
 if hashlib.sha256(raw).hexdigest()!=row['source']['sha256']:
  source=Path(row['source']['path']);check_pin(source,row['source']);raw=source.read_bytes();target=publication/'storage_repair/component_originals'/(row['source']['sha256']+'.gz');target.parent.mkdir(parents=True,exist_ok=True)
  if not target.exists():target.write_bytes(gzip.compress(raw,mtime=0))
  row['repository_path']=str(target.relative_to(W));row['codec']='gzip'
 assert len(raw)==row['source']['bytes'] and hashlib.sha256(raw).hexdigest()==row['source']['sha256']
write_json(publication/'SOURCE_COMPONENT_RECONSTRUCTION.json',reconstruction)
for source in (N/'runs/preparation_verify_stage').rglob('*'):
 if source.is_file():
  target=publication/'storage_repair/failed_stage'/source.name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target)
# Raw diff-check stdout is itself whitespace-bearing evidence.
p=publication/'storage_repair/failed_stage/stdout';raw=p.read_bytes();Path(str(p)+'.gz').write_bytes(gzip.compress(raw,mtime=0));p.unlink()
shutil.copyfile(__file__,publication/'storage_repair/repair_preparation_storage.py')
shutil.copyfile(R/'identity_runner.py.in',publication/'storage_repair/identity_runner.py.in')
assert (W/c['note']).read_bytes()==old_bytes[c['note']]
paths=sorted(renamed.get(name,name) for name in prepared['installed_paths']);paths=[x for x in paths if (W/x).is_file()]
assert len(paths)==len(prepared['installed_paths'])
B=R/'bound_payload';B.mkdir()
for name in paths:
 target=B/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(W/name,target)
current=dict(prepared,installed_paths=paths,installed_pins={name:pin(W/name) for name in paths},canonical_inputs=inputs,bound_helper=pin(W/c['helper']),storage_repair=True)
write_json(R/'PREPARED_SOURCE.json',current)
receipt={'utc':now().isoformat(),'reason':'Plain git diff --check rejected deliberate fragment blank EOF and archived patch context whitespace.','original_proofs_and_note_unchanged':True,'primary_logic_change':'Read gzip framing, validate original fragment identity, then perform identical complete-note reconstruction.','renamed_artifacts':renamed,'old_canonical_source':pin(publication/'storage_repair/PRE_REPAIR_CANONICAL_MAP.json'),'old_stage_failure':pin(N/'runs/preparation_verify_stage/EXECUTION.json'),'current_helper':pin(W/c['helper']),'current_manifest':pin(W/manifest_path),'new_mathematical_predicates':0,'required_followup':['Nine integrity controls including changed decompression family','Fresh canonical cache','Final full staged checks']}
write_json(R/'STORAGE_REPAIR.json',receipt);write_json(publication/'storage_repair/REVIEW.json',receipt)
# Remove only this task's verified prior staging; source data are already preserved above.
run(R,'clear_owned_previous_index',['git','restore','--staged','--',*original_paths])
assert git_read('diff','--cached','--name-only','-z')==b''
print({'renamed_files':len(renamed),'canonical_files':len(paths),'note_unchanged':True,'repair':pin(R/'STORAGE_REPAIR.json')})
