from pathlib import Path
import json,hashlib,gzip,ast,subprocess
R=Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot';sha=lambda b:hashlib.sha256(b).hexdigest();hp=R/'drain8178-author-handoff-v1.json'
assert sha(hp.read_bytes())=='5947a729c010796ac94f840ea02b37bde2835e793df67759b3b985c494bdb541';h=json.loads(hp.read_text())
for e in h['source_files']:assert sha((W/e['path']).read_bytes())==e['sha256'] and len((W/e['path']).read_bytes())==e['bytes']
for e in h['references']:assert sha(Path(e['path']).read_bytes())==e['sha256']
a=W/'docs/history/pr8178-torus-auxiliary-recovery';m=json.loads((a/'pr8178-original-identities.json').read_text());orig=json.loads((R/'drain8178-original/manifest.json').read_text());assert m['original_manifest']==orig
count=0
for e in m['recovery']:
 for kind,s in e['states'].items():
  if s is None:continue
  b=(W/s['recovery_path']).read_bytes();assert sha(b)==s['container_sha256'];raw=gzip.decompress(b);assert sha(raw)==s['sha256'] and len(raw)==s['bytes'];assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==s['blob'];assert raw==Path(s['snapshot']).read_bytes();count+=1
assert gzip.decompress((W/m['delta']['path']).read_bytes())==(R/'drain8178-original/original.delta').read_bytes()
original_note=next(e for e in orig['entries'] if e['path'].startswith('docs/ADMISSIBILITY'))
raw=Path(original_note['head']['snapshot']).read_text();deferred=(a/'pr8178-deferred-science.md').read_text();assert raw in deferred
new=W/'scripts/supplied_torus_auxiliary_field_mode_variance_finite_bracket_2026_09_17.py';old=next((R/'drain8178-original/head/scripts').glob('*.py'))
def funcs(p):return {n.name:ast.dump(n,include_attributes=False) for n in ast.parse(p.read_text()).body if isinstance(n,ast.FunctionDef)}
f,g=funcs(old),funcs(new);unchanged=[k for k in f if k in g and f[k]==g[k]]
parent=W/'docs/SPHERE_LEVEL_KERNEL_MOMENTS_WALK_LOCAL_LIMIT_AND_FINITE_PLANE_MIXING_BOUNDED_THEOREM_NOTE_2026-09-16.md';assert sha(parent.read_bytes())=='bd7968234832dcd13368f4208b2081a69aaf9674b1e9b24b65f44ee986f26b0a'
assert subprocess.check_output(['git','-C',str(W),'rev-parse','HEAD'],text=True).strip()==h['base']
assert not subprocess.check_output(['git','-C',str(W),'diff','--name-only'])
assert not subprocess.check_output(['git','-C',str(W),'diff','--cached','--name-only'])
result=dict(status='identities verified only; no science execution or gate',source_count=len(h['source_files']),recovered_states=count,original_paths=len(m['recovery']),unchanged_function_ast=unchanged,parent_sha256=sha(parent.read_bytes()),handoff_sha256=sha(hp.read_bytes()))
(R/'check8178/early-v1-identities.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
