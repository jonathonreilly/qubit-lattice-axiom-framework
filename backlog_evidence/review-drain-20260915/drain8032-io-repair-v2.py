from pathlib import Path
import ast,contextlib,difflib,hashlib,io,json,os,shutil,subprocess,sys,time,traceback,types,math
sys.dont_write_bytecode=True
R=Path('/private/tmp/review-drain-20260915');W=R/'review-meta-slot';h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=h(p))
def save(n,d):
 p=R/n
 with p.open('x') as f:json.dump(d,f,indent=2);f.write('\n')
 return p
f1=json.loads((R/'drain8032-prepared-v1-source-freeze.json').read_text());d1=json.loads((R/'drain8032-author-prepared-v1.json').read_text());assert json.loads((R/'review-meta-slot.json').read_text())['owner']=='PR8032-author'
git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
assert git('rev-parse','HEAD')==d1['base'];assert not git('diff','--name-only','HEAD') and not git('diff','--cached','--name-only')
for e in f1['files']:assert h(W/e['path'])==h(Path(e['immutable_copy']))==e['sha256']
old="""    _result_path = _REPO_ROOT / 'logs/runner-cache' / (Path(__file__).stem + '.json')
    _result_path.parent.mkdir(parents=True, exist_ok=True)
    with _result_path.open('x') as _result_file:
        json.dump(out, _result_file, sort_keys=True, indent=2, allow_nan=False)
        _result_file.write('\\n')
"""
new="""    # Capture may request a unique external sidecar; ordinary live runs write no file.
    _sidecar = os.environ.get('AUDIT_RESULT_SIDECAR')
    if _sidecar:
        _result_path = Path(_sidecar)
        if not _result_path.is_absolute() or _result_path.resolve().is_relative_to(_REPO_ROOT.resolve()):
            raise ValueError('AUDIT_RESULT_SIDECAR must be an absolute path outside the repository')
        with _result_path.open('x') as _result_file:
            json.dump(out, _result_file, sort_keys=True, indent=2, allow_nan=False)
            _result_file.write('\\n')
"""
patch=[];preservation=[]
for e in d1['runners']:
 p=W/e['path'];s=p.read_text();assert s.count(old)==1;t=s.replace(old,new)
 a=ast.parse(s);b=ast.parse(t)
 # All AST nodes except the output function are identical, including every scientific predicate/result/scope.
 drop=lambda tree:[ast.dump(n,include_attributes=False) for n in tree.body if not (isinstance(n,ast.FunctionDef) and n.name=='_emit')]
 assert drop(a)==drop(b);compile(t,str(p),'exec');p.write_text(t)
 preservation.append(dict(path=e['path'],v1_sha256=e['sha256'],v2_sha256=h(p),all_ast_except_emit_identical=True))
 patch.extend(difflib.unified_diff(s.splitlines(True),t.splitlines(True),fromfile='v1/'+e['path'],tofile='v2/'+e['path']))
with (R/'drain8032-io-v1-to-v2.diff').open('x') as f:f.writelines(patch)
# Only output-layer function definitions are compiled/executed with a synthetic result and mocked resource/timing/signal context.
controls=R/'drain8032-io-controls-v2';controls.mkdir();outcomes=[]
for e in d1['runners']:
 p=W/e['path'];name=p.stem;case=controls/name;case.mkdir();fake_repo=case/'repo';canonical=fake_repo/'logs/runner-cache'/f'{name}.json';canonical.parent.mkdir(parents=True);canonical.write_text('existing canonical evidence\n');canonical_hash=h(canonical)
 selected=[n for n in ast.parse(p.read_text()).body if isinstance(n,ast.FunctionDef) and n.name in ('_emit','_finite')];assert len(selected)==2
 source=ast.unparse(ast.Module(body=selected,type_ignores=[]));(case/'extracted-output-layer.py').write_text(source+'\n')
 fake_os=types.SimpleNamespace(environ={});fake_sys=types.SimpleNamespace(argv=[str(p)])
 ns=dict(Path=Path,json=json,os=fake_os,sys=fake_sys,time=types.SimpleNamespace(monotonic=lambda:1.0),signal=types.SimpleNamespace(alarm=lambda n:None),math=math,_rss=lambda:1.0,_started=0.0,AUDIT_RSS_LIMIT_MIB=180,AUDIT_TIMEOUT_SEC=180,_input_sha256={'synthetic_input':'synthetic_hash'},_REPO_ROOT=fake_repo,__file__=str(p))
 exec(compile(source,str(case/'extracted-output-layer.py'),'exec'),ns)
 fake=dict(TOTAL=1,checks=['synthetic-output-only'],seconds=0.0,rss_MiB=1.0,source_sha256='synthetic-source')
 scopes={'per_element':{'checks':1,'scope':'synthetic output-layer control, no science'}}
 for flag in [[],[],['--json'],['--json']]:
  index=len(outcomes);fake_sys.argv=[str(p),*flag];buf=io.StringIO()
  with contextlib.redirect_stdout(buf):ns['_emit'](fake.copy(),1,scopes)
  text=buf.getvalue();raw=case/f'normal-{index}.stdout.txt';raw.write_text(text)
  if flag:assert json.loads(text)['TOTAL']==1
  else:assert 'TOTAL: 1\n' in text
  assert h(canonical)==canonical_hash;outcomes.append(dict(runner=e['path'],case='repeat '+str(flag),status='success',stdout=ref(raw),canonical_unchanged=True))
 fake_sys.argv=[str(p)]
 for idx in range(2):
  side=case/f'unique-{idx}.json';fake_os.environ={'AUDIT_RESULT_SIDECAR':str(side)};buf=io.StringIO()
  with contextlib.redirect_stdout(buf):ns['_emit'](fake.copy(),1,scopes)
  (case/f'sidecar-{idx}.stdout.txt').write_text(buf.getvalue());assert json.loads(side.read_text())['TOTAL']==1;outcomes.append(dict(runner=e['path'],case='unique external sidecar',status='success',sidecar=ref(side)))
 before=h(side)
 try:
  with contextlib.redirect_stdout(io.StringIO()):ns['_emit'](fake.copy(),1,scopes)
 except FileExistsError:
  err=case/'duplicate-sidecar.error.txt';err.write_text(traceback.format_exc());assert h(side)==before;outcomes.append(dict(runner=e['path'],case='duplicate external sidecar',status='expected FileExistsError; original preserved',error=ref(err)))
 else:raise AssertionError('duplicate sidecar accepted')
 for target in ['relative.json',str(canonical)]:
  fake_os.environ={'AUDIT_RESULT_SIDECAR':target}
  try:ns['_emit'](fake.copy(),1,scopes)
  except ValueError:
   err=case/('relative.error.txt' if target=='relative.json' else 'internal.error.txt');err.write_text(traceback.format_exc());assert h(canonical)==canonical_hash;outcomes.append(dict(runner=e['path'],case='invalid destination '+target,status='expected ValueError',error=ref(err)))
  else:raise AssertionError('invalid path accepted')
control=save('drain8032-io-control-receipt-v2.json',dict(status='IO-ONLY SYNTHETIC CONTROLS PASSED',outcomes=outcomes,source_ast_preservation=preservation,science_executions=0,primary_executions=0,helper_executions=0,v1_failure_preserved=ref(R/'drain8032-early-review-v1.json')))
snapshot=R/'drain8032-prepared-v2-source';snapshot.mkdir();files=[]
for e in f1['files']:
 p=W/e['path'];q=snapshot/e['path'];q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q);files.append(dict(path=e['path'],sha256=h(p),mode=oct(p.stat().st_mode&0o777),immutable_copy=str(q)))
freeze=save('drain8032-prepared-v2-source-freeze.json',dict(base=d1['base'],files=files))
d2=dict(d1);d2['runners']=[dict(path=e['path'],sha256=h(W/e['path'])) for e in d1['runners']];d2['freeze']=ref(freeze);d2['io_correction']=ref(control);save('drain8032-author-prepared-v2.json',d2)
m=json.loads((R/'drain8032-author-full-mapping-v1.json').read_text())
for e in m:
 if e['final_path']:e['final_sha256']=h(W/e['final_path'])
save('drain8032-author-full-mapping-v2.json',m)
sys.path[:0]=[str(W/'scripts'),str(W/'docs/audit/scripts')]
import runner_cache as c
contract=dict(default='No JSON filesystem write; canonical artifacts may already exist. Ordinary stdout unchanged.',json_flag='--json prints the same structured result to stdout without a filesystem requirement.',optional_sidecar_env='AUDIT_RESULT_SIDECAR',sidecar='Caller supplies an absolute unique external path with existing parent directory. Exclusive creation; existing evidence never overwritten. Internal or relative paths rejected.',canonical_json='No runner writes canonical JSON. Capture retains external same-run JSON and may separately package verified evidence; ordinary execution never depends on canonical JSON absence.')
dis=json.loads((R/'drain8032-author-discovery-v1.json').read_text())
for e in dis['runners']:
 e['sha256']=h(W/e['path']);assert list(c.declared_input_paths(W/e['path']))==[x['path'] for x in e['ordered_inputs']];assert c.declared_input_fingerprint(W/e['path'])==e['input_fingerprint'];e.pop('json_output');e['output_contract']=contract;e['cli']='No arguments for ordinary stdout; --json for JSON stdout; optional AUDIT_RESULT_SIDECAR external per-attempt JSON with either mode'
save('drain8032-author-discovery-v2.json',dis)
plan=json.loads((R/'drain8032-author-input-resource-plan-v1.json').read_text());plan['programs']=dis['runners'];plan['output_contract']=contract;plan['capture_requirements']=[x.replace('Same-run exclusive JSON file and exact stdout cache path; do not run --json again to obtain structured data','Capture supplies a unique external AUDIT_RESULT_SIDECAR path per program, retains same-run sidecar and exact stdout cache; never rerun --json solely for structured data') for x in plan['capture_requirements']];plan['io_controls']=ref(control);save('drain8032-author-input-resource-plan-v2.json',plan)
findings=json.loads((R/'drain8032-author-finding-dispositions-v1.json').read_text());findings['findings'].append(dict(id='8032-IO1',author_correction=contract,evidence=ref(control),independent_confirmation='pending'));save('drain8032-author-finding-dispositions-v2.json',findings)
refs=[ref(R/n) for n in ['drain8032-author-prepared-v2.json','drain8032-prepared-v2-source-freeze.json','drain8032-author-full-mapping-v2.json','drain8032-author-discovery-v2.json','drain8032-author-input-resource-plan-v2.json','drain8032-author-finding-dispositions-v2.json','drain8032-io-v1-to-v2.diff','drain8032-io-control-receipt-v2.json','drain8032-author-handoff-v1.json','drain8032-early-review-v1.json']]
p=save('drain8032-author-handoff-v2.json',dict(status='NARROW IO REPAIR; SAME-SESSION AFFECTED CONFIRMATION PENDING',base=d1['base'],source_files=82,original_paths=84,changed_paths=[e['path'] for e in d1['runners']],unchanged='All notes, three inputs, mathematical AST outside _emit, all40/22 scientific checks, archives, and shared registry proposals remain byte-identical to v1.',output_contract=contract,source_ast_preservation=preservation,references=refs,science_executions=0,staging=0,gates=0,draft_status_changed=False))
assert not git('diff','--name-only','HEAD') and not git('diff','--cached','--name-only');assert len(git('ls-files','--others','--exclude-standard').splitlines())==82
print(json.dumps(dict(handoff=ref(p),freeze=ref(freeze),controls=ref(control),prepared=ref(R/'drain8032-author-prepared-v2.json')),indent=2))
