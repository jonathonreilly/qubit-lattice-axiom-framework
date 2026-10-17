"""Bookkeeping validation and final freeze; no scientific program replay."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
import re

D=Path(__file__).resolve().parent
def ident(p):
    b=p.read_bytes(); s=p.stat()
    return {"sha256":sha256(b).hexdigest(),"bytes":len(b),"device":s.st_dev,"inode":s.st_ino,"mtime_ns":s.st_mtime_ns}
def short(p):
    v=ident(p); return {"path":str(p.relative_to(D)),"sha256":v["sha256"],"bytes":v["bytes"]}
def save(p,obj):
    with p.open("x") as f:
        json.dump(obj,f,indent=2); f.write("\n"); f.flush(); os.fsync(f.fileno())
def date(t): return datetime.fromisoformat(t.replace("Z","+00:00"))

started=datetime.now(timezone.utc).isoformat()
m=json.loads((D/"SOURCE_MANIFEST.json").read_text())
pre=json.loads((D/"run01/PRELAUNCH.json").read_text())
receipt=json.loads((D/"run01/RECEIPT.json").read_text())
out=json.loads((D/"run01/stdout.json").read_text())
plan=json.loads((D/"RESOURCE_PLAN.json").read_text())
originals=[]
for e in m["entries"]:
    snap=ident(D/e["snapshot"]); original=ident(Path(e["original"]))
    assert snap["sha256"]==original["sha256"]==e["sha256"]
    assert snap["bytes"]==original["bytes"]==e["bytes"]
    originals.append({"snapshot":e["snapshot"],"original":e["original"],"sha256":e["sha256"],"bytes":e["bytes"],"matching":True})
for e in pre["bindings"]:
    p=Path(e["path"])
    if not p.is_absolute(): p=D/p
    assert ident(p)==e["identity"],e["label"]
    aft=next(x for x in receipt["bindings_after"] if x["label"]==e["label"])
    assert aft["identity"]==e["identity"] and aft["unchanged"]
assert ident(D/"run01/PRELAUNCH.json")==receipt["prelaunch_identity"]
assert ident(D/"run01/stdout.json")==receipt["stdout"]
assert ident(D/"run01/stderr.txt")==receipt["stderr"]
assert ident(D/"check_bounds.py")["sha256"]==ident(D/"run01/executed_source.py")["sha256"]==out["source_identity"]["executed_sha256"]
assert receipt["returncode"]==0 and not receipt["timed_out"]
assert receipt["prelaunch_unchanged"] and receipt["all_bindings_unchanged"] and receipt["all_original_source_contents_unchanged"]
assert all(out["checks"].values()) and out["status"]=="PASS_exact_scalar_corroboration_only"
assert plan["maximum_scientific_runs_without_written_amendment"]==1
assert [x.name for x in D.glob("run[0-9][0-9]")]==["run01"]
assert date(pre["created_before_subprocess_utc"]) < date(receipt["prelaunch_fsync_completed_utc"]) < date(receipt["subprocess_created_after_utc"]) < date(out["started_utc"]) < date(receipt["finished_utc"])
assert (D/"RESOURCE_PLAN.json").stat().st_mtime_ns < (D/"run01/PRELAUNCH.json").stat().st_mtime_ns
assert not (D/"launch01.stderr").read_bytes() and not (D/"run01/stderr.txt").read_bytes()
wrapper=json.loads((D/"launch01.stdout").read_text())
assert wrapper["returncode"]==receipt["returncode"]==0
known={ident(p)["sha256"] for p in D.rglob("*") if p.is_file()}
known.update(e["identity"]["sha256"] for e in pre["bindings"])
claims=set(re.findall(r"\b[0-9a-f]{64}\b",(D/"CANDIDATE.md").read_text()))
assert claims <= known,sorted(claims-known)
validation={"started_utc":started,"finished_utc":datetime.now(timezone.utc).isoformat(),"type":"hash/generation/chronology/bookkeeping only; no scientific replay", "all_passed":True,"source_pairs":originals,"prelaunch_binding_count":len(pre["bindings"]),"runtime_binding_count":sum(x["label"].startswith("runtime:") for x in pre["bindings"]),"actual_scientific_runs":1,"all_stdout_assertions_recorded_true":True,"full_streams_retained":True,"candidate_sha256":ident(D/"CANDIDATE.md")["sha256"],"checker_sha256":ident(D/"check_bounds.py")["sha256"],"no_transitive_runtime_completeness_claim":True}
save(D/"STATIC_VALIDATION.json",validation)
files=[short(p) for p in sorted(D.rglob("*")) if p.is_file() and p.name not in {"FILE_MANIFEST.json","FREEZE.json"}]
save(D/"FILE_MANIFEST.json",{"created_utc":datetime.now(timezone.utc).isoformat(),"scope":"all packet regular files except this manifest and FREEZE.json", "files":files})
freeze={"frozen_utc":datetime.now(timezone.utc).isoformat(),"status":"Frozen conditional author candidate, awaiting distinct independent and root checks; no retained/audit/publication claim", "candidate":short(D/"CANDIDATE.md"),"file_manifest":short(D/"FILE_MANIFEST.json"),"packet_files_including_manifest_and_freeze":len(files)+2,"source_snapshots":len(m["entries"]),"scientific_runs":1,"scientific_checker":short(D/"check_bounds.py"),"prelaunch":short(D/"run01/PRELAUNCH.json"),"receipt":short(D/"run01/RECEIPT.json"),"scientific_output":short(D/"run01/stdout.json"),"validation":short(D/"STATIC_VALIDATION.json"),"scope":"Exact ladder, sigma1e-6, kappa in[1e-12,1e-8]; actual complete comparator; T=1/kappa^2; M=ceil(50T) for[T,2T] only", "claimed_bounds":{"infinite":".003832","finite":".004832"},"failed_routes_preserved":"FAILURES.md and complete scientific output", "no_editable_prompt_files_changed":True,"no_delegation":True,"campaign_deadline_utc":"2026-10-17T23:07:27Z"}
save(D/"FREEZE.json",freeze)
print(json.dumps({"candidate":short(D/"CANDIDATE.md"),"freeze":short(D/"FREEZE.json"),"file_count":len(files)+2,"scientific_runs":1,"source_pairs_validated":len(originals),"all_prelaunch_bindings_unchanged":True,"status":"Frozen unqualified candidate"},indent=2))
