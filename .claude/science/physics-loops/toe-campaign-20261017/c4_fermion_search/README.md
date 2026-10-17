# C4 working files: fermion search in symmetric three-axis-qubit rules

- `soldered_symmetric_survivors.npy`: the 34927 soldered star strings fixed by
  some nontrivial rotation that commute with all rotated translates.
  - The axis-C2 part came from `enum3q_c2.py full axis` (about 36 min,
    `c2axis_full.log`), the edge-C2 part from `enum3q_c2.py full edge`, and
    the C4/C3 part from the C3 enumeration.
- `outsider_cliques.py`: the 60 non-alphabet orbits and the ten maximal sets
  containing them.
- `sample_cliques.py`: random greedy maximal sets. Most land in the 4259-orbit
  alphabet family; this was superseded by the exact outsider analysis.
- `eval_cliques.py`, `evalcl_trivial.log`: the unsoldered survey, with
  validity (phase-tracked torus relations) and code dimensions for the 1224
  maximal sets of at most 70 orbits. The nine 383-orbit sets are abelian
  self-commutant alphabets.
- `stats.py`, `stats_min.py`, `stats_min_out.txt`: the T-junction tool and the
  statistics of the 36 bounded unsoldered rules, each reduced to a minimal
  generating set of orbits.
  - A first pass returned no mobile charges, because redundant product
    generators make single-generator violations inconsistent. Testing all
    same-site patterns fixed this.
- `unsoldered_bounded_rules.json`: the 36 rules as orbit string lists.
- Canonical runner:
  `scripts/three_axis_qubit_symmetric_stabilizer_rules_fermion_search_2026_10_17.py`
  (PASS=8; --full adds the axis-C2 enumeration).
