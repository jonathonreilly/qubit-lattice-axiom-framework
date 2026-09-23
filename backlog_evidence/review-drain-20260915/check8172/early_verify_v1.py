import pathlib,json,hashlib,tarfile,gzip,io,stat,subprocess,time,ast
R=pathlib.Path('/private/tmp/review-drain-20260915'); W=R/'review-meta-slot'; E=W/'docs/work_history/repo/review_feedback/pr8172-evidence';h=lambda b:hashlib.sha256(b).hexdigest();start=time.monotonic()
hand=R/'drain8172-author-handoff-v1.json';assert h(hand.read_bytes())=='f8d2b559198e14560627ff6b0b76afb3a77eb3278ce72640ff11172007dcc47c'
for ref in json.loads(hand.read_text())['references']:assert h(pathlib.Path(ref['path']).read_bytes())==ref['sha256'],ref
f=json.loads((R/'drain8172-prepared-v1-source-freeze.json').read_text())['files']
for r in f:
 p=W/r['path'];assert h(p.read_bytes())==r['sha256'];assert p.read_bytes()==pathlib.Path(r['immutable_copy']).read_bytes();assert oct(stat.S_IMODE(p.stat().st_mode))==r['mode']
orig=json.loads((R/'drain8172-original/inventory.json').read_text()); old={x['path']:x['original'] for x in orig['paths']}
man=json.loads((E/'archive-manifest.json').read_text())['entries'];assert set(old)=={x['original_path'] for x in man}
for x in man:
 raw=(E/x['stored_path']).read_bytes();assert h(raw)==x['stored_sha256'];raw=gzip.decompress(raw) if x['encoding']=='gzip' else raw
 o=old[x['original_path']];assert h(raw)==x['raw_sha256']==o['sha256'];assert x['original_mode']==o['mode'];assert x['git_blob']==o['blob']
raw=gzip.decompress((E/'complete-inherited-packet.tar.gz').read_bytes());assert raw==(R/'drain8172-original/complete-inherited-packet.tar').read_bytes()
inv=json.loads((E/'complete-packet-inventory.json').read_text());dif=[]
with tarfile.open(fileobj=io.BytesIO(raw)) as tf:
 assert {m.name for m in tf.getmembers() if m.isfile()}=={x['path'] for x in inv}
 for x in inv:
  m=tf.getmember(x['path']);assert m.isfile();b=tf.extractfile(m).read();assert h(b)==x['sha256'];assert b==subprocess.check_output(['git','cat-file','blob',x['blob']],cwd=W)
  target=R/'check8172/mode-restoration-v1'/x['path'];target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(b);target.chmod(int(x['mode'],8)&0o777);assert stat.S_IMODE(target.stat().st_mode)==int(x['mode'],8)&0o777
  if m.mode!=(int(x['mode'],8)&0o777):dif.append({'path':x['path'],'tar':oct(m.mode),'git':x['mode']})
runner=next(W/x['path'] for x in f if x['path'].startswith('scripts/'))
oldrunner=next(pathlib.Path(x['original']['snapshot']) for x in orig['paths'] if x['path'].startswith('scripts/'))
def defs(p):return {n.name:ast.dump(n,include_attributes=False) for n in ast.parse(p.read_text()).body if isinstance(n,(ast.FunctionDef,ast.ClassDef))}
a,b=defs(oldrunner),defs(runner);same=[k for k in a.keys()&b.keys() if a[k]==b[k]]
plan=json.loads((R/'drain8172-author-input-resource-plan-v1.json').read_text())
for x in plan['ordered_inputs']+plan['context_only']:assert h((W/x['path']).read_bytes())==x['sha256']
# Independently validate proof's recentered bound using actual predecessor sets, no source function execution.
from itertools import combinations
basis=[(0,0,0),(1,0,-1),(0,1,-1),(-1,0,1)]
for n in range(1,5):
 for I in combinations(basis,n):
  for v in [(0,0,0),(100,-100,0),(-73,19,54)]:
   J=[tuple(a+b for a,b in zip(i,v)) for i in I];origin=J[0];J=[tuple(a-b for a,b in zip(i,origin)) for i in J];M=[max(i[k] for i in J) for k in range(3)];D=sum(M);assert min(M)>=0 and max(M)<=D
   assert 18*(D+1)**3-(D+1)*(6*D+5)*(6*D+4)//2==(D+1)*(9*D+8)
result={'status':'VERIFIED','frozen_files':len(f),'original_recoveries':len(man),'tar_members':len(inv),'mode_restoration_test':'all bytes and Git modes recovered in scratch','tar_header_mode_differences':dif,'unchanged_AST_definitions':sorted(same),'primary_executed':False,'elapsed_seconds':time.monotonic()-start,'limits':'Fixed 31 files,24 payloads,79 tar entries and45 translated subsets; tool yield1000ms is not wall limit; no explicit resource cap imposed; no failure or timeout.'}
(R/'check8172/early_verify_v1.json').write_text(json.dumps(result,indent=2));print({k:v for k,v in result.items() if k!='tar_header_mode_differences'})
