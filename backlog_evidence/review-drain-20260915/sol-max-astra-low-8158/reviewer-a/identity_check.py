"""Verify all frozen packet file identities and inspect the changed graph node."""

import hashlib
import json
from pathlib import Path

PACKET = Path("/private/tmp/review-drain-20260915/sol-max-astra-low-8158/packet")
manifest = json.loads((PACKET / "manifest.json").read_text())
for record in manifest["files"]:
    data = (PACKET / record["path"]).read_bytes()
    assert len(data) == record["bytes"], record["path"]
    assert hashlib.sha256(data).hexdigest() == record["sha256"], record["path"]
print(f"verified {len(manifest['files'])} manifest file hashes and byte lengths")

graph = json.loads((PACKET / "docs/audit/data/citation_graph_manifest.json").read_text())
claim = "admissibility_rule_unrecorded_sites_free_window_versus_integrated_exterior_readings_differ_iff_an_unrecorded_component_touches_two_recorded_sites_bounded_theorem_note_2026-09-15"
print("changed graph node:", graph["nodes"][claim])
