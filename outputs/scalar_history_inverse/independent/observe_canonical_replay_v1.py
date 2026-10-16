"""Run an unchanged copied primary and record repository open events.

Runtime repository paths are relative to --replay-root. This observer writes
only inside its own evidence bundle and rejects outside write attempts.
"""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    "docs/SCALAR_HISTORY_COMPATIBILITY_NOTE_2026-10-16.md",
    "scripts/scalar_history_inverse.py",
    "scripts/scalar_history_inverse_math.py",
]
import argparse
import json
import os
from pathlib import Path
import runpy
import sys

parser=argparse.ArgumentParser()
parser.add_argument("--replay-root",type=Path,required=True)
parser.add_argument("--audit-output",type=Path,required=True)
args=parser.parse_args()
root=args.replay_root.resolve();allowed=Path(__file__).resolve().parent
args.audit_output=args.audit_output.resolve()
root.relative_to(allowed);args.audit_output.relative_to(allowed)
reads=[];writes=[];rejected=[]
def under(path,parent):
    try:return str(path.relative_to(parent))
    except ValueError:return None
def hook(event,event_args):
    if event=="open":
        name,mode,flags=event_args
        if not isinstance(name,(str,bytes,os.PathLike)):return
        path=Path(os.fsdecode(name)).resolve()
        is_write=(isinstance(mode,str) and any(c in mode for c in "wax+")) or bool(flags & (os.O_WRONLY|os.O_RDWR|os.O_CREAT|os.O_TRUNC|os.O_APPEND))
        if is_write:
            if under(path,allowed) is None:
                rejected.append({"event":event,"path":str(path)})
                raise PermissionError("Replay attempted a write outside its evidence bundle")
            writes.append({"path":under(path,allowed),"mode":mode,"flags":flags})
        elif under(path,root) is not None:
            reads.append({"path":under(path,root),"exists_before_open":path.is_file(),"mode":mode,"flags":flags})
    elif event in ("os.mkdir","os.remove","os.rmdir","os.rename"):
        targets=event_args[:2] if event=="os.rename" else event_args[:1]
        for name in targets:
            if not isinstance(name,(str,bytes,os.PathLike)):continue
            path=Path(os.fsdecode(name)).resolve()
            if under(path,allowed) is None:
                rejected.append({"event":event,"path":str(path)})
                raise PermissionError("Replay attempted a filesystem mutation outside its evidence bundle")
sys.dont_write_bytecode=True
sys.path.insert(0,str(root/"scripts"))
sys.argv=[str(root/"scripts/scalar_history_inverse.py")]
sys.addaudithook(hook)
code=0;error=None
try:
    runpy.run_path(str(root/"scripts/scalar_history_inverse.py"),run_name="__main__")
except SystemExit as exc:
    code=exc.code if isinstance(exc.code,int) else (0 if exc.code is None else 1)
except BaseException as exc:
    code=1;error=repr(exc)
    import traceback
    traceback.print_exc()
finally:
    observed=sorted({r["path"] for r in reads if r["exists_before_open"]})
    payload={"kind":"CPython audit-hook observation of copied primary execution","repository_root":str(root),"declared_repository_reads":AUDIT_INPUT_PATHS,"observed_existing_repository_read_paths":observed,"exact_existing_read_closure":observed==sorted(AUDIT_INPUT_PATHS),"read_attempts":reads,"writes_inside_bundle":writes,"rejected_outside_writes":rejected,"returncode":code,"exception":error,"dont_write_bytecode":sys.dont_write_bytecode,"scope":"Repository opens during the copied primary only. Installed Python/library imports outside the repository are environment dependencies, not an independent full-system trace."}
    args.audit_output.write_text(json.dumps(payload,indent=2)+'\n')
if rejected or not payload["exact_existing_read_closure"]:code=1
raise SystemExit(code)
