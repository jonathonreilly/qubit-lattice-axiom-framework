---
claim_id: postmark_electric_simple_bragg_crossing_transfer_2026_09_24
claim_type: bounded_theorem
claim_scope: >-
  For the explicitly tabulated scalar Jacobi family, a single simple
  interior five-site Bragg crossing can be included in a macroscopic transfer
  estimate with an O(S^-1/3) error in a smooth principal-cell eigenbasis.
  The leading phase is the regular local phase plus its eigenvector
  connection. Central, turning, endpoint, multiple-crossing, and readout
  questions remain open.
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: postmark_electric_core_and_boundary_bounded_theorem_note_2026_09_24
target_blocker_text: "joint finite-spin electric limit"
source_of_blocker_text: handoff
reachability_to_target: supports
conditional_surface_status: "conditional on identifying the displayed scalar Jacobi family with the supplied one-vacancy model; the physical identification and prepared readout remain open"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The theorem controls one simple Bragg crossing for the displayed scalar family but does not match every nonregular layer or estimate the prepared readout."
audit_required_before_effective_retained: true
bare_retained_allowed: false
artifact_role: theorem
next_trace_action: "Treat central degeneracies, turning points, physical endpoints, and prepared-overlap transport before attempting the all-alias two-index sum."
upstream_dependencies:
  - postmark_electric_five_site_transfer_phase_expansion_2026_09_24
  - postmark_electric_regular_bulk_phase_transport_2026_09_24
runner: scripts/postmark_electric_simple_bragg_crossing_transfer_2026_09_24.py
---

# Transfer through one simple interior Bragg crossing

**Date:** 2026-09-24
**Type:** bounded theorem
**Status:** proposed_retained

## Exact target

**Exact claim.** For the scalar Jacobi family defined in the
[five-site transfer note](POSTMARK_ELECTRIC_FIVE_SITE_TRANSFER_PHASE_EXPANSION_BOUNDED_THEOREM_NOTE_2026-09-24.md),
fix \(\lambda\) and a compact interval \(J\subset(-1,1)\) such that
\[
w(u)=1-u^2,\qquad
1-\frac{\lambda}{2w(u)}=\cos k(u,\lambda),\qquad
k(u,\lambda)\in[\delta,\pi-\delta].
\]
Assume \(5k(u,\lambda)=m\pi\) has exactly one root \(u_B\in\operatorname{int}J\),
with \(m\in\{1,2,3,4\}\) and \(\partial_u k(u_B,\lambda)\ne0\). For cell
indices \(h_0<h_1\) with \(u_h=h/S\in J\), the exact transfer product
\[
P_S=M_{S,h_1-1}(\lambda)\cdots M_{S,h_0}(\lambda)
\]
has the following diagonal approximation in the smooth principal-cell
eigenbasis. Define
\[
r_0^+(u)=\frac{(e^{ik(u,\lambda)},-w(u))^T}
{\sqrt{w(u)\sin k(u,\lambda)}},\qquad
R_0(u)=(r_0^+(u),\overline{r_0^+(u)}),\qquad
\ell_0^+(u)=e_1^TR_0(u)^{-1},
\]
and
\[
\mathcal B(u,\lambda)=
\operatorname{Im}\!\left(\ell_0^+(u)\partial_u r_0^+(u)\right)
=\frac{(2\cos k-1)w'}{2w\sin k},\qquad w'=-2u.
\]
For
\[
\Theta_S=\sum_{h=h_0}^{h_1-1}
\left[
5k(u_h,\lambda)+\frac1S\left(
\frac{g_1(u_h,\cos k(u_h,\lambda))}{\sin k(u_h,\lambda)}
-\mathcal B(u_h,\lambda)\right)\right],
\]
where \(g_1\) is defined in the five-site transfer note, there is a constant
\(C_J\) such that
\[
\left\|P_S-
R_0(u_{h_1})
\begin{pmatrix}e^{i\Theta_S}&0\\0&e^{-i\Theta_S}\end{pmatrix}
R_0(u_{h_0})^{-1}\right\|
\le C_J S^{-1/3}.
\]
The estimate includes the crossing cells themselves; it does not require
their exact finite-\(S\) cell matrices to remain elliptic.

## Proof dependency graph

| Obligation | Status here | Evidence or dependency |
|---|---|---|
| Exact five-site cell family and first-order matrix expansion | Proved in the linked local transfer note | The exact scalar entries, per-site matrix coefficients, and ordered product recurrence are included in this review unit. |
| Smooth principal eigenbasis through the repeated-root point | Proved here | The one-site eigenvectors remain distinct because \(k\in[\delta,\pi-\delta]\); the five-site leading monodromy may equal \((-1)^m I\) without making this chosen frame singular. |
| First-order diagonal phase in the moving frame | Proved here | Simple-eigenvalue perturbation away from the crossing gives \(g_1/\sin k\); the moving frame contributes \(-\mathcal B\). Both coefficients extend smoothly to \(u_B\). |
| Product inside the shrinking crossing layer | Proved here | Each moving-frame cell is \((-1)^m I+O(|u-u_B|+S^{-1})\); summing over a layer of width \(S^{-2/3}\) gives \(O(S^{-1/3})\). |
| Averaging outside the layer | Proved here | A near-identity homological change removes first-order off-diagonal terms; the remaining \(O(S^{-2}|u-u_B|^{-2})\) errors sum to \(O(S^{-1/3})\). |
| Other Bragg points, central degeneracy, turning points, endpoints, and readout | Open | This note handles one simple Bragg root away from \(u=0\) and from the local band edges only. |

## Proof

Write \(\varepsilon=S^{-1}\). The local coefficient formulas in the
five-site transfer note are analytic in \(u,\varepsilon\) on a compact
interval away from \(|u|=1\). Multiplying the five one-site matrices gives
\[
M_{S,h}(\lambda)=M_0(u_h,\lambda)
+\varepsilon M_1(u_h,\lambda)+O_J(\varepsilon^2),
\]
with the same bound after two \(u\)-derivatives. The leading cell is
\[
M_0(u,\lambda)=D(u)A(k)^5D(u)^{-1},\quad
A(k)=\begin{pmatrix}2\cos k&1\\-1&0\end{pmatrix},\quad
D(u)=\operatorname{diag}(1,w).
\]
Its normalized eigenbasis is \(R_0(u)\), with leading eigenvalues
\(e^{\pm i5k(u,\lambda)}\). Although these eigenvalues coincide at \(u_B\),
the chosen frame \(R_0\) is smooth there and has determinant \(-2i\).

Use moving coordinates between consecutive cells:
\[
W_{S,h}=R_0(u_{h+1})^{-1}M_{S,h}(\lambda)R_0(u_h)
=\Lambda_0(u_h)+\varepsilon A_1(u_h)+O_J(\varepsilon^2),
\quad
\Lambda_0=\operatorname{diag}(e^{i5k},e^{-i5k}).
\]
The derivative of \(R_0\) is included in
\[
A_1=R_0^{-1}M_1R_0-R_0^{-1}(\partial_uR_0)\Lambda_0.
\]
For clarity about coordinates, let \(A(k)\) be the similar one-site matrix
in the local transfer note and \(M_{1s}\) its order-\(\varepsilon\)
coefficient. The order-\(\varepsilon\) coefficient of the five-site product
in those similar coordinates is
\[
\widetilde M_1=\sum_{s=0}^4 A(k)^{4-s}M_{1s}A(k)^s,
\qquad M_1=D(u)\widetilde M_1D(u)^{-1}.
\]
At fixed physical \(\lambda\),
\[
z'=\frac{(1-z)w'}{w},\qquad
k'=-\frac{(1-z)w'}{w\sin k}.
\]
Substitution of these expressions, the displayed principal frame, and the
five-site coefficient table gives the exact identity
\[
-i\,\frac{(A_1)_{11}}{e^{i5k}}
=\frac{g_1(u,\cos k)}{\sin k}-\mathcal B(u,\lambda).
\]
The paired runner checks this rational-trigonometric identity exactly after
reducing by \(\sin^2 k+\cos^2 k=1\), and rejects both the opposite connection
sign and an additive change to \(g_1\). All expressions extend continuously
across \(u_B\), so the moving-frame diagonal phase coefficient is bounded on
the full interval. This calculation uses a smooth frame for the principal
one-site matrix and does not perturb-diagonalize the repeated five-site
eigenvalue at the crossing.

Set \(\rho=\varepsilon^{2/3}\), and separate cells with
\(|u_h-u_B|\le\rho\) from the two outer intervals. Since the crossing is
simple, \(|\sin(5k(u))|\ge c_J|u-u_B|\) near \(u_B\). In the inner layer,
\[
\Lambda_0(u_h)=(-1)^m I+O_J(|u_h-u_B|),
\quad
W_{S,h}=(-1)^m I+O_J(|u_h-u_B|+\varepsilon).
\]
There are \(O(\rho/\varepsilon)\) such cells. The product after removing
the scalar factor \((-1)^{mN_{\rm in}}\) differs from the identity by at
most
\[
O_J\!\left(\sum_{\rm in}(|u_h-u_B|+\varepsilon)\right)
=O_J(\rho^2/\varepsilon+\rho)
=O_J(\varepsilon^{1/3}).
\]
The proposed phase sum over these cells differs from \(m\pi N_{\rm in}\)
by the same order. This argument is matrix-norm based and remains valid if
some exact finite-\(S\) crossing-cell matrices are hyperbolic.

Outside the layer, define a zero-diagonal matrix \(X_h\) by
\[
(X_h)_{ij}
=-\frac{(A_1(u_h))_{ij}}
{(\Lambda_0(u_h))_{ii}-(\Lambda_0(u_h))_{jj}},
\quad i\ne j.
\]
Then \(\|X_h\|\le C_J/|u_h-u_B|\) and
\(\|\partial_uX_h\|\le C_J/|u_h-u_B|^2\). The change of coordinates
\(y_h=(I+\varepsilon X_h)z_h\) gives the exact expansion
\[
z_{h+1}=
(I+\varepsilon X_{h+1})^{-1}W_{S,h}(I+\varepsilon X_h)z_h
=\left[\operatorname{diag}\bigl((\Lambda_0)_{11}
+\varepsilon(A_1)_{11},(\Lambda_0)_{22}
+\varepsilon(A_1)_{22}\bigr)+E_{S,h}\right]z_h,
\]
where the first-order off-diagonal entries cancel by the definition of
\(X_h\), and
\[
\|E_{S,h}\|\le C_J\varepsilon^2|u_h-u_B|^{-2}.
\]
Summing from distance \(\rho\) to a fixed endpoint gives
\[
C_J\varepsilon\int_{\rho}^{O(1)}v^{-2}\,dv
=O_J(\varepsilon/\rho)=O_J(\varepsilon^{1/3}).
\]
The endpoint changes of basis have the same \(O_J(\varepsilon/\rho)\)
size. The diagonal factors stay bounded because their first-order changes
are pure phase in the determinant-one conjugate-paired frame; the remaining
diagonal modulus error is included in the summed remainder.

Combining the two outer estimates with the inner-layer estimate proves the
matrix approximation. Replacing the first-order diagonal coefficient by its
displayed expression gives \(\Theta_S\). No regular-arc second-order
eigenphase expansion is used at the crossing: its coefficient need not stay
bounded as \(\sin(5k)\to0\). The outer normal-form remainder already includes
all higher-order diagonal and off-diagonal terms and sums to
\(O_J(\varepsilon/\rho)\); the inner-layer phase discrepancy is
\(O_J(\rho^2/\varepsilon+\rho)\). Both are
\(O_J(\varepsilon^{1/3})\) for \(\rho=\varepsilon^{2/3}\).

## Scope and strongest missing lemma

The theorem crosses one simple interior Bragg point at a nonzero \(u_B\).
It does not cover the central case \(k'(u_B)=0\), a physical band edge,
multiple roots whose separation shrinks with \(S\), a turning point, or a
physical endpoint. It proves no global eigenvalue quantization, prepared
overlap transport, or cancellation in the exact two-index readout sum. The
strongest missing lemma is a corresponding matched propagation estimate
through all remaining nonregular regions with sufficient phase and overlap
accuracy for the all-alias readout.

## Imports and open bridges

| Input | Role | Provenance | Open bridge |
|---|---|---|---|
| Exact five-site coefficients and their first-order matrix expansion | Supplies the local scalar family | Defined and expanded in the linked five-site transfer note, included in this review unit | Physical identification with the supplied one-vacancy model remains conditional |
| Regular-interval local phase and eigenvector connection | Supplies the phase coefficient used outside the crossing layer | Derived in the linked regular-bulk transport note, included in this review unit | No statement is imported about the central or endpoint regions |
| Smooth finite-dimensional diagonalization and the homological equation | Mathematical tools for the outer normal form | Derived with the displayed gap bounds in this proof | No physical input is imported from these tools |

## Verification

The paired runner checks the first-order phase coefficient against an exact
symbolic five-site product identity, then forms exact finite-spin products
through a simple Bragg crossing and compares them with the displayed
principal-frame phase approximation. The finite-size norms are corroboration
only; the \(O(S^{-1/3})\) error follows from the shrinking-layer and
gap-dependent outer estimates above. The result is conditional on the
explicit scalar Jacobi family and does not establish a prepared-readout
limit.
