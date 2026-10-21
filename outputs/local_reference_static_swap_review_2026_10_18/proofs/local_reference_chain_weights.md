# Nonuniform positive reference-chain weights

ROOT author extension to the checked local-reference static SWAP, requiring a distinct check. The full source local_reference_static_swap/PROPOSAL.md9e68a0eb2f81955e900a23bd88b05321b75ea4e2741da89f812ef2eda59b5c70 and checkbc0e54499663904538b862421d7338c31131cd9dc2923519b7d45fffb323a00b were read completely. Only the reference-chain coefficients are changed; every other block, input, output and scope remains as in that source.

Replace uniform HF by

    HF=sum_{j=1}^{N-1} kappa_j(I-SWAP_Bj,B(j+1)),
    0<kappa_min<=kappa_j<=kappa_max.

Each block remains real, positive, nearestneighbor and energy conserving, with full norm2kappa_j. Every block kills the fully symmetric reference space, even when the weighted SUM fails to commute with arbitrary reference permutations. Its kernel is still exactly that space: a zero expectation of the positive sum with all coefficients positive forces each adjacent-swap difference to vanish, and adjacent swaps generate all permutations. Self-adjointness then gives Pi HF=HF Pi=0.

The already proved quadratic-form inequality sum_j(I-Swap_j)>=N^-2(I-Pi) immediately gives

    HF>=Delta(I-Pi), Delta=kappa_min/N².

No permutation symmetry of HF outside its kernel is used by this argument or by the integration-by-parts lemma. The exact local-exchange projection Pi exchange_PB1 Pi=(1/N)Pi sum_j exchange_PBj Pi is a property of Pi itself, unchanged by chain weights. Consequently equations8-15 of the source transfer unchanged with this new Delta. In particular the same actual free/scalar phase, complete-output comparison and512lambda/Delta elimination bound hold. No additional dynamical error is paid for chain weight variation within this fixed positive matrix family; its cost is the actual lower gap bound and physical incident loads.

For an explicit family fix0<eta<=1, Lambda>omega>0,0<epsilon<=1 and choose

    N=ceil(512pi²/epsilon²), kappa_max=(Lambda-omega)/8,
    kappa_min=eta kappa_max,
    arbitrary kappa_j in[kappa_min,kappa_max],
    Delta=kappa_min/N²,
    C_P=(sqrt5+3)/2+2sqrt2,
    lambda_max=min{omega/2,(Lambda-omega)/(2C_P),epsilon Delta/16384},
    m=ceil[omega/(2lambda_max)],lambda=omega/(2m),tau=pi/lambda,
    w=epsilon/[32(omega+9lambda/4)].

Then all source full-output bounds hold on[tau-w,tau+w]: vector<epsilon/8, unhalved stabilized channel<epsilon/4, and center vector<=epsilon/16. The actual target remains exp[-i(st+pi/4)]SWAP psi tensor beta(t). In particular no separate scalar sum_j kappa_j is added; HF is retained intact and has zero ground energy.

The P and Q loads are unchanged. B1 has load omega+2kappa_1+2g<=omega+2kappa_max+2g. Other reference sites have load at most omega+4kappa_max, with endpoint reduction. The same cap proof therefore applies. Counts N+2 qubits and2N+5 blocks and graph maximumdegree2 are unchanged. At fixed eta,omega and positive cap margin, the sufficient family still has sizeTheta(epsilon^-2) and timeTheta([eta(Lambda-omega)]^-1 epsilon^-5). The nonasymptotic prescription above should be used if eta also varies.

This permits independent, even adversely varying, real scalar coefficients within the specified interval; no probabilistic cancellation or calibration of their individual values is required when the common bounds are certified. It does NOT tolerate generic matrix errors breaking the symmetric kernel, arbitrary added fields, unequal free gaps, inaccurate data coefficients/local exchange, or imperfect product coherence without further error bounds. Reference preparation, full path/record composition, active arbitraryH_PE, halt and reuse remain open. This is an exact structural coefficient family, not a general fabrication guarantee.

This is ROOT's source-exposed author calculation. No solver, simulation, scientific execution, Git, sourceoverwrite, axiom, prompt or model changes occurred. Distinct checking is required before incorporating this extension in publication.
