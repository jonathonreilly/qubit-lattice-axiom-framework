"""Final bookkeeping only: verify immutable evidence and freeze this owned packet."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import os

D=Path(__file__).resolve().parent
def digest(p): return sha256(p.read_bytes()).hexdigest()
manifest=json.loads((D/"SOURCE_MANIFEST.json").read_text())
receipt=json.loads((D/"run01/RECEIPT.json").read_text())
out=json.loads((D/"run01/stdout.json").read_text())
assert receipt["returncode"]==0 and not receipt["timed_out"]
assert receipt["all_bindings_unchanged"] and receipt["prelaunch_unchanged"]
assert out["status"]=="completed"
assert all(r["result"].get("satisfied",True) for r in out["records"])
assert digest(D/"check_route.py")==digest(D/"run01/executed_source.py")==out["source_sha256"]
assert digest(D/"run01/PRELAUNCH.json")==out["prelaunch_sha256"]==receipt["prelaunch_identity"]["sha256"]
assert digest(D/"run01/stdout.json")==receipt["stdout"]["sha256"]
assert digest(D/"run01/stderr.txt")==receipt["stderr"]["sha256"]
sources=[]
for e in manifest["entries"]:
    assert digest(D/e["snapshot"])==e["sha256"]
    current=digest(Path(e["original"]))
    sources.append({"snapshot":e["snapshot"],"snapshot_sha256":e["sha256"],"original_current_sha256":current,"original_still_equal":current==e["sha256"]})
files=[]
for p in sorted(D.rglob("*")):
    if p.is_file() and p.name!="FREEZE.json":
        files.append({"path":str(p.relative_to(D)),"sha256":digest(p),"bytes":p.stat().st_size})
result={
 "frozen_utc":datetime.now(timezone.utc).isoformat(),
 "status":"unqualified author worked failure; separate decisive review pending",
 "primary":"ROUTE.md",
 "primary_sha256":digest(D/"ROUTE.md"),
 "scope":"Two-rail realification of the qualified exact-ladder family, with the actual e0 product seed; no general real-Hamiltonian no-go",
 "proposed_complete_isometry_lower_bounds":{"infinite":"strictly greater than 0.53 for all t>=10^6/kappa^2","finite":"strictly greater than 0.52 on [T,2T], M=ceil(50T) per rail"},
 "scientific_attempts":1,
 "actual_maximum_matrix_dimension":6,
 "actual_graph_vertices":46,
 "exact_core_parameter":"kappa=10^-8; transfer by analytical homogeneity, no sampling study",
 "actual_execution_receipt":"run01/RECEIPT.json",
 "prelaunch_serialization_and_fsync_before_subprocess":True,
 "independent_review_performed_for_this_packet":False,
 "root_acceptance_for_this_packet":False,
 "prompt_files_modified":[],
 "worktree_git_checkpoint_axiom_audit_changes":False,
 "original_source_contents_at_freeze":sources,
 "all_original_source_contents_still_equal":all(x["original_still_equal"] for x in sources),
 "files":files,
 "freeze_self_in_inventory":False
}
with (D/"FREEZE.json").open("x") as f:
    json.dump(result,f,indent=2);f.write("\n");f.flush();os.fsync(f.fileno())
fd=os.open(D,os.O_RDONLY)
try:os.fsync(fd)
finally:os.close(fd)
print(json.dumps({"files":len(files),"primary_sha256":result["primary_sha256"],"freeze_sha256":digest(D/"FREEZE.json"),"all_original_source_contents_still_equal":result["all_original_source_contents_still_equal"]},indent=2))
