# C12: Majorana-per-direction (generalized superfast encoding type) cubic fermion code

- Three qubits per site carry six Majoranas, one per direction. Runner:
  scripts/majorana_per_direction_cubic_fermion_code_full_rotation_covariance_2026_10_17.py (PASS=7).
- The code is O-covariant, with one fermion species, under on-site signed-Majorana-permutation Cliffords.
  Any admissible sign choice works, and 128 generator choices give a consistent group action (order 48,
  containing -1).
- Bug note: the first `gse.py` had gamma_0 = i X1, which is anti-Hermitian. The O-covariance checks
  survived that bug, but the pair tests (`gse_pair*.py`, `gse_conj.py`) did not, and the pair-test logs
  from before the fix are void. Fixed in `gse.py` and in the runner.
- Pair test after the fix (`gse_conj.py`, L = 8):
  - all three axis C2 give lambda = +1;
  - edge C2 results disagree between conjugate elements, probably because the separation is half the
    torus. An L = 12 rerun is in progress (`gse_conj_L12.log`).
- The fractionalization class is not yet claimed.
