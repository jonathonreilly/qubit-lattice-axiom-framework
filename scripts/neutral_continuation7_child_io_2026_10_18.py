"""Stream child stdout immediately while retaining it for the original parser."""
import subprocess,sys,threading
AUDIT_TIMEOUT_SEC=300

def run_tee(args, *, check=False, capture_output=False, text=False, timeout=None, env=None):
    if not capture_output or not text:
        raise ValueError('Owned scientific child requires explicit captured text contract')
    print('CHILD_START',args,flush=True)
    child=subprocess.Popen(args,stdout=subprocess.PIPE,stderr=None,text=True,bufsize=1,env=env)
    pieces=[];errors=[]
    def drain():
        try:
            for line in child.stdout:
                pieces.append(line)
                sys.stdout.write(line);sys.stdout.flush()
        except BaseException as exc:
            errors.append(exc)
    reader=threading.Thread(target=drain,daemon=True);reader.start()
    try:
        code=child.wait(timeout=timeout)
    except BaseException:
        child.kill();child.wait();reader.join(timeout=2)
        print('CHILD_ABORT',args,flush=True)
        raise
    reader.join(timeout=2)
    if reader.is_alive():
        raise RuntimeError('Child output did not close after process exit')
    if errors:raise RuntimeError('Child output streaming failed') from errors[0]
    stdout=''.join(pieces)
    if check and code:raise subprocess.CalledProcessError(code,args,output=stdout)
    print('CHILD_EXIT',code,args,flush=True)
    return subprocess.CompletedProcess(args,code,stdout,None)
