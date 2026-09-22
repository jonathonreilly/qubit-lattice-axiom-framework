from pathlib import Path
import subprocess,json,hashlib,ast
R=Path('/private/tmp/review-drain-20260915');W=R/'resume-author8083';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();g=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
paths=g('diff','--cached','--name-only').splitlines();stems=['native_finite_moment_ward','native_stronger_ward_estimators','native_correlated_ward_certificates','native_gaussian_moment_jet','native_quartic_ward'];inputs={};runners=[]
for stem in stems:
 for p in (W/'scripts').glob(stem+'_2026_09_10*.py'):
  runners.append(str(p.relative_to(W)))
  for n in ast.parse(p.read_text()).body:
   if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUDIT_INPUT_PATHS' for t in n.targets):
    for rel in ast.literal_eval(n.value):inputs[rel]=sha(W/rel)
outputs=['outputs/'+s+'_2026_09_10.json' for s in stems]
f={'role':'author source freeze; no science verdict','base':g('rev-parse','HEAD'),'tree':g('write-tree'),'source_paths':{p:sha(W/p) for p in paths},'nonoutput_sources':{p:sha(W/p) for p in paths if p not in outputs},'inputs':inputs,'outputs':outputs,'runners':runners,'capture_script':str(R/'resume8083-author-outputfix-capture.py'),'capture_script_sha256':sha(R/'resume8083-author-outputfix-capture.py'),'boundary':'Five current compact captures only after independent cold confirmation and shared preflight;30s/384MiB each. No historical worker/oracle replay. Negative certification deferred.'}
(R/'resume8083-author-outputfix-preexecution.json').write_text(json.dumps(f,indent=2)+'\n')
(R/'resume8083-author-outputfix-correction.diff').write_bytes(subprocess.check_output(['git','-C',str(W),'diff','40baeb955183e6c2df01cea4fac2dcfe0689091d','--',*[f'docs/{s.upper()}_NOTE_2026-09-10.md' for s in stems],*runners]))
print(json.dumps({'tree':f['tree'],'sources':len(paths),'inputs':len(inputs)}))
