from pathlib import Path
import json,gzip,hashlib,subprocess,ast,difflib
r=Path('/private/tmp/review-drain-20260915');h=r/'check8104';o=h/'original-8104';repo=r/'author-slot-one';inv=json.load(open(h/'inventory.json'));dest=repo/'docs/work_history/repo/review_feedback/pr8104-evidence';m=json.load(open(dest/'archive-manifest.json'));sha=lambda b:hashlib.sha256(b).hexdigest()
for e in m['entries']:
 b=(dest/e['stored_path']).read_bytes();assert sha(b)==e['stored_sha256'];b=gzip.decompress(b) if e['encoding']=='gzip' else b;assert b==(o/e['original_path']).read_bytes() and sha(b)==e['raw_sha256']
p=o/'.claude/science/physics-loops/flat-holonomy-spectral-floor-20260913';source=(o/inv['canonical'][1]).read_text();tr=ast.parse((p/'verify_block15.py').read_text());spec=next(ast.literal_eval(n.value) for n in tr.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='mutations' for t in n.targets));spec={n:(a,b) for n,a,b in spec};mut=json.load(open(p/'MUTATIONS.json'));assert len(mut['mutations'])==14
for base in [p]:
 data=json.load(open(base/'MUTATIONS.json'));src=source if base==p else gzip.decompress((base/'primary.py.gz').read_bytes()).decode()
 for x in data['mutations']:
  n=x['name'];b=gzip.decompress((base/'mutations'/(n+'.py.gz')).read_bytes());err=gzip.decompress((base/'mutations'/(n+'.stderr.gz')).read_bytes());a,c=spec[n];assert b.decode()==src.replace(a,c,1) and sha(b)==x['source_sha256'];print(base.name,n,err.decode().splitlines()[-1][:180])
for f in p.rglob('*.gz'):gzip.decompress(f.read_bytes())
d=''.join(difflib.unified_diff((p/'BLOCK15_DERIVATION.md').read_text().splitlines(True),(o/inv['canonical'][0]).read_text().splitlines(True)));(h/'derivation-to-note.diff').write_text(d)
statuses=dict(line.split('\t',1)[::-1] for line in subprocess.check_output(['git','-C',str(repo),'diff','--name-status',inv['original_base'],inv['head']],text=True).splitlines());assert set(statuses)=={x['path'] for x in inv['paths']};(h/'original-statuses.json').write_text(json.dumps(statuses,indent=2)+'\n');(h/'history-verification.json').write_text(json.dumps(dict(archive_count=len(m['entries']),all_exact=True,mutants_verified=14,original_path_count=len(statuses),original_status_counts={v:list(statuses.values()).count(v) for v in set(statuses.values())}),indent=2)+'\n')
