from pathlib import Path
import json,gzip,hashlib,subprocess,difflib
r=Path('/private/tmp/review-drain-20260915');h=r/'check8099';o=h/'original-8099';repo=r/'author-slot-one';inv=json.load(open(h/'inventory.json'));dest=repo/'docs/work_history/repo/review_feedback/pr8099-evidence';m=json.load(open(dest/'archive-manifest.json'));sha=lambda b:hashlib.sha256(b).hexdigest()
for e in m['entries']:
 b=(dest/e['stored_path']).read_bytes();assert sha(b)==e['stored_sha256']; b=gzip.decompress(b) if e['encoding']=='gzip' else b;assert b==(o/e['original_path']).read_bytes() and sha(b)==e['raw_sha256']
p=o/'.claude/science/physics-loops/local-hall-free-mixed-quartet-20260913';source=(o/inv['canonical'][1]).read_text();mut=json.load(open(p/'MUTATIONS.json')); assert mut['count']==26
for x in mut['mutations']:
 f=p/'mutation_evidence'/x['name'];b=gzip.decompress((f/'source.py.gz').read_bytes());err=gzip.decompress((f/'stderr.gz').read_bytes());assert b.decode()==source.replace(x['old'],x['new']) and sha(b)==x['mutated_sha256'] and b'AssertionError' in err and x['effective']; print(x['name'],err.decode().splitlines()[-1][:160])
changes={}
for folder in ['first_checks','expanded_checks']:
 f=p/'prior_checks'/folder;b=gzip.decompress((f/'source.py.gz').read_bytes());out=gzip.decompress((f/'stdout.gz').read_bytes()).decode();data=json.JSONDecoder().raw_decode(out[out.index('{'):])[0];assert data['source_sha256']==sha(b);assert not gzip.decompress((f/'stderr.gz').read_bytes());diff=''.join(difflib.unified_diff(b.decode().splitlines(True),source.splitlines(True)));(h/(folder+'-to-final.diff')).write_text(diff);changes[folder]={'count':data['author_check_count'],'source_sha256':sha(b),'diff':str(h/(folder+'-to-final.diff'))}
statuses=dict(line.split('\t',1)[::-1] for line in subprocess.check_output(['git','-C',str(repo),'diff','--name-status',inv['original_base'],inv['head']],text=True).splitlines());assert set(statuses)=={x['path'] for x in inv['paths']};(h/'original-statuses.json').write_text(json.dumps(statuses,indent=2)+'\n')
(h/'history-verification.json').write_text(json.dumps(dict(archive_count=len(m['entries']),all_exact=True,mutants_verified=26,prior_sources=changes,original_path_count=len(statuses),original_status_counts={v:list(statuses.values()).count(v) for v in set(statuses.values())}),indent=2)+'\n')
