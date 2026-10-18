# Focused slow native control review

Disposition: PASS after one narrow wording correction below. This is ordinary scoped review, not an audit verdict or native pole certification.

The canonical scope is appropriate: exact finite-order local coefficients and support/grading proofs are distinguished from finite patch checks and from the prior projected resonance. The supplied uniform reference, proper nonwrapping supports, termwise H0-conserving local decomposition, fixed finite normal-form order, and full compact E8 cutoff are explicit premises. The restricted bound controls finite coefficient tails, not the actual BCH remainder, source accuracy at order lambda^6, or the corrected outgoing fast resolvent. Native lifetime and physical identification remain open.

Reused INDEPENDENT_SLOW_PARITY, SUPPORT, THIRD, FOURTH_DIAGONAL, FOURTH_KERNEL, and RESTRICTED_BOUND. The Hamming argument, ell=3 K3 boundary vertex, folded K4 normalization, vacuum subtraction, affine diagonal extension, x/y phase convention, and finite-cutoff leakage extension agree with these checks. No new full computation was needed.

Inspected all five literal input scripts and runner. They enumerate native bit configurations with exact Fraction arithmetic and explicit boundary energies; no external model or numerical result is silently loaded. The single-wall sequential enumeration provides an independent implementation of the long-row hopping calculation. The aggregate regenerates inputs, checks the stated coefficients and symbol, binds input SHA256 values, and creates its output directory. Parent reports source-bound replay PASS in 18.756166 s; that replay was not independently repeated here.

Narrow fix: section 4 says the K4 symbol has its “bottom value at k=0”. Its negative quadratic coefficient makes that wording incorrect for the isolated K4 symbol. Replace with “value at the leading K2 slow-arm band bottom k=0”. Numerical 109/96 and -3/16 are correct. No other material finding.

Reviewed source hashes (SHA256):
- `docs/NATIVE_SLOW_COMPOSITE_CONTROL_NOTE_2026-10-18.md`: `6e47b683bdf09f805cea1379d24843f73b3a6a968b72c1f08fcee9e2d8fe54c9`
- `scripts/native_slow_composite_control.py`: `b6875f523420656bc6ca9ba24a5e1efdb42cc96f19ac742c6de8f4889f825cbd`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_dispersion.py`: `0e337edde255fed16db83eb3dcbdedc1fab63917472e4df812574ff1b723641f`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_fourth_diagonal.py`: `4624708155ec423cfa8bd1b72b0a4bc6707586645ae63ae11b912f9931765e28`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_fourth_kernel.py`: `fa4baf44e681d06350c0863936e6b38ef945dc0bd373ef21fb65a32867361dc4`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_fourth_kernel_y.py`: `e517989bc9d60a7c3dfc087cb7510c1f5a33a3c2191eac6b7799b2793bfa08a7`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_fourth_local_independent.py`: `99cdba7d514e843be41ec85bb8f92a834ba593637ccd5cd82a707cc21b6c7734`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_host.py`: `c45065369d566859cd563e8108df1b00ca3737c5dfaf1c5ad582ea11c5ad40c2`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_resonance.py`: `46b6aa515b57afa0d01c4b3133468d8a46a8d2c31ec6cae85140b006f8a1176a`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_response.py`: `ef791baf551b21c832c018744535b0dfaba326e769f77e05be0745a0703545a7`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_source_check.py`: `e5de3965646a6967e130dae10fa40cdbcf4e8a60298e2e904dd3cedbef4a88eb`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_third.py`: `723ccb04d6e610fd993e4dc329e4ba9e03564028c41596478c8f9656128e63fa`

Final affected-fix confirmation: PASS. Canonical section 4 now identifies k=0 as the leading K2 slow-arm band bottom, resolving the only finding. No outstanding material fixes. Updated note SHA256: `6e47b683bdf09f805cea1379d24843f73b3a6a968b72c1f08fcee9e2d8fe54c9`. Source scripts unchanged.
