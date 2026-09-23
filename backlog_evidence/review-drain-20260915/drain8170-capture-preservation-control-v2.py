"""Synthetic drift test of exact wrapper with real cache coordinator; no child/science execution."""
from pathlib import Path
import ast,hashlib,json,sys,traceback
sys.dont_write_bytecode=True
R=Path('/private/tmp/review-drain-20260915');W=R/'drain-author-slot'
sys.path.insert(0,str(W/'scripts'));import runner_cache as c
out=R/'drain8170-synthetic-raw-result-v2.json';live=R/'drain8170-synthetic-live-v2.txt';report=R/'drain8170-capture-preservation-control-v2.json'
assert not any(p.exists() for p in [out,live,report])
worker=(R/'drain8170-capture-v2-worker.py.txt').read_text();tree=ast.parse(worker)
function=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='preserve_execute_runner')
fake=dict(runner='synthetic-only.py',status='ok',exit_code=0,stdout='synthetic stdout survives identity drift\n',stderr='synthetic stderr\n',elapsed_sec=0.001,timeout_sec=900,live_log=str(live))
calls=[]
def fake_execute(runner_path,timeout_sec):
    calls.append((runner_path,timeout_sec));live.write_text(fake['stdout']);return fake
ns=dict(original_execute_runner=fake_execute,Path=Path,json=json,sys=type('SyntheticArgv',(),{'argv':['worker','scripts','synthetic-only.py','unused',str(out)]})())
exec(compile(ast.Module(body=[function],type_ignores=[]),'exact-worker-wrapper','exec'),ns)
old=(c.execute_runner,c.capture_runner_execution_identity,c.live_log_path_for,c.write_cache)
ids=iter([object(),object()]);published=[];error=None
try:
    c.execute_runner=ns['preserve_execute_runner'];c.capture_runner_execution_identity=lambda _:next(ids);c.live_log_path_for=lambda _:live;c.write_cache=lambda *a,**k:published.append((a,k))
    try:c.execute_and_write_cache('synthetic-only.py',900)
    except c.RunnerIdentityChangedError as exc:error=repr(exc)
    assert error and calls==[('synthetic-only.py',900)] and not published and not live.exists()
    assert json.loads(out.read_text())==fake
    result=dict(status='SYNTHETIC IDENTITY-DRIFT PRESERVATION CONTROL PASSED',calls=calls,expected_error=error,actual_api_deleted_live=True,external_raw_result_preserved=True,cache_publications=0,science_executions=0,wrapper_sha256=hashlib.sha256(ast.unparse(function).encode()).hexdigest(),raw_result=dict(path=str(out),sha256=hashlib.sha256(out.read_bytes()).hexdigest()),adapter_sha256=hashlib.sha256((R/'drain8170-capture-v2.py').read_bytes()).hexdigest())
except BaseException as exc:
    result=dict(status='CONTROL FAILED',error=repr(exc),traceback=traceback.format_exc());raise
finally:
    c.execute_runner,c.capture_runner_execution_identity,c.live_log_path_for,c.write_cache=old
    report.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2));print('report_sha256',hashlib.sha256(report.read_bytes()).hexdigest())
