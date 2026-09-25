"""Record only the new recovery comparator in this new evidence directory."""
from pathlib import Path
import ast, datetime, hashlib, json, os, subprocess, sys, time

here=Path(__file__).resolve().parent
program=here/'compare_read_only.py'
source=program.read_bytes()
tree=ast.parse(source)
permitted={'pathlib','fractions','itertools','collections','ast','hashlib','json','math','re','stat'}
for node in ast.walk(tree):
    if isinstance(node,ast.Import):assert all(x.name in permitted for x in node.names)
    if isinstance(node,ast.ImportFrom):assert node.module in permitted
    if isinstance(node,ast.Call):
        if isinstance(node.func,ast.Name):assert node.func.id not in {'eval','exec','compile','__import__','open'}
        if isinstance(node.func,ast.Attribute):assert node.func.attr not in {'write_text','write_bytes','open','unlink','chmod','mkdir','rename','run','Popen','system'}
# str.replace is the one inert string operation sharing a mutation-like name.
# Its individual uses were fully inspected in the comparator before this run.
start=datetime.datetime.now(datetime.timezone.utc).isoformat();tick=time.monotonic()
proc=subprocess.run([sys.executable,'-B',str(program)],cwd=here,capture_output=True,
                    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
elapsed=time.monotonic()-tick
for name,data in [('COMPARISON.stdout.json',proc.stdout),('COMPARISON.stderr.txt',proc.stderr)]:
    with (here/name).open('xb') as f:f.write(data)
assert source==program.read_bytes()
receipt=dict(started_utc=start,elapsed_seconds=elapsed,exit_code=proc.returncode,
             command=[sys.executable,'-B',str(program)],cwd=str(here),
             program_sha256=hashlib.sha256(source).hexdigest(),
             stdout_sha256=hashlib.sha256(proc.stdout).hexdigest(),stdout_bytes=len(proc.stdout),
             stderr_sha256=hashlib.sha256(proc.stderr).hexdigest(),stderr_bytes=len(proc.stderr),
             scope='Only new read-only comparator executed; no author code or historical writer.')
with (here/'COMPARISON.execution.json').open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps(receipt,indent=2))
sys.exit(proc.returncode)
