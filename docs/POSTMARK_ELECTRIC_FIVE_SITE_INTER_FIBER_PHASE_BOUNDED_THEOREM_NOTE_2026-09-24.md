---
claim_id: postmark_electric_five_site_inter_fiber_phase_2026_09_24
claim_type: bounded_theorem
claim_scope: Conditional on the supplied finite-spin one-vacancy path and exact signed link-Casimir labels, the
  exact five-site coefficient family, frozen primitive-cell spectrum, four first-order same-fiber crossing compressions,
  period-three inter-fiber action, principal lobe action, and cross-phase stationary set are derived. No global
  finite-spin propagation or readout limit is claimed.
upstream_dependencies:
- fast_vacancy_motion_after_formation_bounded_theorem_note_2026-09-24
- minimal_axioms
- postmark_electric_core_and_boundary_bounded_theorem_note_2026-09-24
- postmark_electric_exact_side_fixed_index_kernel_2026-09-24
- zero_mode_and_goegenbauer_limit_bounded_theorem_note_2026-09-24
runner: scripts/postmark_electric_five_site_inter_fiber_phase_2026_09_24.py
---

# Five-site Casimir reduction and the period-three cross-phase

**Date:** 2026-09-24
**Type:** bounded theorem
**Status:** proposed_retained

**Exact target.** Conditional on the supplied signed edge-Casimir tables, derive the exact five-site Jacobi coefficients and their uniform compact-bulk expansion, the frozen five-cell Bloch bands and period-three fiber shift, the four first-order same-fiber crossing compressions and slopes, the principal cross-phase stationary set, and the classical principal-lobe action with its factor of five in physical-site coordinates.

## Proof dependency graph

| Obligation | Status here | Evidence or dependency |
|---|---|---|
| Finite-spin path, signed edge labels, and staggering convention | Imported condition | Canonical fast-vacancy and zero-mode notes plus `scripts/core_derivation.py`; these are supplied-model inputs, not consequences of the four framework axioms. |
| Exact five-site Casimir coefficients and compact-bulk (S^{-1}) expansion | Proved here | Direct substitution of the signed labels into (f(m)=m(m+1)), followed by a uniform square-root Taylor expansion on (|u|le1-
arepsilon). |
| Frozen five-cell bands and the period-three Fourier-fiber shift | Proved here | Direct Bloch diagonalization and the exact identity (omega^{5h+s}=omega^s e^{4pi i h/3}). |
| Four crossing compressions, principal slopes, and first-order gaps | Proved here | Explicit five-component eigenvectors and finite sums of the displayed first-subprincipal cell matrix; the runner checks the degree-two algebraic identities and slope magnitudes. |
| Principal cross-phase stationary points and lobe action | Proved here | Differentiation of the displayed symbol and an explicit one-dimensional integral evaluation. |
| Global transfer, actual weighted phase correlation, and the finite-spin readout | Open | Requires a uniform moving-index estimate through turning, Bragg, central, and endpoint regions; none follows from the frozen-cell calculation. |

The theorem covers the exact coefficient family, compact bulk intervals, the four listed same-fiber degeneracies, and the principal-symbol action integral. The bulk expansion excludes (|u|\to1); no global transport, quantization error, or actual-readout limit is proved. The strongest missing lemma is an (o(1))-accurate finite-spin phase/overlap estimate for the prepared state at time (C/4), uniform through the central and Bragg layers.

## Result

For the supplied one-vacancy path, the signed 15-residue link labels have an exact five-site reduction after applying the Casimir polynomial (f(m)=m(m+1)). On the bulk scale (u=h/S), this gives the primitive frozen-cell bands

\[
 E_\ell(u,\theta)=2(1-u^2)-2(1-u^2)\cos\!\left(\frac{\theta+2\pi\ell}{5}\right),
 \qquad \ell=0,\ldots,4.
\]

The period-three character (V|n\rangle=e^{2\pi i n/3}|n\rangle) shifts the five-cell Fourier fiber by (4\pi/3\) and sends a plane wave of physical momentum (k) to (k+2\pi/3). Consequently the principal energy difference in the period-three readout is

\[
 \Delta(u,k)=E(u,k+2\pi/3)-E(u,k)
 =2\sqrt3(1-u^2)\sin(k+\pi/3).
\]

On \(-1<u<1\), modulo (2\pi) in (k), its only joint stationary points are \((0,\pi/6)\) and \((0,7\pi/6)\). Both are nondegenerate, with Hessian determinants equal to \(24\). The phase-equality points \(k=-\pi/3,2\pi/3\) are different: there \(\Delta=0\) but \(\partial_k\Delta\ne0\). These are local frozen-symbol facts. They do not prove decay or a limit for the actual readout.

## Exact operator coefficients

Assume the supplied path coordinate (n\in I_S=[-5S,5S-4]\), (C=S(S+1)), and the canonical signed edge-label tables in [the zero-mode note](ZERO_MODE_AND_GOEGENBAUER_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md). Write (n=5h+s), (s\in\{0,1,2,3,4\}), and

\[
 (\ell_s)=(0,1,0,1,1),\qquad
 (\rho_s)=(0,0,0,1,0),\qquad
 (\pi_s)=(-1,0,0,0,1).
\]

To see that the reduction holds for every edge, split each ray into 15-residue blocks. On the positive ray the raw labels in the supplied table are the five-site offsets plus the block shift; on the negative ray each raw label is the reflected value -m-1 of the corresponding positive-offset label. The identity f(m)=f(-m-1) therefore reduces both rays to the 15 residue classes in the supplied tables. This is an exact Casimir identity, not an equality of the signed raw labels.
For every integer (n=5h+s), direct substitution in the positive and negative 15-residue tables, using (f(m)=f(-m-1)) on the reflected side, gives the exact identities

\[
 f(m_L(n))=f(h+\ell_s),\quad
 f(m_R(n))=f(h+\rho_s),\quad
 f(m_R(n-1))=f(h+\pi_s).
\]

Here (m_L,m_R) are the two supplied effective edge labels. The identities are for their Casimir values; the raw signed labels themselves need not equal the displayed five-site labels. For (M_S=A_S^*A_S) and (N_S=JM_SJ), the exact Jacobi entries are therefore

\[
 (N_S)_{n,n}=2-\frac{f(h+\ell_s)+f(h+\pi_s)}{C},
\]

\[
 (N_S)_{n,n+1}=-\sqrt{\left(1-\frac{f(h+\ell_s)}{C}\right)
                           \left(1-\frac{f(h+\rho_s)}{C}\right)}.
\]

The second formula applies when both path sites (n,n+1) exist. The sign is the conjugation by (J|n\rangle=(-1)^n|n\rangle).

For (a\in\{-1,0,1\}) and (u=h/S\), one has the exact scalar identity

\[
1-\frac{f(h+a)}{C}
=1-u^2+\frac{\alpha_a(u)}{S}
-\frac{(u-a)(u-a-1)}{S^2(1+S^{-1})},
\qquad \alpha_a(u)=u^2-u(2a+1).
\]

Fix \(\varepsilon>0\). For \(|u|\le1-\varepsilon\), the leading value (w=1-u^2) is bounded below, so Taylor expansion of the square root has a uniform (O_\varepsilon(S^{-2})) remainder. The diagonal and positive-link expansions are

\[
 (N_S)_{n,n}=2w+S^{-1}d_s(u)+O_\varepsilon(S^{-2}),\qquad
 d_s=(2u^2,2u(u-2),2u(u-1),2u(u-2),2u(u-3))_s,
\]

\[
 -(N_S)_{n,n+1}=w+S^{-1}b_s(u)+O_\varepsilon(S^{-2}),\qquad
 b_s=(u(u-1),u(u-2),u(u-1),u(u-3),u(u-2))_s.
\]

These expansions include a neighborhood of (u=0). The excluded layers are the electric endpoints (|u|\to1), where (w\to0) and this square-root expansion is not uniform.

In the five-cell fiber theta, the first-subprincipal matrix N_1 has diagonal d_s, residue links (N_1)_(s,s+1)=(N_1)_(s+1,s)=-b_s for s=0,...,3, and wrap entries (N_1)_(0,4)=-b_4 exp(-i theta), (N_1)_(4,0)=-b_4 exp(i theta); all other entries vanish.

## Primitive-cell symbol and character action

Freeze (u), write (\psi_{h,s}) for the five components in each cell, and use

\[
 \widehat\psi_s(\theta)=\sum_{h\in\mathbb Z}e^{-ih\theta}\psi_{h,s}.
\]

The principal (5\times5) matrix has diagonal (2w), entries (-w) between neighboring residues, and wrap entries
\(\mathcal N_{0,4}=-we^{-i\theta}\), \(\mathcal N_{4,0}=-we^{i\theta}\). Its eigenvectors are (v_s=e^{iqs}/\sqrt5) with (q=(\theta+2\pi\ell)/5), giving the five bands stated above.

Let (\omega=e^{2\pi i/3}). Since \(\omega^{5h+s}=\omega^s e^{4\pi i h/3}\), multiplication by (V) obeys the exact Fourier identity

\[
 \widehat{(V\psi)}(\theta)
 =\operatorname{diag}(1,\omega,\omega^2,1,\omega)\,
   \widehat\psi(\theta-4\pi/3).
\]

Equivalently, it sends physical momentum (k) to (k+2\pi/3): the coarse-cell momentum shifts by (10\pi/3\equiv4\pi/3\), and the internal band index advances by one when the shifted coarse momentum is kept unwrapped; reducing it modulo 2pi may relabel that band. Subtracting the frozen energies at those two physical momenta gives \(\Delta\) above. For the target state (e^{-iG_S/4}|0\rangle\), (G_S=N_S^2-CN_S), the leading (O(C)) phase difference is (-C\Delta/4); the bounded (N_S^2/4) term and all (1/S) coefficient corrections remain relevant to a global estimate.

The five-cell bands have same-fiber degeneracies at theta=0, for band pairs (1,4) and (2,3), and at theta=pi, for (0,4) and (1,3), with indices 0 through 4. The criterion is cos(q_l)=cos(q_j) exactly when q_j=-q_l modulo 2pi. Compressing the first-subprincipal matrix onto each crossing pair gives the following exact 2 by 2 matrices. Define r_plus=sqrt(10+2sqrt(5)) and r_minus=sqrt(10-2sqrt(5)); each matrix is [[mu,z],[conj(z),mu]]. The principal-slope column gives the positive magnitude of the frozen eigenvalue-difference derivative with respect to theta, and the frozen-cell-gap column gives the eigenvalue splitting of N_S with its O_epsilon(S^-2) remainder.

| Fiber boundary | Band pair | mu(u) | z(u) | Principal slope | Frozen-cell gap |
|---|---|---|---|---|
| theta=0 | (1,4) | u*((25-5sqrt(5))*u-41+9sqrt(5))/10 | u*(2+i*(r_plus-r_minus))/5 | w*sqrt(10+2sqrt(5))/5 | 4*(sqrt(5)-1)*abs(u)/(5S)+O_epsilon(S^-2) |
| theta=0 | (2,3) | u*((25+5sqrt(5))*u-41-9sqrt(5))/10 | u*(2+i*(r_plus+r_minus))/5 | w*sqrt(10-2sqrt(5))/5 | 4*(sqrt(5)+1)*abs(u)/(5S)+O_epsilon(S^-2) |
| theta=pi | (0,4) | u*((15-5sqrt(5))*u-23+9sqrt(5))/10 | 2*u*(3-sqrt(5))/5 | w*sqrt(10-2sqrt(5))/5 | 4*(3-sqrt(5))*abs(u)/(5S)+O_epsilon(S^-2) |
| theta=pi | (1,3) | u*((15+5sqrt(5))*u-23-9sqrt(5))/10 | 2*u*(3+sqrt(5))/5 | w*sqrt(10+2sqrt(5))/5 | 4*(3+sqrt(5))*abs(u)/(5S)+O_epsilon(S^-2) |

Here w=1-u^2, and sigma is the positive magnitude of the principal eigenvalue-difference slope at the crossing. The entries mu and z are the common diagonal and off-diagonal entries of the compression; the last column gives the frozen-cell eigenvalue splitting of N_S with its uniform remainder. With delta_theta=theta-theta_c and the basis ordered by slope sign, the local two-mode matrix is

    E_c*I + (sigma*delta_theta/2)*diag(1,-1) + (1/S)*[[mu,z],[conj(z),mu]]
      + O(delta_theta^2 + abs(delta_theta)/S + S^-2),

uniformly for u in a compact subset of |u|<1. At u=0, both mu and z vanish in all four compressions, so the first-order Bragg gaps close at the central layer. The readout cross-phase is also stationary at u=0, at different momenta. This identifies why isolated-band transport cannot simply be continued through the center; the central connection remains open.

These are local frozen-cell splittings; at fixed nonzero u, their contribution to the leading C/4 generator phase is order S*abs(u). They are distinct from the cross-fiber equal-energy points Delta=0. Neither calculation determines the global moving-coefficient scattering or the prepared-state weight at a crossing.
The principal lobe action of the leading symbol is 5pi(2-sqrt(lambda)) in the physical path coordinate for 0 < lambda < 4, derived below. This is not a quantization or propagation result.

## First-order scalar band correction

The selected plane wave of physical momentum k has internal vector v_s=exp(i k s)/sqrt(5) and five-cell fiber theta=5k modulo 2pi. Its Rayleigh correction from the first-subprincipal matrix is

    <v,N_1(u,theta)v> = (sum_s d_s(u) - 2*cos(k)*sum_s b_s(u))/5
                      = 2*u^2*(1-cos(k)) + u*(18*cos(k)-16)/5.

At fixed eigenvalue lambda, the local five-cell phase increment theta=5k therefore shifts by

    delta_theta = -5*nu_1(u,k)/(2*(1-u^2)*sin(k)*S) + O(S^-2).

This follows by implicit differentiation of the nondegenerate frozen band. It applies only away from sin(k)=0 and the same-fiber Bragg crossings. It is the first local transfer correction in the stated cell coordinate, not an accumulated global transport estimate.

Where the principal band is nondegenerate, this is its first-order eigenvalue correction in the fixed coordinate u=h/S. At a same-fiber crossing, use the two-dimensional compressed matrices above instead; the scalar correction alone does not resolve the crossing.

## Principal action and cell-coordinate scale

For a frozen eigenvalue 0 < lambda < 4, the positive-x superlevel lobe of nu(x,k)=4(1-x^2)sin^2(k/2) has turning point a=sqrt(1-lambda/4). At each x in [0,a], its k-width is 2(pi-k0(x)), where k0(x)=2 arcsin(sqrt(lambda)/(2sqrt(1-x^2))). Its phase-space area in the cell coordinate x=h/S is

    A_plus(lambda)=2 integral_0^a [pi-2 arcsin(sqrt(lambda)/(2sqrt(1-x^2)))] dx.

The boundary integrand vanishes at x=a. Differentiating for 0<lambda<4 gives

    A_plus'(lambda)=-1/sqrt(lambda) integral_0^a dx/sqrt(a^2-x^2)=-pi/(2sqrt(lambda)),

using x=a sin(t), so the integral is pi/2. Since A_plus(0+)=2pi, integration yields A_plus(lambda)=pi(2-sqrt(lambda)). The physical path coordinate is y=n/S=5x, so the corresponding principal action area in physical-site units is

    A_phys(lambda)=5 A_plus(lambda)=5pi(2-sqrt(lambda)).

This confirms the principal action and its factor of five from the exact five-site symbol. It is only a classical lobe area: no quantization condition, subprincipal phase, or finite-spin phase error follows from it.

## Stationary-set proof and scope

The derivatives are

\[
 \partial_u\Delta=-4\sqrt3\,u\sin(k+\pi/3),\qquad
 \partial_k\Delta=2\sqrt3(1-u^2)\cos(k+\pi/3).
\]

On \(|u|<1\), simultaneous vanishing forces \(\cos(k+\pi/3)=0\), hence the sine is nonzero and then (u=0). This gives exactly the two points listed above. At either point the mixed Hessian entry vanishes; the diagonal entries are ((-4\sqrt3,-2\sqrt3)) at (k=\pi/6) and ((4\sqrt3,2\sqrt3)) at (k=7\pi/6), so the determinants are (24).

The result is conditional on the supplied path, hop factors, signed labels, generator and readout. It proves no propagation estimate for the slowly varying finite matrix over time C/4, no control through the same-fiber Bragg layers, no central-layer matching, no endpoint-tail bound for this long-time evolution, and no limit or separated subsequences for the actual readout. In particular, a stationary-phase argument on this frozen symbol alone does not close the target. The supplied model and initial/output maps are not derived from the framework's four axioms; this note gives no reason to update those axioms.

## Imports and source status

| Role | Imported input | Provenance | Open bridge |
|---|---|---|---|
| Coefficient model | One-vacancy path, integer-spin link factors and signed edge labels | The [fast-vacancy note](FAST_VACANCY_MOTION_AFTER_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md) and [zero-mode note](ZERO_MODE_AND_GOEGENBAUER_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md), tracked at the source base recorded below | The four axioms do not select this Hamiltonian or its integer-spin representation. |
| Preparation and readout | First-mark output and period-three observable, reduced to V and V* in the [exact-side note](POSTMARK_ELECTRIC_EXACT_SIDE_FIXED_INDEX_KERNEL_BOUNDED_THEOREM_NOTE_2026-09-24.md) | Conditional six-site model and output convention in the [core and boundary note](POSTMARK_ELECTRIC_CORE_AND_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-24.md) | Their physical identification and axiom derivation remain open. |
| Framework boundary | The current four axioms and registered-primitive qualification in [Minimal Axioms](MINIMAL_AXIOMS_2026-06-29.md) | Tracked source at the current campaign base | This note supplies no new axiom or primitive and establishes no bridge from those axioms to the imported model. |
| Mathematical tools | Finite-dimensional Bloch diagonalization, exact Casimir algebra and a uniform Taylor expansion where 1-u^2 is bounded below | Derived explicitly above from the displayed hypotheses | No global spectral theorem or propagation result is imported or asserted. |

## Machine status and trace

    actual_current_surface_status: conditional-support
    target_claim_type: bounded_theorem
    trace_class: upstream_support
    target_claim_id: postmark_electric_core_and_boundary_bounded_theorem_note_2026-09-24
    target_blocker_text: "joint finite-spin electric limit"
    source_of_blocker_text: handoff
    reachability_to_target: supports
    conditional_surface_status: "Conditional on the supplied finite-spin one-vacancy path, hop factors, signed labels, generator, preparation, and period-three readout."
    hypothetical_axiom_status: null
    admitted_observation_status: null
    claim_type_reason: "The exact coefficient reduction, local frozen-symbol identities, first-order crossing matrices, non-crossing scalar correction and classical action are bounded mathematical results under supplied model inputs; global propagation and the framework bridge remain open."
    audit_required_before_effective_retained: true
    bare_retained_allowed: false
    artifact_role: theorem
    next_trace_action: "Use the first-order five-cell symbol and crossing matrices to test uniform transport through the central and Bragg layers; then bound the actual weighted inter-fiber phase correlation or prove separated actual-readout subsequences."

This support note feeds the conditional fixed-time readout question in the [core and boundary note](POSTMARK_ELECTRIC_CORE_AND_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-24.md) and [exact-side note](POSTMARK_ELECTRIC_EXACT_SIDE_FIXED_INDEX_KERNEL_BOUNDED_THEOREM_NOTE_2026-09-24.md). Its conclusion is local to the frozen principal symbol and adds no independent endpoint or propagation estimate. No formal audit is claimed.

## Verification

The paired deterministic runner checks the signed Casimir identities on 2,001 consecutive edge labels, compares exact coefficients with the physical-hop enumerator on five sentinel spins, verifies the five-by-five Bloch eigenvalues and period-three Fourier shift, checks the noncrossing first-order scalar correction, and checks all four crossing compressions and principal slope magnitudes as exact algebraic identities. Each compressed entry is a polynomial of degree at most two in u; the runner checks exact algebraic zero at u=0, 1, and 2, which verifies the polynomial identity. For the action formula it checks the auxiliary arcsine integral and radicand identity used in the displayed differentiation; the physical-site factor follows from y=5x in the note's derivation. It also checks the symbolic stationary-point Hessians. A finite frozen-cell comparison at S=100, 200, 400, and 800 corroborates the compact-bulk O(S^-2) eigenvalue remainder only at the sampled u and theta values; it is not part of the proof of uniformity. These are reproducibility checks of the displayed bounded algebra, not independent review or evidence for global finite-spin propagation. Source base: 0e6ad8285096ed668816f18caaa6fbbfbd9c50e8.

```bash
python3 scripts/postmark_electric_five_site_inter_fiber_phase_2026_09_24.py
```


## Review scope and recovery

The complete conditional proofs above remain the scientific source. Historical
revision/hash statements and dated numerical values describe the author snapshot;
current execution is bound to the source and actual current inputs in the paired
runner cache. No historical seal or audit output grants authority.
The original PR branches preserve the full campaign packet, failed attempts,
Schur/pole probes, weighted lag decompositions and large-spin diagnostics.
Their broader fixed-time cancellation target remains open. No finite sample or
principal counting law supplies the missing phase-accurate weighted estimate.

- **N1 — Domain:** supplied integer-spin one-vacancy matrix, preparation and stated limit order.
- **N2 — Alternatives:** other preparations, laws and cancellation methods remain possible.
- **N3 — Imports:** model, Hilbert kinematics and readout are supplied, not native premises.
- **N4 — Dependencies:** linked current sources govern; no retained grade is inherited.
- **N5 — Resolution:** finite floating diagnostics corroborate algebra, not asymptotic certification.
- **N6 — Residual:** the interior two-energy phase sum remains unresolved.
- **N7 — Counterroute:** failure of a sufficient kernel or termwise approximation would not alone refute readout convergence.
- **N8 — Authority:** source review only; no audit verdict or framework admission.
