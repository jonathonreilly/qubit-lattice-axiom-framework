# Handoff

## Current result

The strongest results are the exact finite-support formula `C(H2,S-H2,infinity) -> D`, the residue-resolved interior complete-generator edge limit `-196/625` along `S=n=15k`, and the strong-operator short-time theorem `t=tau/C`, whose vacancy curve is `1/3+(2/3)J_0(2 sqrt(3) tau)`. The 15-residue Jacobi correction has a semibounded form and one Friedrichs extension. These statements are conditional on the supplied six-site model and output in open PR #8831.

The new exact-kernel result gives a unique stationary vector with normalized flux density tending to `(15/16)(1-x^2)^2 dx`. Its positive ground-state transform has a compact weighted-form limit; for every fixed `j`, `C lambda_(S,j) -> j(j+5)/25`. The exact endpoint estimate requires `delta_S <= epsilon`, with the limit taken by fixing epsilon, sending S large, and then shrinking epsilon. Finite-spin eigensolver values corroborate the theorem but do not establish it. The fixed-index sector has vanishing prepared-state weight and does not control the growing-index phases.

The fixed-time vacancy projector is not resolved. The exact identity `1[q3=0]=1[n mod 3=0]=(I+V+V*)/3`, with `V|n>=exp(2*pi*i*n/3)|n>`, reduces it to two nontrivial Fourier expectations. The exact commutator has norm of order C and the initial curvature satisfies `p_S''(0)/C^2 -> -4`, so the elementary continuity bound grows with spin. Exact/candidate spectral values extend through S=384; an exact-only scan reaches S=1280. Across S=448..1280 the vacancy probabilities at the three times lie between 0.3259 and 0.3417. They remain near one third but fluctuate, and the scan does not compare the candidate past S=384. No error enclosure or fixed-time asymptotic theorem follows.

## Resume source and exact obligation

- Main source revision used for selection: `5efa36e7c357ae2a62ee586a5407f90982f6ded9`.
- Latest main screened during execution and fast-forwarded in the shared checkout: `8cc5f114f0d703100d6a7a764a1c689c7a56d65f`. Its fifteen new bounded notes concern supplied local clocks, record formation, and lattice locality; they do not derive the #8831 link-spin Hamiltonian or six-site post-mark output. The four minimal axioms, primitive registry, and science workflow are unchanged.
- Open parent: #8831 at `b6eb31bedb3134dfacd8f4ab83cb7d96fc6dc953`, based on `fe6dc2c5ef061fa1e0051063d49178f23b872c13`.
- Exact blocker quoted from its body: “joint finite-spin electric limit”.
- Strongest remaining proof: prove a fixed-time mod-3 Fourier limit or directly control the bounded vacancy expectation, including electric tails, the finite-spin boundary, the candidate domain/extension, and all `H4`/output terms.
- New spectral reduction: the exact zero mode has vanishing initial weight; after its positive ground-state transform, the fixed-index spectrum converges to the Gegenbauer operator with eigenvalues `j(j+5)/25`. Any fixed finite set of these modes has vanishing total initial weight. The unresolved mass is in modes whose index grows with S.
- Approaches tried: exact finite support, full finite-sector comparison, semibounded Jacobi form, macroscopic coefficient expansion, sparse-Krylov diagnostics, spectral exact/candidate propagation through S=384, exact-only propagation through S=1280, mod-3 commutator, and the shrinking-time strong limit. No route has certified the fixed-state observable at the frozen laboratory times.

## Next exact action

Derive the 15-cell bulk symbol for the staggered ground-state transform and a uniform semiclassical phase estimate for the two nontrivial mod-3 matrix elements across the moving-index spectrum at `T=Ct~S^2`. First identify stationary/resonant phase families and test whether the fixed times admit a uniform cancellation bound or a controlled subsequence. Use the exact factorization `exp(-itG_S)|0>=exp(it C M_S)eta_S(t)`, with `eta_S(t)=exp(-itM_S^2)|0>`; do not extrapolate the fixed-`tau` Bessel theorem into this regime. Retain electric tails and candidate-domain obligations; preserve the open status if no uniform result closes.

The block PR [#8943](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8943) is stacked on #8831 and is ready for focused review as a coherent conditional milestone. Its last public science checkpoint before this extension is `d7ba50d4e20a66d995c8fdc4e69254f0536b0108`; the base parent is `b6eb31bedb3134dfacd8f4ab83cb7d96fc6dc953`. The source dependency remains open; full integrated checks, merge, and formal retention await the parent chain. Do not merge or apply an audit verdict. Continue this campaign only after the pushed checkpoint is recovered in a fresh worktree and the disk guard reports at least 20 GiB free. On completion of the current lane, verify the push or main ancestry before removing only its worktree, then prune; never use `git gc` and never touch `archive` or `archive_unlanded`.
