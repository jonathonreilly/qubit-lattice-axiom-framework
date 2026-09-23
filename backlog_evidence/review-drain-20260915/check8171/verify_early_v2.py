import ast,gzip,hashlib,json,pathlib,subprocess
R=pathlib.Path('/private/tmp/review-drain-20260915'); S=R/'drain8171-prepared-source-v2'; W=R/'author-draft-slot'; O=R/'drain8171-original'
h=lambda b:hashlib.sha256(b).hexdigest()
def git(*args):return subprocess.check_output(['git','-C',str(W),*args])
p=json.loads((R/'drain8171-author-prepared-v2.json').read_text()); results={}
for e in p['source']:
 b=(S/e['path']).read_bytes();assert h(b)==e['sha256'];assert (W/e['path']).read_bytes()==b
 mode='100755' if (W/e['path']).stat().st_mode&0o111 else '100644';assert mode==e['mode']
results['source_paths_snapshot_and_worktree_verified']=len(p['source'])
man=json.loads((S/p['original_manifest']['path']).read_text()); inv=json.loads((O/'inventory.json').read_text())
assert {e['original_path'] for e in man['entries']}=={e['path'] for e in inv['paths']}
for e in man['entries']:
 b=(S/e['recovery']['path']).read_bytes(); raw=gzip.decompress(b)
 assert h(b)==e['recovery']['sha256'] and h(raw)==e['sha256']==e['recovery']['decoded_sha256']
 assert raw==git('show',p['head']+':'+e['original_path'])
 mode,typ,blob=git('ls-tree',p['head'],'--',e['original_path']).decode().split('\t')[0].split()
 assert mode==e['mode'] and blob==e['git_blob'] and typ=='blob'
results['complete_original_paths_modes_git_blobs_and_decoded_bytes']=len(man['entries'])
old=ast.parse(next((O/'head/scripts').glob('*.py')).read_text());new=ast.parse((S/p['primaries'][0]).read_text())
class Reports(ast.NodeTransformer):
 def visit_Call(self,n):
  n=self.generic_visit(n)
  if isinstance(n.func,ast.Attribute) and n.func.attr=='check' and len(n.args)==3:n.args[2]=ast.Constant(value='REPORT')
  return n
for name in ['exp_bounds','A_bounds','sqrt_bounds','family_b','family_c','family_d']:
 a=next(n for n in old.body if isinstance(n,ast.FunctionDef) and n.name==name);b=next(n for n in new.body if isinstance(n,ast.FunctionDef) and n.name==name)
 assert ast.dump(Reports().visit(a),include_attributes=False)==ast.dump(Reports().visit(b),include_attributes=False)
results['six_computational_functions_identical_excluding_check_report_text']=True
assign={}
for n in new.body:
 if isinstance(n,ast.Assign) and len(n.targets)==1 and isinstance(n.targets[0],ast.Name):
  try:assign[n.targets[0].id]=ast.literal_eval(n.value)
  except (ValueError,TypeError):pass
for path in assign['AUDIT_INPUT_PATHS']:
 assert h((W/path).read_bytes())==assign['INPUT_SHA256'][path]
results['three_input_pins_verified']=True
paths=['docs/ai_methodology/skills/review-loop','docs/ai_methodology/skills/no-go-discipline','docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md','docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md','docs/MINIMAL_AXIOMS_2026-06-29.md','docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md','docs/audit/data/axiom_premise_nodes.json','docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md','docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md','docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md','docs/repo/DEFERRED_DECISIONS.md']
assert not git('diff','--name-only','012c276a64c80cf5256d68fa7dbb06939586153b',p['base'],'--',*paths)
results['authority_and_applicable_skill_bytes_unchanged']=True
results['tracked_diff']=git('diff','--name-only').decode();results['staged_diff']=git('diff','--cached','--name-only').decode()
assert not results['tracked_diff'] and not results['staged_diff']
for e in p['source']:assert not git('ls-tree',p['base'],'--',e['path'])
results['all_23_paths_additive_to_current_main']=True
results['primary_imported_or_executed']=False
print(json.dumps(results,indent=2))
