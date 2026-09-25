---
claim_id: postmark_electric_principal_weyl_count_2026_09_24
claim_type: bounded_theorem
claim_scope: Conditional on the supplied finite-spin one-vacancy Jacobi family and its exact signed Casimir coefficients,
  the normalized empirical spectral measures converge to dmu(lambda)=1_(0,4)(lambda) d lambda/(4 sqrt(lambda));
  equivalently, the limiting eigenvalue counting fraction is sqrt(lambda)/2. This controls macroscopic eigenvalue
  quantiles but gives no adjacent-gap, phase-modulo-2pi, propagation, or readout limit.
upstream_dependencies:
- postmark_electric_five_site_inter_fiber_phase_2026_09_24
runner: scripts/postmark_electric_principal_weyl_count_2026_09_24.py
---

# Principal Weyl law for the supplied electric Jacobi family

**Date:** 2026-09-24
**Type:** bounded theorem
**Status:** proposed_retained

## Exact target

For the supplied finite-spin Jacobi matrix (N_S=JM_SJ) on
(I_S=[-5S,5S-4]), prove convergence of its normalized empirical spectral
measure and derive the limiting eigenvalue counting fraction. Do not infer a
local spacing law or a fixed-time dynamical limit from this distribution.

## Result

Let (D_S=10S-3), and let (lambda_{0,S}lecdotslelambda_{D_S-1,S})
be the eigenvalues of (N_S), counted with multiplicity. Under the supplied
signed-label and hop-factor identities in the five-site note, the empirical
measures

\[
 \mu_S=\frac1{D_S}\sum_{j=0}^{D_S-1}\delta_{\lambda_{j,S}}
\]

converge weakly to

\[
 d\mu(\lambda)=\frac{\mathbf 1_{(0,4)}(\lambda)}{4\sqrt{\lambda}}\,d\lambda.
\]

Thus, for (0\le\lambda\le4),

\[
 \lim_{S\to\infty}\frac1{D_S}\#\{j:\lambda_{j,S}\le\lambda\}
 =\frac{\sqrt\lambda}{2}.
\]

For any sequence of indices with (j_S/D_S\to\rho\in[0,1]),

\[
 \lambda_{j_S,S}\longrightarrow4\rho^2,
 \qquad
 \frac{C\lambda_{j_S,S}}{4S^2}\longrightarrow\rho^2.
\]

The last statement is only a macroscopic phase profile. It does not control
the phase modulo (2\pi), differences between neighboring eigenvalues, or
the prepared-weighted two-energy sum.

## Proof

Write (n=5h+s), (s\in\{0,1,2,3,4\}), and (x=n/(5S)). The exact
diagonal and link formulas in the five-site note give, on every compact
subinterval (|x|\le1-\varepsilon),

\[
 (N_S)_{n,n}=2(1-x^2)+O_\varepsilon(S^{-1}),\qquad
 (N_S)_{n,n+1}=-(1-x^2)+O_\varepsilon(S^{-1}),
\]

uniformly in the five residues (s). Replacing (h/S) by (n/(5S))
changes the leading coefficient by (O(S^{-1})). The exact-side note gives
the global positive-semidefinite and row-sum bounds

\[
 0\le N_S,\qquad \|N_S\|\le4+24/S.
\]

Fix a nonnegative integer (m). For a site (n) at distance more than
(m) from the path endpoints, ((N_S^m)_{n,n}) is a sum over the finitely
many closed nearest-neighbor walks of length (m) based at (n). If
(|x|\le1-\varepsilon), every coefficient encountered along such a walk
differs from its frozen value by (O_{m,\varepsilon}(S^{-1})). The frozen
Jacobi operator has diagonal (2w) and both off-diagonals (-w), where
(w=1-x^2). Its Fourier symbol is

\[
 \nu(x,k)=2w-2w\cos k=4(1-x^2)\sin^2(k/2).
\]

The closed-walk sum is the zero Fourier coefficient, so uniformly on that
compact bulk,

\[
 (N_S^m)_{n,n}
 =\frac1{2\pi}\int_0^{2\pi}\nu(x,k)^m\,dk
 +O_{m,\varepsilon}(S^{-1}).
\]

The fraction of sites in the excluded endpoint strips is (O(\varepsilon)).
The global norm bound controls their normalized trace contribution by
(O_m(\varepsilon)). Summing the bulk diagonal entries is a Riemann sum
with (D_S\sim10S); first let (S\to\infty), then
(\varepsilon\downarrow0). It follows that

\[
 \lim_{S\to\infty}\frac1{D_S}\operatorname{Tr}(N_S^m)
 =\frac12\int_{-1}^{1}\frac1{2\pi}\int_0^{2\pi}
       [4(1-x^2)\sin^2(k/2)]^m\,dk\,dx.
\]

The momentum integral is
\(\binom{2m}{m}(1-x^2)^m\), and integrating this full expression over normalized x gives
(4^m/(2m+1)); the binomial prefactor is included. Therefore

\[
 \lim_{S\to\infty}\int\lambda^m\,d\mu_S(\lambda)
 =\frac{4^m}{2m+1}
 =\int_0^4\lambda^m\frac{d\lambda}{4\sqrt\lambda}.
\]

All measures are supported in a common compact interval by the norm bound.
Polynomial approximation of continuous functions on that interval upgrades
moment convergence to weak convergence. The limiting measure has a
continuous, strictly increasing distribution function
\(F(\lambda)=\sqrt\lambda/2\) on ([0,4]). Convergence of its quantiles
gives the eigenvalue-index and normalized-phase conclusions for interior
fractions 0<rho<1. At rho=0, positivity supplies the lower bound and
comparison with any fixed interior fraction gives limsup zero. At rho=1,
the upper bound ||N_S||<=4+24/S and comparison with interior fractions
give convergence to 4. Thus endpoint quantiles are covered too.

## Relation to the alias campaign

The exact lobe area in the [five-site inter-fiber note](POSTMARK_ELECTRIC_FIVE_SITE_INTER_FIBER_PHASE_BOUNDED_THEOREM_NOTE_2026-09-24.md)
is (A_+(\lambda)=\pi(2-\sqrt\lambda)). Its superlevel volume gives the
same phase-space distribution. Inverting the limiting count suggests the
smoothed profile

\[
 \lambda_j\approx\left(\frac{j}{5S}\right)^2,
 \qquad
 \frac{C\lambda_j}{4}\approx\frac{S+1}{100S}j^2.
\]

This explains why the sampled one-index phase slopes have O(S) alias
integers. The Weyl theorem proved here is a macroscopic distribution result;
it does not justify differentiating the asymptotic counting function to
obtain individual level spacings. It gives no uniform WKB quantization,
subprincipal phase, alias-summed cancellation, or readout limit.

## Proof dependency and status

| Obligation | Status | Evidence |
|---|---|---|
| Exact finite-spin Jacobi family and bulk coefficients | Imported, conditional | Five-site note and exact-side note at the stated source base |
| Uniform spectral support | Imported, proved | Exact-side note's global row-sum and positivity bound |
| Fixed-moment trace limit | Proved here | Closed nearest-neighbor walks, compact-bulk freezing, and endpoint-strip rank fraction |
| Limiting density and quantile profile | Proved here | Exact moment evaluation and compact-support moment convergence |
| Individual spacings, phase modulo (2\pi), weighted readout | Open | Not implied by weak spectral convergence |

This is conditional mathematics for the supplied finite-spin dynamics. It
does not derive the Hamiltonian, preparation, or output map from the four
framework axioms and supports no axiom update. Formal retained status remains
with the independent audit path.

```yaml
trace_class: upstream_support
target_claim_id: postmark_electric_core_and_boundary_bounded_theorem_note_2026-09-24
target_blocker_text: "joint finite-spin electric limit"
source_of_blocker_text: handoff
reachability_to_target: supports
conditional_surface_status: "Conditional on the supplied finite-spin one-vacancy Jacobi family, exact signed edge labels, and hop factors."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The empirical spectral measure follows from fixed-moment trace convergence; local eigenvalue spacings and the target readout remain open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
artifact_role: theorem
next_trace_action: "Obtain phase-accurate global quantization and prepared overlap estimates that sum all nonzero reciprocal aliases in the fixed-time two-energy readout."
```

## Verification

The paired runner computes exact finite Jacobi spectra and checks the first
nine empirical moments against the limiting formula for several spins. These
finite comparisons reproduce the theorem's limiting moments only
asymptotically and are corroboration, not a proof of the weak limit or a
local-spacing estimate. Source base: `0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`.

```bash
python3 scripts/postmark_electric_principal_weyl_count_2026_09_24.py
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
