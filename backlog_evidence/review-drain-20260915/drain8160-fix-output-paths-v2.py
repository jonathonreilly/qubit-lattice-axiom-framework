from pathlib import Path
import json,hashlib,subprocess,ast,difflib,shutil
b=Path(__file__).resolve().parent;w=b/'drain-author-slot';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=sha(p));git=lambda *a:subprocess.check_output(['git','-C',str(w),*a],text=True).strip()
dp=b/'drain8160-author-unit-draft-v1.json';d=json.loads(dp.read_text());assert git('write-tree')==d['source']['tree'];assert not git('diff','--name-only')
for e in d['source']['paths']:assert sha(w/e['path'])==e['sha256'],e['path']
raw=w/'scripts/rotor_uniform_compact_response_check_2026_09_16.json';saved=b/'drain8160-failed-run1-structured-output.json';assert raw.exists() and not saved.exists();shutil.copy2(raw,saved);assert sha(raw)==sha(saved);raw.unlink()
plan=json.loads((b/'drain8160-capture-plan-v1.json').read_text());patch=[];changes=[];preserve=b/'drain8160-output-fix-originals';assert not preserve.exists();preserve.mkdir()
for x in plan['executions']:
 p=x['runner'];old=(w/p).read_text();patterns=['Path(__file__).with_suffix(".json")',"Path(__file__).with_suffix('.json')"];assert sum(old.count(t) for t in patterns)==1,p
 target='logs/runner-cache/'+Path(p).stem+'.json';replacement="(_REPO / "+repr(target)+")";new=old
 for t in patterns:new=new.replace(t,replacement)
 assert '_REPO = ' in old;ast.parse(new);(preserve/Path(p).name).write_text(old);(w/p).write_text(new)
 patch.extend(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=p+' cold-v1',tofile=p+' output-fix-v2'))
 changes.append({'path':p,'before_sha256':hashlib.sha256(old.encode()).hexdigest(),'after_sha256':sha(w/p),'output':target,'original_copy':ref(preserve/Path(p).name),'change':'One exact output destination expression only; all computation and fixtures byte-identical.'})
patchpath=b/'drain8160-output-path-fix-v2.patch';assert not patchpath.exists();patchpath.write_text(''.join(patch));subprocess.run(['git','-C',str(w),'add','--',*[x['path'] for x in changes]],check=True)
for a in [('diff','--check'),('diff','--cached','--check'),('diff','HEAD','--check')]:subprocess.run(['git','-C',str(w),*a],check=True)
assert not git('ls-files','--others','--exclude-standard');receipt=b/'drain8160-output-path-fix-v2.json';receipt.write_text(json.dumps({'source_changes':changes,'patch':ref(patchpath),'failure':ref(b/'drain8160-execution-rotor_uniform_compact_response_check_2026_09_16.json'),'preserved_structured_output':ref(saved),'diagnosis':'Only scripts directory generation token changed when child wrote sibling JSON; source/input content and leaf tokens unchanged. Output moved away from guarded source ancestors; ABA guard unchanged.','attempt_scope':'One attempted primary only, remaining six not run. runner_cache deleted live stdout on identity error; no stdout/exit result or PASS fabricated. Structured JSON and sampled watchdog preserved.','source_tree':git('write-tree'),'new_execution_needed':'Corrected source requires one fresh capture for first program and first captures for other six; unchanged caps120s512MiB.'},indent=2)+'\n')
handold=b/'drain8160-author-source-handoff-v1.json';h=json.loads(handold.read_text());h['tree']=git('write-tree');h['status']='AUTHOR OUTPUT-PATH FIX; NEW SAME-SESSION COLD CONFIRMATION REQUIRED';h['references'] += [ref(receipt),ref(handold)]
for row in h['original_dispositions']:
 if row.get('canonical_path') in {c['path'] for c in changes}:row['canonical_sha256']=sha(w/row['canonical_path'])
hand=b/'drain8160-author-source-handoff-v2.json';assert not hand.exists();hand.write_text(json.dumps(h,indent=2)+'\n')
d['source']['tree']=git('write-tree')
for e in d['source']['paths']:e['sha256']=sha(w/e['path'])
for rows in d['inputs'].values():
 for e in rows:e['sha256']=sha(w/e['path'])
d['constituents'][0]['dispositions']=dict(ref(hand),json_pointer='/original_dispositions');d['reviewer']['references'] += [ref(dp),ref(hand),ref(receipt),ref(patchpath),ref(saved),ref(Path(__file__))]
newdraft=b/'drain8160-author-unit-draft-v2.json';assert not newdraft.exists();newdraft.write_text(json.dumps(d,indent=2)+'\n');print(ref(newdraft));print(d['source']['tree'])
