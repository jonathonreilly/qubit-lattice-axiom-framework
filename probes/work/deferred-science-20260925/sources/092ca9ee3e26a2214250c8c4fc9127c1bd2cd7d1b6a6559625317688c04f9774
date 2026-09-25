"""Final scoped evidence verification; no author or publication runner execution."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

HERE = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def main():
    pins = load(HERE / "PUBLICATION_SOURCE_PINS.json")
    for source in pins["sources"]:
        origin = Path(source["path"])
        assert digest(origin) == source["sha256"], str(origin)
        assert origin.stat().st_size == source["bytes"]
        frozen = HERE / source["frozen_path"]
        assert digest(frozen) == source.get("frozen_sha256", source["sha256"]), str(frozen)
    seals = pins["prior_seals_verified"]
    for prior in seals:
        directory = Path(prior["directory"])
        seal = directory / prior["seal"]
        assert digest(seal) == prior["sha256"]
        manifest = load(seal)
        assert len(manifest["members"]) == prior["members_verified"]
        for member in manifest["members"]:
            path = directory / member["path"]
            assert digest(path) == member["sha256"]
            assert path.stat().st_size == member["bytes"]
    binding = load(HERE / "PUBLICATION_BINDING_RESULTS.json")
    metadata = load(HERE / "PUBLICATION_METADATA_CHECKS.json")
    assert binding["comparison_code_sha256"] == digest(HERE / "publication_bind_part_a.py")
    assert binding["source_pins_sha256"] == digest(HERE / "PUBLICATION_SOURCE_PINS.json")
    assert metadata["code_sha256"] == digest(HERE / "publication_metadata_checks.py")
    assert binding["author_programs_executed_or_imported"] == []
    assert all(row["all_scientific_leaves_equal"] for row in binding["payload_comparisons"])
    assert sum(sum(row["leaf_counts"].values()) for row in binding["payload_comparisons"]) == 17107
    assert sum(len(row["metadata_differences"]) for row in binding["payload_comparisons"]) == 3
    assert metadata["entire_cache_matches_writer_format_and_execution"]
    assert not metadata["combined_raw_input_fingerprint_independently_recomputed"]
    assert metadata["direct_scoped_input_byte_checks"] == 7
    helper = metadata["cache_helper"]
    assert digest(Path(helper["path"])) == helper["sha256"]
    assert digest(HERE / helper["frozen_excerpt"]) == helper["excerpt_sha256"]
    for filename in ("PUBLICATION_BINDING_STDERR.txt", "PUBLICATION_METADATA_CHECKS_STDERR.txt"):
        assert (HERE / filename).stat().st_size == 0
    incident = load(HERE / "PUBLICATION_SCOPE_INCIDENT.json")
    assert incident["first_incident"]["combined_stdout_copied_into_scoped_evidence"] is False
    assert incident["first_incident"]["scientific_Part_B_conclusion_drawn"] is False
    print(json.dumps({
        "verified_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Part A source/output correspondence, existing seals and explicit process limits only.",
        "publication_source_records_verified": len(pins["sources"]),
        "preserved_seal_member_counts": [row["members_verified"] for row in seals],
        "exact_runtime_files": 2, "exact_payload_leaves_compared": 17107,
        "allowed_metadata_differences": 3, "scientific_value_differences": 0,
        "cache_body_scope": "Verified writer-formatted tail; complete combined stdout not copied.",
        "combined_input_fingerprint_scope": "Recorded metadata; full excluded raw inputs not independently recomputed.",
        "scope_incident_preserved": True, "author_programs_run": [],
        "report_sha256": digest(HERE / "PUBLICATION_COMPARISON.md"),
        "source_pins_sha256": digest(HERE / "PUBLICATION_SOURCE_PINS.json"),
        "binding_results_sha256": digest(HERE / "PUBLICATION_BINDING_RESULTS.json"),
        "metadata_checks_sha256": digest(HERE / "PUBLICATION_METADATA_CHECKS.json"),
        "scope_incident_sha256": digest(HERE / "PUBLICATION_SCOPE_INCIDENT.json"),
        "verifier_sha256": digest(Path(__file__).resolve())
    }, indent=2))


if __name__ == "__main__":
    main()
