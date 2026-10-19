# Outer-boundary comparison: distinct bounded check

No required mathematical correction was found in the final pinned proposal. Both perturbations and their complete-state Duhamel bounds are valid for their separately specified Hamiltonians. The fixed-diagonal perturbation matches the checked positive weak-source endpoint block exactly. The Laplacian-deletion perturbation does not match that block and must remain a separate result. Neither result establishes preparation from a product seed or bounds the required initial error epsilon0.

## Sources, exposure and scope

Paths below are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/`. Fully read and SHA-256 verified:

* `common_product_outer_boundary/PROPOSAL.md`: `af7dfe4193865bb80f9302fcb39f62c7be9ab7693d29b1b53bea8f620f8f2c43`.
* `common_product_autonomous_interface/PROPOSAL.md`: `bcc47793a94d578fcbf403115dcce099f6728752d0953a03d80051f75d3e22b5`.
* `common_product_autonomous_interface_check/REVIEW.md`: `90c7926ed7c681286108afe5a9063a9f63f2be690026ff0abc56844214ab67b2`.

For the endpoint-block comparison I reuse my preceding complete read/check of `common_product_endpoint_launch/PROPOSAL.md`, SHA `fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4`, and its identified positive local block. The preceding report is `common_product_endpoint_launch_check/REVIEW.md`, SHA `51247de9ba58bbfeb7f731c478d939e05e2e9d90956192d2e9e6f612401662c1`. No emission theorem is used as a premise of the present bound.

The exact ideal router h, unitary F, dispersion and S=exp(ik)C are the only router premises needed. The microscopic cell realization, attachment estimate and older finite-cut theorem are not used or re-certified. The reference review is supporting source qualification, not evidence that the new boundary lemma was already checked.

ROOT disclosed reading the original version and final change, catching its diagonal mismatch, and suggesting the new variant. That design exposure and favorable preliminary assessment are not independent verification. I read the final formulas before reconstructing their derivatives, phases, operators and norms. This is a distinct same-model source-exposed check, not blind discovery, model-diverse replication, formal audit or retained status. The original saved version was not separately needed: this report checks both complete variants as stated in the final source, not its historical diff. The workflow/skill snapshots identified in my preceding endpoint report are reused for this coherent bounded task; no remote-main freshness is asserted or Git operation used.

## Exact ideal state and phase planes

The router premise defines h as the graph Laplacian of the joined leads in the enabled sector and two Neumann half-lines in the disabled sector. In the eigenchannels of C, the generalized waves reduce to half-integer cosine and sine bases multiplied by unit-modulus factors. Those bases are complete and normalized, so F is unitary and there is no omitted bound-state column for this ideal router. Resolving C gives S(k)=exp(ik)C. The unitary and norm statements extend through arbitrary passive references.

For f_L=exp(ikL)g xi, ||f_L||=1, so psi(t) is exactly normalized. Substitution into the two traveling components yields phases `(L-n)k-tE` and `(n+L+1)k-tE`. The outgoing +1 is compulsory; replacing S by C would lose it. No derivative of exp(ikL) is omitted: that factor and the exp(ik) scattering factor have been moved exactly into these phases, leaving scalar amplitude g.

For n>=L-1, the incoming derivative is L-n-tE'<=1-tvmin= -q_i, and the outgoing derivative is n+L+1-tE'>=2L-tvmax=q_o. The window guarantees q_i>1 and q_o>2 throughout. It also forces L>2 (and hence the weaker source statement L>=2). Every contact site for either M=L or M=L+1 lies in this controlled range. The more general Laplacian statement M>=L likewise has M-1>=L-1. Although the pointwise envelope is uniform in infinitely many outer sites, the argument only sums it over three radial sites and does not misuse that uniform bound as an infinite-tail norm estimate.

Reversing the local source lead coordinate x=M-1-n sends exp(ikx) to exp(ik(M-1))exp(-ikn). Thus the phase distance is ell=M-1=L, not M. The corresponding outgoing router phase is exp(ik(n+M)), as (1) gives with L=M-1. This verifies the coordinate conversion; it does not identify a launched packet's entire spectral coefficient with g.

## Twice-integrated amplitude and envelope

Write lambda=phi'. After one integration by parts the differentiated amplitude is (g/lambda)'. On the second step one differentiates `(g'/lambda²-g lambda'/lambda³)`. The result is

    g''/lambda² - 3g'lambda'/lambda³
      - g lambda''/lambda³ + 3g(lambda')²/lambda⁴.

The coefficient 3 of the g' term comes from 2+1 quotient derivatives; the squared-derivative term comes from differentiating lambda^-3. This checks both potentially consequential coefficients. Compact support and C2 regularity remove the boundary terms at each step. Here lambda'=-tE'', lambda''=-tE''', with |E''| and |E'''| bounded by 2j. Taking absolute values therefore gives exactly G2/q²+6jtG1/q³+2jtG0/q³+12j²t²G0/q⁴. In particular the E''' contribution is necessary and included.

The two internal vectors xi and Cxi each have norm one. Applying the integral triangle inequality in their full Hilbert space gives M(t) with factor 1/sqrt(2pi), with no program, port or reference-dimension multiplicity. The two traveling contributions can interfere; the bound does not require their orthogonality or individual normalization.

For the incoming part, t/q_i=(1+1/q_i)/vmin<=2/vmin. Factoring q_i^-2 out of H gives precisely the four terms in A_i. Since tvmin>2, q_i>=tvmin/2 also gives the displayed inverse-square time envelope. For the outgoing part, t/q_o<=tf/qof, yielding A_o with all time-window factors preserved. No assertion that A_o stays bounded near return is justified or made.

Integrating q_i^-2 with q_i'=vmin gives `(1/qi0-1/qif)/vmin`. Integrating q_o^-2 with q_o'=-vmax gives `(1/qof-1/qo0)/vmax`. These signs and denominators reproduce B_window. Both terms are nonnegative and vanish for tf=t0. The assumptions ensure all denominators are strictly positive. Thus the integrated estimate (7) follows without a hidden asymptotic regime or exchange of limits.

## Laplacian perturbation

Removing the full cut bond subtracts its two diagonals as well as its hopping. Weakening the inner edge subtracts w times its full Laplacian. Consequently -Delta on the three contact sites is exactly the displayed weighted three-vertex Laplacian. It has zero row sums, trace 2(w+j), and the sum of its three principal two-by-two minors is 3wj. These determine its two nonzero eigenvalues as w+j ± sqrt(w²-wj+j²), confirming d_edge. Since 0<w<j, w+j<=2j and the square root is <=j, proving the stated upper bound 3j.

The remaining graph is the finite router plus disconnected exterior half-lines whose first retained edge is (M+1,M+2). This is not a zero exterior extension. All remaining weights are positive with degree at most two, so the one-head operator is positive with norm at most 4j. This operator's lowered boundary diagonals prevent identifying it with the fixed-diagonal source by a relabeling.

## Fixed-diagonal perturbation and exact source block

Adding w adjacency on (M-1,M) changes -j to -gamma. Adding j adjacency on (M,M+1) changes -j to zero. Neither changes a diagonal. For M=L+1, the three affected sites are interior ideal lead sites, all with original diagonal 2j in both program sectors. At router n=0 the existing enabled/disabled boundary difference is preserved.

In (13), the last inward j bond contributes j to M-1. The block involving M-1 and M is

    Q_gamma(M-1,M)+(j-gamma)n_(M-1)+(2j-gamma)n_M.

Identifying s=M and local lead site 0=M-1 gives exactly the earlier B, with one-head matrix [[2j,-gamma],[-gamma,j]] in the (s,0) order before adding the inward j bond. Its two-site double-occupation diagonal is 2gamma+(j-gamma)+(2j-gamma)=3j. Thus the match includes the full positive local qubit block, not just the hopping or its one-head compression. Including the inward bond raises the lead-site diagonal to 2j while leaving the emitter at 2j.

The exterior half-line's first retained Q_j supplies only j at M+1, so the additional j n_(M+1) in (14) is necessary and exactly restores the unchanged ideal diagonal. Equations (13) and (14) therefore prove the claimed direct-sum identity, with no missing endpoint compensation. Every displayed term is positive in its stated domain. Positivity of Delta_hop itself is neither true nor needed.

The three-site adjacency perturbation has eigenvalues 0 and ±sqrt(w²+j²): squaring it gives middle entry w²+j² and a rank-one outer two-by-two block with the same nonzero eigenvalue. This independently confirms d_hop and its sqrt(2)j upper bound. Both port copies form orthogonal direct summands, so their norms are maximized, not added. Identity factors on programs and passive references leave this norm unchanged.

For h_fixed, each diagonal is at most 2j and each absolute off-diagonal row sum at most 2j, including the disabled router endpoint, which has smaller diagonal and degree. The equal column bound follows by symmetry. Schur's bound gives norm <=4j on the infinite one-head space, as well as on finite restrictions. This says nothing about boundedness on unrestricted infinite many-head sectors. The endpoint block retains the local load conventions checked in the earlier launch report, but this new note does not supply a complete microscopic device load or mediated-router resource certificate.

## Full-state Duhamel bound and uniformity

For either perturbation D, D=D P_3 and ||P_3 psi(t)||<=sqrt(3)M(t), where each radial amplitude already includes both ports and the reference. This gives the residual sqrt(3)||D||M(t) without an additional sqrt(2) or a sum over programs.

Differentiating `exp[-i(tf-t)(h+D)]psi(t)` with respect to t gives `i exp[-i(tf-t)(h+D)]D psi(t)`. Integrating and rearranging yields the stated negative-i Duhamel identity. The rightmost vector follows the exact ideal evolution; unitarity of the left propagator then gives sqrt(3)||D||B_window. Both compared vectors are unit vectors, establishing the cap 2. This proves (11) and (16), respectively, with their distinct norms.

The map xi to psi(t0) is an isometry because multiplication by normalized scalar g and exp(ikL), F, and evolution preserve norm. All estimates hold for every unit xi in the complete legal program/path/reference space. They therefore are induced isometry-norm estimates, not only basis-column tests. A common scalar on both Hamiltonians retains the same physical phase and leaves the norm bound unchanged.

For a normalized physical finite-summand phi, the extra initial distance epsilon0 propagates unchanged by unitarity. Adding it yields exactly the final claimed extension. That distance must include any ideal exterior tail, source residual, packet/phase mismatch and normalization discrepancy. None of those is bounded here. The initial ideal psi(t0) generally has exterior support, and evolving it in a direct sum does not make it a prepared finite-device state.

## Disposition and verification limits

The result supplies an integrable outer-contact perturbation bound during the stated separated window. The corrected fixed-diagonal form is compatible with the specified weak-emitter local Hamiltonian. It does not prove launch, the size of epsilon0, product-seed composition, physical mediator replacement, a final normalized finite outgoing packet, permanent capture, all-late behavior, or optimized runtime. No finite-product-seed derivation was read or imported.

Only this report was written. No scientific program, simulation, symbolic solver, numerical quadrature, source edit, Git/canonical/PR/checkpoint/editable-prompt change, model/effort change or additional delegation occurred. Hashing and directory creation were bookkeeping. This distinct check supports the bounded statements at the specified source identities and assigns no audit or retained status.
