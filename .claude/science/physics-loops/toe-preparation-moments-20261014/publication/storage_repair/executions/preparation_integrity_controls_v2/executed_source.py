from pathlib import Path
import ast,gzip,hashlib,json,shutil
from common import N,W,pin,read_json,write_json,run,now,require_campaign_active
D=N/'publication_integration/preparation/storage_repair';P=N/'preparation_moment_publication_components';B=D/'bound_payload'
require_campaign_active();config=read_json(P/'INPUTS.json');packet=config['packet'];helper=config['helper'];manifest_path=packet+'/IDENTITY_INPUTS.json'
prepared=read_json(D/'PREPARED_SOURCE.json')
for path,expected in prepared['installed_pins'].items():
 actual=pin(W/path);assert actual['sha256']==expected['sha256'] and actual['bytes']==expected['bytes']
def reassign(path,name,value):
 text=path.read_text();lines=text.splitlines(True)
 node=next(n for n in ast.parse(text).body if isinstance(n,ast.Assign) and any(isinstance(x,ast.Name) and x.id==name for x in n.targets))
 lines[node.lineno-1:node.end_lineno]=[name+' = '+repr(value)+'\n'];path.write_text(''.join(lines))
def refresh_outer(root,changed):
 manifest=read_json(root/manifest_path)
 for path in changed:manifest['files'][path]={k:pin(root/path)[k] for k in ['bytes','sha256']}
 write_json(root/manifest_path,manifest)
 reassign(root/helper,'MANIFEST_SHA256',pin(root/manifest_path)['sha256'])
results=[]
for case in ['manifest_anchor','note_byte','proof_interval','object_content','archive_recipe','group_membership','canonical_parent','declared_read','fragment_content']:
 root=D/'integrity_fixtures'/case;assert not root.exists();shutil.copytree(B,root)
 parent=config['parent']['repo_path'];(root/parent).parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(W/parent,root/parent)
 changed=[]
 if case=='manifest_anchor':
  p=root/manifest_path;p.write_bytes(p.read_bytes()+b' ');expected='manifest identity';changed=[manifest_path]
 elif case=='note_byte':
  p=root/config['note'];b=p.read_bytes();p.write_bytes(b'!'+b[1:]);expected='identity: '+config['note'];changed=[config['note']]
 elif case=='proof_interval':
  path=packet+'/BODY_MAP.json';v=read_json(root/path);v['bodies'][0]['byte_end_exclusive']+=1;write_json(root/path,v);refresh_outer(root,[path]);expected='identity: body '+v['bodies'][0]['id'];changed=[path]
 elif case in ['object_content','archive_recipe','group_membership']:
  path=packet+'/SOURCE_ARCHIVE.json';v=read_json(root/path);changed=[path]
  if case=='object_content':
   key,item=next(iter(v['objects'].items()));obj=item['path'];data=gzip.decompress((root/obj).read_bytes())
   (root/obj).write_bytes(gzip.compress(data+b'!',mtime=0));item['stored']={k:pin(root/obj)[k] for k in ['bytes','sha256']};changed.append(obj);expected='identity: uncompressed object'
  elif case=='archive_recipe':
   row=next(r for r in v['records'] if any(x['kind']=='object' for x in r['parts']))
   part=next(x for x in row['parts'] if x['kind']=='object');part['sha256']=next(k for k in v['objects'] if k!=part['sha256']);expected='identity: archive '+row['alias']
  else:
   prefix='assemblies/'+v['groups'][0]['id']+'/'
   row=next(r for r in v['records'] if r['alias'].startswith(prefix) and r['alias']!=prefix+v['groups'][0]['seal'])
   v['records'].remove(row);expected='complete group closure'
  write_json(root/path,v);refresh_outer(root,changed)
 elif case=='fragment_content':
  row=read_json(root/packet/'BODY_MAP.json')['fragments'][0];path=row['path'];p=root/path;p.write_bytes(gzip.compress(gzip.decompress(p.read_bytes())+b'!',mtime=0));refresh_outer(root,[path]);expected='identity: framing fragment';changed=[path]
 elif case=='canonical_parent':
  p=root/parent;b=p.read_bytes();offset=read_json(root/packet/'BODY_MAP.json')['parent']['byte_start_0'];p.write_bytes(b[:offset]+b'!'+b[offset+1:]);refresh_outer(root,[parent]);expected='live canonical parent drift';changed=[parent]
 else:
  reassign(root/helper,'AUDIT_INPUT_PATHS',[x for x in prepared['canonical_inputs'] if x!=manifest_path]);expected='undeclared read: '+manifest_path;changed=[helper]
 argv=['python3',str(Path(__file__).with_name('run_identity_fixture.py')),'--runner',str(root/helper),'--repo',str(root)]
 output=json.loads(run(D/'integrity_runs',case,argv,expected=(1,)))
 assert output['type']=='ValueError' and output['reason']==expected,(case,output,expected)
 results.append({'case':case,'expected_reason':expected,'actual':output,'changed_targets':changed,'mutant_helper':pin(root/helper),'mutant_manifest':pin(root/manifest_path),'actual_receipt':pin(D/'integrity_runs'/case/'EXECUTION.json')})
for path,expected in prepared['installed_pins'].items():
 actual=pin(W/path);assert actual['sha256']==expected['sha256'] and actual['bytes']==expected['bytes']
r={'utc':now().isoformat(),'scope':'Nine independent scratch byte/structure integrity mutations; zero mathematical or physical controls.','results':results,'canonical_source_unchanged':True,'new_mathematical_executions':0}
write_json(D/'INTEGRITY_CONTROLS.json',r);print({'rejections':len(results),'record':pin(D/'INTEGRITY_CONTROLS.json'),'canonical_source_unchanged':True})
