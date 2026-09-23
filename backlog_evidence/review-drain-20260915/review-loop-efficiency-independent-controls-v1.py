import ast,contextlib,copy,hashlib,io,json,types,time,subprocess
from pathlib import Path
R=Path('/private/tmp/review-drain-20260915'); P=R/'review-loop-efficiency-proposal-v1'; W=R/'review-meta-slot'; S=Path('/Users/jonBridger/.codex/skills/review-loop')
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
results=[]
def record(case,actual,expected):
 assert actual==expected,(case,actual,expected)
 results.append(dict(case=case,actual=actual,expected=expected))
manifest=json.loads((P/'manifest.json').read_text())
for f in manifest['files']:
 record('before hash '+f['path'],h(S/f['path']),f['before_sha256']);record('after hash '+f['path'],h(P/f['path']),f['after_sha256'])
for ref in json.loads((P/'evidence.json').read_text())['references']:record('evidence '+ref['path'],h(Path(ref['path'])),ref['sha256'])
# Extract only actual guard, never import or execute capture main or science.
cap=R/'drain8032-capture-v3.py'; t=ast.parse(cap.read_text()); guard=next(n for n in t.body if isinstance(n,ast.FunctionDef) and n.name=='confirm_reviewed_main')
rec={'source':{'base':'base','paths':[{'path':'docs/source.md'}]},'inputs':{k:[{'path':k+'.dat'}] for k in ('runtime','helpers','parents','context','tooling')}}
state=dict(head='base',main='main',ancestor='base',changed=['unrelated.md'])
def git(*a):
 if a==('rev-parse','HEAD'):return state['head']
 if a==('rev-parse','origin/main'):return state['main']
 if a[0]=='merge-base':return state['ancestor']
 if a[0]=='diff':return '\n'.join(state['changed'])
 raise AssertionError(a)
g={'git':git,'COLD_CLEARANCE_BINDING':{'frozen_base':'base','reviewed_main':'main'}}
exec(compile(ast.Module(body=[guard],type_ignores=[]),str(cap),'exec'),g)
def allowed():
 try:g['confirm_reviewed_main'](rec,'base');return True
 except AssertionError:return False
record('different frozen base and reviewed main, unrelated paths',allowed(),True)
for path in ['docs/source.md']+[k+'.dat' for k in rec['inputs']]:
 state['changed']=[path];record('overlap '+path,allowed(),False)
state['changed']=['unrelated.md']
for key,value in [('main','moved'),('head','wrong'),('ancestor','other')]:
 old=state[key];state[key]=value;record(key+' movement',allowed(),False);state[key]=old
# Semantic completeness is a human gate: disjoint paths do not grant it.
record('disjoint new consumer changes meaning: mechanical path guard',allowed(),True)
record('disjoint new consumer changes meaning: full proposed guidance holds', 'holds: changed interactions requires renewed review' if 'Movement,\noverlap or changed interactions holds' in (P/'references/REVIEW_UNITS.md').read_text() else 'missing','holds: changed interactions requires renewed review')
# Synthetic output only from isolated actual emitter AST.
D=R/'review-loop-efficiency-independent-io-v1';D.mkdir(exist_ok=False); repo=D/'repo';repo.mkdir();canonical=repo/'canonical.json';canonical.write_text('prior canonical artifact')
runner=W/'scripts/gauge_wilson_finite_pw_charged_energy_controls_2026_09_07.py';tree=ast.parse(runner.read_text());nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('_emit','_finite')]
import math
ns=dict(Path=Path,json=json,math=math,os=types.SimpleNamespace(environ={}),sys=types.SimpleNamespace(argv=['runner']),time=types.SimpleNamespace(monotonic=lambda:1),signal=types.SimpleNamespace(alarm=lambda x:None),_rss=lambda:1,_started=0,AUDIT_RSS_LIMIT_MIB=180,AUDIT_TIMEOUT_SEC=180,_input_sha256={},_REPO_ROOT=repo,__file__='runner.py')
exec(compile(ast.Module(body=nodes,type_ignores=[]),str(runner),'exec'),ns)
scopes={'synthetic':{'checks':1,'scope':'IO only'}}
out={'TOTAL':1,'checks':['synthetic'],'seconds':1,'rss_MiB':1,'source_sha256':'synthetic'}
for argv in ([],[],['--json'],['--json']):
 ns['sys'].argv=['runner']+argv
 with contextlib.redirect_stdout(io.StringIO()) as buf:ns['_emit'](copy.deepcopy(out),1,scopes)
 record('repeat output '+str(argv),bool(buf.getvalue()),True);record('canonical preserved '+str(argv),canonical.read_text(),'prior canonical artifact')
side=D/'side.json';ns['os'].environ['AUDIT_RESULT_SIDECAR']=str(side)
with contextlib.redirect_stdout(io.StringIO()):ns['_emit'](copy.deepcopy(out),1,scopes)
prior=side.read_bytes()
try:ns['_emit'](copy.deepcopy(out),1,scopes);collision=False
except FileExistsError:collision=True
record('prior sidecar collision rejected',collision,True);record('prior sidecar preserved',side.read_bytes()==prior,True)
# Execute only actual cache wrapper with fake execute_runner; preserve raw first,
# then force the actual later identity rejection branch. No scientific program.
c=W/'scripts/runner_cache.py';node=next(n for n in ast.parse(c.read_text()).body if isinstance(n,ast.FunctionDef) and n.name=='execute_and_write_cache');raw=D/'raw.json';calls=[]
def fake_runner(*args,**kwargs):
 calls.append('synthetic IO return');r={'status':'ok','exit_code':0,'stdout':'synthetic partial/result'}
 with raw.open('x') as f:json.dump(r,f)
 return r
identities=iter(['before','after']);cache_ns={'Path':Path,'capture_runner_execution_identity':lambda p:next(identities),'execute_runner':fake_runner,'live_log_path_for':lambda p:D/'absent-live','RunnerIdentityChangedError':RuntimeError,'write_cache':lambda *a,**k: (_ for _ in ()).throw(AssertionError('must not write success cache'))}
exec(compile(ast.Module(body=[node],type_ignores=[]),str(c),'exec'),cache_ns)
try:cache_ns['execute_and_write_cache']('fake',1);rejected=False
except RuntimeError:rejected=True
record('later API identity failure rejected',rejected,True);record('raw return survives later API rejection',json.loads(raw.read_text())['stdout'],'synthetic partial/result');record('synthetic invocation count',len(calls),1)
# Verify compact original recovery inventory against immutable Git endpoints.
inv=json.loads((R/'drain8174-original/inventory.json').read_text()); delta=subprocess.check_output(['git','-C',str(W),'diff','--name-only','--no-renames',inv['base'],inv['head']],text=True).splitlines();record('complete original path inventory',sorted(x['path'] for x in inv['paths']),sorted(delta))
for row in inv['paths']:
 for endpoint in ('base','head','main'):
  if row[endpoint]:
   b=subprocess.check_output(['git','-C',str(W),'show',inv[endpoint]+':'+row['path']]);assert hashlib.sha256(b).hexdigest()==row[endpoint+'_sha256'];assert (R/'drain8174-original'/endpoint/row['path']).read_bytes()==b
record('original endpoint snapshots verified',True,True)
result={'status':'passed','science_executions':0,'pipeline_executions':0,'checks':results,'sources':[{'path':str(p),'sha256':h(p)} for p in [cap,runner,c,S/'scripts/review_receipt.py',W/'docs/audit/scripts/repo_invariants_check.py']]}
(R/'review-loop-efficiency-independent-controls-v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':'passed','checks':len(results)}))
