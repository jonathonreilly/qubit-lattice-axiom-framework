"""Portable source-root-explicit integration check; never run author code in place.

Source paths below resolve against --source-root. Bundle paths resolve beside
this script, so the closed evidence directory can be copied byte-for-byte.
The graph check invokes isolated unchanged AST definitions, not the pipeline.
"""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    "docs/SCALAR_HISTORY_COMPATIBILITY_NOTE_2026-10-16.md",
    "scripts/scalar_history_inverse.py",
    "scripts/scalar_history_inverse_math.py",
    "outputs/scalar_history_inverse/result.json",
    "docs/audit/scripts/build_citation_graph.py",
]
BUNDLE_INPUT_PATHS = [
    "CANONICAL_SOURCE_SNAPSHOT_v2.json",
    "original_replay/NON_EQUILIBRIUM_SCALAR_CONTROLS_v2.json",
    "observe_canonical_replay_v1.py",
    "check_canonical_integration_v1.py",
]
import argparse
import ast
from datetime import datetime,timezone
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import subprocess
import sys
import time

parser=argparse.ArgumentParser()
parser.add_argument("--source-root",type=Path,required=True)
parser.add_argument("--attempt",default="canonical_attempt01")
args=parser.parse_args()
if not re.fullmatch(r"[a-zA-Z0-9_]+",args.attempt):raise ValueError("Use a simple unique attempt label")
SOURCE=args.source_root.resolve();HERE=Path(__file__).resolve().parent
prefix=HERE/args.attempt;REPLAY=HERE/(args.attempt+"_repository")
if REPLAY.exists() or prefix.with_suffix(".run.json").exists():raise FileExistsError("Use a fresh attempt label; prior evidence is immutable")
def binding(base,paths):
    return {p:{"sha256":hashlib.sha256((base/p).read_bytes()).hexdigest(),"bytes":(base/p).stat().st_size} for p in paths}
before=binding(SOURCE,AUDIT_INPUT_PATHS);bundle_before=binding(HERE,BUNDLE_INPUT_PATHS)
snapshot=json.loads((HERE/BUNDLE_INPUT_PATHS[0]).read_text())["sources"]
initial_pins_match=all(before[n]["sha256"]==snapshot[n]["sha256"] for n in AUDIT_INPUT_PATHS)
if not initial_pins_match:
    prefix.with_suffix(".source_drift.json").write_text(json.dumps({"before":before,"expected":{n:snapshot[n]["sha256"] for n in AUDIT_INPUT_PATHS}},indent=2)+'\n')
    raise RuntimeError("Canonical inputs moved from final snapshot; drift was preserved")
REPLAY.mkdir()
for name in AUDIT_INPUT_PATHS[:3]:
    target=REPLAY/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes((SOURCE/name).read_bytes())

# Exact extraction definitions, without importing the audit module or running
# its module-level registry read, graph builder or output mutation.
extract_source=(SOURCE/AUDIT_INPUT_PATHS[4]).read_text()
tree=ast.parse(extract_source)
function_names={"normalize_claim_type","extract_claim_type_hint","normalize_runner_path","runner_paths","first_runner_path","extract_section","_script_stem_from_path_parts","_path_parts_from_ast","_script_stem_from_ast","_dynamic_loader_param_indexes","_parse_script_imports","resolve_helper_runner_paths","extract_runner"}
constant_names={"CLAIM_TYPES","CLAIM_TYPE_LINE_RE","TYPE_LINE_RE","RUNNER_LABEL_RE","RUNNER_PATH_RE","RUNNER_SECTION_RE","RUNNER_VERIFICATION_SECTION_RE","HEADING_RE"}
selected=[]
for node in tree.body:
    if isinstance(node,ast.FunctionDef) and node.name in function_names:selected.append(node)
    elif isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id in constant_names for t in node.targets):selected.append(node)
env={"ast":ast,"re":re,"Path":Path,"REPO_ROOT":SOURCE}
exec(compile(ast.Module(body=selected,type_ignores=[]),str(SOURCE/AUDIT_INPUT_PATHS[4]),"exec"),env)
note=(SOURCE/AUDIT_INPUT_PATHS[0]).read_text()
primary=env["extract_runner"](note,"SCALAR_HISTORY_COMPATIBILITY_NOTE_2026-10-16.md")
helpers=env["resolve_helper_runner_paths"](primary)
claim_hint=env["extract_claim_type_hint"](note)
primary_tree=ast.parse((SOURCE/AUDIT_INPUT_PATHS[1]).read_text())
declared={}
for node in primary_tree.body:
    if isinstance(node,ast.Assign):
        for target in node.targets:
            if isinstance(target,ast.Name) and target.id in ("AUDIT_TIMEOUT_SEC","AUDIT_INPUT_PATHS"):
                declared[target.id]=ast.literal_eval(node.value)
extraction={"source_sha256":before[AUDIT_INPUT_PATHS[4]]["sha256"],"isolated_functions":sorted(function_names),"pipeline_imported_or_run":False,"primary_runner":primary,"helper_runners":helpers,"claim_hint":claim_hint,"declared_primary_contract":declared}
prefix.with_suffix(".extraction.json").write_text(json.dumps(extraction,indent=2)+'\n')

argv=[sys.executable,"-B",str(HERE/"observe_canonical_replay_v1.py"),"--replay-root",str(REPLAY),"--audit-output",str(prefix.with_suffix(".read_closure.json"))]
start=time.monotonic();utc=datetime.now(timezone.utc).isoformat();r0=resource.getrusage(resource.RUSAGE_CHILDREN);timeout=False
try:
    run=subprocess.run(argv,cwd=REPLAY,env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1"),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=AUDIT_TIMEOUT_SEC,check=False)
    stdout,stderr,code=run.stdout,run.stderr,run.returncode
except subprocess.TimeoutExpired as exc:timeout=True;stdout,stderr,code=exc.stdout or b"",exc.stderr or b"",None
wall=time.monotonic()-start;r1=resource.getrusage(resource.RUSAGE_CHILDREN)
prefix.with_suffix(".stdout.txt").write_bytes(stdout);prefix.with_suffix(".stderr.txt").write_bytes(stderr)
after=binding(SOURCE,AUDIT_INPUT_PATHS);bundle_after=binding(HERE,BUNDLE_INPUT_PATHS)
result_path=REPLAY/"outputs/scalar_history_inverse/result.json"
raw=result_path.read_bytes() if result_path.exists() else b"";reference=(SOURCE/AUDIT_INPUT_PATHS[3]).read_bytes()
try:result=json.loads(raw);parse_error=None
except (ValueError,UnicodeDecodeError) as exc:result=None;parse_error=repr(exc)
old=json.loads((HERE/BUNDLE_INPUT_PATHS[1]).read_text())
old_rows=old["checks"];new_rows=result["checks"] if result else []
index={row['name']:row for row in new_rows}
preserved=all(row==index.get(row['name']) for row in old_rows)
algebra_preserved=bool(result) and result["algebra"]["polynomial"]==old["polynomial"] and result["algebra"]["near_degenerate_root_slope"]==old["near_degenerate_root_slope"]
closure=json.loads(prefix.with_suffix(".read_closure.json").read_text()) if prefix.with_suffix(".read_closure.json").exists() else None
checks={"initial_snapshot_matches":initial_pins_match,"primary_extraction":primary=="scripts/scalar_history_inverse.py","helper_extraction":helpers==["scripts/scalar_history_inverse_math.py"],"bounded_claim_hint":claim_hint[1]=="bounded_theorem","timeout_declared":declared.get("AUDIT_TIMEOUT_SEC")==120,"declared_read_inputs":tuple(declared.get("AUDIT_INPUT_PATHS",()))==(AUDIT_INPUT_PATHS[0],AUDIT_INPUT_PATHS[2]),"successful_primary":code==0 and not timeout and bool(result) and result["failed"]==0,"output_byte_identical_to_final_receipt":raw==reference,"original_46_controls_preserved":preserved,"original_algebra_preserved":algebra_preserved,"exact_repository_read_closure":bool(closure) and closure["exact_existing_read_closure"],"no_outside_writes":bool(closure) and not closure["rejected_outside_writes"],"source_inputs_unchanged":before==after,"bundle_inputs_unchanged":bundle_before==bundle_after,"copied_sources_unchanged":all((REPLAY/n).read_bytes()==(SOURCE/n).read_bytes() for n in AUDIT_INPUT_PATHS[:3])}
meta={"argv":argv,"source_root":str(SOURCE),"cwd":str(REPLAY),"timeout_seconds":AUDIT_TIMEOUT_SEC,"PYTHONDONTWRITEBYTECODE":"1","start_utc":utc,"end_utc":datetime.now(timezone.utc).isoformat(),"wall_seconds":wall,"child_user_seconds":r1.ru_utime-r0.ru_utime,"child_system_seconds":r1.ru_stime-r0.ru_stime,"child_peak_rss_platform_units":r1.ru_maxrss,"platform":sys.platform,"returncode":code,"timed_out":timeout,"stdout_bytes":len(stdout),"stdout_sha256":hashlib.sha256(stdout).hexdigest(),"stderr_bytes":len(stderr),"stderr_sha256":hashlib.sha256(stderr).hexdigest(),"source_binding_before":before,"source_binding_after":after,"bundle_binding_before":bundle_before,"bundle_binding_after":bundle_after,"output_parse_error":parse_error,"output_sha256":hashlib.sha256(raw).hexdigest(),"reference_sha256":hashlib.sha256(reference).hexdigest(),"author_control_summary":{"passed":result['passed'],"failed":result['failed']} if result else None,"integration_checks":checks,"integration_summary":{"passed":sum(checks.values()),"failed":sum(not v for v in checks.values())},"new_canonical_controls":[r['name'] for r in new_rows if r['name'] not in {oldrow['name'] for oldrow in old_rows}],"source_bound_output_path":str(result_path),"author_code_run_in_place":False,"formal_pipeline_or_audit_run":False}
prefix.with_suffix(".run.json").write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps({k:meta[k] for k in ('wall_seconds','returncode','timed_out','author_control_summary','integration_summary','integration_checks')},indent=2))
if not all(checks.values()):sys.exit(1)
