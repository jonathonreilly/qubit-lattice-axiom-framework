# Block-01 Handoff

**Date:** 2026-07-12  
**Claim type:** bounded_theorem  
**Actual current-surface status:** conditional-support  
**Independent audit:** pending

## What landed

- `docs/PER_PLAQUETTE_LICENSE_ONE_TICK_REACHABILITY_DERIVATION_NARROW_THEOREM_NOTE_2026-07-12.md`
  records exact Lemma A, conditional Lemma B, conditional Corollary C, the R4
  attempt, and the narrowly scoped covariant-lift route-pruning witness.
- `scripts/per_plaquette_license_one_tick_reachability_derivation_2026_07_12.py`
  implements Blocks A–E with explicit finite `R`, exact loop enumeration,
  link-stabilizer orbits, a one-tick locality falsifier, and note-surface pins.
- `logs/runner-cache/per_plaquette_license_one_tick_reachability_derivation_2026_07_12.txt`
  is the generated cache artifact. The runner reports `PASS=51 FAIL=0` and
  exits 0.
- `STATE.yaml` and `CLAIM_STATUS_CERTIFICATE.md` checkpoint the conditional
  outcome and the exact next trace action.

The parent note and all audit-ledger surfaces are unchanged in this block.

## R4 outcome

**Outcome:** registered premise.

**Decisive sentence:** The accepted sources supply spatial locality and a
joint carrier, but no update law makes each constituent-link availability a
function of tick-`t` data on that link's `C_1` set.

The Admissibility axiom supplies nearest-neighbor spatial dependence per site;
Record supplies a local lock; the bounded joint-presentation bridge supplies a
commuting multi-site carrier. None supplies a ticked update law or registers a
common multi-link availability at every constituent link. The light-cone
theorem constrains a rule only after `R`-locality is established. Accordingly,
`(P-FUND-1TICK)` is registered and remains load-bearing.

## Computed witness and consequences

- Lemma A: every tested link has the exact 12-site `C_1` set, matching the
  literal distance form for three orientations at three base points.
- Derived-form loop consequences: 24/24 length-4 plaquettes pass; 0/264
  length-6 loops pass; all 288 derived/literal predicate values agree.
- Route-pruning witness: the order-8 undirected-link stabilizer has orbit sizes
  endpoints/axial/transverse = 2/2/8. The strict endpoint-plus-transverse
  domain has size 10 rather than 12, passes 24/24 plaquettes, and passes 0/264
  length-6 loops.
- Locality falsifier: an explicit radius-2 dependency changes a target outside
  `C_1(source)` after one tick; three `C_1`-bounded Boolean update families
  satisfy confinement over 1,024 configuration pairs each.

## Proposed block-03 parent weaving

After independent audit of this block at its conditional scope, block 03 can
edit only the downstream parent
`docs/PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09.md`
to:

1. cite the new one-tick reachability note as the upstream supplier of the
   license conditional on `(P-FUND-1TICK)`;
2. replace the statement that the license is merely the bounded input with the
   precise conditional derivation status;
3. preserve the parent's finite length-4/length-6 domain and its boundary that
   no per-plaquette fundamental action is proved; and
4. keep the citation direction parent-to-upstream-note only, avoiding a cycle.

No block-03 weaving was performed here.

## Verification commands

```bash
python3 scripts/per_plaquette_license_one_tick_reachability_derivation_2026_07_12.py
python3 scripts/precompute_audit_runners.py --runners scripts/per_plaquette_license_one_tick_reachability_derivation_2026_07_12.py --force --allow-non-main --push-mode none
python3 scripts/frontier_per_plaquette_from_adjacency_license_2026_06_09.py | tail -3
git status --short
```

Expected block-01 runner tail:

```text
Block C witness counts: group=8, orbits=2/2/8, domain=10/12, plaquettes=24/24, length6=0/264
TOTAL: PASS=51 FAIL=0
```

## Stop point

Stop after the requested verification. Do not commit, push, open a PR, edit the
parent note, or write under `docs/audit/` in block 01.
