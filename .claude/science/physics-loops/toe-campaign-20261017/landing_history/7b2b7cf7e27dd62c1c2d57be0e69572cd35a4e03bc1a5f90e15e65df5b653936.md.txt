# C10: closing the C8 pair-test coverage

- The first C8 method needed an ordering whose plaquette span the C2 preserves: 72 of 108 (code, C2) pairs.
- `cover.py` tried corner-dressed C2-invariant flux conventions with clean hops for the other 36. It found
  none in the first classes tried, so it was abandoned.
- `pairsym.py` uses a general method. It solves for a pair creator S whose excitations are confined near
  x and Rx and match those of its rotated image. lambda is then the sign of S^dag S^R in the signed group.
  - On the 72 covered pairs it agrees: lambda = +1 (`pairsym_covered.log`).
  - On the 36 uncovered pairs it also gives lambda = +1 (`pairsym_uncovered.log`). This covers the
    order-4 codes' axis C2 and their second edge C2, and 12 single-C2 codes.
- Result: eta_f(C2, C2) = -1 for all 108 pairs under the bare permutation. For every code, the class on its
  rotation stabilizer is w2 restricted:
  - D3: the nontrivial class;
  - D2: the Q8 class (all three squares -1);
  - Z2: the nontrivial class.
- The general method is now in the C8 runner (PASS=9). It includes a control that returns -1: the toric
  code in pi flux under a plaquette-centred C2.
