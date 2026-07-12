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

## Block 02 (2026-07-12, supervisor-executed)

Parent consumption wiring: the parent note's Role paragraph, Boundaries item,
and Dependencies now consume the block-01 derivation (markdown link = edge;
acyclic — upstream note backticks the parent); dated Repair Note quotes the
archived-verdict blocker. Parent runner +4 wiring pins (PASS 9->13); cache
regenerated; vocab lint clean. Stacked on block 01 (uses its note file).
Proposed weaving beyond this: none (publication surfaces untouched per skill).

## Block 03 — Covariant-subdomain completeness classification

**Date:** 2026-07-12  
**Claim type:** bounded_theorem  
**Actual current-surface status:** exact-support  
**Trace class:** upstream_support  
**Reachability to the parent row:** supports  
**Independent audit:** pending

### What landed

- `docs/PER_PLAQUETTE_LICENSE_COVARIANT_SUBDOMAIN_CLASSIFICATION_NOTE_2026-07-12.md`
  proves completeness of the endpoint-containing covariant one-step domain
  lattice and states the enumerated-domain interval theorem.
- `scripts/per_plaquette_license_covariant_subdomain_classification_2026_07_12.py`
  constructs `G_l`, checks its group action, exhausts all 1024 candidate
  subsets, recomputes the five-row loop table, and pins the note surface.
- `logs/runner-cache/per_plaquette_license_covariant_subdomain_classification_2026_07_12.txt`
  is the generated deterministic cache.
- `STATE.yaml`, `CLAIM_STATUS_CERTIFICATE.md`, and this handoff record the
  block-03 exact-support boundary and upstream-support trace.

Blocks 01 and 02, the downstream parent, and all ledger/authority surfaces are
unchanged in block 03.

### Exact result

- The proper-rotation stabilizer of `{0,e1}` has order 8, is closed under all
  64 ordered products, fixes the undirected endpoint set, and splits into four
  endpoint-preserving and four endpoint-swapping elements.
- Its `C_1` orbits have sizes `2/2/8`: endpoints `E`, axial exterior `A`, and
  transverse `T`. The ten non-endpoint sites have exactly the two orbits `A`
  and `T`.
- Exhaustive filtering of all `2^10 = 1024` non-endpoint subsets leaves
  exactly `E`, `E∪A`, `E∪T`, and `C_1`, with sizes `2/4/10/12`.

| domain | length 4 | length 6 | one-tick |
| --- | ---: | ---: | :---: |
| `E` | 0/24 | 0/264 | yes |
| `E∪A` | 0/24 | 0/264 | yes |
| `E∪T` | 24/24 | 0/264 | yes |
| `C_1` | 24/24 | 0/264 | yes |
| radius-2 | 24/24 | 264/264 | NO |

The previously unchecked `E∪A` row is therefore empty at both lengths. The
cubic Manhattan radius-2 link domain has 38 sites, not the provisional 32:
its two 25-site endpoint balls have a 12-site intersection. The named point
`-2e1=(-2,0,0)` is outside `C_1` and matches the block-01 radius-2
source/target violation class.

### Status firewall and stop point

This exact support classifies covariant domains and the enumerated lengths 4
and 6 only. It does not retire `(P-FUND-1TICK)`, prove a fundamental
per-plaquette action, touch `theta_bare`, or change an axiom/primitive. It is
upstream support toward the bounded parent row, not direct blocker closure.

Verification at the block checkpoint:

```text
new runner: TOTAL: PASS=39 FAIL=0 (exit 0)
cache: ok=1, nonzero_exit=0, timeout=0, error=0, missing=0
block-01 runner: TOTAL: PASS=51 FAIL=0 (exit 0)
parent runner: SUMMARY: PASS=13 FAIL=0 (exit 0)
```

Stop after the requested final verification. Do not commit, push, open a PR,
or weave this support into the parent in block 03.
