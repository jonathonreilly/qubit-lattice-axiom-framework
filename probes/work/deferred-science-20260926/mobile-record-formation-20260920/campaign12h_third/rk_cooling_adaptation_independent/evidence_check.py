#!/usr/bin/env python3
"""Read-only source/stream/data verification after the preserved stderr mistake."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import hashlib
import json
import numpy as np

HERE = Path(__file__).resolve().parent


def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    dependencies = json.loads((HERE/"DEPENDENCIES.json").read_text())["sources"]
    for row in dependencies:
        p = Path(row["path"])
        assert p.stat().st_size == row["bytes"] and digest(p) == row["sha256"]
    rows = []
    for stem, script in [("FINITE_COOLER", "finite_cooler_check.py"),
                         ("GAUSSIAN", "gaussian_check.py"),
                         ("VARIATIONAL", "variational_geometry_check.py")]:
        receipt = json.loads((HERE/(stem+"_RUN_RECEIPT.json")).read_text())
        result = json.loads((HERE/(stem+"_RESULTS.json")).read_text())
        assert receipt["returncode"] == 0
        assert receipt["script_sha256"] == digest(HERE/script) == result["script_sha256"]
        assert (HERE/(stem+"_RUN.log")).read_bytes() == (HERE/(stem+"_RESULTS.json")).read_bytes()
        err = HERE/(stem+"_RUN.stderr")
        if stem == "VARIATIONAL":
            assert digest(err) == "fc6cab0cbebc3c2d31bfed89dc808dbb2fe9b90c4d76db9d45183ffe32db270a"
            assert err.stat().st_size == 548 and err.read_text().count("FutureWarning:") == 1
            assert "cast to float64" in err.read_text()
        else:
            assert not err.read_bytes()
        rows.append({"stem": stem, "script_sha256": digest(HERE/script), "returncode": 0,
                     "stdout_equals_results": True, "stderr_bytes": err.stat().st_size,
                     "stderr_sha256": digest(err)})
    var = json.loads((HERE/"VARIATIONAL_RESULTS.json").read_text())
    datafile = HERE/"VARIATIONAL_COMPONENT.npz"
    assert digest(datafile) == var["data_artifact"]["sha256"]
    with np.load(datafile, allow_pickle=False) as data:
        assert set(data.files) == {"states", "degree", "ground", "variational", "eigenvalues"}
        for key in ["states", "degree", "ground", "variational"]: assert data[key].shape == (864,)
        assert (np.diff(data["states"].astype(np.int64)) > 0).all()
        assert hashlib.sha256(json.dumps(data["states"].tolist()).encode()).hexdigest() == var["geometry"]["component_states_sha256"]
        assert {str(k): v for k, v in Counter(data["degree"].tolist()).items()} == var["flippability_histogram"]
        for key in ["ground", "variational"]:
            assert (data[key] > 0).all()
            assert abs(float(data[key]@data[key])-1) < 1e-12
        fidelity = float((data["ground"]@data["variational"])**2)
        assert abs(fidelity-var["variational_fidelity_numeric"]) < 1e-14
    result = {"created_utc": datetime.now(timezone.utc).isoformat(),
              "script_sha256": digest(Path(__file__)), "source_bindings_match": len(dependencies),
              "scientific_runs": rows, "npz_fields_norms_positivity_and_state_identity_checked": True,
              "npz_recomputed_fidelity": fidelity,
              "preserved_bookkeeping_failure": "failed_attempts/seal_stderr_assumption/",
              "scientific_scripts_or_results_changed": False,
              "new_author_adaptation_contents_accessed": False}
    text = json.dumps(result, indent=2)+"\n"
    (HERE/"EVIDENCE_VERIFICATION.json").write_text(text)
    print(text, end="")


if __name__ == "__main__": main()
