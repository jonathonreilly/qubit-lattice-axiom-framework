#!/usr/bin/env python3
"""Certificate: the audit dependency graph is acyclic after the 2026-06-14
keystone cycle-break, the six spurious pointer edges are gone, and every
load-bearing synthesis dependency that shared a cycle with them is preserved.

Context
-------
The audit lane builds a claim DEPENDENCY graph from markdown notes: every
markdown link `[..](OTHER.md)` is treated as a load-bearing dependency edge
(see docs/audit/scripts/build_citation_graph.py). A row can only be marked
`ready` for audit once all its dependencies are at retained-grade, so any
mutual-dependency cycle (strongly-connected component, SCC) permanently
blocks every row inside it from ever becoming auditable.

On origin/main (2026-06-14) the graph carried TWO non-trivial SCCs:
  * a 219-node keystone tangle (max downstream fanout 1136: the
    staggered-Dirac gate / single-clock / observable-principle cluster);
  * a 10-node hierarchy-alpha_LM cluster.

Both were held together purely by ANACHRONISTIC pointer edges: an older note
markdown-linking a strictly later-dated note as a "follow-up source",
"downstream -> this gate" probe, or "no longer retained authority" Tier-A
carrier alias. Those links are navigational, not proof dependencies, and the
citing notes' own prose says so. Demoting the six minimal pointer links from
markdown links to plain back-ticked filenames removes the spurious edges and
turns the graph into a DAG, WITHOUT editing any audited note (so no audit
verdict is reset) and WITHOUT touching any genuine dependency.

This runner re-proves those properties against the live committed graph. It is
deterministic, offline, read-only, and sets no audit status.

Run: python3 scripts/audit_keystone_cycle_break_certificate_2026_06_14.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
GRAPH = REPO / "docs" / "audit" / "data" / "citation_graph.json"

GATE = "staggered_dirac_realization_gate_note_2026-05-03"
HUB = "hierarchy_alpha_lm_magnitude_delta0_open_gate_note_2026-05-30"

# The six spurious pointer edges demoted by this change (must be ABSENT).
DEMOTED_EDGES = [
    ("axiom_first_lattice_noether_theorem_note_2026-04-29", GATE),
    ("axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03",
     "single_clock_axis_selection_from_record_durability_narrow_no_go_note_2026-06-11"),
    (HUB, "hierarchy_delta0_blocking_single_mode_decimation_probe_note_2026-06-11"),
    (HUB, "hierarchy_delta0_ratio_normalized_alpha_s_per_decoupling_reduction_note_2026-06-11"),
    (HUB, "hierarchy_delta0_s1prime_taste_region_kernel_share_probe_note_2026-06-11"),
    (HUB, "hierarchy_delta0_b4_attachment_observable_enumeration_note_2026-06-11"),
]

# Genuine synthesis dependencies the gate legitimately consumes: these MUST
# remain present (they are the reason the gate cut was made on the back-edges,
# not on the gate's real component deps).
PRESERVED_EDGES = [
    (GATE, "staggered_dirac_physical_species_direct_theorem_note_2026-05-07"),
    (GATE, "staggered_dirac_substep4_labeling_no_go_note_2026-05-17"),
]


def tarjan_nontrivial_sccs(nodes, edges):
    adj = {c: [] for c in nodes}
    for e in edges:
        if e["from"] in adj and e["to"] in nodes:
            adj[e["from"]].append(e["to"])
    index, low, onstack, stack, idx, out = {}, {}, {}, [], [0], []

    def sc(v0):
        work = [(v0, 0)]
        while work:
            node, pi = work[-1]
            if pi == 0:
                index[node] = idx[0]; low[node] = idx[0]; idx[0] += 1
                stack.append(node); onstack[node] = True
            recurse = False
            ch = adj[node]
            for i in range(pi, len(ch)):
                w = ch[i]
                if w not in index:
                    work[-1] = (node, i + 1); work.append((w, 0)); recurse = True; break
                elif onstack.get(w):
                    low[node] = min(low[node], index[w])
            if recurse:
                continue
            if low[node] == index[node]:
                comp = []
                while True:
                    w = stack.pop(); onstack[w] = False; comp.append(w)
                    if w == node:
                        break
                if len(comp) > 1:
                    out.append(comp)
            work.pop()
            if work:
                p = work[-1][0]; low[p] = min(low[p], low[node])

    for v in nodes:
        if v not in index:
            sc(v)
    return out


def main() -> int:
    g = json.loads(GRAPH.read_text(encoding="utf-8"))
    nodes = g["nodes"]
    edges = g["edges"]
    eset = {(e["from"], e["to"]) for e in edges}

    checks = []

    sccs = tarjan_nontrivial_sccs(nodes, edges)
    checks.append(("graph is a DAG (zero non-trivial dependency cycles)", len(sccs) == 0,
                   f"non-trivial SCC sizes={sorted((len(s) for s in sccs), reverse=True)}"))

    for fr, to in DEMOTED_EDGES:
        checks.append((f"spurious pointer edge ABSENT: {fr[:34]}.. -> {to[:34]}..",
                       (fr, to) not in eset, ""))

    for fr, to in PRESERVED_EDGES:
        checks.append((f"real synthesis dep PRESENT: {fr[:30]}.. -> {to[:34]}..",
                       (fr, to) in eset, ""))

    # The gate must still be a cited node (cut removed only back-edges, not the node).
    checks.append(("gate node still present in graph", GATE in nodes, ""))

    npass = sum(1 for _, ok, _ in checks if ok)
    nfail = len(checks) - npass
    for desc, ok, detail in checks:
        tag = "PASS" if ok else "FAIL"
        print(f"{tag}: {desc}" + (f"  [{detail}]" if detail and not ok else ""))
    print(f"\nTOTAL: PASS={npass} FAIL={nfail}")
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
