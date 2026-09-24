---
claim_id: postmark_electric_central_bragg_crossing_transfer_2026_09_24
claim_type: bounded_theorem
claim_scope: >-
  For the explicitly tabulated scalar Jacobi family, each central energy
  lambda_m=2(1-cos(m*pi/5)), m=1,...,4, has a double five-site Bragg contact
  at u=0 through which the macroscopic transfer has an O(S^-1/2) principal-
  frame approximation. Turning points, endpoints, global quantization,
  prepared readout, and the all-alias sum remain open.
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: postmark_electric_core_and_boundary_bounded_theorem_note_2026_09_24
target_blocker_text: "joint finite-spin electric limit"
source_of_blocker_text: handoff
reachability_to_target: supports
conditional_surface_status: "conditional on identifying the displayed scalar Jacobi family with the supplied one-vacancy model; physical identification and the prepared readout remain open"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The theorem controls only four fixed-energy central double Bragg contacts for the displayed scalar family and supplies no turning-point, global quantization, or readout estimate."
audit_required_before_effective_retained: true
bare_retained_allowed: false
artifact_role: theorem
next_trace_action: "Match this central layer and simple Bragg layers to turning and endpoint propagation, then carry prepared overlaps into the all-alias two-index estimate."
upstream_dependencies:
  - postmark_electric_five_site_transfer_phase_expansion_2026_09_24
  - postmark_electric_regular_bulk_phase_transport_2026_09_24
  - postmark_electric_simple_bragg_crossing_transfer_2026_09_24
runner: scripts/postmark_electric_central_bragg_crossing_transfer_2026_09_24.py
---

# Transfer through the symmetry-suppressed central Bragg contact

**Date:** 2026-09-24
**Type:** bounded theorem
**Status:** proposed_retained

## Exact target

For \(m\in\{1,2,3,4\}\), fix
\[
\lambda_m=2\bigl(1-\cos(m\pi/5)\bigr),\qquad k_m=m\pi/5.
\]
Let \(J=[-u_0,u_0]\subset(-1,1)\) be a compact interval on which the local
momentum is separated from 0 and \(\pi\), and for which
\(5k(u,\lambda_m)=m\pi\) has no root other than its double root at
\(u=0\). Set \(w(u)=1-u^2\) and
\[
1-\frac{\lambda_m}{2w(u)}=\cos k(u,\lambda_m),\qquad
k(u,\lambda_m)\in[\delta,\pi-\delta].
\]
For integers \(h_0<h_1\) with \(u_h=h/S\in J\) for every
\(h_0\le h\le h_1\), let
\[
P_S=M_{S,h_1-1}(\lambda_m)\cdots M_{S,h_0}(\lambda_m)
\]
be the exact product from the five-site transfer note. Use its smooth
principal-cell frame
\[
r_0^+(u)=\frac{(e^{ik(u,\lambda_m)},-w(u))^T}
{\sqrt{w(u)\sin k(u,\lambda_m)}},\qquad
R_0(u)=(r_0^+(u),\overline{r_0^+(u)}),
\]
and define
\[
\mathcal B(u,\lambda_m)
=\frac{(2\cos k-1)w'}{2w\sin k},\qquad w'=-2u,
\qquad
g_1(u,z)=\frac{u(5uz-5u-9z+8)}{1-u^2}.
\]
Then there is a constant \(C_{J,m}\), independent of the integer spin \(S\),
such that
\[
\left\|P_S-R_0(u_{h_1})
\begin{pmatrix}e^{i\Theta_S}&0\\0&e^{-i\Theta_S}\end{pmatrix}
R_0(u_{h_0})^{-1}\right\|
\le C_{J,m}S^{-1/2},
\]
where
\[
\Theta_S=\sum_{h=h_0}^{h_1-1}
\left[5k(u_h,\lambda_m)+\frac1S\left(
\frac{g_1(u_h,\cos k(u_h,\lambda_m))}{\sin k(u_h,\lambda_m)}
-\mathcal B(u_h,\lambda_m)\right)\right].
\]
The estimate includes the central contact cells. It requires neither
diagonalization at the repeated five-site eigenvalue nor ellipticity of every
finite-spin cell in the central window.

## Proof dependency graph

| Obligation | Status here | Evidence or dependency |
|---|---|---|
| Exact scalar five-site transfer family and its uniform matrix expansion | Proved in the local transfer note | Exact residue coefficients and the compact-(u) Taylor expansion are included in this review unit. |
| Quadratic contact and local gap scale | Proved here | At fixed \(\lambda_m\), \(k-k_m=((1-\cos k_m)/\sin k_m)u^2+O(u^4)\), hence \(|\sin(5k)|\asymp u^2\) on a sufficiently small \(J\setminus\{0\}\). |
| First-order matrix coefficient vanishes linearly | Proved here | Every first-order site matrix vanishes at \(u=0\); also \(w'(0)=k'(0)=0\), so the moving-frame coefficient \(A_1(0)=0\) and \(\|A_1(u)\|\le C_{J,m}|u|\). |
| Central shrinking-window product | Proved here | For \(\rho=S^{-1/2}\), the summed error \(\sum_{|u_h|\le\rho}(u_h^2+S^{-1}|u_h|+S^{-2})\) is \(O(S^{-1/2})\). |
| Outer normal form | Proved here | The gap is \(\asymp u^2\) but the first-order off-diagonal numerator is \(O(|u|)\), so the homological correction and its derivative are \(O(1/|u|)\) and \(O(1/u^2)\); the accumulated remainder is \(O(S^{-1/2})\). |
| Turning points, endpoints, other energies, global quantization, and readout | Open | The theorem is only at the four fixed central Bragg energies and on a small interior interval. |

## Proof

Write \(\varepsilon=S^{-1}\), \(z=\cos k\), and use the smooth principal
frame from the local transfer note. Its frozen five-site eigenvalues are
\(e^{\pm i5k}\), even when both equal
\(\sigma=(-1)^m\). At fixed \(\lambda_m\), put
\(a_m=1-\cos k_m>0\). Since
\[
z(u)=1-\frac{a_m}{1-u^2}
=\cos k_m-a_m u^2+O(u^4),
\]
the inverse cosine expansion gives
\[
k(u,\lambda_m)=k_m+\frac{a_m}{\sin k_m}u^2+O(u^4),
\qquad
|\sin(5k(u,\lambda_m))|\asymp u^2.
\]
The compact interval \(J\) can be chosen so this comparison is uniform away
from \(u=0\), with no other Bragg point in \(J\).

The exact moving-frame cell expansion is
\[
W_{S,h}=R_0(u_h+\varepsilon)^{-1}M_{S,h}(\lambda_m)R_0(u_h)
=\Lambda_0(u_h)+\varepsilon A_1(u_h)+O_{J,m}(\varepsilon^2),
\]
where \(\Lambda_0=\operatorname{diag}(e^{i5k},e^{-i5k})\) and
\[
A_1=R_0^{-1}M_1R_0-R_0^{-1}(\partial_uR_0)\Lambda_0.
\]
In the local coefficient formulas, each first-order site-matrix entry is
linear in the quantities
\(b_s=(\alpha_{\ell_s}+\alpha_{\rho_s})/2\) and
\(d_{1s}=\alpha_{\ell_s}+\alpha_{\pi_s}\), where
\(\alpha_a=u^2-u(2a+1)\). Thus all five first-order site matrices vanish
at \(u=0\) and are smooth \(O(u)\). Also \(w'(0)=0\) and, at fixed
\(\lambda_m\), \(k'(0)=0\); hence \(R_0'(0)=0\). It follows that
\[
A_1(0)=0,\qquad \|A_1(u)\|\le C_{J,m}|u|.
\]
The diagonal phase coefficient is the same exact moving-frame identity
derived and checked in the included simple-crossing note and runner:
\[
-i\frac{(A_1)_{11}}{e^{i5k}}
=\frac{g_1(u,\cos k)}{\sin k}-\mathcal B(u,\lambda_m).
\]
Both terms on the right are \(O(u)\), so this coefficient stays bounded
through the contact.

Choose the central layer \(|u_h|\le\rho\) with
\(\rho=\varepsilon^{1/2}\). There,
\[
\Lambda_0(u_h)=\sigma I+O_{J,m}(u_h^2),\qquad
W_{S,h}=\sigma I+O_{J,m}(u_h^2+\varepsilon|u_h|+\varepsilon^2).
\]
There are O(rho/epsilon+1) cells. Removing the scalar factor
\(\sigma\) from each step and using the product bound by the exponential of
the summed one-step errors gives
\[
\left\|\sigma^{-N_{\rm in}}\prod_{h\in\rm in}W_{S,h}-I\right\|
\le C_{J,m}\sum_{h\in\rm in}
(u_h^2+\varepsilon|u_h|+\varepsilon^2)
=O_{J,m}(\rho^3/\varepsilon+\rho^2+\varepsilon\rho)
=O_{J,m}(\varepsilon^{1/2}).
\]
The proposed phase sum over the same cells differs from
\(m\pi N_{\rm in}\) by \(O_{J,m}(\rho^3/\varepsilon+\rho^2)\), also
\(O(\varepsilon^{1/2})\). This controls the contact without resolving
individual eigenvectors of the repeated cell eigenvalue.

Outside the central layer define the zero-diagonal homological correction
\[
(X_h)_{ij}
=-\frac{(A_1(u_h))_{ij}}
{(\Lambda_0(u_h))_{ii}-(\Lambda_0(u_h))_{jj}},
\qquad i\ne j.
\]
The gap and vanishing numerator imply
\[
\|X_h\|\le C_{J,m}|u_h|^{-1},\qquad
\|\partial_uX_h\|\le C_{J,m}|u_h|^{-2}.
\]
Because \(\varepsilon/\rho=\varepsilon^{1/2}\to0\), the near-identity
change \(v_h=(I+\varepsilon X_h)z_h\) is invertible on the outer pieces.
It cancels the first-order off-diagonal entries, leaving the diagonal factors
\(\Lambda_{0,ii}+\varepsilon(A_1)_{ii}\) and a remainder bounded by
\[
\|E_{S,h}\|\le C_{J,m}\varepsilon^2|u_h|^{-2}.
\]
Summing the remainder from distance \(\rho\) to a fixed endpoint gives
\[
\sum_{\rm out}\|E_{S,h}\|
\le C_{J,m}\varepsilon\int_\rho^{u_0}v^{-2}\,dv
=O_{J,m}(\varepsilon/\rho)
=O_{J,m}(\varepsilon^{1/2}).
\]
The endpoint changes of basis are also \(O(\varepsilon/\rho)\). The
first-order diagonal corrections are pure phase in the determinant-one
conjugate-paired frame; their accumulated modulus error is included in the
same summed remainder. Their phase is exactly the displayed summand in
\(\Theta_S\), up to the already bounded higher-order errors. Combining the
central and outer products proves the estimate.

## Scope and strongest missing lemma

This theorem covers the four fixed energies whose principal momentum at
\(u=0\) is \(m\pi/5\). It does not give an estimate uniform in energy near
those four values, and it does not handle the ordinary turning points
\(k=0,\pi\), physical endpoints \(|u|=1\), prepared spectral-overlap
transport, global eigenvalue quantization, or the two-index readout. The
strongest missing lemma is a phase-accurate transfer and prepared-overlap
estimate uniform on the energy range contributing to the interior readout,
including its turning and endpoint layers and all aliases.

## Imports and open bridges

| Input | Role | Provenance | Open bridge |
|---|---|---|---|
| Exact five-site coefficients, transfer, and \(g_1\) | Defines the scalar family and local matrix expansion | The [five-site transfer note](POSTMARK_ELECTRIC_FIVE_SITE_TRANSFER_PHASE_EXPANSION_BOUNDED_THEOREM_NOTE_2026-09-24.md), included in this review unit | Physical identification with the supplied one-vacancy model remains conditional |
| Principal-frame connection \(\mathcal B\) | Supplies the moving-basis phase | Derived in the [regular bulk transport note](POSTMARK_ELECTRIC_REGULAR_BULK_PHASE_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-09-24.md), included in this review unit | No crossing or endpoint result is imported from the regular theorem |
| First-order moving-frame identity | Fixes the phase coefficient on the punctured sides | Exact coefficient convolution in the [simple-Bragg note](POSTMARK_ELECTRIC_SIMPLE_BRAGG_CROSSING_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-24.md) and its paired runner, included in this review unit | It is local and supplies no global quantization |
| Taylor bounds and the homological equation | Control the inner product and outer remainders | Derived with explicit gap and vanishing-numerator scales in this proof | No physical or axiomatic input is imported |

The supplied model, preparation, and period-three output remain conditional
inputs; this note changes no framework axiom or primitive. No global fixed-time
readout statement is claimed.

## Verification

The paired runner checks that the symbolic moving-frame first-order matrix
vanishes at \(u=0\), verifies the quadratic phase-contact coefficient, and
rejects a constant off-diagonal mutation of that vanishing condition. It then
forms exact finite-spin transfer products at all four \(m\)-values over
\(S=120,240,480,960,1920,3840,7680,15360\). The finite errors and local
ellipticity counts are corroboration only; the \(O(S^{-1/2})\) rate follows
from the displayed inner-layer and outer-gap proof.
