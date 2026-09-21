# Numerical cycle-six fixture correction

The selective independent review found that `killing_bounds()` selected
`cycle6`, while `graph_cases()` provides `cycle_6`. Only that selector changed.
The mathematical note, rates, proof bounds and tolerances remain unchanged.

The reviewed original source is preserved at
`geometric_polynomial_fixture_fix/before_geometric_polynomial_relaxation_check.py`
(SHA-256 fded420e936b93bee16aeba4bfed676363d0298e6c1268fa5193cea5ef0c0202).
All original results, logs and review seals retain their bytes and identities.
The corrected source has SHA-256
996c2098b94a0f3e3331cfb7152af40bf18e7b6307e5a806204e9569e04478f0.
When authenticating old seals, resolve their old runner binding through that
preserved copy; do not reinterpret them as covering the corrected bytes.

`geometric_polynomial_fixture_fix/check_correction.py` runs only the affected
numerical killing group in temporary storage. It verifies that five cycle-six
rows are now present, all 40 rows satisfy their original assertions, and the
previous 35 rows agree with their historical values within the reported
floating comparison tolerance. The successful correction has empty stderr.
The exact rational cycle-six controls were already present in the frozen
original suite and are not represented as new checks.

The separate narrow reviewer acknowledgment is pending. This correction is
executable coverage repair, not a new theorem or formal audit disposition.
