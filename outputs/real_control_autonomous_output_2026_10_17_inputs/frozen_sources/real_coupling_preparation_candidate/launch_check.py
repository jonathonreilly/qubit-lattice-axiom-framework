#!/usr/bin/env python3
"""One bounded local corroboration with serialized, fsynced prelaunch pins."""
import ast
import datetime
import fractions
import hashlib
import importlib.metadata
import json
import os
import platform
import resource
import subprocess
import sys
import time
from pathlib import Path

import sympy

ROOT = Path(__file__).resolve().parent


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def pin(path):
    p = Path(path)
    data = p.read_bytes()
    st = p.stat()
    return {'path':str(p.resolve()),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
            'device':st.st_dev,'inode':st.st_ino,'mtime_ns':st.st_mtime_ns}


def write_sync(path, value):
    with Path(path).open('x') as f:
        json.dump(value,f,indent=2)
        f.write('\n')
        f.flush()
        os.fsync(f.fileno())


def fsync_dir(path):
    fd = os.open(path,os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def main():
    plan = json.loads((ROOT/'RESOURCE_PLAN.json').read_text())
    assert plan['cpu_soft_hard_seconds']==[20,20]
    assert plan['external_wall_seconds']==30
    run = ROOT/'run01'
    run.mkdir(exist_ok=False)
    code = (ROOT/'check_preparation.py').read_bytes()
    ast.parse(code)
    with (run/'executed_source.py').open('xb') as f:
        f.write(code)
        f.flush()
        os.fsync(f.fileno())
    input_paths = [ROOT/'PLAN.md',ROOT/'RESOURCE_PLAN.json',ROOT/'SOURCE_MAP.json',
                   ROOT/'CANDIDATE.md',ROOT/'check_preparation.py',ROOT/'launch_check.py']
    mapping = json.loads((ROOT/'SOURCE_MAP.json').read_text())
    for source in mapping['sources']:
        p = ROOT/source['snapshot']
        assert pin(p)['sha256']==source['sha256'], source['snapshot']
        input_paths.append(p)
    input_paths.append(run/'executed_source.py')
    package = importlib.metadata.distribution('sympy')
    metadata_path = Path(package._path)/'METADATA'
    runtime_paths = [Path(sys.executable).resolve(),Path(fractions.__file__),
                     Path(sympy.__file__),metadata_path]
    before = [pin(p) for p in input_paths]
    runtimes = [pin(p) for p in runtime_paths]
    command = [sys.executable,'-I',str(run/'executed_source.py')]
    env = dict(os.environ)
    env.update({'PYTHONHASHSEED':'0','OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1',
                'MKL_NUM_THREADS':'1','VECLIB_MAXIMUM_THREADS':'1'})
    pre = {'stage':'before Popen; scientific program not yet launched',
           'captured_utc':utc(),'command':command,'cwd':str(ROOT),
           'resource_plan_sha256':pin(ROOT/'RESOURCE_PLAN.json')['sha256'],
           'input_bindings':before,'runtime_bindings':runtimes,
           'runtime_versions':{'python':sys.version,'sympy':sympy.__version__,'platform':platform.platform()},
           'cpu_soft_hard_seconds':[20,20],'external_wall_seconds':30,
           'max_dense_dimension':4,'no_OS_memory_cap':True,
           'thread_environment':{k:env[k] for k in ('PYTHONHASHSEED','OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS')},
           'runtime_pin_limit':'Selected executable/module/distribution files only; not a hermetic transitive runtime image.',
           'flush_protocol':'Each prelaunch/source file flushed and fsynced, then run directory fsynced before Popen.'}
    write_sync(run/'PRELAUNCH.json',pre)
    fsync_dir(run)
    fsync_dir(ROOT)
    prelaunch_binding = pin(run/'PRELAUNCH.json')
    usage0 = resource.getrusage(resource.RUSAGE_CHILDREN)
    started_utc, tick = utc(),time.monotonic()

    def child_limits():
        resource.setrlimit(resource.RLIMIT_CPU,(20,20))

    timed_out = False
    with (run/'stdout.json').open('xb') as out, (run/'stderr.txt').open('xb') as err:
        proc = subprocess.Popen(command,cwd=ROOT,env=env,stdout=out,stderr=err,
                                preexec_fn=child_limits,start_new_session=True)
        try:
            rc = proc.wait(timeout=30)
        except subprocess.TimeoutExpired:
            timed_out = True
            import signal
            os.killpg(proc.pid,signal.SIGKILL)
            rc = proc.wait()
        out.flush(); os.fsync(out.fileno())
        err.flush(); os.fsync(err.fileno())
    elapsed = time.monotonic()-tick
    usage1 = resource.getrusage(resource.RUSAGE_CHILDREN)
    after = [pin(p) for p in input_paths]
    runtimes_after = [pin(p) for p in runtime_paths]
    stable = before==after and runtimes==runtimes_after
    result_valid = False
    result_summary = None
    if rc==0:
        payload = json.loads((run/'stdout.json').read_text())
        result_valid = all(c['passed'] is True for c in payload['checks'])
        result_summary = {'checks':len(payload['checks']),'status':payload['status'],
                          'executed_source_sha256':payload['executed_source_sha256']}
    receipt = {'started_utc':started_utc,'completed_utc':utc(),'pid':proc.pid,
               'prelaunch':prelaunch_binding,'command':command,
               'exit_code':rc,'timed_out':timed_out,'wall_seconds':elapsed,
               'cpu_user_seconds':usage1.ru_utime-usage0.ru_utime,
               'cpu_system_seconds':usage1.ru_stime-usage0.ru_stime,
               'child_maxrss_native_units':usage1.ru_maxrss,
               'maxrss_unit_on_this_platform':'bytes on macOS',
               'limits':{'cpu_soft_hard_seconds':[20,20],'external_wall_seconds':30,'memory_cap':None},
               'input_bindings_after':after,'runtime_bindings_after':runtimes_after,
               'all_bound_files_unchanged':stable,
               'stdout':pin(run/'stdout.json'),'stderr':pin(run/'stderr.txt'),
               'result_summary':result_summary,
               'status':'ok' if rc==0 and result_valid and stable and not timed_out else 'failure'}
    write_sync(run/'RECEIPT.json',receipt)
    fsync_dir(run)
    print(json.dumps({'receipt':str(run/'RECEIPT.json'),'status':receipt['status'],
                      'wall_seconds':elapsed,'exit_code':rc,'summary':result_summary},indent=2))
    return 0 if receipt['status']=='ok' else 1


if __name__=='__main__':
    raise SystemExit(main())
