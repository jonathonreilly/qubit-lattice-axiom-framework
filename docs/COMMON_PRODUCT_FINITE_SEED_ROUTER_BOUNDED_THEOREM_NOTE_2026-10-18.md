# A finite positive controlled router from endpoint seeds

Claim type: bounded_theorem. Conditional mathematical result with a distinct analytical composition check and source-exposed publication integration. No retained audit or native physical realization is asserted.

A supplied, static, positive Hamiltonian on finitely many qubits can approximate the controlled path operation
\[
C=|0\rangle\langle0|\otimes X+|1\rangle\langle1|\otimes I
\]
from two endpoint seed positions. The input contains one encoded head and vacant remaining head sites. At a specified finite time the comparison output has a common normalized radial packet, unchanged legal program contents, and vacant emitters and mediator. The bound includes every physical output and arbitrary passive references.

This is a coherent encoded-path router. It is not the old literal processor operation, a compiler, permanent halt or a native microscopic construction. Exact local blocks, coefficient correlations, site roles, absent interactions and encoded input preparation remain supplied.

## The complete positive finite device

Write \(n=|1\rangle\langle1|\), \(P_0=I-n\), \(P_1=n\), \(a=|0\rangle\langle1|\), and
\[
Q_c(x,y)=c(n_x+n_y-a_x^\dagger a_y-a_y^\dagger a_x).
\]
This full two-qubit block is positive, with spectrum \(0,0,2c,2c\); its double-occupation diagonal is retained. Put \(b>0\), \(D_1>D_0>2b\), \(j=b^2/D_0\), and \(a_0=2j\). The six-qubit cell has head sites \(u,m,v\), program sites \(c_u,c_m,c_v\), and Hamiltonian
\[
\begin{aligned}
H_{\rm cell}={}&Q_b(u,m)+Q_b(m,v)+b(I-n_u)+b(I-n_v)\\
&+[(D_0-2b)P_{0,c_m}+(D_1-2b)P_{1,c_m}]n_m\\
&+a_0P_{0,c_u}n_u+a_0P_{0,c_v}n_v.
\end{aligned}
\]
The legal program subspace is \(|p\rangle\mapsto|ppp\rangle\), \(p=0,1\). The effective enabled central bond is \(Q_j(u,v)\), while the disabled comparator is zero. The microscopic cell contributes the same scalar \(2b\) at every head position. No direct \(u\)-\(v\) bond is physically installed.

Take an integer \(M\ge3\), set \(\ell=M-1\), and attach a ray \(n=0,\ldots,M\) to each endpoint, identifying \((L,0)=u\), \((R,0)=v\). The two emitters are \((r,M)\). Choose \(0<\gamma<j\) and supply
\[
\begin{aligned}
H_{\rm phys}&=H_{\rm cell}+K,\\
K&=\sum_{r=L,R}\left[\sum_{n=0}^{M-2}Q_j((r,n),(r,n+1))+B_r\right],\\
B_r&=Q_\gamma((r,M-1),(r,M))
 +(j-\gamma)n_{r,M-1}+(2j-\gamma)n_{r,M}.
\end{aligned}
\]
Every displayed block is positive on its full support. \(B_r\) has norm \(3j\). Its inward neighbor bond makes both outer one-head diagonals exactly \(2j\), while their hopping is \(-\gamma\). This compensation is essential: weakening or deleting full Laplacian edges would give different diagonals and a different source.

The source cell occupies \(u=(-1,0,0),m=(0,0,0),v=(1,0,0)\), with program sites one lattice step above; straight outward rays realize all added nearest-neighbor supports. Head number and program occupations are conserved. The theorem uses the one-head sector, on which \(\|K\|\le4j\); it makes no infinite-many-head boundedness claim.

The input isometry \(E_{\rm seed}\) places the logical path head at its emitter, encodes the program as \(|ppp\rangle\), and leaves all other heads vacant. Basis program/path inputs are product occupation seeds. Arbitrary coherent or reference-entangled encoded inputs are allowed; their coherence is supplied and is not called a product across the two emitter sites.

## A common packet fixed by the source

The equal-diagonal half-line source has the checked complete spectral probability density
\[
\begin{gathered}
E(k)=2j(1-\cos k),\quad A=2j-\gamma^2/j,\quad d=\gamma^2/j,\\
D(k)=A^2\cos^2k+d^2\sin^2k,\qquad
w(k)=\frac{2\gamma^2\sin^2k}{\pi D(k)},\quad 0<k<\pi,\\
u(k)=e^{ik}\frac{d\sin k-iA\cos k}{\sqrt{D(k)}},\qquad
g_+=u\sqrt w,\quad g_-=\overline u\sqrt w.
\end{gathered}
\]
Here \(\int w=1\), \(|u|=1\), and \(\|g_\pm\|_2=1\). These are reference-source facts, not spectral claims about the finite router.

Choose \(0<\sigma<\sigma'<\pi/3\) and a real \(\chi\in C_c^2((0,\pi))\), with \(0\le\chi\le1\), equal to one on \(|k-\pi/2|\le\sigma\), and supported in \(|k-\pi/2|<\sigma'\). Define
\[
\begin{gathered}
p_\chi=\|\chi g_+\|_2^2>0,\qquad g=\chi g_+/\sqrt{p_\chi},\qquad
G_r=\|g^{(r)}\|_1\ (r=0,1,2),\\
v_-=2j\cos\sigma',\qquad v_+=2j,\qquad
P=\min\!\left(1,\frac{4\gamma^2}{\pi A^2\tan\sigma}\right).
\end{gathered}
\]
The cutoff is an analytical target choice, not a time-dependent control. All derivative norms retain their actual dependence on \(\gamma/j\) and \(\chi\).

At the specified observation time \(t_f\), put
\[
B_n=\frac1{\sqrt{2\pi}}\int_0^\pi
 e^{i[(n+\ell+1)k-t_fE(k)]}g(k)\,dk,
\qquad
\beta_F=\frac{P_{0\le n\le\ell}B}{\|P_{0\le n\le\ell}B\|}.
\]
The conditions below ensure a nonzero denominator; normalization is positive real. The translation phase \(e^{ik\ell}\), scattering phase \(e^{ik}\), and entire dispersion phase are retained. \(\beta_F\) is the same for both programs and paths. The target excludes the emitter sites \(n=M\).

## Complete finite-time error

The following explicit quantities give a sufficient bound. For \(t\ge0,z>0\), define
\[
\mathcal T(t,z)=\frac{G_1+2jtG_0/z}{\sqrt{2\pi}}
                 \sqrt{z^{-2}+z^{-1}}.
\]
Choose an early comparison time \(0<t_0\le t_f\), requiring
\[
t_0v_->2,\qquad \ell+1-t_0v_+>0,\qquad
t_fv_->\ell,\qquad t_fv_+<2\ell-2.
\]
Define the source and early-tail allowances
\[
\begin{aligned}
R_0&=\min(1,2j/(\pi\gamma^2t_0)),\\
L_0&=\frac{\|(\chi g_-)'\|_1+(2j/v_-)\|\chi g_-\|_1}{\sqrt{2\pi}}
       \sqrt{(t_0v_-)^{-2}+(t_0v_-)^{-1}},\\
\delta_{\rm launch}&=\sqrt{R_0^2+(L_0+2\sqrt P)^2}<1,\\
e_{\rm early}&=\min\left(2,2\sum_{m=M+1}^{\infty}\frac{(4jt_0)^m}{m!}\right),\\
e_0&=e_{\rm early}+2\delta_{\rm launch}
  +2\mathcal T(t_0,1+t_0v_-)
  +\sqrt2\,\mathcal T(t_0,\ell+1-t_0v_+).
\end{aligned}
\]
For the boundary allowance, set
\[
\begin{aligned}
q_i(t)&=tv_--1,\qquad q_o(t)=2\ell-tv_+,\\
A_i&=G_2+(12j/v_-)G_1+(4j/v_-+48j^2/v_-^2)G_0,\\
A_o(t)&=G_2+(6jt/q_o(t))G_1
 +(2jt/q_o(t)+12j^2t^2/q_o(t)^2)G_0,\\
\mathcal B(t)&=\frac1{\sqrt{2\pi}}\left\{
 \frac{A_i}{v_-}\left[\frac1{q_i(t_0)}-\frac1{q_i(t)}\right]
 +\frac{A_o(t)}{v_+}\left[\frac1{q_o(t)}-\frac1{q_o(t_0)}\right]\right\},\\
e_{\rm boundary}(t)&=\sqrt{3((j-\gamma)^2+j^2)}\,\mathcal B(t).
\end{aligned}
\]
Use \(e_{\rm boundary}=e_{\rm boundary}(t_f)\) in the pointwise bound. This is the checked closed rational envelope of the integrated twice-IBP bound
\(G_2/q^2+6jtG_1/q^3+2jtG_0/q^3+12j^2t^2G_0/q^4\).
All denominators are positive in the stated window.

The final incoming and discarded-output tails obey
\[
d_{\rm late}=\mathcal T(t_f,t_fv_--\ell)<1,\qquad
d_{\rm out}=\frac{\mathcal T(t_f,2\ell+2-t_fv_+)}{1-d_{\rm late}}<1.
\]
These conditions ensure \(\beta_F\) is defined. They pay both output emitters and every exterior target coordinate when the packet is truncated.

For the physical cell, put
\[
\begin{gathered}
\epsilon_1=\frac{4b^2}{\sqrt{D_1^2+8b^2}+D_1},\quad
r_0=\sqrt2b/D_0,\quad r_1=\sqrt2b/(D_1+\epsilon_1),\\
\kappa=\max_{p=0,1}\sqrt{2-2/\sqrt{1+r_p^2}},\qquad
e_{\rm cell}=\min\{2,2\kappa+t_f(8j\kappa+\epsilon_1)\}.
\end{gathered}
\]
Then the theorem gives the induced isometry bound
\[
\boxed{\left\|e^{-it_fH_{\rm phys}}E_{\rm seed}
 -e^{-i2bt_f}J_{\rm out}(\beta_F\otimes C)\right\|
 \le \min\{2,e_{\rm cell}+e_0+e_{\rm boundary}
                         +2d_{\rm late}+2d_{\rm out}\}.}
\]
Here \(J_{\rm out}\) includes unchanged encoded programs and vacant mediator and emitters. The common physical scalar \(e^{-i2bt_f}\) is compulsory. All actual leakage remains in the norm. No output is postselected or physically renormalized. Passive-reference extension preserves the bound; unhalved channel/trace discrepancy is at most twice its right side, capped by two.

## Why the composition has these terms

The checked standalone source evolves exactly into its residual emitter amplitude plus outgoing and incoming Fourier components. Its source residual is at most \(R_0\); the cutoff and nonstationary incoming tail give \(\delta_{\rm launch}\). Two identical launchers preserve arbitrary encoded path/program/reference input with no branch-dependent phase.

The finite ideal router differs from those reference launchers only at the central junction. A head starting at \(M\) cannot detect that change before the \((M+1)\)-st Hamiltonian power, giving \(e_{\rm early}\). Reversing the source coordinate \(x=M-1-n\) produces the phase distance \(\ell=M-1\). A full-integer Fourier comparison, followed by the exact normalized ideal-router state, gives the two remaining terms in \(e_0\). This pays preparation mismatch before using scattering.

The exact ideal scattering matrix is \(S_p(k)=e^{ik}[(1-p)X+pI]\). To compare it with the finite equal-diagonal device, change only the hoppings at \((M-1,M)\) and \((M,M+1)\). The perturbation norm is \(\sqrt{(j-\gamma)^2+j^2}\). Twice integrating its ideal boundary amplitudes by parts and then applying ordered Duhamel gives \(e_{\rm boundary}\). This controls the full changed evolution during the window; it does not assume returned waves vanish.

The final unwanted incoming component costs \(2d_{\rm late}\) after normalization. Normalized truncation to ordinary sites costs \(2d_{\rm out}\). Finally, the exact literal-code attachment identity \(KJ=JK_{\rm log}\), with \(\|K\|\le4j\), gives the cell residual for **all of the elapsed time \(t_f\)**. Dressed vectors are proof devices, not prepared inputs. Reference atom absence is never assigned to the finite graph.

## Ordered existence and finite resources

For every positive error tolerance and supplied incident-load cap \(\Lambda\), the displayed bounds admit finite choices in the following order. Fix the two central bands and cutoff, choose \(\rho=\gamma/j\) small enough to suppress \(P\), and then hold the resulting spectral derivative norms fixed. Choose \(jt_0\) large to reduce launch error, the near-emitter Fourier tail and the integrated incoming boundary allowance. Choose
\[
\frac1{v_-/j}<\alpha<\frac2{v_+/j}=1,
\qquad t_f=\alpha\ell/j,
\]
and increase the integer \(\ell\). This interval exists because \(v_+<2v_-\). The early factorial tail, early central tails, late incoming tail and output truncation tail vanish. The outgoing boundary allowance is \(O(1/\ell)\); the incoming allowance was already controlled by \(jt_0\). All constants retain their fixed \(\rho,\chi\) dependence.

After these dimensionless choices, put \(s=jt_f\) and make \(\eta=b/D_0\) and \(\zeta=D_0/D_1\) small enough that
\[
e_{\rm cell}\le\min\{2,(2+8s)\sqrt2\eta+2s\zeta\}
\]
fits its allowance. One safe load scaling is
\[
D_1=\Lambda/2,\quad D_0=\zeta D_1,\quad b=\eta D_0,
\quad 0<\eta\le1/8,\quad0<\zeta<1/2.
\]
Rescale \(j=b^2/D_0\), \(\gamma=\rho j\), \(t_0\) and \(t_f\) together. This does not promise a fixed speed while improving precision.

There are \(6+2M\) qubits and \(7+2M\) positive blocks, counting the cell's mediator/program projector as one combined block and each \(B_r\) as one block. Incident norm sums are \(D_1+2b\) at the mediator, \(3b+4j\) at the cell endpoints, \(a_0\) and \(D_1-2b\) at their respective program sites, \(4j\) at ordinary lead interiors, \(5j\) at emitter-adjacent sites, and \(3j\) at emitters. The stated conservative scaling places every sum below \(\Lambda\). This is a sufficient existence family, not a numerical operating point, optimum or practical resource claim.

## A uniform observation window

The same fixed device and seed also admit an interval \([t_-,t_+]\), with
\[
t_0\le t_-<t_+,\qquad t_-v_->\ell,\qquad t_+v_+<2\ell-2.
\]
Keep the same cutoff and spectral amplitude. Define
\[
 d_L=\mathcal T(t_-,t_-v_--\ell)<1,\qquad
 d_O=\frac{\mathcal T(t_+,2\ell+2-t_+v_+)}{1-d_L}<1.
\]
Then, with \(\beta_F(t)\) defined by the same finite Fourier projection,
\[
\sup_{t\in[t_-,t_+]}\left\|e^{-itH_{\rm phys}}E_{\rm seed}
 -e^{-i2bt}J_{\rm out}(\beta_F(t)\otimes C)\right\|
 \le E_{\rm window}
 :=\min\{2,e_{\rm cell}(t_+)+e_0+e_{\rm boundary}(t_+)+2d_L+2d_O\}.
\]
The packet normalization is uniformly positive:
\(\|P_{0\le n\le\ell}B(t)\|\ge(1-d_L)\sqrt{1-d_O^2}>0\).
The late incoming tail decreases, the unnormalized outgoing tail increases,
and the boundary and cell envelopes increase. The normalized outgoing-tail
quotient need not be monotone; its numerator is bounded at \(t_+\) and its
denominator using \(t_-\), which explains the mixed endpoints above.

Choose fixed \(1/(v_-/j)<\alpha_-<\alpha_+<1\) and
\(t_\pm=\alpha_\pm\ell/j\). The ordered existence argument applies
uniformly with the cell duration evaluated at \(t_+\). It preserves the
strictly positive relative width
\((t_+-t_-)/t_-=(\alpha_+-\alpha_-)/\alpha_-\) as accuracy improves
and the bounded-load scale changes. The Hamiltonian does not switch at
any of these times; \(t_0\) is only a proof decomposition. The packet and
scalar phase remain time dependent. This does not establish stationary
storage or permanent halt.

## Classical observation-time uncertainty

For any Borel probability measure \(\mu\) supported on the certified interval
and independent of the logical input and passive reference, define the actual
full-output ensemble channel
\[
\Phi_\mu(\rho)=\int e^{-itH_{\rm phys}}E_{\rm seed}\rho E_{\rm seed}^\dagger
 e^{itH_{\rm phys}}\,d\mu(t),\qquad
\sigma_\mu=\int|\beta_F(t)\rangle\langle\beta_F(t)|\,d\mu(t).
\]
Then, through the same fixed output isometry,
\[
\left\|\Phi_\mu-\left[\rho\mapsto
 J_{\rm out}(\sigma_\mu\otimes C\rho C^\dagger)J_{\rm out}^\dagger\right]
 \right\|_\diamond\le\min\{2,2E_{\rm window}\}.
\]
This retains every physical output, including actual emitter and mediator
residuals. Radial and logical factors are encoded coordinates, not separate
groups of physical site qubits. The common scalar cancels only within each
equal-time density matrix; it remains necessary in the vector theorem.
The result holds for discrete, continuous or singular timing laws without
knowing their shape. The full radial target \(\sigma_\mu\) depends on that law;
no single apparatus state for every law is asserted. Convexity and the
reference-uniform isometry estimate prove the bound. Input-correlated timing,
coherent control of evolution times, and freezing all outputs at a later
common wall-clock time require different physical models. This ensemble
statement supplies no stopping, measurement, storage or reset mechanism.

## Scope and checked evidence

The result supplies an approximate controlled port swap from endpoint occupation seeds under an exact supplied Hamiltonian. Coherent program inputs are not a derived framework Record mechanism. Native coefficient supply, vacant-head preparation, occupation basis, spatial roles and selective absence of couplings remain premises. No old literal-system operation or existing apparatus performance bound is replaced. The finite device can recur and reabsorb its head: the observation time is not permanent capture, storage, reset or an autonomous stopping mechanism.

The complete proof, distinct composition check and separately checked uniform-window and classical timing-mixture extensions, together with source/check ancestry and the preserved boundary correction, are in the [portable evidence manifest](../outputs/common_product_finite_seed_2026_10_18/SOURCES.json). The underlying [common product cell](COMMON_PRODUCT_PROGRAM_CELL_BOUNDED_THEOREM_NOTE_2026-10-18.md) and [attachment interface](COMMON_PRODUCT_PROGRAM_ATTACHMENT_BOUNDED_THEOREM_NOTE_2026-10-18.md) retain their respective domains. The scalar reference check is adopted only for its explicitly defined equal-diagonal operator, complete spectral measure, cyclicity and band-tail estimate. Only section 1 of the older positive endpoint family is a premise; its parity, converter and old-system claims are not imported.

ROOT proposed the architecture and composition route. The source author also wrote the initial synthesis; this is not an independent check. The distinct composition reviewer previously checked the launcher and corrected outer boundary, and read the proposed composition before reconstructing its interfaces. Shared model, design and source exposure are explicit: the check was neither blind nor model-diverse and assigns no retained status. ROOT fully read the composition, its check, the synthesis and all necessary component arguments. The boundary allowance above is exactly the closed rational envelope in composition source equation (9).

No scientific executable, symbolic solver, dynamics simulation, sweep or evaluated numerical operating point supports this result. Source hashes, package links and citation topology are mechanical publication checks, separate from the analytical review. No physical axioms or editable prompts were changed.

## Portable finite controls

Primary runner: `scripts/common_product_program_controls_2026_10_18.py` (timeout: 120 seconds). Its literal declared input closure includes all ten canonical notes and their live proof dependencies. It checks finite physical matrices, complete scattering and explicit sufficient budgets; finite controls corroborate these supplied conditional theorems and do not establish native realization or replace their analytical proofs. Historical statements above about what was executed describe original authorship; this added primary has a separate owner capture.
