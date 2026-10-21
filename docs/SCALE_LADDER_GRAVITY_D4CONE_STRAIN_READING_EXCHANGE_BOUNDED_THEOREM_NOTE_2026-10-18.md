---
claim_id: scale_ladder_gravity_d4cone_strain_reading_exchange_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "Finite supplied-model numerical fixtures and explicitly stated constructive identities only; all universal, asymptotic, physical and unexecuted census claims are deferred."
runner: scripts/scale_ladder_gravity_d4cone_strain_reading_exchange_2026_10_18.py
---

# Finite strain-reading exchange and an exact fourth-moment identity

Claim type: bounded_theorem.

Primary runner: `scripts/scale_ladder_gravity_d4cone_strain_reading_exchange_2026_10_18.py`.

These are supplied-model calculations under review, not adopted physical claims. The bounded claim is exactly the constructive algebra and finite fixture inventory below. Historical stronger statements are excluded from the live claim and preserved with exact original bytes in `archive/gravity_review_2026_10_18/MANIFEST.json`.

## Reading and finite exchange

The 24 site-to-site segments comprise four axes, twelve signed face diagonals and eight body diagonals. If R maps edge variations to squared-length variations, D maps ten metric components to those variations, and W_ii=sqrt(w_class)/length_i^2, the reading is L=(WD)^+ WR. At zero momentum it reproduces constant metrics; the source tests the specified non-site displacement blindness.

H1 evaluates three static momenta and compares null-fluid/static-dust test amplitudes near ratio two. H2 fits alpha T1*.T2 + beta tr(T1)*tr(T2) on the lattice-conserved source basis in six directions at .02/.01; alpha near -4 and beta near 2 are finite observations. Its partner-share ratios do not prove a universal decoupling order. H3 scans and refines shell minima at .08/.04 on three directions and reports the reading of detected nullspaces.

H4 uses seed 7 scalar pairs at .1,.05,.025 and compares corner/cell-averaged gradient Ward residuals. H5 measures the row-dependent registration phase and off-support remainder at the stated finite differences. H6 uses seed 11, two scales and gauge parameters 1 and 10. Its unconserved-source exchange depends on gauge fixing and is a diagnostic of the supplied coupling, not a gauge-invariant observable. H7 tests eight class weights and two directions against alpha=-4, beta=2-(2/3)rho^2, rho=4(w_a-w_b)/(4w_a+12w_f+8w_b). This finite agreement does not prove an exchange theorem for all weights or momenta.

## Exact constructive identity

For the normalized 24 directions n and class weights, F_abcd=sum w n_a n_b n_c n_d. Signed permutations force every odd-index component to vanish. Counting directions gives F_iiii=w_a+(3/2)w_f+(1/2)w_b and F_iijj=(1/2)w_f+(1/2)w_b for i!=j. Thus F is proportional to delta_ab delta_cd+delta_ac delta_bd+delta_ad delta_bc exactly when w_a=w_b (with the zero tensor included as isotropic). This algebra is independent of the numerical exchange fit. H9 verifies all three class-weight coefficients and all 256 tensor components using exact rational arithmetic. H8 checks representative weights and compares the strain reading with two Euclidean pseudoinverse choices. The finite exchange's proposed iff condition is deferred; the fourth-moment identity itself is live.

## Local midpoint placement and finite comparison

The refreshed construction assigns each segment its share of the cell-averaged stress at its midpoint. With segment midpoint m and J the coordinates where m is integral, the finite local average has the exact Fourier factor

`place(q,m) = exp(i q.(m-1/2)) product_{j in J} cos(q_j/2)`.

This follows by independently summing the two offsets plus/minus 1/2 in each coordinate in J. The constant-metric reading is unchanged: at q=0 all factors are one and Lt R(0)=L(0). The phase cancels the segment registration phase in the endpoint strain; the remaining cosine factors have no linear Taylor term. This identifies the local placement mechanism, without establishing a uniform propagator or exchange estimate.

H10 compares the cell-centred and midpoint Ward residuals at s=.1,.05,.025 for the specified seeded scalar pair. The midpoint residuals are approximately 1.04094e-4, 2.59104e-5 and 6.46736e-6; the consecutive ratios are required to lie in (3.8,4.3), while the cell-centred ratios lie in (1.9,2.1). H11 uses the second specified seeded pair and gauge parameters 1 and 10. Relative distances from the displayed EH-form comparison are approximately .00235540, .000696756 and .000178358; relative gauge changes are 1.07183e-6, 5.25584e-8 and 3.14228e-9. Its finite predicates require successive distance ratios in (3,4.5) and gauge-change ratios above 12.

These are three-scale observations on the supplied carrier and matter coupling. They do not prove general O(k^2) exchange error or O(k^4) gauge dependence. Such promotions require control of the inverse and spectrum along the proposed limiting family. The exact fourth-moment identity and all prior finite controls remain part of this note.

## Mathematical construction and scope

The Euclidean lengths, finite simplicial carrier, action orientation, tick coordinate (index 3), matter discretization and metric reading are supplied choices. No primitive selects them. For each triangle t the code constructs area and deficit derivatives a_t(k), d_t(k). The analytic Hessian is the symmetrized sum of a_t(-k)^T d_t(k); at real k this is Hermitian. Vertex displacements give the edge map G(k), while M(k) is the line-integrated metric-to-edge map. Nullities use the stated numerical thresholds, not exact rank certificates. Complex momenta use analytic transpose pairings, not Hermitian continuation.

The generic carriers use finite differences of simplex geometry with step 1e-6. Small eigenvalues, shell searches and fitted coefficients therefore carry conditioning and finite-difference error. A low singular value at a sampled point is not a certified zero, and a two-scale ratio is not a uniform asymptotic estimate. Every predicate below is limited to its literal finite fixtures in the primary source. The source prints measured values on both success and failure.

The original Regge parent is used only for its explicitly invoked area/dihedral/classification helper code where imported. Its historical physical-graviton, complete-classification and OS wording is not a premise here. The present calculations do not establish a positive physical Hilbert space, a real-time Hamiltonian, absence of additional roots, general universality, nonlinear consistency, or a microscopic selection mechanism.

## Reproduction and failure meaning

The primary declares a 300-second cap and literal input paths. It reports each finite predicate and its measured diagnostic, then `TOTAL: PASS=... FAIL=...`; nonzero failures return exit code one. A failure means the stated finite numerical predicate was not reproduced, including possible conditioning/tolerance failure. It does not establish a universal countertheorem. Source identity, a fresh runtime capture and the combined mechanical gate are separate obligations. The historical caches are recovery artifacts, not evidence for this corrected source.

The deferred register is `docs/work_history/repo/review_feedback/GRAVITY_REVIEW_SCOPE_AND_RECOVERY_2026-10-18.md`. Original PR 9774 remains a recovery branch until its deferred content has an explicit later disposition. No audit verdict or retained status is asserted here.
