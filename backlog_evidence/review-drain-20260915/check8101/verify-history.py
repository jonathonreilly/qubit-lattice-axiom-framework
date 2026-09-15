from pathlib import Path
import json,gzip,hashlib,subprocess,ast,difflib
r=Path('/private/tmp/review-drain-20260915');h=r/'check8101';o=h/'original-8101';repo=r/'author-slot-one';inv=json.load(open(h/'inventory.json'));dest=repo/'docs/work_history/repo/review_feedback/pr8101-evidence';m=json.load(open(dest/'archive-manifest.json'));sha=lambda b:hashlib.sha256(b).hexdigest()
for e in m['entries']:
 b=(dest/e['stored_path']).read_bytes();assert sha(b)==e['stored_sha256'];b=gzip.decompress(b) if e['encoding']=='gzip' else b;assert b==(o/e['original_path']).read_bytes() and sha(b)==e['raw_sha256']
p=o/'.claude/science/physics-loops/finite-link-weak-coupling-payload-20260913';source=(o/inv['canonical'][1]).read_text();mut=json.load(open(p/'MUTATIONS.json'));assert len(mut['mutations'])==18
tr=ast.parse((p/'run_mutations.py').read_text());spec=next(ast.literal_eval(n.value) for n in tr.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='mutations' for t in n.targets));spec={n:(a,b) for n,a,b in spec}
for x in mut['mutations']:
 name=x['name'];b=gzip.decompress((p/'mutations'/(name+'.source.py.gz')).read_bytes());err=gzip.decompress((p/'mutations'/(name+'.stderr.gz')).read_bytes());a,c=spec[name];assert b.decode()==source.replace(a,c) and sha(b)==x['source_sha256'] and b'AssertionError' in err and x['effective_mathematical_failure'];print(name,err.decode().splitlines()[-1][:160])
for f in p.rglob('*.gz'):gzip.decompress(f.read_bytes())
print('prior files',[str(f.relative_to(p)) for f in p.rglob('*') if f.is_file() and 'prior' in str(f.relative_to(p))])
statuses=dict(line.split('\t',1)[::-1] for line in subprocess.check_output(['git','-C',str(repo),'diff','--name-status',inv['original_base'],inv['head']],text=True).splitlines());assert set(statuses)=={x['path'] for x in inv['paths']};(h/'original-statuses.json').write_text(json.dumps(statuses,indent=2)+'\n');(h/'history-verification.json').write_text(json.dumps(dict(archive_count=len(m['entries']),all_exact=True,mutants_verified=18,original_path_count=len(statuses),original_status_counts={v:list(statuses.values()).count(v) for v in set(statuses.values())}),indent=2)+'\n')
