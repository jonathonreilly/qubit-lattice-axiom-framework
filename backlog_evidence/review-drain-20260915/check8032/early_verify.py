from pathlib import Path
import json,hashlib,gzip,subprocess,ast,os,time,traceback
r=Path('/private/tmp/review-drain-20260915');w=r/'review-meta-slot';out={}
def h(b):return hashlib.sha256(b).hexdigest()
def load(n):return json.loads((r/n).read_text())
f=load('drain8032-prepared-v1-source-freeze.json');handoff=load('drain8032-author-handoff-v1.json');orig=load('drain8032-original/manifest.json');mapping=load('drain8032-author-full-mapping-v1.json')
for e in f['files']:
 assert h((w/e['path']).read_bytes())==e['sha256']==h(Path(e['immutable_copy']).read_bytes())
 assert oct((w/e['path']).stat().st_mode&0o777)==e['mode']
for e in handoff['references']:assert h(Path(e['path']).read_bytes())==e['sha256']
for e in handoff['current_context']:
 assert h((w/e['path']).read_bytes())==e['sha256']==e['original_review_sha256']
 assert subprocess.check_output(['git','show',f['base']+':'+e['path']],cwd=w)==(w/e['path']).read_bytes()
assert {e['original_path'] for e in mapping}=={e['path'] for e in orig['entries']}
by={e['path']:e for e in orig['entries']}
for e in mapping:
 b=(w/e['recovery']).read_bytes();assert h(b)==e['recovery_sha256'];raw=gzip.decompress(b) if e['recovery_encoding']=='gzip' else b
 old=by[e['original_path']]['head'];assert h(raw)==e['original_sha256']==old['sha256'];assert e['original_blob']==old['blob'];assert e['original_mode']==old['mode']
 assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==e['original_blob']
base=w/'docs/work_history/repo/review_feedback/pr8032-evidence';a=json.loads((base/'pr8032-archive-manifest.json').read_text());d=a['delta'];assert h(gzip.decompress((base/d['path']).read_bytes()))==orig['delta_sha256']
p=load('drain8032-author-prepared-v1.json');cid='gauge_wilson_finite_pw_static_source_energy_upper_bound_bounded_theorem_note_2026-09-07'
def registry(b):
 t=ast.parse(b);return next(ast.literal_eval(n.value) for n in t.body if isinstance(n,ast.Assign) and any(isinstance(v,ast.Name) and v.id=='EXPLICIT_PACKET_HELPER_RUNNER_PATHS' for v in n.targets))
for e in p['registry_proposals']:
 old=(w/e['path']).read_bytes();new=Path(e['proposed']['path']).read_bytes();assert h(old)==e['current_sha256'];assert h(new)==e['proposed']['sha256'];a,b=registry(old),registry(new);assert cid not in a;assert b.pop(cid)==e['change'][cid];assert a==b
# No primary or helper code execution. Compare exact scientific body AST only.
for e in p['runners']:
 old=(r/'drain8032-original/head'/e['path']).read_text();new=(w/e['path']).read_text()
 marker='import time,resource,json,hashlib,itertools' if 'controls_' in e['path'] else 'from fractions import Fraction as F'
 assert ast.dump(ast.parse(old[old.index(marker):old.rindex('_emit(result')]))==ast.dump(ast.parse(new[new.index(marker):new.rindex('_emit(result')]))
# Reproduce only changed _emit IO against a synthetic one-check value in external directory.
source=w/p['runners'][0]['path'];tree=ast.parse(source.read_text());node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='_emit')
testdir=r/'check8032/io-v1';testdir.mkdir(exist_ok=True)
ns={'Path':Path,'json':json,'sys':type('S',(),{'argv':['synthetic']})(),'time':time,'_started':time.monotonic(),'_rss':lambda:1,'AUDIT_RSS_LIMIT_MIB':180,'AUDIT_TIMEOUT_SEC':180,'_input_sha256':{},'_finite':lambda x:None,'_REPO_ROOT':testdir,'__file__':'synthetic_emit.py','signal':type('S',(),{'alarm':lambda *a:None})()}
exec(compile(ast.Module(body=[node],type_ignores=[]),str(source),'exec'),ns)
fake={'TOTAL':1,'checks':['synthetic'],'seconds':0,'rss_MiB':1,'source_sha256':'synthetic'};scopes={'per_element':{'checks':1,'scope':'synthetic IO control only'}}
ns['_emit'](fake.copy(),1,scopes)
try:ns['_emit'](fake.copy(),1,scopes)
except FileExistsError as exc:out['second_emit']='FileExistsError as predicted';out['raw_traceback']=traceback.format_exc();print(out['raw_traceback'])
else:raise AssertionError('expected exclusive-write failure')
out.update(source_count=len(f['files']),original_roundtrips=len(mapping),context_pins=len(handoff['current_context']),registry_proposals_preserve_existing=True,science_AST_unchanged=True,primary_runs=0,helper_runs=0,base=f['base'])
(r/'drain8032-early-verification-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
