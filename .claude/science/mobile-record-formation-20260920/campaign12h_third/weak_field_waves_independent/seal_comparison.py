"""Authenticate the immutable PRE and bounded author packet; seal this comparison."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
BASE = HERE.parent


def identity(path):
    path = Path(path).resolve()
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data), "sha256": sha256(data).hexdigest()}


def verify(rows):
    for row in rows:
        assert identity(row["path"]) == row, row["path"]


pre_path = HERE/"PRE_COMPARISON_SEAL.json"
author_path = BASE/"WEAK_FIELD_WAVEPACKET_AUTHOR_SEAL.json"
assert identity(pre_path)["sha256"] == "d17725c9c6f2b1a973ea89791402c94b1ee87759164a9a551c38b7b499fcf0f6"
assert identity(author_path)["sha256"] == "d05a600d964abc3ae99ce80f1df6e710a33f1fb21415e830821957972a11eaf3"
pre = json.loads(pre_path.read_text())
author = json.loads(author_path.read_text())
verify(pre["sources"]+pre["artifacts"])
verify(author["artifacts"])
context = json.loads((BASE/"WEAK_FIELD_WAVEPACKET_SOURCE_CONTEXT.json").read_text())
verify(context["dependencies"])
result = json.loads((HERE/"COMPARISON_RESULTS.json").read_text())
receipt = json.loads((HERE/"COMPARISON_CHECK_RECEIPT.json").read_text())
assert result["status"] == "PASS" and receipt["exit_code"] == 0
verify([result["runner"],receipt["runner"],receipt["stdout"],receipt["stderr"]])
assert (HERE/"COMPARISON_CHECK.stderr").read_bytes() == b""
assert (HERE/"COMPARISON_CHECK.stdout").read_bytes() == (HERE/"COMPARISON_RESULTS.json").read_bytes()
sources = {}
for row in pre["sources"]+author["artifacts"]+context["dependencies"]:
    if row["path"] in sources:
        assert sources[row["path"]] == row
    sources[row["path"]] = row
sources = sorted(sources.values(),key=lambda x:x["path"])
artifacts = [identity(path) for path in sorted(HERE.rglob("*"))
             if path.is_file() and "__pycache__" not in path.parts
             and path.name not in ("CHECKPOINT.md","PRE_COMPARISON_SEAL.json","FINAL_SEAL.json")]
target = HERE/"FINAL_SEAL.json"
assert not target.exists(), "Do not overwrite a seal."
out = {
    "created_utc": datetime.now(timezone.utc).isoformat(),
    "status": "Bounded author-source scientific comparison complete; no formal audit, publication or retained status.",
    "pre_comparison_seal": identity(pre_path), "author_seal": identity(author_path),
    "sources": sources, "artifacts": artifacts,
    "counts": {"sources": len(sources), "artifacts": len(artifacts),
               "listed_bindings": len(sources)+len(artifacts), "additional_top_level_seals": 2},
    "disposition": "No substantive mathematical defect, required scope correction, or source-binding defect found.",
    "proved_scope": "Finite fixed box, zero electric winding, explicitly prepared cutoff packet, fixed sqrt(KJ)=c/(2a), O(g^2) norm accuracy on fixed times; subsequent fixed finite-mode continuum limit and record composition in stated order.",
    "complete_new_read_coverage": "All bound author scientific note, complete runner, all result fields, source context and receipt; stdout authenticated byte-identical to the fully read JSON, stderr authenticated empty.",
    "reused_dependencies": "Identity-matched complete prior large-spin and uniform-local comparisons; not re-proved or re-executed in this task.",
    "new_execution": "One standalone comparison checker, first execution passed. Exact symbolic scaling, alternative Fourier-trace vacuum coefficient, one independent FFT/sparse-exponential loop control, and stored arithmetic checks.",
    "author_runner_executed": False,
    "read_rerun_limits": [
        "No full repeat of author dense cubic diagonalizations or all compact-loop energy/evolution runs.",
        "Floating finite controls are not interval eigenvalue enclosures; packet theorem checked analytically.",
        "No new external literature read or theorem imported; author historical reading claims not independently certified.",
        "Other new content, static-source, homogeneous, ramp, energy, transport, checkpoint and registry sources remained unopened."
    ],
    "failures": "No failed scientific or helper execution in the blind or comparison packet; all logs retained.",
    "immutable_history": "All 25 PRE bindings and the PRE seal re-authenticated without change.",
    "mutable_exclusion": "CHECKPOINT.md is an unsealed recovery aid."
}
target.write_text(json.dumps(out,indent=2)+"\n")
final = json.loads(target.read_text())
verify(final["sources"]+final["artifacts"])
verify([final["pre_comparison_seal"],final["author_seal"]])
print(json.dumps({"report": identity(HERE/"COMPARISON.md"), "final_seal": identity(target),
                  "counts": final["counts"], "all_bindings_verified": True},indent=2))
