#!/usr/bin/env python3
"""Read-only source/receipt validation; writes only reviewer-owned evidence."""
from pathlib import Path
import datetime
import gzip
import hashlib
import json
import math

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SNAP = HERE/"snapshots_v1"
CHECKS = []


def sha(b):
    return hashlib.sha256(b).hexdigest()


def check(name, condition, **evidence):
    CHECKS.append({"name":name,"pass":bool(condition),**evidence})


def read(name):
    return json.loads((SNAP/name).read_text())


def main():
    for name in ["LINEAGE_RESULTS_v1.json", "ORIGINAL_DISPOSITIONS_v1.json", "EXTERNAL_PRIMARY_PINS_v1.json"]:
        if (HERE/name).exists():
            raise FileExistsError(name)
    pins = json.loads((HERE/"SOURCE_PINS_v1.json").read_text())
    dispositions = []
    for p in pins["sources"]:
        current, recovered = (ROOT/p["path"]).read_bytes(), (HERE/p["snapshot"]).read_bytes()
        check("current_source_and_exact_recovery_"+p["path"], sha(current) == sha(recovered) == p["sha256"]
              and len(current) == p["bytes"])
        dispositions.append({"original_path":str(ROOT/p["path"]),"original_sha256":p["sha256"],
                             "disposition":"checked; unchanged original preserved exactly",
                             "recovery":str(HERE/p["snapshot"]),"final_path":str(ROOT/p["path"]),
                             "final_sha256":sha(current)})
    for freeze_name, key in [("PREPARSE_FREEZE_v1.json","files"),("FREEZE.json","source_hashes"),
                              ("evidence_v1/FREEZE.json","source_hashes"),("evidence_v1/RESULTS.json","source_hashes")]:
        for path, identity in read(freeze_name)[key].items():
            check("freeze_identity_"+freeze_name+"_"+path, sha((SNAP/path).read_bytes()) == identity)
    check("top_freeze_result_identity", sha((SNAP/"evidence_v1/RESULTS.json").read_bytes()) == read("FREEZE.json")["result_sha256"])
    check("execution_freeze_preparse_identity",sha((SNAP/"PREPARSE_FREEZE_v1.json").read_bytes()) == read("evidence_v1/FREEZE.json")["preparse_freeze_sha256"])
    manifest = read("PRIMARY_DATA.json")
    check("execution_data_manifest_identity",read("evidence_v1/FREEZE.json")["data_hashes"] == manifest["files"])
    for path, identity in read("evidence_v1/FREEZE.json")["source_hashes"].items():
        check("author_execution_snapshot_"+path,sha((SNAP/"evidence_v1/source_snapshot"/path).read_bytes()) == identity)
    execution = read("evidence_v1/EXECUTION.json")
    check("single_recorded_author_execution_succeeded",execution["exit_code"] == 0
          and (SNAP/"evidence_v1/stderr.txt").read_bytes() == b"")
    freeze_time = datetime.datetime.fromisoformat(read("evidence_v1/FREEZE.json")["frozen_at"])
    start_time = datetime.datetime.fromisoformat(execution["started_at"])
    end_time = datetime.datetime.fromisoformat(execution["ended_at"])
    check("recorded_freeze_precedes_execution",freeze_time <= start_time < end_time)
    author = read("evidence_v1/RESULTS.json")
    brief = json.loads((SNAP/"evidence_v1/stdout.txt").read_text())
    expected_brief = {"checks":len(author["checks"]),"all_passed":author["all_passed"],
                      "counts":author["processed_data"]["counts"],
                      "contrast":{k:v for k,v in author["processed_data"]["class_contrast"].items() if k != "weights_all_selected"},
                      "curves":{k:{n:v[n] for n in ["intercept_calibration_only","calibration_chi2","calibration_rank","conditional_transfer_chi2","transfer_dimension"]}
                                for k,v in author["processed_data"]["fixed_curves"].items()}}
    check("all_stdout_summary_fields_match_full_result",brief == expected_brief)
    # Validate the exact locally preserved primary bytes; no redownload or mutation.
    external = []
    (HERE/"external_source_snapshots").mkdir(exist_ok=False)
    for entry in read("SOURCE_LEDGER.json")["primary_sources"][0]["artifacts"]:
        p = Path(entry["path"]); b = p.read_bytes()
        check("external_primary_identity_"+p.name,sha(b) == entry["sha256"] and len(b) == entry["bytes"])
        if p.name.endswith(".dat") or p.name.endswith(".cov"):
            name = "table" if p.name.endswith(".dat") else "covariance"
            zipped = SNAP/manifest["files"][name]["local_gzip"]
            check("external_equals_decompressed_numeric_"+name,gzip.decompress(zipped.read_bytes()) == b)
            recovery = {"type":"gzip","path":str(zipped),"decoded_sha256":sha(b)}
        else:
            saved = HERE/"external_source_snapshots"/p.name; saved.write_bytes(b)
            recovery = {"type":"byte_exact_copy","path":str(saved),"sha256":sha(b)}
        external.append({**entry,"reviewer_recovery":recovery})
    # Read every row's three numeric observation fields, including excluded rows.
    table_raw = gzip.decompress((SNAP/manifest["files"]["table"]["local_gzip"]).read_bytes()).decode()
    lines = table_raw.splitlines(); header = lines[0].split()
    table = [dict(zip(header,line.split(),strict=True)) for line in lines[1:] if line.strip()]
    check("all_1701_relevant_observation_fields_finite",all(math.isfinite(float(row[k])) for row in table for k in ["zHD","zHEL","m_b_corr"]))
    # Proof/evolution/result are read separately; these are exact source receipts.
    result = {"created_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"checks":CHECKS,
              "checks_count":len(CHECKS),"all_passed":all(r["pass"] for r in CHECKS),
              "failures":[r for r in CHECKS if not r["pass"]],"original_paths":len(dispositions),
              "external_primary_paths":len(external),"history_limit":"Hashes and recorded timestamps verify source continuity, not an independent observation of the author's prior knowledge or absence of array inspection."}
    for name,data in [("LINEAGE_RESULTS_v1.json",result),("ORIGINAL_DISPOSITIONS_v1.json",dispositions),
                       ("EXTERNAL_PRIMARY_PINS_v1.json",external)]:
        (HERE/name).write_text(json.dumps(data,indent=2)+"\n")
    print(json.dumps({k:result[k] for k in ["checks_count","all_passed","failures","original_paths","external_primary_paths"]},indent=2))


if __name__ == "__main__":
    main()
