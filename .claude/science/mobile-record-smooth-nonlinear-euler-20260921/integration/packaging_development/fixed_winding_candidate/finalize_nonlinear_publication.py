from pathlib import Path
import datetime,hashlib,importlib.util,json,shutil,subprocess,sys,zipfile

R=Path('/Users/jonreilly/Documents/Codex/mobile-record-nonlinear-publication-20260921')
X=Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-21-second')
A=Path('/Users/jonreilly/Documents/Codex/mobile-record-formation-20260920/.claude/science/mobile-record-formation-20260920/campaign12h_second')
E=R/'.claude/science/mobile-record-smooth-nonlinear-euler-20260921'
runner=R/'scripts/mobile_records_smooth_nonlinear_euler_2026_09_21.py'
note=R/'docs/MOBILE_RECORDS_SMOOTH_NONLINEAR_EULER_BOUNDED_THEOREM_NOTE_2026-09-21.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
spec=importlib.util.spec_from_file_location('nonlinear_runner',runner);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
author=json.loads((X/'nonlinear_author_run.json').read_text())
assert author['passed'] and author['control_count']==8 and author['mutation'] is None
for p,h in author['identities'].items():assert sha(R/p)==h
mutations=[]
for name,(source,old,new) in sorted(mod.MUTATIONS.items()):
 data=json.loads((X/('nonlinear_'+name+'.json')).read_text());last=data['suites'][-1]
 assert data['passed'] is False and data['mutation']==name and last['returncode']!=0
 text=(E/'author_checks'/source).read_text();assert text.count(old)==1
 assert last['source_sha256']==sha(E/'author_checks'/source)
 assert last['executed_source_sha256']==hashlib.sha256(text.replace(old,new,1).encode()).hexdigest()
 assert last['stderr'].splitlines()[-1]=='AssertionError'
 for suffix in ['json','log','stderr']:shutil.copy2(X/('nonlinear_'+name+'.'+suffix),E/'mutation_results'/(name+'.'+suffix))
 mutations.append(dict(name=name,source_sha256=last['source_sha256'],mutant_sha256=last['executed_source_sha256'],returncode=last['returncode']))
commands=json.loads((X/'nonlinear_integration_commands.json').read_text())
assert [r['check'] for r in commands['rows']]==['vocab','pipeline','strict_lint']
assert all(r['exit_code']==0 for r in commands['rows'])
for stem in ['author_run','cache','cache_receipt','vocab','pipeline','strict_lint','integration_commands','mutation_receipt','capsule_verification','packaging']:
 for suffix in ['json','log','stderr']:
  p=X/('nonlinear_'+stem+'.'+suffix)
  if p.exists():shutil.copy2(p,E/'integration'/p.name)
if (X/'nonlinear_publication_development').exists():shutil.copytree(X/'nonlinear_publication_development',E/'integration/packaging_development',dirs_exist_ok=True)
trans=json.loads((E/'PUBLICATION_TRANSFORM.json').read_text())
for part in trans['parts']:
 p=E/'primary_sources'/part['primary'];assert sha(p)==part['source_sha256']
 assert p.read_bytes()==(A/p.name).read_bytes()
 body=p.read_text().split('\n',2)[2].rstrip()
 body='\n'.join('#'+line if line.startswith('#') else line for line in body.splitlines())
 assert hashlib.sha256(body.encode()).hexdigest()==part['published_body_sha256']
 assert note.read_text().count(body)==1
for source,_,_ in mod.SUITES:assert (A/source).read_bytes()==(E/'author_checks'/source).read_bytes()
sys.path.insert(0,str(R/'scripts'));import runner_cache
assert runner_cache.cache_status(str(runner.relative_to(R)))=='fresh'
run=subprocess.run([sys.executable,str(E/'verify_evidence.py')],cwd=R,capture_output=True,text=True,check=True)
assert not run.stderr;capsule=json.loads(run.stdout)
(E/'integration/CAPSULE_VERIFICATION.json').write_text(run.stdout)
for p in (E/'independent').glob('*.zip'):
 with zipfile.ZipFile(p) as z:
  assert not any(Path(n).suffix.lower() in ['.pdf','.ps','.csv','.npz','.state','.bin'] for n in z.namelist())
report=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 base_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip(),
 note_sha256=sha(note),runner_sha256=sha(runner),primary_bodies_exact=3,
 author_math_groups=7,bookkeeping_groups=1,cache_fresh=True,
 mutations=mutations,capsules=capsule,integration_commands=commands,
 graph_delta=dict(nodes_added=1,edges_added=2),audit_status='unaudited',
 prompt_files_changed=[],changed_evidence_gate='pending exact staged candidate',
 scope='Root source/proof reading and author integration. Selective independent reconstruction has separate sealed packets; no formal audit verdict or merge.')
(E/'ASSEMBLY_AND_INTEGRATION.json').write_text(json.dumps(report,indent=2)+'\n')
readme=E/'README.md'
readme.write_text(readme.read_text()+'''\nRecursive historical sources also identify third-party PDF and page identities;
their checked scope is recorded in the source packets. Their bytes were authenticated locally but are excluded
from every capsule. Publication helper failures and their narrow repairs are
preserved separately from scientific computations.\n''')
files=[p for p in E.rglob('*') if p.is_file()]
assert not any(p.suffix.lower() in ['.pdf','.ps','.csv','.npz','.state','.bin'] for p in files)
assert all(p.stat().st_size<10_000_000 for p in files)
print(json.dumps(dict(files=len(files),bytes=sum(p.stat().st_size for p in files),note_sha256=sha(note),runner_sha256=sha(runner))))
