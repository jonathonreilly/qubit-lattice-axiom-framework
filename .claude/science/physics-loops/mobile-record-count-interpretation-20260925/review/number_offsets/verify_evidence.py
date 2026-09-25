"""Read-only source and output binding checks for the blind PRE."""
from pathlib import Path
from datetime import datetime, timezone
import ast
import hashlib
import json
import subprocess

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def main():
    pins = load(HERE / "SOURCE_PINS.json")
    science_revision = "b47a67e3a08febd2aaf3545eae9a278b4901a72d"
    assert pins["science_revision"] == science_revision
    expected_science = {
        "docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md":
            "c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b",
        "docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md":
            "7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a",
        "docs/FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES_BOUNDED_THEOREM_NOTE_2026-09-24.md":
            "2ae8d264eaff3ab47ecf4ec41fa21178ff444546bcc2e36d885d092732e30516",
    }
    rows = []
    for row in pins["sources"]:
        frozen = HERE / row["frozen_path"]
        assert frozen.stat().st_size == row["bytes"]
        assert sha(frozen) == row["sha256"]
        if "repository" in row:
            original = subprocess.check_output(
                ["git", "show", row["revision"] + ":" + row["git_path"]],
                cwd=row["repository"])
        else:
            original = Path(row["local_path"]).read_bytes()
        assert original == frozen.read_bytes(), row
        if row["role"] == "scientific parent":
            assert row["revision"] == science_revision
            assert row["sha256"] == expected_science[row["git_path"]]
        rows.append({"frozen_path": row["frozen_path"], "sha256": row["sha256"],
                     "origin_matches": True, "role": row["role"]})
    assert len(rows) == 11
    assert sum(row["role"] == "scientific parent" for row in rows) == 3
    assert (HERE / "sources/INSTALLED_PHYSICS_CLAIM_REVIEWER_SKILL.md").read_bytes() == (
        HERE / "sources/docs/ai_methodology/skills/physics-claim-reviewer/SKILL.md").read_bytes()

    execution = load(HERE / "CONTROL_ATTEMPT_01_EXECUTION.json")
    assert execution["exit_code"] == 0
    assert execution["source_sha256"] == sha(HERE / "number_offset_control.py")
    assert execution["stdout_sha256"] == sha(HERE / execution["stdout_file"])
    assert execution["stderr_sha256"] == sha(HERE / execution["stderr_file"])
    assert (HERE / execution["stderr_file"]).stat().st_size == 0
    result = load(HERE / execution["stdout_file"])
    assert result["execution"]["source_sha256"] == execution["source_sha256"]
    assert result["execution"]["author_programs_run_or_imported"] == []
    assert len(result["star"]["words"]) == 4
    assert len(result["star"]["primitive_birth_rows"]) == 4
    assert all(row["number_change"] == 2 for row in result["star"]["primitive_birth_rows"])
    abstract = result["abstract"]
    assert len(abstract["rows"]) == 6
    assert sum(len(row["path_rows"]) for row in abstract["rows"]) == 18
    assert sum(len(row["energy_rows"]) for row in abstract["rows"]) == 9
    assert abstract["max_comparison_error"] < 2e-11
    assert len(abstract["wrong_claim_discriminators"]) == 2
    assert min(row["incorrect_global_rotation_residual"] for row in abstract["wrong_claim_discriminators"]) > 0.08
    modules = []
    for node in ast.walk(ast.parse((HERE / "number_offset_control.py").read_text())):
        if isinstance(node, ast.Import):
            modules.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            modules.append(node.module)
    allowed = {"pathlib", "hashlib", "json", "platform", "time", "itertools",
               "numpy", "numpy.polynomial.legendre", "scipy.linalg", "scipy"}
    assert set(modules) <= allowed
    print(json.dumps({
        "verified_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Evidence binding, origin verification and result inventory; not an audit or an additional physics proof.",
        "source_count": len(rows), "git_origins": sum("repository" in row for row in pins["sources"]),
        "scientific_parents": 3, "source_rows": rows,
        "control_source_sha256": execution["source_sha256"],
        "control_result_sha256": execution["stdout_sha256"],
        "control_import_modules": modules, "control_author_imports": [],
        "star_words": 4, "star_birth_rows": 4, "abstract_cases": 6,
        "abstract_path_rows": 18, "abstract_energy_rows": 9,
        "maximum_control_residual": abstract["max_comparison_error"],
        "PRE_sha256": sha(HERE / "PRE.md"),
        "SOURCE_PINS_sha256": sha(HERE / "SOURCE_PINS.json"),
        "verifier_sha256": sha(Path(__file__).resolve()),
    }, indent=2))


if __name__ == "__main__":
    main()
