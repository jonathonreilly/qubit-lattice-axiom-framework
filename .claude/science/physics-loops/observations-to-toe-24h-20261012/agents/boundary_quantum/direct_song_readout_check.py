#!/usr/bin/env python3
"""Personally recheck fixed inherited public-data predictions; never refit."""
import os
for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[name] = "1"
import hashlib
import json
import math
import time
from fractions import Fraction as F
from pathlib import Path
import numpy as np
import openpyxl

HERE = Path(__file__).resolve().parent
RUNTIME = Path("/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012")
OUT = RUNTIME / "quantum/direct_song_readout"

def main():
    clock = json.loads((RUNTIME / "DEADLINE.json").read_text())
    assert time.time() < clock["packaging_epoch"]
    assert not any((RUNTIME / n).exists() for n in ("STOP_REQUESTED", "USER_STOP_REQUESTED", "STOP_REQUESTED.json", "USER_STOP_REQUESTED.json"))
    protocol = json.loads((OUT / "PROTOCOL_v1.json").read_text())
    for item in protocol["inputs"]:
        assert hashlib.sha256(Path(item["path"]).read_bytes()).hexdigest() == item["sha256"]
    predfile = HERE / "CALIBRATION_AND_PREDICTIONS_FREEZE.json"
    assert hashlib.sha256(predfile.read_bytes()).hexdigest() == protocol["calibration_freeze_sha256_expected"]
    (OUT / "EXECUTION_SOURCE_v1.json").open("x").write(json.dumps({"source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "protocol_sha256": hashlib.sha256((OUT / "PROTOCOL_v1.json").read_bytes()).hexdigest()}, indent=2) + "\n")
    frozen = json.loads(predfile.read_text())
    tests = json.loads((HERE / "HELDOUT_RESULTS.json").read_text())
    source = json.loads((HERE / "SOURCES.json").read_text())["files"][0]
    workbook = openpyxl.load_workbook(source["path"], data_only=True, read_only=True)
    sheet = workbook["Figure4d"]
    for row in frozen["calibration_data"] + tests["data"]:
        triplet = list(sheet[row["source_cells"]][0])
        assert [float(c.value) for c in triplet] == [float(row["angle"]), row["value"], row["error"]]
    workbook.close()

    def means(model, rows):
        p = frozen["models"][model]["parameters"]
        values = []
        for row in rows:
            j = row["j"]
            t = math.radians(2 * (2 * row["angle"] - 45 * j - p[3*j+2]))
            c = math.cos(t)
            if model == "quantum":
                shape = c
            else:
                u = 2 / math.pi * math.asin(c)
                k = p[6] if model == "boundary" else 0.
                shape = math.copysign(1., u) if abs(u) == 1 else math.tanh(math.atanh(u) + k*c)
            values.append(math.exp(p[3*j]) * (1 + p[3*j+1] * shape))
        return np.asarray(values)

    models = {}
    y = np.array([r["value"] for r in tests["data"]])
    sigma = np.array([r["error"] for r in tests["data"]])
    cy = np.array([r["value"] for r in frozen["calibration_data"]])
    cs = np.array([r["error"] for r in frozen["calibration_data"]])
    for model, old in frozen["models"].items():
        mu = means(model, tests["data"])
        max_mean_change = float(np.max(np.abs(mu-np.asarray(old["predicted_test_mean"]))))
        assert max_mean_change < 1e-8
        residual = y-mu
        score = float(np.sum((residual/sigma)**2))
        calibration = float(np.sum(((cy-means(model, frozen["calibration_data"]))/cs)**2))
        covariance = np.diag(sigma*sigma) + np.asarray(old["local_prediction_covariance"])
        propagated = float(residual @ np.linalg.solve(covariance, residual))
        recorded = tests["models"][model]
        assert abs(score-recorded["test_weighted_square_fixed_parameters"]) < 1e-7
        assert abs(propagated-recorded["test_weighted_square_with_local_correlated_prediction_uncertainty"]) < 1e-7
        assert abs(calibration-old["calibration_weighted_square"]) < 1e-7
        models[model] = {"maximum_prediction_difference": max_mean_change, "calibration_score": calibration, "fixed_test_score": score, "supplied_covariance_test_score": propagated}
    data = {(r["basis"], r["angle"]): r for r in frozen["calibration_data"]}
    floor = F(0)
    pairs = []
    for basis in ("H", "D"):
        for angle in (0, 20, 40, 60):
            a,b = data[basis, angle], data[basis, angle+180]
            v1,v2,e1,e2 = (F(str(x)) for x in (a["value"],b["value"],a["error"],b["error"]))
            value = (v1-v2)**2 / (e1*e1 + e2*e2)
            floor += value
            pairs.append({"basis": basis, "angles": [angle,angle+180], "floor": float(value)})
    oldfloor = json.loads((HERE / "SOURCE_DIAGNOSTICS_AND_PROSPECTIVE.json").read_text())["calibration_periodic_repeat_score_floor"]
    assert abs(float(floor)-oldfloor) < 1e-10
    for item in protocol["inputs"]:
        assert hashlib.sha256(Path(item["path"]).read_bytes()).hexdigest() == item["sha256"]
    result = {"author": "direct parent check", "source_cells_verified": 36, "models": models,
              "stationary_repeat_floor": {"numerator": str(floor.numerator), "denominator": str(floor.denominator), "float": float(floor)}, "pairs": pairs,
              "scope": "Post-exposure reproduction of inherited fixed prediction scores and observed-cell values. No fit, independent new test, validated confidence, causal attribution or fundamental-law exclusion. Supplied local prediction covariance arithmetic checked, not its statistical coverage or fitted Jacobian."}
    (OUT / "RESULTS_v1.json").open("x").write(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))

if __name__ == "__main__":
    main()
