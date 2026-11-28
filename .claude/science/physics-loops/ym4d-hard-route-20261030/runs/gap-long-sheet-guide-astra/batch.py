"""Strictly serial sampler controller; never runs analysis beside a sampler."""
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
SCRATCH = Path('/tmp/sa-gap-long-sheet-guide-astra.ioPBXO')
HOLDER = 'gap-long-sheet-guide-astra-2b67c749c'
THREADS = ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
           'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS')

def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()

def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat()

def gate():
    if any(os.environ.get(k) != '1' for k in THREADS):
        raise RuntimeError('thread environment must be 1')
    env = dict(os.environ, PYTHONPATH=str(SCRATCH))
    lock = subprocess.run([sys.executable, str(ROOT/'scripts/lab_ops.py'),
        'numeric-lock', 'refresh', '--holder', HOLDER, '--ttl-hours', '12'],
        env=env, capture_output=True, text=True, check=True)
    record = json.loads(lock.stdout)
    if record.get('lock', {}).get('holder_id') != HOLDER:
        raise RuntimeError('numeric lock not held')
    pressure = subprocess.run(['memory_pressure', '-Q'], capture_output=True,
                             text=True, check=True).stdout
    pct = int(re.search(r'free percentage:\s*(\d+)', pressure)[1])
    if pct < 50:
        raise RuntimeError(f'free memory {pct}% below 50%')
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if (rss if sys.platform == 'darwin' else rss*1024) > 2e9:
        raise RuntimeError('controller 2 GB RSS stop')
    return pct

def main():
    phase = sys.argv[1]
    planpath = HERE/(phase+'_plan.json')
    plan = json.loads(planpath.read_text())
    receipts = []
    previous = None
    started = utc()
    for item in plan['chains']:
        if previous is not None and previous.poll() is None:
            raise RuntimeError('previous sampler has not exited')
        pct = gate()
        tag = item['tag']
        if (HERE/(tag+'.json')).exists():
            raise RuntimeError('refusing to overwrite completed chain '+tag)
        out = SCRATCH/tag
        binary=SCRATCH/item.get('binary','sheets')
        source=HERE/item.get('source','sheets.cpp')
        argv = [str(binary), item['model'], str(item['L']),
            str(item['T']), str(item['beta']), str(item['coupling']),
            str(item['seed']), str(item['hot']), str(item['burn']),
            str(item['samples']), str(item['stride']), str(out)]
        receipt = dict(item, started=utc(), argv=argv, memory_free_pct=pct,
            source_path=str(source),source_sha256=sha(source),
            shared_source_sha256=sha(HERE.parent/'gap-descent-mc-astra/su2_guarded.cpp'),
            binary_sha256=sha(binary), plan_sha256=sha(planpath),
            predecessor_reaped=True, threads={k:os.environ[k] for k in THREADS})
        t = time.monotonic()
        print('START', tag, receipt['started'], flush=True)
        with (HERE/(tag+'.log')).open('w') as log:
            previous = subprocess.Popen(argv, stdout=log, stderr=subprocess.STDOUT)
            receipt['pid'] = previous.pid
            receipt['exit_code'] = previous.wait()
        # wait has reaped the process. No successor is started until this point.
        receipt['ended'] = utc()
        receipt['seconds'] = time.monotonic()-t
        receipt['reaped'] = previous.poll() is not None
        receipt['records'] = []
        for suffix in ('.f32','.csv','.therm.csv','.cfg'):
            p = Path(str(out)+suffix)
            if p.exists():
                receipt['records'].append(dict(path=str(p), bytes=p.stat().st_size,
                                                sha256=sha(p)))
        (HERE/(tag+'.json')).write_text(json.dumps(receipt,indent=2)+'\n')
        receipts.append(receipt)
        if receipt['exit_code'] != 0:
            raise RuntimeError('sampler failed: '+tag)
        expected = item['samples']*10*item['L']*4
        if Path(str(out)+'.f32').stat().st_size != expected:
            raise RuntimeError('raw length mismatch: '+tag)
        print('EXIT', tag, receipt['exit_code'], round(receipt['seconds'],2), flush=True)
    (HERE/(phase+'_batch.json')).write_text(json.dumps(dict(started=started,
        ended=utc(), chains=len(receipts), all_reaped=True,
        controller_nice=os.getpriority(os.PRIO_PROCESS,0)),indent=2)+'\n')

if __name__ == '__main__':
    main()
