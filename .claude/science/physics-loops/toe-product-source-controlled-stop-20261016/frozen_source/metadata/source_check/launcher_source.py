"""Capture bounded provenance-only commands and preserve each actual outcome."""
from pathlib import Path
import datetime,hashlib,json,subprocess,sys,time
D=Path(__file__).resolve().parent
label=sys.argv[1]
if label not in ('source_check','approval_refusal'):raise ValueError('unknown run label')
run=D/'metadata'/label;run.mkdir(parents=True,exist_ok=False)
source=D/'proposal/scripts/product_source_controlled_stop_2026_10_16.py'
def pin(p):
 b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
launched=pin(source);(run/'executed_source.py').write_bytes(source.read_bytes())
launcher=Path(__file__);(run/'launcher_source.py').write_bytes(launcher.read_bytes())
argv=[sys.executable,'-B',str(source),'--packet-root',str(D)]
if label=='approval_refusal':argv+=['--require-approved']
start=datetime.datetime.now(datetime.timezone.utc).isoformat();tick=time.monotonic();timeout=False
with (run/'stdout').open('wb') as out,(run/'stderr').open('wb') as err:
 try:code=subprocess.run(argv,cwd=D,stdout=out,stderr=err,timeout=30).returncode
 except subprocess.TimeoutExpired:code=124;timeout=True
receipt=dict(scope='metadata only; no scientific execution',argv=argv,cwd=str(D),start_utc=start,end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,exit_code=code,timed_out=timeout,timeout_seconds=30,child_source_at_launch=launched,source_capture=pin(run/'executed_source.py'),recorder=pin(launcher),recorder_capture=pin(run/'launcher_source.py'),stdout=pin(run/'stdout'),stderr=pin(run/'stderr'),source_unchanged_during_run=pin(source)==launched,scientific_executions=0)
(run/'EXECUTION.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2));sys.exit(code)
