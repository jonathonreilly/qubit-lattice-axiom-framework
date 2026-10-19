# Static recovery and a smaller complete error allowance for the same mediated apparatus

Claim type: bounded_theorem. Conditional mathematical result with selective, source-exposed analytical checks; no retained audit or native implementation is asserted.

Under the supplied-model premises below, the exact finite apparatus in the [earlier-window theorem](MEDIATED_EARLIER_WINDOW_BOUNDED_THEOREM_NOTE_2026-10-17.md) satisfies

\[
\sup_{8\cdot10^{18}\le t\le16\cdot10^{18}}
\|J_M e^{-itH_M}V-\mathcal T(t)\|<0.0002,
\qquad M=1\,920\,000\,000\,011.
\]

Its apparatus count remains **1,920,000,000,370 qubits**. The same infinite apparatus separately satisfies complete error below **0.000153 for every \(t\ge8\cdot10^{18}\)**. The previous finite allowance was 0.0005 on this identical interval for this identical Hamiltonian and target. The improvement is a factor 2.5 in a sufficient error certificate, with no reduction of waiting time, receiver size or physical resource requirement.

The new step separates a single static physical recovery map from a residual whose norm decreases as \(C_{\rm res}/t\). It does not alter the source, implement a new physical process or establish a measured error. The full residual proof (`outputs/mediated_residual_precision_2026_10_18/proofs/mediated_recovery_residual_decay__PROPOSAL.md`) and complete point derivation (`outputs/mediated_residual_precision_2026_10_18/proofs/mediated_residual_complete_point__PROPOSAL.md`), including their exact inherited premises, are incorporated as whole arguments. Their labels or numerical summaries are not substitutes for those proofs.

## Physical construction and comparison

Retain the exact correlated supplier prescription from the [finite-point parent](MEDIATED_FINITE_POINT_AND_DECAY_BOUNDED_THEOREM_NOTE_2026-10-17.md), and the installation, complete physical matching and regularity premises of the [mediated complete-output parent](MEDIATED_SOURCE_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md). The three source endpoints are joined by two alternating mediator paths and a third path to the original port. Here

\[
J_m=10^{-3},\quad q=5\cdot10^{-4},\quad m=12,
\quad n_1=n_2=23,\ n_3=12,\quad
 g=5\cdot10^{-8},\quad h=4\cdot10^{-6}.
\]

The original calibrated \(j\), with \(.0027<j<.003\), is fixed. The positive occupation-compensated \(Q\) installation replaces the old \(j n_p\) cap rather than adding a second copy. All source, mediator and background occupations and the original shared internal operator \(B\) are those of the checked installation. There are 116 mediator-internal heads and a 120-head source path including the existing port. No extra routing head or preparation device is introduced.

For precision about the unchanged suppliers, set \(u=10^{-8}\), \(d_\infty=(J_m^2-q^2)^{-1}\), \(A_0=1+u\), \(B_0=8u^2\), and

\[
v(w)=\frac{B_0+\sqrt{B_0^2+4A_0B_0(1+w)}}{2A_0},
\quad C_{\rm tune}=3\sqrt3\,jJ_m d_\infty.
\]

Use the parent's unique supplied root of
\(w^2\sqrt{A_0(A_0+v(w))}=C_{\rm tune}u(1+v(w)+w)\)
in its certified box, and \(\gamma_1=\sqrt{u/d_\infty}\), \(\gamma_2=\sqrt{v/d_\infty}\), \(\gamma_3=\sqrt{w/d_\infty}\). These are correlated exact prescriptions, not independently adjustable decimal intervals. With

\[
Z_0=1+u,\ Z_1=1+u+v,\ Z_2=1+v+w,
\quad a=J_m-q,
\quad \lambda=\frac{\sqrt3\gamma_1^2}{J_m\sqrt{Z_0Z_1}}2^{-22},
\quad \rho=\sqrt{a\lambda},\quad\kappa=\sqrt{3j\lambda},
\]

the saved certificate gives \(3.09\cdot10^{-18}<\lambda<3.10\cdot10^{-18}\) and \(3.93\cdot10^{-11}<\rho<3.94\cdot10^{-11}\). The retained physical windows are centered at \(c_{\rm att}+2j+1\) and \(c_{\rm att}+2j+3\), each with halfwidth \(\rho\).

The input \(V\) is the actual product seed at \(s_0\), the prescribed blank source and record factors, and an arbitrary old input, including any passive reference. The normalized complete target is exactly

\[
\mathcal T(t)=(-1)^{12}e^{-it(c_{\rm att}+2j)}
 J_{\rm out}\left[
 \frac{\beta_+(t)}{\|\beta_+(t)\|}\otimes e^{-itK}W\right],
\quad K=2I+Z_1Z_2,
\quad W=\frac{(9+12i)I+(-16+12i)X_1X_2}{25}.
\]

Here the Pauli labels in \(K\) are distinct from the source mass factors. The output embedding includes record1 and every prescribed source, mediator and background blank output. The packet \(\beta_+\) is the physical \(n\ge0\) restriction of the SAME critical reference \(F_\rho\), including its complex Weyl denominator, flux/Jacobian and phase \(61.5q_{\rm fast}+.5k+172k_{\rm old}\). The raw physical coefficient is \(F_\rho/\sqrt{Z_0}\). Incoming comparison uses \(W^*\) at the same positive time. No phase, waveform or normalization is fitted. This \(Q\) implementation has no additional pure-hopping scalar phase.

All original finite inverse gates remain premises: \(\eta<1.084\cdot10^{-8}\), \(k_C>.1849999981\), \(\zeta<.012344\), positive elimination gaps, \(\rho\le\min(d_{\rm bg},a/2)\), and \(\rho/g,d_{\rm bg}/g\le1/2\). Actual two-lip spectral identification, full-fiber forcing and the derivative of the closed-tail lift in its physical Hilbert norm are required. There is no global spectral-gap assumption for the assembled device.

## One static subtraction on every internal channel

Let \(A_l\) be the fixed alternating adjacency on mediator path \(l\), \(R_l(E)=(D\otimes I+A_l)^{-1}\), and \(R_{0,l}=I_{\rm fiber}\otimes A_l^{-1}\). The common map \(R_0\) is identical on both windows and both lips; it is not a selected-channel or window-dependent approximation. Its norm is at most \(1/a\).

The source endpoint incidence map sends \((s_0,s_1,s_2)\) to \(((s_0,s_1),(s_1,s_2),(s_2,0))\) in the three disjoint paths and has norm \(\sqrt2\). Define

\[
H_{\rm stat}z=(z,-\Gamma R_0 E_s z,0_{\rm background}),
\qquad \|H_{\rm stat}\|\le c_R=1+\sqrt2\gamma_*/a.
\]

For the actual represented source map \(Y_s(t)\), exact recovery gives

\[
N_I(t)=H_{\rm stat}Y_s(t)+Q_I(t),
\qquad \|N_I(t)\|\le c_R\|Y_s(t)\|+C_{\rm res}/|t|.
\]

The residual retains the source-driven difference \(-\Gamma(R-R_0)E_sU\), the entire port-driven third-path recovery and the entire finite background and closed tails. In order, \(w=t_3(D)J_2U\), \(K_p=(I-S_pG)^{-1}\), \(p=\widetilde G w\), and the background is \(LK_pw\). The port is counted once as a physical output. Noncommuting factors cannot be exchanged.

The crucial derivative bounds are full ROW bounds on \(S^{-1}\), not selected prepared columns: \(P\)-row \(\le a_P/R\), complementary row \(\le a_C/R+B_c\), where \(R=\sqrt{\delta^2+\lambda^2}\). Differentiating the exact inverse \(U'=-S^{-1}S'U\) retains complementary forcing. On the selected fiber \((R_l-R_{0,l})P=-\delta R_l A_l^{-1}P\), so the source-driven derivative integral retains \(|\delta|\). On the complement the nonzero bounds \(1/a+1/b\) and \(1/b^2\) remain. No derivative is inferred from a small real-axis value.

For an explicit, reproducible coefficient, the linked residual proof defines the full physical constants \(D_w,e_w,t_1,S_1,A,B_c,H_{p0},H_{p1},M_e,I_{M'}\). Its exact positive integrals are

\[
R_e=\sqrt{\rho^2+\lambda^2},\quad
J_R=2\operatorname{asinh}(\rho/\lambda),\quad
J_{R2}=2\arctan(\rho/\lambda)/\lambda,
\quad J_x=2(R_e-\lambda),\quad
J_{\log}=\log(1+\rho^2/\lambda^2).
\]

In particular \(D_w=t_Pa_P+\tau a_C\), \(e_w=\tau B_c\), with the physical \(t_P=\sqrt{Z_2}\kappa(1+\theta_3)\). Set

\[
w_e=D_w/R_e+e_w,\quad I_w=D_wJ_R+2\rho e_w,
\]
\[
I_{w'}=t_1(AJ_R+2\rho B_c)+S_1[D_wAJ_{R2}
 +(D_wB_c+e_wA)J_R+2\rho e_wB_c],
\]
\[
Q_e=M_e+H_{p0}w_e,\qquad
I_{Q'}=I_{M'}+H_{p1}I_w+H_{p0}I_{w'},\qquad
\boxed{C_{\rm res}=\frac2\pi(2Q_e+I_{Q'}).}
\]

Here \(M_e\) bounds the source-driven internal residual at each hard edge and \(I_{M'}\) bounds its full derivative integral; their four selected/complementary terms and all inverse-domain definitions are equations(8)--(20) of the incorporated residual proof. These definitions are part of the theorem, not optional estimates. Two hard endpoints, two lips and two physical windows produce the displayed factors. Bochner integration by parts occurs after embedding into the fixed physical output space; window pieces need not be orthogonal.

## Checked evaluation and complete budget

The distinct residual check (`outputs/mediated_residual_precision_2026_10_18/proofs/mediated_recovery_residual_decay_check__REVIEW.md`) reconstructs the all-fiber subtraction, ordered derivatives, hard-edge integrals and scope. The distinct point check (`outputs/mediated_residual_precision_2026_10_18/proofs/mediated_residual_complete_point_check__REVIEW.md`) separately reconstructs the finite substitutions and complete sum. At the unchanged tuple the conservative ceilings include

| Quantity | Upper ceiling |
|---|---:|
| Full physical inverse derivative \(S_1\) | 1.002 |
| \(D_w\), \(e_w\) | \(1.025\cdot10^{-9}\), \(1.012\cdot10^{-8}\) |
| \(H_{p0}\), \(H_{p1}\) | 14015, \(7.364\cdot10^{16}\) |
| \(I_w\), \(I_{w'}\) | \(3.691\cdot10^{-8}\), \(6.4\cdot10^9\) |
| \(M_e\), \(I_{M'}\) | 641, \(1.66\cdot10^5\) |
| \(Q_e\), \(2Q_e+I_{Q'}\) | 367000, \(9\cdot10^{13}\) |
| \(C_{\rm res}\) | \(6\cdot10^{13}\) |

The large background derivative is retained. Thus \(C_{\rm res}/t<7.5\cdot10^{-6}\) for \(t\ge T=8\cdot10^{18}\). The actual source comparison remains \(\|Y_s(t)\|\le C_s e^{-\lambda t/2}+S_s\), \(C_s=9/\sqrt{Z_0}\); the new residual only replaces the old static recovery allowance \(E_{\rm rec}\). It does not replace source, traveling, outside or normalization terms.

Crucially, the smaller budget is rebuilt from individual ceilings. One cannot subtract an \(E_{\rm rec}\) upper bound from an old aggregate upper bound. For every \(t\ge T\), the checked sum is:

| Complete contribution | Upper allowance |
|---|---:|
| One actual outside spectral vector | .000100065 |
| Full source comparison \(c_RS_s\) | .0000001071954 |
| Source exponential | .00004357 |
| Full recovery residual \(C_{\rm res}/t\) | .0000075 |
| Both raw traveling discrepancies | .00000003306 |
| Physical ideal incoming halfline | .0000017 |
| Physical seed/transmitted normalization floor | .000000005001 |
| Additional outgoing-halfline normalization | .00000000000576 |
| **Sum** | **.00015298026216 < .000153** |

The source exponential uses \(\lambda T>24.72\) and \(e^{12.36}>217600\). The inherited all-late scalar bounds are \(h_{\rm in}<1.7\cdot10^{-6}\), \(h_{\rm left}<2.4\cdot10^{-6}\); the stronger scalar bound restricted to a shorter scaled interval is not extrapolated. The actual outside witness covers every outside spectral type once, including possible atoms. Critical reference moments only bound the reference mass \(p\), not the actual mediated seed.

For \(\ell=2.4\cdot10^{-6}\), physical restriction gives \(\|\beta_+\|^2\ge p(1-\ell^2)>0\). The one normalization charge obeys
\(1-\sqrt{p(1-\ell^2)/Z_0}\le1-\sqrt{p_*/Z_0}+\ell^2\).
Both raw discrepancies remain, even if their physical images overlap. All bounds are old-input operator bounds and persist with arbitrary passive references.

The unchanged terminal cap \(g n_{\rm last}\) is the exact principal compression. At \(T_1=16\cdot10^{18}\), the g-only cut uses

\[
2gT_1\sinh1<1\,920\,000\,000\,000,
\qquad \log(1.2/.00004)=\log30000<11.
\]

The same integer \(M\) therefore adds at most .00004, giving complete finite error below .000193<.0002 on \([T,T_1]\). The comparator is the normalized infinite packet, not a truncated target renormalized afterwards. Counts remain \(M+354\) head qubits, \(M+359\) apparatus qubits, \(M+355\) head edges and at most \(2M+514\) listed positive blocks. A single chosen read has failure effect at most \(4\cdot10^{-8}I\) and unhalved complete-channel diamond error at most .0004.

## Conditional scaling and limitations

For fixed suppliers and fixed background \(g,h,j\), along the checked family with eventual \(\rho=\sqrt{a\lambda}\) and uniform positive inverse margins, the proof gives

\[
C_{\rm res}=O(\lambda^{-1/2}+\log(1/\lambda)).
\]

Only the small \(D_w\) or \(a_C\) coefficients multiply the unweighted \(J_{R2}\) integral; the selected static difference instead uses \(J_{\log}\). At \(t=\xi/\lambda\), fixed \(\xi>0\), the residual therefore tends to zero as \(O((\sqrt\lambda+\lambda\log(1/\lambda))/\xi)\). This is conditional on fixed background and uniform gaps/margins; it is not a variable-g theorem. The calibration floor and source comparison allowance remain. It does not prove an actual nonzero error floor, an optimal onset or finite permanent storage.

The result neither supplies native interactions nor relaxes correlated coefficients, onsite identities, source/record initialization or the processor premises. No new precision-box or onsite-error proposal is imported. Physical time units, repeated monitoring, capture, reset/reuse and permanent finite halt remain outside scope. Infinite all-late evolution and the finite read window are different statements.

## Evidence and review exposure

No new numerical program, root solve, quadrature, dynamics or sweep was run. The unchanged saved exact enclosure certificate from the finite-point parent supplies the tuple; all new arithmetic consists of displayed positive rational ceilings and elementary bounds. Previous execution evidence is inherited evidence, not a new run. No physical experiment, retained audit or completed publication is claimed.

The four primary files use `outputs/mediated_residual_precision_2026_10_18/proofs/DIRECTORY__FILENAME`; their full arguments and review qualifications remain incorporated:

| Primary file | SHA256 |
|---|---|
| Residual theorem (`outputs/mediated_residual_precision_2026_10_18/proofs/mediated_recovery_residual_decay__PROPOSAL.md`) | `f66b5636cca5cc6ef8e71b40746beb97b831527028738a6ccef7f17bca2b28ea` |
| Residual theorem check (`outputs/mediated_residual_precision_2026_10_18/proofs/mediated_recovery_residual_decay_check__REVIEW.md`) | `4f6784efb2f68f36b5598ac764cc3ae33ee7785048ad440acf16016305cadc5c` |
| Same-device complete point (`outputs/mediated_residual_precision_2026_10_18/proofs/mediated_residual_complete_point__PROPOSAL.md`) | `fd9ee286420775aa54dcd9bee657c04be9a39b30003ab6b73c4fe955dc5e0cbd` |
| Complete point check (`outputs/mediated_residual_precision_2026_10_18/proofs/mediated_residual_complete_point_check__REVIEW.md`) | `041850aafdf054376de82d1c9ff481076c924cdbcd9eeae3f5a95bfd7089cf7c` |

I authored this synthesis and the complete-point check, as well as several inherited recovery/raw/cut arguments. The residual theorem and point were authored by another worker; ROOT separately reconstructed the residual theorem. Shared source exposure and same-model ancestry are disclosed, not treated as independent replication. This draft reuses the full four primary arguments at their fixed identities and preserves their conditional status. ROOT separately owns the publication integration check and portable packaging. The source author drafted this synthesis; its initial metadata was editorially updated for publication. No physical axiom, editable prompt or model setting changed.


## Reproducible finite controls

**Type:** bounded_theorem

Primary runner: `scripts/mediated_complete_output_controls_2026_10_18.py`.
Run `python3 scripts/mediated_complete_output_controls_2026_10_18.py` from the repository root.
The shared runner directly checks finite alternating-chain inverses, ordered full-forcing Schur reconstruction, and conservative residual/onsite arithmetic, and reproduces the baseline exact interval calculation. It does not simulate the full apparatus or prove infinite-time synthesis. The incorporated analytical arguments and their supplied hypotheses remain load-bearing. Earlier statements of no new numerical execution describe the original author preparation; the review adds these bounded controls separately.
