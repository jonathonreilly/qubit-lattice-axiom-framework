#!/usr/bin/env python3
"""Versioned stop-aware wrapper; leaves frozen V1 science scripts untouched.

Both supervisor JSON markers and historical extensionless names stop execution.
Use this wrapper for all subsequent runs of the archived computations.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib,json,runpy,sys
from pathlib import Path

ALLOW={'joint_scalar.py','source_null.py','ross_response.py','global_bounds.py'}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--runtime',type=Path,required=True)
    p.add_argument('--script',choices=sorted(ALLOW),required=True)
    p.add_argument('arguments',nargs=argparse.REMAINDER)
    args=p.parse_args()
    deadline=json.loads((args.runtime/'DEADLINE.json').read_text())
    if datetime.now(timezone.utc).timestamp() >= deadline['deadline_epoch']:
        raise SystemExit('Campaign deadline reached; no science script started.')
    markers=['STOP_REQUESTED.json','USER_STOP_REQUESTED.json',
             'STOP_REQUESTED','USER_STOP_REQUESTED']
    for marker in markers:
        if (args.runtime/marker).exists():
            raise SystemExit('Campaign stop marker exists: '+marker)
    script=Path(__file__).resolve().parent/args.script
    print(json.dumps({'runner':'run_v2.py','created_at':datetime.now(timezone.utc).isoformat(),
          'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'script':script.name,'script_sha256':hashlib.sha256(script.read_bytes()).hexdigest(),
          'deadline_epoch':deadline['deadline_epoch'],'checked_stop_markers':markers}),flush=True)
    extra=args.arguments
    if extra and extra[0]=='--':
        extra=extra[1:]
    sys.argv=[str(script),*extra]
    runpy.run_path(str(script),run_name='__main__')

if __name__=='__main__':
    main()
