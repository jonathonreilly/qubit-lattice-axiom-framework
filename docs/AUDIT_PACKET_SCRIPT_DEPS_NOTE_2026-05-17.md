# Audit Packet Script-Dependency Resolution

**Date:** 2026-05-17

**Claim type:** meta
**Status:** diagnostic + tool + recommendation; not a claim under audit. Read-only against the repo.

## Problem

A recurring pattern observed in recent audits: `audited_conditional class C` verdicts that fall back to "chain depends on a script not in the restricted packet." Concrete example today:

> `lattice_distance_law_note: audited_conditional, class C`
> Reason: the two runner caches now exist and support the bounded numerical fit, but the chain still depends on `scripts/lattice_mirror_distance.py`, which was not in the restricted packet.

**Root cause:** The audit packet currently contains the source note + primary runner + cache. But primary runners often **import** from helper modules in `scripts/*.py`. The auditor sees opaque function imports (`compute_field_at_b`, `generate_lattice_mirror`, `propagate`) and correctly cannot verify their contents — falling back to `class C` (not derivable from class-A inputs in the packet).

This is a **packet-completeness bug**, not a science bug. The chain may be sound; the auditor just doesn't see the helper's source.

## Verified case

`docs/LATTICE_DISTANCE_LAW_NOTE.md` references active runner `scripts/lattice_no_barrier_distance.py`, which begins with:

```python
from scripts.lattice_mirror_distance import compute_field_at_b, generate_lattice_mirror, propagate
```

If `scripts/lattice_mirror_distance.py` is not in the packet, the auditor has no way to verify what `generate_lattice_mirror` or `propagate` actually compute. The class-C verdict is the only honest response.

## Tool

`scripts/audit_packet_script_deps.py` (this PR) — read-only diagnostic that:

1. Iterates every claim in `docs/audit/data/audit_ledger.json`
2. For each claim with a declared `runner_path`, parses the runner's Python AST
3. Extracts `from scripts.X import ...` / `import scripts.X` statements (including relative imports inside `scripts/`)
4. Walks the transitive closure
5. Writes `docs/audit/data/audit_packet_script_deps.json` mapping each `claim_id → {primary_runner, helper_runners[]}`

The JSON is the actionable artifact for the audit orchestrator.

## Snapshot today (2026-05-17)

| metric | value |
|---|---:|
| Total claims in ledger | 2142 |
| Claims with declared runner_path | 1879 |
| Claims with no runner declared | 258 |
| Claims whose runner file is missing | 5 |
| Pending audits (queue) | 1212 |
| **Pending claims with helper imports (would trigger class-C from packet incompleteness)** | **74 / 1082** |
| Ledger claims overall with helper imports | 212 / 1879 |

The 138 already-audited claims with helpers may have been mis-classified as class C in the past from the same bug — those could be candidates for re-audit once packets are complete.

## Top imported helper scripts

| count | helper |
|---:|---|
| 40 | `scripts/minimal_source_driven_field_probe.py` |
| 27 | `scripts/numpy_replay_bootstrap.py` |
| 23 | `scripts/generative_causal_dag_interference.py` |
| 19 | `scripts/two_body_momentum_harness.py` |
| 14 | `scripts/gate_b_grown_joint_package.py` |
| 14 | `scripts/causal_field_gravity.py` |
| 12 | `scripts/topology_families.py` |
| 11 | `scripts/gap_topological_asymmetry.py` |
| 11 | `scripts/combined_gravity_scaling.py` |
| 11 | `scripts/signed_gravity_aps_boundary_index_probe.py` |

## Recommendation for the audit orchestrator

When assembling the audit packet for `claim_id X`:

1. Include the source note (`docs/X.md`)
2. Include the primary runner (`scripts/<primary>.py`)
3. Include the runner cache (`logs/runner-cache/<primary>.txt`)
4. **NEW: Include all transitive helper scripts named in `docs/audit/data/audit_packet_script_deps.json[X]["helper_runners"]`**

Step 4 is the missing piece. The JSON output of this tool is the authoritative source for which helpers each packet needs.

## Expected impact

- Immediate: 74 pending audits no longer subject to spurious class-C verdicts from packet incompleteness alone. They'll get whatever class their chain actually warrants.
- Retrospective: 138 already-audited claims with helpers could be considered for re-audit if their current class-C verdict was driven by the same bug.

The fix is **mechanical** (just include more files in the packet). No science changes needed.

## What this note does NOT establish

- A new positive theorem or retirement of any claim
- A change to the audit pipeline scripts (the fix lives in whatever external orchestrator assembles packets)
- A claim about which of the 74 pending class-C-vulnerable audits are actually sound (each must still be re-audited with the complete packet)

## Re-running

After audit ledger updates, regenerate the dep map:

```bash
python3 scripts/audit_packet_script_deps.py
# Updates docs/audit/data/audit_packet_script_deps.json
```

## Cross-references (non-load-bearing)

- `docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md` (auditor's prompt + packet structure)
- `docs/audit/RUNNER_CACHE_POLICY.md` (cache + runner-source semantics)
- `docs/audit/scripts/run_pipeline.sh` (audit pipeline; audits themselves are external Codex calls)
- [PR #1277](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1277) (audit landscape diagnostic — earlier in this session)
