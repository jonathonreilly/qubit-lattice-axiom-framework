# Selective check: three-site outgoing coefficient

Disposition: supported as a conditional complete-input **outgoing spectral-component** comparison, equations (1)–(17), on the stated domain with Theta<1. No mathematical correction requested. This does not establish complete actual-state accuracy, useful-time halfline normalization, runtime, success, or a finite-device theorem.

## Source and exposure

Checked source: `three_site_outgoing/PROPOSAL.md`, SHA256 `af580b44fc2ebfc35eb014ffc63b8bae17464150677ede4a8b8315886f6f36ac`. I read its complete changed argument. I did not author this outgoing proposal. I authored the scalar three-site source used here, previously checked related background/attachment interfaces, and participated in this research ancestry. This is a distinct synthesis check with that shared exposure, not independent reconstruction of the entire calibration or self-certification of my scalar source. Its separate scalar check is retained below.

I reused the previously fully read scalar, inverse and attachment arguments/checks at their unchanged identities, refreshed the necessary emitter-free row and flux argument, and verified the pins. The source header's attachment-check-pending statement records drafting-time status: the attachment now has the distinct check below. No source change is needed to preserve that history.

| Argument/check | SHA256 |
|---|---|
| three_site_product_source/PROPOSAL.md | a89025dafcb588459e88c14fa802e9e9ce2e5184aa42d9d22f6521a1dadb4823 |
| three_site_product_source_check/REVIEW.md | c161daea2f3a126ad84baaa63d975b5d80fd3243f11ca3b1075673f62530245b |
| three_site_loaded_inverse/PROPOSAL.md | 7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672 |
| three_site_loaded_inverse_check/REVIEW.md | 8ddded69f6c5758650c166c8adbc3c05346478e81d4636b8bc5e226f365c9ca2 |
| three_site_actual_attachment/PROPOSAL.md | 4278633f3436008a770088331a2424d3f42dda06d08853dfe18d9b8a6554f006 |
| three_site_actual_attachment_check/REVIEW.md | ede902f9c1bebc768147e459894f98610689f33655f87d01d91d07531cbd157d |
| slow_lead_wide_outgoing/PROPOSAL.md | 593ed5c43008a40101cfc5a9c8243d7190ea7a3f822becbd9644f30b5f74d606 |
| slow_lead_wide_outgoing_check/REVIEW.md | 55de89b5d0536b0ce8028e4a346feb29bcf073f6012dd9cb9e6c01a5d76ead77 |

## Ordered recovery and unchanged background

Eliminating the first two source equations gives the checked last-source column a1*a2*Q^-1. The physical source-background hopping is negative, so the background forcing is -kappa times that column and the row is exactly -kappa*a1*a2*L_tilde*Q^-1. The comparison sign in (5) follows from L_tilde approximately -(x*omega*rho_att*w^21/j)P. No extra two-head propagation phase should be appended to the complex rational source response.

The noncommuting order matters: Q=Q0(I-K_E), hence Q^-1=(I-K_E)^-1 Q0^-1. On P, Q0^-1 is 1/q3; applying the Neumann remainder to this selected forcing gives theta/(1-Theta), before applying the full row norm. The resulting coefficient j*461 is less than 1.383, so 1.384 is a valid allowance. Equation (6) controls all generated internal components rather than projecting away leakage.

The actual attachment leaves the emitter-free background compression, original port, loads, and outgoing reference planes unchanged. Therefore section 1 of the wider outgoing argument applies without its subsequent one-site emitter hypotheses. In particular the old kappa<=1e-8 restriction cannot be used for the new emitter, but is not needed for this row. The new Q conditioning supplies that missing source argument. Closed-channel bounds and the two feedback margins are inherited as actual background estimates, not recomputed from a selected endpoint inverse.

The complementary column in (15) is also ordered correctly: Q0^-1 C stays in C, so its direct row uses 2e-23, while its Neumann correction must use 461 and Theta/(1-Theta). The bound 170 is applied before the correction. This retains the otherwise dangerous resonantly mixed wrong-window contribution. Lower-lip bounds are reused separately from the checked physical-root inverse interface; no entrywise imaginary-part replacement or unproved adjoint identity for Q is used.

## Scalar measure, flux and error integration

The exact isolated scalar measure is the finite-band measure, not the Markov cubic. Its normalized total mass and second moment lambda^2/3 are valid on this domain (lambda/j is far below the scalar lemma's 1/16 ceiling). The sixth moment used optionally in (12) is likewise the exact scalar moment. Substitution E'_q=2j sin(q) verifies |F3|^2 dq=rho3 ddelta, including the factor 2 and pi. The cancellation of i against rho_att=-i*w^40*rho_n gives the stated phase 61q+172*k_old before the connector.

The physical amplitude multiplier is t_L. Changing from q to k multiplies the Stone coefficient by J, so t_L J=t_f sqrt(J) is essential. Equations (9) use this identity correctly. The final half-integer connector phase is retained. There is no missing sqrt(j/g), and the flux factor has modulus at most one.

For d/g<=1/2, both central angle deviations are at most asin(1/4), giving the denominator lower bound in (11). With g/j<1e-6/.0027, its last, deliberately loose bound |r_L|<=|delta|/g follows. Reference mass loss is the sum of the outside-band scalar tail and the transmitted-window reflection loss. Markov's inequalities with the exact second/sixth moments and the full second moment for reflection give (12); this is an upper bound, not an equality or an installed-seed mass certificate. The exact p is strictly positive even if the displayed Xi exceeds one. The normalization-cost formula is used only with Xi<1, otherwise exact p must be retained.

Minkowski and the full second moment justify (14). The theta-weighted integral is finite and its coarse ceiling Theta^2 p is valid. For wrong windows, E'_q/sqrt(2pi)<.003, each interval has length 2h, and exact flux/Jacobian conversion is contractive in L2. Two-window triangle aggregation therefore gives .006*Bwrong*sqrt(2h), with the actual window energy retained.

## Complete input and limits

The sqrt(2) selected-column allowance is a safe Cauchy–Schwarz bound. The wrong-window term is separately paid on the full complementary domain before prepared-input restriction. Orthogonal parity sectors take the maximum; orthogonal record-X sectors with initial amplitudes 1/sqrt(2) add no extra factor. Extracting x in the ideal sector map recombines record0 into record1. Only after the wrong-window error is paid is it legitimate to factor the ideal old aging exp(-itK) and literal W. The common apparatus phase, including c_att and the carrier 2j, is preserved. Tensoring passive references does not change these operator norms.

The reference normalization cost is paid once: on the full Fourier space the ideal subnormalized map has norm sqrt(p) times an isometry. Thus its distance from the normalized common-packet map is 1-sqrt(p), without an additional sqrt(2). This normalizes the comparator only; it does not renormalize actual output or a postselected branch.

Fourier isometry and halfline restriction do carry the bound to the represented outgoing component at every real time. Unit full-line Fourier norm does **not** imply unit norm on m>=0 at finite time. Source/local/core amplitudes, incoming contributions, closed tails, the global actual omitted state, concentration/onset and finite-cut transfer all remain separate obligations. In particular neither the scalar reference's total mass nor (17) supplies a complete actual-state theorem. The draft correctly states these limits.

This is an analytical source/synthesis check. No scientific execution, numerical sweep, new calibration, original-source recertification, Git/canonical/publication/checkpoint/prompt/model change, or delegation was performed. Exact correlated coefficients, shared B with its vacuum restriction K, prepared seed and the physical Hamiltonian/output identification remain supplied premises. Hash verification establishes identity, not proof.
