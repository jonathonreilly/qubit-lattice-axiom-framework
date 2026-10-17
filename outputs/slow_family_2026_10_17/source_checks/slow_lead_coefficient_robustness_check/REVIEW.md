# Selective check: receiver coefficient perturbations

Disposition: conditional support, with no necessary source correction. The dimension-independent one-head perturbation norm, finite-time Duhamel comparison, single-read consequences and correlated-diagonal variant are valid for the explicitly restricted coefficient-error class. The result is a sufficient perturbation certificate, not a necessary precision bound or a native robustness theorem.

## Evidence and exposure

Read COMPLETE `../slow_lead_coefficient_robustness/PROPOSAL.md`, verified SHA256 `f057da16b1a81ba024721c0b7ca22d6f5a95ce56e7e284b891ab22f5605f0fe1`. I did not author this root-authored proposal. The proposed route and bounds were exposed. I authored uniform composition8cd26edcb7941d8254494480455d17c137652ec779e37e78901de5a04e71ac9e and several gate/recovery interfaces, but not the receiver resource source84b76d1ec9b1e45811b74ecd2594a0622dfb01ef69d1acadf98931c0ed3f9967. That complete resource source was read in preceding coherent work and remains unchanged; its exact receiver block inventory is reused here.

Read COMPLETE the distinct uniform composition check `../slow_lead_uniform_composition_check/REVIEW.md`, SHA256 `b873ac37d8a327f27491f36e80dfe5e8aeef7eb0d7b405bba6b70a6ffb9e71a7`. It supports its pinned composition with the stated scope readings. The perturbation source's statement that composition checking was pending describes its drafting time; the present review does not recertify my own composition. Section3 of the perturbation lemma works with any separately valid nominal finite theorem satisfying its stated hypotheses. The fixed published numerical performance is not a premise for the perturbation proof; its T=10^15 example requires only elementary arithmetic.

This is distinct-author checking of the new perturbation lemma, not blind review or independent recertification of all ancestors. Applicable unchanged review instructions are reused. No solver, sweep, scientific execution, subagent, source revision, W/Git, prompt or model change occurred. An accidentally created bookkeeping placeholder outside the deliverable directory was immediately removed; no such file remains. Only this review is retained.

## 1. Allowed blocks, number conservation and M=1

The receiver inventory has one new connector, M-1 internal slow bonds, M+1 compensating occupations (one at o, one at the first slow site, and M-1 later sites), and one terminal cap. Each physical site has at most one compensation occupation. The cap is a separate installed block and may coexist with that compensation. At M=1 the first slow site is also the last, but there is still only one first-site compensation and one cap; no internal bond or later-site compensation is introduced. These counts match the resource source.

For nonnegative a, Q(-a)=a(n_x+n_y-exchange) has one-head eigenvalues0 and2a, head-vacuum value0 and doubly occupied value2a. Thus it is fullspace PSD and conserves head number. Nonnegative occupations are also PSD and vanish in the head vacuum. Varying their coefficients within nonnegativity preserves the seeded one-head sector. It introduces no vacancy scalar: all these operators annihilate the head vacuum, even if their errors have either sign relative to the nominal values.

The lemma retains the graph and all upstream, emitter, gate and shared-internal interactions. Consequently the receiver perturbation acts as the identity on the entire internal fiber, not only a favorable selected B channel or a prepared source state. It may alter phases through actual occupation-energy changes, but those changes are part of DeltaH, not a discarded common scalar.

## 2. Exact row bound and unitary comparison

In the one-head position basis a bond coefficient error delta contributes delta at each endpoint diagonal and -delta at its two off-diagonal positions. Its absolute contribution to either affected row is at most2|delta|, including its diagonal contribution. Two internal bonds therefore cost at most4e_g; one connector costs at most2e_tau. A compensation and cap add at most e_o and e_c. Adding these safe local maxima yields

    ||DeltaH||<=B=e_o+e_c+4e_g+2e_tau.

Not all maxima can coexist at one site, but this only makes the bound conservative. For M=1 the internal-bond term is absent, giving e_o+e_c+2e_tau. Symmetry gives the same column-sum bound, so the standard row/column Schur inequality proves the operator norm estimate. Tensoring the full internal identity or a passive reference does not change it. No sum over M sites is needed, and the lemma does not assert this norm bound on unrestricted many-head states.

For the finite self-adjoint restrictions, Duhamel integrates exp[-i(t-s)Htilde] DeltaH exp[-isH]. Unitarity bounds the integrand by B, so the full seeded-map difference is <=|t|B. Each evolved seed map has norm one, giving the separate ceiling2. Their minimum is therefore valid for either sign of t. This compares the literal unitaries and their accumulated phases; no phase alignment or gauge quotient is used. Projection and reference tensoring preserve the bound.

## 3. Successful-map and complete-state consequences

On the absolute nominal horizon[0,2T], adding min(2,2TB) to the nominal branch error gives the stated epsilon_pert. For a normalized old/reference input, the reverse triangle inequality against its comparator of norm r(t)>=R_T gives success probability at least(R_T-epsilon_pert)^2 when epsilon_pert<R_T. The standard normalized-vector comparison costs at most2epsilon_pert/r(t), hence2epsilon_pert/R_T. This requires useful positive success and does not claim relative correctness for arbitrarily rare early reads.

Both the successful operator and its subnormalized comparator are contractions. Expanding A rho A*-T rho T* gives completely bounded trace norm at most(||A||+||T||)||A-T||<=2epsilon_pert, including arbitrary references. It is a bound for subnormalized CP maps; conditioning generally is nonlinear.

For the complete finite vector, the ideal normalized vector y lies wholly in record1. The projected error implies Re<y,U_tilde psi>>=r-epsilon_pert. Unit-vector geometry therefore bounds the squared complete error by2(1-r+epsilon_pert)<=2(1-R_T+epsilon_pert), with the trivial distance ceiling2. This retains failure, source and all head coordinates. An independently supplied full nominal vector estimate can also be combined directly by the Duhamel triangle inequality.

The sufficient extra-budget condition B<=e_impl/(2T) is correct. For T=10^15 and e_impl=10^-4, it is B<=5*10^-20. This proves only a conservative sufficient certificate. It does not infer that every allowed error has this impact or that smaller necessary engineering tolerance has been established.

## 4. Exact diagonal correlation and positivity

If all one-head diagonals remain exactly their nominal values, DeltaH loses its diagonal entries. Each internal bond now contributes at most e_g to a row and the connector contributes at most e_tau. Thus2e_g+e_tau is a safe row bound for inhomogeneous realized hoppings; at M=1 the sharper e_tau also follows. Cap and compensation errors have been absorbed into the exact diagonal relation, not silently ignored for independent errors.

The proposal correctly makes nonnegative compensation a separate premise. Explicitly, if the realized connector is tau' and internal bonds are g'_m, gate-o compensation must be j-tau'. For M>=2 the first-site compensation is2j-tau'-g'_0, interior compensations are2j-g'_(m-1)-g'_m, and the last site's compensation plus cap must sum to2j-g'_(M-2). For M=1 that sum is2j-tau'. All individual installed coefficients, including the cap, must be nonnegative. These conditions show concretely why exact diagonals alone do not imply PSD occupations. Subject to them, the same invariant-sector Duhamel proof applies with B_corr; no unproved physical ability to enforce the correlations is assumed.

## 5. Scaling and limitations

With T(a)=T0/a^2, a sufficient B(a)<=a^2 B0 indeed keeps2T(a)B(a)<=2T0B0. A fixed relative connector error generally scales as a because tau(a)=a tau0, so it does not automatically satisfy that sufficient envelope. Receiver compensation coefficients approach nonzero constants (and gate-o compensation approaches j), so fixed relative compensation errors also do not automatically shrink as a^2. Even after exact diagonal compensation, the connector off-diagonal error remains and must fit the correlated budget. The lemma makes none of these conditions necessary.

All claims remain restricted to real, number-preserving receiver errors on the fixed graph acting as internal identity. Source/emitter calibration errors, wrong initial states, unwanted interactions, additional heads, measurement identification, physical-unit supply and native realization require separate treatment. No permanent storage, repeated-monitoring theorem or precision advantage is established. Within that scope the proposed perturbation interface is supported without amendment.
