#!/usr/bin/env python3
"""Compile the scoped algebra with existing pinned task-local dependencies.

No installation is performed. Fresh logs and an olean go to --output-dir;
archived certificate evidence is never overwritten. This is a formal-algebra
reproduction entrypoint, not the numerical claim primary.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import subprocess
import time

AUDIT_TIMEOUT_SEC = 180
MATHLIB_REVISION = '939d5d5d9e6f07d1d8c80a16fa3fa39a7518b716'
LEAN_VERSION = '4.35.0-rc4'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mathlib', type=Path, required=True)
    parser.add_argument('--lean-bin', type=Path, required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    source = Path(__file__).resolve().with_name('RankOneScattering.lean')
    lib, binary, output = (p.resolve() for p in
                           (args.mathlib, args.lean_bin, args.output_dir))
    output.mkdir(parents=True, exist_ok=True)
    names = ['compiler.log', 'execution.json', 'RankOneScattering.olean']
    if any((output / name).exists() for name in names):
        parser.error('choose a fresh output directory; prior evidence is preserved')
    revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=lib,
                                       text=True).strip()
    dirty = subprocess.check_output(['git', 'status', '--porcelain',
                                    '--untracked-files=no'], cwd=lib, text=True)
    if revision != MATHLIB_REVISION or dirty:
        parser.error('Mathlib must have the pinned revision and unchanged tracked files')
    version = subprocess.check_output([str(binary/'lean'), '--version'], text=True).strip()
    if f'version {LEAN_VERSION},' not in version:
        parser.error('the Lean runtime does not match the pinned version')
    before = hashlib.sha256(source.read_bytes()).hexdigest()
    env = dict(os.environ, PATH=str(binary)+os.pathsep+os.environ['PATH'])
    command = [str(binary/'lake'), 'env', 'lean', '-R', str(source.parent),
               str(source), '-o', str(output/'RankOneScattering.olean')]
    start = time.monotonic()
    try:
        result = subprocess.run(command, cwd=lib, env=env, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                timeout=AUDIT_TIMEOUT_SEC)
        code, log = result.returncode, result.stdout
    except subprocess.TimeoutExpired as exc:
        code, log = 124, exc.stdout or ''
        if isinstance(log, bytes):
            log = log.decode(errors='replace')
        log += '\nCOMPILER TIMEOUT\n'
    (output/'compiler.log').write_text(log)
    after = hashlib.sha256(source.read_bytes()).hexdigest()
    receipt = {'command': command, 'cwd': str(lib), 'exit_code': code,
               'elapsed_seconds': time.monotonic()-start,
               'timeout_seconds': AUDIT_TIMEOUT_SEC, 'lean_version': version,
               'mathlib_revision': revision, 'source_sha256_before': before,
               'source_sha256_after': after,
               'scope': 'Rank-one algebra only; no analytical walk theorem formalized'}
    (output/'execution.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(log, end='')
    print(json.dumps(receipt, indent=2))
    if before != after:
        raise SystemExit('source changed during compilation; result is not source-bound')
    raise SystemExit(code)


if __name__ == '__main__':
    main()
