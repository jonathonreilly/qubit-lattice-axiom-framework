from pathlib import Path
import ast,difflib,json,shutil
from common import N,W,pin,check_pin,read_json,write_json,run,now,require_campaign_active,require_clean_branch,git_read

D=N/'publication_integration/preparation'
P=N/'preparation_moment_publication_components'
BRANCH='physics-loop/toe-preparation-moments-20261014'
HEAD='463fa381d9fe9403b6b6f3e3ce19505aa947edf2'
MAIN='92574ffe95192cc0724a27e1acad28e42d325115'
INSTRUCTIONS='3a4b2c66a1ead7a1c48b4359627e968f681e3c39'
require_campaign_active()
a=read_json(D/'COMPONENT_ROOT_ACCEPTANCE.json');assert a['component_review_complete'] is True
check_pin(a['freeze']['path'],a['freeze'])
review=read_json(D/'PREPARE_DRIVER_REVIEW.json');assert review['approved_for_root_execution'] is True
check_pin(__file__,review['source']);check_pin(Path(__file__).with_name('common.py'),review['common'])
require_clean_branch(BRANCH,HEAD)
for ref,want in [('origin/main',MAIN),('origin/ai/execution',INSTRUCTIONS)]:
 assert run(D,'prepare_'+ref.replace('/','_'),['git','rev-parse',ref]).decode().strip()==want
parent=json.loads(run(D,'actual_parent_pr',['gh','pr','view','9574','--json','number,url,state,isDraft,headRefOid,headRefName,baseRefName']))
assert parent['state']=='OPEN' and parent['isDraft'] is False and parent['headRefOid']==HEAD
config=read_json(P/'INPUTS.json');assert config['main']==MAIN and config['instructions']==INSTRUCTIONS
check_pin(W/config['parent']['repo_path'],config['parent'])
freeze=read_json(a['freeze']['path'])
for row in freeze['members']:check_pin(P/row['path'],row)
assert {str(f.relative_to(P)) for f in P.rglob('*') if f.is_file()}=={r['path'] for r in freeze['members']}|{Path(a['freeze']['path']).name}
B=D/'bound_payload';assert not B.exists();shutil.copytree(P/'payload',B)
for f in B.rglob('*'):
 if f.is_file():f.chmod(0o644)
packet=config['packet'];manifest_path=packet+'/IDENTITY_INPUTS.json'
original_manifest=read_json(B/manifest_path)
binding=read_json(B/packet/'PUBLICATION_BINDINGS.json')
binding.update(observed_at_utc=now().isoformat(),actual_parent_pr=parent,actual_child_branch=BRANCH,actual_child_base_head=HEAD,
 actual_child_base_tree=git_read('rev-parse','HEAD^{tree}').decode().strip(),integration_authorized=True,
 driver_bound_root_acceptance=pin(D/'PREPARE_DRIVER_REVIEW.json'),current_component_root_review=pin(D/'COMPONENT_ROOT_ACCEPTANCE.json'),
 scope='Immutable observations before canonical execution and PR creation; later actual execution is recorded in the canonical cache and publication review snapshot. Null later-action fields describe this capture time, not an ongoing pending scientific review.')
write_json(B/packet/'PUBLICATION_BINDINGS.json',binding)
for name,source in [('ROOT_COMPONENT_REVIEW.json',D/'COMPONENT_ROOT_ACCEPTANCE.json'),('ROOT_PREPARE_DRIVER_REVIEW.json',D/'PREPARE_DRIVER_REVIEW.json')]:
 shutil.copyfile(source,B/packet/name)
manifest=dict(original_manifest)
files={str(f.relative_to(B)):{k:pin(f)[k] for k in ['bytes','sha256']} for f in B.rglob('*') if f.is_file() and str(f.relative_to(B)) not in [manifest_path,config['helper']]}
files[config['parent']['repo_path']]={k:pin(W/config['parent']['repo_path'])[k] for k in ['bytes','sha256']}
manifest['files']=files;manifest['integrity_paths']=sorted(set(files)-set(manifest['external_scientific_paths']))
write_json(B/manifest_path,manifest)
inputs=sorted(list(files)+[manifest_path])
template=(P/'templates/identity_runner.py.in').read_text()
helper=template.replace('@AUDIT_INPUT_PATHS@',repr(inputs)).replace('@MANIFEST_PATH@',repr(manifest_path)).replace('@MANIFEST_SHA256@',repr(pin(B/manifest_path)['sha256']))
scopes={
 'per_element':'checked and not executed — source bytes only; no operator algebra or numerical identity is evaluated.',
 'per_site':'checked and not executed — source bytes only; no local preparation or geometry measurement is performed.',
 'per_mode':'checked and not executed — source bytes only; no mode, continuum or native dynamics theorem is tested.',
 'per_block':'checked and not executed — exact argument reconstruction only; no moment inequality is proved by this runner.',
 'lattice_wide':'checked and not executed — preservation only; no all-volume preparation, common cap or physical realization is established.'}
for key,value in scopes.items():helper+='    print('+repr(key+': '+value)+')\n'
(B/config['helper']).write_text(helper)
ast.parse(helper)
expected=(template.replace('@AUDIT_INPUT_PATHS@',repr(inputs)).replace('@MANIFEST_PATH@',repr(manifest_path)).replace('@MANIFEST_SHA256@',repr(pin(B/manifest_path)['sha256'])))
assert helper.startswith(expected)
for name in [config['note'],packet+'/BODY_MAP.json',packet+'/SOURCE_ARCHIVE.json']:
 assert (B/name).read_bytes()==(P/'payload'/name).read_bytes()
changed=[]
for f in B.rglob('*'):
 if not f.is_file():continue
 name=str(f.relative_to(B));old=P/'payload'/name
 if not old.exists() or old.read_bytes()!=f.read_bytes():changed.append(name)
assert set(changed)=={manifest_path,config['helper'],packet+'/PUBLICATION_BINDINGS.json',packet+'/ROOT_COMPONENT_REVIEW.json',packet+'/ROOT_PREPARE_DRIVER_REVIEW.json'}
for name in changed:
 old=P/'payload'/name;before=old.read_text().splitlines(True) if old.exists() else []
 target=D/'source_diffs'/(Path(name).name+'.diff');target.parent.mkdir(exist_ok=True)
 target.write_text(''.join(difflib.unified_diff(before,(B/name).read_text().splitlines(True),fromfile='components/'+name,tofile='bound/'+name)))
paths=sorted(str(f.relative_to(B)) for f in B.rglob('*') if f.is_file())
require_clean_branch(BRANCH,HEAD);require_campaign_active()
for name in paths:
 target=W/name;assert not target.exists(),name
for name in paths:
 target=W/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(B/name,target)
assert not git_read('diff','--cached','--name-only','-z')
status=git_read('status','--porcelain','-z','--untracked-files=all')
actual=[]
for row in status.split(b'\0'):
 if not row:continue
 assert row[:3]==b'?? ',row[:30]
 actual.append(row[3:].decode())
assert set(actual)==set(paths)
r={'utc':now().isoformat(),'status':'bound_source_installed_for_root_review_before_canonical_execution','parent_pr':parent,'branch':BRANCH,'base_head':HEAD,'main':MAIN,'instructions':INSTRUCTIONS,
 'source_component_acceptance':pin(D/'COMPONENT_ROOT_ACCEPTANCE.json'),'driver_review':pin(D/'PREPARE_DRIVER_REVIEW.json'),'bound_note':pin(B/config['note']),'bound_helper':pin(B/config['helper']),
 'new_current_binding':pin(B/packet/'PUBLICATION_BINDINGS.json'),'changed_component_paths':sorted(changed),'installed_files':len(paths),'installed_paths':paths,'installed_pins':{name:pin(W/name) for name in paths},'canonical_inputs':inputs,'new_math_executions':0,'science_bodies_changed':False,'scope_lines':scopes}
write_json(D/'PREPARED_SOURCE.json',r);print({'installed_files':len(paths),'changed_components':len(changed),'canonical_inputs':len(inputs),'note':pin(B/config['note']),'receipt':pin(D/'PREPARED_SOURCE.json')})
