---
claim_id: scale_ladder_gravity_d4cone_exact_ward_site_scalar_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "Exact local Laurent Ward identity and symmetric-stress segment map for a supplied nearest-neighbour scalar; full-carrier displacement cancellation. Separate finite-difference Regge exchange fits and selected-subspace diagnostics are finite numerical tests, not uniform continuum or partner-decoupling theorems."
upstream_dependencies:
  - kinetic_isotropy_primitive
  - minimal_axioms
runner: scripts/scale_ladder_gravity_d4cone_exact_ward_site_scalar_2026_10_18.py
---

# Exact site-scalar Ward algebra and finite D4-cone exchange diagnostics

Claim type: bounded_theorem.
Primary runner: `scripts/scale_ladder_gravity_d4cone_exact_ward_site_scalar_2026_10_18.py`.

The exact result below is local algebra on a supplied scalar and segment construction. The separate Regge calculations use finite-difference area/dihedral derivatives on a supplied 96-simplex, 72-edge-class D4-cone carrier. They test named finite momentum and derivative-step fixtures. Neither source review nor those fits establish a uniform Einstein–Hilbert continuum limit, universal absence of hidden curvature, a physical graviton or uniform partner decoupling.

The carrier has vertices at the integer and half-integer sites of `Z^4 union (Z^4+1/2)` and six deep-hole centers `(e_mu+e_nu)/2`; each Delaunay 16-cell is coned from its center. The resulting eight vertex types have 32 displacement columns. Index 3 is the supplied tick coordinate. The scalar occupies the integer-site species with nearest-neighbour symbol

    K0(k) = sum_mu (2 - 2 cos k_mu).

The triangulation, Regge action, scalar stencil, corner stress, segment map and face weight are supplied constructions. Their physical selection is not derived here. The actual axiom and kinetic-primitive sources delimit the framework context; no additional law is adopted.

## Exact off-shell identity and its on-shell consequence

For two modes `phi1 ~ exp(-i k1.x)` and `phi2 ~ exp(i k2.x)`, put

    x_mu = exp(-i k1_mu), y_mu = exp(i k2_mu),
    w_mu = 1/(x_mu y_mu), d_mu = y_mu-x_mu, u_mu=w_mu-1.

All Laurent variables are nonzero. Define `K0(z)=sum_mu(2-z_mu-z_mu^(-1))`. Direct expansion gives

    sum_mu u_mu d_mu
      = sum_mu (x_mu+x_mu^(-1)-y_mu-y_mu^(-1))
      = K0(y)-K0(x).

The symmetric corner tensor is

    S_mu,nu = -d_mu d_nu/4
              +[u_mu u_nu-delta_mu,nu sum_lambda u_lambda^2]/4.

The divergence of the square bracket vanishes identically, since its two terms are `u_nu sum_mu u_mu^2` with opposite signs. Therefore

    sum_mu u_mu S_mu,nu = -d_nu [K0(y)-K0(x)]/4.

This is an exact off-shell Laurent identity, including complex momenta; it is not inferred from random tests. On the common free shell `K0(k1)=K0(k2)` its divergence is zero. In particular both zero-shell modes satisfy it. The finite Laurent stencil makes locality explicit. The primary symbolically cancels each component and separately prints numerical complex-momentum residuals.

The leading continuum identification is on shell. With small momenta, `d=i(k1+k2)+O(k^2)` and `u=-i(k2-k1)+O(k^2)`. Thus

    S_mu,nu = (k1_mu k2_nu+k2_mu k1_nu)/2
                +delta_mu,nu (k2-k1)^2/4 + O(k^3).

On zero-shell families, `k1^2=k2^2=O(k^4)`, reducing the leading trace term to `-delta_mu,nu (k1.k2)/2`. This is the leading minimal scalar stress in this convention. The comparison used in the runner is

    u0=exp(-ik1)-1, v0=exp(ik2)-1,
    S_min=(u0 v0^T+v0 u0^T)/2-I(u0.v0)/2.

The three chosen scales test its relative difference. They do not establish a uniform error bound over all complex directions or near tensor zeros.

## Exact segment map and all carrier displacements

The four axis and twelve face segments have relative-strain rows, for the integer-site displacement,

    W_axis,mu = 2(w_mu-1)e_mu,
    W_plus,mn = (w_m w_n-1)(e_m+e_n),
    W_minus,mn = (w_m-w_n)(e_m-e_n).

For a symmetric corner tensor `T`, assign diagonal axis weight `T_nu,nu/2`. For each face `(m,n)`, assign plus/minus weights `+T_mn/2,-T_mn/2`, and add axis weights `-(w_n-1)T_mn/4` at m and `-(w_m-1)T_mn/4` at n. Multiplying these rows gives

    b(T).W = (w-1)^T T.

For example the face difference contributes `(w_n-1)(w_m+1)e_m/2` and `(w_m-1)(w_n+1)e_n/2`, while the axis corrections remove the unwanted factors, leaving `(w_n-1)e_m+(w_m-1)e_n`. Diagonal terms complete the divergence. The primary verifies the arbitrary symmetric-tensor identity symbolically, rather than only for a particular stress.

For each straight two-edge face segment, the two collinear half-edge variations cancel the intermediate center displacement exactly. Its endpoints are integer sites. The axis segments also have only integer endpoints. Consequently these first 16 segment rows have zero columns for the half-integer species and all six center types. The symbolic four-column matrix extends by 28 zero columns to the full carrier displacement map. The implementation compares this complete 16-by-32 matrix with the actual geometric `segment_readings(C,-q) @ gauge(-q)`, after division by squared segment lengths. Body-segment coefficients are zero in the coupling; their displacement columns are not silently dropped.

On constant metrics at zero transfer the axis strain is `h_mm` and face strains are `(h_mm+h_nn +/- 2h_mn)/2`. The map then gives

    b(T).epsilon = [sum_m T_mm h_mm+2sum_(m<n)T_mn h_mn]/2.

Finite small-transfer normalization is a diagnostic of the approach to this algebraic value, not an exact identity at nonzero transfer.

The real-action symmetrized bilinear coefficient used numerically is

    b_scalar(k1,k2)
       = [b(S(k1,k2),w)+b(S(-k2,-k1),w)]/segment_length^2.

Both terms obey the same on-shell divergence identity. This proves full-carrier on-shell linear displacement cancellation for this bilinear coupling. Off-shell mutations are measured separately. Complex bilinear exchange retains opposite momenta `q,-q` and transposes; a Hermitian replacement at complex momentum is not made.

## Six exact face-null combinations and a conditional trace cancellation

Each face admits

    N_mn = epsilon_plus+epsilon_minus
             -[(1+w_n)epsilon_axis,m+(1+w_m)epsilon_axis,n]/2.

This is the four-axis-edge plaquette combination, with translation phases explicit. Substitution of the rows above yields zero in every displacement component; the center cancellation extends this to all 32 columns. Each of the six separate null rows is symbolically certified. For constant metrics at zero transfer, the two face strains sum to `h_mm+h_nn`, exactly cancelling the axes. Hence adding these rows preserves the exact Ward identity and does not change the zero-transfer metric coupling. The finite metric-reading measurements at scales .02 and .01 remain separate diagnostics.

The examined family adds each face row with weight `kappa tr S`, comparing `kappa=0` and `kappa=1/24`. On the particular normalized strain pattern with axis value 1, face value 0 and body value -1/2, the axis coupling is `trS/2` and the six null rows contribute `-12 kappa trS`; the latter cancels at `kappa=1/24`. This exact arithmetic is conditional on that pattern. It does not identify every actual finite-momentum partner eigenvector with the pattern or prove uniform decoupling, uniqueness or physical relevance of that mode.

## Finite exchange fits, ranks and derivative-step sensitivity

The supplied Regge matrix is assembled from symmetric area-gradient/deficit-angle derivative products. Derivatives use centered finite differences. At real momentum only, the runner projects onto the Hermitian complement of the actual gauge range, asserts gauge rank 32, reports the carrier gauge residual and checks the reduced inverse residual. Complex on-shell scalar exchange instead uses `Q(q)+lambda G(q)G(-q)^T` and reports both source Ward and solve residuals.

At momentum norms .02 and .01, in axis, tick, generic and body directions, and at derivative steps `1e-6` and `2e-6`, exactly conserved symmetric-source fixtures are fitted to

    q^2 exchange = alpha sum(T1* T2)+beta tr(T1)* tr(T2), T=S/2.

Both complex coefficients, their imaginary parts, fit residuals, source gauge residuals and change between derivative steps are retained. The finite targets are `(-4,4/3)` without the face weight and `(-4,2)` with it. These are numerical comparisons with the indicated tensor structures. They do not turn a finite fit into an analytic leading-symbol or Einstein–Hilbert theorem.

The full generic-direction tensor-fit residual approximately halves in this supplied two-scale comparison; coefficient agreement does not mean that the full matrix lies in the two-invariant span. The corner-source phases and finite lattice tensor structures are retained. The runner requires the original residual bound `0.003` at norm `.01` (and at both norms for the other directions), and requires a residual-halving ratio between `1.8` and `2.2` for the generic direction from `.02` to `.01`, at both weights and both derivative steps. A focused author diagnostic after the failed capture found generic residuals about `0.003295–0.004885` at `.02` and `0.001648–0.002443` at `.01` across the two weights; doubling the derivative step changed these residuals by less than `4e-8`. These numbers diagnose the original coarse-fixture failure and are not a replacement for a fresh primary capture. This is a named finite convergence diagnostic, not a theorem of linear convergence or a uniform error estimate. It does not discard imaginary matrix components. Nongeneric fixtures can reach the derivative/inversion error floor, so no universal monotonic-convergence assertion is supplied. All coefficient, Ward, gauge-rank, inverse and derivative-sensitivity predicates remain in force.

For the two-scale partner diagnostic, the code reports and checks the actual gauge rank, combined metric/gauge rank, gauge/low-cluster spectral gap, low/high cluster gap and singular values of the projected low cluster. The supplied finite diagnostic expects eight low non-gauge modes, and selects a two-dimensional projected subspace only if its numerical rank at the explicitly declared `1e-3` singular threshold is two, the selected singular gap exceeds 20 and the projector/orthogonality residuals pass. The code does not silently equate columns 32:40 with a proved spectral decomposition. If these checks fail, the diagnostic fails rather than asserting a partner interpretation. These are finite tolerance-based ranks, not exact symbolic ranks or a uniform spectral theorem.

Ratios of scalar coupling to that selected subspace and to the metric map are compared at two scales. The original finite inequalities are retained as tests, with their assumptions exposed. Three complex on-shell scalar-pair fixtures compare gauge weights 1 and 10. The Newton search reports its iterations, small-step flag and both shell residuals; residual acceptance is explicit. Small-step termination alone cannot certify the shell. Neither two-scale suppression nor three gauge-weight comparisons proves uniform decoupling or a nonlinear symmetry.

## What is not established

The proved identity is a bilinear free-shell Ward identity. No explicit local scalar field transformation or cancellation of the full action variation is constructed here, so a first-order Noether action-invariance claim is not promoted. Interacting fields, nonlinear gravity, physical partner status, unique face weight, reflection positivity, native interaction supply and physical identification remain open. A different midpoint coupling's finite residuals are not superseded universally by a theorem about this different coupling.

Historical bibliography and novelty assertions are retained in exact recovery as provenance only. No priority claim is inferred from memory. The local algebra above stands on its explicit derivation and does not require an external novelty assertion.

## Reproducibility and source boundary

The primary enforces an aggregate 600-second cap, rejects disabled assertions, prints the actual count of successful predicates and five resolution limits. It combines an exact symbolic certificate with clearly labelled finite numerical diagnostics. No historical cache is consumed as evidence. Its complete literal inputs are pinned by `outputs/d4cone_ward_review_2026_10_18/INPUT_CLOSURE.json`.

All three exact original files, including the complete previous note and numerical cache, are recoverable through `archive/d4cone_ward_review_2026_10_18/MANIFEST.json`. The complete original proof formulas are retained above; broader interpretations have explicit boundaries rather than being silently renamed as exact results.

Current framework context: [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and [kinetic primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md). The earlier Regge note and reviewed D4 source notes are identity-bound lineage/context inputs, not imports of their broader physical interpretations.
