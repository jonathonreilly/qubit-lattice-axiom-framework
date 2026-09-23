from pathlib import Path
import json,hashlib,ast,difflib,shutil
R=Path('/private/tmp/review-drain-20260915');W=R/'review-meta-slot';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();v=json.loads((R/'drain8166-author-prepared-v2.json').read_text());assert all(sha(R/'drain8166-prepared-source-v2'/e['path'])==e['sha256'] for e in v['source']);patch='' 
for i,row in enumerate(v['notes']):
 p=row['primary'];old=(R/'drain8166-prepared-source-v2'/p).read_text();s=old
 s=s.replace('finite matrix covariance and response','finite matrix covariance entries and static response comparisons').replace('finite4D chains and witness memberships','finite four-dimensional chains and witness membership counts').replace('adjacent-face bridge fixtures','declared finite adjacent-face bridge fixtures only').replace('finite periodic spatial side4 fixture','finite periodic spatial side4 fixture with declared time slices').replace('periodic spatial side4 fixture','finite periodic spatial side4 fixture with declared time slices').replace('three completed diagnostic families','three completed finite diagnostic families; no exhaustive theorem execution').replace('five completed diagnostic families','five completed finite diagnostic families; no exhaustive theorem execution').replace('scalar clipped extension derivatives','finite scalar clipped-extension derivative and matching checks').replace('one-face and two-adjacent-face fixtures only','one-face and two-adjacent-face finite bridge fixtures only').replace('finite time Fourier carrier','finite time Fourier carrier identities on the declared slice counts').replace('finite seeded currents and fixed80-digit arithmetic','checked and not executed; no spectral decomposition is performed by this integer-chain program')
 assert s!=old;p0=W/p;p0.write_text(s)
 patch+=''.join(difflib.unified_diff(old.splitlines(True),s.splitlines(True),fromfile=p+'@v2',tofile=p+'@v3'))
 # Every N5 body must now be substantive and >=40 characters.
 tree=ast.parse(s);emit=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='_emit_completed');loop=next(x for x in emit.body if isinstance(x,ast.For));scopes=ast.literal_eval(loop.iter);assert all(len(body)>=40 for _,body in scopes),scopes
 v['runtime_plan'][i]['N5_scopes']=dict(scopes)
# Bridge reporting changed helper bytes; bind exact new helper while preserving all math.
p=v['notes'][1]['primary'];old=(W/p).read_text();helper=v['notes'][0]['primary'];oldhelper=next(e['sha256'] for e in v['source'] if e['path']==helper);s=old.replace(oldhelper,sha(W/helper));assert s!=old;(W/p).write_text(s);patch+=''.join(difflib.unified_diff(old.splitlines(True),s.splitlines(True),fromfile=p+'@v3-wrapper',tofile=p+'@v3-final'))
v['source']=[dict(e,sha256=sha(W/e['path'])) for e in v['source']];v['status']='Untracked preparation v3; reporting-only N5 corrections, confirmation pending'
for plan in v['runtime_plan']:
 plan['runtime_inputs']=[dict(e,sha256=sha(W/e['path'])) for e in plan['runtime_inputs']]
 if 'transitive_runtime_inputs' in plan:plan['transitive_runtime_inputs']=plan['runtime_inputs']
(R/'drain8166-author-prepared-v3.json').write_text(json.dumps(v,indent=2)+'\n');(R/'drain8166-source-freeze-v3.json').write_text(json.dumps(v['source'],indent=2)+'\n');(R/'drain8166-author-corrections-v3.patch').write_text(patch);(R/'drain8166-resource-input-plan-v3.json').write_text(json.dumps(v['runtime_plan'],indent=2)+'\n');snap=R/'drain8166-prepared-source-v3';assert not snap.exists()
for e in v['source']:
 q=snap/e['path'];q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(W/e['path'],q)
print(sha(R/'drain8166-author-prepared-v3.json'))
