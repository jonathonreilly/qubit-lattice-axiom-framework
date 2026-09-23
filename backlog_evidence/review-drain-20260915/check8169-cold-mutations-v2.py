import pathlib,subprocess,ast,hashlib,json,difflib,sys,time,resource
R=pathlib.Path('/private/tmp/review-drain-20260915');D=R/'check8169-cold-mutations-v2';D.mkdir(exist_ok=False);repo=R/'author-draft-slot';p='scripts/frame_attached_menu_exchange_probabilities_2026_09_16.py'
src=subprocess.check_output(['git','-C',str(repo),'show',':'+p]).decode();(D/'frozen-corrected-primary.py').write_text(src)
# Extract computational body only, retaining exact mathematical assertions.
# Strip input hash loop and output-file side effects; no canonical primary invocation.
t=ast.parse(src)
for n in t.body:
 if isinstance(n,ast.FunctionDef) and n.name=='main':
  n.body=[x for x in n.body if not (isinstance(x,ast.For) and isinstance(x.iter,ast.Name) and x.iter.id=='AUDIT_INPUT_PATHS') and not (isinstance(x,ast.Assign) and any(isinstance(y,ast.Name) and y.id=='output' for y in x.targets)) and not (isinstance(x,ast.Expr) and isinstance(x.value,ast.Call) and isinstance(x.value.func,ast.Attribute) and ((isinstance(x.value.func.value,ast.Name) and x.value.func.value.id=='output') or (isinstance(x.value.func.value,ast.Attribute) and isinstance(x.value.func.value.value,ast.Name) and x.value.func.value.value.id=='output')))]
base=ast.unparse(t)+'\n';(D/'baseline.py').write_text(base)
mutations=[('lambda-bound','1 / (1 + t), -1 / (1 + t)','2 / (1 + t), -1 / (1 + t)','linear-bound:'),('lambda-inversion','lam = (4 * alpha - 1) / (1 + t)','lam = (4 * alpha - 1) / (1 - t)','lambda-inverse:'),('slot-exchange','apply_matrix(M, b) == slots[0]','apply_matrix(M, b) == b','slot-exchange:'),('bisector-swap','swap = lambda v: (v[2], -v[1], v[0])','swap = lambda v: (v[0], -v[1], v[2])','bisector-swap'),('raw-normalization','raw = tuple(((1 + dot(s, q)) / 2','raw = tuple(((1 + dot(s, q)) / 3','overlap-normalization:'),('normalized-law','norm = tuple((v / 2 for v in raw))','norm = tuple((v / 3 for v in raw))','overlap-normalization:'),('chain-separator','dot(q, scale(a * b, q))','dot(q, scale(a * b, qp))','chain-endpoint-event'),('endpoint-threshold','abs(dot(l, r)) < 1','abs(dot(l, r)) <= 1','independent-endpoint-analogue')]
rows=[]
def limit():resource.setrlimit(resource.RLIMIT_AS,(256*1024*1024,256*1024*1024))
for name,code,target in [('baseline',base,None)]+[(name,base.replace(old,new),target) for name,old,new,target in mutations]:
 if name!='baseline':
  old=next(x[1] for x in mutations if x[0]==name);assert base.count(old)==1,(name,old,base.count(old));assert code!=base
 path=D/(name+'.py');path.write_text(code);(D/(name+'.diff')).write_text(''.join(difflib.unified_diff(base.splitlines(True),code.splitlines(True),fromfile='baseline.py',tofile=path.name)))
 start=time.monotonic();run=subprocess.run([sys.executable,str(path)],cwd=D,capture_output=True,text=True,timeout=10);(D/(name+'.stdout')).write_text(run.stdout);(D/(name+'.stderr')).write_text(run.stderr)
 failures=[x for x in run.stdout.splitlines() if x.startswith('FAIL:')];ok=run.returncode==0 if name=='baseline' else run.returncode!=0 and any(target in x for x in failures)
 rows.append({'name':name,'sha256':hashlib.sha256(code.encode()).hexdigest(),'returncode':run.returncode,'elapsed':time.monotonic()-start,'expected_failed_check':target,'failures':failures,'observed_expected':ok})
(D/'results.json').write_text(json.dumps({'source_sha256':hashlib.sha256(src.encode()).hexdigest(),'method':'AST extracted computational body, same finite assertions;3 file-input checks and JSON output side effects removed, all math unchanged before each single targeted mutation','timeout_each_seconds':10,'address_space_limit_bytes':None, 'memory_limit_note':'RLIMIT_AS unavailable on this macOS; no enforced memory cap claimed for scratch finite controls. Primary process-tree cap remains separate.','cases':rows},indent=2)+'\n');print(json.dumps(rows,indent=2));assert all(x['observed_expected'] for x in rows)
