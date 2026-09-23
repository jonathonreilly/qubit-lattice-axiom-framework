from pathlib import Path
import ast,json,hashlib,shutil,difflib,subprocess,sys,os,gzip,re
R=Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot';j=json.loads((R/'drain8173-author-prepared-v2.json').read_text());sha=lambda b:hashlib.sha256(b).hexdigest()
def dump(name,x):
 p=R/name;assert not p.exists();p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
dump('drain8173-preparation-packaging-finding-v2.json',dict(schema_version=1,kind='static-source-phrase-check-failure-not-execution',finding='Legacy FORBIDDEN substring selects the matched the explicit non-claim No primitive selects them.',primary_runs=0,simulation_runs=0,mutation_runs=0,repair='Change non-claim wording without changing its scope; preserve v2 source snapshot.'))
note=W/j['canonical_notes'][0];run=W/j['primaries'][0];before=note.read_text();oldhash=sha(note.read_bytes());s=before.replace('No primitive selects them.','No primitive supplies those choices.');assert s!=before;note.write_text(s);runbefore=run.read_text();run.write_text(runbefore.replace(oldhash,sha(note.read_bytes())));compile(run.read_text(),str(run),'exec')
rows=[dict(x,sha256=sha((W/x['path']).read_bytes())) for x in j['source']];snap=R/'drain8173-prepared-source-v3';assert not snap.exists()
for x in rows:(snap/x['path']).parent.mkdir(parents=True,exist_ok=True);shutil.copy2(W/x['path'],snap/x['path'])
j.update(source=rows,snapshot=str(snap),source_revision=3,prior_prepared_sha256=sha((R/'drain8173-author-prepared-v2.json').read_bytes()),revision_reason='N6 explicit non-claim wording avoids legacy selects the substring; pin rebound, no mathematical changes')
dump('drain8173-author-prepared-v3.json',j)
dump('drain8173-source-freeze-v3.json',dict(schema_version=1,base=j['base'],source=rows,snapshot=str(snap),prepared_sha256=sha((R/'drain8173-author-prepared-v3.json').read_bytes())))
(R/'drain8173-author-v2-to-v3.patch').write_text(''.join(difflib.unified_diff(before.splitlines(True),s.splitlines(True),fromfile=j['canonical_notes'][0]+'@v2',tofile=j['canonical_notes'][0]+'@v3'))+''.join(difflib.unified_diff(runbefore.splitlines(True),run.read_text().splitlines(True),fromfile=j['primaries'][0]+'@v2',tofile=j['primaries'][0]+'@v3')))
O=R/'drain8173-original/head';d=json.loads((R/'drain8173-review-original.json').read_text())['dispositions'];on=next(x['path'] for x in d if x['path'].startswith('docs/ADMISSIBILITY'));op=next(x['path'] for x in d if x['path'].startswith('scripts/'))
(R/'drain8173-author-corrections-v3.patch').write_text(''.join(difflib.unified_diff((O/on).read_text().splitlines(True),s.splitlines(True),fromfile=on,tofile=j['canonical_notes'][0]))+''.join(difflib.unified_diff((O/op).read_text().splitlines(True),run.read_text().splitlines(True),fromfile=op,tofile=j['primaries'][0])))
# Continue only the read-only metadata portion; no source or primary import/execution.
code=(R/'drain8173-author-discovery-v2.py').read_text().split('# Parse only; never import or run primary.',1)[1]
code=code.replace('discovery-v2.json','discovery-v3.json').replace('resource-plan-v2.json','resource-plan-v3.json').replace('prepared-v2.json','prepared-v3.json').replace('freeze-v2.json','freeze-v3.json').replace('corrections-v2.patch','corrections-v3.patch').replace('handoff-v2.json','handoff-v3.json')
exec(compile(code,'metadata-discovery-continuation','exec'))
