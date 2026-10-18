# Distinct check: positive nonuniform reference-chain weights

Disposition: SUPPORT for the stated structural coefficient family. No required correction found. The extension changes only the positive scalar weights of the ferromagnetic bonds. Its complete-output guarantee follows with the certified minimum-weight gap, without an added perturbation-time error. This is not a general disorder theorem or retained audit.

## Exact target, evidence and exposure

Fully read and hash verified `local_reference_chain_weights/PROPOSAL.md`, 3976 bytes, SHA256 `7bae8b953e0bbb4435f9398029b42b081257b5c5b0edffc0d37ffb41152f8d5f`. All paths here are under `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`.

The unchanged baseline is `local_reference_static_swap/PROPOSAL.md`, 16601 bytes, SHA256 `9e68a0eb2f81955e900a23bd88b05321b75ea4e2741da89f812ef2eda59b5c70`, with distinct check `local_reference_static_swap_check/REVIEW.md`, 13502 bytes, SHA256 `bc0e54499663904538b862421d7338c31131cd9dc2923519b7d45fffb323a00b`. These hashes were refreshed. I authored the baseline, read its distinct check fully for the publication draft, and reuse its unchanged calculations at their checked scopes. ROOT authored the present extension. This is a distinct source-exposed check of that extension, not a new blind check of my own baseline or an independent scientific lineage.

## Kernel and full-space gap

Let E_j=I-S_j, with S_j the adjacent reference-qubit swap. Each E_j is positive and satisfies E_j^2=2E_j. With all kappa_j>=kappa_min>0,

    <psi,H_F psi>=sum_j kappa_j <psi,E_j psi>=0

holds if and only if every <psi,E_j psi>=0. Equivalently every (I-S_j)psi=0. Adjacent transpositions generate the full permutation group, so this joint fixed space is exactly the fully symmetric reference space Pi. This is true on the complete reference Hilbert space, not just a specified magnetization sector; tensoring data and passive references does not change it.

Every term separately kills Pi. Self-adjointness therefore gives H_F Pi=Pi H_F=0, so Pi remains an invariant projector for H_F. This property must not be confused with invariance of H_F under conjugation by all reference permutations: the latter generally fails for nonuniform edge weights, but is not needed. In particular the ordinary reference permutation symmetry used to identify Pi is still a property of the subspace itself.

The baseline full-space form inequality is

    sum_j E_j >= N^-2(I-Pi).

Positivity of all E_j gives the direct comparison

    H_F=sum_j kappa_j E_j
        >=kappa_min sum_j E_j
        >=(kappa_min/N^2)(I-Pi).

Thus Delta=kappa_min/N^2 is valid. The symbol kappa_min may be a certified common lower bound rather than the attained minimum. The proof does not require measurement or calibration of individual weights. A vanishing allowed lower bound would remove this uniform certificate; no such case is included in the source.

## Projected dynamics and phase

For any reference permutation U, U Pi=Pi U=Pi. Conjugating a single-site reference raising or lowering operator between sites and sandwiching by Pi therefore gives the same compressed operator. Averaging establishes exactly

    Pi exchange_(P,B1) Pi
      =(1/N)Pi sum_j exchange_(P,Bj) Pi.

This uses Pi and the unchanged local exchange, not commutation of the weighted H_F with permutations. The projected W=H_S+g exchange_(P,B1) is consequently identical to the baseline projected star; the latter preserves Pi.

In the elimination lemma take A=the ACTUAL weighted H_F. All its hypotheses remain valid: A Pi=0, A>=Delta(I-Pi), ||W||<4lambda and ||(I-Pi)W Pi||<=sqrt(2)lambda. The complementary compression satisfies D>=(Delta-4lambda)I. The derivative bound ||p'||<=4lambda still uses Pi A=0, so no norm of the weighted chain, accumulated weight difference, or outside-kernel permutation symmetry enters. For lambda<=Delta/8, the complete finite-time bound remains <512lambda/Delta up to2pi/lambda. It includes all reference leakage and correlations.

There is no need to compare the weighted actual Hamiltonian to the uniform actual Hamiltonian by Duhamel. Doing so would produce a needless weight-difference budget. Each admissible weighted operator independently meets the same structural comparison to the projected star. This justifies the source's statement that no additional dynamical error is paid, while the minimum-gap and maximum-load bounds still change the prescription.

Every weighted swap conserves the equal-gap reference energy, so [H_F,H_E]=0. The other terms are unchanged. The factorization is still e^{-ist}e^{-itH_E}e^{-it(H_F+W)}. H_F is retained intact with zero energy on Pi: its sum of positive identity contributions is not a further scalar phase on the effective comparator. Thus the complete target is precisely e^{-i(st+pi/4)}SWAP psi tensor beta(t), with the original ordered-free-factor proof. No reference output is dropped, and the target remains independent of the individual kappa_j within the certified class.

## Parameter policy, cap and sufficient orders

For 0<eta<=1 set kappa_max=(Lambda-omega)/8 and kappa_min=eta kappa_max. These are positive under Lambda>omega>0. The proposed lambda_max uses the new Delta and positive constants. With m=ceil[omega/(2lambda_max)] and lambda=omega/(2m), lambda<=lambda_max, hence lambda<=epsilon Delta/16384<=Delta/8 and512lambda/Delta<=epsilon/32. The revival tau=2pi m/omega is exact on the full free-energy spectrum. The unchanged width gives 0<tau-w<=t<=tau+w<2tau, within the elimination horizon.

The unchanged N prescription supplies star error <epsilon/16 over the window and <=epsilon/32 at its center. The timing term is <=epsilon/32. Adding the new-gap elimination allowance <=epsilon/32 gives vector error <epsilon/8, unhalved stabilized complete-channel error <epsilon/4, and center vector <=epsilon/16. These are complete-input bounds with arbitrary passive references, not rare-event or projected-reference estimates.

For physical loads, B1 meets one chain block with norm2kappa_1 plus the unchanged norm2g exchange and its free occupation. Other reference sites meet at most two chain blocks, so their maximum load is omega+4kappa_max; endpoints have one. These are bounded by exactly the baseline cap proof with kappa_max replacing uniform kappa. Q/P loads and all other blocks are unchanged. Thus all incident full-support sums remain below Lambda. There remain N-1 nonzero chain blocks, because all weights are positive, so the totals N+2 qubits and2N+5 blocks and line degree two are unchanged.

At fixed eta,omega and positive cap margin, N=Theta(epsilon^-2), Delta=Theta(eta(Lambda-omega)epsilon^4), and the epsilon Delta/16384 term eventually dominates lambda_max. Since lambda_max<=omega/2, the integer ceiling places lambda between lambda_max/2 and lambda_max, preserving the order. Hence tau=Theta([eta(Lambda-omega)]^-1 epsilon^-5), with size Theta(epsilon^-2). When eta itself changes, the displayed nonasymptotic maximum/minimum policy, not a fixed-eta assertion, controls the result. These are sufficient-family orders, not lower bounds or physical preparation times.

## Limits and work record

The allowed freedom is in positive REAL scalar multipliers of the exact I-SWAP blocks. It permits adversarially different edge values in the certified interval without statistical assumptions. It does not cover generic two-qubit matrix errors, kernel-breaking fields, unequal gaps, perturbed data coefficients/local exchange, imperfect coherence, or added interactions. Exact input preparation, passive environment, degenerate Q, fixed-window selection and absence of full-loader/capture/halt/reuse claims remain essential.

The complete extension was inspected analytically. Commands performed source reading, Python3 pathlib/hashlib identity checks, and text writing only; no scientific executable, simulation, solver, sweep, external search or delegation occurred. Only this REVIEW.md was created. No candidate or manuscript, W/Git/checkpoint/axiom/editable-prompt/model or publication/audit status changed. No editable prompt changed. SUPPORT here is a selective check of ROOT's weighted-chain extension with explicit shared ancestry, not a retained audit.
