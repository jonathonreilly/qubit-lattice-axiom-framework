#!/usr/bin/env python3
"""Focused controls after the memory-guard and assembly changes. GUIDE only."""
from leakage import *
import shutil,subprocess,platform,importlib.metadata
HERE=Path(__file__).resolve().parent
scratch=Path(sys.argv[1])
# Preserve the initial controls before the updated implementation reruns them.
for stem in ('control','wilson_control'):
    for ext in ('.json','.log'):
        src=HERE/(stem+ext);dest=HERE/(stem+'_initial'+ext)
        if src.exists() and not dest.exists():shutil.copyfile(src,dest)
for script,args,log in [
 ('control.py',[],'control_final.log'),
 ('nested_control.py',[str(scratch)],'nested_control.log'),
 ('wilson.py',['build','--J','1','--E','36','--basis',str(scratch/'wilson_J1E36')],'wilson_J1E36_finalbuild.log'),
 ('wilson_control.py',[str(scratch)],'wilson_control_final.log')]:
    with (HERE/log).open('w') as output:subprocess.run([sys.executable,str(HERE/script),*args],stdout=output,stderr=subprocess.STDOUT,check=True)
# The largest-window box was affected by the earlier numerical investigation.
x=point(6,2.6,2.6,14,18,44,diagnose=True)
d=json.loads((HERE/'sweep.json').read_text())
ref=next(v for p in d['grid'] if p['n']==6 and p['beta']==2.6 for v in p['values'] if v['chars']==14)
x['difference_from_saved_window']=x['difference']-ref['difference']
assert abs(x['difference_from_saved_window'])<1e-9
assert x['reflection_error']<1e-9 and x['direct_gram_error']<1e-9
(HERE/'final_window_control.json').write_text(json.dumps(x,indent=2)+'\n')
from threadpoolctl import threadpool_info
record={'grade':'controls only','python':sys.version,'platform':platform.platform(),'priority':os.getpriority(os.PRIO_PROCESS,0),'threads':{k:os.environ.get(k) for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS','BLIS_NUM_THREADS')},'threadpools':threadpool_info(),'versions':{x:importlib.metadata.version(x) for x in ('numpy','scipy','numba')},'window_control_delta':x['difference_from_saved_window'],'peak_RSS_bytes':base.memory_check()}
(HERE/'environment.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record),flush=True)
