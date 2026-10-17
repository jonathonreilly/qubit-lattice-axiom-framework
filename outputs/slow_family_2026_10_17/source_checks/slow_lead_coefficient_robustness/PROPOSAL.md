# Finite slow receiver: an explicit sufficient coefficient-error interface

Status: root-authored conditional perturbation lemma, requiring a distinct check. This is a finite-time robustness interface for the NEW receiver terms only. It supplies neither a native coefficient generator nor necessary precision, and does not certify perturbations of the calibrated upstream source or emitter. No new physical axioms, numerical experiment or tolerance claim for the whole apparatus is introduced.

## Exact sources and exposure

Read complete slow_lead_resources/PROPOSAL.md, SHA256 84b76d1ec9b1e45811b74ecd2594a0622dfb01ef69d1acadf98931c0ed3f9967, whose paired root check is dd944d8803da24fdfbccfd010e2fd865196aa08ac244605303093a605fef22fe. Read complete uniform composition8cd26edcb7941d8254494480455d17c137652ec779e37e78901de5a04e71ac9e, currently awaiting distinct checking; its formulas below are conditional inputs, not evidence of its acceptance. The fixed published PR9676 note is 2bda0ce48663763bdd3964b2a8bd9c6a160a45a32f7e56e94772cbfa98865d9d. Root integrated that note and authored several ancestors. This proposal is original exposed analysis, not independent verification.

## 1. Allowed finite perturbation and physical premises

Fix M>=1 and retain the same finite head graph, shared internal register, seed, record, all upstream/emitter/gate blocks and literal target phase. Only the following NEW receiver blocks may vary:

- Connector Q(-tau) between gate o and first receiver, tau=sqrt(jg).
- Each of the M-1 internal receiver Q(-g) bonds.
- Each of the M+1 new compensating occupations: at o, first receiver, and subsequent receiver sites.
- The terminal cap g n_last.

Here Q(-a)=a(n_x+n_y-exchange_xy). The operator is PSD for a>=0, vanishes in the head vacuum, and preserves head number. All perturbed coefficients are real and nonnegative. This is an explicit admissible perturbation class; arbitrary added couplings, errors in the shared register, preparation errors, extra heads or changes to measurement are excluded. M=1 has no internal receiver bond and has a first-site occupation plus a distinct cap on the same site. All new terms vanish in the head vacuum, so there is NO new scalar/vacancy offset hidden in this perturbation.

Let connector error be bounded by e_tau, each internal bond error by e_g, each compensating occupation error by e_o, and cap error by e_c, all nonnegative. Errors can have either sign within positivity constraints and vary independently across sites. The calibration relations between these perturbed coefficients need not hold. The one-head sector remains exactly invariant. Passive reference factors are identities.

## 2. Dimension-independent norm bound

On the complete finite one-head Hilbert space, DeltaH is a scalar real symmetric matrix on head positions tensored with the full internal identity. A bond error delta changes two diagonal entries by delta and its two off-diagonal entries by -delta. Its absolute row contribution at either endpoint is at most2|delta|. Each site is incident to at most two internal receiver bonds and at most one connector. Each site carries at most one compensating occupation and at most the one cap. Therefore its absolute row sum is at most

    B=e_o+e_c+4e_g+2e_tau.                         (1)

This safe sum does not assert that all contributions attain their maxima at one site. At M=1, the sharper envelope e_o+e_c+2e_tau suffices. Symmetry makes column sums equal row sums; the Schur bound gives ||DeltaH||<=B on the invariant sector, including all internal states. In particular no factor M appears. A triangle sum over all physical block norms would introduce an unnecessary extensive factor; (1) instead uses the actual one-head row structure. No bound on the unrestricted many-head operator is asserted.

Duhamel between the two finite self-adjoint one-head Hamiltonians now gives, for the SAME seed embedding V,

    ||(exp(-it Htilde_M)-exp(-it H_M))V||
                      <=min{2, |t| B}.           (2)

All coordinates and literal common phases are retained. Unlike a gauge adjustment, this compares the actual unitaries directly. Equation (2) is valid for arbitrary passive references and after any fixed projection by contractivity.

## 3. Composition with an existing finite theorem

Suppose a separately checked nominal theorem supplies ||P1 exp(-it H_M)V-T1(t)||<=epsilon_M on [0,2T], with subnormalized comparator norm r(t) and lower bound r(t)>=R_T>0 on [T,2T]. Its exact mathematical/physical premises remain needed. Then the perturbed device has branch error at most

    epsilon_pert=epsilon_M+min{2,2TB}             (3)

on [0,2T]. If epsilon_pert<R_T, a SINGLE selected read in [T,2T] obeys

    probability(record1)>=(R_T-epsilon_pert)^2,
    normalized successful-vector error<=2epsilon_pert/R_T.

The successful subnormalized CP-map diamond error is <=2epsilon_pert. The normalized conditional operation is nonlinear and is not assigned that diamond bound. The complete vector bound following just from the branch estimate is min{2,sqrt(2(1-R_T+epsilon_pert))}. If a nominal complete finite-state bound is independently available, (2) can instead be added directly to that bound.

An extra amplitude budget e_impl>0 is ensured by B<=e_impl/(2T). For example, at the fixed published horizon T=10^15, an allocated e_impl=10^-4 is ensured by B<=5*10^-20. This is arithmetic for a conservative SUFFICIENT envelope, not a measured engineering tolerance or a lower bound on necessary accuracy. Errors with structure or smaller spectral effect can behave much better than the worst-case operator estimate. No arbitrary-precision native supplier is established.

## 4. Correlated diagonal-preserving variant

If the realized occupations are deliberately chosen using the realized adjacent connector/bond weights so that every receiver diagonal and gate-o diagonal stays EXACTLY2j, and the last cap is chosen for the same exact compression diagonal, DeltaH has only off-diagonal changes. This is a different, stronger supplied-correlation premise. The maximum off-diagonal row sum is bounded by

    B_corr=2e_g+e_tau.                            (4)

This bound still allows inhomogeneous internal hopping. Positivity of every compensation must separately be verified for the realized weights; exact diagonals alone do not imply it. The scalar and upstream terms remain unchanged. Equations (2)-(3) hold with B_corr. This variant explains what diagonal correlation buys without claiming it can be prepared autonomously or tolerantly.

## 5. Scaling and limits

If a nominal family has kappa=a*kappa0, g=a^2*g0, tau=a*tau0, T=T0/a^2 for 0<a<=1, then an implementation-error envelope B(a)<=a^2 B0 gives the SAME sufficient dynamical budget2T0 B0. This is an elementary consequence of (2), conditional on the nominal family theorem. It is not a statement that fixed relative errors in all blocks meet that envelope: fixed relative connector error scales as a, and compensation occupations approach2j rather than zero. The stronger exact-diagonal variant still needs its off-diagonal budget to scale as a^2 for this Duhamel certificate. This does not prove those scalings necessary; it exposes a limitation of this particular certificate.

The lemma is specific to receiver coefficient errors respecting head-number conservation and fixed graph/internal identity. Full native robustness requires source/emitter errors, seed errors, physical Record/readout identification, unwanted couplings and parameter supply to be handled separately. It makes the exact-supply premise quantitatively reviewable for a bounded class, without removing it. Permanent storage, repeated monitoring, capture and reset/reuse are unchanged open obligations.
