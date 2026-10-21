"""Portable bounded execution support; contains no scientific model predicates."""
from pathlib import Path
import atexit,hashlib,json,os,re,signal,subprocess,sys,tempfile,time
AUDIT_TIMEOUT_SEC=600  # Metadata only when imported; the owning primary sets its actual timer.
class Execution:
    def __init__(self, source_pack, cap):
        if not __debug__:
            raise RuntimeError('Optimized Python disables scientific assertions')
        sys.stdout.reconfigure(line_buffering=True)
        sys.stderr.reconfigure(line_buffering=True)
        self.started=time.monotonic();self.deadline=self.started+max(1,cap-2)  # Reserve cleanup time before owner cap.
        self.root=Path(tempfile.mkdtemp(prefix='neutral-continuation-')).resolve()
        self.pack=self.root/'native';self.pack.mkdir();self.source=Path(source_pack)
        self.child=None;self.passed=set();self.calls=0
        print('Fresh execution evidence directory:',self.root,flush=True)
        # Fixed historical scratch paths are changed only in isolated execution copies.
        # Top-level JSON snapshots are deliberately not copied: generated output must be fresh.
        transformations=[]
        for src in self.source.rglob('*'):
            if not src.is_file():continue
            rel=src.relative_to(self.source)
            if len(rel.parts)==1 and src.suffix=='.json':continue
            dst=self.pack/rel;dst.parent.mkdir(parents=True,exist_ok=True)
            raw=src.read_bytes()
            if src.suffix=='.py':
                text=re.sub(r"/(?:private/)?tmp(?=/|['\"])",str(self.root),raw.decode())
                dst.write_text(text)
                transformations.append(dict(source=str(src),execution_copy=str(dst),source_sha256=hashlib.sha256(raw).hexdigest(),execution_sha256=hashlib.sha256(dst.read_bytes()).hexdigest()))
            else:dst.write_bytes(raw)
        (self.root/'execution-copy-map.json').write_text(json.dumps(transformations,indent=2)+'\n')
        atexit.register(self.cleanup_child)
        signal.signal(signal.SIGALRM,self.timeout)
        signal.setitimer(signal.ITIMER_REAL,max(0.001,self.deadline-time.monotonic()))
        sys.path.insert(0,str(self.pack))
    def cleanup_child(self):
        if self.child is not None and self.child.poll() is None:
            try:os.killpg(self.child.pid,signal.SIGKILL)
            except ProcessLookupError:pass
            self.child.wait()
    def timeout(self,*args):
        self.cleanup_child()
        raise TimeoutError('Aggregate primary wall-clock cap exceeded; partial evidence preserved at '+str(self.root))
    def run_child(self,command,**kwargs):
        for key in ('capture_output','text','timeout','check'):kwargs.pop(key,None)
        remaining=self.deadline-time.monotonic()
        if remaining<=0:self.timeout()
        print('Executing child:',command,flush=True)
        self.child=subprocess.Popen(command,start_new_session=True,**kwargs)
        try:code=self.child.wait(timeout=remaining)
        except BaseException:
            self.cleanup_child();raise
        self.child=None
        self.check('child:'+Path(command[1]).stem,code==0)
    def check(self,label,condition):
        self.calls+=1
        if not bool(condition):
            self.passed.discard(label)
            print(f'[FAIL] {label}\nTOTAL: PASS={len(self.passed)} FAIL=1',flush=True)
            raise AssertionError(label)
        self.passed.add(label)
        print('[PASS]',label,flush=True)
    def read(self,path):
        path=Path(path)
        if not path.is_file() or self.root not in path.resolve().parents:
            raise RuntimeError('Missing fresh current-run output: '+str(path))
        return json.loads(path.read_text())
    def finish(self,scope,required=()):
        for relative in required:
            path=self.root/relative
            data=self.read(path)
            self.check('fresh-artifact:'+relative,data is not None)
        aggregate=self.read(self.root/'aggregate.json')
        print('AGGREGATE_RESULT',json.dumps(aggregate,sort_keys=True),flush=True)
        print('per_element: each named assertion checks the declared coefficient, matrix entry or numerical residual; arithmetic scope is retained.')
        print('per_site: the supplied physical-qubit and projected-site models are distinguished; no physical primitive is inferred from them.')
        print('per_mode: finite momenta and selected source channels only; frozen large-grid identities are not fresh spectral replays.')
        print('per_block: actual completed assertion groups and child exit codes are counted; missing fresh artifacts fail closed.')
        print('lattice_wide: '+scope)
        print('Execution evidence:',self.root,'elapsed_seconds=',time.monotonic()-self.started)
        for path in sorted(self.root.rglob('*.json')):
            print('EVIDENCE_JSON',path,'sha256='+hashlib.sha256(path.read_bytes()).hexdigest())
        print(f'Assertion evaluations={self.calls}; PASS counts distinct completed assertion groups.')
        print(f'TOTAL: PASS={len(self.passed)} FAIL=0',flush=True)
