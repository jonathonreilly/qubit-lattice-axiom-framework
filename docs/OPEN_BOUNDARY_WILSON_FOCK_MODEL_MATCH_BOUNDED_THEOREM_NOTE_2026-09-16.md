---
claim_id: open_boundary_wilson_fock_model_match_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
runner: scripts/open_boundary_wilson_hamiltonian_check_2026_09_16.py
claim_scope: "Supplied finite spatial Wilson model; exact open-boundary Fock amplitude and fixed-graph continuous-time match."
upstream_dependencies: ["temporal_wilson_resummation_physical_curl_bounded_theorem_note_2026-09-16"]
---

# Exact open-boundary determinant and its canonical fermion model

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

This is a conditional normalization and boundary-condition join for the supplied Wilson operator. Wilson transfer matrices, dimensional reduction and exterior-power factorization are established machinery. The purpose is to identify exactly which fermionic boundary amplitude the physical curl estimate controls. No audit or compact phase is claimed.

Primary prior art: [Luescher, DESY76/54](https://bib-pubdb1.desy.de/record/396349/files/7611148.pdf?version=1) constructs positive Wilson fermion/gauge transfers and tracks field normalization. [Wenger, arXiv2302.07385](https://arxiv.org/html/2302.07385) explains determinant reduction and canonical minor factorization. [Buividovich-Hind, arXiv2606.20090v1](https://arxiv.org/html/2606.20090v1) gives the anisotropic Wilson-Dirac block transfer and its Hamiltonian expansion; its no-temporal-clover specialization is the same block mechanism used below. Neither generic determinant reduction nor this block mechanism is presented as newly discovered here. The open endpoint prefactor and its connection to the particular temporal-resummation bound are derived explicitly.

Load-bearing model-definition and normalization parent: [TEMPORAL_WILSON_RESUMMATION_PHYSICAL_CURL_BOUNDED_THEOREM_NOTE_2026-09-16.md](TEMPORAL_WILSON_RESUMMATION_PHYSICAL_CURL_BOUNDED_THEOREM_NOTE_2026-09-16.md). The parent supplies the spatial Wilson operator and open temporal determinant normalization used here. This algebraic model match requires only m>0; the stronger m>3kappa hypothesis for the parent's uniform physical-curl estimates is not assumed as necessary for this result.

## 1. Spatial blocks and positive recurrence transfer

Fix a finite free spatial graph as in the temporal-resummation note and temporal gauge on an open time interval. This gauge can always be reached by successively transporting vertex phases along the open temporal chains. The determinant is unchanged by that gauge conjugation. Let r=2|Lambda_s|; each gamma_0 eigenspace has dimension r. For a supplied spatial gauge history write

    mu-K_s(t)=[a_t,b_t;-b_t*,d_t],
    h_t=gamma_0(mu-K_s(t))=[a_t,b_t;b_t*,-d_t].       (1)

The star denotes Hermitian adjoint. The identity gamma_0 K_s gamma_0=K_s* follows by anticommuting gamma_0 through each spatial Wilson projector and exchanging the forward/reverse shift. Hence a_t,d_t are Hermitian and h_t is Hermitian. Compression to either gamma_0 block replaces a spatial projector by I/2, so a_t,d_t>=mI. Their traces are mu r because open spatial shifts have zero diagonal. Also ||h_t||<=mu+3kappa and its spectrum avoids(-m,m), since ||(mu-K_s)f||>=m||f||.

For one time step define A_t=I+delta a_t, B_t=delta b_t, C_t=-B_t*, and D_t=I+delta d_t. The dimensionless full Dirac matrix delta D_full has equations

    f_t=A_t u_t+B_t v_t-u_(t+1),
    g_t=C_t u_t+D_t v_t-v_(t-1),

with u_(M_t)=0 and v_(-1)=0. The homogeneous recurrence is

    [u_(t+1);v_t]=X_t[u_t;v_(t-1)],
    X_t=[A_t+B_t D_t^-1 B_t*,B_t D_t^-1;
                            D_t^-1 B_t*,D_t^-1].   (2)

It is positive Hermitian because

    X_t=[I,B_t;0,I] diag(A_t,D_t^-1)[I,0;B_t*,I].   (3)

This is a recurrence transfer with X_t=I+delta h_t+O(delta^2). The plus sign is retained until complementary minors identify the physical evolution. Inverses exist for all delta>0 under m>0; the expansion is uniform over gauge angles on a fixed graph.

## 2. Determinant prefactor from actual elimination

Put X=X_(M_t-1)...X_0. The exact identity is

    det(delta D_full)=product_t det D_t * det X_(++).            (4)

Here the plus block is taken on the fixed gamma_0 subspace. To prove the prefactor rather than merely identify zeros, first reorder all u variables together and all v variables together, with the same permutation of rows and columns. The v-v block is lower bidiagonal in time with diagonal D_t, so its determinant is product det D_t. Schur elimination leaves an operator S on the u variables with rows

    f_t=sum_(s<=t)R_(t,s)u_s-u_(t+1),

where u_(M_t)=0. Introduce coordinates z=(u_0,f_0,...,f_(M_t-2)). The map from(u_0,...,u_(M_t-1)) to z is block lower triangular, with diagonal I,-I,...,-I, and determinant(-1)^(r(M_t-1)). With the first M_t-1 residuals set to zero, the recurrence(2) gives f_(M_t-1)=X_(++)u_0. Therefore in z coordinates S has its first M_t-1 rows selecting those residuals, and its final row X_(++)u_0 plus a linear combination of them. Moving that last block row to the front has sign(-1)^(r^2(M_t-1))=(-1)^(r(M_t-1)). The two signs cancel. Thus det S=det X_(++), proving(4), including its multiplicative factor. One time slice reduces to the ordinary Schur complement.

This proof does not infer a prefactor from equality of zero sets. It also does not require commuting time slices or an invertible intermediate plus minor.

## 3. Complementary minors and the boundary state

Equation(3) gives det X_t=det A_t/det D_t. The complementary-minor identity for the invertible X gives

    det(delta D_full)=product_t det A_t * det((X^-1)_(--)).     (5)

The inverse X^-1=X_0^-1...X_(M_t-1)^-1 has the opposite order from physical forward time. Since every X_t is Hermitian,

    Y=X_(M_t-1)^-1...X_0^-1=(X^-1)*,

so the moduli of the two negative-sector minors agree. This adjoint identity, rather than a commutation assumption, is why the paired determinant can be written with the chronological product Y.

Let Fock be the full fermion exterior algebra over the2r spatial one-particle modes. For an invertible positive matrix S, Gamma(S) is the direct sum of its exterior powers, a positive operator on Fock. Let Omega_- fill precisely the r negative gamma_0 modes. Cauchy-Binet, or directly the definition of the exterior power, gives

    <Omega_-|Gamma(Y)|Omega_->=det Y_(--).

Define the exact positive one-slice Fock operator

    F_delta(theta_t)=c_delta(theta_t) Gamma(X_t^-1),
    c_delta(theta_t)=det A_t/(1+mu delta)^(2r)>0.     (6)

The normalization in the temporal-resummation note is det(delta D_0)=(1+mu delta)^(2rM_t). Equations(5)-(6) prove the exact finite identity

    |det(D_full D_0^-1)|^2
      =|<Omega_-|F_delta(theta_(M_t-1))...
                              F_delta(theta_0)|Omega_->|^2.   (7)

The scalar c_delta is part of this identity. Its numerator is generally gauge dependent at finite delta and cannot be silently discarded. Equation(7) is a specified boundary amplitude, not a thermal trace and not a ground-state expectation.

## 4. The supplied continuous-time Hamiltonian

Since Tr a_t=mu r,

    c_delta=1-delta mu r+O_graph(delta^2),
    Gamma(X_t^-1)=I-delta dGamma(h_t)+O_graph(delta^2).

Here dGamma(h)=sum c_i* h_(i,j)c_j is the usual number-conserving quadratic Fock operator. These are norm expansions on a fixed finite Fock space, uniformly over spatial gauge angles. Consequently

    F_delta(theta)=I-delta H_F(theta)+O_graph(delta^2),
    H_F(theta)=dGamma(gamma_0(mu-K_s(theta)))+mu r I. (8)

H_F is Hermitian and a finite Laurent polynomial in the link variables. The shift mu r is fixed by the chosen temporal normalization. At K_s=0, the energy of Omega_- under dGamma(mu gamma_0) is-mu r, so its H_F energy is zero and(7) equals1. H_F need not be nonnegative when spatial hopping is restored; a further declared scalar shift can make a finite-graph transfer contractive if needed.

For a continuous external spatial gauge history, delta M_t->T and samples converging uniformly to that history, the bounded-matrix product estimate obtained by telescoping one-step errors gives

    F_delta(theta_(M_t-1))...F_delta(theta_0)
        -> Texp[-integral_0^T H_F(theta(t))dt]        (9)

in norm. For a merely continuous history, first approximate it uniformly by a piecewise constant one, use uniform continuity of H_F and the exponential bound on products, and then use the O(delta^2) local error on each constant interval. Lipschitz histories also give the usual fixed-graph O(delta) rate. No spatial-volume-uniform Fock operator-norm rate follows from this finite-dimensional argument.

Thus(7) converges to the squared modulus of the boundary amplitude of(9). The70-dimensional explicit CAR check verifies this conclusion against the reduced one-particle minor for a time-varying, noncommuting two-site history. It also checks finite-delta identity(7) by exterior powers and the full time-Dirac matrix.

## 5. Positive paired matter and gauge covariance

On Fock tensor its conjugate space define

    F_pair(theta)=F_delta(theta) tensor conjugate(F_delta(theta)),
    Omega_pair=Omega_- tensor conjugate(Omega_-).

This is positive Hermitian, and its chronological boundary amplitude is exactly the right side of(7). Its first-order generator is

    H_pair(theta)=H_F(theta) tensor I+I tensor conjugate(H_F(theta)).

Gauge transformations act by Gamma(S_chi) on the first factor and its conjugate on the second, so the local charge is n_first-n_second. Omega_pair has zero such charge at each spatial site: each factor fills two spin modes there. This is an explicit supplied conjugate-pair realization of the positive determinant weight. It does not infer a physical flavor content from the axioms. The Hamiltonians are even in the fermions, so this tensor representation is equivalent to the corresponding even operators of two-flavor CAR.

Each X_t, its block determinants and F_delta transform covariantly under spatial gauge transformations. Hence the same is true of F_pair, including for finite-cyclic links. This supplies a genuine finite-dimensional, gauge-compatible matter multiplier for a later gauge transfer construction.

## 6. What this match closes

The temporal-resummation note's uniform physical-curl bounds concern exactly the boundary weight(7), with its scalar normalization and filled boundary state now identified. They do not yet describe a thermal trace, arbitrary fermionic insertions, a gapless-matter determinant or a large-volume ground-state phase. The companion `OPEN_WILSON_GAUGE_MATTER_FIXED_GRAPH_STATE_JOIN_BOUNDED_THEOREM_NOTE_2026-09-16.md` (context only) supplies the gauge transfer weights, endpoint factors and physical Gauss restriction explicitly; they are not inferred from the determinant alone. Its fixed-volume regulator/state limits depend on the supplied variance-calibrated transfer and all-mode state proofs.

The mathematical machinery in this note is classical and the generic anisotropic block transfer has direct prior art. The bounded result is the model/source/boundary match needed to interpret the preceding uniform-time estimate, not a claim to have discovered Wilson transfer theory.

## Evidence and execution boundary

Primary runner: `scripts/open_boundary_wilson_hamiltonian_check_2026_09_16.py`.

All original arithmetic, assertions, finite domains, seeds and tolerances are preserved. Each program retains its 180-second limit; memory limits and sole sequential captures are coordinator-owned and must be frozen before execution. `TOTAL: PASS=1 FAIL=0` means one complete diagnostic family finished all its original assertions, not one assertion or exhaustive physical coverage. Source and ordered owner/parent notes are read and hash-bound. JSON diagnostics are written under `logs/runner-cache/`.

The [historical recovery packet](work_history/repo/review_feedback/pr8163-evidence/README.md) preserves all original paths, modes, blobs, complete working derivations, two initial failures and 23 final formula-fault outcomes. Those historical runs are not current-source execution evidence.

## No-Go Discipline Gate

**N1 — Actual alternatives.** The preserved finite diagnostics and 23 specified formula faults test the stated algebra. Five future research routes are open alternatives, not completed attacks or exhaustive exclusions.

**N2 — Shared scope.** Results use the supplied massive Wilson/open-boundary model and its explicit finite-graph or physical-curl quantifiers; no independent-wall theorem is asserted.

**N3 — Inputs.** Model parameters, external time, gauge kernel, CAR representation and endpoint state are supplied. No framework premise selects them.

**N4 — Failed attempts.** The slow refinement failed its original factor-three target, and an initially equivalent orientation mutation survived; both failures and their exact subsequent source corrections remain preserved.

**N5 — Resolution.** Completed finite matrices, integer cycles or sampled directions support the corresponding algebra. They do not exhaust all graphs, native laws or physical spectra.

**N6 — Remaining routes.** Periodic winding, gapless matter, thermal identification, global ground-state selection and infinite-volume phase control remain open.

**N7 — Strongest boundary.** Volume-uniform heavy physical-curl estimates differ from fixed-graph state limits; an open amplitude is not a thermal trace or a global ground-state selection.

**N8 — Reopening.** New model matching, sector/overlap proofs or spatial-volume controls could resolve those extensions; the current result does not exclude them.
