import ast,copy,difflib,hashlib,json,subprocess,sys
from pathlib import Path
sys.dont_write_bytecode=True
R=Path('/private/tmp/review-drain-20260915');W=R/'review-meta-slot';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=sha(p))
p=R/'drain8163-author-prepared-v2.json';assert sha(p)=='c256784ae1b7de82957f535d1e769b75076c29a282a6edd491d9b2f80cd33163';d=json.loads(p.read_text())
assert json.loads((R/'review-meta-slot.json').read_text())['owner']=='PR8163-author'
assert subprocess.check_output(['git','-C',str(W),'rev-parse','HEAD'],text=True).strip()==d['base']
assert not subprocess.check_output(['git','-C',str(W),'diff','--name-only','HEAD']).strip()
for row in d['source_bindings']:assert sha(W/row['path'])==row['sha256']
sys.path.insert(0,str(W/'scripts'));import runner_cache as c
before_api=[dict(runner=x,source_sha256=sha(W/x),declared_input_paths=c.declared_input_paths(W/x),declared_input_fingerprint=c.declared_input_fingerprint(W/x)) for x in d['runners']];assert all(x['declared_input_paths'] is None and x['declared_input_fingerprint'] is None for x in before_api)
failed=R/'drain8163-v2-input-api-failure.json';assert not failed.exists();failed.write_text(json.dumps(dict(status='SOURCE_DECLARATION_NOT_RECOGNIZED_BY_ACTUAL_CACHE_API',api=ref(W/'scripts/runner_cache.py'),results=before_api,execution='No primary; metadata API parses only'),indent=2)+'\n')
store=R/'drain8163-prepared-v2-source-copies';store.mkdir(exist_ok=False);diff=[];checks=[]
for run in d['runners']:
 old=(W/run).read_text();out=store/Path(run).name;out.write_text(old)
 assert old.count('AUDIT_INPUT_FILES')==2
 new=old.replace('AUDIT_INPUT_FILES','AUDIT_INPUT_PATHS');(W/run).write_text(new);compile(new,run,'exec')
 a=ast.parse(old);b=ast.parse(new)
 class Rename(ast.NodeTransformer):
  def visit_Name(self,node):
   if node.id=='AUDIT_INPUT_FILES':node.id='AUDIT_INPUT_PATHS'
   return node
 assert ast.dump(Rename().visit(a),include_attributes=False)==ast.dump(b,include_attributes=False)
 diff.extend(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='prepared-v2/'+run,tofile='prepared-v3/'+run))
 inputs=list(c.declared_input_paths(W/run));pins=ast.literal_eval(next(n.value for n in b.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='EXPECTED_INPUT_SHA256'))
 assert inputs==list(pins) and all(sha(W/x)==pins[x] for x in inputs)
 fingerprint=c.declared_input_fingerprint(W/run);assert re_full_hex(fingerprint) if False else bool(fingerprint and len(fingerprint)==64)
 assert c.declared_timeout_for(W/run)==180
 checks.append(dict(runner=run,source_sha256=sha(W/run),preserved_v2=ref(out),ordered_inputs=[dict(path=x,sha256=pins[x]) for x in inputs],declared_input_fingerprint=fingerprint,timeout=180,AST_change_only='Rename AUDIT_INPUT_FILES to AUDIT_INPUT_PATHS declaration and actual guard iteration; no other AST change'))
patch=R/'drain8163-author-v2-to-v3.diff';patch.write_text(''.join(diff))
api=R/'drain8163-v3-input-api-verification.json';api.write_text(json.dumps(dict(status='PASS_ACTUAL_DECLARED_INPUT_API_NOT_SCIENCE_EXECUTION',api_source=ref(W/'scripts/runner_cache.py'),results=checks,prior_failure=ref(failed),primary_executions=0),indent=2)+'\n')
plans=json.loads((R/'drain8163-author-input-resource-plans-v2.json').read_text())
for plan in plans:
 plan['source_sha256']=sha(W/plan['runner']);plan['declaration_name']='AUDIT_INPUT_PATHS';plan['actual_api_fingerprint']=next(x['declared_input_fingerprint'] for x in checks if x['runner']==plan['runner'])
planp=R/'drain8163-author-input-resource-plans-v3.json';planp.write_text(json.dumps(plans,indent=2)+'\n')
mp=json.loads((R/'drain8163-author-full-mapping-v2.json').read_text())
for row in mp:
 if row['final_path']:row['final_sha256']=sha(W/row['final_path'])
mapfile=R/'drain8163-author-full-mapping-v3.json';mapfile.write_text(json.dumps(mp,indent=2)+'\n')
v3=copy.deepcopy(d);v3['status']='UNTRACKED_AUTHOR_PREPARED_V3_ACTUAL_API_FIX_PENDING_ORIGINAL_REVIEWER_CONFIRMATION';v3['prior_prepared']=ref(p);v3['source_bindings']=[dict(path=x['path'],sha256=sha(W/x['path'])) for x in d['source_bindings']];v3['v3_evidence']=[ref(x) for x in [failed,patch,api,planp,mapfile]];v3['correction']={'scope':'Only six runner declaration/actual guard iteration names changed to AUDIT_INPUT_PATHS. Order, pins, notes, proofs, arithmetic, fixtures and archive unchanged.','changed_paths':d['runners'],'original_reviewer_confirmation':'pending'};v3['remaining']=['Original reviewer affected confirmation for actual API metadata correction','Only after confirmation create future builder v2 binding prepared-v3 and new freeze','Root current-base advancement, registrations, staging and cheap/cold checks','Sole limited captures and final evidence confirmation']
v3p=R/'drain8163-author-prepared-v3.json';v3p.write_text(json.dumps(v3,indent=2)+'\n');print(json.dumps(ref(v3p),indent=2));print(json.dumps(ref(api),indent=2))
