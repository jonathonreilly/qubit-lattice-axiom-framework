# Handoff

## Current result

The strongest results are the exact finite-support formula `C(H2,S-H2,infinity) -> D`, the residue-resolved interior complete-generator edge limit `-196/625` along `S=n=15k`, and the strong-operator short-time theorem `t=tau/C`, whose vacancy curve is `1/3+(2/3)J_0(2 sqrt(3) tau)`. The 15-residue Jacobi correction has a semibounded form and one Friedrichs extension. These statements are conditional on the supplied six-site model and output in open PR #8831.

The fixed-time vacancy projector is not resolved. The exact identity `1[q3=0]=1[n mod 3=0]=(I+V+V*)/3`, with `V|n>=exp(2*pi*i*n/3)|n>`, reduces it to two nontrivial Fourier expectations. The exact commutator has norm of order C and the initial curvature satisfies `p_S''(0)/C^2 -> -4`, so the elementary continuity bound grows with spin. Exact/candidate spectral values extend through S=384; an exact-only scan reaches S=1280. Across S=448..1280 the vacancy probabilities at the three times lie between 0.3259 and 0.3417. They remain near one third but fluctuate, and the scan does not compare the candidate past S=384. No error enclosure or fixed-time asymptotic theorem follows.

## Resume source and exact obligation

- Main source revision used for selection: `5efa36e7c357ae2a62ee586a5407f90982f6ded9`.
- Latest main screened during execution: `7445cc7a50e2c7631d70dc8d9a065d0653ffa6ef`. Its thirteen additional bounded results concern supplied signed-field, eight-species, momentum, and exclusion models; they neither derive the #8831 link-spin Hamiltonian nor its six-site post-mark output.
- Open parent: #8831 at `b6eb31bedb3134dfacd8f4ab83cb7d96fc6dc953`, based on `fe6dc2c5ef061fa1e0051063d49178f23b872c13`.
- Exact blocker quoted from its body: “joint finite-spin electric limit”.
- Strongest remaining proof: prove a fixed-time mod-3 Fourier limit or directly control the bounded vacancy expectation, including electric tails, the finite-spin boundary, the candidate domain/extension, and all `H4`/output terms.
- Approaches tried: exact finite support, full finite-sector comparison, semibounded Jacobi form, macroscopic coefficient expansion, sparse-Krylov diagnostics, spectral exact/candidate propagation through S=384, exact-only propagation through S=1280, mod-3 commutator, and the shrinking-time strong limit. No route has certified the fixed-state observable at the frozen laboratory times.

## Next exact action

Use the exact factorization `exp(-itG_S)|0>=exp(it C M_S)eta_S(t)`, with the convergent profile `eta_S(t)=exp(-itM_S^2)|0>`, to analyze the long-time parameter `T=Ct` on the position-dependent finite Jacobi interval. Seek a uniform estimate for the two nontrivial mod-3 Fourier expectations or a rigorously separated subsequence. Do not extrapolate the fixed-tau Bessel theorem into this regime. Retain electric tails and candidate-domain obligations; preserve the open status if no uniform result closes.

The block PR [#8943](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8943) is stacked on #8831 and is ready for focused review as a coherent conditional milestone. Its science checkpoint is `3eff3c83fbe03592c0ebca300f2dcd84abdceea0`; the base parent is `b6eb31bedb3134dfacd8f4ab83cb7d96fc6dc953`. The source dependency remains open; full integrated checks, merge, and formal retention await the parent chain. Do not merge or apply an audit verdict. Continue this campaign only after the pushed checkpoint is recovered in a fresh worktree and the disk guard reports at least 20 GiB free. On completion of the current lane, verify the push or main ancestry before removing only its worktree, then prune; never use `git gc` and never touch `archive` or `archive_unlanded`.
