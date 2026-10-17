# C1 working files: one-qubit cubic-covariant nearest-neighbour stabilizer rules

- `classify.py`: single-orbit enumeration under the four soldering actions
  (writes `single_orbits.json`; about 15 s).
- `cliques.py`: maximal commuting unions of orbits (`cliques_*.json`; needs
  networkx; the runner has its own Bron–Kerbosch).
- `chamon_mob.sing` and `chamon_mob.out`: a Singular cross-check of the Chamon
  charge ideal over GF(2). It covers saturation, the four minimal primes (no
  embedded component), (I : m1) = I, and mobility along sample translations.
  - The first attempt used `sat(...)[1]`. In this Singular build `sat`
    returns an ideal, so that picked a single generator and gave a wrong
    "dim 2" result; it was caught and fixed before any use.
- `chamon_torus.py`: code dimension and relation signs on L^3 tori (galois).
- The canonical runner is
  `scripts/cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17.py`
  (PASS=20).
