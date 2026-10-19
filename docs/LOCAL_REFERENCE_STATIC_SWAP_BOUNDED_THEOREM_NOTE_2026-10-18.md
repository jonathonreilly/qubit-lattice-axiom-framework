---
claim_id: local_reference_static_swap_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "Conditional static full-output SWAP on a supplied finite nearest-neighbor positive two-body chain with equal gaps, coherent product reference, degenerate Q and passive spectators. Includes the exact coherent gate, full-reference gap bound, complete leakage estimate, positive weighted-chain extension and simultaneous accuracy/load/window prescription. No native preparation, arbitrary active environment, autonomous stopping, full loader, energy-moment return or reuse is established."
upstream_dependencies: []
runner: scripts/local_reference_static_swap_2026_10_18.py
---

# A nearest-neighbor static SWAP with an active energy and a product reference

**Primary runner:** `scripts/local_reference_static_swap_2026_10_18.py`.

A static Hamiltonian of supplied positive one- and two-qubit blocks on the line

\[
Q-P-B_1-\cdots-B_N
\]

can approximate the full \(\operatorname{SWAP}_{QP}\) while retaining the literal active energy \(\omega n_P\). The input on \(Q,P\) is arbitrary and may be entangled with passive references. The additional reference begins in the supplied product \(\beta=|+\rangle^{\otimes N}\); every reference output remains in the comparison. A ferromagnetic reference chain replaces the growing-degree reference star of the intermediate construction.

The result is conditional on exact specified blocks, equal gaps, coherent product preparation, freely degenerate \(Q\), and the absence of additional interactions. It is a standalone SWAP, not the path/record loader or a realization of an arbitrary active old-system Hamiltonian \(H_{PE}\). It supplies a selected observation interval, not stopping, capture, reset or permanent halt. No native preparation or coefficient-synthesis result is asserted.

The local-chain proof and the intermediate star proof are reproduced below, together with the positive nonuniform-chain extension. The three complete source arguments remain live with exact original byte identities in the evidence map. Historical review labels are recovery provenance, not current scientific evidence. The portable primary supplies separate finite computational controls; the general bounds follow from the displayed proofs.

## The physical device and finite-window theorem

Fix \(\Lambda>\omega>0\), \(0<\epsilon\le1\), and write \(n=|1\rangle\langle1|\), \(\sigma^+=|1\rangle\langle0|\), \(\sigma^-=|0\rangle\langle1|\). Choose the following explicit parameters:

\[
\begin{aligned}
N&=\left\lceil512\pi^2/\epsilon^2\right\rceil,&
\kappa&=(\Lambda-\omega)/8,&
\Delta&=\kappa/N^2,\\
C_P&=(\sqrt5+3)/2+2\sqrt2,\\
\lambda_{\max}&=\min\left\{\omega/2,
\frac{\Lambda-\omega}{2C_P},\frac{\epsilon\Delta}{16384}\right\},\\
m&=\left\lceil\frac{\omega}{2\lambda_{\max}}\right\rceil,&
\lambda&=\frac{\omega}{2m},&
\tau&=\frac{\pi}{\lambda}=\frac{2\pi m}{\omega},\\
a&=\lambda/\sqrt2,&b&=\sqrt5\lambda/4,&c&=3\lambda/4,&g&=\sqrt2\lambda,\\
w&=\frac{\epsilon}{32(\omega+9\lambda/4)}.
\end{aligned}                                                    \tag{1}
\]

The symbols \(c\) and \(C_P\) are interaction coefficients and a dimensionless load constant, respectively. Install the separately listed blocks

\[
\begin{gathered}
a(I+X_Q),\quad b(I+Z_Q),\quad b(I+Z_P),\quad c(I+Z_QZ_P),\\
g\bigl(I+\sigma_P^+\sigma_{B_1}^-+\sigma_P^-\sigma_{B_1}^+\bigr),\\
\kappa(I-\operatorname{SWAP}_{B_jB_{j+1}}),\qquad 1\le j<N,\\
\omega n_P,\qquad \omega n_{B_j},\quad 1\le j\le N.
\end{gathered}                                                    \tag{2}
\]

These are ordinary full-support positive blocks. In particular, the exchange-plus-identity block has spectrum \(0,g,g,2g\), and each ferromagnetic block has spectrum in \(\{0,2\kappa\}\). All matrices are real. Their supports are onsite or nearest-neighbor on the stated line, whose maximum graph degree is two. No many-body projection is an installed interaction.

Let \(H\) be the sum of (2), and define

\[
s=a+2b+c+g,
\qquad
\beta(t)=\bigl(e^{-it\omega n}|+\rangle\bigr)^{\otimes N}.
\]

For the insertion \(E_\beta\psi=\psi\otimes\beta\), including arbitrary passive-reference identities, define the normalized complete-output comparator

\[
\mathcal B_t\psi
=e^{-i(st+\pi/4)}\operatorname{SWAP}_{QP}\psi\otimes\beta(t).
                                                                    \tag{3}
\]

The claimed conditional theorem is

\[
\sup_{t\in[\tau-w,\tau+w]}
\left\|e^{-itH}E_\beta-\mathcal B_t\right\|<\epsilon/8.               \tag{4}
\]

The norm is the complete induced vector norm, stabilized by any passive reference. It bounds the unhalved stabilized complete-output channel distance by \(\epsilon/4\). All \(N\) reference qubits are retained, including their actual deviations and correlations through the error bound. At \(t=\tau\), the reference comparator returns to \(\beta\), and a sharper vector ceiling is \(\epsilon/16\). Within the rest of the interval its free profile is explicitly \(\beta(t)\), not a frozen reference. No actual output is projected away or conditionally normalized.

There are exactly \(N+2\) physical qubits and \(2N+5\) nonzero positive blocks. Every incident sum of full-support block norms is below \(\Lambda\). At fixed \(\omega\) and positive margin \(\Lambda-\omega\), this particular sufficient prescription has

\[
N=\Theta(\epsilon^{-2}),\qquad
\tau=\Theta\bigl((\Lambda-\omega)^{-1}\epsilon^{-5}\bigr).             \tag{5}
\]

These are conservative analytical resource orders, with large constants, not optimal or practical times and not a precision-tolerance result. The half-width is \(\Theta(\epsilon/\omega)\); its relative size shrinks as \(\Theta(((\Lambda-\omega)/\omega)\epsilon^6)\). Selecting a time in this interval does not install a clock, record or stopping mechanism.

## Exact free energy and the comparison SWAP

Separate the actual operator as

\[
\begin{aligned}
H_E&=\omega\left(n_P+\sum_j n_{B_j}\right),\\
H_F&=\kappa\sum_{j=1}^{N-1}(I-\operatorname{SWAP}_{B_jB_{j+1}}),\\
H_S&=aX_Q+b(Z_Q+Z_P)+cZ_QZ_P,\\
V_{\rm loc}&=g(\sigma_P^+\sigma_{B_1}^-+\sigma_P^-\sigma_{B_1}^+),\\
W&=H_S+V_{\rm loc},\qquad H=H_E+sI+H_F+W.
\end{aligned}                                                       \tag{6}
\]

Every term of \(H_F+W\) commutes with \(H_E\). The reference swap preserves the sum of the two equal-gap occupations; the P-reference exchange preserves its two occupations in sum; \(Q\) is degenerate and all other P terms are diagonal. Consequently

\[
e^{-itH}=e^{-ist}e^{-itH_E}e^{-it(H_F+W)}.                            \tag{7}
\]

The positive shifts in \(H_F\) remain inside \(H_F\). Its symmetric-sector energy is exactly zero. Adding a further \(\kappa(N-1)\) scalar phase to the effective comparison would double count its identity terms without their compensating swaps.

The analytical two-data-qubit operator is

\[
H_{\rm eff}=a(X_Q+X_P)+b(Z_Q+Z_P)+cZ_QZ_P.                            \tag{8}
\]

It is not an additional physical transverse drive on charged P. On the singlet it has eigenvalue \(-3\lambda/4\). On the triplet basis \(|00\rangle,(|01\rangle+|10\rangle)/\sqrt2,|11\rangle\), the matrix \((H_{\rm eff}+cI)/\lambda\) is

\[
M=\begin{pmatrix}
(3+\sqrt5)/2&1&0\\
1&0&1\\
0&1&(3-\sqrt5)/2
\end{pmatrix}.
\]

Its trace is 3, principal-minor sum is \(-1\), and determinant is \(-3\), so

\[
\det(xI-M)=x^3-3x^2-x+3=(x-3)(x-1)(x+1).
\]

The triplet energies are \(-7\lambda/4,\lambda/4,9\lambda/4\), giving \(\|H_{\rm eff}\|=9\lambda/4\). At \(\tau=\pi/\lambda\) all triplet phases are \(e^{-i\pi/4}\), while the singlet phase is its negative. Therefore

\[
e^{-i\tau H_{\rm eff}}=e^{-i\pi/4}\operatorname{SWAP}_{QP}.            \tag{9}
\]

This is a full four-dimensional gate identity, not merely transfer of two basis states. The physical active energy need not commute with this comparison operator; the free factor will retain the necessary order.

## Symmetric reference sector and its full-space gap

Let \(\Pi\) project onto the fully symmetric reference subspace, tensored with identity on data and passive references, and set \(\Pi_\perp=I-\Pi\). The supplied \(\beta\) lies in \(\Pi\) and \(H_F\Pi=0\).

For a reference transposition \(S_{ij}\), with \(d=j-i\), an adjacent-transposition word has length \(2d-1\), using each intervening edge at most twice. For any such word,

\[
(U_1\cdots U_L-I)\psi
=\sum_{r=1}^L U_1\cdots U_{r-1}(U_r-I)\psi.
\]

Unitary prefixes, Cauchy-Schwarz, and \(\|(I-S)\psi\|^2=2\langle I-S\rangle_\psi\) give

\[
\langle I-S_{ij}\rangle_\psi
\le(4d-2)\sum_{e=i}^{j-1}\langle I-S_{e,e+1}\rangle_\psi.
\]

At an edge \(e\), the coefficient after summing pairs is at most \(4N e(N-e)\le N^3\). Hence the full-space quadratic-form inequality is

\[
\sum_{i<j}(I-S_{ij})\le N^3\sum_{e=1}^{N-1}(I-S_{e,e+1}).            \tag{10}
\]

With total spin \(\mathbf S=\sum_j(X_j,Y_j,Z_j)/2\), the identity \(S_{ij}=2\mathbf s_i\cdot\mathbf s_j+I/2\) yields

\[
\sum_{i<j}(I-S_{ij})=\frac{N(N+2)}4I-\mathbf S^2.
\]

Adding spin-1/2 representations gives maximal spin \(N/2\) precisely on the fully symmetric multiplet. Reducing it to the next possible spin \(N/2-1\) reduces \(S(S+1)\) by \(N\); lower spins reduce it further. The last operator is thus at least \(N\Pi_\perp\). Combining with (10),

\[
H_F\ge\Delta\Pi_\perp,\qquad \Delta=\kappa/N^2.                      \tag{11}
\]

This is a lower bound, not the exact chain gap. It applies to the full reference Hilbert space and remains valid with arbitrary data/reference tensor factors.

Permutation symmetry also gives

\[
\Pi\sigma_{B_1}^{\pm}\Pi=\frac1N\Pi\sum_j\sigma_{B_j}^{\pm}\Pi.
\]

Consequently the exact projected interaction is the reference star:

\[
\Pi W\Pi=\Pi(H_S+V_{\rm star})\Pi,
\qquad
V_{\rm star}=\frac gN\sum_j
(\sigma_P^+\sigma_{B_j}^-+\sigma_P^-\sigma_{B_j}^+).                  \tag{12}
\]

The right side preserves \(\Pi\). This identity on the entire symmetric sector does not presume that the actual single-boundary-exchange dynamics stays in it.

## Complete leakage estimate without an imported perturbation theorem

A finite-dimensional lemma supplies the needed comparison. Suppose \(A\Pi=0\), \(A\ge\Delta\Pi_\perp\), \(W=W^*\), \(\|W\|\le v\), and \(C=\Pi_\perp W\Pi\) obeys \(\|C\|\le c_*\). On the complementary space put \(D=\Pi_\perp(A+W)\Pi_\perp\). If \(d=\Delta-v>0\), then \(D\ge dI\).

For a normalized initial \(\xi\in\Pi\), write \(\psi(t)=e^{-it(A+W)}\xi=p(t)+q(t)\) with components in \(\Pi\) and \(\Pi_\perp\). The block equations imply

\[
q(t)=-i\int_0^t e^{-iD(t-u)}Cp(u)\,du,
\qquad \|p'(u)\|=\|\Pi W\psi(u)\|\le v.
\]

One integration by parts using \(D^{-1}\) bounds the two endpoints by \(2c_*/d\) and the integral by \(c_*vt/d\). Hence

\[
\|q(t)\|\le\frac{c_*}{d}(2+vt).
\]

The projected equation \(ip'=\Pi W\Pi p+C^*q\) then gives by Duhamel

\[
\|p(t)-e^{-it\Pi W\Pi}\xi\|
\le\frac{c_*^2}{d}(2t+vt^2/2).
\]

Thus the complete induced norm, with every leakage output retained, obeys

\[
\|e^{-it(A+W)}\Pi-e^{-it\Pi W\Pi}\Pi\|
\le\frac{c_*}{d}(2+vt)+\frac{c_*^2}{d}(2t+vt^2/2).                  \tag{13}
\]

The second exponential is interpreted on \(\Pi\). This proof requires no global upper bound on \(A\), no nondegenerate ground vector and no assumption about factorization of the actual state. It applies unchanged after passive-reference stabilization.

For the physical model, \(v=4\lambda\) is valid because \(a+2b+c+g<4\lambda\). Only the local exchange connects \(\Pi\) to its complement, so \(c_*=g=\sqrt2\lambda\) is valid. If \(\lambda\le\Delta/8\), then \(d\ge\Delta/2\). Substitution into (13) for \(0\le t\le2\pi/\lambda\) gives

\[
\|e^{-it(H_F+W)}\Pi-e^{-it\Pi W\Pi}\Pi\|
\le[2\sqrt2(2+8\pi)+16\pi+32\pi^2]\frac\lambda\Delta
<512\frac\lambda\Delta.                                           \tag{14}
\]

No omitted perturbation series or finite-volume remainder is used.

## Product-reference residual and closure of the window

On \(\beta\), \(\sum_jX_{B_j}\beta=N\beta\), while the vectors \(Y_{B_j}\beta\) are orthonormal. The exchange identity gives, for arbitrary data/passive-reference vectors,

\[
(V_{\rm star}-aX_P)(\psi\otimes\beta)
=\frac g{2N}Y_P\psi\otimes\sum_jY_{B_j}\beta,
\qquad
\|(V_{\rm star}-aX_P)E_\beta\|=\frac g{2\sqrt N}.                   \tag{15}
\]

The comparator \(e^{-itH_{\rm eff}}\psi\otimes\beta\) leaves the reference product fixed in this interaction representation. Equation (15) therefore holds at every point of that trajectory, even if Q and P become entangled. Duhamel yields the complete star-to-data comparison error \(gt/(2\sqrt N)\). It does not assume that the actual reference remains product or discard its correlations.

Combining (7), (12), (14) and (15), for the stated time range,

\[
\left\|e^{-itH}E_\beta-
 e^{-ist}[e^{-it\omega n_P}e^{-itH_{\rm eff}}]\otimes\beta(t)
\right\|
\le512\frac\lambda\Delta+\frac{gt}{2\sqrt N}.                       \tag{16}
\]

The notation in the middle denotes an input isometry, not multiplication by an unnormalized reference operator. The order of its data factors is essential.

The parameter policy (1) ensures \(512\lambda/\Delta\le\epsilon/32\). At \(\tau\), the entire free-energy evolution is identity because all its eigenvalues are integer multiples of \(\omega\). For \(t=\tau+u\),

\[
\|e^{-it\omega n_P}-I\|\le\omega|u|,
\qquad
\|e^{-itH_{\rm eff}}-e^{-i\tau H_{\rm eff}}\|
\le(9\lambda/4)|u|.
\]

Since \(w<\tau\), every time in the closed interval is positive and less than \(2\tau\). Its star residual is strictly less than \(\sqrt2\pi/\sqrt N\le\epsilon/16\), and the timing error is at most \(\epsilon/32\). Their sum with the leakage error is strictly below \(\epsilon/8\), proving (4). At the center the star ceiling is \(\epsilon/32\), giving the tighter \(\epsilon/16\) total bound. All phases in (3) are fixed; there is no fitted overall phase or scalar subtraction.

## Full-support resources and physical boundaries

The listed blocks total \((N-1)+1+4+(N+1)=2N+5\). The incident norm sums are

\[
\begin{aligned}
L_Q&=\lambda[\sqrt2+(\sqrt5+3)/2],\\
L_P&=\omega+C_P\lambda,\\
L_{B_1}&=\omega+2\kappa+2g,\\
L_{B_j}&\le\omega+4\kappa\quad(j\ge2).
\end{aligned}                                                       \tag{17}
\]

Endpoints have fewer chain terms. These counts use full local norms including every positive identity shift. The second entry of \(\lambda_{\max}\) makes \(L_P\le\omega+(\Lambda-\omega)/2\), and the Q coefficient is smaller. Interior reference loads have that same upper bound. For \(B_1\), the chain contribution is \((\Lambda-\omega)/4\), and \(2g\le\sqrt2(\Lambda-\omega)/C_P<(\Lambda-\omega)/2\). Thus all loads are below \(\Lambda\).

For fixed \(\omega\) and cap margin, \(N=\Theta(\epsilon^{-2})\) and \(\Delta=\Theta((\Lambda-\omega)\epsilon^4)\). As \(\epsilon\to0\), the last term of \(\lambda_{\max}\) dominates. The integer revival choice changes \(\lambda\) by at most a factor two, yielding (5). The other minima and ceilings in (1) are the nonasymptotic prescription.

The initial reference has free-energy mean \(N\omega/2\) and maximum \(N\omega\). Exact conservation of \(H_E\) balances input-dependent changes in P energy through the actual reference and correlations. Proximity in complete norm to \(\beta\) at the revival does not imply exact restoration of energy moments as the reference energy norm grows with N. Subsequent reuse requires a new proof.

The product coherence is supplied, not obtained from \(H_F\beta=0\). The reference ground subspace is degenerate; there is no cooling or initialization claim. The line is a genuine nearest-neighbor geometry within the stated supplied positive-two-body class, but no native material realization or suppression of stray couplings is established. Q remains freely degenerate, and a general active \(H_{PE}\) remains outside this theorem. There is no record qubit, head-clock, receiver, full loader transfer or halt guarantee. Genealogical PR ancestry does not provide any of those mathematical premises.

## Positive nonuniform chain weights

The reference-chain coefficients need not be equal. Replace the uniform chain by

\[
H_F=\sum_{j=1}^{N-1}\kappa_j(I-\operatorname{SWAP}_{B_jB_{j+1}}),
\qquad0<\kappa_{\min}\le\kappa_j\le\kappa_{\max}.
\]

Every positive bond separately kills the fully symmetric subspace. Their common kernel remains precisely that subspace, since adjacent swaps generate all permutations. Thus \(H_F\Pi=\Pi H_F=0\), even though the weighted sum generally is not invariant under arbitrary permutations outside its kernel. Equation (10) gives the full-space lower bound \(H_F\ge(\kappa_{\min}/N^2)\Pi_\perp\). The projection identity (12) depends on \(\Pi\), not on permutation invariance of the whole weighted operator. All hypotheses of (13) therefore remain valid with \(\Delta=\kappa_{\min}/N^2\).

For fixed \(0<\eta\le1\), take \(\kappa_{\max}=(\Lambda-\omega)/8\), \(\kappa_{\min}=\eta\kappa_{\max}\), and any individual weights in that interval. Use (1) with this new \(\Delta\). Equations (3)–(4), the center bound, counts and nearest-neighbor geometry hold unchanged. The reference loads are bounded using \(\kappa_{\max}\), and the gap using \(\kappa_{\min}\). There is no added scalar phase from the weighted chain, which remains intact with zero symmetric-sector energy. At fixed \(\eta,\omega\) and cap margin the sufficient time is \(\Theta([\eta(\Lambda-\omega)]^{-1}\epsilon^{-5})\).

Certified common bounds suffice; individual bond calibration or statistical cancellation is not needed. This covers scalar variation of the exact positive \(I-\operatorname{SWAP}\) blocks. It does not cover kernel-breaking matrix errors, unequal free gaps, inaccurate data coefficients or imperfect product coherence. The weighted-chain source (`outputs/local_reference_static_swap_review_2026_10_18/proofs/local_reference_chain_weights.md`) carries the complete extension; its historical check is preserved as a member of the exact original recovery archive.

## Live proofs and fresh finite controls

The three full mathematical sources are retained byte for byte. Their historical author/exposure statements describe their creation; they do not provide a new review or audit verdict. All mathematical premises are displayed above: exact supplied positive blocks, equal gaps, coherent product reference, degenerate Q, passive spectator identities, and no additional interactions. Genealogical ancestors supply no hidden loader theorem.

| Argument | Live source | Exact source SHA256 |
|---|---|---|
| local_reference_chain_weights | `outputs/local_reference_static_swap_review_2026_10_18/proofs/local_reference_chain_weights.md` | `7bae8b953e0bbb4435f9398029b42b081257b5c5b0edffc0d37ffb41152f8d5f` |
| local_reference_static_swap | `outputs/local_reference_static_swap_review_2026_10_18/proofs/local_reference_static_swap.md` | `9e68a0eb2f81955e900a23bd88b05321b75ea4e2741da89f812ef2eda59b5c70` |
| product_reference_static_swap | `outputs/local_reference_static_swap_review_2026_10_18/proofs/product_reference_static_swap.md` | `1a9e0ee47c8cc5b4f874abb2c8fa47258ee00fbe3cf77a87a2c968b407f0a825` |

The primary uses independent direct matrix assembly and analytic parameter checks accompanying these proofs. It checks the exact four-dimensional characteristic polynomial, complete coherent SWAP phase and phase mutant, full-space symmetric kernel/gap, complete-graph/path inequality, nonuniform positive weights, exact projected boundary exchange, full-input product-reference residual, physical block positivity/commutation/load, ordered free/scalar factors, complete leakage estimates and simultaneous policy across declared scalar fixtures. Numerical chains have N=2,3,4; the prescribed accuracy family can require vastly larger N and is established by the proof, not by pretending those matrices were simulated. The primary declares an enforced180-second cap, literal inputs and five honest resolution statements. A fresh capture is required after source confirmation.

Exact13original path versions, including the original canonical note, three checks, author manuscript and integration/validation records, are recoverable in `archive/local_reference_static_swap_review_2026_10_18/original-recovery.tar.gz`, with members and hashes in `archive/local_reference_static_swap_review_2026_10_18/MANIFEST.json`. The historical manuscript's relative links are not installed as live links; `outputs/local_reference_static_swap_review_2026_10_18/README.md` maps its provenance targets to current live proofs or archive members. Original check labels and generated citation graph are historical only; the graph is regenerated from integrated current source. No audit standing is assigned by this package.
