# Independent derivation: what a finite weighted pair sample estimates

This is a supplier derivation, not the author's scalar-field theorem. It was written before exposure to any new parent `unequal_window` equations or implementation. All expectations, sampling distributions, responses and tolerances below are hypotheses to justify for an actual catalogue.

## 1. Specify the target and its measure

Let `x=(chi,n)` denote a true light-cone position under a supplied distance/clock map, and let `f_a(x)` be a chosen physical signal component, for example a shear component in a specified transported basis or a radial peculiar velocity after reference-frame correction. Define a second moment

    C_ab(x1,x2) = E[f_a(x1) f_b(x2)]
    L_K(C) = integral K_ab(x1,x2) C_ab(x1,x2) dmu(x1) dmu(x2).

The same statement applies to a connected covariance if ensemble means are known and subtracted. Estimating those means from the same survey adds a window-dependent projection and must be included. Summation over channels may be absorbed into K. K may have either sign; fix it independently of the measured signal, or supply the additional conditioning needed for data-adaptive choices. Assume integrability so that sums, expectations and integrals can be interchanged.

The measure is part of the definition. For example `dmu=dchi dOmega` differs from a volume measure with a factor chi squared. On a full isotropic sky, orientation integration yields `8 pi^2 dchi1 dchi2 dcos(theta)` for scalar correlations. At fixed chi1,chi2, converting to separation r gives `abs(dcos(theta))=r dr/(chi1 chi2)` on `|chi1-chi2|<r<chi1+chi2`. These Jacobians belong in K or the reference measure, not silently in both. Spin-component rotations and radial sightline factors must also be accounted for. A mask prevents replacing the angular integral by its full-sky factor without another premise.

A target `C(chi1,chi2,cos(theta))` retains unequal emission times. It needs neither time-translation invariance nor a common deterministic transfer. It is different from evaluating a same-time covariance at a changing separation. The previously derived fixed-separation correction remains necessary if an equal-time derivative is subsequently requested.

## 2. The exact catalogue expectation

For distinct ordered catalogue pairs define the random counting measure

    M_ab(dx1 dx2) = sum_(i in a, j in b, i != j) delta_(Xi,Xj)(dx1 dx2).

For different populations the condition `i != j` means excluding a shared physical object if a self-pair term is not wanted. Let its second factorial moment density relative to the chosen measure be `lambda_ab^(2)(x1,x2)`. Thus `E M_ab = lambda_ab^(2) dmu1 dmu2`. This is a joint pair intensity, not automatically a product of one-object densities. Cross-catalogue overlap, joint targeting, clustering and exclusion can affect it.

Let `Y_ij` be the response-corrected measured mark product, with any justified nuisance subtraction already included. Define

    C_ab^pair(x1,x2) = E[Y_ij | an observed ordered pair at x1,x2].

This is the marked, pair-conditioned expectation (often called a Palm expectation). Partitioning the domain into small cells, taking the expectation of each marked pair count and then the integrable limit gives

    E[sum_ij h(Xi,Xj) Y_ij]
      = integral h(x1,x2) lambda_ab^(2)(x1,x2)
                 C_ab^pair(x1,x2) dmu1 dmu2.                 (A)

For n independent positions drawn from density p, independent of the field, the ordered-pair intensity is `n(n-1) p(x1) p(x2)`. Independent disjoint catalogues of fixed sizes n_a,n_b give `n_a n_b p_a p_b`. These examples do not describe a clustered catalogue without further hypotheses. An unordered-pair sum requires the corresponding factor-of-two convention.

No independence of different pairs is needed for (A). If the *known* pair intensity is positive wherever K is nonzero, the unnormalized estimator

    Lhat_K = sum_ij K(Xi,Xj) Y_ij / lambda_ab^(2)(Xi,Xj)      (B)

has mean `integral K C_ab^pair`. It estimates `L_K(C)` only if `C_ab^pair=C_ab`, or a justified correction converts the pair-conditioned moment to C. Correct reference-measure normalization is understood; the intensity already includes expected pair count. Do not divide again by the observed number of pairs. Positivity alone does not ensure a useful variance; inverse weights may diverge near poorly sampled regions.

One sufficient stronger design is sampling that, conditional on the latent field, has a known positive intensity `lambda_ab^(2)(x1,x2 | f)` and calibrated noise with the desired conditional mark product. Weighting by that *conditional* intensity first cancels sampling conditional on f; averaging over f then gives L. This is an existence statement. An unobserved field-dependent intensity is not an operationally available correction merely because it appears in a formula.

The distinction can be checked in a one-pair exact example. A latent state is equally likely to have product c=1 or c=3. Its pair-inclusion probabilities are respectively 1/4 and 3/4, so the unconditional inclusion probability is 1/2. The desired mean is 2, but

    E[I c /(1/2)] = (1/2)(1/4)(1)/(1/2)
                   +(1/2)(3/4)(3)/(1/2) = 5/2.

Weighting by the true conditional probability gives `E[I c/pi(c)]=2`. This demonstrates why a correct *marginal* pair density can still leave mark-selection bias. It is not a theorem that all surveys have this bias or cannot correct it.

For a density-sampled tracer, a schematic pair product contains

    E[(1+delta_a(x1))(1+delta_b(x2)) f_a(x1) f_b(x2)].

Removing a smooth mean radial/angular selection function does not generally remove the mixed density-field moments. Even dividing by `1+xi_ab` yields a pair-conditioned mark correlation unless further factorization or a calibrated correction holds. Schmidt et al.'s concrete magnification/source-clustering calculation supports this distinction; their cosmological correction values are not imported.

## 3. Fixed populations, normalized ratios and fixed grids

For a genuinely fixed finite population with fixed pair contributions `t_ij` and sample indicators, let `pi_ij=E[I_i I_j] > 0` be the actual joint inclusion probability. Then linearity gives

    E_design[sum_(i != j) I_i I_j t_ij/pi_ij]
      = sum_(i != j) t_ij.                                  (C)

This holds even if inclusions are dependent; replacing pi_ij by pi_i pi_j needs another assumption. It proves an unbiased finite-population total, not that the population occupies an unbiased continuum grid. Unknown population membership or inclusion laws remain supplier inputs.

A catalogue-normalized ratio `sum w_ij Y_ij / sum w_ij` needs its own expectation calculation. In general `E[A/B]` is not `E[A]/E[B]`: equiprobable `(A,B)=(1,1),(0,2)` give 1/2 versus 1/3. This does not make all normalized correlation estimators biased. Conditional on fixed positions/weights, B is fixed; for an exact constant pair moment C in a bin, `E[A | positions]=C B` gives an unbiased ratio. For varying C, the exact target is the actual weighted-bin functional. The point-bin value or an independently specified continuum weight requires a finite-window approximation/error assessment. Data-dependent weights and normalization require retaining their correlations with the marks. Schneider's estimator and Schmidt's explicit random denominator illustrate the two different levels of conditioning.

For nonrandom fixed positions `x_i`, an unbiased mark measurement yields only

    E_marks[sum w_ij Y_ij | grid] = sum w_ij C(x_i,x_j)

under the required conditional mark premise. This is a discrete linear functional. Equality to a prescribed continuum `L_K` for arbitrary smooth C does not follow from smoothness. For finitely many sampled pairs in an open domain, choose a smooth bump in an unsampled region where K has fixed nonzero sign; its point samples vanish while its weighted integral does not. This local witness concerns an unrestricted smooth function class, not every physically constrained covariance family. A physical covariance restriction can itself supply extra information and must be stated.

Legitimate routes include a finite admitted signal basis with exact quadrature, cell-average measurements with represented weights, an error bound from stated derivative/modulus bounds and grid fill distance, or the random-design expectation (A). A fixed grid does not become a random sample because a synthetic code enumerates it.

## 4. Noise, response and distance errors

If calibrated marks have form `f_a+e_a`, their product contains signal-noise cross terms and `E[e_a e_b]`. Zero individual noise means alone do not make these terms vanish. Distinct-object, conditionally independent shape/velocity measurement errors can remove the cross-noise expectation; intrinsic alignments, common calibration, shared objects and signal-dependent selection generally require additional terms. A general subtraction must match the conditional pair moment, not just an unconditional one-object noise variance. Excluding self-pairs only removes the corresponding diagonal contraction when the noise assumptions hold.

Shear ellipticity is a response-calibrated, spin-2 observable; the weak approximation, additive/multiplicative response and intrinsic alignment treatment must match the target. Velocities require a specified radial/observer convention, distance indicator and cosmological distance map. In the nonrelativistic Doppler scope discussed by Davis and Scrimgeour,

    (1+z_obs)=(1+z_cos)(1+z_pec),
    v_rad approximately c (z_obs-z_cos)/(1+z_cos).

These expressions do not identify z_cos from redshift alone or include every relativistic projection correction. Their use needs the distance/background and reference-frame assumptions. The same noisy distance or redshift often enters both the velocity mark and the pair position/weight, so a zero-mean mark-noise model at exact positions may be insufficient. This is an errors-in-variables problem, with selection acting on the noisy quantities as well.

Only after selection and higher-moment terms are controlled so that a linear two-point response is justified, write it schematically as `C_obs = A C + B`. A contains the admitted two-leg source-distance kernels, angular/velocity geometry and mark response; B denotes specified additive contributions. Field-dependent density selection cannot in general be compressed into a known linear A acting on C alone. A measured weighted statistic `g^T C_obs` tests the desired `K^T C` without reconstructing C when `A^* g=K` on the admitted signal space and B is handled. Approximate equality contributes the residual functional `(A^*g-K)^T C`, which needs a justified bound. Finite redshift bins or a photo-z kernel may support useful smooth K, but do not automatically span an arbitrary prescribed K. A data-selected K requires a matching inferential treatment.

## 5. Uncertainty and the permissible conclusion

The variance of a pair sum includes terms for the same pair, overlapping pairs and disjoint but cosmically correlated pairs. It depends on the relevant joint sampling laws and signal/noise higher moments, up to four-point objects for a quadratic statistic. A Gaussian closure can simplify them but is a new statistical assumption. A large number of catalogue pairs is not the number of independent experiments. Unbiasedness in an ensemble does not make the one observed realization equal its mean.

If a concrete finite estimator is shown to have the required mean and a valid variance bound V, elementary inequalities can give conditional statistical bounds (for example `Pr(|Lhat-L|>=t)<=V/t^2`). No V, observational precision or confidence threshold is supplied here. Correlation-error envelopes at fixed weights also omit errors in weights, geometry and selection; those require kernel/intensity-error and cross terms.

A weighted unequal-time target is therefore a constructive possibility with explicit admission conditions. It can avoid selecting a common growth function or pointwise time derivative. The unobserved selection law, calibration, window response and uncertainty model remain physical inputs until actually established. The inspected historical papers do not rule out a future calibrated supplier; they also do not furnish it for this new theory by citation alone.
