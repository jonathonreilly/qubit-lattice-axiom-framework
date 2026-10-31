"""Scoped coordinator integration gate; no whole-PR/audit disposition."""
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import unquote
import ast, hashlib, json, re, subprocess, sys, tempfile

L=Path('.claude/science/toe-ruleset-20261021/agents/ym4d-proof');C=L/'checks'
sha=lambda b:hashlib.sha256(b).hexdigest()
pins={
 'review_uniform_soft_receipt.json':('33b98352bcdae4c40f9db02cefbbdfd225063395da0c7c589ee47626e0ed10a3','files'),
 'review_uniform_soft_scope_receipt.json':('54ef326a0accde7811db80c2ef85cb5c7907959083ca5252e4d6862b85e61dcb','files'),
 'review_uniform_soft_scope_confirmation_receipt.json':('d2df587d27a68cbfed6664b858fe56a24962199ab543a4ebcaa794476371a115','files'),
 'review_source_sea_receipt.json':('06ffa9be999fd3fdf750f93629760001474f159d47d6fc1bc5ad1b0c179a5c24','frozen_review_artifacts'),
 'review_crossover_import_receipt.json':('ad4df40b8d9df19a531c901c80b2ff8a561e24edf8299b696efb860917e25aab','artifacts'),
 'review_euclidean_rotation_freeze.json':('3107a2b1990f804bd60f00037107625f2b1d9f92b0f0027bc2870cee6e95341c','owned_artifacts'),
}
assert not subprocess.check_output(['git','diff','--cached','--name-only'],text=True).strip()
paths=set();bindings=[]
for n,(h,key) in pins.items():
    p=C/n;raw=p.read_bytes();assert sha(raw)==h,n;d=json.loads(raw);rows=d[key]
    if isinstance(rows,dict):rows=[{'path':p,'sha256':h}for p,h in rows.items()]
    rows=rows+[{'path':str(p),'sha256':h}]
    for r in rows:
        p=Path(r['path']);assert sha(p.read_bytes())==r['sha256'],str(p)
        paths.add(str(p));bindings.append(r)
for n in ['HANDOFF.md','APPROACH_REGISTRY.md','SESSION25_RESULTS.md','PROOF.md',
          'LITERATURE_BRIDGES.md','ASSUMPTIONS_AND_IMPORTS.md',
          'UNIFORM_SOFT_MINIMIZER_ASTRA.md','CROSSOVER_LITERATURE_BRIDGE_ASTRA.md',
          'EUCLIDEAN_ROTATION_IMPORT_ASTRA.md','SOFT_FLUCTUATION_COVARIANCE_ASTRA.md']:
    paths.add(str(L/n))
for n in ['crossover_import_exact_v2.py','crossover_import_attempt02.stdout.json',
          'crossover_import_attempt02.stderr.txt','crossover_import_control_fix_receipt.json',
          'crossover_import_control_fix_initial_receipt.json']:
    paths.add(str(C/n))
paths.update(subprocess.check_output(['git','ls-files','--others','--exclude-standard','--',str(C/'full_proof_*')],text=True).splitlines())
assert all(Path(p).is_file() for p in paths)
assert not any(Path(p).suffix.lower()=='.pdf' for p in paths)
report={'created_utc':datetime.now(timezone.utc).isoformat(),'integration_base':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'methodology_revision':subprocess.check_output(['git','rev-parse','origin/main'],text=True).strip(),'source_review_bindings':bindings,'staged_candidate_paths':sorted(paths),'errors':[],'preserved_failed_syntax':[],'empty_diagnostic_streams':[]}
legacy=(L/'PROOF.md').read_text();marker='> **PROVENANCE WARNING';body=legacy[legacy.index(marker):]
assert sha(body.encode())=='4efdee19aa03123a89053e466525f0ef5e9d8a4b8eb1ea38a1e87125043e728c'
report['legacy_proof_body_sha256']=sha(body.encode())
temp=Path(tempfile.mkdtemp(prefix='ym-reviewed-producer-gate-'));md=[];links=[];archives=[]
for name in sorted(paths):
    p=Path(name);raw=p.read_bytes()
    if p.suffix=='.json':
        if raw:json.loads(raw)
        else:report['empty_diagnostic_streams'].append(name)
    if p.suffix=='.py':
        try:ast.parse(raw.decode(),filename=name)
        except SyntaxError as e:
            if p.name!='review_uniform_soft_01_attempt01.py':raise
            report['preserved_failed_syntax'].append({'path':name,'sha256':sha(raw),'exception':str(e),'scope':'Immutable original reviewer implementation failure, not current runnable code.'})
    if p.suffix!='.md':continue
    text=raw.decode();base=p.parent
    if p.name=='PROOF.md':
        text=text[:text.index(marker)];q=temp/'PROOF_status_header.md';q.write_text(text);md.append(str(q))
    else:md.append(name)
    if p.name=='review_euclidean_rotation_original_source.md':
        assert sha(raw)=='71e3ea5e66bc694cee172ab1348594a9645b06df92b3e33b8633cd39c725208e'
        base=L;archives.append({'path':name,'original_context':str(L/'EUCLIDEAN_ROTATION_IMPORT_ASTRA.md'),'reason':'Byte-identical historical source copy retains original relative paths.'})
    prose=re.sub(r'```.*?```','',text,flags=re.S);prose=re.sub(r'`[^`\n]*`','',prose)
    prose=re.sub(r'(?m)^(?:> ?)* {4}.*$','',prose)
    for target in re.findall(r'\[[^\]\n]+\]\(([^\n)]+)\)',prose):
        target=target.strip().strip('<>')
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target) or target.startswith('#'):continue
        local=unquote(target.split('#')[0])
        if not local:continue
        resolved=(base/local).resolve();entry={'file':name,'target':target,'resolved':str(resolved)};links.append(entry)
        if not resolved.exists():report['errors'].append({'broken_link':entry})
report['local_links']=links;report['archive_link_contexts']=archives
report['preserved_preflight_failure']='checks/full_proof_reviewed_producer_validation_attempt01.json: indented mathematical code [Xi](I) was misread as a prose link; parser now excludes indented code, with original script/report preserved.'
vp=temp/'vocabulary.json';v=subprocess.run([sys.executable,'scripts/vocab_lint.py','--report-only','--report-path',str(vp),*md],capture_output=True,text=True)
report['vocabulary']={'exit_code':v.returncode,'stdout':v.stdout,'stderr':v.stderr,'report':json.loads(vp.read_text()) if vp.exists() else None}
if v.returncode:report['errors'].append('vocabulary check failed')
for n in ['full_proof_next_reviews_replay_summary.json','full_proof_bridge_reviews_replay_summary.json']:
    assert json.loads((C/n).read_text())['all_ok'],n
report['reproduced_invocations']=14;report['full_existence_established']=False;report['physical_mass_gap_established']=False
report['scope']='Four bounded independent reviews, exact repairs, covariance author progress and shared-status/literature integration. This is not a whole-PR pipeline or audit PASS.'
out=C/'full_proof_reviewed_producer_validation.json';assert not out.exists()
out.write_text(json.dumps(report,indent=2)+'\n')
assert not report['errors'],report['errors']
paths.add(str(out));subprocess.run(['git','add','--',*sorted(paths)],check=True)
assert set(subprocess.check_output(['git','diff','--cached','--name-only'],text=True).splitlines())==paths
w=subprocess.run(['git','diff','--cached','--check'],capture_output=True,text=True)
if w.returncode:
    fail=C/'full_proof_reviewed_producer_whitespace_failure.json';assert not fail.exists();fail.write_text(json.dumps({'stdout':w.stdout,'stderr':w.stderr,'exit_code':w.returncode},indent=2)+'\n')
assert w.returncode==0,w.stdout
print(json.dumps({'staged_files':len(paths),'review_artifact_records':len(bindings),'links':len(links),'vocabulary_violations':report['vocabulary']['report']['summary']['files_with_violations'],'reproduced_invocations':14,'legacy_proof_body_preserved':True,'frozen_failure_preserved':report['preserved_failed_syntax']}))
