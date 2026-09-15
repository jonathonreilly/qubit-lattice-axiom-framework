# Frozen backlog topology and recovery routing

Main snapshot: `5deabeb698a27c2c3f68c5df685af2521ef15307`. Inventory: `2026-09-15T10:07:30.189345+00:00`. 116 non-draft heads analyzed. The 11 drafts stay outside these proposed units. This is mechanical topology, not scientific review, source coverage or PASS.

The owner’s new open-PR scope replaces the historical 254-PR cutoff. Read current-main coherent-unit contract and origin/ai/execution AGENTS.md. No source edits, checkout changes, GitHub mutations, scientific reviews or worker launches performed. Missing PR objects fetched into refs/topology/prN.

## Findings

- Frozen declared-parent ancestry agrees throughout 8038→8040–8083. The deepest head 8083 inherits 26 open heads and changes 2,185 paths against its main merge base. Do not use this whole tower as a review packet.
- Declared 8013→8016 and 8014→8015 are not exact frozen-head ancestry. Their notes/runners survive by path; blob-level inherited mapping below determines unchanged versus revised bodies. Neither parent can be closed through ancestry alone.
- Every raw original and exact current-main tree delta is retained with old/new blob IDs, including deletions. A direct main→stale-head delta includes unrelated current-main deletions: never transplant that stale tree. Build a current-main candidate from reviewed surviving source.
- Proposed small groups follow actual note/runner path packages and ancestry. They remain routing hypotheses: scientific coherence, imported inputs and semantic dependencies must be established by complete source reads. Singleton packets may still require large transitive closures.

## Early inheritance discrepancy

### #8015 versus declared parent #8014
- `docs/NATIVE_EDGE_RECORD_Z4_FLUX_BRIDGE_CAPACITY_BOUNDED_THEOREM_NOTE_2026-09-07.md`: identical
- `scripts/audit_packet_script_deps.py`: identical
- `scripts/native_edge_record_z4_flux_five_event_check_2026_09_07.py`: identical
- `scripts/native_edge_record_z4_flux_single_bridge_check_2026_09_07.py`: identical

### #8016 versus declared parent #8013
- `docs/GAUGE_WILSON_CUBE_SLAB_WEAK_COUPLING_WINDOW_BOUNDED_THEOREM_NOTE_2026-09-07.md`: identical
- `scripts/gauge_wilson_cube_slab_weak_coupling_window_check_2026_09_07.py`: identical

## Proposed bounded units

Each row is distinct; do not concurrently review constituents in another unit. External parents require bottom-up landing or explicit frozen dependency closure.

| Unit PRs | External declared parents | Incremental source-path count |
|---|---|---|
| 8010 |  | 6 |
| 8011 |  | 2 |
| 8012 |  | 2 |
| 8013, 8016 |  | 6 |
| 8014, 8015 |  | 6 |
| 8017, 8018 | 8016 | 6 |
| 8019 | 8017 | 3 |
| 8020, 8021, 8022 | 8016 | 9 |
| 8034, 8035 |  | 4 |
| 8036 |  | 9 |
| 8037 |  | 7 |
| 8038 |  | 6 |
| 8039 |  | 2 |
| 8040, 8041 | 8038 | 13 |
| 8042, 8043 | 8038 | 15 |
| 8044 | 8038 | 10 |
| 8045, 8046 | 8044 | 10 |
| 8047 | 8044 | 11 |
| 8048 | 8044 | 13 |
| 8050 | 8044 | 4 |
| 8049, 8051 | 8038 | 9 |
| 8052, 8053, 8058 | 8049 | 33 |
| 8054, 8055 | 8051 | 9 |
| 8056, 8057 | 8055 | 9 |
| 8059, 8061 | 8057 | 50 |
| 8060, 8062, 8063 | 8057 | 12 |
| 8064 | 8063 | 4 |
| 8065 | 8038 | 5 |
| 8066, 8067, 8068 | 8063 | 19 |
| 8069, 8070 | 8068 | 27 |
| 8071, 8072 | 8070 | 29 |
| 8073, 8074 | 8072 | 4 |
| 8075, 8076 | 8074 | 4 |
| 8077 | 8076 | 2 |
| 8078, 8079, 8080 | 8076 | 6 |
| 8081, 8082, 8083 | 8080 | 6 |
| 8084 |  | 4 |
| 8085 |  | 5 |
| 8086 |  | 9 |
| 8087 |  | 5 |
| 8088 |  | 4 |
| 8089 |  | 2 |
| 8090 |  | 3 |
| 8091 |  | 3 |
| 8092 |  | 3 |
| 8093 |  | 1 |
| 8094 |  | 3 |
| 8095 |  | 2 |
| 8096 |  | 2 |
| 8097 |  | 2 |
| 8098 |  | 2 |
| 8099 |  | 2 |
| 8100 |  | 2 |
| 8101 |  | 2 |
| 8102 |  | 2 |
| 8103 |  | 2 |
| 8104 |  | 2 |
| 8105 |  | 2 |
| 8106 |  | 2 |
| 8107 |  | 2 |
| 8108 |  | 2 |
| 8109 |  | 2 |
| 8110 |  | 2 |
| 8111 |  | 2 |
| 8112 |  | 2 |
| 8113 |  | 2 |
| 8114 |  | 2 |
| 8115 |  | 2 |
| 8116 |  | 2 |
| 8117 |  | 2 |
| 8118 |  | 2 |
| 8119 |  | 2 |
| 8122 |  | 2 |
| 8123 |  | 2 |
| 8124 |  | 2 |
| 8125 |  | 2 |
| 8126 |  | 2 |
| 8127 |  | 6 |
| 8128 |  | 2 |
| 8129 |  | 2 |
| 8130 |  | 4 |
| 8131 |  | 2 |
| 8132 |  | 2 |
| 8135 |  | 2 |
| 8136 |  | 2 |
| 8120, 8121 |  | 4 |
| 8133, 8134 |  | 12 |

## Independent starter routing

Early standalone starters: 8010, 8011, 8012, 8036, 8037, 8039; base packages 8013+8016, 8014+8015, 8034+8035 and 8038 need complete inherited accounting. Root ancestry alone does not certify independent science.
Contemporary small initial candidates: 8102, 8105, 8107, 8110, 8114, 8122, 8123, 8124, 8125, 8126, 8128, 8129, 8130, 8131, 8132. Each is main-based with no frozen open-head ancestor; their incremental source paths are disjoint from one another under the declared classification. Semantic/input cross-dependencies still need inspection.
Avoid choosing 8093 merely because it changes one path: the source filename is an axiom-sufficiency campaign note, so premise/governance closure may dominate.

## All-PR current-main preservation check

Counts below inspect every original changed path against exact main blobs; they are not claims that content landed.

| PR | Actual immediate ancestors | Original paths identical on main | Original paths absent on main | Original paths different | Current-main-only source paths missing from head |
|---|---|---|---|---|---|
| 8010 | [] | 0 | 82 | 3 | 735 |
| 8011 | [] | 0 | 57 | 1 | 735 |
| 8012 | [] | 0 | 54 | 1 | 735 |
| 8013 | [] | 0 | 54 | 1 | 735 |
| 8014 | [] | 0 | 62 | 3 | 735 |
| 8015 | [] | 0 | 114 | 3 | 735 |
| 8016 | [] | 0 | 138 | 1 | 735 |
| 8017 | [8016] | 0 | 200 | 1 | 735 |
| 8018 | [8017] | 0 | 300 | 3 | 735 |
| 8019 | [8017] | 0 | 266 | 1 | 735 |
| 8020 | [8016] | 0 | 212 | 1 | 735 |
| 8021 | [8020] | 0 | 263 | 1 | 735 |
| 8022 | [8021] | 0 | 333 | 1 | 735 |
| 8034 | [] | 0 | 17 | 6 | 0 |
| 8035 | [8034] | 0 | 25 | 6 | 0 |
| 8036 | [] | 0 | 11 | 1 | 605 |
| 8037 | [] | 0 | 47 | 1 | 545 |
| 8038 | [] | 0 | 81 | 1 | 545 |
| 8039 | [] | 0 | 46 | 1 | 545 |
| 8040 | [8038] | 0 | 154 | 1 | 545 |
| 8041 | [8040] | 0 | 228 | 1 | 545 |
| 8042 | [8038] | 0 | 158 | 1 | 545 |
| 8043 | [8042] | 0 | 248 | 1 | 545 |
| 8044 | [8038] | 0 | 352 | 1 | 545 |
| 8045 | [8044] | 0 | 457 | 1 | 545 |
| 8046 | [8045] | 0 | 539 | 1 | 545 |
| 8047 | [8044] | 0 | 443 | 1 | 545 |
| 8048 | [8044] | 0 | 482 | 1 | 545 |
| 8049 | [8038] | 0 | 150 | 1 | 545 |
| 8050 | [8044] | 0 | 408 | 1 | 545 |
| 8051 | [8049] | 0 | 216 | 1 | 545 |
| 8052 | [8049] | 0 | 224 | 1 | 545 |
| 8053 | [8052] | 0 | 480 | 1 | 545 |
| 8054 | [8051] | 0 | 308 | 1 | 545 |
| 8055 | [8054] | 0 | 378 | 1 | 545 |
| 8056 | [8055] | 0 | 543 | 1 | 545 |
| 8057 | [8056] | 0 | 653 | 1 | 545 |
| 8058 | [8053] | 0 | 578 | 1 | 545 |
| 8059 | [8057] | 0 | 1344 | 1 | 545 |
| 8060 | [8057] | 0 | 722 | 1 | 545 |
| 8061 | [8059] | 0 | 1465 | 1 | 545 |
| 8062 | [8060] | 0 | 769 | 1 | 545 |
| 8063 | [8062] | 0 | 809 | 1 | 545 |
| 8064 | [8063] | 0 | 848 | 1 | 545 |
| 8065 | [8038] | 0 | 165 | 1 | 545 |
| 8066 | [8063] | 0 | 942 | 1 | 545 |
| 8067 | [8066] | 0 | 1019 | 1 | 545 |
| 8068 | [8067] | 0 | 1088 | 1 | 545 |
| 8069 | [8068] | 0 | 1252 | 1 | 545 |
| 8070 | [8069] | 0 | 1304 | 1 | 545 |
| 8071 | [8070] | 0 | 1347 | 1 | 545 |
| 8072 | [8071] | 0 | 1402 | 1 | 545 |
| 8073 | [8072] | 0 | 1483 | 1 | 545 |
| 8074 | [8073] | 0 | 1592 | 1 | 545 |
| 8075 | [8074] | 0 | 1680 | 1 | 545 |
| 8076 | [8075] | 0 | 1737 | 1 | 545 |
| 8077 | [8076] | 0 | 1813 | 1 | 545 |
| 8078 | [8076] | 0 | 1782 | 1 | 545 |
| 8079 | [8078] | 0 | 1854 | 1 | 545 |
| 8080 | [8079] | 0 | 1932 | 1 | 545 |
| 8081 | [8080] | 0 | 2009 | 1 | 545 |
| 8082 | [8081] | 0 | 2091 | 1 | 545 |
| 8083 | [8082] | 0 | 2184 | 1 | 545 |
| 8084 | [] | 0 | 32 | 1 | 0 |
| 8085 | [] | 0 | 34 | 1 | 0 |
| 8086 | [] | 0 | 125 | 1 | 0 |
| 8087 | [] | 0 | 46 | 1 | 0 |
| 8088 | [] | 0 | 140 | 1 | 0 |
| 8089 | [] | 0 | 93 | 1 | 0 |
| 8090 | [] | 0 | 20 | 1 | 0 |
| 8091 | [] | 0 | 108 | 1 | 0 |
| 8092 | [] | 0 | 100 | 1 | 0 |
| 8093 | [] | 0 | 1 | 0 | 0 |
| 8094 | [] | 0 | 152 | 1 | 0 |
| 8095 | [] | 0 | 175 | 1 | 0 |
| 8096 | [] | 0 | 13 | 1 | 0 |
| 8097 | [] | 0 | 183 | 1 | 0 |
| 8098 | [] | 0 | 183 | 1 | 0 |
| 8099 | [] | 0 | 138 | 1 | 0 |
| 8100 | [] | 0 | 93 | 1 | 0 |
| 8101 | [] | 0 | 78 | 1 | 0 |
| 8102 | [] | 0 | 3 | 0 | 0 |
| 8103 | [] | 0 | 126 | 1 | 0 |
| 8104 | [] | 0 | 75 | 1 | 0 |
| 8105 | [] | 0 | 3 | 0 | 0 |
| 8106 | [] | 0 | 38 | 1 | 0 |
| 8107 | [] | 0 | 3 | 0 | 0 |
| 8108 | [] | 0 | 30 | 1 | 0 |
| 8109 | [] | 0 | 37 | 1 | 0 |
| 8110 | [] | 0 | 3 | 0 | 0 |
| 8111 | [] | 0 | 37 | 1 | 0 |
| 8112 | [] | 0 | 37 | 1 | 0 |
| 8113 | [] | 0 | 40 | 1 | 0 |
| 8114 | [] | 0 | 3 | 0 | 0 |
| 8115 | [] | 0 | 41 | 1 | 0 |
| 8116 | [] | 0 | 41 | 1 | 0 |
| 8117 | [] | 0 | 44 | 1 | 0 |
| 8118 | [] | 0 | 57 | 1 | 0 |
| 8119 | [] | 0 | 53 | 1 | 0 |
| 8120 | [] | 0 | 58 | 1 | 0 |
| 8121 | [8120] | 0 | 114 | 1 | 0 |
| 8122 | [] | 0 | 3 | 0 | 0 |
| 8123 | [] | 0 | 3 | 1 | 0 |
| 8124 | [] | 0 | 3 | 1 | 0 |
| 8125 | [] | 0 | 3 | 1 | 0 |
| 8126 | [] | 0 | 3 | 1 | 0 |
| 8127 | [] | 0 | 22 | 1 | 0 |
| 8128 | [] | 0 | 3 | 1 | 0 |
| 8129 | [] | 0 | 3 | 1 | 0 |
| 8130 | [] | 0 | 6 | 1 | 0 |
| 8131 | [] | 0 | 3 | 1 | 0 |
| 8132 | [] | 0 | 3 | 1 | 0 |
| 8133 | [] | 0 | 12 | 1 | 0 |
| 8134 | [8133] | 0 | 27 | 1 | 0 |
| 8135 | [] | 0 | 14 | 1 | 0 |
| 8136 | [] | 0 | 15 | 1 | 0 |

## Source overlap and recovery

`topology.json` contains every pairwise incremental source overlap and every path/blob inventory, plus the inventory recovery records unchanged. No recovery artifact is represented as reviewer coverage; inspect session identity, head and scope before reuse.
.claude, docs/audit and logs are excluded only from the routing overlap summary. Their full changed paths remain in the raw inventories and may contain load-bearing material.

- [8010, 8014]: `scripts/audit_packet_script_deps.py`
- [8010, 8015]: `scripts/audit_packet_script_deps.py`
- [8010, 8018]: `scripts/audit_packet_script_deps.py`
- [8013, 8016]: `docs/GAUGE_WILSON_CUBE_SLAB_WEAK_COUPLING_WINDOW_BOUNDED_THEOREM_NOTE_2026-09-07.md`, `scripts/gauge_wilson_cube_slab_weak_coupling_window_check_2026_09_07.py`
- [8014, 8015]: `docs/NATIVE_EDGE_RECORD_Z4_FLUX_BRIDGE_CAPACITY_BOUNDED_THEOREM_NOTE_2026-09-07.md`, `scripts/audit_packet_script_deps.py`, `scripts/native_edge_record_z4_flux_five_event_check_2026_09_07.py`, `scripts/native_edge_record_z4_flux_single_bridge_check_2026_09_07.py`
- [8014, 8018]: `scripts/audit_packet_script_deps.py`
- [8015, 8018]: `scripts/audit_packet_script_deps.py`

### Frozen recovery inventory

No findings files, scratch paths or unregistered review paths were reported in the frozen scan; this is not proof none exist elsewhere. Registered worktrees:

- `/Users/jonBridger/Documents/New Axioms Lets Go`: dirty_recovery, head `f9346ffb4352db14ad9cabdb8182af7864e8efbd`, matched open PRs []. Preserve any dirty/unpushed content; no review reuse asserted.
- `/private/tmp/review-drain-20260915/coordinator`: clean_checkout, head `5deabeb698a27c2c3f68c5df685af2521ef15307`, matched open PRs []. Preserve any dirty/unpushed content; no review reuse asserted.
