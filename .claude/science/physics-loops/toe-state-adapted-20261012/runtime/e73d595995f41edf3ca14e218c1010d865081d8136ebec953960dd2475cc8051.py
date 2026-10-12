#!/usr/bin/env python3
"""Write complete INNER/OUTER evidence before printing any result summary."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

E = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


seal = json.loads((E/'PRE_EXECUTION_SEAL.json').read_text())
for rel, expected in seal['files'].items():
    actual = digest(E/rel)
    if actual != expected:
        raise SystemExit(f"Pre-execution source mismatch: {rel}")

attempt = E/'attempt_01'
attempt.mkdir(exist_ok=False)
environment = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1')
records = []
for checker in ('check_fock.py', 'check_strong_limit.py'):
    name = Path(checker).stem
    directory = attempt/name
    directory.mkdir()
    command = [sys.executable, '-u', str(E/checker)]
    before = {rel: digest(E/rel) for rel in seal['files']}
    record = dict(command=command, cwd=str(E), timeout_seconds=120,
                  process_group=True, started_utc=utc(), source_hashes_before=before,
                  environment_overrides={key: environment[key] for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS')})
    (directory/'OUTER_START.json').write_text(json.dumps(record, indent=2)+'\n')
    started = time.monotonic()
    with (directory/'INNER.stdout').open('wb') as out, (directory/'INNER.stderr').open('wb') as err:
        process = subprocess.Popen(command, cwd=E, env=environment, stdout=out, stderr=err, start_new_session=True)
        record['pid'] = process.pid
        try:
            record['returncode'] = process.wait(timeout=120)
            record['timed_out'] = False
        except subprocess.TimeoutExpired:
            record['timed_out'] = True
            os.killpg(process.pid, signal.SIGTERM)
            try:
                record['returncode'] = process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                record['returncode'] = process.wait(timeout=5)
        out.flush()
        err.flush()
        os.fsync(out.fileno())
        os.fsync(err.fileno())
    record.update(finished_utc=utc(), elapsed_seconds=time.monotonic()-started,
                  source_hashes_after={rel: digest(E/rel) for rel in seal['files']},
                  inner_stdout_sha256=digest(directory/'INNER.stdout'),
                  inner_stderr_sha256=digest(directory/'INNER.stderr'))
    record['sources_unchanged'] = record['source_hashes_before'] == record['source_hashes_after']
    (directory/'INNER_RECEIPT.json').write_text(json.dumps({key:record[key] for key in ('pid','returncode','timed_out','started_utc','finished_utc','elapsed_seconds')},indent=2)+'\n')
    (directory/'OUTER_END.json').write_text(json.dumps(record,indent=2)+'\n')
    (directory/'OUTER.stdout').write_text(json.dumps(record,indent=2)+'\n')
    (directory/'OUTER.stderr').write_text('')
    records.append(dict(checker=checker, directory=str(directory), returncode=record['returncode'], timed_out=record['timed_out'], sources_unchanged=record['sources_unchanged']))

(attempt/'COMPLETE.json').write_text(json.dumps(dict(completed_utc=utc(), records=records),indent=2)+'\n')
print(json.dumps(records,indent=2))
