import ast,pathlib,hashlib,json,os,contextlib,io,sys
R=pathlib.Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot';P=W/'scripts/supplied_torus_auxiliary_field_mode_variance_finite_bracket_2026_09_17.py';b=P.read_bytes();assert hashlib.sha256(b).hexdigest()=='e5b1c1f3917c1e5cc39fc37080560b97e455f60649bdfdfe0d3e00cc744c1b66'
t=ast.parse(b);main=next(n for n in t.body if isinstance(n,ast.FunctionDef) and n.name=='main');start=next(i for i,n in enumerate(main.body) if isinstance(n,ast.Assign) and any(isinstance(x,ast.Name) and x.id=='sidecar' for x in n.targets));body=main.body[start:];assert len(body)==3 and isinstance(body[-1],ast.Return)
f=ast.FunctionDef(name='emit_only',args=ast.arguments(posonlyargs=[],args=[],kwonlyargs=[],kw_defaults=[],defaults=[]),body=body,decorator_list=[]);mod=ast.fix_missing_locations(ast.Module(body=[f],type_ignores=[]))
D=R/'check8178/synthetic-io-fixture';D.mkdir();root=D/'fake-repo';root.mkdir();(root/'input.txt').write_text('synthetic input, no scientific content\n');side=D/'unique.json'
class Fake:passed=15;failed=1;failed_families={'F'}
g=dict(Path=pathlib.Path,os=os,json=json,hashlib=hashlib,ROOT=root,AUDIT_INPUT_PATHS=('input.txt',),ACTIVE_MUTATION='synthetic_failure',MUTATION_GATE={'synthetic_failure':'F'},checks=Fake())
exec(compile(mod,str(P)+'[emitter-only]','exec'),g);emit=g['emit_only'];observations=[];previous=os.environ.pop('AUDIT_RESULT_SIDECAR',None);oldargv=sys.argv[:]
try:
 for argv in [[],[],['--json'],['--json']]:
  sys.argv=['synthetic-emitter']+argv;before=sorted(str(p) for p in D.rglob('*'));ret=emit();assert ret==1 and sorted(str(p) for p in D.rglob('*'))==before;observations.append(dict(case='ordinary' if not argv else '--json is not a supported emitter option',exit_code=ret,writes=0))
 os.environ['AUDIT_RESULT_SIDECAR']=str(side);ret=emit();assert ret==1;raw=side.read_bytes();data=json.loads(raw);assert data['failed']==1 and data['failed_families']==['F'] and data['mutation']=='synthetic_failure' and data['input_sha256']=={'input.txt':hashlib.sha256((root/'input.txt').read_bytes()).hexdigest()};observations.append(dict(case='unique external sidecar preserves fake failure',exit_code=ret,sha256=hashlib.sha256(raw).hexdigest()))
 try:emit();raise AssertionError('collision accepted')
 except FileExistsError as e:
  assert side.read_bytes()==raw;observations.append(dict(case='sidecar collision',exception=repr(e),prior_bytes_unchanged=True))
 for path in ['relative.json',str(root/'inside.json')]:
  os.environ['AUDIT_RESULT_SIDECAR']=path
  try:emit();raise AssertionError('invalid path accepted')
  except ValueError as e:observations.append(dict(case='invalid sidecar path',path=path,exception=repr(e)))
finally:
 sys.argv=oldargv
 if previous is None:os.environ.pop('AUDIT_RESULT_SIDECAR',None)
 else:os.environ['AUDIT_RESULT_SIDECAR']=previous
print(json.dumps(dict(status='PASS isolated exact emitter IO controls',source_sha256=hashlib.sha256(b).hexdigest(),extracted_ast=ast.dump(mod,include_attributes=False),observations=observations,production_main_executions=0,scientific_checks=0,json_contract='No --json branch exists; isolated emission unchanged with repeated flag. Only explicitly requested sidecar writes.'),indent=2))
