#!/usr/bin/env python3
"""Static portability inspection only; never imports/runs either candidate."""
from pathlib import Path
import ast,datetime,difflib,hashlib,json,resource,textwrap,time

resource.setrlimit(resource.RLIMIT_CPU,(15,15))
START=time.monotonic()
HERE=Path(__file__).resolve().parent
N=HERE.parents[1]
W=N.parent/'correlation_worktree'
items={
 'author_original':N/'two_body_interval_bridge/certify_interval.py',
 'reviewer_original':N/'two_body_interval_review/check_composition.py',
 'primary':W/'scripts/two_body_autonomous_halt_2026_10_17.py',
 'helper':W/'scripts/two_body_autonomous_halt_check_2026_10_17.py',
 'builder':N/'two_body_integration/prepare_code.py',
 'adaptation':N/'two_body_integration/CODE_ADAPTATION.json',
}
def ident(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
sources={k:ident(p) for k,p in items.items()}
assert sources['primary']['sha256']=='6111c95e2add4eb92fbc3f46d49f45085c3e95dc73431a68da7dcd602c912618'
assert sources['helper']['sha256']=='ee4b71de1d1ab3f92dd1c812974a9dac1b740bea2b8fa3c442890b1854881b92'
texts={k:p.read_text() for k,p in items.items()}
trees={k:ast.parse(texts[k]) for k in ('author_original','reviewer_original','primary','helper','builder')}
def asserts(t):
 nodes=sorted((n for n in ast.walk(t) if isinstance(n,ast.Assert)),key=lambda n:(n.lineno,n.col_offset))
 return [ast.dump(n,include_attributes=False) for n in nodes]
assert asserts(trees['author_original'])==asserts(trees['primary'])
assert asserts(trees['reviewer_original'])==asserts(trees['helper'])

p=texts['primary'];a=texts['author_original']
# All numerical definitions, construction, solves, residuals and assertions
# from reading the exact coefficient map to creation of the report are intact.
assert a[a.index('frozen ='):a.index('report={')]==p[p.index('frozen ='):p.index('report={')]
def assigned(tree,name):
 return next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in n.targets))
inputs=ast.literal_eval(assigned(trees['primary'],'AUDIT_INPUT_PATHS').value)
assert isinstance(inputs,tuple) and len(inputs)==len(set(inputs))
record=json.loads(texts['adaptation'])
assert list(inputs)==record['declared_inputs']
for k,record_key in [('author_original','author_source'),('reviewer_original','independent_source'),('primary','primary'),('helper','helper')]:
 for field in ('bytes','sha256'):assert sources[k][field]==record[record_key][field]

fn=next(n for n in trees['helper'].body if isinstance(n,ast.FunctionDef))
assert fn.name=='run_independent_checks' and [x.arg for x in fn.args.args]==['input_root']
h_body=textwrap.dedent(''.join(texts['helper'].splitlines(True)[fn.lineno:fn.end_lineno]))
old_body=texts['reviewer_original'][texts['reviewer_original'].index('START = time.monotonic()'):]
old_prefix=old_body[:old_body.index("(ROOT/'RESULTS.json').write_text")]
expected=old_prefix.replace('ROOT = Path(__file__).resolve().parent','ROOT = input_root',1)
expected=expected.replace("'cpu_seconds_cap':60,'parent_wall_seconds_cap':90","'cpu_seconds_cap':120,'parent_wall_seconds_cap':120")+'return output\n'
assert h_body==expected

input_root=W/'outputs/two_body_autonomous_halt_2026_10_17_inputs/frozen_sources'
author_root=input_root/'two_body_interval_bridge'
helper_root=input_root/'two_body_interval_review'
author_manifest=json.loads((author_root/'SOURCE_MANIFEST.json').read_text())
helper_manifest=json.loads((helper_root/'SOURCE_PINS.json').read_text())
required={str((author_root/'SOURCE_MANIFEST.json').relative_to(W)),
 str((helper_root/'SOURCE_PINS.json').relative_to(W)),
 'scripts/two_body_autonomous_halt_check_2026_10_17.py',
 'docs/TWO_BODY_AUTONOMOUS_HALT_BOUNDED_THEOREM_NOTE_2026-10-17.md'}
basenames=[];verified=[]
for row in author_manifest['sources']:
 name=Path(row['snapshot_path']).name;basenames.append(name)
 path=author_root/'inputs'/name
 assert not path.is_symlink()
 pin=ident(path)
 assert pin['bytes']==row['bytes'] and pin['sha256']==row['sha256']
 required.add(str(path.relative_to(W)));verified.append(pin)
assert len(basenames)==len(set(basenames))
for row in helper_manifest['sources']:
 suffix=Path(row['snapshot_path'])
 assert not suffix.is_absolute() and '..' not in suffix.parts
 path=helper_root/suffix
 assert not path.is_symlink()
 pin=ident(path)
 assert pin['bytes']==row['bytes'] and pin['sha256']==row['sha256']
 required.add(str(path.relative_to(W)));verified.append(pin)
assert set(inputs)==required

direct_helper_reads=[]
for node in ast.walk(fn):
 if isinstance(node,ast.Call) and isinstance(node.func,ast.Name) and node.func.id=='read':
  assert len(node.args)==1 and isinstance(node.args[0],ast.Constant) and isinstance(node.args[0].value,str)
  rel=node.args[0].value;direct_helper_reads.append(rel)
  assert str((helper_root/rel).relative_to(W)) in required
assert str((author_root/'inputs/rational_point_certificate.json').relative_to(W)) in required

writes={}
for key in ('primary','helper'):
 calls=[n for n in ast.walk(trees[key]) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr in ('write_text','write_bytes','open','unlink','mkdir','rename','replace')]
 writes[key]=[{'line':n.lineno,'expression':ast.unparse(n)} for n in calls]
assert writes['helper']==[]
assert len(writes['primary'])==2
for row in writes['primary']:
 assert "REPO / 'outputs/two_body_autonomous_halt_2026_10_17" in row['expression']
 assert '_inputs' not in row['expression']
limits={key:[ast.unparse(n) for n in ast.walk(trees[key]) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='setrlimit'] for key in ('primary','helper')}
assert limits['primary']==['resource.setrlimit(resource.RLIMIT_CPU, (120, 120))']
assert limits['helper']==[]
assert ast.literal_eval(assigned(trees['primary'],'AUDIT_TIMEOUT_SEC').value)==120
assert ast.literal_eval(assigned(trees['helper'],'AUDIT_TIMEOUT_SEC').value)==120
assert 'certificates are inherited by immutable identity, not recomputed by the helper.' in p

observed_inputs=[]
for rel in inputs:
 path=W/rel
 if path.exists(): observed_inputs.append(ident(path))
 else: observed_inputs.append({'path':str(path),'missing_at_inspection':True})

# Keep exact changed text evidence, avoiding a redundant full mathematical copy.
declaration=assigned(trees['primary'],'AUDIT_INPUT_PATHS')
reduced=p.splitlines(True);reduced[declaration.lineno-1:declaration.end_lineno]=['AUDIT_INPUT_PATHS = (...)\n']
diff=''.join(difflib.unified_diff(a.splitlines(True),''.join(reduced).splitlines(True),fromfile='frozen_author',tofile='portable_primary'))
diff+='\n'+''.join(difflib.unified_diff(old_body.splitlines(True),h_body.splitlines(True),fromfile='frozen_reviewer_body',tofile='portable_helper_body'))
(HERE/'COMPLETE_CHANGED_LOGIC.diff').write_text(diff)
(HERE/'sources').mkdir(exist_ok=True)
for name in ('primary','helper','builder','adaptation'):
 (HERE/'sources'/items[name].name).write_bytes(items[name].read_bytes())
out={'scope':'Static comparison only; candidate primary/helper and historical checks never imported or executed',
 'sources':sources,'adapted_source_hashes_match_request':True,
 'assertion_counts':{'author':len(asserts(trees['author_original'])),'independent':len(asserts(trees['reviewer_original']))},
 'mathematical_core_exactly_unchanged':True,'helper_body_exact_after_declared_wrapper_changes':True,
 'literal_input_count':len(inputs),'literal_inputs':list(inputs),'dynamic_manifest_records_verified':len(verified),
 'declared_input_identities_at_inspection':observed_inputs,'helper_direct_read_literals':direct_helper_reads,
 'writes':writes,'resource_calls':limits,'shared_cpu_seconds':120,
 'wall_timeout_declaration_seconds':120,'wall_enforcement_verified':False,
 'wall_qualification':'AUDIT_TIMEOUT_SEC is harness metadata; the canonical harness must enforce the shared wall limit. No candidate execution was authorized in this pass.',
 'inherited_point_state_scope_explicit':True,'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'inspection_cpu_cap_seconds':15,'inspection_elapsed_seconds':time.monotonic()-START}
(HERE/'STATIC_EVIDENCE.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'static comparisons succeeded','assertion_counts':out['assertion_counts'],
 'declared_inputs':len(inputs),'verified_manifest_records':len(verified),
 'missing_inputs':[r['path'] for r in observed_inputs if r.get('missing_at_inspection')],
 'elapsed_seconds':out['inspection_elapsed_seconds']},indent=2))
