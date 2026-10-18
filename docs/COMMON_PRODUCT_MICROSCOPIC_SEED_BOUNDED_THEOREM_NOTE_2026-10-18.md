# A microscopic packet certificate for the finite seeded router

Claim status: bounded_theorem. Conditional mathematical result with distinct analytical checks of scattering, packet evolution, finite composition and simultaneous resource family, followed by source-exposed ROOT integration. No retained audit or native realization is asserted.

For every supplied incident-load cap \(\Lambda>0\) and \(0<\epsilon\le1\), the explicit family below has complete-output isometry error below \(3\epsilon/4\) throughout a relative-width \(1/6\) observation interval. Its size and dimensionless duration are \(\Theta(\epsilon^{-4})\), while its physical duration is \(\Theta(\Lambda^{-1}\epsilon^{-6})\). The change from the parent certificate is to compare the actual seeded device with an exact microscopic packet, thereby replacing the accumulated effective-cell approximation. These are sufficient bounds for an exact supplied family with very large constants, not optimal or practical resource claims.

## Positive device and complete-output contract

The physical architecture is the [parent certificate](COMMON_PRODUCT_REFINED_RESOURCES_BOUNDED_THEOREM_NOTE_2026-10-18.md)'s six-qubit program cell and two finite rays \(n=0,\ldots,M\). Write \(u=(L,0),v=(R,0)\), with mediator \(m\), program bits \(c_u,c_m,c_v\), head occupation \(n_x\), and lowering operator \(a_x=|0\rangle\langle1|\). Supply the full positive block
\[
Q_c(x,y)=c(n_x+n_y-a_x^\dagger a_y-a_y^\dagger a_x).
\]
Its double-occupation diagonal is \(2c\). The cell is
\[
\begin{aligned}
H_{\rm cell}={}&Q_b(u,m)+Q_b(m,v)+b(1-n_u)+b(1-n_v)\\
&+[(D_0-2b)P_{0,c_m}+(D_1-2b)P_{1,c_m}]n_m\\
&+2jP_{0,c_u}n_u+2jP_{0,c_v}n_v,
\qquad j=b^2/D_0,
\end{aligned}
\]
where \(D_1>D_0>2b>0\). The two ordinary rays contribute \(Q_j((r,n),(r,n+1))\) for \(0\le n\le M-2\); their outer blocks are
\[
B_r=Q_\gamma((r,M-1),(r,M))
 +(j-\gamma)n_{r,M-1}+(2j-\gamma)n_{r,M},
\quad0<\gamma<j.
\]
All terms are positive on their full supports. The outer block has norm \(3j\), and both outer one-head diagonals, including the inward bond at \(M-1\), are \(2j\). The parent nearest-neighbor placement, absent couplings and combined mediator-block convention are retained. No effective endpoint-to-endpoint bond is installed.

The supplied seed isometry \(E_{\rm seed}\) places one encoded path head at emitter \(M\), prepares every other head vacant, and encodes the logical program as \(|ppp\rangle\). Basis program/path inputs are occupation products. Arbitrary logical coherence and arbitrary passive-reference entanglement are allowed and supplied; they are not created from a basis product by this theorem.

Let \(\ell=M-1\) and
\[
C=|0\rangle\langle0|\otimes X+|1\rangle\langle1|\otimes I.
\]
The complete comparator is \(e^{-i2bt}J_{\rm out}(\beta_F(t)\otimes C\xi)\), where \(\beta_F(t)\) is one common normalized radial packet on \(0\le n\le\ell\). Its emitters and mediator are vacant and its encoded programs are unchanged. Every actual output coordinate is included in the norm; no actual output is projected, renormalized or traced away. The scalar \(2b\) is common on the full physical head space and all program sectors and is retained in the vector comparison.

## Exact microscopic scattering and normalized packet

Temporarily replace the finite source ends by uniform half-lines, retaining the actual mediator. On the one-head space the relative operator \(h=H-2bI\) is bounded and self-adjoint. No boundedness is asserted for an unrestricted infinite many-head sum. In program sector \(p\), its endpoint diagonal is \(j+a_p\), mediator diagonal \(D_p\), and endpoint/mediator hoppings \(-b\), with \(a_0=2j,a_1=0\).

For \(z=e^{ik}\), \(E(k)=2j(1-\cos k)\), and port projectors \(P_\pm=(I\pm X)/2\), elimination of the mediator gives
\[
v_+=a_p/j-\frac{2b^2}{j(D_p-E)},\quad v_-=a_p/j,
\qquad s(v;k)=\frac{1-v-z}{z^{-1}-1+v},
\]
\[
S_p=s(v_+;k)P_++s(v_-;k)P_-.
\]
The denominator has nonzero imaginary part in the open band and \(|s|=1\). The ideal scattering phase is \(zC\), not merely \(C\). Define the controlled matrices
\[
Q(k)=z^{-1}S(k),\qquad
R_p(k)=\frac{b}{D_p-E(k)}(1,1)(I+S_p(k)).
\]
For \(\eta=b/D_0\le1/8\), \(0<\zeta=D_0/D_1<1/2\), and \(k\in[\pi/3,2\pi/3]\), the checked components give, with \(\delta=\eta^2+\zeta\),
\[
\begin{gathered}
\|Q\|=1,\quad\|Q-C\|\le d_S=\max(13\eta^2,5\zeta),\\
\|Q'\|\le260\delta,\quad\|Q''\|\le4600\delta,
\quad\|R\|\le3\eta,\quad\|R'\|\le420\eta.
\end{gathered}
\]

Use the exact standalone source amplitude
\[
F(k)=-i\sqrt{2/\pi}\,\rho\,
 \frac{e^{ik}}{(2-\rho^2)\cot k-i\rho^2},\qquad \rho=\gamma/j.
\]
Fix a real cutoff: it is one for \(|k-\pi/2|\le\pi/24\), transitions by \(1-10x^3+15x^4-6x^5\), with \(x=(|k-\pi/2|-\pi/24)/(\pi/12)\), over the next width \(\pi/12\), and is zero beyond \(\pi/8\). Put \(p_\chi=\|\chi F\|_2^2\), \(g=\chi F/\sqrt{p_\chi}\), using the positive square root. Its exact source phase is retained. With \(G_r=\|g^{(r)}\|_1\), the checked derivative and spectral estimates give
\[
G_0<2,\quad G_1\le100/\rho,\quad G_2\le2000/\rho^3,
\quad B_-\le200/\rho,\quad P\le11\rho^2,\quad p_\chi>1/2
\]
for the parameter family below. The conservative velocities are \(v_{\min}=\sqrt3j,v_{\max}=2j\).

All packet integrals below are over \(0<k<\pi\). The exact microscopic packet has lead and mediator coordinates
\[
\begin{aligned}
\Psi_n(t)&=\frac1{\sqrt{2\pi}}\int g(k)
 [e^{i[(\ell-n)k-tE]}I+e^{i[(n+\ell+1)k-tE]}Q(k)]\xi\,dk,\\
\Psi_m(t)&=\frac1{\sqrt{2\pi}}\int e^{i[\ell k-tE]}R(k)g(k)\xi\,dk.
\end{aligned}
\]
The packet component proves exact strong evolution and \(\|\Psi(t)\|=\|\xi\|\) by incoming separation in the remote past and conservation of norm. This is a packet-specific isometry, not a completeness theorem. Bound states actually exist: there is a high symmetric bound state in both programs and a negative relative-energy bound state in the disabled program. Their absence is not assumed.

## Early finite seed match and exact outer residual

The finite proposal compares the actual relative generator with two independent standalone launchers on a common extended space. The launcher coordinate is \(x=\ell-n\), its emitter is \(M\), and its lead extends through negative radial coordinates. The reference mediator is isolated with the same \(D_p\) as the actual mediator. Decoupled exterior Dirichlet lines retain diagonal \(2j\).

The contact difference at \(0,-1,m\) consists of endpoint diagonal changes \(a_p-j=\pm j\), removed reference edges \(+j\operatorname{Adj}(0,-1)\), and the actual mediator hoppings. Hence
\[
\|V\|\le2j+\sqrt2b.
\]
The reference seed has zero mediator amplitude at all times, and its invariant launcher subspace has norm bound \(4j\), irrespective of \(D_p\). Reaching contact from \(M\) takes at least \(M\) steps. With \(u_0=jt_0\), ordered Duhamel therefore gives
\[
E_{\rm early}=\min\left\{2,
u_0(2+\sqrt2/\eta)\sum_{r=M}^\infty\frac{(4u_0)^r}{r!}\right\}.
\]
The large actual generator is used only through unitarity. Its norm is not replaced by \(4j\).

For clarity, the complete error envelopes are specified here. Define
\[
\begin{gathered}
H_0=G_0,\quad H_1=G_1+260\delta G_0,\quad
H_2=G_2+520\delta G_1+4600\delta G_0,\\
J_0=3\eta G_0,\quad J_1=3\eta G_1+420\eta G_0,\\
T_A(t,q)=\frac{A_1+(2j|t|/q)A_0}{\sqrt{2\pi}}
 \sqrt{q^{-2}+q^{-1}},\qquad
\mathcal M(t,q)=\frac{J_1/q+2j|t|J_0/q^2}{\sqrt{2\pi}}.
\end{gathered}
\]
Subscripts \(G,H\) choose the corresponding first two norms. The checked standalone launch error is \(2\delta_{\rm launch}\), where
\[
\delta_{\rm launch}=\sqrt{R_0^2+(L_0+2\sqrt P)^2},\quad
R_0=\min\{1,2j/(\pi\gamma^2t_0)\},\quad
L_0=\frac{B_-}{\sqrt{2\pi}}\sqrt{(t_0v_{\min})^{-2}+(t_0v_{\min})^{-1}}.
\]
Coordinate reversal identifies the launched packet with the positive normalization of the incoming Fourier state restricted to \(n\le\ell\). Put
\[
\begin{aligned}
d_{\rm right}&=T_G(t_0,1+t_0v_{\min}),\\
e_{\rm match}^2&=T_G(t_0,\ell+1-t_0v_{\max})^2
 +T_H(t_0,\ell+1-t_0v_{\max})^2+\mathcal M(t_0,\ell-t_0v_{\max})^2,\\
e_0&=E_{\rm early}+2\delta_{\rm launch}+2d_{\rm right}+e_{\rm match}.
\end{aligned}
\]
For positive displayed gaps, the actual finite state and \(\Psi(t_0)\) differ by at most \(e_0\). This is a full-vector bound: it pays all omitted spectral components without setting a bound-state weight to zero or equating finite and infinite spectral projections.

The outer perturbation on each port is exactly
\[
\Delta=(j-\gamma)\operatorname{Adj}(\ell,\ell+1)
       +j\operatorname{Adj}(\ell+1,\ell+2).
\]
It has contact norm \(d_{\rm hop}=\sqrt{(j-\gamma)^2+j^2}\), changes no diagonal, and has no mediator column. The infinite microscopic generator plus \(\Delta\) is the finite actual relative generator direct-summed with exterior Dirichlet lines. This identity avoids a Laplacian-edge-deletion mismatch.

Set \(q_i(t)=tv_{\min}-1\), \(q_o(t)=2\ell-tv_{\max}\), and
\[
\begin{aligned}
A_i&=G_2+(12j/v_{\min})G_1+(4j/v_{\min}+48j^2/v_{\min}^2)G_0,\\
A_o&=H_2+\frac{6jt_+}{q_o(t_+)}H_1
 +\left(\frac{2jt_+}{q_o(t_+)}+\frac{12j^2t_+^2}{q_o(t_+)^2}\right)H_0,\\
E_{\rm outer}&=\frac{\sqrt3d_{\rm hop}}{\sqrt{2\pi}}
 \left\{\frac{A_i}{v_{\min}}\left[\frac1{q_i(t_0)}-\frac1{q_i(t_+)}\right]
 +\frac{A_o}{v_{\max}}\left[\frac1{q_o(t_+)}-\frac1{q_o(t_0)}\right]\right\}.
\end{aligned}
\]
Twice integrating the packet boundary columns by parts and then integrating their residual gives this allowance uniformly from \(t_0\) through \(t_+\), provided \(t_0v_{\min}>2\) and \(t_+v_{\max}<2\ell-2\). The changed outgoing derivatives are included through \(H_1,H_2\); no effective-cell elapsed-time error is inserted.

## Final normalization and simultaneous certificate

Define
\[
\begin{gathered}
d_L=T_G(t_-,t_-v_{\min}-\ell),\quad m_L=\mathcal M(t_-,t_-v_{\min}-\ell),
\quad d_{\rm packet}=d_L+d_S+m_L,\\
n_O=T_G(t_+,2\ell+2-t_+v_{\max}),\qquad d_O=n_O/(1-d_{\rm packet}),\\
B_n(t)=\frac1{\sqrt{2\pi}}\int e^{i[(n+\ell+1)k-tE(k)]}g(k)\,dk,
\quad \beta_F(t)=\frac{P_{0\le n\le\ell}B(t)}{\|P_{0\le n\le\ell}B(t)\|}.
\end{gathered}
\]
If \(t_-v_{\min}>\ell\), \(d_{\rm packet}<1\) and \(d_O<1\), the denominator is positive throughout the window. Separate endpoint envelopes bound decreasing late incoming/mediator tails and the increasing outgoing tail; no monotonicity of their quotient is assumed. The complete bound is
\[
\boxed{\sup_{t_-\le t\le t_+}
\|e^{-itH_{\rm phys}}E_{\rm seed}
 -e^{-i2bt}J_{\rm out}(\beta_F(t)\otimes C)\|
\le\min\{2,e_0+E_{\rm outer}+2d_{\rm packet}+2d_O\}.}
\]
It is an isometry-norm statement, hence retains arbitrary passive references and coherent programs.

Choose exactly
\[
\begin{gathered}
\rho=\epsilon/256,\quad u_0=10^{12}\rho^{-2}\epsilon^{-2},\quad
\ell=\lceil100u_0\rceil,\quad M=\ell+1,\\
\eta^2=\epsilon/1024,\quad\eta>0,\quad\zeta=\epsilon/1024,\\
D_1=\Lambda/2,\quad D_0=\zeta D_1,\quad b=\eta D_0,
\quad j=b^2/D_0,\quad\gamma=\rho j,\\
t_0=u_0/j,\quad t_-=3\ell/(4j),\quad t_+=7\ell/(8j).
\end{gathered}
\]
All gaps above are positive: early matching gaps exceed \(\ell/2\), the late gap exceeds \(\ell/4\), and the outer gap is \(\ell/4\). In particular \(\eta\le1/32\), \(\delta\le1/512\), and
\[
H_1\le200/\rho,\quad H_2\le3000/\rho^3,\quad
J_0\le6\eta,\quad J_1\le1140\eta/\rho.
\]
The early tail must pay its microscopic \(u_0/\eta\) prefactor. Since \(M\ge100u_0\), the factorial estimate gives
\[
\sum_{r=M}^\infty(4u_0)^r/r!
\le(25/24)(4eu_0/M)^M<2\,8^{-M}\le2/M^2.
\]
The resulting twelve nonnegative allocations are:

| Contribution | Sufficient ceiling |
|---|---|
| Early actual/reference comparison | \(1/(100u_0\sqrt\epsilon)\) |
| Source residual \(2R_0\) | \(2\epsilon^2/10^{12}\) |
| Launch incoming term \(2L_0\) | \(400\epsilon/10^6\) |
| Spectral tails \(4\sqrt P\) | \(4\sqrt{11}\epsilon/256\) |
| Right early tail \(2d_{\rm right}\) | \(208\epsilon/10^6\) |
| Early lead matching | \(500\epsilon/10^7\) |
| Early mediator | \(2300\eta/(\rho\ell)\) |
| Integrated outer boundary | \((8200\cdot256/10^{12})\epsilon\) |
| Late incoming normalization \(2d_L\) | \(460\epsilon/10^7\) |
| Scattering discrepancy \(2d_S\) | \(26\epsilon/1024\) |
| Late mediator \(2m_L\) | \(10000\eta/(\rho\ell)\) |
| Finite output normalization \(2d_O\) | \(920\epsilon/10^7\) |

Each is below \(\epsilon/16\). The source verifies \(\delta_{\rm launch}<1\), \(d_{\rm packet}<3\epsilon/64<1/2\), and \(d_O<1\) before using the normalizations. The order-\(\eta\) mediator column is paid by its oscillatory integral, not discarded as a population. The total is below \(3\epsilon/4<\epsilon\). The unhalved channel discrepancy is below \(2\epsilon\); use accuracy argument \(\epsilon/2\) for channel tolerance \(\epsilon\), leaving the exponents unchanged.

## Load cap and same-metric comparison

The exact coefficients and duration are
\[
D_0=\frac{\Lambda\epsilon}{2048},\quad
b=\frac{\Lambda\epsilon^{3/2}}{65536},\quad
j=\frac{\Lambda\epsilon^2}{2097152},\quad
\gamma=\frac{\Lambda\epsilon^3}{536870912},\quad
t_+=\frac{7\ell}{8}\frac{2097152}{\Lambda\epsilon^2}.
\]
There are \(8+2\ell\) qubits and \(9+2\ell\) combined positive blocks. The incident sums \(D_1+2b\), \(3b+4j\), program loads \(2j,D_1-2b\), lead interior \(4j\), emitter-adjacent \(5j\), and emitter \(3j\) are all strictly below \(\Lambda\). Auxiliary comparison sites are not physical resources. No Hamiltonian switch occurs at any window endpoint.

The parent refined certificate and this certificate use the same complete-output isometry accuracy convention, supplied architecture, incident cap, input premises and relative width \((t_+-t_-)/t_-=1/6\):

| Quantity | Microscopic family | Refined parent |
|---|---|---|
| Size and \(jt_\pm\) | \(\Theta(\epsilon^{-4})\) | \(\Theta(\epsilon^{-4})\) |
| Physical \(t_\pm\) | \(\Theta(\Lambda^{-1}\epsilon^{-6})\) | \(\Theta(\Lambda^{-1}\epsilon^{-14})\) |
| Smallest supplied scalar \(\gamma\) | \(\Theta(\Lambda\epsilon^3)\) | \(\Theta(\Lambda\epsilon^{11})\) |

This is a comparison of sufficient parameter families, not a measured speedup of one fixed device. The smallest displayed positive scalar is \(\gamma\), by direct comparison with \(j,j-\gamma,b,D_0-2b\) and the other coefficients. Its magnitude is **not a precision tolerance, fabrication-error allowance, minimal eigenvalue or coefficient-production cost**. The constants \(10^{12}\), \(256^2\), and \(100\) remain in \(u_0\) and \(\ell\).

## Evidence, exposure and limits

The exact parent integration dependency is PR9703 head `bc63bf11de33a9c7919700c1fadb3a2816cccad2`, descending from parent9700. The refined source is `79f5bd9c07fe0eb0f37d051446f69759a32559ba7ce9e8bb835db01287188bb3`; finite-device source `3a195efcf8d5196ed54a74228033d0888e7f18c864e481ce61b2efea6c67992b` and review `5f5b1727a31df17facb9232e902c1d6985cd175058d66e54862ae614fef148a9` retain their scopes. The parent contains the scalar launch, derivative, positive-cell and fixed-diagonal boundary dependencies; none is replaced by an old processor runtime theorem.

The [portable evidence manifest](../outputs/common_product_microscopic_seed_2026_10_18/SOURCES.json) maps every source and scoped check below, including inherited parent dependencies:

- **Scattering source/check**: source `59b59ea3fc51e6ae364716a63ff4b9e001390cba112f48f0b4214c01318865a6`; distinct review `3e1dc92540af46ec3a20b928001c7796795bf6c6a6b8580fe307c3e3ca3f8eb6`.
- **Microscopic packet source/check**: source `c105226ebeead1f87bb11c6afcc8dadac59520401d5f8c0fa6dba4ba3ef90e4e`; distinct review `c27e7a93c6d76e8261d5a081c3af6ad94438aa803a69354dfb7d2e762e6e0234`.
- **Finite composition/check**: source `452231afa993c7a14e1b55c0b302d499e0284ce02266f8a1039a75474053392a`; distinct review `50148e56b0e38556f633cf225df82403b66d2e60c43f6391d355f84d6c4f2a51`, fully read and hash-verified during integration, supports the frozen composition at its stated conditional scope with no required correction. This source contains the complete extended generators, envelope derivations, twelve allocations and cap checks.
- **Inherited parent dependencies**: preserves the parent sources and reviews, including launch `fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4`, derivative `378086fdc6b217f9a2eb9d85fdb1ca862a54905be048d298465e0b123722fec8`, and physical cell `739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088`.

ROOT suggested microscopic elimination, packet-specific matching and candidate detuning choices. The note author also authored the finite composition, earlier launch/derivative/resource sources and reconstructed the twelve allocations. Component reviewers had access to proposed arguments and shared premises; the checks are not blind or model-diverse replication. ROOT integration and source bookkeeping are not additional independent science checks. The combined review reconstructs the operator identification, all twelve allocations, final normalization and sufficient scale; its analytical support is confined to the stated supplied mathematical model.

Exact positive interactions, coefficients and their correlations, occupation basis, role assignments, absent couplings, vacant-head preparation, and encoded program/input coherence are supplied. The theorem does not derive a native realization, implement the old literal processor, capture or reset the head, create stationary output or provide permanent halt. Finite returns remain possible after the observation interval. No timing-mixture, coherent-time-control or coefficient-robustness result is inferred here.

The evidence is analytical. No scientific executable, symbolic solver, dynamics simulation, parameter sweep or evaluated numerical operating point is claimed. ROOT read the full source arguments, scoped reviews and canonical note. Integration history and source identities are preserved in the portable packet; mechanical hash/link/graph checks do not constitute further scientific verification. No editable prompts or physical axioms changed.
