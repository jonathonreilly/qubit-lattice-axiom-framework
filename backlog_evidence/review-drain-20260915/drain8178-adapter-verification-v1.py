from pathlib import Path
import ast,hashlib,json
R=Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot';h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=h(p))
files=[R/n for n in ['drain8178-build-staged-draft-v1.py','drain8178-capture-v1.py','drain8178-mutations-v1.py']]
results=[]
for p in files:
 s=p.read_text();tree=ast.parse(s);compile(s,str(p),'exec');results.append(dict(**ref(p),syntax='parsed and compiled only; no adapter main executed'))
 if 'capture' in p.name or 'mutations' in p.name:
  cold=next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='COLD_CLEARANCE_BINDING' for t in n.targets));assert ast.literal_eval(cold.value) is None
# Synthetic dual-main guard exercises the exact extracted function with stub Git;
# no checkout command or science execution occurs.
record={'source':{'base':'b','paths':[{'path':'own'}]},'inputs':{k:[] for k in ['runtime','helpers','parents','context','tooling']}}
record['inputs']['runtime']=[{'path':'input'}];record['inputs']['tooling']=[{'path':'tool'}]
guardresults=[]
for p in files[1:]:
 tree=ast.parse(p.read_text());node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='confirm_reviewed_main')
 for case,head,main,ancestor,changed,expected in [('same-main','b','b','b','',True),('disjoint-advance','b','m','b','other',True),('source-overlap','b','m','b','own',False),('runtime-overlap','b','m','b','input',False),('tool-overlap','b','m','b','tool',False),('non-descendant','b','m','other','other',False),('moved-main','b','surprise','b','other',False),('moved-head','surprise','m','b','other',False)]:
  binding={'frozen_base':'b','reviewed_main':'b' if case=='same-main' else 'm'}
  def git(*a):
   if a==('rev-parse','HEAD'):return head
   if a==('rev-parse','origin/main'):return main
   if a[0]=='merge-base':return ancestor
   if a[0]=='diff':return changed
   raise AssertionError(a)
  env={'COLD_CLEARANCE_BINDING':binding,'git':git};exec(compile(ast.Module(body=[node],type_ignores=[]),'guard-only','exec'),env)
  try:env['confirm_reviewed_main'](record,'b');accepted=True
  except AssertionError:accepted=False
  assert accepted==expected
  guardresults.append({'adapter':p.name,'case':case,'accepted':accepted,'expected':expected})
# Extract the literal capture worker, substituting a fake cache module and fake
# child result to test raw persistence before deliberate postidentity failure.
s=files[1].read_text();t=ast.parse(s);main=next(n for n in t.body if isinstance(n,ast.FunctionDef) and n.name=='main');worker=next(ast.literal_eval(n.value) for n in ast.walk(main) if isinstance(n,ast.Assign) and any(isinstance(x,ast.Name) and x.id=='worker' for x in n.targets))
wt=ast.parse(worker);preserve=next(n for n in wt.body if isinstance(n,ast.FunctionDef) and n.name=='preserve')
fake={'runner':'synthetic','status':'ok','exit_code':0,'stdout':'SYNTHETIC raw stdout\n','stderr':'SYNTHETIC stderr\n','elapsed_sec':0,'timeout_sec':60};raw=R/'drain8178-synthetic-identity-drift-v1.raw-result.json';calls=[]
class Args:argv=['synthetic','','','',str(raw)]
def original(path,timeout_sec):calls.append((path,timeout_sec));return fake
env={'Path':Path,'sys':Args,'json':json,'original':original};exec(compile(ast.Module(body=[preserve],type_ignores=[]),'wrapper-only','exec'),env)
returned=env['preserve']('synthetic',60)
try:
 assert returned is fake
 raise ValueError('SYNTHETIC post-run source identity changed before cache publication')
except ValueError as e:error=str(e)
assert json.loads(raw.read_text())==fake and calls==[('synthetic',60)]
owned=json.loads((R/'drain8178-prepared-v1-source-freeze.json').read_text())['files'];assert all(h(W/e['path'])==e['sha256'] for e in owned)
report={'adapters':results,'cold_binding':None,'syntax_only':True,'guard_controls':guardresults,'synthetic_identity_drift':{'error':error,'raw_result':ref(raw),'actual_child_calls':0,'fake_result_calls':len(calls),'preserved_before_rejection':True},'owned_source_unchanged':True,'science_executions':0,'staging':0,'known_staging_hold':'Actual Type extractor returns None for frozen note; builder rejects before staging. Add explicit Type metadata only under root direction and obtain affected confirmation/new freeze and builder revision.','vocabulary':ref(R/'drain8178-vocab-verification-v1.json')}
with (R/'drain8178-proposed-adapters-v1.json').open('x') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({'report':ref(R/'drain8178-proposed-adapters-v1.json'),'adapters':results},indent=2))
