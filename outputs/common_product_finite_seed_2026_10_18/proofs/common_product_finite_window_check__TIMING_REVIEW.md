# Classical timing mixture: distinct corollary check

No required mathematical correction was found. For any fixed Borel timing probability measure independent of the entire logical input and passive reference, the proposed full-output channel has the stated diamond-distance bound to the controlled logical operation tensored with a common radial mixed state through the fixed output isometry. The result does not imply a distribution-independent radial target, coherent-time control, or a stopping/storage mechanism.

## Exact pins and exposure

Paths are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/`.

* New source, fully read and SHA-256 verified: `common_product_finite_window/TIMING_MIXTURE.md`, `c2713ddb892b5c1f509ab66a796a6aa17711552496044e558805984db58eef73`.
* Previously fully read window source, hash refreshed: `common_product_finite_window/PROPOSAL.md`, `1ea1943e162c1ab7f0da057a1343b95b859e394c25420d5577830a838d116b1b`.
* My completed window report, hash refreshed: `common_product_finite_window_check/REVIEW.md`, `1337df4d94e3d6b555a88167945e5e8490e9df978b1fbc3e140db17622e36cbb`.
* Previously fully read composition source, hash refreshed: `common_product_finite_seed_router/PROPOSAL.md`, `3a195efcf8d5196ed54a74228033d0888e7f18c864e481ce61b2efea6c67992b`.
* My completed composition report, hash refreshed: `common_product_finite_seed_router_check/REVIEW.md`, `5f5b1727a31df17facb9232e902c1d6985cd175058d66e54862ae614fef148a9`.

These component reads and checks are reused at their exact scopes. They are not a prior check of this channel corollary. ROOT proposed the convex-mixture route; I read the candidate derivation before reconstructing it. This is source-exposed same-model checking, not blind or model-diverse replication. The source's statements about a pending window check reflect authoring chronology; the completed pinned window report is available now, without retroactively making the author derivation independent. No retained or audit status is conferred.

## Fixed output encoding and target factorization

For n=0,...,ell and each legal program/path label (p,r), the claimed J_out basis image is a distinct occupation-basis state: the head is at (r,n), the program occupies |ppp>, and both emitters, mediator and every other head are vacant. Distinct triples are orthogonal and each image has norm one. Linear extension therefore defines one fixed isometry from radial space tensor logical space into the full physical output space. This construction does not require radial and path coordinates to be distinct physical qubit factors.

The window theorem supplies unit beta_F(t), with a positive normalization denominator bounded away from zero and continuity in t. Thus W_t is an isometry for every t and uses the same J_out and same C. The phase exp(-i2bt) is retained in the vector statement. The finite physical generator makes V_t continuous as well.

For any logical operator rho, direct multiplication gives

    W_t rho W_t* = J_out[|beta_F(t)><beta_F(t)| tensor C rho C*]J_out*.

The scalar exp(-i2bt) cancels against its conjugate at this step. This cancellation uses the equal-time density matrix and would not generally hold between amplitudes at different times. Pulling the fixed C, rho and J_out through the integral gives (4) exactly. The radial integral is positive and has trace one because its integrand is a continuous family of rank-one density matrices. It can be mixed; replacing it by a fixed pure packet is not justified or claimed.

The same calculation on rho_LR, with identity on the reference, yields (5) after a fixed tensor-order permutation. Independence of the measure from the entire joint input is what lets the identical radial density factor be pulled out. Consequently the ideal radial factor has no correlation with logical/reference input in this encoded decomposition. No assertion of physical site-group tensor independence follows, and the source explicitly avoids it.

## Arbitrary Borel measures and the diamond estimate

On the compact interval the matrix entries of V_t and W_t are continuous and bounded. Their integrals exist against any Borel probability measure, including atomic or singular measures. Integrating isometric conjugation maps preserves complete positivity and trace preservation. No probability density, quadrature, or timing moment is required. For ancillary references the trace-class integral is likewise well defined; finite input dimension also suffices for the usual finite-ancilla characterization of diamond norm.

For a general trace-class X on input plus reference, add and subtract W_t X V_t*. This yields the source identity

    (V_t-W_t)X V_t* + W_t X(V_t*-W_t*).

The Schatten ideal inequality bounds its trace norm by `2||V_t-W_t|| ||X||_1`, since both isometries have operator norm one. This proof covers nonpositive X as required for the induced diamond norm, rather than only density matrices. Tensoring an identity preserves the isometry-difference operator norm. Integrating with the same input-independent probability measure and applying the norm triangle inequality gives the bound 2E_window for every ancillary input X. Taking the diamond supremum and applying the universal channel-distance ceiling gives exactly min{2,2E_window}. The optional average-of-pointwise-bounds refinement follows from the same inequality when the chosen bound is measurable and integrable; a capped bound can always be used.

Every physical output coordinate remains in these maps. In particular population and coherences outside range(J_out), including nonvacant emitter or mediator states, enter the trace norm and are not projected away. The omitted timing label is an external classical ensemble label in the definition of Phi_mu, not an erased physical time register. The mathematical ideal output may subsequently be decoded or reduced by a specified channel with contractive error, but this corollary supplies no physical decoder.

## Scope checks

The fixed distribution assumption is necessary for the stated product target. For example, if two logical labels select different times whose radial density matrices differ, the resulting ideal output can be classically correlated between radial and logical labels. A timing variable already correlated with the reference similarly defeats the universal radial tensor factor. Measuring a coherent logical input to choose time also changes the process. Such cases are not covered by the one fixed mu channel here; the source excludes them correctly.

Coherent control of time would involve cross-time terms W_t rho W_s* and the phase exp[-i2b(t-s)], as well as a specified time-control system. Convex integration of equal-time channels does not establish that model. This is a scope exclusion, not an impossibility claim about coherent controllers.

The diamond ceiling is uniform over allowed mu, but sigma_mu generally varies with mu. Thus there is no single full-output radial target certified for all unknown distributions. The logical operation remains C in each ideal encoded target. Finally, selecting an observation time in an ensemble is not the same as freezing the physical output or evolving all runs to a later common time. The fixed Hamiltonian continues to act, and the finite-device recurrence limits remain unchanged.

Only this report was written. No source edit, scientific executable, numerical integration, symbolic solver, sweep, W/Git/PR/canonical/checkpoint/editable-prompt change, model override or delegation occurred. Hashing was identity bookkeeping. This supports the bounded classical timing-mixture corollary at its pinned revision without assigning retained or formal audit status.
