# Supporting mathematical source

Original: `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_NATIVE_PERIODIC_POLE_CHECK.md`, SHA256 `9551ad317c122db922b061987fe7c2c4162f83d9a1972631d6c4f3a8357d8a6c`. This extract preserves the mathematical argument and its limitations; historical execution descriptions are not fresh evidence. Current promotion boundaries: `docs/work_history/repo/review_feedback/NEUTRAL_CONTINUATION_BOUNDARIES_2026-10-18.md`. Original report and verdict history are recoverable in the archive manifest.

# Focused finite native periodic response check

Two-point scaling is consistent with the proposed orders, not an asymptotic theorem. No formal audit or repository edits.

## Hamiltonian and source

The script starts with the open 2×2×L native compass bonds, adds exactly the four longitudinal closing ZZ bonds with coefficient -1, and scales only transverse XX/YY bonds by lambda. The YY computational-basis sign is correct. It does not add transverse duplicate periodic edges or a new interaction. The positive rung-Z constraints, global paired X-plane constraint, and two additional commuting signed plane operators define a selected invariant sector. For L8 each physical Y plane has 16 sites and i^16=1, so its (flip,phase,+1) representation has the correct physical sign. Selected-sector minimum does not establish a global ground state over all sectors.

An independent explicit isometric lift from the doubly reduced space to the full 16-spin computational space at L4 verified the periodic H action at lambda .1 and .2 to <9.5e-16 and the original Pauli source action to <4e-16. This tests the supplied reduction against unreduced physical Pauli action, not merely against another reduced implementation. Isometry norm is 1 to floating precision. The same periodic rule has no new L8 sign factor.

The source is O/sqrt(L), O=sum_(j,x,y) Z_(x,y,j)Z_(x,y,j+2 mod L). There are 4L terms. Dividing by sqrt(L), rather than sqrt(4L), is an explicit convention and agrees with the stated leading coefficient 2Z. The connected subtraction removes its expectation in the computed normalized state; total source_weight is the variance in this convention, not the pole weight. At L8 no NNN unordered pair is duplicated.

## Finite prediction

The finite dark matrix is [[-73/192-1,-3sqrt(2)/32],[-3sqrt(2)/32,-13/96]]. The sqrt(2) is the finite-ring terminal folding factor. Its lower eigenvalue is -1.394173009735397 and its boundary weight gives 2Z=1.9780554006912363. This is the L8 two-state matrix, not the infinite half-line bound-state coefficient.

I independently evaluated the bright-host Schur contribution using A=tridiagonal(2,2,2sqrt(2)), B=-A²/16+|0><0|/4, u=-sqrt(2)|1>, v=-sqrt(2)|0>+|2>/sqrt(2), s=-2. The coefficient -2u^T A^-1 v-u^T A^-1(sI-B)A^-1u is -1 to 2e-16, confirming the additional boundary term. The leading bright source 2lambda|0> and induced bright component -lambda A^-1u give magnitude sqrt(2)lambda², hence weight 2lambda⁴ times the normalized boundary probability. This uses the previously checked dressed-source convention; it does not identify an empirical coupling.

## Numerical qualification

For the nearest candidate, (gap-prediction)/lambda^6 equals 1.55000078 at .1 and 1.60077685 at .2. The correction (weight/lambda^4-2Z)/lambda² equals -2.24234198 and -2.33357611. These are consistent finite two-point observations of sixth-order gap error and quadratic relative weight corrections. They neither prove those asymptotic orders nor bound a uniform remainder.

Reconstructed full-H residuals for the first two candidates are (5.95e-10,4.86e-9) at .1 and (9.92e-12,8.61e-11) at .2; ground residuals are <1e-12. The remaining four candidate residuals per lambda range from .045 to .824 and must not be called eigenmodes or physical poles. Agreement of their Rayleigh quotients with quadrature nodes and near-unit reconstructed norms does not rescue them.

Lanczos uses a three-term recurrence without full reorthogonalization. Direct full-H residual reconstruction is therefore essential and correctly present. No exhaustive convergence, spectral isolation, or certified exact eigenvector weight is established: a residual certifies proximity to some spectrum, while an individual spectral weight requires isolation/eigenvector control. The two accepted candidates are numerically well separated relative to their residuals, but this is not a proof that no omitted nearby eigenvalue exists. No duplicate heavy 32-site run was performed by this reviewer; the JSON is supplied numerical evidence, with independent smaller-space construction and finite effective-matrix controls.

The result is a finite selected-sector spectral response with specified source and state. It is not continuum decay, a bulk pole theorem, a physical scalar, or a state-preparation derivation.

## SHA-256 identities

- `/private/tmp/neutral_native_periodic_pole.py`: `ab33b65a91d5ee38fae952467fd375850635b2408deacb7da635a96276170c7e`

- `/private/tmp/neutral_native_periodic_pole.json`: `b72485e438609cecd638ff703bc9ece8e934e5a4cbaef75ffa85a4bda9afd8dd`

- `/private/tmp/neutral-native-periodic-independent.py`: `83406333b84c8293452837615303bdd0da0df6dc93af28ae0d673e60b2597a2c`

- `/private/tmp/neutral-native-periodic-independent.json`: `4159e4ab21484b1d8738da7dbc351b15e3ada69093901584bcbee64bf270cd65`

- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_sector_basis.py`: `903ece39673616ae809fd44e66a186325252f0c75c77618ec905e7f95f5ef529`

- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_sector_solve.py`: `617a143fbd5112cee5d818512b72e9d49abd09970660a07e3a44e6f51b05c3b1`

- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_extra_sector.py`: `39838305b41d3b58515a7d7a424c7b62290bd0886fadab95cde38c7f03913318`
