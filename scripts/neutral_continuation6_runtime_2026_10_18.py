"""Standard-library execution ownership only; no scientific predicates."""
from pathlib import Path
import hashlib,json,os,signal,subprocess,sys,tempfile,time
AUDIT_TIMEOUT_SEC=900

def execute(repo, primary, mapping, cap):
    if sys.flags.optimize:
        raise RuntimeError('Optimized Python disables scientific helper assertions')
    sys.stdout.reconfigure(line_buffering=True)
    sys.stderr.reconfigure(line_buffering=True)
    started=time.monotonic()
    deadline=started+cap-2
    root=Path(tempfile.mkdtemp(prefix=Path(primary).stem+'-')).resolve()
    child=None
    def terminate():
        if child is not None and child.poll() is None:
            try: os.killpg(child.pid,signal.SIGKILL)
            except ProcessLookupError: pass
            child.wait()
    def timeout(*_):
        terminate()
        raise TimeoutError('Aggregate cap exceeded; partial output and evidence retained at '+str(root))
    signal.signal(signal.SIGALRM,timeout)
    signal.setitimer(signal.ITIMER_REAL,max(.001,deadline-time.monotonic()))
    print('Fresh execution evidence directory:',root,flush=True)
    try:
        copies=[]
        for source,relative in mapping:
            target=root/relative
            if target.is_absolute() and root not in target.resolve().parents:
                raise RuntimeError('Execution path escapes fresh directory')
            target.parent.mkdir(parents=True,exist_ok=True)
            raw=(repo/source).read_bytes()
            target.write_bytes(raw)
            copies.append(dict(source=source,execution_path=relative,sha256=hashlib.sha256(raw).hexdigest()))
        (root/'execution-copy-map.json').write_text(json.dumps(copies,indent=2)+'\n')
        env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONUNBUFFERED='1')
        # No PIPE: owner raw capture receives stdout/stderr immediately, including timeout/failure output.
        child=subprocess.Popen([sys.executable,'-B','-u',str(root/primary)],cwd=root,env=env,start_new_session=True)
        try:
            code=child.wait(timeout=max(.001,deadline-time.monotonic()))
        except subprocess.TimeoutExpired:
            timeout()
        if code:
            raise RuntimeError(f'Scientific worker exited {code}; evidence retained at {root}')
        outputs=sorted((root/'outputs').rglob('*.json'))
        if len(outputs)!=1:
            raise RuntimeError(f'Expected one fresh owned result JSON, got {len(outputs)} at {root}')
        for output in outputs:
            raw=output.read_bytes();result=json.loads(raw)
            print('FRESH_RESULT',output,'sha256='+hashlib.sha256(raw).hexdigest(),flush=True)
            print(json.dumps(result,sort_keys=True),flush=True)
        print('per_element: original and added finite coefficient, identity and residual predicates execute; frozen coefficient tables are read-only provenance inputs.')
        print('per_site: supplied spin geometries, projected column models and artificial matrix controls remain distinct; no full-spin diagonalization is inferred.')
        print('per_mode: only declared finite momenta, cutoffs, source channels and symmetry sectors are tested; no untested continuum or pole dominance follows.')
        print('per_block: TOTAL counts distinct completed primary assertion or child control groups, not loop iterations; successful child groups require every child assertion to pass; imported helper assertions are otherwise uncounted.')
        print('lattice_wide: analytical arguments retain their stated finite-size, state, fixed-order and outgoing-continuation hypotheses; finite controls do not themselves prove the separate analytic microscopic-pole theorems or empirical identification.')
        counts=json.loads((root/'assertion-groups.json').read_text())
        if not counts['groups'] or counts['evaluations']<len(counts['groups']):
            raise RuntimeError('Missing executed primary assertion groups')
        print('Evidence preserved:',root,'elapsed_seconds=',time.monotonic()-started,flush=True)
        print(f"TOTAL: PASS={len(counts['groups'])} FAIL=0",flush=True)
    finally:
        terminate()
        signal.setitimer(signal.ITIMER_REAL,0)
