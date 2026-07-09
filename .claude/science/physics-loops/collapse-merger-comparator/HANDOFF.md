# collapse-merger-comparator — campaign handoff (CLOSED 2026-07-09)

## PRs, in review order

1. **#5083** block01 — coupled toy engine, ENGINE-VALID. Includes the
   2026-07-09 Poisson deposition fix (bare product exceeded one on
   bunched states; identical in the validated regime; digests + cache
   refreshed; note changelog documents it).
   Verify: `python3 scripts/collapse_merger_toy_engine_2026_07_08.py`
   (exit 0; diff against
   `logs/runner-cache/collapse_merger_toy_engine_2026_07_08.txt`).
2. **#5084** block02 — frozen-star anatomy, FROZEN-STAR-EXHIBITED.
   Verify: `python3 scripts/collapse_frozen_star_2026_07_08.py`
   (exit 0; diff against its cache).
3. **#5086** block03 — merger by bridging, MERGER-BY-BRIDGING; campaign
   close folded into this branch.
   Verify: `python3 scripts/merger_bridging_2026_07_08.py`
   (exit 0; diff against its cache).

## One-paragraph result

One coupled comparator now runs gravity's whole loop and reproduces the
named extreme-regime correspondences: matter falls toward crowding
(8-sigma, sub-sigma null); a dense blob collapses into a frozen star
(record husk + bound energy shell + frozen boundary clocks) whose
self-formed structure demonstrably gravitates (9.5-sigma probe);
capacity caps the core (no singularity); two stars merge exclusively by
bridging — husks never move, exactly — with an exact never-decreasing
husk-mass law (the area-theorem analog) and a sparse permanent
record shell with a permanent clock offset in the far field (the
memory-like imprint). The saturation endgame (heat death) appears when
the deposition budget exceeds the star-with-exterior regime, exactly as
the season synthesis predicted.

## Findings that corrected prior prose

- Record-mediated gravity has no pre-nucleation contraction channel
  (a fresh blob diffuses first; the Jeans analog is post-nucleation
  self-binding).
- In d = 1, occupancy/concentration statistics cannot separate gravity
  from self-caging at matched kappa; a deposition-frozen probe phase
  isolates the pull (documented so later blocks don't rediscover it).
- Ossification decelerates only in the supply-starved regime; the
  capture-fed regime ACCELERATES (alpha ~ 1.5). The merger thought-pass
  sentence "black holes ossify with age, slowing" is regime-dependent.
- Husk identity over time must be tracked by containment continuity
  (exact, from record permanence); per-snapshot largest-component
  selection aliases.

## Deliberately not done

The fall bias, parcel model, and kappa remain declared comparator
couplings — no derivation claimed. The "radiated burst" memory leg did
not occur natively at this kappa (the imprint is leakage-laid); a
burst-driven leg would need a new declared device and is banked, not
commissioned. d >= 2 lifts banked.

## Weaving proposals (for review lane, not applied)

- The season synthesis (#5081) could cite #5084/#5086 as the
  extreme-regime exhibits of its derived chain.
- The frozen-star note's two-regime ossification law could be cited
  wherever the "ossify with age" heuristic appears.
