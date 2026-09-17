# GOAL — block 32: the minimal marked tree — is block 30's constant a property of the construction or of the counted family? (2026-09-17)

**Directive.** Owner 2026-09-17 (morning): "pick up the next in the queue and get going." The queue's item after block 31 (PR #8175): a differently built explanation tree, judged on the witnesses W1–W3 — would the family admit a constant below 2, and how far below? Lens pass on the item: every construction produces, at each realization, some tree of the counted family; the best any construction can do there is the cheapest tree of the family. So the right object is the family-level quantity `c*(η, x) = min over trees of (E − 3(|S| − 1))/|A|` and its supremum over realizations, not another construction.

**Exact target (claim type `bounded_theorem`).**
- T1 (the reduction): the component lemma; when the component of the root holds one seed, the trees of the family are exactly the closed node sets and the minimum of `E − 3(|S| − 1) − c|A|` is an exact level dynamic program; cross-checked against a brute-force enumeration of the full family (forks included).
- T2 (the family's constant from below): explicit realizations on which every tree of the family has `E ≥ 3(|S| − 1) + |A|`, with exact certificates; hence `c* ≥ 1` for every construction.
- T3 (block 31's witnesses): the family's values there (are they below 1?).
- T4 (the stake and the floor): what `c = 1` would give (block 31's certificates), and the floor of the tree route from `c ≥ 1`.
- Executed, not claimed: hill-climbs on `c*` to look for `c* > 1`.

**Seat plan (supervisor-run, no subagents).** Controls: an integer program over the family (`supervisor_control_block32_mintree.py`), a general level dynamic program with partition states (`..._treedp.py`), the single-seed program (`..._ssdp.py`), brute-force cross-checks (`..._crosscheck.py`), climbs (`..._climb.py`, `..._climb_seeded.py`). Contract with a self-run lens pass; primary; refuting pass with disjoint machinery (`..._refuter.py`); fold; mutation census; gates; independent PR against `main`.

**Stop conditions.** Exact certificates for the lower bound, or a recorded obstacle. Never merge; layman update at the milestone.
