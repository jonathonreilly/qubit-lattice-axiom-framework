#!/usr/bin/env python3
"""Post-seal authentication and selective arithmetic; no author execution."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math

OUT = Path(__file__).resolve().parent
RAW = OUT.parent


def identity(p):
    b = p.read_bytes()
    return {"path": str(p), "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}


def verify(row, alternate=None):
    p = Path(row["path"]) if alternate is None else alternate
    got = identity(p)
    assert got["bytes"] == row["bytes"], (p, got, row)
    assert got["sha256"] == row["sha256"], (p, got, row)
    return got


def main():
    seal = json.loads((OUT / "PRE_COMPARISON_SEAL.json").read_text())
    for row in seal["artifacts"] + seal["dependencies"]:
        verify(row)
    fix = RAW / "dimer_routed_moving_geometry_f1_fix"
    change = json.loads((fix / "F1_CHANGE.json").read_text())
    before = Path(change["before"]["path"])
    after = Path(change["after"]["path"])
    verify(seal["primary_note"], before)
    verify(change["before"])
    verify(change["after"])
    old, new = before.read_text(), after.read_text()
    removed, inserted = change["removed"], change["inserted"]
    assert old.count(removed) == 1
    assert new.count(inserted) == 1
    assert old.replace(removed, inserted) == new
    assert new.replace(inserted, removed) == old
    assert "propagation matrix A(Q)" in inserted
    assert "orbit-isotropic p_a=rho_A/6 on A and p_a=rho_B/8 on B" in inserted
    assert "nonzero gamma and fixed nonzero Q in this isotropic specialization" in inserted
    assert "At gamma=0 all thirteen" in inserted

    result_path = RAW / "dimer_routed_moving_geometry_checks/RESULTS.json"
    result = json.loads(result_path.read_text())
    assert result["status"] == "pass"
    authenticated = []
    for name, sha in result["sources"].items():
        p = before if name == "DIMER_ROUTED_MOVING_GEOMETRY_EXTENSION.md" else RAW / name
        row = identity(p)
        assert row["sha256"] == sha
        authenticated.append(row)
    groups = []
    for group in ["geometry_and_dirichlet", "switched_energy"]:
        p = result_path.parent / (group + ".json")
        assert json.loads(p.read_text()) == result[group]
        groups.append(identity(p))

    geometry = []
    for row in result["geometry_and_dirichlet"]["rows"]:
        N = row["N"]
        assert row["pairs"] == N ** 3 // 2
        assert row["immutable_rotation_replays"] == 2 * row["flippable_squares"]
        assert row["exact_color_projections_and_form_coefficients"] is True
        if row["kind"] == "winding":
            assert row["flippable_squares"] == 0
            predicted = 0.0
        else:
            # In the author's three mode list the axis mode gives this maximum.
            predicted = (math.sin(math.pi / N) / (math.pi / N)) ** 2
            if row["kind"] == "columnar":
                assert row["flippable_squares"] == N ** 3
        err = abs(row["maximum_scaled_geometric_increment"] - predicted)
        assert err < 2e-14
        geometry.append({"N": N, "kind": row["kind"], "formula_error": err})

    energy = []
    for i, row in enumerate(result["switched_energy"]["rows"]):
        assert row["states"] == 4 + i % 3
        assert row["intervals"] == 1 + i % 8
        ws = row["interval_witnesses"]
        assert len(ws) == row["intervals"]
        bound = math.fsum(2 * w["duration"] * w["hminus"] for w in ws)
        assert all(w["duration"] > 0 and w["hminus"] >= 0 for w in ws)
        assert abs(bound - row["energy_upper_bound"]) < 5e-13
        second = row["integral_second_moment"]
        assert 0 <= second <= bound + 2e-10 * max(1.0, bound)
        assert abs(second / bound - row["ratio"]) < 2e-15
        energy.append({"row": i, "bound_reconstruction_error": abs(bound - row["energy_upper_bound"])})
    assert len(energy) == 40
    maximum = max(r["ratio"] for r in result["switched_energy"]["rows"])
    assert maximum == result["switched_energy"]["maximum_ratio"]
    log = RAW / "DIMER_ROUTED_MOVING_GEOMETRY_RUN.log"
    err = RAW / "DIMER_ROUTED_MOVING_GEOMETRY_RUN.stderr"
    assert log.read_text() == "geometry_and_dirichlet PASS\nswitched_energy PASS\n"
    assert not err.read_bytes()

    receipt = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Source authentication and independent arithmetic of saved author witnesses; does not replay author random cases or count authentication as independent science.",
        "precomparison_artifacts_unchanged": len(seal["artifacts"]),
        "precomparison_dependencies_unchanged": len(seal["dependencies"]),
        "original_note_authentication_alias": identity(before),
        "F1": {
            "status": "closed",
            "current_note": identity(after),
            "change_receipt": identity(fix / "F1_CHANGE.json"),
            "complete_forward_and_inverse_string_recovery": True,
            "only_one_paragraph_changed": True,
            "interpretation": "Arbitrary full-support p matrix conclusion retained; scalar speed and four/nine count explicitly restricted to orbit-isotropic p, nonzero gamma and nonzero Fourier mode. Both masses are positive from the unchanged full-support premise. Gamma-zero degeneration retained.",
        },
        "author_sources_authenticated": authenticated,
        "author_evidence": [identity(result_path)] + groups + [identity(log), identity(err)],
        "author_group_payloads_match_complete_results": True,
        "geometry_arithmetic": geometry,
        "energy_arithmetic": energy,
        "maximum_author_energy_ratio": maximum,
        "author_scientific_computations_rerun": False,
        "dynamic_aggregate_outputs_accessed": False,
        "unresolved_findings": [],
    }
    (OUT / "POST_COMPARISON_RESULTS.json").write_text(json.dumps(receipt, indent=2) + "\n")
    (OUT / "F1_CORRECTION_ACK.json").write_text(json.dumps(receipt["F1"], indent=2) + "\n")
    print(json.dumps({"status": "pass", "precomparison_artifacts": len(seal["artifacts"]), "dependencies": len(seal["dependencies"]), "geometry_rows": len(geometry), "energy_rows": len(energy), "F1": "closed"}))


if __name__ == "__main__":
    main()
