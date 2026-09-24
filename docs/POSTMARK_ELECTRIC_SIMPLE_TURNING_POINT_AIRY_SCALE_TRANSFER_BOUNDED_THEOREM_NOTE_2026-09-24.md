---
claim_id: postmark_electric_simple_turning_point_airy_scale_transfer_2026_09_24
claim_type: bounded_theorem
claim_scope: >-
  For the explicitly tabulated scalar Jacobi family and energies in a compact
  subset of (0,4), the exact five-site transfer at the positive simple band
  edge has a Jordan-scaled Airy limit on S^-2/3 spatial windows. On the allowed
  side this limit matches the adjacent principal-cell WKB basis, including its
  first subprincipal phase. It does not control the remote forbidden tail,
  the other turning point, physical endpoints, quantization, or readout.
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: postmark_electric_core_and_boundary_bounded_theorem_note_2026_09_24
target_blocker_text: "joint finite-spin electric limit"
source_of_blocker_text: handoff
reachability_to_target: supports
conditional_surface_status: "conditional on the displayed scalar Jacobi family being identified with the supplied one-vacancy model; the physical identification and prepared readout remain open"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The note proves a local discrete Airy transfer limit and its oscillatory-side match for the defined scalar family; it supplies no endpoint-selected eigenfunction or readout estimate."
audit_required_before_effective_retained: true
bare_retained_allowed: false
artifact_role: theorem
next_trace_action: "Derive the endpoint forbidden-tail and boundary-selection estimate, then transport prepared overlaps through the full spectral range before the all-alias two-index sum."
upstream_dependencies:
  - postmark_electric_five_site_transfer_phase_expansion_2026_09_24
  - postmark_electric_regular_bulk_phase_transport_2026_09_24
  - postmark_electric_simple_bragg_crossing_transfer_2026_09_24
runner: scripts/postmark_electric_simple_turning_point_airy_scale_transfer_2026_09_24.py
---

# Airy-scale transfer at the positive simple turning point

**Date:** 2026-09-24
**Type:** bounded theorem
**Status:** proposed_retained

## Exact target

Use the five-site scalar Jacobi family and transfer matrices defined in the
[local transfer note](POSTMARK_ELECTRIC_FIVE_SITE_TRANSFER_PHASE_EXPANSION_BOUNDED_THEOREM_NOTE_2026-09-24.md).
Fix a compact energy interval \(\Lambda\subset(0,4)\), and write
\[
a_\lambda=\sqrt{1-\lambda/4},\qquad
w_a=1-a_\lambda^2=\lambda/4,\qquad
b_\lambda=800a_\lambda/\lambda.
\]
On the allowed side just inside the positive turning point, let
\[
z(u,\lambda)=1-\frac{\lambda}{2(1-u^2)}=\cos k(u,\lambda),
\qquad k(u,\lambda)\in(0,\pi).
\]
Choose \(d_0>0\), uniformly for \(\lambda\in\Lambda\), so
\([a_\lambda-d_0,a_\lambda+d_0]\subset(0,1)\) and the only root of
\(\sin(5k(u,\lambda))=0\) in this interval is the band edge \(u=a_\lambda\).

Let \(M_{S,h}(\lambda)\) be the exact five-site transfer at \(u_h=h/S\).
For each fixed \(R>0\), set
\[
\epsilon=S^{-1},\qquad
\tau_h=\frac{u_h-a_\lambda}{\epsilon^{2/3}},\qquad
\Delta=\epsilon^{1/3}.
\]
Use the fixed edge similarity \(D_a=\operatorname{diag}(1,w_a)\), the exact
Jordan basis
\[
P=\begin{pmatrix}1&1/10\\1&-1/10\end{pmatrix},
\qquad
-P^{-1}A(-1)^5P=
\begin{pmatrix}1&1\\0&1\end{pmatrix},
\qquad
A(z)=\begin{pmatrix}2z&1\\-1&0\end{pmatrix},
\]
and define scaled cell coordinates by
\[
\xi_h=\epsilon^{1/6}
\begin{pmatrix}1&0\\0&\epsilon^{-1/3}\end{pmatrix}
(-1)^hP^{-1}D_a^{-1}Y_h,
\]
where \(Y_h\) satisfies \(Y_{h+1}=M_{S,h}(\lambda)Y_h\). Uniformly for
\(\lambda\in\Lambda\) and \(\tau_h\in[-R,R]\), the exact scaled one-cell
matrix is
\[
\xi_{h+1}=
\left[
I+\Delta\begin{pmatrix}0&1\\b_\lambda\tau_h&0\end{pmatrix}
+O_{\Lambda,R}(\Delta^2)
\right]\xi_h.
\]
Consequently, between any two cell indices in this fixed Airy window, the
exact scaled propagator differs by \(O_{\Lambda,R}(S^{-1/3})\) from the
fundamental matrix of
\[
\frac{d}{d\tau}\begin{pmatrix}q\\p\end{pmatrix}
=\begin{pmatrix}0&1\\b_\lambda\tau&0\end{pmatrix}
\begin{pmatrix}q\\p\end{pmatrix},
\qquad q''=b_\lambda\tau q.
\]
With \(x=b_\lambda^{1/3}\tau\), this is the Airy equation \(q_{xx}=xq\).

The frozen finite-\(S\) cell edge is shifted by
\[
u_{\mathrm{edge}}(S,\lambda)
=a_\lambda-\frac{\lambda\,g_1(a_\lambda,-1)}{80a_\lambda S}
+O_\Lambda(S^{-2}),
\]
where \(g_1\) is the coefficient in the local transfer note. This
\(O(S^{-1})\) displacement is smaller than the Airy width \(S^{-2/3}\);
the leading scaled coordinate is therefore centered at \(a_\lambda\).

## Proof obligations and disposition

| Obligation | Status here | Evidence |
|---|---|---|
| Parabolic cell and fixed Jordan basis | Proved here | Direct multiplication of \(A(-1)^5\) and the displayed \(P\). |
| Coefficient of the linearly opening Jordan entry | Proved here | The determinant-one identity equates that entry's derivative to the trace derivative; \(T_5'(-1)=25\) and \(z'(a_\lambda)=-16a_\lambda/\lambda\). |
| Airy-scaled one-step expansion | Proved here | Uniform analytic expansion of the exact five-site matrix in \((u-a_\lambda,\epsilon)\), followed by the displayed diagonal rescaling. |
| Fixed-window propagator limit | Proved here | Euler-product comparison with the Airy first-order system and a discrete Grönwall bound. |
| Oscillatory-side WKB match | Proved here | The principal-frame columns have an explicit Jordan-scaled limit at \(u=a_\lambda-R\epsilon^{2/3}\); the outer normal-form error is \(O(R^{-3/2})\). |
| Remote forbidden tail and boundary-selected decay | Open | No estimate is asserted outside a fixed Airy-scaled window on the forbidden side. |
| Other turning point, physical endpoints, quantization, prepared overlaps, and readout | Open | These require separate uniform transport and spectral-weight arguments. |

## Proof

For real \(u\) near \(a_\lambda\), extend the exact link factors analytically
by
\[
r_j(u,\epsilon)=1-\frac{(u+j\epsilon)(u+(j+1)\epsilon)}{1+\epsilon},
\qquad j\in\{-1,0,1\}.
\]
This is exactly \(1-f(h+j)/(S(S+1))\) when \(u=h/S\). The five site
transfers built from these \(r_j\) define a frozen cell \(M_\epsilon(u,\lambda)\);
at \(u=u_h\), it equals \(M_{S,h}(\lambda)\). Since \(w_a\) is uniformly
positive on \(\Lambda\), all square roots and matrices are analytic on a
common neighborhood of \((a_\lambda,0)\), with uniform Taylor bounds.

At \(\epsilon=0\),
\[
M_0(u,\lambda)=D(u)A(z(u,\lambda))^5D(u)^{-1},
\qquad D(u)=\operatorname{diag}(1,1-u^2).
\]
At \(u=a_\lambda\), \(z=-1\), \(D(u)=D_a\), and direct multiplication gives
\[
-P^{-1}D_a^{-1}M_0(a_\lambda,\lambda)D_aP
=J=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]
Write
\[
\mathcal B_\epsilon(u)
=-P^{-1}D_a^{-1}M_\epsilon(u,\lambda)D_aP.
\]
It has determinant one and the uniform expansion
\[
\mathcal B_\epsilon(u)
=J+(u-a_\lambda)C_\lambda+\epsilon E_\lambda
+O_\Lambda((u-a_\lambda)^2+\epsilon|u-a_\lambda|+\epsilon^2).
\]
To identify \((C_\lambda)_{21}\), differentiate
\(\det\mathcal B_0(u)=1\) at \(u=a_\lambda\). Since
\(J^{-1}=I-(J-I)\), the determinant identity gives
\(\operatorname{tr} C_\lambda=(C_\lambda)_{21}\). The trace is unchanged by
the fixed similarities, and
\[
\operatorname{tr}\mathcal B_0(u)=-2T_5(z(u,\lambda)),\qquad
T_5'(-1)=25,\qquad
\partial_u z(a_\lambda,\lambda)=-\lambda a_\lambda/w_a^2
=-16a_\lambda/\lambda.
\]
Hence
\[
(C_\lambda)_{21}
=\partial_u\operatorname{tr}\mathcal B_0(a_\lambda)
=800a_\lambda/\lambda=b_\lambda>0.
\]
This trace calculation fixes both the orientation and factor in the Airy
potential.

Now put \(\Delta=\epsilon^{1/3}\) and
\(\tau_h=(u_h-a_\lambda)/\epsilon^{2/3}\). Consecutive cells differ by
\(\epsilon\), so \(\tau_{h+1}-\tau_h=\Delta\). Factoring the cell sign
\((-1)^h\) turns the exact cell matrix into \(\mathcal B_\epsilon(u_h)\).
Conjugating its Jordan coordinates by
\(\operatorname{diag}(1,\epsilon^{-1/3})\), and using
\(u_h-a_\lambda=\epsilon^{2/3}\tau_h\), gives
\[
\operatorname{diag}(1,\epsilon^{-1/3})
\mathcal B_\epsilon(u_h)
\operatorname{diag}(1,\epsilon^{1/3})
=I+\Delta
\begin{pmatrix}0&1\\b_\lambda\tau_h&0\end{pmatrix}
+O_{\Lambda,R}(\Delta^2).
\]
The scalar factor \(\epsilon^{1/6}\) in \(\xi_h\) cancels from the
one-step equation and keeps the matched principal modes bounded. The Airy
system's coefficient matrix is Lipschitz on \([-R,R]\), so its exact
one-step propagator is \(I+\Delta A(\tau_h)+O_{\Lambda,R}(\Delta^2)\).
There are at most \(2R/\Delta+2\) steps. A discrete Grönwall estimate
therefore bounds the difference of the exact and Airy propagators by
\(C_{\Lambda,R}\Delta\), proving the fixed-window claim.

The finite-\(S\) shift follows from the same exact trace expansion. At fixed
\(\lambda\), the local transfer note gives
\[
\operatorname{tr}M_\epsilon(u,\lambda)
=2T_5(z)-2\epsilon U_4(z)g_1(u,z)+O_\Lambda(\epsilon^2),
\qquad U_4(-1)=5.
\]
Thus
\[
\operatorname{tr}\mathcal B_\epsilon(u)-2
=b_\lambda(u-a_\lambda)+10\epsilon g_1(a_\lambda,-1)
+O_\Lambda((u-a_\lambda)^2+\epsilon|u-a_\lambda|+\epsilon^2).
\]
The implicit-function theorem gives the stated simple root and its
\(S^{-1}\) displacement. It does not move the leading Airy center, since
\(S^{-1}=o(S^{-2/3})\).

For the allowed-side overlap, let \(t=a_\lambda-u>0\) and
\(K_\lambda=\sqrt{32a_\lambda/\lambda}\). Then
\[
\pi-k(u,\lambda)=K_\lambda\sqrt t+O_\Lambda(t^{3/2}),
\qquad b_\lambda=25K_\lambda^2.
\]
The principal eigenframe from the regular transport note becomes singular
like \(t^{-1/4}\), but its Jordan-scaled columns have a finite Airy-scale
asymptotic. At \(u=a_\lambda-R\epsilon^{2/3}\),
\[
\epsilon^{1/6}
\operatorname{diag}(1,\epsilon^{-1/3})
P^{-1}D_a^{-1}R_0(u)
=\frac{1}{\sqrt{w_aK_\lambda}}
\begin{pmatrix}
-R^{-1/4}&-R^{-1/4}\\
i\sqrt{b_\lambda}R^{1/4}&-i\sqrt{b_\lambda}R^{1/4}
\end{pmatrix}
+o_{\epsilon\to0}(1).
\]
Let \(h_t=\lfloor Sa_\lambda\rfloor\), and let \(h_0\) be the fixed interior
reference cell. The accumulated factored phase to the edge is
\[
\chi_{S,\lambda}
=\sum_{h=h_0}^{h_t-1}
\left[5(k(u_h,\lambda)-\pi)
+\epsilon\left(\frac{g_1(u_h,\cos k)}{\sin k}
-\mathcal B(u_h,\lambda)\right)\right].
\]
The plus-mode phase from that reference cell to the overlap point is
\[
\chi_{S,\lambda}+\phi_R+o_{\epsilon\to0}(1),\qquad
\phi_R=\frac23\sqrt{b_\lambda}R^{3/2},
\]
with the common alternating-cell sign included in the phase origin. The
subprincipal phase density is
\(O_\Lambda(t^{-1/2})\), hence integrable at the turn; its omitted inner-tail
contribution is \(O_\Lambda(\sqrt t)=o(1)\) for fixed \(R\).

For completeness, the adjacent regular product admits a uniform
normal-form estimate on
\([a_\lambda-d_0,a_\lambda-\delta]\):
\[
\left\|
(-1)^N R_0(u_H)^{-1}
M_{S,h_1-1}\cdots M_{S,h_0}R_0(u_0)
-
\operatorname{diag}(e^{i\Theta^\sharp_S},e^{-i\Theta^\sharp_S})
\right\|
\le C_\Lambda\epsilon\delta^{-3/2},
\]
where \(u_0=u_{h_0}\), \(u_H=u_{h_1}\),
\(N=h_1-h_0\), and
\[
\Theta^\sharp_S=\sum_{h=h_0}^{h_1-1}
\left[5(k(u_h,\lambda)-\pi)
+\epsilon\left(\frac{g_1(u_h,\cos k)}{\sin k}
-\mathcal B(u_h,\lambda)\right)\right].
\]
Indeed, with \(t=a_\lambda-u\), the principal eigenvalue gap is
\(\asymp t^{1/2}\), the diagonal first-order term is \(O(t^{-1/2})\), and
the off-diagonal first-order term is \(O(t^{-1})\). To see the singular
orders directly, write the unnormalized frame as
\[
V(u)=\begin{pmatrix}e^{ik}&e^{-ik}\\-w&-w\end{pmatrix},
\qquad R_0=(w\sin k)^{-1/2}V.
\]
The scalar normalization contributes only a diagonal term to
\(R_0^{-1}R_0'\), while
\[
(R_0^{-1}R_0')_{12}
=\frac{e^{-ik}(-wk'+iw')}{2w\sin k},\qquad
(R_0^{-1}R_0')_{21}
=\frac{e^{ik}(-wk'-iw')}{2w\sin k}.
\]
Here \(\sin k\asymp t^{1/2}\), \(k'=O(t^{-1/2})\),
\(w(a_\lambda)=\lambda/4\), and \(w'(a_\lambda)=-2a_\lambda\).
Consequently each displayed off-diagonal connection entry is
\(1/(4t)+O_\Lambda(t^{-1/2})\). The transformed \(M_1\) contribution is
only \(O_\Lambda(t^{-1/2})\), since \(M_1\) is smooth in the fixed
coefficient frame and both \(R_0\) and \(R_0^{-1}\) have norm
\(O_\Lambda(t^{-1/4})\). This proves the stated \(A_1\) bounds and the
leading off-diagonal order. The homological
correction is therefore \(O(t^{-3/2})\), with derivative \(O(t^{-5/2})\).
Its near-identity transform is valid when \(\epsilon t^{-3/2}\) is small.
Taylor's theorem in the fixed coefficient frame gives a second-order
moving-frame remainder \(O_\Lambda(\epsilon^2t^{-2})\). The homological
change adds terms bounded by \(C_\Lambda\epsilon^2t^{-5/2}\), which dominate
that remainder. Summing from distance \(\delta\) to \(d_0\) gives
\(C_\Lambda\epsilon\delta^{-3/2}\), including the endpoint changes of
basis. At
\(\delta=R\epsilon^{2/3}\), this is \(C R^{-3/2}\). The sum of
\(5(k-\pi)\) from the overlap cell to the edge is \(-\phi_R+o(1)\), so the
phase from the reference cell is \(\chi_{S,\lambda}+\phi_R+o(1)\).

The Airy asymptotics for \(\tau=-R\) are
\[
\operatorname{Ai}(b^{1/3}\tau)
\sim \pi^{-1/2}b^{-1/12}R^{-1/4}\sin(\phi_R+\pi/4),
\qquad
\operatorname{Bi}(b^{1/3}\tau)
\sim \pi^{-1/2}b^{-1/12}R^{-1/4}\cos(\phi_R+\pi/4).
\]
Consequently the normalized principal plus/minus modes match respectively
to
\[
-\mathcal N_\lambda e^{i\chi_{S,\lambda}}e^{-i\pi/4}
\bigl(\operatorname{Bi}(b^{1/3}\tau)+i\operatorname{Ai}(b^{1/3}\tau)\bigr),
\qquad
-\mathcal N_\lambda e^{-i\chi_{S,\lambda}}e^{i\pi/4}
\bigl(\operatorname{Bi}(b^{1/3}\tau)-i\operatorname{Ai}(b^{1/3}\tau)\bigr),
\]
with
\[
\mathcal N_\lambda=\sqrt{5\pi/w_a}\,b_\lambda^{-1/6}.
\]
On the forbidden side \(\tau>0\), \(\operatorname{Ai}(b^{1/3}\tau)\) is the
decaying Airy solution and \(\operatorname{Bi}(b^{1/3}\tau)\) is the growing
one. This is the local connection law; it does not select a boundary
condition or bound the exact tail at a macroscopic distance from the edge.
The matching error tends to zero in the ordered limit \(S\to\infty\) at
fixed \(R\), followed by \(R\to\infty\).

## Imports and scope

| Input | Role | Boundary |
|---|---|---|
| Five-site coefficient family and trace expansion | Exact cell and \(g_1\) | The [local transfer note](POSTMARK_ELECTRIC_FIVE_SITE_TRANSFER_PHASE_EXPANSION_BOUNDED_THEOREM_NOTE_2026-09-24.md) defines the scalar family; identification with the supplied physical model remains conditional. |
| Regular principal frame and connection | WKB phase and normalized eigenvectors | The [regular transport note](POSTMARK_ELECTRIC_REGULAR_BULK_PHASE_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-09-24.md) applies only away from the turning point; the overlap bound is derived here. |
| Moving-frame diagonal phase identity | First subprincipal phase density | The [simple-Bragg note](POSTMARK_ELECTRIC_SIMPLE_BRAGG_CROSSING_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-24.md) proves the identity for the displayed family and adds no global quantization. |
| Mathematical tools | Taylor's theorem, determinant differentiation, discrete Grönwall, and Airy asymptotics | Used only on the compact energy interval and explicit local domain above. |

No framework axiom, approved primitive, measured value, or fitted parameter
enters the scalar transfer calculation. The supplied Hamiltonian,
preparation, and period-three output remain conditional inputs; this note
proposes no axiom or primitive update.

## Verification

The paired runner checks the exact parabolic Jordan form, differentiates the
cell trace to verify \(b_\lambda=800a_\lambda/\lambda\), checks the
first-order frozen-edge displacement, and rejects a factor-of-two mutation.
It compares exact finite-spin scaled one-cell matrices with the Airy Euler
step at several energies and spins, and compares layer products with an
independently integrated Airy system. Those finite checks are diagnostics;
the uniform \(O(S^{-1/3})\) limit and overlap estimate follow from the
Taylor, homological, and Euler-product bounds in the proof.

    python3 scripts/postmark_electric_simple_turning_point_airy_scale_transfer_2026_09_24.py

The result JSON and canonical runner-cache record are stored under
outputs/postmark_moving_index_2026_09_24/ and logs/runner-cache/.
No independent review or formal audit status is claimed.
