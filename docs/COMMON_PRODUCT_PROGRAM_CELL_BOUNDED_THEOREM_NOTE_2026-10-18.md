# A common endpoint product interface for an isolated program cell

Claim type: bounded_theorem. Conditional mathematical result with a distinct analytical source check and separate publication integration; no retained audit, native microscopic law or network implementation is asserted.

One supplied, fixed, positive Hamiltonian on six qubits supports an approximate programmed exchange/identity interface on the **same literal endpoint input with a vacant mediator**. The result covers all four endpoint occupation states, coherent superpositions and arbitrary passive references. Every physical output qubit is retained. The literal code is not invariant: mediator leakage is bounded rather than discarded.

For \(b>0\), \(D_1>D_0>2b\), and the exactly supplied correlation \(a_0=2b^2/D_0\), define
\[
r_0=\sqrt2 b/D_0,\quad
\epsilon_1=\frac{\sqrt{D_1^2+8b^2}-D_1}{2},\quad
r_1=\frac{\epsilon_1}{\sqrt2 b}
    =\frac{\sqrt2 b}{D_1+\epsilon_1},\quad
\beta_p=\frac{r_p}{\sqrt{1+r_p^2}}.
\]
For every \(|t|\le T\), the physical injection \(J\) specified below obeys
\[
\|e^{-itH}J-JU_{\rm tar}(t)\|
 \le \delta_T
 :=\max\{\min(2,2\beta_0),\min(2,2\beta_1+\epsilon_1T)\},
\]
where
\[
U_{\rm tar}(t)=e^{-i2bt}
 \left[|0\rangle\langle0|\otimes e^{-itQ_{a_0/2}}
       +|1\rangle\langle1|\otimes I_4\right].
\]
The common scalar phase \(e^{-i2bt}\) is part of the vector comparison, including the vacuum. This is an isolated supplied-cell result. It does not prepare program contents, derive native interactions, justify attaching neighboring cells or improve an existing apparatus certificate.

## The complete local Hamiltonian

Place dynamic head qubits at \(u=(-1,0,0),m=(0,0,0),v=(1,0,0)\), and program qubits at \(c_u=(-1,1,0),c_m=(0,1,0),c_v=(1,1,0)\). Let \(n=|1\rangle\langle1|\), \(P_0=I-n,P_1=n\), and \(a=|0\rangle\langle1|\). On head pairs use the full positive block
\[
Q_b(x,y)=b(n_x+n_y-a_x^\dagger a_y-a_y^\dagger a_x).
\]
Its one-head matrix is \(\begin{pmatrix}b&-b\\-b&b\end{pmatrix}\), its vacuum energy is0 and its double-occupation energy is \(2b\); its spectrum is \(0,0,2b,2b\).

Supply the single time-independent Hamiltonian
\[
\begin{aligned}
H={}&Q_b(u,m)+Q_b(m,v)+b(I-n_u)+b(I-n_v)\\
 &+[(D_0-2b)P_{0,c_m}+(D_1-2b)P_{1,c_m}]n_m\\
 &+a_0P_{0,c_u}n_u+a_0P_{0,c_v}n_v .
\end{aligned}
\]
Every term is positive on its entire support. All installed two-site terms are nearest-neighbor interactions on this patch; there is no directly installed \(u\)-\(v\) interaction. The absence of other geometrically adjacent interactions, site roles, occupation basis, coefficients and isolation are supplied premises.

Every program occupation and total head number commute with \(H\). The two legal program settings are the already supplied equal patterns000 and111. For any conserved pattern \(q\), let \(a_u=a_0(1-q_u)\), \(a_v=a_0(1-q_v)\), \(D=D_{q_m}\). Exact expansion gives
\[
H_q=2bI_8+a_un_u+Dn_m+a_vn_v
       -b(X_{h,um}+X_{h,mv}),\quad
X_{h,xy}=a_x^\dagger a_y+a_y^\dagger a_x .
\]
Thus \(2b\) is a true common scalar, not a one-head-only phase. Mixed programs have definite dynamics from this formula, but are not assigned the promised on/off interface.

For a legal program \(p\), put \(a=a_p\), with \(a_1=0\). After removing only \(2bI\), the one-head and two-head matrices are respectively
\[
h_1=\begin{pmatrix}a&-b&0\\-b&D&-b\\0&-b&a\end{pmatrix},
\qquad
h_2=\begin{pmatrix}a+D&-b&0\\-b&2a&-b\\0&-b&a+D\end{pmatrix}.
\]
Their bases are \((|100\rangle,|010\rangle,|001\rangle)\) and \((|110\rangle,|101\rangle,|011\rangle)\). Vacuum has relative energy0; triple occupation has energy \(2a+D\). Hard-core hopping retains coefficient \(-b\) in both matrices. Together with the general-pattern formula these specify all64 physical columns.

## Why all four endpoint states work

Write
\[
S=(|100\rangle+|001\rangle)/\sqrt2,\quad
A=(|100\rangle-|001\rangle)/\sqrt2,\quad M=|010\rangle,
\quad E=|101\rangle,\quad B=(|110\rangle+|011\rangle)/\sqrt2 .
\]
The symmetric one-head matrix on \((S,M)\) is
\(\begin{pmatrix}a&-\sqrt2b\\-\sqrt2b&D\end{pmatrix}\).
The symmetric two-head matrix on \((E,B)\) is
\(\begin{pmatrix}2a&-\sqrt2b\\-\sqrt2b&a+D\end{pmatrix}\).
The antisymmetric energies are \(a\) and \(a+D\).

Let \(\alpha_p=(1+r_p^2)^{-1/2}\). For enabled program000, the low vectors
\(f_0=\alpha_0S+\beta_0M\) and \(g_0=\alpha_0E+\beta_0B\) have energies0 and \(a_0\). Their symmetric high energies are \(D_0+a_0\) and \(D_0+2a_0\). The identity \(a_0D_0=2b^2\) makes the mixing angle exactly the same in both number sectors. The resulting auxiliary invariant dressed code realizes
\[
a_0R_-=Q_{a_0/2},\qquad
R_-=(n_L+n_R-X_{h,LR})/2.
\]
This is the full positive-\(Q\) action: the logical double-occupation energy is \(a_0\), not zero.

For disabled program111, the symmetric blocks coincide. Their low vectors \(f_1,g_1\) have relative energy \(-\epsilon_1\), the high energies are \(D_1+\epsilon_1\), and \(A\) has energy0. The auxiliary dressed code realizes \(-\epsilon_1R_+\), with
\(R_+=(n_L+n_R+X_{h,LR})/2\).
Both \(R_-\) and \(R_+\) are projectors on the entire four-state logical space and have double-occupation eigenvalue1. The negative relative energy is consistent with physical positivity: the common \(2b\) remains and \(\epsilon_1<2b^2/D_1<b\).

These dressed codes are proof devices, not prepared states. The actual injection in both programs is
\[
J_{\rm lit}|00\rangle=|000\rangle,\quad
J_{\rm lit}|10\rangle=|100\rangle,\quad
J_{\rm lit}|01\rangle=|001\rangle,\quad
J_{\rm lit}|11\rangle=|101\rangle.
\]
It tensors an arbitrary endpoint input with a vacant mediator. For an abstract program qubit,
\(J(|p\rangle\otimes\psi)=|ppp\rangle\otimes J_{\rm lit}\psi\).
Supplying equal classical contents, or a coherent state in this redundant program subspace, remains a preparation premise. This Hamiltonian does not copy or form those contents. Mathematical coherent program control does not by itself establish a framework Record interpretation.

## Full physical error and phase

For either auxiliary code, its distance from the literal injection is
\[
\|J_p^d-J_{\rm lit}\|=\sqrt{2-2\alpha_p}\le r_p.
\]
Only the symmetric one-head and double-head columns differ, in orthogonal number sectors; there is no four-column norm penalty.

The sharper direct calculation writes \(S=\alpha_pf_p-\beta_ph_p\), with \(h_p\) its orthogonal high mode, and uses the identical decomposition for \(E\). The complete enabled error is exactly
\[
\|e^{-itH_0}J_{\rm lit}
 -e^{-i2bt}J_{\rm lit}e^{-ita_0R_-}\|
 =2\beta_0|\sin((D_0+a_0)t/2)|.
\]
The double-head comparison includes its \(e^{-ia_0t}\) phase, so its gap is again \(D_0+a_0\). For the disabled branch, comparison first with its residual logical generator gives
\[
\|e^{-itH_1}J_{\rm lit}
 -e^{-i2bt}J_{\rm lit}e^{it\epsilon_1R_+}\|
 =2\beta_1|\sin((D_1+2\epsilon_1)t/2)|.
\]
The subsequent identity comparison costs \(2|\sin(\epsilon_1t/2)|\le\epsilon_1|t|\). The trivial distance cap2 for isometries completes the stated bound. Orthogonal conserved program sectors combine by a maximum.

No mediator output is traced away, postselected or renormalized. The literal subspace is not invariant: a symmetric endpoint input immediately couples to the mediator. The theorem bounds that physical discrepancy at every time in the claimed interval. It extends unchanged to passive references; the unhalved output trace or channel diamond discrepancy is at most \(2\delta_T\).

## Horizon and bounded-load resource convention

For \(0<\eta<2\), a sufficient condition is
\[
D_0\ge2\sqrt2 b/\eta,\qquad
D_1>\max\{D_0,(2\sqrt2b+2b^2T)/\eta\},
\]
together with \(D_0>2b\). Enabled error is bounded uniformly for all real times. Disabled identity has a finite-horizon guarantee; its nonzero \(R_+\) residual is not a removable common scalar.

There are six qubits and seven listed positive blocks when the two mediator program projectors are supplied as the **one combined positive block** displayed in \(H\). Splitting that block into two separately listed projectors gives eight blocks and different incident-norm bookkeeping. Under the combined convention, block norms are \(2b,2b,b,b,D_1-2b,a_0,a_0\), and
\[
\|H\|\le D_1+4b+2a_0.
\]
Incident norm sums are \(3b+a_0\) at \(u,v\), \(D_1+2b\) at \(m\), \(a_0\) at \(c_u,c_v\), and \(D_1-2b\) at \(c_m\). Since \(a_0<b\), the mediator load dominates. An incident cap \(\Lambda\) requires \(D_1+2b\le\Lambda\); an individual-block cap instead requires \(\max(2b,D_1-2b,a_0)\le\Lambda\).

One explicit sufficient bounded-load family, for any supplied \(\Lambda>0\) and \(0<\eta\le1\), is
\[
R=8\pi/\eta,\quad D_1=\Lambda/2,\quad D_0=D_1/R,\quad
b=D_0\eta/(8\sqrt2),\quad a_0=D_0\eta^2/64.
\]
It satisfies the exact tuning, \(D_1>D_0>2b\), and incident load \(D_1+2b<\Lambda\). Through
\[
T_{\rm gate}=\pi/a_0
 =\frac{1024\pi^2}{\Lambda\eta^3},
\]
enabled error is below \(\eta/4\), while disabled error is below
\(\eta/(4R)+\pi/R<\eta/2\). This is one sufficient symbolic family, not a numerical point, optimum, lower bound or free speed/precision gain. Its coefficients and exact correlations must be supplied. At this exchange time the one-head operation swaps endpoints, but double occupation receives phase \(-1\); the complete operation is not ordinary SWAP.

## Scope and evidence

The earlier six-qubit cell used different program-dependent dressed embeddings and program-dependent vacuum phases. It is contextual comparison only: no performance theorem from it supplies this result. The present proof removes that particular dressed-head preparation premise by establishing an approximate common literal injection. It does not provide an encoder, decoder, preparation procedure, exact disabled identity, native law or network compatibility.

Attaching other interacting cells may change low modes, gaps and leakage. No pending attachment theorem is imported, and these bounds do not authorize replacement of apparatus edges. An exactly independent environment may tensor its own evolution onto both sides; an interacting environment requires new work. A full initial joint trace error may be added by contractivity, but correct marginals alone are insufficient.

The two primary files, including their complete arguments and scope qualifications, are incorporated at exact identities:

| File | SHA256 |
|---|---|
| Common-product source (`outputs/common_product_program_2026_10_18/proofs/mediated_common_product_program__PROPOSAL.md`) | 739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088 |
| Distinct analytical check (`outputs/common_product_program_2026_10_18/proofs/mediated_common_product_program_check__REVIEW.md`) | 809a2083527cf942e6a6e879a6211600c9f144938915a43dbcf56d5680858fb6 |

ROOT proposed the algebraic route; the resources worker authored the source. I distinctly reconstructed all physical sectors, product-code error, phase and load scaling in the linked review, and authored this publication synthesis. Shared design exposure and mediator/positive-block ancestry are explicit; the check is not blind replication or a whole-ancestry audit. ROOT integration and portable packaging are recorded separately in the evidence packet.

No scientific or symbolic program, eigensolver, numerical dynamics, sweep or parameter search was run for this result or synthesis. The earlier cell's symbolic evidence is not validation of these new matrices. Native interactions, selected roles and absent couplings, occupation basis, coefficient supply, program/vacancy preparation, isolation and lawful Record interpretation remain premises. No existing apparatus certificate, permanent output, capture/reset or universal negative theorem is established. The source/check and publication integration have distinct recorded roles; no physical axiom or editable prompt is changed.

## Portable finite controls

Primary runner: `scripts/common_product_program_controls_2026_10_18.py` (timeout: 120 seconds). Its literal declared input closure includes all ten canonical notes and their live proof dependencies. It checks finite physical matrices, complete scattering and explicit sufficient budgets; finite controls corroborate these supplied conditional theorems and do not establish native realization or replace their analytical proofs. Historical statements above about what was executed describe original authorship; this added primary has a separate owner capture.
