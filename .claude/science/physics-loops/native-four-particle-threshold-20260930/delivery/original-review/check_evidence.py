import ast, difflib, gzip, hashlib, json, pathlib, subprocess, sys
from fractions import Fraction as F
ROOT=pathlib.Path('/private/tmp/toe-native-four-particle-threshold-20260930')
OUT=pathlib.Path(__file__).parent
PACK=ROOT/'.claude/science/physics-loops/native-four-particle-threshold-20260930'
sha=lambda b:hashlib.sha256(b).hexdigest()
git=lambda *a:subprocess.check_output(['git','-C',str(ROOT),*a])
paths=git('diff','--cached','--name-only','--no-renames').decode().splitlines()
assert git('write-tree').decode().strip()=='d4774b427e5c9ed059d64dd01bc5aefc636c261e'
assert not git('diff','--name-only') and not git('ls-files','--others','--exclude-standard')
inventory=json.loads((PACK/'CHANGED_PATHS.json').read_text())
assert set(paths)=={x['path'] for x in inventory['files']}
for x in inventory['files']:
 if 'sha256' in x: assert sha((ROOT/x['path']).read_bytes())==x['sha256'],x['path']
for x in json.loads((PACK/'FINAL_BINDINGS.json').read_text())['files']:
 assert sha((ROOT/x['path']).read_bytes())==x['sha256'],x['path']
for p in paths: assert (ROOT/p).read_bytes()==git('show',':'+p),p
sys.path.insert(0,str(ROOT/'scripts'))
import runner_cache as rc
caches={}
payloads={}
for name in ['native_four_particle_threshold_2026_09_30','native_four_particle_normalization_2026_09_30']:
 p='scripts/'+name+'.py'
 assert rc.declared_timeout_for(p)==180
 assert rc.cache_status(p)=='fresh'
 body=(ROOT/('logs/runner-cache/'+name+'.txt')).read_text()
 payload=json.JSONDecoder().raw_decode(body.split('----- stdout -----\n',1)[1])[0]
 caches[p]={'sha256':sha((ROOT/p).read_bytes()),'cache_status':rc.cache_status(p),'declared_inputs':rc.declared_input_paths(p),'input_fingerprint':rc.declared_input_fingerprint(p)}
 payloads[name]=payload
primary=payloads['native_four_particle_threshold_2026_09_30']
assert primary['normalization']==payloads['native_four_particle_normalization_2026_09_30']
t=primary['trial']; num=[[int(x) for x in r] for r in t['raw_upper_numerator']]
gram=[[int(x) for x in r] for r in t['residual_gram_numerator']]
assert all(num[i][j]==num[j][i] and gram[i][j]==gram[j][i] for i in range(15) for j in range(15))
assert all((num[i][j]+gram[i][j])%1920==0 for i in range(15) for j in range(15))
def ldlt(m):
 n=len(m); a=[[F(x) for x in r] for r in m]; piv=[]
 for k in range(n):
  p=a[k][k]; assert p>0,(k,p);piv.append(str(p))
  for i in range(k+1,n):
   for j in range(k+1,n): a[i][j]-=a[i][k]*a[k][j]/p
 return piv
pivots=ldlt(num)
mon=[tuple(x) for x in t['raw_monomial_order']]
pe={mon.index((0,0)):1,mon.index((0,1)):-1,mon.index((1,1)):1}
E=sum(F(num[i][j]*a*b,2*t['raw_upper_denominator']) for i,a in pe.items() for j,b in pe.items())
T=F(num[mon.index((2,2))][mon.index((2,2))],2*t['raw_upper_denominator'])
assert str(E)==t['normalized_directional_upper']['E1']
assert str(T)==t['normalized_directional_upper']['T12']
data=json.loads((ROOT/'outputs/native_four_particle_threshold_2026_09_30/compact_trial.json').read_text())
assert len(data['core'])==len(data['numerator'])==1487 and data['denominator']==65536
assert all(len(r)==15 and all(type(x)==int for x in r) for r in data['numerator'])
assert len({tuple(map(tuple,s)) for s in data['core']})==1487
mutation_summary=[]
for version in ['mutations','mutations-footer']:
 result=json.loads((PACK/version/'RESULTS.json').read_text())
 for m in result['mutations']:
  base=(ROOT/'scripts'/m['file']).read_bytes() if version.endswith('footer') else (PACK/'historical/before-footer'/f"{m['file']}.txt").read_bytes()
  assert base.count(m['old'].encode())==1
  assert sha(base.replace(m['old'].encode(),m['new'].encode()))==m['mutated_sha256']
  d=PACK/version/m['name'];r=json.loads((d/'result.json').read_text())
  assert r==m
  stderr=(d/'stderr.txt').read_bytes();stdout=(d/'stdout.txt').read_bytes()
  assert sha(stderr)==m['stderr_sha256'] and sha(stdout)==m['stdout_sha256']
  assert m['exit_code']==1 and stderr.rstrip().endswith(b'AssertionError')
  mutation_summary.append({'version':version,'name':m['name'],'mutation':(d/'mutation.txt').read_text(),'assertion':stderr.decode().splitlines()[-3:]})
history=[]
for f in (PACK/'historical/before-footer').glob('*.py.txt'):
 current=(ROOT/'scripts'/f.name.removesuffix('.txt')).read_text()
 diff=''.join(difflib.unified_diff(f.read_text().splitlines(True),current.splitlines(True)))
 history.append({'path':str(f.relative_to(ROOT)),'delta':diff})
initial=(PACK/'preexecution/INITIAL_CANONICAL_SOURCE.md').read_text()
current=(ROOT/'docs/NATIVE_FOUR_PARTICLE_THRESHOLD_BOUNDED_THEOREM_NOTE_2026-09-30.md').read_text()
history.append({'path':'preexecution/INITIAL_CANONICAL_SOURCE.md','delta':''.join(difflib.unified_diff(initial.splitlines(True),current.splitlines(True)))})
base=json.loads(git('show','HEAD:docs/audit/data/citation_graph_manifest.json'))
manifest=json.loads((ROOT/'docs/audit/data/citation_graph_manifest.json').read_text())
record={'tree':git('write-tree').decode().strip(),'paths':paths,'caches':caches,'upper_matrix_exact_positive_pivots':pivots,'upper_values':{'E':str(E),'T':str(T)},'max_trial_integer':max(abs(x) for r in data['numerator'] for x in r),'mutation_inspection':mutation_summary,'historical_deltas':history,'manifest_base_keys':list(base),'manifest_current_keys':list(manifest)}
(OUT/'EVIDENCE_INSPECTION.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'paths_bound':len(paths),'caches':caches,'upper_values':record['upper_values'],'mutation_receipts_checked':len(mutation_summary),'historical_deltas':history,'manifest_keys':list(manifest)},indent=2))
