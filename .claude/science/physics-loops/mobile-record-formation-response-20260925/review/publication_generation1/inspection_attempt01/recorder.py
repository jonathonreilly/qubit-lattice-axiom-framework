from pathlib import Path
import json,hashlib,ast,subprocess,sys,time,datetime
D=Path('.').resolve();I=D.parent
source=D/'verify_publication_readonly.py';body=source.read_text();tree=ast.parse(body)
for node in ast.walk(tree):
 if isinstance(node,(ast.Import,ast.ImportFrom)):
  names=[x.name.split('.')[0] for x in node.names] if isinstance(node,ast.Import) else [node.module.split('.')[0]]
  assert set(names)<=set(['pathlib','collections','ast','datetime','hashlib','json','re','sys'])
 if isinstance(node,ast.Call):
  called=ast.unparse(node.func)
  assert not any(part in called for part in ['write','unlink','mkdir','chmod','rename','replace_file','Popen','subprocess','exec','eval(']),called
pins=json.loads((D/'SOURCE_PINS_INITIAL.json').read_text());post=json.loads((I/'POST_SOURCE_PINS.json').read_text())
origins=[Path(x['origin']) for x in pins['sources']+post['author39_sources']+post['permitted_main_parents']]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def file_map():
 paths=set(p for p in I.rglob('*') if p.is_file())|set(origins)
 return {str(p):digest(p) for p in sorted(paths)}
before=file_map();start=time.perf_counter();at=datetime.datetime.now(datetime.timezone.utc).isoformat()
r=subprocess.run([sys.executable,str(source)],cwd=D,capture_output=True)
elapsed=time.perf_counter()-start;after=file_map();unchanged=before==after
assert unchanged
out=D/'verification_attempt01';assert not out.exists();out.mkdir()
(out/source.name).write_bytes(source.read_bytes());(out/'stdout.log').write_bytes(r.stdout);(out/'stderr.log').write_bytes(r.stderr)
receipt={'started_utc':at,'command':[sys.executable,str(source)],'source_sha256':digest(source),'elapsed_seconds':elapsed,'exit_code':r.returncode,'stdout_bytes':len(r.stdout),'stderr_bytes':len(r.stderr),'all_observed_source_maps_unchanged':unchanged,'observed_files':len(before),'science_programs_executed':False,'verifier_AST_read_and_safe_calls_checked':True}
(out/'EXECUTION.json').write_text(json.dumps(receipt,indent=2)+'\n')
(out/'OBSERVED_SOURCE_MAP.json').write_text(json.dumps(before,indent=2)+'\n')
if r.returncode==0:
 result=json.loads(r.stdout);(out/'VERIFICATION_REPORT.json').write_bytes(r.stdout)
 print(json.dumps({'execution':receipt,'report_sha256':digest(out/'VERIFICATION_REPORT.json'),'body':result['body_correspondence'],'differences':result['all_differences'],'leaf_count':result['leaf_count'],'geometry_groups':len(result['geometry']),'row_count':len(result['complete_scientific_rows'])},indent=2))
else:
 print(json.dumps(receipt,indent=2));print(r.stderr.decode())
