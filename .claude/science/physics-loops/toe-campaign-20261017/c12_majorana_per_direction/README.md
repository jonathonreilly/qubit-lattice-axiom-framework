# C12: Majorana-per-direction (generalized superfast encoding type) cubic fermion code

- Three qubits per site carry six Majoranas, one per direction. Runner:
  scripts/majorana_per_direction_cubic_fermion_code_full_rotation_covariance_2026_10_17.py (PASS=7).
- The code is O-covariant, with one fermion species, under on-site signed-Majorana-permutation Cliffords.
  Any admissible sign choice works, and 128 generator choices give a consistent group action (order 48,
  containing -1).
- Bug note: the first `gse.py` had gamma_0 = i X1, which is anti-Hermitian. The O-covariance checks
  survived that bug, but the pair tests (`gse_pair*.py`, `gse_conj.py`) did not, and the pair-test logs
  from before the fix are void. Fixed in `gse.py` and in the runner.
- Second bug: `map_pauli` used +k instead of -k when inverting gamma_sub = i^k X^x Z^z. The map was still a
  homomorphism but implemented the wrong automorphism. `maptest.py` now checks the gamma images.
- After both fixes, `gse_conj2.py` (L = 8, the two uniform sectors, two consistent group choices) gives
  lambda = +1 for every axis C2 and -1 for every edge C2, consistent across conjugates and positions.
  This solver allowed excitations within distance 1 of the endpoints.
- The independent check used strictly clean pair creators and found lambda = -1 for both types
  (eta_f = +1, +1). It also showed that a flux-dressed creator gives +1 for the axis C2. `gse_conj3.py`
  reruns with clean creators (L = 10).
- The fractionalization class is not yet claimed.
