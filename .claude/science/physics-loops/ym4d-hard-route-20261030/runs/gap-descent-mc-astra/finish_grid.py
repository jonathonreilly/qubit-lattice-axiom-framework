"""Wait for this task's sampler controller, then run its controls and analysis.

This coordinator does no numerical work while run_grid.py is alive. Missing
receipts abort the handoff; sampler failures must not silently become results.
"""
import json
import os
from pathlib import Path
import subprocess
import sys
import time

here=Path(__file__).resolve().parent
pid=int(sys.argv[1]);scratch=sys.argv[2]
while True:
    try:os.kill(pid,0)
    except ProcessLookupError:break
    time.sleep(10)
manifest=json.loads((here/'manifest.json').read_text())
for j in manifest['jobs']:
    tag=f"L{j['L']}_b{j['beta']:.1f}_{j['mult']}_c{j['chain']}"
    receipt=json.loads((here/(tag+'.json')).read_text())
    if not receipt['complete']:raise RuntimeError('incomplete '+tag)
for name,args in [('run_extra.py',[scratch]),('run_o4.py',[scratch]),('analyze.py',[]),('verify_records.py',[scratch]),('report_tables.py',[])]:
    print('START',name,flush=True)
    with (here/(name.removesuffix('.py')+'.log')).open('w') as log:
        subprocess.run([sys.executable,str(here/name),*args],stdout=log,stderr=subprocess.STDOUT,check=True)
    print('DONE',name,flush=True)
print('CONTROLS AND ANALYSIS COMPLETE',flush=True)
