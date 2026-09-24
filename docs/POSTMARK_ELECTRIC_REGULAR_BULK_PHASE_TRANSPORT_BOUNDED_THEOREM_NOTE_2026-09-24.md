---
claim_id: postmark_electric_regular_bulk_phase_transport_2026_09_24
claim_type: bounded_theorem
claim_scope: >-
  For the explicitly tabulated scalar Jacobi family and a fixed energy whose
  local momentum stays in a compact nonturning, non-Bragg interval, the exact
  product across O(S) consecutive five-site cells has an O(S^-1) diagonal
  transport approximation. Its phase includes both the sum of local cell
  phases and a geometric eigenvector-overlap correction. No crossing match,
  global quantization, or readout estimate is claimed.
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: postmark_electric_core_and_boundary_bounded_theorem_note_2026_09_24
target_blocker_text: "joint finite-spin electric limit"
source_of_blocker_text: handoff
reachability_to_target: supports
conditional_surface_status: "conditional on identifying the displayed scalar coefficient family with the supplied one-vacancy model; the physical identification and readout connection remain open"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The adiabatic product estimate is proved on the stated regular interval for the displayed scalar Jacobi family; it does not control the nonregular layers or the prepared readout."
audit_required_before_effective_retained: true
bare_retained_allowed: false
artifact_role: theorem
next_trace_action: "Match the regular-interval transfer through Bragg, central, turning, and endpoint layers, then carry prepared overlaps into an all-alias two-index estimate."
upstream_dependencies:
  - postmark_electric_five_site_transfer_phase_expansion_2026_09_24
runner: scripts/postmark_electric_regular_bulk_phase_transport_2026_09_24.py
---

# Regular bulk phase transport across a macroscopic five-site interval

**Date:** 2026-09-24
**Type:** bounded theorem
**Status:** proposed_retained

## Exact target

**Exact claim.** For the scalar five-residue Jacobi family defined in the
[local transfer note](POSTMARK_ELECTRIC_FIVE_SITE_TRANSFER_PHASE_EXPANSION_BOUNDED_THEOREM_NOTE_2026-09-24.md),
fix an energy \(\lambda\) and a compact interval \(J\subset(-1,1)\) on which
\[
w(u)=1-u^2,\qquad z(u,\lambda)=1-\frac{\lambda}{2w(u)}=\cos k(u,\lambda),
\]
obey \(k\in[\delta,\pi-\delta]\) and
\(|\sin(5k(u,\lambda))|\ge\kappa>0\). On every such interval, the exact
transfer product over \(O(S)\) consecutive five-site cells admits a
diagonal approximation with uniform operator-norm error \(O(S^{-1})\).
Its phase is the sum of the exact local cell phases plus the phase accumulated
from the overlaps of neighboring normalized cell eigenvectors. This note
gives the limiting overlap integral explicitly.

Let \(h_0<h_1\) be integers with \(u_h=h/S\in J\) for
\(h_0\le h\le h_1\). Write \(M_{S,h}(\lambda)\) for the exact
five-site matrix of the preceding note at cell \(h\), and
\[
P_S=M_{S,h_1-1}(\lambda)\cdots M_{S,h_0}(\lambda).
\]
Let \(e^{\pm i\Phi_{S,h}}\) be its local eigenvalues, with
\(\Phi_{S,h}\to5k(u_h,\lambda)\). Put
\[
B_{S,h}=(M_{S,h})_{12},\qquad A_{S,h}=(M_{S,h})_{11},
\]
and define the plus eigenvector and eigenbasis by
\[
r_{S,h}=
\frac{e^{ik(u_h,\lambda)}
 \bigl(B_{S,h},\,e^{i\Phi_{S,h}}-A_{S,h}\bigr)^T}
{\sqrt{B_{S,h}\sin\Phi_{S,h}}},
\qquad
R_{S,h}=(r_{S,h},\overline{r_{S,h}}).
\]
Here the numerator notation means scalar multiplication of the vector
\((B_{S,h},e^{i\Phi_{S,h}}-A_{S,h})^T\) by \(e^{ik(u_h,\lambda)}\);
the positive square root is well-defined for all sufficiently large \(S\)
on \(J\), and \(\det R_{S,h}=-2i\). Define
\[
\beta_{S,h}=\bigl(R_{S,h+1}^{-1}R_{S,h}\bigr)_{11},\qquad
\eta_S=\prod_{h=h_0}^{h_1-1}e^{i\Phi_{S,h}}\beta_{S,h}.
\]
Then, for a constant depending only on the compact regular interval and its
margins,
\[
\left\|P_S-
R_{S,h_1}
\begin{pmatrix}\eta_S&0\\0&\overline{\eta_S}\end{pmatrix}
R_{S,h_0}^{-1}\right\|\le \frac{C_J}{S}.
\]

For the limiting principal cell, set
\[
r_0^+(u)=\frac{(e^{ik(u,\lambda)},-w(u))^T}
{\sqrt{w(u)\sin k(u,\lambda)}},\qquad
R_0(u)=(r_0^+(u),\overline{r_0^+(u)}),\qquad
\ell_0^+(u)=e_1^T R_0(u)^{-1}.
\]
This gauge has \(\det R_0=-2i\). Its connection is
\[
\mathcal B(u,\lambda)
=\operatorname{Im}\!\left(\ell_0^+(u)\,\partial_u r_0^+(u)\right)
=\frac{(w'/w)\cos k+(\partial_u k)\sin k}{2\sin k}
=\frac{(2\cos k-1)w'}{2w\sin k},
\quad w'=-2u,\quad
\partial_u k=-\frac{(1-\cos k)w'}{w\sin k}.
\]
Choose each \(\operatorname{Arg}\beta_{S,h}\) in \((-\pi/2,\pi/2)\), which is
possible for sufficiently large \(S\), and define the unwrapped phase
\[
\Theta_S=\sum_{h=h_0}^{h_1-1}
\bigl(\Phi_{S,h}+\operatorname{Arg}\beta_{S,h}\bigr).
\]
With the eigenvector gauge displayed above,
\[
\Theta_S
=\sum_{h=h_0}^{h_1-1}
\left(5k(u_h,\lambda)+\frac{g_1(u_h,\cos k(u_h,\lambda))}
{S\sin k(u_h,\lambda)}\right)
-\int_{u_{h_0}}^{u_{h_1}}\mathcal B(u,\lambda)\,du
+O_J(S^{-1}),
\]
where \(g_1\) is defined in the local transfer note. The \(S^{-2}\) local
phase coefficient contributes only \(O(S^{-1})\) after summing over this
interval, so it is within the displayed remainder.

## Proof dependency graph

| Obligation | Status here | Evidence or dependency |
|---|---|---|
| Exact five-site matrices and local phase expansion | Proved in the linked local transfer note | Its exact coefficient table and trace/phase formulas are part of this review unit; the paired local runner has exact symbolic checks. |
| Smooth normalized eigenbasis on the regular interval | Proved here | The principal transfer has a simple elliptic spectrum, \(|\sin(5k)|\ge\kappa\), and \(B_{0}(u)=\sin(5k)/(w\sin k)\) stays nonzero; analytic perturbation gives a smooth \(R_{S,h}\) with bounded derivatives. |
| Neighboring-basis overlap structure | Proved here | \(R_{S,h+1}^{-1}R_{S,h}=I+S^{-1}C(u_h)+O(S^{-2})\), its determinant is one, and conjugate pairing makes the diagonal first-order terms purely imaginary. |
| Removal of first-order off-diagonal mixing | Proved here | Solve the two off-diagonal homological equations using the uniform gap \(|e^{i\Phi}-e^{-i\Phi}|=2|\sin\Phi|\ge\kappa\) after reducing \(S\) sufficiently large. |
| Product error over \(O(S)\) cells | Proved here | The conjugated one-step remainder is \(O(S^{-2})\), the diagonal product is uniformly bounded, and summing \(O(S)\) steps gives \(O(S^{-1})\). |
| Limiting overlap integral | Proved here | Differentiate the explicit principal eigenbasis; the runner independently verifies the connection identity symbolically and compares its integral with exact finite-cell overlaps. |
| Propagation through Bragg, central, turning, or endpoint layers | Open | These regions violate at least one of the uniform gap or smooth-eigenbasis hypotheses. |
| Prepared spectral overlaps and the two-index readout sum | Open | The transfer product estimate alone supplies neither the prepared weights nor an all-alias cancellation bound. |

## Proof

Write \(\varepsilon=S^{-1}\) and
\(\Lambda_{S,h}=\operatorname{diag}(e^{i\Phi_{S,h}},
e^{-i\Phi_{S,h}})\). The local expansion in the upstream note and
compactness give uniform bounds on \(M_{S,h}\), its first two \(u\)
derivatives, and the reciprocal spectral gap. The leading cell is
\(D(u)A(k)^5D(u)^{-1}\), where
\[
A(k)=\begin{pmatrix}2\cos k&1\\-1&0\end{pmatrix},
\qquad D(u)=\operatorname{diag}(1,w(u)).
\]
Its eigenvalue \(e^{i5k}\) has eigenvector
\((e^{ik},-w)^T\). The upper-right entry of the leading cell is
\(B_0=\sin(5k)/(w\sin k)\), uniformly separated from zero on \(J\).
For large \(S\), \(B_{S,h}\sin\Phi_{S,h}>0\); direct substitution shows
that the displayed normalized eigenvector has eigenvalue \(e^{i\Phi_{S,h}}\)
and that \(\det R_{S,h}=-2i\). The eigenbasis and its first two derivatives
are uniformly bounded.

Set
\[
Q_{S,h}=R_{S,h+1}^{-1}R_{S,h}.
\]
Smoothness gives
\(Q_{S,h}=I+\varepsilon C(u_h)+O_J(\varepsilon^2)\). It has determinant
one and the form
\[
Q_{S,h}=
\begin{pmatrix}\beta_{S,h}&\gamma_{S,h}\\
\overline{\gamma_{S,h}}&\overline{\beta_{S,h}}\end{pmatrix},
\qquad |\beta_{S,h}|^2-|\gamma_{S,h}|^2=1.
\]
Thus \(\gamma_{S,h}=O_J(\varepsilon)\) and
\(|\beta_{S,h}|=1+O_J(\varepsilon^2)\); any \(O(S)\)-cell product of the
diagonal magnitudes is uniformly bounded.

In the moving basis, one step is \(Q_{S,h}\Lambda_{S,h}\). Write
\(X_{S,h}\) for the zero-diagonal matrix whose off-diagonal entries solve
\[
(X_{S,h})_{ij}
=-\frac{C_{ij}(u_h)(\Lambda_{S,h})_{jj}}
{(\Lambda_{S,h})_{ii}-(\Lambda_{S,h})_{jj}},
\qquad i\ne j.
\]
The gap bound makes \(X_{S,h}\) uniformly bounded, and smoothness gives
\(X_{S,h+1}-X_{S,h}=O_J(\varepsilon)\). Conjugating by
\(I+\varepsilon X_{S,h}\) cancels the first-order off-diagonal entries.
The resulting one-step matrix is
\[
\operatorname{diag}(e^{i\Phi_{S,h}}\beta_{S,h},
e^{-i\Phi_{S,h}}\overline{\beta_{S,h}})+O_J(\varepsilon^2).
\]
Multiplying \(O(S)\) such matrices accumulates only \(O(S^{-1})\) error:
the diagonal factors remain uniformly bounded, the sum of local errors is
\(O(S\varepsilon^2)\), and the endpoint conjugacies differ from identity
by \(O(\varepsilon)\). Returning to the physical basis proves the product
estimate.

To obtain the connection term, differentiate \(r_0^+\) at fixed \(\lambda\).
With \(\ell_0^+=e_1^TR_0^{-1}\), direct calculation gives the displayed
\(\mathcal B\). The exact finite-\(S\) basis satisfies
\[
\beta_{S,h}
=1-\varepsilon\,\ell_0^+(u_h)\partial_u r_0^+(u_h)
+O_J(\varepsilon^2).
\]
Its argument is therefore
\(-\varepsilon\mathcal B(u_h,\lambda)+O_J(\varepsilon^2)\). Summing and
using the compact-interval Riemann-sum error gives
\[
\arg\prod_h\beta_{S,h}
=-\int_{u_{h_0}}^{u_{h_1}}\mathcal B(u,\lambda)\,du+O_J(S^{-1}).
\]
Finally, summing the local phase expansion contributes \(O(S^{-2})\) from
its \(O(S^{-3})\) remainder, while the sum of its \(S^{-2}\) coefficient is
\(O(S^{-1})\). This proves the stated phase formula.

## Scope and strongest missing lemma

This result controls propagation only where the exact five-site cell stays
uniformly elliptic and nondegenerate. It supplies a phase-accurate transfer
factor on one macroscopic regular interval, but it is not a global
quantization law: no matching is provided at Bragg or central crossings,
turning points, or physical endpoints. The strongest missing lemma remains
an all-alias \(o(1)\) bound for the exact prepared two-energy readout sum after
global phase and overlap transport across those regions.

The physical identification of the explicitly displayed scalar family with
the supplied one-vacancy model is conditional. This theorem derives no
Hamiltonian, preparation, observable, axiom, or primitive.

## Imports and open bridges

| Input | Role | Provenance | Open bridge |
|---|---|---|---|
| Local five-site transfer trace and phase expansion | Supplies the exact cell family and uniform local phase expansion | The linked local transfer note is included in this review unit | Its physical interpretation is conditional on the model identification stated there |
| The scalar Jacobi family | Defines the mathematical transfer product studied here | Exact residue arrays and coefficients are defined in the linked local transfer note | Its identification with the physical one-vacancy model is not re-derived |
| Smooth eigenvector diagonalization and a finite-dimensional homological equation | Mathematical tools for the regular-interval product estimate | Derived explicitly in the proof below | No external physical input is taken from these tools |

## Verification

The paired runner checks the Berry connection identity by symbolic
differentiation using an independent principal-eigenvector formula. It also
forms exact finite-spin cell products over macroscopic regular intervals,
compares them with the normalized-eigenvector diagonal approximation, and
compares the discrete overlap phase with the connection integral. The
finite-size matrix and quadrature results are corroboration only; the
uniform \(O(S^{-1})\) estimate follows from the gap-based averaging proof.
No global quantization or readout result is inferred.
