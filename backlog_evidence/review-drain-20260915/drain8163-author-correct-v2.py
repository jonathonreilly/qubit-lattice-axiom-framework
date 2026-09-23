import ast,copy,difflib,hashlib,json,subprocess
from pathlib import Path
R=Path('/private/tmp/review-drain-20260915');W=R/'review-meta-slot'
def sha(b):return hashlib.sha256(b).hexdigest()
def ref(p):return {'path':str(p),'sha256':sha(p.read_bytes())}
review=R/'drain8163-early-affected-review-v1.json';assert sha(review.read_bytes())=='1a51fc949008b8ebdb345e18bd74f1be4ed6e97e695960ba8e2c1d98f5d934b3'
d=json.loads((R/'drain8163-author-prepared-v1.json').read_text())
for x in d['source_bindings']:assert sha((W/x['path']).read_bytes())==x['sha256']
assert subprocess.check_output(['git','-C',str(W),'rev-parse','HEAD'],text=True).strip()==d['base']
model=d['notes'][1];curl=d['notes'][0];run=d['runners'][2];join=d['runners'][3]; paths=[model,run,join];before={p:(W/p).read_text() for p in paths}
s=before[model];assert s.count('upstream_dependencies: []')==1
s=s.replace('upstream_dependencies: []','upstream_dependencies: ['+json.dumps(Path(curl).stem.lower())+']',1)
anchor='## 1. Spatial blocks and positive recurrence transfer\n'
addition='Load-bearing model-definition and normalization parent: ['+Path(curl).name+']('+Path(curl).name+'). The parent supplies the spatial Wilson operator and open temporal determinant normalization used here. This algebraic model match requires only m>0; the stronger m>3kappa hypothesis for the parent\'s uniform physical-curl estimates is not assumed as necessary for this result.\n\n'
assert s.count(anchor)==1;s=s.replace(anchor,addition+anchor,1);(W/model).write_text(s)
for p in [run,join]:
 src=before[p];tree=ast.parse(src);vals={n.targets[0].id:ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in ['AUDIT_INPUT_FILES','EXPECTED_INPUT_SHA256']}
 inputs=vals['AUDIT_INPUT_FILES']
 if p==run:assert inputs==[model];inputs.append(curl)
 newhash={n:sha((W/n).read_bytes()) for n in inputs}
 lines=src.splitlines(True)
 for i,line in enumerate(lines):
  if line.startswith('AUDIT_INPUT_FILES='):lines[i]='AUDIT_INPUT_FILES='+repr(inputs)+'\n'
  if line.startswith('EXPECTED_INPUT_SHA256='):lines[i]='EXPECTED_INPUT_SHA256='+repr(newhash)+'\n'
 out=''.join(lines);(W/p).write_text(out);compile(out,p,'exec')
 a=[n for n in tree.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))];b=[n for n in ast.parse(out).body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))];assert ast.dump(ast.Module(body=a,type_ignores=[]),include_attributes=False)==ast.dump(ast.Module(body=b,type_ignores=[]),include_attributes=False)
assert [x for x in before[model].splitlines() if x.startswith('    ')]==[x for x in s.splitlines() if x.startswith('    ')]
patch=''.join(''.join(difflib.unified_diff(before[p].splitlines(True),(W/p).read_text().splitlines(True),fromfile='prepared-v1/'+p,tofile='prepared-v2/'+p)) for p in paths)
patchfile=R/'drain8163-author-v1-to-v2.diff';assert not patchfile.exists();patchfile.write_text(patch)
plans=json.loads((R/'drain8163-author-input-resource-plans.json').read_text())
for plan in plans:
 src=ast.parse((W/plan['runner']).read_text());inputs=next(ast.literal_eval(n.value) for n in src.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='AUDIT_INPUT_FILES')
 plan['ordered_inputs']=[{'path':x,'sha256':sha((W/x).read_bytes())} for x in inputs]
planfile=R/'drain8163-author-input-resource-plans-v2.json';assert not planfile.exists();planfile.write_text(json.dumps(plans,indent=2)+'\n')
mapping=json.loads((R/'drain8163-author-full-mapping.json').read_text())
for row in mapping:
 if row['final_path']:row['final_sha256']=sha((W/row['final_path']).read_bytes())
mapfile=R/'drain8163-author-full-mapping-v2.json';assert not mapfile.exists();mapfile.write_text(json.dumps(mapping,indent=2)+'\n')
v2=copy.deepcopy(d);v2['status']='UNTRACKED_AUTHOR_PREPARED_V2_DEPENDENCY_FIX_PENDING_AFFECTED_CONFIRMATION';v2['source_bindings']=[{'path':x['path'],'sha256':sha((W/x['path']).read_bytes())} for x in d['source_bindings']]
v2['prior_prepared']=ref(R/'drain8163-author-prepared-v1.json');v2['finding_reference']=ref(review);v2['correction']={'finding':'8163-EARLY-DEPENDENCY-1','changed_paths':paths,'scope':'Actual temporal-resummation definition/normalization parent declared and linked; owner-then-parent literal runtime inputs read by existing hash guard; downstream owner hash updated. Algebraic m>0 scope explicit; no heavy-curl hypothesis imported.','function_ASTs_unchanged':True,'indented_formula_lines_unchanged':True,'reverse_context_links_unchanged':True,'archive_unchanged':True};v2['v2_evidence']=[ref(p) for p in [patchfile,planfile,mapfile]]
v2['remaining']=['Original reviewer affected confirmation','Coordinator current-base advancement and staging, three explicit curl-helper registrations','Actual preflight and same-session cold confirmation','Sole limited captures and final evidence confirmation; combined coordinator validation']
out=R/'drain8163-author-prepared-v2.json';assert not out.exists();out.write_text(json.dumps(v2,indent=2)+'\n');print(json.dumps(ref(out),indent=2));print(patch)
