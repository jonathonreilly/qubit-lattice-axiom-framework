# Three-Family Card Missing-Distance Live Bridge

**Date:** 2026-06-18
**Claim type:** bounded_theorem (source-side partial bridge only; not full
card repair)
**Actual current-surface status:** source-side partial re-audit bridge;
independent audit owns any verdict or effective-status propagation.
**Target row:** `three_family_card_note`
**Primary runner:**
`scripts/three_family_card_missing_distance_live_bridge_2026_06_18.py`

## Result

The archived `THREE_FAMILY_CARD_NOTE.md` failed correctly as a 9/9
three-family equality / geometry-independence claim. Its table left Family 3
distance alpha as `(not yet)` and no runner recomputed every listed property
for all three families.

This bridge is narrower. It packages only the live source-side evidence for the
specific missing Family 3 distance-alpha slot:

- [`DISTANCE_LAW_PRESERVING_THIRD_FAMILY_NOTE.md`](DISTANCE_LAW_PRESERVING_THIRD_FAMILY_NOTE.md)
- [`scripts/DISTANCE_LAW_PRESERVING_THIRD_FAMILY.py`](../scripts/DISTANCE_LAW_PRESERVING_THIRD_FAMILY.py)
- [`logs/runner-cache/DISTANCE_LAW_PRESERVING_THIRD_FAMILY.txt`](../logs/runner-cache/DISTANCE_LAW_PRESERVING_THIRD_FAMILY.txt)
- archive firewall:
  [`scripts/family_card_archive_firewall_2026_06_16.py`](../scripts/family_card_archive_firewall_2026_06_16.py)

The live runner builds the high-drift/high-restore third grown family
`drift=0.50`, `restore=0.90`, sweeps seeds `0..5`, checks exact zero-source
and neutral controls, verifies sign orientation and weak charge scaling, and
fits the distance tail at `b = 5, 6, 7, 8, 10`.

## Safe Re-Audit Scope

The live result supports only:

- third family `drift=0.50`, `restore=0.90`;
- exact zero-source baseline;
- exact neutral `+1/-1` cancellation;
- `+1`/`-1` sign orientation;
- weak charge scaling exponent near `1`;
- Family 3 direct distance tail `alpha = -1.150`, `R^2 = 0.971`, `5/5`
  toward.

The primary cache reports:

```text
sign gate: PASS
tail gate: PASS
alpha = -1.150
r2 = 0.971
toward = 5/5
```

## Boundary

This bridge does not edit audit results, restore the archived card as evidence,
or claim:

- all-nine-property recomputation;
- three-family equality;
- geometry independence;
- a holdout-family check;
- Family 1/2 recomputation in the same runner;
- universal grown-family portability;
- retained or retained-bounded effective status.

The correct source-side reading is:

> the old archived card remains failed historical evidence, while the live
> third-family distance runner closes the missing Family 3 distance-alpha slot
> as a bounded partial bridge. Full card repair still requires a single
> all-nine-property runner over all three families plus a holdout check.

## Verification

Run:

```bash
python3 scripts/family_card_archive_firewall_2026_06_16.py
python3 scripts/three_family_card_missing_distance_live_bridge_2026_06_18.py
```

The distance runner is cached because it is a heavy sweep with
`AUDIT_TIMEOUT_SEC = 1800`. To refresh the source cache, run:

```bash
python3 scripts/DISTANCE_LAW_PRESERVING_THIRD_FAMILY.py
```

Expected bridge result:

```text
SUMMARY: THREE FAMILY CARD MISSING DISTANCE LIVE BRIDGE PASS=51 FAIL=0
```
