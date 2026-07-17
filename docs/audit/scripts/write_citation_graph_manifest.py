#!/usr/bin/env python3
"""Write the tracked citation-graph manifest from the in-pass graph cache.

The manifest (docs/audit/data/citation_graph_manifest.json) is the
acknowledgment surface for graph topology: one entry per node with its
out-degree and a hash of its sorted dependency list. Criticality is graph
topology only (FRESH_LOOK_REQUIREMENTS section 4), so any change that adds,
removes, or rewires nodes must ship the refreshed manifest — making the
topology delta reviewable in the diff instead of silently reshaping
audit-lane prioritization. repo_invariants_check compares a recomputation
against the INDEX version and fails (under --enforce-links) on any
unacknowledged delta.

Deterministic: same citation_graph.json -> byte-identical manifest.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
GRAPH_PATH = REPO_ROOT / "docs" / "audit" / "data" / "citation_graph.json"
MANIFEST_PATH = REPO_ROOT / "docs" / "audit" / "data" / "citation_graph_manifest.json"


def compute_manifest(graph: dict) -> dict:
    nodes: dict[str, dict] = {}
    for node_id in sorted(graph.get("nodes", {})):
        deps = sorted(graph["nodes"][node_id].get("deps", []))
        nodes[node_id] = {
            "out_degree": len(deps),
            "deps_hash": hashlib.sha256("\n".join(deps).encode("utf-8")).hexdigest()[:12],
        }
    return {
        "schema_version": 1,
        "node_count": len(nodes),
        "edge_count": sum(entry["out_degree"] for entry in nodes.values()),
        "nodes": nodes,
    }


def main() -> None:
    with GRAPH_PATH.open(encoding="utf-8") as fh:
        graph = json.load(fh)
    manifest = compute_manifest(graph)
    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=1, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        f"Wrote {MANIFEST_PATH.relative_to(REPO_ROOT)} "
        f"({manifest['node_count']} nodes, {manifest['edge_count']} edges)"
    )


if __name__ == "__main__":
    main()
