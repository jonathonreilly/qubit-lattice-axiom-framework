"""Seal the new independent PRE only; this is an explicit writing utility."""
from pathlib import Path
import ast,datetime,hashlib,json,subprocess
HERE=Path(__file__).resolve().parent
assert HERE.name=='native-charge-identification-independent'
target=HERE/'PRE_SEAL.json';assert not target.exists()
sha=lambda b:hashlib.sha256(b).hexdigest()
pins=json.loads((HERE/'SOURCE_PINS.json').read_text());bindings=[]
for item in pins['sources']:
 body=(HERE/item['frozen_path']).read_bytes();assert sha(body)==item['sha256'] and len(body)==item['bytes']
 if item['origin'].startswith('/'):
  assert Path(item['origin']).read_bytes()==body
  if item.get('exact_git_object'):
   p=Path(item['origin']);repo=p.parent.parent
   assert subprocess.check_output(['git','show',item['revision']+':docs/'+p.name],cwd=repo)==body
 else:
  assert subprocess.check_output(['git','show',item['revision']+':AGENTS.md'],cwd=item['repository'])==body
 bindings.append({'origin':item['origin'],'sha256':item['sha256'],'bytes':len(body)})
executions=[]
for tag in ['freeze','exploration','supersolution','decisive','charge_coherence','verification','small_period','small_verification']:
 r=json.loads((HERE/f'{tag}.execution.json').read_text())
 assert sha(Path(r['command'][1]).read_bytes())==r['source_sha256']
 for stream in ['stdout','stderr']:
  body=(HERE/f'{tag}.{stream}.txt').read_bytes();assert sha(body)==r[f'{stream}_sha256'] and len(body)==r[f'{stream}_bytes']
 assert r['exit_code']==0 and r['stderr_bytes']==0
 executions.append({'receipt':f'{tag}.execution.json','receipt_sha256':sha((HERE/f'{tag}.execution.json').read_bytes()),'source_sha256':r['source_sha256'],'stdout_sha256':r['stdout_sha256'],'exit_code':0,'stderr_bytes':0})
for name in ['verification','small_verification']:
 assert json.loads((HERE/f'{name}.stdout.txt').read_text())['all_checks_completed'] is True
for name in ['verify_read_only.py','verify_small_period_read_only.py']:
 tree=ast.parse((HERE/name).read_text())
 for node in ast.walk(tree):
  if isinstance(node,ast.Call):
   if isinstance(node.func,ast.Name):assert node.func.id not in {'open','exec','eval','compile','__import__'}
   if isinstance(node.func,ast.Attribute):assert node.func.attr not in {'write_text','write_bytes','open','chmod','unlink','mkdir','rmdir','rename','replace','run','Popen','system'}
  if isinstance(node,ast.Import):assert all(n.name.split('.')[0] in {'hashlib','json','math'} for n in node.names)
  if isinstance(node,ast.ImportFrom):assert node.module in {'collections','fractions','itertools','pathlib'}
report=(HERE/'PRE.md').read_text()
assert report.count('\\[')==report.count('\\]') and report.count('\\(')==report.count('\\)')
assert not any(ord(c)<32 and c not in '\r\n\t' for c in report)
final={'verified_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_bindings':bindings,'execution_bindings':executions,'read_only_verifiers_static_scan':True,'PRE_sha256':sha(report.encode()),'forbidden_sources_read':False,'author_programs_executed_or_imported':False,'scope':'Final identity/bookkeeping refresh only; scientific calculations are in saved source and result files.'}
with (HERE/'FINAL_BINDINGS.json').open('x') as f:json.dump(final,f,indent=2);f.write('\n')
members=[]
for p in sorted(HERE.rglob('*')):
 assert not p.is_symlink()
 if p.is_file():
  body=p.read_bytes();members.append({'path':str(p.relative_to(HERE)),'sha256':sha(body),'bytes':len(body)})
seal={'phase':'Blind bounded PRE check40, before author release','sealed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'report':'PRE.md','report_sha256':sha((HERE/'PRE.md').read_bytes()),'source_pins':'SOURCE_PINS.json','source_pins_sha256':sha((HERE/'SOURCE_PINS.json').read_bytes()),'members':members,'forbidden_candidate_or_current_checkpoint_read':False,'parent_runtime_or_author_program_used_for_new_controls':False,'historical_exposure':'Earlier authorized root33/35/36 work is known. Current computation imports only the four pinned public notes and its own new helper.','model_or_effort_changed':False,'delegation':False,'publication_or_audit_mutation':False,'failed_search_routes_preserved':True,'next_action':'Stop and send completion hashes/paths only; await root review before any author disclosure.'}
with target.open('x') as f:json.dump(seal,f,indent=2);f.write('\n')
for item in members:
 p=HERE/item['path'];assert sha(p.read_bytes())==item['sha256'];p.chmod(0o444)
target.chmod(0o444)
print(json.dumps({'PRE':str(HERE/'PRE.md'),'PRE_sha256':seal['report_sha256'],'PRE_SEAL':str(target),'PRE_SEAL_sha256':sha(target.read_bytes()),'source_pins_sha256':seal['source_pins_sha256'],'member_count':len(members)},indent=2))
