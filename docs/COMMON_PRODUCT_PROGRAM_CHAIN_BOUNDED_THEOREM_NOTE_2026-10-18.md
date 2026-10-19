# A positive program chain with a common product mediator input

Claim type: bounded_theorem. Conditional mathematical result with a distinct analytical source check and separate publication integration. No retained audit, native Hamiltonian or algorithm implementation is asserted.

A finite chain of disjoint supplied six-qubit cells, joined only through their literal endpoint qubits, admits a complete finite-time comparison with a specified programmed logical Hamiltonian. The actual injection places every mediator in its vacuum and is the same in both legal settings of every cell. The statement covers arbitrary endpoint occupations, entanglement between cells, coherent legal programs and passive references. Every mediator and program output remains in the comparison.

The direct mathematical premise is the [isolated common-product program cell](COMMON_PRODUCT_PROGRAM_CELL_BOUNDED_THEOREM_NOTE_2026-10-18.md). Its full positive blocks, exact coefficient correlation and four-state dressed intertwiners are used below. Its isolated-cell error is not simply assumed to survive attachment: the network proof bounds the new local attachment residual explicitly. No pending generic attachment result or finite-mass source theorem is imported.

For \(N\ge1\), the physical chain has \(6N\) qubits and \(8N-1\) listed positive blocks under the combined mediator-block convention. Define the exact code distances and disabled residuals below. The main comparison is
\[
\left\|e^{-itH_{\rm net}}J-J e^{-itA_{\rm net}}\right\|
\le \delta_N(t)
:=\min\!\left\{2,\,
2\kappa_{\rm all}+|t|
\left[\sum_{i=1}^{N}\epsilon_i
       +4\sum_{i=1}^{N-1}c_i\kappa_{\{i,i+1\}}\right]\right\}.
\]
This holds for every real \(t\) as an upper bound; a useful guarantee is specified on a finite horizon. The target is the evolution of the whole logical Hamiltonian \(A_{\rm net}\), not a product of independent swaps or a demonstrated computation.

## The supplied physical chain

For cell \(i=1,\ldots,N\), place the three head qubits at
\[
u_i=(3i-1,0,0),\qquad m_i=(3i,0,0),\qquad
v_i=(3i+1,0,0),
\]
and its three program qubits one unit above these positions in the \(y\) direction. Different cells share no qubit. Let \(n=|1\rangle\langle1|\), \(P_0=I-n\), \(P_1=n\) and \(a=|0\rangle\langle1|\). The head exchange block is
\[
Q_b(x,y)=b(n_x+n_y-a_x^\dagger a_y-a_y^\dagger a_x).
\]
It is positive on the full two-qubit space, with spectrum \(0,0,2b,2b\). In particular its double-occupation energy is \(2b\), not zero.

Supply \(b_i>0\), \(D_{1,i}>D_{0,i}>2b_i\), and the exact correlation
\[
a_i=\frac{2b_i^2}{D_{0,i}}.
\]
The cell Hamiltonian is the translated parent construction
\[
\begin{aligned}
H_i={}&Q_{b_i}(u_i,m_i)+Q_{b_i}(m_i,v_i)
 +b_i(I-n_{u_i})+b_i(I-n_{v_i})\\
&+\big[(D_{0,i}-2b_i)P_{0,c_{m_i}}
       +(D_{1,i}-2b_i)P_{1,c_{m_i}}\big]n_{m_i}\\
&+a_iP_{0,c_{u_i}}n_{u_i}
  +a_iP_{0,c_{v_i}}n_{v_i}.
\end{aligned}
\]
Each displayed block is positive on its entire support. Install the additional bonds
\[
K_i=Q_{c_i}(v_i,u_{i+1}),\quad c_i\ge0,\qquad
H_{\rm net}=\sum_{i=1}^{N}H_i+\sum_{i=1}^{N-1}K_i .
\]
The external pair is a cubic nearest-neighbor pair because its two \(x\) coordinates are \(3i+1\) and \(3i+2\). All internal two-qubit supports remain nearest neighbors. Other geometrically adjacent pairs, including those in the program row, have no installed interaction. These omissions, roles, occupation frame and coefficient suppliers are explicit premises.

There is no time-dependent control. Every program occupation and total head number commute with the physical Hamiltonian. Each legal program triple is restricted to the supplied patterns000 or111. Mixed triples have physical dynamics under the displayed positive Hamiltonian, but are outside the promised logical interface.

## Common injection and the exact logical target

For each cell, the literal head injection sends
\[
|00\rangle\mapsto|000\rangle,\quad
|10\rangle\mapsto|100\rangle,\quad
|01\rangle\mapsto|001\rangle,\quad
|11\rangle\mapsto|101\rangle.
\]
It tensors an arbitrary two-endpoint state with a vacant mediator. For the abstract program bit, \(J_i(|p\rangle\otimes\psi)=|ppp\rangle\otimes J_{{\rm lit},i}\psi\), and \(J=\bigotimes_iJ_i\). The global input need not be a product between logical cells. Only the mediator-vacancy injection is fixed; supplying the endpoint/program joint state remains a separate premise.

On the full four-state endpoint space define
\[
R_{\mp,i}
=\frac{n_{L_i}+n_{R_i}\mp
(a_{L_i}^\dagger a_{R_i}+a_{R_i}^\dagger a_{L_i})}{2}.
\]
Both are projectors with double-occupation eigenvalue1. In the vacuum, symmetric one-head, antisymmetric one-head and double basis, \(R_-\) has eigenvalues \(0,0,1,1\) and \(R_+\) has eigenvalues \(0,1,0,1\).

With \(P_{p,i}\) now denoting the abstract program projection, set
\[
A_i=2b_iI+P_{0,i}a_iR_{-,i},\qquad
K_{{\rm log},i}=Q_{c_i}(R_i,L_{i+1}),\qquad
A_{\rm net}=\sum_iA_i+\sum_iK_{{\rm log},i}.
\]
The scalar \(2\sum_i b_i\) is retained on the entire logical space and every program setting, including vacuum. It contributes the common physical phase \(e^{-2it\sum_i b_i}\). No head-number or program-dependent phase is discarded.

Adjacent logical terms generally do not commute. “Disabled” removes that cell's internal \(a_iR_-\) term from the prescribed target; its external endpoint bonds remain present. The statement does not assert isolated identity evolution for a disabled cell inside the interacting chain. Even an isolated enabled cell at its one-head exchange time has a double-occupation phase \(-1\), so its full four-state operation is not ordinary SWAP.

## Tensor code distance on the full domain

Use the parent's auxiliary exact dressed isometry \(J_i^d\), only as a proof device. Define
\[
\epsilon_i=\frac{\sqrt{D_{1,i}^2+8b_i^2}-D_{1,i}}2,\qquad
r_{0,i}=\frac{\sqrt2b_i}{D_{0,i}},\qquad
r_{1,i}=\frac{\sqrt2b_i}{D_{1,i}+\epsilon_i},\qquad
\alpha_{p,i}=(1+r_{p,i}^2)^{-1/2}.
\]
The exact full-cell intertwiner is
\[
H_iJ_i^d=J_i^d\left(A_i-\epsilon_iP_{1,i}R_{+,i}\right).
\]
It includes the logical double-occupation column and the common \(2b_i\) scalar. The disabled residual is a full projector term, not a removable common phase. It satisfies \(\epsilon_i<2b_i^2/D_{1,i}\).

Within each legal program, the overlap \(J_i^\dagger J_i^d\) is positive diagonal in the full endpoint basis, with eigenvalues
\[
1,\ \alpha_{p,i},\ 1,\ \alpha_{p,i}.
\]
Since \(r_{1,i}<r_{0,i}\), its least eigenvalue on the legal program domain is \(\alpha_{0,i}\). For \(J^d=\bigotimes_iJ_i^d\),
\[
(J^d-J)^\dagger(J^d-J)
=2I-2\bigotimes_i(J_i^\dagger J_i^d).
\]
All minimal eigenvectors are available in the legal domain. Therefore the exact tensor distance is
\[
\kappa_{\rm all}
=\|J^d-J\|
=\sqrt{2-2\prod_i\alpha_{0,i}}
\le\sqrt{\sum_i r_{0,i}^2}.
\]
The last step uses \(1-\prod_i\alpha_i\le\sum_i(1-\alpha_i)\) and \(2(1-\alpha_{0,i})\le r_{0,i}^2\).

For an edge \(e=\{i,i+1\}\), the identical two-cell argument gives
\[
\kappa_e=\sqrt{2-2\alpha_{0,i}\alpha_{0,i+1}}
\le\sqrt{r_{0,i}^2+r_{0,i+1}^2}.
\]
These are operator-norm code distances, not observed leakage probabilities. Entangled inputs and passive references do not alter them. No four-column or whole-chain penalty is inserted into a two-cell distance.

## Local residual and complete evolution

An external bond touches only literal endpoint qubits. It thus exactly intertwines the two-cell literal injection:
\[
K_eJ_e=J_eK_{{\rm log},e},\qquad
\|K_e\|=\|K_{{\rm log},e}\|=2c_e.
\]
This equality holds on the full endpoint/program domain, including the external bond's double-occupation diagonal. Subtract it from the dressed expression:
\[
K_eJ_e^d-J_e^dK_{{\rm log},e}
=K_e(J_e^d-J_e)-(J_e^d-J_e)K_{{\rm log},e}.
\]
Its norm is at most \(4c_e\kappa_e\). Tensoring the remaining dressed isometries preserves that norm. The error is therefore charged to the two incident cells, rather than to the entire interaction norm times the entire chain's code distance.

The exact cell residuals and the local edge bounds give
\[
\|H_{\rm net}J^d-J^dA_{\rm net}\|
\le \sum_i\epsilon_i+4\sum_ec_e\kappa_e.
\]
This does not presume that attachments preserve the dressed subspace; generally they do not. It uses neither commutation of neighboring logical terms nor a one-head restriction.

Rectangular Duhamel bounds the evolution discrepancy through \(J^d\) by \(|t|\) times this residual. Replacing \(J^d\) by the actual \(J\) at each end costs \(\kappa_{\rm all}\) twice. Both complete comparison maps are isometries, giving the cap2 and the displayed main bound.

All physical mediator and program outputs are retained. The statement pays deviations from the literal code rather than asserting exact output vacancy or reset. Tensoring a passive reference preserves the norm; the corresponding unhalved output trace or complete-channel diamond discrepancy is at most \(2\delta_N(t)\). Correct separate input marginals are insufficient to establish the required joint preparation.

## Positive-block counts and physical load

Each cell contributes seven listed positive blocks when its two mediator program projectors are combined into the single positive two-qubit block displayed in \(H_i\). With \(N-1\) external bonds this gives \(8N-1\) listed blocks and \(6N\) physical qubits. Zero blocks may be omitted. Splitting the mediator block into separately counted projectors changes the listed norm accounting; the convention here is explicit.

For identical cell parameters \(b,D_0,D_1,a=2b^2/D_0\), let \(c_i=za\) for a fixed supplied \(z\ge0\). Each endpoint touches at most one external bond. The actual incident block-norm sums are

| Physical qubit | Incident norm sum or upper bound |
|---|---:|
| Cell mediator | \(D_1+2b\) |
| Endpoint | \(3b+a+2za\) |
| Endpoint program bit | \(a\) |
| Mediator program bit | \(D_1-2b\) |

The total listed block-norm sum is at most
\[
N(D_1+4b+2a)+2(N-1)za.
\]
These are physical interaction loads, not effective logical strengths.

Put \(r=\sqrt2b/D_0\). At the reference horizon \(T=\pi/a\), the preceding bounds imply the uncapped sufficient error envelope
\[
2\sqrt N\,r
 +4\sqrt2\pi z(N-1)r
 +N\pi D_0/D_1.
\]
The same envelope bounds every \(|t|\le T\). Naming this an exchange-scale horizon does not turn \(e^{-itA_{\rm net}}\) into independent cell operations.

## One sufficient family under an incident-load cap

For any supplied \(\Lambda>0\) and desired \(0<\eta\le1\), take
\[
\begin{gathered}
L=1+2\sqrt2\pi z,\qquad R=16\pi N/\eta,\\
D_1=\Lambda/2,\qquad D_0=D_1/R,\qquad
r=\frac{\eta}{16NL},\\
b=\frac{rD_0}{\sqrt2},\qquad a=r^2D_0,\qquad c_i=za.
\end{gathered}
\]
The exact tuning \(aD_0=2b^2\) holds. Since \(r\le1/16\) and \(R>1\), \(D_1>D_0>2b\). The mediator incident load satisfies
\[
D_1+2b=D_1+\sqrt2rD_0<\Lambda.
\]
For endpoints, divide the incident bound by \(D_0\):
\[
\frac{3b+a+2za}{D_0}
=\frac{3r}{\sqrt2}+(1+2z)r^2<1.
\]
Indeed the three terms are bounded by \(3/(16\sqrt2)\), \(1/256\) and \(1/(256\sqrt2\pi)\), using \(L\ge1\) and \(2z\le L/(\sqrt2\pi)\). Thus endpoint loads are below \(D_0<\Lambda\); both kinds of program-bit loads are also below \(\Lambda\). The large detuning has not been left outside the cap.

The first two error contributions obey
\[
2\sqrt N\,r+4\sqrt2\pi z(N-1)r
\le2NLr=\eta/8.
\]
The disabled residual contribution is strictly below
\[
N\pi D_0/D_1=N\pi/R=\eta/16.
\]
Consequently the complete norm discrepancy is strictly below \(3\eta/16<\eta\) throughout
\[
|t|\le T,\qquad
T=\frac{\pi}{a}
=\frac{8192\pi^2N^3L^2}{\Lambda\eta^3}.
\]
Strictness follows from \(\epsilon<2b^2/D_1\). For \(N=1\) the external bonds disappear and the family remains valid, though loose.

This is one exact symbolic sufficient family, not a numerical point, benchmark, optimum or lower bound. It changes the supplied coefficients with \(N,\eta,z\), including the shrinking endpoint compensation and external bonds. Exact correlations and their precision remain premises. No achieved physical timescale, algorithmic speedup or robustness to independent coefficient errors follows.

## What the network result establishes

The new conclusion is a complete finite-chain comparison for disjoint cells with endpoint-only attachments and a common vacant-mediator injection. It goes beyond isolation through the explicit local residual proof. It does not prove compatibility for bonds to mediators, overlapping cells, shared codes, additional onsite terms or unspecified interacting environments.

The logical many-body Hamiltonian is explicitly prescribed and generally noncommuting. This theorem does not identify its evolution with a desired algorithm, provide a universal compiler, replace the old calibrated processor or transfer an emitted-packet apparatus certificate. It neither prepares the legal program contents nor identifies them with native framework Records.

Supplied block shapes, local roles, absent couplings, occupation frame, correlated coefficients and endpoint/program preparation remain physical assumptions. There is no decoder, measurement procedure, capture, permanent halt, reset or reuse theorem. The comparison retains all outputs and the exact common phase over the stated finite horizon.

## Exact evidence and exposure

The publication mapping for the complete source argument and its distinct analytical reconstruction is:

| File | SHA256 |
|---|---|
| Network source (`outputs/common_product_program_2026_10_18/proofs/mediated_program_network__PROPOSAL.md`) | 1d830ee1638794876d2a5062f436be9e32b484fef0c79de095aa54d16c0e5edc |
| Distinct network check (`outputs/common_product_program_2026_10_18/proofs/mediated_program_network_check__REVIEW.md`) | 4e6e229f5cbc92321f72bf71289ed8f911c7663773e3731fa0ab54997f22db77 |
| Direct cell source (`outputs/common_product_program_2026_10_18/proofs/mediated_common_product_program__PROPOSAL.md`) | 739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088 |
| Distinct cell check (`outputs/common_product_program_2026_10_18/proofs/mediated_common_product_program_check__REVIEW.md`) | 809a2083527cf942e6a6e879a6211600c9f144938915a43dbcf56d5680858fb6 |

ROOT authored the network proof. Its distinct reviewer authored the common-product cell and the provisional generic attachment proposal; that exposure is disclosed in the review. The cell's separate analytical check is reused at its exact four-state scope. The network proof itself supplies the attachment residual and does not depend on acceptance of the provisional generic attachment.

For this synthesis I read both complete network files, the complete cell source and check, and the isolated-cell publication draft. I previously authored an earlier, different dressed-code cell and share mediator/positive-block ancestry; this drafting is not another independent mathematical check. The linked reviews provide selective conditional support, not blind replication or an audit of all ancestral premises. Historical pending labels inside the original source remain unchanged.

No scientific or symbolic program, numerical dynamics, solver, sweep or parameter search was run for this network result or publication synthesis. The older cell's symbolic evidence is not evidence for these new network calculations. ROOT publication integration and portable packet verification are recorded separately. No physical axiom or editable prompt is changed.

## Portable finite controls

Primary runner: `scripts/common_product_program_controls_2026_10_18.py` (timeout: 120 seconds). Its literal declared input closure includes all ten canonical notes and their live proof dependencies. It checks finite physical matrices, complete scattering and explicit sufficient budgets; finite controls corroborate these supplied conditional theorems and do not establish native realization or replace their analytical proofs. Historical statements above about what was executed describe original authorship; this added primary has a separate owner capture.
