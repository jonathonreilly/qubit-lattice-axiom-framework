# Focused native correlated-state source review

Disposition: PASS for the stated conditional model mathematics and prepared-state diagnostics. This is an independent source review, not a formal audit or landing authorization. Root retains authorship. Branch codex/neutral-state-selection-20261018; base HEAD c17f762306964cd53b839f8ba4b582198c7cd5dd; reviewed working-tree sources.

## Findings and resolved corrections

No remaining material mathematical or physical overclaim found. Corrected canonical prose had described magnetized real preparations as time-reversal symmetric. Reality suffices for zero initial slope here; physical spin time reversal is broken by magnetization. The final note now removes that identification. A stale statement that the bulk dimer count remained undocumented was also removed after the explicit independent leakage derivation was included.

## Independent assessment

The separability bound follows directly from ab <= (a²+b²)/2, the cubic bond incidence and Bloch-vector length <=1, and extends to mixtures. The -17J/16 dimer and -1153J/1056 four-site bounds are variational upper bounds, correctly oriented. I independently checked the rational optimization B=33/16, s=1/(2B)=8/33 and (B+1/(4B))/2=1153/1056. The elementary lower bound is valid: the three distinct positive-directed compass bonds at each site anticommute, hence h_x²=3J²I and summing h_x >= -sqrt(3)JI yields H >= -sqrt(3)JNI. Neither this wide bracket nor floating cluster improvements certifies a ground-state approximation.

The full CNOT coordinate map retains both logical and parity qubits, with the six Pauli maps and oriented bond factors consistent. Its partial expectation is explicitly a variational functional. The even-parity compression is not an invariant sector. The independent local parity count gives leakage/N=J²(3/2+s²); at s=1/4, total 201/128 minus projected 1/128 equals 25/16, with fraction 200/201. Small-torus alias corrections remain explicit.

The cluster variance implementation uses final actual moments and includes both incoming and outgoing face fields only in h_eff, while counting energy interfaces once. Its tensor-pair norm is sum_ij G_upper,ij G_lower,ij, with no extra conjugation. Orthogonality by excited-block support justifies the decomposition on the infinite simple block graph; the note excludes repeated-neighbor short-torus misuse. Tiny local residuals are not confused with the positive full variance. The acceleration contraction has the correct H=-sum-bonds derivative sign, floor-division mapping for negative coordinates, little-endian Pauli action, and unit-cell anchor averaging. Nonzero second derivative is a direct local nonstationarity witness; no equilibrium spectral function or scalar pole is inferred.

## Reproducibility and scope

Read the canonical note, runner, all nine declared Python inputs (the transport algebra was reviewed in the preceding native transport block), and the five independent state/projection/four-site/variance/acceleration reports. The aggregate result contains 14 result objects; all nine declared source hashes match current files. Stored cluster energies and accelerations agree with the note. No heavy optimization replay was duplicated: parent completed aggregate replay and is running its cache check. The independent 2x2x2 acceleration report checks a separately constructed commutator and dense local contraction; larger sizes remain explicitly root-only numerical checks. The numerical cluster searches preserve unsuccessful seeds and do not claim global optimality. State choice, Hamiltonian and J=1 numerical convention remain supplied assumptions. Exact compatible-tiling statements are distinguished from finite-size controls and floating values. No added interaction, state-selection mechanism, ground-state claim, measurement coupling or cosmological scalar identification is introduced.

## SHA256 source snapshot

- `docs/NATIVE_CORRELATED_STATES_NOTE_2026-10-18.md`: `d236dd4c297ead1538e91f51d38b321feded2721ee1d325215b8d95b5035b543`
- `scripts/native_correlated_states.py`: `3a7a3d43a0a4e367a61457eecf0cfd790a4b77d2a250d7d850a19fd03f405b0f`
- `outputs/native_correlated_states/result.json`: `f3038f684a2c54af317bb6cb77df6934cbc94bcae312c9c1305e172a7732c2cf`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_product_state.py`: `c3223bee6ecf9bcbcab0ad2c1fac3c530fb1eb8e77c69f72345874b7ba4fd756`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_dimer_state.py`: `f7fdcfbbbdfae2d3177eff80e3a456b3a42cdf29cb8150f3a895499273599a31`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_dimer_projection.py`: `7174a60ac69de4b95fd28c65b20d322a41b297f676803e2e985db835a6f7a5a2`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_full_dimer_map.py`: `47a1db76749fb08e31b010740e771db74927576b831f9b019e5ca67c21a52e80`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_four_site_trial.py`: `13e5cb62e26f18dede1c4aad37922d8e9c8f4c8fb128caefd2c58a1b31bf8fca`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_four_site_residual.py`: `003eec88e86810079755b6b9fd3f90d2225b54ddf89d6d99c07996e51321bfc6`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_cluster_variational.py`: `da4b125d8ca862e6383de2600eda44bdb4677b33f324c38535a3d6cf938220c6`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_cluster_neutral_acceleration.py`: `bf4d86aa7d64eea468f71d545963638f91c8aae6b50a10ca21a525af6b79e9ca`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_local_transport.py`: `3f025982118f00fab1e96412d77eb9f2080fe1a086f4a5f3b5c9583d77f0c53e`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/STATE_ROUTE_DERIVATION.md`: `8e55b95279bc90772d64d01578ab53d4b637dcbc51e14455e35e8e34910e6be4`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_STATE_CHECK.md`: `dd1000ed195558e07a5d402bd9790ff7aeefbaa7bd11554026924af771cf675e`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_DIMER_PROJECTION_CHECK.md`: `361c8a979d9d286aedbaa2df708926c4c8a6926e5e15e55aa28f4fab123b7f27`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_FOUR_SITE_CHECK.md`: `0c750899e3328f5bef7f5b3ad9c9b6e73a4e4ec2b1c962cc8ff63d784d7d801c`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_CLUSTER_VARIANCE_CHECK.md`: `c6d47f5b7bba65ea066741e605cd75b99a6fbb0859c767d47694f6ee23f194bc`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_CLUSTER_ACCELERATION_CHECK.md`: `c4d71a070d69367232e994974cfe5562d5f1c943f77560b66299f7cb689f50ef`
