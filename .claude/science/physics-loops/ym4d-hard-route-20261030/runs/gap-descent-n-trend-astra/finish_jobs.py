#!/usr/bin/env python3
"""Sequential remaining jobs. The caller must already hold the numeric lock."""
import subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
scratch=sys.argv[1]
jobs=[('sweep.py',[],'sweep_final.log'),('wilson_sweep.py',[scratch],'wilson_sweep_final.log')]
for script,args,logname in jobs:
    with (HERE/logname).open('w') as log:subprocess.run([sys.executable,str(HERE/script),*args],stdout=log,stderr=subprocess.STDOUT,check=True)
    print('COMPLETED',script,flush=True)
