"""Capture the permitted author comparison unit without changing its files."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    "MODE_INVERSE_ROOT_FREEZE_v1.json", "MODE_GAIN_ROOT_FREEZE_v1.json",
    "MODE_INVERSE_NEUTRAL_CONTRACT_v1.json", "MODE_INVERSE_DERIVATION_v1.md",
    "MODE_GAIN_DERIVATION_v1.md", "check_mode_inverse_v1.py",
    "check_mode_inverse_jets_v1.py", "check_mode_gain_v1.py", "check_mode_gain_jets_v1.py",
    "MODE_INVERSE_CONTROLS_v1.json", "MODE_INVERSE_JETS_v1.json",
    "MODE_GAIN_CONTROLS_v1.json", "MODE_GAIN_JETS_v1.json",
    "SCALAR_RESPONSE_DERIVATION_v1.md", "SCALAR_RESPONSE_CLOSURE_v1.md",
    "MATTER_CLOCK_DERIVATION_v2.md", "run_mode_inverse_mutations_v1.py",
    "mode_inverse_mutations_v1/REPORT.json",
]
import argparse,hashlib,json
from pathlib import Path
from datetime import datetime,timezone
parser=argparse.ArgumentParser();parser.add_argument("pack");args=parser.parse_args()
pack=Path(args.pack).resolve();here=Path(__file__).resolve().parent
dest=here/"author_snapshot"
if dest.exists():raise FileExistsError("Do not overwrite a frozen source snapshot")
dest.mkdir()
files={}
for n in AUDIT_INPUT_PATHS:
    data=(pack/n).read_bytes()
    target=dest/n;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
    files[n]={"sha256":hashlib.sha256(data).hexdigest(),"bytes":len(data)}
matches={}
for fn in AUDIT_INPUT_PATHS[:2]:
    f=json.loads((dest/fn).read_text())
    for name,digest in f["sources"].items():
        matches[name]=files[name]["sha256"]==digest
record={"captured_utc":datetime.now(timezone.utc).isoformat(),"source_pack":str(pack),
        "stage":"After independent proof and executable-output freeze; bounded author comparison",
        "author_freeze_matches":matches,"all_author_freeze_matches":all(matches.values()),
        "files":files,
        "historical_integrity_only_copies":["SCALAR_RESPONSE_DERIVATION_v1.md","SCALAR_RESPONSE_CLOSURE_v1.md","MATTER_CLOCK_DERIVATION_v2.md"],
        "no_parent_files_modified":True}
out=here/"AUTHOR_SNAPSHOT_BINDING_v1.json";out.write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps({"all_author_freeze_matches":record["all_author_freeze_matches"],"binding_sha256":hashlib.sha256(out.read_bytes()).hexdigest(),"files":files},indent=2))
if not all(matches.values()):raise SystemExit(1)

