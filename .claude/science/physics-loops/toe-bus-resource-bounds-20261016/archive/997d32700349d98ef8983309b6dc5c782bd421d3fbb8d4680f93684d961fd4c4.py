"""Record one actual metadata-only capture command, retaining source and full streams."""
from pathlib import Path
import datetime, hashlib, json, subprocess, sys, time

OUT = Path(__file__).resolve().parent
SOURCE = OUT / 'capture_sources.py'
RUN = OUT / 'metadata_run'

def digest(data): return hashlib.sha256(data).hexdigest()
def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat()

def main():
    RUN.mkdir(exist_ok=False)
    source_bytes = SOURCE.read_bytes()
    launcher_bytes = Path(__file__).read_bytes()
    (RUN/'executed_source.py').write_bytes(source_bytes)
    (RUN/'executed_launcher.py').write_bytes(launcher_bytes)
    argv = [sys.executable, '-B', str(SOURCE)]
    start = utc()
    t0 = time.monotonic()
    launch = dict(started_utc=start, argv=argv, cwd=str(OUT),
                  source_sha256=digest(source_bytes),
                  launcher_sha256=digest(launcher_bytes),
                  scope='Metadata source identity capture only; no scientific calculation.',
                  scientific_executions=0, timeout_seconds=30)
    (RUN/'LAUNCH.json').write_text(json.dumps(launch, indent=2)+'\n')
    try:
        result = subprocess.run(argv, cwd=OUT, capture_output=True, timeout=30, check=False)
        stdout, stderr, code = result.stdout, result.stderr, result.returncode
        timeout = False
    except subprocess.TimeoutExpired as exc:
        stdout, stderr, code = exc.stdout or b'', exc.stderr or b'', None
        timeout = True
    (RUN/'stdout').write_bytes(stdout)
    (RUN/'stderr').write_bytes(stderr)
    receipt = dict(launch, completed_utc=utc(), elapsed_seconds=time.monotonic()-t0,
                   exit_code=code, timed_out=timeout,
                   source_unchanged=SOURCE.read_bytes()==source_bytes,
                   launcher_unchanged=Path(__file__).read_bytes()==launcher_bytes,
                   stdout_sha256=digest(stdout), stderr_sha256=digest(stderr),
                   stdout_bytes=len(stdout), stderr_bytes=len(stderr))
    (RUN/'EXECUTION.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt, indent=2))
    if timeout or code != 0 or not receipt['source_unchanged'] or not receipt['launcher_unchanged']:
        raise SystemExit(1)

if __name__ == '__main__': main()
