# Engineered finite clock for the exact positive two-body loader

ROOT candidate, 2026-10-18. Proposed conditional theorem pending distinct check. This is a supplied architecture with ordinary freely degenerate Q/P, blank R, supplied endpoint coherence and passive references. It does not implement an active historical system Hamiltonian, derive native coefficients, or prove permanent halt. All apparatus outputs and the common phase are retained.

## Dependencies and attribution

In this renewal directory, exact_two_body_direct_loader_composition/PROPOSAL.md SHA256 f874302baf42f962939fb0c9497b2c4f55283ed9189671048faadeeb04eca946 and review41a080068c63261491aeaa04b9c4b397fb31de03f160724be0024b81020e73f6 establish the ordered26-layer gate and actual record projection. exact_loader_structured_coefficients/PROPOSAL.md SHA515c9e17df0a0c12e7df0dab6431015348af4140cef69189d334cd3574ea3de2 and review273da0a0d28269e6e40aff0695f5465456acd35abe4c0b4eddc1acf0578334c8 establish nonuniform scalar Jacobi realization by positive blocks with correlated arms/rails. ROOT fully read those arguments/checks. This candidate supplies new coefficients, finite performance and resource calculations, requiring a distinct check.

The engineered spin-chain transfer mechanism is established machinery, not claimed as new: M. Christandl, N. Datta, A. Ekert and A. J. Landahl, Perfect state transfer in quantum spin networks, Phys. Rev. Lett.92,187902 (2004), arXiv quant-ph/0309131v2, https://arxiv.org/pdf/quant-ph/0309131. ROOT read the primary PDF, especially equations12–15. Its engineered couplings reduce to a spin rotation. The positive-block loader adaptation, complete external-window estimate and inventory below are separate arguments; that paper is not evidence for them.

## 1. Installed finite clock and exact scalar identity

Let0<epsilon<=1, Lambda>0, and choose integer

 L >= max{296, ceil(4 log(16/epsilon))}.

Set Jstar=Lambda/40, alpha=2Jstar/(L+1), C=4Jstar, and

 kappa_r=alpha sqrt(r(L+1-r)), r=1,...,L.

Every kappa_r<=Jstar, since r(L+1-r)<=(L+1)^2/4. These are exactly supplied real positive coefficients. Minimum kappa=2Jstar sqrt(L)/(L+1); this coefficient scale is not a fabrication-tolerance theorem.

Shift the74 virtual positions of the global exact loader from0,...,73 to1,...,74. Attach one new left endpoint at0 on each of four rails, and identical right output chains at75,...,L. Use four identical finite scalar chains, including unused input rails, so the literal global gauge tensors with the full rail/data fiber. The supplied initial one-head state is at0, with the same rail/logical embedding as in the global source (selected a=1, arbitrary coherent b), arbitrary Q/P and R0. The new single left endpoint is adjacent to the first module. No weak emitter, momentum packet, spectral filter or timed preparation is assumed.

Use the structured family to set each virtual link to the corresponding kappa_r. At a diamond the outer physical arm bonds are a_L=kappa_left/sqrt2 and a_R=kappa_right/sqrt2, and the central contact parameter is g=kappa_middle. At a Hadamard mixer take t=kappa_link, hence physical bond weight t/sqrt2; at the permutation take t=kappa_link. Cables have their corresponding kappa. Within each layer repeat these parameters over all four rails and both required arms exactly.

Add one positive physical occupation potential to every head. If c_L,c_R are the adjoining cable weights, the diamond potentials are

 p_L=C-(2a_L+c_L), p_R=C-(2a_R+c_R),
 p_A=C-(a_L+a_R+g) equally on u and v.

Hadamard ports have p=C-(sqrt2 t+c); permutation ports p=C-(t+c). Ordinary sites have p=C-(kappa_left+kappa_right), with missing endpoint bond interpreted as zero. All are strictly positive: the largest subtracted expression is at most (sqrt2+1)Jstar<C. Identity-diamond u retains its separate2g occupation contact and v its zero contact, as in the structured source; p_A is added equally, not substituted for the identity contact.

The exact head-arm unitary A and ordered prefix gauge W consequently give, in the full one-head sector,

 (AW)* H (AW) = h_L tensor I,
 h_L=C I-sum_(r=1)^L kappa_r(|r><r-1|+|r-1><r|).

All other outputs are retained. The global output prefix is W_x=-U_f for x>=74, with U_f=I_a X_R C_P^(b) SWAP_QP and the exact ordered convention of the global source. External output begins at75. There is no additional mu phase: h_L includes its full constant C already. Before the gate the source gauge is identity. The two-body blocks are exactly those of the checked structured family, together with ordinary positive Q bonds and positive occupations on the added rays. No many-body gated hopping is installed.

## 2. Exact scalar solution

Identify |x> with the normalized symmetric weight-x vector of L auxiliary mathematical spins. This is an algebraic representation of an(L+1)-dimensional clock, not L extra installed qubits. Sum of their Pauli X operators has offdiagonal sqrt((x+1)(L-x)). Hence

 h_L=C I-alpha sum_(j=1)^L X_j

on that symmetric subspace. The factors commute, and exp(i alpha t X)|0>=cos(alpha t)|0>+i sin(alpha t)|1>. Expanding the tensor product and collecting equal-weight terms gives exactly

 f_x(t)=exp(-iCt) sqrt(binomial(L,x)) [i sin(alpha t)]^x [cos(alpha t)]^(L-x).

The coefficients retain their signs also when cos is negative. Their squared moduli sum to1 by the binomial identity. At T=pi/(2alpha), the endpoint amplitude is exp(-iCT)i^L and all other amplitudes vanish. This is exact common output phase, not its absolute value.

Define the closed finite window

 I=[pi/(3alpha), 2pi/(3alpha)]=[2T/3,4T/3].

For every t in I, p=sin^2(alpha t)>=3/4. The position distribution is Binomial(L,p). The bad event for external-only arrival is X<=74. Because L>=296, 74<=L/4; therefore X<=74 implies X-E X<=-L/2.

For completeness an elementary exponential estimate: for independent Bernoulli variables Y_j, the centered logarithmic moment generating function g_j(s)=log E exp[s(Y_j-EY_j)] has g_j(0)=g_j'(0)=0 and g_j''(s)<=1/4 (the tilted Bernoulli variance). Integrating twice gives g_j(s)<=s^2/8 for real s. Markov at s=-2 gives Pr[X-E X<=-L/2]<=exp(-L) exp(L/2)=exp(-L/2). Thus uniformly on I,

 q(t)=sum_(x=0)^74 |f_x(t)|^2 <= exp(-L/2).

This bound is on every source/interior/non-output amplitude together. No residual localized component, unnormalized filter or omitted apparatus is discarded.

## 3. Complete output and actual record

Let z_t be the positively normalized restriction of the exact scalar f(t) to75,...,L. Since 1-q>0, this is well-defined and includes exp(-iCt), i^x and the sign of cos. On these external coordinates A is identity and W=-U_f. Define the ideal complete output isometry to be -z_t tensor U_f with the fixed physical external-head embedding. The minus is part of the common phase.

For each normalized input, including arbitrary passive reference, orthogonal clock support gives squared vector error

 q+(1-sqrt(1-q))^2 = 2-2sqrt(1-q) <=2q.

In particular the looser bound2sqrt(q)<=2 exp(-L/4)<=epsilon/8 holds uniformly on I. This is an induced isometry-norm estimate on the full input subspace. The unhalved complete channel trace/diamond distance is at most twice that vector bound, hence<=epsilon/4. External success probability>=1-exp(-L/2)>=1-epsilon^2/256. At T the complete external transfer is exact.

The checked actual-record projection remains exact: after the coordinate shift its threshold is virtual73, mapping to the final antisymmetric physical arms, and then x>=74. Consequently the actual R1 branch has an input-independent common head profile and exactly U_f whenever its probability is nonzero. In the stated window its probability is at least the external success probability. The record event includes internal final arms/origin and does not certify external vacancy on its own. At other times it is still an exact logical branch but may be rare or absent. This applies only to the exact correlated coefficient family. There is no finite-device permanent halt: the finite coherent clock returns, and the logical prefix/record can be undone. No environment capture, irreversible readout, reset or reuse has been installed.

## 4. Full support loads, inventory and geometry

Use actual block norms, not scalar cancellations. A diamond endpoint's full incident load is4a+2c+p=C+2a+c <=(5+sqrt2)Jstar. An arm's load is2a_L+2a_R+2g+p_A=C+a_L+a_R+g <=(5+sqrt2)Jstar; identity v may be smaller. Hadamard ports have2sqrt2 t+2c+p=C+sqrt2 t+c <=(5+sqrt2)Jstar. Permutation ports have2t+2c+p=C+t+c<=6Jstar; ordinary sites have2(k_left+k_right)+p=C+k_left+k_right<=6Jstar. Endpoints satisfy the same bound. Q/P each have20 contacts of norm<=2Jstar, so load<=40Jstar=Lambda. R has8 contacts and load<=16Jstar. All supports thus obey Lambda. Each block is real positive and at most two-qubit. Total head vacuum energy remains zero for this construction, with no independent data Hamiltonian.

The fixed interior has296 head qubits and3 data qubits. It has392 head-head blocks,48 nontrivial contacts,20 separate identity occupations, total460 before the new296 compensating potentials. Its total is756. Exterior heads are four at0 and4(L-74) at75,...,L:4L-292. Their head-head bonds, including the first attaching bond, also number4L-292. Each has one occupation potential. Thus total

 heads=4(L+1), qubits=4L+7, blocks=8L+172.

This counting convention keeps identity contacts and added potentials separate; no old8 permutation mu terms are also included. Scalar auxiliary spins in section2 are not counted because they are not installed.

Reuse the explicit range18 embedding of the299 interior qubits in the7-by-7-by-7 cube from the global source. The eight reserved ports support disjoint vertical rays: four left rays of length1 and four right rays of length L-74. All new edges are nearest-neighbor along their rays; interior range remains18. This is a supplied bounded-range layout, not a nearest-neighbor implementation or a native Q/P hardware identification. Data contact degree remains20.

Taking the smallest allowed integer L gives sufficient size O(log(1/epsilon)) and time T=pi(L+1)/(4Jstar)=10pi(L+1)/Lambda. The entire window endpoints scale likewise. These are upper-bound recipes, not optimality or measured operating times. The minimum L296 has1191 qubits. The improvement relative to earlier sufficient recipes comes from an exactly engineered clock and exact gate identity; it does not show old scattering bounds were necessary.

## 5. Precision and open obligations

The required square-root couplings, paired signs, equality of rails/arms and compensating occupations are supplied exactly. This source does not derive them from native physical axioms. The structured-family perturbation lemma could be applied on a finite horizon only with its actual fixed-support, local-head-conservation, local-vacuum-annihilation, positivity and load-margin premises. It must not be invoked at Jstar=Lambda/40 without separately providing head/data load margin. Exact rare-event correctness is not robust to arbitrary small asymmetry; normalized rare branches require their own probability floor. No perturbative extension is asserted here.

Outstanding: distinct analytical check of this candidate; publication integration with frozen exact dependencies; comparison against the separately proposed uniform-chain finite bound; physically native coefficient/state supply; active historical dynamics; record-environment capture with proved transport; permanence/reset/reuse. No empirical prediction, formal retained audit, solver execution or editable prompt change is claimed.
