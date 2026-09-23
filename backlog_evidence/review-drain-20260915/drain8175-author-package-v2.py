from pathlib import Path
import json,hashlib,shutil,difflib,ast
R=Path('/private/tmp/review-drain-20260915');W=R/'drain-author-slot';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def dump(n,x):
 p=R/n;assert not p.exists();p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
j=json.loads((R/'drain8175-author-prepared-v1.json').read_text());mp=W/j['original_manifest']['path'];m=json.loads(mp.read_text());renames={}
for e in m['entries']:
 old=e['recovery']['path'];p=Path(old);new=str(p.with_name('pr8175-'+p.name));assert not (W/new).exists();(W/old).rename(W/new);e['recovery']['path']=new;renames[old]=new
mp.write_text(json.dumps(m,indent=2,ensure_ascii=False)+'\n')
note=W/j['canonical_notes'][0];run=W/j['primaries'][0];before=note.read_text();oldpin=sha(note)
changes={'counts16/10/1,20/12/1,23/12/2':'counts 16/10/1, 20/12/1, 23/12/2','periods2/1/1':'periods 2/1/1','ratios8/5,5/3,5/3':'ratios 8/5, 5/3, 5/3','counts2,1,1':'counts 2, 1, 1','remains20checks':'remains 20 checks','has27nodes,10refinements and10bad':'has 27 nodes, 10 refinements and 10 bad','has33nodes,12refinements and12bad':'has 33 nodes, 12 refinements and 12 bad','has37nodes,13refinements':'has 37 nodes, 13 refinements','12bad pairs':'12 bad pairs','has300cones of depths3through8':'has 300 cones of depths 3 through 8','historical40000-cone':'historical 40,000-cone','least1':'least 1','between8and10':'between 8 and 10','constant2':'constant 2','below2':'below 2','seeded300-cone':'seeded 300-cone','not20 independent':'not 20 independent'}
body=before
for a,b in changes.items():body=body.replace(a,b)
note.write_text(body);r0=run.read_text();run.write_text(r0.replace(oldpin,sha(note)));compile(run.read_text(),str(run),'exec')
rows=[]
for x in j['source']:
 p=renames.get(x['path'],x['path']);rows.append(dict(path=p,mode=x['mode'],sha256=sha(W/p)))
rows.sort(key=lambda x:x['path']);snap=R/'drain8175-prepared-source-v2';assert not snap.exists()
for x in rows:(snap/x['path']).parent.mkdir(parents=True,exist_ok=True);shutil.copy2(W/x['path'],snap/x['path'])
j.update(source=rows,snapshot=str(snap),source_revision=2,original_manifest=dict(path=j['original_manifest']['path'],sha256=sha(mp)),prior_prepared_sha256=sha(R/'drain8175-author-prepared-v1.json'),revision_reason='Prefix every archive basename with pr8175 after ALL-docs collision scan found generic gzip basenames shared with other units; prose spacing/pin only, no math change')
dump('drain8175-author-prepared-v2.json',j);dump('drain8175-source-freeze-v2.json',dict(schema_version=1,source=rows,base=j['base'],snapshot=str(snap),prepared_sha256=sha(R/'drain8175-author-prepared-v2.json')))
d=json.loads((R/'drain8175-author-dispositions-v1.json').read_text());d['constituents'][0]['dispositions']=m['entries'];dump('drain8175-author-dispositions-v2.json',d)
dump('drain8175-preparation-collision-finding-v1.json',dict(schema_version=1,kind='static-preparation-packaging-failure-not-science-execution',finding='Initial markdown/text-only scan passed, but requested ALL new docs scan detected shared generic gzip basenames.',repair='Every original archive now has pr8175-prefixed unique basename; original gzip bytes/raw modes/blob identities unchanged.',renames=renames,source_runs=0))
O=R/'drain8175-original/head';orig=json.loads((R/'drain8175-review-original.json').read_text())['path_dispositions'];on=next(x['path'] for x in orig if x['path'].startswith('docs/ADMISSIBILITY'));op=next(x['path'] for x in orig if x['path'].startswith('scripts/'))
(R/'drain8175-author-corrections-v2.patch').write_text(''.join(difflib.unified_diff((O/on).read_text().splitlines(True),body.splitlines(True),fromfile=on,tofile=j['canonical_notes'][0]))+''.join(difflib.unified_diff((O/op).read_text().splitlines(True),run.read_text().splitlines(True),fromfile=op,tofile=j['primaries'][0])))
(R/'drain8175-author-v1-to-v2.patch').write_text(''.join(difflib.unified_diff(before.splitlines(True),body.splitlines(True),fromfile='note@v1',tofile='note@v2'))+''.join(difflib.unified_diff(r0.splitlines(True),run.read_text().splitlines(True),fromfile='runner@v1',tofile='runner@v2')))
code=(R/'drain8175-author-discovery-v1.py').read_text().replace('prepared-v1.json','prepared-v2.json').replace('freeze-v1.json','freeze-v2.json').replace('dispositions-v1.json','dispositions-v2.json').replace('corrections-v1.patch','corrections-v2.patch').replace('discovery-v1.json','discovery-v2.json').replace('resource-plan-v1.json','resource-plan-v2.json').replace('handoff-v1.json','handoff-v2.json')
exec(compile(code,'metadata-discovery-v2','exec'))
