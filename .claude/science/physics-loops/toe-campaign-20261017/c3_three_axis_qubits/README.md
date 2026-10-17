# C3 working files: three axis-labelled qubits per site

- `enum3q.py ACTION`: C4/C3-fixed star strings commuting with all rotated translates
  (soldered `full`: 719 strings; unsoldered `trivial`: 9327).
- `analyze3q.py`: sign-consistent orbits, compatibility, single-site TQO candidates
  and Ext^3 tests (`an3q_full.log`). Single-site trivial commutant is necessary
  but not sufficient for bounded code dimension: the soldered single-orbit hits
  with 3D-mobile charges (e.g. orbit 125) have log2 code dimension L^3 + 16.
- `cliques3q.py`, `torus3q.py`, `ext3q.py`, `ext_big.log`: maximal sets, their
  torus code dimensions and Ext^3.
- `tc8_torus.py`, `t_tc8.sing`: the unsoldered interleaved toric codes (log2 = 24
  at L = 4, 6; charge module supported at (1,1,1)).
- `tqo_search.py`: the two-qubit version of the candidate search.
- An earlier C2-element (order 2) restriction ran out of memory (10^9
  strings under the trivial action) and was replaced by the C4/C3 restriction.
- Canonical runner:
  `scripts/three_axis_qubit_site_stabilizer_rules_soldering_and_three_dimensional_charge_mobility_2026_10_17.py`
  (PASS=10 with Singular).
