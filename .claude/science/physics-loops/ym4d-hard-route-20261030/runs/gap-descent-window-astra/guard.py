"""Mac mini start gate; the lab numeric lock is acquired by the caller."""
import os,re,subprocess,sys
sys.dont_write_bytecode=True
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS','BLIS_NUM_THREADS'):
    os.environ[name]='1'
if sys.platform=='darwin':
    text=subprocess.run(['memory_pressure','-Q'],check=True,capture_output=True,text=True).stdout
    match=re.search(r'free percentage:\s*(\d+)',text)
    if match is None:raise RuntimeError('cannot establish the Mac memory start gate')
    free=int(match[1]);print('MEMORY_START_GATE',free,'percent free',flush=True)
    if free<50:raise MemoryError('numeric start requires at least 50 percent memory free')
