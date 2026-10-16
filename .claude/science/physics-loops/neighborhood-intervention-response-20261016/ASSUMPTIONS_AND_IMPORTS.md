# Assumptions and imports

The candidate supplies finite real coordinates, unit kinetic normalization, a fixed positive symmetric stiffness, linear source and readout, zero initial data for transfer response, a calibrated change theta*w*w^T, stable intervened matrices, and valid deterministic error/norm bounds. These are theorem conditions whose physical realization remains open. No framework primitive is used as an unstated substitute.

The Schur complement, rank-one inverse and convergent matrix series are standard mathematics re-derived in the note. Mori1965 is non-load-bearing prior-art context; only its abstract was consulted. No outside theorem, unmerged source, raw dataset or historical runner is needed for the canonical computation. The sole helper is imported normally.

Mathematically eliminated: explicit solution of all hidden coordinates when computing the boundary memory response; unknown response parameters H,J in the three-setting relation. Not retired physically: action, coordinate identification, preparation, source/readout, intervention calibration, physical scales and scalar/environment bridge. The later cross-ratio/preparation probe remains separately in the campaign development pack and is outside this PR.
